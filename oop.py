# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin):
        self._name = name  # Encapsulation: private attribute
        self._power = power  # Encapsulation: private attribute
        self._origin = origin  # Encapsulation: private attribute

    def display_info(self):
        return f"Name: {self._name}, Power: {self._power}, Origin: {self._origin}"

    # Method that can be overridden by subclasses
    def use_power(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass: Speedster
class Speedster(Superhero):
    def __init__(self, name, origin):
        super().__init__(name, "Super Speed", origin)

    def use_power(self):
        return f"{self._name} is running at the speed of light! ⚡"

# Subclass: Flyer
class Flyer(Superhero):
    def __init__(self, name, origin):
        super().__init__(name, "Flight", origin)

    def use_power(self):
        return f"{self._name} is soaring through the skies! 🦅"

# Subclass: Telepath
class Telepath(Superhero):
    def __init__(self, name, origin):
        super().__init__(name, "Telepathy", origin)

    def use_power(self):
        return f"{self._name} is communicating telepathically! 🧠"

# Creating instances of each subclass
flash = Speedster("Flash", "Earth-1")
superman = Flyer("Superman", "Kryptonian")
professor_x = Telepath("Professor X", "X-Mansion")

# Displaying information and using powers
print(flash.display_info())
print(flash.use_power())

print(superman.display_info())
print(superman.use_power())

print(professor_x.display_info())
print(professor_x.use_power())


#activity 2
# Base class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass: Car
class Car(Vehicle):
    def __init__(self, name, fuel_type):
        super().__init__(name)
        self.fuel_type = fuel_type

    def move(self):
        return f"{self.name} is driving on the road 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def __init__(self, name, airline):
        super().__init__(name)
        self.airline = airline

    def move(self):
        return f"{self.name} is flying in the sky ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def __init__(self, name, type_of_boat):
        super().__init__(name)
        self.type_of_boat = type_of_boat

    def move(self):
        return f"{self.name} is sailing on the water 🚤"

# Creating instances of each subclass
car = Car("Toyota Corolla", "Gasoline")
plane = Plane("Boeing 747", "Delta Airlines")
boat = Boat("Yacht", "Luxury")

# Demonstrating polymorphism
vehicles = [car, plane, boat]

for vehicle in vehicles:
    print(vehicle.move())
