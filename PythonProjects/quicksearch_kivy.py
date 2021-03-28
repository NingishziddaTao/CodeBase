#!/usr/bin/env python3
#quicksearch_kivy.py
import webbrowser as webb
import pickle
import os

#os change workspace
os.system("wmctrl -s 0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config

#window config
Window.size = (500, 100)
Window.borderless = True
Window.left = 100 
Window.top = 800

import pickle 

class QuickSearch(GridLayout):
    """This app will take textinput and uses it to search on google or youtube
    use the arrow up and down key to choose search engine and press enter to
    close the app and start search"""

    def __init__(self, **kwargs):
        super(QuickSearch, self).__init__(**kwargs)
        self.cols = 1
        self.size = 1,1

        with open('/sda5/quicksearch_kivy.pkl', 'rb') as pklin:
            self.pkl_load = pickle.load(pklin)
            print(self.pkl_load)

        #objects
        self.labeltext = self.pkl_load
        #self.labeltext = "google"

        #label
        self.url_label = Label(text=self.labeltext, markup = True, font_size = '40sp',
                pos = (1, 4), size =[1,1])
        self.add_widget(self.url_label, index = 1 )

        #textinput 
        self.search_textinput = TextInput(multiline = False, font_size = '30sp')
        self.add_widget(self.search_textinput)
        self.search_textinput.focus = True

        Window.bind(on_key_down=self.key_action)

    def key_action(self, *args):
        """the kivy.core.window.window_sdl2.WindowSDL object takes keystrokes
        and turn them into a list of args then uses the output the create a key
        event*"""
        print ("got a key event: %s" % list(args)[2])

        #takes the third item of the kivy.core.window.window_sdl2.WindowSDLlist
        #object checks for key code of arrow down
        if list(args)[2] == 81:
        #Turn into google search when keypress is arrow dowh and changes label text
            print (self.search_textinput.text)
            self.labeltext = 'google'
            self.clear_widgets(children=[self.url_label])
            self.url_label = Label(text=self.labeltext, markup = True, font_size = '40sp', pos = (1, 4))
            self.add_widget(self.url_label, index = 1 )

            #pickle dump url_tuple[0]
            with open('/sda5/quicksearch_kivy.pkl', 'wb') as self.pklin:
                pickle.dump(self.labeltext, self.pklin)
                print("dumped google")

        #takes the third item of the kivy.core.window.window_sdl2.WindowSDLlist object
        #checks for key code of arrow down
        if list(args)[2] == 82: 
        #Turn into youtube search when keypress is arrow up and changes label
            print (self.search_textinput.text)
            self.labeltext = 'youtube'
            self.clear_widgets(children=[self.url_label])
            self.url_label = Label(text=self.labeltext, markup = True, font_size = '40sp', pos = (1, 4))
            self.add_widget(self.url_label, index = 1 )

            #pickle dump url_tuple[0]
            with open('/sda5/quicksearch_kivy.pkl', 'wb') as self.pklin:
                pickle.dump(self.labeltext, self.pklin)
                print("dumped youtube ")

        #This will search the input in on the google search engine and close the app
        if list(args)[2] == 40 and self.labeltext == 'google':
            print (self.search_textinput.text)
            self.search_textinput.focus = True
            webb.open("https://www.google.com/search?q="+self.search_textinput.text)
            MyApp().stop()

        #This will search the input in on the youtube search engine and close the app
        if list(args)[2] == 40 and self.labeltext == 'youtube':
            print (self.search_textinput.text)
            self.search_textinput.focus = True
            webb.open("https://www.youtube.com/results?search_query="+self.search_textinput.text)
            MyApp().stop()

class MyApp(App):
    def build(self):
        return QuickSearch()

if __name__ == '__main__':
    MyApp().run()
