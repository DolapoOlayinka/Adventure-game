import time
import random

# choose a creature to defeat
creature_list = ["witch", "fairy", "dragon", "troll"]
creature = ""

# choose a weapon to fight with
weapon_list = ["axe", "dagger", "knife"]
weapon = ""


# delay printed messages
def pause_message(print_message):
    print(print_message)
    time.sleep(2)


# print user's choice
def valid_input(question, users_choice):
    while True:
        choice = input(question).lower()
        if choice in users_choice:
            return choice


# replay game
def restart_game():
    choice = valid_input("Would you like to play again? (y/n)\n", ["y", "n"])
    if choice == "y":
        global weapon
        pause_message("Excellent, restarting game...")
        weapon = ""
        play_game()
    else:
        end_game()


# message for game options
def game_options():
    pause_message("Enter 1 to knock on the door of the house.")
    pause_message("Enter 2 to peer into the cave.")
    pause_message("What would you like to do?")
    choose_an_option()


# to proceed to the house
def house():
    pause_message("You approach the door of the house.")
    pause_message(
        f"You are about to knock when the door"
        f" opens and out steps a {creature}."
    )
    pause_message(f"Eep! This is the {creature}'s house!\n")
    pause_message(f"The {creature} attacks you!")
    fight_or_run()


# to go to cave to change weapon
def cave():
    global weapon
    pause_message("You peer cautiously into the cave.")
    if weapon == "sword":
        pause_message("You've been here before, and "
                      "gotten all the good stuff.")
        pause_message("It's just an empty cave now")
    else:
        pause_message("It turns out to be only a small cave.")
        pause_message("Your eye catches a glint of metal behind a rock.")
        pause_message(f"You have found the magical sword of Ogoroth!")
        pause_message(
            f"You discard your silly old {weapon}"
            f" and take the sword with you."
        )
        weapon = "sword"
        pause_message("You walk back out to the field.")
    game_options()


# this executes when user selects the fight option
def fight():
    if weapon == "sword":
        pause_message(
            f"As the {creature} moves to attack, you"
            f" unsheath your new {weapon}."
        )
        pause_message(
            f"The sword of Ogoroth shines brightly in your"
            " hand as you brace yourself for the attack."
        )
        pause_message(
            f"But the {creature} takes one look at your"
            " shiny new toy and runs away!"
        )
        pause_message(
            f"You have rid the town of the {creature}." " You are victorious!"
        )
    else:
        pause_message(
            f"You feel a bit under-prepared for this,"
            f" with only having a tiny {weapon}. \n"
        )
        pause_message("You do your best...")
        pause_message(f"but your {weapon} is no match for the {creature}.")
        pause_message("You have been defeated! \n")
    restart_game()


# if the user selects the run option
def run():
    pause_message("You run back into the field. "
                  "Luckily, you don't seem to have been followed")
    game_options()


# pick an option between the house and the cave
def choose_an_option():
    choice = valid_input("Please enter 1 or 2.\n", ["1", "2"])
    if choice == "1":
        house()
    else:
        cave()


# pick an option to fight or to run
def fight_or_run():
    choice = valid_input("Would you like to (1) fight or (2) run away?\n",
                         ["1", "2"])
    if choice == "1":
        fight()
    else:
        run()


# finish the game
def end_game():
    print("Thanks for playing! See you next time.")


# adventure game intro message
def intro():
    pause_message(
        "You find yourself standing in an open field, "
        "filled with grass and yellow"
        " wildflowers."
    )
    pause_message(
        f"Rumor has it that a wicked {creature}"
        " is somewhere around here,"
        " and has been terrifying the nearby"
        " village."
    )
    pause_message("In front of you is a house")
    pause_message("To your right is a dark cave.")
    pause_message(f"In your hand you hold your"
                  f" trusty (but not very effective) {weapon}.\n")


# defining the adventure game
def play_game():
    global creature
    creature = random.choice(creature_list)
    global weapon
    weapon = random.choice(weapon_list)
    intro()
    game_options()


# play adventure game
play_game()
