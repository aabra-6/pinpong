import pygame
pygame.init()

light_blue = (0, 190, 255)
win32 = pygame.display.set_mode((1000, 700))
fps = pygame.time.Clock()
eventlist = [ ]
font_texk= pygame.font.Font('minecraft.ttf',50)
speed=5
gooooool=0
gooooool2=0
WIT=(225, 225, 225)
BLUE=(0, 0, 255)
RED= (255, 0, 0)
GREEN=( 0, 255, 0)

class bol():
    def __init__(self, cord_x, cord_y, width, length) -> None:
        self.hitbox = pygame.Rect(cord_x, cord_y, width, length)
        self.speedx=5
        self.speedy=5
    def move3(self):
        global gooooool,gooooool2
        self.hitbox.x -= self.speedx
        self.hitbox.y -= self.speedy
        if self.hitbox.y < 0:
            self.speedy=-5
        if self.hitbox.y > 600:
            self.speedy=5
        if self.hitbox.x < 0:
            self.speedx=-5
            boll.hitbox.x=500
            boll.hitbox.y=350
            gooooool+=1
        if self.hitbox.x > 900:
            self.speedx=5
            boll.hitbox.x=500
            boll.hitbox.y=350
            gooooool2+=1
    def move4(self):
        if boll.hitbox.colliderect(player.hitbox):
            self.speedx=-5
        if boll.hitbox.colliderect(player2.hitbox):
            self.speedx=5

boll=bol(500,350,100,100)

class pleer():
    def __init__(self, cord_x, cord_y, width, length) -> None:
        self.hitbox = pygame.Rect(cord_x, cord_y, width, length)
    def move(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_w] == True:
            self.hitbox.y -= speed
        if key_list[pygame.K_s] == True:
            self.hitbox.y += speed
        if self.hitbox.y > 500:
            self.hitbox.y = 500
        if self.hitbox.y < 0:
            self.hitbox.y = 0
class pleer2():
    def __init__(self, cord_x, cord_y, width, length) -> None:
        self.hitbox = pygame.Rect(cord_x, cord_y, width, length)
    def move2(self):
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_UP] == True:
            self.hitbox.y -= speed
        if key_list[pygame.K_DOWN] == True:
            self.hitbox.y += speed
        if self.hitbox.y > 500:
            self.hitbox.y = 500
        if self.hitbox.y < 0:
            self.hitbox.y = 0
    
player = pleer(50, 0, 50, 200)
player2 = pleer2(900,0,50,200)

while True:
    win32.fill(light_blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    player.move()
    player2.move2()
    boll.move3()
    boll.move4()
    pygame.draw.rect(win32, BLUE, (player.hitbox))
    pygame.draw.rect(win32, RED, (player2.hitbox))
    pygame.draw.rect(win32, GREEN, (boll.hitbox))
    score_img=font_texk.render(str(gooooool)+'vs'+str(gooooool2), True, (0, 0, 0))
    win32.blit(score_img, (450, 0))
    pygame.display.update()
    fps.tick(120) 