from tkinter.messagebox import showinfo
from Model.Scores import Scores
from tkinter import *





class Jouer(object):
    afficherScore = Scores(0,0)
    def __init__(self, grille,bouton):
        self.grille = grille
        self.bouton = bouton
        self.joueur1()   
        self.vaisseauxTrouve1 = 0
        self.vaisseauxTrouve2 = 0
        self.score1 = 0
        self.score2 = 0

        
        
    
    def jouer1(self,event): 
        bool = "true"
        if(self.grille.getCasePos(event.x//40,event.y//40,1).getsituation()==1):
            self.grille.getCasePos(event.x//40,event.y//40,1).setsituation(2)
            self.vaisseauxTrouve1 = self.vaisseauxTrouve1 + 1
            self.score1 = self.score1 + 50
            Jouer.afficherScore.ScoreJ1.set(self.score1)
            

        elif(self.grille.getCasePos(event.x//40,event.y//40,1).getsituation()==2):
            self.joueur1()
        
        elif(self.grille.getCasePos(event.x//40,event.y//40,1).getcouleur() == "red"):
            self.joueur1()
            bool = "false"
            
        else:
            self.grille.getCasePos(event.x//40,event.y//40,1).setcouleur("red")
            self.joueur2()
        self.grille._dessiner_grille()
        
        if(self.grille.getCasePos(event.x//40,event.y//40,1).getsituation()==0 and bool == "true" ):            
            showinfo("Au joueur 2 de jouer", "Essayez de trouvez le vaisseau du joueur 1  !!")
        if(self.vaisseauxTrouve1 == 5):
            self.fin_jeux("Joueur 1")

        
    def jouer2(self,event): 
        bool = "true"
        if(self.grille.getCasePos(event.x//40,event.y//40,2).getsituation()==1):
            self.grille.getCasePos(event.x//40,event.y//40,2).setsituation(2)
            self.vaisseauxTrouve2 = self.vaisseauxTrouve2 + 1
            self.score2 = self.score2 + 50
            Jouer.afficherScore.ScoreJ2.set(self.score2)



        elif(self.grille.getCasePos(event.x//40,event.y//40,2).getsituation()==2):
            self.joueur2()

        elif(self.grille.getCasePos(event.x//40,event.y//40,2).getcouleur() == "red"):
            self.joueur2()
            bool = "false"
             
        else:
            self.grille.getCasePos(event.x//40,event.y//40,2).setcouleur("red")
            self.joueur1()
        self.grille._dessiner_grille()
        
        if(self.grille.getCasePos(event.x//40,event.y//40,2).getsituation()==0 and bool == "true"):            
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
     
        