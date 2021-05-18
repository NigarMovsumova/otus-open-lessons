from tkinter import *
import requests
from mail_sending import send_email, change_email_address

labels = []
cycles = 0
symbols = ['GOOG', 'SC/BNB', 'AAPL']
prices = [2800, 0.0002, 126]
twelvedate_api_url = 'https://api.twelvedata.com/time_series?symbol={' \
                     '}&interval=1min&type=stock&outputsize=2&format=JSON&dp=4&timezone=Asia/Baku&apikey' \
                     '=221481cc802c42d8abe9b77a00297f2d'
label_text = '{datetime}    {symbol}:  {current_close_price}    {price_difference}'


def update_prices():
    global cycles
    counter = 0
    for symbol in symbols:
        response = requests.get(twelvedate_api_url.format(symbol))
        datetime = response.json()['values'][0]['datetime']
        current_close_price = float(response.json()['values'][0]['close'])
        previous_close_price = float(response.json()['values'][1]['close'])
        if current_close_price >= prices[counter]:
            send_email(symbol + ': ' + str(current_close_price) + "   " + datetime)

        price_difference = str(round(current_close_price - previous_close_price, 4))
        price_difference = f" { '' if current_close_price - previous_close_price < 0 else '+'}{price_difference}"
        # labels[counter].configure(text=datetime + "   " + symbol + ': ' + str(current_close_price) + "   "  +
        #                           "   " + price_difference)
        labels[counter].configure(text=label_text.format(datetime=datetime,
                                                         symbol=symbol,
                                                         current_close_price=current_close_price,
                                                         price_difference=price_difference))
        counter += 1

    root_window.after(60000, update_prices)


# def update_prices():
#     print('Обновление цен...')
#     print(datetime.today().strftime("%H:%M:%S"))
#     root_window.after(5000, update_prices)


def create_labels():
    global symbols
    for symbol in symbols:
        response = requests.get(twelvedate_api_url.format(symbol))
        print(response)
        datetime = response.json()['values'][0]['datetime']
        print(datetime)
        current_close_price = float(response.json()['values'][0]['close'])
        previous_close_price = float(response.json()['values'][1]['close'])
        price_difference = str(round(current_close_price - previous_close_price, 4))
        label = Label(root_window, font=('Arial', 25),
                      text=label_text.format(datetime=datetime,
                                             symbol=symbol,
                                             current_close_price=current_close_price,
                                             price_difference=price_difference))
        label.pack()
        labels.append(label)


root_window = Tk()
root_window.title("Trader App")
root_window.geometry('800x800')

create_labels()

entry = Entry(borderwidth=5)
entry.pack()

button = Button(text='Change email address', command=lambda: change_email_address(entry.get()),
                fg='blue', bg='red')
button.pack()

root_window.after(3, update_prices)
root_window.mainloop()
