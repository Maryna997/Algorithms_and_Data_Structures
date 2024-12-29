def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))

def exists_in_list(arr, x):
    return linear_search(arr, x) != -1

print(exists_in_list(numbers, 7))
print(exists_in_list(numbers, 2))


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:    
            high = mid - 1
        # інакше x присутній на позиції і повертаємо його
        else: 
            return mid  
    # якщо елемент не знайдений
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")


# import matplotlib.pyplot as plt
# import numpy as np

# # Визначаємо кількість елементів та відповідні кроки для лінійного та двійкового пошуку
# n = np.arange(1, 21)
# linear_search_steps = n
# binary_search_steps = np.log2(n)

# # Побудова графіка
# plt.figure(figsize=(10, 6))
# plt.plot(n, linear_search_steps, label='Linear Search', color='blue')
# plt.plot(n, binary_search_steps, label='Binary Search', color='green')
# plt.xlabel('Number of elements (n)')
# plt.ylabel('Number of steps')
# plt.title('Comparison of Linear and Binary Search')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()

# # Відображення графіка
# plt.show()


def create_index_table(array, step):
    index_table = []
    for i in range(0, len(array), step):
        index_table.append((array[i], i))
    return index_table

# Основний відсортований масив
main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

# Створення індексної таблиці з кроком 4
index_table = create_index_table(main_array, 4)
print(index_table)

# Функція для індексно-послідовного пошуку
def indexed_sequential_search(array, index_table, target):
    # Пошук в індексній таблиці
    start = 0
    end = len(index_table) - 1
    while start <= end:
        mid = (start + end) // 2
        if index_table[mid][0] == target:
            return index_table[mid][1]
        elif index_table[mid][0] < target:
            start = mid + 1
        else: 
            end = mid - 1

    # Визначення діапазону для послідовного пошуку
    if start == 0:
        search_range = (0, index_table[0][1])
    elif start >= len(index_table):
        search_range = (index_table[-1][1], len(array))
    else: search_range = (index_table[start - 1][1], index_table[start][1])

    # Послідовний пошук в діапазоні
    for i in range(search_range[0], search_range[1]):
        if array[i] == target:
            return i
    return -1    # якщо елемент не знайдено


target = 15
result = indexed_sequential_search(main_array, index_table, target)
if result != -1:
    print(f"Елемент {target} знайдено на позиції {result}")
else:
    print(f"Елемент {target} не знайдено")



arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
key = 15
low = 0
high = len(arr) -1    # тобто high = 9
index = int(low + ((key - arr[low]) / (arr[high] - arr[low])) * (high - low))
print(index)


def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
            high = index - 1

    return -1


arr = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 25, 28, 30]
index = interpolation_search(arr, 25) # 11
print(arr[index])  # 25


phone_book = {'John Doe': '+1234567890', 'Jane Doe': '+0987654321'}
print(phone_book['John Doe'])  # Output: '+1234567890'


print((hash("Hello")))
print((hash("World")))



class Hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value 
                    return True 
            self.table[key_hash].append(key_value)
            return True 
        
    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


# Тестуємо нашу хеш-таблицю:
H = Hashtable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
print(H.get("orange"))  # Виведе: 20
print(H.get("banana"))  # Виведе: 30




def naive_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    # Перебір по символах головного рядка
    for i in range(N - M + 1):
        j = 0

        # Перебір по символах підрядка
        while j < M:
            if main_string[i + j] != pattern[j]:
                break
            j += 1

        # Якщо значення j дорівнює довжині підрядка, то підрядок знайдено
        if j == M:
            return i
        
    return -1

main_string = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
position = naive_search(main_string, pattern)

if position != -1:
    print(f"Підрядок знайдено на позиції {position}")
else:
    print("Підрядок не знайдено в головному рядку.")




def compute_lps(pattern):
    lps = [0] * len(pattern)
    lenght = 0
    i = 1

    while i <len(pattern):
        if pattern[i] == pattern[lenght]:
            lenght += 1
            lps[i] = lenght
            i += 1
        else:
            if lenght != 0:
                lenght = lps[lenght - 1]
            else:
                lps[i] = 0
                i += 1 
    return lps 

def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j
    return - 1    # якщо підрядок не знайдено

raw = "Цей алгоритм часто використовується в текстових редакторах та системах пошуку для ефективного знаходження підрядка в тексті."

pattern = "алг"

print(kmp_search(raw, pattern))




def build_shift_table(pattern):
 """Створити таблицю зсувів для алгоритму Боєра-Мура."""
 table = {}
 length = len(pattern)
 # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
 for index, char in enumerate(pattern[:-1]):
  table[char] = length - index - 1
 # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
 table.setdefault(pattern[-1], length)
 return table

def boyer_moore_search(text, pattern):
 # Створюємо таблицю зсувів для патерну (підрядка)
 shift_table = build_shift_table(pattern)
 i = 0 # Ініціалізуємо початковий індекс для основного тексту

 # Проходимо по основному тексту, порівнюючи з підрядком
 while i <= len(text) - len(pattern):
  j = len(pattern) - 1 # Починаємо з кінця підрядка

  # Порівнюємо символи від кінця підрядка до його початку
  while j >= 0 and text[i + j] == pattern[j]:
   j -= 1 # Зсуваємось до початку підрядка

  # Якщо весь підрядок збігається, повертаємо його позицію в тексті
  if j < 0:
   return i # Підрядок знайдено

  # Зсуваємо індекс i на основі таблиці зсувів
  # Це дозволяє "перестрибувати" над неспівпадаючими частинами тексту
  i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

 # Якщо підрядок не знайдено, повертаємо -1
 return -1

text = "Being a developer is not easy"
pattern = "developer"

position = boyer_moore_search(text, pattern)
if position != -1:
 print(f"Substring found at index {position}")
else:
 print("Substring not found")






def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)
    
    # Базове число для хешування та модуль
    base = 256 
    modulus = 101  
    
    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    
    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus
    
    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1

main_string = "Being a developer is not easy"
substring = "developer"

position = rabin_karp_search(main_string, substring)
if position != -1:
    print(f"Substring found at index {position}")
else:
    print("Substring not found")



# def polynomial_hash(s, base=256, modulus=101):
# 		"""
#     Повертає поліноміальний хеш рядка s.
#     """
#     n = len(s)
#     hash_value = 0
#     for i, char in enumerate(s):
#         power_of_base = pow(base, n - i - 1) % modulus
#         hash_value = (hash_value + ord(char) * power_of_base) % modulus
#     return hash_value

# print(polynomial_hash("abc"))  # 90
# print(polynomial_hash("developer"))  # 35
# print(polynomial_hash("general"))  # 82
