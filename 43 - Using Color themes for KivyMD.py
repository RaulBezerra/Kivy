from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton

from kivymd.uix.button import MDIconButton
from kivy.core.window import Window
#from kivymd.uix.filemanager import MDFileManager

# ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’,
# ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’,
# ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’,
# ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’,
# ‘Brown’, ‘Gray’, ‘BlueGray’.

tema = 'Dark'

class MainApp(MDApp):

    def light(self):
        global tema
        tema = 'Light'
        self.theme_cls.theme_style = tema

    def dark(self):
        global tema
        tema = 'Dark'
        self.theme_cls.theme_style = tema

    def build(self):
        print(self)
        self.theme_cls.theme_style = tema
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        #return Builder.load_file('kvs/color_theme.kv')
        return Builder.load_string('''
Screen:

    MDRectangleFlatButton:
        text: "Light Button"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_light
        on_press: app.light()


    MDRaisedButton:
        text: "Primary Button"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}


    MDRaisedButton:
        text: "Dark Button"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        md_bg_color: app.theme_cls.primary_dark
        on_press: app.dark()

        ''')

MainApp().run()