from wizard import Wizard
# hunter weapons
LONG_BOW = 'Long bow'
RECURIVED_BOW = 'Recurived bow'
CROSS_BOW = 'Cross bow'

# hunter armour
HUNTER_HOOD = 'Hunter hood'
HUNTER_CLOAK = 'Hunter cloak'
HUNTER_BOOTS = 'Hunter boots'

# Bow damage
def long_bow_dmg(player_level):
    return 14 + player_level

def recurived_bow_dmg(player_level):
    return 15 + player_level

def cross_bow(player_level):
    return 16 + player_level

# hunter armour
def hunter_hood_dmg_reduction(player_level):
    return 4 + player_level

def hunter_cloak_dmg_reduction(player_level):
    return 2 + player_level

def hunter_boots_dmg_reduction(player_level):
    return 3 + player_level

class Bows:
    def __init__(self, type, dmg):
        self.type = type
        self.damage = dmg


class Hunter(Wizard):
    def __init__(self, health, weapon, head_armour, middle_armour, lower_armour, name):
        super().__init__(health, weapon, head_armour, middle_armour, lower_armour, name)
