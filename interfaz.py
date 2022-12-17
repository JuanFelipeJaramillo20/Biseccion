import tkinter as tk
from tkinter import ttk
import biseccion as bis
from matplotlib import pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

def biseccion():
    functiontxt = functionent.get()
    interval=[int(aent.get()), int(bent.get())]
    error = float(errorent.get())
    def f(x):
        f = eval(functiontxt)
        return f
    res = bis.bisection(f, interval, error)
    raizReslbl.configure(text=res[2])
    iteracionesReslbl.configure(text=res[1])
    iteracionescalculadasreslbl.configure(text=res[0])
    print(res)

    
    xpoint = [res[2]]
    ypoint = [0]
    x = np.linspace(interval[0] -1,interval[1] + 1,200)
    plt.plot(x, bis.functionTest(x), color='red')
    plt.plot(xpoint, ypoint, marker="o", markersize=10, markeredgecolor="red")
    plt.show()





app = tk.Tk()
app.title("Cálculo de raíces por medio de método de bisección")
app.geometry("600x250")

content = ttk.Frame(app)
#frame = ttk.Frame(content, borderwidth= 5, relief= "ridge", width = 200, height = 100)
funcLbl = ttk.Label(content, text ="Función: ")
functionent = ttk.Entry(content)
albl = ttk.Label(content, text ="a: ")
aent = ttk.Entry(content)
blbl = ttk.Label(content, text ="b: ")
bent = ttk.Entry(content)
errorlbl = ttk.Label(content, text ="Error: ")
errorent = ttk.Entry(content)
raizlbl = ttk.Label(content, text ="Raiz: ")
iteracioneslbl = ttk.Label(content, text ="Nº Iteraciones reales: ")
calcularbtn = ttk.Button(content, text ="Calcular", command=biseccion)
raizReslbl = ttk.Label(content, text ="0")
iteracionesReslbl = ttk.Label(content, text ="0")
iteracionescalculadaslbl = ttk.Label(content, text ="Nº Iteraciones calculadas: ")
iteracionescalculadasreslbl = ttk.Label(content, text ="0")

content.grid(column=0, row=0)
funcLbl.grid(column=0, row=0, padx=5, pady=5)
functionent.grid(column=1, row=0, padx=5, pady=5)
albl.grid(column=0, row=1, padx=5, pady=5)
aent.grid(column=1, row=1, padx=5, pady=5)
blbl.grid(column=2, row=1, padx=5, pady=5)
bent.grid(column=3, row=1, padx=5, pady=5)
errorlbl.grid(column=0, row=2, padx=5, pady=5)
errorent.grid(column=1, row=2, padx=5, pady=5)
calcularbtn.grid(column=4, row=3, padx=5, pady=5)
raizlbl.grid(column=0, row=4, padx=5, pady=5)
raizReslbl.grid(column=1, row=4, padx=5, pady=5)
iteracioneslbl.grid(column=2, row=4, padx=5, pady=5)
iteracionesReslbl.grid(column=3, row=4, padx=5,pady = 5)
iteracionescalculadaslbl.grid(column=2, row=5, padx=5,pady = 5)
iteracionescalculadasreslbl.grid(column=3, row=5, padx=5,pady = 5)
app.mainloop()
