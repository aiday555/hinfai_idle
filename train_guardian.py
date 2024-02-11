import time
import pyautogui
from utils import isImageOnScreen
from config import *

TRAIN_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/train.png"
# Custom prefix
prefix = "[GuardianTrainer]"

# Open world map
print(f"{prefix} Going to the Magic Quarter.")
pyautogui.press("g")

# Search for the image on the screen
train_pos = isImageOnScreen(TRAIN_PATH)

if train_pos:
    print(f"{prefix} Training guardian.")
    # Click on the center of the target image
    train_center = pyautogui.center(train_pos)
    pyautogui.click(train_center)
    time.sleep(SEARCH_INTERVAL_SECONDS)
else:
    print(f"{prefix} Training is not ready yet.")
