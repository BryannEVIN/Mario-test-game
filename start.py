# au préalable installer la bibliothèque pygame avec:
# pip install game

import pygame

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

background = pygame.image.load("./assets/img/background.jpg").convert()
perso = pygame.image.load("./assets/img/Issatos.png").convert_alpha()
mario = pygame.image.load("./assets/img/mario.png").convert_alpha()


sound = pygame.mixer.Sound("./assets/audio/1685.mp3")
sounddead = pygame.mixer.Sound("./assets/audio/dead.mp3")

def mario_collision(left, top):
    global mario, mario_rect
    print(f"position perso left : {left}")
    print(f"position perso top : {top}")
    if (left < 50 and top < 70):
        print("mario t'es dead chacal")
        mario = pygame.image.load("./assets/img/Mariodead.png").convert_alpha()
        sounddead.play()
    else :
        mario = pygame.image.load("./assets/img/mario.png").convert_alpha()


perso_rect = perso.get_rect()
perso_rect.topleft = (320, 240)
mario_rect = mario.get_rect()
mario_rect.topleft = (0, 0)

fenetre.blit(background, (0, 0))
# je crée une boucle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 27:  # touche espace
                continuer = False

            if event.key == 100:  # Touche D deplacement à droite
                if perso_rect.left < 500:
                    perso_rect = perso_rect.move(25, 0)
                    mario_collision(perso_rect.left, perso_rect.top)
                else:
                    sound.play()
            if event.key == 113:  # Touche Q deplacement à gauche
                if perso_rect.left > 0:
                    perso_rect = perso_rect.move(-25, 0)
                    mario_collision(perso_rect.left, perso_rect.top)
                else:
                    sound.play()
            if event.key == 115:  # Touche S deplacement bas
                if perso_rect.top < 380:
                    perso_rect = perso_rect.move(0, 25)
                    mario_collision(perso_rect.left, perso_rect.top)
                else:
                    sound.play()
            if event.key == 122:  # Touche Z deplacement haut
                if perso_rect.top > 0:
                    perso_rect = perso_rect.move(0, -25)
                    mario_collision(perso_rect.left, perso_rect.top)
                else:
                    sound.play()

    fenetre.blit(background, (0, 0))
    fenetre.blit(perso, perso_rect,)

    fenetre.blit(mario, mario_rect,)
    pygame.display.update()
pygame.quit()
