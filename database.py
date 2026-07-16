import sqlite3

conexao = sqlite3.connect("pokedexdesafioxx.db")

cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        nome TEXT UNIQUE,
        tipo TEXT,
        altura REAL,
        peso REAL
    )
""")

def inserir_pokemon(nome, tipo, altura, peso):
    cursor.execute("""
        INSERT OR IGNORE INTO pokemon
        VALUES (?, ?, ?, ?)
    """, (nome, tipo, altura, peso))

def ctrlc_pokemon():
    cursor.execute("""
        SELECT * FROM pokemon
    """)

    selecao = cursor.fetchall()
    return selecao

def ctrlv_pokemon():
    selecao = ctrlc_pokemon()
    print(f'Pokémon escolhido: {selecao[-1][0].capitalize()}')
    print(f'Tipo: {selecao[-1][1].capitalize()}')
    print(f'Altura: {selecao[-1][2]}')
    print(f'Peso: {selecao[-1][3]}')
    print("Banco de dados atualizado!")

def ver_pokedex():
    selecao = ctrlc_pokemon()

    for i, tupla_pokemon in enumerate(selecao, start=1):
        print(f'Pokémon {i}: {tupla_pokemon[0].capitalize()}')

def pokedex_lista():
    selecao = ctrlc_pokemon()
    lista_pokedex = []

    for tupla in selecao:
        pokemon_loop = tupla[0]
        lista_pokedex.append(pokemon_loop)
    
    return lista_pokedex

def remover_pokemon():
    remocao = input("Escola um pokemón para remover: ")
    lista = pokedex_lista()
    if remocao in lista:
        cursor.execute("""
            DELETE FROM pokemon
            WHERE nome = ?
        """, (remocao,))
        conexao.commit()
        print("Removido com Sucesso!")
    
    else:
        print("Não encontrado!")