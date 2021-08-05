## this file declares all the functions used in the engine

init -6 python:
    if 'mouseup_2' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('mouseup_2')
    if 'h' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('h')
    if 'mouseup_3' in config.keymap['game_menu']:
        config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['screenshot'] = ['s']

    import math
    import os, os.path
    from copy import copy,deepcopy
    
    #FULL_PATH = "I:/renpy/renpy-6.99.3-sdk/Sunrider Liberation Day/game/" #as used by os.listdir. probably needs to be changed when the game is built!

    def get_modified_damage(damage,faction):
        #implementing difficulty setting.
        Difficulty = store.Difficulty #to be safe

        if Difficulty == 0: #VNmode
            if faction == 'Player':
                damage = int(damage * 0.25)
            else:
                damage = int(damage * 4)

        elif Difficulty == 1: #Casual mode
            if faction == 'Player':
                damage = int(damage * 0.50)
            else:
                damage = int(damage * 2)

        elif Difficulty == 2: #Ensign
            if faction == 'Player':
                damage = int(damage * 0.75)
            else:
                damage = int(damage * 1.33)

        elif Difficulty == 3: #Captain
            pass
            # if faction == 'Player':
                # damage = int(damage * 1.0)
            # else:
                # damage = int(damage * 1.0)

        elif Difficulty == 4: #Hard
            if faction == 'Player':
                damage = int(damage * 1.33)
            else:
                damage = int(damage * 0.75)

        elif Difficulty == 5: #Space Whale Mode
            if faction == 'Player':
                damage = int(damage * 2)
            else:
                damage = int(damage * 0.50)

        return damage

    def reset_upgrades(ship):
        if ship == None:
            return
        money_returned = 0
        upgrades = ship.upgrades
        for key in upgrades:
            name,level,increase,cost,multiplier = upgrades[key]
            if level > 1:
                for count in range(level-1):
                    cost = int(round(cost / float(multiplier) ))
                    money_returned += cost
                    new_value = getattr(ship,key)-increase
                    setattr(ship,key,new_value)
        tempship = copy(ship)
        tempship.__init__()
        ship.upgrades = tempship.upgrades
        BM.intel += money_returned

    def update_upgrades(ship):
        if ship == None:
            return
        
        # make a backup of the current upgrade level and player intel
        original_intel = BM.intel
        upgrades = copy(ship.upgrades)
        
        # reset upgrades to level 1
        for key in upgrades:
            name,level,increase,cost,multiplier = upgrades[key]
            if key in ship.upgrades:
                for count in range(level-1):
                    reverse_upgrade(ship, key)
        
        # calculate the amount of intel used to originally purchase the upgrades
        BM.intel = 1000000000
        for key in upgrades:
            name,level,increase,cost,multiplier = upgrades[key]
            if key in ship.upgrades:
                for count in range(level-1):
                    process_upgrade(ship, key)
        old_cost = 1000000000 - BM.intel
        
        # calculate the new cost to purchase the upgrades and update upgrades to the latest version
        reset_upgrades(ship)
        BM.intel = 1000000000
        for key in upgrades:
            name,level,increase,cost,multiplier = upgrades[key]
            if key in ship.upgrades:
                for count in range(level-1):
                    process_upgrade(ship, key)
        new_cost = 1000000000 - BM.intel
        
        # update player intel to the correct cost
        BM.intel = original_intel + old_cost - new_cost
        
        #I don't really want people ending up with negative intel after an update
        if BM.intel < 0:
            BM.intel = 0

    def process_upgrade(ship, upgrade, min_level=None):
        if min_level is None:
            name,level,increase,cost,multiplier = ship.upgrades[upgrade]
            if BM.intel >= cost or BM.mission == 'skirmish':  #sanity check
                renpy.music.play('sound/upgrade_purchase.ogg',channel = 'sound1')
                if not BM.mission == 'skirmish':
                    BM.intel -= cost
                new_value = getattr(ship,upgrade)+increase
                setattr(ship,upgrade,new_value)
                level += 1
                cost = int(round(cost * multiplier))
                ship.upgrades[upgrade] = [name,level,increase,cost,multiplier]
                BM.active_upgrade = ship.upgrades[upgrade]
                max_stats()
                chivo_process("Isn't it Sad, Chigara?")
                return
            else:
                renpy.music.play('sound/Voice/chi_Others_03.ogg',channel = 'chivoice') #not enough money
                return
        else:
            while ship.upgrades[upgrade][1] < min_level:
                name,level,increase,cost,multiplier = ship.upgrades[upgrade]
                new_value = getattr(ship,upgrade)+increase
                setattr(ship,upgrade,new_value)
                level += 1
                cost = int(round(cost * multiplier))
                ship.upgrades[upgrade] = [name,level,increase,cost,multiplier]
            max_stats()            
            return

    def reverse_upgrade(ship, upgrade):
        renpy.music.play('sound/beep2.ogg',channel = 'sound2')
        name,level,increase,cost,multiplier = ship.upgrades[upgrade]
        level -= 1
        cost = int(round(cost / multiplier))
        if not BM.mission == 'skirmish': #better safe than sorry
            BM.intel += cost
        new_value = getattr(ship,upgrade)-increase
        setattr(ship,upgrade,new_value)
        ship.upgrades[upgrade] = [name,level,increase,cost,multiplier]
        BM.active_upgrade = ship.upgrades[upgrade]
        max_stats()        
        return

    def max_stats():
        for ship in player_ships:
            ship.hp = ship.max_hp
            ship.en = ship.max_en
            ship.missiles = ship.max_missiles
            # ship.rockets = ship.max_rockets
        return
        
    
    def buy_upgrades():  #defunct
        renpy.show_screen('upgrade')
        active = True
        renpy.music.play('sound/Voice/Chigara/Others Line 1.ogg',channel = 'chivoice')

        while active:
            result = ui.interact()

            if result[0] == 'quit':
                renpy.hide_screen('upgrade')

                voicelist = [
                    'sound/Voice/Chigara/Others Line 2.ogg',
                    'sound/Voice/Chigara/Others Line 3.ogg'
                    ]
                renpy.music.play(renpy.random.choice(voicelist),channel = 'chivoice')

                for ship in player_ships:
                    ship.hp = ship.max_hp
                    ship.en = ship.max_en
                    ship.missiles = ship.max_missiles
                active = False
                return

            elif result[0] == 'reset':
                reset_upgrades(BM.selected)

            elif result[0] == 'update':
                update_upgrades(BM.selected)

            elif result != None:
                if result[0] == '+':
                    process_upgrade(BM.selected, result[1])

                elif result[0] == '-':
                    reverse_upgrade(BM.selected, result[1])
                    renpy.music.play('sound/upgrade_sell.ogg',channel = 'sound2')

    def battlemode():
        BM.battlemode = True
        renpy.start_predict_screen('battle_screen')
        renpy.free_memory()
        config.rollback_enabled = False
        if BM.show_battle_log:
            renpy.show_screen('battle_log')

    def VNmode():
        BM.battlemode = False
        renpy.stop_predict_screen('battle_screen')
        config.rollback_enabled = True
        if BM.show_battle_log:
            renpy.hide_screen('battle_log')
            BM.show_battle_log = False

    def instant_win():
        temp_list = enemy_ships[:]
        for ship in temp_list:
            ship.destroy(sunrider,no_cmd = True,no_animation=True)
            if ship.boss:
                return

    def apply_modifier(target,modifier,magnitude,duration, cumulative = False):
        """attempts to apply a buff or a curse and return True on success, False on failure"""
        if target == None:
            return False
        if not hasattr(target,'modifiers'):
            return False

        if cumulative:
            current_magnitude, current_duration = target.modifiers[modifier]
            magnitude += current_magnitude
            # don't extend ongoing buff duration further than duration + 1
            # TODO extension limit should probably be a property of the buff object instead of this magic formula
            new_duration = min(duration + current_duration, duration + 1)
            new_duration = max(current_duration, new_duration) 
            
            target.modifiers[modifier] = [magnitude,new_duration]
            return True

        if magnitude > 0:  #I may have to make a better check at some point
            #buffs
            if modifier in target.modifiers:
                if target.modifiers[modifier][0] > magnitude:
                    return False
                elif target.modifiers[modifier][0] == magnitude:
                    if target.modifiers[modifier][1] >= duration:
                        return False
        else:
            #curses
            if modifier in target.modifiers:
                if target.modifiers[modifier][0] < magnitude:
                    return False
                elif target.modifiers[modifier][0] == magnitude:
                    if target.modifiers[modifier][1] >= duration:
                        return False
        target.modifiers[modifier] = [magnitude,duration]
        return True

    def clean_grid():
        BM.grid = []
        BM.ships = []
        BM.covers = []
        store.enemy_ships = []

        for a in range(GRID_SIZE[0]):
                BM.grid.append([False]*GRID_SIZE[1])
        for ship in player_ships:
            BM.ships.append(ship)

    def add_enemy_list():
        store.all_enemies = [
            PactBomber(),  PactMook(),
            MissileFrigate(), PactCruiser(),
            PactCarrier(), PactOutpost(),
            PactBattleship(),RyuvianCruiser(),
            Havoc(), PirateBomber(),
            PirateGrunt(), PirateDestroyer(),
            PirateBase()
            ]
        for ship in store.all_enemies:
            ship.location = None

    def set_weapon_parent(weapon):
        for ship in BM.ships:
            if weapon in ship.weapons:
                weapon.parent = ship
                return
                
    def get_modified_accuracy(weapon):
        if weapon is None: return 0
        if weapon.parent is None: set_weapon_parent(weapon)
        attacker = weapon.parent
        accuracy = weapon.accuracy
        
        wtype = get_weapon_type(weapon)
        if wtype == 'Kinetic': accuracy *= attacker.kinetic_acc
        elif wtype == 'Energy': accuracy *= attacker.energy_acc
        elif wtype == 'Melee': accuracy *= attacker.melee_acc
        
        return int(accuracy)
        
    #drat this and the real_damage function are doubles
    def get_modified_weapon_damage(weapon):
        if weapon is None: return 0
        if weapon.parent is None: set_weapon_parent(weapon)
        attacker = weapon.parent
        if attacker is None: return 0
        damage = weapon.damage
        
        wtype = get_weapon_type(weapon)
        if wtype == 'Kinetic': damage *= attacker.kinetic_dmg
        elif wtype == 'Energy': damage *= attacker.energy_dmg
        elif wtype == 'Melee': damage *= attacker.melee_dmg
        elif wtype == 'Missile': damage *= attacker.missile_dmg
        
        return int(damage)   

    def real_damage(weapon,parent):
        if weapon == None or parent == None:
            return 0
        wtype = get_weapon_type(weapon)
        if wtype == 'Kinetic':
            return int(weapon.damage*parent.kinetic_dmg)
        elif wtype == 'Energy':
            return int(weapon.damage*parent.energy_dmg)
        elif wtype == 'Missile':
            return int(weapon.damage*parent.missile_dmg)
        elif wtype == 'Melee':
            return int(weapon.damage*parent.melee_dmg)
        else:
            return 0        
    
    def get_acc(weapon, attacker, target, guess = False, range_reduction = 0,custom_range=0): #calculate the chance to hit an enemy ship
        if hasattr(weapon,'max_range'): 
            if weapon.max_range and custom_range == 0:  #if this value is not None, False or 0.
                if get_ship_distance(attacker,target) > weapon.max_range: return 0

        accuracy = weapon.accuracy

        #upgrades modify the base stat
        wtype = get_weapon_type(weapon)
        if wtype == 'Kinetic': accuracy *= attacker.kinetic_acc
        elif wtype == 'Energy': accuracy *= attacker.energy_acc
        elif wtype == 'Melee': accuracy *= attacker.melee_acc
        else: pass

        #subtract the targets evasion from accuracy.
        accuracy -= target.evasion 
        
        #AI gets some fudging.
        if guess:
            accuracy += renpy.random.randint(-10,10)

        #an acc. buff is added as a flat bonus
        if not weapon.wtype == 'Support' or weapon.wtype == 'Curse':
            accuracy += attacker.modifiers['accuracy'][0]

        #accuracy degrades over distance based on a weapon stat. missiles and rockets usually degrade much more slowly
        if custom_range:
            distance = custom_range
        else:
            distance = (max(get_ship_distance(attacker,target) - range_reduction,1))
        accuracy += weapon.base_accuracy - (weapon.acc_degradation * distance)

        #environmental effects are added
        accuracy *= BM.environment['accuracy'] / 100.0

        if accuracy > 100: return 100
        if accuracy < 0.0: return 0
        return int(accuracy)

    def get_cell_available(location):
        '''Returns True is a space is free - False if it is not'''
        if location != None:
            a,b = location
            X,Y = GRID_SIZE
            if a > 0 and a <= X and b > 0 and b <= Y:
                try:
                    if BM.grid[a-1][b-1]:
                        return False
                    else:
                        return True
                except:
                    return False
            else:
                return False #out of bounds is not available
        else:
            return False #None location is not free. failsafes.

    def get_player_ships_in_battle():
        result = []
        for ship in player_ships:
            if ship.location != None:
                result.append(ship)
        return result

    def set_cell_available(location, available=False):
        #False in the matrix means available(empty/nil), True means occupied
        #parameter 'available' defaults to False meaning it sets a hex to empty
        if location != None:
            a,b = location
            X,Y = GRID_SIZE
            if a > 0 and a <= X and b > 0 and b <= Y:
                BM.grid[a-1][b-1] = available
            else:
                if config.developer:
                    raise Exception("tried to set availability on a hex that does not exist")
                else:
                    pass  #not sure if I should raise an exception or not

    def show_message(message,xpos=0.5,ypos=0.7,pause = MESSAGE_PAUSE):
        """briefly show some text on screen"""
        renpy.hide_screen('message')
        renpy.show_screen('message', message=message,xpos=xpos,ypos=ypos)
        try:
            renpy.pause(pause)
        except:
            pass
        renpy.hide_screen('message')

    def get_distance(location1, location2):
        if location1 == None or location2 == None: return 999
        cubic1 = convert_to_cubic(location1)
        cubic2 = convert_to_cubic(location2)
        result = cubic_distance(cubic1, cubic2)
        return result

    def get_ship_distance(ship1,ship2):
        if ship1 == None or ship2 == None: return 999
        if ship1.location == None or ship2.location == None: return 999
        cubic1 = convert_to_cubic(ship1.location)
        cubic2 = convert_to_cubic(ship2.location)
        result = cubic_distance(cubic1, cubic2)
        return result

    def update_stats():
          #first update the shields
          #we loop through all ships and then loop through all ships again
          #we then check if the first ships is in range of the 2nd one
          #if they are, the shield generation value of the 2nd gets added to the total shield value of the first
          #we also update armor (to match damage levels) while we are at it.
          #the font color is also updated to show a value is buffed or not from baseline

        #this should've been set from the beginning
        for ship in BM.ships:
            ship.flaksim = None
            for weapon in ship.weapons:
                if weapon.parent is None:
                    weapon.parent = ship
        
        #loop through ships and get shield generation near each ship.
        for ship1 in player_ships:
            try:
                if ship1.modifiers['energy regen'][0] == -100: #DEFUNCT
                    ship1.en = 0
            except:
                ship1.modifiers['energy regen'] = (0,0)
            ship1.shields = 0
            #check for allied ships nearby
            for ship2 in player_ships:
                if get_ship_distance(ship1,ship2) <= ship2.shield_range:
                    actual_generation = ship2.shield_generation
                    try:
                        mod,duration = ship2.modifiers['shield_generation']
                    except:
                        ship2.modifiers['shield_generation'] = [0,0]
                        mod,duration = (0,0)
                    if mod != 0: actual_generation += mod
                    if actual_generation < 0: actual_generation = 0
                    ship1.shields += actual_generation
            #check for allied drones nearby
            for drone in BM.drones:
                if drone.location is not None:
                    if get_ship_distance(ship1,drone) <= drone.shield_range:
                        ship1.shields += drone.shield_generation
                        #dirty hack as proper buff passing mechanics would be quite the pain.
                        if BM.active_strategy[0] == 'all guard' and drone.shield_generation > 0:
                            ship1.shields += 10
            if ship1.shields > 100: ship1.shields = 100
            ship1.shield_color = '000'
            if ship1.shields > ship1.shield_generation: ship1.shield_color = '070'
            ship1.update_armor()
        for ship1 in enemy_ships:
            try:
                if ship1.modifiers['energy regen'][0] == -100:
                    ship1.en = 0
            except:
                ship1.modifiers['energy regen'] = (0,0)
            ship1.shields = 0
            for ship2 in enemy_ships:
                if ship2.shield_generation > 0:
                    if get_ship_distance(ship1,ship2) <= ship2.shield_range:
                        actual_generation = ship2.shield_generation
                        try:
                            mod,duration = ship2.modifiers['shield_generation']
                        except:
                            ship2.modifiers['shield_generation'] = [0,0]
                            mod,duration = ship2.modifiers['shield_generation']
                        if mod != 0:
                            actual_generation += mod
                        if actual_generation < 0:
                            actual_generation = 0
                        ship1.shields += actual_generation
            if ship1.shields > 100: ship1.shields = 100
            ship1.shield_color = '000'
            if ship1.shields > ship1.shield_generation: ship1.shield_color = '070'
            ship1.update_armor()
            

    def get_weapon_type(weapon):
        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
            return 'Kinetic'
        elif weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
            return 'Energy'
        elif weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
            return 'Missile'
        elif weapon.wtype == 'Melee':
            return 'Melee'
        else:
            return weapon.wtype #return support or curse types

    def add_new_vars():
        firstvars = copy(AllVariables().__dict__)
        for key in firstvars:
            if not hasattr(store,key) or getattr(store,key) == None:
                setattr(store,key,firstvars[key])

    def reset_classes(silent = False):
        """experimental save file compatibility keeper
        this reruns the __init__() function of every relevant class in the game
        so that newly added fields can be added to classes from an old save file.
        copy() is used because creating an alias is exactly what's not needed here"""

