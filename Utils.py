import os
import pygame
from Colours import Colours
from Constants import Constants

class Utils:
    @staticmethod
    def LoadImage(imageName : str, width: int, heigth : int):
        player_img = pygame.image.load(os.path.join(Constants.RECOURCES_PATH, imageName)).convert()
        player_img = pygame.transform.scale(player_img, (heigth, width))
        return player_img
