import json
import boto3
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="", intents=intents)

@bot.command(name="dog1")
async def SendMEssage(ctx):
    sqs_client = boto3.client("sqs")
    message = {
        "animal": "dog",
        "number": 1, }
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/536460581283/akaque",
        MessageBody=json.dumps(message)
    )
    print(response)


@bot.command(name="dog2")
async def SendMessage(ctx):
    sqs_client = boto3.client("sqs")
    message = {
        "animal": "dog",
        "number": 2, }
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/536460581283/akaque",
        MessageBody=json.dumps(message)
    )
    print(response)

@bot.command(name="dog3")
async def SendMessage(ctx):
    sqs_client = boto3.client("sqs")
    message = {
        "animal": "dog",
        "number": 3, }
    response = sqs_client.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/536460581283/akaque",
        MessageBody=json.dumps(message)
    )
    print(response)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':

    bot.run("KEY_HERE")