#        #store a list of BM.ships. copy() does not create aliased variables
#        ships = copy(BM.ships)

        if not silent:
            show_message('You loaded a save file from a previous version of the game. reinitializing game data...')
            try:
                renpy.pause(1.0) #this will typically fail when a ui.interact is running, like it usually is during battle
            except:
                pass

        #copy the dict from BM
        fields = copy(BM.__dict__)

        #add missing fields to BM
        BM.__init__()

        #restore the old values to the dict in BM
        for key in fields:
            if type(BM.__dict__[key]) is dict:
                dictionary = BM.__dict__[key]
                for key2 in fields[key]:
                    #only put missing keys in nested dicts
                    #this will re-add orders that are not part of the default
                    if not key2 in dictionary:
                        dictionary[key2] = fields[key][key2]
            else:
                BM.__dict__[key] = fields[key]

        #repeat same concept for basic variables inside firstvariables.rpy
        #add_new_vars()

        #remake the BM.ships list
        BM.ships = []
        for ship in player_ships:
            BM.ships.append(ship)
        for ship in enemy_ships:
            BM.ships.append(ship)

        #the all_enemies list also needs to be updated or you get problems in skirmish
        iterate_list = BM.ships + store.all_enemies
        #going to re-init all the ships
        for ship in iterate_list:
            weapons = ship.weapons

            #re-init all the weapons to default values
            if ship.faction == 'Player':
                weaponlist = weapons
            else:
                weaponlist = weapons + ship.default_weapon_list

            for weapon in weaponlist:
                #make a copy of the weapon if required
                weaponcopy = None
                if hasattr(weapon,'keep_after_reset'):
                    if weapon.keep_after_reset != {}:
                        weaponcopy = copy(weapon)
                #reset all values to default
                weapon.__init__()
                if weaponcopy is not None:
                    #change back the values to what they should be.
                    for key in weaponcopy.keep_after_reset:
                        weapon.__dict__[key] = weaponcopy.keep_after_reset[key]
                    weapon.keep_after_reset = weaponcopy.keep_after_reset

            #make a copy of the ship instance
            ship_copy = copy(ship)
            #re-init the ship
            ship.__init__()
            #loop over all the keys in the dict of the copy
            for key in ship_copy.__dict__:
                ship_value = getattr(ship_copy,key)  #= hp value or upgrades dict etc
                #check if this key represents a nested dict
                if type(ship_value) is dict: #such as ship.upgrades
                    new_ship_dict = getattr(ship,key) #the default dict part of the recently reinitialized ship
                    #loop over all the keys in the dict from the copied ship
                    for key2 in ship_value:
                        #overwrite the default values with the ones that were there originally
                        #otherwise all upgrades would get wiped out.
                        if key2 in new_ship_dict:
                            new_ship_dict[key2] = ship_value[key2]
                else:
                    # key is not a dict
                    if hasattr(ship,key):
                        setattr(ship,key, getattr(ship_copy,key) )

            #restore the old weapon list
            ship.weapons = weapons

        # for pship in player_ships:    #this needs to be altered so that it doesn't restore everything when called mid-battle
            # update_upgrades(pship)        
        
        if not silent:
            show_message('Reinitialization complete.')
        return

    def update_weapon(weapon):
        """reset a weapon to init so it's compatible with current code. most useful for custom actions that store weapons from old code"""
        keep_dict = {}
        parent = weapon.parent
        if hasattr(weapon,'keep_after_reset'):
            keep_dict = weapon.keep_after_reset
        weapon.__init__()
        if keep_dict != {}:
            for stat in keep_dict:
                setattr(weapon,stat,keep_dict[stat])
            weapon.keep_after_reset = keep_dict
        weapon.parent = parent
        return weapon    

    def fix_enemy_list():
        store.all_enemies = [
            PactBomber(),  PactMook(),
            MissileFrigate(), PactCruiser(),
            PactCarrier(), PactOutpost(),
            PactBattleship(),RyuvianCruiser(),
            Havoc(), PirateBomber(),
            PirateGrunt(), PirateDestroyer(),
            PirateBase()
            ]
        for ship in store.all_enemies:
            ship.location = None

    def update_mp():
        for variable in important_variables:
            if hasattr(store,variable):
                setattr(mp,variable, getattr(store,variable) )
        mp.save()
        
    def libday_save_dump():
        
        dump_variables = [
        'captain_moralist','captain_prince','affection_ava','affection_asaga',
        'affection_chigara','affection_icari','affection_claude','affection_kryska',
        'affection_sola','affection_cosette','wishall','Saveddiplomats',
        'OngessTruth','legion_destroyed','cosette_dead','havoc_save','discoverfalcon',
        'lynn_chigaranotoneofyou','chigaradidntbetray','tielynncargo','avareconcile',
        'soladefinitelyprotect']
        
        for variable in dump_variables:
            if hasattr(store,variable):
                setattr(libday_mp,variable, getattr(store,variable) )
        libday_mp.save()
        
        return
        
    def libday_txtfile_dump():
        import sys
        if not sys.platform == "win32": return
        
        dump_variables = [
        'captain_moralist','captain_prince','affection_ava','affection_asaga',
        'affection_chigara','affection_icari','affection_claude','affection_kryska',
        'affection_sola','affection_cosette','wishall','Saveddiplomats',
        'OngessTruth','legion_destroyed','cosette_dead','havoc_save','discoverfalcon',
        'lynn_chigaranotoneofyou','chigaradidntbetray','tielynncargo','avareconcile',
        'soladefinitelyprotect']
        #get a path of the bonus directory to make
        bonusdir_path = os.path.abspath(os.path.join(config.basedir, "game clear save"))
        
        #try to make the bonus directory
        try:
            os.makedirs(bonusdir_path, 0777)
        except:
            pass
             
        #path of the filename of the save dump
        gameclear_path = os.path.join(bonusdir_path, 'game_cleared.dat')
        
        gameclear = open(gameclear_path, "w")
        
        #write the dump
        for variable in dump_variables:
            gameclear.write(variable+':'+str(getattr(store,variable))+'\n')
             
        #close the file
        gameclear.close()
        return
        
    def ltd():
        try:
            libday_txtfile_dump()
        except:
            pass
        return
        
    def get_game_cleared():
        import sys
        if not sys.platform == "win32": return False #hopefully the mp works
        bonusdir_path = os.path.abspath(os.path.join(config.basedir, "game clear save"))
        gameclear_path = os.path.join(bonusdir_path, 'game_cleared.dat')
        return os.path.isfile(gameclear_path)
        
    def check_for_all_endings():
        for ending in persistent.unlocked_endings:
            if persistent.unlocked_endings[ending] == False:
                return
        chivo_process('REturn Completed')
        
        
    def time_warp_easeout(t):  ##probably never got used
        return 1.0 - math.cos(t * math.pi / 2.0)

    def get_mouse_location():
        """get the mouse position and return the hex location the mouse is over."""
        a,b = renpy.get_mouse_pos()
        yoffset = 27 * store.zoomlevel
        hexheight = HEXD * store.zoomlevel
        hexwidth = HEXW * store.zoomlevel
        # xmax,ymax = GRID_SIZE

        y = int( (b+BM.yadj.value-yoffset) / hexheight )
        if y%2==0:
            xoffset = hexwidth/2
        else:
            xoffset = 0
        x = int( (a+BM.xadj.value-xoffset) / hexwidth )
        return (x,y)

    def ship_position(ship):  #used to sort ships in BM.ships
        if ship.location is None:
            return 0

        a, b = ship.location
        return a + b * 100

    def sort_ship_list():
        BM.ships.sort(key=ship_position)

    def zoom_handling(result,bm):
        if result == None:
            return
        if bm == None:
            return
        mouse_xpos, mouse_ypos = renpy.get_mouse_pos() #such a handy function. Thanks Tom!  I use this to zoom in onto your mouse position
        if result[1] == 'in':   #fudging the mouse position a little so you zoom in further than you actually point
            if mouse_xpos > 960:
                adjusted_xpos = 960 + (mouse_xpos-960)*1.5
            else:
                adjusted_xpos = mouse_xpos - (960-mouse_xpos)*0.75
            if mouse_ypos > 540:
                adjusted_ypos = 540 + (mouse_ypos-540)*1.5
            else:
                adjusted_ypos = mouse_ypos - (540-mouse_ypos)*0.75
        else:
            adjusted_xpos = 960   #when you zoom out you do not do so based on your cursor position.
            adjusted_ypos = 540

        real_xpos = (bm.xadj.value + adjusted_xpos) / (1920*store.zoomlevel/0.5)  #this stores the position of the mouse relative to the entire battlefield
        real_ypos = (bm.yadj.value + adjusted_ypos) / (1080*store.zoomlevel/0.5)

        if result[1] == "in": #check if you scrolled up or scrolled down.
            store.zoomlevel *= (1 + ZOOM_SPEED)
            if store.zoomlevel >= 2.0: store.zoomlevel = 2.0 #set a maximum value so you can't zoom in endlessly

        elif result[1] == "out":
            store.zoomlevel *= (1 - ZOOM_SPEED)
            if store.zoomlevel <= 0.5: store.zoomlevel = 0.5

        side_distance = (1920*store.zoomlevel/0.5)*real_xpos-adjusted_xpos #I use the mousepostion that was stored at the start to calculate the new viewport position
        if side_distance < 0: side_distance = 0
        top_distance = (1080*store.zoomlevel/0.5)*real_ypos-adjusted_ypos
        if top_distance < 0: top_distance = 0

        # renpy.restart_interaction()
        renpy.hide_screen('battle_screen') #the zoomlevel must to be processed BEFORE I adjust the viewport location
        renpy.show_screen('battle_screen')
        bm.xadj.value = int(side_distance) #actually set the new viewport values
        bm.yadj.value = int(top_distance)

    def clear_animations():
        for ship in BM.ships:
            ship.getting_cursed = False
            ship.getting_buffed = False
        return
    
    def create_ship(ship,location=None,weapons=[]):

        #find the location
        if location != None:
            location = get_free_spot_near(location)
            if BM.grid[location[0]-1][location[1]-1]:
                return
            else:
                #indicate that the cell on the grid is occupied
                BM.grid[location[0]-1][location[1]-1]= True

        #set the location
        ship.location = location

        #confirm the weapon list
        if weapons == None or weapons == []:
            weapons = ship.default_weapon_list

        #register the weapons
        for weapon in weapons:
            ship.register_weapon(weapon)

        #register the ship
        if ship.faction == 'Player':
            store.player_ships.append(ship)
        else:
            store.enemy_ships.append(ship)
        store.BM.ships.append(ship)

        #retun the a player ship for easy aliasing
        if ship.faction == 'Player':
            return ship
        else:

            #add newly encountered enemy ships to the list of enemies in skirmish.
            in_all_enemies = False
            for eship in store.all_enemies:
                if ship.__class__ == eship.__class__:
                    in_all_enemies = True
            if not in_all_enemies:
                store.all_enemies.append( ship.__class__() )
                store.all_enemies[-1].location = None

            return ship
            
    def delete_ship(ship,playerfaction = True):
        shiplist = player_ships if playerfaction else enemy_ships
        
        if type(ship) is str:
            for pship in shiplist[:]:
                if pship.name == ship:
                    shiplist.remove(pship)
                    if pship in BM.ships:
                        BM.ships.remove(pship)
                    set_cell_available(pship.location)
                    return True
        else:
            if ship in shiplist:
                shiplist.remove(ship)
                if ship in BM.ships:
                    BM.ships.remove(ship)
                set_cell_available(ship.location)
                return True
        return False
        
    def debug_wipe():
        store.enemy_ships = [ store.enemy_ships[0] ]
        store.BM.ships = store.player_ships + store.enemy_ships

    def get_free_spot_near(location):
        radius = 0
        # don't make the radius larger than width and height of the grid
        while radius < GRID_SIZE[0] or radius < GRID_SIZE[1]:
            # get the locations in the ring at radius 'radius'
            locations = get_in_ring(location, radius)

            # return the first available location in the list
            for loc in locations:
                if get_cell_available(loc):
                    return loc
            # increment radius
            radius += 1
        return location

    def short_pause(t=1): #very useful combined with renpy.invoke_in_new_context
        renpy.show_screen('battle_screen')
        renpy.pause(t)

    def get_remaining_player_ships():
        count = 0
        for ship in player_ships:
            if ship.location != None:
                count += 1
        return count

    def clean_battle_exit(save_destroyed_mercenaries = False):
        if BM.selected != None: BM.unselect_ship(BM.selected)
        BM.targetingmode = False
        BM.vanguardtarget = False
        BM.weaponhover = None
        BM.hovered = None
        BM.enemy_vanguard_path = []
        renpy.hide_screen('tooltips')
        BM.phase = 'Player'
        BM.turn_count = 1
        BM.active_strategy = [None,0]
        BM.end_turn_callbacks = []
        BM.ships = []
        BM.selectedmode = False
        
        #check Asaga's awakening and reset if required.
        if blackjack.has_weapon("Cancel Awakening"):
            blackjack.remove_weapon("Cancel Awakening")
            blackjack.register_weapon(AwakenAsaga())
        
        for drone in BM.drones:
            drone.location = None
        
        for ship in destroyed_ships:
            if ship.faction == 'Player' and (not ship.mercenary or save_destroyed_mercenaries):
                player_ships.append(ship)
                BM.ships.append(ship)
        for ship in player_ships:
            BM.ships.append(ship)        
            ship.en = ship.max_en
            ship.hp = ship.max_hp
            ship.hate = 100
            ship.total_damage = 0
            ship.total_missile_damage = 0
            ship.total_kinetic_damage = 0
            ship.total_energy_damage = 0
            ship.missiles = ship.max_missiles
            ship.location = None #this helps if you add new ships but don't know the current location of the existing ones.
            ship.buffs = []
            for modifier in ship.modifiers:
                ship.modifiers[modifier] = [0,0]

        #reset the entire grid to empty and BM.ships with only the player_ships list
        clean_grid()
        BM.covers = []
        # renpy.hide_screen('battle_screen')
        # renpy.hide_screen('commands')
        # renpy.block_rollback()
        # renpy.music.play("Music/Mission_Briefing.ogg") #else battle theme keeps playing after battle

    def battle_setup():
        BM.battlestart.player_ships = copy(player_ships)
        for ship in BM.ships:
            ship.battlestart_location = copy(ship.location)
        BM.battlestart.enemy_ships = copy(store.enemy_ships)
        BM.battlestart.covers = copy(BM.covers)
        BM.battlestart.sunrider_rockets = copy(sunrider.rockets)
        BM.battlestart.sunrider_repair_drones = copy(sunrider.repair_drones)
        BM.battlestart.cmd = copy(BM.cmd)
        BM.stopAI = False
        BM.order_used = False
        BM.enemy_vanguard_path = []
        BM.player_vanguard_path = []
        BM.active_strategy = [None,0]
        renpy.take_screenshot()
        renpy.save('battlestart{}'.format(BM.mission))
        if BM.show_tooltips:
            renpy.show_screen('tooltips')
        for ship in player_ships:
            ship.hp = ship.max_hp
            ship.en = ship.max_en
        store.zoomlevel = 0.65
        update_stats()
        return
    
    def get_shot_hit(accuracy,shotcount,faction):
        #fudging with actual hit chances for fun and profit  (lolhiddenmechanics)
        #for now no fudging for AI.
        if faction == 'Player' and store.Difficulty <=3 and shotcount == 1 and accuracy >50:
            RNG2 = renpy.random.randint(1,50) + renpy.random.randint(0,50)
            return RNG2 <= int(accuracy)
        elif faction == 'Player' and store.Difficulty > 3 and accuracy < 50 and shotcount == 1: #muhahaha
            RNG2 = renpy.random.randint(1,50) + renpy.random.randint(0,50)
            return RNG2 <= int(accuracy)
        else:
            return renpy.random.randint(1,100) <= accuracy

    def test_RNG(accuracy):
        #you can use this to see the difference between the 2 ways of calculating a hit.
        hits1RN = 0
        hits2RN = 0

        for i in range(1000):
            if (renpy.random.randint(1,50) + renpy.random.randint(0,50)) < accuracy:
                hits2RN += 1
            if renpy.random.randint(1,100) < accuracy:
                hits1RN += 1

        return (hits1RN,hits2RN)

    def debuglog_add(text):
        if config.developer:
            BM.debug_log.append(text)
            if len(BM.debug_log) > 50:
                BM.debug_log = BM.debug_log[-49:-1]
        else:
            pass

    def get_shipcount_in_list(shipname,list):
        #count number of times a ship is in a list. useful for merc counting
        if len(list) == 0: return 0
        if shipname == None: return 0

        count = 0
        for item in list:
            if shipname == item.name:
                count+=1
        return count

    def create_cover(location):
        BM.covers.append(Cover(location))
        return

    def cover_mechanic(weapon,target,accuracy):
            for cover in BM.covers:
                if cover.location == target.location:
                    if renpy.random.randint(1,100) <= cover.cover_chance:
                        show_message('the shot was blocked by an asteroid!')
                        renpy.pause(1.0)
                        total_damage = 0
                        for shot in range(weapon.shot_count):
                                total_damage += weapon.damage  #asteroid has no defenses
                        cover.receive_damage(total_damage)
                        return True
            return False

    def get_movement_tiles(ship, move_range = None):
        if ship == None: return []
        if ship.location == None: return []

        if move_range == None:
            if not hasattr(ship,'move_cost'):
                raise Exception("error:"," variable ship is {} ".format(str(ship.__class__.__name__)))
                debuglog_add("{} has no move_cost attr!".format(str(ship)))
                return []
            if ship.move_cost == 0:
                move_range = 1
            else:
                move_range = int(float(ship.en) / ship.move_cost)
        if move_range > 4 : move_range = 4  #limit the max number of movement tiles on screen
        tile_locations = []
        for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
            for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                loc1 = convert_to_cubic(ship.location)
                loc2 = convert_to_cubic([a,b])
                cell_distance = cubic_distance(loc1, loc2)

                if not BM.grid[a-1][b-1] and cell_distance <= move_range:
                    xposition = dispx(a,b,zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                    yposition = dispy(a,b,zoomlevel,0.5 * ADJY) + int(zoomlevel * MOVY)
                    tile_locations.append((xposition,yposition,-cell_distance,a,b))
        return tile_locations

    def has_weapon(ship,wtype):
        """check if a ship has a weapon of a given type. the weapon type is passed as a string"""
        for weapon in ship.weapons:
            if weapon.wtype == wtype:
                return True
        return False

    def get_counter_attack(location, AI = False):
        """check if a location is next to an (enemy) unit that has an Assault type weapon"""
        if location is None: return False
        if BM.selected is None: return False
        
        shiplist = enemy_ships
        if AI:
            shiplist = player_ships
            
        for ship in shiplist:
            if get_distance(ship.location,location) == 1:
                for weapon in ship.weapons:
                    if weapon.wtype == 'Assault' and ship.flak > 0 or weapon.force_counter:
                        return True
        return False

    def update_modifiers():
        """called when the phase changes. it ticks down modifiers and removes them when expired."""

        #player phase starts
        if BM.phase == 'Player':

            #order management
            order_expired = False
            strat,duration = BM.active_strategy
            if strat != None:
                if duration <= 1:
                    message = "{} has expired!".format(strat)
                    BM.battle_log_insert(['order'], message)
                    show_message(message)
                    order_expired = True
                    BM.active_strategy = [None,0]
                    #remove the buffs. they'll expire on their own too, but this skips the message
                    for ship in player_ships:
                        ship.remove_buff('Full Forward')
                        ship.remove_buff('All Guard')
                else:
                    BM.active_strategy = [strat,duration -1]

            #handle the buffs and any callbacks
            for ship in player_ships[:]:
                for buff in ship.buffs[:]:
                    buff.turn_start()
                    buff.callback()
                for weapon in ship.weapons[:]:
                    weapon.callback()
            
        #enemy turn starts
        else:
            for ship in enemy_ships[:]:
                for buff in ship.buffs[:]:
                    buff.turn_start()
                    buff.callback()
                for weapon in ship.weapons[:]:
                    weapon.callback()

    def game_over():
        renpy.hide_screen('game_over_gimmick')
        renpy.show_screen('game_over_gimmick')

## FUNCTIONS RELATED TO HEXES

    def convert_to_cubic(location):  #converts offset coordinates to cubic coordiantes
        r = location[0]              #works on even horizontal offset
        q = location[1]
        x = q
        z = r - ((q + (q % 2))/2)
        y = (-1 * x) - z
        return [x,y,z]

    def convert_to_offset(location):  #converts cubic coordinates to offset coordinates
        x = location[0]               #works on even horizontal offset
        y = location[1]
        z = location[2]
        q = x
        r = z + (x + (x%2)) / 2
        return (r, q)

    def cubic_distance(location1, location2):  #calculates the distances between two cubic coordiantes
        x1 = location1[0]
        y1 = location1[1]
        z1 = location1[2]

        x2 = location2[0]
        y2 = location2[1]
        z2 = location2[2]

        result = (abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))/2
        return result

    def hex_round(location):  #rounds cubic coordinates to the nearest hexagon
        x = location[0]
        y = location[1]
        z = location[2]
        rx = int(x)
        ry = int(y)
        rz = int(z)

        x_diff = abs(rx - x)
        y_diff = abs(ry - y)
        z_diff = abs(rz - z)

        if x_diff > y_diff and x_diff > z_diff:
            rx = -ry-rz
        elif y_diff > z_diff:
            ry = -rx-rz
        else:
            rz = -rx-ry

        return [rx, ry, rz]

    def interpolate_hex(location1, location2):  #creates a path between location1 and location2
        tiles = []
        loc1 = location1
        loc2 = location2
        cube1 = convert_to_cubic(loc1)
        cube2 = convert_to_cubic(loc2)
        disN = get_distance(loc1, loc2)

        if disN != 0:
            N = (1.0)/disN
            for i in range(0, disN+1):
                x = cube1[0] + (cube2[0] - cube1[0])*i*N
                y = cube1[1] + (cube2[1] - cube1[1])*i*N
                z = cube1[2] + (cube2[2] - cube1[2])*i*N
                #x = cube1[0] * (1 - float(i)/disN) + cube2[0] * float(i)/disN
                #y = cube1[1] * (1 - float(i)/disN) + cube2[1] * float(i)/disN
                #z = cube1[2] * (1 - float(i)/disN) + cube2[2] * float(i)/disN
                cuberound = hex_round([x, y, z])
                newloc = convert_to_offset(cuberound)
                if isvalid(newloc):
                    tiles.append(newloc)
        return tiles
        
    def interpolate_hex_splash(location1, location2,range=1):
        tiles = []
        result = []
        target_tiles = get_all_in_radius(location2,range)
        for tile in target_tiles:
            tiles = tiles + (interpolate_hex(location1,tile))
        for tile in tiles:
            if tile not in result:
                result.append(tile)
        return result    
            
