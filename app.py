import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
# hi
# Hello

@bot.command(name="hi")
async def SendMEssage(ctx):
    await ctx.send('Hello')

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
if __name__ == '__main__':
    bot.run("MTAzNzExMjU5MDU0NDkzMjkxNQ.GWkIEE.H4XO9b8-KS8naL6mj0w2OxH5eeb-hhtOhAaeIo")