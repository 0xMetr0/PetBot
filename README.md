# PetBot
This Discord bot simulates pet behavior for a cat and a dog. It responds to commands with random, time-of-day appropriate messages about what the pets are doing.

## Features

- Separate bot scripts for a cat (`catbot.py`) and a dog (`dogbot.py`)
- Time-based responses (morning, afternoon, evening, night)
- Pet interaction commands
- Attention-getting command
- Responses for misspelled pet names

## Commands

For both cat and dog:
- `/PETNAME`: Get a random message about what the pet is doing
- `/PETNAME_pet`: Pet the animal and get a response
- `/PETNAME_getattention`: The pet gives attention to a randomly chosen user from two mentioned users
- `/MISSPELL1`: Triggers a negative response from the pet (as if the name was misspelled)
Replace `PETNAME` with the actual name of the pet in your implementation. 
Replace `MISSPELL1` with a common misspelling of your animals name. If you misspell the pet's name when using a command, it will elicit a negative response from the pet.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-pet-bot.git
   cd discord-pet-bot
   ```

2. Install the required dependencies:
   ```
   pip install discord.py
   ```

3. Create a Discord bot and get your bot token:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application
   - Go to the "Bot" tab and add a bot to your application
   - Copy the bot token

4. Replace `'DISCORDAPIKEY'` in both `catbot.py` and `dogbot.py` with your actual bot token.

5. Customize the pet names, owner names, and messages in the scripts as desired.

6. Run the bot:
   ```
   python catbot.py
   ```
   or
   ```
   python dogbot.py
   ```

## Customization

You can easily customize the bot by modifying the message lists in the Python files:

- `morning_messages`
- `afternoon_messages`
- `evening_messages`
- `night_messages`
- `pet_messages`
- `error_messages` (responses for misspelled names)

Replace `PETNAME`, `OWNER`, `FRIEND`, and other placeholders with appropriate names or terms for your use case.

## Time-based Responses

The bot uses the current time to determine which set of messages to use:
- Morning: 12:00 AM to 11:59 AM
- Afternoon: 12:00 PM to 4:59 PM
- Evening: 5:00 PM to 8:59 PM
- Night: 9:00 PM to 11:59 PM

## Misspelled Name Responses

The `error_messages` list contains responses that the pet will give if its name is misspelled. The `/MISSSPELL1` and `/MISSSPELL2` commands allow you to trigger these responses directly.

## Note on Privacy

Some of the cat's messages include sensitive information (like credit card numbers or SSN). These are placeholder jokes and should be replaced or removed before deploying the bot in a real environment.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
