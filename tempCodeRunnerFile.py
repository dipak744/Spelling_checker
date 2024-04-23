from textblob import TextBlob
from tkinter import *

def main_window():
    win = Tk()
    win.geometry("500*400")
    win.resizable(False,False)
    win.config(bg="Blue")
    win.title("Dipak Sah")
    
    label1 = Label(win,text="Incorrect Spelling",font=("Time New Roman", 25, "bold"), bg="Blue", fg="white")
    label1.place(x=100, y=20, height=50, width=300)
    
    
    win.mainloop()
    
    
main_window()
    