import pygame
pygame.init()

Width, Height = 400,500
pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Addig image in pygame")

backround_image = pygame.transform.scale(pygame.image.load(background.jpeg().convert(),(Width,Height)))