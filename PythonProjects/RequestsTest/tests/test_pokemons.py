import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9c73e6bcf09e809f77fe2ca382c20daf'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '39743'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'),('trainer_id', TRAINER_ID), ('id', '390278')])
def test_parametrize(key, value):
    response_parametrize= requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()['data'][0][key] == value

def test_status_code_trainer():
    response_trainer = requests.get(url=f'{URL}/trainers')
    assert response_trainer.status_code == 200

def test_name_trainer():
    response_name = requests.get(url=f'{URL}/trainers/39743')
    assert response_name.json()['trainer_name'] == 'Gante'
