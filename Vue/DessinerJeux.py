import tkinter as tk
from Model.Scores import Scores
from tkinter import *
from Controller.Jouer import Jouer



class DessinerJeux(object):
    '''
    classdocs
    '''


    def __init__(self, grille,vaisseaux,root):
        self.grille = grille
        self.root = root
        self.vaisseaux = vaisseaux   
        Jouer.afficherScore.ScoreJ1 = StringVar()  
        Jouer.afficherScore.ScoreJ2 = StringVar() 
        self.dessiner()    
        
        


    
    # Cette fonction dessine les différents composants graphique du jeux
    def dessiner(self):
        
        self.grille._dessiner_grille()         
        self.widget = Label(self.vaisseaux.canvas, text='Joueur 1', fg='white', bg='blue')
        self.widget.pack(side = LEFT ,anchor = tk.NW)
        
        widget1 = Label(self.vaisseaux.canvas, text='Joueur 2', fg='white', bg='blue')
        widget1.pack(side = RIGHT ,anchor = tk.NE)
        
        Scores.ScoreJ1 = StringVar()
        widget2 = tk.Label(self.vaisseaux.canvas, textvariable= Jouer.afficherScore.ScoreJ1, fg='white', bg='blue')
        widget2.pack(side = LEFT ,anchor = tk.SW)
        
        widget3 = tk.Label(self.vaisseaux.canvas, textvariable= Jouer.afficherScore.ScoreJ2, fg='white', bg='blue')
        widget3.pack(side = RIGHT ,anchor = tk.SE)
        
        B1 = Button(self.vaisseaux.canvas, text ='     Quitter     ', command = self.root.destroy)
        B1.pack(side = tk.BOTTOM,pady=80)
        
        
        
        