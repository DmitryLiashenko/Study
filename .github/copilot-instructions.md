# Copilot instructions for this repository

Краткое назначение

- Репозиторий содержит набор упражнений и мини‑проектов на Python (учебные задания GoIT и self-study). Основные рабочие компоненты: простые Flask-приложения и парсер/скрепер в `self_study/companies_general_data_collection_full`.

Big picture (архитектура)

- `Modul_1(python_core)` — коллекция домашних заданий и примеров. Внутри есть несколько отдельных приложений (каждое — небольшой самостоятельный проект).
- `self_study/companies_general_data_collection_full` — самостоятельный пайплайн для сбора данных: код в `src/` + `run.sh` запускает основную задачу.
- `Modul_2_Data_Siense/lesson_1` и `goit-hw-06/flask-docker-app` — минимальные Flask-приложения, которые запускаются напрямую через `python app.py`.

Ключевые файлы и примеры

- Скрипт запуска скрейпера: `self_study/companies_general_data_collection_full/run.sh` — вызывает:
  `python -m src.main --input data/companies.csv --output output/results.csv --concurrency 20 --timeout 25 --max-pages 6`
- Основной код скрепера: `self_study/companies_general_data_collection_full/src/main.py` (использует `aiohttp`, `beautifulsoup4`, `pandas` и т.п.).
- Flask-приложения: `Modul_2_Data_Siense/lesson_1/app.py` и `Modul_1(python_core)/goit-hw-06/flask-docker-app/app.py` — минимальные примеры; запускаются через `python app.py` и слушают `0.0.0.0`.
- Зависимости: проектные `requirements.txt` рядом с проектами (например, `self_study/companies_general_data_collection_full/requirements.txt`).

Проектные конвенции и паттерны

- В проектах часто есть локальная виртуальная среда в каталоге `env/` (у каждого упражнения свой `env/`). AI-агентам: не удаляйте эти каталоги; ориентируйтесь на `requirements.txt` для восстановления сред.
- Отсутствуют интеграционные тесты и общая CI-конфигурация — изменения должны быть проверены локально. Тестов/папки `tests/` не обнаружено.
- Малые проекты держатся автономно (не общий package); правки в одном подпроекте не затрагивают другие.

Команды разработчика (практические примеры)

- Создать/активировать venv (macOS/Linux):
  - `python3 -m venv env`
  - `source env/bin/activate`
  - `pip install -r requirements.txt`
- Запустить скрейпер (из `self_study/companies_general_data_collection_full`):
  - `./run.sh` (скрипт уже содержит команду `python -m src.main ...`)
- Запустить Flask-приложение:
  - `python app.py`
    (скрипты запуска уже используют `app.run(... host='0.0.0.0')`)

Интеграции и зависимости

- Скрепер полагается на: `aiohttp`, `beautifulsoup4`, `lxml`, `pandas`, `tldextract` и др. — см. `requirements.txt` рядом с проектом.
- Нет явных внешних API-ключей в репозитории; если добавляются секреты, хранить вне репо (env vars or .env).

Что полезно знать AI-агенту

- При изменении кода обратите внимание, что многие директории содержат собственный `env/` — тестируйте, активируя виртуальную среду внутри соответствующего подпроекта.
- Для изменений в скрепере используйте `run.sh` или вызывайте `python -m src.main` с аргументами, как в `run.sh`, чтобы проверить поведение на коротких лимитах (`--max-pages`).
- При добавлении новых зависимостей — обновите соответствующий `requirements.txt` рядом с подпроектом.

Запрос на уточнение

- Если нужно, уточните предпочитаемый формат команд запуска (docker-compose, Makefile, CI) — добавлю примеры и шаги для автоматизации.

---

Автор заметок: автоматически сгенерировано AI‑ассистентом; прошу подтвердить или дополнить детали (особенно команды сборки/CI/секреты).
