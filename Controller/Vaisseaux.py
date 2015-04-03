from tkinter import DISABLED
import tkinter as tk
from tkinter import *
from Controller.Jouer import Jouer
from tkinter.messagebox import showinfo
from tkinter import Button
from tkinter.constants import BOTTOM, LEFT





class Vaisseaux(object):
    '''
    classdocs
    '''


    def __init__(self,grille,canvas,logo):
        self.grille = grille
        self.canvas = canvas
        self.logo= logo
        self.B = Button(self.canvas, text ="Commencer",command = self.placer_vaisseaux1)
        self.B.pack(side = tk.BOTTOM,pady=80)
  
  
    def placer_vaisseaux1(self):
        showinfo("Joueur 1", "Choisissez la position de vos 5 vaisseaux")
        self.grille.canvas.bind("<Button-1>", self.jouer1)
        self.B.config(state=DISABLED)

    def jouer1(self,event):
        if (self.grille.nbVaisseauxPlaces(self.grille.pos) < 5):
            self.grille.get_pos(event.x//40,event.y//40).setsituation(2)
            self.grille._dessiner_grille()
        if(self.grille.nbVaisseauxPlaces(self.grille.pos) == 5):
            showinfo("Joueur 2", "Choisissez la position de vos 5 vaisseaux")
            self.placer_vaisseaux2()
       
        
    def placer_vaisseaux2(self):
        self.grille.canvas1.bind("<Button-1>", self.jouer2)

    def jouer2(self,event):
        if (self.grille.nbVaisseauxPlaces(self.grille.pos2) < 5):
            self.grille.get_pos2(event.x//40,event.y//40).setsituation(2)
            self.grille._dessiner_grille()
        if(self.grille.nbVaisseauxPlaces(self.grille.pos2) == 5):
            self.grille.commencer()
            self.grille._dessiner_grille()
            showinfo("Joueur 1", "Au joueur 1 de jouer !!")
            self.grille.permuterGrilles(self.grille.pos,self.grille.pos2)
            Jouer(self.grille,self.B)