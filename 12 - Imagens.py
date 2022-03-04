from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.uix.image import Image

Builder.load_file('kvs/imagens.kv')

class MyGridLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1) #Deixa o fundo branco
        return MyGridLayout()

if __name__ == '__main__':
    AwesomeApp().run()