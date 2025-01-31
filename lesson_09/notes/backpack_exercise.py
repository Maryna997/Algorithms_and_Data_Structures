# (Brute-force), або повний перебір:
# Функція для обчислення максимальної вартості
def knapSack(W, wt, val, n):
    # Базовий випадок
    if n == 0 or W == 0:
        return 0

    # Якщо вага n-го предмета більше, ніж місткість рюкзака, то цей предмет не можна включити у рюкзак
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

    # повертаємо максимум із двох випадків:
    # (1) n-ий предмет включено
    # (2) не включено
    else:
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1),
        )

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# викликаємо функцію
print(knapSack(capacity, weight, value, n))  # 220




# У жадібному підході до задачі про рюкзак вибір предметів відбувається на основі певного критерію. Найпоширенішим критерієм є відношення вартість/вага (value-to-weight ratio) кожного предмета
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapSack(items: list[Item], capacity: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
    return total_value

# Дані предметів
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
# Місткість рюкзака
capacity = 50
# Виклик функції
print(knapSack(items, capacity))  # 160





#Динамічне програмування
def knapSack(W, wt, val, n):
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# виклик функції
print(knapSack(capacity, weight, value, n))  # 220

