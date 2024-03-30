import pygame
import pygame.freetype
from pygame import mixer
import time
import os
from pygame.locals import *

pygame.init()
mixer.pre_init(44100, -16, 2, 1024)

screen_width, screen_height = 1200, 650
screen = pygame.display.set_mode((screen_width, screen_height))
coordinates = {
    "xc": 80,
    "yc": 420
}

width, height, vel, jumpvel = 30, 60, 4, 18
obst_width, obst_height = 80, 90
ox, oy = 800, 500
sens = ['']
run = True
obst_list = [[800, 500, 80, 70], [100, 300, 30, 70]]
# my idea is to make every obstacle coordinates stored in a list then check if this coodinate in list
direction = 0
minion1_image = pygame.image.load(os.path.join("images/hezbminion1.png"))
minion_anim_1 = pygame.transform.scale(minion1_image, (60, 55.375))
minion2_image = pygame.image.load(os.path.join("images/hezbminion2.png"))
minion_anim_2 = pygame.transform.scale(minion2_image, (60, 55.375))
minion_animation = [minion_anim_1, minion_anim_2]

dahyeman1_image = pygame.image.load(os.path.join("images/dahyeman1.png"))
dahyeman1 = pygame.transform.scale(dahyeman1_image, (52, 60.))
dahyeman2_image = pygame.image.load(os.path.join("images/dahyeman2.png"))
dahyeman2 = pygame.transform.scale(dahyeman2_image, (52, 60))
dahyeman3_image = pygame.image.load(os.path.join("images/dahyeman3.png"))
dahyeman3 = pygame.transform.scale(dahyeman3_image, (52, 60))
dahyeman4_image = pygame.image.load(os.path.join("images/dahyeman4.png"))
dahyeman4 = pygame.transform.scale(dahyeman4_image, (52, 60))
walking_list = [dahyeman4, dahyeman1, dahyeman2, dahyeman3]
walk_animation_index = 0
walking = False
coords_list = []
brick_list = []
collide_right = False
collide_left = False
jump = False
jump_traj = ""
on_brick_list = []
thing = 0 #I seriously had no idea what to call this variable smh
on_brick = False

def check_x_coords(x, list):
    for i in list:
        c = i[0]
        if c-width == x or x == c+i[2]:
            return False
        return True


def check_y_coords(y, list):
    for i in list:
        c = i[1]
        if c-height == y or y == c+i[3]:
            return False
        return True


screen_width = 1000
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dahye Run')
pygame.display.set_icon(pygame.image.load("images/hezbminion1.png"))

tile_size = 30
bg_img = pygame.image.load('images/background.png')


def draw_world(x_coords, y_coords):
    global coords_list
    coords_list = list(zip(x_coords,y_coords))
    for i in range(len(x_coords)):
        screen.blit(img, coords_list[i])



world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
#making the world
brick = pygame.image.load('images/brick.png')
pygame.transform.scale(brick, (tile_size, tile_size))
x_coords_of_all_blocks = []
y_coords_of_all_blocks = []
row_count = 0
for r in world_data:
    col_count = 0
    for c in r:
            if c == 1:
                img = pygame.transform.scale(brick, (tile_size, tile_size))
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                x_coords_of_all_blocks.append(img_rect.x)
                img_rect.y = row_count * tile_size
                y_coords_of_all_blocks.append(img_rect.y)
                brick_list.append(img_rect)
            col_count += 1
    row_count += 1


class Enemy:
    def __init__(self, type, coords):
        if type=="minion":
            self.image = minion_animation
        elif type=="harake":
            pass
        self.coords = coords
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()
        self.rect = pygame.Rect(coords[0], coords[1], self.image[0].get_width(), self.image[0].get_height())

        screen.blit(self.image[0], coords)

    def draw_enemy(self):
        screen.blit(self.image[0], self.coords)
        #pygame.draw.rect(screen, (255,0,0), self.rect)

    def mov(self, sens):
        if sens=="right":
            self.coords[0] += vel
        elif sens=="left":
            self.coords[0] -= vel

    def get_rect(self):
        return self.rect


