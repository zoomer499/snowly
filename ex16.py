#WRITE
from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать его, нажмите сочетание CTR+C (^C).")
print("Если хотите стереть файл, нажмите Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'w')

print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю у Вас три строки.")

line1 = input("строка 1: ")
line2 = input("строка 2: ")
line3 = input("строка 3: ")

print("Это я запишу в файл.")

line_common = line1 + '\n' + line2 + '\n' + line3 + '\n'
target.write(line_common)
#target.write(line1)
#target.write("/n")
#target.write(line2)
#target.write("/n")
#target.write(line3)
#target.write("/n")

print("И наконец , я закрою файл.")
target.close()

#READ
from sys import argv

script, filename =  argv

print(f"Я собираюсь прочитать этот файл {filename}.")
print("Если вы не хотите читать его, нажмите CTR+C (^C).")
print("Если хотите прочесть файл нажмите Enter.")

input("?")

print("Открытие файла...")
target = open(filename, 'r')
print(target.read())
