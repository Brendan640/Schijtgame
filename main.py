import pygame
import random

Initialiseer Pygame
pygame.init()
Stel de schermgrootte in
screen_width = 800
screen_height = 750

Maak het scherm
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Schijt Het Schijt")
pygame.display.set_caption("Cijfers tekenen")

Kleuren
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
black = (0, 0, 0)

font = pygame.font.Font(None, 36)
