
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
        self.level = 1
    def check_inventory_space(self):
        if self.inventory == 15:
            print('To many items in your inventory')
            return False
        else:
            return True    
    def change_weapon(self, new_weapon):
        on = True
        while on:
            player_input = input('Would you like to delete your current weapon or put it in your inventory? (D)elete, (I)nventory').lower()
            if player_input == 'd' or player_input == 'delete':
                print(f'Deleting {self.weapon}')
                self.weapon = new_weapon
            elif player_input == 'i' or player_input == 'inventory':
                if self.check_inventory_space():
                    print(f'Storing {self.weapon} in inventory')
                    self.inventory.append(self.weapon)
                    self.weapon = new_weapon
                else:
                    break    
            else:
                print('Please enter a valid option')  
    def attack(self, weapon, target):
        target.health -= weapon
    def delete_item_inventory(self, item):
        self.inventory.remove(item)
    def change_head_armour(self, new_head_gear):
        if self.check_inventory_space():
            self.head_armour = new_head_gear    
    def help_manual(self):
        pass
    def look_inventory(self):
        print(self.inventory)
        user_input = input('(D)elete item/(C)hange gear/(E)xit').lower()
        if user_input == 'd' or 'delete':
            self.delete_item_inventory()
