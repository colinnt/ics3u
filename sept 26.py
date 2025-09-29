import math
#1
total = 20 + 32
print(total)

power = 5 ** 2
print(power)

expression = (5 + 9) * (15 - 7)
print(expression)

hour = 9
minute = 10
hour = hour - 1
print(hour)
total_minutes = hour * 60 + minute
print(total_minutes)

# 352
# 25
# 112
# 8
# 490

#2
print ("number 2")
x = 2
y = x + x
print ( y )

s = "2"
t = s + s
print ( t )

#4
# 22

#3
#print ("number 3")
number = 7
print (number + 5)


#Write a program that asks the user for a year of birth and outputs their age in the current year.
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - year_of_birth
print(f'Your age in {current_year} is {age}')

#Calculate the volume of a sphere with a radius of 5 using the formula four thirds pi r cubed

radius = 5
volume = (4/3) * math.pi * radius**3
print(f'The volume of a sphere with radius {radius} is {volume:.2f}')

#The Andromeda galaxy is 2.9 million light-years away. There are 5.878 times 10 to the 12th power miles per light-year. 
#Calculate how many miles it is to the Andromeda galaxy.

distance_light_years = 2.9e6
miles_per_light_year = 5.878 * math.pow(10, 12)
distance_miles = distance_light_years * miles_per_light_year
print(f'The distance to the Andromeda galaxy is {distance_miles:.2e} miles')

#Assume the universe is 15 billion years old. Calculate how many seconds old it is.
age_universe_years = math.pow(10, 10) * 1.5
seconds_per_year = 365.25 * 24 * 60 * 60
age_universe_seconds = age_universe_years * seconds_per_year
print(f'The universe is approximately {age_universe_seconds:.2e} seconds old.')

#a)  Type in and run the following program.
# b)  Can you enter input to make the program crash?
#      What logic would you use to fix the problem?  (NOT CODE, just logic)
# c)  Change the program to convert from cm to inches.

converstion_factor = 2.54
inches = int(input("please enter number of inches to convert to cm: "))
cm = inches * converstion_factor
print(f'{inches} inches =  {cm: .1f} cm')

# Finish the program to output the name in the format  
# last name, first name  including the comma.

last_name = input("Please enter your last name")
first_name = input("Please enter your first name")
print(f'{last_name}, {first_name}')

# number 10
# The sum
# The difference
# The product
# The average
# The maximum  Hint ... use the function    max(integer1, integer2)  

number_one = float(input("Enter first number"))
number_two = float(input("Enter second number"))

print(f'The sum is {number_one + number_two}')
print(f'The difference is {number_one - number_two}')
print(f'The product is {number_one * number_two}')
print(f'The average is {(number_one + number_two) / 2}')
print(f'The maximum is {max(number_one, number_two)}')

#Ask a user to enter an integer and then display the remainder when that number is divided by 2, 5, 10. 

number = int(input("Enter an integer"))
remainder = number % 2
print(f'The remainder when {number} is divided by 2 is {remainder}')

remainder = number % 5
print(f'The remainder when {number} is divided by 5 is {remainder}')

remainder = number % 10
print(f'The remainder when {number} is divided by 10 is {remainder}')

# Write a program that asks the user for the lengths of the sides of a rectangle
# and prints out the area of the rectangle. Remember that A = length * width

side_one = float(input("Enter first rectangle side"))
side_two = float(input("Enter second rectangle side"))
area = side_one * side_two
print(f'The area of the rectangle is {area}')

# Python allows you to do math (operations) with strings. 
n = 5
s = "Hello"
t = "World"

print (s + t)
print (s * n)
print('-' * 20)
print('|' + 'A' * 18 + '|')

# Write a program that prints the following grids.
# Use Python's ability to multiply strings.
def print_grid(rows, cols):

    horizontal = "+---" * cols + "+"
    vertical = "|   " * cols + "|"

    for r in range(rows):
        print(horizontal)
        for _ in range(1): 
            print(vertical)
    print(horizontal)

print_grid(3, 3)

#Type the following line of code.  What information does the function len  calculate?

name = "Aaron"
print (len(name))

#prints number of letters

#Write a program that prints a grid of symbols around a name. Challenge is that your program should work for any name of any length without changing the program!

name = input("Please enter your name")
name_length = len(name)
dashes = '-' * (name_length + 2)
print (dashes)
print ("|" + name + "|" )
print (dashes)
