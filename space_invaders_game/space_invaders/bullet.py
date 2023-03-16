import pygame


class Bullet():

    def __init__(self, window, postiton_x, postion_y, speed, path_img):
        self.window = window
        self.postion_y = postion_y
        self.postiton_x = postiton_x
        self.speed = speed
        self.path_img = path_img

    def draw(self):
        bullet_img = pygame.image.load(self.path_img)
        self.window.blit(bullet_img, (self.postiton_x, self.postion_y))

    def move(self):
        self.postion_y += self.speed
