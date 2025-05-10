
class HeadArmour:
    def __init__(self, type, defence):
        self.defence = defence
        self.type = type

class ChestArmour(HeadArmour):
    def __init__(self, type, defence):
        super().__init__(type, defence)

class PantsArmour(HeadArmour):
    def __init__(self, type, defence):
        super().__init__(type, defence)

