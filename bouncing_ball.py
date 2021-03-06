# Импортируем необходимые пакеты
# Генерация случайных значений
import random
# Пакет для работы с графикой. Из него импортируются все элементы.
from time import sleep
from tkinter import *

# Создаем основное окно
tk = Tk()
tk.title('Заставка')
# Запрещаем изменение размера формы
tk.resizable(False, False)
# Задаем ширину и высоту окна
WIDTH, HEIGHT = 400, 300
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

# И мячик (цвет будет отличаться каждый запуск)
ball = canvas.create_oval(10, 10, 50, 50, fill="#{:06x}".format(random.randint(0, 256 ** 3)))
# скорость шарика по x и y
x_speed = y_speed = 8


def move_ball():
    """ Основная движения шарика """
    # Определяем что переменные скорости мы берем из глобальной видимости пакета
    global x_speed, y_speed

    # Двигаем мячик на один раз! на значение скорости x и y
    canvas.move(ball, x_speed, y_speed)

    # Получаем координаты мячика
    (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)

    # Если мячик "столкнулась" с границей меняем значение скорости на противоположное
    if leftPos <= 0 or rightPos >= WIDTH:
        x_speed = -x_speed
    if topPos <= 0 or bottomPos >= HEIGHT:
        y_speed = -y_speed

    # Обновляем изображение
    tk.update()


if __name__ == '__main__':
    while True:
        # Двигаем шарик
        move_ball()
        # Делаем небольшую паузу для того чтобы изображение не казалось
        # слишком быстрым
        sleep(0.03)
