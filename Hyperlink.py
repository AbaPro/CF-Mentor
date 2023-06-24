import webbrowser
import tkinter as ttk

class Hyperlink(ttk.Label):
    def __init__(self, master, url, text, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.url = url
        self.text = text
        self.configure(text=self.text, foreground="blue", cursor="hand2")
        self.bind("<Button-1>", self.callback)
    def callback(self, event):
        webbrowser.open_new(self.url)
    def change_url(hyperlink, new_url):
        hyperlink.url = new_url
        hyperlink.configure(text=hyperlink.text)