#### Lines 656, 2219, 2589 alterated



## This file declares all the classes in the battle engine
# 1) battle manager class
# 2) custom displayables
# 3) Action objects (these gets activated when you click a button)  [[DEFUNCT]]
# 4) battleship blueprint class
# 5) Weapon blueprint classes
# 6) library (specific ships/weapons)  [[MOVED]]
# 7) planet class
# 8) bonus stuff
# 9) actions

init -2 python:
    import pygame

        ##here the Battle class gets defined. it forms the core and spine of the entire combat engine.
        ##it gets initialized into an instance called BM, short for battlemanager
    class Battle(store.object): # handles managing a list of all battle units, handles turns and manages enemy AI

        def __init__(self):
            #when the first instance gets created a couple of default values get initialized.
            self.cmd = 0              #your command point total
            self.max_cmd = 4000
            self.money = 0            #go on, set this to 999'999'999. you know you want to.
            self.intel = 0            #your intel total, used for upgrades (research).
            self.seen_skirmish = False #if not seen skirmish before Ava explains it.
            self.save_version = config.version
            self.ships = []           #holds all ships to display on the map
            self.covers = []          #holds a list of all the cover on the map
            self.drones = []          #list of all drones active on the battlefield. they can't be targeted but they can have effects like project shields
            self.enemy_vanguard_path = []#stores the hexes that the enemy's vanguard will go through.
            self.player_vanguard_path = []#stores the hexes that the player's vanguard will go through (only used by AI).
            self.missiles = []        #all the missiles on screen. right now all missiles are fired one by one
            self.selected = None      #current selection
            self.hovered = None       #what unit are you hovering over
            self.target = None        #the current target of whatever attack is going on
            self.attacker = None
            self.selectedmode = False #this makes the move target buttons appear
            self.targetingmode = False#keeps chance to hit target windows on screen etc
            self.moving = False       #set to true when a ship is moving from point a to b
            self.just_moved = False   #when True the button to take back your last movement is shown
            self.missile_moving = False #tells the battle screen a missile is moving from a to b
            self.shooting = False     #similar to previous, but no flak going on. when not false it contains the bullet sprite
            self.phase = 'Player'     #keeps track of who's turn it is
            self.weaponhover = None   #the weapon you are hovering over. used for chance to hit target window and tooltips
            self.buffhover = None     #the buff you are hovering over. used for tooltips.
            self.active_weapon = None #similar to weaponhover, but is used after you actually click a weapon so you can target something
            self.active_upgrade = None#used in the upgrade screen to see what you are hovering over.
            self.mission = 1          #what mission are we on? decides where to loop and is important for in battle events
            self.turn_count = 1       #most important when calculating command points awarded
            self.grid = []            #keep track of what cells in the grid are free and which are not.
            self.vanguard = False     #when not False the vanguard is being fired. it should contain where it's shooting at.
            self.vanguard_splash = False #when True vanguard targets not 1 hex but 6.
            self.active_strategy = [None,0] #you can have either 'full forward' or 'all guard' active, but not both.
            self.vanguardtarget = False #When True the player can select a target for the VC cannon
            self.warping = False      #used by the short range warp order. it makes an outline of the selected ship show at the mouse cursor
            self.targetwarp = False   #used by the short ranged warp order.  it creates buttons on the tiles
            self.showing_orders = False #This is True when the list of orders is visible.
            self.show_tooltips = True #hide or show tooltips
            self.enable_hotkeys = True #when enabled hotkeys should work
            self.debugoverlay = False #overlay coords etc for debug purposes
            self.show_grid = True     #show or hide the grid. no grid is much faster!
            self.formation_range = 6  #the farthest column the player can place units during the formation phase
            self.mercenary_count = 0  #the number of mercenaries in service to the Sunrider. [no longer used]
            self.temp_battleship_active = False #when True you can't summon another battleship
            self.remove_mode = False  #when True the player can easily remove units in skirmish
            self.taking_damage = False#when True damage is shown on a unit. when not false it contains the unit taking damage and the amount in a tupple
            self.exploding = False    #when not false it contains the exploding ship.
            self.cmd_gained = None    #shows what unit gave how many CMD points
            self.win_when_alone = True#if false you can kill all enemies but still not win.
            self.formation_editable = True #when False ships need to be set manually before a mission
            self.english_battle_voices = False  #when True english voices are used in battle.
            self.supress_menu = False #When True a right click will not open the menu
            self.player_ai = False
            self.battlestart = store.object()
            self.end_turn_callbacks = []
            self.achievement_data = {  #used to keep track of game specific achievement progress.
                'Penny Pincher':True,
                "Isn't it Sad, Chigara?":True,
                }
            self.lowest_difficulty = 5 #lowest recorded difficulty. bragging rights!
            self.lead_ships = []
            self.mouse_location = (0,0)
            self.vanguard_damage = 2000
            self.vanguard_range = 99
            self.repair_drone_heal = 0.5
            self.orders = {
                _('FULL FORWARD'):[750,'full_forward'],
                _('ALL GUARD'):[750,'all_guard'],
                _('REPAIR DRONES'):[750,'repair_drones'],
                _('VANGUARD CANNON'):[4000,'vanguard_cannon']
                }
            self.order_used = False   #when True the orders button is hidden.
              #environment modifiers are initialized here and can be changed later
            self.environment = {
                'accuracy':100,
                'turndamage':0,
                'damage':0,
                'energyregen':0,
                }
            self.battlemode = False   #True during battle. when set to False the battle loop will end.
            self.stopAI = False       #when set to True all AI action is disabled.
            self.edgescroll = (0,0)
            self.xadj = ui.adjustment() #used by the viewport in the battlescreen
            self.yadj = ui.adjustment()

            #when True you can drag the main viewport (the battle map with the grid) around. this needs to be
            #disabled when text is showing on screen otherwise mouseclicks get eaten by the viewport and do not advance text
            #DEFUNCT!
            self.draggable = True
            self.debug_log = []
            #Battle log
            self.show_battle_log = False
            self.battle_log = []
            self.battle_log_yadj = ui.adjustment(adjustable=True)
            #dispatchers
            self.skirmish_dispatcher = { 'start'         : self.skirmish_start,
                                         'quit'          : self.skirmish_quit,
                                         'remove'        : self.skirmish_remove,
                                         'playermusic'   : self.skirmish_playermusic,
                                         'enemymusic'    : self.skirmish_enemymusic,
                                         "zoom"          : self.common_zoom,
                                         "next ship"     : self.common_next_ship,
                                         "deselect"      : self.common_deselect,
                                         "selection"     : self.skirmish_selection,
                                         "warptarget"    : self.skirmish_warptarget }
            self.formation_dispatcher = { "start"        : self.formation_start,
                                          "zoom"         : self.common_zoom,
                                          "next ship"    : self.common_next_ship,
                                          "deselect"     : self.common_deselect,
                                          "selection"    : self.formation_selection,
                                          "warptarget"   : self.formation_warptarget }
            self.battle_dispatcher = { "anime"            : self.battle_anime,
                                       "cheat"            : self.battle_cheat,
                                       "I WIN"            : self.battle_inst_win,
                                       "deselect"         : self.battle_deselect,
                                       "next ship"        : self.battle_next_ship,
                                       "previous ship"    : self.battle_previous_ship,
                                       "zoom"             : self.battle_zoom,
                                       "selection"        : self.battle_selection,
                                       "move"             : self.battle_move,
                                       "cancel movement"  : self.battle_cancel_movement,
                                       _("ALL POWER TO ENGINES") : self.battle_order_injection_rods,
                                       _("SUMMON BATTLESHIP") : self.battle_order_summon_battleship,
                                       _("RESURRECTION")     : self.battle_order_resurrection,
                                       _("ALL GUARD")        : self.battle_order_all_guard,
                                       _("FULL FORWARD")     : self.battle_order_full_forward,
                                       _("REPAIR DRONES")    : self.battle_order_repair_drones,
                                       _("SHORT RANGE WARP") : self.battle_short_range_warp,
                                       _("RETREAT")          : self.battle_retreat,
                                       _("VANGUARD CANNON")  : self.battle_order_vanguard_cannon,
                                       "toggle player ai" : self.toggle_player_ai,
                                       "endturn"          : self.battle_end_turn,
                                       "battle won"       : self.you_win, }

              #stores a matrix of the grid to keep track of what spots are free. False is free, True is occupied
            for a in range(GRID_SIZE[0]):
                self.grid.append([False]*GRID_SIZE[1])
            self.battle_bg = "Background/space{!s}.jpg".format(renpy.random.randint(1,9))
            self.result = None #store result of ui.interact()
            #add (new) achievements to persistent object
            add_achievements()

        #here we start defining a few methods which part of the battlemanager
        ## insert entry to battle log
        # @param type The list of tags
        # @param message The formatted string
        # @param position Determines position of log entry
        def battle_log_insert(self, type, message, position = None):
            entry = [type, message]
            #zero is not supposed to be
            if position:
                self.battle_log.insert(position, entry)
            else:
                self.battle_log.append(entry)
            self.battle_log_yadj.change(self.battle_log_yadj.value + 125)

        #trimming, in case this list can lead to or contribute to memory leaks.
        def battle_log_trimm(self):
            if len(self.battle_log) > 500:
                start = len(self.battle_log) - 500
                self.battle_log = self.battle_log[start:]
                self.battle_log_yadj.change(self.battle_log_yadj.value - (125 * start))

        ## pop entry from battle log
        # @param index The index of entry to remove
        def battle_log_pop(self, index = None):
            if index is None:
                self.battle_log.pop()
            else:
                self.battle_log.pop(index)
            self.battle_log_yadj.change(self.battle_log_yadj.value - 125)

        def select_ship(self,ship,play_voice = True):
            if ship is None: return  
            BM.supress_menu = True
            self.selected = ship
            if ship.faction == 'Player' and play_voice:
                if ship.pilot is not None:
                    ship.voice('Sel')
                else:
                    if ship.selection_voice is not None:
                        if not type(ship.selection_voice) is list:
                            renpy.music.play(ship.selection_voice,channel = ship.voice_channel)
                        else:
                            random_voice = renpy.random.choice(ship.selection_voice)
                            renpy.music.play(random_voice,channel = ship.voice_channel)

            if self.mission != 'skirmish' and BM.phase != 'formation':
                renpy.show_screen('commands')
                ship.movement_tiles = get_movement_tiles(ship)
                self.selectedmode = True

        def unselect_ship(self,ship):
            renpy.hide_screen('commands')
            self.selectedmode = False
            self.selected = None
            self.targetingmode = False
            if ship != None:
                ship.movement_tiles = []

        def dispatch_handler(self, result, dispatch_type = 'battle'):
            ui_action = None
            #check handling of dispatcher
            if result is None: return self.common_none
            elif isinstance(result, bool): return self.common_bool
            elif isinstance(result, list):
                disp_type = dispatch_type + "_dispatcher"
                ui_action = getattr(self, disp_type).get(result[0], self.common_unexpected)
            else:
                disp_type = dispatch_type + "_dispatcher"
                ui_action = getattr(self, disp_type).get(result, self.common_unexpected)
            return ui_action

        ########################################################
        ## Common dispatcher
        ########################################################
        def common_unexpected(self):
            if isinstance(self.result, list):
                self.debug_log.append("Unexpected dispatcher key: " + str(self.result[0]))
            else:
                self.debug_log.append("Unexpected dispatcher key: " + self.result)

        def common_none(self):
            pass

        def common_bool(self):
            pass

        def common_zoom(self):
            zoom_handling(self.result, self)

        def common_next_ship(self):
            templist = []
            for ship in player_ships:
                if ship.location == None:
                    templist.append(ship)

            if self.selected == None:
                if len(templist) > 0:
                    self.select_ship(templist[0])
            else:
                if self.selected.location != None:
                    set_cell_available(self.selected.location)
                if self.selected in templist:
                    index = templist.index(self.selected)
                else:
                    index = 0
                if index == (len(templist)-1):
                    index = 0
                else:
                    index += 1
                self.select_ship(templist[index])

            if self.selected != None:
                self.targetwarp = True
                renpy.show_screen('mousefollow')

        def common_deselect(self):
            #if you picked up an enemy unit that was already put down right clicking should delete it entirely
            #player ships automatically return to the blue pool to be placed again later.
            if self.selected != None:
                if self.selected in enemy_ships:
                    self.ships.remove(self.selected)
                    enemy_ships.remove(self.selected)
            self.targetwarp = False
            renpy.hide_screen('mousefollow')
            self.unselect_ship(self.selected)
        ########################################################
        ## Common dispatcher end
        ########################################################
        #------------------------------------------------------#
        ########################################################
        ## Skirmish dispatcher
        ########################################################
        #similar to formation. Should be merged?
        def skirmish_start(self):
            if len(enemy_ships) == 0:
                show_message('Please add at least 1 enemy ship')
                renpy.jump('mission_skirmish')
            player_ship_present = False

            for ship in player_ships:
                if ship.location != None:
                    player_ship_present = True
            if not player_ship_present:
                 show_message('Please add at least 1 player ship')
                 renpy.jump('mission_skirmish')

            renpy.hide_screen('player_unit_pool_collapsed')
            renpy.hide_screen('enemy_unit_pool_collapsed')
            renpy.hide_screen('player_unit_pool')
            renpy.hide_screen('enemy_unit_pool')
            renpy.hide_screen('mousefollow')
            renpy.hide_screen('battle_screen')
            renpy.hide_screen('store_union') #seems like it has trouble staying closed?
            self.battlemode = False

        def skirmish_quit(self):
            renpy.hide_screen('store_union') #seems like it has trouble staying closed?
            renpy.hide_screen('player_unit_pool_collapsed')
            renpy.hide_screen('enemy_unit_pool_collapsed')
            renpy.hide_screen('player_unit_pool')
            renpy.hide_screen('enemy_unit_pool')
            renpy.hide_screen('mousefollow')
            renpy.hide_screen('battle_screen')
            
            BM.cmd = store.tempcmd
            BM.money = store.tempmoney
            BM.mission = None
            store.player_ships = store.player_ships_original
            store.sunrider = store.original_sunrider
            BM.mission = None
            BM.ships = []
            for pship in player_ships:
                BM.ships.append(pship)
            clean_battle_exit()
            renpy.jump('dispatch')

        def skirmish_remove(self):
            if self.remove_mode:
                self.remove_mode = False
            else:
                self.remove_mode = True

        def skirmish_playermusic(self):
            store.PlayerTurnMusic = self.result[1]
            show_message('Player music was changed')

        def skirmish_enemymusic(self):
            store.EnemyTurnMusic = self.result[1]
            show_message('Enemy music was changed')

        def skirmish_selection(self):
            # this result can be from one of the imagebuttons in the pool screens or returned from
            # MouseTracker because a hex with a unit in it was clicked.
            selected_ship = self.result[1]
            # BM.selected = selected_ship

            if self.remove_mode:
                if selected_ship.location != None:
                    if selected_ship.faction != 'Player':
                        if selected_ship in enemy_ships:
                            self.ships.remove(selected_ship)
                            enemy_ships.remove(selected_ship)
                            set_cell_available(selected_ship.location)
                    else:
                        set_cell_available(selected_ship.location)
                        selected_ship.location = None


            else:  #normal mode
                self.targetwarp = True
                renpy.show_screen('mousefollow')

                if selected_ship.faction == 'Player':
                    self.select_ship(selected_ship)
                else:
                    if selected_ship.location != None:
                        self.select_ship(selected_ship)
                        if selected_ship in enemy_ships:
                            self.ships.remove(self.selected)
                            enemy_ships.remove(self.selected)
                    else:
                        self.selected = copy(selected_ship) #breaks alias
                        self.selected.weapons = self.selected.default_weapon_list

            if self.selected != None:
                if self.selected.location != None:
                    set_cell_available(self.selected.location)
                self.selected.location = None

        def skirmish_warptarget(self):
            # returned from MouseTracker if you click on an empty hex when BM.warptarget == True.
            if self.selected != None:
                new_location = self.result[1]
                set_cell_available(new_location,True)

                if self.selected.faction != 'Player':
                    enemy_ships.append(self.selected)
                    self.ships.append(self.selected)

                self.selected.location = new_location

                if self.selected.faction != 'Player' and pygame.key.get_mods() != 0:
                    self.selected = copy(self.selected) #breaks alias
                else:
                    self.targetwarp = False
                    renpy.hide_screen('mousefollow')
                    self.unselect_ship(self.selected)

            sort_ship_list()
        ########################################################
        ## Skirmish dispatcher end
        ########################################################
        def skirmish_phase(self):
            self.result = ui.interact()
            self.dispatch_handler(self.result, 'skirmish')()

        #------------------------------------------------------#
        ########################################################
        ## Formation dispatcher
        ########################################################
        def formation_start(self):
            #check if there are still player units that are not placed
            unplaced_units = False
            for ship in player_ships:
                if ship.location == None:
                    unplaced_units = True
            if unplaced_units:
                show_message(_('there are still ships you have not placed!'))
            else:
                renpy.hide_screen('player_unit_pool_collapsed')
                renpy.hide_screen('enemy_unit_pool_collapsed')
                renpy.hide_screen('player_unit_pool')
                renpy.hide_screen('enemy_unit_pool')
                renpy.hide_screen('mousefollow')
                self.phase = 'Player'
                battle_setup()
                renpy.jump('mission{}'.format(self.mission))

        def formation_selection(self):
            # this result can be from one of the imagebuttons in the pool screens or returned from
            # MouseTracker because a hex with a unit in it was clicked.
            selected_ship = self.result[1]

            if selected_ship.faction == 'Player':
                self.targetwarp = True
                renpy.show_screen('mousefollow')
                self.select_ship(selected_ship)

                if self.selected.location != None:
                    set_cell_available(self.selected.location)
                self.selected.location = None

        def formation_warptarget(self):
            # returned from MouseTracker if you click on an empty hex when self.warptarget == True.
            if self.selected != None:
                new_location = self.result[1]

                #when setting up before a mission you can't put your ships farther to the right than column 7
                if new_location[0] > self.formation_range:
                    show_message(_('too far infield'))
                else:
                    set_cell_available(new_location,True) #passing True actually sets it unavailable

                    if self.selected.faction != 'Player':
                        enemy_ships.append(self.selected)
                        self.ships.append(self.selected)

                    self.selected.location = new_location

                    if self.selected.faction != 'Player' and pygame.key.get_mods() != 0:
                        self.selected = copy(self.selected) #breaks alias
                    else:
                        self.targetwarp = False
                        renpy.hide_screen('mousefollow')
                        self.unselect_ship(self.selected)
        ########################################################
        ## Formation dispatcher end
        ########################################################
        def formation_phase(self):
            self.phase='formation'
            while True:
                self.result = ui.interact()
                self.dispatch_handler(self.result,'formation')()
                if self.battlemode == False: #whenever this is set to False battle ends.
                    break
            return
        #------------------------------------------------------#
        ########################################################
        ## Battle dispatcher
        ########################################################
        def battle_anime(self):
            if not hasattr(store,'damage'):
                store.damage = 50
            if not hasattr(self,'attacker'):
                self.attacker = sunrider
            if not hasattr(store,'hit_count'):
                store.hit_count = 1
            if not hasattr(store,'total_armor_negation'):
                store.total_armor_negation = 10
            if not hasattr(store,'total_shield_negation'):
                store.total_shield_negation = 10
            if not hasattr(store,'total_flak_interception'):
                store.total_flak_interception = 0
            if self.target == None:
                self.target = sunrider
            try:
                renpy.call_in_new_context('atkanim_legion_missile')
            except:
                show_message('animation label does not exist!')

        def battle_cheat(self):
            self.cmd = 99999
            for ship in player_ships:
                ship.set_stat('en',9999)

        def battle_inst_win(self):
            instant_win()

        def battle_deselect(self):
            if self.active_weapon != None:
                self.active_weapon = None
                self.targetingmode = False
                self.weaponhover = None
                self.supress_menu = True
                renpy.restart_interaction()
            elif self.selected != None:
                self.unselect_ship(self.selected)
            else:
                pass

        def battle_next_ship(self):
            if self.selected == None or not BM.selected in player_ships: #rollback can screw with the identity of BM.selected
                self.select_ship(player_ships[0])
                return

            if self.selected != None and len(player_ships) > 1:
                if self.selected.faction == 'Player':
                    index = player_ships.index(self.selected)
                    looping = True
                    while looping:
                        if index == (len(player_ships)-1):
                            index = 0
                        else:
                            index += 1
                        if player_ships[index].location != None:
                            looping = False
                    self.select_ship(player_ships[index])

        def battle_previous_ship(self):
            if self.selected is None or not BM.selected in player_ships:
                self.select_ship(player_ships[0])
                return
                
            if self.selected != None and len(player_ships) > 1:
                if self.selected.faction == 'Player':
                    index = player_ships.index(self.selected)
                    looping = True
                    while looping:
                        if index == 0:
                            index = len(player_ships)-1
                        else:
                            index -= 1
                        if player_ships[index].location != None:
                            looping = False
                    self.select_ship(player_ships[index])

        #def battle_mousefollow_click(self):
        #    pass

        def battle_zoom(self):
            zoom_handling(self.result,self) #see funtion.rpy how this is handled. it took a LONG time to get it to a point I am happy with
            if self.selectedmode: self.selected.movement_tiles = get_movement_tiles(self.selected)

        def battle_selection(self):
            if self.result is None: return
            if self.result[1] is None: return
            if not hasattr(self.result[1],'name'): return
            
            self.target = self.result[1]
            self.hovered = None

            #if no ship is currently selected select the ship that was just clicked on.
            if self.selected == None:
                self.select_ship(self.target)
                return

            #you do not have a weapon active.
            if not self.targetingmode:
                #did you select the active ship?
                if self.target == self.selected:
                    self.unselect_ship(self.selected)
                else:
                    self.select_ship(self.target)
                return
            #you do have a weapon active.
            else:
                if self.active_weapon is None: return
                
                weapon = self.active_weapon
                #is this a valid target?
                if weapon.wtype == 'Melee':
                    if get_ship_distance(self.selected,self.target) > 1 or self.target.stype != 'Ryder':
                        return
                self.targetingmode = False

                #did you click the currently selected ship?
                if self.target == self.selected:
                    if weapon.wtype == 'Support':
                        pass  #you clicked your selected ship with a support weapon active. do not end the method.
                    else:
                        self.unselect_ship(self.result[1])
                        return #do end the method. this is important.
                #did you click an ally?
                elif self.target.faction == 'Player':
                    if weapon.wtype == 'Support' or weapon.wtype == 'Special':
                        if self.target.cth <= 0:
                            self.draggable = False
                            renpy.say('',"The target is out of range, captain!")
                            self.draggable = True
                            self.targetingmode = True #try again
                            return #do end the method, this is important.
                        else:
                            #you clicked an ally unit with a support weapon active. do not end the method.
                            pass
                    else:
                        self.select_ship(self.target)
                        return

                #you clicked an enemy with an active weapon.
                else:
                    #check if you can hit the target. if not, let the player know he's stupid.
                    if self.target.cth <= 0:
                        self.draggable = False
                        if self.mission == 1 and legion_destroyed == True:
                            voicer = 'Kryska'
                        else:
                            voicer = 'Ava'
                        renpy.say(voicer,_('It\'s hopeless, captain!'))
                        self.draggable = True
                        self.targetingmode = False
                        self.active_weapon = None
                        self.weaponhover = None
                        return # end the method, this is important.
                    else:
                        self.attacker = self.selected
                        if self.active_weapon.wtype == 'Curse' or self.active_weapon.wtype == 'Special':
                            weapon.fire(self.selected,self.target)
                            self.active_weapon = None
                            self.weaponhover = None
                            if self.selected != None:
                                self.selected.movement_tiles = get_movement_tiles(self.selected)
                            return

                        elif self.active_weapon.wtype == 'Melee':
                            pass #do not show the atkanim, because there aren't any for melee.
                        else:
                            #show attack animation. now defunct
                            pass
                        
                            #try:
                                #animation_name = self.active_weapon.wtype.lower()
                                #if weapon.animation_name != None:
                                    #animation_name = weapon.animation_name
                                #renpy.call_in_new_context('atkanim_{}_{}'.format(self.selected.animation_name,animation_name))
                            #except:
                                #show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(self.selected.animation_name,self.active_weapon.wtype.lower()))
                                
                                
            #up till now nothing ended the method meaning it's okay to fire the weapon at the target - be it support or not.
            result = weapon.fire(self.selected,self.target)
            
            #chivo
            if self.selected.name == 'Black Jack': chivo_process('Black Jack')
            
            if type(result) is dict:
                damage_multiple_ships(result,attacker = self.selected)
            else:
                self.target.receive_damage(result,self.selected,weapon.wtype)
            if self.selected != None:
                self.selected.movement_tiles = get_movement_tiles(self.selected)
