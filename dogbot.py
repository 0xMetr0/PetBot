import discord
from discord import app_commands
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True

class PetBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        print(f'{self.user} is connecting to Discord!')
        await self.tree.sync()

bot = PetBot()

morning_messages = [
    "PETNAME is hiding behind his plant",
    "PETNAME is on a walk",
    "PETNAME is eating the tomatos in the garden",
    "PETNAME is licking his nuts",
    "PETNAME is peeing on the green chairs",
    "PETNAME is scratching his ear",
    "PETNAME is knocked out on the couch",
    "PETNAME is just happy to see you",
    "PETNAME is finding a way onto the table",
    "PETNAME is distracted by other people",
    "PETNAME and OTHERPET are unionizing to have the walk end at the alley",
    "PETNAME is hiding behind his plant",
    "PETNAME is distracted by OTHERPET"
]

afternoon_messages = [
    "PETNAME is looking at Mom like she is Jesus",
    "PETNAME is making busciuts on the couch",
    "PETNAME is barking at a bike",
    "PETNAME is stretching (to go sit in the other room)",
    "PETNAME is barking at the rentor coming down the stairs",
    "PETNAME is racing OWNER from the front yard to the back door after a walk",
    "PETNAME is tired (walked two houses down the block)",
    "PETNAME is on a walk strike",
    "PETNAME goes onto the hamock with you even though he doesnt like it",
    "PETNAME is distracted by his lack of a fuck to give",
    "PETNAME is thinking about OWNER's friends",
    "PETNAME is laying on the couch looking at you",
    "PETNAME is rolling around and rubbing his face in the grass",
    "PETNAME is just done with everyones shit today",
    "PETNAME is chilling by the gate waiting for mom",
    "PETNAME has was to much energy to spend in one day",
    "PETNAME is distracted by a moving object",
    "PETNAME is laying on his back with his head off the cushion, looking at you upsidedown with his tounge out a little",
    "PETNAME doesnt get what the humans are trying to say"
]

evening_messages = [
    "PETNAME is sitting in the butler pantry",
    "PETNAME is peeing in the basement",
    "PETNAME is following OTHERPET while she barks",
    "PETNAME is playing with his puzzle",
    "PETNAME is distracted by an itch",
    "PETNAME is scratching his ear",
    "PETNAME is protecting his meal (a paper towel)",
    "PETNAME thinks you have a treat so he is doing every trick he knows to try to get it",
    "PETNAME is trying to figure out why OTHERPET is so upset",
    "PETNAME is distracted by food",
    "PETNAME is distracted by the food in your hand",
    "PETNAME is trying to repay you by licking your face"
]

night_messages = [
    "PETNAME is protecting his trophy (a sock)",
    "PETNAME is sitting on his pile of pillows",
    "PETNAME is laying on OWNERs bed looking at him",
    "PETNAME can tell hes better than you",
    "PETNAME is sleeping in his cage",
    "PETNAME is sleeping in his cage",
    "PETNAME is sleeping in his cage",
    "PETNAME is sleeping in his cage",
    "PETNAME is distracted by a noise"
]

error_messages = [
    "PETNAME wrinkles their nose",
    "PETNAME snaps at you",
    "PETNAME sits somewhere else"
]

pet_messages = [
    "PETNAME looks at the toy you show him and walks away to lick his nuts",
    "PETNAME leans into your head scratches",
    "PETNAME rolls onto his back, expecting scratches",
    "PETNAME looks up and puffs his chest for neck scritches",
    "PETNAME puts a paw on your chest while you are sitting with him",
    "PETNAME licks your face and licks his nuts immediately after",
    "PETNAME starts talking after you find his sweet spot"
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.tree.command(name="PETNAME", description="Check on PETNAME")
async def pet_slash(interaction: discord.Interaction):
    current_time = datetime.datetime.now().time()
    
    if current_time < datetime.time(12, 0):
        message = random.choice(morning_messages)
    elif current_time < datetime.time(17, 0):
        message = random.choice(afternoon_messages)
    elif current_time < datetime.time(21, 0):
        message = random.choice(evening_messages)
    else:
        message = random.choice(night_messages)
    
    print(f'[{interaction.user}] - PETNAME command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="PETNAME_pet", description="Pet PETNAME")
async def pet_pet_slash(interaction: discord.Interaction):
    message = random.choice(pet_messages)
    print(f'[{interaction.user}] - PETNAME pet command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="PETNAME_getattention", description="Test who PETNAME loves more")
@app_commands.describe(
    user1="First user vying for PETNAME's attention",
    user2="Second user vying for PETNAME's attention"
)
async def pet_getattention_slash(interaction: discord.Interaction, user1: discord.User, user2: discord.User):
    chosen_user = random.choice([user1, user2])
    message = f"PETNAME sits next to {chosen_user.mention}!"
    print(f'[{interaction.user}] - PETNAME getattention command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="MISSPELL1", description="Misspell PETNAME and see what happens")
async def misspell1_slash(interaction: discord.Interaction):
    message = random.choice(error_messages)
    print(f'[{interaction.user}] - MISSPELL1 command: {message}')
    await interaction.response.send_message(message)



# Replace 'DISCORDAPIKEY' with your actual bot token
bot.run('DISCORDAPIKEY')
