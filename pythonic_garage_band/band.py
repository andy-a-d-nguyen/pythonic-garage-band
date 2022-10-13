from abc import ABC


class Musician(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{super().__str__()} and I play guitar"

    @staticmethod
    def get_instrument():
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{super().__str__()} and I play drums"

    @staticmethod
    def get_instrument():
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"{super().__str__()} and I play bass"

    @staticmethod
    def get_instrument():
        return "bass"

    @staticmethod
    def play_solo():
        return "bom bom buh bom"


class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"{self.__class__.__name__} name is {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances
