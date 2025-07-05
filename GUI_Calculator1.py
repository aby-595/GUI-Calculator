import tkinter as tk
from tkinter import messagebox

# Try to import a custom font if available
try:
    from tkinter import font as tkfont
except:
    tkfont = None

root = tk.Tk()
root.title("⚡ AI Neon Calculator")
root.geometry("500x500")
root.config(bg="#0d0d0d")  # Dark futuristic background

# Fancy font setup
main_font = ("Segoe UI", 11)
if tkfont:
    if "Orbitron" in tkfont.families():
        main_font = ("Orbitron", 11)

# Neon-style colors
neon_blue = "#00ffff"
neon_pink = "#ff2cd4"

# Entry fields
entry1 = tk.Entry(root, font=("Consolas", 16), bg="#111", fg=neon_blue, insertbackground=neon_blue, bd=0, highlightthickness=2, highlightcolor=neon_blue)
entry1.place(x=100, y=60, width=300, height=40)

entry2 = tk.Entry(root, font=("Consolas", 16), bg="#111", fg=neon_blue, insertbackground=neon_blue, bd=0, highlightthickness=2, highlightcolor=neon_blue)
entry2.place(x=100, y=120, width=300, height=40)

# Operation variable
operation = tk.IntVar()

# Custom radio buttons
operations = [("➕", 1), ("➖", 2), ("✖", 3), ("➗", 4)]
for i, (text, val) in enumerate(operations):
    rb = tk.Radiobutton(root, text=text, variable=operation, value=val, font=("Arial", 16), fg=neon_pink,
                        selectcolor="#222", bg="#0d0d0d", activebackground="#0d0d0d", activeforeground=neon_blue)
    rb.place(x=120 + (i * 70), y=190)

# Result label
result_label = tk.Label(root, text="Result will appear here", font=("Segoe UI", 13, "bold"), fg=neon_blue, bg="#0d0d0d")
result_label.place(x=120, y=300)

# Glow button
hover_effect = {"bg": neon_pink, "fg": "#000"}
def on_enter(e):
    calc_btn.config(**hover_effect)
def on_leave(e):
    calc_btn.config(bg=neon_blue, fg="#000")

def perform_operation():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        op = operation.get()

        if op == 0:
            messagebox.showwarning("⚠️", "Please select an operation")
            return

        result = 0
        if op == 1:
            result = n1 + n2
        elif op == 2:
            result = n1 - n2
        elif op == 3:
            result = n1 * n2
        elif op == 4:
            if n2 == 0:
                messagebox.showerror("❌ Error", "Cannot divide by zero")
                return
            result = n1 / n2

        result_label.config(text=f"💡 Result: {round(result, 3)}")

    except ValueError:
        messagebox.showerror("❌ Error", "Please enter valid numbers")

# Fancy button
calc_btn = tk.Button(root, text="⚡ Calculate", font=("Orbitron", 14, "bold"), bg=neon_blue, fg="#000",
                     activebackground=neon_pink, bd=0, padx=20, pady=10, command=perform_operation)
calc_btn.place(x=180, y=240)
calc_btn.bind("<Enter>", on_enter)
calc_btn.bind("<Leave>", on_leave)

# Drop-shadow glow simulation (just for look)
shadow = tk.Label(root, bg=neon_blue, width=40, height=2)
shadow.place(x=160, y=400)

root.mainloop()




