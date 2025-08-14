import os
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import shutil
import subprocess

# ---------------------------
# Helper functions
# ---------------------------

def get_disk_usage(path):
    usage = []
    try:
        for root, dirs, files in os.walk(path):
            total_size = 0
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    total_size += os.path.getsize(fp)
                except:
                    continue
            usage.append((root, total_size))
    except Exception as e:
        print("Error scanning:", e)
    usage.sort(key=lambda x: x[1], reverse=True)
    return usage[:20]  # top 20 largest

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}P{suffix}"

def delete_selected():
    selected = [path for var, path in checkboxes if var.get()]
    if not selected:
        messagebox.showinfo("Disk Cleanup", "No folders selected for deletion")
        return
    confirm = messagebox.askyesno("Confirm Deletion",
                                  f"Are you sure you want to delete {len(selected)} items?")
    if confirm:
        deleted = 0
        for path in selected:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                deleted += 1
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
        messagebox.showinfo("Disk Cleanup", f"Deleted {deleted} items successfully")
        refresh_list()

def refresh_list():
    for widget in frame.winfo_children():
        widget.destroy()
    usage = get_disk_usage(scan_path.get())
    global checkboxes
    checkboxes = []
    for path, size in usage:
        var = tk.BooleanVar()
        cb = tk.Checkbutton(frame, text=f"{path} ({sizeof_fmt(size)})", variable=var, anchor="w")
        cb.pack(fill="x")
        checkboxes.append((var, path))

# ---------------------------
# Linux Ext4 reserved space reduction
# ---------------------------

def ext4_reserved_space_option():
    if platform.system() != "Linux":
        messagebox.showinfo("Ext4 Reserved Space", "This feature is Linux-only")
        return
    path = scan_path.get()
    try:
        result = subprocess.check_output(['df', path], text=True).splitlines()
        device = result[1].split()[0]
        output = subprocess.check_output(['sudo', 'tune2fs', '-l', device], text=True)
        reserved_blocks = total_blocks = 0
        for line in output.splitlines():
            if "Reserved block count" in line:
                reserved_blocks = int(line.split(":")[1].strip())
            if "Block count" in line:
                total_blocks = int(line.split(":")[1].strip())
        current_percentage = reserved_blocks / total_blocks * 100 if total_blocks else 0
    except Exception as e:
        messagebox.showerror("Error", f"Cannot determine filesystem info: {e}")
        return
    confirm = messagebox.askyesno(
        "Reduce Reserved Space",
        f"Current reserved space: {current_percentage:.2f}%\n"
        "Reduce to 1% to free up space? Requires root privileges."
    )
    if confirm:
        try:
            subprocess.run(['sudo', 'tune2fs', '-m', '1', device], check=True)
            messagebox.showinfo("Success", "Reserved space reduced to 1%")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to reduce reserved space: {e}")

# ---------------------------
# GUI
# ---------------------------

root = tk.Tk()
root.title("Cross-Platform Disk Cleanup")
root.geometry("600x600")

system = platform.system()
default_path = "/"
if system == "Windows":
    default_path = "C:\\"
elif system == "Darwin":
    default_path = "/"

scan_path = tk.StringVar(value=default_path)

tk.Label(root, text="Scan Path:").pack(pady=5)
entry = tk.Entry(root, textvariable=scan_path, width=50)
entry.pack(pady=5)

tk.Button(root, text="Refresh List", command=refresh_list).pack(pady=5)

# Scrollable frame
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
frame = scrollable_frame

tk.Button(root, text="Delete Selected", command=delete_selected).pack(pady=10)

# Linux-only Ext4 reserved space button
if system == "Linux":
    tk.Button(root, text="Reduce Ext4 Reserved Space", command=ext4_reserved_space_option).pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

checkboxes = []

refresh_list()

root.mainloop()
