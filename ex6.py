types_of_people = 10
x = f"Существует {types_of_people} типов людей."

binary = "Python"
do_not = "нет"
y = f"Те, кто понимает {binary}, и те, кто - {do_not}."

print(x)
print(y)

print(f"Я сказал: {x}")
print(f"А еще я сказал: '{y}'")

hilarious = False
joke_evaluation = "Разве это не смешно?! {}"

print(joke_evaluation.format(hilarious))

w = "Это часть строки слева..."
e = "а это справа."

print(w + e)




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
