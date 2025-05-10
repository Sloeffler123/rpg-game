
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
        self.name = name
        self.inventory = []
        self.level = 1
        self.gold = 0
        self.xp_bar = 0
    def check_inventory_space(self):
        if self.inventory == 15:
            print('To many items in your inventory')
            return False
        else:
            return True    
    def change_weapon(self, new_weapon):
        while True:
            if self.check_inventory_space():
                print(f'Storing {self.weapon} in inventory')
                self.inventory.append(self.weapon)
                self.weapon = new_weapon
                break   
            else:
                print('Please enter a valid option')  
                break
    def change_head_armour(self, new_head_gear):
        self.head_armour = new_head_gear    
    def change_chest_armour(self, chest_armour):
        self.middle_armour = chest_armour
    def change_leg_armour(self, leg_armour):
        self.lower_armour = leg_armour
    def attack(self, weapon, target):
        target.health -= weapon
    def delete_item_inventory(self, item):
        self.inventory.remove(item)
    def help_manual(self):
        print('Player can only change loadout when they are in there inventory.' \
        'Player can swap between what enemy they want to target.' \
        )
    def look_inventory(self):  
        print(f'Inventory: {self.inventory}')
        user_input = input('(D)elete item/(C)hange gear/(E)xit').lower()
        if user_input == 'd' or 'delete':
            while True:
                delete_item = input('What item would you like to delete from your inventory? (E)xit').lower()
                if delete_item in self.inventory:
                    print(f'Deleting {delete_item}')
                    self.delete_item_inventory(delete_item)   
                    break
                else:
                    print('Please enter a valid item') 
        elif user_input == 'c' or 'change':
            change_item = input('What item slot would you like to change? (W)eapon, (H)ead gear, (C)hest plate, (L)eg plate, (E)xit').lower()
            if change_item == 'w' or change_item == 'weapon':
                while True:
                    weapon_change = input('What weapon in your inventory would you like to swap with? (E)xit').lower()
                    print(f'Inventory: {self.inventory}')
                    if weapon_change in self.inventory:
                        self.change_weapon(weapon_change)
                        break
                    elif weapon_change == 'e' or weapon_change == 'exit':
                        break
                    else:
                        print('Please enter a valid option')    
            elif change_item == 'h' or change_item == 'head':
                while True:
                    head_armour = input('What head armour in your inventory would you like to swap with? ')
                    print(f'Inventory: {self.inventory}')
                    if head_armour in self.inventory:
                        self.change_head_armour(head_armour)
                        break
                    else:
                        print('Please enter a valid option')  
            elif change_item == 'c' or change_item == 'chest':
                while True:
                    chest_armour = input('What chest armour in your inventory would you like to swap with? ')   
                    print(f'Inventory: {self.inventory}')
                    if chest_armour in self.inventory:
                        self.change_chest_armour(chest_armour)
                        break
                    else:
                        print('Please enter a valid option')     
            elif change_item == 'l' or change_item == 'leg':
                while True:
                    leg_armour = input('What leg plate armour in your inventory would you like to swap with? ')   
                    print(f'Inventory: {self.inventory}')
                    if leg_armour in self.inventory:
                        self.change_leg_armour(leg_armour)
                        break
                    else:
                        print('Please enter a valid option')    
            elif change_item == 'e' or change_item == 'exit':
                pass                        
        elif user_input == 'e' or user_input == 'exit':
            pass
    def swap_enemies(self, target, enemies_lst):
        enemy = enemies_lst[target]
        enemies_lst.pop(enemy)
        enemies_lst.insert(0, enemy)
    def attack_enemy(self, enemies_lst):
        while True:
            print(enemies_lst)
            player_attack = int(input('Which enemy would you like to attack? '))
            if type(player_attack) == int:
                print(f'Attacking enemy {player_attack}')
                self.swap_enemies(player_attack)
                self.attack(self.weapon, enemies_lst[0])
                break
            else:
                print('Please enter the number of the positon of the enemy you would like to attack')    

