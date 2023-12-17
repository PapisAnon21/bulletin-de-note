import sqlite3 

connexion = sqlite3.connect('database.db')
curseur = connexion.cursor()


### CREATEtion de nos tables
"""
#requete_1 = 'DROP TABLE IF EXISTS user;'
creation_user= '''CREATE TABLE IF NOT EXISTS user_ingenieur(
												id_user INTEGER primary key autoincrement,
												prenom VARCHAR(30),
												nom VARCHAR(30),
												password VARCHAR(30),
												niveau VARCHAR(30) 
);
'''



matieres_notes_tc1_1 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_tc1_1(
							id INTEGER primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT default 0,
							ponderation_devoir SMALLINT default 0 ,
							note_examen SMALLINT default 0,
							ponderation_examen SMALLINT  default 0,
							moyenne_semestrielle SMALLINT default 0
							
);		 
'''



matieres_notes_tc1_2 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_tc1_2(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT,
							ponderation_examen SMALLINT,
							moyenne_semestrielle SMALLINT 
							
);		 
'''


matieres_notes_tc2_1 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_tc2_1(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT,
							ponderation_examen SMALLINT ,
							moyenne_semestrielle SMALLINT
							
);		 
'''


			
matieres_notes_tc2_2 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_tc2_2(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT,
							ponderation_examen SMALLINT ,
							moyenne_semestrielle SMALLINT 
							
);		 
'''

matieres_notes_dic1_1 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_dic1_1(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT ,
							note_examen SMALLINT ,
							ponderation_examen SMALLINT,
							moyenne_semestrielle SMALLINT
							
);		 
'''


matieres_notes_dic1_2 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_dic1_2(
							id INTEGER primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT,
							ponderation_examen SMALLINT,
							moyenne_semestrielle SMALLINT
							
);		 
'''


matieres_notes_dic2_1 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_dic2_1(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30) ,
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT ,
							note_examen SMALLINT ,
							ponderation_examen SMALLINT ,
							moyenne_semestrielle SMALLINT 
							
);		 
'''


matieres_notes_dic2_2 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_dic2_2(
							id INTEGER primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT ,
							ponderation_examen SMALLINT,
							moyenne_semestrielle SMALLINT
							
);		 
'''


matieres_notes_dic3_1 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_dic3_1(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30) ,
							note_devoir SMALLINT,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT ,
							ponderation_examen SMALLINT ,
							moyenne_semestrielle SMALLINT
							
);		 
'''

matieres_notes_dic3_2 = ''' CREATE TABLE IF NOT EXISTS matieres_notes_dic3_2(
							id INTEGER  primary key autoincrement,
							matieres_name VARCHAR(30),
							note_devoir SMALLINT ,
							ponderation_devoir SMALLINT,
							note_examen SMALLINT,
							ponderation_examen SMALLINT,
							moyenne_semestrielle SMALLINT
							
);		 
'''


# executons pour la creation des differentes tables
#curseur.execute(requete_1)
curseur.execute(creation_user)
curseur.execute(matieres_notes_tc1_1)
curseur.execute(matieres_notes_tc1_2)
curseur.execute(matieres_notes_tc2_1)
curseur.execute(matieres_notes_tc2_2)
curseur.execute(matieres_notes_dic1_1)
curseur.execute(matieres_notes_dic1_2)
curseur.execute(matieres_notes_dic2_1)
curseur.execute(matieres_notes_dic2_2)
curseur.execute(matieres_notes_dic3_1)
curseur.execute(matieres_notes_dic3_2)
connexion.commit()
print('donne enregistre avec succes')



matieres_notes_tc1_1 = ['Analyse','Algebre','Cinematique Dinamique' ,'Informatique','Construction Mecanique','Chimie Generale','TECOM','Anglais','Atelier Mecanique','Atelier Civil']


matieres_notes_tc1_2 = ['Analyse','Electromagnetisme','Thermodynamique Generale','Informatique','Construction Mecanique',"Chimie de l'Ingenieur",'Geometre Descriptive','Anglais', 'Atelier Mecanique','Atelier Civil']

for i in matieres_notes_tc1_1:
	curseur.execute('INSERT INTO matieres_notes_tc1_1 VALUES( ?,?, ?,?,?,?,?)',(matieres_notes_tc1_1.index(i)+1,i ,0,0,0,0,0))
	connexion.commit()

for i in matieres_notes_tc1_2:
	curseur.execute('INSERT INTO matieres_notes_tc1_2 VALUES(?,?, ?,?,?,?,?)',(matieres_notes_tc1_2.index(i)+1,i ,0,0,0,0,0))
	connexion.commit()
"""
# pour ce qui eqt du mis a jour
# maintena cest de cette maniere quon insere totes les donnes on insere toutes en meeme temps 
# puis on donnera lbre a l'utilisateur de lies modifier par la requete update
valeur = 12
idd = 1
requete = 'UPDATE matieres_notes_tc1_1 SET note_devoir = ? where id = ?'
curseur.execute(requete ,(valeur , idd))


requete2 = 'SELECT * FROM matieres_notes_tc1_1'
resultats = curseur.execute(requete2)

print(resultats.fetchall())


connexion.close()
