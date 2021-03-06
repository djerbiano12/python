from Vue.Grille import Grille
from Controller.Vaisseaux import Vaisseaux
import tkinter as tk
from tkinter import PhotoImage
from Vue.DessinerJeux import DessinerJeux



 
if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root , width= 400, height=400)
    canvas1 = tk.Canvas(root , width= 400, height=400)
    canvas2 = tk.Canvas(root , width= 400, height=400)

    
logo = PhotoImage(file="C:/Users/amine/My Documents/LiClipse Workspace/Projet/logo.PNG")
G = Grille(10,10,canvas,canvas1,logo)
v = Vaisseaux(G,canvas2,logo)
d = DessinerJeux(G,v,root)


canvas.pack(side = tk.LEFT)
canvas1.pack(side = tk.RIGHT)
canvas2.pack()


root.mainloop()