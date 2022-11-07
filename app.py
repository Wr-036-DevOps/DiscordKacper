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
    print(1)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(1, f, ensure_ascii=False, indent=4)

@bot.command(name="dog2")
async def SendMEssage(ctx):
    print(2)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(2, f, ensure_ascii=False, indent=4)

@bot.command(name="dog3")
async def SendMEssage(ctx):
    print(3)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(3, f, ensure_ascii=False, indent=4)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("MTAzNTU0MzE4NTM4MTkzMzA5Ng.GuXShx.FS8Yr1jMU-m3XOCCRgFNwB2KxzeYC3ti03AyoQ")
