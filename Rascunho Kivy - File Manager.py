from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
# from kivy.graphics import Color, Rectangle
# from kivy.uix.button import Button
# from kivy.app import App
# from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton

# from kivy.uix.widget import Widget
#
# from kivy.input import MotionEvent

from kivy.core.window import Window

from kivymd.uix.filemanager import MDFileManager

#Builder.load_file('Rascunho_telas/tela1.kv')

Builder.load_string(
    '''
<Tela1>: #TELA INICIAL

    MDRaisedButton:
        text: "Selecionar arquivo"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        md_bg_color: app.theme_cls.primary_dark
        on_release: app.selecionar_arquivo()
    '''

)

class marcador:
    def __init__(self):
        self.indice = 0
        self.tipo
        self.botao
        self.img_associada


class Tela1(Screen): #TELA INICIAL
	pass

class Tela2(Screen): #TELA DA PLANTA
	pass

class Tela3(Screen): #TELA DOS DETALHES
	pass


def eh_img(nome):
    resposta = False
    if nome is None:
        pass
    elif (nome[-4:] == '.png') or (nome[-4:] == '.jpg'):
        resposta = True
    return resposta

def get_fit (canvas_w, canvas_h, img_w, img_h):
    fit = 1
    if (img_h + 200) > img_w:
        fit = img_h/(canvas_h-200)
    else:
        fit = img_w/(canvas_w)
    return fit


class MainApp(MDApp):


    def __init__(self, **kwargs):



    #####Gerenciador de arquivos - INÍCIO#####
        super().__init__(**kwargs)
        self.manager_open = False
        self.file_manager = MDFileManager(exit_manager=self.exit_manager,
            select_path=self.select_path, preview = True)

    def file_manager_open(self):
        self.path = ''
        print(self.path)
        self.file_manager.show("C:/Users/Raul/Desktop/OneDrive/APP/Kivy")  # output manager to the screen
        #self.file_manager.show("/")
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
        self.manager_open = False
        self.file_manager.close()
        self.ir_tela2()

    #####Gerenciador de arquivos - FIM #####


    # Adiciona o marcador com base nos critérios
    def adicionar_marcador(self, x, y, cor):
        self.root.children[0].ids.tela2.add_widget(MDIconButton(  # CONFERIR SE CHILDREN[0] FUNCIONA SEMPRE
            icon='map-marker',
            pos_hint={"center_x": x, "center_y": y},
            theme_text_color='Custom',
            text_color=cor,
            on_press=lambda x: self.print_ok()
            )
        )

    def aceita_marcador(self):
        self.aceita = True

    def rejeita_marcador(self):
        self.aceita = False

    def define_tema_cor(self):

        tema = 'Dark'
        cor = 'Indigo'
        self.theme_cls.theme_style = tema
        self.theme_cls.primary_palette = cor

    def build(self): #Carrega Tela Inicial

        self.title = 'Inspektor'
        self.define_tema_cor()

        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(Tela1(name="tela1"))


        self.sm.add_widget(Tela3(name="tela3"))

        return self.sm

    def carregar_tela_2(self):
        Builder.load_file('Rascunho_telas/tela2.kv')
        self.sm.add_widget(Tela2(name="tela2"))

    def emite_alerta(self):
        self.alerta_img = MDDialog(
            title="Erro de formato!",
            text="Escolha uma imagem no formato .png ou .jpg!",
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, on_release=self.fecha_alerta
                ),
            ],
        )
        self.alerta_img.open()

    def fecha_alerta(self, obj): #obj não pode sair dessa função msm não sendo utilizado
        # Close alert box
        self.alerta_img.dismiss()

    def marcar(self, window, x, y, botao, lista_teclas):
        x_hint = x / window.width
        y_hint = 1 - y / window.height
        if self.aceita and botao=='left':
            self.adicionar_marcador(x_hint, y_hint, (0,0,1,1))

    def print_ok(self):
        print('ok')

    def print_ok2(self):
        print('ok2')

    def selecionar_arquivo(self):
        # self.arquivo_base = easygui.fileopenbox()
        # return self.arquivo_base
        self.file_manager_open()

    def ir_tela2(self):

        self.arquivo_base = self.path
        self.aceita = True

        if not eh_img(self.arquivo_base):
            if self.arquivo_base == '':
                pass
            else: #Emite alerta se não for .png ou .jpg
                self.emite_alerta()

        else: #Caso seja imagem:

            self.carregar_tela_2()
            self.sm.current = "tela2"

            Window.bind(on_mouse_up = self.marcar)


MainApp().run()

