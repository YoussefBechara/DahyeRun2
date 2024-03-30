import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Menu")
class Game_over():
    def __init__(self, BG):
        self.BG = BG
        
    def get_font(self,size): 
        return pygame.font.Font("assets/font.ttf", size)

    def restart_func(self):
        quit()
        
    def shop(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            OPTIONS_TEXT = self.get_font(45).render("This is the shop screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):
        run = True
        while run:
            SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("GAME OVER", True, "red")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            RESTART_BUTTON = Button(image=pygame.image.load("assets/level_bg.png"), pos=(640, 250), 
                                text_input="RESTART", font=self.get_font(75), base_color="#d7fcd4", hovering_color="green")
            SHOP_BUTTON = Button(image=pygame.image.load("assets/shop_bg.png"), pos=(640, 400), 
                                text_input="Shop", font=self.get_font(75), base_color="#d7fcd4", hovering_color="green")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="green")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [RESTART_BUTTON, SHOP_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESTART_BUTTON.checkForInput(MENU_MOUSE_POS):
                        run = False
                        break
                    if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.shop()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

BG = pygame.image.load('assets/background.png')
game = Game_over(BG)
game.main_menu