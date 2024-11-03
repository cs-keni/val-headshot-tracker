import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.messages = True

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!", intents=intents)

overall_headshot_rate = 

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    
@bot.command(name="headshot")
async def fetch_headshot_stats(ctx):
    puuid = "sample_puuid"
    matches = get_recent_matches(puuid)
    if matches:
        await ctx.send(f"Recent match data: {matches}")
    else:
        await ctx.send("Could not fetch match data.")
    
def get_recent_matches(puuid):
    url = f"https://americas.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}"
    headers = {"X-Riot-Token": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching matches:", response.status_code)
        return None
    
def calculate_headshot_percentage(match_data):
    headshots = match_data.get("headshots", 0)
    bodyshots = match_data.get("bodyshots", 0)
    legshots = match_data.get("legshots", 0)
    
    total_shots = headshots + bodyshots + legshots
    if total_shots == 0:
        return 0, headshots
    
    headshot_percentage = (headshots / total_shots) * 200
    return headshot_percentage, headshots
    
bot.run(DISCORD_TOKEN)