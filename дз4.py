import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.is_clean = 50
        self.is_dirty = 50
        self.alive = True
    def eat(self):
        print(f"{self.name} їсть.")
        self.hunger += 20
        if self.hunger > 100:
            self.hunger = 100
        self.energy -= 5

    def sleep(self):
        print(f"{self.name} спить.")
        self.energy += 25
        if self.energy > 100:
            self.energy = 100
        self.hunger -= 20

    def play(self):
        print(f"{self.name} грається")
        self.happiness += 20
        if self.happiness > 100:
            self.happiness = 100
        self.energy -= 15
        self.hunger -= 20

    def take_a_shower(self):
        print(f"{self.name} миється.")
        self.energy -= 10
        self.happiness += 10
        self.is_clean += 20
        if self.is_clean > 100:
            self.is_clean = 100
        self.is_dirty -= 10


    def is_alive(self):
        if self.hunger <= 0:
            print(f"{self.name} помер з голоду...")
            self.alive = False
        elif self.energy <= 0:
            print(f"{self.name} перевтомився...")
            self.alive = False
        elif self.happiness <= 0:
            print(f"{self.name} занепав духом...")
            self.alive = False

    def show_status(self, day):
        print(f"\nДень {day}: Стан {self.name}")
        print(f"Голод: {self.hunger}")
        print(f"Енергія: {self.energy}")
        print(f"Щастя: {self.happiness}")
        print(f"Чистота: {self.is_clean}")

    def live_day(self, day):
        if not self.alive:
            return
        self.show_status(day)

        action = random.choice(['eat', 'sleep', 'play', 'take_a_shower'])
        if action == 'eat':
            self.eat()
        if action == 'sleep':
            self.sleep()
        if action == 'play':
            self.play()
        if action == 'take_a_shower':
            self.take_a_shower()

        self.is_alive()

my_pet = Pet("Беня")

for day in range(1, 10):
        if not my_pet.alive:
            break
        my_pet.live_day(day)