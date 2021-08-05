## this file is a horrible mishmash of experimental code that often end up used in the game
## many of this stuff should be organized in other files...

init:
    image black = Solid((0, 0, 0, 255))
    
    style _console_text is _default:
        size 20
        color "#ffffff"

# label test:    
    # return
    
    python:
        def test():
            for entry in sunrider.__dict__:
                data = getattr(sunrider,entry)
                if not type(data) is dict and not type(data) is list:
                    renpy.say( 'debug' , str(entry) + ' : ' + str(data) )
    
label RnD_skirmish:

    window hide

    python:
        store.xadj = ui.adjustment()
        store.yadj = ui.adjustment()
        BM.active_upgrade = None
        buy_upgrades()
    
jump mission_skirmish

transform shake(time=0.5,repeats=20): #defunct?
    xalign 0.5 yalign 0.5
    pause time
    block:
        ease 0.01 xpos 0.51
        ease 0.02 xpos 0.49
        ease 0.01 xpos 0.5
        repeat repeats

label test_battle:
    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []
        BM.mission = 'test'

        BM.orders['SALTO DE CORTO RANGO'] = [750,'short_range_warp']

        #create the sunrider. you only have to create a player ship once:
        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault()]
        sunrider = create_ship(Sunrider(),(8,6),sunrider_weapons)

        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse(),AwakenAsaga()]
        blackjack = create_ship(BlackJack(),(10,5),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),DamageUp(),AccDown()]
        liberty = create_ship(Liberty(),(8,7),liberty_weapons)

        phoenix_weapons = [PhoenixMelee(),Stealth(),GravityGun()]
        phoenix = create_ship(Phoenix(),(10,7),phoenix_weapons)

        create_ship(Havoc(),(13,5),[Melee(),HavocAssault(),HavocMissile(),HavocRocket()])
        enemy_ships[-1].name = 'Legion' #testing out the new cannon
        havoc = enemy_ships[-1]

        # enemy_ships[-1].hp = 1
        # create_ship(PactSupport(),(14,5))
        # create_ship(PirateGrunt(),(13,7),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        # create_ship(PirateGrunt(),(13,6),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        # create_ship(PirateGrunt(),(13,8),[PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()])
        # create_ship(PactCruiser(),(14,8),[])

        # create_ship(PirateDestroyer(),(16,5),[PirateDestroyerLaser(),PirateDestroyerKinetic()])
        # create_ship(PirateDestroyer(),(16,7),[PirateDestroyerLaser(),PirateDestroyerKinetic()])

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Titan.ogg"
    $ EnemyTurnMusic = "music/Dusty_Universe.ogg"

#    $ buy_upgrades() ##testing

    $BM.start()
    return

label missiontest:

    $BM.battle()  #continue the battle

    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump missiontest #loop back
    else:
        pass #continue down

    # jump dispatch
    return

label battle_start:
    play music PlayerTurnMusic
    python:
        BM.stopAI = False
        BM.order_used = False
        BM.enemy_vanguard_path = []
        BM.player_vanguard_path = []
        BM.active_strategy = [None,0]
        BM.active_weapon = None
        BM.weaponhover = None
        BM.hovered = None
        store.zoomlevel = 0.65
        BM.show_grid = False
        sort_ship_list()
        BM.start()

