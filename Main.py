import PySimpleGUI as sg

def salva_dati(nome, cognome, linguaggio, sistema_operativo, console):
    file = open("dati.txt", "a")
    file.write(f"Nome: {nome}, Cognome: {cognome}, Linguaggio: {linguaggio}, Sistema operativo: {sistema_operativo}, Console: {', '.join(console)}\n")
    sg.popup("Grazie per aver risposto alle domande. Le tue risposte sono state registrate.")
    file.close()

layout = [
    [sg.Text("Nome"), sg.InputText(key="nome")],
    [sg.Text("Cognome"), sg.InputText(key="cognome")],
    [sg.Text("Qual è il tuo linguaggio di programmazione preferito?")],
    [sg.InputText(key="linguaggio")],
    [sg.Text("Quale sistema operativo preferisci?")],
    [sg.Radio("Windows", "sistema_operativo", key="windows"), sg.Radio("macOS", "sistema_operativo", key="macos")],
    [sg.Text("Qual'è la tua console preferita?")],
    [sg.Checkbox("Playstation", key="playstation"), sg.Checkbox("Xbox", key="xbox"), sg.Checkbox("Nintendo", key="nintendo")],
    [sg.Button("Salva")]
]

window = sg.Window("Questionario", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Salva":
        nome = values["nome"]
        cognome = values["cognome"]
        linguaggio = values["linguaggio"]
        sistema_operativo = "Windows" if values["windows"] else "macOS"
        console = [c for c in ["Playstation", "Xbox", "Nintendo"] if values[c.lower()]]
        salva_dati(nome, cognome, linguaggio, sistema_operativo, console)

window.close()
