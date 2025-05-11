import sys
STAGE = 1
# enemy armour 
head_armour_reduction = 1 + STAGE
chest_armour_reduciton = 2 + STAGE
leg_armour_recution = 2 + STAGE 

class Enemies:
    total_enemeies = []
    def __init__(self, health, weapon, name):
        self.health = health + STAGE
        self.weapon = weapon
        self.name = name
        # self.head = head
        # self.chest = chest
        # self.leg = leg
        Enemies.total_enemeies.append(self)
    
    def attack(self, target):
        print(f'{self}s turn to attack')
        target.health -= self.weapon.damage
        if target.health <= 0:
                print('You died')
                sys.exit(0)
        print(f'{target} took {self.weapon.damage} damage')
    def check_health(self):
        return self.health 
    def get_stats(self):
        print(f'{self.name}s stats: health: {self.health}, weapon: {self.weapon}')
    def __str__(self):
        return self.name     