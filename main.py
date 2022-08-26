from cProfile import label
from email import message
from logging import root
from tkinter import *
from tkinter import messagebox
from unittest import result
from PIL import Image,ImageTk

# Head App

def on_closing():
    if messagebox.askokcancel('Exit', 'Do You want to exit the App?\n Values won`t  be saved'):
        root.destroy()

root = Tk()
root.protocol('WM_DELETE_WINDOW', on_closing)
root.title('BMI App')
root.geometry('1280x960')
root.resizable(width=False, height=False)
root.wm_attributes('-topmost', 1)
root['background']='#E9E9E9'

 #Image( if You want)

   #bmi_table = Image.open('bmitable.png')
   #bmi_table = ImageTk.PhotoImage(bmi_table)
   #bmi_label = Label(image = bmi_table)
   #bmi_label.place(x = 170, y = 500)

# Widgets

    #Height

label_for_height = Label(
    text='Enter Your height (meters)',
    font=('Bahnschrift','36')
)
entry_for_height = Entry(
    width=20,
    font=('Bahnschrift','60'),
    justify=CENTER
)


   #Weight

label_for_weight = Label(
    text='Enter Your weight (kilograms)',
    font=('Bahnschrift','36')
)
entry_for_weight = Entry(
    width=20,
    font=('Bahnschrift','60'),
    justify=CENTER
)

   #Buttons And Calculate

def calculate():
    height = float(entry_for_height.get())
    weight = float(entry_for_weight.get())

    # BMI formula = weight / (height ** 2)

    BMI = round(weight / (height ** 2),1 )

    if BMI < 15.99:
        status = 'severe underweight'
    elif BMI > 16 and BMI < 18.49:
        status = 'underweight'
    elif BMI > 18.5 and BMI < 24.49:
        status = 'normal weight'
    elif BMI > 25 and BMI < 29.99:
        status = 'obesity'
    elif BMI > 30 and BMI < 34.99:
        status = 'first degree of obesity'
    elif BMI > 35 and BMI <39.99:
        status = 'second degree of obesity'
    else:
        status = ' third degree of obesity'

    



    result_label = Label(
        text = f'''
    Your BMI: {BMI} kg/m²\n
    It`s {status} 
        ''',
        font=('Bahnschrift','26')
    )
   
        
    result_label.pack()



submit_button = Button(
    text='Calculate',
    bg='#B9B9B9',
    activebackground='#A4A4A4',
    font=('Bahnschrift','30'),
    command=calculate

)









# Placing widgets

label_for_height.pack()
entry_for_height.pack()
label_for_weight.pack()
entry_for_weight.pack()
submit_button.pack()


if __name__ == '__main__':
    root.mainloop()
