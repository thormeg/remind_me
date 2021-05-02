from datetime import datetime
import json
import tkinter as tk
import tkinter.ttk as ttk

from remind_me.json_parser import JsonParser
from remind_me.utils import calculate_days as cd


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.jp = JsonParser()
        self.data = self.jp.read()

        self.title("My Reminders")
        self.configure(bg="white")
        self.geometry("680x680")

        self.parent = tk.Frame(self)
        self.create_grid_widgets()

        self.parent.grid()

    def build_notification_list(self, k, notification_list, i):
        bgc = "#e54624" if i & 1 == 1 else "#40bf77"
        self.key = tk.Label(self, bg="white", fg=bgc)
        self.key["text"] = k
        self.key.grid(column=0, row=i, padx=10, pady=5, sticky=tk.W)

        self.value = tk.Label(self, bg="white", fg=bgc)
        self.value["text"] = notification_list[k]
        self.value.grid(column=1, row=i, padx=10, pady=5, sticky=tk.E)

    def build_no_notifications(self):
        self.title = tk.Label(self, bg="white")
        self.title["text"] = "No events this time!"
        self.title.grid(column=0, row=1, padx=10, pady=5, sticky=tk.N)

    def create_grid_widgets(self):
        self.title = tk.Label(self, bg="white")
        self.title["text"] = "My upcoming events:"
        self.title.grid(column=0, row=0, padx=10, pady=5, sticky=tk.N)

        notification_list = self.calculate_notifications()

        i = 1
        if not notification_list:
            self.build_no_notifications()
        else:
            for k in notification_list.keys():
                self.build_notification_list(k, notification_list, i)
                i += 1

        # Dates entry box
        self.dates_entry = tk.Text(
            self.parent, bg="white", fg="black", height=5, width=50, relief="flat", bd=0
        )

        self.dates_entry.grid(
            column=1, row=i, padx=10, pady=15, rowspan=2, columnspan=5
        )
        self.populate_text_area()

        self.save_dates = tk.Button(
            self.parent, bg="white", text="Save", command=self.save_dates
        )
        self.save_dates.grid(column=1, row=i+2, pady=10, padx=10, sticky=tk.S)

        # Quit button
        self.quit = tk.Button(
            self, text="Quit", fg="red", bg="white", command=self.destroy
        )
        self.quit.grid(column=0, row=i + 2, pady=10, sticky=tk.S)

    def save_dates(self):
        text = self.dates_entry.get(1.0, tk.END).strip()
        new_list = text.split("\n")

        for line in new_list:
            date_portion = line[0:11]
            string_portion = line[12:]
            self.data[date_portion] = string_portion

        self.jp.write(self.data)

    def calculate_notifications(self):
        start = 1
        end = 15
        today = datetime.now()

        total_days = cd.days_in_month(today)
        if str(today.date().day) != 1:
            start = 16
            end = total_days

        dates_in_range = {}
        for date, string in self.data.items():
            dt = cd.format_date(date)
            if dt.month == today.month:
                if dt.day >= start and dt.day <= end:
                    dates_in_range[date] = string

        return dates_in_range

    def populate_text_area(self):
        for k, v in self.data.items():
            self.dates_entry.insert(tk.INSERT, f"{k} {v}\n")
