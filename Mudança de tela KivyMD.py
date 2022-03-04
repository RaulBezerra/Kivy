from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder

Builder.load_file("kvs/telas.kv")


class Tela1(Screen):
    pass


class Tela2(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(Tela1(name="tela1"))
        self.sm.add_widget(Tela2(name="tela2"))
        return self.sm

    def change_screen(self, tela):
        self.sm.current = tela

if __name__ == "__main__":
    MainApp().run()