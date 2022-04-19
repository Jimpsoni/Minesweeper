import pygame as pg

"""
TO DO:
"""

# Make the pygame window
WIDTH, HEIGHT = 600, 600

# Board dimension
B_WIDTH, B_HEIGHT, X, Y, COLOR = 500, 500, 50, 50, (255, 255, 255)

# Initialize pygame
pg.init()
pg.display.set_caption("Minesweeper")

WIN = pg.display.set_mode((WIDTH, HEIGHT))


running = True


def set_up_board():
    # 50, 50, 500, 500
    pg.draw.rect(WIN, COLOR, (X, Y, B_WIDTH, B_HEIGHT))

    # Draw lines
    for num in range(0, 8):
        pg.draw.line(WIN, (20, 20, 20), (100 + num * 56, 50), (100 + num * 56, 550), width=2)
        pg.draw.line(WIN, (20, 20, 20), (50, 100 + num * 56), (550, 100 + num * 56), width=2)


def update_screen():
    pg.display.update()


set_up_board()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    update_screen()
