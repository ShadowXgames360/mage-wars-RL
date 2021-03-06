import map_functions as mpfn
import object_classes as obcl
import libtcodpy as libtcod
import ai_dictionary as aidic
import attack_dictionary as adic

#############################################################
# MONSTER DICTIONARY                                        #
# This file contains following:                             #
# 1. The function to create a monster                       #
# 2. Definitions for all monsters in the game.              #
#############################################################

################################
# 1: Monster Creation Function #
################################

def get_monster(title, x, y):
    arg = mons_dict[title]

    #get monster's attacks
    
    attacks = []
    if arg['attacks']:
        for atk in arg['attacks']:
            attacks.append(adic.get_attack(atk))

    #get monster's defense

    defense = [adic.get_defense(arg['defense'])]
    
    creature_component = obcl.Creature(
        hp = arg['life'],
        mana = arg['mana'],
        channeling = arg['channeling'],
        armor = arg['armor'],
        xp = arg['experience'],
        attacks = attacks,
        defense = defense,
        alignment = 'dungeon',
        death_function=obcl.monster_death)
    
    #ai_component = obcl.BasicMonster()
    ai = arg['ai']
    
    ai_component = aidic.Ai(ai['personality'],ai['traits'], ai['senses'])#aidic.ai_dict['traits'])
    monster = obcl.Object(
        x, y,
        traits = arg['traits'],
        properties = arg['properties'].copy(), #it is necessary to copy the dictionary, else all creatures will use the same dictionary.
        blocks=True, creature=creature_component, ai=ai_component)
    return monster

#########################
# 2: Monster Dictionary #
#########################

#error- creatures not appearing when they are supposed to. I think the levels are not being incremented.

mons_dict = {}

mons_dict['goblin grunt'] = {
    'spawn chance' : [
        {'level' : 1, 'value' : 40},
        {'level' : 2, 'value' : 10}],
    'life' : 4,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 0,
    'experience' : 20,
    'traits' : [],
    'attacks' : [{
        
        'name' : 'shortsword',
        'attack dice' : 3,
        'traits' : [],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],
    
    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'goblin grunt',
        'graphic' : 'g',
        'color' : libtcod.light_red,
        'level' : 1,
        'subtypes' : ['goblin', 'soldier'],
        'description' : 'The frontline troops of the Warlord are determined and enthusiastic, but easily killed with the first hit.'}}

mons_dict['goblin grunt'] = {
    'spawn chance' : [
        {'level' : 1, 'value' : 40},
        {'level' : 2, 'value' : 10}],
    'life' : 4,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 0,
    'experience' : 20,
    'traits' : [],
    'attacks' : [{
        
        'name' : 'shortsword',
        'attack dice' : 3,
        'traits' : [],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],
    
    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'goblin grunt',
        'graphic' : 'g',
        'color' : libtcod.light_red,
        'level' : 1,
        'subtypes' : ['goblin', 'soldier'],
        'description' : 'The frontline troops of the Warlord are determined and enthusiastic, but easily killed with the first hit.'}}

mons_dict['firebrand imp'] = {
    'spawn chance' : [
        {'level' : 1, 'value' : 10},
        {'level' : 2, 'value' : 40},
        {'level' : 3, 'value' : 20},],
    'life' : 6,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 0,
    'experience' : 40,
    'traits' : [['flame immunity']],
    'attacks' : [{
        
        'name' : 'hellfire claws',
        'attack dice' : 2,
        'traits' : [['flame'],['defrost']],
        'effects' : [[['burn'],8]],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],
    
    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'firebrand imp',
        'graphic' : 'i',
        'color' : libtcod.light_red,
        'level' : 1,
        'subtypes' : ['demon'],
        'description' : '...and there, silhouetted against the flames of the burning bodies, was the Firebrand Imp that had killed my men.\n  -Captain Klendel of Lonewall Keep'}}

