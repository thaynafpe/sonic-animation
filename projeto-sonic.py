import pygame
from pygame.locals import *
from pygame import mixer
from sys import exit

pygame.init()


largura = 640
altura = 448

bg = pygame.image.load('background.png')
bg1 = pygame.transform.scale(bg, (320 * 2, 224 * 2))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sonic The Hedgehog')

mixer.init()
mixer.music.load('C:\\Users\\thay\\Downloads\\song.mp3')
mixer.music.play(-1)

class Sonic(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sonic 1.png'))
        self.sprites.append(pygame.image.load('sonic 2.png'))
        self.sprites.append(pygame.image.load('sonic 3.png'))
        self.sprites.append(pygame.image.load('sonic 4.png'))
        self.sprites.append(pygame.image.load('sonic 5.png'))
        self.sprites.append(pygame.image.load('sonic 4.png'))
        self.sprites.append(pygame.image.load('sonic 5.png'))
        self.sprites.append(pygame.image.load('sonic 4.png'))
        self.sprites.append(pygame.image.load('sonic 5.png'))
        self.sprites.append(pygame.image.load('sonic 4.png'))
        self.sprites.append(pygame.image.load('sonic 5.png'))
        self.sprites.append(pygame.image.load('sonic 6.png'))
        self.sprites.append(pygame.image.load('sonic 7.png'))
        self.sprites.append(pygame.image.load('sonic 8.png'))
        self.sprites.append(pygame.image.load('sonic 9.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.rect = self.image.get_rect()
        self.rect.bottomright = 400, 385

        self.animar = True

    def animacao(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = True
            self.image = self.sprites[int(self.atual)]


todas_as_sprites = pygame.sprite.Group()
sonic = Sonic()
todas_as_sprites.add(sonic)

relogio = pygame.time.Clock()

while True:

    relogio.tick(10)
    tela.blit(bg1, (0, 0), (0, 0, 640, 448))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    sonic.animacao()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
