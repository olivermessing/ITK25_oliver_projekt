import json
from Device import Device

class JSONDataHandler:
    def __init__(self, filename):
        self.filename = filename

    def save(self, devices):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([device.to_dict() for device in devices], file, ensure_ascii=False, indent=4)

    def load(self):
        devices = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for device_data in data:
                    device = Device(device_data['name'], device_data['device_type'], device_data['status'], device_data['additional_field'])
                    devices.append(device)
        except FileNotFoundError:
            print(f"JSON fail {self.filename} ei leitud.")
        return devices


def dump(param, file, ensure_ascii, indent):
    return None


def load(file):
    return None

