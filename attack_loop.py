
def enemy_attack(player, random_loot_func, enemies_obj):
    enemies = enemies_obj.total_enemeies
    for enemy in enemies[:]:
        if enemy.health <= 0:
            input(f'You killed {enemy} (esc)')
            enemies.remove(enemy)
            random_loot_func(player)
        else:
            enemy.attack(player)

def attack_loop(player, chest_or_enemies, enemies_obj, weapon_func, stage, random_loot):
    check = chest_or_enemies
    if check:
        while enemies_obj.total_enemeies:
            player.player_attack_inventory()
            player.attack_enemy(enemies_obj.total_enemeies)
            enemy_attack(player, random_loot, enemies_obj)
 