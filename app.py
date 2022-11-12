import json
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)


# hi
# Hello


@bot.command(name="dog1")
async def SendMEssage(ctx):
    value = {
        "animal": "dog1",
        "number": 1,
    }
    print(json.dumps(value))

@bot.command(name="dog2")
async def SendMEssage(ctx):
    value = {
        "animal": "dog2",
        "number": 2,
    }
    print(json.dumps(value))

@bot.command(name="dog3")
async def SendMEssage(ctx):
    value = {
        "animal": "dog3",
        "number": 3,
    }
    print(json.dumps(value))


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("MTAzNTU0MzE4NTM4MTkzMzA5Ng.GuXShx.FS8Yr1jMU-m3XOCCRgFNwB2KxzeYC3ti03AyoQ")
