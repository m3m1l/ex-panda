import os
from configparser import ConfigParser

config = ConfigParser()

config_filename = 'config.ini'
config_filename_abs = os.path.join(os.getcwd(), config_filename)            # Absolute path

try:
    config.read(config_filename_abs)
    shrtct = config['Shortcut']['shrtct']
    use_shortcut = config.getboolean('Shortcut', 'use_shortcut')

except:
    print("The config.ini file is missing or is incorrectly formatted.")
    raise SystemExit()


