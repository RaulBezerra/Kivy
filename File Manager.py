from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager

KV = """
MDScreen:

    MDToolbar:
        title: 'MDFileManager'
        pos_hint: {"top": 1}

    MDRoundFlatIconButton:
        text: 'Open manager'
        icon: 'folder'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.file_manager_open()
"""


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            preview=True
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        self.path= 'nada'
        #print(self.path)
        self.file_manager.show("/")  # output manager to the screen
        self.manager_open = True


    def select_path(self, path):
        """It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        """
        self.path = path
        self.exit_manager()

        return
    def exit_manager(self, *args):
        """Called when the user reaches the root of the directory tree."""
        #print(self.path)
        self.manager_open = False
        self.file_manager.close()


Example().run()
