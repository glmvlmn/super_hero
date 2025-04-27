import requests

api_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
class Check:


    def hero():
        response = requests.get(api_url)
        assert response.status_code == 200
        assert response.json()[0]["name"] == "A-Bomb"
        assert response.headers["Connection"] == "keep-alive"