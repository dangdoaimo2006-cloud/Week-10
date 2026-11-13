from abc import ABC, abstractmethod


class IDevice(ABC):
    def __init__(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Device name must not be empty.")
        self.name = name.strip()

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class ILockable(ABC):
    @abstractmethod
    def lock(self) -> None:
        pass

    @abstractmethod
    def unlock(self) -> None:
        pass


class SmartLight(IDevice):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.is_on = False

    def turn_on(self) -> None:
        self.is_on = True
        print(f"{self.name}: ON")

    def turn_off(self) -> None:
        self.is_on = False
        print(f"{self.name}: OFF")


class SmartFan(IDevice):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.is_on = False

    def turn_on(self) -> None:
        self.is_on = True
        print(f"{self.name}: ON")

    def turn_off(self) -> None:
        self.is_on = False
        print(f"{self.name}: OFF")


class SmartDoor(IDevice, ILockable):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.is_on = False
        self.is_locked = False

    def turn_on(self) -> None:
        self.is_on = True
        print(f"{self.name}: ON")

    def turn_off(self) -> None:
        self.is_on = False
        print(f"{self.name}: OFF")

    def lock(self) -> None:
        self.is_locked = True
        print(f"{self.name}: LOCKED")

    def unlock(self) -> None:
        self.is_locked = False
        print(f"{self.name}: UNLOCKED")
