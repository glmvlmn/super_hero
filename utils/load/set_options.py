import requests
import json

api_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'


def from_api(api_url):
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()
    return data


def load_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


api_data = from_api(api_url)


def with_key(data, key):
    if isinstance(data, dict):
        return data.get(key)
    elif isinstance(data, list):
        values = []
        for item in data:
            if isinstance(item, dict):
                value = item.get(key)
                if value is not None:
                    values.append(value)
    return values if values else None


def search_hight(api_data):
    list_hero_dict = []
    hero_hight = 0
    for hero in api_data:

        occupation = with_key(hero['work'], "occupation")
        gender = with_key(hero["appearance"], "gender")
        if occupation != '-' and gender != '-':
            hieght = with_key(hero["appearance"], "height")
            rost = hieght[1].split()
            if float(rost[0]) > hero_hight:
                hero_hight = float(rost[0])
                name = with_key(hero, 'name')
    list_hero_dict.append(name)


    print(f'Cамый высокий герой по заданым входным данным: {''.join(list_hero_dict)}!')
    return ''.join(list_hero_dict)


class Find_hero:

    def find_hero():
        search_hight(api_data)
