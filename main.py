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
from kivy.properties import StringProperty
from kivy.clock import Clock
from din import calc_skier_code, calc_bsl_code, calc_din_setting
from din import feet_to_cm

class MainScreen(Screen):
    din_setting = StringProperty()
    def __init__(self, **kwargs):
        super(Screen,self).__init__(**kwargs)
        self.din_setting = ""

    def getSkierType(self, skier_type):
        self.skier_type = skier_type

    def getBootLength(self, bsl):
        self.boot_length = bsl

    def getWeight(self, weight):
        self.weight = weight

    def getTall(self, tall):
        self.tall = tall

    def getFeet(self,feet):
        self.feet = feet

    def getInch(self,inch):
        self.inch = inch

    def getAge(self, age):
        self.age = age

    def calculate_din(self):
        """Calculate the din setting of the skier"""
        try:
            self.tall = feet_to_cm(self.feet,self.inch)
            skier_code = calc_skier_code(self.weight,self.tall,self.age,self.skier_type)
            bsl_code = calc_bsl_code(self.boot_length)
        except AttributeError:
            pass
        else:
            din = calc_din_setting(skier_code,bsl_code)
            self.din_setting = str(din)

    #event = Clock.schedule_interval(calculate_din, 1 / 30.)

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
