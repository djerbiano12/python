from tkinter.messagebox import showinfo
from tkinter import NORMAL


class Jouer(object):
 
    def __init__(self, grille,bouton):
        self.grille = grille
        self.bouton = bouton
        self.joueur1()   
        self.vaisseauxTrouve1 = 0
        self.vaisseauxTrouve2 = 0

    
    def jouer1(self,event): 
        if(self.grille.get_pos(event.x//40,event.y//40).getsituation()==1):
            self.grille.get_pos(event.x//40,event.y//40).setsituation(2)
            self.vaisseauxTrouve1 = self.vaisseauxTrouve1 + 1

        elif(self.grille.get_pos(event.x//40,event.y//40).getsituation()==2):
            self.joueur1()
            
        else:
            self.grille.get_pos(event.x//40,event.y//40).setcouleur("red")
            self.joueur2()
        self.grille._dessiner_grille()
        
        if(self.grille.get_pos(event.x//40,event.y//40).getsituation()==0):            
            showinfo("Joueur 2", "Au joueur 2 de jouer !!")
        if(self.vaisseauxTrouve1 == 5):
            self.fin_jeux("Joueur 1")

        
    def jouer2(self,event): 
        if(self.grille.get_pos2(event.x//40,event.y//40).getsituation()==1):
            self.grille.get_pos2(event.x//40,event.y//40).setsituation(2)
            self.vaisseauxTrouve2 = self.vaisseauxTrouve2 + 1


        elif(self.grille.get_pos2(event.x//40,event.y//40).getsituation()==2):
            self.joueur2()

        else:
            self.grille.get_pos2(event.x//40,event.y//40).setcouleur("red")
            self.joueur1()
        self.grille._dessiner_grille()
        
        if(self.grille.get_pos2(event.x//40,event.y//40).getsituation()==0):            
            showinfo("Joueur 1", "Au joueur 1 de jouer !!")
        if(self.vaisseauxTrouve2 == 5):
            self.fin_jeux("Joueur 2")
        
    def joueur1(self):
        self.grille.canvas1.bind("<Button-1>", "")
        self.grille.canvas.bind("<Button-1>", self.jouer1)
    
    def joueur2(self):
        self.grille.canvas.bind("<Button-1>", "")
        self.grille.canvas1.bind("<Button-1>", self.jouer2)
        
    def fin_jeux(self,joueur):
        showinfo(joueur, "Félicitation!! Tu as gagné !!")
        self.grille.initialiser()
        self.grille._dessiner_grille()
        self.vaisseauxTrouve1 = 0
        self.vaisseauxTrouve2 = 0
        self.bouton.config(state=NORMAL) 
     
        