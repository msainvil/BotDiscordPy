from discord import Client
import discord
import logging
import logging.config
import time
from src import getMeteo
import random

class Bot(Client):

    def __init__(self):
        logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.INFO)
        self.logger = logging.getLogger('log')   
        handler = logging.StreamHandler()  
        handler.setLevel(logging.INFO)  
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') 

        handler.setFormatter(formatter)  
        self.logger.addHandler(handler)  

        f = time.ctime()
        super().__init__()
        self.icon = {"01d":"icon/01d@2x.png",
                "02d":"icon/02d@2x.png",
                "03d":"icon/03d@2x.png",
                "04d":"icon/04d@2x.png",
                "09d":"icon/09d@2x.png",
                "10d":"icon/10d@2x.png",
                "11d":"icon/11d@2x.png",
                "13d":"icon/13d@2x.png",
                "50d":"icon/50d@2x.png"
        }
        self.article = ["article/_sac_puma_.jpg",
                        "article/_casque_bl_.jpg",
                        "article/_struct_.jpg",
                        "article/_scoot_.jpg",
                        "article/_ordi_.jpg"]

        self.command = "Les commande sont : !Hello, !Méteo, !Telegram, !Nombre"
        self.Help = "!Hello : Pour avoir un salut , !Meteo +[Ville] : pour avoir la meteo d'eune ville accompagné d'un icone du temps , !Telegram : pour recevoir le lien du télégram en message privé , !Nombre : Pour generer un nombre aleatoire compris entre 0 et 100"
    
    async def on_ready(self):
        self.logger.info(f"{self.user} has connected to Discord!")
        #logging.info(f"{self.user} has connected to Discord!")
        print("The bot is ready")
    
    async def on_member_join(self,member):
        self.logger.info(f"{member.display_name} has joinned the Channel")
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")


    async def on_message(self, message):
        self.logger.warning(f"{message.author} has sent : {message.content}")
        if message.content == "!Help":
            await message.channel.send(self.command)
            await message.channel.send(self.Help)

        if message.content == "!Hello":
            await message.channel.send("Salut")

        
        if message.content.startswith('!Meteo'):
            ville = message.content.split()[-1]
            meteo = getMeteo(ville)['weather'][0]
  
            with open(self.icon[meteo['icon']], 'rb') as f:
                picture = discord.File(f)
            
            await message.channel.send(meteo['description']) 
            await message.channel.send(file=picture)
        
        if message.content == "!Telegram":
            await message.channel.send("nous vous avons envoyer le lien en privée")
            dm = await message.author.create_dm()  
            await dm.send("https://telegram.me/theprogrammingart")  

        if message.content == "!Nombre":
            nombre = random.randint(0,100)
            await message.channel.send(nombre)

        if message.content == "!Image":
            indice = random.randint(0,len(self.article)-1)
            with open(self.article[indice], 'rb') as f:
                picture = discord.File(f)  

            await message.channel.send(file=picture)



        






    

