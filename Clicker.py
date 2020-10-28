from tkinter import *
from pynput.mouse import Listener,Button as Butt,Controller
import threading
from tkinter import messagebox



class MyWindow:

    def __init__(self, win):

        self.timer = None
        self.listener = None

        Label(win, text="Mouse Position",fg="white", bg="black").grid(row=1, column=0)
        Label(win, text="X").grid(row=1, column=1)
        Label(win, text="Y").grid(row=1, column=2)

        self.displayx = Label(win, text="") 
        self.displayx.grid(row=2, column=1)

        self.displayy = Label(win, text="") 
        self.displayy.grid(row=2, column=2)

        Button(win, text="Start Pointer", command=lambda: self.startlistener()).grid(row=2, column=0)
        Button(win, text="Stop Pointer", command=lambda: self.stopListener()).grid(row=2, column=7)

        Label(win, text="Enter X:Y").grid(row=3, column=0)

        self.t1=Entry(bd=3)
        self.t1.grid(row=3, column=1)
        self.t2=Entry(bd=3)
        self.t2.grid(row=3, column=2)

        Label(win, text="Time").grid(row=4, column=0)
        self.t3=Entry(bd=3)
        self.t3.grid(row=4, column=1)

        Button(win, text="Set & Start", command=lambda: self.setStart()).grid(row=4, column=2)
        Button(win, text="Stop", command=lambda: self.stop()).grid(row=4, column=3)

        Label(win, text="Button Clicked").grid(row=5, column=0)

        self.displayl = Label(win, text="")
        self.displayl.grid(row=5, column=2)
        self.displayh = Label(win, text="")
        self.displayh.grid(row=7, column=0)

    def startlistener(self):
        self.listener = Listener(on_move=self.movement)
        self.listener.start()
    
    def stopListener(self):
        if not self.listener:
            self.conOutput(2)
        else:
            self.listener.stop()
            self.conOutput(4)

    def movement(self, x, y):
        self.displayx.configure(text=x)
        self.displayy.configure(text=y)
    
    def setStart(self):

        if (self.validator()):
            self.conOutput(1)
            self.theClicker()

        else:
            self.conOutput(0)
            self.displayh.configure(text="Value of X Y and Time Should not be empty")
    
  
    def stop(self):

        if not self.timer:
            self.conOutput(2)
        else:
            self.timer.cancel()
            self.conOutput(4)
        
            

    def validator(self):

        if not self.t1.get() or not self.t2.get() or not self.t3.get():
            return False
        else:
            return True

    def theClicker(self):

        self.timer = threading.Timer(int(self.t3.get()), self.theClicker)
        self.timer.start()

        mouse = Controller()
        mouse.position = (int(self.t1.get()),int(self.t2.get()))
        mouse.click(Butt.left,2)
        self.displayl.configure(text="left Button Clicked")

        self.conOutput(5)
        self.conOutput(6)
        

    def conOutput(self,x):

        Dict = {0: 'False',
                1: 'True', 
                2: 'Its not running', 
                3: 'Started',
                4: 'Stopped',
                5: 'Left Button Clicked',
                6: '-'*50
                }
        print(Dict.get(x))



def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        mywin.stop()
        window.destroy()

window=Tk()
mywin=MyWindow(window)
window.title('Mouse Clicker')
window.geometry("500x400+10+10")
window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()







