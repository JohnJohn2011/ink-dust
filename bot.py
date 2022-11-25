import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '!')

@bot.event
async def funcname(parameter_list):
    print(">> bot is online <<")

bot.run('MTA0NDIwNDUzMjQ1ODA2MTgyNQ.GGXI9p.lTagWO8Bnw3OZwWQCTnc7Hq-VzMWXMqNCQCKtE')