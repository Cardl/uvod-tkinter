from os.path import basename, splitext
import tkinter as tk
from tkinter import Scale, Canvas, HORIZONTAL, StringVar, Entry, ALL

# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "ColorMix"
    length = 255


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.VarR = StringVar(name='VarR')
        self.VarR.set(0)
        self.VarR.trace('w', self.entryUpdate)
        self.entryR = Entry(fg='#ff0000' ,textvariable=self.VarR)
        self.entryR.pack()

        self.scaleR = Scale(from_= 0, to = 255, orient=HORIZONTAL, 
                            command=self.change,
                            background='#ff0000', length=self.length)
        self.scaleR.pack()
        self.scaleG = Scale(from_= 0, to = 255, orient=HORIZONTAL, 
                            command=self.change, 
                            background='#00ff00', length=self.length)
        self.scaleG.pack()
        self.scaleB = Scale(from_= 0, to = 255, orient=HORIZONTAL, 
                            command=self.change,
                            background='#0000ff', length=self.length)
        self.scaleB.pack()

        self.Canvas = Canvas(background="#000000")
        self.Canvas.pack()

        self.varColor = StringVar()
        self.entryColor = Entry(textvariable= self.varColor, width= 7)
        self.entryColor.pack()

                #*arg všechny parametry co "přetečou" tak se zapíší do arg
    def entryUpdate(self, *arg):
        r = self.VarR.get()
        if r.isdigit():
            r =int(r)
        else:
            self.VarR.set(0)
            r = 0
        self.scaleR.set(r)
    def entryValidate(self):
        return False

    def change(self,event):
        r = self.scaleR.get()
        self.VarR.set(r)
        g = self.scaleG.get()
        b = self.scaleB.get()
        hashcolor = "#%02x%02x%02x" %(r, g, b)
        print(hashcolor)
        self.Canvas.config(background = hashcolor)
        self.varColor.set(hashcolor)


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
