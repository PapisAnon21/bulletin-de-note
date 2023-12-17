from tkinter import *
from tkinter import ttk
import sqlite3

class Application(Tk):
    def __init__(self):
        self.root=Tk()
        self.root.title("Mr Corazon")
        self.root.resizable(width=False,height=False)
        self.creer_widgets()

    def logo(self):
        #texte1=Label(self.root, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=107)
        #texte1.grid(row=0, column=1, columnspan=5)
        logo = PhotoImage(file = 'logo.png')
        label_logo = Label(image = logo)
        label_logo.image = logo
        label_logo.grid(row = 1 , column=0, columnspan=5, padx = 165 , pady = 10 , sticky = W)

    def creer_widgets(self):
        self.logo()
        Label(self.root, text="Bienvenue au Calculateur de moyenne version polytechs-TC1-2021/2022", font=('cambria' ,13, 'bold'), bg="BLACK", fg="WHITE", justify=CENTER, width=75).grid(row=2, column=0, columnspan=5)
        Label(self.root, text="Veuillez svp choisir l'année et le semestre  correspondant", justify=CENTER, fg="GREEN", font=('cambria' ,12, 'bold')).grid(row=3, column=0, columnspan=5)
        Button(self.root, text="TC1-->Premier semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.PremierSemestreTC1).grid(row=4, sticky=W, padx=3, pady=3)
        Button(self.root, text="TC1-->Second semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.SecondSemestreTC1).grid(row=4,column=2, sticky=W, padx=0, pady=3)
        Button(self.root, text="TC2-->Premier semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=5, sticky=W, padx=3, pady=3)
        Button(self.root, text="TC2-->Second semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=5,column=2, sticky=W, padx=0, pady=3)
        Button(self.root, text="DIC1_GIT-->Premier semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=6, sticky=W, padx=3, pady=3)
        Button(self.root, text="DIC1_GIT-->Second semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=6,column=2, sticky=W, padx=0, pady=3)
        Button(self.root, text="DIC1_GEM-->Premier semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=7, sticky=W, padx=3, pady=3)
        Button(self.root, text="DIC1_GEM-->Second semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=7,column=2, sticky=W, padx=0, pady=3)
        Button(self.root, text="DIC1_GC-->Premier semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=8, sticky=W, padx=3, pady=3)
        Button(self.root, text="DIC1_GC-->Second semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=8,column=2, sticky=W, padx=0, pady=3)
        Button(self.root, text="DIC1_Aéro-->Premier semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=9, sticky=W, padx=3, pady=3)
        Button(self.root, text="DIC1_Aéro-->Second semestre", font=('cambria' ,13, 'bold'), fg="BLUE", width=36, command=self.indisponible).grid(row=9,column=2, sticky=W, padx=0, pady=3)
        texte1=Label(self.root, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=107)
        texte1.grid(row=10, column=0, columnspan=5)

    def PremierSemestreTC1(self):
        self.root.destroy()
        self.fenetre1=Tk()
        self.fenetre1.title("TC1 1er Semestre")
        self.fenetre1.resizable(width=False,height=False)

        #texte1=Label(self.fenetre1, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=107)
        #texte1.grid(row=0, column=0, columnspan=5)
        logo = PhotoImage(file = 'logo.png')
        label_logo = Label(image = logo)
        label_logo.image = logo
        label_logo.grid(row = 0 , column=4,  padx = 0 , pady = 10 , sticky = W)
        Label(self.fenetre1, text="Bienvenue au Calculateur de moyenne version polytechs-TC1-2021/2022", font=('cambria' ,13, 'bold'),  fg="black", justify=CENTER, width=75).grid(row=3, column=0, columnspan=5)
        Label(self.fenetre1, text="Veuillez svp entrer les notes dans chacune de vos matiere dans les cases correspondant", justify=CENTER, fg="GREEN", font=('cambria' ,12, 'bold')).grid(row=4, column=0, columnspan=5)
        self.first_champs()
        
        # les configurations du treeview
        style_ttk = ttk.Style()
        style_ttk.configure("Treeview", font = ('Cambria', 11 , 'bold'))
        style_ttk.configure("Treeview.Heading", font = ('cambria', 12,'bold'))
        #style_ttk.configure("Treeview.#0", font = ('cambria', ,'bold'))

        self.vue_darbre()
        self.insertion_des_materes_test()
        self.element_at_row()
        #self.element_at_row()
        '''
        Label(self.fenetre1, text="==>Note 1er smestre de la première années(TC1):<==", justify=CENTER, font=('cambria' ,11, 'bold')).grid(row=4, column=0, columnspan=5)
        Label(self.fenetre1, text="Analyse=====>", width=15, justify=LEFT, fg="BLUE", font=('cambria' ,12, 'bold')).grid(row=5, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=5, column=1)
        self.nd_analyse=Entry(self.fenetre1, width=15)
        self.nd_analyse.grid(row=5, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=5, column=3)
        self.ne_analyse=Entry(self.fenetre1, width=15)
        self.ne_analyse.grid(row=5, column=4)
        Label(self.fenetre1, text="Alg_Lin=====>", width=15, justify=LEFT, fg="BLUE", font=('cambria' ,12, 'bold')).grid(row=6, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=6, column=1)
        self.nd_algebre=Entry(self.fenetre1, width=15)
        self.nd_algebre.grid(row=6, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=6, column=3)
        self.ne_algebre=Entry(self.fenetre1, width=15)
        self.ne_algebre.grid(row=6, column=4)
        Label(self.fenetre1, text="Physique=====>", width=15, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=7, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=7, column=1)
        self.nd_physique=Entry(self.fenetre1, width=15)
        self.nd_physique.grid(row=7, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=7, column=3)
        self.ne_physique=Entry(self.fenetre1, width=15)
        self.ne_physique.grid(row=7, column=4)
        Label(self.fenetre1, text="Informatique=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=8, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=8, column=1)
        self.nd_informatique=Entry(self.fenetre1, width=15)
        self.nd_informatique.grid(row=8, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=8, column=3)
        self.ne_informatique=Entry(self.fenetre1, width=15)
        self.ne_informatique.grid(row=8, column=4)
        Label(self.fenetre1, text="Cons_Méca=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=9, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=9, column=1)
        self.nd_mecanique=Entry(self.fenetre1, width=15)
        self.nd_mecanique.grid(row=9, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=9, column=3)
        self.ne_mecanique=Entry(self.fenetre1, width=15)
        self.ne_mecanique.grid(row=9, column=4)
        Label(self.fenetre1, text="Chimie=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=10, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=10, column=1)
        self.nd_chimie=Entry(self.fenetre1, width=15)
        self.nd_chimie.grid(row=10, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=10, column=3)
        self.ne_chimie=Entry(self.fenetre1, width=15)
        self.ne_chimie.grid(row=10, column=4)
        Label(self.fenetre1, text="Tech_d'Exp=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=11, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=11, column=1)
        self.nd_communication=Entry(self.fenetre1, width=15)
        self.nd_communication.grid(row=11, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=11, column=3)
        self.ne_communication=Entry(self.fenetre1, width=15)
        self.ne_communication.grid(row=11, column=4)
        Label(self.fenetre1, text="Anglais=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=12, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=12, column=1)
        self.nd_anglais=Entry(self.fenetre1, width=15)
        self.nd_anglais.grid(row=12, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=12, column=3)
        self.ne_anglais=Entry(self.fenetre1, width=15)
        self.ne_anglais.grid(row=12, column=4)
        Label(self.fenetre1, text="At.Civil=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=13, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=13, column=1)
        self.nd_atelier_c=Entry(self.fenetre1, width=15)
        self.nd_atelier_c.grid(row=13, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=13, column=3)
        self.ne_atelier_c=Entry(self.fenetre1, width=15)
        self.ne_atelier_c.grid(row=13, column=4)
        Label(self.fenetre1, text="At.Mécanique=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=14, column=0)
        Label(self.fenetre1, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=14, column=1)
        self.nd_atelier_m=Entry(self.fenetre1, width=15)
        self.nd_atelier_m.grid(row=14, column=2)
        Label(self.fenetre1, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=14, column=3)
        self.ne_atelier_m=Entry(self.fenetre1, width=15)
        self.ne_atelier_m.grid(row=14, column=4)
        Button(self.fenetre1, text="Valider", width=15, justify=CENTER, font=('cambria' ,11, 'bold'), command=self.recup_notes_PSTC1).grid(row=15, columnspan=5, pady=10)
        Label(self.fenetre1, text="------------------------------------------------------------------------------------------------------------------------------------------------------", bg="BLACK", fg="WHITE", justify=CENTER, width=107).grid(row=17, column=0, columnspan=5)
        '''
    def vue_darbre(self):
        #self.defiler = Scrollbar(orient = 'vertical')
        self.arbre = ttk.Treeview(height = 10 , columns = ('Note_devoir','Ponderation','Note_examen','Ponderation','Moyenne_Matiere'))
        self.arbre.grid(row = 5 , column = 0 , columnspan = 8, sticky = S , pady = 4)
        self.arbre.heading('#0', text = 'Matieres' , anchor = W)
        #self.arbre.heading("email", text = 'Note Devoir' , anchor = W)
        self.arbre.heading("#1", text = 'Note Devoir' , anchor = W)
        self.arbre.heading("#2", text = 'Ponderation Devoir' , anchor = W)
        self.arbre.heading("#3", text = 'Note Examen' , anchor = W)
        self.arbre.heading("#4", text = 'Ponderation Examen' , anchor = W)
        self.arbre.heading("#5", text = 'Moyenne Obtenue' , anchor = W)

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
        
        # bouton de validation
        Valider_button = Button(frame_lab , text = 'Modifier' , font = ('Verdanana' ,12,'bold') , command = self.function_update)
        Valider_button.grid(row = 6 , column = 1, padx = 10, pady = 10 )
        #
        #function_update

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
            #str(infos[1]) = (str(infos[1]).replace('0','--')
            
            self.arbre.insert('',0, text = infos[0] , values = (str(infos[1]).replace('0','---').replace('10','10').replace('20','20') + ' /20 ',str(infos[2]) +' % ',str(infos[3]).replace('0','---').replace('10','10').replace('20','20') + ' /20 ',str(infos[4]) +' % ',str(infos[5]).replace('0','---')))
            
                
# voici comment prendre un element d'un treeview selectionne
#name = self.tree.item(self.tree.selection())['text']
#old_number = self.tree.item(self.tree.selection())['values'][1]        
        # label frame
#self.defiler = Scrollbar(self.root)
#self.defiler.config(command = self.arbre.yview)
#self.defiler.grid() 

    def element_at_row(self):
        #dans un premier temps on verifie si qlq chose a ete selectionne
        c = self.arbre.item(self.arbre.selection())['text']
        #on recupere l'index de l'elemen selectioone

        #if len(c) != 0:
        
        try:
                #ide = self.arbre.identify_row(self.arbre.item(self.arbre.selection()))
                #print(ide)
            self.index = self.arbre.index(self.arbre.selection()) + 1
                #print(self.index)
                #self.index = self.arbre.index(self.arbre.item(self.arbre.selection())['values'][0]) + 1
                #print(self.index)
            self.matiere_entry.config(textvariable = StringVar(value = c))
                #ainsi les autres sont dispo on les ajoue
            note_de_devoir = self.arbre.item(self.arbre.selection())['values'][0]
                #self.Note_dev_entry.insert(0 , note_de_devoir )
                #value_of_mark = note_de_devoir.split("/")
            ponderation_de_devoir = self.arbre.item(self.arbre.selection())['values'][1]
            note_examenn = self.arbre.item(self.arbre.selection())['values'][2]

            ponderation_de_examen = self.arbre.item(self.arbre.selection())['values'][3]

            moyenne_get = self.arbre.item(self.arbre.selection())['values'][4]

                #self.moyenne_entry

                #self.Note_dev_entry.delete(0 ,END)
                #if len(self.Note_dev_entry.get())  == 0:
                #self.Note_dev_entry.delete(0,END)
            
                #if self.Note_dev_entry.get() != note_de_devoir:
            if len(self.Note_dev_entry.get()) == 0:
            	self.Note_dev_entry.insert(0,note_de_devoir)        
                #if self.Note_dev_entry.get() != note_de_devoir:  # vraimenet nous demandons de l'aide au Seigneur
            #elif len(self.Note_dev_entry.get())  == 0:    
                #self.Note_dev_entry.insert(0,note_de_devoir)
                #if self.Note_dev_entry.get() != note_de_devoir:
                #self.Note_dev_entry.insert(0,note_de_devoir)

            if len(self.pond_dev_entry.get()) == 0:
                #self.pond_dev_entry.delete(0,END)
            	self.pond_dev_entry.insert(0,ponderation_de_devoir)
            #self.pond_dev_entry.config(textvariable = StringVar(value = ponderation_de_devoir))
            #je vois qu'on ne doit pas utliser delete
            #self.pond_dev_entry.delete(4,END)

            #if len(self.Note_exam_entry.get()) == 0:
            #self.Note_exam_entry.delete(0,END)
            self.Note_exam_entry.insert(0,note_examenn)
                #if len(self.Ponderation_exam_entry.get()) == 0:
                #self.Ponderation_exam_entry.delete(0,END)
            self.Ponderation_exam_entry.insert(0,ponderation_de_examen)
                #if len(self.moyenne_entry.get()) == 0:
            self.moyenne_entry.config(textvariable = StringVar(value = moyenne_get))
                #self.fenetre1.after(100, self.element_at_row)
        except:
            print("l'except est execute")
                #return
        self.fenetre1.after(100, self.element_at_row)            



    def function_update(self):
        try:
            self.donne_recupere_sur_notedevoir = self.Note_dev_entry.get()
            if "/" in self.donne_recupere_sur_notedevoir:
                self.donne_recupere_sur_notedevoir = int(self.donne_recupere_sur_notedevoir.split("/")[0])
            self.donne_recupere_sur_ponderationdevor = self.pond_dev_entry.get()[:2]
        
            self.donne_recupere_sur_noteexamen = self.Note_exam_entry.get()
            if "/" in self.donne_recupere_sur_noteexamen:
                self.donne_recupere_sur_noteexamen = int(self.donne_recupere_sur_noteexamen.split("/")[0])

            self.donne_recupere_sur_ponderationexamen = self.Ponderation_exam_entry.get()[:2]
            #on lance la requete update
        except Exception as e:
            print(e)
            print("erreur lors des saisies des donnees")
        

        requete = 'UPDATE matieres_notes_tc1_1 SET note_devoir =? where id = ? ' 
        parametre = (self.donne_recupere_sur_notedevoir , self.index )
        self.requete_sql(requete,parametre)
        requete =   'UPDATE matieres_notes_tc1_1 SET ponderation_devoir =? where id = ?' 
        parametre = (self.donne_recupere_sur_ponderationdevor, self.index)
        self.requete_sql(requete , parametre)
        requete =   'UPDATE matieres_notes_tc1_1 SET note_examen =? where id = ?' 
        parametre = (self.donne_recupere_sur_noteexamen, self.index)
        self.requete_sql(requete , parametre)
        requete =   'UPDATE matieres_notes_tc1_1 SET ponderation_examen =? where id = ?' 
        parametre = (self.donne_recupere_sur_ponderationexamen, self.index)
        self.requete_sql(requete , parametre)
        


        #requete2 = 'UPDATE matieres_notes_tc1_1  SET ponderation_devoir = '+ str(self.donne_recupere_sur_ponderationdevor) +  'where id = ' + str(self.index)
        #parametre2 = (self.donne_recupere_sur_ponderationdevor , self.index)
        #self.requete_sql()
        
        
        #requete3 = 'UPDATE matieres_notes_tc1_1 SET note_examen = '+ str(self.donne_recupere_sur_noteexamen) + 'where id = ' + str(self.index)
        #parametre3 = (self.donne_recupere_sur_noteexamen , self.index)
        
        
        #requete4 = 'UPDATE matieres_notes_tc1_1 SET ponderation_examen = ' + str(self.donne_recupere_sur_ponderationexamen) + 'where id = ' + str(self.index)
        #parametre4 = (self.donne_recupere_sur_ponderationexamen , self.index)
        
        #self.requete_sql(requete2)
        #self.requete_sql(requete3)
        #self.requete_sql(requete4)

        self.insertion_des_materes_test()
        self.element_at_row()
#'UPDATE contacts_list SET number=? WHERE number =? AND name =?'
#note_devoir,ponderation_devoir,note_examen,ponderation_examen
#self.fenetre1.after(1000 , self.element_at_row)

#self.Note_exam_entry.insert(0,c)
        
#self.Note_dev_entry.insert(2)

        #self.pond_dev_entry
        #self.Note_exam_entry
        #self.Ponderation_exam_entry
        #self.moyenne_entry

    def recup_notes_PSTC1(self):
        try:
            #Définiton des noms de variables
            self.ndevoir_analyse=self.nd_analyse.get()
            self.nexamen_analyse=self.ne_analyse.get()
            self.ndevoir_algebre=self.nd_algebre.get()
            self.nexamen_algebre=self.ne_algebre.get()
            self.ndevoir_physique=self.nd_physique.get()
            self.nexamen_physique=self.ne_physique.get()
            self.ndevoir_inf=self.nd_informatique.get()
            self.nexamen_inf=self.ne_informatique.get()
            self.ndevoir_cons=self.nd_mecanique.get()
            self.nexamen_cons=self.ne_mecanique.get()
            self.ndevoir_chimie=self.nd_chimie.get()
            self.nexamen_chimie=self.ne_chimie.get()
            self.ndevoir_communication=self.nd_communication.get()
            self.nexamen_communication=self.ne_communication.get()
            self.ndevoir_anglais=self.nd_anglais.get()
            self.nexamen_anglais=self.ne_anglais.get()
            self.ndevoir_civil=self.nd_atelier_c.get()
            self.nexamen_civil=self.ne_atelier_c.get()
            self.ndevoir_mecanique=self.nd_atelier_m.get()
            self.nexamen_mecanique=self.ne_atelier_m.get()
            #Calcules des moyennes
            self.moy_analyse=(float(self.ndevoir_analyse)*0.5)+(float(self.nexamen_analyse)*0.5)
            self.moy_algebre=(float(self.ndevoir_algebre)*0.5)+(float(self.nexamen_algebre)*0.5)
            self.moy_physique=(float(self.ndevoir_physique)*0.4)+(float(self.nexamen_physique)*0.6)
            self.moy_inf=(float(self.ndevoir_inf)*0.4)+(float(self.nexamen_inf)*0.6)
            self.moy_cons=(float(self.ndevoir_cons)*0.5)+(float(self.nexamen_cons)*0.5)
            self.moy_chimie=(float(self.ndevoir_chimie)*0.4)+(float(self.nexamen_chimie)*0.6)
            self.moy_com=(float(self.ndevoir_communication)*0.4)+(float(self.nexamen_communication)*0.6)
            self.moy_ang=(float(self.ndevoir_anglais)*0.5)+(float(self.nexamen_anglais)*0.5)
            self.moy_civil=(float(self.ndevoir_civil)*0.5)+(float(self.nexamen_civil)*0.5)
            self.moy_meca=(float(self.ndevoir_mecanique)*0.4)+(float(self.nexamen_mecanique)*0.6)
            self.moyenne=(float(self.moy_analyse)+float(self.moy_algebre)+float(self.moy_physique)+float(self.moy_inf)+float(self.moy_cons)+float(self.moy_chimie)+float(self.moy_com)+float(self.moy_ang)+float(self.moy_civil)+float(self.moy_meca))/10
        except:
            Label(self.fenetre1, text="Veuillez Svp remplire toutes les cases avec des valeurs numérique avant de valider", font=('cambria' ,13), fg="RED", justify=CENTER, width=75).grid(row=16, column=0, columnspan=5)
            
        else:
            Label(self.fenetre1, text="Moyenne:{}".format(self.moyenne), font=('cambria' ,13, 'bold'), bg="BLACK", fg="WHITE", justify=CENTER, width=75).grid(row=16, column=0, columnspan=5)

    def SecondSemestreTC1(self):
        self.root.destroy()
        self.fenetre2=Tk()
        self.fenetre2.title("TC1 2nd Semestre")
        self.fenetre2.resizable(width=False,height=False)
        texte1=Label(self.fenetre2, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=107)
        texte1.grid(row=0, column=0, columnspan=5)
        logo = PhotoImage(file = 'logo.png')
        label_logo = Label(image = logo)
        label_logo.image = logo
        label_logo.grid(row = 1 , column=0, columnspan=5, padx = 165 , pady = 10 , sticky = W)
        Label(self.fenetre2, text="Bienvenue au Calculateur de moyenne version polytechs-TC1-2021/2022", font=('cambria' ,13, 'bold'), bg="BLACK", fg="WHITE", justify=CENTER, width=75).grid(row=2, column=0, columnspan=5)
        Label(self.fenetre2, text="Veuillez svp entrer les notes dans chacune de vos matiere dans les cases correspondant", justify=CENTER, fg="GREEN", font=('cambria' ,12, 'bold')).grid(row=3, column=0, columnspan=5)
        Label(self.fenetre2, text="==>Note 2em smestre de la première années(TC1):<==", justify=CENTER, font=('cambria' ,11, 'bold')).grid(row=4, column=0, columnspan=5)
        Label(self.fenetre2, text="Analyse=====>", width=15, justify=LEFT, fg="BLUE", font=('cambria' ,12, 'bold')).grid(row=5, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=5, column=1)
        self.nd_analyse=Entry(self.fenetre2, width=15)
        self.nd_analyse.grid(row=5, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=5, column=3)
        self.ne_analyse=Entry(self.fenetre2, width=15)
        self.ne_analyse.grid(row=5, column=4)
        Label(self.fenetre2, text="Thermodynamique=====>", width=25, justify=LEFT, fg="BLUE", font=('cambria' ,12, 'bold')).grid(row=6, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=6, column=1)
        self.nd_thermo=Entry(self.fenetre2, width=15)
        self.nd_thermo.grid(row=6, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=6, column=3)
        self.ne_thermo=Entry(self.fenetre2, width=15)
        self.ne_thermo.grid(row=6, column=4)
        Label(self.fenetre2, text="Physique=====>", width=15, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=7, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=7, column=1)
        self.nd_physique=Entry(self.fenetre2, width=15)
        self.nd_physique.grid(row=7, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=7, column=3)
        self.ne_physique=Entry(self.fenetre2, width=15)
        self.ne_physique.grid(row=7, column=4)
        Label(self.fenetre2, text="Informatique=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=8, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=8, column=1)
        self.nd_informatique=Entry(self.fenetre2, width=15)
        self.nd_informatique.grid(row=8, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=8, column=3)
        self.ne_informatique=Entry(self.fenetre2, width=15)
        self.ne_informatique.grid(row=8, column=4)
        Label(self.fenetre2, text="Cons_Méca=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=9, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=9, column=1)
        self.nd_mecanique=Entry(self.fenetre2, width=15)
        self.nd_mecanique.grid(row=9, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=9, column=3)
        self.ne_mecanique=Entry(self.fenetre2, width=15)
        self.ne_mecanique.grid(row=9, column=4)
        Label(self.fenetre2, text="Chimie=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=10, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=10, column=1)
        self.nd_chimie=Entry(self.fenetre2, width=15)
        self.nd_chimie.grid(row=10, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=10, column=3)
        self.ne_chimie=Entry(self.fenetre2, width=15)
        self.ne_chimie.grid(row=10, column=4)
        Label(self.fenetre2, text="Géo_descriptive=====>", width=25, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=11, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=11, column=1)
        self.nd_gd=Entry(self.fenetre2, width=15)
        self.nd_gd.grid(row=11, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=11, column=3)
        self.ne_gd=Entry(self.fenetre2, width=15)
        self.ne_gd.grid(row=11, column=4)
        Label(self.fenetre2, text="Anglais=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=12, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=12, column=1)
        self.nd_anglais=Entry(self.fenetre2, width=15)
        self.nd_anglais.grid(row=12, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=12, column=3)
        self.ne_anglais=Entry(self.fenetre2, width=15)
        self.ne_anglais.grid(row=12, column=4)
        Label(self.fenetre2, text="At.Civil=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=13, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=13, column=1)
        self.nd_atelier_c=Entry(self.fenetre2, width=15)
        self.nd_atelier_c.grid(row=13, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=13, column=3)
        self.ne_atelier_c=Entry(self.fenetre2, width=15)
        self.ne_atelier_c.grid(row=13, column=4)
        Label(self.fenetre2, text="At.Mécanique=====>", width=17, justify=LEFT, fg="BLUE", font=('cambria' ,11, 'bold')).grid(row=14, column=0)
        Label(self.fenetre2, text="Devoir----->", font=('cambria' ,11, 'bold')).grid(row=14, column=1)
        self.nd_atelier_m=Entry(self.fenetre2, width=15)
        self.nd_atelier_m.grid(row=14, column=2)
        Label(self.fenetre2, text="Examen----->", font=('cambria' ,11, 'bold')).grid(row=14, column=3)
        self.ne_atelier_m=Entry(self.fenetre2, width=15)
        self.ne_atelier_m.grid(row=14, column=4)
        Button(self.fenetre2, text="Valider", width=15, justify=CENTER, command=self.recup_notes_SSTC1, font=('cambria' ,11, 'bold')).grid(row=15, columnspan=5, pady=10)
        Label(self.fenetre2, text="------------------------------------------------------------------------------------------------------------------------------------------------------", bg="BLACK", fg="WHITE", justify=CENTER, width=107).grid(row=17, column=0, columnspan=5)


    def recup_notes_SSTC1(self):
        try:
            #Définiton des noms de variables
            self.ndevoir_analyse=self.nd_analyse.get()
            self.nexamen_analyse=self.ne_analyse.get()
            self.ndevoir_thermo=self.nd_thermo.get()
            self.nexamen_thermo=self.ne_thermo.get()
            self.ndevoir_physique=self.nd_physique.get()
            self.nexamen_physique=self.ne_physique.get()
            self.ndevoir_inf=self.nd_informatique.get()
            self.nexamen_inf=self.ne_informatique.get()
            self.ndevoir_cons=self.nd_mecanique.get()
            self.nexamen_cons=self.ne_mecanique.get()
            self.ndevoir_chimie=self.nd_chimie.get()
            self.nexamen_chimie=self.ne_chimie.get()
            self.ndevoir_gd=self.nd_gd.get()
            self.nexamen_gd=self.ne_gd.get()
            self.ndevoir_anglais=self.nd_anglais.get()
            self.nexamen_anglais=self.ne_anglais.get()
            self.ndevoir_civil=self.nd_atelier_c.get()
            self.nexamen_civil=self.ne_atelier_c.get()
            self.ndevoir_mecanique=self.nd_atelier_m.get()
            self.nexamen_mecanique=self.ne_atelier_m.get()
            #Calcules des moyennes
            self.moy_analyse=(float(self.ndevoir_analyse)*0.5)+(float(self.nexamen_analyse)*0.5)
            self.moy_thermo=(float(self.ndevoir_thermo)*0.5)+(float(self.nexamen_thermo)*0.5)
            self.moy_physique=(float(self.ndevoir_physique)*0.4)+(float(self.nexamen_physique)*0.6)
            self.moy_inf=(float(self.ndevoir_inf)*0.4)+(float(self.nexamen_inf)*0.6)
            self.moy_cons=(float(self.ndevoir_cons)*0.5)+(float(self.nexamen_cons)*0.5)
            self.moy_chimie=(float(self.ndevoir_chimie)*0.4)+(float(self.nexamen_chimie)*0.6)
            self.moy_gd=(float(self.ndevoir_gd)*0.5)+(float(self.nexamen_gd)*0.5)
            self.moy_ang=(float(self.ndevoir_anglais)*0.5)+(float(self.nexamen_anglais)*0.5)
            self.moy_civil=(float(self.ndevoir_civil)*0.5)+(float(self.nexamen_civil)*0.5)
            self.moy_meca=(float(self.ndevoir_mecanique)*0.4)+(float(self.nexamen_mecanique)*0.6)
            self.moyenne=(float(self.moy_analyse)+float(self.moy_thermo)+float(self.moy_physique)+float(self.moy_inf)+float(self.moy_cons)+float(self.moy_chimie)+float(self.moy_gd)+float(self.moy_ang)+float(self.moy_civil)+float(self.moy_meca))/10

        except:

            Label(self.fenetre2, text="Veuillez Svp remplire toutes les cases avec des valeurs numérique avant de valider", font=('cambria' ,13), fg="RED", justify=CENTER, width=75).grid(row=16, column=0, columnspan=5)

        else:

            Label(self.fenetre2, text="Moyenne:{}".format(self.moyenne), font=('cambria' ,13, 'bold'), bg="BLACK", fg="WHITE", justify=CENTER, width=75).grid(row=16, column=0, columnspan=5)

    def indisponible(self):
        self.indispo=Tk()
        self.indispo.resizable(width=False, height=False)
        self.indispo.title("Indisponible")
        Label(self.indispo, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=80).grid(row=0)
        Label(self.indispo, text="Desolé, Cette partie du programme n'est pas encore disponible", fg="RED", font=('cambria' ,13, 'bold')).grid(row=1, padx=10, pady=10)
        Label(self.indispo, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=80).grid(row=3)
        Button(self.indispo, text="Quitter", command=self.quit, font=('cambria' ,11, 'bold')).grid(row=2, pady=2)

    def quit(self):
        self.indispo.destroy()

     
f=Application()
f.root.mainloop()
