import random

def entering_dungeon():
    input('Entering dungeon... good luck brave one (esc)')
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

def make_enemies(enemies_obj, weapon_func, stage):
    random_num_enemies = random.randint(1, 1 + stage)
    print(f'You ran into {random_num_enemies} enemies')
    for i in range(random_num_enemies):
        enemy = enemies_obj(20, weapon_func, f'Enemy {i + 1}')
        enemy.get_stats()

def spawn_chest(player):
    print('You got a chest')
    player.gold += 10
    input('10 gold added (esc)')

def spawn_chest_or_enemies(player):
    random_num = random.randint(0,10)
    if random_num >= 9:
        print()
        spawn_chest(player)
        return False
    else:
        make_enemies()
        return True

def random_loot_drop(player):
    random_num = random.randint(0, 10)
    if random_num >= 8:
        print('dropped loot')
    else:
        player.gold += 1
        player.xp_bar += 2
   