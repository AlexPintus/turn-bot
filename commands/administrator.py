import discord 

class AdministratorCommands:
    def __init__(self,bot):
        self.bot = bot
        self.setup_commands()
    
    def setup_commands(self):
        @self.bot.tree.command(name="clear-chat", description="Pulire un numero definito di messaggi precedenti al interno di una chat")
        async def clearChat(interaction: discord.Interaction, number: int):
            await interaction.response.defer(ephemeral=True)

            if not interaction.guild:
               await interaction.followup.send("Questo commando puo essere eseguito solo in un server")
               return

            if not interaction.user.guild_permissions.administrator:
                await interaction.followup.send("Devi essere un ammistratore per eseguire questo commando")
                return
            
            if number <= 0:
                await interaction.followup.send("Mi raccomando inserisci solo numeri maggiori di 0")
                return
            
            deleted = await interaction.channel.purge(limit=number)
            await interaction.followup.send(f"Ho rimosso {len(deleted)} messaggi come e stato richiesto.")