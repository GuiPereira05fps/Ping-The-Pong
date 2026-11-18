import pygame as pg

pg.init()
mainWindow = pg.display.set_mode(size=(900, 600))

while True:
    # Checks events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
