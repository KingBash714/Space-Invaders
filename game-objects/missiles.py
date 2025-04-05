import sys
import math
import stdio, stdrandom, stddraw, stdaudio, stdarray


# constants
MISSILE_SIZE = 0.02
MISSILE_VELOCITY = 1 # this can be experimented with (in units/s)

class Missile:

    x = 0
    y = 0

    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def update_pos(self, FPS): # FPS is a constant stored somewhere idk (maybe in some module to manage the game window)
        self.x += MISSILE_VELOCITY / FPS
        self.y += MISSILE_VELOCITY / FPS

    def draw_missile(self):
        stddraw.setPenColor(RED)
        stddraw.filledCircle(self.x, self.y, MISSILE_SIZE)


def detect_collision(missiles, enemies): # implemented in enemies or in missile?
    for i in range(len(missiles)):
        for k in range(len(enemies)):
            pass # boundary checking, depends on implementation of enemies, pls check

def main():
    pass
    # TODO: make module tests


if __name__ == "__name__":
    main()
