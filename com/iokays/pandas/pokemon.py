#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pandas as pd

raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']
            }

pokemon = pd.DataFrame(raw_data)
print(pokemon.head())

pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]
print(pokemon.head())

pokemon['place'] = ['park','street','lake','forest']
print(pokemon.head())

print(pokemon.dtypes)





