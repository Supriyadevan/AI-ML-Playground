#install PySimpleGUI

import PySimpleGUI as sg

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

def OuncestoMilli(Ounces):
   return (Ounces * 29.57353)

label1 = sg.Text("Enter Feet:    ")
label1input = sg.Input(key = "Feet")

label2 = sg.Text("Enter Inches: ")
label2input = sg.Input(key = "Inches")

add_button = sg.Button("Convert")
output_label = sg.Text("", key="Output")

window = sg.Window('Meter Convertor',
                   layout = [[label1,label1input],
                            [label2,label2input],
                            [add_button,output_label]])
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    print(event, values)

    EnteredFeet = float(values["Feet"])
    EnteredInches = float(values["Inches"])
    Result = convert(EnteredFeet, EnteredInches)

    window["Output"].update(value=f"{Result} m", text_color="white")

#OuncestoMilliliters

label3 = sg.Text("Enter Ounces: ")
label3Input = sg.Input(key = "Ounces")

label3button = sg.Button("Convert")
label3Output = sg.Text("", key = "ResultinMilli")

OunceWindow = sg.Window('OuncesConverter',
    layout = [[label3,label3Input,label3button,label3Output]])


while True:
    event2, values2 = OunceWindow.read()
    if event2 == sg.WINDOW_CLOSED:
        break

    print(event2,values2)
    Ounces = float(values2["Ounces"])
    MilliLiters = OuncestoMilli(Ounces)
    OunceWindow["ResultinMilli"].update(value=f"{MilliLiters} m", text_color="white")



window.close()









