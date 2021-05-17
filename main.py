from tkinter import *
from tkinter import messagebox
import requests

sample_list = []
root_window = Tk()
root_window.title("Investment App")
root_window.geometry('800x800')


def create_labels(names):
    for name in names:
        response = requests.get(
            f'https://api.twelvedata.com/time_series?symbol={name}&interval=1min&type=stock&outputsize=2'
            f'&format=JSON&dp=4&timezone=Asia/Baku&apikey=221481cc802c42d8abe9b77a00297f2d')
        label = Label(root_window, font=("Arial", 25), text=name + ':' + response.json()['values'][0]['close'])
        label.pack()
        sample_list.append(label)


def change_email(new_email):
    f = open("email", "w")
    f.write(new_email)
    f.close()
    messagebox.showinfo("Success", "Email is changed to " + new_email)


def get_email():
    f = open("email", "r")
    contents = f.read()
    print(contents)


entry = Entry()
entry.pack()
button = Button(text='Change email address', command=lambda: change_email(entry.get()))
button.pack()
names = ['GOOG', 'AAPL']
create_labels(names)

root_window.mainloop()
