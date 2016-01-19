# -*- coding: utf-8 -*-

import sqlite3 # nous importons le paquet Python capable d'interagir avec sqlite

db_loc = sqlite3.connect('Notes.db')
# créer ou ouvre un fichier nommé 'Notes.db' qui doit donc se trouver dans le même
# répertoire que l'endroit où Python est lancé sinon :


db_ram = sqlite3.connect(':memory:')
# Cette commande permet de créer une base de donnée en RAM
# (aucun fichier ne sera créer, il s'agit de cérer une base de données virtuelle).
# Cela permet notamment de vérifier des commandes avant de les lancer sur une base
# de données où les opérations sont irréversibles.

db_loc = sqlite3.connect('Notes.db')
cursor = db_loc.cursor()
# cursor est un object auquel on passe les commandes SQL en vue d'être executées.

cursor.execute('''CREATE TABLE eleve(
             id INTEGER PRIMARY KEY,
             name TEXT,
             first_name TEXT,
             classe TEXT);''')
# execute ne lance pas la commande
# il est important de noter le champ 'id' de type nombre entier qui sert de clef primaire
db_loc.commit()

eleves = [(3, "Hallyday", "Johnny", "5iemeB"), (4, "Mitchelle", "Eddy", "4ieme3"), (5, "Rivers", "Dick", "3ieme2")]
# liste de tuples contenant toutes les informations nécessaires pour ajouter les élèves à la base de données
cursor.executemany('''INSERT INTO eleve VALUES (?,?,?,?);''', eleves)
db_loc.commit()