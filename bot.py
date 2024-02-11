import subprocess
import time
from config import *

prefix = "[Main Thread]"

print(f"{prefix} Waiting 3 seconds before starting...")
time.sleep(3)


def doExternal(file):
    print(f"{prefix} Starting {file}")
    subprocess.call(["python", file])

    print(f"{prefix} Going back to the home.")
    subprocess.call(["python", "go_home.py"])


while True:
    if(AUTOMATE_LIBRARIAN):
        doExternal("start_lib.py")

    if(AUTOMATE_HERO_UPGRADES):
        doExternal("upgrade.py")

    if(AUTOMATE_GUARDIAN_TRAIN):
        doExternal("train_guardian.py")

    if(AUTOMATE_MAP_MISSIONS):
        doExternal("do_map_missions.py")

    if(AUTOMATE_GUILD_MISSIONS):
        doExternal("do_guild_missions.py")

    if(AUTOMATE_ALCHEMIST):
        doExternal("alchemist.py")

    if(AUTOMATE_ARMY_LOOT):
        doExternal("do_army_loot.py")

    if(AUTOMATE_GUILD_PICKAXES):
        doExternal("claim_pickaxes.py")

    # Wait 20 seconds to not spam
    print(f"{prefix} Waiting {MAIN_THREAD_SLEEP} seconds to not spam...")
    time.sleep(MAIN_THREAD_SLEEP)
