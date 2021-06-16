# Diagrame una interfaz en PySimpleGUI que permita ingresar dos datos:
# temperatura y humedad, junto con la fecha y hora actual. Al presionar
# Añadir , deberá cargar los valores en una lista (Listbox). Añada un botón,
# que permita guardar esta información en un archivo en formato json.
import json
import PySimpleGUI as sg
from random import randint
sg.ChangeLookAndFeel('DarkGreen')      

lista_temperaturas=[]

# Column layout      
col2 = [
        [ sg.Text('Humedad', text_color='white', background_color='Green'), sg.Input('',key='hum',size=(15,20),do_not_clear=False) ]
      ]

col1 = [
        [ sg.Text('Temperatura', text_color='white', background_color='Green'), sg.Input('',key='temp',size=(18,20),do_not_clear=False) ]
      ]


layout = [
            [sg.Column(col1, background_color='Green'), sg.Column(col2, background_color='Green'),sg.Button('Generar',key='generar')],
            [sg.Listbox(values=['Ingrese temperaturas'], size=(50, 6),key='listaTemperaturas')], 
            [sg.Exit(),sg.Button('Guardar' ,key='guardar'),sg.Button('Agregar' ,key='agregar')]
        ]      


window = sg.Window('Temp&Hum', layout)


# Display the Window and get values    
while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == 'guardar':
        dic={}
        for item in lista_temperaturas:
            tempe,sep,hume = item.partition(',')
            dic['temperatura'] = tempe
            dic['humedad'] = hume
        with open('temperaturas.txt', 'w') as outfile:
            json.dump(dic, outfile)
    if event == 'agregar':
        lista_temperaturas.append('Temperatura: {0}, Humedad: {1}'.format(values['temp'],values['hum']))
        window['listaTemperaturas'].update(values=lista_temperaturas)
    if event == 'generar':
        temp=randint(0,40)
        hum=randint(5,100)
        window['hum'].update(str(hum)+' %')
        window['temp'].update(str(temp)+' °C')
window.close()