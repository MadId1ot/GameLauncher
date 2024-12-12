import os
import webbrowser
import time
import customtkinter
customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("215x40")
app.resizable(False, False)
app.title("Launch")

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

games = {
    'Rainbow 6 Siege': {
        'type': 'link',
        'location': 'steam://rungameid/359550'
    },
    'Counter Strike 2': {
        'type': 'link',
        'location': 'steam://rungameid/730'
    },
    'Apex Legends': {
        'type': 'link',
        'location': 'steam://rungameid/1172470'
    },
    'Valorant': {
        'type': 'command',
        'location': r'C:\"Riot Games"\"Riot Client"\RiotClientServices.exe --launch-product=valorant --launch-patchline=live'
    },
    'Deadlock': {
        'type': 'link',
        'location': 'steam://rungameid/1422450'
    },
    'Fortnite': {
        'type': 'link',
        'location': 'com.epicgames.launcher://apps/fn%3A4fe75bbc5a674f4f9b356b5c90567da5%3AFortnite?action=launch&silent=true'
    },
    'Geometry Dash': {
        'type': 'link',
        'location': 'steam://rungameid/322170'
    },
    'Portal': {
        'type': 'link',
        'location': 'steam://rungameid/400'
    },
}

def button_event():
    if games[menu_var.get()]['type'] == 'link':
        webbrowser.open(games[menu_var.get()]['location'])
    else:
        os.system(games[menu_var.get()]['location'])

menu_var = customtkinter.StringVar(value="Rainbow 6 Siege")
menu = customtkinter.CTkOptionMenu(app,values=[i for i in games], variable=menu_var)
menu.grid(row=0, column=0, padx=5, pady=5)

button = customtkinter.CTkButton(app, text="Launch", command=button_event, width=60)
button.grid(row=0, column=1, padx=0, pady=5)

app.mainloop()

