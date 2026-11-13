# Nguyễn Hải Đăng - MSSV: 202418863

from src.device_factory import DeviceFactory


def main() -> None:
    light = DeviceFactory.create("light", "Living room light")
    fan = DeviceFactory.create("FAN", "Living room fan")
    door = DeviceFactory.create("door", "Main door")

    light.turn_on()
    fan.turn_off()
    door.lock()


if __name__ == "__main__":
    main()
