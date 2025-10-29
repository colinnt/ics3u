import time
import random

game = True
gun = False
map = False
compass = False
stick = False
health = 100
energy = 100
luck = random.randint(1, 10)  
discoveries_made = 0
danger_level = 0
mood = "neutral"  

def paths():
    global game, gun, map, compass, health, energy, mood, danger_level, discoveries_made
    

    print("\nYou find yourself at a crossroads...")
    time.sleep(1.5)
    

    atmosphere = [
        "The wind howls through the trees.",
        "Birds chirp in the distance.",
        "Clouds drift slowly overhead.",
        "A distant thunder rumbles.",
        "Leaves rustle in the breeze."
    ]
    print(random.choice(atmosphere))
    time.sleep(1)
    
    print("Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()

    if choice == 'left':
        left_path()
    elif choice == 'right':
        right_path()
    else:
        print("Invalid choice.")
        time.sleep(0.5)
        paths()

def left_path():
    global gun, health, energy, mood, discoveries_made, luck
    
    print("You choose the left path...")
    time.sleep(0.67)
    

    events = [
        "You find a flare gun on the ground. You save it for later.",
        "You spot footprints near the mud. Someone has been here recently.",
        "A small animal darts across your path and disappears into the bushes.",
    ]
    

    if luck >= 7:
        events.append("You find a healing herb that restores some energy!")
        events.append("You discover a hidden cache of supplies!")
    
    event = random.choice(events)
    print(event)
    discoveries_made += 1
    

    if event == "You find a healing herb that restores health!":
        energy += 20
        print(f"Your energy increases! (Energy: {energy})")
    elif event == "You discover a hidden cache of medical equipment!":
        health += 15
        print(f"Your health improves! (Health: {health})")
    
    time.sleep(0.67)
    
    gun = True
    print("You find a river. There is an abandoned boat and a bridge.")
    time.sleep(1)

    river_descriptions = [
        "The water flows downstream.",
        "The river looks calm but deep.",
        "Mist rises from the cold water.",
        "You can hear the sound of rushing water."
    ]
    print(random.choice(river_descriptions))
    time.sleep(1)
    
    choice = input("Do you want to take the boat or cross the bridge? ").lower()

    if choice == 'boat':
        boat_path()
    elif choice == 'bridge':
        bridge_path()
    else:
        print("Invalid choice.")
        time.sleep(0.5)
        left_path()

def right_path():
    global compass, map, health, energy, mood, discoveries_made, danger_level, luck
    
    print("You choose the right path...")
    time.sleep(1)
    

    print("The path grows darker as you walk...")
    time.sleep(1.5)
    
    discoveries = [
        "You find a broken compass on the ground.",
        "You find a note: 'Don't go into the cave.'",
        "You find nothing but silence and wind.",
        "You discover an old map fragment.",
        "You find strange markings on a tree."
    ]

    if luck >= 8:
        discoveries.append("You find a working compass!")
        discoveries.append("You discover a detailed map!")
    
    event = random.choice(discoveries)
    print(event)
    discoveries_made += 1
    

    if event == "You find a working compass!":
        compass = True
        print("You now have a working compass!")
    elif event == "You discover a detailed map!":
        map = True
        print("You now have a map!")
    
    time.sleep(1.5)
    
    if event == "You find a note: 'Don't go into the cave.'":
        mood = "scared"
        print("The warning makes you feel uneasy...")
        time.sleep(1)
        note()
    else:
        paths()

def note():
    global mood, danger_level
    
    print("The ominous warning echoes in your mind...")
    time.sleep(1.5)
    print("Do you still want to enter the cave? (yes/no)")
    choice = input("> ").lower()
    
    if choice == 'yes':
        mood = "confident"
        danger_level += 1
        print("You steel yourself and prepare for danger...")
        time.sleep(1)
        cave_path()
    elif choice == 'no':
        mood = "scared"
        print("You decide to heed the warning and turn back...")
        time.sleep(1)
        paths()
    else:
        print("Invalid choice.")
        time.sleep(0.5)
        note()

def boat_path():
    global health, energy, mood, danger_level, luck
    
    print("You take the boat and drift down the river...")
    time.sleep(2)
    

    journey_events = [
        "The current speeds up—you see rapids ahead!",
        "You see a waterfall in the distance!",
        "A thick fog rolls in—you can't see the shore.",
        "The boat starts to leak water.",
        "You hear strange sounds from the riverbank."
    ]
    

    if luck >= 6:
        journey_events.append("The river is calm and peaceful.")
        journey_events.append("You spot a safe landing spot ahead.")
    
    event = random.choice(journey_events)
    print(event)
    time.sleep(1.5)
    

    if event == "The current speeds up—you see rapids ahead!" or event == "You see a waterfall in the distance!":
        danger_level += 1
        energy -= 10
    elif event == "The river is calm and peaceful.":
        energy += 5
        mood = "confident"
    
    print("Do you want to jump out or stay in?")
    pick = input("> ").lower()

    if pick == "jump out":
        health -= 15
        energy -= 20
        print("You swim to shore, exhausted but alive.")
        print(f"Health: {health}, Energy: {energy}")
        time.sleep(1)
        paths()
        return
    elif pick == "stay in":
        if luck >= 5:
            print("You crash into rocks but manage to crawl out of the water.")
            health -= 10
            print(f"Health: {health}")
            time.sleep(1)
            village()
        else:
            print("The boat crashes and you're badly injured.")
            health -= 25
            print(f"Health: {health}")
            time.sleep(1)
            village()
        return
    else:
        print("You hesitate and the river takes you downstream.")
        time.sleep(1)
        paths()
        return


def bridge_path():
    global mood, danger_level, energy
    
    print("You cross the bridge and find a cave.")
    time.sleep(1)
    

    dangers = [
        "You hear growling from inside.",
        "You see glowing crystals through the darkness.",
        "A cold wind blows from deep within.",
        "Strange shadows dance on the walls.",
        "You hear dripping water echoing ominously."
    ]
    
    danger_description = random.choice(dangers)
    print(danger_description)
    time.sleep(1.5)
    

    if danger_description == "You hear growling from inside.":
        mood = "scared"
        danger_level += 1
    elif danger_description == "You see glowing crystals through the darkness.":
        mood = "confident"
        energy += 5
    
    print("Do you want to enter or go back?")
    choice = input("> ").lower()

    if choice == 'enter':
        cave_path()
    elif choice == 'go back':
        print("You retreat back across the bridge...")
        time.sleep(1)
        left_path()
    else:
        print("Invalid choice.")
        time.sleep(0.5)
        bridge_path()
def village():
    global game, map, compass
    print("You arrive at a small village.")
    choice = input("Do you want to use the map or compass? ").lower()
    if choice == "map":
        print("You use the map but you can't find your way out.")
        game = False
        print("Game Over")
    elif choice == "compass":
        print("You use the compass to find your way out of the area.")
        game = False
        print("You Win!😤")
    else:
        print("Invalid choice.")
        village()
def flying():
    global game
    time_val = random.randint(0, 20)
    print("The bat takes you flying")
    if time_val < 10:
        print("You enjoy a scenic flight and land back on the ground.")
        village()
    elif 10 < time_val < 20:
        print("The bat flies into a storm and you fall to your death.")
        game = False
        print("Game Over")

def cave_path():
    global stick
    print("You walk into the cave. You hear water dripping in the dark.")
    findings = [
        "You find a skeleton holding a key.",
        "You find a small chest, but it’s locked.",
        "You find strange carvings on the walls.",
    ]
    print(random.choice(findings))
    print("Do you want to explore deeper or leave? (explore deeper/leave)")
    choice = input("> ").lower()
    if choice == "explore deeper":
        print("You find a hidden tunnel leading somewhere new with a stick")
        stick = True
        explore_deeper()

    elif choice == "leave":
        paths()
    else:
        print("You stand still, unsure.")
        cave_path()

def explore_deeper():
    global stick
    print("You go deeper into the cave and discover a giant bat.")
    print("Do you want to fight it with your stick?")
    choice = input("> ").lower()
    if choice == "yes" and stick == True:
        print("You bravely fight the bat with your stick and emerge victorious!")
        flying()

    elif choice == "yes" and stick == False:
        print(
            "You try to fight the bat, but without a weapon, you are quickly overwhelmed."
        )
        print("You manage to escape the cave, shaken but alive.")
        paths()
    elif choice == "no":
        print("You decide to make friends with the bat. It takes you flying!")
        flying()

    
    paths()

paths()