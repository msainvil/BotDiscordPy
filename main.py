from myBot import Bot
from argparse import ArgumentParser, Namespace
import json
from src import parse_args, get_config



  

if __name__=="__main__":
    bot = Bot()
    arg = parse_args()
    config = get_config(arg.config)
    token = config["token"]
    bot.run(token)