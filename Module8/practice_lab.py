'''Practice Lab: Building a GUI with Tkinter'''
import tkinter as tk

class GUI:
    '''Main application window class'''
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.mainloop()

app = GUI()
