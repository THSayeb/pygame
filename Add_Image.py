import pygame
pygame.init()

Width, Height = 400,500
display_surface = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Addig image in pygame")

backround_image = pygame.transform.scale(pygame.image.load("background.jpeg").convert(),(Width,Height))

object_image = pygame.transform.scale(pygame.image.load("object.jpeg").convert_alpha(),(200,100))
object_rect = object_image.get_rect(center=(Width//2, Height//2-30))

test = pygame.font.Font(None,36).render("Hello World", True, pygame.Color("black"))
test_rect = test.get_rect(center=(Width//2,Height//2+110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        display_surface.blit(backround_image, (0,0))
        display_surface.blit(object_image, object_rect)
        display_surface.blit(test, test_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()