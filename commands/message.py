import discord
import asyncio 
import re
from transformers import MarianMTModel, MarianTokenizer


def check_string(s):
    # Controllo per numeri
    if re.match(r'^[0-9]+$', s):
        return "Errore: la stringa contiene solo numeri"
    
    # Controllo per sigle 'm', 'h', 's'
    if re.match(r'^[mhs]+$', s):
        return "Errore: la stringa contiene solo lettere 'm', 'h', o 's'"

    # Se la stringa contiene una combinazione di numeri e lettere non valide
    return None  # Nessun errore

def split_time_string(s):
    # Cerca un numero seguito da una lettera (m, h o s)
    match = re.match(r'(\d+)([mhs])', s)
    
    if match:
        time = int(match.group(1))  # Estrai il numero come intero
        unit = match.group(2)        # Estrai la sigla
        return time, unit
    else:
        return None  # La stringa non è nel formato corretto


class MessageCommands:
    def __init__(self,bot):
        self.bot = bot
        self.setup_commands()

    def setup_commands(self):
        @self.bot.tree.command(name="delayed-message",description="Invia un messaggio dopo un certo tempo")
        async def delayedMessage(interaction: discord.Interaction, delay:str, message: str):
            check_result = check_string(delay)

            if check_result:
                await interaction.response.send_message(check_result)
                return
            
            result = split_time_string(delay)

            if result:
                time, unit = result
                if unit == 'm':
                    time *= 60
                elif unit == 'h':
                    time *= 3600

                await interaction.response.send_message("Invio programmato")
                await asyncio.sleep(time)
                await interaction.followup.send(message)
            else: 
                await interaction.response.send_message("Si è verificato un errore") 

        @self.bot.tree.command(name="translate-message",description="Invia un messaggio tradotto in una determinata lingua.")
        async def translateMessage(interaction: discord.Interaction, message: str):
            await interaction.response.defer()  # Segnala che il bot sta elaborando la richiesta.
            # Carica il modello e il tokenizer
            model_name = 'Helsinki-NLP/opus-mt-it-en'
            model = MarianMTModel.from_pretrained(model_name)
            tokenizer = MarianTokenizer.from_pretrained(model_name)

            # Traduci il testo
            translated = tokenizer.decode(model.generate(tokenizer.encode(message, return_tensors="pt"), num_beams=4, max_length=50)[0], skip_special_tokens=True)

            await interaction.followup.send(translated)
                               
                                            
                                
