class Sensor:
    def __init__(self, id=None, is_active, car_park=None):
        self.id = id or []
        self.is_active = is_active
        self.car_park = car_park or []

    def __str__(self):
        return f"Sensor(id={self.id}, is_active={self}"

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    pass
