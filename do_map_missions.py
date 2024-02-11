import time
import pyautogui
import math
from utils import isImageOnScreen
from config import *

# Path to the reference image file
REF_IMAGE_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/collect_map_mission.png"
# Custom prefix
prefix = "[WorldMapCollector]"
START_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/mission_start.png"
WAR_MISSION_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/war_mission.png"
SCOUT_MISSION_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/scout_mission.png"
ADVENTURE_MISSION_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/adventure_mission.png"
MONSTER_MISSION_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/monster_mission.png"
DRAGON_MISSION_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/dragon_mission.png"
NAVAL_MISSION_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/naval_mission.png"
NO_SQUADS_PATH = f"images/{SCREEN_RESOLUTION}/{GAME_LANGUAGE}/no_squads.png"
# Set a radius (in pixels) around each previously clicked image to ignore
RADIUS = 50


def check_squads():
    print(f"{prefix} Checking if squads are available.")

    is_not_available = isImageOnScreen(NO_SQUADS_PATH)

    if is_not_available:
        print(f"{prefix} No squads are available. Aborting.")
        exit(0)
    else:
        print(f"{prefix} Squads are available. Starting missions.")


def start_mission(image_path):
    print(f"{prefix} Checking and starting all {image_path} missions.")

    clicked_positions = []

    war_found = pyautogui.locateAllOnScreen(
        image_path, grayscale=True, confidence=0.9)

    for war_pos in war_found:
        # Check if the image is within RADIUS pixels of a previously clicked image
        for clicked_pos in clicked_positions:
            if math.sqrt((war_pos.left - clicked_pos.left) ** 2 +
                         (war_pos.top - clicked_pos.top) ** 2) < RADIUS:
                break  # Ignore this image and move on to the next one
        else:
            # The image is far enough away from all previously clicked images, so click it
            target_center = pyautogui.center(war_pos)
            pyautogui.click(target_center)
            clicked_positions.append(war_pos)

            time.sleep(SEARCH_INTERVAL_SECONDS)

            start_pos = pyautogui.locateOnScreen(
                START_PATH, grayscale=True, confidence=0.9)

            if start_pos:
                start_center = pyautogui.center(start_pos)
                pyautogui.click(start_center)
                time.sleep(SEARCH_INTERVAL_SECONDS)
                pyautogui.press("esc")
            else:
                pyautogui.press("esc")

            time.sleep(SEARCH_INTERVAL_SECONDS)


def claim_completed():
    target_pos = isImageOnScreen(REF_IMAGE_PATH)

    if target_pos:
        print(f"{prefix} Found collect button. Collecting.")
        # Click on the center of the target image
        target_center = pyautogui.center(target_pos)
        pyautogui.click(target_center)
        time.sleep(SEARCH_INTERVAL_SECONDS)
        pyautogui.move(0, -250)
        pyautogui.press("esc")

        time.sleep(SEARCH_INTERVAL_SECONDS)
        claim_completed()
    else:
        print(f"{prefix} Target image not found.")


# Open world map
print(f"{prefix} Going to the world map.")
pyautogui.press("m")

time.sleep(SEARCH_INTERVAL_SECONDS)

# Claiming
claim_completed()

time.sleep(SEARCH_INTERVAL_SECONDS)

check_squads()
start_mission(NAVAL_MISSION_PATH)

check_squads()
start_mission(SCOUT_MISSION_PATH)

check_squads()
start_mission(MONSTER_MISSION_PATH)

check_squads()
start_mission(ADVENTURE_MISSION_PATH)

check_squads()
start_mission(DRAGON_MISSION_PATH)

check_squads()
start_mission(WAR_MISSION_PATH)
