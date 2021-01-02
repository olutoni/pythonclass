# program to Print All the Prime Numbers in a Range
number = input("enter number: ")

if number.isnumeric():
    number = int(number)

    if number < 2:
        print("Error, number less than 2")
    else:
        # assume number is a prime number by default
        prime_number = True
        for i in range(2, number+1):
           # print(i)
            for j in range(2, i):
                #print(i, j)
                if i % j == 0:
                    prime_number = False
                    break
            if prime_number:
                print(f"{i} is prime number")
            prime_number = True


else:
    print("Error, not an integer")
