from hunter import Hunter, HUNTER_BOOTS,HUNTER_CLOAK, HUNTER_HOOD, LONG_BOW, CROSS_BOW, RECURIVED_BOW, hunter_hood_dmg_reduction, hunter_boots_dmg_reduction, hunter_cloak_dmg_reduction, long_bow_dmg, cross_bow, recurived_bow_dmg

from wizard import Wizard, WIZARD_HAT, WIZARD_BOOTS, WIZARD_ROBE, MAGIC_STAFF, WATER_STAFF, LIGHTING_STAFF, FIRE_STAFF, wizard_boots_dmg_reduction, wizard_hat_dmg_reduction, wizard_robe_dmg_reduction, magic_staff_dmg, lighting_staff_dmg, water_staff_dmg, fire_staff_dmg

from knight import Knight, KNIGHT_HELMET, KNIGHT_CHESTPLATE, KNIGHT_LEGPLATES, KATANA, LONG_SWORD, RAPIER, knight_legplates_dmg_reduction, knight_chestplate_dmg_reduction, knight_helmet_armour_dmg_reduction, long_sword_dmg, rapier_dmg, katana_dmg

from armour import HeadArmour, ChestArmour, PantsArmour

from weapons import Bows, Swords, Staffs

def hunter_class(player_level, player_name):
    health = 150
    weapon = Bows(LONG_BOW, long_bow_dmg(player_level))
    head_armour = HeadArmour(HUNTER_HOOD, hunter_hood_dmg_reduction(player_level))
    mid_armour = ChestArmour(HUNTER_CLOAK, hunter_cloak_dmg_reduction(player_level))
    low_armour = PantsArmour(HUNTER_BOOTS,hunter_boots_dmg_reduction(player_level))
    return Hunter(health, weapon, head_armour, mid_armour, low_armour, player_name)

def wizard_class(player_level, player_name):
    health = 200
    weapon = Staffs(MAGIC_STAFF, magic_staff_dmg(player_level))
    head_armour = HeadArmour(WIZARD_HAT, wizard_hat_dmg_reduction(player_level))
    mid_armour = ChestArmour(WIZARD_ROBE, wizard_robe_dmg_reduction(player_level))
    low_armour = PantsArmour(WIZARD_BOOTS, wizard_boots_dmg_reduction(player_level))
    return Wizard(health, weapon, head_armour, mid_armour, low_armour, player_name)

def knight_class(player_level, player_name):
    health = 250
    weapon = Swords(LONG_SWORD, long_sword_dmg(player_level))
    head_armour = HeadArmour(KNIGHT_HELMET, knight_helmet_armour_dmg_reduction(player_level))  
    mid_armour = ChestArmour(KNIGHT_CHESTPLATE, knight_chestplate_dmg_reduction(player_level))
    low_armour = PantsArmour(KNIGHT_LEGPLATES, knight_legplates_dmg_reduction(player_level))
    return Knight(health, weapon, head_armour, mid_armour, low_armour, player_name)

def starter_class():
    while True:
        player_name = input('What should we call you \n').title()
        player_level = 1
        player_input = input('What class would you like to play? (W)izard, (H)unter, or (K)night: \n').lower()
        if player_input == 'h' or player_input == 'hunter':
            return hunter_class(player_level, player_name)
        elif player_input == 'w' or player_input == 'wizard':
            return wizard_class(player_level, player_name)
        elif player_input == 'k' or player_input == 'knight':
            return knight_class(player_level, player_name)
        else:
            print('Please enter a valid class')
    
player = starter_class()