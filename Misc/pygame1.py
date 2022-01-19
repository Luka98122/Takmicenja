import pygame as pg
import pygamebg as pgbg
import math

pg.init()
prozor = pg.display.set_mode((2000, 2000))
#
#
#
iceCreamX = 1000
iceCreamY = 775
clock = pg.time.Clock()


def inCircle(px, py, cx, cy, cr):
    dx = px - cx
    dy = py - cy
    a = dx
    b = dy
    c = math.sqrt(dx * dx + dy * dy)
    if c <= cr:
        return 1
    return 0


for i in range(400):
    prozor.fill(pg.Color("yellow"))
    iceCreamX += 1

    pg.draw.polygon(
        prozor,
        pg.Color("sandyBrown"),
        [
            (iceCreamX, iceCreamY + 650),
            (iceCreamX - 300, iceCreamY),
            (iceCreamX + 300, iceCreamY),
            (iceCreamX, iceCreamY + 650),
        ],
    )

    pg.draw.circle(prozor, pg.Color("HotPink"), (iceCreamX, iceCreamY), 300)
    pg.draw.circle(prozor, pg.Color("limegreen"), (iceCreamX, iceCreamY), 200)
    pg.draw.circle(prozor, pg.Color("Red"), (iceCreamX, iceCreamY), 100)

    ev = pg.event.get()
    prozor.blit(text, textRect)
    # proceed events
    for event in ev:

        # handle MOUSEBUTTONUP
        if event.type == pg.MOUSEBUTTONDOWN:
            position = pg.mouse.get_pos()
            a = 2
            a = 3
            if inCircle(position[0], position[1], iceCreamX, iceCreamY, 100) == 1:
                exit()
    pg.display.update()

    clock.tick(60)


#
#
#
pg.quit()
