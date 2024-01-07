import pygame
import sys


class Entity:
    def __init__(self, width, height, frames) -> None:
        self.height = height
        self.width = width
        self.frames = [pygame.transform.scale(x, (width, height)) for x in frames]
        self.curr_x = None
        self.curr_y = None

    def draw_element(self, surface, position, frame_index=0):
        self.curr_x = position[0]
        self.curr_y = position[1]
        element_rect = pygame.Rect(position[0], position[1], self.width, self.height)
        current_frame = self.frames[frame_index]
        current_frame_rect = current_frame.get_rect(center=element_rect.center)
        surface.blit(current_frame, current_frame_rect)


