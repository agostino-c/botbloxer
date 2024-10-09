import discord
import os
from dotenv import load_dotenv

load_dotenv()

class DiscordClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None: # Change this to search for a "welcome" channel set by user if not create one
            message = f'Welcome {member.mention} to {guild.Name}!'
            await guild.system_channel.send(message)
        



intents = discord.Intents.default()
intents.message_content = True
client = DiscordClient(intents=intents)


client.run(os.getenv('DISCORD_BOT_SECRET'))