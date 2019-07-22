import tkinter as tk


def doorbell(event):
    print('You rang the Doorbell!')


window = tk.Tk()
window.title('Doorbell App')
window.geometry('300x200')
ring_button = tk.Button(window, text = 'Doorbell')
ring_button.grid(column=1, row=0)
ring_button.bind('<Button-1>', doorbell)
window.mainloop()

