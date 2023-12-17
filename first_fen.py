import tkinter as tk

def first_fenetr():
	fenetre_1 = tk.Tk()
	fenetre_1.title('Conservation de Notes et Calcule de Moyenne')
	#fenetre_1.geometry("")
	#ajout de widgets
	#logo
	logo_ept = tk.PhotoImage(file = 'logo.png')
	label_logo = tk.Label(image = logo_ept)
	label_logo.image = logo_ept
	label_logo.grid(row = 1 ,column = 1 , pady= 5)
	# label frame
	# text de description
	tk.Label(text = 'Cette application presente deux(2) fonctionnalites : Conserver vos Notes & Calcul de Moyenne Semestrielle', bg = "black" , fg = 'white' , justify = tk.CENTER , font = ('Cambria' , 12)).grid(row = 2 , column = 1 , pady = 15) 
	ensemble_label = tk.LabelFrame( fenetre_1 , text = 'Identification',font= ('Verdana',14))
	ensemble_label.grid(row = 3 , column = 1 , sticky = tk.S , pady = 20) 
	#
	prenom = tk.Label(ensemble_label , text = 'Prenom(*): ' , fg = 'black', font = ('Verdana',10,'bold' ))
	prenom.grid(row = 0 , column = 0, pady =4)
	saisi_du_prenom = tk.Entry(ensemble_label , font = ('Cambria',15 ,'bold'))
	saisi_du_prenom.grid(row = 0 , column = 1, pady = 8 ,padx = 8)
	nom = tk.Label(ensemble_label , text = 'Nom(*) :', fg = 'black' , font = ('Verdana',10,'bold'))
	nom.grid(row = 1  , column = 0, pady =4)
	saisi_du_nom = tk.Entry(ensemble_label, font = ('Cambria',15 ,'bold'))
	saisi_du_nom.grid(row = 1 , column = 1,pady = 4 )
	mot_de_passe = tk.Label(ensemble_label , text = 'Mot de passe: ', fg = 'black', font = ('Verdana',10,'bold'))
	mot_de_passe.grid(row = 2 , column = 0, pady =4)
	saisi_password = tk.Entry(ensemble_label,show = '*', font = ('Cambria',15 ,'bold'))
	saisi_password.grid(row = 2 , column = 1,pady = 4)
	"""
	Niveau = tk.Label(ensemble_label , text = "Niveau d'Etude(*): " , fg = 'black', font = ('Verdana',10,'bold'))
	Niveau.grid(row = 3 , column = 0, pady =4)
	
	saisi_du_niveau = tk.Entry(ensemble_label, font = ('Cambria',15 ,'bold') , width = 4)
	saisi_du_niveau.grid(row = 3 , column = 1,pady = 4 , padx = 8)
	"""
	valider_button = tk.Button(ensemble_label , text = 'Valider', font = ('cambria', 12), command = second_fenetr )
	valider_button.grid(row = 4 ,column = 1, sticky = tk.E , padx = 4 , pady = 4 )

	fenetre_1.mainloop()

def second_fenetr():
	fenetre_1 = tk.Tk()
	fenetre_1.title('Conservation de Notes et Calcule de Moyenne')
	#fenetre_1.geometry("")
	#ajout de widgets
	#logo
	logo_ept = tk.PhotoImage(file = 'logo.png')
	label_logo = tk.Label(image = logo_ept)
	label_logo.image = logo_ept
	label_logo.grid(row = 1 ,column = 1 , pady= 5)
	# label frame
	# text de description
	tk.Label(text = 'Cette application presente deux(2) fonctionnalites : Conserver vos Notes & Calcul de Moyenne Semestrielle', bg = "black" , fg = 'white' , justify = tk.CENTER , font = ('Cambria' , 12)).grid(row = 2 , column = 1 , pady = 15) 
	ensemble_label = tk.LabelFrame( fenetre_1 , text = 'Connection',font= ('Verdana',14))
	ensemble_label.grid(row = 3 , column = 1 , sticky = tk.S , pady = 20) 
	#
	password = tk.Label(ensemble_label , text = 'Mot de passe: ' , fg = 'black', font = ('Verdana',10,'bold' ))
	password.grid(row = 0 , column = 0, pady =4)
	saisi_password = tk.Entry(ensemble_label , font = ('Cambria',15 ,'bold'),width = 12 , show = '*')
	saisi_password.grid(row = 0 , column = 1, pady = 8 ,padx = 8)
	niveau = tk.Label(ensemble_label , text = 'Niveau:', fg = 'black' , font = ('Verdana',10,'bold'))
	niveau.grid(row = 1  , column = 0, pady =4)
	saisi_du_niveau = tk.Entry(ensemble_label, font = ('Cambria',15 ,'bold'),width = 4)
	saisi_du_niveau.insert(0,'dic2')
	saisi_du_niveau.grid(row = 1 , column = 1,pady = 8 ,padx = 8, sticky = tk.W )
	semestre_correspond = tk.Label(ensemble_label , text = 'Semestre ', fg = 'black', font = ('Verdana',10,'bold'))
	semestre_correspond.grid(row = 2 , column = 0, pady =4)
	saisi_semestre = tk.Entry(ensemble_label, font = ('Cambria',15 ,'bold') , width = 4)
	saisi_semestre.insert(0 , "1")
	saisi_semestre.grid(row = 2 , column = 1,pady = 8 ,padx = 8 , sticky = tk.W)

	fenetre_1.mainloop()
