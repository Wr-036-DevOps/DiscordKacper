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


@bot.command(name="dog")
async def SendMEssage(ctx, arg):
    sqs_client = boto3.client("sqs", region_name="eu-central-1")
    if int(arg) < 5:
        message = {
            "animal": "dog",
            "number": arg, }  # {"animal": "dog", "number": "n"}
        response = sqs_client.send_message(
            QueueUrl="https://sqs.eu-central-1.amazonaws.com/536460581283/akaque",
            MessageBody=json.dumps(message)
        )
        print(response)
    else:
        print("Too much images")


@bot.command(name="cat")
async def SendMEssage(ctx, arg):
    sqs_client = boto3.client("sqs")

    if int(arg) < 5:
        message = {
            "animal": "cat",
            "number": arg, }
        response = sqs_client.send_message(
            QueueUrl="https://sqs.eu-central-1.amazonaws.com/536460581283/akaque",
            MessageBody=json.dumps(message)
        )
        print(response)
    else:
        print("Too much images")


@bot.command(name="elephant")
async def SendMEssage(ctx, arg):
    sqs_client = boto3.client("sqs")

    if int(arg) < 5:
        message = {
            "animal": "elephant",
            "number": arg, }
        response = sqs_client.send_message(
            QueueUrl="https://sqs.eu-central-1.amazonaws.com/536460581283/akaque",
            MessageBody=json.dumps(message)
        )
        print(response)
    else:
        print("Too much images")


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")
    bot.run(TOKEN)
