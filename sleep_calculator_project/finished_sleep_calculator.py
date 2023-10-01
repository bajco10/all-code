import tkinter as tk

def time_calculation():
        """returns times when you should go to bed"""
        hours, minutes = ent_time.get().split(", ")
        t_in_min = 60*int(hours) + int(minutes)
        wake_up_times = []
        for i in range(1, 7):
            # 15 additional minutes to fall asleep
            if t_in_min-(i*90+15) < 0:
                t_in_min+= (24*60)
            wake_up_times.append(convert_m_into_h_and_m(t_in_min-(i*90+15)))
        # return wake_up_times
        lbl_times["text"] = wake_up_times[::-1]

def convert_m_into_h_and_m(minutes):
    """convenient way of dealing with time formats"""
    hours = minutes // 60
    minutes = minutes % 60
    formatted_time = f"{hours}:{minutes}"#[hours, minutes]
    return formatted_time

# the GUI

window=tk.Tk()
window.title("Sleep Calculator")
window.resizable(width=False, height=False)

lbl_time = tk.Label(master=window, text="Enter your wake-up time:\n(use ',' between h and m)")
ent_time = tk.Entry(master=window, width=10)
btn_calc = tk.Button(
     master=window,
     text="calculate",
     command=time_calculation
)
lbl_times = tk.Label(master=window, text="")

lbl_time.grid(row=0, column=0, sticky="nsew")
ent_time.grid(row=1, column=0, sticky="nsew")
btn_calc.grid(row=2, column=0)
lbl_times.grid(row=3, column=0)

window.mainloop()