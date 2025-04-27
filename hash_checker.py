# File Hash Checker
# Author: 23R
# Created: April 2025
# Description: A small tool I built to calculate MD5 or SHA256 hashes for files.
#              You can also compare the hash to check if a file is legit.
# Requirements: Just Python 3.8+, uses tkinter and hashlib (built-in).

import tkinter as tk
from tkinter import messagebox, filedialog
import hashlib
import json

def get_file_hash(file_path, algo):
    # This function reads a file and calculates its hash
    # I chose 4096 bytes for chunks because it’s fast enough
    if algo == "MD5":
        hasher = hashlib.md5()
    else:
        hasher = hashlib.sha256()
    
    # Open the file in binary mode and read it in chunks
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            hasher.update(chunk)
    
    # Return the final hash as a string
    return hasher.hexdigest()

def save_to_json(file_path, algo, hash_value):
    # Save the hash result to a JSON file
    # I keep it simple: just the file name, algo, and hash
    result = {
        "file": file_path.split("/")[-1],  # Only the file name, not the full path
        "algo": algo,
        "hash": hash_value
    }
    
    # Try to load existing results, or start with an empty list
    try:
        with open("hashes.json", "r") as f:
            results = json.load(f)
    except:
        results = []
    
    # Add the new result and save it
    results.append(result)
    with open("hashes.json", "w") as f:
        json.dump(results, f)

def main_gui():
    # This is the main GUI function
    # I used Tkinter because it’s easy and built into Python
    window = tk.Tk()
    window.title("Hash Checker by 23R")

    # Label and entry for picking a file
    tk.Label(window, text="Pick a file:").grid(row=0, column=0, padx=5, pady=5)
    file_entry = tk.Entry(window, width=30)
    file_entry.grid(row=0, column=1, padx=5, pady=5)
    
    # Button to open file picker
    def pick_file():
        # Opens a dialog to choose a file
        # Updates the entry with the file path
        path = filedialog.askopenfilename()
        if path:
            file_entry.delete(0, tk.END)
            file_entry.insert(0, path)
    
    tk.Button(window, text="Browse", command=pick_file).grid(row=0, column=2, padx=5, pady=5)

    # Dropdown for choosing MD5 or SHA256
    tk.Label(window, text="Hash type:").grid(row=1, column=0, padx=5, pady=5)
    algo_choice = tk.StringVar(value="SHA256")
    tk.OptionMenu(window, algo_choice, "MD5", "SHA256").grid(row=1, column=1, padx=5, pady=5)

    # Entry for expected hash
    tk.Label(window, text="Expected hash:").grid(row=2, column=0, padx=5, pady=5)
    expected_entry = tk.Entry(window, width=30)
    expected_entry.grid(row=2, column=1, padx=5, pady=5)

    # Label to show results
    result_label = tk.Label(window, text="Result: ")
    result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def calculate():
        # This calculates the hash when you click the button
        file_path = file_entry.get()
        algo = algo_choice.get()
        
        # Check if a file is selected
        if not file_path:
            messagebox.showerror("Error", "Pick a file first!")
            return
        
        # Try to calculate the hash
        try:
            hash_value = get_file_hash(file_path, algo)
            result_label.config(text=f"Result: {algo} = {hash_value}")
            
            # Save the result to JSON
            save_to_json(file_path, algo, hash_value)
            
            # Check if the hash matches the expected one
            expected = expected_entry.get().strip()
            if expected:
                if hash_value.lower() == expected.lower():
                    result_label.config(text=f"Result: {algo} = {hash_value}\nMatches!")
                else:
                    result_label.config(text=f"Result: {algo} = {hash_value}\nDoesn't match!")
        except:
            messagebox.showerror("Error", "Something broke, check your file!")
    
    # Button to start the calculation
    tk.Button(window, text="Calculate", bg="green", fg="white", command=calculate).grid(row=3, column=1, padx=5, pady=10)

    window.mainloop()

if __name__ == "__main__":
    main_gui()
