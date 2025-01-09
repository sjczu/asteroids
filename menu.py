import pygame
import sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

class Menu:
    menu_options = ["Start","Customize","Options","Profile","Leaderboard","Exit"]
    settings_options = ["BGM Volume", "Resolution", "Difficulty","Back"]
    diff_options = ["Easy","Medium","Hard"]
    def __init__(self,screen,options=None):
        self.screen = screen
        self.options = options if options is not None else Menu.menu_options
        self.selected_option = 0
        self.font = pygame.font.Font(None, 74)

    def display_menu(self):
        self.screen.fill((0,0,0))
        for i, option in enumerate(self.options):
            color = (255,255,255) if i != self.selected_option else (255,0,0)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (100,100 + i*100))
        pygame.display.flip()
        
    def navigate(self):
        while True:
            self.display_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        return self.options[self.selected_option]
                    
    def start_game(self, screen, fpsClock):
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()

        pygame.font.init()
        font = pygame.font.Font(None, 36)
        
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        Asteroid.containers = (updatable, drawable, asteroids)
        AsteroidField.containers = (updatable)
        asteroid_field = AsteroidField()

        Shot.containers = (updatable, drawable, shots)

        while True:
            dt = fpsClock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            for object in updatable:
                object.update(dt)

            for object in asteroids:
                if player.check_collision(object):
                    if player.lives <= 1:
                        print("Game over!")
                        return
                    object.kill()
                    player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            for object in asteroids:
                for bullet in shots:
                    if object.check_collision(bullet):
                        object.split()
                        bullet.kill()
                        break

            screen.fill((0, 0, 0))

            for object in drawable:
                object.draw(screen)

            draw_ui(screen, font, player)
            
            pygame.display.flip()
            
            
    def customize(self,screen):
        pass
    
    def options_menu(self,screen):
        settings_menu = Menu(screen,Menu.settings_options)
        selected_option = settings_menu.navigate()
        if selected_option == "BGM Volume":
            pass
        elif selected_option == "Resolution":
            res_h_options = ["720","1080","1440","2160"]
            res_w_options = ["1280","1920","2560","3440","3840"]
            res_full_options = ["1280x720", "1920x1080", "2560x1440", "3440x1440", "3840x2160"]
            
            res_dropdown = Dropdown(screen,res_full_options,100,100)
            
            while True:
                screen.fill((0,0,0))
                res_dropdown.display_menu()
                pygame.display.flip()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    res_dropdown.event_handler(event)
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        selected_option = res_dropdown.get_selected_option()
                        res_w, res_h = map(int, selected_option.split("x"))
                        # global SCREEN_HEIGHT, SCREEN_WIDTH
                        SCREEN_HEIGHT = res_h
                        SCREEN_WIDTH = res_w
                        update_constants_file(SCREEN_WIDTH, SCREEN_HEIGHT)
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                        return
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
        elif selected_option == "Difficulty":
            diff_menu = Menu(screen,Menu.diff_options)
            selected_option = diff_menu.navigate()
            # global ASTEROID_SPAWN_RATE
            if selected_option == "Easy":
                ASTEROID_SPAWN_RATE = 2.0
                update_constants_file(ASTEROID_SPAWN_RATE)
            elif selected_option == "Medium":
                ASTEROID_SPAWN_RATE = 1.2
                update_constants_file(ASTEROID_SPAWN_RATE)
            elif selected_option == "Hard":
                ASTEROID_SPAWN_RATE = 0.8
                update_constants_file(ASTEROID_SPAWN_RATE)
        elif selected_option == "Back":
            return
    
    def profile(self,screen):
        pass
    
    def leaderboard(self,screen):
        pass
    
    def exit(self):
        pygame.quit()
        sys.exit()

class Dropdown(Menu):
    def __init__(self,screen,options,x,y):
        super().__init__(screen,options)
        self.font = pygame.font.Font(None, 56)
        self.x = x
        self.y = y
        self.selected_option = 0
        self.is_open = False
    def display_menu(self):
        selected_text = self.font.render(self.options[self.selected_option], True, (255,0,0))
        self.screen.blit(selected_text, (self.x,self.y))
        
        if self.is_open:
            for i, option in enumerate(self.options):
                # color = (255,255,255) if i != self.selected_option else (255,0,0)
                text = self.font.render(option, True, (255,255,255) if i != self.selected_option else (255,0,0))
                self.screen.blit(text, (self.x,self.y + (i+1)*30))
            
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            if event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            if event.key == pygame.K_RETURN:
                self.is_open = not self.is_open
                if not self.is_open:
                    return self.options[self.selected_option]
        return None
    
    def get_selected_option(self):
        return self.options[self.selected_option]
        
def draw_ui(screen,font,player):
        lives_text = font.render(f"Lives: {player.lives}", True, (255,255,255))
        screen.blit(lives_text, (10,10))
        
        score_text = font.render(f"Score: {player.score}", True, (255,255,255))
        screen.blit(score_text, (10,50))

def update_constants_file(width=None, height=None, spawn_rate=None):
        with open('constants.py', 'r') as file:
            lines = file.readlines()

        with open('constants.py', 'w') as file:
            for line in lines:
                if line.startswith('SCREEN_WIDTH') and width is not None:
                    file.write(f'SCREEN_WIDTH = {width}\n')
                elif line.startswith('SCREEN_HEIGHT') and height is not None:
                    file.write(f'SCREEN_HEIGHT = {height}\n')
                elif line.startswith('ASTEROID_SPAWN_RATE') and spawn_rate is not None:
                    file.write(f'ASTEROID_SPAWN_RATE = {spawn_rate}\n')
                else:
                    file.write(line)