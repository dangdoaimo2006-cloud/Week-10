from .devices import IDevice, SmartDoor, SmartFan, SmartLight


class DeviceFactory:
    @staticmethod
    def create(device_type: str, name: str) -> IDevice:
        normalized_type = device_type.strip().casefold()
        device_types: dict[str, type[IDevice]] = {
            "light": SmartLight,
            "fan": SmartFan,
            "door": SmartDoor,
        }
        device_class = device_types.get(normalized_type)
        if device_class is None:
            raise ValueError(f"Unsupported device type: {device_type}")
        return device_class(name)