class Player:
    def __init__(self, anim_list):
        self.sens = sens[-1]
        self.animation = anim_list
        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(
        ), self.animation[walk_animation_index].get_height())

    def draw_player(self):
        if sens[-1] == "right":
            #pygame.draw.rect(screen, (255,0,0), (coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height()), 50)
            screen.blit(self.animation[walk_animation_index],
                        (self.player_rect.x, self.player_rect.y))
        elif sens[-1] == "left":
            #pygame.draw.rect(screen, (255,0,0), (coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height()), 50)
            screen.blit(pygame.transform.flip(
                self.animation[walk_animation_index], True, False),  (self.player_rect.x, self.player_rect.y))
        else:
            #pygame.draw.rect(screen, (255,0,0), (coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height()), 50)
            screen.blit(self.animation[walk_animation_index],
                        (self.player_rect.x, self.player_rect.y))
        

    def jump(self, keys, event):
        global jump, collide_right, jump_traj
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                jump = True
                screen.blit(bg_img, (0, 0))
                draw_world(x_coords_of_all_blocks, y_coords_of_all_blocks)
                minion1.draw_enemy()
                minion2.draw_enemy()
                

                for i in range(5):
                    if jump:
                        jump_traj = "up"
                        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width < 860:
                            #coordinates["xc"] += vel
                            for i in range(len(x_coords_of_all_blocks)):
                                x_coords_of_all_blocks[i] -= vel
                        if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"] > 0:
                            #coordinates["xc"] -= vel
                            for i in range(len(x_coords_of_all_blocks)):
                                x_coords_of_all_blocks[i] += vel
                        coordinates["yc"] -= jumpvel
                        pygame.draw.rect(
                            screen, (0, 0, 255), (obst_list[0][0], obst_list[0][1], obst_list[0][2], obst_list[0][3]))
                        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(
                        ), self.animation[walk_animation_index].get_height())
                        self.draw_player()
                        pygame.display.update()
                        screen.blit(bg_img, (0, 0))
                        draw_world(x_coords_of_all_blocks, y_coords_of_all_blocks)
                        minion1.draw_enemy()
                        minion2.draw_enemy()
                        collision(dahyeman, coords_list, brick_list)
                        print(coordinates["yc"]+dahyeman.get_rect().height+6)
                        time.sleep(0.03)

                for i in range(5):
                    if jump:
                        jump_traj = "down"
                        keys = pygame.key.get_pressed()
                        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width < 860:
                            #coordinates["xc"] += vel
                            for i in range(len(x_coords_of_all_blocks)):
                                x_coords_of_all_blocks[i] -= vel
                        if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"] > 0:
                            #coordinates["xc"] -= vel
                            for i in range(len(x_coords_of_all_blocks)):
                                x_coords_of_all_blocks[i] += vel
                        if (coordinates["yc"] + jumpvel) == oy or (coordinates["yc"] - jumpvel) == oy:
                            break
                        coordinates["yc"] += jumpvel
                        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(
                        ), self.animation[walk_animation_index].get_height())
                        self.draw_player()
                        pygame.display.update()
                        screen.blit(bg_img, (0, 0))
                        draw_world(x_coords_of_all_blocks, y_coords_of_all_blocks)
                        minion1.draw_enemy()
                        minion2.draw_enemy()
                        collision(dahyeman, coords_list, brick_list)
                        time.sleep(0.03)
                jump_traj = ""

    def mov(self, keys):
        global walk_animation_index, walking, collide_right, collide_left
        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width < 860:
            collide_left = False
            if not collide_right:
            #coordinates["xc"] += vel
                sens.append('right')
                for i in range(len(x_coords_of_all_blocks)):
                    x_coords_of_all_blocks[i] -= vel
                if walk_animation_index+1 < len(self.animation):
                    walking = True
                    walk_animation_index += 1
                    time.sleep(0.06)
                else:
                    walk_animation_index = 0
        elif ((keys[pygame.K_a]) or (keys[pygame.K_LEFT])) and check_x_coords(coordinates["xc"]-vel, obst_list) is True and coordinates["xc"] > 0:
            collide_right = False
            if not collide_left:
                #coordinates["xc"] -= vel
                sens.append('left')
                for i in range(len(x_coords_of_all_blocks)):
                    x_coords_of_all_blocks[i] += vel
                if walk_animation_index+1 < len(self.animation):
                    walking = True
                    walk_animation_index += 1
                    time.sleep(0.06)
                else:
                    walk_animation_index = 0
        else:
            walking = False

    def get_rect(self):
        return self.player_rect
    
def collision(player, brick_coords, bricks):
    global collide_right, collide_left, jump, on_brick
    for i in range(len(brick_list)):
        brick_list[i].x = brick_coords[i][0]
        
    for i in bricks:
        if sens[-1]=="right":
            if player.get_rect().colliderect(i):
                    if player.get_rect().x+player.get_rect().width>i.x:
                        collide_right = True
                        for j in range(len(x_coords_of_all_blocks)):
                            x_coords_of_all_blocks[j] += 5

            if player.get_rect().y+66==i.y:
                if i.x<player.get_rect().x+player.get_rect().width<i.x+i.width and jump_traj=="down":
                    jump = False
                    coordinates["yc"] += 6
                    collide_right = False
                    for j in brick_list:
                        if j in on_brick_list and j.y!=i.y:
                            on_brick_list.remove(j)
                        if j.y==i.y:
                            on_brick_list.append(j)
                    on_brick = True
                    break

        elif sens[-1]=="left":
            if player.get_rect().colliderect(i):
                    if player.get_rect().x<i.x+i.width:
                        collide_left = True
                        for j in range(len(x_coords_of_all_blocks)):
                            x_coords_of_all_blocks[j] -= 5
                            
            if player.get_rect().y+66==i.y :
                if i.x<player.get_rect().x<i.x+i.width and jump_traj=="down":
                    jump = False
                    coordinates["yc"] += 6
                    for j in brick_list:
                        if j in on_brick_list and j.y!=i.y:
                            on_brick_list.remove(j)
                        if j.y==i.y:
                            on_brick_list.append(j)
                    on_brick = True
                    break



run = True


### MAIN LOOP ###
while run:
    minion1 = Enemy("minion", [500, 425])
    minion2 = Enemy("minion", [700, 335])
    minion_list = [minion1, minion2]
    dahyeman = Player(walking_list)
    keys = pygame.key.get_pressed()
    pygame.time.delay(1)
    draw_world(x_coords_of_all_blocks,y_coords_of_all_blocks)
    #print(coords_list)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        dahyeman.jump(keys, event)
    if not walking:
        walk_animation_index = 0
    keys = pygame.key.get_pressed()
    dahyeman.mov(keys)
    minion1.draw_enemy()
    minion2.draw_enemy()
    dahyeman.draw_player()
    collision(dahyeman, coords_list, brick_list)
    #print(on_brick_list)
    pygame.display.update()
    screen.blit(bg_img, (0, 0))

pygame.quit()
