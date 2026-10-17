from tkinter import *
from tkinter import messagebox
PD_1_Y = 0
PD_2_Y = 0
wd = Tk()
wd.geometry("600x550")
wd.config(background="white")
wd.title("Ping Pong Match")
def Move_PD1(event):
    global PD_1_Y
    if event.keysym == "w":
         PD_1_Y = -5
    elif event.keysym == "s":
         PD_1_Y = 5
def Stop_PD1(event):
     global PD_1_Y
     if event.keysym == "w":
          PD_1_Y = 0
     elif event.keysym == "s":
          PD_1_Y = 0
def Move_PD2(event):
     global PD_2_Y
     if event.keysym == "Up":
          PD_2_Y = -5
     elif event.keysym == "Down":
          PD_2_Y = 5

def Stop_PD2(event):
     global PD_2_Y
     if event.keysym == "Up":
          PD_2_Y = 0
     elif event.keysym == "Down":
          PD_2_Y = 0
def M_1(PD_1_O, PD_1_Y):
      C.move(PD_1_O,0,PD_1_Y)
      XY1 = C.coords(PD_1_O)
      if XY1[1] < 0:
            C.move(PD_1_O,0,-XY1[1])
      elif XY1[3] > 550:
            C.move(PD_1_O,0,550-XY1[3])
def M_2(PD_2_G, PD_2_Y):
      C.move(PD_2_G,0,PD_2_Y)
      XY2 = C.coords(PD_2_G)
      if XY2[1] < 0:
            C.move(PD_2_G,0,-XY2[1])
      elif XY2[3] > 550:
            C.move(PD_2_G,0,550-XY2[3])
     
     
C = Canvas(wd, bg = "black",bd = 1,highlightthickness= 3,highlightbackground="black", width = 600, height = 550)
C.place(x = 0, y = 0)
C.bind_all("<KeyPress-w>", Move_PD1)
C.bind_all("<KeyPress-s>", Move_PD1)
C.bind_all("<KeyRelease-w>",Stop_PD1)
C.bind_all("<KeyRelease-s>",Stop_PD1)
C.bind_all("<KeyPress-Up>", Move_PD2)
C.bind_all("<KeyPress-Down>", Move_PD2)
C.bind_all("<KeyRelease-Up>", Stop_PD2)
C.bind_all("<KeyRelease-Down>", Stop_PD2)


C.create_line(300,0,300,550,fill = "white")
C.create_oval(250, 215, 350,315,outline = "white")
C.create_oval(250,230,300,280,fill = "yellow")
PD_1_O = C.create_rectangle(0,200,15,280,fill = "orange")

PD_2_G = C.create_rectangle(585,200,596,280,fill = "green")
def game_loop():


     M_1(PD_1_O,PD_1_Y)
     M_2(PD_2_G,PD_2_Y)
     wd.after(15,game_loop)

game_loop()




wd.mainloop()