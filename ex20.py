# ипользуем библиотеку argv, которая позволяет добавять аргументы при запуске скрипта
from sys import argv

# создаем аргументы для функции argv
script, input_file = argv

# вводим новую функцию с аргументом f, который нужно вывести на экран
def print_all(f):
    print(f.read())

# создаем функцию обнуления позиции файла, если 0, то действия с файлом обнуляются
def rewind(f):
    f.seek(0)

# создаем функцию с двумя переменными на входе, котороя выводит только одну линию на экран
def print_a_line(line_count, f):
    print(line_count, f.readline())

# переменная открывающая файл на входе
current_file = open(input_file)

# вывести на экран
print("Первым делом выведем этот файл целиком: \n")

# используем функцию print_all для того чтобы вывести на эран файл
print_all(current_file)

# выводим на экран заданное  предложение
print("Теперь отматаем назад, словно это кассета.")

# используем функцию для обнуления действий с файлом
rewind(current_file)

# выводим заданную строку на экран
print("Выведем три строки:")

# далее используем функцию с двумя переменными
current_line = 1
print_a_line(current_line, current_file)

#current_line = 1, += означает прибавление к перемнной current_line единицы
current_line += 1
print_a_line(current_line, current_file)

#current_line = 1
current_line += 1
print_a_line(current_line, current_file)
