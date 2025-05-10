from starter import player
from dungeon import spawn_chest_or_enemies
from enemies import Enemies
def attack_loop():
    check = spawn_chest_or_enemies()
    if check:
        while Enemies.total_enemeies:
            player.player_attack_inventory()
            player.attack_enemy(Enemies.total_enemeies)
            print('Its the enemies turn to attack')
            enemy = Enemies.total_enemeies[0]
            enemy.attack(player)
            print(f'You took {enemy.weapon} damage')
            for i in Enemies.total_enemeies:
                if i.health <= 0:
                    Enemies.total_enemeies.remove(i)
