# def convert_to_fah(c_temp):
#     return (c_temp * 9/5) + 32


# def main():
#     celcius = float(input("Please enter temperature in Celcius"))
#     fahrenheit = convert_to_fah(celcius)

#     print(f'Temp in Celcius: {celcius:.0f}')
#     print(f'Temp in Fahren: {fahrenheit:.0f}')

# main()

import math

# def calculate_tax( price ):
#     tax = price*0.13
#     total = price + tax
#     return total


# def main():
#     price = float(input("Enter price: "))
#     total_price = calculate_tax(price)
#     print(f'Total price with tax: ${total_price:.2f}')
# main()

# def area_circle( r ):
#     area = math.pi * r**2
#     return area

# def volume_sphere( r ):
#     volume = (4/3) * math.pi * r**3
#     return volume

# def main():
#     radius = float(input("Enter the radius: "))
#     print(f'Area of circle: {area_circle(radius):.2f}')
#     print(f'Volume of sphere: {volume_sphere(radius):.2f}')
    
# main()

name = input("Enter your name")

s = '*'*(len(name)+2) + '\n'
s += f'*{name}*\n'
s += '*'*(len(name)+2) + '\n'

print(s)
#Create a function that accepts the name as a parameter and returns the formatted string back to a main function to print.
def framed_name(name):
    s = '*'*(len(name)+2) + '\n'
    s += f'*{name}*\n'
    s += '*'*(len(name)+2) + '\n'
    return s



def center_word(word, width):
    total_spaces = width - len(word)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    return ' ' * left_spaces + word + ' ' * right_spaces


def main():
    result = center_word('PYTHON', 30)
    print(result)
    result = center_word('CODE', 30)
    print(result)

main()

import random

def phone_number(areacode, exchange, subnumber):
    return f'({areacode}) {exchange}-{subnumber}'
    
    



def main():
    a = random.randint(111, 999)
    e = random.randint(111, 999)
    s = random.randint(1000,9999)
    print(phone_number(a, e, s))

main()
def convert_days_hours(hours):
    days = hours // 24
    hours = hours % 24
    return days, hours


def main():
    total_hours = int(input("Enter total hours: "))
    days_left, hours_left = convert_days_hours(total_hours)
    print(f"Days: {days_left}, Hours: {hours_left}")


    days_left, hours_left = convert_days_hours(total_hours)

main()




def main():
    days = random.randint(0, 10)
    hours = random.randint(0, 23)
    print(f"Randomly generated time: {days} days, {hours} hours")
    total_hours = days * 24 + hours
    days_left, hours_left = convert_days_hours(total_hours)
    print(f"Converted back to days and hours: {days_left} days, {hours_left} hours")

main()

#Write a function called is_even(number) that returns True if the number is even and False if the number is not.
#*** This question requires a conditional which is our next lesson. If you can finish it, awesome!
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():

    user_num = int(input("Please enter a number"))

    if is_even(user_num) == True:
        print(f'{user_num} is even')

    else:
        print(f'{user_num} is odd')

main()

