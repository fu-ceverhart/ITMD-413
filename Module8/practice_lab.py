'''Practice Lab: Building a GUI with Tkinter'''
import tkinter as tk

class GUI:
    '''Main application window class'''
    def __init__(self):
        self.main_window = tk.Tk()
        self.gallons_label = tk.Label(self.main_window, text="Gallons:")
        self.gallons_entry = tk.Entry(self.main_window)
        self.gallons_label.pack()
        self.gallons_entry.pack()
        self.main_window.mainloop()

app = GUI()
