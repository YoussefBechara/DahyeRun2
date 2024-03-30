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
clock = pygame.time.Clock()
#GAMEOVER MENU
BG = pygame.image.load("images/northernlights_bg.jpg")
thing = 0
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
    "yc": 200 #420
}

jump = False
jump_traj = ""
global fall_count
fall_count = []
jump_count = []
collide_right = False
collide_left = False
on_brick = []
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

player_width , player_height = 70, 90
dahyeman1_image = pygame.image.load(os.path.join("images/dahyeman1.png"))
dahyeman1 = pygame.transform.scale(dahyeman1_image, (player_width , player_height))
dahyeman2_image = pygame.image.load(os.path.join("images/dahyeman2.png"))
dahyeman2 = pygame.transform.scale(dahyeman2_image, (player_width , player_height))
dahyeman3_image = pygame.image.load(os.path.join("images/dahyeman3.png"))
dahyeman3 = pygame.transform.scale(dahyeman3_image, (player_width , player_height))
dahyeman4_image = pygame.image.load(os.path.join("images/dahyeman4.png"))
dahyeman4 = pygame.transform.scale(dahyeman4_image, (player_width , player_height))
walking_list = [dahyeman1, dahyeman2, dahyeman3, dahyeman4]
walk_animation_index = 0
walking = False

dahyemanjump1_img = pygame.image.load(os.path.join("images/dahyemanjump1.png"))
dahyemanjump1 = pygame.transform.scale(dahyemanjump1_img, (player_width , player_height))
dahyemanjump2_img = pygame.image.load(os.path.join("images/dahyemanjump2.png"))
dahyemanjump2 = pygame.transform.scale(dahyemanjump2_img, (player_width , player_height))
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


world_data = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 0, 0, 0,0, 1, 1, 1, 1, 1, 1, 1, 0, 7, 7, 0, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
] # 14  29
brick_list = []
x_coords_of_all_blocks = []
y_coords_of_all_blocks = []
col_counts=[]
coords_of_all_enemies_kill = []
row_count = 0
for r in world_data:
    col_count = 0
    for c in r:
            if c == 1:
                img = pygame.transform.scale(brick, (tile_size, tile_size))
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                col_counts.append(col_count)
                x_coords_of_all_blocks.append(img_rect.x)
                img_rect.y = row_count * tile_size
                y_coords_of_all_blocks.append(img_rect.y)
                brick_list.append(img_rect)
            elif c ==2 or c==3:
                coords_of_all_enemies_kill.append((col_count,row_count))
            col_count += 1
    row_count += 1
#Yo adel if you seeing these you be a spoiled kid
def update_world(x_list):
    for i in range(len(x_list)):
        x_list[i] = col_counts[i] * tile_size + int(vel_blocks[0])
