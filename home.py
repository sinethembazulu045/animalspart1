from animals import Animal
from cat import Cat
from dog import Dog
class Home:
    def __init__(self, pets=[]):
        self.pets =pets
    def Adopt_pets(self, pet):
        for each in self.pets:
            if each == pet:
                raise Exception ("you cann't adopt 2 pets")
        self.pets.append(pet)


if __name__=="__main__":
    home = Home()
    dog_1 =Dog("Rax", "barks")
    cat_1 = Cat("Stormy", " meows")
    home.Adopt_pets(dog_1)
    home.Adopt_pets(cat_1)
    print(home.pets[0].name)
    print(home.pets[1].name)