import tkinter as tk
window = tk.Tk()
window.title("My first GUI")
window.geometry("300x200")
label1 = tk.Label(text="Vogon Poetry")
label1.grid(column=0,row=0)
window.mainloop()
