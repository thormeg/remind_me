import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook

import requests


class TranslateBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Translation")
        self.geometry("500x300")

        self.menu = tk.Menu(self, bg="lightgrey", fg="black")

        self.languages_menu = tk.Menu(self.menu, tearoff=0, bg="lightgrey", fg="black")

        self.menu.add_cascade(label="Languages", menu=self.languages_menu)

        self.config(menu=self.menu)

        self.notebook = Notebook(self)

        english_tab = tk.Frame(self.notebook)
        french_tab = tk.Frame(self.notebook)

        self.french_translation = tk.StringVar(french_tab)
        self.french_translation.set("")

        self.translate_button = tk.Button(
            english_tab,
            text="Translate",
            command=lambda langs=["fr"], elems=[
                self.french_translation
            ]: self.translate(langs, None, elems),
        )
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.english_entry = tk.Text(english_tab, bg="white", fg="black")
        self.english_entry.pack(side=tk.TOP, expand=1)

        self.french_copy_button = tk.Button(
            french_tab, text="Copy to Clipboard", command=self.copy_to_clipboard
        )
        self.french_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.french_label = tk.Label(
            french_tab, textvar=self.french_translation, bg="lightgrey", fg="black"
        )
        self.french_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(english_tab, text="English")
        self.notebook.add(french_tab, text="French")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    def translate(self, target_languages=None, text=None, elements=None):
        if not text:
            text = self.english_entry.get(1.0, tk.END).strip()
        if not elements:
            elements = [self.french_translation]
        if not target_languages:
            target_languages = ["fr"]

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl={}&dt=t&q={}"

        try:
            for code, element in zip(target_languages, elements):
                full_url = url.format("en", code, text)
                r = requests.get(full_url)
                r.raise_for_status()
                translation = r.json()[0][0][0]
                element.set(translation)
        except Exception as e:
            msg.showerror("Translation Failed", str(e))

    def copy_to_clipboard(self, text=None):
        if not text:
            text = self.french_translation.get()

        self.clipboard_clear()
        self.clipboard_append(text)


if __name__ == "__main__":
    translatebook = TranslateBook()
    translatebook.mainloop()
