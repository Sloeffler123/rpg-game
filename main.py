from starter import player
from dungeon import entering_dungeon, player_direction_choice, random_loot_drop, make_enemies, spawn_chest, spawn_chest_or_enemies
from enemies import Enemies
print('\n')
print(f'Welcome {player.name}\n')
print('In these dungeons lies death and terror at every turn.\n')
print('It is your job to make it across the other side while obtaining any loot that might be valuable for yourself.\n')
print('Once entered the only options you have is going straight, left, or right unless other wise stated. You will not be allowed to exit the dungeon once entered so make sure you have the proper gear.\n')


# main game loop
on = True
while on:
    entering_dungeon()
    player_direction_choice()
    check = spawn_chest_or_enemies()
    if check:
        player_input = input('what would you like to do? (I)nventory, (A)ttack ').lower()
        if player_input == 'a' or player_input == 'attack':
            player.attack_enemy(Enemies.total_enemeies)
        elif player_input == 'i' or player_input == 'inventory':
            player.look_inventory()    
    else:
        print('\n')
        
