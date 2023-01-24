days_vacation = int(input()) - 1
room_type = input()
grade = input()

price_for_room = 0

if room_type == "room for one person":
    price_for_room = 18.00 * days_vacation
elif room_type == "apartment":
    price_for_room = 25.00 * days_vacation
    if days_vacation < 10:
        price_for_room *= 0.70
    elif 10 <= days_vacation <= 15:
        price_for_room *= 0.65
    else:
        price_for_room *= 0.50

elif room_type == "president apartment":
    price_for_room = 35.00 * days_vacation
    if days_vacation < 10:
        price_for_room *= 0.90
    elif 10 <= days_vacation <= 15:
        price_for_room *= 0.85
    elif days_vacation > 15:
        price_for_room *= 0.80

if grade == "positive":
    price_for_room *= 1.25
else:
    price_for_room *= 0.90

print(f"{price_for_room:.2f}")