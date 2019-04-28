import pygame
import player as plyr
import projectile
from network import Network
import game_state as g_s

def main():
    # pygame.init()

    n = Network()
    game_state = n.get_p()

    # logo = pygame.image.load("resources/smile.png")
    screen = pygame.display.set_mode((500, 500))
    # pygame.display.set_icon(logo)
    # pygame.display.set_caption("minimal program")

    clock = pygame.time.Clock()
     
    projectile = None 

    while True:
        clock.tick(60)

        game_state = n.send([game_state.get_p(), projectile])
        projectile = None


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 1 - left, 2 - middle, 3 - right, 4 - scroll up, 5 - scroll down
                proj = game_state.get_p().get_projectile(event)
                if proj != None:
                    projectile = proj


        game_state.get_p().update()

        screen.fill([255, 255, 255])
          
        print(len(game_state.players))
        for p_ in game_state.players:
            p_.draw(screen)

        for key in game_state.projectiles:
            for p_ in game_state.projectiles[key]:
                p_.draw(screen) #             p_.update()

        pygame.display.update()

     

if __name__=="__main__":
    main()