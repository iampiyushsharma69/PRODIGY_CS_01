
"""
Caesar Cipher GUI Tool

This program encrypts or decrypts a given text using the Caesar Cipher algorithm.
Users can input a message and a shift value, and choose whether to encrypt or decrypt.
A simple Windows GUI is provided using Tkinter.

Author: [Piyush Sharma]
Date: [15 april 2025]
"""

import tkinter as tk
from tkinter import ttk, messagebox


def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypt or decrypt text using the Caesar Cipher algorithm.

    Parameters:
        text (str): The input text to process.
        shift (int): The number of positions to shift each letter.
        mode (str): Operation mode - either 'encrypt' or 'decrypt'.
    
    Returns:
        str: The processed text after shifting.
    """
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            # Determine ASCII offset based on uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Compute the new character code, wrapping around with modulo 26
            shifted_code = (ord(char) - ascii_offset + shift) % 26 + ascii_offset
            result.append(chr(shifted_code))
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return ''.join(result)


def process_text():
    """
    Retrieve user input, perform the encryption/decryption, and display the result.
    """
    # Get the message and the shift value from the GUI
    text = text_input.get("1.0", tk.END).rstrip("\n")
    shift_value = shift_entry.get()
    mode = operation.get()

    # Validate shift value
    try:
        shift = int(shift_value)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for the shift value.")
        return

    # Process the text using the caesar_cipher function
    processed_text = caesar_cipher(text, shift, mode)
    result_output.config(state=tk.NORMAL)
    result_output.delete("1.0", tk.END)
    result_output.insert(tk.END, processed_text)
    result_output.config(state=tk.DISABLED)


# Create the main application window
root = tk.Tk()
root.title("Professional Caesar Cipher Tool")
root.resizable(False, False)

# Create and position the main frame
main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Label for the input message
ttk.Label(main_frame, text="Enter your message:").grid(column=0, row=0, sticky=tk.W)
text_input = tk.Text(main_frame, width=50, height=6, wrap=tk.WORD)
text_input.grid(column=0, row=1, columnspan=3, pady=5)

# Label and Entry widget for the shift value
ttk.Label(main_frame, text="Shift Value:").grid(column=0, row=2, sticky=tk.W, pady=(10, 0))
shift_entry = ttk.Entry(main_frame, width=10)
shift_entry.grid(column=1, row=2, sticky=tk.W, pady=(10, 0))
shift_entry.insert(0, "3")  # default shift value

# Radio buttons for selecting operation mode (Encrypt or Decrypt)
operation = tk.StringVar(value="encrypt")
ttk.Radiobutton(main_frame, text="Encrypt", variable=operation, value="encrypt").grid(column=0, row=3, sticky=tk.W, pady=(10, 0))
ttk.Radiobutton(main_frame, text="Decrypt", variable=operation, value="decrypt").grid(column=1, row=3, sticky=tk.W, pady=(10, 0))

# Button to execute the cipher process
process_button = ttk.Button(main_frame, text="Process", command=process_text)
process_button.grid(column=0, row=4, columnspan=2, pady=(15, 0))

# Label for displaying the result
ttk.Label(main_frame, text="Result:").grid(column=0, row=5, sticky=tk.W, pady=(15, 0))
result_output = tk.Text(main_frame, width=50, height=6, wrap=tk.WORD, state=tk.DISABLED)
result_output.grid(column=0, row=6, columnspan=3, pady=5)

# Add padding to all children of the main_frame
for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
