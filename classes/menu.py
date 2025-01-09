import pygame
import sys
import time
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from config.stats import PLAYER_TOTAL_SCORE
from classes.player import Player, Shot
from classes.asteroid import Asteroid
from classes.asteroidfield import AsteroidField

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
            start_time = time.time()
            dt = fpsClock.tick(60) / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            update_start = time.time()
            for object in updatable:
                object.update(dt)
            update_end = time.time()

            collision_start = time.time()
            for object in asteroids:
                if player.check_collision(object):
                    if player.lives <= 1:
                        print("Game over!")
                        print(f"Updating score...\nOld score: {player.total_score}\nconstants.py score: {PLAYER_TOTAL_SCORE}\nGame score: {player.score}\nNew score: {round(player.total_score) + round(player.score)}\n")
                        update_file(score=player.score,player=player)
                        go_menu = GameOver(screen,GameOver.go_options)
                        selected_option = go_menu.navigate(player)
                        if selected_option == "Restart":
                            player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                        elif selected_option == "Main Menu":    
                            return
                        return
                    object.kill()
                    player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

            for object in asteroids:
                for bullet in shots:
                    if object.check_collision(bullet):
                        object.split()
                        bullet.kill()
                        player.add_score(object)
                        break
            collision_end = time.time()

            render_start = time.time()

            screen.fill((0, 0, 0))

            for object in drawable:
                object.draw(screen)

            draw_ui(screen, font, player)
            
            pygame.display.flip()
            render_end = time.time()

            end_time = time.time()
            print(f"Total Time: {end_time - start_time:.4f}s, Update: {update_end - update_start:.4f}s, Collision: {collision_end - collision_start:.4f}s, Render: {render_end - render_start:.4f}s")
                     
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
                        SCREEN_HEIGHT = res_h
                        SCREEN_WIDTH = res_w
                        update_file(filepath="config/settings.py",width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
                        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                        return
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
        elif selected_option == "Difficulty":
            diff_menu = Menu(screen,Menu.diff_options)
            selected_option = diff_menu.navigate()
            if selected_option == "Easy":
                ASTEROID_SPAWN_RATE = 2.0
                update_file(filepath="config/settings.py",spawn_rate=ASTEROID_SPAWN_RATE)
            elif selected_option == "Medium":
                ASTEROID_SPAWN_RATE = 1.2
                update_file(filepath="config/settings.py",spawn_rate=ASTEROID_SPAWN_RATE)
            elif selected_option == "Hard":
                ASTEROID_SPAWN_RATE = 0.8
                update_file(filepath="config/settings.py",spawn_rate=ASTEROID_SPAWN_RATE)
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
 
class GameOver(Menu):
    go_options = ["Main Menu"]
    def __init__(self,screen,options=None):
        super().__init__(screen,options)
        self.font = pygame.font.Font(None, 74)
    
    def display_menu(self,player):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.font.render("GAME OVER", True, (255, 255, 255)), (100, 100))
        score_text = self.font.render(f"Score: {round(player.score)}", True, (255, 255, 255))
        self.screen.blit(score_text, (100, 200))
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i != self.selected_option else (255, 0, 0)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (100, 300 + i * 100))
        pygame.display.flip()
    
    def navigate(self,player):
        while True:
            self.display_menu(player)
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
     
        
def draw_ui(screen,font,player):
        lives_text = font.render(f"Lives: {player.lives}", True, (255,255,255))
        screen.blit(lives_text, (10,10))
        
        score_text = font.render(f"Score: {round(player.score)}", True, (255,255,255))
        screen.blit(score_text, (10,50))

def update_file(filepath="config/stats.py",width=None, height=None, spawn_rate=None,score=None,player=None):
        with open(filepath, 'r') as file:
            lines = file.readlines()

        with open(filepath, 'w') as file:
            for line in lines:
                if line.startswith("SCREEN_WIDTH") and width is not None:
                    file.write(f"SCREEN_WIDTH = {width}\n")
                elif line.startswith("SCREEN_HEIGHT") and height is not None:
                    file.write(f"SCREEN_HEIGHT = {height}\n")
                elif line.startswith("ASTEROID_SPAWN_RATE") and spawn_rate is not None:
                    file.write(f"ASTEROID_SPAWN_RATE = {spawn_rate}\n")
                elif line.startswith("PLAYER_TOTAL_SCORE") and score is not None:
                    new_score = round(player.total_score) + score
                    file.write(f"PLAYER_TOTAL_SCORE = {round(new_score)}\n")
                else:
                    file.write(line)