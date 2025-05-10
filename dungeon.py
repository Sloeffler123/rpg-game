import random
from enemies import Enemies, head_armour_reduction, leg_armour_recution, chest_armour_reduciton, STAGE
from knight import LONG_SWORD, long_sword_dmg
from weapons import Swords


def player_direction_choice():
    while True:
        user_input_direction = input('Which direction would you like to go? (L)eft, (S)traight, (R)ight ').lower()
        if user_input_direction in ('left', 'right', 'straight', 's', 'l', 'r'):
            break
        else:
            print('Please enter a valid option')
    return user_input_direction

def random_chance_armour(armour):
    random_num = (0, 9 + STAGE)
    if random_num >= 8:
        return armour
    else:
        return None

def make_enemies():
    random_num_enemies = random.randint(1, 1 + STAGE)
    weapon = Swords(LONG_SWORD, long_sword_dmg)
    for i in range(random_num_enemies):
        Enemies(10, weapon, random_chance_armour(head_armour_reduction), random_chance_armour(chest_armour_reduciton), random_chance_armour(leg_armour_recution))



