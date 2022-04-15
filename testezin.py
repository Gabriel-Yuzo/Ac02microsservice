


from unicodedata import name
import requests
from pokemon import Pokemon, PokemonNaoExisteException, numero_do_pokemon
site_treinador = "http://127.0.0.1:9000"
site_pokeapi = "http://pokeapi.co"
limite = (4, 12)



def evolucoes_proximas(nome):
    lista =[]
    if nome == "": raise PokemonNaoExisteException()

    respRequest = requests.get(f"{site_pokeapi}/api/v2/pokemon-species/{nome}/", timeout=limite)

    respUrl = respRequest.json()

    evolutionChain = respUrl["evolution_chain"]["url"]

    requestEvolve =  requests.get(evolutionChain)

    
    jsonEvolucao = requestEvolve.json()

    if jsonEvolucao['chain']["species"]["name"] == name:
        lista.append(jsonEvolucao["chain"]["evolves_to"][0]["species"]["name"])

    evolucao = jsonEvolucao["chain"]["evolves_to"][0]["species"]["name"]
    if nome == evolucao:
        evolus = jsonEvolucao["chain"]["evolves_to"][0]['evolves_to']
        print(evolus)
        for evolu in evolus:  
            x = evolus[evolu["species"]["name"]]
            print(x)
            lista.append()        

    return print(lista)   





evolucoes_proximas("ivysaur")
