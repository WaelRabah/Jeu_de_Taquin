from tkinter import * 
from Solver import Solver , AStar
from Solver import Node
from Solver import Puzzle 
import time

global puzzl , t ,j

j=0
fenetre = Tk()


print("Donner la taille de votre puzzle : \n 3 --> 3*3 \n 4 --> 4*4")
t=int(input())
time.sleep(2)

if(t==3):
	board = [[0,1,2],[3,4,5],[6,7,8]]
else :
	board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

photos=[]
for i in range(0,16):
	photos.append(PhotoImage(file="./images/"+str(i)+".png"))

global Lph , LAff
if ( t==3 ):
	Lph = photos[0:9]
else :
	Lph = photos[0:16]


can=Canvas( width=180*t,height=180*t,bg='white')
can.pack( side =TOP, padx =20, pady =20)
fenetre['bg']='white'
fenetre.title (' Taquin resolution IA')

puzzl = Puzzle(board,can,Lph)
s = Solver(puzzl,fenetre)
goal = Puzzle(board,can,Lph)
a_star=AStar(fenetre,puzzl,Node(puzzl),Node(goal),int(t),0)
def Astar_solve_manhattan():
	global a_star , puzzl
	a_star=AStar(fenetre,puzzl,Node(puzzl),Node(goal),int(t),1)
	puzzl=a_star.solve()
def Astar_solve_misplaced():
	global a_star , puzzl
	a_star=AStar(fenetre,puzzl,Node(puzzl),Node(goal),int(t),0)
	puzzl=a_star.solve()

def solv():
	global s
	s =Solver(puzzl,fenetre)
	s.solve()

def mel():
	global puzzl
	puzzl = puzzl.shuffle()

def melanger():
	print(puzzl.board)

LAff = list([0,1,2,3,4,5,6,7,8])
LAff=[]
for row in board:
    LAff.extend(row)
menubar = Menu(fenetre)
menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="melanger", command=mel)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="melanger", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Recherche en longeur", command=solv)
menu2.add_command(label="Recherche en largeur", command=solv)
menu2.add_command(label="A * : Σ distances de chaque pièce à sa position finale", command=Astar_solve_manhattan)
menu2.add_command(label="A * : nb de pièces mal placées", command=Astar_solve_misplaced)
menubar.add_cascade(label="Résoudre", menu=menu2)
fenetre.config(menu=menubar)

Button(text='MEL',command=mel).pack(side=LEFT)
Button(text='RESO1',command=solv).pack(side=LEFT)
Button(text='RESO2',command=solv).pack(side=LEFT)
Button(text='A* : h1',command=Astar_solve_manhattan).pack(side=LEFT)
Button(text='A* : h2',command=Astar_solve_misplaced).pack(side=LEFT)




for k in range(len(Lph)) :
    eff = can.create_image((30+ 150*(k % t)), 30+(150*( k // t)), anchor=NW, image=Lph[0])
    aff = can.create_image((30+ 150*(k % t)), 30+(150*( k // t)), anchor=NW ,image = Lph[LAff[k]])

can.pack()

fenetre.mainloop()