from tkinter import*
window=Tk()

window.title("BIM Calculator")
window.geometry("800x800")
window.configure(bg='yellow')
app_label =Label(window, text= "BODY MASS INDEX Calculator", fg='black',bg='lightcyan', font=('Calibri',15),bd=5)
app_label.place(x=150,y=20)
name_label =Label(window, text= "Enter your name", fg='black',bg='lightcyan', font=('Calibri',15),bd=5)
name_label.place(x=50,y=100)

user_label =Entry(window, text= "Your Name", width=25,bd=17)
user_label.place(x=300,y=100)

height_label= Label(window,text="Enter Your height",font=('Calibri',15))
height_label.place(x=50,y=175)

height_entry= Entry(window,text="Your height",width=25,bd=17)
height_entry.place(x=300,y=175)

weight_label= Label(window,text="Enter Your weight",font=('Calibri',15))
weight_label.place(x=50,y=225)

weight_entry= Entry(window,text="Your weight",width=25,bd=17)
weight_entry.place(x=300,y=225)

result_frame = LabelFrame(window , text= "Result", bg='pink',font=('Calibri',20))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=300)
result_label = Label(result_frame, text= " ", bg='lightcyan', font=('Calibri',25),width=25)
result_label.place(x=20,y=20)
result_label.pack()

def calculate():
    weight=int(weight_entry.get())
    height=int(height_entry.get())/100
    bmi=weight/(height*height)
    bmi= round(bmi,1)
    result_label.destroy()
    msg=""
    if bmi<18.5:
        msg="You are under weight"
    elif bmi>18.5 and bmi<24.9:
        msg="You are normal"
    elif bmi>25 and bmi<29.9:
        msg="You are over weight"
    elif bmi>30:
        msg="You are obse"
    else:
        msg="some think went wrong"
        
    output_label = Label(result_frame, text= "Your BMI ="+str(bmi)+msg, bg='lightcyan', font=('Calibri',10),width=50)
    output_label.place(x=20,y=20)
    output_label.pack()
    
cButton = Button(window,text="Calculate",fg="black", bg='green', command=calculate)
cButton.place(x=20,y=250)
mainloop()