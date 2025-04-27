import requests
from utils.load.json import Get_json
from utils.options.value import Value

api_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
api_data = Get_json.from_api(api_url)


class Give_options:

    def hight():
        Value.search_hight(api_data)


give_options=Give_options()


class Check:

    def check_hero():
        response = requests.get(api_url)
        assert response.status_code == 200
        assert response.json()[0]["name"] == "A-Bomb"
        assert response.headers ["Connection"] == "keep-alive"





