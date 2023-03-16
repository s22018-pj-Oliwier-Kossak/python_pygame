import pygame


class UserShip():
    def __init__(self, window, positon_x, path, speed):
        self.positon_x = positon_x
        self.window = window
        self.path = path
        self.speed = speed

    def draw_ship(self):
        user_ship_img = pygame.image.load(self.path)
        self.window.blit(user_ship_img, (self.positon_x, 754))

    def move_ship(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.positon_x -= self.speed
            if self.positon_x < 0:
                self.positon_x += self.speed

        if keys[pygame.K_RIGHT]:
            self.positon_x += self.speed
            if self.positon_x >762:
                self.positon_x -= self.speed



