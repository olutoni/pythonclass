# Counting to Twenty:
for number in range(1, 21):
    print(number)

# Summing a Million:
count = [number for number in range(1, 10000001)]
print(min(count))
print(max(count))
print(sum(count))

# odd numbers
for number in range(1, 21, 2):
    print(number)

# multiples of 3
multiples_of_3 = [number for number in range(3, 31, 3)]
print(multiples_of_3)

# cubes
cubes = [number**3 for number in range(1, 11)]
print(cubes)
