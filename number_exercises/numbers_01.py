number = 100
i = 4.7
int_value = 1
string_value = '1.5'

# prints the type of the variables defined above
print(type(number))
print(type(i))
print(type(int(i)))


float_value = float(int_value)
print('\nint value as a float:', float_value)
print(type(float_value))
float_value = float(string_value)
print('string value as a float:', float_value)
print(type(float_value))
