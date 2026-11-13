class HomeConfiguration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "home_name"):
            self.home_name = "My Home"
            self.night_light_level = 30

    @classmethod
    def instance(cls):
        return cls()
