import nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True
command_prefix = '!'

client = commands.Bot(command_prefix, intents = intents)

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  print(command_prefix)

testserver = 988598060538015815

@nextcord.slash_command(name = "hello", description = "Bot Says Hello", guild_ids = [testserver])
async def hellocommand(interaction: Interaction):
  await interaction.response.send_message("yoooo")


client.run("MTAzNTU0MzE4NTM4MTkzMzA5Ng.GT1uxl.nEvPEUXS1oDql5KpsuDUcsOdWW8bc-Cl2mkG8U")
