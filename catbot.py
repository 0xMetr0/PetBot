import discord
from discord.ext import commands
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

morning_messages = [
    "PETNAME is gazing into the bed",
    "PETNAME is snoring on the couch",
    "PETNAME is pacing around the apartment",
    "PETNAME is sniffing his blunt toy",
    ":3 :3 meow meow :3 :3",
    "PETNAME is considering the trees",
    "PETNAME is asserting his undying need for attention",
    "PETNAME tells you OWNER's credit card number is 85272783926394576 exp. 12/26 sc. 142",
    "PETNAME is thinking about you",
    "PETNAME is dreaming of eating grass",
    "PETNAME wishes someone would pet master",
    "PETNAME is thinking about Purr",
    "PETNAME wishes he was being brushed right now",
    "PETNAME is just sittin there all weird",
    "PETNAME is yapping his heart out"
]

afternoon_messages = [
    "PETNAME is meowing",
    "PETNAME is begging you for food",
    "PETNAME is digging for gold in his litterbox",
    "PETNAME can't with you rn",
    "PETNAME is asserting his undying need for attention",
    "PETNAME is looking at you, then he looks at his food, then he looks back at you",
    "PETNAME is standing next to his food and being as loud as possible",
    "PETNAME is practically yelling at you (he is hungry)",
    "PETNAME is soooooo hungry....... (he ate 15 minutes ago)",
    "PETNAME wishes he was being brushed right now",
    "PETNAME is snoring loudly",
    "PETNAME is sleeping on the chair in the living room",
    "PETNAME is dreaming about trees and flowers",
    "PETNAME tells you OWNER's SSN is 94475924083",
    "PETNAME is so sleepy",
    "PETNAME is throwing up on something important to OWNER",
    "mewing on the scratch post",
    "PETNAME is sniffing his alligator toy",
    "PETNAME wishes FRIEND was petting him right now",
    "PETNAME is exhausted from a long hard day of being a cat",
    "PETNAME is so small",
    "PETNAME is just sittin there all weird",
    "PETNAME is sooooo tired",
    "PETNAME is listening to OWNERs music"
]

evening_messages = [
    "PETNAME is biting FRIEND",
    "PETNAME is looking at you",
    "PETNAME wants you to brush him",
    "PETNAME is thinking about dinner",
    "PETNAME meows at you",
    "PETNAME wishes FRIEND was being pet rn",
    "PETNAME is astral projecting",
    "PETNAME is your friend <3",
    "PETNAME is trying to hypnotize OWNER by staring into their eyes",
    "PETNAME is thinking of something so sick and twisted dark acadamia that you couldn't even handle it",
    "PETNAME is not your friend >:(", 
    "PETNAME is wandering about",
    "PETNAME is just sittin there all weird",
    "PETNAME is chewing on the brush taped to the wall"
]

night_messages = [
    "PETNAME is so small",
    "PETNAME is judging how human sleeps",
    "PETNAME meows once, and loudly.",
    "PETNAME is just a little guy.",
    "PETNAME is in the clothes basket",
    "PETNAME is making biscuits in the bed",
    "PETNAME is snoring loudly",
    "PETNAME is asserting his undying need for attention",
    "PETNAME is thinking about FRIEND",
    "PETNAME is using OWNER's computer to steal corporate secrets",
    "PETNAME is scheming",
    "PETNAME is just sittin there all weird"
]
error_messages = [
    "PETNAME hisses and runs away",
    "PETNAME bites you",
    "PETNAME moves just far enough away that you can't pet them",
    "PETNAME attempts to crush you with their mind",
    "PETNAME walks away",
    "PETNAME farts and looks at you in disgust"
]

pet_messages = [
    "PETNAME purrs contentedly",
    "PETNAME nuzzles your hand",
    "PETNAME stretches out and purrs",
    "PETNAME enjoys a good pet",
    "PETNAME rolls over for belly rubs",
    "PETNAME blinks slowly",
    "PETNAME happily accepts the pets",
    "PETNAME curls up in your lap",
    "PETNAME can't comprehend what you are doing to them"
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='PETNAME')
async def PETNAME(ctx):
    current_time = datetime.datetime.now().time()
    
    if current_time < datetime.time(12, 0):
        message = random.choice(morning_messages)
    elif current_time < datetime.time(17, 0):
        message = random.choice(afternoon_messages)
    elif current_time < datetime.time(21, 0):
        message = random.choice(evening_messages)
    else:
        message = random.choice(night_messages)
    
    print(f'[{ctx.author}] - PETNAME command: {message}')
    await ctx.send(message)

@bot.command(name='PETNAME_pet')
async def PETNAME_pet(ctx):
    message = random.choice(pet_messages)
    print(f'[{ctx.author}] - PETNAME pet command: {message}')
    await ctx.send(message)

@bot.command(name='PETNAME_getattention')
async def PETNAME_getattention(ctx, user1: discord.User, user2: discord.User):
    chosen_user = random.choice([user1, user2])
    message = f"PETNAME is giving attention to {chosen_user.mention}!"
    print(f'[{ctx.author}] - PETNAME getattention command: {message}')
    await ctx.send(message)

@bot.command(name='MISSSPELL1')
async def MISSSPELL1(ctx):
    message = random.choice(error_messages)
    print(f'[{ctx.author}] - MISSSPELL1 command: {message}')
    await ctx.send(message)

@bot.command(name='MISSSPELL2')
async def MISSSPELL2(ctx):
    message = random.choice(error_messages)
    print(f'[{ctx.author}] - MISSSPELL2 command: {message}')
    await ctx.send(message)

# Replace 'DISCORDAPIKEY' with your actual bot token
bot.run('DISCORDAPIKEY')