label endofturn: 
    # -everything- about this is dreadful. can't be arsed to make it not suck though.
    # a shining monument to the earliest days of development.
    
    show screen battle_screen
    $update_stats()

    if not BM.phase == 'Player':
        play sound1 'sound/battle.ogg'
        show sunrider_phase onlayer screens zorder 50
        $ renpy.pause(TURN_SPEED, hard=True)
        play sound2 'sound/drum.ogg'
        hide sunrider_phase onlayer screens zorder 50 with dissolve
        $ BM.phase = 'Player'
    else:
        if len(enemy_ships) > 0:
            if enemy_ships[0].faction == 'PACT':
                play sound1 'sound/battle.ogg'
                show PACT_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide PACT_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'PACT'
            elif enemy_ships[0].faction == 'Pirate':
                play sound1 'sound/battle.ogg'
                show Pirate_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide Pirate_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'Pirate'
            elif enemy_ships[0].faction == 'Alliance':
                play sound1 'sound/battle.ogg'
                show Alliance_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide alliance_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'Alliance'                
        else:
            if destroyed_ships[-1].faction == 'PACT':
                play sound1 'sound/battle.ogg'
                show PACT_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide PACT_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'PACT'
            elif destroyed_ships[-1].faction == 'Pirate':
                play sound1 'sound/battle.ogg'
                show Pirate_phase onlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide Pirate_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'Pirate'
            elif destroyed_ships[0].faction == 'Alliance':
                play sound1 'sound/battle.ogg'
                show Alliance_phaseonlayer screens zorder 50
                $ renpy.pause(TURN_SPEED, hard=True)
                play sound2 'sound/drum.ogg'
                hide alliance_phase onlayer screens zorder 50 with dissolve
                $ BM.phase = 'Alliance'                 

    $update_modifiers() #update buffs and curses

    if BM.phase == 'Player':
        $ renpy.take_screenshot()
        $ renpy.save('beginturn')

    return

label sunrider_destroyed:
    hide screen commands
    hide screen battle_screen
    show badend

    $ BM.phase = 'Player' #this makes it so you can save and load again, as it's normally blocked during the enemy's turn

    call screen bad_end_options
    
    # "You've met with a terrible fate, haven't you?"
    pause
    jump sunrider_destroyed
    return
    
label upgrades_label:
    show screen upgrade
    hide screen quick_menu
    python:
        action,upgrade = ui.interact()
        
        if action == 'return':
            renpy.hide_screen('upgrade')
            renpy.hide_screen('store_union')
            renpy.show_screen('quick_menu')
            #sadly overlaps with regular dialogue voicing.
            # a = renpy.random.choice(['2','4'])
            # renpy.music.play('sound/Voice/chi_Others_0{}.ogg'.format(a),channel = 'chivoice') #goodbye
            
        elif action == 'store':
            renpy.hide_screen('upgrade')
            ShowStore()()
            
        elif action == 'process_upgrade':
            process_upgrade(BM.selected,upgrade)
            renpy.jump('upgrades_label')
            
        elif action == 'reverse_upgrade':
            reverse_upgrade(BM.selected,upgrade)
            renpy.jump('upgrades_label')
    
    if hasattr(store,'pre_battle'):
        if pre_battle:
            jump battlewarning_label
    return
    
label store_label:    
    show screen store_union
    hide screen quick_menu
    python:
        action,item = ui.interact()
        
        if action == 'return':
            renpy.hide_screen('store_union')
            renpy.hide_screen('upgrade')
            renpy.show_screen('quick_menu')
            
        elif action == 'upgrades':
            renpy.hide_screen('store_union')
            renpy.jump('upgrades_label')
            
        elif action == 'buy':
            item()
            renpy.jump('store_label')
    
    if hasattr(store,'pre_battle'):
        if pre_battle:
            jump battlewarning_label
    return
    
label battlewarning_label:
    show screen battlewarning
    $pre_battle = True
    if ui.interact() == 'continue':
        hide screen battlewarning
        $pre_battle = False
        $renpy.jump(pre_mission)
    jump battlewarning_label
    

label loadsavedgame:   #used when the player chooses to load a saved game after game over
    show screen load
    pause
    jump sunrider_destroyed
    return

