favorite_numbers = {
    "Fola": 2,
    "Fred": 6,
    "Eni": 9,
    "Tomi": 15,
    "Ben": 65,
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}")

print()
for name in favorite_numbers:
    print(f"{name}'s favorite number is {favorite_numbers[name]}")

names = list(favorite_numbers.keys())
print(names)

languages = {'python', 'ruby', 'python', 'c'}

print(languages)
