import yaml
import os
def open_file(file_name):
    with open(file_name) as f:
        k = f.read()
        return k

def read_config():
    config_file = os.path.join(os.path.expanduser('~'), '.config/jarvis', 'config.yaml')
    try:
        with open(config_file) as file:
            configration = yaml.safe_load(file)
            provider = configration['provider']
            api_key = configration['api_key']
            model = configration['model']
            return provider, model, api_key
    except:
        print('failed to read the config file, does ~/.config/jarvis/config.yaml exist?')
