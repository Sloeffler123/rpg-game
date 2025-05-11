
class Bows:
    def __init__(self, type, dmg):
        self.type = type
        self.damage = dmg
    def __str__(self):
        return self.type    

class Staffs(Bows):
    def __init__(self, type, dmg):
        super().__init__(type, dmg)

class Swords(Bows):
    def __init__(self, type, dmg):
        super().__init__(type, dmg)