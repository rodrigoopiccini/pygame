import pygame
import random

pygame.init()

#Gerar tela principal
largura = 700
altura = 850
window = pygame.display.set_mode ((largura, altura))
pygame.display.set_caption('UP Challenge')

#Gera passaros
passaro_largura = 40
passaro_altura = 28
casa_largura = 150
casa_altura = 290
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('imagens/ceu_azul.jpg').convert()
fundo = pygame.transform.scale(fundo, (700, 850))
passaro_img = pygame.image.load('imagens/passaro.gif').convert_alpha()
passaro_img = pygame.transform.scale(passaro_img, (passaro_largura, passaro_altura))
casa_img = pygame.image.load('imagens/casa.png').convert_alpha()
casa_img = pygame.transform.scale(casa_img, (casa_largura, casa_altura))

class Casa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = altura-10
        self.speedx = 0

    def update(self):
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class Passaro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = largura
        self.rect.y = random.randint (5, 750)
        self.speedx = random.randint(-10, -6)
        self.speedy = 0
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = largura
            self.rect.y = random.randint (5, 750)
            self.speedx = random.randint(-10, -6)
            self.speedy = 0


#inicia estruturas
game = True

clock = pygame.time.Clock()
FPS = 30

todospassaros = pygame.sprite.Group()

jogador = Casa(casa_img)

todospassaros.add(jogador)

for i in range(8):
    passaro = Passaro(passaro_img)
    todospassaros.add(passaro)

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    todospassaros.update()


#gera fundo

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    todospassaros.draw(window)
    pygame.display.update()



pygame.quit()


