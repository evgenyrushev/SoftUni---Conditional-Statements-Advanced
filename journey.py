budget = float(input())
season = input()

destination = None
resort = None
amount = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        amount = budget * 0.30
        resort = "Camp"
    else:
        amount = budget * 0.70
        resort = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        amount = budget * 0.40
        resort = "Camp"
    else:
        amount = budget * 0.80
        resort = "Hotel"
else:
    destination = "Europe"
    amount = budget * 0.90
    resort = "Hotel"

print(f"Somewhere in {destination}")
print(f"{resort} - {amount:.2f}")
