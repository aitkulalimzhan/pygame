from typing import Any
import pygame
import random


screen = pygame.display.set_mode((640,800))
clock = pygame.time.Clock()
FPS = 60    
running = True
background = pygame.transform.scale(pygame.image.load('race.py/road.png'),(640,800))
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('race.py/Player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 620
        self.speed= 5
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
        if self.rect.left < 85:
            self.rect.x = 85
        if self.rect.right > 555:
            self.rect.x = 515

class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('race.py/Enemy.png')
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.y = -10
        self.rect.x = random.randint(200,440)
    def update(self):
        
        self.rect.y += self.speed
        if self.rect.y > 850:
            self.rect.y = -10
            self.rect.x = random.randint(200,440)
            self.speed = random.randint(5,15)    

p = player()
e = enemy()
d = enemy()
all_sprites = pygame.sprite.Group()
all_sprites.add(p)
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(e)
enemy_sprites.add(d)
x_bg = 0
dx = 5

pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')
    x_loop = x_bg % 800
    screen.blit(background,(0, x_loop - 800))
    if x_loop < 800:
        screen.blit(background, (0,x_loop))
    x_bg -= dx
    
    all_sprites.draw(screen)
    all_sprites.update()
    enemy_sprites.draw(screen)
    enemy_sprites.update()
    if pygame.sprite.groupcollide(all_sprites,enemy_sprites, True, False):
        running = False

 
    pygame.display.flip()
    clock.tick(FPS)
