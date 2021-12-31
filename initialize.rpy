##this module does boring init work so that the script module is more
##accessible and readable

#1) initialize sound channels
#2) init images and backgrounds
#3) init classes and functions (not needed?)

## a few constants
define TURN_SPEED = 0.75 #in seconds    
define MOVE_IN_SPEED = 0.5 #for buttons and status displays
define MOVE_OUT_SPEED = 0.5
define MESSAGE_PAUSE = 0.75
define MISSILE_SPEED = 0.3
define SHIP_SPEED = 0.3
define ZOOM_SPEED = 0.1
define GRID_SIZE = (18,16) #(X,Y) aka (width,height)
define AI_WAIT_TIME = 0  #time in between highlighting an enemy unit and executing its action
define HEXW = 192   #width of hexagon (3.0 ** .5)/2.0 * HEXH
define HEXH = 222   #height of hexagon
define HEXD = 167   #vertical distance between hexagons (3/4) * HEXH
define SLIDEY = 0   #vertical offset .5 * HEXH
define SLIDEX = 96  #horixontal offset .5 * HEXW
define ADJY = 120.0/HEXD  #needed to make sure the displayables stay in the right place
define ADJX = 1.0   #192.0/HEXW
define MOVY = 60    #used to offset the displayables
define MOVX = 0

init -10 python:
    MESSAGE_PAUSE = 0.75
    planets = []

    #mods can add item classes to this and they will be loaded into the store. since items are flexible and very powerful, this is pretty cool.
    mod_items = []

    mp = MultiPersistent("Sunrider")
    IC = ImageCache()
    important_variables = [
        'captain_moralist','captain_prince','affection_ava','affection_asaga',
        'affection_chigara','affection_icari','affection_claude','affection_tera',
        'affection_sola','affection_cosette','wishall','Saveddiplomats',
        'OngessTruth','legion_destroyed' ]
    DIFFICULTY_NAMES = {
        0 : 'Visual Novel Mode',
        1 : 'Casual Mode',
        2 : 'Ensign',
        3 : 'Captain',
        4 : 'Admiral',
        5 : 'Space Whale Mode' }
        
    
        
    # CG_list = [x for x in renpy.list_files() if 'CG/' in x and '3DCG' not in x and x.count('/') == 1][20:]

