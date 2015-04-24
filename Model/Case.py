class Case(object):
    # Cette classe est utilisee pour reperer la position des rectangles 
    # Construisant la grille
    def __init__(self, x,y,couleur,situation):
        self.x = x
        self.y= y
        self.couleur = couleur
        self.situation = situation
   
        
    def getcouleur(self):
        return self.couleur
    
    def setcouleur(self,couleur):
        self.couleur = couleur
        
    def getsituation(self):
        return self.situation
    
    def setsituation(self,situation):
        self.situation = situation