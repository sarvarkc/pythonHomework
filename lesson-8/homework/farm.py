class Animal:
    def __init__(self, num):
        self.num = num

    def eat(self):
        if self == cow:
            return 'Cow eats grass'
        elif self == chicken:
            return 'Chicken eata its own food'
        elif self == dog:
            return 'Dog eats meat'
class Cow(Animal):
    def __init__(self, num):
        super().__init__(num)

    def sound(self):
        return "Cow says 'Moo'"
    
    def left(self):
        if self.num > 0:
            return f"There are {self.num} cows left"
        return "Number can't be negative"

class Chicken(Animal):
    def __init__(self, num):
        super().__init__(num)

    def sound(self):
        return "Chicken says 'Hello World'"
    
    def left(self):
        if self.num > 0:
            return f"There are {self.num} chickens left"
        return "Number can't be negative"

class Dog(Animal):
    def __init__(self, num):
        super().__init__(num)

    def sound(self):
        return "Dog says 'Gaf'"

    def left(self):
        if self.num > 0:
            return f"There are {self.num} dogs left"
        return "Number can't be negative"
cow = Cow(50000)
chicken = Chicken(1)
dog = Dog(7777777)

print(cow.sound())
print(cow.eat())
print(cow.left())
print(chicken.eat())