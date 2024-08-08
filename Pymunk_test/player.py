import pygame as pg
import pymunk
from settings import Settings

class Player:
    def __init__(self, game, space):
        self.screen = game.screen
        self.settings = game.settings
        self.space = space

        self.radius = 40  
        self.body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, self.radius))
        self.body.position = self.screen.get_rect().center
        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.elasticity = 1.0 # Elasticity for bouncing
        self.shape.friction = 1.0
        space.add(self.body, self.shape)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 200.0 
        self.create_boundaries()

    def create_boundaries(self):
        static_lines = [
            pymunk.Segment(self.space.static_body, (0, 0), (self.settings.screen_width, 0), 1),
            pymunk.Segment(self.space.static_body, (0, 0), (0, self.settings.screen_height), 1),  
            pymunk.Segment(self.space.static_body, (self.settings.screen_width, 0), (self.settings.screen_width, self.settings.screen_height), 1),  # Right boundary
            pymunk.Segment(self.space.static_body, (0, self.settings.screen_height), (self.settings.screen_width, self.settings.screen_height), 1)  # Bottom boundary
        ]
        for line in static_lines:
            line.elasticity = 1.0
            self.space.add(line)

    def update(self, dt):
        if self.moving_right:
            self.body.apply_impulse_at_local_point((self.speed * dt, 0))
        if self.moving_left:
            self.body.apply_impulse_at_local_point((-self.speed * dt, 0))
        if self.moving_up:
            self.body.apply_impulse_at_local_point((0, -self.speed * dt))
        if self.moving_down:
            self.body.apply_impulse_at_local_point((0, self.speed * dt))

    def blitme(self):
        # Draw the player as a circle at its current position
        pg.draw.circle(self.screen, (0, 191, 255), (int(self.body.position.x), int(self.body.position.y)), self.radius)