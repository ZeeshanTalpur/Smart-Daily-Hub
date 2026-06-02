import tkinter as tk
import random

#main window
root=tk.Tk()
root.title("Smart Daily Hub")
root.geometry("600x600")

#frames creation
main_menu=tk.Frame(root)
motivation_screen=tk.Frame(root)
timer_screen=tk.Frame(root)
calculator_screen=tk.Frame(root)
notes_screen=tk.Frame(root)

#navigation
def show_frame(frame):
    for f in (main_menu, motivation_screen, timer_screen, calculator_screen, notes_screen):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

#main menu
tk.Label(main_menu, text="SMART DAILY HUB", font=("Arial",18,"bold")).pack(pady=15)
tk.Button(main_menu, text="Motivation", width=20,
          command=lambda: show_frame(motivation_screen)).pack(pady=5)
tk.Button(main_menu, text="Timer", width=20,
          command=lambda: show_frame(timer_screen)).pack(pady=5)
tk.Button(main_menu, text="Calculator", width=20,
          command=lambda: show_frame(calculator_screen)).pack(pady=5)
tk.Button(main_menu, text="Notes", width=20,
          command=lambda: show_frame(notes_screen)).pack(pady=5)

#motivation screen
quotes = [
    "Stay consistent, success will follow.",
    "Small steps every day lead to big results.",
    "Discipline beats motivation.",
    "You are closer than you think.",
    "Keep going, even when it's hard."
]

tk.Button(motivation_screen, text="⬅ Back",
          command=lambda: show_frame(main_menu)).pack(anchor="nw", padx=10, pady=10)
motivation_label = tk.Label(motivation_screen, text="Thought of the moment", font=("Arial", 12), wraplength=400)
motivation_label.pack(pady=30)

def generate_quote():
    motivation_label.config(text=random.choice(quotes))

tk.Button(motivation_screen, text="Generate Quote", command=generate_quote).pack()

#timer screen
tk.Button(timer_screen, text="⬅ Back",
          command=lambda: show_frame(main_menu)).pack(anchor="nw", padx=10, pady=10)
tk.Label(timer_screen, text="Focus Timer", font=("Arial",16)).pack(pady=10)
time_entry = tk.Entry(timer_screen)
time_entry.pack(pady=5)
unit_var = tk.StringVar(value="seconds")
unit_menu = tk.OptionMenu(timer_screen, unit_var, "seconds", "minutes", "hours")
unit_menu.pack(pady=5)

timer_label = tk.Label(timer_screen, text="", font=("Arial", 14))
timer_label.pack(pady=10)

timer_running = False

def format_time(seconds):
    hrs = seconds // 3600
    mins = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"

def countdown(seconds):
    global timer_running
    if timer_running and seconds >= 0:
        timer_label.config(text=f"Time Left: {format_time(seconds)}")
        root.after(1000, countdown, seconds - 1)

def start_timer():
    global timer_running
    timer_running = True

    try:
        value = int(time_entry.get())
    except:
        timer_label.config(text="Enter valid number")
        return

    unit = unit_var.get()

    if unit == "seconds":
        total = value
    elif unit == "minutes":
        total = value * 60
    else:
        total = value * 3600

    countdown(total)

tk.Button(timer_screen, text="Start Timer", command=start_timer).pack()


#calculator
tk.Button(calculator_screen, text="⬅ Back",
          command=lambda: show_frame(main_menu)).pack(anchor="nw", padx=10, pady=10)
tk.Label(calculator_screen, text="Calculator", font=("Arial",16)).pack(pady=10)
entry1 = tk.Entry(calculator_screen)
entry1.pack(pady=5)
entry2 = tk.Entry(calculator_screen)
entry2.pack(pady=5)

calc_result = tk.Label(calculator_screen, text="")
calc_result.pack(pady=10)

def calculate(op):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            res = a / b if b != 0 else "Error"
        else:
            res = "Invalid"
        calc_result.config(text=f"Result: {res}")
    except:
        calc_result.config(text="Invalid Input")

for op in ["+", "-", "*", "/"]:
    tk.Button(calculator_screen, text=op,
              command=lambda o=op: calculate(o)).pack()



#notes
tk.Button(notes_screen, text="⬅ Back",
          command=lambda: show_frame(main_menu)).pack(anchor="nw", padx=10, pady=10)
tk.Label(notes_screen, text="Notes", font=("Arial",16)).pack(pady=10)
text_box = tk.Text(notes_screen, height=12, width=40)
text_box.pack(pady=10)

def save_note():
    data = text_box.get("1.0", tk.END).strip()
    if data:
        with open("notes.txt", "a") as f:
            f.write(data + "\n---\n")
        text_box.delete("1.0", tk.END)

def load_notes():
    try:
        with open("notes.txt", "r") as f:
            content = f.read()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, content)
    except:
        text_box.insert(tk.END, "No notes found.")


#load
tk.Button(notes_screen, text="Save Note", command=save_note).pack()
tk.Button(notes_screen, text="Load Notes", command=load_notes).pack()



























show_frame(main_menu)
root.mainloop()