def draw_world(x_coords, y_coords):
    global coords_list
    coords_list = list(zip(x_coords,y_coords))
    for i in range(len(x_coords)):
        screen.blit(img, coords_list[i])
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
    del x_of_all_enemies[index]
    del y_of_all_enemies[index]
    del world_data[coords_of_all_enemies_kill[index][1],coords_of_all_enemies_kill[index][0]]
    dahyeman = Player(walking_list, jumping_list, 'yes')
    #dahyeman.double_jump(vel_blocks, 'yes')

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
            if ((screen_width//5)*3.35<=px<=screen_width) and (walking == True) and (sens[-1] =='right'):
                        ex_list[i] -=evel*3
                        evels_added[i].append(3)
            elif (0<=coordinates['xc']<=(screen_width//5)) and (walking == True) and (sens[-1] =='left'):
                        ex_list[i] +=evel*3
                        evels_added[i].append(-3)
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
                #print('hi')
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
    update_world(x_coords_of_all_blocks)
    draw_world(x_coords_of_all_blocks, y_coords_of_all_blocks)
    draw_coins(x_of_all_coins,y_of_all_coins)
    draw_mushrooms(x_of_all_mushrooms,y_of_all_mushrooms)
    draw_enemies(x_of_all_enemies,y_of_all_enemies, type_of_minion,sens_of_enemies,enemies_state_list)
    draw_scoreboard()
    #print(enemies_state_list)

    
    
class Player:
    def __init__(self, anim_list,jumplist, is_forced):
        self.on_brick = False
        self.GRAVITY = 1
        self.y_vel = 0
        self.jump_count = 0
        self.sens = sens[-1]
        self.animation = anim_list
        self.jump_animation = jumplist
        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height())
        self.jumprect_rise = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index].get_width(),self.jump_animation[jump_animation_index].get_height() )
        self.fall_vel = 0
        self.jumprect_fall = pygame.Rect(coordinates["xc"], coordinates["yc"],self.jump_animation[jump_animation_index+1].get_width(),self.jump_animation[jump_animation_index+1].get_height() )
        if is_forced == 'yes':
            self.double_jump(vel_blocks,is_forced)
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
        pygame.draw.rect(screen, (255,255,255),self.jumprect_rise, 2)
    def draw_player(self):
        if sens[-1] == "right":
            screen.blit(self.animation[walk_animation_index],(self.player_rect.x, self.player_rect.y))
        elif sens[-1] == "left":
            screen.blit(pygame.transform.flip(self.animation[walk_animation_index], True, False),  (self.player_rect.x, self.player_rect.y))
        else:
            screen.blit(self.animation[walk_animation_index],(self.player_rect.x, self.player_rect.y))
        pygame.draw.rect(screen, (255,255,255), self.player_rect, 2)
        # pygame.draw.rect(screen, (255,0,0), (coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height()), 50)
    def jurrmp(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_count.append(0)
                coordinates['yc'] -= len(jump_count) *5 -10
                time.sleep(0.02)
    def mov(self, keys, vel_blocks, phase):
        global walk_animation_index, walking
        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width < 860:
            coordinates["xc"] += vel
            sens.append('right')
            if (0<=coordinates['xc']<=screen_width//6) or ((screen_width//5)*3.5<=coordinates['xc']<=screen_width):
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
            if (0<=coordinates['xc']<=screen_width//6) or ((screen_width//4)*3.5<=coordinates['xc']<=screen_width):
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
        if is_forced == 'yes':
            print('h')
        jumpvelup = 32
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN) or is_forced =='yes':
                if (event.key == pygame.K_SPACE)or is_forced =='yes':
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
                        self.collision(self.player_rect, coords_list, brick_list)
                        time.sleep(0.02)
    def jump(self,keys, event, vel_blocks):
        can_doublejump = True
        global jumpjump_traj
        has_jumped = False
        jumpvelup = 32
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fall_count.clear()
                enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
                check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
                check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
                draw_everything()
                time_passed.append(0)
                for i in range(8):
                    self.collision(self.player_rect, coords_list, brick_list)
                    if self.collision(self.player_rect, coords_list, brick_list) == 'collide_up':
                        can_doublejump = False
                        break
                    jump_traj == 'up'
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
            if can_doublejump == True:
                self.double_jump(vel_blocks,'not_forced')
            #self.fall(keys)
    def gravity(self):
        #print(len(on_brick))
        if len(on_brick) % 2 == 0:
            if self.on_brick == False:
            #self.fall_vel += min(1, (self.fall_count / 60) * self.GRAVITY)
            #print(len(fall_count))
                fall_count.append(0)
            #print(len(fall_count))
                coordinates['yc'] += len(fall_count)
        
    def get_rect(self):
        return self.player_rect
    
    def get_hits(self):
        hits = []
        for tile in brick_list:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits
    def collisionsx(self):
        collisions = self.get_hits()
        for tile in collisions:
            if sens[-1] == 'right':
                coordinates['xc'] = tile.rect.left - self.get_rect.width
                
    def collision(self,player, brick_coords, bricks):
            global collide_right, collide_left, jump
            for i in range(len(brick_list)):
                brick_list[i].x = brick_coords[i][0]
            
            for i in bricks:
                if sens[-1]=="right":
                    if self.get_rect().colliderect(i):
                            if i.y-20<=coordinates["yc"]+player_height<= i.y+20: #landed on brick
                                    #print((i.x,self.get_rect().x), (i.y,self.get_rect().y+self.get_rect().height))
                                    coordinates["yc"] = i.y - player_height +1
                                    #print('h')
                                    self.on_brick = True
                                    fall_count.clear()
                                    if len(on_brick) %2 == 0:
                                        on_brick.append(0)
                                    return False
                            else:
                                self.on_brick = False
                            if coordinates['xc']+player_width>i.x:
                                coordinates['xc'] = i.x - player_width - 1
                                if (0<=coordinates['xc']<=screen_width//6) or ((screen_width//5)*3.5<=coordinates['xc']<=screen_width):
                                    vel_blocks[0] += vel//2    
                                #break
                    else:
                        if len(on_brick) %2 != 0:
                            on_brick.append(0)
                        self.on_brick = False
                elif sens[-1]=="left":
                    if self.get_rect().colliderect(i):
                            if i.y-20<coordinates["yc"]+player_height< i.y+20:
                                    #print('hi')
                                    coordinates["yc"] = i.y - player_height+1
                                    self.on_brick = True
                                    fall_count.clear()
                                    if len(on_brick) %2 == 0:
                                        on_brick.append(0)
                                    return False
                            if self.get_rect().x<i.x+i.width:
                                coordinates['xc'] = i.x + self.get_rect().width
                                if (0<=coordinates['xc']<=screen_width//6) or ((screen_width//4)*3.5<=coordinates['xc']<=screen_width):
                                    vel_blocks[0] -= vel//2 
                                break     
                    else:
                        if len(on_brick) %2 != 0:
                            on_brick.append(0)
                        self.on_brick = False
                if (i.x-player_width-10<=coordinates['xc']<=i.x+player_width+10) and (i.y-self.get_rect().height-10<=self.jumprect_rise.y):
                    #print((i.y)+tile_size-14,self.jumprect_rise.y)
                    if (i.y)+tile_size-30<=self.get_rect().y<=i.y+tile_size:
                            coordinates["yc"] = i.y + tile_size
                            #print(coordinates["yc"])
                            return 'collide_up'
                elif self.jumprect_fall.colliderect(i):
                    if i.y-20<self.jumprect_fall.y+self.jumprect_fall.height< i.y+10:
                        coordinates["yc"] = i.y - tile_size*2
                        if len(on_brick) %2 == 0:
                            on_brick.append(0)
                            pass
                        return False
                else:
                    pass
                    

    



# MAIN LOOP
def main_loop(bg):
    global walk_animation_index
    walk_animation_index = 0
    run = True
    while run:
        #print(len(jump_count))
        dahyeman = Player(walking_list, jumping_list, 'no')
        keys = pygame.key.get_pressed()
        pygame.time.delay(10)
        draw_everything()
        if len(jump_count)==8:
            jump_count.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            dahyeman.jurrmp(event)
            #dahyeman.jump(keys, event, vel_blocks)
        if not walking:
            walk_animation_index = 0
        if (0<len(jump_count)<8):
                coordinates['yc'] -= len(jump_count) * 5
                jump_count.append(0)
        keys = pygame.key.get_pressed()
        if (len(jump_count)== 0) or (len(jump_count)<3):
            dahyeman.collision(dahyeman , coords_list, brick_list)
        dahyeman.gravity()
        dahyeman.mov(keys, vel_blocks, 'walking')
        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_coins,y_of_all_coins, 'coin')
        check_element_collected(coordinates["xc"],coordinates["yc"], x_of_all_mushrooms,y_of_all_mushrooms, 'mushroom')
        enemy_ai_move(coordinates["xc"],coordinates["yc"], x_of_all_enemies,y_of_all_enemies, enemy_vel,sens_of_enemies)
        if coordinates['yc'] > screen_height:
            game_over()
        #dahyeman.adjust_height()
        if 0<len(jump_count) <8:
            dahyeman.draw_jump('rise')
            fall_count.clear()
            print(coordinates['yc'])
        else:
            dahyeman.draw_player()
        time_passed.append(0)
        pygame.display.update()
        clock.tick(60)


    pygame.quit()
    
main_loop(bg_img)

#NEVER GONNA GIVE YOU UP , NEVER GONNA LET YOU DOWN , NEVER GONNA RUNNN AROUND AND DESERT YOU!!!!!
#GET
#scroll background