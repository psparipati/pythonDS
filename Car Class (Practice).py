class Car:
    def __init__(self, fuel_tank_capacity, max_speed, mileage, fuel_level=0, speed=0):
        self.fuel_tank_capacity = fuel_tank_capacity
        self.max_speed = max_speed
        self.mileage = mileage
        self.fuel_level = fuel_level
        self.speed = speed

    def __ge__(self, other):
        return self.fuel_level >= other.fuel_level

    def __lt__(self, other):
        return self.fuel_level < other.fuel_level

    def __le__(self, other):
        return self.fuel_level <= other.fuel_level

    def __gt__(self, other):
        return self.fuel_level > other.fuel_level

    def __repr__(self):
        print(f"Car can hold {self.fuel_tank_capacity} gallons, but is currently at {self.fuel_level}.")
        print(f"Car can go upto {self.max_speed} mph but is currently at {self.speed} mph.")
        print(f"Car has {self.mileage} MPG as current fuel efficiency.")

    def fill_fuel(self, amount):
        self.fuel_level = min(self.fuel_level + amount, self.fuel_tank_capacity)
        return None

    def travel_by_time(self, time):
        if self.speed == 0:
            return None
        else:
            distance = time * self.speed
            max_distance = self.fuel_level * self.mileage  # Maximum distance based on fuel
            if distance > max_distance:
                distance = max_distance
            fuel_used = distance / self.mileage
            self.fuel_level -= fuel_used
            return distance

    def travel_by_distance(self, distance):
        max_distance = self.fuel_level * self.mileage
        if distance <= max_distance:
            actual_distance = distance
        else:
            actual_distance = max_distance
        self.fuel_level -= (actual_distance / self.mileage)
        return actual_distance

    def get_current_fuel(self):
        return self.fuel_level

    def can_travel_distance(self, distance):
        max_distance = self.fuel_level * self.mileage
        return distance <= max_distance

    def accelerate(self, accelerate_speed=5):
        self.speed = self.speed + accelerate_speed

    def brake(self, brake_speed=5):
        self.speed = self.speed - brake_speed


def test_car1():
    car = Car(fuel_tank_capacity=13, max_speed=120, mileage=30, fuel_level=5)

    assert car.get_current_fuel() == 5, "Initial fuel amount should be 5 gallons."
    car.fill_fuel(4)
    assert car.get_current_fuel() == 9, "Fuel amount should be 9 gallons after filling 4 gallons."

    car.accelerate()
    assert car.speed == 5, "Speed should be 5 mph after accelerating."
    car.accelerate(50)
    assert car.speed == 55, "Speed should be 55 mph after accelerating by 50."

    car.brake()
    assert car.speed == 50, "Speed should be 50 mph after braking."
    car.brake()
    assert car.speed == 45, "Speed should be 45 mph after braking."

    distance_travelled = car.travel_by_time(2)  # Travel for 2 hours
    assert distance_travelled == 90, "Car should have traveled 90 miles."

    assert car.get_current_fuel() == 6, "Fuel should be reduced after traveling."

    assert car.can_travel_distance(25), "Car should be able to travel 25 miles."
    assert not car.can_travel_distance(500), "Car should not be able to travel 500 miles with current fuel."

    print("All tests passed.")


if __name__ == "__main__":
    test_car1()
