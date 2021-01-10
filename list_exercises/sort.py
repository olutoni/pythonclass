#listed = sorted(["Eva", "eva", "string", "Aaron", 2.4, 1], key=str)

# the same result using lambda
#listed = sorted(["Eva", "eva", "string", "Aaron"])

# listed = sorted(["Eva", "eva", "string", "Aaron", 2.4, 1],
#                 key=lambda x: str(x).lower())

# names = ["Eva", "eva", "string", "Aaron", 1, 2.4]
# names.sort(key=str)
# print(listed)

first_list_len = int(input("Number of items in list A: "))


first_list = []
second_list = []


for i in range(0, first_list_len):
    item = input("provide your list: ")

    first_list.append(item)

print(first_list)

second_list_len = int(input("Number of items in list B: "))

for i in range(0, second_list_len):
    item = input("provide your list: ")

    second_list.append(item)

print(second_list)

first_list.sort()
second_list.sort()

print(first_list)
print(second_list)

if first_list == second_list:
    print("list is a match")
else:
    print("no match")

#first = ['Apple', 'Lime', 'Lemon', 'Orange']
#second = ['Apple', 'Lime', 'Lemon', 'Orange']
#second = ['Apple', 'Orange', 'Lime', 'Lemon']

# if first == second:
#    print("list is a match")
# else:
#     print("no match")
