import tkinter as tk
import numpy as np


# Functions
def roll():
    rng = np.random.default_rng()
    new_val = rng.integers(1, 6)
    lbl_value["text"] = new_val


# Layout
window = tk.Tk()
window.title("Dice stimulator")
window.rowconfigure([0, 1], weight=1, minsize=100)
window.columnconfigure(0, weight=1, minsize=250)

btn_roll = tk.Button(master=window, text="Roll", command=roll)
lbl_value = tk.Label(master=window, text='1')

btn_roll.grid(row=0, column=0, sticky='ewns')
lbl_value.grid(row=1, column=0, sticky='ew')

window.mainloop()

