import PySimpleGUI as sg

# le da un estilo de color diferente
sg.theme("DarkAmber")

# layout contiene todas
# las cosas que estan en tu ventana
layout = [  [sg.Text('algo de texto en la fila 1')],
            [sg.Text('algo de texto en la fila 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Creando una ventana
window = sg.Window('titulo de ventana', layout)
# loop de evento para procesar "eventos" y obtener los valores de las entradas
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('Ingresaste ', values[0])

window.close()