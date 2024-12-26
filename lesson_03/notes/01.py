def factorial(n):
    if n == 0:    # базовий випадок
        return 1
    else: 
        return n * factorial(n-1)    # рекурсивний випадок
    
print(factorial(5))
    


def fibonacci(n):
    if n <= 1:    # базовий випадок
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)    # рекурсивний випадок
    
print(fibonacci(10))


def factorial(n):
    print("Виклик функції factorial з n =", n)
    if n == 1:
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
        result = n * factorial(n-1)
        print("Повернення результату для n =", n, ":", result)
        return result

print(factorial(5))


def sum_iter(n):
    result = 0 
    for i in range (1, n+1):
        result += i
    return result

print(sum_iter(5))


def sum_rec(n):
    if n == 0:    # базовий випадок
        return 0
    else:
        return n + sum_rec(n-1)    # рекурсивний випадок
    
print(sum_rec(5))


def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

print(fibonacci_iterative(10))

 
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value    
    return value 


from functools import lru_cache

@lru_cache(maxsize=None)   # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle(vertices, ax):
    triangle = patches.Polygon(vertices, fill=False, edgecolor='black')
    ax.add_patch(triangle)

def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

def sierpinski(vertices, level, ax):
    draw_triangle(vertices, ax)
    if level > 0:
        sierpinski([vertices[0], midpoint(vertices[0], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)
        sierpinski([vertices[1], midpoint(vertices[0], vertices[1]), midpoint(vertices[1], vertices[2])], level-1, ax)
        sierpinski([vertices[2], midpoint(vertices[2], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    vertices = [[0, 0], [0.5, 0.75], [1, 0]]
    sierpinski(vertices, 3, ax)
    plt.show()

main()




import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size = 300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    koch_curve(t, order, size)

    window.mainloop()

# Виклик функції
draw_koch_curve(3)