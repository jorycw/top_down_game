import pygame

SPEED = 4

class Player:

    def __init__(self, x, y):
        self.image = pygame.image.load("resources/player.png")
        self.x = x
        self.y = y

    def detect_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.x -= SPEED
        if keys_pressed[pygame.K_RIGHT]:
            self.x += SPEED
        if keys_pressed[pygame.K_UP]:
            self.y -= SPEED
        if keys_pressed[pygame.K_DOWN]:
            self.y += SPEED

    def detect_click(self):
        not_done = True

    def update(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


def main():
     

    pygame.init()

    logo = pygame.image.load("resources/smile.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((1280,720))
    screen.fill([255, 255, 255])     


    player = Player(50, 50)

    pygame.display.flip()
     
    while True:
        screen.fill([255, 255, 255])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                break

        player.detect_movement()
        player.update(screen)

        clock.tick(60)

            # if event.type == pygame.KEYDOWN:
            #     player.move(event)

     


     

if __name__=="__main__":
    main()