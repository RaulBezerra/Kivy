from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem

KV = """
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>:

    IconLeftWidget:
        icon: root.icon


MDScreen:

    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            adaptive_height: True

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: app.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
"""


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class Example(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.set_list_md_icons()

    def set_list_md_icons(self, text="", search=False):
        """Builds a list of icons for the screen MDIcons."""

        def add_icon_item(name_icon):
            self.root.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x,
                }
            )

        self.root.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)


Example().run()
