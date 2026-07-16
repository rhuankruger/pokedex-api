import requests

def buscapokedex():

    escolha = input("Escolha um Pokémon: ")
    
    try:
        resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{escolha.lower()}")

        if resposta.status_code == 200:
            dados = resposta.json()
        
        elif resposta.status_code == 404:
            print("Pokémon não encontrado!")
    
    except requests.ConnectionError:
        print("ERRO: Sem internet")
    except requests.Timeout:
        print("ERRO: O servidor demorou muito para conectar!")

    pokenome =  dados["name"]
    poketipo = dados["types"][0]["type"]["name"]
    pokealtura = dados["height"]
    pokepeso = dados["weight"]

    return pokenome, poketipo, pokealtura, pokepeso