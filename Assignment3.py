# Program Name: Assignment3.py 
# Course: IT3883/Section W02
# Student Name: Leonardo Barranco
# Assignment Number: Lab3
# Due Date: 2/23/2025
# Purpose: Create a GUI applicationt that conversts MGP to KMPL
# https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/#google_vignette
#https://www.geeksforgeeks.org/tkinter-colors/
#https://www.geeksforgeeks.org/tkinter-fonts/
import tkinter as tk

#The math that goes into the GUI
def convert_mpg_to_kmpl(event=None):
    try:
        mpg = float(entry_mpg.get())
        kmpl = mpg * 0.425144
        result.config(text=f"{kmpl:.2f} Km/L")
    except ValueError:
        result.config(text="Enter valid numbes")

# Creates the window and gives it a title
root = tk.Tk()
root.title("MPG to Km/L Converter")

# Widgets for the GUI
root.geometry('350x150') #size of the box
label_mpg = tk.Label(root, text="Miles per Gallon (MPG):") #lable of what the user is inputing
entry_mpg = tk.Entry(root, bg="white") #entry box, I left it as white but it can be changed to other colors
result = tk.Label(root, text="0.00 Km/L", font=("Arial", 14, "bold"))

# Binds the entry so the user does not have to hit enter
entry_mpg.bind("<KeyRelease>", convert_mpg_to_kmpl)

# creates layout of the GUI
label_mpg.grid(row=0, column=0, padx=10, pady=10)
entry_mpg.grid(row=0, column=1, padx=10, pady=10)
result.grid(row=1, column=0, columnspan=2, pady=10)

# Run main loop
root.mainloop()