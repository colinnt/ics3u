#Write a main function for the function compare ( x, y ) shown below.
#Call the function multiple times to test out different values for x and y.
from ast import main
import random


def compare (x,y):
    if x < y:
        return f'{x} is less than {y}'

    elif x > y:
        return f'{x} is greater than {y}'

    else:
        return f'{x} and {y} are equal'
    
def main():
        user_number1 = int(input("Enter first number: "))
        user_number2 = int(input("Enter second number: "))
        print(compare(user_number1, user_number2))
main()

def determine_weightclass( weight ):
    if weight <= 115:
        print("feather")
    elif weight > 115 and weight < 135:
        print("medium")
    elif weight < 150 and weight >= 135:
        print("sebastian")
    elif weight >= 150 and weight <= 300:
        print("sebastian")



def main():

    w = int(input("Please enter a weight"))
    result = determine_weightclass(w)

main()

import random

def convert_to_day(number):
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    elif number == 7:
        return "Sunday"


def main():
    day_num = random.randint(1, 7) #don't forget to call the function
    result = convert_to_day(day_num)
    print(result)

main()
    
def determine_temp_icon( precipitation_chance, temp):

    icons = ['☁️', '🌧️', '❄️', '⛅']

    if precipitation_chance < 20 and temp > 0:
        return '☀️'
    

def main():

    rain_chance = 30
    temp_cel = 25

    icon = determine_temp_icon(rain_chance, temp_cel)

    print(f'{icon} : {temp_cel}°C with {rain_chance}% rain')


main()

def is_vowel( c ):
    if c  == 'aeiouAEIOU':
        return True
    else:
        return False



def main():
    char = input("Please enter a letter. ")
    result = is_vowel(char)
    print(f' {char} is a vowel: {result}')

main()




# printed based on validity of expression
print (4 < 7)
print (4 > 7)
print (True and True)
print (4 < 7 and 1 < 10)

print (True and False)
print (4 < 7 and 1 > 10)

print (True or False)
print (4 < 7 or 1 > 10)

print (not(False))

print(bool("hello"))
print(bool(""))
print(bool(100))
print(bool(0))

def is_divisible_by_3( n ):
    if n % 3 == 0:
        return True
    else:
        return False
    
def main():
    number = int(input("Enter a number: "))
    result = is_divisible_by_3(number)
    print(f'{number} is divisible by 3: {result}')
    print(result)
main()
    
def calculate_payroll(hours_worked, hourly_rate):
    if hours_worked <= 40:
        total_pay = hours_worked * hourly_rate
    else:
        overtime_hours = hours_worked - 40
        total_pay = (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5)
    return total_pay

def main():
    hours = int(input("Enter hours worked: "))
    rate = int(input("Enter hourly rate: "))
    result = calculate_payroll(hours, rate)
    print(f'Total payroll: ${result:.2f}')
    
main()

def calculate_total_price( price, coupon_code ): 
    discount = 0.4
    tax = 0.13
    if coupon_code == "Bonus" or coupon_code == "bonus40":
         return price * (1 - discount) * (1 + tax)
    else:
         return price * (1*tax)



def main():
    coupon = input("Please enter your coupon code: ")
    price = 239.99   #or generate a random value
    result = calculate_total_price(round(price, 2), coupon)
    print(result)
main()

# Under 18, must have a G1 permit.
# Between 18 and 70, must have a G permit.
# Over the age of 70, must have a G permit and updated yearly test.

def check_driving_eligibility( age ):
    if age < 18 :
        return "G1 permit."
    elif 18 <= age <= 70:
        return "G permit."
    elif age > 70:
        return "G permit and must update yearly test."
    else:
        return "Not eligible to drive."
def main():
    user_age = int(input("Enter your age: "))

    eligibility = check_driving_eligibility(user_age)
    print(eligibility)
main()

def determine_temp_icon( precipitation_chance, temp):

#'☁️', '🌧️', '❄️', '⛅'

    if precipitation_chance < 20 and temp > 0:
        return '☀️'
    elif 20 <= precipitation_chance < 60:
        return '⛅'
    elif precipitation_chance >= 60 and temp < 0:
        return '❄️'
    else:
        return '🌧️'

def main():

    rain_chance = random.randint(0, 100)
    temp_cel = random.randint(-20, 35)
    icon = determine_temp_icon(rain_chance, temp_cel)
    print(f'{icon} : {temp_cel}°C with {rain_chance}% rain')


main()

# Write a function called real_root_exist(a, b, c) that will determine if a quadratic equation has read or imaginary roots.
def real_root_exist(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        return "2 reals roots"
    elif discriminant == 0:
        return "1 real root"
    elif discriminant < 0:
        return "No real roots (imaginary roots)"
    
    else:
        return False
def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    result = real_root_exist(a, b, c)
    print(f'Real roots exist: {result}')
    
main()

print (4 < 7) #checks if 4 is less than 7
print (4 > 7) #checks if 4 is greater than 7
print (True and True) # prints true if both sides are true
print (4 < 7 and 1 < 10) # checks if 4 is less than 7 and 1 is less than 10

print (True and False) #
print (4 < 7 and 1 > 10)

print (True or False)
print (4 < 7 or 1 > 10)

print (not(False))

print(bool("hello"))
print(bool(""))
print(bool(100))
print(bool(0))
print("")


