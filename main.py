# Nguyễn Hải Đăng - MSSV: 202418863

from src.device_factory import DeviceFactory
from src.home_configuration import HomeConfiguration


def main() -> None:
    light = DeviceFactory.create("light", "Living room light")
    fan = DeviceFactory.create("FAN", "Living room fan")
    door = DeviceFactory.create("door", "Main door")

    config1 = HomeConfiguration.instance()
    config2 = HomeConfiguration.instance()
    print(f"Same configuration: {config1 is config2}")
    print(f"Night light level: {config1.night_light_level}%")

    light.turn_on()
    fan.turn_off()
    door.lock()


if __name__ == "__main__":
    main()
