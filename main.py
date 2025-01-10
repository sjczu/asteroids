# DONE Add a scoring system
# DONE Implement multiple lives and respawning
# TODO: Add an explosion effect for the asteroids
# TODO: Add acceleration to the player movement
# TODO: (optional) Make the objects wrap around the screen instead of disappearing
# TODO: (optional) Add a background image
# TODO: (optional) Add sound effects
# DONE (optional) Add BGM
# TODO: Create different weapon types
# DONE Make the asteroids lumpy instead of perfectly round
# DONE Make the ship have a triangular hit box instead of a circular one
# TODO: Add a shield power-up
# TODO: Add a speed power-up
# TODO: Add bombs that can be dropped
# TODO: Add main menu and game over screens
# TODO: Add customization screen
# TODO: Add leveling system



import pygame
import time
import threading
from pydub import AudioSegment
from pydub.playback import play
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, APP_VERSION
from classes.menu import Menu

def play_music():
    try:
        print("Loading music...")
        song = AudioSegment.from_file("audio/retro-8bit-happy-videogame-music.mp3")
        print("Music loaded. Starting playback...")
        while True:
            play(song)
            print("Music playback finished. Restarting...")
            time.sleep(len(song) / 1000) 
    except Exception as e:
        print(f"Error playing music: {e}")

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(f"Asteroids v{APP_VERSION}")
    fpsClock = pygame.time.Clock()

    music_thread = threading.Thread(target=play_music)
    music_thread.daemon = True
    music_thread.start()

    menu = Menu(screen)
    while True:
        selected_option = menu.navigate()

        time.sleep(0.1)
        if selected_option == "Start":
            menu.start_game(screen,fpsClock)    
        elif selected_option == "Customize":
            menu.customize(screen)
        elif selected_option == "Options":
            menu.options_menu(screen)
        elif selected_option == "Profile":
            menu.profile(screen)
        elif selected_option == "Leaderboard":
            menu.leaderboard(screen)
        elif selected_option == "Exit":
            menu.exit()


if __name__ == "__main__":
    main()