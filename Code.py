from tkinter.ttk import*
from tkinter import*
from tkinter import messagebox
import datetime
import winsound
window=Tk()
window.title("Alarm Clock")
window.geometry("350x150")
frameline=Frame(window,width=400,height=5,bg="#98FF98").grid(row=0,column=0)
framebody=Frame(window,width=400,height=290,bg="white").grid(row=1,column=0)
img=PhotoImage(file="./clock.png")
l1=Label(framebody,image=img,height=100,bg="white")
l1.place(x=10,y=10)
name=Label(framebody,text="Alarm",height=1,font="Ivy 18 bold",fg="black",bg="white")
name.place(x=125,y=10)
def alarm():
    if(c_period.get()=="AM"):
        x=int(c_hour.get())
        y=int(c_min.get())
        z=int(c_sec.get())
    if(c_period.get()=="PM"):
        x=int(c_hour.get())+12
        y=int(c_min.get())
        z=int(c_sec.get())
    messagebox.showinfo("notification","alarm has been set")
    while(True):
        if(x==datetime.datetime.now().hour and y==datetime.datetime.now().minute and z==datetime.datetime.now().second):
            for i in range(0,100):
                winsound.Beep(1000,100)
            messagebox.showinfo("notification","WAKE UP")
            break
hour=Label(framebody,text="hour",height=1,font="Ivy 10 bold",fg="blue",bg="white")
hour.place(x=127,y=40)
c_hour=Combobox(framebody,width=2,font="Arial 15")
c_hour['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=58)
min=Label(framebody,text="min",height=1,font="Ivy 10 bold",fg="blue",bg="white")
min.place(x=177,y=40)
c_min=Combobox(framebody,width=2,font="Arial 15")
c_min['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_min.current(0)
c_min.place(x=180,y=58)
sec=Label(framebody,text="sec",height=1,font="Ivy 10 bold",fg="blue",bg="white")
sec.place(x=227,y=40)
c_sec=Combobox(framebody,width=2,font="Arial 15")
c_sec['values']=("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
c_sec.current(0)
c_sec.place(x=230,y=58)
period=Label(framebody,text="period",height=1,font="Ivy 10 bold",fg="blue",bg="white")
period.place(x=277,y=40)
c_period=Combobox(framebody,width=3,font="Arial 15")
c_period['values']=("AM","PM")
c_period.current(0)
c_period.place(x=280,y=58)
set=Button(framebody,text="Set Alarm",height=2,font="Arial 10",fg="red",bg="white",command=alarm)
set.place(x=220,y=100)

window.mainloop()