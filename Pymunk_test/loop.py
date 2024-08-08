import pygame as pg
import sys
import pymunk
from pymunk.pygame_util import DrawOptions
from settings import Settings
from player import Player
from player2 import Player2

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Dupa")
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pg.time.Clock()
        self.run = True

        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.draw_options = DrawOptions(self.screen)

        self.player = Player(self, self.space) 
        self.player2 = Player2(self, self.space)

    def run_game(self):
        while self.run:
            self._check_events()
            dt = self.clock.tick(60)/ 500
            self._update_game(dt)
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pg.K_w:
            self.player.moving_up = True
        elif event.key == pg.K_s:
            self.player.moving_down = True
        elif event.key == pg.K_a:
            self.player.moving_left = True
        elif event.key == pg.K_d:
            self.player.moving_right = True
        elif event.key == pg.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pg.K_w:
            self.player.moving_up = False
        elif event.key == pg.K_s:
            self.player.moving_down = False
        elif event.key == pg.K_a:
            self.player.moving_left = False
        elif event.key == pg.K_d:
            self.player.moving_right = False

    def _update_game(self,dt):
        self.player.update(dt)
        self.player2.update(dt)
        self.space.step(1/60.0)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.space.debug_draw(self.draw_options)
        self.player.blitme()
        self.player2.blitme()
        pg.display.flip()

if __name__ == "__main__":
    gra = Game()
    gra.run_game()
