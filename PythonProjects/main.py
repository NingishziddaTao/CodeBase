#buffer_proj.py
import curses
import os
import argparse
from glob import glob
from curses import panel
from curses import wrapper
from time import sleep

class App():

    def _refresh_all(self):
        self.debug.clear()
        self.debug.addstr(1,1, str(self.description_list[self.position]))
        self.debug.addstr(2,1, str(os.getcwd()))

        #self.screen.box();self.screen.refresh()
        self.box1.refresh(self.yScroll, self.xScroll, self.yOffset, self.xOffset ,self.height,self.width)
        #self.debug.box()
        #self.debug.noutrefresh()

    def display_terminal(self, arg):
        self.screen.clear()
        curses.endwin()
        os.system(arg)
        os.system("read")
        os.system("clear")
        #self._refresh_all()

    def debug(self):
        height = int(self.max_y * 0.3)
        width = int(self.max_x * 0.96)
        yOffset = int(self.max_y * 0.7)
        xOffset = int(self.max_x * 0.03)
        debug = curses.newwin(height, width, yOffset, xOffset)
        debug.box()    
        debug.addstr("*debug ")
#        self.debug.addstr(1,1, str(self.description_list[self.position]))
#        self.debug.addstr(2,1, str(os.system("pwd")))
#        self.debug.addstr(3,1, str(len(self.command_list)))

        return debug

    def __init__(self, stdscr):
        curses.curs_set(0)
        self.screen = stdscr
        self.screen.box()
        self.screen.addstr("*screen ")

        self.max_y, self.max_x  = self.screen.getmaxyx()

        self.description_list = []
        self.command_list = []

        # Argparse
        parser = argparse.ArgumentParser(description="reminder")
        parser.add_argument("command_file", help = "reminder")
        args = parser.parse_args()

        def get_file(command_file):#argparse
            with open(command_file) as reader:
                commands = reader.read().split("\n")
                for line in commands:
                    if line.startswith("#"):
                        self.description_list.append(line)
                    if line.startswith(" "):
                        self.command_list.append(line)

            dic = zip(self.description_list, self.command_list)

            # Box1
            self.position = 0
            self.yScroll = 0 
            self.xScroll = 0 
            self.yOffset = int(self.max_y * 0.1)
            self.xOffset = int(self.max_x * 0.03)
            self.height = int(self.max_y * 0.60)
            self.width = int(self.max_x * 0.96)
            self.box1 = curses.newpad(60, self.width)
            self.box1.box()
            self.box1.addstr("*box1 ")

            self.debug = self.debug()

            # Process
            while 1:

                for i, x in enumerate(self.command_list):
                    if self.position == i:
                        mod = curses.A_REVERSE
                    else:
                        mod = curses.A_NORMAL
     
                    self.box1.addstr(i+2, 2, self.command_list[i], mod)
                    self._refresh_all()

                # Controls
                self.key = self.box1.getch() 
                if self.key == ord("q"):#quit
                    break

                elif self.key == ord("j") and self.position > len(self.command_list)-1:#pad down
                    self.position += 1
                    if self.key == ord("j") and self.position > 5:
                        self.yScroll +=1

                elif self.key == ord("k") and self.position > -0:#pad up
                    self.position -= 1
                    if self.key == ord("k") and self.position > len(self.command_list)-5:
                        self.yScroll -=1

                elif self.key == 10: #press enter to execute commands
                    self.display_terminal(self.command_list[self.position])

        get_file(args.command_file)

if __name__ == "__main__":
    wrapper(App)

