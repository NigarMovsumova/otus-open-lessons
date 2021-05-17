from tkinter import *
from tkinter import messagebox
import requests


def create_labels(symbols):
    for symbol in symbols:
        response = requests.get(
            f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&type=stock&outputsize=1'
            f'&format=JSON&dp=4&timezone=Asia/Baku&apikey=221481cc802c42d8abe9b77a00297f2d')
        datetime = response.json()['values'][0]['datetime']
        close_price = response.json()['values'][0]['close']
        label = Label(root_window, font=('Arial', 25),
                      text=symbol + ': ' + close_price + "   " + datetime)
        label.pack()


def change_email_address(new_email):
    f = open("email", "w")
    f.write(new_email)
    f.close()
    messagebox.showinfo("Success", "Email is changed to " + new_email)


root_window = Tk()
root_window.title("Trader App")
root_window.geometry('800x800')

symbols = ['GOOG', 'SC/BNB', 'AAPL', '0xBTC/ETH']
create_labels(symbols)

entry = Entry(borderwidth=5)
entry.pack()

button = Button(text='Change email address', command=lambda: change_email_address(entry.get()))
button.pack()

root_window.mainloop()