#def vue_darbre(self):
    #self.defiler = Scrollbar(orient = 'vertical')
"""
def third_fenetr():
	self.arbre = ttk.Treeview(height = 10 , columns = ('Note_devoir','Ponderation','Note_examen','Ponderation','Moyenne_Matiere'))
    self.arbre.grid(row = 5 , column = 0 , columnspan = 8, sticky = S , pady = 4)
    self.arbre.heading('#0', text = 'Matieres' , anchor = W)
    #self.arbre.heading("email", text = 'Note Devoir' , anchor = W)
    self.arbre.heading("#1", text = 'Note Devoir' , anchor = W)
    self.arbre.heading("#2", text = 'Ponderation Dev' , anchor = W)
    self.arbre.heading("#3", text = 'Note Examen' , anchor = W)
    self.arbre.heading("#4", text = 'Ponderation Examen' , anchor = W)
    self.arbre.heading("#5", text = 'Moyenne_Obtenue' , anchor = E)

def first_champs(self):
    frame_lab = LabelFrame(text = 'Remplir ou Modifier' ,font = 18)
    frame_lab.grid(row = 0 , column = 5 , sticky = E )
    # label et entry de la matiere
    self.matiere_select = Label(frame_lab ,  text = 'Matieres'  , fg ='white' , bg = 'green')
    self.matiere_select.grid(row = 0 , column = 0 , pady = 3)
    self.matiere_entry = Entry(frame_lab ,textvariable = StringVar(),state = 'readonly')
    self.matiere_entry.grid(row = 0 , column = 1)

    # label et entry de la note du devoir
    self.Note_dev = Label(frame_lab ,text = 'Note de Devoir :' , fg = 'white' , bg = 'green')
    self.Note_dev.grid(row = 1 , column = 0 , pady = 4)
    self.Note_dev_entry = Entry(frame_lab)
    self.Note_dev_entry.grid(row = 1 , column = 1 , padx = 4)

    # label et entry de la ponderation
    self.pond_dev = Label( frame_lab ,text = 'Ponderation du Devoir :' , fg = 'white' , bg = 'green')
    self.pond_dev.grid(row = 2 , column = 0)
    self.pond_dev_entry = Entry(frame_lab)
    self.pond_dev_entry.grid(row = 2 , column = 1 , padx = 4)

        # label et entry de la note exam
    self.Note_exam = Label( frame_lab , text = 'Note Examen'  , fg ='white' , bg = 'green')
    self.Note_exam.grid(row = 3 , column = 0 , pady = 3)
    self.Note_exam_entry = Entry(frame_lab )
    self.Note_exam_entry.grid(row = 3 , column = 1)

        ## label et entry de la ponderation de l'exam
    self.Ponderation_exam = Label(frame_lab , text = 'Ponderation Examen'  , fg ='white' , bg = 'green')
    self.Ponderation_exam.grid(row = 4 , column = 0 , pady = 3)
    self.Ponderation_exam_entry = Entry(frame_lab)
    self.Ponderation_exam_entry.grid(row = 4 , column = 1)
        
        # label et entry de la moyenne
    self.moyenne = Label(frame_lab ,text = 'Moyenne :' , fg = 'white' , bg = 'green')
    self.moyenne.grid(row = 5 , column = 0 , pady = 4)
    self.moyenne_entry = Entry(frame_lab , textvariable = StringVar(),state = 'readonly')
    self.moyenne_entry.grid(row = 5 , column = 1 , padx = 4)
    #Valider_button = Button(grand_lab , text = 'Ajouter' , font = ('Verdanana' ,12,'italic') , command = self.save_record)
    #Valider_button.grid(row = 3 , column = 2 , sticky = E ,padx = 5)
def requete_sql(self ,requete , parametre = ()):
    connexion = sqlite3.connect('database.db')
    curseur = connexion.cursor()
    resultat = curseur.execute(requete , parametre)
    connexion.commit()
    return resultat

def insertion_des_materes_test(self):
	elements_tree = self.arbre.get_children()
    for element in elements_tree:
    	self.arbre.delete(element)
               
	requete = 'SELECT matieres_name,note_devoir,ponderation_devoir,note_examen,ponderation_examen,moyenne_semestrielle FROM matieres_notes_tc1_1 ORDER by id desc'

	resultat_requete = self.requete_sql(requete)
        #print(resultat_requete)

	for infos in resultat_requete:
   		if infos[5]== 0:
        	self.arbre.insert('',0, text = infos[0] , values = (str(infos[1]) + ' /20 ',str(infos[2]) +' % ',str(infos[3]) + ' /20 ',str(infos[4]) +' % ',''))
        else:
        	self.arbre.insert('',0, text = infos[0] , values = (str(infos[1]) + ' /20 ',str(infos[2]) +' % ',str(infos[3]) + ' /20 ',str(infos[4]) +' % ',infos[5]))

             






#
second_fenetr()
"""
first_fenetr()
