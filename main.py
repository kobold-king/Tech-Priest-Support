from ascii_art import mechanicus, portrait
import time

# Bootup Sequence to feel like this is a old slow program
def startup_rp():
    loading = """
    +-----------------------------------------------+
    |      Loading Mechanicus Support Software      |
    +-----------------------------------------------+
    """
    centered_loading = loading.center(40)
    print(centered_loading)
    time.sleep(1)

    my_string = "..........."
    for char in my_string:
        print(char, end='', flush=True)
        time.sleep(0.3)

    # Mechanicus ascii art
    print(mechanicus.center(40))
    time.sleep(2)

    loaded = """
    +-----------------------------------------------+
    |                 System Loaded                 |
    |                  Initiating                   |
    +-----------------------------------------------+
    """
    loaded_lines = loaded.splitlines()
    for line in loaded_lines:
        print(line.center(40))

    print(portrait, end=' ')
    print("Blessings of the Omnissiah upon thee.")

def main():
    #
    startup_rp()

    time.sleep(2)
    choice = ("""
            Select a catoagory of your querey.
    __________________________________________________
    | Consumer | Commercial/ Industrial | Specalized |
    __________________________________________________
    """)
    user_input = input(f"{choice.center(40)}\n")
    if user_input == "Consumer" or "consumer":
        response = f"You said: '{user_input}' — that's interesting!"
        print(response)



main()
