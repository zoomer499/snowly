types_of_people = 10 # количество типов людей
x = f"Существует {types_of_people} типов людей." #переменная с функцией

binary = "Python" #переменная
do_not = "нет"    # переменная нет
y = f"Те, кто понимает {binary}, и те, кто - {do_not}." # переменная строковая с добавлением переменных внутри

print(x) # вывести переменную x
print(y) # вывести переменную y

print(f"Я сказал: {x}") # вывести а экран фразу + переменная
print(f"А еще я сказал: '{y}'") # вывести а экран фразу + переменная

hilarious = False # переменная с булевым значением
joke_evaluation = "Разве это не смешно?! {}" # переменная с форматируемым значением в круглых скобках

print(joke_evaluation.format(hilarious))  # вывести на экран значение переменной joke_evaluation с добавлением переменной hilarious

w = "Это часть строки слева..." # строковая переменная
e = "а это справа." # строковая переменная

print(w + e) # вывести сумму строковых переменных 

#Тестовая проверка
#x = "There are %d types of people." %10
#binary = "binary"
#do_not = "don't"
#y = "Those who know %s and those who %s." %(binary, do_not)

#print x
#print y

#print "I said: %r." %x
#print "I also said: '%s'." %y

#hilarious = False
#joke_evalution = "Isn't that joke so funny?! %r"

#print joke_evalution % hilarious

#w = "This is the left side of..."
#e = "a string with a right side."

#print w + e
