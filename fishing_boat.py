budget = int(input())
season = input()
number_fishermen = int(input())

spring_rent = 3000
summer_rent = 4200
winter_rent = 2600

total_amount = 0

if season == "Spring":
    total_amount += spring_rent
elif season == "Winter":
    total_amount += winter_rent
else:
    total_amount += summer_rent

if number_fishermen <= 6:
    total_amount *= 0.90
elif 7 <= number_fishermen <= 11:
    total_amount *= 0.85
else:
    total_amount *= 0.75

if number_fishermen % 2 == 0 and season != "Autumn":
    total_amount *= 0.95

if total_amount <= budget:
    print(f"Yes! You have {budget - total_amount:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_amount - budget:.2f} leva.")

