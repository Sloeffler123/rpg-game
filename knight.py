from wizard import Wizard
from hunter import Bows
# knight weapons
LONG_SWORD = 'Long sword'
RAPIER = 'Rapier'
KATANA = 'Katana'
# knight armour
KNIGHT_HELMET = 'Knight helmet'
KNIGHT_CHESTPLATE = 'Knight chestplate'
KNIGHT_LEGPLATES = 'Knight legplate'

# Sword damage
def long_sword_dmg(player_level):
    return 14 + player_level

def rapier_dmg(player_level):
    return 15 + player_level

def katana_dmg(player_level):
    return 16 + player_level

# knight armour
def knight_helmet_armour_dmg_reduction(player_level):
    return 5 + player_level

def knight_chestplate_dmg_reduction(player_level):
    return 5 + player_level

def knight_legplates_dmg_reduction(player_level):
    return 5 + player_level

class Swords(Bows):
    def __init__(self, type, dmg):
        super().__init__(type, dmg)


class Knight(Wizard):
    def __init__(self, health, weapon, head_armour, middle_armour, lower_armour, name):
        super().__init__(health, weapon, head_armour, middle_armour, lower_armour, name)


