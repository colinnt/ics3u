import random
import time

game = True
gun = False
map = False
compass = False

def paths():
    global game, gun, map, compass
    print("You find yourself at a crossroads. Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()
    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice. Please try again.")
        paths()

def left_path():
    global map, compass
    print("You find a river. There is an abandoned boat and a bridge.")
    choice = input("Do you want to take the boat or cross the bridge? ").lower()
    if choice == 'boat':
        print("You row down the river and discover a village. You receive a map and a compass.")

        map = True
        compass = True
        escape()
        

        
    elif choice == 'bridge':
        print("You cross the bridge and find a cave")
    else:
        print("Invalid choice. Please try again.")
        left_path()
        

def right_path():
    global game, gun, map, compass
    print("You find a cave")
    choice = input("Do you want to enter the cave or walk around? ").lower()
    if choice == 'enter':
        cave()
    elif choice == 'walk around':
        walk_cave()
    else: 
        right_path()

def cave():
    global game, gun
    print("Inside the cave, you find a stick")
    outcomes = ["the stick snaps and you fall into a pit", "a giant bat comes flying and takes you away", "you wander around and find a flare gun"]
    outcome = random.choice(outcomes)
    print(outcome)
    if outcome == "the stick snaps and you fall into a pit":
        game = False
        print("Game Over")
    elif outcome == "a giant bat comes flying and takes you away":
        hitbat()
        nohit()
    elif outcome == "you wander around and find a flare gun":
        print("Would you like to shoot the flare gun?")
        shoot_flare()
        gun = True

def shoot_flare():
        if input().lower() == 'yes':
            print("The flare lights up the cave and nothing happens. You die of starvation.")
            game = False
            gun = False
            print("Game Over")
        else:
            print("You save the flare gun for later")
            left_path()

def walk_cave():
    global game, map, compass
    print("You walk around the cave and go deeper into the forest") 
    list = ["you get lost and die", "you find an abandoned vehicle and drive to a village", "you find a hole that brings you back to the cave"]
    randomoutcome = random.choice(list)
    print(randomoutcome)
    if randomoutcome == "you get lost and die":
        game = False
        print("Game Over")
    elif randomoutcome == "you find an abandoned vehicle and drive to a village":
        print("You receive a map and a compass")
        map = True
        compass = True
    elif randomoutcome == "you find a hole that brings you back to the cave":
        cave()

def hitbat():
    global game
    print("you hit the bat with the stick but it eats you")
    game = False
    print("Game Over")

def nohit():
    print("the bat carries you out of the cave")
    flying()

def flying():
    global game
    time_val = random.randint(0, 20)
    print("The bat takes you flying")
    if time_val < 10:
        print("You enjoy a scenic flight and safely land back on the ground.")
    elif 10 < time_val < 20:
        print("The bat flies into a storm and you fall to your death.")
        game = False
        print("Game Over")
        
def escape():
    global compass
    global map
    global game
    
    print("You have a compass and a map. Do you want to use the compass or the map to find your way?")
    if input().lower() == 'compass':
        print("You use the compass to find your way back to civilization.")

    elif input().lower() == 'map':
        print("You use the map but you get lost and die.")
        game = False
        print("Game Over")
def exit():
    if input.lower() == 'exit':
        print("Exiting the game.")
        global game
        game = False

        

def main():
    paths()



main()
