'''Practice Lab: Building a GUI with Tkinter'''
import tkinter as tk

class GUI:
    '''Main application window class'''
    def __init__(self):
        self.main_window = tk.Tk()
        #Looked this up on geeks for geeks. I didn't like now small the default window was.
        self.main_window.geometry("640x480") 
        self.gallons_label = tk.Label(self.main_window, text="Gallons:")
        self.gallons_entry = tk.Entry(self.main_window)
        self.gallons_label.pack()
        self.gallons_entry.pack()
        self.miles_label = tk.Label(self.main_window, text="Miles:")
        self.miles_entry = tk.Entry(self.main_window)
        self.miles_label.pack()
        self.miles_entry.pack()
        self.main_window.mainloop()

app = GUI()
