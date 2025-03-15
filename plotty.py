from tkinter import *
import matplotlib.pyplot as plt, numpy as np, re

x = np.linspace(-2, 2, 100)

def plotting():
    try:
        func = e1.get()
        safe = re.sub(r'\b(sin|cos|tan|exp|log|sqrt|abs)\(', r'np.\1(', func)
        y = eval(safe, {"x": x, "np": np})
        fig = plt.figure(figsize = (10, 5))
        plt.plot(x, y)
        plt.show()
    except Exception as fuck:
        print(f"Oops! Python says: {fuck}")

master = Tk()
master.geometry("500x300")
w = Label(master, text='Visual Representation of a Function')
Label(master, text='Enter function formula', font=("Arial", 15)).grid(row=0)
e1 = Entry(master, font=("Arial", 18), width=30)
e1.grid(row=1, column=0, ipady=6)
Button(master, text="Go!", command=plotting,font=("Arial", 16)).grid(row=1, column=3, columnspan=3)
mainloop()