## functions to calculate position of displayables

    def dispx(x, y, zoom, add = 0):
        xposition = 0
        if y % 2 == 0:
            xposition = int(((x + add) * HEXW + SLIDEX) * zoom)
        else:
            xposition = int(((x + add) * HEXW) * zoom)
        return xposition

    def dispy(x, y, zoom, add = 0):
        yposition = 0
        if x % 2 == 0:
            yposition = int(((y + add) * HEXD + SLIDEY) * zoom)
        else:
            yposition = int(((y + add) * HEXD) * zoom)
        return yposition

    def interpolate_grid(location1, location2): #draws a line from location1 to location2
        tiles = []
        loc1 = location1
        loc2org = location2
        mx = loc2org[0] - loc1[0] #extrapolation
        my = loc2org[1] - loc1[1]
        loc2 = [10*mx+loc2org[0],10*my+loc2org[1]]
        ystep = 0
        xstep = 0
        error = 0
        errorprev = 0
        y = loc1[1]
        x = loc1[0]
        ddx = 0
        ddy = 0
        dx = loc2[0] - loc1[0]
        dy = loc2[1] - loc1[1]
        if dy < 0:
            ystep = -1
            dy = -dy
        else:
            ystep = 1
        if dx < 0:
            xstep = -1
            dx = -dx
        else:
            xstep = 1
        ddy = 2*dy
        ddx = 2*dx
        if ddx >= ddy:
            errorprev = dx
            error = dx
            for i in range(0,dx):
                x+=xstep
                error+=ddy
                if error > ddx:
                    y+=ystep
                    error-=ddx
                    if error + errorprev < ddx:
                        if get_distance(location1,(x,y-ystep))<= 6 and isvalid((x,y-ystep)):
                            tiles.append([x,y-ystep])
                    else:
                        if get_distance(location1,(x-xstep,y))<= 6 and isvalid((x-xstep,y)):
                            tiles.append([x-xstep,y])
                if get_distance(location1,(x,y))<= 6 and isvalid((x,y)):
                    tiles.append([x,y])
                errorprev = error
        else:
            errorprev = dy
            error = dy
            for i in range(0,dy):
                y+=ystep
                error+=ddx
                if error > ddy:
                    x+=xstep
                    error-=ddy
                    if error + errorprev < ddy:
                        if get_distance(location1,(x-xstep,y))<= 6 and isvalid((x-xstep,y)):
                            tiles.append([x-xstep,y])
                    else:
                        if get_distance(location1,(x,y-ystep))<= 6 and isvalid((x,y-ystep)):
                            tiles.append([x,y-ystep])
                if get_distance(location1,(x,y))<= 6 and isvalid((x,y)):
                    tiles.append([x,y])
                errorprev = error
        return tiles

    def isvalid(location): #determines if the location in on the grid
        valid = True
        if location[0] > GRID_SIZE[0] or location[0] <=0:
            valid = False
        if location[1] > GRID_SIZE[1] or location[1] <=0:
            valid = False
        return valid

    def get_all_in_radius(location, radius):
        if radius < 0 or location == None:
            return []
        if location < 2:
            return get_all_in_radius_slow(location, radius)

        locations = []
        cx, cy, cz = convert_to_cubic(location)
        for dx in range(-radius, radius + 1):
            for dy in range(max(-radius, -dx - radius), min(radius, -dx + radius) + 1):
                dz = -dx - dy
                locations.append(convert_to_offset([cx + dx, cy + dy, cz + dz]))

        return clean_locations(list(set(locations)))

    def get_all_in_radius_slow(location, radius):
        if radius < 0 or location == None:
            return []

        locations = []
        pending = [location]
        while radius > 0:
            pending2 = []
            for loc in pending:
                x, y = loc
                pending2.append((x + 1, y))
                pending2.append((x - 1, y))
                pending2.append((x, y + 1))
                pending2.append((x, y - 1))
                if y % 2 == 0:
                    pending2.append((x + 1, y + 1))
                    pending2.append((x + 1, y - 1))
                else:
                    pending2.append((x - 1, y + 1))
                    pending2.append((x - 1, y - 1))
            locations.extend(pending)
            pending = list(set(pending2))
            for loc in locations:
                if loc in pending:
                    pending.remove(loc)
            radius -= 1
        locations.extend(pending)
        return clean_locations(list(set(locations)))

    def get_in_ring(loc, radius):
        outer = get_all_in_radius(loc, radius)
        inner = get_all_in_radius(loc, radius - 1)
        # remove all locations in the inner ring from the outer ring
        for x in inner:
            a,b = x
            if a > 1 and a < GRID_SIZE[0] and b > 1 and b < GRID_SIZE[1]:
                outer.remove(x)
        return outer

    def clean_locations(locations):
        """removes all the locations that are out of bounds"""
        if locations == None: return []
        if locations == []: return []

        result = []
        x,y = GRID_SIZE

        for location in locations:
            a,b = location
            if a > 0 and a <= x and b > 0 and b <= y:
                result.append(location)

        return result

    def get_ship_from_list(ship_list, ship_name):
        for ship in ship_list:
            if ship.name == ship_name:
                return ship
        return None

    def check_list(input):
        #return the input if it's a list or make it into one if it isn't.
        try:
            a = input[0] #allows not just lists but everything that acts like one, like strings
        except:
            return [input]
        else:
            return input
        
    def dshow (input_string,xpos=None,ypos=1750,zoom=0.9,t=dissolve,zorder=0,behind=[],layer='master',blush=False,cry=False): #WARNING: a leading 0 makes python interpret an int as base 8, so don't do that.
        if type(input_string) is int:
            input_string = get_sprite_combination(input_string)
            if blush: input_string = input_string +' '+ 'blush'
            if cry: input_string = input_string +' '+ cry
        
        name = input_string.split(' ',1)[0]
        
        if not hasattr(store,'sprite_positions'): store.sprite_positions = {} 
        if name not in store.sprite_positions: store.sprite_positions[name] = 0.5
        
        if xpos is None:
            xpos = store.sprite_positions[name]
        else:
            store.sprite_positions[name] = xpos
        
        d = store.sprites[input_string]
        renpy.show(name,[sprite_default(xpos,ypos,zoom)],layer,d,zorder,name,behind)
        renpy.with_statement(t)
        return
        
    def reset_sprites():
        for name in store.sprite_positions:
            store.sprite_positions[name] = 0.5 #default
        
    def get_elementlist(name,base):
        
        path = 'Character/'+name+'/'+base+'/' #as known to renpy using game folder as base. eg 'Character\Ava\armscrossed'
        name = name.lower()
        base = base.lower()
        
        mouth_files = [f for f in os.listdir(FULL_PATH+path+'mouth') if '.png' in f]
        mouths = {}
        for mouth in mouth_files:
            mouths[mouth.split('.')[0]] = (path+'mouth/'+mouth)
        
        eye_files = [f for f in os.listdir(FULL_PATH+path+'eyes') if '.png' in f]
        eyes = {}
        for eye in eye_files:
            eyes[eye.split('.')[0]] = (path+'eyes/'+eye)

        eyebrow_files = [f for f in os.listdir(FULL_PATH+path+'eyebrows') if '.png' in f]
        eyebrows = {}
        for eyebrow in eyebrow_files:
            eyebrows[eyebrow.split('.')[0]] = (path+'eyebrows/'+eyebrow)             
        
        elementlist = [
            name,
            {base:path+'base.png'},
            {'blush':path+'blush.png'},
            mouths,eyes,eyebrows
            ]
            
        if not renpy.loadable(path+'blush.png'):
            elementlist[2]['blush'] = "Null()"

        return elementlist
        
    def get_expressions(char):
        return [f for f in store.sprites if char in f]

    def test_sprites(name):
        f = get_expressions(name)
        sprite_name = f[renpy.random.randint(0,len(f)-1)]
        dshow(sprite_name)
        return sprite_name
        
    def get_voices(voiceless_ship=None):
        """populate ship objects with their voices"""
        #get a full list of all files in the sound/Voice folder. also lists everything in an archive.
        voice_files_list = [x for x in renpy.list_files() if 'sound/Voice' in x and 'mission' not in x and x.count('/') == 2]
        
        if BM.english_battle_voices:
            get_english_voices(voiceless_ship)
        else:
            if voiceless_ship is None:
                shiplist = BM.ships
            else:
                shiplist = [voiceless_ship]
            #loop through player ships who have a named pilot. (pilot attribute is abused as flag of having any voicing)
            for ship in shiplist:
                if ship.pilot is not None:
                    voice_id = ship.voice_channel[0:3] #eg 'chi' for the liberty
                    for voice in voice_files_list:
                        if not voice.startswith('sound/Voice/' + voice_id):
                            continue
                        event = voice.split('_')[1]
                        if not event in ship.voice_files:
                            ship.voice_files[event] = []
                        ship.voice_files[event].append(voice)
        return
        
    def get_english_voices(ship=None):
        evoices = [x for x in renpy.list_files() if 'sound/Voice' in x and x.count('/') == 3]
        
        looplist = player_ships if ship is None else [ship]
        for pship in looplist:
            if pship.pilot is None: continue
            evoices_ship = sorted([x for x in evoices if pship.pilot in x])
            for voice_file in evoices_ship:
                event = None
                
                if pship.pilot == 'Sola': #for some reason her file names are quite different
                    if 'attack 11' in voice_file.lower(): #turns out she hass no buff voice at all, so this is used for awakening.
                        event = 'Buff'
                    elif 'attack' in voice_file.lower():
                        event = 'Kin'
                    elif 'die' in voice_file.lower():
                        event = 'Ret'
                    elif 'curse' in voice_file.lower():
                        event = 'HitCur'
                    elif 'kill' in voice_file.lower():
                        event = 'EnKill'
                        
                if pship.pilot == 'Asaga' or pship.pilot == 'Kryska': #awakening and drawfire need a buff voice
                    if 'general 3' in voice_file.lower() or 'general 4' in voice_file.lower():
                        event = 'Buff'
                
                if event is None:
                    
                    if "kinetic" in voice_file.lower():
                        event='Kin'
                    elif "lasers" in voice_file.lower():
                        event='Las'
                    elif "missile" in voice_file.lower():
                        event='Missile'
                    elif "buffed" in voice_file.lower():
                        event='HitBuff'
                    elif "cursed" in voice_file.lower():
                        event='HitCur'
                    elif "no damage" in voice_file.lower() or 'evade' in voice_file.lower(): 
                        event='NoDam'
                    elif "damage" in voice_file.lower():
                        event='Dam'
                    elif "destroyed" in voice_file.lower():
                        if pship.pilot == 'Ava': #always the troublesome one
                            if 'enemy' not in voice_file.lower():continue
                        event='EnKill'
                    elif "miss" in voice_file.lower():
                        event='FaiAtk'
                    elif "backward" in voice_file.lower():
                        event='Bac'
                    elif "forward" in voice_file.lower():
                        event='For'
                    elif "select" in voice_file.lower():
                        event='Sel'
                    elif "retreat" in voice_file.lower():
                        event='Ret'
                    elif "melee" in voice_file.lower():
                        event='Mel'
                    elif "buff" in voice_file.lower():
                        event='Buff'
                    elif "curse" in voice_file.lower() and pship.pilot != "Sola":
                        event='Cur'
                    elif "stealth" in voice_file.lower():
                        event='Stealth'
                    elif "revive" in voice_file.lower():
                        event='Rev'
                    elif "success" in voice_file.lower() or 'hit' in voice_file.lower():
                        event='SucAtk'
                    
                if event is not None:
                    if event not in pship.evoice_files:
                        pship.evoice_files[event] = []
                    pship.evoice_files[event].append(voice_file)
            
        return
        
    #test
    def get_voice_events():
        store.voice_events = set()
        
        for ship in player_ships:
            for event in ship.voice_files:
                store.voice_events.add(event)
        return
    
    def validate_beach_decision():
        if his_beach1 == his_beach2 or his_beach1 == his_beach3 or his_beach2 == his_beach3:
            return False
        return True
        
    def is_number(s):
        try:
            float(s)
            return True
        except:
            return False
            
    def increment_attribute(obj,attr,value,addition=True):
        v = store.object.__getattribute__(obj,attr)
        if addition:
            return v+value
        else:
            return v*value
    
    def play_sound_effects(sound,number):
        # for a in range(number):
            # renpy.hide_screen('battle_screen')
            # renpy.show_screen('battle_screen')
            # if a >= 2:break
        renpy.music.play(sound,channel='sound{}'.format(1))
            # renpy.pause(0.05)
            # renpy.invoke_in_new_context(renpy.pause,0.1,hard=True)
        return
            
    def prepare_map_animation():
        renpy.hide_screen('battle_screen')
        renpy.show_screen('battle_screen')
        renpy.hide_screen('commands')
        renpy.hide_screen('orders')
        return
        
    def end_map_animation():
        if BM.phase == 'Player' and BM.selectedmode and BM.selected.faction == 'Player':
            renpy.show_screen('commands')
        renpy.hide_screen('battle_screen')
        renpy.show_screen('battle_screen')
        return
    
    def get_ships_around_hex(location,range=1,faction=None):
        if location == (0,0): location = None
        if location is None: return []
        if range == 0: return []
        shiplist = []
        for ship in BM.ships:
            if faction is not None and ship.faction != faction:
                continue
            if get_distance(location,ship.location) <= range:
                shiplist.append(ship)
        return shiplist
    
    def damage_multiple_ships(shipdict,attacker=None,wtype="Rocket",no_cmd=False):
        """shipdict should be a dict with ships and damage to apply"""
        if shipdict is None: return
        if len(shipdict) == 0: return
        if attacker is None: attacker = sunrider #nice scapegoat
        
        #let the battle screen know what to display
        BM.taking_damage = {}
        for ship in shipdict:
            damage = shipdict[ship]
            
            energy_mitigation = 0
            armor_mitigation = 0
            if type(damage) is tuple:
                damage,energy_mitigation,armor_mitigation = damage
             
            if damage != 'miss':
                BM.taking_damage[ship] = (get_modified_damage(damage,ship.faction),energy_mitigation,armor_mitigation)
        
        prepare_map_animation()
        renpy.pause(2)
        BM.taking_damage = False
        end_map_animation()
        player_count = 0
        for ship in shipdict:
            if ship.faction == 'Player':player_count += 1
            damage = shipdict[ship] #makes the next line easier to read
            ship.receive_damage(damage,attacker,wtype,animate=False,no_cmd = no_cmd)
        if player_count >= 5: chivo_process('Spread Out!')
        if BM.phase == 'Player' and len(shipdict) >=8: chivo_process('Grand Tactician')
        return
        
    def disable_weapontype(wtype,faction='Player'):
        if wtype is None: return
        if faction is None: return
        
        for ship in BM.ships:
            if ship.faction == faction:
                for weapon in ship.weapons:
                    if weapon.wtype == wtype:
                        weapon.disabled = True
        return
        
    def enable_weapontype(wtype,faction='Player'):
        if wtype is None: return
        if faction is None: return
        
        for ship in BM.ships+store.destroyed_ships:
            if ship.faction == faction:
                for weapon in ship.weapons:
                    if weapon.wtype == wtype:
                        weapon.disabled = False
        return
        
    def clear_ship_animations():
        """exists mostly as a failsafe"""
        for ship in BM.ships:
            ship.taking_damage = False
            ship.getting_buff = False
            ship.getting_curse = False
        return
        
    def scroll_wasd(pressed_key):
        x = y = 0
        if pressed_key == "W":
            y = int(-100 * zoomlevel)
        elif pressed_key == "A":
            x = int(-100 * zoomlevel)
        elif pressed_key == "S":
            y = int(100 * zoomlevel)
        elif pressed_key == "D":
            x = int(100 * zoomlevel)
        
        BM.xadj.change(BM.xadj.value + x)
        BM.yadj.change(BM.yadj.value + y)
            
    
    def move_view(location):
        """try and center view on specific x,y location"""
        if location is None: return
        a,b = location
        time_base = 0.2 #complete the move within this timeframe
        steps = 5 #number of individual changes to the viewscreen before moving is complete. default is 20fps
        #account for screen size aka convert to top left
        a = max(a - 960,0)
        b = max(b - 540,0)
        xvalue = BM.xadj.value
        yvalue = BM.yadj.value
        x_to_move = a - xvalue #number of pixels to move in a dimension
        y_to_move = b - yvalue
        
        if max(x_to_move,y_to_move) <= 100:
            return
        
        for step in range(steps):
            BM.xadj.change(xvalue + (x_to_move * step / steps))
            BM.yadj.change(yvalue + (y_to_move * step / steps))
            renpy.pause(time_base / steps)
        return
        
    def AI_move_view(ship1,ship2):
        if ship1 is None: return
        if ship2 is None: return
        if ship1.location is None or ship2.location is None: return
        zoomlevel = store.zoomlevel
        xposition1 = dispx(ship1.location[0],ship1.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
        yposition1 = dispy(ship1.location[0],ship1.location[1],zoomlevel, 0.50 * ADJY) + int(zoomlevel * MOVY)
        xposition2 = dispx(ship2.location[0],ship2.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
        yposition2 = dispy(ship2.location[0],ship2.location[1],zoomlevel, 0.50 * ADJY) + int(zoomlevel * MOVY)
        targetx = (xposition1 + xposition2)/2
        targety = (yposition1 + yposition2)/2
        # store.test = [ship1.location,ship2.location,zoomlevel,(xposition1,yposition1),(xposition2,yposition2),(targetx,targety)]
        move_view( (targetx,targety) )
        return
        
    def get_achievement_list():
        #plunder globals() for everything in the store that has a base class
        object_strings = [f for f in globals() if hasattr(getattr(store,f),'__base__')]
        #select from the previous results the objects with the base class we want and turn it from a string to a class reference
        return [getattr(store,f) for f in object_strings if getattr(getattr(store,f),'__base__') is Achievement]
        
    def add_achievements():
        if persistent.achievements is None:
            persistent.achievements = {}
            
        chivos = get_achievement_list()
        chivo_names = [x.name for x in chivos]
        for chivo in chivos:
            if chivo.name not in persistent.achievements:
                persistent.achievements[chivo.name] = chivo()
                
        #in case some get deleted.
        for chivo in persistent.achievements.keys():
            if chivo not in chivo_names:
                del persistent.achievements[chivo]
        
        renpy.save_persistent()
        return
        
    def chivo_process(name,*arg):
        if persistent.achievements is None or persistent.achievements == {}: 
            add_achievements()
        if name in persistent.achievements:
            persistent.achievements[name].process(*arg)
        return
            
    def validate_spire():
        global his_pactspire, his_capturetraffickers
        Confirm = True
        if his_pactspire == False and his_capturetraffickers == None:
            Confirm = False
        return Confirm
        
    def show_confirm():
        Confirm = True
        if Optionsvars != []:
            for item in Optionsvars:
                if eval(item) == None:
                    Confirm = False
        if Optionsfuncs != []:
            for item in Optionsfuncs:
                if item() == False:
                    Confirm = False
        return Confirm

    def options_insert(point,insert_list):
        global setoptions
        note = 0 #Failsafe, if no match it goes to the top
        #Find the point in the setoptions list
        for item in setoptions:
            if item[1] == point:
                note = setoptions.index(item)
        setoptions_hold = setoptions[note:]
        setoptions = setoptions[:note]
        for piece in insert_list:
            setoptions.append(piece)
        for piece in setoptions_hold:
            setoptions.append(piece)
        return
        
    def setoptions_ypos(list):
        global optionsypos, optionsxpos, optpoint
        OptDepth = 0
        StoreHoldingNumber = 1
        HoldingNumber = 0
        optionsypos = []
        optionsxpos = []
        for item in list[:]:
            try:
                if item[0] == 1:
                    HoldingNumber += 1
                    if HoldingNumber > StoreHoldingNumber:
                        OptDepth += 1
                        StoreHoldingNumber += 1
                    HoldingCount = 0
                    optionsypos.append(10+(OptDepth*40))
                    optionsxpos.append(10)
                    
                if item[0] == 2:
                    if HoldingCount == 2:
                        HoldingCount = 0
                        OptDepth += 1
                    optionsypos.append(10+(OptDepth*40))
                    if HoldingCount == 0: optionsxpos.append(430)
                    if HoldingCount == 1: optionsxpos.append(740)
                    HoldingCount += 1 # If there are more than 2 options, start a new line for the next ones, repeat every 2 options
            except:
                pass
        for item in list:
            if item[0] == 2:
                optpoint += 1
        optpoint /= 2

    def setoptionssp_ypos(list):
        global optionsypos, optionsxpos, optpoint
        OptDepth = 0
        StoreHoldingNumber = 1
        HoldingNumber = 0
        optionsypos = []
        optionsxpos = []
        for item in list[:]:
            try:
                if item[0] == 1:
                    HoldingNumber += 1
                    if HoldingNumber > StoreHoldingNumber:
                        OptDepth += 1
                        StoreHoldingNumber += 1
                    HoldingCount = 0
                    optionsypos.append(10+(OptDepth*40))
                    optionsxpos.append(10)
                    
                if item[0] == 2:
                    if HoldingCount == 2:
                        HoldingCount = 0
                        OptDepth += 1
                    optionsypos.append(10+(OptDepth*40))
                    if HoldingCount == 0: optionsxpos.append(430)
                    if HoldingCount == 1: optionsxpos.append(740)
                    HoldingCount += 1 # If there are more than 2 options, start a new line for the next ones, repeat every 2 options
            except:
                pass
        for item in list:
            if item[0] == 2:
                optpoint += 1
        optpoint /= 2
        
    def play_voice_move(ship, location, new_location): # plays voices with new move function
        if ship.pilot is not None:
            if ship.location[0] > new_location[0]: #going west
                if ship.Direction == "West":
                    ship.voice('For')
                else:
                    ship.voice('Bac')
            elif ship.location[0] < new_location[0]: #going east
                if ship.Direction == "East":
                    ship.voice('For')
                else:
                    ship.voice('Bac')
        return
        return
        
    def get_sprite_elements_names():
        x = [x for x in renpy.list_files() if 'Character' in x and '.png' in x]
        x = [x.replace("Character/","").replace(".png","") for x in x]
        x.sort()
        return x
        
    def get_numbered_segment(input_index,input_list):
        options = []
        for input_string in input_list:
            x = input_string.split('/')[0]
            if x not in options:
                options.append(x)
        return options[input_index]
        
    def get_posture_count(name_index):
        options = []
        x = get_sprite_elements_names()
        name = get_numbered_segment(name_index,x)
        x = [x.replace(name+'/',"") for x in x if name in x]
        for input_string in x:
            x = input_string.split('/')[0]
            if x not in options:
                options.append(x)
        return len(options)
        
    def get_sprite_combination(input_int): #WARNING: a leading 0 makes python interpret an int as base 8, so don't do that.
        x = get_sprite_elements_names()
        input_string = str(input_int)
        if len(input_string) > 5:
            return 'input error'
        else:
            while len(input_string) < 5:
                input_string = '0' + input_string
        name = get_numbered_segment(int(input_string[0]),x)
        # store.test = name
        x = [x.replace(name+'/',"") for x in x if name in x]
        posture = get_numbered_segment(int(input_string[1]),x)
        x = ["/".join(y.split("/")[1:]) for y in x if y.split("/")[0] == posture]
        # store.test = store.test + ' ' + posture
        eyebrows = [y.replace("eyebrows/","") for y in x if 'eyebrows/' in y]
        if int(input_string[4]) >= len(eyebrows):
            return 'out of range'
        eyebrow = eyebrows[int(input_string[4])]
        # store.test = store.test + ' ' + eyebrow
        eyes = [y.replace("eyes/","") for y in x if 'eyes/' in y]
        if int(input_string[3]) >= len(eyes):
            return 'out of range'
        eye = eyes[int(input_string[3])]
        # store.test = store.test + ' ' + eye
        mouths = [y.replace("mouth/","") for y in x if 'mouth/' in y]
        if int(input_string[2]) >= len(mouths):
            return 'out of range'
        mouth = mouths[int(input_string[2])]
        # store.test = store.test + ' ' + mouth
        result = name.lower() + ' ' + posture + ' ' + mouth + ' ' + eye + ' ' + eyebrow
        return result
        
        