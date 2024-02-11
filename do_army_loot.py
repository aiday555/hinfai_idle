import time
import pyautogui
from utils import isImageOnScreen
from config import *

CAMPAIGN_POS = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/campaign.png"
COLLECT_POS = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/campaign_collect.png"
# Custom prefix
prefix = "[ArmyLoot]"

# Open world map
print(f"{prefix} Going to the Map.")
pyautogui.press("m")

# Search for the image on the screen
campaign_pos = isImageOnScreen(CAMPAIGN_POS)

if campaign_pos:
    print(f"{prefix} Found campaign.")
    # Click on the center of the target image
    campaign_center = pyautogui.center(campaign_pos)
    pyautogui.click(campaign_pos)
    time.sleep(SEARCH_INTERVAL_SECONDS)
else:
    print(f"{prefix} Cannot find Campaign!.")
    exit(1)

collect_pos = isImageOnScreen(COLLECT_POS)

if collect_pos:
    print(f"{prefix} Collecting.")
    # Click on the center of the target image
    train_center = pyautogui.center(collect_pos)
    pyautogui.click(collect_pos)
    time.sleep(SEARCH_INTERVAL_SECONDS)
else:
    print(f"{prefix} Collecting is not ready yet.")
