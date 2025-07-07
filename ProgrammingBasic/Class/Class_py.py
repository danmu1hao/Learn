from abc import ABC, abstractmethod

class AnimalInfo:
    def __init__(self, name, species, age, lifespan):
        self.name = name
        self.species = species
        self.age = age
        self.lifespan = lifespan

class IShout(ABC):
    @abstractmethod
    def shout(self):
        pass

class Animal(IShout, ABC):
    def __init__(self, info):
        self.info = info
    @abstractmethod
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        print(f"{self.info.name}は飛びます。")
    def shout(self):
        print(f"{self.info.name}はピヨピヨと鳴きます。")

class Fish(Animal):
    def move(self):
        print(f"{self.info.name}は泳ぎます。")
    def shout(self):
        print(f"{self.info.name}はブクブクと鳴きます。")

class Rabbit(Animal):
    def move(self):
        print(f"{self.info.name}は走ります。")
    def shout(self):
        print(f"{self.info.name}はピョンピョンと鳴きます。")

bird_info = AnimalInfo("スズメ", "鳥", 1, 3)
fish_info = AnimalInfo("金魚", "魚", 2, 5)
rabbit_info = AnimalInfo("うさぎ", "哺乳類", 3, 8)

bird = Bird(bird_info)
fish = Fish(fish_info)
rabbit = Rabbit(rabbit_info)

bird.move(); bird.shout()
fish.move(); fish.shout()
rabbit.move(); rabbit.shout() 