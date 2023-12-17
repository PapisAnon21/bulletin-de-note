import sqlite3

connexion = sqlite3.connect('donne.db')
curseur = connexion.cursor()
notes 
requete = 'INSERT into notes_tc1_1(id,note_devoir) VALUES(n,16,connexion)'
curseur.execute(requete)
connexion.commit()
connexion.close()