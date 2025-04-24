import yaml
import os
def open_file(file_name):
    with open(file_name) as f:
        k = f.read()
        return k

def read_config():
    config_file = os.path.join(os.path.expanduser('~'), '.config/jarvis', 'config.yaml')
    with open(config_file) as file:
        configration = yaml.safe_load(file)
        model = configration['model']
    return model
        
    
