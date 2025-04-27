import requests
import json


class Get_json:

    def from_api(api_url):
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data

    def load_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
