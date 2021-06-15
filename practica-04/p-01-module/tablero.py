import filas as f
import PySimpleGUI as sg


MAX_ROWS = MAX_COL = 10
sg.theme("DarkGreen7")


layout =  [
             [[sg.Button(' ', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)],
             [sg.Text('Porfavor seleccione una letra y haga click en un panel del tablero')],
             [f.row]
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
                letter_target,button_target,active = f.update_buttom_seleted(window,event,f.letras_row)
            else:
                letter_target,button_target,active = f.update_buttom_unselected(window,event)
        else:
            if ant != -1:
                window[ant].update(button_color=('yellow','darkslategrey'))
            window[event].update(button_color=('white','blue'))
            letter_target = f.letras_row[event]
            button_target = event
            active=True

    elif type(event) == tuple:
        if letter_target != ' ':
            window[event].update(letter_target, button_color=('white','black'))
            letter_target=' '
        if button_target != None:
            window[button_target].update(' ',button_color=('yellow','darkslategrey'),disabled=True)
window.close()