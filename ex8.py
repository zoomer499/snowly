formatter = "{} {} {} {}" # вводим новую переменную

print(formatter.format(1,2,3,4)) # добавляем в переменную значения для вывода на экран
print(formatter.format("раз", "два", "три", "четыре"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
			"Спят в конюшне пони,",
			"начал пес дремать,",
			"только мальчик Джонни",
			"не ложится спать!"
))




#formatter = "%r %r %r %r"

#print formatter % (1, 2, 3, 4)
#print formatter % ("one", "two", "three", "four")
#print formatter % (True, False, False, True)
#print formatter % (formatter, formatter, formatter, formatter)
#print formatter % (
#	"I had this thing.",
#	"That you could type up right.",
#	"But it didn't sing.",
#	"So I said goodhight."
#)
