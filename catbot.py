import discord
from discord import app_commands
import random
import datetime
import os
from dotenv import load_dotenv

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