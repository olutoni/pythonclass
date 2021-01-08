friends = ["Wale", "Blaise", "Ladi", "Josh"]
for friend in friends:
    print(f"Hi {friend}, This is me wishing you a great 2021!!! ")

print()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append("BMW")
motorcycles.insert(2, "Harleys")
print(motorcycles)
del motorcycles[3]
print()
print(motorcycles)
last_motocycle = motorcycles.pop()
first_owned = motorcycles.pop(0)
print(f"The last motocycle is \"{last_motocycle}\"")
print(f"The first motocycle is \"{first_owned}\"")
motorcycles.remove("Harleys")
print(motorcycles)

cars = ["Toyota", "Honda", "BWM", "Benz", "Honda", "Mazda", "Kia"]

for car in cars:
    if car == "Honda":
        cars.remove(car)

print(cars)
