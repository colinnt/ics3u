import time
import random
import sys


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
        print("Invalid choice.")
        paths()
def left_path():
    global gun
    events = [
        "You find a flare gun on the ground. You save it for later.",
        "You spot footprints near the mud. Someone has been here recently.",
        "A small animal darts across your path and disappears into the bushes."
    ]
    print(random.choice(events))
    gun = True
    print("You find a river. There is an abandoned boat and a bridge.")
    choice = input("Do you want to take the boat or cross the bridge? ").lower()

    if choice == 'boat':
        boat_path()
    elif choice == 'bridge':
        bridge_path()
    else:
        print("Invalid choice.")
        left_path()

def right_path():
    discoveries = [
        "You find a broken compass on the ground.",
        "You find a note: 'Don’t go into the cave.'",
        "You find nothing but silence and wind."
    ]
    print(random.choice(discoveries))
    time.sleep(1)
    print("You can head back to the crossroads.")
    paths()

def boat_path():
    print("You take the boat and drift down the river...")
    time.sleep(2)
    outcomes = [
        "The current speeds up—you see rapids ahead!",
        "You see a waterfall in the distance!",
        "A thick fog rolls in—you can’t see the shore."
    ]
    print(random.choice(outcomes))
    print("Do you want to jump out or stay in?")
    choice = input("> ").lower()

    if choice == 'jump out':
        print("You swim to shore, exhausted but alive.")
        paths()
    elif choice == 'stay in':
        print("You crash into rocks but manage to crawl out of the water.")
        paths()
    else:
        print("You hesitate and the river takes you downstream.")
        paths()

def bridge_path():
    print("You cross the bridge and find a cave.")
    dangers = [
        "You hear growling from inside.",
        "You see glowing crystals through the darkness.",
        "A cold wind blows from deep within."
    ]
    print(random.choice(dangers))
    print("Do you want to enter or go back?")
    choice = input("> ").lower()

    if choice == 'enter':
        cave_path()
    elif choice == 'go back':
        left_path()
    else:
        print("Invalid choice.")
        bridge_path()

def cave_path():
    print("You walk into the cave. You hear dripping water echoing in the dark.")
    findings = [
        "You find a skeleton holding a key.",
        "You find a small chest, but it’s locked.",
        "You find strange carvings on the walls."
    ]
    print(random.choice(findings))
    print("Do you want to explore deeper or leave?")
    choice = input("> ").lower()
 
    if choice == 'explore deeper':
        print("You find a hidden tunnel leading somewhere new...")
        paths()
    elif choice == 'leave':
        paths()
    else:
        print("You stand still, unsure.")
        cave_path()

paths()