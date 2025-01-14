# DONE Add a scoring system
# DONE Implement multiple lives and respawning
# TODO: Add an explosion effect for the asteroids
# DONE Add acceleration to the player movement
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
# DONE Add main menu and game over screens
# TODO: Add customization screen
# TODO: Add leveling system



import pygame
import time
import threading
import logging
import importlib
from pydub import AudioSegment
from pydub.playback import play
# from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, APP_VERSION, BGM_VOLUME
import config.settings
from classes.menu import Menu

logging.basicConfig(level=logging.DEBUG, filename='game.log',filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')

def play_music():
    # try:
    #     logging.info("Loading music...")
    #     song = AudioSegment.from_file("audio/retro-8bit-happy-videogame-music.mp3")
    #     chunk_duration_ms = 200 #ms
    #     total_duration_ms = len(song)
    #     logging.info(f"Music loaded. Song length: {total_duration_ms}, chunk duration: {chunk_duration_ms}. Starting playback...")
    #     pos = 0
    #     while True:
    #         try:
    #             importlib.reload(config.settings)
    #             curr_vol = config.settings.BGM_VOLUME
    #         except Exception as e:
    #             logging.error(f"Error reloading settings: {e}")
    #             curr_vol = 0.5
                
    #         try:
    #             chunk = song[pos:pos+chunk_duration_ms]
    #             new_chunk = chunk - (1-curr_vol) * 60
                
    #             play(new_chunk)
                
    #             pos += chunk_duration_ms
                
    #             if pos >= total_duration_ms:
    #                 pos = 0
    #                 logging.info("Music playback finished. Restarting...")
    #         except Exception as e:
    #             logging.error(f"Error playing music: {e}")
    #             break
                
    #         time.sleep(chunk_duration_ms / 1000) 
    # except Exception as e:
    #     logging.error(f"Error playing music: {e}")
    pass

def main():
    logging.info(f"Starting asteroids!\nScreen width: {config.settings.SCREEN_WIDTH}\nScreen height: {config.settings.SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((config.settings.SCREEN_WIDTH, config.settings.SCREEN_HEIGHT))
    pygame.display.set_caption(f"Asteroids v{config.settings.APP_VERSION}")
    fpsClock = pygame.time.Clock()
    try:    
        music_thread = threading.Thread(target=play_music)
        music_thread.daemon = True
        music_thread.start()
    except Exception as e:
        logging.error(f"Error starting music thread: {e}")

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
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        pygame.quit()
        exit()