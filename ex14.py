from sys import argv

script, first_name, second_name = argv
promt = '()===3 '

print(f"Привет, {first_name} {second_name}, я - сценарий {script}.")
print("Я хочу задать тебе несколько вопросов.")
print(f"Я тебе нравлюсь, {first_name} {second_name}?")
likes = input(promt)

print(f"Где ты живешь, {first_name} {second_name}?")
lives = input(promt)

print(f"На каком компьютере ты работаешь?")
computer = input(promt)

print(f"""
Итак, ты ответил {likes} на вопрос, нравлюсь ли я тебе.
Ты живешь {lives}. Не представляю что это за задница.
И у тебя есть компьютер {computer}. Прекрасно!
""")
