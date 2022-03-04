# importing mdapp from kivymd framework
from kivymd.app import MDApp

# importing builder from kivy
from kivy.lang import Builder


# this is the main class which
# will render the whole application
class uiApp(MDApp):

    # method which will render our application
    def build(self):
        return Builder.load_string("""

MDBoxLayout:
    spacing:300
    MDIconButton:

        # name of mdicon
        icon:"language-python"                          
        pos_hint: {"center_x": .5, "center_y": .5}
        user_font_size: "64sp"

        # bgcolor of iconbutton
        md_bg_color:[1,1,0,1]                           

    MDIconButton:

        # custom image as mdicon
        icon:"Imagens/indicador1.png"                                  
        pos_hint: {"center_x": .5, "center_y": .5}
        #user_font_size: "16sp"

    MDIconButton:

        icon:"language-python"
        pos_hint: {"center_x": .5, "center_y": .5}
        text_icon_color: .2, .2, .2, 1

                                   """)


# running the application
uiApp().run()