mons_dict['bitterwood fox'] = {
    'spawn chance' : [
        {'level' : 1, 'value' : 30},
        {'level' : 2, 'value' : 20}],
        
    'life' : 5,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 0,
    'experience' : 35,
    'traits' : [['fast']],
    'attacks' : [{
        
        'name' : 'bite',
        'attack dice' : 3,
        'traits' : [],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],
    
    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'bitterwood fox',
        'graphic' : 'f',
        'color' : libtcod.light_red,
        'level' : 1,
        'subtypes' : ['animal', 'canine'],
        'description' : '\"Their meat is gamey and their teeth are sharp. It\'s best just to avoid them.\"\n  -Quelesta, Elven Ranger'}}

mons_dict['emerald tegu'] = {
    'spawn chance' : [
        {'level' : 2, 'value' : 10},
        {'level' : 3, 'value' : 30}],
    'life' : 8,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 3,
    'experience' : 35,
    'traits' : [],
    'attacks' : [{
        
        'name' : 'venomous bite',
        'attack dice' : 3,
        'traits' : [],
        'effects' : [[['rot'],8]],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],
    
    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'emerald tegu',
        'graphic' : 't',
        'color' : libtcod.dark_chartreuse,
        'level' : 2,
        'subtypes' : ['animal', 'reptile'],
        'description' : '\"Our spears snapped, as if twigs, against its hide. And when Dayel turned purple and choked on his own tongue, I knew its bite was poison.\"\n-Telgrin, Knight of Westlock'}}

mons_dict['death\'s head scorpion'] = {
    'spawn chance' : [
        {'level' : 2, 'value' : 10},
        {'level' : 3, 'value' : 30}],
    'life' : 6,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 4,
    'experience' : 60,
    'traits' : [],
    'attacks' : [{
        
        'name' : 'deadly stinger',
        'attack dice' : 1,
        'traits' : [['piercing +',2]],
        'effects' : [[['tainted','tainted'],8]],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'full', 'turns' : 4}},{

        'name' : 'pinchers',
        'attack dice' : 3,
        'traits' : [],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],
    
    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'death\'s head scorpion',
        'graphic' : 's',
        'color' : libtcod.black,
        'level' : 2,
        'subtypes' : ['insect'],
        'description' : '\"Rajan created its mark as a warning. One many do not heed.\"'}}

mons_dict['darkfenne hydra'] = {
    'spawn chance' : [
        {'level' : 3, 'value' : 5},
        {'level' : 5, 'value' : 20}],
    'life' : 15,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 1,
    'experience' : 100,
    'traits' : [['slow'],['regenerate ',2]],
    'attacks' : [{
        
        'name' : 'triple bite',
        'attack dice' : 3,
        'traits' : [['triplestrike']],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'full', 'turns' : 4}},{

        'name' : 'snapping bite',
        'attack dice' : 4,
        'traits' : [['counterstrike']],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],

    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'darkfenne hydra',
        'graphic' : 'H',
        'color' : libtcod.dark_red,
        'level' : 4,
        'subtypes' : ['serpent'],
        'description' : ''}}

mons_dict['stonegaze basilisk'] = {
    'spawn chance' : [
        {'level' : 2, 'value' : 10},
        {'level' : 3, 'value' : 20}],
    'life' : 10,
    'mana' : 0,
    'channeling' : 0,
    'armor' : 2,
    'experience' : 50,
    'traits' : [['slow']],
    'attacks' : [{
        
        'name' : 'paralysis beam',
        'attack dice' : 2,
        'traits' : [],
        'effects' : [[['cripple'],7]],
        'target type' : 'creature',
        'range' : {'type' : 'ranged', 'distance' : 6},
        'speed' : {'type' : 'full', 'turns' : 4}},{

        'name' : 'bite',
        'attack dice' : 4,
        'traits' : [],
        'effects' : [],
        'target type' : 'creature',
        'range' : {'type' : 'melee', 'distance' : 1},
        'speed' : {'type' : 'quick', 'turns' : 2}}],

    'defense' : None,
    'ai' : aidic.ai_dict['canine'],
    'properties' : {
        'name' : 'stonegaze basilisk',
        'graphic' : 'B',
        'color' : libtcod.dark_orange,
        'level' : 3,
        'subtypes' : ['reptile','lizard'],
        'description' : ''}}
