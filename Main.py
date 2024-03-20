import PySimpleGUI as sg

def salva_dati(linguaggio, sistema_operativo):
    file = open("dati.txt", "a")
    file.write(f"Linguaggio: {linguaggio}, Sistema operativo: {sistema_operativo}\n")
    sg.popup("Grazie per aver risposto alle domande. Le tue risposte sono state registrate.")

layout = [
    [sg.Text("Qual è il tuo linguaggio di programmazione preferito?")],
    [sg.InputText(key="linguaggio")],
    [sg.Text("Quale sistema operativo preferisci?")],
    [sg.Radio("Windows", "sistema_operativo", key="windows"), sg.Radio("macOS", "sistema_operativo", key="macos")],
    [sg.Button("Salva")]
]

window = sg.Window("Questionario", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Salva":
        linguaggio = values["linguaggio"]
        sistema_operativo = "Windows" if values["windows"] else "macOS"
        salva_dati(linguaggio, sistema_operativo)

window.close()


