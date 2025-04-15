import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process_text():
    text = entry_message.get()
    shift_val = shift.get()
    
    if not shift_val.isdigit():
        messagebox.showerror("Error", "Shift must be a number!")
        return

    shift_int = int(shift_val)
    if mode.get() == "Encrypt":
        result = encrypt(text, shift_int)
    else:
        result = decrypt(text, shift_int)
    
    result_label.config(text="Result: " + result)

# GUI setup
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x250")

# Message Entry
tk.Label(window, text="Enter Message:").pack(pady=5)
entry_message = tk.Entry(window, width=40)
entry_message.pack()

# Shift Entry
tk.Label(window, text="Enter Shift:").pack(pady=5)
shift = tk.Entry(window, width=10)
shift.pack()

# Mode: Encrypt or Decrypt
mode = tk.StringVar(value="Encrypt")
tk.Radiobutton(window, text="Encrypt", variable=mode, value="Encrypt").pack()
tk.Radiobutton(window, text="Decrypt", variable=mode, value="Decrypt").pack()

# Button
tk.Button(window, text="Process", command=process_text).pack(pady=10)

# Result Display
result_label = tk.Label(window, text="Result: ", fg="blue")
result_label.pack()

window.mainloop()
