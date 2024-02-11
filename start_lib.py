import time
import pyautogui
import math
from utils import isImageOnScreen
from config import *

# Custom prefix
prefix = "[LibraryStarter]"
FIRESTONE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/firestone_research.png"
FIRESTONE_SQUADS_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/firestone_squads_empty.png"
WORKING_RESEARCH_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/firestone_research_available.png"
START_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/firestone_research_button.png"
RADIUS = 20


def check_slots():
    target_pos = isImageOnScreen(FIRESTONE_SQUADS_PATH)

    if target_pos:
        print(f"{prefix} There are no slots available. Aborting.")
        exit(0)


def start_research():
    check_slots()

    clicked_positions = []

    research_found = pyautogui.locateAllOnScreen(
        WORKING_RESEARCH_PATH, grayscale=True, confidence=0.9)

    for research_pos in research_found:
        # Check if the image is within RADIUS pixels of a previously clicked image
        for clicked_pos in clicked_positions:
            if math.sqrt((research_pos.left - clicked_pos.left) ** 2 +
                         (research_pos.top - clicked_pos.top) ** 2) < RADIUS:
                break  # Ignore this image and move on to the next one
        else:
            # The image is far enough away from all previously clicked images, so click it
            target_center = pyautogui.center(research_pos)
            pyautogui.click(target_center)
            clicked_positions.append(research_pos)

            time.sleep(SEARCH_INTERVAL_SECONDS)

            start_pos = isImageOnScreen(START_PATH)

            if start_pos:
                start_center = pyautogui.center(start_pos)
                pyautogui.click(start_center)
                time.sleep(SEARCH_INTERVAL_SECONDS)
                check_slots()
            else:
                pyautogui.press("esc")

            time.sleep(SEARCH_INTERVAL_SECONDS)


print(f"{prefix} Opening the library")
pyautogui.press("l")
time.sleep(SEARCH_INTERVAL_SECONDS)

print(f"{prefix} Switching to Firestone view")

target_pos = isImageOnScreen(FIRESTONE_PATH)

if target_pos:
    print(f"{prefix} Found button, switching")
    target_center = pyautogui.center(target_pos)
    pyautogui.click(target_center)
else:
    print(f"{prefix} ERROR: could not find image on screen!")
    exit(1)

time.sleep(SEARCH_INTERVAL_SECONDS)

start_research()
