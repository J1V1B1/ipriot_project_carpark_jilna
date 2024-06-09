class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.sensors = sensors or []
        self.capacity = capacity or []
        self.plates = plates or []
        self.displays = displays or []

    def __str__(self):
        return f"Location: {self.location}, Capacity: {self}"
