from pathlib import Path
import argparse

def parse_args():
    # 1. Створюємо об'єкт парсера
    parser = argparse.ArgumentParser(description="Рекурсивне сортування файлів за розширенням")
    
    # 2. Додаємо обов'язковий аргумент (джерело)
    parser.add_argument("source", help="Шлях до вихідної директорії")
    
    # 3. Додаємо опціональний аргумент (призначення)
    parser.add_argument("output", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist)")
    
    # 4. Зчитуємо аргументи 
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print(f"Вихідна папка: {args.source}")
    print(f"Папка призначення: {args.output}")