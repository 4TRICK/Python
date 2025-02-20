import json


def load_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Ошибка: Файл со словами не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка: Файл имеет неверный формат.")
        return None


def main():
    words = load_words("words.txt")
    if words is None:
        return

    print("Добро пожаловать! Введите слово, чтобы узнать его значения.")

    while True:
        user_input = input("Введите слово: ").strip() #.strip() — удаляем лишние пробелы в начале и конце строки

        if user_input in words:
            print(f"Значения слова '{user_input}': {', '.join(words[user_input])}")
        else:
            print("Ошибка: слово не найдено.")
            retry = input("Хотите попробовать снова? (да/нет): ").strip().lower()
            if retry != "да":
                print("До свидания!")
                break


if __name__ == "__main__":
    main()
