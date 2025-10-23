import time
import random
import cv2
import numpy as np

EMOJI_WINDOW_SIZE = (720, 450)


try:
    hands_up_emoji = cv2.imread("air.jpg")

    if hands_up_emoji is None:
        raise FileNotFoundError("air.jpg not found")

    hands_up_emoji = cv2.resize(hands_up_emoji, EMOJI_WINDOW_SIZE)

    print("Emoji images loaded successfully!\n")

except Exception as e:
    print(" Error loading emojis:", e)
    print("- air.jpg")


game = True
gun = False
map = False
compass = False
stick = False


def paths():
    global game, gun, map, compass
    print("You find yourself at a crossroads. Do you want to go left or right?")
    choice = input("Type 'left' or 'right': ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice.")
        paths()


def left_path():
    global gun
    events = [
        "You find a flare gun on the ground. You save it for later.",
        "You spot footprints near the mud. Someone has been here recently.",
        "A small animal darts across your path and disappears into the bushes.",
    ]
    print(random.choice(events))
    gun = True
    print("You find a river. There is an abandoned boat and a bridge.")
    choice = input("Do you want to take the boat or cross the bridge? ").lower()

    if choice == "boat":
        boat_path()
    elif choice == "bridge":
        bridge_path()
    else:
        print("Invalid choice.")
        left_path()


def right_path():
    discoveries = [
        "You find a broken compass on the ground.",
        "You find a note: 'Don’t go into the cave.'",
        "You find nothing but silence and wind.",
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
        "A thick fog rolls in—you can’t see the shore.",
    ]
    print(random.choice(outcomes))
    print("Do you want to jump out or stay in?")
    choice = input("> ").lower()

    if choice == "jump out":
        print("You swim to shore, exhausted but alive.")
        paths()
    elif choice == "stay in":
        print("You crash into rocks but manage to crawl out of the water.")
        village()
    else:
        print("You hesitate and the river takes you downstream.")
        paths()


def bridge_path():
    print("You cross the bridge and find a cave.")
    dangers = [
        "You hear growling from inside.",
        "You see glowing crystals through the darkness.",
        "A cold wind blows from deep within.",
    ]
    print(random.choice(dangers))
    print("Do you want to enter or go back?")
    choice = input("> ").lower()

    if choice == "enter":
        cave_path()
    elif choice == "go back":
        left_path()
    else:
        print("Invalid choice.")
        bridge_path()


def cave_path():
    global stick
    print("You walk into the cave. You hear dripping water echoing in the dark.")
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


def flying():
    global game
    time_val = random.randint(0, 20)
    print("The bat takes you flying")
    if time_val < 10:
        print("You enjoy a scenic flight and safely land back on the ground.")
        village()
    elif 10 < time_val < 20:
        print("The bat flies into a storm and you fall to your death.")
        game = False
        print("Game Over")


def explore_deeper():
    global stick
    print("You venture deeper into the cave and discover a giant bat.")
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


def village():
    global game, map, compass
    print("You arrive at a small village.")
    choice = input("Do you want to use the map or compass? ").lower()
    if choice == "map":
        print("You use the map but you can't find your way out.")
        game = False
        print("Game Over")
    elif choice == "compass":
        print("You use the compass to navigate safely out of the area.")
        game = False
        print("You Win!")
    else:
        print("Invalid choice.")
        village()
def show_emoji(emoji):
    cv2.imshow(emoji, emoji)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()


def main():
    global game
    paths()


main()
