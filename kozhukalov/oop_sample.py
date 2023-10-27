
class Pet:
    def __init__(self):
        self.name = "Unknown"
        self._vaccinated = False

    def get_name(self):
        return self.name

    def vaccinate(self):
        self._vaccinated = True

    def voice(self):
        return "silent"


class Cat(Pet):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def voice(self):
        return "meow"


class Dog(Pet):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        return "gav"


fish = Pet()

cat1 = Cat("vasya", 5, "main coon")
cat2 = Cat("murka", 3, "unknown")



dog = Dog("tuzik", 10)

print(cat1.voice())
print(fish.voice())
print(dog.voice())
