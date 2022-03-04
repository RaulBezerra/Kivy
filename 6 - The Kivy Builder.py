from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('aula6.kv')
'''
Builder.load_string("""
<MyGridLayout>

    nome: nome
    pizza: pizza
    cor: cor

    GridLayout:
        cols:1
        size: root.width, root.height

        GridLayout:
            cols:2

            Label:
                text: 'Nome'
            TextInput:
                id: nome
                multiline: False

            Label:
                text: 'Favourite Pizza'
            TextInput:
                id: pizza
                multiline: False

            Label:
                text: 'Cor'
            TextInput:
                id: cor
                multiline: False

        Button:
            text: "Submit"
            font_size: 32
            on_press: root.press()
""")
'''
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