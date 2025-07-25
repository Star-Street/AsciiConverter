# ASCII art converter
import sys

import pygame as pg
from pygame import SurfaceType


def get_image_prefer(path: str, size: float) -> tuple[pg.Surface, int, int]:
    img = pg.image.load(path)
    img = pg.transform.scale_by(img, size)

    height = img.get_height()
    width = img.get_width()

    return img, height, width


def print_image(img: pg.Surface, width: int, height: int):
    for y in range(0, height):
        for x in range(0, width):
            r, g, b, a = img.get_at((x, y))

            print("\u001B[38;2;{0};{1};{2}m".format(r, g, b), end="@")
            print("\u001B[0m", end="")
        print()


def save_image(img: pg.Surface, width: int, height: int):
    out_image = create_image(img, width, height)
    pg.image.save(out_image, "assets/images/image_ascii.jpg")


def show_image(img: pg.Surface, width: int, height: int):
    out_image = create_image(img, width, height)
    window = pg.display.set_mode((1920, 1080))
    window.blit(pg.transform.scale_by(out_image, window.get_width() / out_image.get_width()), (0, 0))

    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()


def create_image(img: pg.Surface, width: int, height: int) -> pg.Surface:
    author = "power by StarStrit"
    # symbol = "\u2588"
    symbol = "#"

    font = pg.font.SysFont("Courier New", 12)
    char_width, char_height = font.size(symbol)

    char_width = char_width / 1
    char_height = char_height / 2

    out_image = pg.Surface((width * char_width, height * char_height))

    counter = 0
    for y in range(0, height):
        for x in range(0, width):
            r, g, b, a = img.get_at((x, y))

            # if y == height - 1 and width - len(author) <= x:
            #     symbol = author[x - width]

            symbol = author[counter]
            counter += 1
            if counter >= len(author):
                counter = 0

            text_surface = font.render(symbol, True, (r, g, b))
            pos_x = x * char_width
            pos_y = y * char_height - 3

            out_image.blit(text_surface, (pos_x, pos_y))

    return out_image


if __name__ == "__main__":
    pg.init()

    image, imgHeight, imgWidth = get_image_prefer("assets/images/test.png", 0.6)
    # print_image(image, imgWidth, imgHeight)
    save_image(image, imgWidth, imgHeight)
    # show_image(image, imgWidth, imgHeight)