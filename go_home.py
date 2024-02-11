import time
import pyautogui
from utils import isImageOnScreen
from config import *

# Path to the reference image file
REF_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/home_identifier.png"
RATE_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/rate_now.png"
# Interval in seconds to search for image
# Custom prefix
prefix = "[GoHome]"

found = True
counter = 0

while found:
    # Search for the reference image on the screen
    target_pos = isImageOnScreen(REF_IMAGE_PATH)

    if target_pos:
        print(f"{prefix} Home image was found. Aborting.")
        # Click on the center of the target image
        found = False
    else:
        # DEACTIVATED DUE TO IMAGE MISSING IN VERSIONS
        # if counter >= 10:
        #     counter = 0
        #     rate_pos = isImageOnScreen(RATE_IMAGE_PATH)
        #
        #     if(rate_pos):
        #         print(f"{prefix} Rating found. Clicking and returning.")
        #         pyautogui.click(SHOULD_RATE_CLOSE_X, SHOULD_RATE_CLOSE_Y)
        #     else:
        #         print(f"{prefix} Rating not found. Returning.")

        print(f"{prefix} Home image not found. Pressing Escape.")
        pyautogui.press("esc")
        counter += 1

    # Wait for the next search interval
    time.sleep(SEARCH_INTERVAL_SECONDS)
