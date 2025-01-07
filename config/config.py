import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))


def get_api_key():
    return config['DEFAULT']['OPENAI_API_KEY']
