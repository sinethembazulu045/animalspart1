from animals import Animal
class Cat(Animal):
    def __init__(self,name,eat, sounds):
        super().__init__(name,eat,sounds)

    def sound(self):
        print(self.sounds)
        return "{0}".format(self.sounds)
    
    def eats(self):
        print(self.eat)
        return "{0}".format(self.eat)


cat_1 =Cat("Cat","Food","Meow")  
cat_1.sound()