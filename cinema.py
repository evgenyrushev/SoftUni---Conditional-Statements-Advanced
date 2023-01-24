movie_type = input()
rows = int(input())
cols = int(input())

price = 0

if movie_type == "Premiere":
    price = cols * rows * 12
elif movie_type == "Normal":
    price = cols * rows * 7.50
else:
    price = cols * rows * 5

print(f"{price:.2f} leva")
