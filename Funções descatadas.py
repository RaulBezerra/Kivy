
#RASCUNHO
#DENTRO DA CLASSE MAINAPP
def on_motion(self, etype, motionevent):
    # will receive all motion events.
    print(f'etype: {etype}')
    print(f'motionevent: {motionevent}')
    pass

def mouse_pos(self, window, pos):
    print(f'w: {pos[0] / window.width}')
    print(f'h: {pos[1] / window.height}')

def on_mouse_up(self, window, x, y, botao, lista_teclas):
    #lista_teclas: lista de teclas ativas no moomento do click como 'shift' 'numlock'
    x_hint = x/ window.width
    y_hint = y/ window.height

    print(f'w: {x_hint}')
    print(f'h: {y_hint}')