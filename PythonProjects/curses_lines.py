#nerate_pad_from_file_list_curses.py
import curses
import webbrowser as web
from curses import panel
from curses import wrapper

def main(stdscr):
    stdscr = curses.initscr()
    comment_list = ["#################################################"]
    main_list = ["#################################################"]
    curses.curs_set(0)
    pos = 0

    with open("") as reader:
        ls = reader.read().split("\n")
        for i in ls:
            if i.startswith("#"):
                comment_list.append(i)
            else:
                main_list.append(i)

    index_list = zip(comment_list, main_list)
    while True:

        pad1 = curses.newpad(100, 100)
        for i, x in enumerate(comment_list):
            if pos == i:
                mod = curses.A_REVERSE
            else:
                mod = curses.A_NORMAL
            pad1.addstr(i+2,2, str(i)+x, mod)
        pad1.refresh(0,0, 0,0, 20,40)

        key = pad1.getch()
        if key == ord("d"):
            pos +=1
        if key == ord("e"):
            pos -=1
        if key == 10:
            web.open(main_list[pos])
        if key == ord("q"):
            break

    curses.endwin()
    print index_list

wrapper(main)
