import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
@bot.command()
async def meme(ctx):
   
    lista = os.listdir('images')

    imagem = random.choice(lista)

    with open(f'images/{imagem}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def reciclar(ctx, material):
  
    reciclagem = {"plastico" :"https://youtu.be/H5rbcjYYTXA",
                  "oleo usado" : "https://youtu.be/FsV4gAfIPdM",
                   "cano pvc" : "https://www.youtube.com/shorts/ZE9lsiSGk0w?feature=share", 
                 "latinha" :"https://www.youtube.com/shorts/ZlHJjfLQe8c?feature=share" }

    

    await ctx.send(reciclagem[material])


bot.run("")

