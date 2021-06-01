import tkinter as tk
from tkinter import filedialog, Text

import os
from tkinter.constants import X, Y

root = tk.Tk()


def addFile(label):
    filename = filedialog.askopenfilename(initialdir="./", title="select round file", filetypes=(("comma seperated values", "*.csv"),("All files", "*.*")))
    label['text'] = filename


canvas = tk.Canvas(root, height=700, width=700)
canvas.grid(row=0, column=0)
canvas.configure(background="black")


frame = tk.Frame(root, bg="white")
frame.grid(column=0, row=0)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


roundOneFile = tk.Button(frame, text="Open Round one File", padx=10, pady=7, fg="blue", bg="white", command= lambda: addFile(roundOneLabel))
roundOneFile.grid(column=0, row=0)

roundOneLabel = tk.Label(frame)
roundOneLabel.grid(column=1, row=0)

roundTwoFile = tk.Button(frame, text="Open Round two File", padx=10, pady=7, fg="blue", bg="white", command=lambda : addFile(roundTwoLabel))
roundTwoFile.grid(column=0, row=1)

roundTwoLabel = tk.Label(frame)
roundTwoLabel.grid(column=1, row=1)

# roundOneFile.pack()
# roundOneLabel.pack()

root.mainloop()
