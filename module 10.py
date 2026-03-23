#############################     1     #####################
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
e = Elevator(1, 10)
e.go_to_floor(5)
e.go_to_floor(1)

#########################   2     ###############################

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)
b = Building(1, 10, 3)
b.run_elevator(0, 7)
b.run_elevator(1, 3)

########################     3    #####################

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("🔥 Fire alarm activated!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.elevators = []
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("🔥 Fire alarm activated!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

###########################    4     ########################

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.speed = max(0, car.speed + change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("Name\tSpeed\tDistance")
        for car in self.cars:
            print(f"{car.name}\t{car.speed}\t{car.distance:.2f}")

    def race_finished(self):
        return any(car.distance >= self.distance for car in self.cars)
cars = []
for i in range(10):
    cars.append(f"Car{i+1}")

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()
print("\n🏁 Race finished!")