import pygame
from pygame import Vector2
from scripts.engine import advancedDraw, moveLocal


class Bullet:
    # Holds a list of every bullet object and makes it possible to create more bullet instances.
    objs = []

    def __init__(self, x, y, image_path, init_angle, player_pos):
        # Sets up the sprite.
        self.sprite = pygame.image.load(image_path).convert()
        self.sprite.set_colorkey((0, 0, 0))

        # Creates the rect based on the sprite and positions it.
        self.rect = self.sprite.get_rect()
        self.rect.topleft = Vector2(x, y)

        # Stores the player position when the instance was created.
        self.playerPos = Vector2(player_pos)

        # The angle and the movespeed.
        self.angle = init_angle
        self.moveSpeed = 10

    # This is called once every cycle
    def update(self, surface, deltatime, targetFPS):

        # Automatically moves the bullet forward.
        moveLocal(self, deltatime, targetFPS, 1, 0)

        # Checks if bullet is far enough from the player
        self.farCheck()

        # Draws the instance and it's angle.
        advancedDraw(self, surface)

    def farCheck(self):

        # Gets current positon of bullet
        currentPosition = Vector2(self.rect.topleft)
        # Gets the distance between the bullet and the coord the player was at when it shot the bullet.
        distance = Vector2.distance_to(currentPosition, self.playerPos)

        # Deletes itself once the distance is great enough.
        if distance > 1000:
            Bullet.objs.remove(self)
