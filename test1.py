#!/usr/bin/python

#str name
#int age
#float height
#float weight
#float bmi
#str descripion

name = input("Ваше имя: ")
print("Привет, ", name, "!")
age = int(input("Сколько вам полных лет? "))
height = float(input("Какой у вас рост? "))
weight = float(input("Какой у вас вес? "))

if age < 10 or height <= 0 or height > 3 or weight <= 0 or weight > 500:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2
    bmi = round(bmi, 2)

    if bmi < 18.5:
        description = "недостаточной массой тела."
    elif bmi < 25:
        description = "нормальной массой тела."
    elif bmi < 30:
        description = "избыточной массой тела."
    else:
        description = "ожирением."

    print("Ваш индекс массы тела: ", bmi)
    print("Вы относитесь к группе людей с", description)
