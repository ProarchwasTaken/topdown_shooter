import pygame
from scripts.engine import angleRollOver, moveLocal, advancedDraw
from scripts.bullet import Bullet


# This holds the player class.
class Player:
    ammo = 15

    def __init__(self, x, y, image, bullet_path, prev_time):
        # Sets up the sprite
        self.sprite = pygame.image.load(image).convert()
        # Sets the transparent color of the image, which will be black.
        self.sprite.set_colorkey((0, 0, 0))
        # Gets the dimensions of the sprite.
        self.rect = self.sprite.get_rect()
        # Sets the player's starting position as Vector2
        self.rect.topleft = pygame.math.Vector2(x, y)
        # The player's angle.
        self.angle = 0
        # How fast the player rotates
        self.rotoSpeed = 5
        # How fast the player will move
        self.moveSpeed = 3

        # Saves the file path for bullet sprite.
        self.bulPath = bullet_path
        # Hands the delay between shooting bullets
        self.lastShot = prev_time
        self.shootDelay = 0.5

    # This is run once every cycle.
    def update(self, surface, deltatime, targetfps, cur_time):
        # Handles player input.
        self.input(deltatime, targetfps, cur_time)

        # Makes sure the player's angle doesn't go over 360 or under 0
        angleRollOver(self)

        # Draws the player on the screen.
        advancedDraw(self, surface)

    # This checks if a key is pressed and executes code as long as said key is pressed.
    def input(self, dt, tFPS, curtime):
        keys = pygame.key.get_pressed()

        # Rotates the player clockwise or counterclock wise.
        if keys[pygame.K_LEFT]:
            self.angle -= self.rotoSpeed * dt * tFPS
        if keys[pygame.K_RIGHT]:
            self.angle += self.rotoSpeed * dt * tFPS

        # This moves player locally.
        if keys[pygame.K_w]:
            moveLocal(self, dt, tFPS, 1, 0)
        if keys[pygame.K_s]:
            moveLocal(self, dt, tFPS, -1, 0)
        if keys[pygame.K_a]:
            moveLocal(self, dt, tFPS, 0, -1)
        if keys[pygame.K_d]:
            moveLocal(self, dt, tFPS, 0, 1)

        # Shoot bullets from player's position and angle
        if keys[pygame.K_SPACE]:
            self.shootBullet(curtime)

    # Handles creating Bullet instances as long as the Player still has ammo.
    def shootBullet(self, curtime):
        if Player.ammo > 0:
            if curtime - self.lastShot >= self.shootDelay:
                # Creates bullet instance at the player's position and angle
                Bullet.objs.append(Bullet(self.rect.x, self.rect.y, image_path=self.bulPath, init_angle=self.angle,
                                          player_pos=self.rect.topleft
                                          ))
                # Decrements the player's ammo by 1
                Player.ammo -= 1

                self.lastShot = curtime