label tryagain_experimental:
    hide badend with battlewipe
    $ clean_battle_exit(True)
    python:
        store.battle1_check1 = False
        store.battle2_check1 = False
        store.battle2_check2 = False
        store.battle_check1 = False
        
        i = 1
        while True:
            if hasattr(store, 'bcheck{}'.format(i)):
                setattr(store, 'bcheck{}'.format(i), False)
                i += 1
            else:
                break
        
        store.destroyed_ships = []
        store.player_ships = BM.battlestart.player_ships
        for ship in store.player_ships:
            ship.missiles = ship.max_missiles
            ship.location = ship.battlestart_location
            ship.buffs = []
            ship.hate = 100
        sunrider.rockets = BM.battlestart.sunrider_rockets
        sunrider.repair_drones = BM.battlestart.sunrider_repair_drones
        BM.cmd = BM.battlestart.cmd
        BM.turn_count = 1
        
        store.enemy_ships = BM.battlestart.enemy_ships
        for ship in store.enemy_ships:
            ship.location = ship.battlestart_location
            ship.hp = ship.max_hp
            ship.missiles = ship.max_missiles
            ship.rockets = ship.max_rockets
            if isinstance(ship, Havoc):
                store.havoc = ship
        
        BM.covers = BM.battlestart.covers
        for cover in BM.covers:
            cover.hp = cover.max_hp
        BM.ships = []
        for ship in store.player_ships:
            BM.ships.append(ship)
        for ship in store.enemy_ships:
            BM.ships.append(ship)
        
        BM.grid = []
        for a in range(GRID_SIZE[0]):
            BM.grid.append([False]*GRID_SIZE[1])
        for ship in BM.ships:
            if ship.location == None:
                continue
            x, y = ship.location
            BM.grid[x - 1][y - 1] = True
            
        #rebind store shortcuts to these new ships
        for ship in player_ships:
            if ship.pilot is not None:
                setattr(store,ship.__class__.__name__.lower(),ship)
                
        reset_classes(True)
        
        BM.start()
    return


label tryagain:
    python:
        try:
            renpy.load('battlestart{}'.format(BM.mission))
        except AttributeError:
            renpy.jump('tryagain_experimental')
    pause
    return

label restartturn:
    $renpy.load('beginturn')
    pause
    $show_message('this should never show up')
    pause
    return

label after_load:

    python:
        
        try:
            achievement.sync()
        except:
            pass
        
        if not hasattr(store,'dlc'):
            dlc = False
        
        if dlc == False:
            renpy.music.set_volume(0.27, delay=0, channel='music')
            renpy.music.set_volume(0.8, delay=0, channel='sound')
            renpy.music.set_volume(1.0, delay=0, channel='voice')
        
            #temp
            # persistent.achievements = {}
            # add_achievements()

            if not hasattr(store,'BM'): BM = Battle()
            if not hasattr(BM,'debug_log'): BM.debug_log = []

            #check if the classes should be reset
            reset = False
            if not hasattr(store,'BM'):
                store.BM = Battle()
                store.MasterBM = BM
            if hasattr(store.BM,'save_version'):
                if store.BM.save_version != config.version:
                    reset = True
                else:
                    pass #everything is fine, do not reset
            else:
                reset = True

            if reset:

                #initialize the image cache introduced in 7.2
                IC = ImageCache()
                
                #working around an issue I noticed but can't explain.
                if BM.selected is not None:
                    if BM.selected.faction == 'Player':
                        if not BM.selected in player_ships:
                            BM.selected = None

                #updates the BM, ships and weapons used so that new default values are added.
                reset_classes()
                get_voices()
                get_english_voices()
                for ship in player_ships: #add pilots for old mercenaries so they use their voice method instead of bleep
                    ship.pilot = ship.__class__().pilot
                
                #temporary. should get removed post release or any further patch will wipe all chivos
                # persistent.achievements = {}
                # add_achievements()
                
                if store.legion_destroyed:
                    if sunrider is not None:
                        sunrider.portrait = Image('Battle UI/ava_portrait_eyepatch.png')
                        
                for ship in player_ships:
                    if ship.pilot is None:
                        ship.voice_channel = "othvoice"
                        ship.selection_voice = ['sound/beep1.ogg']
                        ship.moveforward_voice = ['sound/beep2.ogg']
                        ship.movebackward_voice = ['sound/beep2.ogg']
                        ship.buffed_voice = ['sound/beep2.ogg']
                        ship.cursed_voice = ['sound/beep2.ogg']

                #set the new save version
                store.BM.save_version = config.version
                
            if not BM.battlemode: config.rollback_enabled = True

    return




