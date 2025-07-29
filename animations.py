from ascii_art import loading_1, loading_2, loading_3, loading_4
from terminaltexteffects.effects.effect_waves import Waves
from terminaltexteffects.effects.effect_binarypath import BinaryPath
import time



def wave_animation(word):
    # Create a Waves effect instance with the given word
    effect = Waves(word)
    # Use the effect's terminal output context
    with effect.terminal_output() as terminal:
        # Print each frame of the animation
        for frame in effect:
            terminal.print(frame)

def binarypath_animation(word):
    # Create a Waves effect instance with the given word
    effect = BinaryPath(word)
    # Use the effect's terminal output context
    with effect.terminal_output() as terminal:
        # Print each frame of the animation
        for frame in effect:
            terminal.print(frame)

def loading_anim():
    count = 0
    while count < 3:
        print("++loading++", end='\r', flush=True)
        time.sleep(1)
        print("--loading--", end='\r', flush=True)
        time.sleep(1)
        print("++loading++", end='\r', flush=True)
        time.sleep(1)
        print("--loading--", end='\r', flush=True)
        time.sleep(1)
        count += 1
