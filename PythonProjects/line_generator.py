#line_ge]nerator.py
from Tkinter import *
import webbrowser as web
import tkFileDialog as tkf
import pyautogui as pyg
import tkFont
import time

#help("pyautogui")
#pyg.displayMousePosition()
#help("Tkinter")


class LineGenerator:
    """yieldFile nextLine buttonShift"""

    def __init__(self, root):
        self.root = root
        #var
        self.web_count = 0
        self.font1 = tkFont.Font(size = 16)
        #open file and make a list of lines called self.file_list
        with open(tkf.askopenfilename(initialdir = "/")) as self.open_file:
            self.file_list = self.open_file.read().split("\n")
        #print amount of lines 
        for i in range(len(self.file_list)):
            i += 1 
        print (i,"lines inside of 'file_list'")
        ##generator
        self.yieldFile()
        self.yield_file = self.yieldFile()
        #tk_frame
        self.frame = Frame(root, image = None, bg = "black", borderwidth = 1) 
        self.frame.pack(side = None)
        #tk_button
        btn = Button(self.frame, text = "press 'Enter' to go to next", font =
                self.font1, fg = None, bg = None, width = None, command = self.buttonShift) 
        btn.grid(row = 1, column = 1, ipadx = None)
        #tk bind
        self.root.bind("<Return>", lambda bind_event: self.nextLine())
        #self.root.bind("<Escape>", lambda bind_event: self.root.destroy())
        print (self.file_list)

    def buttonShift(self):
        #tk_entry
        entry = Entry(self.frame, font = self.font1, bg = "black", fg = "white", width = None) 
        entry.focus()
        entry.insert(0, "")
        entry.grid(row = 1, column = 1, ipadx = None)

    def yieldFile(self):
        for i in self.file_list:
            if i == '':
                pass
            else:
                yield i

    def nextLine(self):
        #close second last window
 #       if self.web_count >= 3:
 #           time.sleep(1)
 #           pyg.click(x = 1000, y = 600, clicks = 1)
 #           pyg.hotkey("ctrl", "shift", "tab")
 #           pyg.hotkey("ctrl", "w")

        for line in self.file_list:
            #open  url
            if line[0:4] == "http":
                self.web_count += 1 
                print (self.web_count)
                web.open_new(next(self.yield_file))
                time.sleep(2)
                self.root.lift()
                break

root = Tk()
root.geometry("+0+0")
LineGenerator(root)
root.mainloop()
