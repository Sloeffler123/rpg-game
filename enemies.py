
STAGE = 1

# enemy armour 
head_armour_reduction = 1 + STAGE
chest_armour_reduciton = 2 + STAGE
leg_armour_recution = 2 + STAGE 

class Enemies:
    total_enemeies = []
    def __init__(self, health, weapon):
        self.health = health + STAGE
        self.weapon = weapon
        # self.head = head
        # self.chest = chest
        # self.leg = leg
        Enemies.total_enemeies.append(self)
    
    def attack(self, target):
        target.health -= self.weapon.damage