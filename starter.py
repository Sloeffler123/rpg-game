#todo
#make the classes with there health and starting loadouts
#make a level increase method that increases there hp attack  and defense
#make a weapons class


import random

def starting_classes():
    pass
    # Wizard
    # Knight
    # Calvary
    # Hunter



# Weapons

# TODO
# make a change weapon method that switched the players current weapon
# figure out how to determine the damage output based off of type of weapon and level of player
# add a stats method that shows the stats of the weapon such as damage and special abilites
#

LONG_BOW = 'Long bow'
RECURIVED_BOW = 'Recurived bow'
CROSS_BOW = 'Cross bow'

MAGIC_STAFF = 'Magic staff'
FIRE_STAFF = 'Fire staff'
WATER_STAFF = 'Water staff'
LIGHTING_STAFF = 'Lighting staff'

LONG_SWORD = 'Long sword'
RAPIER = 'Rapier'
KATANA = 'Katana'

# Bow damage
def long_bow_dmg(player_level):
    return 14 + player_level

def recurived_bow_dmg(player_level):
    return 15 + player_level

def cross_bow(player_level):
    return 16 + player_level

# Staff damage
def magic_staff_dmg(player_level):
    return 15 + player_level

def fire_staff_dmg(player_level):
    return 16 + player_level

def water_staff_dmg(player_level):
    return 16 + player_level

def lighting_staff_dmg(player_level):
    return 16 + player_level

# Sword damage
def long_sword_dmg(player_level):
    return 14 + player_level

def rapier_dmg(player_level):
    return 15 + player_level

def katana_dmg(player_level):
    return 16 + player_level

def delete_weapon(weapon_class_object):
    del weapon_class_object

class Bows:
    def __init__(self, type, dmg):
        self.type = type
        self.damage = dmg
         

class Staffs(Bows):
    def __init__(self, type, ):
        super().__init__(type, )

class Swords(Bows):
    def __init__(self, type, ):
        super().__init__(type, )

# Armour

# TODO
# make a method that allows for the user to change gear
# make a del function that allows the user to delete any current gear they have
# 
class HeadArmour:
    def __init__(self, defence, special_stats, special_abilites):
        self.defence = defence
        self.special_stats = special_stats
        self.special_abilites = special_abilites

class ChestArmour(HeadArmour):
    def __init__(self, defence, special_stats, special_abilites):
        super().__init__(defence, special_stats, special_abilites)

class PantsArmour(HeadArmour):
    def __init__(self, defence, special_stats, special_abilites):
        super().__init__(defence, special_stats, special_abilites)


# Classes

# TODO
# This is where the player can change there gear
# make a method that allows the player to view their inventory and del stuff out of their inventory
# make a mehtod that allows the user to switch the char that is attacking
# make a method that allows the user to switch the enemy that is targeted

def starter_hunter():
    health = 150
    weapon = Bows(LONG_BOW, long_bow_dmg())
    head_armour = HeadArmour()


class Wizard:
    def __init__(self, health, weapon, head_armour, middle_armour, lower_armour, name):
        self.health = health
        self.weapon = weapon
        self.head_armour = head_armour
        self.middle_armour = middle_armour
        self.lower_armour = lower_armour
        self.inventory = []
        self.name = name
    def change_weapon(self, new_weapon):
        self.weapon = new_weapon    
    def attack(self, weapon, target):
        target.health -= weapon


class Knight(Wizard):
    def __init__(self, health, weapon, head_armour, middle_armour, lower_armour, name):
        super().__init__(health, weapon, head_armour, middle_armour, lower_armour, name)

class Hunter(Wizard):
    def __init__(self, health, weapon, head_armour, middle_armour, lower_armour, name):
        super().__init__(health, weapon, head_armour, middle_armour, lower_armour, name)


hunter = Hunter(250, 'Bow', )