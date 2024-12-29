import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_pokemons = {
    "name": "Tagiil",
    "photo_id": 111
}
body_change = {
    "pokemon_id": "174756",
    "name": "Bulba",
    "photo_id": 44
}
body_catch = {
    "pokemon_id": "174756"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)