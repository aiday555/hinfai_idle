import time
import pyautogui
from utils import isImageOnScreen
from config import *

# Dragon blood image
BLOOD_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/alc_blood.png"
# Dust image
DUST_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/alc_dust.png"
# Custom prefix
prefix = "[Alchemist]"

# Open world map
print(f"{prefix} Going to the alchemist.")
pyautogui.press("a")

# Search for the image on the screen
blood_pos = isImageOnScreen(BLOOD_PATH)

if blood_pos:
    print(f"{prefix} Starting dragon blood research.")
    # Click on the center of the target image
    blood_center = pyautogui.center(blood_pos)
    pyautogui.click(blood_center)
    time.sleep(SEARCH_INTERVAL_SECONDS)
else:
    print(f"{prefix} Dragon blood is not ready yet.")

# Search for the image on the screen
dust_pos = isImageOnScreen(DUST_PATH)

if dust_pos:
    print(f"{prefix} Starting dust research.")
    # Click on the center of the target image
    dust_center = pyautogui.center(dust_pos)
    pyautogui.click(dust_center)
    time.sleep(SEARCH_INTERVAL_SECONDS)
else:
    print(f"{prefix} Dust is not ready yet.")
