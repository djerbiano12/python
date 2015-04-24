from Model.Case import Case




class Grille(object):
  
    def __init__(self, width,height,canvas,canvas1,logo):
        self.width = width
        self.height= height
        self.logo = logo
        self.canvas= canvas
        self.canvas1= canvas1
        self.pos = [[Case] * width for _ in range(height)]
        self.pos2 = [[Case] * width for _ in range(height)]
        self.initialiser()
        #self._dessiner_grille()

        
    def _dessiner_grille(self):
        self._dessiner_grille1()
        self._dessiner_grille2()

    
    def _dessiner_grille1(self):
        pas=400/self.width
        #self.canvas.create_image(10,10,image = self.logo)
        #widget = tk.Label(self.canvas2, text='Spam', fg='white', bg='black')
        #widget.pack(side = "center") 
        #tk.Label(self.canvas2, text = "Texte", bg="red", fg="white" , font=("Helvetica", 10) ).pack( side = tk.BOTTOM , anchor = tk.S)  
        

        for i in range(self.width):
            for j in range(self.height):
                if(self.pos[i][j].getsituation() == 1 ):
                    self.canvas.create_rectangle(pas*i, pas*j, pas*(i+1), pas*(j+1), fill=self.pos[i][j].getcouleur(),outline = 'white')
                    self.pos[i][j] = Case(pas*i,pas*j,self.pos[i][j].getcouleur(),1)
                elif(self.pos[i][j].getsituation() == 2):
                    self.canvas.create_image(pas*(i+0.55),pas*(j+0.55),image = self.logo)
                          
                else:  
                    self.canvas.create_rectangle(pas*i, pas*j, pas*(i+1), pas*(j+1), fill=self.pos[i][j].getcouleur(),outline = 'white')
                    self.pos[i][j] = Case(pas*i,pas*j,self.pos[i][j].getcouleur(),0)
  

    def _dessiner_grille2(self):
        pas=400/self.width
        for i in range(self.width):
            for j in range(self.height):
                if(self.pos2[i][j].getsituation() == 1 ):
                    self.canvas1.create_rectangle(pas*i, pas*j, pas*(i+1), pas*(j+1), fill=self.pos2[i][j].getcouleur(),outline = 'white')
                    self.pos2[i][j] = Case(pas*i,pas*j,self.pos2[i][j].getcouleur(),1)
                
                elif(self.pos2[i][j].getsituation() == 2):
                    self.canvas1.create_image(pas*(i+0.55),pas*(j+0.55),image = self.logo)
                
                else:  
                    self.canvas1.create_rectangle(pas*i, pas*j, pas*(i+1), pas*(j+1), fill=self.pos2[i][j].getcouleur(),outline = 'white')
                    self.pos2[i][j] = Case(pas*i,pas*j,self.pos2[i][j].getcouleur(),0)
        
    def getCasePos(self,x,y,z):
        if(z == 1):
            if(x == self.height or y == self.width):
                return Case(x,y,"black",4)
            return self.pos[x][y]
        else:
            if(x == self.height or y == self.width):
                return Case(x,y,"black",4)
            return self.pos2[x][y]

    
    def initialiser(self): 
        for i in range(self.width):
            for j in range(self.height):
                self.pos[i][j] = Case(i,j,"black",0)

        for i in range(self.width):
            for j in range(self.height):
                self.pos2[i][j] = Case(i,j,"black",0)
                
    def commencer(self):        
        for i in range(self.width):
            for j in range(self.height):
                if(self.pos[i][j].getsituation() == 2): self.pos[i][j].setsituation(1)
                if(self.pos2[i][j].getsituation() == 2): self.pos2[i][j].setsituation(1)
                
    def nbVaisseauxPlaces(self,pos):
        nb = 0
        for i in range(self.width):
            for j in range(self.height):
                if(pos[i][j].getsituation() == 2):
                    nb = nb + 1
        return nb
    
    def permuterGrilles(self,pos1,pos2):
        for i in range(self.width):
            for j in range(self.height):
                interm = pos1[i][j]
                pos1[i][j] = pos2[i][j]
                pos2[i][j] = interm
                
                
                
                
                
                
                
                
        