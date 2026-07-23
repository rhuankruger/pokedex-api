from api import buscapokedex
from menu import menu
from database import inserir_pokemon, ctrlc_pokemon, ctrlv_pokemon, ver_pokedex, remover_pokemon

while True:
    decisao = menu()

    if decisao == 1:
        nome, tipo, altura, peso = buscapokedex()
        inserir_pokemon(nome, tipo, altura, peso)
        ctrlc_pokemon()
        ctrlv_pokemon()

    elif decisao == 2:
        ver_pokedex()

    elif decisao == 3:
        remover_pokemon()

    elif decisao == 4:
        print("Até mais, não esqueça de avaliar nosso app!")
        print("Até logo, obrigado por usar a PokeDex!")
        break