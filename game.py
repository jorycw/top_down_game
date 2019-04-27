import pygame
import player as plyr
import projectile
from network import Network

def read_pos(s):
    if s == '' or s is None:
        s = '0,0'
    s = s.split(',')
    return int(s[0]), int(s[1])

def make_pos(t):
    return f'{t[0]},{t[1]}'

def main():
    pygame.init()

    n = Network()
    start_pos = read_pos(n.get_pos())

    logo = pygame.image.load("resources/smile.png")
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    clock = pygame.time.Clock()
    screen.fill([255, 255, 255])     


    p1 = plyr.Player(start_pos[0], start_pos[1])
    p2 = plyr.Player(0, 0)


    pygame.display.flip()
     
    projectiles = [] 

    while True:
        screen.fill([255, 255, 255])
        p2_pos = read_pos(n.send(make_pos((p1.rect.x, p1.rect.y))))
        p2.rect.x = p2_pos[0]
        p2.rect.y = p2_pos[1]

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 1 - left, 2 - middle, 3 - right, 4 - scroll up, 5 - scroll down
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                proj = p1.get_projectile(event)
                if proj != None:
                    projectiles.append(proj)


        p1.update(screen)
        p2.update(screen)
        
        for proj in projectiles:
            proj.update(screen)

        pygame.display.flip()
        clock.tick(60)
     

if __name__=="__main__":
    main()