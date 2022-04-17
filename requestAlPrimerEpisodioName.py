import requests
import json
url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()
# TODO: muestra una lita de episodios print(j['characters'])
personajes = j['characters']
list_names = list()  # TODO: lista para guardar nombres


for personaje in personajes:  # TODO:  recorremos la lista y xcada episodio
    req = requests.get(personaje)  # TODO: traemos cada personaje
    js = req.json()  # TODO: pasamos cada id de personaje a json
    name = js['name']  # TODO:  extraemos de cada personaje el nombre
    print(name)  # TODO: se muestra cada nombre del episodio 1
    # TODO: cada nombre lo agregamos en una lista previamente declarada
    list_names.append(name)

print(list_names)  # TODO: imprimimos la lista
