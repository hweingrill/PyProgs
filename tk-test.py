import tkinter as tk

root = tk.Tk()

# Textausgabe erzeugen
label1 = tk.Label(root, text="Hallo Welt")

# in GUI Elemente einbetten
label1.pack(side="left")

# Grafik einbetten
bild1 = tk.PhotoImage(file="biene.png")
label2 = tk.Label(root, image=bild1).pack(side="right")

root.mainloop()
