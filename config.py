# Language of your game
# Supported:
# eng -> English
# ger -> German
GAME_LANGUAGE = "eng"

# Resolution of your screen
# Supported:
# 3840x2160
# 1920x1080
SCREEN_RESOLUTION = "1920x1080"

# The time the bot should sleep between the last phase & repeating the first phase again. Provided in seconds
MAIN_THREAD_SLEEP = 20

# The location of the x button from the "Are you enjoying this game?" button
# This menu occurs every time you make significant progress in the game
# This is needed because is simple press on ESCAPE won't close this menu
SHOULD_RATE_CLOSE_X = 4760
SHOULD_RATE_CLOSE_Y = 605

# Interval between searching for images again and waiting for the game to update the screen
# Change this value according to your PC. If you menus / screens take longer to load, feel free to increase it
# I recommend a minimum of one second
SEARCH_INTERVAL_SECONDS = 1

# The locations of the claim / start new guild expedition on your screen
# Those are found in the guild menu on the "Expeditions" menu
# It should be able to click "COLLECT" and also start a new one
GUILD_CLAIM_X = 1300
GUILD_CLAIM_Y = 330

# Coordinates of the hero upgrades on screen
# Those are the buttons you press to upgrade your heroes 1 to 5 and your ability
ABILITY_UPGRADE_X = 1700
ABILITY_UPGRADE_Y = 223
FIRST_HERO_X = 1742
FIRST_HERO_Y = 441
SECOND_HERO_X = 1742
SECOND_HERO_Y = 552
THIRD_HERO_X = 1742
THIRD_HERO_Y = 650
FOURTH_HERO_X = 1742
FOURTH_HERO_Y = 764
FIFTH_HERO_X = 1752
FIFTH_HERO_Y = 864

# Coordinates of the button to switch from x1 to x10 etc.
# This button should be able to be pressed when menu is in the "BASIC" OR "EXPANDED" mode
CYCLE_LOCATION_X = 1597
CYCLE_LOCATION_Y = 977

# Toggle features on / off
# True = Activated
# False = Deactivated
AUTOMATE_LIBRARIAN = False
AUTOMATE_HERO_UPGRADES = True
AUTOMATE_GUARDIAN_TRAIN = False
AUTOMATE_MAP_MISSIONS = False
AUTOMATE_GUILD_MISSIONS = False
AUTOMATE_ALCHEMIST = False
AUTOMATE_ARMY_LOOT = False
AUTOMATE_GUILD_PICKAXES = False
