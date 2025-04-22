# question 1 - Superhero class
class Superhero:
    def __init__(self, name, power, energy_level=100):
        self._name = name
        self._power = power
        self._energy_level = energy_level
     # Getter for encapsulation
    @property
    def name(self):
        return self._name
    
    # method to use power
    def use_power(self):
        if self._energy_level >= 20:
            self._energy_level -= 20
            return f"{self._name} uses {self._power}! Energy left: {self._energy_level}"
        else:
            return f"{self._name} is too tired to use {self._power}."
    
    # method to rest and  recover energy
    def rest(self):
        self._energy_level = min(100, self._energy_level + 50)
        return f"{self._name} rests. Energy restored to {self._energy_level}."
    
    # method to describe superhero
    def describe(self):
        return f"{self._name} is a superhero with the power of {self._power}."
    
    #inherted class - flying superhero
class FlyingSuperhero(Superhero):
        def __init__(self, name, power, flight_speed, energy_level = 100):
            super().__init__(name, power, energy_level)
            self._flight_speed = flight_speed 

# overide use power to include flying
        def use_power(self):
            if self._energy_level >= 30:
                self._energy_level -= 30
                return f"{self._name} soars at {self._flight_speed} mph using {self._power}! Energy left: {self._energy_level}"
            else:
                return f"{self._name} is too tired to fly or use {self._power}."
        def fly(self):
            if self._energy_level >= 10:
                self._energy_level -= 10
                return f"{self._name} flies at {self._flight_speed} mph! Energy left: {self._energy_level}"
            else:
                return f"{self._name} is too tired to fly."
if __name__ =="__main__":
    # regular superhero
    spiderman = Superhero("Spider-man", "Web-slinging")
    print(spiderman.describe())
    print(spiderman.use_power())
    print(spiderman.rest())

    # flying superhero
    superman = FlyingSuperhero("Superman", "Super Strength", flight_speed=500)
    print(superman.describe())
    print(superman.use_power())
    print(superman.fly())


# Activity 2  - polymorphism challenge (Animals)
class Animal:
    def __init__(self,name):
        self.name = name
        # move method
    def move(self):
        return f"{self.name} is moving."
    
    #derived classes - Dog, Bird, Fish

class Dog(Animal):
    def move(self):
        return f"{self.name} is running on four legs."

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying in the sky."

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming in the water."

if __name__ =="__main__":
    animals = [Dog("Bosco"),
               Bird("Cheeky"),
               Fish("Meno")
    ]
    for animal in animals:
        print(animal.move())
   

