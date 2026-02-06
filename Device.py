
class Device:
    def __init__(self, name, device_type, status, additional_field):
        self.name = name
        self.device_type = device_type
        self.status = status
        self.additional_field = additional_field

    def __str__(self):
        return f"{self.name} ({self.device_type}) - {self.status}, {self.additional_field}"

    def to_dict(self):

        return {
            'name': self.name,
            'device_type': self.device_type,
            'status': self.status,
            'additional_field': self.additional_field
        }
