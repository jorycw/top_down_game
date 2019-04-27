import pygame
import player as plyr

def main():
     

    pygame.init()

    logo = pygame.image.load("resources/smile.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((1280,720))
    screen.fill([255, 255, 255])     


    player = plyr.Player(50, 50)

    pygame.display.flip()
     
    while True:
        screen.fill([255, 255, 255])
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        player.update(screen)

        clock.tick(60)

            # if event.type == pygame.KEYDOWN:
            #     player.move(event)
     

if __name__=="__main__":
    main()