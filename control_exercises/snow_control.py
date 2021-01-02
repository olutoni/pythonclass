temp = int(input("What is the temperature: "))
snowing = input("Is it snowing?: Enter \"Yes\" or \"No\" ")

if temp >= 0 and snowing == "No":
    print("No snow, no boots and we will be having a cold drink")
elif temp >= 0 and snowing == "Yes":
    print("Put on your boots and we will be having a cold drink")
elif temp < 0:
    print("It is freezing")
    if snowing == "Yes":
        print("It is also snowing, put on your boots")
    elif snowing == "No":
        print("It is not snowing, so no need for boots")
    print("Time for hot chocolate")
print("Bye")
