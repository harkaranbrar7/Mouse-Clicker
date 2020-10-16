from tkinter import *
from pynput.mouse import Listener,Button as Butt,Controller
import threading



class MyWindow:

    def __init__(self, win):


        self.listener = Listener(on_move=self.Move)

        Label(win, text="Mouse Position",fg="white", bg="black").grid(row=1, column=0)
        Label(win, text="X").grid(row=1, column=1)
        Label(win, text="Y").grid(row=1, column=2)
        self.displayx = Label(win, text="") # we need this Label as a variable!
        self.displayx.grid(row=2, column=1)
        self.displayy = Label(win, text="") # we need this Label as a variable!
        self.displayy.grid(row=2, column=2)
        Button(win, text="Start Pointer", command=lambda: self.startlistener()).grid(row=2, column=0)
        Button(win, text="Stop Pointer", command=lambda: self.listener.stop()).grid(row=2, column=7)

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
        self.displayl = Label(win, text="")
        self.displayl.grid(row=5, column=2)
        self.displayh = Label(win, text="")
        self.displayh.grid(row=7, column=0)

    def startlistener(self):
        
        if not self.listener.is_alive():
            self.listener.restart()
        else:
            self.listener.start()

    def Move(self, x, y):
        print("Mouse moved to ({0}, {1})".format(x, y))
        self.displayx.configure(text=x)
        self.displayy.configure(text=y)
    
    def setPoint(self):
        x,y,t = self.t1.get(),self.t2.get(),self.t3.get() 
      
        
        if not x or not y or not t :
            print ("Value of X Y and Time Should not be empty")
            self.displayh.configure(text="Value of X Y and Time Should not be empty")
        
        else:
              print(" x: ",x," y: ",y," t: ",t)

            
        # threading.Timer(int(t), self.setPoint).start() # called every minute
        # mouse = Controller()
        # print("Mouse Position: ",mouse.position)
        # mouse.position = (x,y)
        # mouse.click(Butt.left,2)
        # self.displayl.configure(text="left Button Clicked")
        # print("left Button Clicked")
        # # print("Refreshed")
        # print('-'*50)







window=Tk()
mywin=MyWindow(window)
window.title('Mouse Clicker')
window.geometry("500x400+10+10")
window.mainloop()




