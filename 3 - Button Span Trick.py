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
        # Força as medidas para esse grid
        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        #Criando Segundo Grid
        self.top_grid = GridLayout(
            row_force_default=True, #Força as medidas para esse grid
            row_default_height=40,
            col_force_default=True,
            col_default_width=100,

        )
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
        self.submit = Button(text='Submit',
                             font_size= 28,
                             size_hint_y = None,
                             height=50,
                             size_hint_x= None,
                             width=120)

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