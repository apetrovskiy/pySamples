name = "Alice"
print(name)
age = 25
print(name, age)

name, age = "Alice", 25
print(name, age)

other_name = name
print(other_name)

x = 3
y = 4
x, y = y, x
print(x, y)

variable = 1
print(type(variable))
variable = "Hello, world"
print(type(variable))

my_integer = 10
my_float = 20.5

# integer
x = 10
y = 5
summary = x + y
print(summary)

# float
x = 10.5
y = 5.5
summary = x + y
print(summary)

# multiplication
x = 10
y = 5
z = x * y
print(z)

# division
z = x / y
print(z)

# division by zero
try:
    x = 10
    y = 0
    z = x / y
    print(z)
except ZeroDivisionError as err:
    print(err)

# extent
x = 2
print(x**3)
print(x * x * x)

# modulo
print(9 / 4 == 2 * 4 + 1)
print(9 == 2 * 4 + 1)

x = 9
y = 4

print(x // y)
print(x % y)

# order of operations
integer = 2 + 3 * 5
print(integer)
integer = (2 + 3) * 5
print(integer)

# integer and float
my_integer = 10
my_float = 5.5

print(my_integer + my_float)

# variables' sizes
big_number = 10**1000
print(big_number)

# type conversion
my_int = 1
my_float = float(my_int)

print(my_float)

my_float = 1.5
my_integer = int(my_float)

print(my_integer)

my_float = 1.999999
my_integer = int(my_float)

print(my_integer)

# rounding
my_float = 1.999999
my_integer = round(my_float)

print(f"rounded = {my_integer}")
