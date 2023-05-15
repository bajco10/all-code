import tkinter as tk
import time

# Define a function to get the time and print it in the terminal
def get_time():
    current_time = time.strftime("%H:%M:%S")
    print("Current time is:", current_time)

# Create a Tkinter windowbutton = tk.Button(text="Get Time", command=get_time)
button.pack()
window = tk.Tk()
window.title("Time Input")

# Create a label to display instructions
label = tk.Label(text="Enter the time in hours and minutes (24-hour format):")
label.pack()

# Create two Entry widgets for the hours and minutes inputs
hours_entry = tk.Entry(width=2)
hours_entry.pack(side="left")
tk.Label(text=":").pack(side="left")
minutes_entry = tk.Entry(width=2)
minutes_entry.pack(side="left")

# Create a button to get the time
button = tk.Button(text="Get Time", command=get_time)
button.pack()

# Start the main event loop
window.mainloop()
