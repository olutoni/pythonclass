# Program to calculate the Factorial of a Number
number = input("Enter integer number: ")

if number.isnumeric():
    number = int(number)

    # Check to see if the number is Zero—if it is then the answer is 1—print this out.
    if number == 0:
        print(f"{number}! = 1 ")

    # Otherwise use a loop to generate the result and print it out.
    else:
        factorial = 1
        for i in range(1, number+1):
            factorial *= i
        print(f"{number}! = {factorial}")
else:
    print("Error, not an integer")
