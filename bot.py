import discord
import random

import os

from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot en ligne !"

def run_web():
    app.run(host='0.0.0.0', port=8080)


TOKEN = os.getenv("DISCORD_TOKEN")

# Active les permissions de lecture de message
intents = discord.Intents.default()
intents.message_content = True

# Création du client Discord
client = discord.Client(intents=intents)

# Banque de phrases
phrases = [
    "Test 1",
    "test 2",
    "test 3",
    "test 4",
    "test 5"
]

@client.event
async def on_ready():
    print(f"✅ Connecté en tant que {client.user}")

@client.event
async def on_message(message):
    # Ignore les messages du bot lui-même
    if message.author == client.user:
        return

    # Si un message commence par !promptWB
    if message.content.startswith("!promptWB"):
        phrase = random.choice(phrases)
        await message.channel.send(phrase)

# Démarrage du bot
threading.Thread(target=run_web).start()
client.run(TOKEN)
