import tkinter as tk
from tkinter import messagebox
from Controller.Jouer import Jouer
from tkinter.messagebox import showinfo
from tkinter import Button
from tkinter import DISABLED
import time
import random






class Vaisseaux(object):
    '''
    classdocs
    '''


    def __init__(self,grille,canvas,logo):
        self.grille = grille
        self.canvas = canvas
        self.logo= logo
        self.B = Button(self.canvas, text ="Commencer",command = self.ouvrirDialogue1)
        self.B.pack(side = tk.BOTTOM,pady=80)
        self.posX = 0
        self.posY = 0
 
  
  
    # Cette fonction est appelee pour placer les vaisseaux au debut du jeux
    def placer_vaisseaux1(self):
        self.grille.canvas.bind("<Button-1>", self.jouer1)
        self.B.config(state=DISABLED)
        
    # Cette fonction permet au joueur 1 de palcer ses vaisseaux
    def jouer1(self,event):
        if (self.grille.nbVaisseauxPlaces(self.grille.pos) < 5):
            
            if(self.grille.getCasePos(event.x//40,event.y//40,1).getcouleur() == "green" or self.grille.nbVaisseauxPlaces(self.grille.pos) == 0):
                self.effacerGreen(1)
                self.grille.getCasePos(event.x//40,event.y//40,1).setsituation(2)
                self.guider(event.x//40,event.y//40,1)
                self.grille._dessiner_grille()
                self.posX = event.x//40
                self.posY = event.y//40
                
            
        if(self.grille.nbVaisseauxPlaces(self.grille.pos) == 5):
            self.posX = 0
            self.posY = 0
            self.ouvrirDialogue2()
            #self.placer_vaisseaux2()
       
    # Cette fonction permet au joueur 2 de palcer ses vaisseaux    
    def placer_vaisseaux2(self):
        self.grille.canvas1.bind("<Button-1>", self.jouer2)

    # Cette fonction permet au joueur 2 de palcer ses vaisseaux    
    def jouer2(self,event):
        if (self.grille.nbVaisseauxPlaces(self.grille.pos2) < 5):
            if(self.grille.getCasePos(event.x//40,event.y//40,2).getcouleur() == "green" or self.grille.nbVaisseauxPlaces(self.grille.pos2) == 0):
                self.effacerGreen(2)
                self.grille.getCasePos(event.x//40,event.y//40,2).setsituation(2)
                self.guider(event.x//40,event.y//40,2)
                self.grille._dessiner_grille()
                self.posX = event.x//40
                self.posY = event.y//40
                
        if(self.grille.nbVaisseauxPlaces(self.grille.pos2) == 5):
            self.grille.commencer()
            self.grille._dessiner_grille()
            showinfo("Au joueur 1 de jouer", "Essayez de trouvez le vaisseau du joueur 2  !!")
            self.grille.permuterGrilles(self.grille.pos,self.grille.pos2)
            Jouer(self.grille,self.B)
    
    def guider(self,pos1,pos2,num):
        if(num == 1):
            tableau = self.grille.pos
        else:
            tableau = self.grille.pos2
        if (self.posX == 0 and self.posY == 0):
            self.grille.getCasePos(pos1+1,pos2,num).setcouleur("green")
            self.grille.getCasePos(pos1-1,pos2,num).setcouleur("green")
            self.grille.getCasePos(pos1,pos2+1,num).setcouleur("green")
            self.grille.getCasePos(pos1,pos2-1,num).setcouleur("green")
        elif(pos1 > self.posX and self.grille.nbVaisseauxPlaces(tableau) < 5 ):
            if(pos1 == self.grille.width - 1):
                pos1 = pos1 - self.grille.nbVaisseauxPlaces(tableau)
                self.grille.getCasePos(pos1,pos2,num).setcouleur("green")
            else: 
                self.grille.getCasePos(pos1+1,pos2,num).setcouleur("green")
        elif(pos1 < self.posX and self.grille.nbVaisseauxPlaces(tableau) < 5):
            if(pos1 == 0):
                pos1 = pos1 + self.grille.nbVaisseauxPlaces(tableau) 
                self.grille.getCasePos(pos1,pos2,num).setcouleur("green")      
            else:
                self.grille.getCasePos(pos1-1,pos2,num).setcouleur("green")
                
        elif(pos2 > self.posY and self.grille.nbVaisseauxPlaces(tableau) < 5 ):
            if(pos2 == self.grille.height - 1):
                pos2 = pos2 - self.grille.nbVaisseauxPlaces(tableau)
                self.grille.getCasePos(pos1,pos2,num).setcouleur("green")
            else:
                self.grille.getCasePos(pos1,pos2+1,num).setcouleur("green")
        elif(pos2 < self.posY and self.grille.nbVaisseauxPlaces(tableau) < 5 ):
            if(pos2 == 0):
                pos2 = pos2 + self.grille.nbVaisseauxPlaces(tableau) 
                self.grille.getCasePos(pos1,pos2,num).setcouleur("green")      
            else:
                self.grille.getCasePos(pos1,pos2-1,num).setcouleur("green")
            
        
    def effacerGreen(self,num):
        for i in range(self.grille.width):
            for j in range(self.grille.height):
                if(self.grille.getCasePos(i,j,num).getcouleur() == "green"):
                    self.grille.getCasePos(i,j,num).setcouleur("black")
        self.grille._dessiner_grille()
      
        
    def placerVaisseauAleatoire(self):
        r = random.randint(1,10)   
        for i in range(1,6):
            self.grille.getCasePos(r,i,1).setsituation(2)
            self.grille._dessiner_grille() 
        self.ouvrirDialogue2()   
        
    def placerVaisseauAleatoire2(self):
        r = random.randint(1,10)   
        for i in range(1,6):
            self.grille.getCasePos(r,i,2).setsituation(2)
        self.grille._dessiner_grille() 
        showinfo("Joueur 1", "Au joueur 1 de jouer !!")
        self.grille.commencer()
        self.grille._dessiner_grille()
        self.grille.permuterGrilles(self.grille.pos,self.grille.pos2)
        Jouer(self.grille,self.B)
            
    def ouvrirDialogue1(self):
        if messagebox.askquestion("Joueur 1", "Voulez vous placez les vaisseausx aléatoirement?")=="no":
            showinfo("Joueur 1", "Placez votre vaisseau en cliquant sur 5 cases de votre grille !!")
            self.placer_vaisseaux1()
        else:
            self.B.config(state=DISABLED)
            self.placerVaisseauAleatoire()
           
    def ouvrirDialogue2(self):
        if messagebox.askquestion("Joueur 2", "Voulez vous placez les vaisseausx aléatoirement?")=="no":
            showinfo("Joueur 2", "Placez votre vaisseau en cliquant sur 5 cases de votre grille !!")
            self.placer_vaisseaux2()
        else:
            self.placerVaisseauAleatoire2()
                