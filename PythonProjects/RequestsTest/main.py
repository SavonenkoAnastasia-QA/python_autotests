import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '{ТОКЕН}'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}

body_confirmation = {
    'trainer_token' : TOKEN
    }

body_change = {
    "pokemon_id": "390278",
    "name": "Бибуля",
    "photo_id": 385
}

body_pokeball = {
    "pokemon_id": "390278"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_change)
print(response_change.text)'''

response_pakeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball) 

print(response_pakeball.text)
