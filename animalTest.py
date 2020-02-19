import unittest
from animals import Animal
from cat import Cat
from dog import Dog

class testAnimal(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.dog_1 = Animal("Dog", "Food","Barks")
        self.cat_1 = Animal("Cat", "Food","Meow")


    def testDogSound(self):
        print("testDogSounds")
        self.assertEqual(self.dog_1.sounds,'Barks')

    def testDogEats(self):
        print("testDogEats")
        self.assertEqual(self.dog_1.eat,'Food')

    def testCatSound(self):
        print("testCatSounds")
        self.assertEqual(self.cat_1.sounds,'Meow')

    def testCatEats(self):
        print("testCatEats")
        self.assertEqual(self.dog_1.eat,'Food')

    

if __name__ == "__main__":
    unittest.main()