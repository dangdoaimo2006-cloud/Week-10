import unittest

from src.device_factory import DeviceFactory
from src.devices import SmartDoor, SmartFan, SmartLight
from src.home_configuration import HomeConfiguration


class DeviceFactoryTests(unittest.TestCase):
    def test_create_supported_devices(self):
        self.assertIsInstance(DeviceFactory.create("light", "Den phong khach"), SmartLight)
        self.assertIsInstance(DeviceFactory.create("fan", "Quat phong khach"), SmartFan)
        self.assertIsInstance(DeviceFactory.create("door", "Cua chinh"), SmartDoor)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            DeviceFactory.create("camera", "Camera")


class HomeConfigurationTests(unittest.TestCase):
    def test_instance_returns_same_configuration(self):
        config1 = HomeConfiguration.instance()
        config2 = HomeConfiguration.instance()
        self.assertIs(config1, config2)
        self.assertEqual(config1.night_light_level, 30)


if __name__ == "__main__":
    unittest.main()
