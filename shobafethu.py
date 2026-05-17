from tkinter import *
from tkinter import messagebox
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        
        birth_date = date(year, month, day)

        
        today = date.today()

        
        age = today.year - birth_date.year

        
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"Present Age: {age} years")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date.")


root = Tk()
root.title("Age Calculator")
root.geometry("350x250")

heading = Label(root, text="Age Calculator")
heading.pack(pady=10)

day_label = Label(root, text="Day:")
day_label.pack()
day_entry = Entry(root)
day_entry.pack()

month_label = Label(root, text="Month:")
month_label.pack()
month_entry = Entry(root)
month_entry.pack()

year_label = Label(root, text="Year:")
year_label.pack()
year_entry = Entry(root)
year_entry.pack()

calc_button = Button(root, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()