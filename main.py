import discord
from discord.ext import commands
import random
import datetime

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())

# Random String
string_kt =[
    "Katzen ein",
    "Katzen aus House",
    "Katzen in Kalt",
    "Katzen Raus",
    "Katzen vier",
    
]
# secret number 
screet_number = 3

@bot.event
async def on_ready():
    print("Bot is ready")

# random string command 
     
@bot.command()
async def frent(ctx):
    fremtEin = random.choice(string_kt)
    await ctx.send(fremtEin)
    print ('random strings')
    
#random number command 

@bot.command()
async def spiel(ctx):
    global screet_number
    screet_number = random.randint(1,9)
    await ctx.send("Ich habe eine Zahl zwischen 1 und 9 gegessen")
    
@bot.command()
async def gessen(ctx, number: int):
    global screet_number
    if number == screet_number:
        await ctx.send("Gewonnen!")
    elif number > screet_number:
        await ctx.send("Zu hoch!")
    else:
        await ctx.send ("Zu niedrig!")
    print ('gessen spiel')
        
#zeit

@bot.command()
async def zeit(ctx):
    zeit = datetime.datetime.now().strftime ("%H:%M:%S")
    await ctx.send(f"Die Zeit ist {zeit}")
    print ('zeit')
    
# t0k3n aus README (</>)