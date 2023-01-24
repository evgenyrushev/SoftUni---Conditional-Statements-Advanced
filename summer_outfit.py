temp = int(input())
time_day = input()

outfit = None
shoes = None

if 10 <= temp <=18:
    if time_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < temp <= 24:
    if time_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
elif temp >= 25:
    if time_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")
