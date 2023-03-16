import pygame



class EnemyShip():
    def __init__(self, window, position_x, position_y, speed, path):
        self.position_x = position_x
        self.window = window
        self.position_y = position_y
        self.speed = speed
        self.path = path

    def draw_ship(self):
        enemy_ship_img = pygame.image.load(self.path)
        self.window.blit(enemy_ship_img, (self.position_x, self.position_y))

    def move_ship(self):
        self.position_y += self.speed

    def enemy_position_x(self):
        return self.position_x

    def enemy_position_y(self):
        return self.position_y
