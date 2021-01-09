my_favorite_fruits = ["Oranges", "Bananas", "Apples", "Grapes"]

converted_fruits_list = [fruits.lower() for fruits in my_favorite_fruits]
your_fruit = input("what is your favorite fruit?: ")

if your_fruit.lower() in converted_fruits_list:
    print(f"I really like {your_fruit} ")
