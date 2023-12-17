import sqlite3

connexion = sqlite3.connect('database.db')
curseur = connexion.cursor()

niveau = 'tc1'
semestre = str(2)
table_a_charger = 'matieres_notes_' + niveau + '_' + semestre
print(table_a_charger)

requete = 'SELECT * FROM ' + table_a_charger
print(requete)
c = curseur.execute(requete)
print(c.fetchall())
# test reusi a 100%
