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
    print_centered("""
    +-----------------------------------------------+
    |      Loading Mechanicus Support Software      |
    +-----------------------------------------------+
    """)
    time.sleep(1)

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
    loaded_lines = loaded.splitlines()
    for line in loaded_lines:
        print_centered(line)

    print_centered(portrait + "Blessings of the Omnissiah upon thee.")


def main():
    startup_rp()

    time.sleep(2)
    choice = ("""
            Select a catoagory of your querey.
    __________________________________________________
    | Consumer | Commercial/Industrial | Specialized |
    __________________________________________________
    """)
    print_centered(choice)

    user_input = ""  # Initialize user_input to an empty string

    while not user_input:  # Loop continues as long as user_input is empty
        user_input = input("Select your catagory, varlet: ")
        if not user_input:  # Check if input is still empty after prompt
            print_centered("Your inability to follow instructions is disappointing yet not unexpected. Try again.")
    time.sleep(2)
    choice_response(user_input)



main()
