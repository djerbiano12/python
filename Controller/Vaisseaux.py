import tkinter as tk
from Controller.Jouer import Jouer
from tkinter.messagebox import showinfo
from tkinter import Button
from tkinter import DISABLED





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
        self.posX = 0
        self.posY = 0
        self.deborder = False
 
  
  
    # Cette fonction est appelee pour placer les vaisseaux au debut du jeux
    def placer_vaisseaux1(self):
        showinfo("Joueur 1", "Choisissez la position de vos 5 vaisseaux")
        self.grille.canvas.bind("<Button-1>", self.jouer1)
        self.B.config(state=DISABLED)
        
    # Cette fonction permet au joueur 1 de palcer ses vaisseaux
    def jouer1(self,event):
        if (self.grille.nbVaisseauxPlaces(self.grille.pos) < 5):
            self.effacerGreen()
            self.grille.get_pos(event.x//40,event.y//40).setsituation(2)
            self.guider(event.x//40,event.y//40)
            self.grille._dessiner_grille()
            self.posX = event.x//40
            self.posY = event.y//40
            
        if(self.grille.nbVaisseauxPlaces(self.grille.pos) == 5):
            showinfo("Joueur 2", "Choisissez la position de vos 5 vaisseaux")
            self.placer_vaisseaux2()
       
    # Cette fonction permet au joueur 2 de palcer ses vaisseaux    
    def placer_vaisseaux2(self):
        self.grille.canvas1.bind("<Button-1>", self.jouer2)

    # Cette fonction permet au joueur 2 de palcer ses vaisseaux    
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
    
    def guider(self,pos1,pos2):

        if (self.posX == 0 and self.posY == 0):
            self.grille.get_pos(pos1+1,pos2).setcouleur("green")
            self.grille.get_pos(pos1-1,pos2).setcouleur("green")
            self.grille.get_pos(pos1,pos2+1).setcouleur("green")
            self.grille.get_pos(pos1,pos2-1).setcouleur("green")
        elif(pos1 > self.posX and self.grille.nbVaisseauxPlaces(self.grille.pos) < 5 or (self.deborder == True and self.posX != pos1)):
            if(pos1 == self.grille.width - 1):
                pos1 = -1
                self.deborder = True
                self.grille.get_pos(pos1+1,pos2).setcouleur("green")
            else: 
                self.deborder = False    
                self.grille.get_pos(pos1+1,pos2).setcouleur("green")
        elif(pos1 < self.posX and self.grille.nbVaisseauxPlaces(self.grille.pos) < 5):
            self.grille.get_pos(pos1-1,pos2).setcouleur("green")
        elif(pos2 > self.posY and self.grille.nbVaisseauxPlaces(self.grille.pos) < 5  or self.deborder == True):
            if(pos2 == self.grille.height - 1):
                pos2 = -1
                self.grille.get_pos(pos1,pos2+1).setcouleur("green")
                self.deborder = True
            else:
                self.deborder = False
                self.grille.get_pos(pos1,pos2+1).setcouleur("green")
        elif(pos2 < self.posY and self.grille.nbVaisseauxPlaces(self.grille.pos) < 5):
            self.grille.get_pos(pos1,pos2-1).setcouleur("green")
            
        
    def effacerGreen(self):
        for i in range(self.grille.width):
            for j in range(self.grille.height):
                if(self.grille.get_pos(i,j).getcouleur() == "green"):
                    self.grille.get_pos(i,j).setcouleur("black")
        self.grille._dessiner_grille()
        
        
        
        
        
        
        
        