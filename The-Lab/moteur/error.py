from tkinter import Tk
from tkinter import messagebox


def error(errortext,stop):

    tk = Tk()
    tk.geometry("0x0")
    tk.iconbitmap('assets/img/logo/logo.ico')
    messagebox.showerror("Erreur", errortext)
    tk.destroy()
    if stop:
        exit(0)