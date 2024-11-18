import tkinter as tk
from tkinter import messagebox
from shodan_api import get_account_info, search_ip

def fetch_account_info():
    api_key = api_key_entry.get()
    if not api_key:
        messagebox.showwarning("API Key", "Please enter your Shodan API Key.")
        return
    try:
        account_info = get_account_info(api_key)
        if account_info:
            messagebox.showinfo("Account Info", f"Account Information:\n{account_info}")
        else:
            messagebox.showerror("Error", "Failed to fetch account info.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_ip_info():
    api_key = api_key_entry.get()
    ip_address = ip_entry.get()
    if not api_key or not ip_address:
        messagebox.showwarning("Input Missing", "Please enter both API Key and IP Address.")
        return
    try:
        ip_info = search_ip(api_key, ip_address)
        if ip_info:
            messagebox.showinfo("IP Info", f"IP Information:\n{ip_info}")
        else:
            messagebox.showerror("Error", "Failed to fetch IP info.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Shodan GUI")
root.geometry("500x300")

# API Key Section
tk.Label(root, text="Shodan API Key:").pack(pady=5)
api_key_entry = tk.Entry(root, width=50, show="*")  # Mask API key
api_key_entry.pack(pady=5)

# IP Address Section
tk.Label(root, text="IP Address to Search:").pack(pady=5)
ip_entry = tk.Entry(root, width=50)
ip_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Get Account Info", command=fetch_account_info).pack(pady=5)
tk.Button(root, text="Search IP Address", command=fetch_ip_info).pack(pady=5)

root.mainloop()
