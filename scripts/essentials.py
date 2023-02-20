import os
from pygame import font

# This file hold valuable variables and functions that's used by other files in the project.

# Initilizes the font side of pygame
# I had to do this for some reason.
font.init()

# Stores all the colors
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}
# Stores fonts
fonts = {
    "basic": font.Font(None, 32)
}


# When called, fetchs the exact file paths to external files.
def loadDirectories():
    # Gets the file path to init.py
    # Pretty cool trick I figured out. like if __name__ == "__main__", you can actually use __main__ for other purposes.
    FILE_DIR = os.path.dirname("__main__")

    # Saves the file to sprites
    sprite_directories = {
        "player": os.path.join(FILE_DIR, "sprites/player.png"),
        "bullet": os.path.join(FILE_DIR, "sprites/bullet.png"),
        "ammo": os.path.join(FILE_DIR, "sprites/ammo_gui.png")
    }
    # Returns sprite_directories to whatever that called the function.
    return sprite_directories

