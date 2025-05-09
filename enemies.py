
class Enemies:
    total_enemeies = []
    def __init__(self, health, weapon, head, chest, leg):
        self.health = health
        self.weapon = weapon
        self.head = head
        self.chest = chest
        self.leg = leg
        Enemies.total_enemeies.append(self)
    
    def attack(self, target):
        target.health -= self.weapon

    
    