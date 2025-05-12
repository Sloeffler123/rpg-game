import random
from knight import LONG_SWORD, long_sword_dmg
from wizard import MAGIC_STAFF, magic_staff_dmg
from hunter import LONG_BOW, long_bow_dmg

def random_weapon(stage):
    sword = Swords(LONG_SWORD, long_sword_dmg(stage))
    bow = Bows(LONG_BOW, long_bow_dmg(stage))
    staff = Staffs(MAGIC_STAFF, magic_staff_dmg(stage))
    weapons = [sword, bow, staff]
    weapon = random.choice(weapons)
    return weapon     

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