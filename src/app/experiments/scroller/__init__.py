import logging
import os
import pygame
import sys
from pygame.locals import RESIZABLE, SCALED

NAME = "scroller"
DESCRIPTION = "Scroller Experiment"

TARGET_FPS = 60
WIDTH = 640
HEIGHT = 64

logger = logging.getLogger(NAME)

logger.info("SCROLLER EXPERIMENT")

pygame.init()
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 16)
pygame.display.set_caption(DESCRIPTION)

screen_flags = RESIZABLE | SCALED
screen = pygame.display.set_mode((WIDTH, HEIGHT), screen_flags, 16)

frame = 0


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, index, width=64, height=64, color=None):
        super().__init__()
        self.width = width
        self.height = height
        self.index = index
        self.color = color or (255, 255, 0)
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def update(self, frame):
        self.image = pygame.Surface([self.width, self.height])
        pygame.draw.rect(
            self.image,
            self.color,
            pygame.Rect(0, 0, self.width, self.height),
        )


squares = pygame.sprite.Group()

for i in range(0, 10):
    squares.add(Square(0 + (i * 32), 0, index=i, width=16, height=16))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((0, 0, 0))
    squares.update(frame)
    squares.draw(screen)
    pygame.display.flip()
    clock.tick(TARGET_FPS)
    frame += 1
