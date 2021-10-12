#library
from scilab import scilab as sci

from tkinter import *
from tkinter import ttk
from math import *
#window's properties
root = Tk()
root.iconbitmap('Calculator.ico')
root.title('Calculadora de Sistemas de ecuaciones')
root.resizable(0,0)
root.geometry("720x420")
#extra settings
root.config()

style = ttk.Style(root)
style.theme_use("winnative")
#end window's properties
 
frame = Frame(root)
print ('hello world')

root.mainloop()
