def add(a, b):
    print(f"СЛОЖЕНИЕ {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"ВЫЧИТАНИЕ {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"УМНОЖЕНИЕ {a} * {b}")
    return a * b

def divide(a, b):
    print(f"ДЕЛЕНИЕ {a} / {b}")
    return a / b


print ("Давайте выполним несколько вычислений с помощью функций!")

age = add(30, 5)
height = subtract(190, 4)
weight = multiply(35, 2)
iq = divide(250, 2)

print(f"Возраст: {age}, Рост: {height}, Вес: {weight}, IQ: {iq}")


# Головоломка, как доп.задание
print("Это головоломка.")
print("Напишите свое количество пальце и размер полового органа с плавающей точкой: ")
finger = int(input("> "))
fuck = float(input("> "))

#what = add(age, subtract(height, multiply(weight, divide(iq,2))))
iqn = divide(age,2)
multi = multiply(weight, iqn)
subt = subtract(height, multi)
what = add(iqn, subt)
realnost =

print("Получается: ", what, "Вы можете это вычислить вручную?")
