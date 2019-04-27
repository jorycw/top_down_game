import pygame
import player as plyr
import projectile
import obj


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
     
    projectiles = [] 

    while True:
        screen.fill([255, 255, 255])
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 1 - left, 2 - middle, 3 - right, 4 - scroll up, 5 - scroll down
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                proj = player.get_projectile(event)
                if proj != None:
                    projectiles.append(proj)

        rock = obj.Object(80, 20, "resources/block.png")

        player.update(screen)

        for proj in projectiles:
            proj.update(screen)

        pygame.display.flip()
        clock.tick(60)
     

if __name__=="__main__":
    main()