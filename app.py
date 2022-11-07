import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)

# hi
# Hello



@bot.command(name="1")
async def SendMEssage(ctx):
    await ctx.send(
        'https://media3.giphy.com/media/xT1XGEyW6Ra9TMA1vW/giphy.gif?cid=ecf05e47khj6tnviib82w52jgihr5ialauoz27414zz43332&rid=giphy.gif&ct=g')
@bot.command(name="2")
async def SendMEssage(ctx):
    await ctx.send(
        'https://media3.giphy.com/media/xT1XGEyW6Ra9TMA1vW/giphy.gif?cid=ecf05e47khj6tnviib82w52jgihr5ialauoz27414zz43332&rid=giphy.gif&ct=g')

@bot.command(name="3")
async def SendMEssage(ctx):
    await ctx.send(
        'https://media3.giphy.com/media/xT1XGEyW6Ra9TMA1vW/giphy.gif?cid=ecf05e47khj6tnviib82w52jgihr5ialauoz27414zz43332&rid=giphy.gif&ct=g')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("MTAzNTU0MzE4NTM4MTkzMzA5Ng.GuXShx.FS8Yr1jMU-m3XOCCRgFNwB2KxzeYC3ti03AyoQ")
