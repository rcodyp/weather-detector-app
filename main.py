from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=1f2b95b915e7e13a3d8710f8407da772").json()
    label1.config(text=data["weather"][0]["main"])
    label2.config(text=data["weather"][0]["description"])
    label3.config(text=str(int(data["main"]["temp"]-273)))
    label4.config(text=data["main"]["pressure"])

win = Tk()
win.title("weather app")
win.config(bg = "grey")
win.geometry("500x700")
win.wm_attributes('-toolwindow', 'True')


city_name = StringVar()
state_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com =ttk.Combobox(win,value = state_name, 
                  font=("Comic"),textvariable=city_name)
com.place(x=25, y=120, height = 50 , width=450)

#search button
search_button = Button(win, text="search",font=("Comic",10),command=data_get)
search_button.place(x=200, y=220, height = 30 , width=50)

#label
label_1 = Label(win, text="weather climate:",font=("Comic",10),fg="black",bg="grey")
label_1.place(x=25, y=270, height = 30 , width=100)
label1 = Label(win, text="",font=("Comic",10),fg="black")
label1.place(x=250, y=270, height = 30 , width=150)

label_2 = Label(win, text="weather description:",font=("Comic",10),fg="black",bg="grey")
label_2.place(x=25, y=310, height = 30 , width=120)
label2 = Label(win, text="",font=("Comic",10),fg="black")
label2.place(x=250, y=310, height = 30 , width=150)

label_3 =  Label(win, text="temperature:",font=("Comic",10), fg="black",bg="grey")
label_3.place(x=25, y=350, height = 30 , width=79)
label3 =  Label(win, text="",font=("Comic",10), fg="black")
label3.place(x=250, y=350, height = 30 , width=150)

label_4 =  Label(win, text="pressure:",font=("Comic",10), fg="black",bg="grey")
label_4.place(x=27, y=390, height = 30 , width=55)
label4 =  Label(win, text="",font=("Comic",10), fg="black")
label4.place(x=250, y=390, height = 30 , width=150)






win.mainloop()