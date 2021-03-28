#auto_gui
from Tkinter import *
import pyautogui as pyg

class App:
    def __init__(self, master): 
        self.master = master

        #tk.button
        self.find_position =Button(self.master, text = 'find position', command = self.findPosition)
        self.find_position.pack()

        self.click_position = Button(self.master, text = 'click position', command = self.clickPosition)
        self.click_position.pack()

        #tk.bind
        self.master.bind('<Escape>', lambda x: self.guit())

    def findPosition(self):
        pass

        def key(event):
            print "pressed", event.char
            if event.char == 'q':
                self.q = pyg.position()
                print 'saved', self.q
            if event.char == 'w':
                self.w = pyg.position()
                print 'saved', self.w
            if event.char == 'e':
                self.e = pyg.position()
                print 'saved', self.e
            if event.char == 'r':
                self.r = pyg.position()
                print 'saved', self.r

        self.master.bind("<Key>", key)

    def clickPosition(self):
        pass

        def key(event):
             
            if event.char == 'q':
                pyg.click(self.q, interval=0.0, button='left', duration=0.1, pause=None, _pause=True)
                self.master.focus_force()

            if event.char == 'w':
                pyg.click(self.w, interval=2.0, button='left', duration=0.1, pause=None, _pause=True)
                self.master.focus_force()

            if event.char == 'e':
                pyg.click(self.e, clicks=1, interval=2.0, button='left', duration=0.1, pause=None, _pause=True)
                self.master.focus_force()

            if event.char == 'r':
                pyg.click(self.r, clicks=1, interval=2.0, button='left', duration=0.1, pause=None, _pause=True)
                self.master.focus_force()

        self.master.bind("<Key>", key)

    def guit(self):
        self.master.destroy()

master = Tk()
app = App(master)
master.mainloop()
