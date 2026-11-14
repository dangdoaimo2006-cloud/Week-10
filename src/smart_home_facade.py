from .devices import IDevice, ILockable
from .home_configuration import HomeConfiguration


class SmartHomeFacade:
    def __init__(
        self,
        light: IDevice,
        fan: IDevice,
        door: ILockable,
        configuration: HomeConfiguration | None = None,
    ):
        self.light = light
        self.fan = fan
        self.door = door
        self.configuration = configuration or HomeConfiguration.instance()

    def go_to_work(self):
        self.light.turn_off()
        self.fan.turn_off()
        self.door.lock()

    def go_to_sleep(self):
        self.fan.turn_off()
        self.door.lock()
        self.light.turn_on()
        print(f"Night light level: {self.configuration.night_light_level}%")
