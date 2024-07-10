from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

TOKEN = os.environ.get("TOKEN")


import discord
from discord import app_commands

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print("起動しました")
    await tree.sync()


client.run(TOKEN)
