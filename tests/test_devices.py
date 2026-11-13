import unittest

from src.device_factory import DeviceFactory
from src.devices import SmartDoor, SmartFan, SmartLight


class DeviceFactoryTests(unittest.TestCase):
    def test_create_supported_devices(self):
        self.assertIsInstance(DeviceFactory.create("light", "Den phong khach"), SmartLight)
        self.assertIsInstance(DeviceFactory.create("fan", "Quat phong khach"), SmartFan)
        self.assertIsInstance(DeviceFactory.create("door", "Cua chinh"), SmartDoor)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            DeviceFactory.create("camera", "Camera")


if __name__ == "__main__":
    unittest.main()
