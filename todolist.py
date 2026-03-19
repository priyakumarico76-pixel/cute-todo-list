import tkinter as tk

# create window
window = tk.Tk()
window.title("🌸 Priya's Sticky Note 🌸")

# sticky note size
window.geometry("260x320")

# disable resizing
window.resizable(False, False)

# sticky note pink color
window.configure(bg="#ffd6e7")

tasks = []

# title label
title = tk.Label(
    window,
    text="My Tasks ✨",
    bg="#ffd6e7",
    font=("Arial", 14, "bold")
)
title.pack(pady=10)

# input box
entry = tk.Entry(
    window,
    width=22,
    font=("Arial", 10)
)
entry.pack(pady=5)

# function to add task
def add_task():

    task = entry.get()

    if task != "":
        tasks.append(task)

        label = tk.Label(
            window,
            text="☐ " + task,
            bg="#ffd6e7",
            anchor="w",
            font=("Arial", 10)
        )

        label.pack(fill="x", padx=20, pady=2)

        entry.delete(0, tk.END)

# add task button
button = tk.Button(
    window,
    text="Add Task",
    command=add_task,
    bg="#ff9ecb",
    relief="flat"
)

button.pack(pady=10)

# run window
window.mainloop()
