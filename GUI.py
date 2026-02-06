import tkinter as tk
from tkinter import messagebox, simpledialog
from Device import Device
from Device_Manager import DeviceManager

class DeviceManagerGUI:
    def __init__(self, root, device_manager):
        self.root = root
        self.device_manager = device_manager
        self.root.title("Seadmete haldamine")
        self.root.geometry("800x600")

        # Nimekiri seadmetest
        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.pack(padx=20, pady=10)

        # Nupud
        self.add_button = tk.Button(self.root, text="Lisa seade", command=self.add_device)
        self.add_button.pack(padx=20, pady=5)

        self.update_button = tk.Button(self.root, text="Kuva seadmed", command=self.list_devices)
        self.update_button.pack(padx=20, pady=5)

        self.update_status_button = tk.Button(self.root, text="Muuda seisundit", command=self.update_device_status)
        self.update_status_button.pack(padx=20, pady=5)

        self.remove_button = tk.Button(self.root, text="Kustuta seade", command=self.remove_device)
        self.remove_button.pack(padx=20, pady=5)

        self.save_button = tk.Button(self.root, text="Salvesta seadmed CSV", command=self.save_devices_csv)
        self.save_button.pack(padx=20, pady=5)

        self.load_button = tk.Button(self.root, text="Laadi seadmed CSV", command=self.load_devices_csv)
        self.load_button.pack(padx=20, pady=5)

        self.save_json_button = tk.Button(self.root, text="Salvesta seadmed JSON", command=self.save_devices_json)
        self.save_json_button.pack(padx=20, pady=5)

        self.load_json_button = tk.Button(self.root, text="Laadi seadmed JSON", command=self.load_devices_json)
        self.load_json_button.pack(padx=20, pady=5)

        self.list_devices()

    def add_device(self):
        name = simpledialog.askstring("Seadme nimi", "Sisesta seadme nimi:")
        device_type = simpledialog.askstring("Seadme tüüp", "Sisesta seadme tüüp:")
        status = simpledialog.askstring("Seisund", "Sisesta seisund (terve, katki, muu):")
        additional_field = simpledialog.askstring("Lisaväli", "Sisesta lisaväli (nt. asukoht):")

        device = Device(name, device_type, status, additional_field)
        self.device_manager.add_device(device)
        self.list_devices()
        messagebox.showinfo("Seade lisatud", f"Seade {name} on lisatud.")

    def list_devices(self):
        self.listbox.delete(0, tk.END)
        for device in self.device_manager.list_devices():
            self.listbox.insert(tk.END, str(device))

    def update_device_status(self):
        selected_device = self.listbox.curselection()
        if selected_device:
            device_name = self.listbox.get(selected_device[0]).split()[0]
            new_status = simpledialog.askstring("Uus seisund", "Sisesta uus seisund (terve, katki):")
            if self.device_manager.update_device_status(device_name, new_status):
                self.list_devices()
                messagebox.showinfo("Seisund muudetud", f"Seadme {device_name} seisund on nüüd {new_status}.")
            else:
                messagebox.showerror("Viga", f"Seadet {device_name} ei leitud.")
        else:
            messagebox.showerror("Viga", "Vali seade, mille seisundit muuta.")

    def remove_device(self):
        selected_device = self.listbox.curselection()
        if selected_device:
            device_name = self.listbox.get(selected_device[0]).split()[0]
            self.device_manager.remove_device(device_name)
            self.list_devices()
            messagebox.showinfo("Seade kustutatud", f"Seade {device_name} on kustutatud.")
        else:
            messagebox.showerror("Viga", "Vali seade, mis kustutada.")

    def save_devices_csv(self):
        filename = simpledialog.askstring("Failinimi", "Sisesta faili nimi (lõpp .csv):")
        if filename:
            self.device_manager.save_to_csv(filename)
            messagebox.showinfo("Andmed salvestatud", f"Seadmed on salvestatud faili {filename}.")

    def load_devices_csv(self):
        filename = simpledialog.askstring("Failinimi", "Sisesta faili nimi (lõpp .csv):")
        if filename:
            self.device_manager.load_from_csv(filename)
            self.list_devices()  # Kuvame uuesti seadmed
            messagebox.showinfo("Andmed laetud", f"Seadmed on laaditud failist {filename}.")

    def save_devices_json(self):
        filename = simpledialog.askstring("Failinimi", "Sisesta faili nimi (lõpp .json):")
        if filename:
            self.device_manager.save_to_json(filename)
            messagebox.showinfo("Andmed salvestatud", f"Seadmed on salvestatud faili {filename}.")

    def load_devices_json(self):
        filename = simpledialog.askstring("Failinimi", "Sisesta faili nimi (lõpp .json):")
        if filename:
            self.device_manager.load_from_json(filename)
            self.list_devices()  # Kuvame uuesti seadmed
            messagebox.showinfo("Andmed laetud", f"Seadmed on laaditud failist {filename}.")

# Rakenduse käivitamine
if __name__ == "__main__":
    root = tk.Tk()
    device_manager = DeviceManager()
    app = DeviceManagerGUI(root, device_manager)
    root.mainloop()
