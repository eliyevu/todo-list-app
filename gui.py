import tkinter as tk
from to_do import add_task, delete_task, clear_all_tasks, mark_complete

# ===== MAIN WINDOW SETUP =====
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x600")
root.resizable(False, False)
root.config(bg="#f0f0f0")  # Light gray background
root.resizable(True, True)

# ===== HEADER SECTION =====
header_frame = tk.Frame(root, bg="#4a7c9e")
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="📝 My To-Do List", 
    font=("Arial", 18, "bold"), 
    bg="#4a7c9e", fg="white")
header_label.pack(pady=15)

# ===== INPUT SECTION =====
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=20)
# Text entry box for adding new tasks
task_entry = tk.Entry(input_frame, width=35, font=("Arial", 13), 
    bd=2, relief=tk.GROOVE)
task_entry.pack(side=tk.LEFT, padx=10, ipady=5)
# Button to add a new task
add_button = tk.Button(input_frame, text="Add Task", width=12, 
    font=("Arial", 11, "bold"),
    bg="#5cb85c", fg="white", 
    activebackground="#4cae4c",
    bd=0, cursor="hand2",
    command=lambda: add_task(task_entry, task_listbox))
add_button.pack(side=tk.LEFT)

# ===== LISTBOX SECTION =====
list_frame = tk.Frame(root, bg="#f0f0f0")
list_frame.pack(pady=10, padx=20, fill= "both", expand=0)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
# Main list where tasks appear
task_listbox = tk.Listbox(list_frame, width=55, height=14, 
    font=("Arial", 11),
    bd=2, relief=tk.SUNKEN,
    selectmode=tk.SINGLE,
    activestyle='none',
    bg="white",
    selectbackground="#d4e6f1",
    selectforeground="black",
yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ===== BUTTON SECTION =====
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)
# Button to mark a task as complete
mark_button = tk.Button(button_frame, text="✓ Mark Complete", width=15, 
    font=("Arial", 10, "bold"),
    bg="#5bc0de", fg="white",
    activebackground="#46b8da",
    bd=0, cursor="hand2",
    command=lambda: mark_complete(task_listbox))
mark_button.grid(row=0, column=0, padx=8)
# Button to delete selected task
delete_button = tk.Button(button_frame, text="✕ Delete Task", width=15, 
    font=("Arial", 10, "bold"),
    bg="#d9534f", fg="white",
    activebackground="#c9302c",
    bd=0, cursor="hand2",
    command=lambda: delete_task(task_listbox))
delete_button.grid(row=0, column=1, padx=8)
# Button to clear all tasks
clear_button = tk.Button(button_frame, text="Clear All", width=15, 
    font=("Arial", 10, "bold"),
    bg="#f0ad4e", fg="white",
    activebackground="#ec971f",
    bd=0, cursor="hand2",
    command=lambda: clear_all_tasks(task_listbox))
clear_button.grid(row=0, column=2, padx=8)


# Start the event loop
root.mainloop()