import PySimpleGUI as sg
import string
from random import randint,choice


MAX_ROWS = MAX_COL = 10
LETRAS = list(string.ascii_uppercase)

sg.theme("DarkGreen7")
# sg.theme_previewer()

# -----------CUSTOM MODULES---------------------

def update_buttom_seleted(window,letter_target,button_target,active):
    window[event].update(button_color=('white','blue'))
    letter_target = letras_row[event]
    button_target = event
    active = True

def update_buttom_unselected(window,letter_target,button_target,active):
    window[event].update(button_color=('yellow','darkslategrey'))
    letter_target = ' ' 
    button_target = None
    active = False

# ----------------------------------------------



letras_row = [choice(LETRAS) for i in range(MAX_COL)]
row = [sg.Button(letras_row[i], size=(4, 2), key=i, pad=(0,0),button_color=('yellow','darkslategrey')) for i in range(MAX_COL)]


layout =  [
             [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)],
             [sg.Text('Porfavor seleccione una letra y haga click en un panel del tablero')],
             [row]
          ]

window = sg.Window('Minesweeper', layout)

# variables para controlar la seleccion de botones
button_target=None
letter_target=' '

ant = act = -1
active=False

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if type(event) == int:
        ant=act
        act=event
        if ant == act:
            if active == False:
                update_buttom_seleted(window,letter_target,button_target,active)
            else:
                update_buttom_unselected(window,letter_target,button_target,active)
        else:
            if ant != -1:
                window[ant].update(button_color=('yellow','darkslategrey'))
            window[event].update(button_color=('white','blue'))
            letter_target = letras_row[event]
            button_target = event
            active=True

    elif type(event) == tuple:
        if letter_target != ' ':
            window[event].update(letter_target, button_color=('white','black'))
            letter_target=' '
        if button_target != None:
            window[button_target].update(' ',button_color=('yellow','darkslategrey'),disabled=True)
window.close()