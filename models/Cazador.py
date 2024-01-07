from models.Entity import Entity
from models.Mascota import Pet
import pygame


class Cazador(Entity):
    def __init__(self, width, height, frames, lp=100, dmg=10, mov_speed=10, shot_speed=10, fire_rate=1):
        super().__init__(width, height, frames)
        self.max_lp = lp
        self.lp = lp
        self.dmg = dmg
        self.mov_speed = mov_speed
        self.shot_speed = shot_speed
        self.fire_rate = fire_rate

    def is_alive(self):
        return self.lp > 0

    def attack(self, target: Pet):
        if self.is_alive():
            target.take_damage(self.dmg)

    def get_mov_speed(self):
        return self.mov_speed

    def move_right(self, x, surface, frame_index):
        while self.curr_x <= x:
            x_increment = self.curr_x + self.mov_speed
            self.draw_element(surface, (x_increment, self.curr_y),frame_index)
            self.curr_x = x_increment

    def move_left(self, x, surface, frame_index):
        while self.curr_x >= x:
            x_decrement = self.curr_x - self.mov_speed
            self.draw_element(surface, (x_decrement, self.curr_y), frame_index)
            self.curr_x = x_decrement

    def take_damage(self, amount):
        if self.lp - amount <= 0:
            self.lp = 0
        else:
            self.lp -= amount




