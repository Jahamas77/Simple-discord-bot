import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def roll(ctx, sides: int = 6):
    result = random.randint(1, sides)
    await ctx.send(f"🎲 You rolled a {result}!")

@bot.command()
async def compliment(ctx):
    compliments = [
        "You're an amazing person!",
        "You're so talented!",
        "You brighten up the room!",
        "You have a great sense of humor!",
        "You're incredibly kind!"
    ]
    await ctx.send(random.choice(compliments))

bot.run("YOUR_BOT_TOKEN")
