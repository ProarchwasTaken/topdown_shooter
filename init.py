import pygame, time
from scripts.essentials import colors, loadDirectories
from scripts.player import Player
from scripts.bullet import Bullet
from scripts.gui import AmmoGUI
running = bool
'''=====================================================================================================================
This program was writen as learning exerise, and so I could use this program for future reference.
This features: Direction strafe movement, object rotation, shooting projectiles with limited ammo, usage of Vector2
and adding an proper gui.
========================================================================================================================
You are free to use this program as a reference for future projects, that basically how I'm gonna use this program
or from now on
========================================================================================================================
Excluding this long docstring, the entire program holds a total of about 330 lines. Yes that includes blank spaces 
and comments because I'm too lazy at counting and I don't think pycharm has a feature for counting how many useful 
lines of code there are.
=======================================================================================================================
 Controls:
    Press the WASD keys to move, the direction you move is based on your current angle.
    Press the Left and Right arrow keys to turn.
    Press the Space key to shoot
====================================================================================================================='''
# This is the main file, run this first.
if __name__ == '__main__':
    running = True
# I'm going to try

FILEDIR = loadDirectories()  # Gets the file paths to all sprites

# Sets up the window.
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Sets up the clock and window timer
CLOCK = pygame.time.Clock()
PREV_TIME = time.time()
# The maximum FPS and the FPS the game is meant to be played at.
FPS = 60
TARGET_FPS = 60

# Initilizes player instance.
player = Player(  # This is formated this way to make it more readable
    x=400, y=300,
    image=FILEDIR["player"],
    bullet_path=FILEDIR["bullet"],
    prev_time=PREV_TIME
)
# Initilizes the Ammo GUI
ammo_GUI = AmmoGUI(25, 25, FILEDIR["ammo"])

# This is for a pretty neat custom icon. Just for fun.
pygame.display.set_icon(player.sprite)

# Main game loop
while running:
    # This updates the clock
    CLOCK.tick(FPS)
    # Declares current time.
    CURRENT_TIME = time.time()
    # Sets up delta time value
    DELTA_TIME = CURRENT_TIME - PREV_TIME
    # Sets previous time to current time.
    PREV_TIME = CURRENT_TIME

    # Updates window caption.
    pygame.display.set_caption(f"Topdown Shooter | FPS: {int(CLOCK.get_fps())}")

    # Refreshes the screen
    SCREEN.fill(colors["black"])

    # Checks each game event.
    for event in pygame.event.get():
        # Allows the player to quit the game.
        if event.type == pygame.QUIT:
            running = False

    # Updates all bullet instances
    for obj in Bullet.objs:
        obj.update(surface=SCREEN, deltatime=DELTA_TIME, targetFPS=TARGET_FPS)
    # Updates player instance
    player.update(surface=SCREEN, deltatime=DELTA_TIME, targetfps=TARGET_FPS, cur_time=CURRENT_TIME)

    # Draws the GUI
    ammo_GUI.draw(SCREEN)

    # Updates the screen.
    pygame.display.flip()
