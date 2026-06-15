import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime


class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged as {self.user}")

        try: 
            guild = discord.Object(id=Your guild ID)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print (f'Error syncing commands {e}')

    async def on_message(self, message):
        print(f'Wiadomość od {message.author}: {message.content}')
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi {message.author}')
        if "ping" in message.content:
            await message.channel.send('pong')
        if "pong" in message.content:
            await message.channel.send('ping')
        
    #async def on_reaction_add(self, reaction, user):
        #await reaction.message.channel.send(f'{user} reacted to a message')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

TEST_GUILD = discord.Object(id=Your guild ID)

now = datetime.now()

@client.tree.command(name="hello", description="Says hello", guild = TEST_GUILD)
async def Hello(interaction: discord.Interaction):
    await interaction.response.send_message('Hello there!')

@client.tree.command(name="print", description="Makes the bot type whatever you imput", guild = TEST_GUILD)
async def Print(interaction: discord.Interaction, input: str):
    await interaction.response.send_message(input)

@client.tree.command(name="embed", description="Embed test", guild = TEST_GUILD)
async def Embed(interaction: discord.Interaction):
    embed = discord.Embed(title="Title", url="https://www.youtube.com/@krahscimsoc", description="Description", color=interaction.user.top_role.color)
    embed.set_thumbnail(url=client.user.display_avatar.url)
    embed.add_field(name="Field 1", value="Field content")
    embed.add_field(name="Field 2", value="CosmicBot is the greatest bot ever (trust)")
    embed.add_field(name="Field 3", value="Honestly, I don't know what to put here", inline=False)
    embed.set_footer(text="Footer")
    embed.set_author(name=interaction.user.name, url="https://discord.com/channels/1353423401108377720/1513587799578640514",icon_url=interaction.user.display_avatar.url)
    await interaction.response.send_message(embed=embed)
    
@client.tree.command(name="check_info", description="Displays user information", guild = TEST_GUILD)
async def Profile(interaction: discord.Interaction):
    roles = [role.mention for role in reversed(interaction.user.roles) if role.name != "@everyone"]
    embed = discord.Embed(title=interaction.user.name, description="Your information: ", color=interaction.user.top_role.color)
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.add_field(name="Main role", value=interaction.user.top_role.name, inline=False)
    embed.add_field(name="Joined", value=interaction.user.joined_at.strftime("%d.%m.%Y %H:%M"))
    embed.add_field(name="Registered", value=interaction.user.created_at.strftime("%d.%m.%Y %H:%M"))
    embed.add_field(name="Roles", value=roles, inline=False)
    embed.set_footer(text=now.strftime("%d.%m.%Y %H:%M"))
    await interaction.response.send_message(embed=embed)

class View(discord.ui.View):
    @discord.ui.button(label="Click me", style=discord.ButtonStyle.red, emoji="👍")
    async def button_callback(self, button, interaction):
        await button.response.send_message(f"{interaction.user.name} clicked me.")

    @discord.ui.button(label="Button 2", style=discord.ButtonStyle.blurple, emoji="🤔")
    async def button_link(self, button, interaction):
        await button.response.send_message("My YouTube channel" url="https://www.youtube.com/@krahscimsoc")

    @discord.ui.button(label="Button 3", style=discord.ButtonStyle.green, emoji="☢️")
    async def button_callback(self, button, interaction):
        await button.response.send_message("You have successfully clicked the button.")

@client.tree.command(name="button", description="Test button", guild = TEST_GUILD)
async def buttonTest(interaction: discord.Interaction):
   await interaction.response.send_message(view=View())
  
client.run("Your bot token")
