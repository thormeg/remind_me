from datetime import datetime
import json
import tkinter as tk
from tkinter.ttk import *

from remind_me.json_parser import JsonParser 

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        jp = JsonParser()
        self.data = jp.read()

        self.title("My Reminders")
        self.configure(bg='white')
        self.geometry("680x680")

        self.parent = tk.Frame(self)
        self.create_grid_widgets(self.data)

        self.parent.grid()

    def donothing(self):
        x = 0

    
    def create_grid_widgets(self, data):
        self.title = tk.Label(self, bg='white')
        self.title["text"] = 'My upcoming events:'
        self.title.grid(column=0, row=0, padx=10, pady=5, sticky=tk.N)
        
        # Build date list
        i = 1
        for k in data.keys():
            bgc = '#e54624' if i & 1 == 1 else '#40bf77'
            self.key = tk.Label(self, bg='white', fg=bgc)
            self.key["text"] = k
            self.key.grid(column=0, row=i, padx=10, pady=5, sticky=tk.W)

            self.value = tk.Label(self, bg='white', fg=bgc)
            self.value["text"] = data[k]
            self.value.grid(column=1, row=i, padx=10, pady=5, sticky=tk.E)
    
            i += 1

        # Dates entry box
        self.dates_entry = tk.Text(self.parent, bg="white", fg="black", height=5, width=50, relief="flat")
        self.dates_entry.grid(column=1, row=i, padx=10, pady=5, rowspan=2, columnspan=5, sticky=tk.S)
        self.save_dates = tk.Button(self.parent, bg='white',
                                          text="Save",
                                          command=self.save_dates)
        self.save_dates.grid(pady=10, padx=10, sticky=tk.S)

        # Quit button
        self.quit = tk.Button(self, text="Quit", fg="red", bg='white', command=self.destroy)
        self.quit.grid(column=1, row=i, pady=10, sticky=tk.S)


    def save_dates(self):
        text = self.dates_entry.get(1.0, tk.END).strip()
        print(text)
        print(type(text))


    def edit_dates(self):
        pass
    #     self.dates_entry = tk.Text(self.parent, bg="white", fg="black")
    #     self.dates_entry.grid(column=1, row=3, padx=100, pady=5, rowspan=3, columnspan=3, sticky=tk.S)
    #     print(self.data)
