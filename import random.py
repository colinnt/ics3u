import random
# #Generate a random integer in a user defined range.
# #Ask the user for a low & high value.
# #Use those values to choose a random integer in that range.
# low = int(input("Enter a low value"))
# high = int(input("Enter a high value"))
# print(random.randint(low, high))

# #3 random integers between 1000 and 2000 which are divisible by 50
# for i in range(3):
#     print(random.randrange(1000, 2001, 50))
    
#     #Generate a random password and print to the REPL (shell).
# #Password should be in the form
# n1 = random.randint(0,9)
# n2 = random.choice('abcdefghijklmnopqrstuvwxyz')
# n3 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# n4 = random.randint(80,89)
# n5 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# print(f"{n1}{n2}{n3}{n4}{n5}")

# #Generate a randomized symmetrical drawing in the Rorschach inkblot style


# b_dot = '⚫'
# w_dot = '⚪'

# for i in range(20):
#     line = ''
#     for j in range(20):
#         if random.randint(0,1) == 1:
#             line += w_dot
        
#         else:
#             line += '  '
#     print(line + line[::-1])
    
    #To force the probability that one item gets chosen more than another item set the choices to choose from to reflect that probability.
#20% chance to choose the colour "red"?  Make 20% of the choices red.
# Create a list of words.
# 10% chance to choose word "hello"
# 20% chance to choose word "salut"
# 10% chance to choose word "hola"
# 30% chance to choose word "ni hao"
# 30% chance to choose word "ahlan"
words = ['hello'] * 10 + ['salut'] * 20 + ['hola'] * 10 + ['ni hao'] * 30 + ['ahlan'] * 30
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))
print(random.choice(words))



            



# Generate a grid with random treasure placed.
ground = '🟫'
treasure = '💎'

for i in range(5):
    treasure_pos = random.randint(0, 4)


    row = ground * treasure_pos + treasure + ground * (5 - treasure_pos - 1)
    print(row)
    
    

