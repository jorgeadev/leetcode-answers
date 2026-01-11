import tkinter as tk
from tkinter import ttk, messagebox
import os
import re

def extract_problem_name(url):
    # Extract problem name from URL
    match = re.search(r'/problems/([^/]+)/', url)
    if match:
        return match.group(1).replace('-', '_')
    return None

def generate_folder():
    url = url_entry.get().strip()
    difficulty = difficulty_var.get()
    description = description_text.get("1.0", tk.END).strip()
    prefix = prefix_entry.get().strip()
    initial_code = initial_code_text.get("1.0", tk.END).strip()

    if not url or not difficulty or not description or not prefix:
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    problem_name = extract_problem_name(url)
    if not problem_name:
        messagebox.showerror("Error", "Invalid URL format. Could not extract problem name.")
        return

    # Create folder path
    folder_name = f"{prefix.zfill(2)}-{problem_name}"
    folder_path = os.path.join("python", difficulty, folder_name)

    try:
        os.makedirs(folder_path, exist_ok=True)

        # Write challenge.md
        with open(os.path.join(folder_path, "challenge.md"), "w") as f:
            f.write(description)

        # Write answer.py with initial code
        with open(os.path.join(folder_path, "answer.py"), "w") as f:
            f.write(initial_code)

        messagebox.showinfo("Success", f"Folder created successfully at {folder_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create folder: {str(e)}")

# Create main window
root = tk.Tk()
root.title("LeetCode Problem Generator")
root.geometry("700x800")
root.configure(bg="#F0F4F8")  # Light background

# Style configuration
style = ttk.Style()
style.configure("TLabel", background="#F0F4F8", foreground="#2E3440", font=("Helvetica", 12))
style.configure("TButton", background="#4A90E2", foreground="#FFFFFF", font=("Helvetica", 12, "bold"))
style.map("TButton", background=[("active", "#357ABD")])
style.configure("TEntry", fieldbackground="#FFFFFF", foreground="#2E3440", font=("Helvetica", 10))
style.configure("TText", fieldbackground="#FFFFFF", foreground="#2E3440", font=("Helvetica", 10))
style.configure("TMenubutton", background="#4A90E2", foreground="#FFFFFF", font=("Helvetica", 10))

# Title
title_label = ttk.Label(root, text="🚀 LeetCode Problem Generator", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

# URL input
url_frame = ttk.Frame(root, style="Card.TFrame")
url_frame.pack(pady=10, padx=20, fill="x")
ttk.Label(url_frame, text="🔗 LeetCode URL:").pack(anchor="w")
url_entry = ttk.Entry(url_frame, width=80)
url_entry.pack(pady=5, fill="x")

# Difficulty selection
diff_frame = ttk.Frame(root, style="Card.TFrame")
diff_frame.pack(pady=10, padx=20, fill="x")
ttk.Label(diff_frame, text="📊 Difficulty:").pack(anchor="w")
difficulty_var = tk.StringVar(value="easy")
difficulty_menu = ttk.OptionMenu(diff_frame, difficulty_var, "easy", "easy", "medium", "hard")
difficulty_menu.pack(pady=5, anchor="w")

# Problem description
desc_frame = ttk.Frame(root, style="Card.TFrame")
desc_frame.pack(pady=10, padx=20, fill="x")
ttk.Label(desc_frame, text="📝 Problem Description:").pack(anchor="w")
description_text = tk.Text(desc_frame, height=8, width=80, bg="#FFFFFF", fg="#2E3440", font=("Consolas", 10), insertbackground="#2E3440")
description_text.pack(pady=5, fill="x")

# Prefix number
prefix_frame = ttk.Frame(root, style="Card.TFrame")
prefix_frame.pack(pady=10, padx=20, fill="x")
ttk.Label(prefix_frame, text="🔢 Prefix Number (e.g., 03):").pack(anchor="w")
prefix_entry = ttk.Entry(prefix_frame, width=20)
prefix_entry.pack(pady=5, anchor="w")

# Initial code
code_frame = ttk.Frame(root, style="Card.TFrame")
code_frame.pack(pady=10, padx=20, fill="x")
ttk.Label(code_frame, text="💻 Initial Code:").pack(anchor="w")
initial_code_text = tk.Text(code_frame, height=8, width=80, bg="#FFFFFF", fg="#2E3440", font=("Consolas", 10), insertbackground="#2E3440")
initial_code_text.pack(pady=5, fill="x")

# Generate button
generate_button = ttk.Button(root, text="⚡ Generate", command=generate_folder)
generate_button.pack(pady=30)

# Custom style for frames (cards)
style.configure("Card.TFrame", background="#E8EEF7", relief="raised", borderwidth=2)

root.mainloop()