#            update_stats() - updated in receive_damage()
            self.active_weapon = None
            self.weaponhover = None
#            renpy.hide_screen('battle_screen')
#            renpy.show_screen('battle_screen')
            return #battle_selection end

        def battle_move(self): #this means you clicked on one of the blue squares indicating you want to move somewhere
            self.selected.move_ship(self.result[1],self) #result[1] is the new location to move towards
            update_stats()

        def battle_cancel_movement(self):
            #expect that any actions will remove cancel button
            self.battle_log_pop()
            ship = self.selected
            ship.en = increment_attribute(ship,'en',get_distance(ship.location,ship.current_location)*ship.get_stat('move_cost'))
            a = ship.location[0]-1  #make the next line of code a little shorter
            b = ship.location[1]-1
            self.grid[a][b] = False #tell the BM that the old cell is now free again

            ship.location = ship.current_location

            a = ship.location[0]-1  #make the next line of code a little shorter
            b = ship.location[1]-1
            self.grid[a][b] = True #tell the BM that the old cell is now free again

            ship.movement_tiles = get_movement_tiles(ship)
            update_stats()

        def battle_order_injection_rods(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]
                
                for ship in player_ships:
                    ship.set_buff(InjectionRods)
                
                #bookkeeping
                self.battle_log_insert(['order'], "ORDER: ALL POWER TO ENGINES")
                BM.order_used = True
                store.show_message(_('all ships gained improved mobility!'))

                #play a voice
                random_ship = renpy.random.choice( get_player_ships_in_battle() )
                if random_ship.pilot is not None:
                    random_ship.voice('HitBuff')
                else:
                    if random_ship.buffed_voice is not None:
                        random_voice = renpy.random.choice(random_ship.buffed_voice)
                        renpy.music.play('{}'.format(random_voice),channel = random_ship.voice_channel)

                #animation
                for ship in player_ships:
                    ship.getting_buff = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.pause(1)
                for ship in player_ships:
                    ship.getting_buff = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                update_stats()

            else:
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                self.order_used = False
        
        def battle_order_summon_battleship(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                if self.temp_battleship_active:
                    renpy.say('Ava','You can not summon another battleship at this time, captain.')
                    return
                self.cmd -= self.orders[self.result[0]][0]
                if self.selected != None:
                    self.unselect_ship(self.selected)
                temp_battleship = create_ship( TemporaryAllianceBattleship() )
                self.selected = temp_battleship #show the sunrider's label
                self.phase = None #disables the end turn button
                self.order_used = False #debug
                self.targetwarp = True
                renpy.hide_screen('commands')
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.show_screen('mousefollow')
                looping = True
                while looping:
                    result = ui.interact()
                    if result[0] == "warptarget":
                        new_location = result[1]
                        store.flash_locations = [ new_location ]
                        self.warping = True
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                        renpy.hide_screen('mousefollow')
                        renpy.music.play('sound/large_warpout.ogg', channel = 'sound5')
                        renpy.pause(1.0, hard=True) #hard means unskippable
                        self.warping = False
                        self.selected.location = new_location
                        x,y = self.selected.location
                        self.grid[x-1][y-1] = True
                        looping = False
                        self.phase = 'Player'
                        self.targetwarp = False
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                        self.temp_battleship_active = True

                    if result[0] == "zoom":
                        zoom_handling(result,self)

                    if result[0] == 'deselect':
                        self.end_turn_callbacks.remove(temp_battleship.expiry_callback)
                        BM.ships.remove(temp_battleship)
                        player_ships.remove(temp_battleship)
                        self.cmd += self.orders['SUMMON BATTLESHIP'][0]
                        looping = False
                        renpy.hide_screen('mousefollow')
                        self.phase = 'Player'
                        self.targetwarp = False
            else:
                self.order_used = False
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                
        def battle_order_resurrection(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]

                renpy.show_screen('ryderlist')
                result = ui.interact()

                if result[0] == 'deselect':
                    self.cmd += self.orders['RESURRECTION'][0]
                    renpy.hide_screen('ryderlist')
                    self.order_used = False
                    return

                elif result[0] == 'selection':
                    revived_ship = result[1]
                    renpy.hide_screen('ryderlist')
                    launch_location = get_free_spot_near(sunrider.location) #so useful
                    revived_ship.set_stat('en',0) 
                    revived_ship.set_stat('hp',revived_ship.get_stat('max_hp'))
                    destroyed_ships.remove(revived_ship)
                    player_ships.append(revived_ship)
                    self.ships.append(revived_ship)
                    revived_ship.location = launch_location
                    set_cell_available(launch_location, True) #the optional True actually lets me set this cell /un/available
                    message = "ORDER: {0} is resurrected".format(revived_ship.name)
                    self.battle_log_insert(['order'], message)
                    BM.order_used = True
                    if BM.selected is not None: 
                        temp_selected = BM.selected
                        BM.unselect_ship(BM.selected)
                        BM.select_ship(temp_selected,False)

                    #Phoenix rising from the ashes!
                    if revived_ship.name == 'Phoenix':
                        revived_ship.set_stat('en',revived_ship.get_stat('max_en') / 2)
                        chivo_process('Phoenix Down')

                    #wipe all modifiers after a res
                    revived_ship.buffs = [x for x in revived_ship.buffs[:] if x.name == "Disruption"] #disruption can stay. executive order.

                    #play the resurrect voice
                    if revived_ship.pilot is not None:
                        revived_ship.voice('Rev')
                        
                    update_stats() #new unit could have shield generation
                    
                    
            else:
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                self.order_used = False

        def battle_order_all_guard(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]

                strategy,remaining_turns = self.active_strategy
                
                if strategy == 'full forward':
                    show_message(_('Full Forward order cancelled!'))
                    for ship in player_ships:
                        ship.remove_buff('Full Forward')
                
                if strategy == "all guard" and remaining_turns == 3:
                    show_message(_('alredy active!'))
                    self.order_used = False
                    self.cmd += self.orders[self.result[0]][0]
                
                #actually process the buffs
                self.active_strategy = ['all guard',3]
                for ship in player_ships:
                    ship.set_buff(AllGuard)
                    
                #bookkeeping
                self.battle_log_insert(['order'], "ORDER: ALL GUARD")
                BM.order_used = True
                store.show_message(_('all ships gained improved flak, shielding and evasion!'))

                #play a voice
                random_ship = renpy.random.choice( get_player_ships_in_battle() )
                if random_ship.pilot is not None:
                    random_ship.voice('HitBuff')
                else:
                    if random_ship.buffed_voice is not None:
                        random_voice = renpy.random.choice(random_ship.buffed_voice)
                        renpy.music.play('{}'.format(random_voice),channel = random_ship.voice_channel)

                #animation
                for ship in player_ships:
                    ship.getting_buff = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.pause(1)
                for ship in player_ships:
                    ship.getting_buff = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                update_stats()

            else:
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                self.order_used = False

        def battle_order_full_forward(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]

                strategy,remaining_turns = self.active_strategy
                
                if strategy == 'all guard':
                    show_message(_('All Guard order cancelled!'))
                    for ship in player_ships:
                        ship.remove_buff('All Guard')
                
                if strategy == "full forward" and remaining_turns == 3:
                    show_message(_('alredy active!'))
                    self.order_used = False
                    self.cmd += self.orders[self.result[0]][0]
                
                #actually process the buffs
                self.active_strategy = ['full forward',3]
                for ship in player_ships:
                    ship.set_buff(FullForward)
                
                #bookkeeping
                self.battle_log_insert(['order'], "ORDER: FULL FORWARD")
                BM.order_used = True
                store.show_message(_('All ships gain 20% damage and 15% accuracy!'))
                
                #play a voice
                if BM.english_battle_voices:
                    try:
                        renpy.music.play("sound/Voice/Shields/Cpt Shields 4.ogg",channel="kayvoice")
                        renpy.pause(4)
                    except:
                        pass 
                        
                random_ship = player_ships[renpy.random.randint(0,len(player_ships)-1)]
                if random_ship.pilot is not None:
                    random_ship.voice('HitBuff')
                else:
                    if random_ship.buffed_voice is not None:
                        random_voice = renpy.random.randint(0,len(random_ship.buffed_voice)-1)
                        renpy.music.play('{}'.format(random_ship.buffed_voice[random_voice]),channel = random_ship.voice_channel)
                
                #animation
                for ship in player_ships:
                    ship.getting_buff = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.pause(1)
                for ship in player_ships:
                    ship.getting_buff = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')

            else:
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                self.order_used = False

        def battle_order_repair_drones(self):
            if self.cmd >= self.orders[self.result[0]][0]:
                if sunrider.repair_drones != None:
                    if sunrider.repair_drones <= 0:
                        show_message(_('no available droids in storage!'))
                        self.order_used = False
                        return
                    else:
                        sunrider.repair_drones -= 1
                self.cmd -= self.orders[self.result[0]][0]
                message = _("ORDER: Repair drones restore {}% of Sunrider's hull integrity").format(str(int(BM.repair_drone_heal*100)))
                self.battle_log_insert(['order'], message)
                show_message(message)
                BM.order_used = True
                sunrider.hp = increment_attribute(sunrider,'hp',int(sunrider.max_hp * BM.repair_drone_heal))
                if sunrider.hp > sunrider.max_hp: sunrider.hp = sunrider.max_hp
                sunrider.getting_buff = True
                if BM.english_battle_voices:
                    try:
                        renpy.music.play("sound/Voice/Shields/Cpt Shields 9.ogg",channel="kayvoice")
                        renpy.pause(4)
                    except:
                        pass                        
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                sunrider.voice('HitBuff')
                renpy.pause(1)
                sunrider.getting_buff = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
            else:
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                self.order_used = False

        def battle_short_range_warp(self):
            order_cost,order_name = self.orders['SHORT RANGE WARP'] #yes, second term is pointless. I don't even remember why it exists anymore
            if self.cmd >= order_cost:
                self.cmd -= order_cost
                if self.selected != None:
                    self.unselect_ship(self.selected)
                self.selected = sunrider #show the sunrider's label
                self.phase = None #disables the end turn button
                self.order_used = False #debug
                self.targetwarp = True
                renpy.hide_screen('commands')
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.show_screen('mousefollow')
                looping = True
                while looping:
                    result = ui.interact()
                    if result[0] == "warptarget":
                        new_location = result[1]
                        store.flash_locations = [ sunrider.location,new_location ]
                        self.warping = True
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                        renpy.hide_screen('mousefollow')
                        renpy.music.play('sound/large_warpout.ogg', channel = 'sound5')
                        renpy.pause(1.0, hard=True) #hard means unskippable
                        self.warping = False
                        x,y = self.selected.location
                        self.grid[x-1][y-1] = False
                        self.selected.location = new_location
                        x,y = self.selected.location
                        self.grid[x-1][y-1] = True
                        looping = False
                        self.phase = 'Player'
                        self.targetwarp = False
                        renpy.hide_screen('battle_screen')
                        renpy.show_screen('battle_screen')
                        self.orders['SHORT RANGE WARP'] = [order_cost+250,order_name]
                        chivo_process("Can't Touch This")

                    if result[0] == "zoom":
                        zoom_handling(result,self)

                    if result[0] == 'deselect':
                        self.cmd += order_cost
                        looping = False
                        renpy.hide_screen('mousefollow')
                        self.phase = 'Player'
                        self.targetwarp = False
            else:
                self.order_used = False
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')

        def battle_retreat(self):
            clean_battle_exit()
            renpy.jump('retreat')

        def battle_order_vanguard_cannon(self):
            #range is now infinite! booyah!
            if self.cmd >= self.orders[self.result[0]][0]:
                self.cmd -= self.orders[self.result[0]][0]
                self.vanguardtarget = True
                if BM.english_battle_voices:
                    try:
                        renpy.music.play("sound/Voice/Shields/Cpt Shields 13.ogg",channel="kayvoice")
                        renpy.pause(3)
                    except:
                        pass
                looping = True
                while looping:
                    result = ui.interact()

                    if result[0] == "selection":
                        #the player has clicked a location
                        loc1 = sunrider.location
                        loc2 = result[1].location
                        
                        if self.vanguard_splash:
                            listlocs = interpolate_hex_splash(loc1, loc2)
                        else:
                            listlocs = interpolate_hex(loc1, loc2)
                        
                        hasship = False

                        #test whether there are targets in the path.
                        for loc in listlocs:
                            if not get_cell_available(loc):
                                for ship in enemy_ships:
                                    if ship.location[0] == loc[0] and ship.location[1] == loc[1]:
                                        hasship = True
                        if not hasship:
                            #no good targets found
                            self.cmd += self.orders['VANGUARD CANNON'][0]
                            looping = False
                            self.order_used = False
                            self.vanguardtarget = False
                            return

                        self.vanguardtarget = False  #resolve firing the VGC, no further targeting is required.
                        if not renpy.music.get_playing() == "Music/Sora_no_Kodoh.ogg":
                            renpy.music.play('Music/The_Final_Battle_Cut.ogg')
                            renpy.music.queue('Music/The_Final_Battle.ogg',loop=True)
                        
                        #show order animation/movie
                        renpy.call_in_new_context('atkanim_sunrider_vanguard')
                        
                        #show map wave
                        BM.vanguard = loc2
                        prepare_map_animation()
                        renpy.pause(3)
                        BM.vanguard = False
                        end_map_animation()
                        
                        # store.damage = BM.vanguard_damage
                        # store.hit_count = 1
                        # store.total_armor_negation = 0
                        # store.total_shield_negation = 0
                        # store.total_flak_interception = 0
                        self.battle_log_insert(['order'], "ORDER: FIRE VANGUARD CANNON")
                        
                        #deal damage
                        shipdict = {}
                        main_path = interpolate_hex(loc1, loc2)
                        for ship in enemy_ships:
                            if ship.location in listlocs:
                                shipdict[ship] = BM.vanguard_damage if ship.location in main_path else BM.vanguard_damage / 2
                        damage_multiple_ships(shipdict,no_cmd = True)
                        looping = False
                        chivo_process('This is My Command!')

                        if BM.battlemode: #have to check this because killing the last enemy unit ends the battle.
                            renpy.hide_screen('battle_screen')
                            renpy.show_screen('battle_screen')
                            BM.order_used = True

                    if result[0] == 'deselect':
                        self.cmd += self.orders['VANGUARD CANNON'][0]
                        looping = False
                        self.vanguardtarget = False
                        self.order_used = False

            else:
                if self.english_battle_voices:
                    renpy.music.play('sound/Voice/Ava/Ava Others 9.ogg',channel='avavoice')
                else:
                    renpy.music.play('sound/Voice/ava_Others_05.ogg',channel='avavoice')
                self.order_used = False

        def toggle_player_ai(self):
            self.player_ai = not self.player_ai

        def battle_end_turn(self):
            if self.targetingmode:
                self.battle_deselect()
            store.show_sidemenu = False
            self.end_player_turn()
            return
        ########################################################
        ## Battle dispatcher end
        ########################################################
        def start(self):
            self.battle_log_insert(['system'], "-------------BATTLE START-------------")
            BM.player_ai = False
            battlemode() #stop scrollback and set BM.battlemode = True
            update_stats()  #used to update some attributes like armour and shields
            renpy.show_screen('battle_screen')
            if start_funcs != []:
                for item in start_funcs:
                    if eval(item[0]): item[1]()
                    
            #formation feature
            if self.editableformations():
                self.phase = 'formation'

                for ship in player_ships:
                    if ship.location != None:
                        set_cell_available(ship.location)
                        ship.location = None                    
                    if not ship in BM.ships:
                        BM.ships.append(ship)

                renpy.show_screen('player_unit_pool_collapsed')
                renpy.show_screen('player_unit_pool')
                BM.selectedmode = False #failsafe
                BM.targetmode = False
                BM.selected = None #the selected unit doesn't show up in the pool
                self.formation_phase()
            else:
                battle_setup()
                self.phase = 'Player'
                self.jumptomission()

        def jumptomission(self):
            renpy.jump('mission{}'.format(self.mission))

        def editableformations(self):
            if hasattr(self,'formation_editable'):
                return self.formation_editable
            else:
                return True

        def battle(self):
            global battle_turn_count
            for ship in player_ships:
                if not hasattr(ship, 'blbl'):
                    ship.blbl = ship.lbl

            if self.player_ai:
                self.player_AI()
                self.toggle_player_ai()
                self.result = 'endturn'
            else:
                #battle_screen should be shown, and ui.interact waits for your input. 'result' stores the value return from the Return actionable in the screen
                self.result = ui.interact()

            if store.Difficulty < self.lowest_difficulty:
                self.lowest_difficulty = store.Difficulty

            self.just_moved = False #this sets it so you can no longer take back your move
            renpy.hide_screen('game_over_gimmick') #disables the screensaver gimmick

            if self.stopAI and sunrider.hp < 0:  #some failsafe checking. stopAI functions like an emergency stop for AI code
                renpy.jump('sunrider_destroyed')
            if hasattr(store,'mochi'):
                if hasattr(mochi,'hp'):
                    if mochi.hp < 0 and mochi in player_ships:
                        renpy.jump('sunrider_destroyed')

            #sanity check
            self.taking_damage = False
            for ship in self.ships:
                if ship.hp <= 0:
                    destroyed_ships.append(ship)
                    if ship in player_ships:
                        player_ships.remove(ship)
                    if ship in enemy_ships:
                        enemy_ships.remove(ship)
                    if ship in self.ships:
                        self.ships.remove(ship)
                        
            if battle_interupts != []:
                for item in battle_interupts: 
                    battle_interupts.remove(item)
                    item()

            self.dispatch_handler(self.result)()

            self.check_for_loss()
            self.check_for_win()
            return

        def check_for_loss(self):
            if len(player_ships) == 0:
                self.you_lose()

        def you_lose(self,*args):  #mods can overwrite for greater flexibility. also, you can replace a units destroy method with this.
            BM.stopAI = True
            sunrider.hp = -1
            if self.mission != 'skirmishbattle':
                renpy.jump('sunrider_destroyed')
            else:
                show_message(_('You were defeated! better luck next time...'))
                clean_battle_exit()
                renpy.jump('dispatch')

        def boss_died(self, deadboss):
            if (self.mission != 'skirmishbattle'):
                self.you_win()

        def check_for_win(self):
            if len(enemy_ships) == 0 and BM.win_when_alone:
                self.you_win()

        def you_win(self):
            self.stopAI = True
            if self.battlemode: #Ignore calls to you_win if we're not actually in battle mode.
                renpy.hide_screen('commands')
                self.battle_end()
                renpy.hide_screen('battle_screen')
            if renpy.has_label('after_mission{}'.format(BM.mission)):
                renpy.jump('after_mission{}'.format(BM.mission))

#ending a turn
        def end_player_turn(self):
            #bookkeeping
            self.battle_log_insert(['system'], "---------Player turn end---------")
            self.battle_log_trimm()
            
            #call all chivos and process end of turn
            for chivo in persistent.achievements:
                if persistent.achievements[chivo].active:
                    persistent.achievements[chivo].end_turn()
            
            self.turn_count += 1
            
            #cleanup
            renpy.hide_screen('commands')
            self.selected = None #some sanity checking
            self.target = None
            self.moving = False
            self.selectedmode = False
            self.targetingmode = False
            self.active_weapon = None
            self.weaponhover = None
            
            #reset short range warp order to standard cost
            if 'SHORT RANGE WARP' in self.orders: self.orders['SHORT RANGE WARP'] = [750,'short_range_warp' ]
            
            #end of turn animation and sound
            renpy.music.play(EnemyTurnMusic)
            renpy.call_in_new_context('endofturn')

            #reset flak
            for ship in self.ships:
                ship.flak_effectiveness = 100

            #call the AI to take over
            self.enemy_AI() 
            self.battle_log_insert(['system'], "---------{0} turn end---------".format(self.phase))
            self.battle_log_trimm()
             ##I have NO idea why this dumb workaround is needed, but the destroy() method -somehow- doesn't want to jump to this label sometimes.
            if sunrider.hp <= 0:
                renpy.jump('sunrider_destroyed')

            #end of turn resets etc
            for ship in self.ships:
                ship.flak_effectiveness = 100
                ship.getting_curse = False #failsafes
                ship.getting_buff = False
            for ship in player_ships:
                ship.en = ship.max_en * (100 + ship.modifiers['energy regen'][0] ) / 100
                if ship.en < 0: ship.en = 0
            for ship in BM.ships:
                ship.turns_alive += 1
                
            self.active_weapon = None
            self.targetingmode = False
            self.target = None
            self.selected = None
            self.selectedmode = False
            self.order_used = False
            self.moving = False

            #run the end of turn callbacks
            if BM.end_turn_callbacks != []:
                for callback in BM.end_turn_callbacks:
                    callback()

            if self.battlemode:
                renpy.music.play(PlayerTurnMusic)
                renpy.call_in_new_context('endofturn')
            renpy.take_screenshot()

            # I've sometimes been getting this error for some silly reason:
            # WindowsError: [Error 183] Cannot create a file when that file already exists
            # may just be me, but to be safe I'll put a catch here
            try:
                renpy.save('beginturn')
            except:
                debuglog_add('making start of turn save failed')
                pass

        def player_AI(self):

              ##lead ships don't care about looking for other ships for protection
              ##other ships come to them! instead, lead ships typically go on the
              ##offensive, dragging allies along.
            self.support_ships = []
            self.lead_ships = []
            total_defense = 0
            update_stats()

            #support ships take their turn first, so they can improve the effects of all other units.
            for pship in player_ships:
                if pship.support:
                    self.support_ships.append(pship)

            for pship in player_ships:
                total_defense += pship.shield_generation + pship.flak + pship.armor
            average_defense = total_defense / float(len(player_ships))

              ##because I assume  most of the time there will be many mooks and only
              ##a few high defense ships the few that are are definitely above average.
              ##this method is very dynamic and doesn't rely on blueprint flags.
            for pship in player_ships:
                defense = pship.shield_generation + pship.flak + pship.armor
                if defense > average_defense and pship not in self.support_ships:
                    self.lead_ships.append(pship)

            for pship in self.support_ships:
                if BM.stopAI:
                    return

                pship.en = pship.max_en
                pship.lbl = im.MatrixColor(pship.blbl,im.matrix.brightness(0.3))

                #a number of people have reported crashes: Exception: ui.interact called with non-empty widget/layer stack.
                #this is but a work-around.
                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass

                # if config.developer:
                    # renpy.pause()

                try:
                    if not pship.modifiers['energy regen'][0] == -100:
                        pship.AI()
                    else:
                        show_message(_('the {} is disabled!').format(pship.name) )
                except:
                    pship.modifiers['energy regen'] = (0,0)
                    pship.AI()
                pship.lbl = pship.blbl

                ##the lead ships take their turn after the support ships.
            for pship in self.lead_ships:
                if BM.stopAI:
                    return

                pship.en = pship.max_en
                pship.lbl = im.MatrixColor(pship.blbl,im.matrix.brightness(0.3))

                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass
                # if config.developer:
                    # renpy.pause()

                try:
                    if not pship.modifiers['energy regen'][0] == -100:
                        pship.AI()
                    else:
                        show_message(_('the {} is disabled!').format(pship.name) )
                except:
                    pship.modifiers['energy regen'] = (0,0)
                    pship.AI()
                pship.lbl = pship.blbl

                ## the rest of the enemy units take their turns last
            for ship in player_ships:
                if BM.stopAI:
                    clear_ship_animations()
                    return
                #now all the non-lead and all the non-support ships take their turn
                if ship not in self.lead_ships and ship not in self.support_ships:

                    try:
                        if ship.modifiers['energy regen'][0] == -100:
                            show_message(_('the {} is disabled!').format(pship.name) )
                            ship.en = 0
                        else:
                            ship.en = ship.max_en
                    except:
                        ship.modifiers['energy regen'] = (0,0)
                        ship.en = ship.max_en

                    ship.lbl = im.MatrixColor(ship.blbl,im.matrix.brightness(0.3))
                    try:
                        renpy.pause(AI_WAIT_TIME)
                    except:
                        pass
                    # if config.developer:
                        # renpy.pause()
                    ship.AI()
                    ship.lbl = ship.blbl
                    clear_ship_animations() #failsafe

        def enemy_AI(self):

              ##lead ships don't care about looking for other ships for protection
              ##other ships come to them! instead, lead ships typically go on the
              ##offensive, dragging allies along.
            self.support_ships = []
            self.lead_ships = []
            total_defense = 0
            update_stats()

            #support ships take their turn first, so they can improve the effects of all other units.
            for eship in enemy_ships:
                if eship.support:
                    self.support_ships.append(eship)

            for eship in enemy_ships:
                total_defense += eship.shield_generation + eship.flak + eship.armor
            if len(enemy_ships) > 0:
                average_defense = total_defense / float(len(enemy_ships))
            else:
                average_defense = total_defense

              ##because I assume  most of the time there will be many mooks and only
              ##a few high defense ships the few that are are definitely above average.
              ##this method is very dynamic and doesn't rely on blueprint flags.
            for eship in enemy_ships:
                defense = eship.shield_generation + eship.flak + eship.armor
                if defense > average_defense and eship not in self.support_ships:
                    self.lead_ships.append(eship)

            for eship in self.support_ships:
                if BM.stopAI:
                    return

                eship.en = eship.max_en
                eship.lbl = im.MatrixColor(eship.blbl,im.matrix.brightness(0.3))
                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass
                # if config.developer:
                    # renpy.pause()

                try:
                    if not eship.modifiers['energy regen'][0] == -100:
                        eship.AI()
                        clear_ship_animations() #failsafe
                    else:
                        show_message(_('the {} is disabled!').format(eship.name) )
                except:
                    eship.modifiers['energy regen'] = (0,0)
                    eship.AI()
                eship.lbl = eship.blbl

                ##the lead ships take their turn after the support ships.
            for eship in self.lead_ships:
                if BM.stopAI:
                    return

                eship.en = eship.max_en
                eship.lbl = im.MatrixColor(eship.lbl,im.matrix.brightness(0.3))

                #a number of people have reported crashes: Exception: ui.interact called with non-empty widget/layer stack.
                #this is but a work-around.
                try:
                    renpy.pause(AI_WAIT_TIME)
                except:
                    pass

                # if config.developer:
                    # renpy.pause()

                try:
                    if not eship.modifiers['energy regen'][0] == -100:
                        eship.AI()
                    else:
                        show_message(_('the {} is disabled!').format(eship.name) )
                except:
                    eship.modifiers['energy regen'] = (0,0)
                    eship.AI()
                    clear_ship_animations() #failsafe
                eship.lbl = eship.blbl

                ## the rest of the enemy units take their turns last
            for ship in enemy_ships:
                if BM.stopAI:
                    return
                #now all the non-lead and all the non-support ships take their turn
                if ship not in self.lead_ships and ship not in self.support_ships:

                    try:
                        if ship.modifiers['energy regen'][0] == -100:
                            show_message(_('the {} is disabled!').format(ship.name) )
                            ship.en = 0
                        else:
                            if not ship.just_spawned: ship.en = ship.max_en
                    except:
                        ship.modifiers['energy regen'] = (0,0)
                        ship.en = ship.max_en

                    ship.lbl = im.MatrixColor(ship.blbl,im.matrix.brightness(0.3))

                    #a number of people have reported crashes: Exception: ui.interact called with non-empty widget/layer stack.
                    #this is but a work-around.
                    try:
                        renpy.pause(AI_WAIT_TIME)
                    except:
                        pass

                    ship.AI()
                    clear_ship_animations() #failsafe
                    ship.lbl = ship.blbl
            clear_ship_animations() #failsafe


        def battle_end(self, lost = False):
            """ending the battle - reset values for next battle"""
            self.battlemode = False #this ends the battle loop
            if self.selected != None: self.unselect_ship(self.selected)
            self.targetingmode = False
            self.vanguardtarget = False
            self.weaponhover = None
            self.hovered = None
            self.temp_battleship_active = False
            BM.enemy_vanguard_path = []
            renpy.hide_screen('tooltips')
            BM.phase = 'Player'
            if 'SHORT RANGE WARP' in self.orders: self.orders['SHORT RANGE WARP'] = [750,'short_range_warp' ]

            if store.Difficulty < self.lowest_difficulty:
                self.lowest_difficulty = store.Difficulty
                
            #dirty hack assuming there is only 1 drone.
            if len(self.drones) > 0:
                if self.drones[0].location is not None:
                    self.drones[0].location = None
                    liberty.shield_generation = self.drones[0].shield_generation

            if not lost:
                #show the victory screen
                renpy.music.stop()
                renpy.music.play('Music/Posthumus_Regnum_Cut.ogg', loop = False)
                renpy.hide_screen('commands')
                self.draggable = False
                renpy.show_screen('victory')
                renpy.pause(3.0)
                renpy.hide_screen('victory')
                
                #check Asaga's awakening and reset if required.
                if blackjack.has_weapon("Cancel Awakening"):
                    blackjack.remove_weapon("Cancel Awakening")
                    blackjack.register_weapon(AwakenAsaga())
                    
                #process end of mission callbacks to all chivos
                for chivo in persistent.achievements:
                    if not persistent.achievements[chivo].cleared:
                        persistent.achievements[chivo].end_mission()

                for drone in BM.drones:
                    drone.location = None
                
                store.repair_cost = 0
                store.total_money = 0
                store.intel_gain = 0
                store.boss_killed = False
                store.surrender_bonus = 0
                for ship in destroyed_ships:
                    if ship.faction == 'Player' and not ship.mercenary:
                        #cost for destroyed non-merc ships
                        store.repair_cost += int(ship.max_hp * 1.5)
                    else:
                        if ship.boss: store.boss_killed = True #check if a boss was killed
                        store.total_money += ship.money_reward

                if store.boss_killed:
                    for ship in enemy_ships:
                        if ship.hp > 0:
                            store.surrender_bonus += ship.money_reward / 2

                for ship in player_ships:
                    #cost for damage taken throughout the battle. healing is not counted
                    store.repair_cost += int(ship.total_damage*0.5)

                #SPACE WHALE TAX!
                penalty = 0.8 if store.Difficulty == 5 else 1
                
                store.intel_gain = int((store.total_money + store.surrender_bonus)*penalty)
                store.net_gain = int(store.total_money + store.surrender_bonus - store.repair_cost)
                
                self.money += int(net_gain * penalty)
                self.intel += store.intel_gain
                
                if self.money >= 50000: chivo_process('Mogul')

                renpy.show_screen('victory2')
                renpy.pause(1)
                renpy.hide_screen('victory2')
                self.draggable = True

            self.turn_count = 1
            self.active_strategy = [None,0]
            self.ships = []
            self.end_turn_callbacks = []
            self.selectedmode = False
            self.battle_log = []
            renpy.hide_screen("battle_log")
            setattr(store,'mission{}_complete'.format(str(BM.mission)),True)

            VNmode() #return to visual novel mode. this mostly just restores scrolling rollback
            for ship in destroyed_ships:
                if self.mission == 'skirmish' or (ship.faction == 'Player' and not ship.mercenary):
                    player_ships.append(ship)
                    self.ships.append(ship)
            for ship in player_ships[:]:
                if ship.temporary: player_ships.remove(ship)
                self.ships.append(ship)            
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
            self.covers = []
            renpy.hide_screen('battle_screen')
            renpy.hide_screen('commands')

            renpy.block_rollback()


    #SHIT A BUG IN THE CODE! KILL IT WITH FIRE!!!
                          #ug
                       #b
                      #g           bug
                      #u        bug
      #bugbug          b       g
            #bug      bugbug bu
               #bug  bugbugbugbugbugbug
  #bug   bug   bugbugbugbugbugbugbugbugb
     #bug   bug bugbugbugbugbugbugbugbugbu
   #bugbugbugbu gbugbugbugbugbugbugbugbugbu
  #bugbugbugbug
   #bugbugbugbu gbugbugbugbugbugbugbugbugbu
     #bug   bug bugbugbugbugbugbugbugbugbu
  #bug   bug  gbugbugbugbugbugbugbugbugb
               #bug  bugbugbugbugbugbug
            #bug      bugbug  bu
      #bugbug          b        g
                      #u         bug
                      #g            bug
                       #b
                        #ug

    ## Displayables ##
    #custom displayables harness the power of pygame directly.

    class MouseTracker(renpy.Displayable):
        """
        this class keeps track of where the mouse is and what it does and relates
        drags and clicks to the viewport and the BM. This way the ships can be simple
        images instead of imagebuttons, reducing lag. I guess this doesn't have to be
        a displayable but it works so meh
        """

        def __init__(self,**kwargs):
            renpy.Displayable.__init__(self,**kwargs)
            self.width = 0
            self.height = 0
            self.mouse_has_moved = True
            self.rel = (0,0)

        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            return render

        def event(self, ev, x, y, st):
            if not BM.shooting == False: return
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.mouse_has_moved = False
                self.rel = pygame.mouse.get_rel()

            if ev.type == pygame.MOUSEMOTION:
                self.mouse_has_moved = True
                renpy.hide_screen('game_over_gimmick')   #why this no werk?

                # if the left mouse button is pressed, it's a drag
                if ev.buttons[0] == 1:
                    if BM.draggable:
                        BM.xadj.change(BM.xadj.value - ev.rel[0] * 2)
                        BM.yadj.change(BM.yadj.value - ev.rel[1] * 2)
                        # if abs(ev.rel[0]) + abs(ev.rel[1]) > 5:

                mouse_location = get_mouse_location()

                #vanguard targeting
                if BM.vanguardtarget:
                    if BM.mouse_location != mouse_location and ev.buttons[0] != 1:
                        BM.mouse_location = mouse_location
                        self.mouse_has_moved = True
                        renpy.restart_interaction()

                #check for hovering over movement tiles
                if BM.selected != None:
                    if BM.mouse_location != mouse_location and ev.buttons[0] != 1:
                        if get_distance(BM.selected.location,mouse_location) <=4:
                            BM.mouse_location = mouse_location
                            self.mouse_has_moved = True
                            renpy.restart_interaction()

                #check for hovering over ships
                if BM.hovered != None:
                    if BM.hovered.location != mouse_location:
                        BM.hovered = None
                        renpy.restart_interaction()
                else:
                    for ship in BM.ships:
                        if ship.location == mouse_location:
                            BM.hovered = ship
                            renpy.restart_interaction()
                            break
                    for drone in BM.drones:
                        if drone.location == mouse_location:
                            BM.hovered = drone
                            renpy.restart_interaction()
                            break

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                # being very careful that the mouse -did not move- recently before an actual click is registered
                # otherwise it's a drag
                if not self.mouse_has_moved and pygame.mouse.get_rel() == (0,0):
                    # show_message('tried to click')
                    mouse_location = get_mouse_location()

                    # if you are using short range warp or are in skirmish mode this is used
                    if BM.targetwarp:
                        if get_cell_available(mouse_location) or BM.selected.drone:
                            return ['warptarget',get_mouse_location()]

                    #move handling
                    elif BM.selected != None and BM.weaponhover == None:
                        if BM.selected.faction == 'Player':
                            if get_cell_available(mouse_location):
                                distance = get_distance(BM.selected.location,mouse_location)
                                if distance <= 4:  #perhaps not really needed anymore?
                                    if BM.selected.move_cost == 0:
                                        move_range = 1
                                    else:
                                        move_range = int(float(BM.selected.en) / BM.selected.move_cost)
                                    if distance <= move_range:
                                        return [ 'move' , mouse_location ]

                    #sometimes it's possible to have nothing selected and still something left in BM.weaponhover
                    if BM.selected == None:
                        BM.weaponhover == None

                    #selection handling
                    if (BM.weaponhover == None or BM.active_weapon is not None) and not BM.targetwarp:
                        x,y = mouse_location
                        #out of bounds checking.
                        if x < 1 or y < 1:
                            return
                        for ship in BM.ships:
                            if BM.targetingmode and BM.active_weapon is not None:
                                #check if the active weapon is only usuable on certain types of enemies
                                if BM.active_weapon.wtype == 'Support':
                                    if hasattr(BM.active_weapon,'target_type_restriction'):
                                        if BM.active_weapon.target_type_restriction != []:
                                            if ship.stype not in BM.active_weapon.target_type_restriction:
                                                continue
                                #you can't select your own units with an active weapon, unless the active wapon is of the support of special type.
                                if ship.faction == "Player" and BM.active_weapon.wtype != 'Support' and BM.active_weapon.wtype != "Special":
                                    continue
                            #send the ship back to the battlemanager for selection processing.
                            if ship.location == mouse_location:
                                return ['selection',ship]
                        #vanguard can target a location rather than a specific ship. requires a bit of object spoofing due to legacy code.
                        if BM.vanguardtarget:
                            spoof_ship = store.object()
                            spoof_ship.location = mouse_location
                            spoof_ship.faction = 'Not the Player'
                            return ['selection', spoof_ship]

    class MouseFollow(renpy.Displayable):
        """
        this class creates an object that will display an image at the mouse cursor
        which gets redrawn every frame so it follows the cursor.
        """

        def __init__(self,child,**kwargs):
            renpy.Displayable.__init__(self,**kwargs)
            self.child = renpy.displayable(child)
            self.width = 0
            self.height = 0
            self.position = renpy.get_mouse_pos()

        def render(self, width, height, st, at):
            #create the basic Render from the passed displayable (the child)
            child_render = renpy.render(self.child, width, height, st ,at)
            #get the size of the label
            self.width, self.height = child_render.get_size()
            #make a new Render object with the size of the child.
            render = renpy.Render(self.width, self.height)
            #grab the mouse location
            x,y = renpy.get_mouse_pos()
            #adjust the position so that the middle of the label lines up with the mouse cursor
            self.position = (x - self.width / 2 , y - self.height / 2)
            #blitting means actually showing it on screen
            render.blit(child_render, self.position)
            # request a redraw asap (= next frame)
            renpy.redraw(self, 0)
            #return the render object so that renpy can do things with it.
            return render

        def event(self, ev, x, y, st):
            pass
            # if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:


        def visit(self):
           return [ self.child ]

    ##blueprints##

    class Battleship(store.object):
        """this class is the basis of all unit types in the game.
        these values are the default one if none are specified."""
        def __init__(self):
            self.name = None
            self.brain = DefaultAI(self)
            self.buffs = []
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = -1
            self.shield_color = '000'
            self.max_hp = 200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.repair = 0
            self.flak = 0
            self.flak_range = 1
            self.flak_effectiveness = 100
            self.flak_used = False
            self.flaksim = None
            self.fireing_flak = False
            self.just_spawned = False
            self.turns_alive = 1
            self.melee_location = None
            self.morale = 100
            self.enemies = {}
            self.hate = 100 #this is actually how much the enemy hates you. aka threat
            self.attraction = 0 #defunct
            self.fear = {
                'kinetics':20,
                'missiles':20,
                'energy':20,
                }
            self.kinetic_dmg = 1  #normal damage at start. increased by upgrades
            self.kinetic_acc = 1
            self.kinetic_cost = 1
            self.energy_dmg = 1
            self.energy_acc = 1
            self.energy_cost = 1
            self.missile_dmg = 1
            self.missile_eccm = 0
            self.missile_cost = 1
            self.melee_dmg = 1
            self.melee_acc = 1
            self.melee_cost = 1
            self.move_cost_multiplier = 1.0
            #[display name, level,increase/upgrade,upgrade cost,cost multiplier]
            self.upgrades = {
                'max_hp':['Hull Plating',1,100,100,1.5],
                'max_en':['Energy Reactor',1,5,200,1.4],
                'move_cost_multiplier':['Move Cost',1,-0.05,100,2.5],
                'evasion':['Evasion',1,5,350,1.8],
                'kinetic_dmg':['Kinetic Damage',1,0.05,105,1.55],
                'kinetic_acc':['Kinetic Accuracy',1,0.05,100,1.5],
                'kinetic_cost':['Kinetic EN Cost',1,-0.05,100,2.0],
                'energy_dmg':['Energy Damage',1,0.1,100,1.3],
                'energy_acc':['Energy Accuracy',1,0.05,150,1.75],
                'energy_cost':['Energy EN Cost',1,-0.05,100,2.0],
                'missile_dmg':['Missile Damage',1,0.10,100,1.5],
                'missile_eccm':['Missile Flak Resistance',1,1,100,1.5],
                'missile_cost':['Missile EN Cost',1,-0.1,150,2.5],
                'max_missiles':['Missile Storage',1,1,500,3],
                'melee_dmg':['Melee Damage',1,0.05,100,1.5],
                'melee_acc':['Melee Accuracy',1,0.05,100,1.5],
                'melee_cost':['Melee EN Cost',1,-0.05,100,2.0],
                'shield_generation':['Shield Power',1,5,500,2],
                'shield_range':['Shield Range',1,1,5000,2],
                'flak':['Flak',1,5,500,1.4],
                'base_armor':['Armor',1,5,500,1.4],
                'repair':['Repair Crew',1,50,500,2]
                }
            #self.upgrades = {
                #'max_hp':['Hull Plating',1,100,100,1.5],
                #'max_en':['Energy Reactor',1,5,200,1.4],
                #'move_cost_multiplier':['Move Cost',1,-0.05,100,2.5],
                #'evasion':['Evasion',1,5,350,1.8],
                #'kinetic_dmg':['Kinetic Damage',1,0.05,105,1.55],
                #'kinetic_acc':['Kinetic Accuracy',1,0.05,100,1.5],
                #'kinetic_cost':['Kinetic Energy Cost',1,-0.05,100,2.0],
                #'energy_dmg':['Energy Damage',1,0.1,100,1.3],
                #'energy_acc':['Energy Accuracy',1,0.05,150,1.75],
                #'energy_cost':['Energy Cost',1,-0.05,100,2.0],
                #'missile_dmg':['Missile Damage',1,0.10,100,1.5],
                #'missile_eccm':['Missile Flak Resistance',1,1,100,1.5],
                #'missile_cost':['Missile Energy Cost',1,-0.1,150,2.5],
                #'max_missiles':['Missile Storage',1,1,500,3],
                #'melee_dmg':['Melee Damage',1,0.05,100,1.5],
                #'melee_acc':['Melee Accuracy',1,0.05,100,1.5],
                #'melee_cost':['Melee Energy Cost',1,-0.05,100,2.0],
                #'shield_generation':['Shield Power',1,5,500,2],
                #'shield_range':['Shield Range',1,1,5000,2],
                #'flak':['Flak',1,5,500,1.4],
                #'base_armor':['Armor',1,5,500,1.4],
                #'repair':['Repair Crew',1,50,500,2]
                #}
            self.total_damage = 0
            self.total_kinetic_damage = 0
            self.total_missile_damage = 0
            self.total_energy_damage = 0
            self.base_armor = 10
            self.armor = self.base_armor
            self.armor_color = '000'
            self.weapons = []
            self.default_weapon_list = []
            self.max_weapons = 9
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.move_cost = 50
            self.cmd_reward = 100
            self.money_reward = 100
            self.cth = 0
            self.getting_buff = False
            self.getting_curse = False
            self.boss = False
            self.AI_ignores = False #when true the AI can't see it.
            self.mercenary = False  #if true you don't get it back upon death
            self.spawns = []
            self.support = False #used by AI to check whether to run support ability code
            self.location = None
            self.current_location = None
            self.next_location = None
            self.movement_tiles = []
            self.portrait = None
            self.pilot = None  
            self.temporary = False #if True it will get removed after battle
            self.melee_counter = False #if True this unit counters with melee when moving next to it.
            self.drone = False
            self.death_animation = 'no_animation'  #the default death animation: none.
            self.miss_animation = 'no_animation' #gets called when this ship avoids getting hit
            self.battlestart_location = None
            self.selection_voice = None
            self.voice_files = {}
            self.evoice_files = {} #english voice files
            self.voice_channel = "othvoice"
            self.id = 0 #used to identify enemy_ships more easily
              ##old buff system. now DEFUNCT
            self.modifiers = {
                'accuracy':[0,0],
                'move_cost':[0,0],
                'evasion':[0,0],
                'damage':[0,0],
                'armor':[0,0],
                'shield':[0,0],
                'flak':[0,0],
                'energy':[0,0],
                'stealth':[0,0],
                'shield_generation':[0,0],
                'energy regen':[0,0],
                }

        def __eq__(self,other):
            #set equality
            if isinstance(self, other.__class__):
                return (self.name == other.name) and self.name is not None and self.location == other.location
        
        #defunct
        def get_stat(self,stat):
            return getattr(self,stat)
            
        #defunct
        def set_stat(self,stat,value):
            setattr(self,stat,value)
            return
            
        def has_buff(self,name):
            for buff in self.buffs:
                if name == buff.name:
                    return True
            return False
        
        def set_buff(self,buff):
            if buff is None: 
                debuglog_add("error: {} was told to set a None buff".format(self.name))
                return False
            
            if self.has_buff(buff.name):
                if buff.cumulative:
                    for i in self.buffs:
                        if i.name == buff.name:
                            i.stack_counter += 1
                            if i.turns_left <= 1:
                                i.turns_left += 1
                            self.update_stats()
                            
                            if i.function_at_stacksize is not None:
                                stacksize,function = i.function_at_stacksize
                                if stacksize <= i.stack_counter:
                                    BM.stopAI = True
                            return True
                else:
                    for i in self.buffs:
                        if i.name == buff.name and i.turns_left < buff.duration:
                            i.turns_left = buff.duration
                            self.update_stats()
                            return True
                #didn't increase the stack and didn not refresh duration -> failure
                return False 
            else:
                self.buffs.append(buff(self))
                self.update_stats()
                return True
                
        def get_buff(self,buffname):
            for buff in self.buffs:
                if buff.name == buffname:
                    return buff
            return False
            
        def is_cursed(self):
            for buff in self.buffs:
                if buff.curse:
                    return True
            else:
                return False
                
        def remove_buff(self,buff_name):
            self.buffs[:] = [f for f in self.buffs if f.name != buff_name] #interesting alternative. may even be faster.
            self.update_stats()
            
            ## regular way of doing it?
            # for buff in ship.buffs:
                # if buff.name == buff_name:
                    # buff.remove()
                    # break
            return
            
        def __getattribute__(self,name):
            v = store.object.__getattribute__(self, name)
            if not is_number(v): return v #speedup the code
            
            # try to not crash the game
            if not hasattr(self,'buffs'):
                return v
                
            buffs = store.object.__getattribute__(self, 'buffs')
            
            for buff in buffs:
                for affected_stat in buff.affected_stats:
                    if name == affected_stat:
                        v = buff.get_modified_stat(name,v)
                        continue
        
            return v
        
        def update_armor(self):
            self.armor = int((self.base_armor * ( 100 + self.modifiers['armor'][0]) / 100.0 ) * self.hp / float(self.max_hp))
            self.armor_color = '000'
            if self.armor < self.base_armor: self.armor_color = '700'
            if self.armor > self.base_armor: self.armor_color = '070'

        def update_stats(self):
        
            #curse my lack of foresight
            for weapon in self.weapons:
                if weapon.parent is None:
                    weapon.parent = self
        
        #WILL NEED TO CHANGE TO ACCOMODATE FOR BUFF SYSTEM
            try:
                if self.modifiers['energy regen'][0] == -100:
                    self.en = 0
            except:
                self.modifiers['energy regen'] = (0,0)

            self.shields = 0
            #update shield generation
            if self in player_ships:
                for ship in player_ships:
                    if get_ship_distance(self, ship) <= ship.shield_range:
                        actual_generation = ship.shield_generation
                        try:
                            mod,duration = ship.modifiers['shield_generation']
                        except:
                            ship.modifiers['shield_generation'] = [0,0]
                            mod,duration = (0,0)
                        if mod != 0: actual_generation += mod
                        if actual_generation < 0: actual_generation = 0
                        self.shields = increment_attribute(self,'shields',actual_generation)
            elif self in enemy_ships:
                for ship in enemy_ships:
                    if ship.shield_generation > 0:
                        if get_ship_distance(self, ship) <= ship.shield_range:
                            actual_generation = ship.shield_generation
                            try:
                                mod,duration = ship.modifiers['shield_generation']
                            except:
                                ship.modifiers['shield_generation'] = [0,0]
                                mod,duration = ship.modifiers['shield_generation']
                            if mod != 0:
                                actual_generation += mod
                            if actual_generation < 0:
                                actual_generation = 0
                            self.shields = increment_attribute(self,'shields',actual_generation)
            if self.shields > 100: self.shields = 100
            self.shield_color = '000'
            if self.shields > self.shield_generation: self.shield_color = '070'
            self.update_armor()

        def receive_damage(self,damage,attacker,wtype,animate=True,no_cmd=False):
            BM.attacker = attacker
            
            energy_mitigation = 0
            armor_mitigation = 0
            
            if type(damage) is tuple:
                damage,energy_mitigation,armor_mitigation = damage
            
            if damage == None:
                return
            if damage == 'no energy':
                renpy.say('ERROR','the {} does not have the energy for this attack'.format(attacker.name))
                return
            elif damage == 'no ammo':
                renpy.say('ERROR','the {} does not have enough ammo for this attack'.format(attacker.name))
                return
            elif damage == 0:
                #most likely a buff failed to be applied
                return
            
            if damage == 'miss':
                BM.battle_log_insert(['attack'], "{0}'s attack misses".format(attacker.name))
            else:

                #this stuff was supposed to be used by the AI, but never was.
                if wtype == 'Missile' or wtype == 'Rocket':
                    attacker.total_missile_damage += damage
                    self.fear['missiles'] += damage / 10
                if wtype == 'Kinetic' or wtype == 'Assault':
                    attacker.total_kinetic_damage += damage
                    self.fear['kinetics'] += damage / 10
                if wtype == 'Laser' or wtype == 'Pulse':
                    attacker.total_energy_damage += damage
                    self.fear['energy'] += damage / 10

                #this stuff -is- used by the AI
                attacker.hate = increment_attribute(attacker,'hate',damage*0.5)  #damaging enemies increases how likely they are to target you
                self.hate = increment_attribute(self,'hate',damage)  #getting damaged lowers your threat back down
                if self.hate < 100: self.hate = 100
                BM.target = self

                #difficulty fudging
                if not wtype == 'Support':
                    damage = get_modified_damage(damage,self.faction)
                    energy_mitigation = get_modified_damage(energy_mitigation,self.faction)
                    armor_mitigation = get_modified_damage(armor_mitigation,self.faction)

                store.damage = damage #the global variant is used by the health_animation screen
                BM.battle_log_insert(['attack'], "{0} inflicts {1} damage to {2}".format(attacker.name, damage, self.name))
                
                #handle healing
                if wtype == 'Support':
                    BM.battle_log.append("{0} is healed for {1} HP".format(self.name, str(int(damage))))
                    self.hp = increment_attribute(self,'hp',int(damage))
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                else:
                    self.hp -= damage
                    self.total_damage += damage

            #show damage on map
            if animate:
                #play attacker attack successful voice
                if damage != "miss":
                    if wtype == 'Support':
                        #voice already gets triggered by the support weapon.
                        pass
                    else:
                        if attacker.pilot is not None:
                            attacker.voice('SucAtk')
                        # renpy.pause(1.5)
                        if self.pilot is not None:
                            self.voice('Dam')
                else:
                    if attacker.pilot is not None:
                        attacker.voice('FaiAtk')
                    # renpy.pause(1.5)
                    if self.pilot is not None:
                        self.voice('NoDam')
                    
                explosions = ['sound/explosion1.ogg','sound/explosion2.ogg','sound/explosion3.ogg',
                              'sound/explosion5.ogg']  
                if damage != 'miss' and wtype != 'Support' and attacker.name != 'The Boss': 
                    renpy.music.play( renpy.random.choice(explosions), channel = 'sound9')
                
                if wtype == 'Support':
                    BM.taking_damage = (self,-damage)
                else:
                    BM.taking_damage = (self,(damage,energy_mitigation,armor_mitigation))
                prepare_map_animation()
                renpy.pause(1.5)
                BM.taking_damage = False
                end_map_animation()
                
            #check for chivo
            if self.faction == 'Player':
                if self.hp > 0 and self.hp < 10:
                    chivo_process('Lucky!')
                if self.hp <= 0 and self.hp > -9:
                    chivo_process('Unlucky!')
                
            if self.hp <= 0:
                BM.battle_log_insert(['attack'], "{0} destroys {1}".format(attacker.name, self.name))
                self.destroy(attacker,no_cmd) #if no_cmd is set to True, the destruction gives no cmd points. used by vanguard for example.
                if self.name == 'PACT Support' and wtype == 'Melee': chivo_process('Meet My Little Friend')
                if self.name == 'PACT Support' and attacker.name == 'Seraphim':chivo_process('Natural Enemy') 
                if (self.stype == 'Battleship' or self.stype == 'Carrier') and wtype == 'Assault' and self.faction != 'Player': chivo_process('Sting Like a Bee')
                if self.faction != 'Player' and wtype == 'Melee': chivo_process('There Can Only Be One')
                update_stats()
            else:
                self.update_stats()

        def destroy(self,attacker=None,no_cmd=False,no_animation = False):
              #first take care of some AI data tracking stuff
              #destroying enemy ships increases hate, but lowers enemy morale too (latter isn't really used)
            self.en = 0 #this turns out to be useful especially for not having the AI do stuff with dead units.
            
            if attacker is None:
                attacker = Battleship()
            
            #target killed voice
            if not no_animation: #no anime also is taken to mean silent. most useful for the I WIN cheat.
                if attacker.pilot is not None:
                    attacker.voice('EnKill')
                if self.pilot is not None:
                    self.voice("Ret")
            
            #functions:
            if self.death_funcs != []:
                for item in self.death_funcs:
                    if item[0] == self.damage_id:
                        item[1](self)
                for item in self.death_funcs[:]:
                    if eval(item[0]):
                        item[1](self)
            #achievements
            if self.faction == 'Player':
                if self.mercenary:
                    chivo_process('People Die When They Are Killed')
                else:
                    chivo_process('Lose a life')
                    if self.name == 'Paladin' and self.has_buff('Sentinel'):chivo_process('Deathwish')
            else:
                chivo_process('Vengeance')
                chivo_process('Domination')
            
            #grid maintenance
            set_cell_available(self.location)

            if self == BM.selected:   # useful when you suicide into a counter
                BM.unselect_ship(self)

            #hate/morale management
            self.hate = 100  #reset hate so that after getting resurrected it doesn't pull everything again.
            if not self.faction == 'Player':
                attacker.hate = increment_attribute(attacker,'hate',self.max_hp*0.3)
                attacker.target = None
                
                #not used (yet)
                for eship in enemy_ships:
                    if get_ship_distance(self,eship) <= 4:
                        eship.morale = increment_attribute(eship,'morale',-20)

            #show the animation of the ship getting blown up
            renpy.music.play('sound/explosion4.ogg',channel = 'sound9')
            if not no_animation:
                if self.pilot is not None:
                    BM.ships.remove(self)
                BM.exploding = self
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                renpy.pause(0.75,hard=True)
                BM.exploding = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                
            #this list gets used after battle
            destroyed_ships.append(self)

            #list maintenance
            if self in BM.ships:
                BM.ships.remove(self)
                
            #award command points or show the money you lose in penalty.
            if not no_cmd:
            
                if self in enemy_ships:
                    difficulty_penalty = store.Difficulty - 1
                    if difficulty_penalty < 0: difficulty_penalty = 0
                    reward = int((self.money_reward*5)/(self.turns_alive+difficulty_penalty+2))
                    BM.cmd += reward
                    if BM.cmd > BM.max_cmd: BM.cmd = BM.max_cmd
                
                    #show +CMD gain
                    BM.cmd_gained = (self,reward)
                    
                elif self in player_ships and not self.mercenary:
                    BM.cmd_gained = (self,int(self.max_hp * 1.5))
                    
                if BM.cmd_gained is not None:
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    renpy.hide_screen('commands')
                    renpy.pause(0.75)
                    BM.cmd_gained = None
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    renpy.show_screen('commands')
                
            if self in enemy_ships:
                enemy_ships.remove(self)                
                
            elif self in player_ships:
                player_ships.remove(self)
                self.location = None
                BM.unselect_ship(self)
                BM.selected = None
                BM.selectedmode = False

            #did you lose a mercenary?   (not really used anymore)
            if self.mercenary and BM.mission != 'skirmish':
                BM.mercenary_count -= 1
            if self.temporary: BM.temp_battleship_active = False 
            
            #drone management
            if self.name == "Liberty" and self.shield_generation == 0:
                if len(BM.drones) > 0:
                    self.shield_generation = BM.drones[0].shield_generation
                    BM.drones[0].location = None

            #killing a boss ends the battle (the rest surrenders)
            #if this was the last enemy ship you win too, but that can be handled by the battle manager
            if self.boss:
                BM.boss_died(self)

            BM.check_for_loss()
            BM.check_for_win()
            renpy.restart_interaction()
            return

        def register_weapon(self, weapon):
            if len(self.weapons) >= self.max_weapons:
                raise IndexError('ERROR: too many weapons assigned to the {}'.format(self.name))
            else:
                weapon.parent = self
                self.weapons.append(weapon)

        def remove_weapon(self, weapon):
            if type(weapon) is str:
                for w in self.weapons:
                    if w.name == weapon:
                        self.weapons.remove(w)
                        return
            
            else:
                if weapon in self.weapons:
                    self.weapons.remove(weapon)
                    return
                
        def has_weapon(self,weapon_name):
            if weapon_name is None: return False
            for weapon in self.weapons:
                if weapon.name == weapon_name:
                    return True
            return False
            
        def modify_weapon(self,weapon_name,field,value):
            if weapon_name is None: return False
            for weapon in self.weapons:
                if weapon.name == weapon_name:
                    setattr(weapon,field,value)
                    return True
            return False

        def set_location(self,xnew,ynew):
            if self.location != None:
                a,b = self.location
                if a > 0 and b > 0:
                    BM.grid[a-1][b-1] = False
            BM.grid[xnew-1][ynew-1] = True
            self.location = (xnew,ynew)

        def AI_estimate_damage(self,pship,en = 0, range_reduction = 0):  #part of the AI
            self.brain.AI_estimate_damage(pship,en,range_reduction)

        def AI_attack_target(self,pship,weapon,counter=False):
            self.brain.AI_attack_target(pship,weapon,counter)

        def AI_basic_loop(self):
            self.brain.AI_basic_loop()

        def AI_move_towards(self, target, melee_distance = False, max_move_distance = 0, preferred_distance = 0,rush=False):
            self.brain.AI_move_towards(target,melee_distance,max_move_distance,preferred_distance,rush)

        def AI(self):
            self.brain.parent = self #there seems to be a bug somewhere that brains lose track of their parents.
            self.brain.AI()

        def move_ship(self, new_location,bm):
            if not get_cell_available(new_location):  #failsafe
                show_message(_('Destination is occupied!'))
                show_message("Destination is occupied")
                return
            
            if self.faction == 'Player':

                if not self in player_ships: #sanity check - sometimes weird things happen when loading old saves.
                    BM.selected = None
                    return

            bm.selectedmode = False #this disables showing movement tiles
            renpy.hide_screen('commands')

            #sanity check and deduct movement cost
            total_move_cost = self.move_cost * get_distance(self.location,new_location)
            if self.en < total_move_cost:
                return
            elif self.move_cost == 0 and get_distance(self.location,new_location) > 1: #gravity gun hack
                return
            else:
                self.en = increment_attribute(self,'en',-total_move_cost)

            a = self.location[0]-1  #make the next line of code a little shorter
            b = self.location[1]-1
            bm.grid[a][b] = False #tell the BM that the old cell is now free again

            self.current_location = self.location #store a temporary location
            self.next_location = new_location
            if self.move_funcs != []:
                for item in self.move_funcs[:]:
                    if item[0] == 1: item[1](self, self.location, new_location)
            bm.battle_log_insert(['detailed'], "{0} moved from {1} to {2}".format(self.name, str(self.current_location)[1:-1].replace(', ', '/'), str(self.next_location)[1:-1].replace(', ', '/')))
            self.travel_time = get_distance(self.location,new_location) * SHIP_SPEED
            self.location = None #this makes the imagebutton of this ship not be displayed on battle_screen
            bm.moving = True

            order_state = BM.order_used

            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')

            renpy.pause(self.travel_time+0.3)
            BM.moving = False

            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')

            BM.order_used = order_state

            self.location = new_location
            sort_ship_list()
            a = self.location[0]-1
            b = self.location[1]-1
            bm.grid[a][b] = True
            if self.faction == 'Player':
                BM.just_moved = True

            ## BLIND SIDE ATTACKS
            if self.faction == 'Player' and not self.has_buff("Stealth") and not self.has_buff("Cloak"):
                #player unit moves next to enemy unit
                for enemy in enemy_ships:
                    #if next to enemy, not dead and the enemy isn't cursed.
                    if get_ship_distance(self,enemy) == 1 and self in player_ships: # and enemy.flak > 0:
                        counter = None
                        for weapon in enemy.weapons:
                            if weapon.wtype == 'Assault' or weapon.force_counter:
                                counter = weapon
                        if counter != None:
                            if counter.force_counter or enemy.flak > 0:
                                enemy.en = enemy.max_en
                                show_message(_('COUNTER ATTACK!'))
                                BM.battle_log_insert(['attack'], "{0} counter-attacks {1}".format(enemy.name, self.name))
                                enemy.AI_attack_target(self,counter,True)
                                BM.just_moved = False
            else:
                #enemy moves next to player unit
                if self.name != 'Phoenix': #enemy phoenix is immune to counter attacks without having to buff itself.
                    for ship in player_ships:
                        if get_ship_distance(self,ship) == 1 and self in enemy_ships: # and ship.flak > 0: #if next to enemy and -not dead-
                            counter = None
                            for weapon in ship.weapons:
                                if weapon.wtype == 'Assault' or weapon.force_counter:
                                    counter = weapon
                            if counter != None:
                                if counter.force_counter or ship.flak > 0:
                                    EN = ship.en
                                    ship.en = 200
                                    show_message(_('COUNTER ATTACK!'))
                                    BM.battle_log_insert(['attack'], "{0} counter-attacks {1}".format(ship.name, self.name))
                                    self.update_stats()
                                    ##defunct
                                    ##show assault animation for counter attack
                                    #try:
                                        #renpy.call_in_new_context('atkanim_{}_{}'.format(ship.animation_name,counter.wtype.lower()))
                                    #except:
                                        #show_message('missing animation. "atkanim_{}_{}" does\'t seem to exist'.format(ship.animation_name,counter.wtype.lower()))
                                        
                                    damage = counter.fire(ship,self,True)
                                    self.receive_damage(damage,ship,counter.wtype)
                                    ship.en = EN
            if self.move_funcs != []:
                for item in self.move_funcs[:]:
                    if item[0] == 2: item[1](self)
            if self.hp > 0:bm.select_ship(self, play_voice = False) #you can control your ship again
            
        def voice(self,event): 
            """ Play a voice file depending on the passed event"""
            
            #failsaves
            if event is None: return False
            if not type(event) is str: return False
            
            #set language
            if BM.english_battle_voices:
                if event not in self.evoice_files: get_english_voices(self)
                if event not in self.evoice_files: return False
                event_voices = self.evoice_files[event]
            else:
                if event not in self.voice_files: get_voices(self)
                if event not in self.voice_files: return False
                event_voices = self.voice_files[event]
                
            if event_voices == []: return False
            
            if event != "Dam":
                #play a random voice that is tied to this event
                voice_to_play = renpy.random.choice(event_voices)
                if renpy.loadable(voice_to_play): 
                    renpy.music.queue(voice_to_play,channel = self.voice_channel,clear_queue = False)            
                else:
                    get_voices()
            else:
                #damage voices depend on level of damage
                if self.hp > 0 and self.hp <= self.max_hp:
                    threshold_value = int(self.max_hp / (len(event_voices)+0))
                    voice_index = int((self.max_hp-self.hp)/threshold_value)
                    try:
                        renpy.music.play(event_voices[voice_index],channel = self.voice_channel)
                    except IndexError:
                        renpy.music.play(event_voices[-1],channel = self.voice_channel)
            return

        ### Weapon Blueprints ###
    class Weapon(store.object): #superclass of all weapon objects
        def __init__(self):
            self.damage = 0
            self.uses_missiles = False
            self.uses_rockets = False
            self.energy_use = 30 #don't refer to this directly, use the energy_cost method instead
            self.hp_cost = 0
            self.acc_degradation = 15
            self.base_accuracy = 50
            self.wtype = ''
            self.aoe_range = 0
            self.repair = False
            self.friendly_fire = False
            self.splash_reduction = 0.25
            self.name = None
            self.attack_voice = None
            self.fire_sound = None
            self.max_range = None
            self.self_buff = False
            self.animation_name = None
            self.force_counter = False #counter with this weapon even if it's not an assault
            self.shot_count = 1
            self.disabled = False #when True the weapon is hidden from view but not removed. used for story reasons.
            self.accuracy = 100
            self.eccm = 0
            self.tooltip = ''
            self.tooltip_es = ''
            #a dict that keeps track of what specific fields on this class should be after a reset.
            self.keep_after_reset = {}
            self.parent = None
            self.ignores_shielding = False
            
        def energy_cost(self,parent):
            if parent is None:
                set_weapon_parent()                
            return self.energy_use
            
        def __getattribute__(self,name):
            v = store.object.__getattribute__(self, name)
            if not is_number(v): return v #speedup the code
            
            if not hasattr(self,'parent'):
                return v
            parent = store.object.__getattribute__(self, 'parent')
            
            if parent is None:
                # I'd like to raise an exception here but that freezes the game...
                # whenever it's not set right it's certain to cause issues. better be careful
                return v
            
            buffs = store.object.__getattribute__(parent, 'buffs')
            for buff in buffs:
                for affected_stat in buff.affected_stats:
                    if name == affected_stat:
                        v= buff.get_modified_stat(name,v)
            return v

        def callback(self):
            """should be overwritten. will be called at the start of a turn."""
            return

        # def __eq__(self,other):
            # if isinstance(self, other.__class__):
                # return (self.name == other.name) and self.name is not None
            
        ## Laser ##
    class Laser(Weapon): #starter laser weapon and parent of all other lasers
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.acc_degradation = 10
            self.base_accuracy = 40
            self.wtype = 'Laser'
            self.fire_sound = 'sound/Laser 1.ogg'
            self.name = 'Basic Laser'
            self.lbl = 'Battle UI/button_laser.png'
            self.ignores_shielding = False  #can be an integer which reduces effective shielding subractively.

        def energy_cost(self, parent):
            if parent is None and self.parent is None: set_weapon_parent()
            if self.parent is None: self.parent = parent
            if self.parent is None: return 0
            self.parent = parent #curse my past self for not setting this from the beginning
            return int(self.energy_use * parent.energy_cost)

        def fire(self, parent, target, counter = False): #firing lasers!
            if self.parent is None: self.parent = parent
            target.update_armor()
            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))
            accuracy = get_acc(self, parent, target)
            
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0, 0, 0)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0, 0, 0)
            
            BM.battle_log_insert(['attack', 'laser'], "{0} attacks {1} with laser weapon".format(parent.name, target.name))
                ## actual damage calculation
            total_damage = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0
            store.hit_count = 0
            
            #show shots on map
            BM.shooting = BulletSprite(parent,target,self)
            if self.parent.pilot is not None:
                self.parent.voice('Las')
            if self.wtype == 'Pulse': 
                if self.fire_sound == 'sound/Laser 1.ogg':
                    play_sound_effects('sound/pulse1.ogg',1) #temp hack. should be set in library instead
                else:
                    play_sound_effects(self.fire_sound,1)
            else:
                play_sound_effects(self.fire_sound,1)
            
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            renpy.hide_screen('commands')            
            
            remaining_wait = get_ship_distance(parent,target)*2 # - target_wait
            remaining_wait = int(remaining_wait)/10.0  #round to 1 decimal
            
            if self.wtype == 'Laser': remaining_wait = 0.75
            renpy.pause(remaining_wait)
            
            BM.shooting = False

            renpy.show_screen('commands')
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            #stop showing shots moving across map
            
            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(self.shot_count):
                if not get_shot_hit(accuracy,self.shot_count,parent.faction):
                    BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}> miss".format(str(shot)))
                else:
                    damage = self.damage * parent.energy_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if target.shields > 0:
                        if not self.ignores_shielding:
                            negation = damage * target.shields / 100.0
                        else:
                            effective_shielding = target.shields - self.ignores_shielding
                            if effective_shielding < 0: effective_shielding = 0
                            negation = damage * effective_shielding / 100.0
                        damage -= negation
                        store.total_shield_negation += int(negation)
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s shields negated {2} damage of {3}'s laser attack".format(str(shot), target.name, str(int(negation)), parent.name))

                    if damage <= target.armor:
                        damage = 1
                        store.total_armor_negation += damage
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s armour withstood {2}'s laser attack".format(str(shot), target.name, parent.name))
                    else:
                        damage -= target.armor
                        store.total_armor_negation += target.armor
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s laser attack".format(str(shot), target.name, target.armor, parent.name))
                    total_damage += int(damage)
                    store.hit_count += 1

            if total_damage > 0:
                damage_id = renpy.random.random()
                BM.battle_log_insert(['attack', 'laser'], "{0}'s shields negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
                BM.battle_log_insert(['attack', 'laser'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
                if BM.attacker.weapon_funcs != []:
                    for item in BM.attacker.weapon_funcs[:]:
                        if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
                        
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
                if BM.attacker.weapon_funcs != []:
                    for item in BM.attacker.weapon_funcs[:]:
                        if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)

                return total_damage
            else:
                return 'miss'

        ## GUNZ ##
    class Kinetic(Weapon): #starter Kinetic weapon
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 150
            self.shot_count = 4
            self.energy_use = 50
            self.accuracy = 50
            self.wtype = 'Kinetic'
            # self.fire_sound = 'sound/railgun.ogg'
            self.name = 'Basic Guns'
            self.lbl = 'Battle UI/button_kinetic.png'

        def energy_cost(self, parent):
            if self.parent is None: self.parent = parent
            return int(self.energy_use * parent.kinetic_cost)

        def fire(self, parent, target, counter = False): #firing gunz!
            if self.parent is None: self.parent = parent
            target.update_armor()

            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))

            BM.battle_log_insert(['attack', 'kinetic'], "{0} attacks {1} with kinetic weapon".format(parent.name, target.name))
            accuracy = get_acc(self, parent, target)
            
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0, 0, 0)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0, 0, 0)
            
            if accuracy == 0: return 'miss'

            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0

            #show shots on map
            if self.fire_sound is None:
                if self.wtype == "Kinetic":
                    self.fire_sound = 'sound/railgun.ogg'
                else:
                    self.fire_sound = 'sound/Flak.ogg'
                    
            BM.shooting = BulletSprite(parent,target,self)
            order_state = BM.order_used
            if self.parent.pilot is not None:
                if self.wtype == 'Assault' and self.parent == paladin and not BM.english_battle_voices:
                    self.parent.voice('Assault')
                else:
                    self.parent.voice('Kin')
            else:
                if self.attack_voice is not None:
                    renpy.music.play(renpy.random.choice(self.attack_voice),channel = parent.voice_channel)
            play_sound_effects(self.fire_sound,1)
            
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            renpy.hide_screen('commands')
            
            remaining_wait = get_ship_distance(parent,target)*2 # - target_wait
            remaining_wait = int(remaining_wait)/10.0 + (self.shot_count *0.02)  #round to 1 decimal
            renpy.pause(remaining_wait)
            
            BM.shooting = False
            
            renpy.show_screen('commands')
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            #stop showing shots moving across map            
            
            
            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(self.shot_count):
                if not get_shot_hit(accuracy,self.shot_count,parent.faction):
                    BM.battle_log_insert(['attack', 'kinetic', 'detailed'], "<{0}> miss".format(str(shot)))
                else:
                    damage = self.damage * parent.kinetic_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if counter:
                        #when countering, flak buffs give an extra damage bonus.
                        damage = damage * (100+parent.modifiers['flak'][0]) /100.0
                    if damage < target.armor *2:
                        store.total_armor_negation += damage - 1
                    else:
                        store.total_armor_negation += target.armor *2
                    damage -= target.armor * 2
                    if damage <= 1:
                        damage = 1 #it's rpg tradition you still do 1 damage against a big armored enemy :)
                        BM.battle_log_insert(['attack', 'kinetic', 'detailed'], "<{0}>{1}'s armour withstood {2}'s kinetic attack".format(str(shot), target.name, parent.name))
                    else:
                        BM.battle_log_insert(['attack', 'kinetic', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s kinetic attack".format(str(shot), target.name, target.armor *2, parent.name))
                    total_damage += damage
                    store.hit_count += 1
            if total_damage == 0: return 'miss'
            damage_id = renpy.random.random()
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
                    
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
                    
            BM.battle_log_insert(['attack', 'kinetic'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
            return int(total_damage)

        ## Missiles ##
    class Missile(Weapon): #starter Missile weapon
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 60    #multiplied by shot count
            self.energy_use = 30
            self.uses_missiles = True
            self.ammo_use = 1
            self.aoe_range = 0
            self.accuracy = 60
            self.acc_degradation = 5
            self.wtype = 'Missile'
            self.name = 'Basic Missiles'
            self.fire_sound = 'sound/missilelaunch.ogg'
            self.type = 'standard'
            self.shot_count = 8
            self.eccm = 0
            self.lbl = 'Battle UI/button_missile.png'
            self.flaklist = []

        def energy_cost(self, parent):
            if self.parent is None: self.parent = parent
            return int(self.energy_use * parent.missile_cost)

        def fire(self, parent, target, counter = False):
            if self.parent is None: self.parent = parent
            target.update_armor()
            BM.missiles = []
            wName = "missile"

            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))

            if self.uses_missiles:
                if self.ammo_use > parent.missiles:
                    return 'no ammo'
                else:
                    parent.missiles -= self.ammo_use
                    BM.battle_log_insert(['attack', 'missile'], "{0} attacks {1} with missiles".format(parent.name, target.name))
                    wName = "missile"

            if self.uses_rockets:
                if self.ammo_use > parent.rockets:
                    return 'no ammo'
                else:
                    parent.rockets -= self.ammo_use
                    BM.battle_log_insert(['attack', 'missile'], "{0} attacks {1} with rocket".format(parent.name, target.name))
                    wName = "rocket"

            #setup
            accuracy = get_acc(self, parent, target)
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0,0,0)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0,0,0)
            BM.selectedmode = False
            starting_location = parent.location
            BM.selected = parent
            BM.target = target

            #simulate resulte of flak
            missile = self.simulate(parent,target)
            
            #show missile moving across map
            BM.missile_moving = True
            if self.parent.pilot is not None:
                self.parent.voice('Missile')
            play_sound_effects(self.fire_sound,1)
            order_state = BM.order_used
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            renpy.hide_screen('commands')
            

            if missile.shot_down != None:
                remaining_wait = missile.shot_down
            else:
                remaining_wait = get_ship_distance(parent,target)*(MISSILE_SPEED)*15 # - target_wait
                remaining_wait = int(remaining_wait)/10.0  #round to 1 decimal
            renpy.pause(remaining_wait+0.4)
            BM.missile_moving = False
            
            
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            renpy.show_screen('commands')
            if BM.phase == "Player":
                BM.selectedmode = True
            #stop showing missile moving across map

            BM.order_used = order_state

            for ship in BM.ships:
                ship.flak_used = False
                ship.flaksim = None

            #if all missiles are shot down skip damage application
            if missile == 'miss':
                BM.missiles = []
                return 'miss'
            else:
                pass

            #start handeling actual damage
            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            #store.total_flak_interception = 0  # this is applied before it reaches the GUI; we'll let simulate() reset it instead

            #cover mechanic. it returns true if cover is hit. see functions.rpy
            if cover_mechanic(self,target,accuracy):
                return 'miss'

            for shot in range(missile.shot_count):
                if get_shot_hit(accuracy,self.shot_count,parent.faction):
                    damage = self.damage * parent.missile_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    damage -= target.armor
                    store.total_armor_negation += target.armor
                    if damage <= 1:
                        damage = 1
                        BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> {1}'s armour withstood {2}'s {3}".format(str(shot), target.name, parent.name, wName))
                    else:
                        BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> {1}'s armour negated {2} damage of {3}'s {4}".format(str(shot), target.name, target.armor, parent.name, wName))
                    total_damage += damage
                    store.hit_count += 1
                else:
                    BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> miss".format(str(shot)))

            BM.missiles = []
            if total_damage == 0: return 'miss'
            damage_id = renpy.random.random()
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
                    
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
                    
            BM.battle_log_insert(['attack', 'missile'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, store.total_armor_negation, parent.name))
            return int(total_damage)
            
        def simulate(self,parent,target,multi_rocket = False):
            """simulate the path the missile takes on it's way to the target.
            the missile takes a tiny step every part of the main while loop and scans
            for enemy ships in range that have a flak greater than zero. when it finds one
            it runs the flak_intercept() method part of the MissileSprite class. the result is stored in
            the flaksim field on enemy units and is later used to show how many missiles
            got intercepted and when"""
            store.total_flak_interception = 0 #defunct
            missile = MissileSprite(parent,target,self)
            BM.missiles = BM.missiles + [missile]  #somehow append method doesn't work with the boss rocket. I can't fathom why.
            
            if type(target) is tuple:
                path = interpolate_hex(parent.location,target) #get a list of locations between parent and target
            else:
                path = interpolate_hex(parent.location,target.location)

            #store how much time has passed since the missile was launched. used to time the flak icon etc
            time = 0.5

            for ship in BM.ships:
                ship.flak_used = False

            enemy_list = None
            if parent in player_ships:
                enemy_list = enemy_ships 
            if parent in enemy_ships:
                enemy_list = player_ships
            if enemy_list is None:
                #seemingly parent is in neither of the two, which should not be possible.
                raise ValueError("missile fired by {} which is in neither player_ships nor enemy_ships".format(parent.name))
                return
            
            for hex in path:
                for ship in BM.ships:
                    if ship.location is not None and not ship.flak_used:
                        if ship in enemy_list:
                            if get_distance(hex,ship.location) <= ship.flak_range:
                                effective_flak = ship.flak + ship.modifiers['flak'][0]
                                if effective_flak > 100: effective_flak = 100
                                elif effective_flak < 0: effective_flak = 0

                                if effective_flak > 0:
                                    if not multi_rocket or ship.flaksim is None:
                                        ship.flaksim = None
                                        ship.flaksim = (time,missile.flak_intercept(ship))
                                    else:
                                        ship.flaksim = (time,missile.flak_intercept(ship)+ship.flaksim[1])
                                    if missile.shot_count == 0:
                                        missile.shot_down = time + MISSILE_SPEED
                                        for ship2 in BM.ships:
                                            ship2.flak_used = False
                                        return missile

                time += MISSILE_SPEED

            for ship in BM.ships:
                ship.flak_used = False
            return missile

          ##this class is the missile shown on screen when missiles are fired##
    class MissileSprite(store.object):
        def __init__(self,parent,target,weapon):
            self.location = parent.location
            self.parent = parent
            self.aoe_range = weapon.aoe_range
            if type(target) is tuple:
                self.target = object()
                self.target.location = target
            else:
                self.target = target
            a = (parent.location[0] - self.target.location[0])*192
            b = (parent.location[1] - self.target.location[1])*120
              #calculate the angle between the attacker and the target
            self.angle = math.degrees(math.atan2(a,b))
            self.damage = weapon.damage
            self.shot_count = weapon.shot_count
            self.type = weapon.wtype
            if self.type == 'Missile':
                self.lbl = im.Rotozoom('Battle UI/map missile.png',self.angle,1.0)
            else:
                zoom = 1
                if weapon.aoe_range > 0:
                    zoom = 1.5
                    self.AoE = True
                self.lbl = im.Rotozoom('Battle UI/map rocket.png',self.angle,zoom)
            self.eccm = parent.missile_eccm + weapon.eccm
            self.flak_degradation = 0.02  #this is how much flak effectiveness gets reduced by each missile
            self.next_location = None
            self.shot_down = None

        def flak_intercept(self,interceptor):
            shots_remaining = self.shot_count
            interceptor.flak_used = True
            effective_flak = (interceptor.flak-self.eccm)*interceptor.flak_effectiveness/100.0

            if effective_flak > 0:
                for shot in range(self.shot_count):
                    if renpy.random.randint(0,100) <= effective_flak:
                        shots_remaining -= 1
            shot_down = 0
            if self.shot_count > shots_remaining:
                shot_down = self.shot_count - shots_remaining
            interceptor.flak_effectiveness *= 1.0 - (self.shot_count * self.flak_degradation)
            if interceptor.flak_effectiveness < 33: interceptor.flak_effectiveness = 33
            self.shot_count = shots_remaining

            store.total_flak_interception += shot_down

            return shot_down
    
    class BulletSprite(MissileSprite):
        def __init__(self,parent,target,weapon):
            MissileSprite.__init__(self,parent,target,weapon)
            if self.type == "Pulse": 
                self.lbl = im.Rotozoom('Battle UI/pulse map.png',self.angle,2.0)
            elif self.type == "Kinetic":
                self.lbl = im.Rotozoom('Battle UI/kinetic_round map.png',self.angle,1.5)
            elif self.type == "Assault":
                self.lbl = im.Rotozoom('Battle UI/flakbullet map.png',self.angle,1.5)
            elif self.type == "Melee":
                self.lbl = im.Rotozoom('Battle UI/melee_map.png',self.angle-135,1.5)    

    class SuperRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 500
            self.energy_use = 60
            self.aoe_range = 1 # 0 would be single hex
            self.friendly_fire = False
            self.accuracy = 999 #explosion is big enough that just exploding near the target is fine
            self.eccm = 10
            self.acc_degradation = 0
            self.shot_count = 1
            self.name = "Splash Rocket"
            self.lbl = 'Battle UI/button_rocket.png'
            self.wtype = 'Rocket'
            self.uses_rockets = True
            self.uses_missiles = False
            self.splash_reduction = 0.25  #outside of the prime hex units take 75% damage
            
        def fire(self, parent, target, counter = False):
            if self.parent is None: self.parent = parent
            target.update_armor()
            BM.missiles = []
            wName = "missile"

            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))

            if self.ammo_use > parent.rockets:
                return 'no ammo'
            else:
                parent.rockets -= self.ammo_use
                BM.battle_log_insert(['attack', 'missile'], "{0} attacks {1} with super rocket".format(parent.name, target.name))
                wName = "rocket"

            #setup
            accuracy = 999
            if parent.weapon_funcs != []: #accuracy is only here for the guaranteed trigger
                for item in parent.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0,0,0)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0,0,0)
            BM.selectedmode = False
            starting_location = parent.location
            BM.selected = parent
            BM.target = target

            #simulate resulte of flak
            missile = self.simulate(parent,target)
            
            #show missile moving across map
            BM.missile_moving = True
            prepare_map_animation() #hides commands and orders screens
            if self.parent.pilot is not None:
                self.parent.voice('Missile')
            play_sound_effects(self.fire_sound,1)
            
            if missile.shot_down != None:
                renpy.pause(missile.shot_down)
                BM.missile_moving = False
                return 'miss'
            else:
                remaining_wait = get_ship_distance(parent,target)*(MISSILE_SPEED)*15 # - target_wait
                remaining_wait = int(remaining_wait)/10.0  #round to 1 decimal
            renpy.pause(remaining_wait+0.4)
            BM.missile_moving = False
            
            #show explosion
            BM.exploding = target
            renpy.music.play( 'sound/explosion4.ogg', channel = 'sound8')
            renpy.pause(1.0,hard=True)
            BM.exploding = False
            
            end_map_animation()
            if BM.phase == 'Player':
                BM.selectedmode = True
            #stop showing missile moving across map

            #reset flak and simulation
            for ship in BM.ships:
                ship.flak_used = False
                ship.flaksim = None

            #if all missiles are shot down skip damage application
            if missile == 'miss':
                BM.missiles = []
                return 'miss'
            else:
                pass

            #start handeling actual damage
            total_damage = 0
            store.hit_count = self.shot_count
            

            shiplist = get_ships_around_hex(target.location)
            ship_damage_dict = {}
            
            for ship in shiplist:
                if not self.friendly_fire:  
                    if ship.faction == parent.faction:
                        continue
                armor_mitigation = 0
                for shot in range(missile.shot_count):
                    damage = self.damage * parent.missile_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if ship != target:
                        damage -= ( damage * self.splash_reduction*get_ship_distance(ship,target) )
                        if damage < 1: damage = 1
                    damage -= ship.armor
                    armor_mitigation += ship.armor
                    if damage <= 1:
                        damage = 1
                        BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> {1}'s armour withstood {2}'s {3}".format(str(shot), target.name, parent.name, wName))
                    else:
                        BM.battle_log_insert(['attack', 'missile', 'detailed'], "<{0}> {1}'s armour negated {2} damage of {3}'s {4}".format(str(shot), target.name, target.armor, parent.name, wName))
                    total_damage += damage
                BM.battle_log_insert(['attack', 'missile'], "{0}'s armour negated {1} total damage of {2}'s attack".format(target.name, armor_mitigation, parent.name))
                damage_id = renpy.random.random()
                
                #modding stuff
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
                if BM.attacker.weapon_funcs != []:
                    for item in BM.attacker.weapon_funcs[:]:
                        if item[0] == 1: item[1](total_damage, store.hit_count, damage_id)
                        
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
                if BM.attacker.weapon_funcs != []:
                    for item in BM.attacker.weapon_funcs[:]:
                        if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
                
                ship_damage_dict[ship] = (int(total_damage),0,armor_mitigation)
                total_damage = 0 #things are funny when you forget this line

            BM.missiles = []
            return ship_damage_dict
    
    class Melee(Weapon):
        def __init__(self):
            Weapon.__init__(self)
            self.damage = 400    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 1
            self.max_range = 1
            self.accuracy = 140
            self.acc_degradation = 100
            self.fire_sound = "sound/Sword Shing 2.ogg"
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_melee.png'

        def energy_cost(self, parent):
            if self.parent is None: self.parent = parent
            return int(self.energy_use * parent.melee_cost)

        def fire(self, parent, target, counter = False):
            if self.parent is None: self.parent = parent
            target.update_armor()

            #maybe parent died in a counter attack
            if parent.hp < 0:
                return 0
            #don't really want to fix this yet :D
            # if target.stype != 'Ryder':
                # return 0

            energy_cost = int(self.energy_use * parent.melee_cost)
            if parent.en < energy_cost:  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-energy_cost)

            renpy.music.play("sound/Sword Shing 2.ogg",channel='sound7')
            
            #animation
            BM.shooting = BulletSprite(parent,target,self)
            if self.parent.pilot is not None:
                self.parent.voice('Mel')
            prepare_map_animation()
            renpy.pause(2)
            BM.shooting = False
            end_map_animation()
            
            BM.battle_log_insert(['attack', 'melee'], "{0} attacks {1} melee".format(parent.name, target.name))
            accuracy = get_acc(self, parent, target)
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0,0,0)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 0: accuracy += item[1](0,0,0)
            if accuracy == 0: return 'miss'
            total_damage = 0
            store.hit_count = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0
            for shot in range(self.shot_count):
                if not get_shot_hit(accuracy,self.shot_count,parent.faction):
                    BM.battle_log_insert(['attack', 'melee', 'detailed'], "<{0}> miss".format(str(shot)))
                else:
                    damage = self.damage * parent.melee_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if damage < target.armor:
                        store.total_armor_negation += damage -1
                    else:
                        store.total_armor_negation += target.armor
                    damage -= target.armor
                    if damage <= 1:
                        damage = 1 #it's rpg tradition you still do 1 damage against a big armored enemy :)
                        BM.battle_log_insert(['attack', 'melee', 'detailed'], "<{0}>{1}'s armour withstood {2}'s melee attack".format(str(shot), target.name, parent.name))
                    else:
                        BM.battle_log_insert(['attack', 'melee', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s melee attack".format(str(shot), target.name, target.armor * 2, parent.name))
                    total_damage += damage
                    store.hit_count += 1
                    
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 1: item[1](total_damage, store.hit_count, 0)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 1: item[1](total_damage, store.hit_count, 0)
                    
            if total_damage == 0: return 'miss'
            damage_id = renpy.random.random()
            if parent.weapon_funcs != []:
                for item in parent.weapon_funcs[:]:
                    if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)
            if BM.attacker.weapon_funcs != []:
                for item in BM.attacker.weapon_funcs[:]:
                    if item[0] == 2: total_damage += item[1](total_damage, store.hit_count, damage_id)

            BM.battle_log_insert(['attack', 'melee'], "{0}'s armour negated {1} total damage of {2}'s melee attack".format(target.name, store.total_armor_negation, parent.name))
            return int(total_damage)

    class Support(store.object):
        """the base support skill. often gets treated the same as a weapon"""
        def __init__(self):
            self.applied_buff = None
            self.repair = False
            self.self_buff = False #if true this skill automatically casts on self only
            self.damage = 0 #also used to repair
            self.uses_missiles = False
            self.uses_rockets = False
            self.max_range = None
            self.base_accuracy = 50
            self.target_type_restriction = [] #for example, adding 'Ryder' would make it only affect ryders
            self.energy_use = 60
            self.hp_cost = 0
            self.wtype = 'Support'
            self.fire_sound = None
            self.disabled = False
            self.end_of_turn_callback = None
            self.parent = None
            self.force_counter = False
            self.keep_after_reset = {} #used by save compat code.
            self.cumulative = False  #if true it does not overwrite but add to the current value.
            self.modifies = '' #what modifier key will it affect. e.g. 'accuracy'
            self.buff_strength = 0 #how many points does it increase a stat?
            self.buff_duration = 1
            self.hate_penalty = 0 #get this much hate for using the skill
            self.weapon_replace = None #after using this skill it gets replaced by another.

            #effective range is 3 cells away and always hits
            self.accuracy = 350
            self.acc_degradation = 100

            self.name = None
            self.shot_count = 1
            self.lbl = ''

        def fire(self,parent,target,counter = False,hidden=False):
            store.debug = 'support weapon begins'

            #energy  management
            if parent.en < self.energy_cost(parent):
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))
                #pretty much only relevant for awakaning skills
                if self.hp_cost:
                    parent.hp -= self.hp_cost
                    if parent.hp < 1: parent.hp = 1

            #autocast
            if self.self_buff:
                target = parent

            #if this is a healing skill
            if self.repair:
                healing = int(self.damage * renpy.random.triangular(0.8,1.2) )
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 2: healing += item[1](0,0,0)
                if BM.attacker.weapon_funcs != []:
                    for item in BM.attacker.weapon_funcs[:]:
                        if item[0] == 2: healing += item[1](0,0,0)
                #chivo
                if parent.name == 'Liberty':
                    chivo_process('Liberty or Death',healing)
                
                #animation
                if self.wtype == 'Support':
                    target.getting_buff = True
                else:
                    target.getting_curse = True
                BM.selectedmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                
                #voice
                if target.faction == 'Player': #probably superfluous as one usually does not heal the enemy
                    #play buffing voice of parent
                    if self.parent.pilot is not None:
                        self.parent.voice('Buff')
                    renpy.pause(1.5)
                    #play getting-buffed voice from target
                    if target.pilot is not None:
                        if target != self.parent:
                            target.voice('HitBuff')
                    else:
                        if target.buffed_voice is not None:
                            a = renpy.random.randint(0,len(target.buffed_voice)-1)
                            renpy.music.play('{}'.format(target.buffed_voice[a]),channel = target.voice_channel)
                            del a

                target.getting_buff = False
                target.getting_curse = False
                if BM.phase == 'Player':
                    BM.selectedmode = True
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                
                #log update
                if parent is target:
                    #heal itself
                    BM.battle_log_insert(['support', 'heal'], "{0} heals {1} HP".format(parent.name, str(int(healing))))
                else:
                    BM.battle_log_insert(['support', 'heal'], "{0} heals {1} for {2} HP".format(parent.name, target.name, str(int(healing))))

                #time to hear the lamentations of the women.
                parent.hate = increment_attribute(parent,'hate',healing / 5)
                
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 1: item[1](0, 0, 0)
                if BM.attacker.weapon_funcs != []:
                    for item in BM.attacker.weapon_funcs[:]:
                        if item[0] == 1: item[1](0, 0, 0)

                return healing

            #if it's a buff/curse
            else:

                #try to set the buff
                successful = target.set_buff(self.applied_buff) #returns False if it could not apply the buff
                
                #chivo
                if successful:
                    if target.faction != 'Player': 
                        chivo_process('All For One',target)
                    else:
                        chivo_process('One For All',target)

                #lots of bookkeeping
                if parent is target:
                    # let's hope that we cannot use self-debuff...
                    target.getting_buff = True
                    log_tags = ['support', 'buff']
                    BM.battle_log_insert(log_tags, "{0} uses {1}".format(parent.name, self.name))
                else:
                    if self.wtype == 'Support':
                        target.getting_buff = True
                        log_tags = ['support', 'buff']
                        BM.battle_log_insert(log_tags, "{0} uses {1} on {2}".format(parent.name, self.name, target.name))
                    else:
                        target.getting_curse = True
                        log_tags = ['support', 'debuff']
                        BM.battle_log_insert(log_tags, "{0} uses {1} on {2}".format(parent.name, self.name, target.name))                    
                    
                if not successful:
                    #wasted
                    message = _("The buff could not be applied to the {0}").format(target.name)
                    BM.battle_log_insert(log_tags, message)
                    target.getting_buff = False
                    target.getting_curse = False
                    show_message(message)
                    parent.en = increment_attribute(parent,'en',self.energy_cost(parent))
                    if self.hp_cost:
                        parent.hp += self.hp_cost
                    return 0                    
                    
                update_stats()
                #more logging
                if target.getting_buff:
                    BM.battle_log_insert(['support', 'buff'], "{0} is buffed with {1}".format(target.name, self.name))
                else:
                    BM.battle_log_insert(['support', 'debuff'], "{0} is cursed with {1}".format(target.name, self.name))
                
                #animate the buff or curse and play relevant voice files
                if not hidden:
                    BM.selectedmode = False
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                    if BM.phase == 'Player':
                        if target.faction == 'Player':
                        #targeting a player unit
                            #play giving-buff voice of parent
                            if self.parent.pilot is not None:
                                if self.parent is phoenix: #not a dirty hack at all. we call that a graceful workaround around here.
                                    phoenix.voice("Stealth")
                                else:
                                    self.parent.voice('Buff')
                            renpy.invoke_in_new_context(short_pause)
                            #play getting-buff voice of target
                            if target.pilot is not None and target != self.parent:
                                target.voice('HitBuff')
                        else:
                        #targeting an enemy
                            #play cursing voice of parent
                            if self.parent.pilot is not None:
                                self.parent.voice('Cur')
                            renpy.invoke_in_new_context(short_pause)
                            #play getting-curse voice of target
                            if target.pilot is not None:
                                target.voice('HitCur')
                    else:
                        #enemy turn. 
                        if target.faction == 'Player':
                            #I assume no enemies with cursing voices
                            #play 'getting cursed' voice of target
                            renpy.invoke_in_new_context(short_pause)
                            if target.pilot is not None:
                                target.voice('HitCur')
                    
                    #end of animation
                    # renpy.invoke_in_new_context( short_pause )
                    if BM.phase == 'Player':
                        BM.selectedmode = True
                    renpy.hide_screen('battle_screen')
                    renpy.show_screen('battle_screen')
                target.getting_buff = False
                target.getting_curse = False

                #caster accrues hate for casting depening on weapon setting
                parent.hate = increment_attribute(parent,'hate',self.hate_penalty)

                #switch out the skill - only used by Asaga's true awakening so far.
                if self.weapon_replace is not None:
                    parent.remove_weapon(self)
                    parent.register_weapon(self.weapon_replace)
                
                #all weapon fire methods are expected to return an int
                if parent.weapon_funcs != []:
                    for item in parent.weapon_funcs[:]:
                        if item[0] == 1: item[1](0,0,0)
                if BM.attacker is not None:
                    if BM.attacker.weapon_funcs != []:
                        for item in BM.attacker.weapon_funcs[:]:
                            if item[0] == 1: item[1](0,0,0)
                return 0

        def energy_cost(self, parent):
            return int(self.energy_use)
            
        def __getattribute__(self,name):
            v = store.object.__getattribute__(self, name)
            if not is_number(v): return v #speedup the code
            
            if not hasattr(self,'parent'):
                return v
            parent = store.object.__getattribute__(self, 'parent')
            
            if parent is None:
                # I'd like to raise an exception here but that freezes the game...
                # whenever it's not set right it's certain to cause issues. better be careful
                return v
            
            buffs = store.object.__getattribute__(parent, 'buffs')
            for buff in buffs:
                for affected_stat in buff.affected_stats:
                    if name == affected_stat:
                        v= buff.get_modified_stat(name,v)
            return v            
            
        def callback(self):
            return

        # def __eq__(self, other):
            # if isinstance(self, other.__class__):
                # return (self.name == other.name) and self.name is not None
            
            
    class Curse(Support):
        def __init__(self):
            Support.__init__(self)
            self.wtype = 'Curse'
            self.sort_on = 'pship.hate' #not used anymore. may be useful later though.

    class GravityGun(store.object):
        def __init__(self):
            self.repair = False
            self.self_buff = False #if true this skill automatically casts on self only
            self.damage = 0 #also used to repair
            self.uses_missiles = False
            self.uses_rockets = False
            self.max_range = None
            self.base_accuracy = 50
            self.energy_use = 60
            self.hp_cost = 0
            self.works_only_on = 'Ryder' #set to None for it to work on all.
            self.wtype = 'Special'
            self.parent = None
            self.disabled = False
            self.force_counter = False
            self.modifies = '' #what modifier key will it affect. e.g. 'accuracy'
            self.buff_strength = 0 #how many points does it increase a stat?
            self.buff_duration = 1
            self.keep_after_reset = {} #used by save compatibility code
            self.tooltip = """
            Allows Claude to move any Ryder a single hex.
            This movement will provoke Blindside attacks, if you move an enemy Ryder
            into the range of a friendly unit with an Assault type weapon.
            Has unlimited range."""
            self.tooltip_es = "Permite al usuario mover a cualquier unidad una sola casilla.\nEste movimiento provocará contraataques, si mueves a una unidad enemiga\ndentro de el rango de una unidad aliada con un arma de tipo Asalto.\nTiene rango ilimitado."""

            #always hits
            self.accuracy = 9999
            self.acc_degradation = 0

            self.name = 'Gravity Gun'
            self.shot_count = 1
            self.lbl = 'Battle UI/button_gravity.png'
            
        def __getattribute__(self,name):
            v = store.object.__getattribute__(self, name)
            if not is_number(v): return v #speedup the code
            
            if not hasattr(self,'parent'):
                return v
            parent = store.object.__getattribute__(self, 'parent')
            
            if parent is None:
                # I'd like to raise an exception here but that freezes the game...
                # whenever it's not set right it's certain to cause issues. better be careful
                return v
            
            buffs = store.object.__getattribute__(parent, 'buffs')
            for buff in buffs:
                for affected_stat in buff.affected_stats:
                    if name == affected_stat:
                        v= buff.get_modified_stat(name,v)
            return v                        

        def fire(self,parent,target,counter=False):

            #basic verison only works on ryders
            if self.works_only_on is not None:
                if target.stype != self.works_only_on:
                    show_message(_('you can only use this ability on ryders!'))
                    return

            #energy handeling
            if parent.en < self.energy_use:
                return
            parent.en = increment_attribute(parent,'en',-self.energy_use)

            #make movement buttons appear
            BM.selectedmode = True

            #store the target's faction and weapons and EN value
            target_faction = target.faction
            target_weapons = target.weapons
            target_move_cost = store.object.__getattribute__(target,'move_cost') #need to get the real unbuffed value or injection rods will conflict.

            #set the target up for the player to move it one space
            target.faction = 'Player'
            target.weapons = []
            target.move_cost = 0
            BM.select_ship(target, play_voice = False)
            #show movement tiles around the target for 1 hex away
            target.movement_tiles = get_movement_tiles(target,1)

            #set up the loop
            looping = True
            cancel = False
            BM.weaponhover = None

            #movement loop
            while looping:
                result = ui.interact()

                # player clicked a spot to move to
                if result[0] == 'move':
                    #if we don't reset the faction now enemies will counter attack their own allies!
                    target.faction = target_faction
                    target.move_ship(result[1],BM) #result[1] is the new location to move towards
                    BM.battle_log_insert(['support'], "{0} used Gravity Gun on {1}".format(parent.name, target.name))
                    looping = False

                # player clicked the right mouse button
                if result[0] == 'deselect':
                    cancel = True
                    looping = False

            if cancel:
                #refund the energy cost of the gravity gun as the target never moved
                parent.en = increment_attribute(parent,'en',self.energy_use)

            #hand the target over back to the enemy (if applicable) and reset their weapons and energy.
            target.faction = target_faction
            target.weapons = target_weapons
            target.move_cost = target_move_cost

            #select the parent again (usually the bianca)
            BM.select_ship(parent, play_voice = False)
            #update the movement tiles as the target could now be blocking a spot the parent could have moved to before.
            parent.movement_tiles = get_movement_tiles(parent)
            #cancelling the movement just leads to annoying problem
            BM.just_moved = False
            return

        def energy_cost(self,parent):
            return self.energy_use
            
        def callback(self):
            return
            
    class PortableShieldDrone(Battleship):
        def __init__(self):
            Battleship.__init__(self)
            BM.drones.append(self)
            self.name = "shield drone"
            self.faction = 'Player'
            self.drone = True
            self.max_hp = 50 #bit of future proofing? for now they're invulnerable
            self.evasion = 100
            # renpy.invoke_in_new_context(show_message,'debug: newly added drone')
            self.drone_lbl = Text('SHIELD DRONE',size=10)
            self.lbl = 'Battle UI/blue hex.png'
            
        def __eq__(self,other):
            if isinstance(self, other.__class__):
                return self.location == other.location and self.lbl == other.lbl
        
    
    class PortableShieldGenerator(GravityGun): #inherits from gravity gun mostly because it's a 'Special' type weapon
        def __init__(self):
            GravityGun.__init__(self)
            self.energy_use = 0
            self.self_buff = True
            self.name = "Portable Shield Generator"
            if not hasattr(self,'drone'):
                self.drone = PortableShieldDrone()
                self.drone.location = None
            self.lbl = 'Battle UI/button_shldfly.png'
            self.tooltip ="""
            Allows the Liberty to send a drone with a personal shield anywhere on the battlefield."""
            self.tooltip_es = "Permite al Liberty enviar a un dron con un escudo personal a cualquier lado del campo de batalla."
            
        def fire(self,parent,target,counter=False):
            self.parent = parent
            
            #failsafe
            if self.drone not in BM.drones:
                BM.drones.append(self.drone)
            
            #set up the hex select environment
            if BM.selected != None:
                BM.unselect_ship(BM.selected)
            BM.selected = self.drone #show the drone's label
            BM.phase = None #disables the end turn button
            BM.order_used = False #debug
            BM.targetwarp = True
            if store.object.__getattribute__(liberty,'shield_generation') > 0: #gotta go roundabout to dodge buffs
                self.drone.shield_generation = store.object.__getattribute__(liberty,'shield_generation')
                self.drone.shield_range = store.object.__getattribute__(liberty,'shield_range')
                liberty.base_shieldgen = store.object.__getattribute__(liberty,'shield_generation') 
            
            renpy.invoke_in_new_context(self.targeting_loop) #hah. zuig hier maar op met je kutinteracties
            BM.targetwarp = False
            BM.phase = 'Player'
            BM.selected = liberty
            renpy.show_screen('commands')
            update_stats()
            return
            
        def targeting_loop(self):
            looping = True
            renpy.show_screen('battle_screen')
            renpy.show_screen('mousefollow')
            while looping:
                result = ui.interact()
                renpy.show_screen('battle_screen')  
                if result[0] == "warptarget":
                    new_location = result[1]
                    renpy.hide_screen('mousefollow')
                    
                    if liberty.location == new_location:
                        self.drone.location = None
                        if hasattr(liberty,'base_shieldgen'):
                            liberty.shield_generation = liberty.base_shieldgen
                        else:
                            liberty.shield_generation = self.drone.shield_generation
                    else:
                        self.drone.location = new_location
                        liberty.shield_generation = 0
                    looping = False
                    BM.phase = 'Player'
                    BM.targetwarp = False
                    #energy handeling
                    BM.selected = liberty
                    renpy.music.play('sound/sldfly.ogg',channel='sound1')
                    update_stats()
                    return

                if result[0] == "zoom":
                    zoom_handling(result,BM)
                    return

                if result[0] == 'deselect':
                    looping = False
                    renpy.hide_screen('mousefollow')
                    BM.phase = 'Player'
                    BM.targetwarp = False
                    BM.selected = liberty
                    return
            return

    class CharacterSprite(store.object):
        """used for composite sprites in VN mode."""
        def __init__(self,name,bodies,blushes,mouths,eyes,eyebrows,extras=None,tears={},*args,**kwargs):
            self.name = name
            
            #list of all the variants per standard position
            #these are now actually dicts though...
            self._list_bodies = bodies
            self._list_blushes = blushes
            self._list_blushes['None'] = None #we do need to allow all combinations where this element does not appear
            self._list_mouths = mouths
            self._list_eyes = eyes
            self._list_eyebrows = eyebrows
            self._list_extras = extras #eyepatches anyone?
            self._list_tears = tears
            self._list_tears['None'] = None
            
            self.body = ''
            self.blush = ''
            self.mouth = ''
            self.eyes = ''
            self.eyebrows = ''
            self.tears = ''
            # self.extra = ''
            
        def init_images(self):
            """this builds the LiveComposites and registers the results in the sprites dict"""
            
            #deal with offsets which became required after cropping the elements due to performance reasons.
            if self.name == 'ava':
                offset = (223,40)
            elif self.name == 'chigara':
                offset = (281,37)
            elif self.name == 'claude':
                offset = (297,104)
            elif self.name == 'sola':
                offset = (49,23)
            elif self.name == 'asaga':
                offset = (270,454)
            elif self.name == 'icari':
                offset = (182,67)
            elif self.name == 'kryska':
                offset = (260,20)
            elif self.name == 'zalice':
                offset = (213,68)
            else:
                offset = (0,0)
            
            #cycle through all the main categories to build every combination into the sprites dict
            for body in self._list_bodies:
                # component_list = [(2400,3300),(0,0),self._list_bodies[body]]
                self.body = self._list_bodies[body]
                sprite_dimensions = Image(self.body).load().get_size()
                
                #deal with weird posture of Claude which needs a separate offset
                if 'boobs' in body:
                    offset = (80, 362)
                #asaga is also annoying
                if body == 'leanforward':
                    offset = (248, 836)
                #sola's shot pose is off a bit
                if self.name == "sola":
                    if body == 'zshot':
                        offset = (109, 23)
                    
                #easter egg! thomas is een sukkel :)
                    
                for blush in self._list_blushes:
                    if not blush == 'None':
                        self.blush = self._list_blushes[blush]
                    else:
                        self.blush = ''
                    for mouth in self._list_mouths:
                        self.mouth = self._list_mouths[mouth]
                        for eye in self._list_eyes:
                            self.eyes = self._list_eyes[eye]
                            for eyebrow in self._list_eyebrows:
                                self.eyebrows = self._list_eyebrows[eyebrow]
                                for tear in self._list_tears:
                                    if not tear == 'None':
                                        self.tears = self._list_tears[tear]
                                    else:
                                        self.tears = ''
                                
                                    component_list = [
                                        sprite_dimensions,
                                        (0,0), self.body,
                                        offset, self.mouth,
                                        offset, self.eyes,
                                        offset, self.eyebrows]
                                            
                                    if not self.blush == '':
                                        component_list.insert(3,self.blush)
                                        component_list.insert(3,offset)
                                            
                                    if not tear == 'None':
                                        component_list.append(offset)
                                        component_list.append(self.tears)
                                    
                                    if not self._list_extras is None:
                                        for extra in self._list_extras:
                                            component_list.append((0,0))
                                            component_list.append(self._list_extras[extra])
                                    
                                    d = LiveComposite(*component_list)
                                    
                                    # d = Transform(LiveComposite(*component_list))
                                    # d.zoom = 0.9
                                    # d.xanchor = 0.5
                                    # d.yanchor = 0.0
                                    # d.ypos = -80
                                    # d.xpos = 0.5
                                    
                                    #register the results
                                    sprite_name = self.name+' '+body+' '+mouth+' '+eye+' '+eyebrow
                                    if not self.blush == '':
                                        sprite_name = sprite_name+' '+blush
                                    if not self.tears == '':
                                        sprite_name = sprite_name+' '+tear
                                    
                                    store.sprites[sprite_name] = d
                                    # self.blush = ''
                                    # self.tears = ''

    class Cover(store.object):
        def __init__(self,location = (1,1)):
            self.location = location
            self.cover_chance = 50 #percentage chance of blocking an incoming attack
            self.max_hp = 500
            self.hp = self.max_hp
            self.label = 'Battle UI/asteroid cover.png'
            self.angle = renpy.random.randint(1,360)

        def receive_damage(self,damage):
            
            #show damage on map
            BM.taking_damage = (self,damage)
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            renpy.pause(1)
            BM.taking_damage = False
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            
            self.hp -= damage
            if self.hp <=0: self.destroy()

        def destroy(self):
            if self in BM.covers:
                BM.covers.remove(self)
                show_message(_('The asteroid was destroyed!'))
                renpy.pause(0.5)

         ### WEAPONFIRE PARTICLE GENERATOR ###
    class FlakShield(object): #created for us by RenpyTom! thanks man!

        def __init__(self, d, generators, speed, angle=135, interval=0.05, dispersion=0):

            # The displayable we use.
            self.d = Transform(d, rotate=angle-90)
            # Are we running?
            self.running = True
            # A list of bullets that are in the air at
            # the moment.
            self.bullets = [ ]
            # The time the next bullets should be shot at.
            self.next_shot = None
            # The interval between shots.
            self.interval = interval
            # The locations of flak generators as (x, y) tuples.
            self.generators = generators
            # The angle bullets appear at.
            self.angle = angle
            # The dispersion between bullet angles.
            self.dispersion = dispersion
            # The speed of a bullet.
            self.speed = speed
            # The sprite manager.
            self.manager = SpriteManager(self.update)

        def update(self, st):
            if self.next_shot is None:
                self.next_shot = st
            if self.next_shot < st - 10 * self.interval:
                self.next_shot = st - 10 * self.interval

            # Generate shots.
            while self.next_shot <= st:
                if self.running:
                    for startx, starty in self.generators:
                            angle = (self.angle + renpy.random.uniform(-self.dispersion, self.dispersion)) / 180.0 * math.pi
                            xdt = 1.0 * self.speed * math.sin(angle)
                            ydt = 1.0 * self.speed * -math.cos(angle)
                            sprite = self.manager.create(self.d)
                            self.bullets.append((
                                self.next_shot,
                                startx,
                                starty,
                                xdt,
                                ydt,
                                sprite))
                self.next_shot += self.interval

            new_bullets = [ ]
            for b in self.bullets:
                startt, startx, starty, xdt, ydt, sprite = b
                t = st - startt
                sprite.x = startx + xdt * t
                sprite.y = starty + ydt * t
                if sprite.x < 0 or sprite.x > self.manager.width:
                    sprite.destroy()
                    continue
                if sprite.y < 0 or sprite.y > self.manager.height:
                    sprite.destroy()
                    continue
                new_bullets.append(b)

            self.bullets = new_bullets
            return 0

        def show(self):
            ui.layer('master')
            ui.add(self.manager)
            ui.close()

        def hide(self):
            ui.layer('master')
            ui.remove(self.manager)
            ui.close()

        def start(self):
            """
            Starts shooting flak.
            """
            self.running = True

        def stop(self):
            """
            Stops shooting flak.
            """
            self.running = False

    class Planet(store.object):
        def __init__(self, name, jumpLocation, xPos, yPos, showOnMapCondition, background = None, info = None, info_es = None):
            self.name = name
            self.jumpLocation = jumpLocation
            if jumpLocation == None:
                self.jumpLocation = "Dynamic_mission"
            self.xPos = xPos
            self.yPos = yPos
            self.showOnMapCondition = showOnMapCondition
            self.background = background
            self.info = info
            self.missions = []
            self.active_check = []
            if self not in planets:
                planets.append(self)
            globals()[self.name.replace(" ", "_")] = self 
            globals()[self.name.replace("{p}", "_")] = self 

        def shouldShowOnMap(self):
        # showOnMapCondition is evaluated as a python expression.
        # the variable can contain something like "not bool" or "bool == False"
        # and it will be evaluated. This makes it perfect in the event that you
        # have multiple conditions that need to be true
            return eval(self.showOnMapCondition)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                if self.name == other.name and self.jumpLocation == other.jumpLocation and self.xPos == other.xPos and self.yPos == other.yPos and self.showOnMapCondition == other.showOnMapCondition:
                    return True
            return False

    class BonusItem(store.object):
        def __init__(self, image, text, jumpLoc, zoom):
            self.image = image
            self.text = text
            self.jumpLoc = jumpLoc
            self.zoom = zoom

    class Chapter(BonusItem, Action):
        # VERY DEFUNCT
        def __init__(self, image, text, jumpLoc, zoom, startMoney = 0, lastMission = -1):
            self.image = image
            self.text = text
            self.jumpLoc = jumpLoc
            self.zoom = zoom
            self.startMoney = startMoney
            self.lastMission = lastMission

        def __call__(self):

            add_new_vars() #this actually should cover most of what you need...
            store.BM = Battle()
            store.MasterBM = store.BM
            store.BM.money = self.startMoney
            store.BM.cmd = self.lastMission * 1000
            if store.BM.cmd > 4000: store.BM.cmd = 4000  #you gain a lot over the course of the game but you typically spend a lot too.
            store.player_ships = []
            store.enemy_ships = []
            store.sunrider = None
            store.blackjack = None
            store.liberty = None
            store.phoenix = None
            store.bianca = None
            store.seraphim = None
            store.paladin = None
            store.havoc = None
            store.paradigm = None

            store.check1 = False
            store.check2 = False
            store.check3 = False
            store.check4 = False
            store.check5 = False
            store.check6 = False
            store.check7 = False
            store.check8 = False
            store.check9 = False

            store.captain_moralist = 0
            store.captain_prince = 0
            store.affection_ava = 0
            store.affection_asaga = 0
            store.affection_chigara = 0
            store.affection_icari = 0
            store.affection_claude = 0
            store.affection_tera = 0
            store.affection_sola = 0
            store.affection_cosette = 0

            store.MetAsaga = False
            store.ChigaraNamed = False
            store.ChigaraRefugee = False
            store.mission_pirateattack = False
            store.amissionforalliance = False
            store.missionforryuvia = False
            store.OngessTruth = False

            store.battlemusic = True

            store.galaxymission1 = False
            store.galaxymission2 = False
            store.galaxymission3 = False
            store.mission1 = None
            store.mission2 = None
            store.mission3 = None
            store.mission1_name = None
            store.mission2_name = None
            store.mission3_name = None

            for count in range(self.lastMission):
                setattr(store,'mission{}_complete'.format(count+1),True)

            store.mission4_complete = False
            store.mission7_complete = False

            store.ava_location = None
            store.asa_location = None
            store.chi_location = None
            store.pro_location = None
            store.gal_location = None
            store.cal_location = None
            store.res_location = None
            store.ica_location = None
            store.sol_location = None
            store.cla_location = None
            store.cos_location = None
            store.kry_location = None

            store.ava_event = None
            store.asa_event = None
            store.chi_event = None
            store.pro_event = None
            store.gal_event = 'jumptogalaxy'
            store.cal_event = 'ftltransponder'
            store.res_event = 'allocatefunds'
            store.ica_event = None
            store.sol_event = None
            store.cla_event = None
            store.cos_event = None
            store.kry_event = None

            store.warpto_occupiedcera = self.lastMission >= 1
            store.warpto_tydaria = self.lastMission >= 1
            store.warpto_astralexpanse = self.lastMission >= 2
            store.warpto_pactstation1 = self.lastMission >= 3
            store.warpto_versta = self.lastMission >= 5
            store.warpto_nomodorn = self.lastMission >= 8
            store.warpto_ryuvia = self.lastMission >= 10
            store.warpto_farport = self.lastMission >= 12
            store.warpto_ongess = self.lastMission >= 13 #not sure

            store.ep2_cancelwarp = False

            store.supportedasagacards = False
            store.Saveddiplomats = self.lastMission >= 8
            store.protectmochi = False

            ##new constants##

            TURN_SPEED = 0.75 #in seconds
            MOVE_IN_SPEED = 0.5 #for buttons and status displays
            MOVE_OUT_SPEED = 0.5
            MESSAGE_PAUSE = 0.75
            MISSILE_SPEED = 0.3
            SHIP_SPEED = 0.3
            ZOOM_SPEED = 0.1
            GRID_SIZE = (18,16) #(X,Y) aka (width,height)
            AI_WAIT_TIME = 0  #time in between highlighting an enemy unit and executing its action
            HEXW = 192   #width of hexagon (3.0 ** .5)/2.0 * HEXH
            HEXH = 222   #height of hexagon
            HEXD = 167   #vertical distance between hexagons (3/4) * HEXH
            SLIDEY = 0   #vertical offset .5 * HEXH
            SLIDEX = 96  #horixontal offset .5 * HEXW
            ADJY = 120.0/HEXD  #needed to make sure the displayables stay in the right place
            ADJX = 1.0   #192.0/HEXW
            MOVY = 60    #used to offset the displayables
            MOVX = 0

            store.all_enemies = [
                PactBomber(),  PactMook(),
                MissileFrigate(), PactCruiser(),
                PactCarrier(), PactOutpost(),
                PactBattleship(),RyuvianCruiser(),
                Havoc(), PirateBomber(),
                PirateGrunt(), PirateDestroyer(),
                PirateBase(),
                ]
            for ship in all_enemies:
                ship.location = None

            if self.lastMission >= 3:
                store.liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
                store.liberty = create_ship(Liberty(),None,store.liberty_weapons)

            if self.lastMission >= 9:
                store.bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
                store.bianca = create_ship(Bianca(),None,store.bianca_weapons)

            if self.lastMission >= 10:
                store.seraphim_weapons = [SeraphimKinetic(),Awaken()]
                store.seraphim = create_ship(Seraphim(),(6,8),store.seraphim_weapons)

            for num in range(0, self.lastMission):
                renpy.call_in_new_context('mission' + str(num + 1) + '_inits')

            if self.lastMission >= 3:
                store.sunrider.register_weapon(SunriderPulse())
                store.cal_location = 'captainsloft'

            if self.lastMission >= 6:
                store.res_location = 'lab'

            if hasattr(store,'agamemnon'):
                if agamemnon in player_ships: player_ships.remove(agamemnon)

            if hasattr(store,'mochi'):
                if mochi in player_ships: player_ships.remove(mochi)

            if self.lastMission >= 10:
                if blackjack not in player_ships:
                    store.player_ships.append(store.blackjack)

            if self.lastMission >= 10:
                store.sunrider.repair_drones = 0

            if self.lastMission >= 11:
                BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']

            clean_grid() #cleans BM.grid, BM.ships, BM.covers and store.enemy_ships
            renpy.jump_out_of_context(self.jumpLoc)

    class StoreItem(store.object):
        """master class of all store objects
        the actual items are defined in the library"""
        def __init__(self):
            self.id = ''                         #unique name for this item
            self.visibility_condition = 'True'   #when is this item visible in store?
            self.display_name = 'master item'    #how it appears in the store
            self.cost = 0                        #cost of this item
            self.tooltip = ''                    #text explaining what this item does
            self.tooltip_es = ''                 #text explaining what this item does in spanish
            self.variable_name = "None"          #[string or None] what variable keeps track of how many of this item the player has?
            self.max_amt = 0                     #maximum allowed of this item. irrelevant if self.amount_variable == None
            self.background_image = "store/item_consumable.png"  #tells what background image to use in the store.

            # if self not in store_items:
                # store_items.append(self)

        def __call__(self):
            self.buy()
            BM.money -= self.cost
            chivo_process('Penny Pincher')
            chivo_process('Forming the Fleet')
            chivo_process('Compulsive Hoarding',self)
            renpy.restart_interaction()

        def buy(self):
            #needs to be overwritten
            pass

        def isVisible(self):
            return eval(self.visibility_condition)

    class Buff(store.object):
        """objects derived from this object get attached to units and modifies stats when looked up.
        The individual buffs are defined in the Library."""
        name = "Unnamed Buff"
        tooltip = "Empty Tooltip"
        tooltip_es = "Empty Tooltip"
        affected_stats = []
        cumulative = False #when True applying the same buff on a target has some effect
        function_at_stacksize = None #stacking a buff a certain number of times can trigger something to happen, like an instant win for example.
        duration = 5 #number of turns in effect.
        
        def __init__(self,type,curse=False,parent=None): 
            self.curse = curse # if True this is a debuff. affects the icon and if Restore removes it.
            self.type = type #offense, defense or utility. affects icon
            self.parent = parent #what ship owns this buff. may be useful
            self.turn_counter = 0
            self.stack_counter = 0
            
            # if self.type == 'offense':
                # self.icon = 'Battle UI/icon_intercept.png'
            # elif self.type == 'defense':
                # self.icon = 'Battle UI/icon_armor.png'
            # else:
                # self.icon = 'Battle UI/move_tile_small.png'
            # if self.curse:
                # self.icon = im.MatrixColor(self.icon,im.matrix.tint(1.0, 0.5, 0.5)) #debuffs have their icon tinted red            
            
            self.turns_left = self.duration
            
        def get_modified_stat(self,stat,v):
            """should be overwritten"""
            return v
            
        def remove(self,silent=False):
            self.parent.buffs.remove(self)
            if self.parent.hp > 0:
                if self.curse:
                    message = __("{0} recovered from {1}").format(self.parent.name, self.name)
                    BM.battle_log_insert(['support', 'debuff'], message)
                else:
                    message = __("{1} expired from {0}").format(self.parent.name, self.name)
                    BM.battle_log_insert(['support', 'buff'], message)
                if not silent:
                    show_message(message)
                    renpy.pause(0.5)
            
        def turn_start(self):
            if self.duration != -1: #duration of -1 means it does not expire.
                self.turns_left -= 1
                if self.turns_left <= 0:
                    self.remove()
        
        def callback(self):
            """should be overwritten. gets called at the start of every turn."""
            return
        
    
    ## CUSTOM ACTIONS ##
    class BonusPageNext(Action):
        def __init__(self):
            self.page = store.bonusPage + 1

        def __call__(self):
            if not self.get_sensitive():
                return

            store.bonusPage = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.page is not None
            
        def __eq__(self,other):
            return self.page == other.page

    class BonusPagePrevious(Action):
        def __init__(self):
            self.page = store.bonusPage - 1
            if self.page < 0:
                self.page = 0

        def __call__(self):
            if not self.get_sensitive():
                return

            store.bonusPage = self.page
            renpy.restart_interaction()

        def get_sensitive(self):
            return store.bonusPage
            
        def __eq__(self,other):
            return self.page == other.page
            
    class ResetBonusPage(Action):
        def __call__(self):
            store.bonusPage = 0
            renpy.restart_interaction()

    class CreateShipAction(Action):
        def __init__(self, ship, weapons, location = None):
            self.ship = ship
            self.weapons = weapons
            self.location = location

        def __call__(self):
            #copy() is used to break aliasing (we don't want to add the same ship x times)
            create_ship(copy(self.ship), self.location, self.weapons)
            
        def __eq__(self,other):
            if not other.__class__ == CreateShipAction:
                return False
            else:
                return self.ship == other.ship and self.location == other.location

    class HoverWeapon(Action):
        def __init__(self, weapon):
            self.weapon = weapon

        def __call__(self):
            #the weapon stored at __init__ might be from old code so the weapon must be updated or things can crash.
            BM.weaponhover = update_weapon(self.weapon)

            #wtype:'Support' targets only allies, wtype:'Special' targets everyone
            if BM.weaponhover.wtype == 'Support' or BM.weaponhover.wtype == 'Special':
                for ship in player_ships:
                    ship.cth = 100
            else:
                ignore_evasion = False
                if BM.weaponhover.wtype == 'Curse' or BM.weaponhover.wtype == 'Special':
                    ignore_evasion = True

                for ship in enemy_ships:
                    ship.cth = get_acc(BM.weaponhover, BM.selected, ship, ignore_evasion)

            renpy.restart_interaction()
            return
            
        def __eq__(self,other):
            if not other.__class__ == HoverWeapon:
                return False
            else:
                return self.weapon == other.weapon
            
    class BuffHover(Action):
        def __init__(self, buff):
            self.buff = buff

        def __call__(self):
            BM.buffhover = self.buff
            renpy.restart_interaction()
            return        

        def __eq__(self,other):
            if not other.__class__ == BuffHover:
                return False
            else:
                return self.buff == other.buff
            
            
    class FireWeapon(Action):  #gets called when player clicks a weapon button
        def __init__(self, weapon):
            self.weapon = weapon

        def __call__(self):
            BM.weaponhover = None
            BM.just_moved = False
            
            #the weapon stored at __init__ might be from old code so the weapon must be updated or things can crash.
            weapon = update_weapon(self.weapon)
            if weapon.self_buff:
                weapon.fire(BM.selected,BM.selected)
                update_stats()
                BM.selected.movement_tiles = get_movement_tiles(BM.selected)
                renpy.restart_interaction()
                if BM.stopAI: 
                    return "battle won"  #mostly for the disrupt ability
                else:
                    return

            BM.targetingmode = True   #displays targeting info over enemy_ships
            BM.active_weapon = weapon
            # BM.weaponhover = BM.active_weapon
            ignore_evasion = False

            #the hover thing is not 100% trustworthy so we calculate CTH again based on the selected weapon
            if BM.active_weapon.wtype == 'Curse':
                ignore_evasion = True
            for ship in enemy_ships:
                ship.cth = get_acc(self.weapon, BM.selected, ship, ignore_evasion)

            update_stats()
            renpy.restart_interaction()   
            renpy.hide_screen("battle_screen")
            renpy.show_screen("battle_screen")

        # def __eq__(self,other):
            # if not other.__class__ == FireWeapon:
                # return False
            # else:
                # return self.weapon == other.weapon

    class ZoomAction(Action):
        def __init__(self,direction):
            self.direction = direction

        def __call__(self):
            zoom_handling(self.direction,BM)
            if BM.selectedmode: BM.selected.movement_tiles = get_movement_tiles(BM.selected)
            renpy.restart_interaction()
            
        def __eq__(self,other):
            if not other.__class__ == ZoomAction:
                return False
            else:
                return self.direction == other.direction

    class RestartInteraction(Action):
        def __init__(self):
            Action.__init__(self)

        def __call__(self):
            renpy.restart_interaction()
            
    class AutoPlace(Action):
        def __call__(self):
            if sunrider in BM.ships:
                sunrider.set_location(5,9)
            if blackjack in BM.ships:
                blackjack.set_location(5,8)
            if paladin in BM.ships:
                paladin.set_location(6,9)
            if phoenix in BM.ships:
                phoenix.set_location(5,10)
            if bianca in BM.ships:
                bianca.set_location(4,10)
            if liberty in BM.ships:
                liberty.set_location(4,8)
            if seraphim in BM.ships:
                seraphim.set_location(4,9)
            renpy.restart_interaction()
            
    class ShowStore(Action):
        def __call__(self):
            store.store_items = []

            store.store_items.append(NewWarhead())
            store.store_items.append(RocketUpgrade())
            store.store_items.append(NewRepairDrone())
            store.store_items.append(SunriderShieldUpgrade())
            store.store_items.append(ContractAllianceCruiser())
            store.store_items.append(ContractUnionFrigate())
            store.store_items.append(ContractUnionBattleship())
            store.store_items.append(ContractCeraGunboat())
            store.store_items.append(ContractRyuvianFalcon())
            store.store_items.append(SellWishallArtifact())
            store.store_items.append(RepairUpgrade())
            store.store_items.append(GravityGunBooster())
            store.store_items.append(OngessiteThrusters())
            store.store_items.append(ShipCLeanUp())
            store.store_items.append(RepairDronesMk2())
            store.store_items.append(OngessiteInjectionRods())
            store.store_items.append(ArmorPenetratingRoundsAsaga())
            store.store_items.append(MIRVTorpedoLicence())
            store.store_items.append(PortableShieldGeneratorUpgrade())
            store.store_items.append(AllianceHoloShow())
            store.store_items.append(UpgradeStealth())
            store.store_items.append(CMDupgrade())
            store.store_items.append(VanguardSplash())
            
            #old compat hacks
            if not hasattr(store,'sunrider_rocket'):store.sunrider_rocket = sunrider.weapons[3]
            if not hasattr(store,'mission5_complete'):store.mission5_complete = False
            if not hasattr(store,'chigara_repair'):store.chigara_repair = liberty.weapons[1]

            if hasattr(store,'mod_items'):
                for moditem in store.mod_items:
                    store.store_items.append(moditem())
                    
            renpy.call('store_label')
            # renpy.hide_screen("quick_menu")
            # renpy.show_screen('store_union')
            # renpy.restart_interaction()
            return
            
        def __eq__(self,other):
            return other.__class__ is ShowStore
                
            
    class ShowUpgrades(Action):
        def __call__(self):
            renpy.call('upgrades_label')
            renpy.music.play('sound/Voice/chi_Others_01.ogg',channel = 'chivoice') #welcome
            # renpy.hide_screen("quick_menu")
            # renpy.show_screen("upgrade")
            # renpy.restart_interaction()
            return
            
        def __eq__(self,other):
            return other.__class__ is ShowUpgrades
    
