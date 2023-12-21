"""Anonimowe disco wyznania"""
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import DefaultHelpCommand

from utils import get_commit_version, read_json_file


class CustomHelpCommand(DefaultHelpCommand):

    def __init__(self, **options):
        super().__init__(**options)
        self.no_category = 'General'


config = read_json_file('config.json')
desc = 'AnonimoweDiscoWyznania.'
intents = discord.Intents.default()
intents.message_content = True
activity = discord.Game('Made by NosApki')
client = discord.Client(
    intents=intents,
    command_prefix=config.get('cmd_prefix', '/'),
    activity=activity,
    description=desc,
    help_command=CustomHelpCommand(),
)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    """Print that bot logged in as."""
    print(f'Logged in as {client.user.name} | ID: {client.user.id}!')
    await tree.sync()


class AnonymousModal(discord.ui.Modal, title='AnonimoweDiscoWyznania'):
    designation = discord.ui.TextInput(
        label='Wyznanie',
    )

    async def on_submit(self, interaction):
        pass


@tree.command(description='Wyślij anonimową wiadomość')
async def anonim(interaction):
    await interaction.response.send_modal(AnonymousModal())


client.run(config.get('token'))
