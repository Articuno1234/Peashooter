import sys
import os
import time
import random
import datetime
import subprocess

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("> ").lower().strip()

def main():
    clear_screen()
    since = datetime.datetime(2017, 10, 6, 0, 0)
    days_since = (datetime.datetime.utcnow() - since).days
    print("============================ \n"
          " -- Peashooter - Launcher -- \n"
          "============================ \n")
    print("1. Run Peashooter")
    print("2. Install requirements")
    print("3. Credits")
    print("0. Exit")
    print("\n"
          "Running Since {} days".format(days_since))
    choice = user_choice()
    if choice == "1":
        clear_screen()
        subprocess.call((sys.executable, "cogs/bot.py"))
    if choice == "2":
        clear_screen()
        subprocess.call(("sudo", "pip3", "install", "time"))
        subprocess.call(("sudo", "pip3", "install", "random"))
        subprocess.call(("sudo", "pip3", "install", "datetime"))
        subprocess.call(("sudo", "pip3", "install", "subprocess"))
        subprocess.call(("sudo", "python3", "-m", "pip", "install", "-U", "discord.py[voice]"))
        main()
    if choice == "3":
        c()
    if choice == "0":
        clear_screen()
        print("Exited with code 1")
        sys.exit(1)
        

def c():
    clear_screen()
    print("=============\n"
          "Credits\n"
          "=============\n")
    print("Founders:\n"
          "TheBabyPeashooter\n"
          "TheBabySunflower\n")
    print("\n"
          "\n"
          "say 'back' to go back!\n")
    choice = user_choice()
    if choice == "back":
        main()


main()
    
