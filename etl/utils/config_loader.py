import os
import yaml
from scripts.find_root import find_project_root

path_to_config = os.path.join(find_project_root(), "configs/api_config.yaml")
    
def load_config():
    with open(path_to_config, "r") as file:
        return yaml.safe_load(file)