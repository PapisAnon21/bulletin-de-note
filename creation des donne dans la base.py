import sqlite3 

connexion = sqlite3.connect('donne.db')


requete_1 = 'DROP TABLE IF EXISTS user;'
requete_de_creation_default = '''CREATE TABLE IF NOT EXISTS user(
												id_user  SMALLINT not null primary key,
												prenom VARCHAR(30) not null,
												nom VARCHAR(30) not null,
												password VARCHAR(30),
												niveau VARCHAR(30) not null
);
'''
curseur = connexion.cursor()
#curseur.execute(requete_de_creation_default)


table_des_matiere = ''' CREATE TABLE IF NOT EXISTS matieres_and_mark_tc1_1(
							id_matiere SMALLINT not null primary key,
							matieres_name VARCHAR(30) not null,
							note_devoir SMALLINT not null,
							ponderation_devoir SMALLINT not null,
							note_examen SMALLINT not null,
							ponderation_examen SMALLINT not null,
							moyenne_semestrielle SMALLINT not null



);		 
'''

curseur.execute(requete_1)
curseur.execute(requete_de_creation_default)
curseur.execute(table_des_matiere)

connexion.commit()





connexion.close()