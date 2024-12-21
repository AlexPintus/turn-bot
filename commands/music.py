import discord
from discord import FFmpegPCMAudio

class MusicCommands:
    def __init__(self, bot):
        self.bot = bot
        self.setup_commands()

    def setup_commands(self):
        @self.bot.tree.command(name="join", description="Unisciti al canale vocale")
        async def join(interaction: discord.Interaction):
            # Controlla se l'utente è in un canale vocale
            if interaction.user.voice is None or interaction.user.voice.channel is None:
                await interaction.response.send_message("Devi essere connesso a un canale vocale per utilizzare questo comando!")
                return
        
            # Ottieni il canale vocale dell'utente
            channel = interaction.user.voice.channel
            
            # Connettiti al canale vocale
            await channel.connect()
            await interaction.response.send_message("Connesso al canale vocale!")


        @self.bot.tree.command(name="leave", description="Lascia il canale vocale")
        async def leave(interaction: discord.Interaction):
            await interaction.guild.voice_client.disconnect()
            await interaction.response.send_message("Disconnesso dal canale vocale!")

        @self.bot.tree.command(name="play", description="Riproduci un file musicale")
        async def play(interaction: discord.Interaction, music_name: str):
            messages = [message async for message in interaction.channel.history(limit=50)]  # Ricava i messaggi recenti
            audio_url = None

            for message in messages:
                if message.attachments:
                    for attachment in message.attachments:
                        print(attachment.filename)
                        if music_name in attachment.filename.lower():
                            audio_url = attachment.url
                            break
                if audio_url:
                    break

            if not audio_url:
                await interaction.channel.send(f"Non ho trovato il file `{music_name}`!")
                return

            # Controlla che l'utente sia in un canale vocale
            channel = interaction.user.voice.channel
            if not channel:
                await interaction.channel.send("Devi essere in un canale vocale per usare questo comando!")
                return

            # Connettiti al canale vocale e riproduci il file
            vc = await channel.connect()
            # Usa FFmpegPCMAudio per trasmettere direttamente dallo stream
            source = FFmpegPCMAudio(audio_url)
            vc.play(source, after=lambda e: print("Riproduzione terminata", e))

        @self.bot.tree.command(name="pause", description="Pausa la musica")
        async def pause(interaction: discord.Interaction):
            voice_client = interaction.guild.voice_client
            if voice_client.is_playing():
                voice_client.pause()
                await interaction.response.send_message("Musica in pausa.")
            else:
                await interaction.response.send_message("Nessuna musica in riproduzione.")

        @self.bot.tree.command(name="resume", description="Riprendi la musica")
        async def resume(interaction: discord.Interaction):
            voice_client = interaction.guild.voice_client
            if voice_client.is_paused():
                voice_client.resume()
                await interaction.response.send_message("Riprendendo la musica.")
            else:
                await interaction.response.send_message("La musica non è in pausa.")

        @self.bot.tree.command(name="stop", description="Ferma la musica")
        async def stop(interaction: discord.Interaction):
            voice_client = interaction.guild.voice_client
            if voice_client.is_playing():
                voice_client.stop()
                await interaction.response.send_message("Musica fermata.")
            else:
                await interaction.response.send_message("Nessuna musica in riproduzione.")
