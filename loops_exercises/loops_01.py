# Loop over a set of values using while loop and counter
count = 0
print('Starting')
while count < 10:
    print(count, ' ', end='')  # part of the while loop
    count += 1  # also part of the while loop
print()  # not part of the while loop
print('Done')
print("*" * 30)


# Loop over a set of values in a range
print('Print out values in a range')
for i in range(0, 10):
    print(i, ' ', end='')
print()
print('Done')

for _ in range(0, 10):
    print('.', end='')
print()
