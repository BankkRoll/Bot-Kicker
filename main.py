import os
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


client = discord.Client()
bot_token = os.environ['bot_token']
intents = discord.Intents.default()
intents.members = True
client =commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
      await client.change_presence(activity=discord.Game("Scanning " + str(len(client.guilds)) + " servers!"))
      print(f'{client.user} has connected to Discord!')





@client.command()
@has_permissions(administrator=True)
async def kickroleless(ctx: commands.Context):
    members = ctx.guild.members
    kicked = 0
    for member in members:
        if len(member.roles) == 1:
            await member.kick()
            kicked += 1
    await ctx.reply(f'**{kicked}** members were kicked from the server.')

    
  
@client.event
async def on_message(message):
    if "<@bot_user_id>" in message.content:
        welcome = f"""**__👋 I'm Bot Kicker!__**
      
**⚠️⚠️WARNING!! MY ONLY COMMAND WILL DELETE ALL MEMBERS WITHOUT A ROLE!!**
      
Use `$kickroleless` to kick all users without a role. 

Developed by:https://twitter.com/bankkroll_eth
"""
        await message.channel.send(welcome)
        


if __name__ == '__main__':
    client.run(bot_token)
    