python early: ##achievements / cheevos
    class Achievement(store.object):
        name = 'Placeholder'       #name to display in gallery and identify this chivo in relevant dicts
        
        def __init__(self):
            self.active = True              #when not active it gets ignored. useful with failed and completed achievements.
            self.cleared = False            #when True this achievement was unlocked by the player.
            self.icon = 'UI/ctc.png'        #string pointing to an icon shown in gallery and popup
            self.cleared_icon = self.icon   #can be used to show a different icon for cleared chivos
            self.description = ''           #usually explains how to unlock or gives a hint.
            self.hidden = False             #doesn't show up in gallery until unlocked.
            self.attribution = None         #attribute a chivo to the person who suggested it
            self.total_missions = 10
            self.tracked_value = None
            if not hasattr(self,'stat_max'):
                self.stat_max = None
                self.stat_modulo = None
                store.achievement.register(self.name)
            else:
                store.achievement.register(self.name,stat_max=self.stat_max,stat_modulo=self.stat_modulo)
            
        def end_turn(self):
            #gets run at the end of every turn in battle
            return
            
        def end_mission(self):
            #gets run at the end of every mission
            return
            
        def process(self,*args,**kwargs):
            #should be called with data that changes the chivo's internal state and also checks whether it is cleared.
            #by default it immediately unlocks the achievement. complicated chivos should have this method overwritten.
            if self.active:
                self.unlock()
            return
            
        def unlock(self):
            #show notification and talk to steam if able (todo).
            if not self.cleared: #tiny failsafe
                self.icon = self.icon.replace('locked','unlocked') #I quite like this for some reason :3
            renpy.hide_screen('achievement_toast')
            renpy.show_screen('achievement_toast',self)
            self.cleared = True
            self.hidden = False
            self.active = False
            store.achievement.grant(self.name)
            return
            
        def __eq__(self,other):
            #set equality
            if isinstance(self, other.__class__):
                return (self.name == other.name) and self.name is not None
            
        
        
