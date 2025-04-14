def parse_input(user_input):
    """Парсит ввод пользователя."""
    path_log, *command = user_input.split()
    if command:
        command = command[0].strip().lower()
    else:
        command = None
    return path_log, command


def parse_log_line(line: str) -> dict:
    """Парсит строку лога и возвращает словарь."""
    parts = line.strip().split(" ", 2)
    if len(parts) < 3:
        return {}
    timestamp, level, message = parts
    return {"timestamp": timestamp, "level": level, "message": message}


def load_logs(file_path: str) -> list:
    """Загружает логи из файла в список."""
    logs = []
    try:
        with open(file_path, "r", encoding="utf8") as log_file:
            for line in log_file:
                log_entry = parse_log_line(line)
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фильтрует логи по уровню (info, error, debug, warning)."""
    return [log for log in logs if log.get("level", "").lower() == level]


def count_logs_by_level(logs: list) -> dict:
    """Подсчитывает количество логов каждого уровня."""
    counts = {"info": 0, "error": 0, "debug": 0, "warning": 0}
    for log in logs:
        level = log.get("level", "").lower()
        if level in counts:
            counts[level] += 1
    return counts


def display_log_counts(counts: dict):
    """Выводит количество логов по уровням."""
    for level, count in counts.items():
        print(f"{level.capitalize()}: {count}")


def main():
    while True:
        user_input = input("Введите путь к файлу логов и команду: ")
        path_log, command = parse_input(user_input)

        if path_log in ["exit", "close"]:
            break

        logs = load_logs(path_log)
        if not logs:
            continue

        if command in ["info", "error", "debug", "warning"]:
            filtered_logs = filter_logs_by_level(logs, command)
            for log in filtered_logs:
                print(f"{log['timestamp']} [{log['level'].upper()}] {log['message']}")
        elif command == "count":
            counts = count_logs_by_level(logs)
            display_log_counts(counts)
        else:
            print(
                "Ошибка: Неверная команда. Доступные: info, error, debug, warning, count"
            )


if __name__ == "__main__":
    main()
