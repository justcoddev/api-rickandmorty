import requests
import json
url = 'https://rickandmortyapi.com/api/episode/1'
r = requests.get(url)
j = r.json()
# TODO: muestra una lita de episodios print(j['characters'])
personajes = j['characters']
list_names_human = list()  # TODO: lista para guardar nombres de human species
list_names_other = list()  # TODO: lista para guardar nombres de otras species


for personaje in personajes:  # TODO:  recorremos la lista y xcada episodio
    req = requests.get(personaje)  # TODO: traemos cada personaje
    js = req.json()  # TODO: pasamos cada id de personaje a json
    name = js['name']  # TODO:  extraemos de cada personaje el nombre
    print(name)  # TODO: se muestra cada nombre del episodio 1
    '''
    Aqui el detalle
    '''
    if js['species'] == 'Human':    # TODO:  si el personaje en la llave Species es humano o no
        list_names_human.append(name) # TODO: se agrega el name de specie human a la lsit
    else:
        list_names_other.append(name)  # TODO: se agrega el name de specie otra a la lsit



print(list_names_human)  # TODO: imprimimos la lista
print(list_names_other)  # TODO: imprimimos la lista
