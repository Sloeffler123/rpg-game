import random
from enemies import Enemies, STAGE
from knight import LONG_SWORD, long_sword_dmg
from weapons import Swords
from starter import player

def entering_dungeon():
    print('Entering dungeon... good luck brave one')
    print('\n')

def player_direction_choice():
    while True:
        user_input_direction = input('Which direction would you like to go? (L)eft, (S)traight, (R)ight ').lower()
        if user_input_direction in ('left', 'right', 'straight', 's', 'l', 'r'):
            break
        else:
            print('Please enter a valid option')
    return user_input_direction

# def random_chance_armour(armour):
#     random_num = (0, 9 + STAGE)
#     if random_num >= 8:
#         return armour
#     else:
#         return None

def make_enemies():
    random_num_enemies = random.randint(1, 1 + STAGE)
    weapon = Swords(LONG_SWORD, long_sword_dmg)
    print(f'You ran into {random_num_enemies} enemies')
    count = 1
    for _ in range(random_num_enemies):
        enemy = Enemies(10, weapon)
        print(f'Enemy {count} stats: {enemy}')
        count += 1

def spawn_chest():
    print('You got a chest')
    print('10 gold added')

def spawn_chest_or_enemies():
    random_num = random.randint(0,10)
    if random_num >= 9:
        spawn_chest()
        return False
    else:
        make_enemies()
        return True

def random_loot_drop():
    random_num = random.randint(0, 10)
    if random_num >= 8:
        print('dropped loot')
    else:
        player.gold += 1
        player.xp_bar += 2