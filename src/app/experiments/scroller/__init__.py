import logging
import os
import pygame
import sys
from pygame.locals import RESIZABLE, SCALED, DOUBLEBUF

from app.utils.rss import get_rss_items

NAME = "scroller"
DESCRIPTION = "Scroller Experiment"

TARGET_FPS = 60
WIDTH = 640
HEIGHT = 64

NEWS_RSS_URL = os.environ.get("NEWS_RSS_URL")
assert NEWS_RSS_URL is not None, "NEWS_RSS_URL environment variable not set"


logger = logging.getLogger(NAME)

logger.info("SCROLLER EXPERIMENT")

pygame.init()

FONT_SYSTEM = pygame.font.SysFont(None, 32)

clock = pygame.time.Clock()
pygame.display.set_caption(DESCRIPTION)
screen_flags = RESIZABLE | SCALED | DOUBLEBUF
screen = pygame.display.set_mode((WIDTH, HEIGHT), screen_flags, 16)

frame = 0


class Message:
    def __init__(self, text, transient):
        self.text = text
        self.transient = transient


class MessageSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        position,
        text,
        font=FONT_SYSTEM,
        antialias=True,
        color=(255, 255, 255),
        margin=60,
        transient=False,
    ):
        super().__init__()
        self.position = position
        self.text = text
        self.margin = margin
        self.transient = transient
        self.image = font.render(self.text, antialias, color)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect[0], self.rect[1] = self.position[0], self.position[1]

    def update(self, frame):
        self.rect[0] -= 1
        if self.rect[0] < 0 - self.get_width():
            logger.info(f"Msg Kill: {self.text}")
            self.kill()

    def get_width(self):
        return self.rect[2] + self.margin


class MessageQueue:
    def __init__(self):
        self.items = []

    def add(self, text, transient=False):
        self.items.append(Message(text, transient))

    def get_next(self):
        if not len(self.items):
            return
        next_item = self.items.pop(0)
        if not next_item.transient:
            self.items.append(next_item)
        return MessageSprite(
            (WIDTH, 10), text=next_item.text, transient=next_item.transient
        )


messages = MessageQueue()
group_messages = pygame.sprite.Group()

news = get_rss_items(NEWS_RSS_URL)
for article in news.entries:
    messages.add(article["title"])

messages.add("T1", True)
messages.add("T2", True)

msg_current = None
msg_current_remain = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    if frame % 5000 == 0:
        msg_auto = f"Transient #{frame}"
        logger.info(f"Msg Add: {msg_auto}")
        messages.add(msg_auto, True)

    if msg_current_remain is None or msg_current_remain <= 0:
        msg_current = messages.get_next()
        msg_current_remain = msg_current.get_width()
        group_messages.add(msg_current)
        logger.info(f"Msg Count: {len(messages.items)}")
    if msg_current_remain > 0:
        msg_current_remain -= 1

    group_messages.update(frame)
    group_messages.draw(screen)

    pygame.display.flip()
    clock.tick(TARGET_FPS)
    frame += 1
