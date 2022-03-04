import kivy
from kivy.app import App
from kivy.uix.widget import Widget


class Touch(Widget):

    def on_touch_down(self, touch):
        print('Mouse Down', touch.spos[0]) #Spos[0] = x, Spos[1] = y

    def on_touch_move(self, touch):
        print('Mouse Move', touch)

    def on_touch_up(self, touch):
        print('Mouse Up', touch)


class MyApp(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    MyApp().run()