from ascii_art import mechanicus, portrait
import time
from animations import binarypath_animation
from pip._vendor.rich import print
from choice_tree import choice_response, print_centered

# Default Text Color
GREEN = '\033[32m'  # ANSI code for green text
RESET = '\033[0m'   # ANSI code to reset text formatting

# Bootup Sequence to feel like this is a old slow program
def startup_rp():
    intro = """
    +-----------------------------------------------+
    |      Loading Mechanicus Support Software      |
    +-----------------------------------------------+
    """

    line_print(intro)

    my_string = "..........."
    for char in my_string:
        print(char, end='', flush=True)
        time.sleep(0.3)
    print("")

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

    print_centered(portrait + "Blessings of the Omnissiah upon thee.")


def line_print(text):
    split_text = text.splitlines()
    for line in split_text:
        print_centered(line)
        time.sleep(.5)


def main():
    startup_rp()

    time.sleep(2)
    choice = """
    Select a catoagory of your querey.
    __________________________________________________
    | Consumer | Commercial/Industrial | Specialized |
    __________________________________________________
    """

    line_print(choice)

    user_input = ""  # Initialize user_input to an empty string

    while not user_input:  # Loop continues as long as user_input is empty
        user_input = input("Select your catagory, varlet: ")
        if not user_input:  # Check if input is still empty after prompt
            print_centered("Your inability to follow instructions is disappointing yet not unexpected. Try again.")
    time.sleep(2)
    choice_response(user_input)





if __name__ == "__main__":
    restart_program = True
    while restart_program:
        main()
        user_input = input("Do you want to restart? (yes/no): ").lower()
        if user_input == "yes" or user_input == "y":
            restart_program = True  # Or just continue as it's already True
            print("\nRestarting...\n")
        else:
            restart_program = False
            print("Exiting program.")
