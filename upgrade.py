import time
import pyautogui
from utils import isImageOnScreen
from config import *

MAX_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/max_hero.png"
prefix = "[HeroUpgrader]"


def cycle_until_max():
    print("Searching for image:", MAX_PATH) 
    target_pos = isImageOnScreen(MAX_PATH)

    if target_pos:
        print(f"{prefix} Hero upgrade is at MAX. Starting upgrades.")
    else:
        print(f"{prefix} Hero upgrade is not at MAX. Cycling.")
        pyautogui.click(CYCLE_LOCATION_X, CYCLE_LOCATION_Y)
        time.sleep(SEARCH_INTERVAL_SECONDS)
        cycle_until_max()


print(f"{prefix} Opening upgrade menu")
pyautogui.press("u")

time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Setting upgrades to Next Milestone")
cycle_until_max()

time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Upgrading abilities")
pyautogui.click(ABILITY_UPGRADE_X, ABILITY_UPGRADE_Y)
time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Upgrading hero #1")
pyautogui.click(FIRST_HERO_X, FIRST_HERO_Y)
time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Upgrading hero #2")
pyautogui.click(SECOND_HERO_X, SECOND_HERO_Y)
time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Upgrading hero #3")
pyautogui.click(THIRD_HERO_X, THIRD_HERO_Y)
time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Upgrading hero #4")
pyautogui.click(FOURTH_HERO_X, FOURTH_HERO_Y)
time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Upgrading hero #5")
pyautogui.click(FIFTH_HERO_X, FIFTH_HERO_Y)
time.sleep(SEARCH_INTERVAL_SECONDS)