init -1 python:   #create sound channels for simultanious sfx playback
    renpy.music.register_channel("sound1", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound5", "sfx", False)
    renpy.music.register_channel("sound6", "sfx", False)
    renpy.music.register_channel("sound7", "sfx", False)
    renpy.music.register_channel("sound8", "sfx", False)
    renpy.music.register_channel("sound9", "sfx", False)

    renpy.music.register_channel("avavoice", "voice", False)
    renpy.music.register_channel("asavoice", "voice", False)
    renpy.music.register_channel("chivoice", "voice", False)
    renpy.music.register_channel("cosvoice", "voice", False)
    renpy.music.register_channel("kryvoice", "voice", False)
    renpy.music.register_channel("icavoice", "voice", False)
    renpy.music.register_channel("clavoice", "voice", False)
    renpy.music.register_channel("solvoice", "voice", False)
    renpy.music.register_channel("kayvoice", "voice", False)
    renpy.music.register_channel("othvoice", "voice", False)

    #set music volume to 75%. This is seperate from the setting in preferences screen!
    renpy.music.set_volume(0.1)

    Difficulty = 3
    
    for a in range(50):
        setattr(store,'mission{}_complete'.format(a),False)
    
init -5:
    image sunrider_phase:
        'Battle UI/sunrider_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1
    image PACT_phase:
        'Battle UI/pact_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1
    image Pirate_phase:
        'Battle UI/pirate_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1
    image Alliance_phase:
        'Battle UI/alliance_phase.png'
        xalign 0.5
        yalign 0.5
        zoom 5
        easeout TURN_SPEED zoom 1



label initialize:
    python:
                
        if not hasattr(store,'BM'):
            BM = Battle() #create an instance of the battle manager which keeps track of lots of things
        MasterBM = BM #Keep the main battle manager in a variable of its own, in case some modder goes switching out the battle manager.
        player_ships = []
        enemy_ships = []
        sprite_positions = {}
        sunrider = None
        blackjack = None
        liberty = None
        phoenix = None
        bianca = Bianca()
        bianca.weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
        seraphim = None
        paladin = None
        havoc = None
        paradigm = None

        all_enemies = [
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
            
        # if config.developer:
            # renpy.show_screen("debug_screen")

    return

label beginstat:
    
    if his_ceraflag == True:
        $ captain_prince += 1
    if his_ceraflag == False:
        $ captain_moralist += 1

    if his_professionalreunion == True:
        $ affection_ava -= 1
    if his_professionalreunion == False:
        $ affection_ava += 2
        
    if his_loosenrule == True:
        $ affection_asaga += 3
        $ captain_moralist += 1
    if his_loosenrule == False:
        $ affection_ava += 2
        $ captain_prince += 1
        
    if his_pactspire == True:
        $ captain_prince += 3
        $ affection_ava += 1
        $ warpto_pactstation = False
    if his_pactspire == False:
        $ warpto_pactstation = True
        
    if his_capturetraffickers == True:
        $ captain_moralist += 3
        $ affection_chigara += 1
        $ affection_asaga += 3
    if his_capturetraffickers == False:
        $ captain_moralist += 3
        $ affection_ava += 1
        $ affection_asaga += 4
        
    if his_diplomatssaved == True:
        $ Saveddiplomats = True
        $ captain_moralist += 13
        $ affection_asaga += 2
    if his_diplomatssaved == False:
        $ Saveddiplomats = False
        $ captain_prince += 13
        $ affection_icari += 4
        $ affection_asaga -= 2
        $ affection_ava += 1

    if his_mochirescue == True:
        $ captain_moralist += 2
    if his_mochirescue == False:
        $ captain_prince += 2

    if his_claudesupport == True:
        $ affection_claude += 2

    if his_chigaraforgive == True:
        $ affection_chigara += 1

    if his_solacareful == True:
        $ affection_sola += 1
        $ captain_moralist += 1
    if his_solacareful == False:
        $ captain_prince += 1

    if his_noallianceregulations == True:
        $ affection_icari += 2
    if his_noallianceregulations == False:
        $ affection_kryska += 2

    if his_cafeteriaasaga == True:
        $ affection_asaga += 1
    if his_cafeteriaasaga == False:
        $ affection_chigara += 1

    if his_notinterestedinfame == True:
        $ captain_moralist += 1
    if his_notinterestedinfame == False:
        $ captain_prince += 1

    if his_beforefarportsuspectalliance == False:
        $ captain_moralist += 1
        $ affection_kryska += 3
        
    if his_techdangerous == True:
        $ captain_moralist += 1
    if his_techdangerous == False:
        $ affection_chigara += 1
        
    if his_beach1 == 1:
        $ affection_asaga += 1
    if his_beach1 == 2:
        $ affection_chigara += 1
    if his_beach1 == 3:
        $ affection_ava += 1
    if his_beach1 == 4:
        $ affection_icari += 1
        $ affection_kryska += 1
    if his_beach1 == 5:
        $ affection_claude += 1
    if his_beach1 == 6:
        $ affection_sola += 1
        
    if his_beach2 == 1:
        $ affection_asaga += 1
    if his_beach2 == 2:
        $ affection_chigara += 1
    if his_beach2 == 3:
        $ affection_ava += 1
    if his_beach2 == 4:
        $ affection_icari += 1
        $ affection_kryska += 1
    if his_beach2 == 5:
        $ affection_claude += 1
    if his_beach2 == 6:
        $ affection_sola += 1
        
    if his_beach3 == 1:
        $ affection_asaga += 1
    if his_beach3 == 2:
        $ affection_chigara += 1
    if his_beach3 == 3:
        $ affection_ava += 1
    if his_beach3 == 4:
        $ affection_icari += 1
        $ affection_kryska += 1
    if his_beach3 == 5:
        $ affection_claude += 1
    if his_beach3 == 6:
        $ affection_sola += 1   
        
    if his_mothernaive == True:
        $ captain_prince += 1
    if his_mothernaive == False:
        $ captain_moralist += 1

    if his_solaprotect == True:
        $ affection_sola += 2
        $ captain_moralist += 1
    if his_solaprotect == False:
        $ captain_prince += 1

    if his_acquitteddeserters == True:
        $ captain_moralist += 1
    if his_acquitteddeserters == False:
        $ captain_prince += 1
        $ affection_ava += 1

    if his_soldwishall == True:
        $ wishall = False
    if his_soldwishall == False:
        $ wishall = True
        
    if his_backgrey == True:
        $ captain_prince += 1
    if his_backgrey == False:
        $ captain_moralist += 1

    if his_supportrelief == True:
        $ affection_kryska += 1

    if his_gotopress == True:
        $ captain_moralist += 4
        $ affection_asaga += 1
        $ affection_cosette += 1
        $ OngessTruth = True
        
    if his_gotopress == False:
        $ captain_prince += 4
        $ affection_ava += 1
        $ OngessTruth = False
        
    if his_backalliance == True:
        $ captain_prince += 1
        $ affection_kryska += 2
    if his_backalliance == False:
        $ captain_moralist += 1
        
    if his_suppportnuke == True:
        $ captain_prince += 1
    if his_suppportnuke == False:
        $ affection_cosette += 1
        $ captain_moralist += 2
        
    if his_legionsank == True:
        $ legion_destroyed = True
        $ captain_prince += 5
    if his_legionsank == False:
        $ captain_moralist += 5
        $ legion_destroyed = False
        
    python:
        if stat_labels != []:
            for label in stat_labels[:]:
                renpy.jump(label)
    return
    
label mission0_inits:

    python:
        
        BM.money = 3000
        BM.cmd = 4000
        BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']
        BM.orders["RESURRECTION"] = [2500,'resurrection']

        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault(),SunriderPulse()]
        sunrider = create_ship(Sunrider(),(1,1),sunrider_weapons)
        sunrider.repair_drones = 0
        process_upgrade(sunrider,"max_hp",10)
        process_upgrade(sunrider,"max_en",7)
        process_upgrade(sunrider,"evasion",1)
        process_upgrade(sunrider,"kinetic_dmg",6)
        process_upgrade(sunrider,"kinetic_acc",3)
        process_upgrade(sunrider,"kinetic_cost",4)
        process_upgrade(sunrider,"energy_dmg",6)
        process_upgrade(sunrider,"energy_acc",3)
        process_upgrade(sunrider,"energy_cost",4)
        process_upgrade(sunrider,"missile_dmg",6)
        process_upgrade(sunrider,"missile_eccm",2)
        process_upgrade(sunrider,"missile_cost",2)
        process_upgrade(sunrider,"max_missiles",3)
        process_upgrade(sunrider,"flak",3)
        process_upgrade(sunrider,"base_armor",2)

        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
        blackjack = create_ship(BlackJack(),(1,1),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
        liberty = create_ship(Liberty(),(1,1),liberty_weapons)

        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(1,1),phoenix_weapons)

        bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
        bianca = create_ship(Bianca(),(1,1),bianca_weapons)

        seraphim_weapons = [SeraphimKinetic(),Awaken()]
        seraphim = create_ship(Seraphim(),(1,1),seraphim_weapons)

        paladin_weapons = [PaladinMissile(),PaladinAssault(),PaladinKinetic(), Taunt()]
        paladin = create_ship(Paladin(),(1,1),paladin_weapons)

        process_upgrade(blackjack,"max_hp",3)
        process_upgrade(blackjack,"max_en",3)
        process_upgrade(blackjack,"evasion",1)
        process_upgrade(blackjack,"kinetic_dmg",3)
        process_upgrade(blackjack,"kinetic_acc",3)
        process_upgrade(blackjack,"kinetic_cost",2)
        process_upgrade(blackjack,"energy_dmg",3)
        process_upgrade(blackjack,"energy_acc",3)
        process_upgrade(blackjack,"energy_cost",2)
        process_upgrade(blackjack,"missile_dmg",3)
        process_upgrade(blackjack,"missile_eccm",1)
        process_upgrade(blackjack,"missile_cost",1)
        process_upgrade(blackjack,"max_missiles",2)
        process_upgrade(blackjack,"melee_dmg",3)
        process_upgrade(blackjack,"melee_acc",1)
        process_upgrade(blackjack,"melee_cost",1)
        process_upgrade(blackjack,"flak",2)
        process_upgrade(blackjack,"base_armor",2)

        process_upgrade(liberty,"max_hp",3)
        process_upgrade(liberty,"max_en",6)
        process_upgrade(liberty,"evasion",2)
        process_upgrade(liberty,"energy_dmg",1)
        process_upgrade(liberty,"energy_acc",1)
        process_upgrade(liberty,"energy_cost",1)
        process_upgrade(liberty,"shield_generation",2)
        process_upgrade(liberty,"shield_range",2)
        process_upgrade(liberty,"base_armor",1)

        process_upgrade(phoenix,"max_hp",3)
        process_upgrade(phoenix,"max_en",3)
        process_upgrade(phoenix,"evasion",3)
        process_upgrade(phoenix,"kinetic_dmg",3)
        process_upgrade(phoenix,"kinetic_acc",3)
        process_upgrade(phoenix,"kinetic_cost",2)
        process_upgrade(phoenix,"melee_dmg",3)
        process_upgrade(phoenix,"melee_acc",2)
        process_upgrade(phoenix,"melee_cost",2)
        process_upgrade(phoenix,"flak",2)
        process_upgrade(phoenix,"base_armor",1)

        process_upgrade(bianca,"max_hp",3)
        process_upgrade(bianca,"max_en",5)
        process_upgrade(bianca,"evasion",1)
        process_upgrade(bianca,"kinetic_dmg",2)
        process_upgrade(bianca,"kinetic_acc",2)
        process_upgrade(bianca,"kinetic_cost",1)
        process_upgrade(bianca,"shield_generation",2)
        process_upgrade(bianca,"shield_range",1)
        process_upgrade(bianca,"base_armor",1)

        process_upgrade(seraphim,"max_hp",3)
        process_upgrade(seraphim,"max_en",3)
        process_upgrade(seraphim,"evasion",1)
        process_upgrade(seraphim,"kinetic_dmg",7)
        process_upgrade(seraphim,"kinetic_acc",2)
        process_upgrade(seraphim,"kinetic_cost",3)
        process_upgrade(seraphim,"base_armor",1)
        
        process_upgrade(paladin,"max_hp",3)
        process_upgrade(paladin,"max_en",3)
        process_upgrade(paladin,"evasion",1)
        process_upgrade(paladin,"kinetic_dmg",4)
        process_upgrade(paladin,"kinetic_acc",2)
        process_upgrade(paladin,"kinetic_cost",3)
        process_upgrade(paladin,"missile_dmg",2)
        process_upgrade(paladin,"missile_eccm",2)
        process_upgrade(paladin,"missile_cost",2)
        process_upgrade(paladin,"max_missiles",1)
        process_upgrade(paladin,"flak",1)
        process_upgrade(paladin,"base_armor",2)

        player_ships.remove(sunrider)
        BM.ships.remove(sunrider)
        player_ships.remove(blackjack)
        BM.ships.remove(blackjack)
        player_ships.remove(liberty)
        BM.ships.remove(liberty)
        player_ships.remove(phoenix)
        BM.ships.remove(phoenix)
        player_ships.remove(bianca)
        BM.ships.remove(bianca)
        player_ships.remove(seraphim)
        BM.ships.remove(seraphim)
        player_ships.remove(paladin)
        BM.ships.remove(paladin)

        alliancebs1 = create_ship(AllianceBattleship(),(1,1))
        alliancebs2 = create_ship(AllianceBattleship(),(1,1))
        alliancecruiser1 = create_ship(AllianceCruiser(),(1,1))
        alliancecruiser2 = create_ship(AllianceCruiser(),(1,1))
        del BM.orders['VANGUARD CANNON']
        del BM.orders['SHORT RANGE WARP']

        

        

        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(PirateGrunt(),(12,4))
        create_ship(PirateGrunt(),(12,5))
        create_ship(PirateGrunt(),(11,6))
        create_ship(PirateGrunt(),(11,8))
        create_ship(PirateGrunt(),(12,9))
        create_ship(PirateGrunt(),(12,10))
        create_ship(PirateBomber(),(11,5))
        create_ship(PirateBomber(),(12,6))
        create_ship(PirateBomber(),(11,9))
        create_ship(PirateBomber(),(12,8))
        create_ship(PirateDestroyer(),(14,5))
        create_ship(PirateDestroyer(),(14,9))

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Danger.ogg"
    $ EnemyTurnMusic = "Music/VolatileReaction.ogg"

    return


label mission1_inits:

    python:
        
        BM.money = 3000
        BM.cmd = 0
        BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']
        BM.orders["RESURRECTION"] = [2500,'resurrection']

        sunrider_weapons = [SunriderLaser(),SunriderKinetic(),SunriderMissile(),SunriderRocket(),SunriderAssault(),SunriderPulse()]
        sunrider = create_ship(Sunrider(),(1,1),sunrider_weapons)
        sunrider.repair_drones = 0
        process_upgrade(sunrider,"max_hp",10)
        process_upgrade(sunrider,"max_en",7)
        process_upgrade(sunrider,"evasion",1)
        process_upgrade(sunrider,"kinetic_dmg",6)
        process_upgrade(sunrider,"kinetic_acc",3)
        process_upgrade(sunrider,"kinetic_cost",4)
        process_upgrade(sunrider,"energy_dmg",6)
        process_upgrade(sunrider,"energy_acc",3)
        process_upgrade(sunrider,"energy_cost",4)
        process_upgrade(sunrider,"missile_dmg",6)
        process_upgrade(sunrider,"missile_eccm",2)
        process_upgrade(sunrider,"missile_cost",2)
        process_upgrade(sunrider,"max_missiles",3)
        process_upgrade(sunrider,"flak",3)
        process_upgrade(sunrider,"base_armor",2)
               
        if legion_destroyed == True:
            
            player_ships.remove(sunrider)
            BM.ships.remove(sunrider)
            alliancebs1 = create_ship(AllianceBattleship(),(5,5))
            alliancecruiser1 = create_ship(AllianceCruiser(),(10,13))
            del BM.orders['VANGUARD CANNON']
            del BM.orders['SHORT RANGE WARP']

        blackjack_weapons = [BlackjackMelee(),BlackjackLaser(),BlackjackAssault(),BlackjackMissile(),BlackjackPulse()]
        blackjack = create_ship(BlackJack(),(1,2),blackjack_weapons)

        liberty_weapons = [LibertyLaser(),Repair(),AccUp(),Disable(),FlakOff(),ShutOff()]
        liberty = create_ship(Liberty(),(5,7),liberty_weapons)

        phoenix_weapons = [PhoenixAssault(),PhoenixMelee(),Stealth()]
        phoenix = create_ship(Phoenix(),(9,5),phoenix_weapons)

        bianca_weapons = [BiancaAssault(),GravityGun(),AccDown(),DamageUp(),Restore()]
        bianca = create_ship(Bianca(),(14,7),bianca_weapons)

        seraphim_weapons = [SeraphimKinetic(),Awaken()]
        seraphim = create_ship(Seraphim(),(6,8),seraphim_weapons)

        paladin_weapons = [PaladinMissile(),PaladinAssault(),PaladinKinetic(), Taunt()]
        paladin = create_ship(Paladin(),(9,8),paladin_weapons)

        process_upgrade(blackjack,"max_hp",3)
        process_upgrade(blackjack,"max_en",3)
        process_upgrade(blackjack,"evasion",1)
        process_upgrade(blackjack,"kinetic_dmg",3)
        process_upgrade(blackjack,"kinetic_acc",3)
        process_upgrade(blackjack,"kinetic_cost",2)
        process_upgrade(blackjack,"energy_dmg",3)
        process_upgrade(blackjack,"energy_acc",3)
        process_upgrade(blackjack,"energy_cost",2)
        process_upgrade(blackjack,"missile_dmg",3)
        process_upgrade(blackjack,"missile_eccm",1)
        process_upgrade(blackjack,"missile_cost",1)
        process_upgrade(blackjack,"max_missiles",2)
        process_upgrade(blackjack,"melee_dmg",3)
        process_upgrade(blackjack,"melee_acc",1)
        process_upgrade(blackjack,"melee_cost",1)
        process_upgrade(blackjack,"flak",2)
        process_upgrade(blackjack,"base_armor",2)

        process_upgrade(liberty,"max_hp",3)
        process_upgrade(liberty,"max_en",6)
        process_upgrade(liberty,"evasion",2)
        process_upgrade(liberty,"energy_dmg",1)
        process_upgrade(liberty,"energy_acc",1)
        process_upgrade(liberty,"energy_cost",1)
        process_upgrade(liberty,"shield_generation",2)
        process_upgrade(liberty,"shield_range",2)
        process_upgrade(liberty,"base_armor",1)

        process_upgrade(phoenix,"max_hp",3)
        process_upgrade(phoenix,"max_en",3)
        process_upgrade(phoenix,"evasion",3)
        process_upgrade(phoenix,"kinetic_dmg",3)
        process_upgrade(phoenix,"kinetic_acc",3)
        process_upgrade(phoenix,"kinetic_cost",2)
        process_upgrade(phoenix,"melee_dmg",3)
        process_upgrade(phoenix,"melee_acc",2)
        process_upgrade(phoenix,"melee_cost",2)
        process_upgrade(phoenix,"flak",2)
        process_upgrade(phoenix,"base_armor",1)

        process_upgrade(bianca,"max_hp",3)
        process_upgrade(bianca,"max_en",5)
        process_upgrade(bianca,"evasion",1)
        process_upgrade(bianca,"kinetic_dmg",2)
        process_upgrade(bianca,"kinetic_acc",2)
        process_upgrade(bianca,"kinetic_cost",1)
        process_upgrade(bianca,"shield_generation",2)
        process_upgrade(bianca,"shield_range",1)
        process_upgrade(bianca,"base_armor",1)

        process_upgrade(seraphim,"max_hp",3)
        process_upgrade(seraphim,"max_en",3)
        process_upgrade(seraphim,"evasion",1)
        process_upgrade(seraphim,"kinetic_dmg",7)
        process_upgrade(seraphim,"kinetic_acc",2)
        process_upgrade(seraphim,"kinetic_cost",3)
        process_upgrade(seraphim,"base_armor",1)
        
        process_upgrade(paladin,"max_hp",3)
        process_upgrade(paladin,"max_en",3)
        process_upgrade(paladin,"evasion",1)
        process_upgrade(paladin,"kinetic_dmg",4)
        process_upgrade(paladin,"kinetic_acc",2)
        process_upgrade(paladin,"kinetic_cost",3)
        process_upgrade(paladin,"missile_dmg",2)
        process_upgrade(paladin,"missile_eccm",2)
        process_upgrade(paladin,"missile_cost",2)
        process_upgrade(paladin,"max_missiles",1)
        process_upgrade(paladin,"flak",1)
        process_upgrade(paladin,"base_armor",2)
        
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(Havoc(),(13,9))
        create_ship(PirateDestroyer(),(13,7))
        create_ship(PirateDestroyer(),(13,8))
        create_ship(PirateDestroyer(),(13,10))
        create_ship(PirateIronhog(),(13,6))
        create_ship(PirateGrunt(),(11,6))
        create_ship(PirateGrunt(),(11,7))
        create_ship(PirateGrunt(),(11,10))
        create_ship(PirateGrunt(),(11,11))
        create_ship(PirateBomber(),(11,12))
        create_ship(PirateBomber(),(11,5))

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Danger.ogg"
    $ EnemyTurnMusic = "Music/VolatileReaction.ogg"

    return

label mission2_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        player_ships.remove(sunrider)
        sunrider.location = None
        del BM.orders['VANGUARD CANNON']
        del BM.orders['SHORT RANGE WARP']
        del BM.orders['REPAIR DRONES']
        
        create_ship(PactMook(),(12,5))
        create_ship(PactMook(),(11,6))

        create_ship(PactMook(),(11,9))
        create_ship(PactMook(),(11,10))
        
        create_ship(Arcadius(),(10,6))
        create_ship(Arcadius(),(10,10))
        
        create_ship(PactBattleship(),(12,6))
        create_ship(PactBattleship(),(12,7))
        create_ship(PactBattleship(),(12,9))
        create_ship(PactBattleship(),(12,10))

        create_ship(PactCarrier(),(17,7))

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "music/Danger.ogg"
    $ EnemyTurnMusic = "music/Gore_and_Sand.ogg"

    return

label mission3_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(PactMook(),(9,5))
        create_ship(PactMook(),(9,6))
        create_ship(PactMook(),(9,7))
        create_ship(PactMook(),(9,9))
        create_ship(PactMook(),(9,10))
        create_ship(PactMook(),(9,11))

        create_ship(PactBattleship(),(10,6))
        create_ship(PactFastCruiser(),(10,7))
        create_ship(PactFastCruiser(),(10,9))
        create_ship(PactBattleship(),(10,10))
        
        create_ship(PactAssaultCarrier(),(12,8))
        create_ship(PactSupport(),(12,7))
        create_ship(PactSupport(),(12,9))
        
        create_ship(PactMook(),(13,13))
        create_ship(PactMook(),(13,14))
        create_ship(PactCarrier(),(15,13))
        create_ship(PactDestroyer(),(15,14))

        
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Epic_Action_Hero.ogg"
    $ EnemyTurnMusic = "Music/Gore_and_Sand.ogg"

    return

label mission4_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(PirateDestroyer(),(11,4))
        create_ship(PirateDestroyer(),(11,5))
        create_ship(PirateDestroyer(),(11,13))
        create_ship(PirateDestroyer(),(11,14))
        
        create_ship(PirateGrunt(),(12,6))
        create_ship(PirateGrunt(),(12,7))
        create_ship(PirateGrunt(),(12,11))
        create_ship(PirateGrunt(),(13,6))
        create_ship(PirateGrunt(),(13,7))

        create_ship(PirateGrunt(),(12,12))
        create_ship(PirateGrunt(),(11,8))
        create_ship(PirateGrunt(),(11,10))
        create_ship(PirateGrunt(),(13,12))
        create_ship(PirateGrunt(),(13,11))

        create_ship(PirateBase(),(12,8))
        create_ship(PirateBase(),(12,9))
        create_ship(PirateBase(),(12,10))
        
        create_ship(PirateBomber(),(13,8))
        create_ship(PirateBomber(),(13,10))
        
        create_ship(PirateIronhog(),(16,3))
        create_ship(PirateIronhog(),(16,15))
                
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Danger.ogg"
    $ EnemyTurnMusic = "Music/VolatileReaction.ogg"

    return

label mission5_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(PactMook(),(11,5))
        create_ship(PactMook(),(10,6))
        create_ship(PactMook(),(10,7))
        create_ship(PactMook(),(9,8))
        
        create_ship(PactMook(),(9,10))
        create_ship(PactMook(),(10,11))
        create_ship(PactMook(),(10,12))
        create_ship(PactMook(),(11,13))
        
        create_ship(PactFastCruiser(),(11,6))
        create_ship(PactFastCruiser(),(11,7))
        create_ship(PactFastCruiser(),(10,8))

        create_ship(PactFastCruiser(),(10,10))
        create_ship(PactFastCruiser(),(11,11))
        create_ship(PactFastCruiser(),(11,12))
        
        create_ship(PactSupport(),(12,7))
        create_ship(PactSupport(),(12,11))
        
        create_ship(PactBattleship(),(13,6))
        create_ship(PactBattleship(),(13,7))
        create_ship(PactBattleship(),(13,11))
        create_ship(PactBattleship(),(13,12))
        
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Epic_Action_Hero.ogg"
    $ EnemyTurnMusic = "Music/Gore_and_Sand.ogg"

    return
    
label mission6_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(PactMook(),(10,4))
        create_ship(PactMook(),(10,5))
        create_ship(PactMook(),(10,6))
        
        create_ship(PactMook(),(10,10))
        create_ship(PactMook(),(10,11))
        create_ship(PactMook(),(10,12))

        create_ship(PactBomber(),(11,3))
        create_ship(PactBomber(),(11,7))
        create_ship(PactBomber(),(11,9))
        create_ship(PactBomber(),(11,13))

        create_ship(PactElite(),(9,5))
        create_ship(PactElite(),(9,11))
        create_ship(Arcadius(),(11,5))
        create_ship(Arcadius(),(11,11))
                
        create_ship(PactBattleship(),(17,4))
        create_ship(PactBattleship(),(17,5))
        create_ship(PactBattleship(),(17,13))
        create_ship(PactBattleship(),(17,14))
        create_ship(PactBattleship(),(16,8))
        create_ship(PactBattleship(),(16,10))

        create_ship(PactSupport(),(18,3))
        create_ship(PactSupport(),(18,9))
        create_ship(PactSupport(),(17,15))

        create_ship(PactCruiser(),(16,3))
        create_ship(PactCruiser(),(16,4))
        create_ship(PactCruiser(),(17,5))
        create_ship(PactCruiser(),(16,13))
        create_ship(PactCruiser(),(16,14))
        create_ship(PactCruiser(),(17,15))

        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Danger.ogg"
    $ EnemyTurnMusic = "Music/Gore_and_Sand.ogg"
    
    return
    
label mission7_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(PactBomber(),(11,6))
        create_ship(PactBomber(),(11,7))
        create_ship(PactBomber(),(11,9))
        create_ship(PactBomber(),(11,10))

        create_ship(Arcadius(),(10,5))
        create_ship(Arcadius(),(10,9))
        create_ship(Arcadius(),(13,7))
        create_ship(Arcadius(),(12,8))
        create_ship(Arcadius(),(13,9))
                
        create_ship(PactBattleship(),(11,5))
        create_ship(PactBattleship(),(10,6))
        create_ship(PactBattleship(),(10,10))
        create_ship(PactBattleship(),(11,11))
        create_ship(PactBattleship(),(13,8))

        create_ship(PactDestroyer(),(13,4))
        create_ship(PactDestroyer(),(14,5))
        create_ship(PactDestroyer(),(13,16))
        
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Epic_Action_Hero.ogg"
    $ EnemyTurnMusic = "Music/Gore_and_Sand.ogg"
    
    return
    
label mission8_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        create_ship(Arcadius(),(9,6))
        create_ship(Arcadius(),(9,8))
        create_ship(Arcadius(),(9,9))
        create_ship(Arcadius(),(9,10))
        create_ship(Arcadius(),(9,12))

        create_ship(Arcadius(),(10,4))
        create_ship(Arcadius(),(10,5))
        create_ship(Arcadius(),(10,13))
        create_ship(Arcadius(),(10,14))
        
        create_ship(PactBattleship(),(13,7))
        create_ship(PactBattleship(),(13,8))
        create_ship(PactBattleship(),(13,10))
        create_ship(PactBattleship(),(13,11))
        
        create_ship(PactCruiser(),(12,6))
        create_ship(PactCruiser(),(12,7))
        create_ship(PactCruiser(),(12,8))
        create_ship(PactCruiser(),(12,10))
        create_ship(PactCruiser(),(12,11))
        create_ship(PactCruiser(),(12,12))
        
        create_ship(PactDestroyer(),(13,3))
        create_ship(PactDestroyer(),(13,4))
        create_ship(PactDestroyer(),(13,15))
        create_ship(PactDestroyer(),(13,16))
        
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = None
    $ EnemyTurnMusic = None
    
    return
    
label mission9_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []

        nightmare_ascendant = create_ship(Nightmare_Ascendant(),(14,9))

        create_ship(Arcadius(),(12,7))
        create_ship(Arcadius(),(12,6))
        create_ship(Arcadius(),(13,5))
        create_ship(Arcadius(),(13,4))

        create_ship(Arcadius(),(12,11))
        create_ship(Arcadius(),(12,12))
        create_ship(Arcadius(),(13,13))
        create_ship(Arcadius(),(13,14))
        
        create_ship(Nightmare_Flierdrone(),(12,8))
        create_ship(Nightmare_Flierdrone(),(13,7))
        create_ship(Nightmare_Flierdrone(),(13,6))
        create_ship(Nightmare_Flierdrone(),(14,5))
        
        create_ship(Nightmare_Flierdrone(),(12,10))
        create_ship(Nightmare_Flierdrone(),(13,11))
        create_ship(Nightmare_Flierdrone(),(13,12))
        create_ship(Nightmare_Flierdrone(),(14,13))
        
        create_ship(PactProtoCarrier(),(15,7))
        create_ship(PactProtoCarrier(),(15,11))
        
        create_ship(PactBattleship(),(11,5))
        create_ship(PactBattleship(),(11,4))
        create_ship(PactBattleship(),(11,13))
        create_ship(PactBattleship(),(11,14))
                
        #center the viewport on the sunrider
        BM.xadj.value = 872
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Riding_With_the_Wind.ogg"
    $ EnemyTurnMusic = "Music/Posthumus_Regnum.ogg"
    
    return
    
label mission10_inits:

    python:
        zoomlevel = 1
        enemy_ships = []
        destroyed_ships = []
        
        if 'SHORT RANGE WARP' in BM.orders:
            del BM.orders['SHORT RANGE WARP']
        if 'ALL POWER TO ENGINES' in BM.orders:
            del BM.orders['ALL POWER TO ENGINES']
        if 'SUMMON BATTLESHIP' in BM.orders:
            del BM.orders['SUMMON BATTLESHIP']
        
        sunrider.set_location(1,9)
        
        phoenix.set_location(2,8)
        paladin.set_location(2,10)
        
        if cosette_dead == False and havoc_save == True:
            havoc = create_ship(HavocPlayer(),(2,9))
            
        if discoverfalcon == True:
            falcon1 = create_ship(RyuvianFalcon(),(1,8))
            
        gunboat1 = create_ship(CeraGunboat(),(3,8))
        gunboat2 = create_ship(CeraGunboat(),(3,9))
        gunboat3 = create_ship(CeraGunboat(),(3,10))

        frigate1 = create_ship(UnionFrigate(),(1,10))
        frigate2 = create_ship(UnionFrigate(),(2,11))
        frigate3 = create_ship(UnionFrigate(),(1,11))

        create_ship(EnemyAllianceCruiser(),(8,7))
        create_ship(EnemyAllianceCruiser(),(8,11))
        
        create_ship(EnemyAllianceInfantry(),(11,8))
        create_ship(EnemyAllianceInfantry(),(11,9))
        create_ship(EnemyAllianceInfantry(),(11,10))
        
        create_ship(EnemyAllianceBattleship(),(12,8))
        create_ship(EnemyAllianceBattleship(),(12,10))
        
        #center the viewport on the sunrider
        BM.xadj.value = 100
        BM.yadj.value = 370

    $ PlayerTurnMusic = "Music/Riding_With_the_Wind.ogg"
    $ EnemyTurnMusic = "Music/Gore_and_Sand.ogg"
