

import time
import random

weapon = []
enemies_list = ["pirate", "wicked fairy", "Troll", "Gorgon"]
enemy = random.choice(enemies_list)


def print_delay(message):  # two second delay between messages
    print(message)
    time.sleep(2)


def print_delay2(message):  # 4 second delay between messages for effect
    print(message)
    time.sleep(4)


def intro():  # first messages seen at start of new game
    print_delay("You find yourself standing in an open field, filled with" +
                " grass and yellow wildflowers.")
    print_delay(f"Rumor has it that a {enemy}  is somewhere around here")
    print_delay("and has been terrifying the nearby village....")
    print_delay("In front of you is a house.")
    print_delay("To your right is a dark cave.")
    print_delay("In your hand you hold your trusty (but not very effective)" +
                "dagger.")


def cave():
    print_delay("You peer cautiously into the cave.")
    if "sword" in weapon:  # checks to see if sword was already collected
        print_delay("You've been here before, and gotten all the good" +
                    "stuff. It's just an empty cave now.")
        print_delay("You walk back out to the field.\n")
    else:
        print_delay("It turns out to be only a very small cave.")
        print_delay("Your eye catches a glint of metal behind a rock.")
        print_delay("You have found the magical Sword of Ogoroth!")
        print_delay("You discard your silly old dagger and take the sword" +
                    "with you")
        print_delay("You walk back out to the field.\n")
        weapon.append("sword")


def house_or_cave():
    print_delay("Enter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")
    print_delay("What would you like to do?")
    action = input("(Please enter 1 or 2.) ")
    if ("1") in action:
        house()
        encounter()
    elif ("2") in action:
        cave()
        house_or_cave()
    else:
        print_delay("please try again! enter either 1 or 2 as your response\n")
        house_or_cave()


def house():
    print_delay("You approach the door of the house.")
    print_delay(f"You are about to knock when the door opens and" +
                "out steps a {enemy} .")
    print_delay(f"Eep! This is the {enemy}'s house!")
    print_delay(f"the {enemy} attacks you!\n")


def encounter():
    fight_or_run = input("Would you like to (1) fight or (2) run away?  ")
    if ("1") in fight_or_run and ("sword") in weapon:
        armed()
    elif ("1") in fight_or_run:
        defeat()
    elif ("2") in fight_or_run:
        run()
    else:
        print_delay("please try again! enter either 1 or 2 as your response")
        encounter()


def new_game():
    replay = input("Would you like to play again? (y/n)  ")
    if ("y") in replay.lower():
        intro()
        house_or_cave()
    elif ("n") in replay.lower():
        print_delay("thanks for playing! Bye for now!")
        return
    else:
        print_delay("please try again. Enter y or n as your response")
        new_game()


def armed():
    print_delay(f"As the {enemy} moves to attack, you unsheath your" +
                " new sword.")
    print_delay("""The Sword of Ogoroth shines brightly in your hand as you
    brace yourself for the attack.
    But the troll takes one look at your shiny new toy and runs away!
    You have rid the town of the troll. You are victorious!""")
    weapon.clear()
    new_game()


def defeat():
    print_delay2("You do your best...")
    print_delay("but your dagger is no match for the gorgon.")
    print("You have been defeated!")
    new_game()


def run():
    print_delay("You run back into the field. Luckily, you don't seem to have")
    print("been followed.")
    house_or_cave()


def start_game():
    intro()
    house_or_cave()


start_game()
