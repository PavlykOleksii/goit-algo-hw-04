import turtle
import argparse

def koch_curve(t, order, size):
    if order == 0:
        # Базовий випадок: малюємо звичайну пряму лінію
        t.forward(size)
    else:
        # Рекурсивний випадок: ділимо лінію на 4 менші частини
        size /= 3.0

        koch_curve(t, order - 1, size)
        t.left(60)

        koch_curve(t, order - 1, size)
        t.right(120)

        koch_curve(t, order - 1, size)
        t.left(60)

        koch_curve(t, order - 1, size)

def draw_koch_snowflake(order, size=300):

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Фрактал: Сніжинка Коха")

    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()

    screen.mainloop()

def parse_args():
    parser = argparse.ArgumentParser(
        description="Візуалізація фракталу Сніжинка Коха"
    )
    parser.add_argument(
        "order",
        type=int,
        nargs="?",
        default=3,
        help="Рівень рекурсії (наприклад: 1, 2, 3, 4)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    # Перевіряємо, щоб рівень рекурсії був невід'ємним
    if args.order < 0:
        print("Помилка: Рівень рекурсії має бути невід'ємним числом (>= 0).")
    else:
        print(f"Малюємо Сніжинку Коха з рівнем рекурсії: {args.order}")
        draw_koch_snowflake(args.order)