import pygame
from pygame.locals import *
pygame.init()

# Variablen/KONSTANTEN setzen
W, H = 800, 600
FPS  = 30
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

spielaktiv = True

# Definieren und Öffnen eines neuen Fensters
fenster = pygame.display.set_mode((W, H))
pygame.display.set_caption("Varroa Invaders")
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv == False:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        # Beenden bei [ESC] oder [X]
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            spielaktiv = False

    # Spiellogik

    # Spielfeld löschen
    fenster.fill(WEISS)

    # Spielfeld/figuren zeichnen

    # Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)
