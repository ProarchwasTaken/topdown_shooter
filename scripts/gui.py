import pygame
from scripts.essentials import fonts, colors
from scripts.player import Player
basic_font = fonts["basic"]


# Used to display how much ammo the player has
class AmmoGUI:
    def __init__(self, x, y, image):
        # Image setup
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey((0, 0, 0))

        # Rect Setup
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y

        # Sets the text position
        textx = self.rect.x + 60
        texty = self.rect.y + 2

        # Text Setup
        self.text = basic_font.render("10", True, colors["white"])
        self.textRect = self.text.get_rect()
        self.textRect.topleft = textx, texty

    def draw(self, surface):
        # Updates the text of the player's ammo count
        self.text = basic_font.render(str(Player.ammo), True, colors["white"])

        # Draws the text and gui on screen.
        surface.blit(self.image, self.rect)
        surface.blit(self.text, self.textRect)

