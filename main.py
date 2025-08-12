from ascii_art import mechanicus, portrait
import time
from animations import binarypath_animation, cenetered_input, line_print
from pip._vendor.rich import print
from choice_tree import choice_response, print_centered
import shutil


# Bootup Sequence to feel like this is a old slow program
def startup_rp():
    intro = """
    +-----------------------------------------------+
    |   +++Loading Mechanicus Support Software+++   |
    +-----------------------------------------------+
    """

    line_print(intro)

    # Mechanicus ascii art
    binarypath_animation(mechanicus)

    time.sleep(2)

    loaded = """
    +-----------------------------------------------+
    |                 System Loaded                 |
    |                  Initiating                   |
    +-----------------------------------------------+
    """
    line_print(loaded)

    line_print(portrait + "Blessings of the Omnissiah upon thee.")

def choice_one():
    choice = """
    Select a catoagory of your querey.
    +------------------------------------------------+
    | Consumer | Commercial/Industrial | Specialized |
    +------------------------------------------------+
    """

    line_print(choice)

    terminal_width = shutil.get_terminal_size().columns

    user_input = ""  # Initialize user_input to an empty string

    while not user_input:  # Loop continues as long as user_input is empty
        user_input = input("Select your catagory, varlet: ".rjust(terminal_width//2))
        if not user_input:  # Check if input is still empty after prompt
            print_centered("Your inability to follow instructions is disappointing yet not unexpected. Try again.")
    time.sleep(2)
    choice_response(user_input)


def main():
    startup_rp()
    time.sleep(2)

    restart_program = True
    while restart_program:
        choice_one()
        user_input = input(cenetered_input("Is there more you require of me, varlet? (yes/no): ").lower())
        if user_input == "yes" or user_input == "y":

            restart_program = True  # Or just continue as it's already True
            line_print("\nRestarting...\n")
        else:
            restart_program = False
            line_print("+++End Transmission+++")



if __name__ == "__main__":
    main()
