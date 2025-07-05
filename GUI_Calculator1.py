import tkinter as tk
from tkinter import ttk, messagebox
 
# --- FUNCTIONS ---
def perform_operation():
    if entry1.get().strip() == "" or entry2.get().strip() == "":
        messagebox.showwarning("⚠️ Missing Input", "Please enter both numbers!")
        return

    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
    except ValueError:
        messagebox.showerror("❌ Invalid Input", "Please enter valid numbers!")
        return

    if radio_var.get() == 0:
        messagebox.showwarning("⚠️ No Operation", "Please select an operation!")
        return

    if radio_var.get() == 1:
        result = n1 + n2
    elif radio_var.get() == 2:
        result = n1 - n2
    elif radio_var.get() == 3:
        result = n1 * n2
    elif radio_var.get() == 4:
        if n2 == 0:
            messagebox.showerror("❌ Math Error", "Division by zero not allowed!")
            return
        result = n1 / n2

    result_label.config(text=f"🧠 Result: {result}")


# --- MAIN WINDOW ---
root = tk.Tk()
root.title("🧠Calculator")
root.geometry("400x400")
root.configure(bg="#1f1f1f")

style = ttk.Style(root)
style.theme_use("clam")

# --- STYLES ---
style.configure("TLabel", background="#1f1f1f", foreground="#ffffff", font=("Helvetica", 11))
style.configure("TButton", font=("Helvetica", 11, "bold"), padding=6)
style.configure("TRadiobutton", background="#1f1f1f", foreground="#ffffff", font=("Helvetica", 10))

# --- INPUTS FRAME ---
frame = ttk.Frame(root, padding=20)
frame.pack(pady=20)

ttk.Label(frame, text="Enter First Number:").grid(row=0, column=0, sticky="w", pady=5)
entry1 = ttk.Entry(frame, width=20)
entry1.grid(row=0, column=1)

ttk.Label(frame, text="Enter Second Number:").grid(row=1, column=0, sticky="w", pady=5)
entry2 = ttk.Entry(frame, width=20)
entry2.grid(row=1, column=1)

# --- RADIO BUTTONS ---
radio_var = tk.IntVar(value=0)
ttk.Label(frame, text="Select Operation:").grid(row=2, column=0, sticky="w", pady=(15, 5))

ops = [("➕ Add", 1), ("➖ Subtract", 2), ("✖️ Multiply", 3), ("➗ Divide", 4)]

for i, (text, val) in enumerate(ops):
    ttk.Radiobutton(frame, text=text, variable=radio_var, value=val).grid(row=3+i//2, column=i%2, sticky="w", padx=10, pady=2)

# --- BUTTON ---
def on_enter(e):
    calc_btn.configure(style="Hover.TButton")

def on_leave(e):
    calc_btn.configure(style="TButton")

style.configure("Hover.TButton", background="#00ffcc", foreground="#000", font=("Helvetica", 11, "bold"))

calc_btn = ttk.Button(root, text="✨ Calculate", command=perform_operation)
calc_btn.pack(pady=15)
calc_btn.bind("<Enter>", on_enter)
calc_btn.bind("<Leave>", on_leave)

# --- RESULT ---
result_label = ttk.Label(root, text="Result will appear here", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()




