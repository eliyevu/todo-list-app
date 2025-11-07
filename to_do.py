import tkinter as tk

# Add a task to the listbox
def add_task(task_entry, task_listbox):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        print("Please enter a task!")

# Delete selected task
def delete_task(task_listbox):
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        print("Please select a task to delete!")

# Clear all tasks
def clear_all_tasks(task_listbox):
    task_listbox.delete(0, tk.END)

# Mark task as complete
def mark_complete(task_listbox):
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)

        if not task.startswith("✓ "):
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, "✓ " + task)
            task_listbox.itemconfig(selected_index, fg="#808080")
    except IndexError:
        print("Please select a task to mark as complete!")

