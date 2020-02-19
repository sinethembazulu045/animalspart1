from animals import Animal
class Dog(Animal):
    def __init__(self,name,eat, sounds):
        super().__init__(name,eat,sounds)

    def sound(self):
        print(self.sounds)
        return "{0}".format(self.sounds)

    def eats(self):
        print(self.eat)
        return "{0}".format(self.eat)

dog_1 =Dog("Dog","Food", "Barks")
dog_1.sound()
