import multiprocessing
import psutil
import tkinter as tk

# Global variable to store the load percentage
load_percent = 0

def increase_load(percent):
    while True:
        x = 0
        for i in range(10**6):
            x += i
        if percent == 0:
            break

def update_load():
    global load_percent
    load_percent += 10
    if load_percent > 100:
        load_percent = 100
    processes = []
    for i in range(num_cores):
        p = multiprocessing.Process(target=increase_load, args=(load_percent,))
        processes.append(p)
        p.start()
    update_display()

def reset_load():
    global load_percent
    load_percent = 0
    for p in processes:
        p.terminate()
    update_display()

def update_display():
    for i, cpu_percent in enumerate(psutil.cpu_percent(percpu=True)):
        label_text = f"Core {i}: {cpu_percent}%"
        labels[i].config(text=label_text)

if __name__ == '__main__':
    # Get the number of CPU cores
    num_cores = multiprocessing.cpu_count()

    # Create the GUI
    root = tk.Tk()
    root.title("CPU Load Test")

    # Create the labels for displaying the CPU load
    labels = []
    for i in range(num_cores):
        label = tk.Label(root, text=f"Core {i}: 0%")
        label.pack()
        labels.append(label)

    # Create the buttons for updating and resetting the load
    update_button = tk.Button(root, text="Increase Load", command=update_load)
    update_button.pack()
    reset_button = tk.Button(root, text="Reset Load", command=reset_load)
    reset_button.pack()

    # Start the GUI loop
    root.mainloop()
