type_flower = input()
number_flowers = int(input())
budget = int(input())

total_amount = 0

if type_flower == "Roses":
    total_amount = number_flowers * 5.00
    if number_flowers > 80:
        total_amount *= 0.9
elif type_flower == "Dahlias":
    total_amount = number_flowers * 3.80
    if number_flowers > 90:
        total_amount *= 0.85
elif type_flower == "Tulips":
    total_amount = number_flowers * 2.80
    if number_flowers > 80:
        total_amount *= 0.85
elif type_flower == "Narcissus":
    total_amount = number_flowers * 3.00
    if number_flowers < 120:
        total_amount *= 1.15
elif type_flower == "Gladiolus":
    total_amount = number_flowers * 2.50
    if number_flowers < 80:
        total_amount *= 1.20

if budget >= total_amount:
    print(f"Hey, you have a great garden with {number_flowers} {type_flower} and {budget - total_amount:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_amount - budget:.2f} leva more.")
