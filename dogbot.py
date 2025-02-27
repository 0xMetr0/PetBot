import random
import datetime
import os
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

class PetBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        
    async def setup_hook(self):
        """A hook that is called when the bot is starting up"""
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
    """Event handler for when the bot is ready and connected to Discord"""
    print(f'{bot.user} has connected to Discord!')
    print(f"Bot is in {len(bot.guilds)} guild(s)")
    
def get_time_based_message():
    current_time = datetime.datetime.now().time()
    
    if current_time < datetime.time(12, 0):
        return random.choice(morning_messages)
    elif current_time < datetime.time(17, 0):
        return random.choice(afternoon_messages)
    elif current_time < datetime.time(21, 0):
        return random.choice(evening_messages)
    else:
        return random.choice(night_messages)

@bot.tree.command(name="PETNAME", description="Check on PETNAME")
async def pet_slash(interaction: discord.Interaction):
    """Slash command to check on the pet"""
    message = get_time_based_message()
    print(f'[{interaction.user}] - PETNAME command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="PETNAME_pet", description="Pet PETNAME")
async def pet_pet_slash(interaction: discord.Interaction):
    """Slash command to pet the pet"""
    message = random.choice(pet_messages)
    print(f'[{interaction.user}] - PETNAME pet command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="PETNAME_getattention", description="Test who PETNAME loves more")
@app_commands.describe(
    user1="First user who might get PETNAME's attention",
    user2="Second user who might get PETNAME's attention"
)
async def pet_getattention_slash(interaction: discord.Interaction, user1: discord.User, user2: discord.User):
    """Slash command to see which user gets the pet's attention"""
    chosen_user = random.choice([user1, user2])
    message = f"PETNAME is giving attention to {chosen_user.mention}!"
    print(f'[{interaction.user}] - PETNAME getattention command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="MISSPELL1", description="Misspell PETNAME and see what happens")
async def misspell1_slash(interaction: discord.Interaction):
    """Slash command for misspelling the pet's name"""
    message = random.choice(error_messages)
    print(f'[{interaction.user}] - MISSPELL1 command: {message}')
    await interaction.response.send_message(message)

@bot.tree.command(name="MISSPELL2", description="Misspell PETNAME and see what happens")
async def misspell2_slash(interaction: discord.Interaction):
    """Slash command for misspelling the pet's name again"""
    message = random.choice(error_messages)
    print(f'[{interaction.user}] - MISSPELL2 command: {message}')
    await interaction.response.send_message(message)

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    """Global error handler for all application commands"""
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(
            f"This command is on cooldown. Try again in {error.retry_after:.2f} seconds.", 
            ephemeral=True
        )
    elif isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message(
            "You don't have permission to use this command.", 
            ephemeral=True
        )
    else:
        print(f"Error in {interaction.command.name}: {error}")
        await interaction.response.send_message(
            f"Something went wrong with that command. Please try again later.",
            ephemeral=True
        )

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if not TOKEN:
        raise ValueError("No token found. Please set the DISCORD_TOKEN environment variable.")
    
    bot.run(TOKEN)