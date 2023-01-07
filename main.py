from tkinter import *
from tkinter import ttk
import requests 



def get_data():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=23d232e84ee0b9dcb771d9c5e356c75b").json()
    w_lab1.config(text=data["weather"][0]["main"])
    t_lab1.config(text=str(int(data["main"]["temp"]-273.15)))
    p_lab1.config(text=data["main"]["pressure"])






win=Tk()
city_name=StringVar()
win.title('weather--app')
win.config(bg='black')
win.geometry('600x500')

gg=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
name=Label(win,text='WEATHER',
                 font=('Andalé Mono',30),bg='black',fg='white')
name.place(x=100,y=40,height=40,width=400)
c=ttk.Combobox(win,text='WEATHER',values=gg,font=('Andalé Mono',18),textvariable=city_name)
c.place(x=75,y=100,height=35, width=450)


w_lab=Label(win,text='Weather-type--',
                 font=('Andalé Mono',16),bg='black',fg='white')
w_lab.place(x=100,y=220,height=45,width=150)
w_lab1=Label(win,text='',
                 font=('Andalé Mono',16),bg='black',fg='white')
w_lab1.place(x=300,y=220,height=45,width=150)



t_lab=Label(win,text='Temperature--',
                 font=('Andalé Mono',16),bg='black',fg='white')
t_lab.place(x=100,y=280,height=45,width=150)
t_lab1=Label(win,text='',
                 font=('Andalé Mono',16),bg='black',fg='white')
t_lab1.place(x=300,y=280,height=45,width=150)



p_lab=Label(win,text='Pressure--',
                 font=('Andalé Mono',16),bg='black',fg='white')
p_lab.place(x=100,y=340,height=45,width=150)
p_lab1=Label(win,text='',
                 font=('Andalé Mono',16),bg='black',fg='white')
p_lab1.place(x=300,y=340,height=45,width=150)





butt=Button(win,text='DONE',
                 font=('Andalé Mono',16),bg='black',fg='white',command=get_data)
butt.place(x=450,y=150,height=35,width=70)






win.mainloop()
