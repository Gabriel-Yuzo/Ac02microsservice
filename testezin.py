


import requests
from pokemon import Pokemon, PokemonNaoExisteException, numero_do_pokemon
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "http://pokeapi.co"
limite = (4, 12)



def evolucao_anterior(nome):
    if nome == "": raise Pokemon.PokemonNaoExisteException()
    idPokemon = numero_do_pokemon(nome)
    respRequest = requests.get(f"{site_pokeapi}/api/v2/pokemon-species/{idPokemon}/", timeout=limite)
    if  respRequest.status_code != 200: raise PokemonNaoExisteException()
    returnNamePokemon = respRequest.json()
    if returnNamePokemon["evolves_from_species"] is None:
        return print(None)
    else:
        return print(returnNamePokemon["evolves_from_species"]["name"])





evolucao_anterior("togepi")