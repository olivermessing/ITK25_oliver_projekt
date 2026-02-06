import json
from Device import Device
import csv

class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def list_devices(self):
        return self.devices

    def update_device_status(self, device_name, new_status):
        for device in self.devices:
            if device.name == device_name:
                device.status = new_status
                return True
        return False

    def remove_device(self, device_name):
        self.devices = [device for device in self.devices if device.name != device_name]

    def save_to_csv(self, filename):

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['name', 'device_type', 'status', 'additional_field'])
            for device in self.devices:
                writer.writerow([device.name, device.device_type, device.status, device.additional_field])

    def load_from_csv(self, filename):

        devices = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)  # Skip päiserida
                for row in reader:
                    device = Device(row[0], row[1], row[2], row[3])
                    devices.append(device)
            self.devices = devices
        except FileNotFoundError:
            print(f"CSV fail {filename} ei leitud.")

    def save_to_json(self, filename):

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([device.to_dict() for device in self.devices], file, ensure_ascii=False, indent=4)

    def load_from_json(self, filename):

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                devices = [Device(d['name'], d['device_type'], d['status'], d['additional_field']) for d in data]
                self.devices = devices
        except FileNotFoundError:
            print(f"JSON fail {filename} ei leitud.")
