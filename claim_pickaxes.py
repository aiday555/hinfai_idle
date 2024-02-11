import time
import pyautogui
from utils import isImageOnScreen
from config import *

# Path to the referenced image files
GUILD_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/guild.png"
CRYSTAL_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/crystal.png"
CLAIM_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/crystal_pick_claim.png"
CLAIM_PICKAXE_POS = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/claim_pickaxe.png"
# Custom prefix
prefix = "[Pickaxes]"


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

print(f"{prefix} Navigating to Crystal.")

# Search for the expedition image on the screen
crystal_pos = isImageOnScreen(CRYSTAL_IMAGE_PATH)

if crystal_pos:
    crystal_center = pyautogui.center(crystal_pos)
    pyautogui.click(crystal_center)
else:
    print(f"{prefix} ERROR: Unable to find image {CRYSTAL_IMAGE_PATH}")
    exit(1)

time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Navigating to Claim Page.")

# Search for the expedition image on the screen
claim_pos = isImageOnScreen(CLAIM_IMAGE_PATH)

if claim_pos:
    claim_center = pyautogui.center(claim_pos)
    pyautogui.click(claim_center)
else:
    print(f"{prefix} ERROR: Unable to find image {CLAIM_IMAGE_PATH}")
    exit(1)

time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Claiming pickaxes.")

# Search for the expedition image on the screen
pick_pos = isImageOnScreen(CLAIM_PICKAXE_POS)

if pick_pos:
    pick_center = pyautogui.center(pick_pos)
    pyautogui.click(pick_center)
else:
    print(f"{prefix} No pickaxes left to claim.")
    exit(0)

time.sleep(SEARCH_INTERVAL_SECONDS)
