from abc import ABC, abstractmethod


class Mammal(ABC):
    @abstractmethod
    def speak():
        pass


class Walker(ABC):
    @abstractmethod
    def walk():
        pass


class Swimmer(ABC):
    @abstractmethod
    def swim():
        pass


class Human(Mammal, Walker, Swimmer):
    def speak():
        print("Humans can speak")

    def walk():
        print("Humans can walk")

    def swim():
        print("Humans can swim")


class Whale(Mammal, Swimmer):
    def speak():
        print("Whales can speak")

    def swim():
        print("Whales can swim")


if __name__ == "__main__":
    Human.speak()
    Human.walk()
    Human.swim()

    Whale.speak()
    Whale.swim()
