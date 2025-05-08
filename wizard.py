from hunter import Bows
# wizard weapons
MAGIC_STAFF = 'Magic staff'
FIRE_STAFF = 'Fire staff'
WATER_STAFF = 'Water staff'
LIGHTING_STAFF = 'Lighting staff'        

# wizard armour
WIZARD_HAT = 'Wizard hat'
WIZARD_ROBE = 'Wizard robe'
WIZARD_BOOTS = 'Wizard boots'

# Staff damage
def magic_staff_dmg(player_level):
    return 15 + player_level

def fire_staff_dmg(player_level):
    return 16 + player_level

def water_staff_dmg(player_level):
    return 16 + player_level

def lighting_staff_dmg(player_level):
    return 16 + player_level

# wizard armour
def wizard_hat_dmg_reduction(player_level):
    return 3 + player_level

def wizard_robe_dmg_reduction(player_level):
    return 4 + player_level

def wizard_boots_dmg_reduction(player_level):
    return 2 + player_level


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


class Staffs(Bows):
    def __init__(self, type, dmg):
        super().__init__(type, dmg)

