
# Даны несколько списков, состоящих из строк.
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# В переменную first_result запишем список из длин строк(len) списка first_strings, пройдем циклом (for),
# при условии (if), что длина строк не менее(>=) 5 символов. Выведем результат переменной на консоль(print).
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)

# В переменную second_result запишем список из пар слов(кортежей), при условии(if) если слова в списках одинаковой длины(len).
# Каждое слово из списка first_strings сравним с каждым словом из second_strings, пройдем циклом(for) по обоим спискам.
# Выведем результат переменной на консоль(print).
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

# В переменную third_result запишем словарь({}), где парой ключ-значение будет строка-длина строки(len).
# Значения строк будут перебираться циклом(for) из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки(остаток от деления на 2 равен 0).
# Выведем результат переменной на консоль(print).
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print(third_result)


# Вывод на консоль:
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}