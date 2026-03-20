import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# window
window = tk.Tk()
window.title("Priya's Sticky Note")
window.geometry("320x420")
window.resizable(False, False)
window.configure(bg="#ffd6e7")

tasks = []

# ---------- BACKGROUND ----------
bg_label = tk.Label(window)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def change_bg():
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = img.resize((320, 420))
        photo = ImageTk.PhotoImage(img)

        bg_label.config(image=photo)
        bg_label.image = photo   # IMPORTANT (keeps image)

# ---------- FAKE TOP BAR ----------
top_bar = tk.Frame(window, bg="#ffb6c1", height=40)
top_bar.pack(fill="x")

title = tk.Label(top_bar, text="🌸 Priya’s Sticky Note 🌸", bg="#ffb6c1", fg="white")
title.pack(pady=8)

# ---------- MAIN AREA ----------
frame = tk.Frame(window, bg="#ffd6e7")
frame.pack(pady=10)

# ---------- ENTRY ----------
entry = tk.Entry(frame, width=25)
entry.pack(pady=5)

# ---------- ADD TASK ----------
def add_task(event=None):
    task = entry.get()
    if task != "":
        var = tk.BooleanVar()
        cb = tk.Checkbutton(frame, text=task, variable=var, bg="#ffd6e7")
        cb.var = var
        cb.pack(anchor="w")
        tasks.append(cb)
        entry.delete(0, tk.END)

entry.bind("<Return>", add_task)

# ---------- BUTTONS ----------
add_btn = tk.Button(frame, text="Add Task", command=add_task)
add_btn.pack(pady=3)

def delete_task():
    for cb in tasks[:]:
        if cb.var.get():
            cb.destroy()
            tasks.remove(cb)

delete_btn = tk.Button(frame, text="Delete Selected", command=delete_task)
delete_btn.pack(pady=3)

bg_btn = tk.Button(frame, text="Change Background", command=change_bg)
bg_btn.pack(pady=5)

# ---------- RUN ----------
window.mainloop()
