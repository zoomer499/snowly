#Добавление метода sys и использование его параметра argv
from sys import argv

# Приравниваем двум переменным значения argv
script, filename = argv

# Переменная txt равно имени переменной filename
txt = open(filename)

# Вывести на экран строку с именем файла filename
print(f"Содержимое файла {filename}:")
# Вывести на экран текст файла, используя параметр read()
print(txt.read())

# Вывестии на экран строку с требованиями
print("Снова введите имя файла:")
# Новая перемнная  file_again, в которую пользователь может внести данные с клавиатуры
file_again = input("> ")

# Новая переменная для прочтения файла
txt_again = open(file_again)

# Вывести содержимое файла на экран
print(txt_again.read())