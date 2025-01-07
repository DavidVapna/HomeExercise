import configparser
import os
#config.ini file required, private data kept there.
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))


def get_api_key():
    return config['DEFAULT']['OPENAI_API_KEY']
