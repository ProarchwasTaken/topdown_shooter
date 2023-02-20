import pygame
from pygame import Vector2

# This file is holds the standard game features that is used by most of the other class
# I found this was a better way of not repeating code since most of these functions are used regularly.


# Draws the object and rotates it based on it's angle used for certain game elements.
def advancedDraw(obj, surface):
    # Creates a copy of the self.sprite and sets it rotation to self.angle
    sprite_copy = pygame.transform.rotate(obj.sprite, int(-obj.angle))

    # This gets the center position of sprite_copy
    centerX = obj.rect.x - int(sprite_copy.get_width() / 2)
    centerY = obj.rect.y - int(sprite_copy.get_height() / 2)
    # The code above is there to make sure that the player will be centered when rotating.

    # Draws the sprite copy
    surface.blit(sprite_copy, (centerX, centerY))


# Handles moving the player locally thanks to Vector2
def moveLocal(obj, deltatime, targetfps, directionX, directionY):
    # Depending on what value is given to directionX and DirectionY
    # It will dictate with direction the player will move locally.
    # 0 = Don't move | 1 = move forward | -1 = move backwards

    moveX = directionX
    moveY = directionY

    # Sets a movement velocity of player by moveX and moveY, rotating the Vector by self.angle,
    # and multiplying it by moveSpeed * deltatime
    velocityX = Vector2(moveX, 0).rotate(obj.angle) * obj.moveSpeed * deltatime * targetfps
    velocityY = Vector2(0, moveY).rotate(obj.angle) * obj.moveSpeed * deltatime * targetfps

    # Increases the player's x and y coord by velocity
    obj.rect.topleft += velocityX
    obj.rect.topleft += velocityY


# Makes sure the object's angle doesn't go over 360 or under 0
def angleRollOver(obj):
    # The math is quite simple to grasp
    if obj.angle > 360:
        # Sets the angle to angle minus 360
        obj.angle = obj.angle - 360

    # Prevents the angle from going into the negatives
    if obj.angle < 0:
        # 360 - angle that has be negated into a positive value
        obj.angle = 360 - (obj.angle * -1)
