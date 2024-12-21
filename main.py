import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from commands.music import MusicCommands
from commands.message import MessageCommands
from commands.administrator import AdministratorCommands

# Carica il token dal file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configura gli intenti e il bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Sincronizza i comandi al login del bot
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.tree.sync()  # Sincronizza i comandi

# Inizializza i comandi musicali
MusicCommands(bot)

# Inizializza i comandi di messaggio
MessageCommands(bot)

# Inizializza i comandi di amministrazione
AdministratorCommands(bot)

# Avvia il bot
bot.run(TOKEN)
