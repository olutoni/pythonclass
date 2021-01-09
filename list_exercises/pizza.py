my_pizza = ["Deluxe", "BBQ Chicken Feast", "Brooklyn"]

for pizza in my_pizza:
    print(f"I like {pizza} pizza.\n")

print("I really love pizza!!!\n")

friend_pizza = my_pizza[:]
my_pizza.append("Pepperoni")
friend_pizza.append("meat lovers")

print(f"My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)

print()
print(f"My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)
