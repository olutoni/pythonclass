my_foods = ['pizza', 'falafel', 'carrot cake', 'rice', 'beans', 'salad']
friend_foods = my_foods[:]

# The first three items in the list.
print(f"The first three items in the list are: {my_foods[:3]}")

# Using list comprehension to get the first three items in the list.
first_three_items = [my_foods[i] for i in range(0, 3)]
print(f"The first three items in the list are: {first_three_items}")

# Three items from the middle of the list
print(f"Three items from the middle of the list are: {my_foods[2:5]}")

# The last three items in the list
print(f"The last three items in the list are: {my_foods[-3:]}")
