from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")
    entry_sensor = EntrySensor(1, True, car_park)
    exit_sensor = ExitSensor(2, True, car_park)
    display = Display(1, "Welcome to Moondalup", True, car_park)

    for i in range(10):
        entry_sensor.detect_vehicle()

    for i in range(2):
        exit_sensor.detect_vehicle()

if __name__ == "__main__":
    main()
