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
MESSAGE_MARGIN = 10

logger = logging.getLogger(NAME)

logger.info("SCROLLER EXPERIMENT")

pygame.init()

FONT_SYSTEM = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()
pygame.display.set_caption(DESCRIPTION)
screen_flags = RESIZABLE | SCALED
screen = pygame.display.set_mode((WIDTH, HEIGHT), screen_flags, 16)

frame = 0
messages = []


class Message(pygame.sprite.Sprite):
    def __init__(
        self, position, text, font=FONT_SYSTEM, antialias=True, color=(255, 255, 255)
    ):
        super().__init__()
        self.text = text
        self.image = font.render(self.text, antialias, color)
        self.rect = self.image.get_rect()
        self.rect[0], self.rect[1] = position[0], position[1]

    def update(self, frame):
        self.rect[0] -= 1


def build_message(text):
    return Message((WIDTH, 10), text)


group_messages = pygame.sprite.Group()

msg_init_1 = build_message("This is the first")
msg_init_2 = build_message("And the second message")
msg_init_3 = build_message("Finally, the third message")
messages.extend([msg_init_1, msg_init_2, msg_init_3])
logger.info(f"Messages: {messages}")


msg_current = None
msg_current_remain = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    if frame % 500 == 0:
        print("Adding new message...")
        messages.append(build_message(f"Auto message at frame #{frame}"))

    if msg_current_remain is None or msg_current_remain <= 0:
        if len(messages):
            msg_current = messages.pop(0)
            msg_current_remain = msg_current.rect[2] + MESSAGE_MARGIN
            group_messages.add(msg_current)
    if msg_current_remain > 0:
        msg_current_remain -= 1

    group_messages.update(frame)
    group_messages.draw(screen)

    pygame.display.flip()
    clock.tick(TARGET_FPS)
    frame += 1
