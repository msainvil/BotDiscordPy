
from argparse import ArgumentParser, Namespace
import json
import requests

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    return parser.parse_args()

def get_config(file_name):
    with open(file_name, "r") as file:
        config = json.load(file)
    return config


def getMeteo(ville):
    config = get_config(parse_args().config)
    api_key = config["api_openweathermap"]
    city = ville.lower()
    url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s" %(city,api_key)
    print(url)
    r = requests.get(url)
    if r.status_code == requests.codes.NOT_FOUND:
        print("ip not found")
    if r.status_code == requests.codes.OK:
        return r.json()