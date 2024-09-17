import random
import pygame

pygame.init()
wight = 800
height = 600
size = (wight, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("jumping_simulator")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PURPLE = (138, 43, 226)


def make_text(text, font_size, color, bool):
    font = pygame.font.Font(None, font_size)
    if bool == 0:
        Text = font.render(text, True, color)
        return Text
    else:
        return 0

cube_x = 100
cube_y = 500
cube_wight = 30
cube_height = 30
gravity = 10
cube_speed = 2.25
jump = False
height = cube_y - 100
ground = True
saitama = 800
t = 0
breath = False
point_x = random.randint(0, 500)
point_y = 0
point_speed = 7.5
lava_speed = 5
lava_x = 800
lava_y = 510
p = 0
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)
    screen.fill(WHITE)
    text1 = make_text("point: {}".format(p), 34, RED, 0)
    fps = clock.get_fps()
    text2 = make_text("fps: {}".format(fps), 30, RED, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cube_x -= cube_speed
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cube_x += cube_speed

    if keys[pygame.K_LSHIFT] and not breath:
        cube_speed = 7.5
        t += 2
    else:
        cube_speed = 2.25

    if t >= saitama:
        breath = True

    if breath:
        t -= 2

    if t <= 0:
        breath = False

    # jumping
    if keys[pygame.K_SPACE] and ground:
        jump = True

    if jump:
        cube_y -= gravity
        ground = False

    if cube_y <= height:
        jump = False

    if not jump:
        cube_y += gravity

    if cube_y >= 500:
        cube_y = 500
        ground = True

    if cube_x <= 0:
        cube_x = 0
    elif cube_x >= wight - cube_wight:
        cube_x = wight - cube_wight

    point_y += point_speed
    lava_x -= lava_speed

    pygame.draw.rect(screen, RED, (point_x, point_y, 10, 10))
    point = pygame.Rect(point_x, point_y, 10, 10)
    player = pygame.Rect(cube_x, cube_y, cube_wight, cube_height)
    lava = pygame.Rect(lava_x, lava_y + 10, 20, 20)
    pygame.draw.rect(screen, BLUE, (t, 550, 8000, 5))
    pygame.draw.rect(screen, RED, (cube_x, cube_y, cube_wight, cube_height))
    pygame.draw.rect(screen, PURPLE, (lava_x, lava_y, 20, 20))

    if pygame.Rect.colliderect(point, player):
        p += 5
        point_y = 0
        point_x = random.randint(0, 500)
        print("point: ", p)

    if point_y == 600:
        point_y = 0
        point_x = random.randint(0, 500)

    if pygame.Rect.colliderect(lava, player):
        p -= 1
        lava_x = 0
        print("point: ", p)

    if lava_x <= 0:
        lava_x = 800

    pygame.display.flip()

pygame.quit()
print("your point: ", p)
input("press enter to exit... ")
