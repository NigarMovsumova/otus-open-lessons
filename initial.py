from tkinter import *

import requests
import json

root_window = Tk()
root_window.title("Investment App")
root_window.geometry('800x800')

apple_label = Label(root_window, fg="green", font=("Arial", 25), text='AAPL')
apple_label.pack()

google_label = Label(root_window, fg='red', font=("Arial", 25), text='GOOGL')
google_label.pack()

indonesian_rupiah = Label(root_window, fg='red', font=("Arial", 25), text='USD IDR :')
indonesian_rupiah.pack()

google_response = requests.get(
    'https://api.twelvedata.com/time_series?symbol=GOOG&interval=1min&type=stock&outputsize=2'
    '&format=JSON&dp=4&timezone=Asia/Baku&apikey=221481cc802c42d8abe9b77a00297f2d')

print(json.loads(google_response.text)['values'])

print(google_response.json()['values'][0]['close'])
# print(json.loads(google_response.text)['values'][0]['open'])
# print(json.loads(google_response.text)['values'][0]['close'])
# print(json.loads(google_response.text)['values'][0]['high'])
# print(json.loads(google_response.text)['values'][0]['low'])
#
apple_response = requests.get('https://api.twelvedata.com/time_series?symbol=AAPL&interval=1min&type=stock&outputsize'
                              '=1&format=JSON&dp=4&timezone=Asia/Baku&apikey=221481cc802c42d8abe9b77a00297f2d')

rupiah_response = requests.get('https://api.twelvedata.com/time_series?symbol=USD/IDR&interval=1min&outputsize=1'
                               '&format=JSON&dp=4&timezone=Europe/Moscow&apikey=221481cc802c42d8abe9b77a00297f2d')

# stock_prices['AAPL'] = google_response.json()['values'][0]['close']
# stock_prices['GOOGL'] = google_response.json()['values'][0]['close']

apple_label.config(text='GOOGL : ' + google_response.json()['values'][0]['close'])
google_label.configure(text='AAPL : ' + apple_response.json()['values'][0]['close'])
indonesian_rupiah.config(text='IDR : ' + rupiah_response.json()['values'][0]['close'])

# Создание десктопного приложения для анализа цен на фондовом рынке

root_window.mainloop()
