# создаем функцию cheese_and_crackers для вывода определенного сценария с задаваемыми аргументами
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"У нас есть {cheese_count} сырков!")
    print(f"У нас есть {boxes_of_crackers} пачек чипсов!")
    print("Это достаточно для вечеринки!")
    print("Погнали!\n")

# непосредственно, вызов функции с числовыми аргументами внутри скобок
print("Мы можем непосредственно передать числа функции:")
cheese_and_crackers(20,30)

# вызов функции с заранеем заданными переменными
print("ИЛИ, мы можем использовать переменные из нашего сценария:")
#amount_of_cheese = 10
#amount_of_cracker = 50
amount_of_cheese = int(input("> "))
amount_of_cracker = int(input("> "))
cheese_and_crackers(amount_of_cheese, amount_of_cracker)

# вызов функции и суммирование аргументов внутри ()
print("Мы даже можем выполнять вычисления внутри функции:")
cheese_and_crackers(10 + 20, 5 + 6)

# объединение переменных и числовых значений внутри функции
print("И объединять переменные с вычислениями:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_cracker + 1000)
