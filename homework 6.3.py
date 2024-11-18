import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
     self._cords = [0, 0, 0]
     self.speed = speed
    def move(self, dx, dy, dz):
        x = self._cords[0] + dx * self.speed
        y = self._cords[1] + dy * self.speed
        z = self._cords[2] + dz * self.speed
        if z < 0:
            print(f"It's too deep, i can't dive")
        else:
            self._cords[0] = x
            self._cords[1] = y
            self._cords[2] = z
    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful")
        elif self._DEGREE_OF_DANGER == 5 or self._DEGREE_OF_DANGER > 5:
            print(f"Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        numbers = [1,2,3,4]
        lay_eggs = random.choice(numbers)
        print(f'Here are(is) {lay_eggs}  eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self._cords[2] -= abs(dz * self.speed) / 2

class PoisonousAnimal(Animal):
    DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = 'Click-click-click'
    def speak(self):
        print(self.sound)



db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()








