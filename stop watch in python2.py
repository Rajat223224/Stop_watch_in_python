import tkinter as tk
import time

def start():
    global start_time
    start_time = time.time()
    update_time()

def stop():
    global start_time
    start_time = 0
    label.config(text = "00:00:00")

def update_time():
    if start_time != 0:
        elapsed_time = time.time() - start_time
        formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        label.config(text = formatted_time)
        label.after(1000, update_time)

root = tk.Tk()
root.geometry("200x200")
root.title("Stopwatch")

label = tk.Label(root, font = ("Arial", 30))
label.pack()

start_button = tk.Button(root, text = "Start", command = start)

stop_button = tk.Button(root, text = "Stop", command = stop)
start_button.place(x=80,y=60)
stop_button.place(x=80,y=120)

root.mainloop()
