# FirestoneBot

## About
This bot plays a huge part of the mobile & Steam game "Firestone: Online Idle RPG" for you. This is useful because this game literally expects you to be there 5+ hours a day

## Setup
To successfully set up this bot you need to do the following:

 - Make sure you have python and pip installed and working
 - Start a terminal in this folder and run "pip install -r requirements.txt"
 - Change your translation if needed. To do this, simply open your wanted translation (in the translations folder) and simply copy & replace those files with those found in the main folder.
 - Update your RESOLUTION and LANGUAGE in the config.py. If your resolution / language is not supported, feel free to create it and make a pull request
 - Update the coordinates in the config.py
 - Run the bot.py with python using a terminal. IMPORTANT: You **need** to be in the directory of the bot.py file

## Important to remember
 - The script will train the guardian you have currently selected in the magic quarter.
 - Also, it will only research things in the library if you are **scrolled so that it can reach them**. It will not scroll to the right / left by itself
 - The script has a 3-second starting delay. Use it to position yourself in-game.
 - You need to be at "home" when you are starting this. What does this mean? You need to be at the screen where your heroes are fighting. No menu opened. Not even the "Upgrade Heroes" one!
 - This script uses image recognition. Make sure no similar images are present on any other monitor, or it will try to click those
 - This script takes control over your mouse. So you can't just do something else while it runs

## How to exit the script
To exit this script simply go into the terminal window and hit CONTROL+C or close the window

## Features
 - Easy configuration
 - Alchemist starting
 - Claiming Guild Pickaxes
 - Army Loot collection
 - Guild Missions
 - Librarian starting
 - Guardian training
 - Upgrading heroes
 - Map missions
