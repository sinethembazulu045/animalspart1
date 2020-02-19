class Animal:
    def __init__ (self, name,eat, sounds):
        self.name =name
        self.eat =eat
        self.sounds= sounds

    def eats(self):
        print(self.eat)
        return "{0}".format(self.eats)

    def sound(self):
        print(self.sounds)
        return "{0}".format(self.sounds)
    
dog = Animal("Dog", "Food","Barks")
cat = Animal("Cat", "Food","Meow")
dog.eats()
dog.sound() 

cat.eats()
cat.sound()
  