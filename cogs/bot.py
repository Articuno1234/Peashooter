import discord
from discord.ext.commands import Bot
from discord.ext import commands
import logging
import config
import sys
import os

logging.basicConfig(level=logging.INFO) # Configurates the logger
logger = logging.getLogger('discord')
bot = Bot(command_prefix=config.PREFIX) # Sets the client and sets the prefix
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

@bot.event
async def on_ready():
    clear_screen()
    if __name__ == "__main__":
        for extension in config.startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}\n==================='.format(extension, exc))
    users = len(set(bot.get_all_members()))
    servers = len(bot.servers)
    channels = len([c for c in bot.get_all_channels()])
    commands = len(bot.commands)
    print("o.o.o.o.o.o.o.o.o.o\n"
          "Peashooter - Online\n"
          "o.o.o.o.o.o.o.o.o.o\n")
    print("Servers : {}\n"
          "Users : {}\n"
          "Channels : {}\n"
          "Commands : {}\n".format(servers, users, channels, commands))
    print("\n"
          "Bot Invite URL : https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0".format(bot.user.id))
    
try:
    bot.run(config.TOKEN)
except Exception as e:
    print("Error in Launcher 'cogs/bot.py' \n{}".format('{}: {}'.format(type(e).__name__, e)))
    sys.exit()

