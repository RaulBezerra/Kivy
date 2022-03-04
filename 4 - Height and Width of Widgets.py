import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        #Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #Set columns
        self.cols = 1

        #Criando Segundo Grid
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #Nome ------------------------------
        #Add widgets
        self.top_grid.add_widget(Label(text='Nome: '))

        #Add Input Box
        self.nome = TextInput(multiline=False)
        self.top_grid.add_widget(self.nome)

        #PIZZA------------------------------
        # Add widgets
        self.top_grid.add_widget(Label(text='Pizza: '))

        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        # COR-------------------------------
        # Add widgets
        self.top_grid.add_widget(Label(text='Cor: '))

        # Add Input Box
        self.cor = TextInput(multiline=False)
        self.top_grid.add_widget(self.cor)
        ##################################

        #Add the new top_grid to our app
        self.add_widget(self.top_grid)

        #Create a Submit Button
        self.submit = Button(text='Submit', font_size= 32)

        #Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        nome = self.nome.text
        pizza = self.pizza.text
        cor = self.cor.text

        #Printa na tela
        self.add_widget(Label(text=f'Hello {nome}, you like {pizza}, your color is {cor} '))

        #Clear the input boxes
        self.nome.text=""
        self.pizza.text = ""
        self.cor.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()