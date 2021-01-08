# program to check if a number is a prime number using recursion
number = int(input("enter number: "))


def is_prime(num, i=2):

    if num <= 2:
        return True if number == 2 else False
    if num % i == 0:
        return False
    if i * i > num:
        return True

    return is_prime(num, i+1)


print(is_prime(number))
