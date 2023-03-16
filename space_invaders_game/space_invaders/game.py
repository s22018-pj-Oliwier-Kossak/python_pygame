import pygame
import random
from user_ship import UserShip
from enemy_ship import EnemyShip
from bullet import Bullet

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


pygame.init()

player_score = 0
health = 3
level = 1
user_bullet_speed = 0
run = True

health_1_position_x = 635
health_2_position_x = 680
health_3_position_x = 725

font = pygame.font.SysFont('timesnewroman', 30)
user_img = r'../img/statek42x45.png'
bullet_img = r'../img/user_bullet.png'
enemy_ship = r'../img/Enemy55x55.png'
enemy_ship2 = r'../img/Enemy55x55.png'
enemy_bullet = r'../img/enemy_bullet.png'
enemy_bullet2 = r'../img/enemy_bullet.png'
health_img = pygame.image.load(r'../img/health.png')
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


start_random_enemy_postion_x = random.randint(500, 600)
start_random_enemy_postion_y = random.randint(-300, -100)
start_random_enemy_postion_x2 = random.randint(100, 200)
start_random_enemy_postion_y2 = random.randint(-150, -100)

user = UserShip(screen, 375, user_img, 8.5)
user_bullet = Bullet(screen, user.positon_x + 11, 720, 10, bullet_img)
user_bullet2 = Bullet(screen, user.positon_x + 11, 720, 10, bullet_img)
enemy = EnemyShip(screen, start_random_enemy_postion_x, start_random_enemy_postion_y, 4, enemy_ship)
enemy2 = EnemyShip(screen, start_random_enemy_postion_x2, start_random_enemy_postion_y2, 3, enemy_ship2)
enemy_bullet = Bullet(screen, start_random_enemy_postion_x + 15, start_random_enemy_postion_y + 70, 5, enemy_bullet)
enemy_bullet2 = Bullet(screen, start_random_enemy_postion_x2 + 15, start_random_enemy_postion_y2 + 70, 6, enemy_bullet2)
user_bullet_list = [1, user_bullet2]

while run:

    text_score = font.render(f"Score: {player_score}", False, WHITE)
    text_level = font.render(f'Level:{level}', False, WHITE)
    screen.fill(BACKGROUND_COLOR)
    screen.blit(health_img, (health_3_position_x, 10))
    screen.blit(health_img, (health_2_position_x, 10))
    screen.blit(health_img, (health_1_position_x, 10))
    screen.blit(text_score, (10, 10))
    screen.blit(text_level, (10, 40))

    random_enemy_postion_x = random.randint(40, 750)
    random_enemy_postion_x2 = random.randint(40, 740)

    pygame.time.Clock().tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_SPACE]:
        user_bullet_speed = -10

    for i in user_bullet_list:
        count_bullet = 1

        user_bullet_list[count_bullet].draw()
        user_bullet_list[count_bullet].postion_y += user_bullet_speed

        if user_bullet_list[count_bullet].postion_y == 720:
            user_bullet_list[count_bullet].postiton_x = user.positon_x + 11
        if user_bullet_list[count_bullet].postion_y < 0:
            user_bullet_list[count_bullet].postiton_x = user.positon_x + 11
            user_bullet_list.remove(user_bullet_list[count_bullet])
            print(count_bullet)
        if len(user_bullet_list) <= 1:
            user_bullet_speed = 0
            user_bullet.postion_y = 720
            user_bullet_list.append(user_bullet)

    if user_bullet_list[1].postiton_x < enemy.position_x + 55 and user_bullet_list[
        1].postiton_x > enemy.position_x - 15:

        if user_bullet_list[1].postion_y < enemy.position_y + 50 and user_bullet_list[1].postion_y > enemy.position_y:
            enemy.position_y = -225
            enemy.position_x = random_enemy_postion_x
            player_score += 1

    if user_bullet_list[1].postiton_x < enemy2.position_x + 55 and user_bullet_list[
        1].postiton_x > enemy2.position_x - 15:

        if user_bullet_list[1].postion_y < enemy2.position_y + 50 and user_bullet_list[1].postion_y > enemy2.position_y:
            enemy2.position_y = -150
            enemy2.position_x = random_enemy_postion_x2
            player_score += 1

    if enemy_bullet.postiton_x < user.positon_x + 25 and enemy_bullet.postiton_x > user.positon_x - 10:

        if enemy_bullet.postion_y > 750:
            print(enemy_bullet.postion_y)
            enemy_bullet.postion_y = enemy.position_y + 50
            enemy_bullet.postiton_x = enemy.position_x + 15
            health -= 1

    if enemy_bullet2.postiton_x < user.positon_x + 25 and enemy_bullet2.postiton_x > user.positon_x - 10:

        if enemy_bullet2.postion_y > 750:
            print(enemy_bullet2.postion_y)
            enemy_bullet2.postion_y = enemy2.position_y + 50
            enemy_bullet2.postiton_x = enemy2.position_x + 15
            health -= 1

    if enemy.position_y > 800:
        enemy.position_y = -150
        enemy.position_x = random_enemy_postion_x
        enemy_bullet.postion_y = -90
        enemy_bullet.postiton_x = random_enemy_postion_x + 15
        health -= 1

    if enemy2.position_y > 800:
        enemy2.position_y = -150
        enemy2.position_x = random_enemy_postion_x
        enemy_bullet2.postion_y = -90
        enemy_bullet2.postiton_x = random_enemy_postion_x2 + 15
        health -= 1

    if enemy_bullet.postion_y > 800:
        enemy_bullet.postion_y = enemy.position_y + 50
        enemy_bullet.postiton_x = enemy.position_x + 15

    if enemy_bullet2.postion_y > 800:
        enemy_bullet2.postion_y = enemy2.position_y + 50
        enemy_bullet2.postiton_x = enemy2.position_x + 15

    if health == 2:
        health_1_position_x = -100

    if health == 1:
        health_2_position_x = -100
    if health <= 0:
        health_3_position_x = -100
        user.speed = 0
        font1 = pygame.font.SysFont('timesnewroman', 50)
        text_game_over = font1.render(f"GAME OVER", False, RED)
        screen.blit(text_game_over, (250, 300))

    if player_score > 10 and player_score < 25:
        level = 2
        enemy.speed = 4.5
    elif player_score >= 25 and player_score < 35:
        level = 3
        enemy.speed = 4.5
        enemy2.speed = 3.5
    elif player_score >= 35 and player_score < 50:
        level = 4
        enemy.speed = 4.5
        enemy2.speed = 3.5
        enemy_bullet.speed = 5.5

    elif player_score > 51 and player_score < 65:
        level = 5
        enemy.speed = 5
        enemy2.speed = 4.25
        enemy_bullet.speed = 5.75
        enemy_bullet2.speed= 5

    elif player_score >= 65 and player_score < 80:
        level = 6
        enemy.speed = 5.25
        enemy2.speed = 4.50
        enemy_bullet.speed = 6
        enemy_bullet2.speed= 6.25

    elif player_score >= 80:
        level = 7
        enemy.speed = 5.5
        enemy2.speed = 5
        enemy_bullet.speed = 6.5
        enemy_bullet2.speed= 6.5

    enemy_bullet.draw()
    enemy_bullet.move()
    enemy.draw_ship()
    enemy.move_ship()
    enemy_bullet2.draw()
    enemy_bullet2.move()
    enemy2.draw_ship()
    enemy2.move_ship()
    user.draw_ship()
    user.move_ship()

    pygame.display.update()

pygame.quit()
