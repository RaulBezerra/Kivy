from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('kvs/cores.kv')

class MyGridLayout(Widget):

    name =  ObjectProperty(None)
    pizza = ObjectProperty(None)
    cor = ObjectProperty(None)

    def press(self): #Removido instance
        nome = self.nome.text
        pizza = self.pizza.text
        cor = self.cor.text

        #Printa na tela
        #self.add_widget(Label(text=f'Hello {nome}, you like {pizza}, your color is {cor} '))
        print(f'Hello {nome}, you like {pizza}, your color is {cor} ')

        #Clear the input boxes
        self.nome.text=""
        self.pizza.text = ""
        self.cor.text = ""

class AwesomeApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    AwesomeApp().run()