class Abductable:

    fear_coefficient = 1

    def __init__(self, fear_level=0):
        self.fear_level = fear_level

    def change_mood(self, num: int):
        self.fear_level += num * self.fear_coefficient

    def react(self):
        print("There is no such thing as a basic abductable.")


class Cow(Abductable):

    fear_coefficient = 2

    def __init__(self, name):
        self.name = name
        super().__init__(fear_level=3)

    def react(self):
        print("Moo!")

    @classmethod
    def make_herd(cls):
        return [cls("Bessie"), cls("Frank"), cls("Daisy"),
                cls("Big Macs")]

    @classmethod
    def update_fear_coefficient(cls, num):
        cls.fear_coefficient = num

class UFO:

    def __init__(self, capacity=5, storage=[]):
        self.capacity = capacity
        self.storage = storage

    def abduct(self, target: Abductable):

        # Check if we've got the space
        if len(self.storage) >= self.capacity:
            raise Exception("Cannot abduct; storage at capacity.")

        # The target's fear level will rise a lot
        target.change_mood(3)

        # The target will be stored in storage
        self.storage.append(target)

        # The target will react emotionally
        target.react()