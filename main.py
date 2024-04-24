from tkinter import *
from tkinter import messagebox 
import webbrowser
from bmi_calculation import bmi_calculate 


def show_bmi():
    name = name_entry.get()
    height_str= height_entry.get()
    weight_str= weight_entry.get()
    if height_str and weight_str:
        height = float(height_str)
        weight = float(weight_str)

        if weight <= 0 or weight > 635:
            messagebox.showerror('Error', 'Enter a valid input')
        elif height <= 0 or height > 2.72:
            messagebox.showerror('Error', 'Enter a valid input')
        else: 
            result, bmi_score = bmi_calculate(weight, height)
            result_label.config(text=f"{name}'s BMI is {result} by {bmi_score}")

            if bmi_score < 18.5:
                button_for_underweight.grid(row=7, column=0, columnspan=2, pady=10)
            elif bmi_score > 30:
                button_for_obesity.grid(row=7, column=0, columnspan=2, pady=10)


        
def open_link_underweight():
    url = "https://www.healthdirect.gov.au/what-to-do-if-you-are-underweight"
    webbrowser.open(url)


def open_link_obesity():
    url = "https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight"
    webbrowser.open(url)
 
root = Tk()
root.title("BMI Calculation")
root.geometry('600x400')

#Welcome 
welcome_label = Label(root, text= "Welcome to BMI Calculation", font=('courier', 15, 'bold'))
welcome_label.grid(row= 0, column= 0, columnspan=2, padx= 20, pady= 10)

# Instruction 
instruction_label = Label(root, text= "Please enter your height in cm and weight in kg to get your BMI result", font=('courier', 10, 'bold'))
instruction_label.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

# Label and Entry fields using grid layout
Label(root, text = "Name: ", font=('courier', 10, 'bold')). grid(row =2, column=0, columnspan=1)
name_entry = Entry(root)
name_entry.grid(row=2, column=1)

Label(root, text="Height in cm: ",font=('courier', 10, 'bold')).grid(row =3, column=0, columnspan=1)
height_entry = Entry(root)
height_entry.grid(row=3, column=1)

Label(root, text="Weight in kg: ",font=('courier', 10, 'bold')). grid(row =4, column=0, columnspan=1)
weight_entry = Entry(root)
weight_entry.grid(row=4, column=1)

# add button to calculation
button = Button(root, text="Calculate",font=('courier', 10), command = show_bmi, bg="green", fg="white")
button.grid(row=5, column=0, columnspan= 2, pady=5) 

# show the result of bmi values
result_label = Label(root, text="", font=('courier', 10))
result_label.grid(row=6, column=0, columnspan=2)

# if bmi_score underweight, show button to click for more info
button_for_underweight = Button(root, text="click for more infomation about underweight", command= open_link_underweight, bg="blue", fg="white")

# if bmi score > 30, show button to learn more about obesity 
button_for_obesity = Button(root, text="Click here for more infomation about obesity", command=open_link_obesity, bg="blue", fg="white")

# add button to exist
exit_button = Button(root, text="Exit", command=root.quit, font=('courier', 10), bg="red", fg="white")
exit_button.grid(row=5, column=1, columnspan=2, pady=5)

#run the tk 
root.mainloop()

