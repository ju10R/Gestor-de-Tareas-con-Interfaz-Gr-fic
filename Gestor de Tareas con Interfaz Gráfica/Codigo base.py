import tkinter as tk
from tkinter import messagebox
import json
from typing import TextIO

# Archivo donde se guardarán las tareas
TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    file: TextIO
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task = entry_task.get()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        del tasks[selected_index]
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["completed"] else "✖"
        listbox_tasks.insert(tk.END, f"{status} {task['task']}")

# Cargar tareas
tasks = load_tasks()

# Interfaz gráfica
root = tk.Tk()
root.title("Gestor de Tareas")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_task = tk.Entry(frame, width=40)
entry_task.pack(side=tk.LEFT, padx=10)
btn_add = tk.Button(frame, text="Agregar", command=add_task)
btn_add.pack(side=tk.LEFT)

listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

btn_delete = tk.Button(root, text="Eliminar", command=delete_task)
btn_delete.pack()

btn_complete = tk.Button(root, text="Marcar Completada", command=mark_completed)
btn_complete.pack()

update_listbox()

root.mainloop()
