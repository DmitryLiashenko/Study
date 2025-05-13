import os
import gspread

from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

load_dotenv()  # Загружает переменные из .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
ALLOWED_USERNAMES = ["Pir_1202", "DmitryLiashenko"]


# Авторизация
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('bot_debts/credentials.json', scope)
client = gspread.authorize(creds)

# Открытие таблицы
SPREADSHEET_ID = SPREADSHEET_ID
sheet = client.open_by_key(SPREADSHEET_ID).sheet1


async def get_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = sheet.get_all_values()

        # Получаем нужный диапазон строк (со 2-й по 15-ю)
        rows = data[1:15]

        # Формируем три отдельных блока
        dolgimy = ["*ДОЛГИ МЫ*"]
        dolginam = ["*ДОЛГИ НАМ*"]
        kassa = ["*КАССА*"]
        balans = ["*БАЛАНС*"]

        for row in rows:
            # Долги МЫ: A и C (индексы 0 и 2)
            if len(row) > 2 and (row[0] or row[2]):
                dolgimy.append(f"{row[0]} — {row[2]}")

            # Долги НАМ: E и F (индексы 4 и 5)
            if len(row) > 5 and (row[4] or row[5]):
                dolginam.append(f"{row[4]} — {row[5]}")

            # Касса: H и I (индексы 7 и 8)
            if len(row) > 8 and (row[7] or row[8]):
                kassa.append(f"{row[7]} — {row[8]}")

            # Получаем ячейку A20
        balance_value = sheet.acell('A20').value
        if balance_value:
            balans.append(balance_value)

        # Отправка сообщений
        await update.callback_query.message.reply_text("\n".join(dolgimy), parse_mode='Markdown')
        await update.callback_query.message.reply_text("\n".join(dolginam), parse_mode='Markdown')
        await update.callback_query.message.reply_text("\n".join(kassa), parse_mode='Markdown')
        await update.callback_query.message.reply_text("\n".join(balans), parse_mode='Markdown')

    except Exception as e:
        await update.callback_query.message.reply_text(f"Ошибка: {e}")

# Функция для отправки кнопки "Долги" при запуске бота
async def send_debt_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Долги", callback_data='data')]  # Создаем кнопку "Долги"
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажмите на кнопку, чтобы получить данные о долгах", reply_markup=reply_markup)

# Обработка нажатия кнопки
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'data':
        # Когда кнопка нажата, отправляем команду /data
        await get_data(update, context)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    if user.username in ALLOWED_USERNAMES:
        await update.message.reply_text(f"Привет, {user.username}! Ты авторизован.")
    else:
        await update.message.reply_text("Извините, у вас нет доступа к этому боту.")


def main():
    TELEGRAM_TOKEN = BOT_TOKEN

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Заменяем команду /start на send_debt_button, чтобы кнопка отображалась сразу при входе
    app.add_handler(CommandHandler("start", send_debt_button))  # Добавляем команду /start для отправки кнопки
   # app.add_handler(CommandHandler("start", start))  # Функция start с проверкой ALLOWED_USERNAMES
    app.add_handler(CallbackQueryHandler(button))  # Обрабатываем нажатие кнопки
    app.add_handler(CommandHandler("data", get_data))  # Добавляем команду /data для вызова функции get_data

    app.run_polling()

if __name__ == "__main__":
    main()
