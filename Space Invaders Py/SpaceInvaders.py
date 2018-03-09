import pygame, sys, random, time
from pygame.locals import *

# Set mixer defaults (frequency, size, channels, buffer
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

# Load in sound files
pygame.mixer.music.load('pacman_beginning.wav')
beep = pygame.mixer.Sound('beep.wav')
shoot = pygame.mixer.Sound('shoot.wav')

# Load fonts
fontOne = pygame.font.SysFont("arial", 50, True)

# Set caption at top of screen
pygame.display.set_caption("Space Invaders")

# This function will create a display Surface
screen = pygame.display.set_mode((1000,600))  

COLOUR = (255, 255, 255)

# Define colour as WHITE = (255, 255, 255)	

spaceship = pygame.image.load("Rocket.png")
enemy_image = pygame.image.load("Invader.png").convert_alpha() 
enemy_image.set_colorkey((255,255,255))


last_time_enemy_spawned = 0

clock = pygame.time.Clock()

score = 0
health = 100

class Enemies:

        # Give initial position
        # Move it downwards
        # Draw it!

        def __init__(self):
                self.x = random.randint(0,640)
                self.y = -40
                # ACCELERATION
                self.dy = 0
                self.dx = 0

        def move(self):
                self.dy += 0.005
                self.dx += random.choice((-1,1))*self.dy*0.05

                self.y += self.dy
                self.x += self.dx

        def bounce(self):
                if self.x < 0 or self.x > 640:
                        self.dx *= -1

        def draw(self):
                screen.blit(enemy_image, (self.x, self.y))

        def hit_by(self, missile):
                return pygame.Rect(self.x, self.y, 50, 50).collidepoint((missile.x, missile.y))




class Fighter:

        def __init__(self):
                self.x = 300
                self.y = 430

        def draw(self):
                screen.blit(spaceship, (self.x, self.y))

        def fire(self):
                missiles.append(Missile(self.x))
                shoot.play()

        def move(self):
                if pressed_keys[K_RIGHT] and self.x<600:
                        self.x += 5
                if pressed_keys[K_LEFT] and self.x>0 :
                        self.x -= 5
        def hit_by(self, enemies):
                return pygame.Rect(self.x, self.y, 50, 50).collidepoint((enemies.x, enemies.y))




class Missile:

        def __init__(self, x):
                self.x = x
                self.y = 430

        def draw(self):
                pygame.draw.line(screen, (255,0,0), (self.x,self.y), (self.x, self.y-5), 1) 

        def move(self):
                 self.y -= 10
                         


enemies = []
missiles = []

fighter = Fighter()


pygame.mixer.music.play(0)
while 1:
        #SET FRAMERATE
        clock.tick(60)

        # EXIT PROCESS
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.display.quit() 
                        sys.exit()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_ESCAPE]:
                sys.exit()
        # RENDERING PROCESS
        screen.fill(COLOUR)

        if time.time() - last_time_enemy_spawned > 0.6:
                enemies.append(Enemies())
                last_time_enemy_spawned = time.time()

         
        fighter.move()
        fighter.draw()

        if pressed_keys[K_SPACE]:
                fighter.fire() 

        j=0
        while j < len(missiles):
                missiles[j].move()
                missiles[j].draw()
                j += 1


        i = 0
        while i < len(enemies):
                enemies[i].move()		
                enemies[i].draw()
                enemies[i].bounce()
                
                if enemies[i].y > 480 or enemies[i].x > 640:
                        del enemies[i]
                        i -= 1
                i += 1

        i = 0
        while i < len(enemies):
                j=0
                while j < len(missiles):
                        if enemies[i].hit_by(missiles[j]):
                                del enemies[i]
                                del missiles[j]
                                beep.play()
                                score += 100
                                i -= 1
                                break
                        j +=1
                i += 1

        i = 0
        while i < len(enemies):
            if fighter.hit_by(enemies[i]):
                del enemies[i]
                health -= 5
                i -= 1                     
            i += 1

        pygame.draw.rect(screen, (200,0,50), (10,10,health*3,50))
        screen.blit(fontOne.render("Score: " + str(score), True, (200,0,50)), (350,5))
        pygame.display.update() 

        

