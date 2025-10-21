# Identify the statement below that evaluates to False   


# print(len('happy') == 5)
# print(True or False)
print(15 % 3 == 1)
# print(12 < 20)
print(15 - 15 % 3) #modulo first then subtraction

import random
# num = int(input("enter low number"))
# num2 = int(input("enter high number"))
# print(random.randint(num, num2))    


# num3 = random.randrange(0,9)
# letter = random.choice("abcdefghijklmnopqrstuvwxyz")
# letter1 = random.choice("abcdefghijklmnopqrstuvwxyz")
# num4 = random.randrange(80,90)
# letter2 = random.choice("abcdefghijklmnopqrstuvwxyz")
# print(f"{num3}{letter}{letter1}{num4}{letter2}")

# import math
# def calculate_hypotenuse(a, b):
#     c = math.sqrt(a**2 + b**2)
#     return c
# def main():
#     side1 = int(input("Enter length of side 1: "))
#     side2 = int(input("Enter length of side 2: "))
#     hypotenuse = calculate_hypotenuse(side1, side2)
#     print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
# main()

# radius = 5

# volume = 4/3 * math.pi * (radius**3)
# print(f"{volume:.3f}")

# import math

# def area_circle( r ):
#     return math.pi * (r**2)

# def volume_sphere( r ):
#    return 4/3 * math.pi * (r**3)

# def main():
#     radius = float(input("enter radius"))
#     print(f"{area_circle(radius):.3f}")
    
#     print(f"{volume_sphere(radius):.3f}")

# main()

# import random

def phone():
    a = random.randint(111, 999)
    e = random.randint(111, 999)
    s = random.randint(1000,9999)
    print(f"({a}) {e}-{s}")



def main():
    phone()
main()

#205 - 265 lbs Heavyweight
# 185 - 205 lbs Light Heavyweight
# 170 - 185 lbs Middleweight
# 155 - 170 lbs Welterweight
# 145 - 155 lbs Lightweight

def weight_class(weight):
    if weight>= 205 and weight <= 265:
        return "heavyweight"
    elif weight >= 185 and weight < 205:
        return "light heavyweight"
    elif weight >= 170 and weight < 185:                
        return "middleweight"
    elif weight >= 155 and weight < 170:
        return "welterweight"
    elif weight >= 145 and weight < 155:
        return "lightweight"
    else:
        return "featherweight"
def main():
        w = int(input("Enter weight: "))
        print(weight_class(w))
main()  

# Why doesn't the armature of a DC motor stop when the split in the commutator ring allows no contact with the
# brushes?
# The inertia of the armature keeps it spinning until the split in the commutator ring makes contact with the brushes again.

def vowel():
    return "aeiouAEIOU"

def main():
    c = input("enter letter")
    if c in vowel():
        print("vowel")
    else:
        print("consonant")
        
main()



    

