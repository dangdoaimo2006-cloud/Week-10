import unittest
import contextlib
import io

from src.device_factory import DeviceFactory
from src.devices import SmartDoor, SmartFan, SmartLight
from src.home_configuration import HomeConfiguration
from src.smart_home_facade import SmartHomeFacade


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


class SmartHomeFacadeTests(unittest.TestCase):
    def setUp(self):
        self.light = SmartLight("Test light")
        self.fan = SmartFan("Test fan")
        self.door = SmartDoor("Test door")
        self.configuration = HomeConfiguration.instance()
        self.configuration.night_light_level = 25
        self.home = SmartHomeFacade(
            self.light, self.fan, self.door, self.configuration
        )

    def tearDown(self):
        self.configuration.night_light_level = 30

    def test_go_to_work(self):
        self.light.turn_on()
        self.fan.turn_on()
        with contextlib.redirect_stdout(io.StringIO()):
            self.home.go_to_work()
        self.assertFalse(self.light.is_on)
        self.assertFalse(self.fan.is_on)
        self.assertTrue(self.door.is_locked)

    def test_go_to_sleep(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.home.go_to_sleep()
        self.assertTrue(self.light.is_on)
        self.assertFalse(self.fan.is_on)
        self.assertTrue(self.door.is_locked)
        self.assertIn("Night light level: 25%", output.getvalue())


if __name__ == "__main__":
    unittest.main()
