import tkinter as tk
from tkinter import messagebox
import os

# ------------ Setup ------------
window = tk.Tk()
window.title("Superna's To-Do List 💕")
window.geometry("500x500")
window.config(bg="#ffffff")  # cherry red background 💗

# Set your cute icon before mainloop 🥺✨
window.iconbitmap(r"c:\Users\bisht\Downloads\favicon.ico")  # Or just "favicon.ico" if in same folder

tasks = []
TASKS_FILE = "tasks.txt"

# ------------ Functions ------------
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        update_listbox()

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get().upper()
    if task and task not in tasks:
        tasks.append(task)
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks()
    elif task in tasks:
        messagebox.showinfo("Oops!", "This task already exists.")
    else:
        messagebox.showwarning("Oops!", "You forgot to type something!")

def complete_task():
    try:
        selected_index = listbox.curselection()[0]
        task = listbox.get(selected_index)
        tasks.remove(task)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Wait!", "Select a task first, silly!")

def exit_app():
    print("App is closing... bye Superna! 💖")
    window.destroy()


def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# ------------ Styling Variables ------------
font_style = ("Georgia", 12,"italic")
button_color = "#f7b2d9"
hover_color = "#f58fb1"

# ------------ Widgets ------------
title = tk.Label(window, text="💖 My To-Do List 💖", font=("Georgia", 16, "italic"), bg="#fff5f8", fg="#d63384")
title.pack(pady=10)

entry = tk.Entry(window, font=font_style, width=30, bd=2)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task ➕", font=font_style, bg=button_color, fg="black", command=add_task)
add_button.pack(pady=5)

listbox = tk.Listbox(window, font=font_style, width=70, height=12, bd=2, bg="#fff0f6")
listbox.pack(pady=10)

complete_button = tk.Button(window, text="Task Completed ✅", font=font_style, bg=button_color, command=complete_task)
complete_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit ✖", font=font_style, bg="#ffb3b3", command=exit_app)
exit_button.pack(pady=10)

# ------------ Start App ------------
load_tasks()
window.mainloop()
