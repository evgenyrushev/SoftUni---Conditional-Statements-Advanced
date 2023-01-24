month = input()
days = int(input())

studio = 0
apart = 0

if month == "May" or month == "October":
    studio = 50 * days
    apart = 65 * days
    if days > 14:
        studio *= 0.70
        apart *= 0.90
    elif days > 7:
        studio *= 0.95


if month == "June" or month == "September":
    studio = 75.20 * days
    apart = 68.70 * days
    if days > 14:
        studio *= 0.80
        apart *= 0.90


if month == "July" or month == "August":
    studio = 76 * days
    apart = 77 * days
    if days > 14:
        apart *= 0.90

print(f"Apartment: {apart:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
