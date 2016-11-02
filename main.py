from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

class MainScreen(Screen):
    pass

class ChartScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file('dincalc.kv')

class DincalcApp(App):
    def build(self):
        carousel = Carousel(direction='right')
        return presentation

if __name__ == '__main__':
    DincalcApp().run()

#
