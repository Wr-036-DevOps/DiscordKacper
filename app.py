import json
import boto3
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command(aliases=["show"])
async def SendMEssage(ctx,search,*,arg:int):
    animalList = ["dog", "cat", "elephant","monkey","lion","shark","bird","bear","fish","horse","chicken"]
    
    sqs_client = boto3.client("sqs", region_name="eu-central-1")
    
    if arg < 6 and search in animalList:
        message = {
            "animal": search,
            "number": arg, } 
        response = sqs_client.send_message(
            QueueUrl="https://sqs.eu-central-1.amazonaws.com/536460581283/akaque",
            MessageBody=json.dumps(message)
        )
        print(response)
    elif arg>=6:
        channel = bot.get_channel(1034847969255628884)
        await channel.send("Too much images - max number is: 5")
        print("Too much images")  
    else:
        channel = bot.get_channel(1034847969255628884)
        await channel.send("This animal not exist available animals are: {}".format(animalList))
        print("This animal not exist available animals are:")

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    bot.run(TOKEN)
