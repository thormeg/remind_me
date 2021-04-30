from datetime import date
import json

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hello = tk.Button(self)
        self.hello["text"] = "Hello World\n(click me)"
        self.hello["command"] = self.say_hi
        self.hello.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hello, World!")
