"""Anonimowe disco wyznania"""
import discord
from discord.ext import commands
from discord.ext.commands import DefaultHelpCommand
from utils import read_json_file
from utils import get_commit_version


class CustomHelpCommand(DefaultHelpCommand):

    def __init__(self, **options):
        super().__init__(**options)
        self.no_category = 'General'


config = read_json_file('config.json')
desc = 'AnonimoweDiscoWyznania.'
intents = discord.Intents.default()
intents.message_content = True
activity = discord.Game('Made by NosApki')
bot = commands.Bot(
    intents=intents,
    command_prefix='!',
    activity=activity,
    description=desc,
    help_command=CustomHelpCommand(),
)


@bot.event
async def on_ready():
    """Print that bot logged in as."""
    print(f'Logged in as {bot.user.name} | ID: {bot.user.id}!')


@bot.command(brief='Shows user avatar')
async def avatar(ctx):
    if ctx.message.mentions:
        mention = ctx.message.mentions[0]
        await ctx.send(mention.avatar.url)


@bot.command(brief='Estimates ping from bot server to discord')
async def ping(ctx):
    await ctx.send(f'Pong: {round(bot.latency, 7)}...')


@bot.command(brief='Get actual running version of AnonimoweDiscoWyznania')
async def version(ctx):
    await ctx.send(f'{get_commit_version()}')


bot.run(config.get('token'))