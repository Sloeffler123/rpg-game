from starter import player
from dungeon import entering_dungeon, player_direction_choice, random_loot_drop, make_enemies, spawn_chest, spawn_chest_or_enemies
from enemies import Enemies
from intro import story
from attack_loop import attack_loop

story()
print('\n')
print(f'Welcome {player.name}\n')
print('In these dungeons lies death and terror at every turn.\n')
print('It is your job to make it across the other side while obtaining any loot that might be valuable for yourself.\n')
print('Once entered the only options you have is going straight, left, or right unless other wise stated. You will not be allowed to exit the dungeon once entered so make sure you have the proper gear.\n')

# main game loop
def main():
    # entering the dungeon print statement
    entering_dungeon()
    on = True
    while on:
        # asks the user what direction they want to go
        player_direction_choice()
        # player attacks
        attack_loop()   
main()