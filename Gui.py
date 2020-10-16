from tkinter import *
from pynput.mouse import Listener,Button as Butt,Controller
import threading



class MyWindow:
    def __init__(self, win):
        Label(win, text="Mouse Position").grid(row=1, column=0)
        Label(win, text="X").grid(row=1, column=1)
        Label(win, text="Y").grid(row=1, column=2)
        self.displayx = Label(win, text="") # we need this Label as a variable!
        self.displayx.grid(row=2, column=1)
        self.displayy = Label(win, text="") # we need this Label as a variable!
        self.displayy.grid(row=2, column=2)
        Button(win, text="Show Pointer", command=lambda: self.point()).grid(row=2, column=0)

        Label(win, text="Enter X:Y").grid(row=3, column=0)
        self.t1=Entry(bd=3)
        self.t1.grid(row=3, column=1)
        self.t2=Entry(bd=3)
        self.t2.grid(row=3, column=2)

        Label(win, text="Time").grid(row=4, column=0)
        self.t3=Entry(bd=3)
        self.t3.grid(row=4, column=1)
        Button(win, text="Set Position", command=lambda: self.setPoint()).grid(row=4, column=2)

        Label(win, text="Button Clicked").grid(row=5, column=0)
        self.displayl = Label(win, text="") # we need this Label as a variable!
        self.displayl.grid(row=5, column=2)

    def point(self):
        def on_move(x, y):
            print("Mouse moved to ({0}, {1})".format(x, y))
            self.displayx.configure(text=x)
            self.displayy.configure(text=y)
        listener = Listener(on_move=on_move)
        listener.start()

    
    def setPoint(self):
        x,y,t = self.t1.get(),self.t2.get(),self.t3.get() 

        threading.Timer(int(t), self.setPoint).start() # called every minute
        mouse = Controller()
        print("Mouse Position: ",mouse.position)
        mouse.position = (x,y)
        mouse.click(Butt.left,2)
        self.displayl.configure(text="left Button Clicked")
        print("left Button Clicked")
        # print("Refreshed")
        print('-'*50) 


window=Tk()
mywin=MyWindow(window)
window.title('Mouse Clicker')
window.geometry("500x400+10+10")
window.mainloop()


