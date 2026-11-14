# Nguyễn Hải Đăng - MSSV: 202418863

from typing import cast

from src.device_factory import DeviceFactory
from src.devices import ILockable
from src.home_configuration import HomeConfiguration
from src.smart_home_facade import SmartHomeFacade


def main() -> None:
    light = DeviceFactory.create("light", "Living room light")
    fan = DeviceFactory.create("FAN", "Living room fan")
    door = DeviceFactory.create("door", "Main door")

    config1 = HomeConfiguration.instance()
    config2 = HomeConfiguration.instance()
    print(f"Same configuration: {config1 is config2}")
    print(f"Night light level: {config1.night_light_level}%")

    home = SmartHomeFacade(light, fan, cast(ILockable, door), config1)

    print("\n--- Go to work ---")
    home.go_to_work()
    print("\n--- Go to sleep ---")
    home.go_to_sleep()


if __name__ == "__main__":
    main()
