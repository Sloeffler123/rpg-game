from starter import player
from dungeon import spawn_chest_or_enemies
from enemies import Enemies
from dungeon import random_loot_drop
def enemy_attack():
    enemies = Enemies.total_enemeies
    for enemy in enemies[:]:
        if enemy.health <= 0:
            print(f'You killed {enemy}')
            enemies.remove(enemy)
            random_loot_drop()
        else:
            enemy.attack(player)

def attack_loop():
    check = spawn_chest_or_enemies()
    if check:
        while Enemies.total_enemeies:
            player.player_attack_inventory()
            player.attack_enemy(Enemies.total_enemeies)
            enemy_attack()
