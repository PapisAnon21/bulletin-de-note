from tkinter import *

class Application(Tk):
    def __init__(self):
        self.root=Tk()
        self.root.title("Mr Corazon")
        self.root.resizable(width=False,height=False)
        self.creer_widgets()

    def logo(self):
        texte1=Label(self.root, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=107)
        texte1.grid(row=0, column=0, columnspan=5)
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
        texte1=Label(self.fenetre1, text="", bg="BLACK", fg="WHITE", justify=CENTER, width=107)
        texte1.grid(row=0, column=0, columnspan=5)
        logo = PhotoImage(file = 'logo.png')
        label_logo = Label(image = logo)
        label_logo.image = logo
        label_logo.grid(row = 1 , column=0, columnspan=5, padx = 165 , pady = 10 , sticky = W)
        Label(self.fenetre1, text="Bienvenue au Calculateur de moyenne version polytechs-TC1-2021/2022", font=('cambria' ,13, 'bold'), bg="BLACK", fg="WHITE", justify=CENTER, width=75).grid(row=2, column=0, columnspan=5)
        Label(self.fenetre1, text="Veuillez svp entrer les notes dans chacune de vos matiere dans les cases correspondant", justify=CENTER, fg="GREEN", font=('cambria' ,12, 'bold')).grid(row=3, column=0, columnspan=5)
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
