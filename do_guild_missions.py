import time
import pyautogui
from utils import isImageOnScreen
from config import *

# Path to the referenced image files
GUILD_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/guild.png"
EXPEDITIONS_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/expeditions.png"
# Custom prefix
prefix = "[ClaimGuildMissions]"


print(f"{prefix} Navigating to guild.")

# Search for the guild image on the screen
guild_pos = isImageOnScreen(GUILD_IMAGE_PATH)

if guild_pos:
    guild_center = pyautogui.center(guild_pos)
    pyautogui.click(guild_center)
else:
    print(f"{prefix} ERROR: Unable to find image {GUILD_IMAGE_PATH}")
    exit(1)

time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Navigating to expeditions.")

# Search for the expedition image on the screen
expedition_pos = isImageOnScreen(EXPEDITIONS_IMAGE_PATH)

if expedition_pos:
    expedition_center = pyautogui.center(expedition_pos)
    pyautogui.click(expedition_center)
else:
    print(f"{prefix} ERROR: Unable to find image")
    exit(1)

time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Claiming / Starting a new expedition.")

pyautogui.click(GUILD_CLAIM_X, GUILD_CLAIM_Y)

time.sleep(SEARCH_INTERVAL_SECONDS)

pyautogui.click(GUILD_CLAIM_X, GUILD_CLAIM_Y)

time.sleep(SEARCH_INTERVAL_SECONDS)
