#!/usr/bin/env python3
#print_position_kv.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(
"""
<Box>:

    Button:
        relative: True
        text: 'Middle'
        on_touch_down: print('Middle: {}'.format(args[1].pos))

""")
class Box(BoxLayout):
    pass

class main(App):
    def build(self):
        return Box()

if __name__ == '__main__':
    main().run()
