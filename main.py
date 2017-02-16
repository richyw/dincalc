import re
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.carousel import Carousel
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from calc_skier_code import calc_skier_code
from calc_bsl_code import calc_bsl_code
from calc_din_setting import calc_din_setting

def calc_din_setting(weight,height,age,skier_type):
    """Calculate the din setting of the skier"""
    skier_code = calc_skier_code(weight,height,age,skier_type)
    bsl_code = calc_bsl_code(boot_length)
    din_setting = calc_din_setting(skier_code,bsl_code)
    return din_setting

class MainScreen(Screen):

    def getSkierType(self, skier_type):
        self.skier_type = skier_type

    def getBootLength(self, bsl):
        self.boot_length = bsl

    def getWeight(self, weight):
        self.weight = weight

    def getTall(self, tall):
        self.tall = tall

    def getAge(self, age):
        self.age = age

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
