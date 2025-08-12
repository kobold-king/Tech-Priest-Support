from terminaltexteffects.effects.effect_binarypath import BinaryPath
import time
import shutil
import os

def binarypath_animation(word):
    terminal_width = shutil.get_terminal_size().columns

    centered_lines = []

    for line in word.splitlines():
        centered_line = line.center(terminal_width)
        centered_lines.append(centered_line)

    centered_text_value = "\n".join(centered_lines)
    # Create a Waves effect instance with the given word
    effect = BinaryPath(centered_text_value)
    effect.terminal_config.canvas_width = terminal_width
    # Use the effect's terminal output context
    with effect.terminal_output() as terminal:
        # Print each frame of the animation
        for frame in effect:
            terminal.print(frame.center(terminal_width))


def print_centered(text):
    """Prints the given text centered in the terminal."""
    colored = (f"\033[32m{text}\033[0m")
    terminal_width = shutil.get_terminal_size().columns
    print(colored.center(terminal_width))

def line_print(text):
    split_text = text.splitlines()
    for line in split_text:
        print_centered(line)
        time.sleep(.5)

def cenetered_input(prompt):
    # Get terminal width for dynamic centering
    terminal_width = os.get_terminal_size().columns

    prompt_text = (f"\033[32m{prompt}\033[0m")
    centered_prompt = prompt_text.center(terminal_width)
    return centered_prompt
