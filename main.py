# DONE Add a scoring system
# DONE Implement multiple lives and respawning
# TODO: Add an explosion effect for the asteroids
# DONE Add acceleration to the player movement
# TODO: (optional) Make the objects wrap around the screen instead of disappearing
# TODO: (optional) Add a background image
# TODO: (optional) Add sound effects
# DONE/REMOVED (optional) Add BGM - BGM implementation with pygame.mixer was not working at all (sound was breaking up after 20-30 seconds), switched to PyDub and simpleaudio, but both caused game crashes after song end instead of looping it, so removed it altogether, maybe I'll come back to it some day
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
import simpleaudio
# from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, APP_VERSION, BGM_VOLUME
import config.settings
from classes.menu import Menu

logging.basicConfig(level=logging.DEBUG, filename='game.log',filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info(f"Starting asteroids!\nScreen width: {config.settings.SCREEN_WIDTH}\nScreen height: {config.settings.SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((config.settings.SCREEN_WIDTH, config.settings.SCREEN_HEIGHT))
    pygame.display.set_caption(f"Asteroids v{config.settings.APP_VERSION}")
    fpsClock = pygame.time.Clock()

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