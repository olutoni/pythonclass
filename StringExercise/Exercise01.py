print("hello world")

name = input("enter your name: ")
print(f"hello {name}")

str1 = "Good"
str2 = " Day"
str3 = str1 + str2

print(str3)
print(len(str3))

my_string = 'Bookkeeping'
print(my_string[2:5])


title = "The Good, The Bad, and The Ugly"

print(title.split(","))
print("title.count('The'):", title.count('The'))
print(title.replace("Ugly", "Pretty"))
print(title.find("God"))
print(title.swapcase())
