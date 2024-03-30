import pygame
import sys
from button import Button
import time

pygame.init()
screen_width, screen_height = 1000, 500
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")
BG_img = pygame.image.load("images/sunset_bg.png")
BG = pygame.transform.scale(BG_img, (1000, 500))
level = pygame.image.load('assets/level_bg.png')
level_img = pygame.transform.scale(level, (400, 100))
quit = pygame.image.load('assets/Quit Rect.png')
quit_img = pygame.transform.scale(level, (200, 50))
coin = pygame.image.load('images/coin.png')
coin_img = pygame.transform.scale(coin, (40, 40))
NORTHERN_BG = pygame.image.load('images/northernlights_bg.jpg')
NORTHERN_BG_img = pygame.transform.scale(NORTHERN_BG, (300, 150))
lightning_BG = pygame.image.load('images/lightning_bg.png')
lightning_BG_img = pygame.transform.scale(lightning_BG, (300, 150))
winter_BG = pygame.image.load('images/winter_bg.png')
winter_BG_img = pygame.transform.scale(winter_BG, (300, 150))
spooky_BG = pygame.image.load('images/spooky_bg.png')
spooky_BG_img = pygame.transform.scale(spooky_BG, (300, 150))
sunset_BG = pygame.image.load('images/sunset_bg.png')
sunset_BG_img = pygame.transform.scale(sunset_BG, (300, 150))


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


SHOP_TEXT = get_font(45).render(f"BACKGROUNDS", True, "WHITE")
SHOP_RECT = SHOP_TEXT.get_rect(center=(280, 50))
warning_TEXT = get_font(50).render("NOT ENOUGH COINS", True, "RED")
warning_rect = warning_TEXT.get_rect(
    center=(screen_width//2, screen_height//5))


def warning():
    SCREEN.blit(warning_TEXT, warning_rect)


def levels_func():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        LEVEL_TEXT = get_font(75).render("PICK A LEVEL", True, "#b68f40")
        level_rect = LEVEL_TEXT.get_rect(
            center=(screen_width//2, screen_height//5))

        LEVEL1_BUTTON = Button(image=level_img, pos=(screen_width//2, screen_height - screen_height//2),
                               text_input="Level 1", font=get_font(50), base_color="#d7fcd4", hovering_color="green")
        LEVEL2_BUTTON = Button(image=level_img, pos=(screen_width//4,  screen_height - screen_height//5),
                               text_input="Level 2", font=get_font(50), base_color="#d7fcd4", hovering_color="green")
        LEVEL3_BUTTON = Button(image=level_img, pos=(screen_width - screen_width//3.5, screen_height - screen_height//5),
                               text_input="Level 3", font=get_font(50), base_color="#d7fcd4", hovering_color="green")
        back_button = Button(image=quit_img, pos=(850, screen_height-screen_height//2),
                             text_input="BACK", font=get_font(30), base_color="#d7fcd4", hovering_color="green")
        SCREEN.blit(LEVEL_TEXT, level_rect)

        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, back_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    from level1 import main_loop
                    mainloop()
                if back_button.checkForInput(MENU_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def shop(coins_collected, bg):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Magenta")

        SCREEN.blit(SHOP_TEXT, SHOP_RECT)

        coins_TEXT = get_font(35).render(
            f"You have:{coins_collected}", True, "WHITE")
        coins_RECT = coins_TEXT.get_rect(center=(720, 50))
        SCREEN.blit(coins_TEXT, coins_RECT)
        SCREEN.blit(coin_img, (950, 28))

        SCREEN.blit(NORTHERN_BG_img, (20, 300))
        northern_button = Button(image=quit_img, pos=(160, 375), text_input="200", font=get_font(
            30), base_color="#d7fcd4", hovering_color="green")

        SCREEN.blit(lightning_BG_img, (20, 100))
        lightning_button = Button(image=quit_img, pos=(160, 175), text_input="100", font=get_font(
            30), base_color="#d7fcd4", hovering_color="green")

        SCREEN.blit(sunset_BG_img, (340, 100))
        sunset_button = Button(image=quit_img, pos=(480, 175), text_input="150", font=get_font(
            30), base_color="#d7fcd4", hovering_color="green")

        SCREEN.blit(winter_BG_img, (340, 300))
        winter_button = Button(image=quit_img, pos=(480, 375), text_input="500", font=get_font(
            30), base_color="#d7fcd4", hovering_color="green")

        SCREEN.blit(spooky_BG_img, (660, 100))
        spooky_button = Button(image=quit_img, pos=(800, 175), text_input="300", font=get_font(
            30), base_color="#d7fcd4", hovering_color="green")
        back_button = Button(image=quit_img, pos=(850, screen_height-screen_height//5),
                             text_input="BACK", font=get_font(30), base_color="#d7fcd4", hovering_color="green")
        for button in [back_button, northern_button, lightning_button, sunset_button, spooky_button, winter_button]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if winter_button.checkForInput(OPTIONS_MOUSE_POS):
                    if coins_collected >= 1:
                        bg = pygame.image.load('images/winter_bg.png')
                    else:
                        warning()
                if lightning_button.checkForInput(OPTIONS_MOUSE_POS):
                    if coins_collected >= 100:
                        pass
                    else:
                        warning()
                if northern_button.checkForInput(OPTIONS_MOUSE_POS):
                    if coins_collected >= 200:
                        pass
                    else:
                        warning()
                if sunset_button.checkForInput(OPTIONS_MOUSE_POS):
                    if coins_collected >= 150:
                        pass
                    else:
                        warning()
                if spooky_button.checkForInput(OPTIONS_MOUSE_POS):
                    if coins_collected >= 300:
                        pass
                    else:
                        warning()

        pygame.display.update()


def main_menu(coins_collected, bg):
    while True:
        SCREEN.fill((0, 0, 0))
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(75).render("DAHYE RUN", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(
            center=(screen_width//2, screen_height//5))

        LEVELS_BUTTON = Button(image=pygame.image.load("assets/level_bg.png"), pos=(screen_width//2, screen_height - screen_height//2),
                               text_input="Levels", font=get_font(75), base_color="#d7fcd4", hovering_color="green")
        SHOP_BUTTON = Button(image=pygame.image.load("assets/shop_bg.png"), pos=(screen_width//4,  screen_height - screen_height//5),
                             text_input="Shop", font=get_font(75), base_color="#d7fcd4", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(screen_width - screen_width//3.5, screen_height - screen_height//5),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LEVELS_BUTTON, SHOP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVELS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    levels_func()
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    shop(coins_collected, bg)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
