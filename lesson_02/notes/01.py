import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr) # Output: array([1, 2, 3, 4, 5])
print(arr + 2) # Output: array([3, 4, 5, 6, 7])


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2) # Output: array([5, 7, 9])

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # Output: 15
print(np.mean(arr)) # Output: 3.0

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)



my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list) # Output: [1, 2, 3, 4, 5, 6]



my_list = [1, 2, 3, 5]
my_list.insert(3, 4) # Insert number 4 at position 3
print(my_list) # Output: [1, 2, 3, 4, 5]


my_list = [1, 2, 3, 4, 5]
my_list.remove(3) # Removes number 3 from the list
print(my_list) # Output: [1, 2, 4, 5]



my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list) # Output: [1, 1, 2, 3, 4, 5, 9]


my_dict = {'name': 'John', 'age': 25}
print(my_dict['name']) # Output: John



my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26
print(my_dict) # Output: {'name': 'John', 'age': 26}



my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict) # Output: {'name': 'John', 'age': 25, 'city': 'New York'}



my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['city']
print(my_dict) # Output: {'name': 'John', 'age': 25}



my_set = set([1, 2, 3, 4, 5])
print(my_set) # Output: {1, 2, 3, 4, 5}


my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set) # Output: {1, 2, 3, 4, 5, 6}


my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
print(my_set) # Output: {2, 3, 4, 5}



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}


stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack) # Output: ['a', 'b', 'c']

print(stack.pop()) # Output: 'c'
print(stack) # Output: ['a', 'b']

def peek(stack):
    return stack[-1]

print(peek(stack)) # Output: 'b'

def is_empty(stack):
    return len(stack) == 0

print(is_empty(stack)) # Output: False



class Stack:
    def __init__(self):
        self.stack = []

# Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

# Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

# Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

# Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
s = Stack()
s.push('a')
s.push('b')
s.push('c')
print(s.peek()) # Output: 'c'
print(s.pop())  # Output: 'c'
print(s.peek()) # Output: 'b'
print(s.is_empty()) # Output: False





from queue import Queue

# Створюємо чергу
q = Queue()

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

print(q.queue) # Output: deque(['a', 'b', 'c'])

# Видаляємо елемент
q.get()
print(q.queue) # Output: deque(['b', 'c'])




from queue import Queue

# Створюємо чергу
q = Queue(maxsize = 3)

# Перевіряємо, чи черга порожня
print(q.empty()) # Output: True

# Додаємо елементи
q.put('a')
q.put('b')
q.put('c')

# Перевіряємо, чи черга повна
print(q.full()) # Output: True

# Перевіряємо розмір черги
print(q.qsize()) # Output: 3

# Видаляємо елементи
print(q.get()) # Output: 'a'
print(q.get()) # Output: 'b'



from queue import Queue
import random

class Client:
    def __init__(self, name):
        self.name = name
        self.operations = random.randint(1, 5) # Випадкова кількість операцій

class Bank:
  def __init__(self):
    self.clients = Queue()

  def new_client(self, client):
    self.clients.put(client)

  def serve_clients(self):
    while not self.clients.empty():
      current_client = self.clients.get()
      print(f"Обслуговуємо клієнта {current_client.name} з {current_client.operations} операцій")
      # Тут можна додати час обслуговування та іншу логіку

# Створюємо банк
bank = Bank()

# Додаємо клієнтів
for i in range(5):
  bank.new_client(Client(f"Client-{i}"))

# Обслуговуємо клієнтів
bank.serve_clients()





from collections import deque

d = deque()
print(d)  # deque([])

d.append('right')
d.appendleft('left')
print(d)  # deque(['left', 'right'])

d.pop()
d.popleft()
print(d)  # deque([])

d.extend(['a', 'b', 'c'])
d.extendleft(['x', 'y', 'z'])
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

d.rotate(2)
print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

d.rotate(-2)
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

d = deque(maxlen=3)
d.extend([1, 2, 3])
print(d)  # deque([1, 2, 3])

d.append(4)
print(d)  # deque([2, 3, 4])

d = deque([1, 2, 3, 4, 2, 5])
print(d.count(2))  # 2
