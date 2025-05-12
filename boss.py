from enemies import Enemies

class Boss(Enemies):
    def __init__(self, health, head, chest, leg, weapon, name):
        self.health = health
        self.head_armour = head
        self.chest_armour = chest
        self.leg_armour = leg
        self.weapon = weapon
        self.name = name
    def dialogue(self):
        input('HAHAHAHAHAHA (esc)')
        input('Who dares challenge the BIG BOSS? (esc)')
        input('Leave now or face your doom brave one. (esc)')
        input('Fine have it your way. (esc)')
    def __str__(self):
        return f'{self.name}'
# boss fight loop
def make_boss(knight_helm, knight_chest, knight_leg, weapon_func):
    input('The boss that protects this dungeon is up ahead... good luck brave one (esc)')
    boss = Boss(300, knight_helm, knight_chest, knight_leg, weapon_func, 'Big Boss')
    return boss

def boss_fight_loop(player, knight_helm, knight_chest, knight_leg, weapon_func):
    boss = make_boss(knight_helm, knight_chest, knight_leg, weapon_func)
    boss.dialogue()
    while boss.health > 0:
            player.player_attack_inventory()
            player.attack_boss(boss)
            boss.attack(player)
    print('You did it brave one. That evil monster has been terrorizing this dungeon for centuries.')        
