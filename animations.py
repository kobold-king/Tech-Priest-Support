from terminaltexteffects.effects.effect_binarypath import BinaryPath
import time
import shutil
import os
import sys

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

def loading(duration=3):
    width = shutil.get_terminal_size().columns
    spinner_chars = ['|', '/', '-', '\\']
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in spinner_chars:
            centered = (f"\033[32m{char} LOADING {char}\033[0m").center(width)
            sys.stdout.write("\r" + centered)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 20 + "\r")  # Overwrite with spaces to clear the line # Clear the line and add newline
    sys.stdout.flush()

def left_cen_print(text):
    terminal_width = shutil.get_terminal_size().columns // 4
    split_text = text.splitlines()
    for line in split_text:
        colored = " " * terminal_width + (f"\033[32m{line}\033[0m")
        print(colored)
        time.sleep(.5)

def user_choice():
    return input
