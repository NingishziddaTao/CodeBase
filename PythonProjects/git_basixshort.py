#git_basixshort.py
import curses
import os
from glob import glob
from time import sleep
from curses import panel
from curses import wrapper

""" basic git commands, with shortcuts,
iterates tru git maps changes working directory
creates a menu with list of repository defined in git.txt and executes the commands.

j = down k = up and if you press they key of the numbers you will activate the
git functions
"""

def main(stdscr):
    #init
    curses.curs_set(0)
    position = 0
    offset = 0
    pad2_length = 5
    repo_list = []
    url_list = []

    #lists
    with open("/git.txt") as reader:
        git_list = reader.read().split("\n")
        for line in git_list:
            if line.startswith("#"):
                repo_list.append(line[1:])
            else:
                url_list.append(line)

    git_commands = (
        "1. git pull",
        "2. git status",
        "3. git add -A",
        "4. git commit -m comment",
        "5. git push -u repo"
        )

    def for_addstr(widget, iterable):
        for index, string in enumerate(iterable):
            widget.addstr(index ,0, string)

    def layout(arg1, arg2):
        y = stdscr.getmaxyx()[0]
        x = stdscr.getmaxyx()[1]
        win_y = int(round(y * arg1, 0))
        win_x = int(round(x * arg2, 0))
        return win_y,win_x

    def panel_setup(h,l, y,x, *args):
        win = stdscr.subwin(h,l, y,x)
        win.box(*args)
        pan = curses.panel.new_panel(win)
        return win

    def display_terminal(arg):
        stdscr.clear()
        #curses.putp("press any key")
        curses.endwin()
        curses.wrapper(main)
        #curses.setupterm([termstr, fd])
        stdscr.clear()
        #os.system("clear")
        os.system(arg)
        stdscr.getch()
        #stdscr.box()

    #scaling
    spaceY = 4 #upper window
    stdscrY, stdscrX = layout(0.80, 1.00) #mid window
    win1y, win1x = layout(0.20, 0) #lower window
    win1 = panel_setup(win1y,win1x, stdscrY,0)
    pad2 = curses.newpad(100, 100)

    while True:
        #init
        push = ("https://ningishziddatao@"+url_list[position][8:])
        cwd = os.chdir(repo_list[position])

        #update
        #pad.refresh(offsetY ,offsetX, start_posY, start_posX ,end_posY, end_posX)
        pad2.refresh(offset ,0, spaceY,40 ,stdscrY-1, stdscrX-1)
        stdscr.hline(ord("_"), stdscrX)
        stdscr.refresh()
        curses.panel.update_panels()
        win1.clear()

        #display_info
        win1.box(0,ord("_"))
        win1.addstr(1,1,repo_list[position])
        win1.addstr(2,1, "current workig directory = "+os.getcwd())
        win1.addstr(3,1, "push = "+push)
        #win1.addstr(2,1, "cwd = "+repo_list[position])
        #win1.addstr(3,1, "repo path = "+os.getcwd()+repo_list[position])
        win1.refresh()

        #display_commands
        pad1 = curses.newpad(100,40)
        for_addstr(pad1, git_commands)
        stdscr.refresh()
        pad1.refresh(0,0, spaceY,6, stdscrY-1,30)

        #pad2_menu
        for i, x in enumerate(repo_list):
            if position == i:
                mod = curses.A_REVERSE
            else:
                mod = curses.A_NORMAL

            pad2.addstr(i, 0, x, mod)

        pad2.refresh(offset ,0, spaceY,40 ,stdscrY-1, stdscrX-1)
        #pad2.refresh(offset ,0, spaceY,stdscrX ,len(repo_list)+2,40+stdscr)
        stdscr.refresh()

        #controls
        key = pad2.getch()

        #pad2_down
        if key == ord("j") and position < len(repo_list)-1:
            position += 1
            if key == ord("j") and offset < len(git_commands)-pad2_length:
                offset +=1

        #pad2_up
        if key == ord("k") and position > -0:
            position -= 1
            if key == ord("k") and offset > 0:
                offset -=1

        #display_widge_name
        if key == 10:
            win1.erase()
            win1.addstr(git_commands[position])
            win1.refresh()

        if key == ord("q"):
            os.system("clear")
            break

        #options

        if key == ord("1"):
            display_terminal("git pull "+url_list[position])

        if key == ord("2"):
            display_terminal("git status")

        if key == ord("3"):
            display_terminal("git add -A")

        if key == ord("4"):
            display_terminal("git commit -m comment") 

        if key == ord("5"):
            display_terminal("git push "+push)

if __name__ == '__main__':
    curses.wrapper(main)

