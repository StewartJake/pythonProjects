import tkinter as tk
import webbrowser


def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/jacob-stewart-847933126/')


def github(event):
    webbrowser.open_new_tab('https://github.com/StewartJake')


window = tk.Tk()
window.title('Social Media Bookmarks')
window.geometry('300x200')
linkedin_btn = tk.Button(window, text='LinkedIn')
github_btn = tk.Button(window, text='Github')
linkedin_btn.grid(column=1, row=0)
github_btn.grid(column=1, row=1)
linkedin_btn.bind('<Button-1>', linkedin)
github_btn.bind('<Button-1>', github)
window.mainloop()

