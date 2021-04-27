from tkinter import Tk
from tkinter import messagebox
import sys

def error(errortext,stop):

    tk = Tk()
    tk.geometry("0x0")
    tk.iconbitmap('assets/img/logo/logo.ico')
    messagebox.showerror("Erreur", errortext)
    tk.destroy()
    if stop:
        sys.exit(0)