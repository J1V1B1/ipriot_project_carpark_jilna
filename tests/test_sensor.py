import unittest
from sensor import EntrySensor, ExitSensor, CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Test Location", 100)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_entry_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_active, True)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)

    def test_exit_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_active, True)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)

    def test_detect_vehicle_entry_sensor(self):
        initial_bays = self.car_park.available_bays
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, initial_bays + 1)

    def test_detect_vehicle_exit_sensor(self):
        initial_bays = self.car_park.available_bays
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, initial_bays - 1)

if __name__ == '__main__':
    unittest.main()
