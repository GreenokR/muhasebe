import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import database

def add_entry():
    tx_type = var_type.get()
    desc = entry_desc.get()
    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Hata", "Tutar geçerli değil.")
        return

    if not desc:
        messagebox.showerror("Hata", "Açıklama boş olamaz.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    database.add_transaction(tx_type, desc, amount, date)
    messagebox.showinfo("Başarılı", "Kayıt eklendi.")
    entry_desc.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    refresh_list()
    update_balance()

def refresh_list():
    listbox.delete(0, tk.END)
    records = database.get_all_transactions()
    for r in records:
        listbox.insert(tk.END, f"{r[4]} - {r[1]} - {r[2]} - {r[3]:.2f} TL")

def update_balance():
    balance = database.get_balance()
    label_balance.config(text=f"Kasa Bakiyesi: {balance:.2f} TL")

def create_ui():
    global entry_desc, entry_amount, var_type, listbox, label_balance

    window = tk.Tk()
    window.title("Muhasebe Takip")
    window.geometry("500x500")

    label_balance = tk.Label(window, text="Kasa Bakiyesi: 0.00 TL", font=("Arial", 14), fg="green")
    label_balance.pack(pady=10)

    var_type = tk.StringVar(value="Gelir")
    frame_type = tk.Frame(window)
    tk.Radiobutton(frame_type, text="Gelir", variable=var_type, value="Gelir").pack(side=tk.LEFT)
    tk.Radiobutton(frame_type, text="Gider", variable=var_type, value="Gider").pack(side=tk.LEFT)
    frame_type.pack()

    entry_desc = tk.Entry(window, width=50)
    entry_desc.insert(0, "Açıklama")
    entry_desc.pack(pady=5)

    entry_amount = tk.Entry(window, width=50)
    entry_amount.insert(0, "Tutar")
    entry_amount.pack(pady=5)

    tk.Button(window, text="Kaydet", command=add_entry, bg="lightblue").pack(pady=10)

    listbox = tk.Listbox(window, width=70)
    listbox.pack(pady=10)

    refresh_list()
    update_balance()

    window.mainloop()
