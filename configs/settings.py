import os
from dotenv import load_dotenv
import yaml
from urllib.parse import urlencode
from scripts.find_root import find_project_root
from etl.utils.config_loader import load_config

PROJECT_ROOT = find_project_root()
load_dotenv(PROJECT_ROOT / '.env')

config = load_config()

API_KEYS = {
    'weather_api': os.getenv('WEATHER_API_KEY'),
    'holiday_api': os.getenv('HOLIDAY_API_KEY'),
}

def build_url(service_name, endpoint_name=None, **override_params):
    """
    Build complete API URL with parameters and API key
    
    service_name: 'weather_api', 'holiday_api', etc.
    endpoint_name: specific endpoint key (optional)
    override_params: dynamic parameters to add/override
    """
    service = config.get(service_name)
    base_url = service['base_url']

    if endpoint_name:
        endpoint = service['endpoints'].get(endpoint_name)
        url = f"{base_url}{endpoint}"
    else:
        url = base_url
    
    # Merge params: config defaults + overrides
    params = {**service['params'], **override_params}

    # Add API key if available
    if service_name in API_KEYS:
        params[service['auth']['key_name']] = API_KEYS[service_name]
    
    # Build the final url
    if params:
        query_string = urlencode(params)
        url = f"{url}?{query_string}"
    return url
