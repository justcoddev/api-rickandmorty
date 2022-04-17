import requests
import json

# TODO:  request simple.................................................

url = 'https://rickandmortyapi.com/api/character/2'
r = requests.get(url)
j = r.json()
#print(j.keys()) # TODO: para imprimir todas las llaves
status = j['status']
print(status)

i = 1

while i < 6:
    url = 'https://rickandmortyapi.com/api/character/{}'.format(i)
    r = requests.get(url)
    j = r.json()
    name = j['name']
    status = j['status']
    print('El personaje {} tiene status: {}'.format(name, status))
    #print(f'El personaje {name} tiene status: {status}')
    i += 1


