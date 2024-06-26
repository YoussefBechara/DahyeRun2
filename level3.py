import pygame, sys
import pygame.freetype
from pygame import mixer
import time
import os
from button import Button
from pygame.locals import *
import random
pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 1024)

#defining game variables
screen_width, screen_height = 1000,500
screen = pygame.display.set_mode((screen_width, screen_height))
NORTHERN_BG = pygame.image.load('images/northernlights_bg.jpg')
NORTHERN_BG_img = pygame.transform.scale(NORTHERN_BG,(300,150))
lightning_BG = pygame.image.load('images/lightning_bg.png')
lightning_BG_img = pygame.transform.scale(lightning_BG,(1000,500))
winter_BG = pygame.image.load('images/winter_bg.png')
winter_BG_img = pygame.transform.scale(winter_BG,(1000,500))
spooky_BG = pygame.image.load('images/spooky_bg.png')
spooky_BG_img = pygame.transform.scale(spooky_BG,(300,150))
sunset_BG = pygame.image.load('images/sunset_bg.png')
sunset_BG_img = pygame.transform.scale(sunset_BG,(300,150))
bg_list = []
#GAMEOVER MENU
BG = pygame.image.load("images/northernlights_bg.jpg")

def restart_func():
    screen.blit(BG, (0,0))
    player_coords_change[0] += 1
    for i in range(len(x_of_all_enemies)):
        x_of_all_enemies.pop()
        y_of_all_enemies.pop()
    get_coords_of_all_enemies(x_of_all_enemies,y_of_all_enemies,type_of_minion,world_data,vel_blocks)
    vel_blocks.pop()
    vel_blocks.append(0)
    from level1_restart import main_loopz
    main_loopz()
    
def back_to_menu():
    from main import main_menu
    main_menu(len(coins_collected), bg_img)

