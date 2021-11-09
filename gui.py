"""
import tkinter

window = tkinter.Tk()
"""
from tkinter import *
import getdata

def run_gui(user_input):

    def search_button_func():
        print("You searched Data")
        new_text = stock_input.get()
        #stocks_label.config(text=new_text)

        result_data = getdata.get_data(new_text)
        
        name_label.config(text="Stock Name: "+result_data[0]['stock_name'])
        opening_label.config(text="Opening Price: "+result_data[0]['opening_price'])
        closing_label.config(text="Closing Price: "+result_data[0]['closing_price'])
        low_price_label.config(text="Low Price: "+result_data[0]['low_price'])
        high_price_label.config(text="High Price: "+result_data[0]['high_price'])
        volume_label.config(text="Volume: "+result_data[0]['volume'])

    window = Tk()

    window.title("Stocks API Search")

    window.minsize(width=750, height=500)
    window.config(padx=100, pady=100)

    #Label
    stocks_label = Label(text="Daily Stocks You are searching:", font=("Arial", 25, "bold"))
    #stocks_label.config(text="New Text")   
    stocks_label.grid(column=1, row=0)
    stocks_label.config(padx=25, pady=25)

    #Input
    stock_input = Entry()
    stock_input.grid(column=1, row=1)
    stocks_label.config(padx=25, pady=25)

    #Button
    search_button = Button(text="Search Stock", font=("Arial", 20, "bold"), command=search_button_func)
    search_button.grid(column=1, row=2)
    stocks_label.config(padx=25, pady=25)

    #Results Label name
    name_label = Label(text="", font=("Arial", 25, "bold")) 
    name_label.grid(column=2, row=0)
    name_label.config(padx=25, pady=25)

    #Results Label opening
    opening_label = Label(text="", font=("Arial", 25, "bold")) 
    opening_label.grid(column=2, row=1)
    opening_label.config(padx=25, pady=25)

    #Results closing
    closing_label = Label(text="", font=("Arial", 25, "bold")) 
    closing_label.grid(column=2, row=2)
    closing_label.config(padx=25, pady=25)

    #Results Label low price
    low_price_label = Label(text="", font=("Arial", 25, "bold")) 
    low_price_label.grid(column=2, row=3)
    low_price_label.config(padx=25, pady=25)

    #Results Label high
    high_price_label = Label(text="", font=("Arial", 25, "bold")) 
    high_price_label.grid(column=2, row=4)
    high_price_label.config(padx=25, pady=25)

    #Results Label volume
    volume_label = Label(text="", font=("Arial", 25, "bold")) 
    volume_label.grid(column=2, row=5)
    volume_label.config(padx=25, pady=25)



    window.mainloop()



