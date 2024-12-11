import turtle
import math

def draw_pythagoras_tree(t, branch_length, angle, depth):
    """
    Рекурсивна функція для малювання дерева Піфагора
    
    :param t: об'єкт turtle для малювання
    :param branch_length: довжина гілки
    :param angle: кут між гілками
    :param depth: поточна глибина рекурсії
    """
    if depth == 0:
        return
    
    # Малювання поточної гілки
    t.forward(branch_length)
    
    # Збереження поточного стану черепахи
    current_pos = t.pos()
    current_heading = t.heading()
    
    # Права гілка
    t.left(angle)
    right_branch = branch_length * math.cos(math.radians(angle))
    draw_pythagoras_tree(t, right_branch, angle, depth - 1)
    
    # Повернення до попереднього стану
    t.penup()
    t.setpos(current_pos)
    t.setheading(current_heading)
    t.pendown()
    
    # Ліва гілка
    t.right(angle)
    left_branch = branch_length * math.cos(math.radians(angle))
    draw_pythagoras_tree(t, left_branch, angle, depth - 1)
    
    # Повернення до попереднього стану
    t.penup()
    t.setpos(current_pos)
    t.setheading(current_heading)
    t.pendown()

def create_pythagoras_tree(depth=5, branch_length=100, angle=45):
    """
    Створення вікна та налаштування параметрів для малювання дерева Піфагора
    
    :param depth: рівень рекурсії (глибина фракталу)
    :param branch_length: початкова довжина гілки
    :param angle: кут між гілками
    """
    # Налаштування вікна та черепахи
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.title(f"Дерево Піфагора (Рівень: {depth})")
    window.bgcolor("white")
    
    # Створення черепахи
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.color("green")
    t.width(2)
    
    # Початкове налаштування положення
    t.left(90)  # Повертаємо черепаху вгору
    t.penup()
    t.goto(0, -250)  # Встановлюємо початкову позицію в нижній частині вікна
    t.pendown()
    
    # Малювання дерева
    draw_pythagoras_tree(t, branch_length, angle, depth)
    
    # Завершення малювання
    window.mainloop()

# Приклад використання
if __name__ == "__main__":
    # Можливість змінити рівень рекурсії, довжину гілки та кут
    create_pythagoras_tree(depth=7, branch_length=150, angle=45)