def game_over():
    run = True
    pygame.display.set_caption('Game Over')
    while run:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("GAME OVER", True, "red")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_width//2, screen_height//5))

        RESTART_BUTTON = Button(image=pygame.image.load("assets/level_bg.png"), pos=(screen_width//2, screen_height - screen_height//2), 
                            text_input="RESTART", font=get_font(75), base_color="#d7fcd4", hovering_color="green")
        MENU_BUTTON = Button(image=pygame.image.load("assets/shop_bg.png"), pos=(screen_width//4,  screen_height - screen_height//5), 
                            text_input="MENU", font=get_font(75), base_color="#d7fcd4", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width - screen_width//3.5, screen_height - screen_height//5), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="green")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [RESTART_BUTTON, MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                    restart_func()
                    run = False
                    break
                if MENU_BUTTON.checkForInput (MENU_MOUSE_POS):
                    back_to_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
    
coordinates = {
    "xc": 64,
    "yc": 420
}

global vel_blocks
vel_blocks = [0]
player_coords_change = [0]
tile_size = 30
enemy_size = 50
brick = pygame.image.load('images/grass.png')
global brick_img
brick_img = pygame.transform.scale(brick, (tile_size, tile_size))
harake_minion = pygame.image.load('images/harakeminion1.png')
global harake_minion_img
harake_minion_img = pygame.transform.scale(harake_minion, (enemy_size, enemy_size))
hezb_minion = pygame.image.load('images/hezbminion1.png')
global hezb_minion_img 
hezb_minion_img = pygame.transform.scale(hezb_minion, (enemy_size, enemy_size))
width, height, vel, jumpvelup, jumpveldown, enemy_vel = 30, 60, 20, 18, 4, 3
obst_width, obst_height = 80, 90
ox, oy = 800, 500
sens = ['hi']
run = True
obst_list = [[800, 500, 80, 70], [100, 300, 30, 70]]
# my idea is to make every obstacle coordinates stored in a list then check if this coodinate in list
direction = 0

#graphical loading
hezb_minion_image_standing = pygame.image.load(os.path.join("images/hezbminion1.png"))
hezb_minion_standing = pygame.transform.scale(hezb_minion_image_standing, (60, 55.375))
hezb_minion1_image = pygame.image.load(os.path.join("images/hezbminion2.png"))
hezb_minion_anim_1 = pygame.transform.scale(hezb_minion1_image, (enemy_size, enemy_size))
hezb_minion2_image = pygame.image.load(os.path.join("images/hezbminion3.png"))
hezb_minion_anim_2 = pygame.transform.scale(hezb_minion2_image, (enemy_size, enemy_size))
hezb_minion_animation = [hezb_minion_anim_1, hezb_minion_anim_2]
hezb_minion_index = []

harake_minion_image_standing = pygame.image.load(os.path.join("images/harakeminion1.png"))
harake_minion_standing = pygame.transform.scale(harake_minion_image_standing, (60, 55.375))
harake_minion1_image = pygame.image.load(os.path.join("images/harakeminion2.png"))
harake_minion_anim_1 = pygame.transform.scale(harake_minion1_image, (enemy_size, enemy_size))
harake_minion2_image = pygame.image.load(os.path.join("images/harakeminion3.png"))
harake_minion_anim_2 = pygame.transform.scale(harake_minion2_image, (enemy_size, enemy_size))
harake_minion_animation = [harake_minion_anim_1, harake_minion_anim_2]
harake_minion_index = []

dahyeman1_image = pygame.image.load(os.path.join("images/dahyeman1.png"))
dahyeman1 = pygame.transform.scale(dahyeman1_image, (65, 60.45))
dahyeman2_image = pygame.image.load(os.path.join("images/dahyeman2.png"))
dahyeman2 = pygame.transform.scale(dahyeman2_image, (65 ,60.45))
dahyeman3_image = pygame.image.load(os.path.join("images/dahyeman3.png"))
dahyeman3 = pygame.transform.scale(dahyeman3_image, (40, 60.45))
dahyeman4_image = pygame.image.load(os.path.join("images/dahyeman4.png"))
dahyeman4 = pygame.transform.scale(dahyeman4_image, (65, 60.45))
walking_list = [dahyeman1, dahyeman2, dahyeman3, dahyeman4]
walk_animation_index = 0
walking = False

dahyemanjump1_img = pygame.image.load(os.path.join("images/dahyemanjump1.png"))
dahyemanjump1 = pygame.transform.scale(dahyemanjump1_img, (80, 100))
dahyemanjump2_img = pygame.image.load(os.path.join("images/dahyemanjump2.png"))
dahyemanjump2 = pygame.transform.scale(dahyemanjump2_img, (65, 60.45))
jumping_list = [dahyemanjump1, dahyemanjump2]
jump_animation_index = 0

dahyeman1_p_image = pygame.image.load(os.path.join("images/powered_mario1.png"))
dahyeman1_p = pygame.transform.scale(dahyeman1_p_image, (90, 80))
dahyeman2_p_image = pygame.image.load(os.path.join("images/powered_mario2.png"))
dahyeman2_p = pygame.transform.scale(dahyeman2_p_image, (90, 80))
dahyeman3_p_image = pygame.image.load(os.path.join("images/powered_mario3.png"))
dahyeman3_p = pygame.transform.scale(dahyeman3_p_image, (90, 80))
dahyeman4_p_image = pygame.image.load(os.path.join("images/powered_mario4.png"))
dahyeman4_p = pygame.transform.scale(dahyeman4_p_image, (90, 80))

mushroom = pygame.image.load('images/tabouleh.png')
mushroom_size = 40
mushroom_img = pygame.transform.scale(mushroom, (mushroom_size,mushroom_size))
saved_walking_animation = [dahyeman1, dahyeman2, dahyeman3, dahyeman4]
saved_jumping_list = [dahyemanjump1, dahyemanjump2]
powered_jumping_list = [dahyeman1_p, dahyeman4_p]
is_powered_up = [0]
power_up_animation = [dahyeman4_p, dahyeman2_p,dahyeman3_p,dahyeman1_p]
def power_up():
    is_powered_up.append(0)
    for i in range(len(walking_list)):
        del walking_list[i]
        walking_list.insert(i, power_up_animation[i])
    for i in range(len(jumping_list)):
        del jumping_list[i]
        jumping_list.insert(i, powered_jumping_list[i])
    coordinates['yc'] -= 17
def power_off(x):
    is_powered_up.append(0)
    for i in range(len(saved_walking_animation)):
        del walking_list[i]
        walking_list.insert(i, saved_walking_animation[i])
    for i in range(len(saved_jumping_list)):
        del jumping_list[i]
        jumping_list.insert(i, saved_jumping_list[i])
    coordinates['xc'] -=100
    coordinates['yc'] += 17
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



screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dahye Run')
pygame.display.set_icon(pygame.image.load("images/hezbminion1.png"))

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

#DRAWING SECTION
bg_img = pygame.image.load('images/background.png')

class World:
    def __init__(self, data, vel_blocks):
        self.drawings_list = []

        # load images
        row_count = 0
        for r in data:
            col_count = 0
            for c in r:
                if c == 1:
                    img_rect = brick_img.get_rect()
                    img_rect.x = col_count * tile_size + int(vel_blocks[0])
                    img_rect.y = row_count * tile_size
                    c = (brick_img, img_rect)
                    self.drawings_list.append(c)
                col_count += 1
            row_count += 1
    def make(self, data):
        self.drawings_list = []

        # load images
        row_count = 0
        for r in data:
            col_count = 0
            for c in r:
                if c == 1:
                    img_rect = brick_img.get_rect()
                    img_rect.x = col_count * tile_size + int(vel_blocks[0])
                    img_rect.y = row_count * tile_size
                    if (0-tile_size<img_rect.x<screen_width+tile_size) and (0-tile_size<img_rect.y<screen_height+tile_size):
                        c = (brick_img, img_rect)
                        self.drawings_list.append(c)
                col_count += 1
            row_count += 1
    def draw(self):
        for tile in self.drawings_list:
            screen.blit(tile[0], tile[1])
#Yo adel if you seeing these you be a spoiled kid
world_data = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 7, 7, 7, 7, 0, 0, 0,0, 1, 1, 1, 1, 1, 1, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0,0,1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
] # 14  29
world = World(world_data, vel_blocks)
evels_added = []
type_of_minion = []
x_of_all_enemies = []
y_of_all_enemies = []
sens_of_enemies = []
enemies_state_list = []
enemies_randomly_walking = []

def get_coords_of_all_enemies(x_list,y_list,type, data, vel_blocks):
    x_list.clear()
    y_list.clear()
    type.clear()
    row_count = 0
    for r in data:
            col_count = 0
            for c in r:
                if c==2 or c==3:
                    x_list.append(col_count*tile_size + int(vel_blocks[0]))
                    y_list.append(row_count*tile_size)  
                    if c==2:
                        type.append('harake')
                    else:
                        type.append('hezb')                  
                col_count += 1
            row_count += 1

get_coords_of_all_enemies(x_of_all_enemies,y_of_all_enemies,type_of_minion,world_data,vel_blocks)
evels_added = []
for i in range(len(x_of_all_enemies)):
    evels_added.append([])
    enemies_randomly_walking.append([])
def assign_random_state(list,ex_list):
    list.clear()
    for i in range(len(ex_list)):
        num = random.randint(1,3)
        if num == 1:
            list.append([0, 'standing'])
        elif num==2:
            list.append([0, 'left'])
        else:
            list.append([0, 'right'])
assign_random_state(enemies_randomly_walking,x_of_all_enemies)
    
def kill_enemy(x, y, index): 
    evel = 0
    type_index = 0
    evels_add = evels_added[index]
    for i in range(len(evels_add)):
        evel += evels_add[i]
    xc , yc = ((x+evel)-vel_blocks[0])//tile_size,y//tile_size
    for i in range(-5, 20):
        print(yc,xc+i)
        if (world_data[yc][xc+i] == 3) or (world_data[yc][xc+i] == 2):
            del world_data[yc][xc+i]
            world_data[yc].insert(xc+i, 0)
            print(yc, xc+i,world_data[yc][xc+i])
            for i in range(len(x_of_all_enemies)):
                if x_of_all_enemies[i] == x:
                    break
                type_index += 1
            x_of_all_enemies.remove(x)
            y_of_all_enemies.remove(y)
            del type_of_minion[type_index]
            break

def enemy_ai_move(px,py, ex_list,ey_list, evel,sens_list):
    jumprect_fall = pygame.Rect(coordinates["xc"], coordinates["yc"],jumping_list[jump_animation_index+1].get_width(),jumping_list[jump_animation_index+1].get_height() )
    sens_list.clear()
    enemies_state_list.clear()
    for i in range(len(ex_list)):
        try:
            if (ex_list[i]-400<px<ex_list[i]+400) and (ey_list[i]-100<py<ey_list[i]+100):
                if px > ex_list[i]:
                    ex_list[i] += evel
                    evels_added[i].append(-1*evel)
                    sens_list.insert(i, 'right')
                    enemies_state_list.append('moving')
                    if ((screen_width//5)*3.35<=px<=screen_width) and (walking == True) and (sens[-1] =='right'):
                        ex_list[i] -=evel*3
                        evels_added[i].append(3)
                    if (0<=coordinates['xc']<=(screen_width//4)+(screen_width//67)) and (walking == True) and (sens[-1] =='left'):
                        ex_list[i] +=evel*3
                        evels_added[i].append(-3)
                elif (ex_list[i]-jumprect_fall.width*0.5<=jumprect_fall.x) and (ey_list[i]-(jumprect_fall.height//2)>=jumprect_fall.y>=ey_list[i]-jumprect_fall.height):
                    enemies_state_list.append('standing')
                    kill_enemy(ex_list[i], ey_list[i], i)
                elif (ex_list[i]-jumprect_fall.width*0.8<=px<=ex_list[i]+width*2) and (ey_list[i]-enemy_size<py<ey_list[i]+enemy_size) :
                    enemies_state_list.append('standing')
                    if len(is_powered_up) %2!=0:
                        game_over()
                    else:
                        power_off(coordinates['xc'])
                    
                elif px-width<ex_list[i]<px+width:
                    continue
                elif px == ex_list[i]:
                    sens_list.insert(i, sens)
                else:
                    ex_list[i] -= evel
                    enemies_state_list.append('moving')
                    evels_added[i].append(1*evel)
                    sens_list.insert(i, 'left')
                    if (0<=coordinates['xc']<=(screen_width//4)+(screen_width//67)) and (walking == True) and (sens[-1]=='left') :
                        ex_list[i] +=evel*3
                        evels_added[i].append(-3*evel)
                    elif ((screen_width//5)*3.35<=px<=screen_width) and (walking == True) and (sens[-1] =='right'):
                        ex_list[i] -=evel*3
                        evels_added[i].append(3*evel)
            else:
                for r in range(len(enemies_randomly_walking)):
                    if enemies_randomly_walking[r][0] < 50:
                        if enemies_randomly_walking[r][1] == 'left':
                            ex_list[i] -= evel
                            enemies_state_list.append('moving')
                            evels_added[i].append(1*evel)
                            sens_list.insert(i, 'left')
                        elif enemies_randomly_walking[r][1] == 'right':
                            ex_list[i] += evel
                            evels_added[i].append(-1*evel)
                            sens_list.insert(i, 'right')
                            enemies_state_list.append('moving')
                
                        num = enemies_randomly_walking[r][0]
                        del enemies_randomly_walking[r][0]
                        enemies_randomly_walking[r].insert(0, num+1)
                    else:
                        assign_random_state(enemies_randomly_walking,ex_list)
        except:
            h = 1
     
enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
def draw_enemies(x_list,y_list,type,sens_list, state):
    enemy_coords = list(zip(x_list, y_list))
    enemy_tuple = list(zip(type, enemy_coords))
    for i in range(len(enemy_tuple)):
        if enemy_tuple[i][0] == 'harake':
            try:
                if sens_list[i] == 'left':
                    if state[i] == 'moving':
                        screen.blit(harake_minion_animation[len(harake_minion_index)-1],enemy_tuple[i][-1])
                        harake_minion_index.append(0)
                        if len(harake_minion_index) == 3:
                            harake_minion_index.clear()
                    else:
                        screen.blit(hezb_minion_img, enemy_tuple[i][-1])
                        
                else:
                    if state[i] == 'moving':
                        screen.blit(pygame.transform.flip(harake_minion_animation[len(harake_minion_index) - 1], True, False),enemy_tuple[i][-1])
                        harake_minion_index.append(0)
                        if len(harake_minion_index) == 3:
                            harake_minion_index.clear()
                    else:
                        
                        screen.blit(pygame.transform.flip(harake_minion_img, True, False),  (enemy_tuple[i][-1]))
            except:
                screen.blit(harake_minion_img, enemy_tuple[i][-1])
        elif enemy_tuple[i][0] == 'hezb':
            try:
                if sens_list[i] == 'left':
                    if state[i] == 'moving':
                        screen.blit(hezb_minion_animation[len(hezb_minion_index)-1],enemy_tuple[i][-1])
                        hezb_minion_index.append(0)
                        if len(hezb_minion_index) == 3:
                            hezb_minion_index.clear()
                    else:
                        screen.blit(hezb_minion_img, enemy_tuple[i][-1])
                        
                else:
                    if state[i] == 'moving':
                        screen.blit(pygame.transform.flip(hezb_minion_animation[len(hezb_minion_index) - 1], True, False),enemy_tuple[i][-1])
                        hezb_minion_index.append(0)
                        if len(hezb_minion_index) == 3:
                            hezb_minion_index.clear()
                    else:
                        
                        screen.blit(pygame.transform.flip(hezb_minion_img, True, False),  (enemy_tuple[i][-1]))
            except:
                screen.blit(hezb_minion_img, enemy_tuple[i][-1])
        if state == 'moving':
                print('hi')
                hezb_minion_index.append(0)
                if len(hezb_minion_index) == 3:
                    hezb_minion_index.clear()

x_of_all_coins, y_of_all_coins = [], []
coins_collected = []
def get_coords_of_all_element(x_list,y_list, data, vel_blocks,element):
    x_list.clear()
    y_list.clear()
    row_count = 0
    for r in data:
            col_count = 0
            for c in r:
                if c==7 and (element == 'coin' or element == 'coins'):
                    x_list.append(col_count*tile_size + int(vel_blocks[0]))
                    y_list.append(row_count*tile_size)
                elif c==9 and (element =='mushroom' or element == 'mushrooms'):
                    x_list.append(col_count*tile_size + int(vel_blocks[0]))
                    y_list.append(row_count*tile_size)                 
                col_count += 1
            row_count += 1
coin = pygame.image.load('images/coin.png')
coin_image = pygame.transform.scale(coin, (tile_size,tile_size))
get_coords_of_all_element(x_of_all_coins,y_of_all_coins,world_data,vel_blocks, 'coin')
def check_element_collected(px,py,x_list,y_list, element):
    for i in range(len(x_list)):
            if (x_list[i]-width*1.8<=px<=x_list[i]+width*0.7) and (y_list[i]-enemy_size<py<y_list[i]+enemy_size):
                if element == 'coin':
                    coins_collected.append(1)
                elif element == 'mushroom' and len(is_powered_up)%2!= 0:
                    power_up()
                coords = (x_list[i]//tile_size-(vel_blocks[0]//tile_size),y_list[i]//tile_size)
                del world_data[coords[1]][coords[0]]
                world_data[coords[1]].insert(coords[0], 0)
def draw_coins(x_list,y_list):
    get_coords_of_all_element(x_of_all_coins,y_of_all_coins,world_data,vel_blocks, 'coin')
    coin_coords = list(zip(x_list, y_list))
    for i in range(len(coin_coords)):
            screen.blit(coin_image, coin_coords[i])
            
time_clock = 500#in secs
time_passed = []
time_passed_int = len(time_passed)
def draw_scoreboard():
    time_passed_int = len(time_passed)
    time_text = get_font(20).render(f"Time:{time_clock-time_passed_int//18}", True, "red")
    coin_text = get_font(20).render(f"Coins:{len(coins_collected)}", True, "yellow")
    screen.blit(time_text, (screen_width*0.8,screen_height//10))
    screen.blit(coin_text, (screen_width*0.05,screen_height//10))

x_of_all_mushrooms, y_of_all_mushrooms = [],[]
get_coords_of_all_element(x_of_all_mushrooms,y_of_all_mushrooms,world_data,vel_blocks,'mushroom')
def draw_mushrooms(x_list,y_list):
    get_coords_of_all_element(x_of_all_mushrooms,y_of_all_mushrooms,world_data,vel_blocks, 'mushroom')
    mushroom_coords = list(zip(x_list, y_list))
    for i in range(len(mushroom_coords)):
            screen.blit(mushroom_img, mushroom_coords[i])
            
def draw_everything():
    screen.blit(bg_img, (0, 0))
    world.make(world_data)
    world.draw()
    draw_coins(x_of_all_coins,y_of_all_coins)
    draw_mushrooms(x_of_all_mushrooms,y_of_all_mushrooms)
    draw_enemies(x_of_all_enemies,y_of_all_enemies, type_of_minion,sens_of_enemies,enemies_state_list)
    draw_scoreboard()
    #print(enemies_state_list)

    
    
class Player:
    def __init__(self, anim_list,jumplist):
        self.sens = sens[-1]
        self.animation = anim_list
        self.jump_animation = jumplist
        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height())
        self.jumprect_rise = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index].get_width(),self.jump_animation[jump_animation_index].get_height() )
        self.jumprect_fall = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index+1].get_width(),self.jump_animation[jump_animation_index+1].get_height() )
    def horizontal_collision(self):
        player = self.player_rect
        player.rect.x += player.direction.x * vel
        for tile in self.tiles_list():
            if tile.rect.colliderect(player)
    def draw_jump(self, phase):
        if phase == "rise":
            if sens[-1] == "right":
                screen.blit(self.jump_animation[jump_animation_index],(self.jumprect_rise.x, self.jumprect_rise.y))
            elif sens[-1] == "left":
                screen.blit(pygame.transform.flip(self.jump_animation[jump_animation_index], True, False),  (self.jumprect_rise.x, self.jumprect_rise.y))
        elif phase == 'fall':
            if sens[-1] == "right":
                screen.blit(self.jump_animation[jump_animation_index+1],(self.jumprect_fall.x, self.jumprect_fall.y))
            elif sens[-1] == "left":
                screen.blit(pygame.transform.flip(self.jump_animation[jump_animation_index+1], True, False),  (self.jumprect_fall.x, self.jumprect_fall.y))
    def draw_player(self):
        if sens[-1] == "right":
            screen.blit(self.animation[walk_animation_index],(self.player_rect.x, self.player_rect.y))
        elif sens[-1] == "left":
            screen.blit(pygame.transform.flip(self.animation[walk_animation_index], True, False),  (self.player_rect.x, self.player_rect.y))
        else:
            screen.blit(self.animation[walk_animation_index],(self.player_rect.x, self.player_rect.y))
        # pygame.draw.rect(screen, (255,0,0), (coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height()), 50)
    def mov(self, keys, vel_blocks, phase):
        global walk_animation_index, walking
        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width < 860:
            coordinates["xc"] += vel
            sens.append('right')
            if (0<=coordinates['xc']<=screen_width//4) or ((screen_width//5)*3.5<=coordinates['xc']<=screen_width):
                vel_blocks[0] -= vel//2
                if ((screen_width//5)*3.5<=coordinates['xc']<=screen_width):
                    coordinates["xc"] -= vel
            if walk_animation_index+1 < len(self.animation):
                walking = True
                walk_animation_index += 1
                if phase == 'walking':
                    time.sleep(0.03)
                else:
                    time.sleep(0.006)
            else:
                walk_animation_index = 0
        elif ((keys[pygame.K_a]) or (keys[pygame.K_LEFT])) and check_x_coords(coordinates["xc"]-vel, obst_list) is True and coordinates["xc"] > 0:
            coordinates["xc"] -= vel
            sens.append('left')
            if (0<=coordinates['xc']<=screen_width//4) or ((screen_width//4)*3.5<=coordinates['xc']<=screen_width):
                vel_blocks[0] += vel//2
                if (0<=coordinates['xc']<=screen_width//4):
                    coordinates["xc"] += vel
            if walk_animation_index+1 < len(self.animation):
                walking = True
                walk_animation_index += 1
                if phase == 'walking':
                    time.sleep(0.03)
                else:
                    time.sleep(0.006)
            else:
                walk_animation_index = 0
        else:
            walking = False
    
    def double_jump(self, vel_blocks, is_forced):
        jumpvelup = 32
        jumpveldown = 7.5
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.blit(bg_img, (0, 0))
                    enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                    check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
                    check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
                    draw_everything()
                    time_passed.append(0)
                    for i in range(8):
                        keys = pygame.key.get_pressed()
                        self.mov(keys, vel_blocks, 'jumping')
                        coordinates["yc"] -= jumpvelup//2
                        jumpvelup -= 3.9
                        enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
                        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
                        self.jumprect_rise = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index].get_width(),self.jump_animation[jump_animation_index].get_height() )
                        self.draw_jump('rise')
                        pygame.display.update()
                        time_passed.append(0)
                        draw_everything()
                        time.sleep(0.02)
                    
                    for i in range(8):
                        keys = pygame.key.get_pressed()
                        self.mov(keys, vel_blocks, 'jumping')
                        coordinates["yc"] += jumpveldown//2
                        jumpveldown += 3.3
                        enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
                        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
                        self.jumprect_fall = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index+1].get_width(),self.jump_animation[jump_animation_index+1].get_height() )
                        self.draw_jump('fall')
                        pygame.display.update()
                        time_passed.append(0)
                        draw_everything()
                        time_passed.append(0)
                        time.sleep(0.02)
    def jump(self,keys, event, vel_blocks):
        has_jumped = False
        jumpvelup = 32
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
                check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
                draw_everything()
                time_passed.append(0)
                for i in range(8):
                    keys = pygame.key.get_pressed()
                    self.mov(keys, vel_blocks, 'jumping')
                    coordinates["yc"] -= jumpvelup
                    jumpvelup -= 4
                    check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins,  'coin')
                    check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
                    enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                    self.jumprect_rise = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index].get_width(),self.jump_animation[jump_animation_index].get_height() )
                    self.draw_jump('rise')
                    pygame.display.update()
                    time_passed.append(0)
                    draw_everything()
                    time.sleep(0.02)
                has_jumped = True
        if has_jumped ==True:
            self.double_jump(vel_blocks,'not_forced')
            self.fall(keys)
        
    def fall(self,keys):
        jumpveldown = 7.5
        for i in range(8):
                    keys = pygame.key.get_pressed()
                    self.mov(keys, vel_blocks, 'jumping')
                    coordinates["yc"] += jumpveldown
                    jumpveldown += 3
                    enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                    self.jumprect_fall = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index+1].get_width(),self.jump_animation[jump_animation_index+1].get_height() )
                    self.draw_jump('fall')
                    pygame.display.update()
                    time_passed.append(0)
                    draw_everything()
                    time.sleep(0.02)
                    
        
    

    def get_rect(self):
        return self.player_rect.x, self.player_rect.y, self.player_rect.width, self.player_rect.height



# MAIN LOOP
def main_loop(bg):
    global walk_animation_index
    walk_animation_index = 0
    run = True
    while run:
        double_jump_count = 0
        dahyeman = Player(walking_list, jumping_list)
        keys = pygame.key.get_pressed()
        pygame.time.delay(10)
        draw_everything()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            dahyeman.jump(keys, event, vel_blocks)
        if not walking:
            walk_animation_index = 0
        keys = pygame.key.get_pressed()
        dahyeman.mov(keys, vel_blocks, 'walking')
        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
        enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
        if player_coords_change[0] %2!=0:
            coordinates['xc'] = 64
            coordinates["yc"] = 420
            vel_blocks[0] = 0
            player_coords_change[0] += 1
        dahyeman.draw_player()
        time_passed.append(0)
        pygame.display.update()


    pygame.quit()
    
main_loop(bg_img)

#NEVER GONNA GIVE YOU UP , NEVER GONNA LET YOU DOWN , NEVER GONNA RUNNN AROUND AND DESERT YOU!!!!!
#GET