import nextcord
from nextcord.ext import commands
import os
import aiohttp
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix="!", intents = intents)
client.remove_command("help")
@client.event
async def on_ready():
    print(f"{client.user.name}#{client.user.discriminator} id now ready!")
for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        client.load_extension(f"cogs.{cog[:-3]}")
        print(cog)
client.run("token")
