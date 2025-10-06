import os
import discord
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://models.github.ai/inference"
<<<<<<< HEAD
model = "openai/gpt-4.1-mini"
#deepseek/DeepSeek-V3-0324
#openai/gpt-4.1-mini
=======
model = "deepseek/DeepSeek-R1-0528" #" deepseek/DeepSeek-V3-0324
>>>>>>> 143630af493972767f95201891c560ab8c2d07e3
token = os.getenv('AI_TOKEN')
discord_token = os.getenv('DISCORD_TOKEN')

clientAI = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

intents = discord.Intents.all()
intents.message_content = True

client = commands.Bot(command_prefix='',intents=intents)

@client.event
async def on_ready():
    print("2B Activated.")

intents.members = True
'''s'''

@client.event
async def on_message(message, *, erm=""):
    userquery = message.content
    author = message.author
    if message.author == client.user:
        return

    if message.content.startswith("twob"):
        await message.reply(f'{author}, i\'m here. <:2B_smile:1383738668413620295>')
    
    if message.content.startswith(erm):
        print(f'{author}: {userquery}')
        response = clientAI.complete(
            messages=[
                SystemMessage(f"."),
                UserMessage(userquery),
            ],
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model
        )
<<<<<<< HEAD
        if message.reference and message.reference.message_id:
            replied_to = await message.channel.fetch_message(message.reference.message_id)
        if replied_to.author == client.user:
            await message.reply(response.choices[0].message.content, mention_author=True)
=======
        await message.reply(response.choices[0].message.content, mention_author=True)
        
client.run(discord_token)
>>>>>>> 143630af493972767f95201891c560ab8c2d07e3

client.run(discord_token)
