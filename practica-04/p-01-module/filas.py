import PySimpleGUI as sg
import string
from random import choice
MAX_COL = 10
LETRAS = list(string.ascii_uppercase)
# -----------CUSTOM MODULES---------------------
def update_buttom_seleted(window,event,letras_row):
    # ,letter_target,button_target,active
    window[event].update(button_color=('white','blue'))
    # letter_target = letras_row[event]
    # button_target = event
    # active = True
    return letras_row[event],event,True

def update_buttom_unselected(window,event):
    # ,letter_target,button_target,active
    window[event].update(button_color=('yellow','darkslategrey'))
    # letter_target = ' ' 
    # button_target = None
    # active = False
    return ' ',None,False
# ----------------------------------------------
letras_row = [choice(LETRAS) for i in range(MAX_COL)]
row = [sg.Button(letras_row[i], size=(4, 2), key=i, pad=(0,0),button_color=('yellow','darkslategrey')) for i in range(MAX_COL)]
# SECCION DE PRUEBAS PARA ESTE MODULO
if __name__ == '__main__':
    layout =  [ [row] ]
    window = sg.Window('prueba de filas', layout)
    # variables para controlar la seleccion de botones
    button_target,letter_target,active=None,' ',False
    ant = act = -1
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if type(event) == int:
            ant=act
            act=event
            if ant == act:
                if active == False:
                    letter_target,button_target,active = update_buttom_seleted(window,event,letras_row)
                else:
                    letter_target,button_target,active = update_buttom_unselected(window,event)
            else:
                if ant != -1:
                    window[ant].update(button_color=('yellow','darkslategrey'))
                window[event].update(button_color=('white','blue'))
                letter_target = letras_row[event]
                button_target = event
                active=True

    window.close()