from Vue.Grille import Grille
from Model.Vaisseaux import Vaisseaux
import tkinter as tk
from tkinter import PhotoImage



 
if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root , width= 450, height=450)
    canvas1 = tk.Canvas(root , width= 450, height=450)
    canvas2 = tk.Canvas(root , width= 450, height=450)

    
logo = PhotoImage(file="C:/Users/amine/My Documents/LiClipse Workspace/Projet/logo.PNG")
G = Grille(10,10,canvas,canvas1,logo)
v = Vaisseaux(G,canvas2,logo)

#widget = tk.Label(canvas, text='Spam', fg='white', bg='black')
#widget.pack(side =tk.LEFT,padx = 5,pady = 5)


canvas.pack(side = tk.LEFT)
canvas1.pack(side = tk.RIGHT)
canvas2.pack(side = tk.RIGHT)


root.mainloop()