from models.Entity import Entity
import random
import pygame

class Pet(Entity):
    def __init__(self, msgs, name, width, height, frames, death_frame, lp=100, hap=100, food=100) -> None:
        super().__init__(width, height, frames)
        self.msgs = msgs
        self.name = name
        self.max_lp = lp
        self.max_hap = hap
        self.max_food = food
        self.lp = lp
        self.hap = hap
        self.food = food
        self.death_frame = pygame.transform.scale(death_frame, (width+125, height+150))


    def is_alive(self) -> bool:
        return self.lp > 0

    def evolve(self, lp, food, hap):
        self.max_lp += lp
        self.max_food += food
        self.max_hap += hap

    def eat(self, amount):
        if amount + self.food > self.max_food:
            self.food = self.max_food
        else:
            self.food += amount

    def is_hungry(self):
        return self.food <= 50

    def is_sad(self):
        return self.hap <= 25

    def handle_health(self):
        if self.food == self.max_food and self.hap == self.max_hap:
            self.lp = self.max_lp

        elif self.is_sad() or self.is_hungry():
            self.take_damage(15)

        elif not self.is_sad() and not self.is_hungry():
            self.heal(10)


    def take_damage(self, amount):
        if self.lp - amount <= 0:
            self.lp = 0
        else:
            self.lp -= amount

    def reduce_food(self, amount):
        if self.food - amount > 0:
            self.food -= amount
        else:
            self.food = 0


    def display_fact(self):
        msg_idx = random.randint(0, len(self.msgs))
        return self.msgs[msg_idx-1]


    def pet_him(self, amount):
        if self.hap + amount >= self.max_hap:
            self.hap = self.max_food
        else:
            self.hap += amount

    def heal(self, amount):
        if self.lp + amount > self.max_lp:
            self.lp = self.max_lp
        else:
            self.lp += amount
    def reduce_hap(self, amount):
        if self.hap - amount <= 0:
            self.hap = 0
        else:
            self.hap -= amount

    def draw_kill(self, surface, frame_index):
        self.food = 0
        self.hap = 0
        previous_frames = self.frames
        self.frames = [self.death_frame]
        self.draw_element(surface, (self.curr_x, self.curr_y), frame_index)
        self.frames = previous_frames
