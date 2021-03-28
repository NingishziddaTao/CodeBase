#!/usr/bin/env python
#mount_iso.py
from Tkinter import *
import os
import pickle 
import tkFileDialog as tkf
import subprocess as sub
import glob

class MountIso:
    #functions inside class
    """choose_iso, mount_iso, open_exe, unmount_iso"""

    def __init__(self, master):
        #variables
        self.master = master
        self.font_size = 140
        self.btn_width = 30
        self.mount_check = 0
        #open iso.pkl to display label
        with open('iso.pkl', 'rb') as self.pklin:
            self.iso_file = pickle.load(self.pklin)
        #tk frame
        self.lbl_frame1 = Frame(self.master)
        self.lbl_frame1.pack()
        #tk label
        self.iso_lbl = Label(self.lbl_frame1, text = self.iso_file)
        self.iso_lbl.grid(row = 0, column = 0)
        #tk frame
        self.btn_frame1 = Frame(self.master)
        self.btn_frame1.pack()
        #tk button
        self.choose_btn = Button(self.btn_frame1, text = 'choose iso', command = self.choose_iso, font = self.font_size , width = 30).grid(row = 0, column = 0)
        #tk button
        self.mount_btn = Button(self.master, text = 'Mount iso', command = self.mount_iso, font =
                self.font_size , width = 30).pack()
        #tk button
        self.exe_btn = Button(self.master, text = 'wine open exe', command = self.open_exe, font =
                self.font_size, width = 30).pack()
        #tk bind
        self.master.bind('<Return>', lambda bind_event: self.master.destroy())

    #open iso and save as iso.pkl
    def choose_iso(self):
        self.iso_file = tkf.askopenfilename(initialdir = "/mnt/sda5/", title = "Selectfile",filetypes = (("iso files","*.iso"),("all files","*.*")))
        print (self.iso_file)
        with open('iso.pkl', 'wb') as pklout:
                    pickle.dump(self.iso_file, pklout)
        #tk label
        self.iso_lbl = Label(self.lbl_frame1, text = self.iso_file)
        self.iso_lbl.grid(row = 0, column = 0)

    #mount iso in terminal
    def mount_iso(self):
        print self.mount_check
        with open('iso.pkl', 'rb') as self.pklin:
            self.iso_file = pickle.load(self.pklin)
            print self.iso_file
        os.system("gnome-terminal --geometry 100x3 -e 'bash -c \"sudo mount "+str(self.iso_file)+" /mnt/sda5/iso; exec bash\"'")
        self.mount_check += 1
        if self.mount_check == 1:
            self.unmount_btn = Button(self.btn_frame1, text = 'unmount iso', command = self.unmount_iso, font
                = self.font_size , width = 30).grid(row = 0, column = 0)

    #open iso with wine
    def open_exe(self):
        exe_file = glob.glob('/mnt/sda5/iso/*.exe')
        try: 
            sub.call(['wine', str(exe_file)[2:-2]])
        except:
            pass

    def unmount_iso(self):
        self.mount_check -= 1
        os.system("gnome-terminal --geometry 100x3 -e 'bash -c \"sudo umount "+str(self.iso_file)+" ; exec bash\"'")
        if self.mount_check == 0:
            #tk button
            self.choose_btn = Button(self.btn_frame1, text = 'choose iso', command = self.choose_iso, font = self.font_size , width = 30).grid(row = 0, column = 0)

#exe
master = Tk()
MountIso(master)
master.mainloop()
