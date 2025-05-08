from hunter import Hunter, Bows, HUNTER_BOOTS,HUNTER_CLOAK, HUNTER_HOOD, LONG_BOW, CROSS_BOW, RECURIVED_BOW, hunter_hood_dmg_reduction, hunter_boots_dmg_reduction, hunter_cloak_dmg_reduction, long_bow_dmg, cross_bow, recurived_bow_dmg

from wizard import Wizard, Staffs, WIZARD_HAT, WIZARD_BOOTS, WIZARD_ROBE, MAGIC_STAFF, WATER_STAFF, LIGHTING_STAFF, FIRE_STAFF, wizard_boots_dmg_reduction, wizard_hat_dmg_reduction, wizard_robe_dmg_reduction, magic_staff_dmg, lighting_staff_dmg, water_staff_dmg, fire_staff_dmg

from knight import Knight, Swords, KNIGHT_HELMET, KNIGHT_CHESTPLATE, KNIGHT_LEGPLATES, KATANA, LONG_SWORD, RAPIER, knight_legplates_dmg_reduction, knight_chestplate_dmg_reduction, knight_helmet_armour_dmg_reduction, long_sword_dmg, rapier_dmg, katana_dmg


#todo
#make the classes with there health and starting loadouts
#make a level increase method that increases there hp attack  and defense
#make a weapons class


# Weapons

# TODO
# make a change weapon method that switched the players current weapon
# figure out how to determine the damage output based off of type of weapon and level of player
# add a stats method that shows the stats of the weapon such as damage and special abilites
#

def delete_weapon(weapon_class_object):
    del weapon_class_object

# Armour

# TODO
# make a method that allows for the user to change gear
# make a del function that allows the user to delete any current gear they have


class HeadArmour:
    def __init__(self, type, defence):
        self.defence = defence
        self.type = type

class ChestArmour(HeadArmour):
    def __init__(self, type, defence):
        super().__init__(defence)

class PantsArmour(HeadArmour):
    def __init__(self, type, defence):
        super().__init__(defence)


# Classes

# TODO
# This is where the player can change there gear
# make a method that allows the player to view their inventory and del stuff out of their inventory
# make a mehtod that allows the user to switch the char that is attacking
# make a method that allows the user to switch the enemy that is targeted

def starter_class():
    player_input = input('What class would you like to play')
    player_name = input('What should we call you')
    if player_input == 'h':
        health = 150
        weapon = Bows(LONG_BOW, long_bow_dmg())
        head_armour = HeadArmour(HUNTER_HOOD, hunter_hood_dmg_reduction())
        mid_armour = ChestArmour(HUNTER_CLOAK, hunter_cloak_dmg_reduction())
        low_armour = PantsArmour(HUNTER_BOOTS,hunter_boots_dmg_reduction())
        Hunter(health, weapon, head_armour, mid_armour, low_armour, player_name)
    elif player_input == 'w':
        health = 200
        weapon = Staffs(MAGIC_STAFF, magic_staff_dmg())
        head_armour = HeadArmour(WIZARD_HAT, wizard_hat_dmg_reduction())
        mid_armour = ChestArmour(WIZARD_ROBE, wizard_robe_dmg_reduction())
        low_armour = PantsArmour(WIZARD_BOOTS, wizard_boots_dmg_reduction())
        Wizard(health, weapon, head_armour, mid_armour, low_armour, player_name)
    elif player_input == 'k':
        health = 250
        weapon = Swords(LONG_SWORD, long_sword_dmg())
        head_armour = HeadArmour(KNIGHT_HELMET, knight_helmet_armour_dmg_reduction())  
        mid_armour = ChestArmour(KNIGHT_CHESTPLATE, knight_chestplate_dmg_reduction())
        low_armour = PantsArmour(KNIGHT_LEGPLATES, knight_legplates_dmg_reduction())
        Knight(health, weapon, head_armour, mid_armour, low_armour, player_name)
    
