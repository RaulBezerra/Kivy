from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivymd.app import MDApp

# Designate Our .kv design file
#Builder.load_file('kvs/menu.kv')


class MyLayout(Widget):
    Builder.load_string("""
<MyLayout>
    id: my_widget
    FloatLayout:

        #orientation: "vertical"
        size: root.width, root.height

        #padding: 50
        #spacing: 20

        Image:
            id: my_image
            source: ""
            size_hint: (0.4, 0.4)
            pos_hint: {"center_x":.5, "top":1}



        FileChooserIconView:
            id: filechooser
            on_selection: my_widget.selected(filechooser.selection)
            size_hint: (1, 0.4)
            pos_hint: {"center_x":0.5, "top":0.6}



        MDRaisedButton:
            text: "Selecionar Arquivo"
            font_size: 25
            size_hint: (0.3, 0.1)
            pos_hint: {"x":.7, "bottom":1}
            on_press: app.root.selecionar_arquivo()
    """)
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        # print(filename[0])
        except:
            pass

    def selecionar_arquivo(self):
        print(self.ids.my_image.source)


class AwesomeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()