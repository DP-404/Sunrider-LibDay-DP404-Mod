## this module creates custom screens. I prefer not to clutter the ren'py
## default screens.rpy module as it's pretty full already

## 0) transforms
## 1) status screens
## 2) battle map
## 3) command menu

init -20:  ##0) transforms
#    $import random

    transform hoverglow(img1):  #makes units glow when you mouseover
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.0))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(0.0))
        pause 0.1
        repeat

    transform vanguard_cannon(hh):
        alpha 0
        ease 0.4 alpha 1
        pause 0.2
        ease 1.5 alpha 0

    transform warpout:
        alpha 0
        easein 1 alpha 1

    transform buffup(xx):
        ypos xx
        alpha 1

        parallel:
            linear 1 ypos int(xx-190*zoomlevel)
        parallel:
            time 0.5
            linear 0.5 alpha 0
        pause 3

    transform cursedown(xx):
        ypos xx
        alpha 1

        parallel:
            linear 1 ypos int(xx+190*zoomlevel)
        parallel:
            time 0.5
            linear 0.5 alpha 0
        pause 3

    transform zoom_button(xx,yy=1):
        zoom xx
        alpha yy

    transform move_ship(x1,y1,x2,y2,speed=0.45,delay=0):
        on start:
            pause delay
            xpos x1 ypos y1
            linear speed xpos x2 ypos y2
            pause 3
            
    transform move_bullet(x1,y1,x2,y2,speed=0.45,delay=0):
        on start:
            pause delay
            xpos x1 ypos y1
            linear speed xpos x2 ypos y2
            alpha 0
            pause 3            
            
    transform move_missile(x1,y1,x2,y2,speed=0.45):            
        xpos x1 ypos y1
        linear speed xpos x2 ypos y2
        alpha 0
        pause 3
            
    transform tr_explosion(p=0):
        # 'Battle UI/kinetic_explode.png'
        alpha 0
        pause p
        ease 0.5 alpha 1
        pause 0.5
        ease 1.5 alpha 0
        pause 3
            
    transform delayed_image(wait,img):
        alpha 0
        pause wait
        alpha 0.8

    transform delay_float_text(yy,wait):
        ypos yy
        alpha 0
        time wait
        alpha 1
        easein 1.0 ypos int(yy-80*zoomlevel)
        pause 2
        alpha 0
        
    transform damage_float(yy,t=0):        
        pause t
        ypos yy        
        linear 2.0 ypos (yy - 100)
        
    transform tr_melee_animation():
        alpha 0
        ease 0.2 alpha 1
        pause 0.5
        ease 0.2 alpha 0
        
    transform ship_dissolve:
        alpha 1
        ease 1.5 alpha 0
        
        #proper crop animation is gonna be HARD as it'll need to account for angle. let's go easy mode instead
        # crop_relative True
        # crop (0,0,1,0)
        # linear 0.2 crop (0,0,1,1)
        # pause 1
        # linear 0.2 crop (0,0,1,0)

    python:
        class ImageCache(store.object):
            """Stores all the images used by the battle screen so they stay cached"""
            def __init__(self):
                self.hexgrid = Image('Battle UI/hexgrid.png')
                self.blue_hex = Image("Battle UI/blue hex.png")
                self.red_hex = Image("Battle UI/red hex.png")
                self.player_base = Image("Battle UI/player base.png")
                self.pact_base = Image("Battle UI/pact_base.png")
                self.pirate_base = Image("Battle UI/pirate_base.png")
                self.hp_bar = Image('Battle UI/label hp bar.png')
                self.energy_bar = Image('Battle UI/label energy bar.png')
                self.targeting_window = Image('Battle UI/targeting_window.png')
                self.move_tile = Image('Battle UI/move_tile.png')



screen battle_screen():
    tag tactical
    modal False
    zorder -5
    key "mousedown_4" action [ If(zoomlevel<2.0,ZoomAction(["zoom", "in"]),NullAction()) ]    #scroll in and out
    key "mousedown_5" action [ If(zoomlevel>0.5,ZoomAction(["zoom", "out"]),NullAction()) ]
    key "K_PAGEUP" action Return(["zoom", "in"])
    key "K_PAGEDOWN" action Return(["zoom", "out"])
    if 'mouseup_2' not in config.keymap['hide_windows']:
        key "mousedown_2" action Return(["next ship"])
    if 'mouseup_3' not in config.keymap['game_menu']:
        key "mousedown_3" action Return(["deselect"])
    
    if (BM.phase == "Player" or BM.phase == 'formation') and BM.battlemode and BM.active_weapon is None:
        key "[" action Return(["previous ship"])
        key "]" action Return(["next ship"])
        
    #experimental
    if BM.enable_hotkeys:
        key "repeat_K_w" action Function(scroll_wasd,"W")
        key "K_w" action Function(scroll_wasd,"W")
        key "repeat_K_a" action Function(scroll_wasd,"A")
        key "a" action Function(scroll_wasd,"A")
        key "repeat_K_s" action Function(scroll_wasd,"S")
        key "s" action Function(scroll_wasd,"S")
        key "repeat_K_d" action Function(scroll_wasd,"D")
        key "d" action Function(scroll_wasd,"D")
        
        if BM.active_weapon is None:
            key "K_F1" action If( sunrider in player_ships and sunrider.location is not None,Return(['selection',sunrider]), NullAction())
            key "K_F2" action If( blackjack in player_ships and blackjack.location is not None,Return(['selection',blackjack]), NullAction())
            key "K_F3" action If( liberty in player_ships and liberty.location is not None,Return(['selection',liberty]), NullAction())
            key "K_F4" action If( phoenix in player_ships and phoenix.location is not None,Return(['selection',phoenix]), NullAction())
            key "K_F5" action If( bianca in player_ships and bianca.location is not None,Return(['selection',bianca]), NullAction())
            key "K_F6" action If( seraphim in player_ships and seraphim.location is not None,Return(['selection',seraphim]), NullAction())
            key "K_F7" action If( paladin in player_ships and paladin.location is not None,Return(['selection',paladin]), NullAction())

    ##messing with the player for fun and profit
    if BM.battlemode:
        timer 900 repeat False action Show('game_over_gimmick')

    add MouseTracker() #relates drags and clicks to the viewport and the BM

    if config.developer: #a release version should have set this to False
        key "Q" action Jump(['quit'])  ##DEBUG FAST QUIT##
        # key "A" action Return(['anime'])
        if BM.phase != 'formation':
            key "P" action Return(['I WIN'])

    $childx = round(3840*zoomlevel) #this makes it so you can't scroll past the edge of the battlefield when zoomed out
    $childy = round(3006*zoomlevel+300) #extra 300 is so that the status window doesn't occlude ships in the far right bottom corner

    add BM.battle_bg xalign 0.5 yalign 0.5 #zoom 0.5 ##background for the battlefield##

    viewport id "grid":
        xmaximum 1920
        ymaximum 1080
        xadjustment BM.xadj
        yadjustment BM.yadj
        child_size (childx,childy)
        draggable False #BM.draggable
        mousewheel False
        edgescroll BM.edgescroll #(0,0) #(70,400*zoomlevel)

                ##CREATE HEX GRID##

##laggy as fuck!!
        if BM.show_grid:
            for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                    $xposition = dispx(a, b, zoomlevel)
                    $yposition = dispy(a, b, zoomlevel)
                    $xsize = int((HEXW + 4) * zoomlevel)
                    $ysize = int((HEXH + 4) * zoomlevel)
                    add "Battle UI/hex.png":
                        xpos xposition
                        ypos yposition
                        size (xsize,ysize)
                        alpha 0.4
        else:
##much faster!
            $xsize = int((HEXW+5.5) * zoomlevel * 18)
            $ysize = int((HEXD+4) * zoomlevel * 16)
            $grid_image = "Battle UI/start_hexgrid.png" if BM.phase == 'formation' else IC.hexgrid
            add grid_image:
                alpha 0.4
                # zoom zoomlevel * 0.685
                size (xsize,ysize)
                xpos int(HEXW * zoomlevel)
                ypos int((HEXD-2) * zoomlevel)

        if not BM.hovered == None: #when you hover over a ship
            if BM.hovered.shield_generation > 0:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.shield_range:
                            $ ship = BM.hovered
                            $ effective_shielding = ship.shield_generation + ship.modifiers['shield_generation'][0]
                            if effective_shielding > 0:
                                $xposition = dispx(a,b,zoomlevel)
                                $yposition = dispy(a,b,zoomlevel)
                                $xsize = int((HEXW + 4) * zoomlevel)
                                $ysize = int((HEXH + 4) * zoomlevel)
                                add IC.blue_hex:
                                    xpos xposition
                                    ypos yposition
                                    size (xsize,ysize)
                                    alpha 0.7
            if BM.hovered.flak > 0:
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                    for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                        if get_distance(BM.hovered.location,(a,b)) <= BM.hovered.flak_range:
                            $ ship = BM.hovered
                            $effective_flak = ship.flak + ship.modifiers['flak'][0]
                            if effective_flak > 0:
                                $xposition = dispx(a,b,zoomlevel)
                                $yposition = dispy(a,b,zoomlevel)
                                $xsize = int((HEXW + 4) * zoomlevel)
                                $ysize = int((HEXH + 4) * zoomlevel)
                                add IC.red_hex:
                                    xpos xposition
                                    ypos yposition
                                    size (xsize,ysize)
                                    alpha 0.9

        if not BM.weaponhover == None: #when you hover over a weapon button
            if BM.weaponhover.wtype == 'Missile' or BM.weaponhover.wtype == 'Rocket' or BM.weaponhover.name == 'Flak Off':
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            for ship in enemy_ships:
                                if get_distance(ship.location,(a,b)) <= ship.flak_range:
                                    $effective_flak = ship.flak + ship.modifiers['flak'][0]
                                    if effective_flak > 0:
                                        $xposition = dispx(a,b,zoomlevel)
                                        $yposition = dispy(a,b,zoomlevel)
                                        $xsize = int((HEXW + 4) * zoomlevel)
                                        $ysize = int((HEXH + 4) * zoomlevel)
                                        add IC.red_hex:
                                            xpos xposition
                                            ypos yposition
                                            size (xsize,ysize)
                                            alpha 0.9
            if BM.weaponhover.wtype == 'Laser' or BM.weaponhover.wtype == 'Pulse' or BM.weaponhover.name == 'Shield Down' or BM.weaponhover.name == 'Shield Jam':
                for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                        for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                            for ship in enemy_ships:
                                if get_distance(ship.location,(a,b)) <= ship.shield_range:
                                    $effective_shielding = ship.shield_generation + ship.modifiers['shield_generation'][0]
                                    if effective_shielding > 0:
                                        $xposition = dispx(a,b,zoomlevel)
                                        $yposition = dispy(a,b,zoomlevel)
                                        $xsize = int((HEXW + 4) * zoomlevel)
                                        $ysize = int((HEXH + 4) * zoomlevel)
                                        add IC.blue_hex:
                                            xpos xposition
                                            ypos yposition
                                            size (xsize,ysize)
                                            alpha 0.7

                ## DISPLAY COVER ##
        for cover in BM.covers:
            $xposition = dispx(cover.location[0],cover.location[1],zoomlevel, 0.5)
            $yposition = dispy(cover.location[0],cover.location[1],zoomlevel, 0.5)
            $xsize = int(210 * zoomlevel)
            $ysize = int(120 * zoomlevel)
            add cover.label:
                xanchor 0.5
                yanchor 0.5
                xpos xposition
                ypos yposition
                size (xsize,ysize)
                at Transform(cover.label,rotate = cover.angle)



                ## DISPLAY SHIP AVATARS ##

        for ship in BM.ships: #cycle through every ship in the battle
                  ##first we show the circle base below every unit
            if ship.location != None: #and ship.hp > 0:
                $ x,y = ship.location
                if x > 0 and y > 0:
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJY) + int(zoomlevel * MOVY)
                    $xsize = int(210 * zoomlevel)
                    $ysize = int(120 * zoomlevel)
                    if ship.faction == 'Player':
                        add IC.player_base:
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            size (xsize,ysize)
                    if ship.faction == 'PACT':
                        add IC.pact_base:
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            size (xsize,ysize)
                    if ship.faction == 'Pirate' or ship.faction == 'Alliance':
                        add IC.pirate_base:
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            size (xsize,ysize)

                    $cell_width = 1920 / ((GRID_SIZE[0]+2)/2)
                    $cell_height = 1503 / ((GRID_SIZE[1]+2)/2)
                    #$cell_offset = cell_width / 2

                    #calculate the position of the ships on the field
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel, 0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel, 0.25 * ADJY) + int(zoomlevel * MOVY)

                    if ship.getting_buff:  #used if you buff someone
                        add 'Battle UI/buff_back.png':
                            xpos int(xposition-(cell_width/2)*zoomlevel)
                            zoom (zoomlevel/2.0)
                            at buffup(yposition)

                    if ship.getting_curse:  #used if you curse someone
                        add 'Battle UI/curse_back.png':
                            xpos int(xposition-(cell_width/2)*zoomlevel)
                            zoom (zoomlevel/2.0)
                            at cursedown(yposition-(190)*zoomlevel)

                    #default values.
                    $mode = '' #default
                    $lbl = ship.lbl
                    $hvr = im.MatrixColor(ship.lbl,im.matrix.brightness(0.2))  #hoverglow(ship.lbl) #turned off for performance reasons
                    $ship_alpha = 1

                    ##depending on the circumstance of the particular ship in the loop the avatar should appear normally, should blink(target) or should appear dark(offline).

                    if ship.faction == 'Player':
                        #by default player ships can be selected, which the above values are already set to.
                        
                        if ship.has_buff("Cloak"):
                            $ship_alpha = 0.4

                        if BM.targetingmode:
                            #you cannot target yourself with an active weapon
                            $ mode = 'offline'

                            if BM.active_weapon != None:
                                if BM.active_weapon.wtype == 'Support':
                                    #except when the active weapon is a support skill. in that case, player ships become targets
                                    $ mode = 'target'
                                    #except except if this support weapon is only usable on certain types
                                    if hasattr(BM.active_weapon,'target_type_restriction'):
                                        if BM.active_weapon.target_type_restriction != []:
                                            if ship.stype not in BM.active_weapon.target_type_restriction:
                                                $ mode = 'offline'

                            if ship.cth <=0:
                                #if the target cannot be affected it should be made obvious.
                                $ mode = 'offline'

                    else: #ship is an enemy faction
                        #by default enemy ships can be selected (to view stat details), which the above values are already set to.

                        if BM.targetingmode and BM.active_weapon != None:
                            #with an active weapon selected enemies become targets
                            $ mode = 'target'

                            if BM.active_weapon.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(BM.selected,ship) != 1):
                                #except when the active weapon is melee and this enemy is neither a ryder nor next to the attacking ship
                                $ mode = 'offline'

                            if BM.active_weapon.wtype == 'Support':
                                $ mode = 'offline'

                    if BM.active_weapon != None:
                        if BM.active_weapon.name == 'Gravity Gun':
                            #the gravity gun is a bit unique
                            $mode = 'target'
                            if BM.active_weapon.works_only_on is not None:
                                if ship.stype != BM.active_weapon.works_only_on:
                                    $ mode = 'offline'

                    if mode == 'target':
                        $ lbl = im.MatrixColor(ship.lbl,im.matrix.brightness(0.2))  #no more hoverglow as it's laggy
                    elif mode == 'offline':
                        $ lbl = im.MatrixColor(ship.lbl,im.matrix.brightness(-0.3))

                    if BM.hovered != None:
                        if BM.hovered == ship:
                            if mode != 'offline':
                                $ lbl = im.MatrixColor(ship.lbl,im.matrix.brightness(0.2)) #hoverglow(ship.lbl)
                    
                    add lbl:
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition
                        zoom (zoomlevel/2.5)
                        alpha ship_alpha

                    if ship.getting_buff:
                        add 'Battle UI/buff_front.png':
                            xpos int(xposition-96*zoomlevel)
                            zoom (zoomlevel/2.0)
                            at buffup(int(yposition+50*zoomlevel))

                    if ship.getting_curse:
                        add 'Battle UI/curse_front.png':
                            xpos int(xposition-96*zoomlevel)
                            zoom (zoomlevel/2.0)
                            at cursedown(yposition-(190-50)*zoomlevel)

                      ##add the HP bar and the EN bar
                    if ship.faction == 'Player':
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.08 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.66 * ADJY) + int(zoomlevel * MOVY)
                        $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                        add IC.hp_bar:
                            xpos xposition
                            ypos yposition
                            zoom (zoomlevel/2.5)
                            crop (0,0,hp_size,79)

                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.08 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.72 * ADJY) + int(zoomlevel * MOVY)
                        $energy_size = int(405*(float(ship.en)/ship.max_en))
                        add IC.energy_bar:
                            xpos xposition
                            ypos yposition
                            zoom (zoomlevel/2.5)
                            crop (0,0,energy_size,79)

                        text str(ship.hp):
                            xanchor 0.5
                            yanchor 0.5
                            xpos int(xposition+80*zoomlevel)
                            ypos int(yposition+27*zoomlevel)
                            size int(16) #*zoomlevel)
                            font "Fonts/SourceCodePro-Regular.ttf"
                            outlines [(2,'000',0,0)]

                    else:    #enemies
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.09 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.70 * ADJY) + int(zoomlevel * MOVY)
                        $hp_size = int(405*(float(ship.hp)/ship.max_hp))
                        add IC.hp_bar:
                            xpos xposition
                            ypos yposition
                            zoom (zoomlevel/2.5)
                            crop (0,0,hp_size,90)

                        text str(ship.hp):
                            xanchor 0.5
                            yanchor 0.5
                            xpos int(xposition+80*zoomlevel)
                            ypos int(yposition+27*zoomlevel)
                            size int(16) #*zoomlevel)
                            font "Fonts/SourceCodePro-Regular.ttf"
                            outlines [(2,'000',0,0)]
                            
                    if ship.is_cursed():
                        add 'Battle UI/cursedicon.png':
                            xanchor 0.5
                            yanchor 0.5
                            xpos xposition
                            ypos yposition
                            zoom 1.5

##show drones  <<experimental>>
        for drone in BM.drones:
            if drone.location is not None:
                $xposition = dispx(drone.location[0],drone.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(drone.location[0],drone.location[1],zoomlevel,1.25 * ADJY) + int(zoomlevel * MOVY)
                
                add drone.drone_lbl:
                    anchor (0.5,0.5)
                    xpos xposition
                    ypos yposition
                            
##show flak icon and intercept text
        if BM.missile_moving:
            for ship in BM.ships:
                if ship.flaksim != None and ship.flak > 0 and ship.location is not None:
                    $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                    $ wait = ship.flaksim[0]
                    $ intercept_count = ship.flaksim[1]
                    if intercept_count:
                        $ BM.battle_log_insert(['attack', 'missile'], "{0} intercepted {1} missiles! Effectiveness: {2}%".format(ship.name, intercept_count, int(ship.flak_effectiveness)))

                    add 'Battle UI/warning icon.png':
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition
                        zoom (zoomlevel/2.5)
                        alpha 1
                        at delayed_image(wait,'Battle UI/warning icon.png')

                    $ textcolor = 'f00'
                    if ship.faction == 'Player':
                        $ textcolor = '0f0'

                    text '{} intercepted! \neffectiveness: {}%'.format( intercept_count , int(ship.flak_effectiveness) ):
                        xanchor 0.5
                        yanchor 0.5
#                        xmaximum 200
                        xpos xposition
                        ypos yposition
                        size 24
                        color textcolor
                        outlines [(2,'000',0,0)]
                        at delay_float_text(yposition,wait)


##show missiles on the map that are currently flying in space##

        if BM.missile_moving:
            for missile in BM.missiles:
                if missile.parent.location != None and missile.target.location != None: #failsafes
                    $xposition = dispx(missile.parent.location[0], missile.parent.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(missile.parent.location[0], missile.parent.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                    $next_xposition = dispx(missile.target.location[0],missile.target.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                    $next_yposition = dispy(missile.target.location[0],missile.target.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)

                    #calculate travel time and set explosion size
                    $ travel_time = get_ship_distance(missile.parent,missile.target)*MISSILE_SPEED*1.5
                    if missile.shot_down:
                        $explosion_size = 0.08
                    else:
                        if missile.aoe_range > 0:
                            $explosion_size = 0.6
                        else:
                            $explosion_size = 0.15
                        
                    #show missile. the transform handles movement animation
                    add missile.lbl:
                        at move_missile(xposition,yposition,next_xposition,next_yposition,travel_time)
                        xanchor 0.5
                        yanchor 0.5
                        zoom (zoomlevel/4.0)
                        
                    #show an explosion at destination.
                    add 'Battle UI/map_splashexplode.png':
                        at tr_explosion(travel_time)
                        xpos next_xposition
                        ypos next_yposition
                        zoom explosion_size
                        xanchor 0.5
                        yanchor 0.5

##show other types of bullets moving
        if not BM.shooting == False:
            $ bullet = BM.shooting
            if bullet.parent.location is not None and bullet.target.location is not None: #failsafes
                $xposition = dispx(bullet.parent.location[0], bullet.parent.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(bullet.parent.location[0], bullet.parent.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                $next_xposition = dispx(bullet.target.location[0],bullet.target.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $next_yposition = dispy(bullet.target.location[0],bullet.target.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
            
                $adjacent = next_xposition - xposition
                $opposite = next_yposition - yposition
                $angle = math.degrees( math.atan2(adjacent,opposite) )
            
                if bullet.type == 'Laser':
                    add "Battle UI/laserhit map.png":
                        xpos xposition
                        ypos yposition
                        yanchor 0.5
                        xanchor 0.0
                        rotate (360-angle)+90
                        transform_anchor True
                        # at tr_explosion
            
                elif bullet.type == 'Melee':
                    add bullet.lbl:
                        at tr_melee_animation
                        pos (next_xposition,next_yposition)
                        yanchor 0.5
                        xanchor 0.5
                        # rotate (360-angle)-135
                        # transform_anchor True
                        zoom 0.2
                
                else:
                    $wait = 0
                    for a in range(bullet.shot_count):
                        $x_fudging = renpy.random.randint(-25,25)
                        $y_fudging = renpy.random.randint(-20,20)
                        $wait += 0.02
                        
                        $ travel_time = get_ship_distance(bullet.parent,bullet.target)*0.2
                        add bullet.lbl:
                            at move_bullet(xposition,yposition,next_xposition+x_fudging,next_yposition+y_fudging,travel_time,wait)
                            xanchor 0.5
                            yanchor 0.5
                            zoom (zoomlevel/3.0)
                        
##DISPLAY MOVEMENT OPTIONS##
        if BM.selectedmode and BM.selected != None and not BM.shooting and not BM.exploding and not BM.taking_damage and not BM.vanguard and not BM.missile_moving and not BM.cmd_gained:
            if BM.selected.faction == 'Player' and not BM.targetingmode and not BM.phase == 'formation':
                for tile in BM.selected.movement_tiles:
                    $ lbl = IC.move_tile
                    $ tile_location = (tile[3],tile[4])

                    #trick for gravity gunned units.
                    $gravved = False
                    if BM.selected.move_cost == 0 and BM.selected not in player_ships: 
                        $gravved = True
                    
                    if get_counter_attack(tile_location,gravved) and not (BM.selected.has_buff("Stealth") or BM.selected.has_buff("Cloak")):
                        $ lbl = im.MatrixColor(lbl,im.matrix.tint(1.0, 0.5, 0.5))

                    if tile_location == BM.mouse_location:
                        $ lbl = hoverglow(lbl)
                    add lbl:
                        zoom (0.2 * zoomlevel)
                        alpha 0.5
                        xanchor 0.5
                        yanchor 0.5
                        xpos tile[0]
                        ypos tile[1]

                    text (str(BM.selected.move_cost*tile[2]) + ' EN'):
                        xpos tile[0]
                        ypos tile[1]
                        xanchor 0.5
                        yanchor 0.5
                        size (20) # * zoomlevel)
                        outlines [(2,'000',0,0)]

        ##targeting window##

          ##if targeting mode is active show a targeting window over all enemy_ships that gives you chance to hit and other data
        if BM.weaponhover != None or BM.targetingmode and BM.selected != None:
            $ selected = BM.selected  #the screen sometimes seems to get confused so a local copy is probably safer

            ##DISPLAY TARGETING WINDOW##          
            for ship in BM.ships:
                if ship.location is not None and (BM.active_weapon is not None or BM.weaponhover is not None) and ship.cth > 0:

                    $skip = False
                    if BM.weaponhover == None:
                        $BM.weaponhover = BM.active_weapon
                    if BM.weaponhover.wtype == 'Support' and (ship.faction != 'Player' or BM.weaponhover.self_buff == True):
                        $skip = True
                    elif BM.weaponhover.wtype != 'Support' and ship.faction == 'Player' and BM.weaponhover.wtype != 'Special':
                        # wtype:'Special' is a support type that's neither a curse nor a buff but can be used on enemies and player units both
                        $skip = True
                    elif BM.weaponhover.wtype == 'Melee' and (ship.stype != 'Ryder' or get_ship_distance(ship,selected) > 1):
                        $skip = True
                    if BM.weaponhover.wtype == 'Support':
                        if hasattr(BM.weaponhover,'target_type_restriction'):
                            if BM.weaponhover.target_type_restriction != []:
                                if ship.stype not in BM.weaponhover.target_type_restriction:
                                    $skip = True

                    #the gravity gun is a little... special
                    elif BM.weaponhover.name == 'Gravity Gun':
                        if BM.weaponhover.works_only_on is not None:
                            if ship.stype != BM.weaponhover.works_only_on:
                                $skip = True
                    
                    if not skip:
                        #targeting window
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        add IC.targeting_window:
                            xpos xposition
                            ypos yposition
                            xanchor 0.234
                            yanchor 0.347
                            zoom 0.9
                            
                        #chance to hit text
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        text (str(ship.cth) + '%'):
                            xpos xposition -15
                            ypos yposition -25
                            xanchor -1.5
                            yanchor -0.5
                            size (20) # * zoomlevel)
                            min_width 50
                            text_align 1.0
                            color '000'
                            
                        #effective flak text
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        if selected == None:  #workarounds
                            $ effective_flak = 0
                        else:
                            if BM.weaponhover.wtype == 'Rocket':
                                #this looks double but missile_eccm is from a ship through upgrades whereas weaponhover.eccm is rom the rocket itself. (default 10)
                                $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm - BM.weaponhover.eccm
                            else:
                                $effective_flak = ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm

                        if effective_flak < 0:
                            $ effective_flak = 0
                        elif effective_flak > 100:
                            $ effective_flak = 100

                        text str(effective_flak):
                            xpos xposition -20
                            ypos yposition -25
                            xanchor 0.0
                            yanchor -1.9
                            size (17) # * zoomlevel)
                            min_width 50
                            text_align 1.0
                            color 'fff'
                            
                        #shield strength
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                        text str(ship.shields):
                            xpos xposition -20
                            ypos yposition -25
                            xanchor -0.85
                            yanchor -1.9
                            size (17) # * zoomlevel)
                            min_width 50
                            text_align 1.0
                            color 'fff'
                        
                        #armor strength
                        $xposition = dispx(ship.location[0],ship.location[1],zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                        $yposition = dispy(ship.location[0],ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                          ##when you hover over a weapon that does kinetic or assault type damage it shows you armor is double as effective
                        if BM.weaponhover == None:
                            $weapon = BM.active_weapon
                        else:
                            $weapon = BM.weaponhover
                        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                            text (str(ship.armor) + 'x2'):
                                xpos xposition -20
                                ypos yposition -28
                                xanchor -1.75
                                yanchor -2.1
                                size (15) # * zoomlevel)
                                min_width 50
                                text_align 1.0
                                color 'fff'
                                outlines [(1,'000',0,0)]
                        else:
                            text str(ship.armor):
                                xpos xposition -22
                                ypos yposition -25
                                xanchor -1.6
                                yanchor -1.9
                                size (17) # * zoomlevel)
                                min_width 50
                                text_align 1.0
                                color 'fff'

            # draw missile path
            if BM.hovered != None and BM.active_weapon != None and (BM.active_weapon.wtype == 'Missile' or BM.active_weapon.wtype == 'Rocket'):
                $ loc1 = selected.location
                $ loc2 = BM.hovered.location
                $ tiles = interpolate_hex(loc1, loc2)
                $ effective_flak = 0
                $ total_effective_flak = 0
                for i, tile in enumerate(tiles):
                    $xposition = dispx(tile[0],tile[1],zoomlevel)
                    $yposition = dispy(tile[0],tile[1],zoomlevel)
                    $xsize = int((HEXW + 4) * zoomlevel)
                    $ysize = int((HEXH + 4) * zoomlevel)

                    add "Battle UI/missile hex.png":
                        xpos xposition
                        ypos yposition
                        size (xsize,ysize)
                        alpha 0.4

                    for ship in enemy_ships:
                        if ship.location is not None and not ship.flak_used:
                            if get_distance(tile,ship.location) <= ship.flak_range:
                                if BM.active_weapon.wtype == 'Rocket':
                                    #this looks double but missile_eccm is from a ship through upgrades whereas weaponhover.eccm is from the rocket itself. (default 10)
                                    $ effective_flak = (ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm - BM.active_weapon.eccm)
                                else:
                                    $effective_flak = (ship.flak + ship.modifiers['flak'][0] - selected.missile_eccm)
                                if effective_flak > 100:
                                    $ effective_flak = 100
                                elif effective_flak < 0:
                                    $ effective_flak = 0

                                $ total_effective_flak = total_effective_flak + (1 - total_effective_flak/100.0) * effective_flak
                                $ ship.flak_used = True

                    if total_effective_flak > 100:
                        $total_effective_flak = 100

                    if i+1 == len(tiles):
                        if total_effective_flak > 0:
                            # FIXME I canna get tile[0] and tile[1] to work properly
                            add 'Battle UI/icon_intercept.png':
                                zoom (2 * zoomlevel)
                                #alpha 0.7
                                xpos xposition -20
                                ypos yposition -20
                                xoffset xsize/3
                                yoffset ysize/2
                                xanchor 0.5
                                yanchor 0.5
                            text str(int(round(total_effective_flak,0))) + "%":
                                xpos xposition -20
                                ypos yposition -20
                                xoffset xsize/3
                                yoffset ysize/2
                                xanchor 0.5
                                yanchor 0.5
                                size (30 * zoomlevel)
                                color 'bbb'
                                outlines [(2,'000',0,0)]

                for ship in BM.ships:
                    $ ship.flak_used = False
                $ effective_flak = 0
                $ total_effective_flak = 0          
          
          #firing the vanguard cannon 
        if BM.vanguard != False and sunrider.location is not None:
            $xposition = dispx(sunrider.location[0], sunrider.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
            $yposition = dispy(sunrider.location[0], sunrider.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
            $next_xposition = dispx(BM.vanguard[0],BM.vanguard[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
            $next_yposition = dispy(BM.vanguard[0],BM.vanguard[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
            
            #yay high school math
            $adjacent = next_xposition - xposition
            $opposite = next_yposition - yposition
            $angle = math.degrees( math.atan2(adjacent,opposite) )
            $hypotenuse  = int(math.hypot(adjacent,opposite)) + 200
            
            $vanguard_image = Image('Battle UI/vanguard beam wave.png')
            $beam_width = 500 if BM.vanguard_splash else 200
            $vanguard_transform = Transform(vanguard_image, size =(hypotenuse , beam_width))
            
            add vanguard_transform:
                xpos xposition + 25
                ypos yposition
                yanchor 0.5
                xanchor 0.0
                rotate (360-angle)+90
                transform_anchor True
                at vanguard_cannon(hypotenuse)
                

         #selecting target for vanguard cannon
        if BM.vanguardtarget:
            $ loc1 = sunrider.location
            $ loc2 = BM.mouse_location
            if not BM.vanguard_splash:
                $tiles = interpolate_hex(loc1, loc2)
            else:
                $tiles = interpolate_hex_splash(loc1,loc2)
            
            for i in tiles:
                $xposition = dispx(i[0],i[1],zoomlevel)
                $yposition = dispy(i[0],i[1],zoomlevel)
                $xsize = int((HEXW + 4) * zoomlevel)
                $ysize = int((HEXH + 4) * zoomlevel)
                add "Battle UI/vanguard hex.png":
                    xpos xposition
                    ypos yposition
                    size (xsize,ysize)
                    alpha 0.7

        if BM.enemy_vanguard_path is not None:
            for hex in BM.enemy_vanguard_path:
                $xposition = dispx(hex[0],hex[1],zoomlevel)
                $yposition = dispy(hex[0],hex[1],zoomlevel)
                $xsize = int((HEXW + 4) * zoomlevel)
                $ysize = int((HEXH + 4) * zoomlevel)
                add "Battle UI/vanguard hex.png":
                    xpos xposition
                    ypos yposition
                    size (xsize,ysize)
                    alpha 0.7

          #the Sunrider warps from one cell to another
        if BM.warping:
            for location in store.flash_locations:
                $xposition = dispx(location[0],location[1],zoomlevel) + int(zoomlevel * MOVX)
                $yposition = dispy(location[0],location[1],zoomlevel,-0.5 * ADJY) + int(zoomlevel * MOVY)
                add 'Battle UI/label_warpflash.png':
#                    anchor 0.5  #I get a float object not iterable crash. very annoying
                    xpos xposition
                    ypos yposition
                    at warpout
                    zoom 0.25 * zoomlevel

            ##MOVE SHIP FROM GRID TO GRID##
        if BM.moving and BM.selected != None:
            if BM.selected.current_location != None and BM.selected.next_location != None:
                $xposition = dispx(BM.selected.current_location[0],BM.selected.current_location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(BM.selected.current_location[0],BM.selected.current_location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                $next_xposition = dispx(BM.selected.next_location[0],BM.selected.next_location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $next_yposition = dispy(BM.selected.next_location[0],BM.selected.next_location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)

                $travel_time = BM.selected.travel_time

                add BM.selected.lbl:
                    at move_ship(xposition,yposition,next_xposition,next_yposition,travel_time)
                    xanchor 0.5
                    yanchor 0.5
                    zoom (zoomlevel/2.5)

        if BM.debugoverlay:  #may use this later for AI debug things too
            for a in range(1,GRID_SIZE[0]+1):  #cycle through rows
                for b in range(1,GRID_SIZE[1]+1):  #cycle through columns
                    $xposition = dispx(a,b,zoomlevel,0.5 * ADJX) + int(zoomlevel * MOVX)
                    $yposition = dispy(a,b,zoomlevel,0.5 * ADJY) + int(zoomlevel * MOVY)

                    text '{}/{}'.format(a,b):
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition
                        
        ##show an explosion when shit be dying
        if not BM.exploding == False:
            if type(BM.exploding) is not list:
                $explosions = [BM.exploding]
            else:
                $explosions = BM.exploding
            
            for explosion in explosions:
                $fading = False
                if type(explosion) is tuple:
                    $location = explosion
                else:
                    if explosion.pilot is not None: 
                        $fading = True
                    $location = explosion.location
                $xposition = dispx(location[0],location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(location[0],location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
            
                if not fading:
                    add 'Battle UI/kinetic_explode.png':
                        at tr_explosion
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition
                else:
                    add explosion.lbl:
                        at ship_dissolve
                        xanchor 0.5
                        yanchor 0.5
                        xpos xposition
                        ypos yposition
                        zoom (zoomlevel/2.5)
                        
        ##show damage on top of units
        if BM.taking_damage:
            if not type(BM.taking_damage) is dict:
                $ship,damage = BM.taking_damage
                $shiplist = {}
                $shiplist[ship] = damage
            else:
                $shiplist = BM.taking_damage
            
            for ship in shiplist:
                $energy_mitigation = 0
                $armor_mitigation = 0
                if type(shiplist[ship]) is tuple:
                    $damage,energy_mitigation,armor_mitigation = shiplist[ship]
                else:
                    $damage = shiplist[ship]
                $xposition = dispx(ship.location[0], ship.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(ship.location[0], ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                $damage_color = 'c00'
                if damage < 0:
                    $damage_color = '070'
                    $damage = -damage
                    
                if damage >= 0:
                    text str(damage):
                        at damage_float(yposition)
                        xpos xposition
                        xanchor 0.5
                        yanchor 0.5
                        size 40
                        color damage_color
                        outlines [(2,'fff',0,0)]
                
                $delay_float_text = 0.2
                $y_offset = 15
                
                if energy_mitigation > 0:
                    # hbox:
                        # at damage_float(yposition,delay_float_text)
                        # xpos xposition
                    add "Battle UI/icon_shield.png":
                        zoom 0.5 
                        xpos xposition 
                        at damage_float(yposition+y_offset,delay_float_text)
                        xanchor 0.5
                        yanchor 0.5
                    text "       "+str(energy_mitigation):
                        at damage_float(yposition+y_offset,delay_float_text)
                        xpos xposition
                        xanchor 0.5
                        yanchor 0.5
                        size 20
                        color '44F'
                        outlines [(2,'fff',0,0)]
                    $y_offset += 20
                
                if armor_mitigation > 0:
                        
                    add "Battle UI/icon_armor.png":
                        at damage_float(yposition+y_offset,delay_float_text)
                        zoom 0.5
                        xpos xposition
                        xanchor 0.5
                        yanchor 0.5
                    text "     "+str(armor_mitigation):
                        at damage_float(yposition+y_offset,delay_float_text)
                        xpos xposition
                        xanchor 0.5
                        yanchor 0.5
                        ymaximum 50
                        size 20
                        color '444'
                        outlines [(2,'fff',0,0)]

        ##show +CMD message after something blows up.
        if hasattr(BM,'cmd_gained'): 
            if BM.cmd_gained is not None:
                $ship,points = BM.cmd_gained
                $xposition = dispx(ship.location[0], ship.location[1],zoomlevel,0.50 * ADJX) + int(zoomlevel * MOVX)
                $yposition = dispy(ship.location[0], ship.location[1],zoomlevel,0.25 * ADJY) + int(zoomlevel * MOVY)
                $floating_text = "+"+str(points)+" CMD" if ship in enemy_ships else "-$"+str(points)
                
                text floating_text:
                    at damage_float(yposition)
                    xpos xposition
                    xanchor 0.5
                    yanchor 0.5
                    size 40
                    color '007'
                    outlines [(2,'fff',0,0)]                          


##not part of the viewport##
    if BM.phase != 'formation':
        vbox:
            xalign 1.0
            ypos 80
            vbox:
                xalign 1.0
                # disable until restart turn is redone
                #if store.Difficulty < 3 or config.developer:
                #    textbutton "restart turn" xalign 1.0 action Jump('restartturn')
                if BM.mission == 'skirmish' or config.developer and debugbuttons == True:
                    textbutton "Player AI" xalign 1.0 action Return(['toggle player ai'])
            if config.developer and debugbuttons == True:
                vbox:
                    xalign 1.0
                    textbutton "Debug Cheats" xalign 1.0 action Return(['cheat'])
                    textbutton "Fast Quit" xalign 1.0 action Jump('quit')

                    if BM.debugoverlay:
                        textbutton "coord overlay" xalign 1.0 action SetField(BM,'debugoverlay',False)
                    else:
                        textbutton "coord overlay" xalign 1.0 action SetField(BM,'debugoverlay',True)
                    if BM.show_grid:
                        textbutton "new grid" xalign 1.0 action SetField(BM,'show_grid',False)
                    else:
                        textbutton "old grid" xalign 1.0 action SetField(BM,'show_grid',True)
                    textbutton "debug log" xalign 1.0 action Show('debug_window')
                    textbutton "debug pships" xalign 1.0 action Show('debug_pships')
                    textbutton "debug eships" xalign 1.0 action Show('debug_eships')

    if BM.just_moved:
        if _preferences.language == "spanish":
            textbutton 'cancelar movimiento':
                ypos 70
                text_size 50
                text_color 'fff'
                action Return(['cancel movement'])
        else:
            textbutton 'cancel movement':
                ypos 70
                text_size 50
                text_color 'fff'
                action Return(['cancel movement'])

    if not BM.showing_orders and not BM.missile_moving and not BM.moving and BM.phase == "Player" and sunrider.location != None:
        imagebutton:
            xpos 0
            ypos 0
            idle 'Battle UI/commandbar.png'
            hover hoverglow('Battle UI/commandbar.png')
            action [SetField(BM,'showing_orders',True),Show('orders')]
        text '{!s}'.format(BM.cmd):
            xanchor 1.0
            xpos 165
            ypos 10
            size 30
            color 'fff'
            outlines [(1,'000',0,0)]

    if BM.phase == 'Player':
        $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(0.6, 1.0, 0.5))
        for ship in player_ships:
            if ship.en >= ship.max_en:
                $endturnbutton_idle = im.MatrixColor('Battle UI/button_endturn.png',im.matrix.tint(1.0, 0.6, 0.5))

        imagebutton:
            xpos 90
            yalign 1.0
            idle endturnbutton_idle
            hover hoverglow(endturnbutton_idle)
            action Return(['endturn'])

    ## skirmish buttons start, return, remove, e.music, p.music
    if BM.phase == 'formation':
        imagebutton:
            xpos 170
            yalign 1.0
            idle 'Skirmish/start.png'
            hover hoverglow('Skirmish/start.png')
            action [ If( BM.selected==None , Return(['start']) ) ]

        if BM.mission == 'skirmish':
            imagebutton:
                xpos 88
                ypos 690
                idle 'Skirmish/return.png'
                hover hoverglow('Skirmish/return.png')
                action Return(['quit'])

            $ idl = 'Skirmish/remove.png'
            if BM.remove_mode:
                $ idl = hoverglow(im.MatrixColor('Skirmish/remove.png',im.matrix.tint(1.0, 1.0, 0)))

            imagebutton:
                xpos 208
                ypos 759
                idle idl
                hover hoverglow('Skirmish/remove.png')
                action Return(['remove'])

            imagebutton:
                xpos 328
                ypos 828
                idle 'Skirmish/enemymusic.png'
                hover hoverglow('Skirmish/enemymusic.png')
                action Show('enemy_music')

            imagebutton:
                xpos 448
                ypos 897
                idle 'Skirmish/playermusic.png'
                hover hoverglow('Skirmish/playermusic.png')
                action Show('player_music')

            imagebutton:
                xpos 414
                ypos 1022
                xanchor 0.5
                yanchor 0.5
                idle 'Menu/res_button.png'
                hover hoverglow('Menu/res_button.png')
                action Jump('RnD_skirmish')

transform move_down(ystart,yend,xx=0):
    xpos xx
    ypos ystart
    linear 0.5 ypos yend
    on hide:
        linear 0.5 ypos ystart
        #not sure why this is needed. I'm calling bug in renpy
        time 2
        alpha 0

screen orders:
    zorder 1
    modal True

    key "mousedown_3" action [Hide('orders'),SetField(BM,'showing_orders',False)]

    frame:
        background 'Battle UI/commandbar_window.png'
        at move_down(-590,0)
        vbox:
            spacing 20
            for order in BM.orders:
                $hide_order = False
                if order == 'RESURRECTION' and sunrider not in player_ships or order == 'RESURRECCIÓN' and sunrider not in player_ships:
                    $hide_order = True
                
                if not hide_order:
                    button:
                        xpos 20
                        idle_background 'Battle UI/commandbar_button.png'
                        hover_background hoverglow('Battle UI/commandbar_button.png')
                        action [Return([order]),Hide('orders'),SetField(BM,'showing_orders',False)]

                        has hbox

                        text order:
                            ypos 5
                            min_width 300
                            size 22
                            outlines [(1,'222',0,0)]

                        text str(BM.orders[order][0]):
                            ypos 5
                            xpos 50
                            min_width 50
                            text_align 1.0
    #                       first_indent 150
                            size 18
                            outlines [(1,'222',0,0)]

                        hbox:
                            #I should rework orders to include this info :/

                            if order == 'REPAIR DRONES' or order == 'DRONES REPARADORES':
                                if sunrider.repair_drones != None:
                                    if sunrider.repair_drones == 0:
                                        $colour = '900'
                                    else:
                                        $colour = '050'
                                    text '[[' + str(sunrider.repair_drones) + ']':
                                        ypos 5
                                        first_indent -140
                                        size 22
                                        color colour
                                        outlines [(1,colour,0,0)]

                            if order == 'FULL FORWARD' and BM.show_tooltips == True or order == 'AVANCE COMPLETO' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Provides +15 Aim and +20% damage to all allied units. Will cancel All Guard if active.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text unicode('Provee +15 Presición y +20% Daño a todas las unidades aliadas. Se cancelará si DEFENSA TOTAL se activa.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]

                            if order == 'ALL GUARD' and BM.show_tooltips == True or order == 'DEFENSA TOTAL' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Provides +15 Aim and +20% damage to all allied units. Will cancel All Guard if active.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text unicode('Provee +20 Flak, +10 Evasión y +10 Generación de Escudo a todas las naves. Se cancelará si AVANCE COMPLETO se activa.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                        
                            if order == 'ALL POWER TO ENGINES' and BM.show_tooltips == True or order == 'MÁXIMO PODER A LOS MOTORES' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Halves energy cost of movement for 2 turns'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text str('Reduce a la mitad el costo de movimiento durante 2 turnos.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                            
                            if order == 'SUMMON BATTLESHIP' and BM.show_tooltips == True or order == 'INVOCAR NAVE DE BATALLA' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Summon an Alliance battleship to your designated coordinates to fight alongside your fleet for three turns.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text str('Invoca una nave de batalla de la Alianza en las coordenadas designadas para luchar a tu lado durante 3 turnos.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]

                            if order == 'REPAIR DRONES' and BM.show_tooltips == True or order == 'DRONES REPARADORES' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Restores {}% of the Sunrider\'s health.'.format(str(int(BM.repair_drone_heal*100)))):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text str('Restaura el {}% de la salud del Sunrider.'.format(str(int(BM.repair_drone_heal*100)))):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]

                            if order == 'VANGUARD CANNON' and BM.show_tooltips == True or order == 'CAÑÓN VANGUARDIA' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    $ damage = get_modified_damage(BM.vanguard_damage,'notplayer')
                                    if _preferences.language != "spanish":
                                        text str('Deals {} unavoidable damage to all units in a straight line extending outwards from the Sunrider with a maximum range of {} hexes.'.format(damage,BM.vanguard_range)):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text unicode('Provoca {} de daño inevadible a todas las unidades en la línea que se extiende desde el Sunrider con un rango ilimitado.'.format(damage,BM.vanguard_range)):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]

                            if order == 'SHORT RANGE WARP' and BM.show_tooltips == True or order == 'SALTO DE CORTO RANGO' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Moves the Sunrider to any point on the map. Subsequent uses in the same turn become more expensive each time.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text str('Mueve al Sunrider a cualquier punto en el mapa. Subsiguientes usos en el mismo turno se volveran mas caros cada vez.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]

                            if order == 'RESURRECTION' and BM.show_tooltips == True or order == 'RESURRECCIÓN' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Select a downed unit to launch into the battle once more at full health.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text unicode('Selecciona una unidad destruida para lanzarla a la batalla una vez más con toda la salud.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]

                            if order == 'RETREAT' and BM.show_tooltips == True or order == 'RETIRADA' and BM.show_tooltips == True:
                                frame:
                                    background Solid((0,0,0,200))
                                    xpos 150
                                    ycenter 20

                                    if _preferences.language != "spanish":
                                        text str('Retreat your units from battle without applying penalties.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]
                                    else:
                                        text str('Retira a tus unidades de la batalla sin aplicar penalidades.'):
                                            xpos 0
                                            ypos 0
                                            size 18
                                            font "Fonts/SourceCodePro-Regular.ttf"
                                            outlines [(1,'000',0,0)]


                                        #I couldn't get the mouse detection working properly with the buttons. Sorry! :S

    imagebutton:
            at move_down(0,590)
            idle 'Battle UI/commandbar.png'
            hover hoverglow('Battle UI/commandbar.png')
            action [Hide('orders'),SetField(BM,'showing_orders',False)]
    text '{!s}'.format(BM.cmd):
        xanchor 1.0
        xpos 165
        ypos 10
        at move_down(10,600,165)
        size 30
        color 'fff'
        outlines [(1,'000',0,0)]

screen commands: ##show the weapon buttons etc##
    zorder 1 #always show on top of the battle screen

        ##show status window and its data
    if not BM.selected == None:
        $ ship = BM.selected
        add 'Battle UI/statuswindow.png' xalign 1.0 yalign 1.0
        if not hasattr(BM.selected,'portrait'):
            python:
                raise Exception("error: BM.selected is {}".format(BM.selected.__dict__))
            $BM.selected.portrait = None
        if BM.selected.portrait is not None:
            add BM.selected.portrait xalign 1.0 yalign 1.0
        else:
            $ index = ''
            if config.developer and BM.selected.faction != 'Player':
                if BM.selected in enemy_ships:
                    $ index = ' ' + str(enemy_ships.index(BM.selected))
                # text str(index) xanchor 1.0 xpos 1880 ypos 800 size 20 outlines [(1,'000',0,0)]
            text (BM.selected.name + index) xanchor 1.0 xpos 1880 ypos 726 outlines [(1,'000',0,0)]

        $hp_size = int(374*(float(BM.selected.hp)/BM.selected.max_hp))
        $en_size = int(298*(float(BM.selected.en)/BM.selected.max_en))
        add 'Battle UI/status window_HP.png' xpos 1080 ypos 779 crop (0,0,hp_size,49)
        add 'Battle UI/status window_EN.png' xpos 1133 ypos 805 crop (0,0,en_size,19)
        text (str(BM.selected.hp) + '/' + str(BM.selected.max_hp)) xanchor 0.5 xpos 1510 ypos 779 size 19 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]
        text (str(BM.selected.en) + '/' + str(BM.selected.max_en)) xanchor 0.5 xpos 1490 ypos 805 size 19 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]

        $effective_flak = ship.flak + ship.modifiers['flak'][0]
        if effective_flak < 0:
            $ effective_flak = 0
        elif effective_flak > 100:
            $ effective_flak = 100
        text (str(effective_flak)) xanchor 1.0 xpos 1149 ypos 847 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]

        text (str(BM.selected.shields)) xanchor 1.0 xpos 1149 ypos 897 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,BM.selected.shield_color,0,0)]
        text (str(BM.selected.armor)) xanchor 1.0 xpos 1149 ypos 947 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,BM.selected.armor_color,0,0)]
        text (str(BM.selected.evasion)) xanchor 1.0 xpos 1149 ypos 997 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]

        ##show weapon stats in status window on hover

        if not BM.weaponhover is None or not BM.active_weapon is None:
            if BM.weaponhover is None:
                $weapon = BM.active_weapon
            else:
                $weapon = BM.weaponhover
            text (str(real_damage(weapon,ship))) xanchor 1.0 xpos 1380 ypos 840 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]
            text (str(real_damage(weapon,ship)*weapon.shot_count)) xanchor 1.0 xpos 1380 ypos 870 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]
            text (str(weapon.shot_count)) xanchor 1.0 xpos 1515 ypos 840 size 24 font "Fonts/SourceCodePro-Regular.ttf" outlines [(1,'000',0,0)]

        # default tt = Tooltip("")

        ##show buffs
        $count = 0
        $duration_correction = 1
        if BM.selected.faction == 'Player' and BM.selected.move_cost > 0: #last part is gravity gun safety.
            $duration_correction = 0
        for buff in BM.selected.buffs:
            if not buff.curse:
                $ buff_turns_left = '  [[?]' if buff.turns_left == -1 else "  [[" + str(buff.turns_left-duration_correction) + "]"
                $ stacksize = '' if not buff.cumulative else str(buff.stack_counter)+'x '
                textbutton (stacksize + buff.name + buff_turns_left) action NullAction() xpos 1217 ypos (925+count*24) text_size 20 text_color 'fff' hovered BuffHover(buff) unhovered SetField(BM,'buffhover',None) #tt.Action(buff.tooltip) #outlines [(1,'000',0,0)]
                $count += 1
        $count = 0
        for buff in BM.selected.buffs:    
            if buff.curse:
                $ stacksize = '' if not buff.cumulative else str(buff.stack_counter)+'x '
                textbutton (stacksize + buff.name + "  [[" + str(buff.turns_left-duration_correction) + "]") action NullAction() xpos 1562 ypos (925+count*24) text_size 20 text_color 'a00' hovered BuffHover(buff) unhovered SetField(BM,'buffhover',None) text_align 1.0 xanchor 1.0
                # text (buff.name + "  [[" + str(buff.turns_left) + "]") xpos 1562 ypos (925+count*24) size 20 outlines [(1,'000',0,0)] color 'a00' text_align 1.0 xanchor 1.0
                $count += 1
        
        ##show weapon buttons
        if BM.selected.faction == 'Player':
            add 'Battle UI/button_arc.png' xalign 0.0 yalign 1.0
            $count = 0
            for weapon in BM.selected.weapons:
                if count < 4:
                    $x_offset = 8
                    $y_offset = 690
                else:
                    $x_offset = -353
                    $y_offset = 345

                #calculate the cost of this weapon based off of upgrades
                if weapon is not None:
                    $ energy_cost = weapon.energy_cost(BM.selected)
                else:
                    $ energy_cost = 99999
                # if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
                    # $ energy_cost = int(-weapon.energy_use * BM.selected.kinetic_cost)
                # if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
                    # $ energy_cost = int(-weapon.energy_use * BM.selected.energy_cost)
                # if weapon.wtype == 'Missile' or weapon.wtype == 'Rocket':
                    # $ energy_cost = int(-weapon.energy_use * BM.selected.missile_cost)
                # if weapon.wtype == 'Melee':
                    # $ energy_cost = int(-weapon.energy_use * BM.selected.melee_cost)

                #check if this weapon can be fired right now
                $can_fire = BM.selected.en >= energy_cost
                if weapon.hp_cost > BM.selected.hp:
                    $ can_fire = False
                if weapon.uses_missiles:
                    $ can_fire = can_fire and weapon.ammo_use <= BM.selected.missiles
                if weapon.uses_rockets:
                    $ can_fire = can_fire and weapon.ammo_use <= BM.selected.rockets
                if weapon.disabled:
                    $ can_fire = False

                #default behaviour
                $ lbl = weapon.lbl
                $ hvr = hoverglow(weapon.lbl)
                $ act = If(can_fire,FireWeapon(weapon))
                $ hvrd = HoverWeapon(weapon)
                $ unhvrd = SetField(BM,'weaponhover',None)
                $ insens = im.MatrixColor(weapon.lbl,im.matrix.brightness(-0.50))

                #the behavior of the imagebutton (representing a weapon) changes depending on various circumstances
                if BM.targetingmode: #you are selecting a target to attack or use a support skill on.
                    if BM.active_weapon == weapon:
                        $ lbl = hoverglow(weapon.lbl)
                        $ hvr = im.MatrixColor(weapon.lbl,im.matrix.brightness(0.2))
                        $ act = [SetField(BM,'targetingmode',False),SetField(BM,'active_weapon',None),SetField(BM,'weaponhover',None)]
                    else:
                        $ lbl = im.MatrixColor(weapon.lbl,im.matrix.brightness(-0.50))
                        $ hvr = lbl
                        $ hvrd = None
                        $ act = NullAction()

                imagebutton:
                    insensitive insens
                    xpos (x_offset+120*count)
                    ypos (y_offset+69*count)
                    idle lbl
                    hover hvr
                    action act
                    hovered hvrd
                    unhovered unhvrd
                        
                if BM.enable_hotkeys:
                    if act is not None:
                        key str(count+1) action [HoverWeapon(weapon),act,Function(renpy.restart_interaction)]

                  ##show energy cost of weapon on weaponbutton
                text str(-energy_cost) + 'EN':
                    xanchor 0.5
                    yanchor 0.5
                    xpos (x_offset+80+120*count)
                    ypos (y_offset+95+69*count)
                    size 20
                    font "Fonts/SourceCodePro-Regular.ttf"
                    outlines [(1,'000',0,0)]
                python:
                    if not hasattr(weapon,'hp_cost'): weapon.hp_cost = 0
                if weapon.hp_cost > 0:
                    text str(-weapon.hp_cost) + 'HP':
                        xanchor 0.5
                        yanchor 0.5
                        xpos (x_offset+80+120*count)
                        ypos (y_offset+115+69*count)
                        size 20
                        font "Fonts/SourceCodePro-Regular.ttf"
                        outlines [(1,'000',0,0)]

                  ##show ammo available and max_ammo
                if weapon.uses_missiles:
                    text '[[{!s}/{!s}]'.format(BM.selected.missiles,BM.selected.max_missiles):
                        xanchor 0.5
                        yanchor 0.5
                        xpos (x_offset+80+120*count)
                        ypos (y_offset+40+69*count)
                        size 20
                        font "Fonts/SourceCodePro-Regular.ttf"
                        outlines [(1,'000',0,0)]
                if weapon.uses_rockets:
                    text '[[{!s}/{!s}]'.format(BM.selected.rockets,BM.selected.max_rockets):
                        xanchor 0.5
                        yanchor 0.5
                        xpos (x_offset+80+120*count)
                        ypos (y_offset+40+69*count)
                        size 20
                        font "Fonts/SourceCodePro-Regular.ttf"
                        outlines [(1,'000',0,0)]
                
                text str(count+1):
                    xanchor 0.5
                    yanchor 0.5
                    xpos (x_offset+80+120*count) - 33
                    ypos (y_offset+40+69*count) - 30
                    size 16
                    font "Fonts/SourceCodePro-Regular.ttf"
                    outlines [(1,'000',0,0)]
                
                $count += 1    

transform move_vertical(xstart,xend,xx=0):
    #used by skirmish windows
    xpos xstart
    linear 0.5 xpos xend
    on hide:
        linear 0.5 xpos xstart
        time 2 #not sure why this is needed. I'm calling bug in renpy
        alpha 0

screen player_unit_pool_collapsed:
    #this just shows the 'add player units' text and puts a button over it
    zorder 2

    add 'Skirmish/addplayer.png':
        xpos -152

    button:
        background None
        xpos 0
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Show('player_unit_pool')

screen player_unit_pool:
    zorder 3

    if BM.mission == 'skirmish':
        $ frame_background = 'Skirmish/addplayer.png'
    else:
        $ frame_background = 'Skirmish/addplayer_nocmd.png'

    frame:
        background frame_background
        xmaximum 200
        at move_vertical(-152,0)

        viewport:
            # xpos 20
            # ypos 20
            mousewheel True #luckily this viewport eats scrolls above it, so the main one doesn't return it.
            scrollbars "vertical"
            child_size (200,3000)
            area (0, 20, 150, 990)
        
            vbox:
                ypos 200
                spacing 35
                for ship in player_ships:
                    if ship.location == None and ship != BM.selected:
                        
                        # because fuck using consistent image sizes >.>    _sigh_
                        $ y_padding = 0
                        if ship.pilot is None:
                            $ y_padding = 20
                        
                        imagebutton:
                            # yminimum 100
                            # ymaximum 100
                            # ysize 100
                            # xsize 100
                            xpos 60
                            ypos 30
                            # area (0,0,150,200)
                            xysize (150,250)
                            xanchor 0.5
                            yanchor 0.5
                            yfill True
                            at zoom_button(0.2)
                            # ypadding y_padding
                            idle ship.lbl
                            hover hoverglow(ship.lbl)
                            action Return(['selection',ship])

    button:
        background None  # Solid((0,0,0,255)) #for testing
        xpos 152
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Hide('player_unit_pool')

    #experimental.
    if config.developer:
        textbutton "Auto place units":
            xpos 0
            ypos 0.95
            action AutoPlace()
            text_color 'fff'
    
    if BM.mission == 'skirmish':

        text str(BM.cmd):
            xalign 0.5
            xpos 75
            ypos 998
            size 28
            color '000'

        imagebutton:
            xpos 18
            ypos 1038
            idle 'skirmish/increase_cmd.png'
            hover hoverglow('skirmish/increase_cmd.png')
            action SetField( BM , 'cmd' , (BM.cmd + 100) )
            alternate SetField( BM , 'cmd' , (BM.cmd + 1000) )

        imagebutton:
            xpos 80
            ypos 1038
            idle 'skirmish/decrease_cmd.png'
            hover hoverglow('skirmish/decrease_cmd.png')
            action If( BM.cmd <= 100 , SetField(BM,'cmd',0) , SetField(BM,'cmd',(BM.cmd - 100)) )
            alternate If( BM.cmd <= 1000 , SetField(BM,'cmd',0) , SetField(BM,'cmd',(BM.cmd - 1000)) )

screen enemy_unit_pool_collapsed:
    zorder 2

    add 'Skirmish/addenemy.png':
        xpos 1890

    button:
        background None
        xpos 1890
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Show('enemy_unit_pool')

screen enemy_unit_pool:
    zorder 3

    #I will want to put this in a BM field and add new stuff when they get encountered.
    #I think I'll modify the create_ship function to add it automatically if it's not there yet
    $ all_enemies = store.all_enemies

    frame:
        background 'Skirmish/addenemy.png'
        # xalign 1.0
        xmaximum 176
        at move_vertical(1890,1744)

        viewport:
            xpos 20
            ypos 20
            mousewheel True #luckily this viewport eats scrolls above it, so the main one doesn't return it.
            scrollbars "vertical"

            vbox:
                spacing 20

                for ship in all_enemies:
                    imagebutton:
                        at zoom_button(0.15)
                        idle ship.lbl
                        hover hoverglow(ship.lbl)
                        action Return(['selection',ship])

    button:
        background None
        xpos 1738
        ypos 410
        yminimum 250
        ymaximum 250
        xminimum 40
        xmaximum 40
        action Hide('enemy_unit_pool')

screen player_music:
    modal True

    #maybe this list should be defined in the inits
    python:
        music_list = {
            "Driving The Top Down": 'Music/Driving_the_Top_Down.ogg',
            "La Busqueda de Lanna": 'Music/La_Busqueda_de_Lanna.ogg',
            "Overpowered": 'Music/Overpowered.ogg',
            "Powerful": 'Music/Powerful.ogg',
            "Riding With The Wind": 'Music/Riding_With_the_Wind.ogg',
            "The Bladed Druid": 'Music/The_Bladed_Druid.ogg',
            "Titan": 'Music/Titan.ogg',
            }

    add "Skirmish/playermusic_back.png"

    vbox:
        xalign 0.4
        yalign 0.4
        spacing 20

        for song in music_list:

            button:
                xpos 0
                idle_background "Skirmish/song_button.png"
                hover_background hoverglow("Skirmish/song_button.png")
                action [ Hide('player_music'), Return( ["playermusic",music_list[song]] ) ]

                text song:
                    min_width 544   #length of the background. needed for hover
                    xalign 0.5
                    color '000'
                    size 28

screen enemy_music:
    modal True

    python:
        music_list = {
            "Battle Against Time": 'Music/Battle_Against_Time.ogg',
            "Dusty Universe": 'Music/Dusty_Universe.ogg',
            "Intruders": 'Music/Intruders.ogg',
            "Poltergeist Attack": 'Music/Poltergeist_Attack.ogg',
            "Posthumus Regium": 'Music/Posthumus_Regium.ogg',
            "Sui Generis": 'Music/Sui_Generis.ogg',
            "The Departure": 'Music/The_Departure.ogg',
            "The Flight of the Crow": 'music/The_Flight_of_the_Crow.ogg',
            }

    add "Skirmish/enemymusic_back.png"

    vbox:
        xalign 0.4
        yalign 0.4
        spacing 20

        for song in music_list:

            button:
                xpos 0
                idle_background "Skirmish/song_button.png"
                hover_background hoverglow("Skirmish/song_button.png")
                action [ Hide('enemy_music'), Return( ["enemymusic",music_list[song]] ) ]

                text song:
                    min_width 544   #length of the background. needed for hover
                    xalign 0.5
                    color '000'
                    size 28

screen tooltips:
    zorder 9

    #I fear I'll be needing a custom displayable for this eventually

    #grab mouse location
    $ mouse_x,mouse_y = renpy.get_mouse_pos()

    #check if you're hovering over a weapon, tooltips are enabled and you're not currently selecting a target. also buffs now because why not.
    if BM.show_tooltips and ((BM.weaponhover is not None and BM.active_weapon is None) or BM.buffhover is not None):
        if BM.weaponhover is not None:
            $ hovered_object = BM.weaponhover
            $ xposition = -70
            $ x_anchor = 0
            $ xpos_adjustment = 100
        else:
            $ hovered_object = BM.buffhover
            $ xposition = 0
            $ x_anchor = 1.0
            $ xpos_adjustment = -100

        if hovered_object.tooltip != None:
            frame:
                background Solid((0,0,0,200))
                xpos mouse_x + xpos_adjustment
                ycenter mouse_y

                xanchor x_anchor

                if _preferences.language != "spanish":
                    text str(hovered_object.tooltip):
                        xpos xposition #NO IDEA why I can only get things to align right this way.
                        ypos -10
                        size 18
                        font "Fonts/SourceCodePro-Regular.ttf"
                        outlines [(1,'000',0,0)]
                else:
                    text unicode(hovered_object.tooltip_es):
                        xpos 0 #NO IDEA why I can only get things to align right this way.
                        ypos -5
                        size 18
                        font "Fonts/SourceCodePro-Regular.ttf"
                        outlines [(1,'000',0,0)]

transform hp_falls(hp_size1,hp_size2):
    crop (0,0,hp_size1,42)
    linear 1 crop (0,0,hp_size2,42)

transform float_up:
    xpos 0.5
    ypos 0.5
    linear 3 ypos 0.2 alpha 0

screen animation_hp:
    zorder 2
    default damage_delay = 1.0
    timer damage_delay action [Hide('animation_hp'),Show('animation_hp2')]

    add 'Battle UI/dmgstatus.png':
        xalign 1.0

    if store.damage == 'miss':
        $current_hp = BM.target.hp
    else:
        $current_hp = BM.target.hp+ store.damage

    $hp_size1 = int(409*(float(current_hp)/BM.target.max_hp))
    add 'Battle UI/dmgstatus_bar.png':
        xpos 1340
        ypos 3
        crop (0,0,hp_size1,42)
    text 'HP: {!s}/{!s}'.format(current_hp,BM.target.max_hp):
        xpos 1750
        ypos 8
        size 19
        color 'fff'

screen animation_hp2:
    zorder 3

    add 'Battle UI/dmgstatus.png':
        xalign 1.0

    if store.damage == 'miss':
        $damage = 0
        $current_hp = BM.target.hp
    else:
        $damage = store.damage
        $current_hp = BM.target.hp+ store.damage
    $hp_size1 = int(409*(float(current_hp)/BM.target.max_hp))
    $hp_size2 = int(409*(float(current_hp-damage)/BM.target.max_hp))

    add 'Battle UI/dmgstatus_bar.png':
        xpos 1340
        ypos 3
        at hp_falls(hp_size1,hp_size2)

    text 'HP: {!s}/{!s}'.format((current_hp-damage),BM.target.max_hp):
        xpos 1750
        ypos 8
        size 19
        color 'fff'
    text '{!s}'.format(damage):
        xanchor 1.0
        xpos 1670
        ypos 45
        size 40
        color '800'
        outlines [(1,'fff',0,0)]
    text '{!s}'.format(store.hit_count):
        xanchor 1.0
        xpos 1780
        ypos 45
        size 40
        color '800'
        outlines [(1,'fff',0,0)]
    text '{!s}'.format(-damage):
        xanchor 0.5
        at float_up
        size 30
        color '800'
        outlines [(1,'fff',0,0)]

    vbox:
        xalign 1.0
        ypos 0.2

        # moved shield to before armor since it is applied first
        if store.total_shield_negation > 0:
            text ( '{image=Battle UI/icon_shield.png} ' + '-{} dmg'.format(int(store.total_shield_negation)) ):
                xalign 1.0
                xoffset -32
                size 32
                color '6bf'
                outlines [(1,'000',0,0)]
        if store.total_armor_negation > 0:
            text ( '{image=Battle UI/icon_armor.png} ' + '-{} dmg'.format(int(store.total_armor_negation)) ):
                xalign 1.0
                xoffset -32
                size 32
                color 'fff'
                outlines [(1,'000',0,0)]

        if hasattr(store,'total_flak_interception') and store.total_flak_interception > 0:
            text ( '{image=Battle UI/icon_intercept.png} ' + '{} intercepts'.format(int(store.total_flak_interception)) ):
                xalign 1.0
                xoffset -32
                size 32
                color 'fa6'
                outlines [(1,'000',0,0)]

transform victory_tf(xx,wait):
    alpha 0
    ypos 0
    xpos (xx+500)
    zoom 20
    time wait
    linear 0.5 alpha 1 xpos xx ypos 242 zoom 1
    time (1+wait)
    linear 0.5 ypos -100 alpha 0

screen victory:
#    modal True
    if _preferences.language != "spanish":
        $word = 'Victory!'
    else:
        $word = '¡Victoria!'
    $wait = 0.22
    $xx = 750

    add Solid((0,0,0,200))

    for letter in word:
        text letter:
            xanchor 0.5
            size 150
            color 'fff'
            outlines [(4,'000',0,0)]
            at victory_tf(xx,wait)

        $wait += 0.2
        $xx += 75

transform victory_ships(xx,wait,zz):
    alpha 0
    ypos 0
    xpos (xx+500)
    zoom 20
    time wait
    linear 0.5 alpha 1 xpos xx ypos 350 zoom zz

transform delay_text(wait):
    alpha 0
    time wait
    linear 1 alpha 1

screen victory2:
    modal True
    $wait = 0.2
    $xx = 200

    add Solid((0,0,0,200))

    if _preferences.language != "spanish":
        textbutton 'Continue':
            xalign 0.5
            ypos 0.8
            text_size 30
            action Hide('victory2')
            text_color 'fff'

        text 'Destroyed enemy ships:':
            xpos 0.2
            ypos 0.2
            size 50
            outlines [(2,'000',0,0)]

    else:
        textbutton 'Continuar':
            xalign 0.5
            ypos 0.8
            text_size 30
            action Hide('victory2')
            text_color 'fff'

        text 'Naves enemigas destruidas:':
            xpos 0.2
            ypos 0.2
            size 50
            outlines [(2,'000',0,0)]

    $ textsize = 50
    if len(destroyed_ships) > 12:
        $ textsize = 40
    elif len(destroyed_ships) > 20:
        $ textsize = 30

    $ total_ships = len(destroyed_ships)
    if store.boss_killed:
        $ total_ships += len(enemy_ships)

    $total_wait_time = len(destroyed_ships) * 0.2
    if total_wait_time > 3.0:
        $ total_wait_time = 3.0
    if len(destroyed_ships) > 0:
        $ wait_time = total_wait_time / len(destroyed_ships)
    else:
        $ wait_time = 0

    for ship in destroyed_ships:
        if not ship.faction == 'Player':
            add ship.blbl:
                xanchor 0.5
                at victory_ships(xx,wait,0.5)
            text '{}$'.format(int(ship.money_reward)):
                xanchor 0.5
                yanchor 1.0
                size textsize
                outlines [(2,'000',0,0)]
                at victory_ships(xx,wait,1)

            $ wait += wait_time

            $xx += 1520/total_ships

    if store.boss_killed:
        for ship in enemy_ships:
            add ship.blbl:
                xanchor 0.5
                at victory_ships(xx,wait,0.5)
            if _preferences.language != "spanish":
                text 'Surrendered':
                    xanchor 0.5
                    yanchor 1.0
                    color '090'
                    size textsize - 15
                    outlines [(2,'000',0,0)]
                    at victory_ships(xx,wait,1)
            else:
                text 'Rendida':
                    xanchor 0.5
                    yanchor 1.0
                    color '090'
                    size textsize - 15
                    outlines [(2,'000',0,0)]
                    at victory_ships(xx,wait,1)

            $wait += 0.3
            $xx += 1520/total_ships

    $wait += 0.5
    if _preferences.language != "spanish":
        text 'Enemy destruction reward: {}$'.format(int(store.total_money)):
            xpos 0.2
            ypos 0.6
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
    else:
        text 'Recompensa por enemigos destruidos: {}$'.format(int(store.total_money)):
            xpos 0.2
            ypos 0.6
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)

    $ yposition = 0.65
    if store.surrender_bonus > 0:
        $wait += 0.1
        if _preferences.language != "spanish":
            text 'Surrender bonus: {}$'.format(int(store.surrender_bonus)):
                xpos 0.2
                ypos yposition
                size 40
                outlines [(2,'000',0,0)]
                at delay_text(wait)
        else:
            text 'Bonus por rendición: {}$'.format(int(store.surrender_bonus)):
                xpos 0.2
                ypos yposition
                size 40
                outlines [(2,'000',0,0)]
                at delay_text(wait)
        $ yposition += 0.05


    $wait += 0.1
    if _preferences.language != "spanish":
        text 'Repair costs: {}$'.format(int(store.repair_cost)):
            xpos 0.2
            ypos yposition
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
    else:
        text 'Costos por reparaciones: {}$'.format(int(store.repair_cost)):
            xpos 0.2
            ypos yposition
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
    $ yposition += 0.05

    $net_gain_modifier = 1
    if store.Difficulty == 5:
        $wait += 0.1
        $net_gain_modifier = 0.8
        if _preferences.language != "spanish":
            text 'Space Whale tax: {}$'.format(int(store.net_gain * 0.2)):
                xpos 0.2
                ypos yposition
                size 40
                outlines [(2,'000',0,0)]
                at delay_text(wait)
        else:
            text 'Impuesto por Ballena Espacial: {}$'.format(int(store.net_gain * 0.2)):
                xpos 0.2
                ypos yposition
                size 40
                outlines [(2,'000',0,0)]
                at delay_text(wait)
        $ yposition += 0.05

    $wait += 0.1
    if _preferences.language != "spanish":
        text 'Net gain: {}$'.format(int(store.net_gain*net_gain_modifier)):
            xpos 0.2
            ypos yposition
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
    else:
        text 'Ganancia neta: {}$'.format(int(store.net_gain*net_gain_modifier)):
            xpos 0.2
            ypos yposition
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)

    $wait += 0.5
    
    # defunct as command points are no longer received at end of turn
    if _preferences.language != "spanish":
        text 'Intel gathered: {}'.format(store.intel_gain):
            xanchor 1.0
            xpos 0.8
            ypos 0.6
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)
    else:
        text 'Intel conseguido: {}'.format(store.intel_gain):
            xanchor 1.0
            xpos 0.8
            ypos 0.6
            size 40
            outlines [(2,'000',0,0)]
            at delay_text(wait)

    # $wait += 0.1
    # text 'Número de turnos: {}'.format(BM.turn_count):
        # xanchor 1.0
        # xpos 0.8
        # ypos 0.65
        # size 40
        # outlines [(2,'000',0,0)]
        # at delay_text(wait)

    # $wait += 0.1

    # $ difficulty_penalty = store.Difficulty - 1
    # if difficulty_penalty < 0:
        # $ difficulty_penalty = 0

    # text 'command points received: {}'.format( int( (store.net_gain*10)/(BM.turn_count+difficulty_penalty) ) ):
        # xanchor 1.0
        # xpos 0.8
        # ypos 0.70
        # size 40
        # outlines [(2,'000',0,0)]
        # at delay_text(wait)

    if _preferences.language != "spanish":
        $ diff_text = "Current dificulty: {}".format( DIFFICULTY_NAMES[store.Difficulty] )
        $ low_diff_text = "Lowest dificulty: {}".format( DIFFICULTY_NAMES[BM.lowest_difficulty] )
    else:
        $ diff_text = "Dificultad actual: {}".format( DIFFICULTY_NAMES[store.Difficulty] )
        $ low_diff_text = "Menor dificultad: {}".format( DIFFICULTY_NAMES[BM.lowest_difficulty] )
        

    vbox:
        xalign 1.0
        yalign 1.0

        text diff_text:
            size 12
            xalign 1.0
        text low_diff_text:
            size 12
            xalign 1.0

transform message_transform(x,y):
    # These control the position.
    xalign x yalign y
    # These control the actions on show and hide.
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

screen message:
    zorder 50
    text message:
        at message_transform(xpos,ypos)
        size 24
        color 'fff'
        outlines [(2,'000',0,0)]

    timer 3.25 action Hide('message')

screen mousefollow:
    zorder 10
    if BM.selected == None:
        $ follow_image = sunrider.lbl
    else:
        $ follow_image = BM.selected.lbl

    $ follow_image = im.Rotozoom(follow_image,0,0.25)
#    $ follow_image = im.matrix(follow_image).opacity(0.4)
    add MouseFollow(follow_image):
        alpha 0.7

screen ryderlist:
    zorder 3
    modal True

    key "mousedown_3" action Return(["deselect"])

    if _preferences.language == "spanish":
        text 'Selecciona cuál Ryder reparar':
                xalign 0.5
                yalign 0.1
                size 40
                outlines [(2,'000',0,0)]
    else:
        text 'Choose which Ryder to repair':
                xalign 0.5
                yalign 0.1
                size 40
                outlines [(2,'000',0,0)]


    frame:
        xalign 0.5
        ypos 0.2
        xminimum 400
        xmaximum 400
        yminimum 300
        ymaximum 800
        background Solid((0,0,0,200))

        $ count = 0
        for iconship in destroyed_ships:
            if iconship.faction == 'Player' and not iconship.mercenary and iconship.stype == 'Ryder':
                $ icon = None
                $ hovericon = None
                $ xposition = 50
                if count % 2 != 0:
                    $ xposition = 168
                $ yposition = 20 + count * 70

                #this is the sort of mess you get if you don't put this stuff in the library
                if iconship.name == 'Sunrider':
                    $ icon = 'Menu/upgrade_sunrider_button.png'
                    $ hovericon = 'Menu/upgrade_sunrider_button_hover.png'
                elif iconship.name == 'Liberty':
                    $ icon = 'Menu/upgrade_liberty_button.png'
                    $ hovericon = 'Menu/upgrade_liberty_button_hover.png'
                elif iconship.name == 'Black Jack':
                    $ icon = 'Menu/upgrade_blackjack_button.png'
                    $ hovericon = 'Menu/upgrade_blackjack_button_hover.png'
                elif iconship.name == 'Havoc':
                    $ icon = 'Menu/upgrade_havoc_button.png'
                    $ hovericon = 'Menu/upgrade_havoc_hover.png'
                elif iconship.name == 'Phoenix':
                    $ icon = 'Menu/upgrade_phoenix_button.png'
                    $ hovericon = 'Menu/upgrade_phoenix_button_hover.png'
                elif iconship.name == 'Seraphim':
                    $ icon = 'Menu/upgrade_seraphim_button.png'
                    $ hovericon = 'Menu/upgrade_seraphim_hover.png'
                elif iconship.name == 'Bianca':
                    $ icon = 'Menu/upgrade_bianca_button.png'
                    $ hovericon = 'Menu/upgrade_bianca_hover.png'
                elif iconship.name == 'Paladin':
                    $ icon = 'Menu/upgrade_paladin_button.png'
                    $ hovericon = 'Menu/upgrade_paladin_button_hover.png'

                imagebutton:
                    xpos xposition
                    ypos yposition
                    action Return( ['selection',iconship] )
                    idle icon
                    hover hovericon
                    focus_mask True

                $ count += 1

screen skirmishhelp:

    frame:
        xalign 0.5
        ypos 0.2
        xminimum 600
        # xmaximum 600
        yminimum 300
        ymaximum 800
        background Solid((0,0,0,200))

        vbox:
            text "Welcome to skirmish mode! Here, you will be able to refine your strategies by fighting custom battles."
            text "Click on ADD PLAYER SHIPS and click and drop your units to the map. Do the same to add enemy units."
            text "Pressing SHIFT allows you to add the selected unit multiple times to the map."
            text "Pressing the MIDDLE MOUSE BUTTON allows you to instantly grab the next player unit from the player pool."
            text "To remove placed units, simply press the REMOVE button, then click on the unit you wish to remove."
            text "You may set the amount of usable command points during the battle using the buttons on the player pool bar."
            text "Additionally, you can freely try out all possible upgrades by clicking the blue upgrades button."
            text "Keep in mind that you will {b}not{/b} earn any money or command points in Skirmish Mode!"

            textbutton "PROCEED":
                xalign 0.5
                action Hide('skirmishhelp')

screen battle_log():
    default filter_all      = True
    default filter_system   = True
    default filter_order    = True
    default filter_attack   = True
    default filter_kinetic  = True
    default filter_laser    = True
    default filter_missile  = True
    default filter_melee    = True
    default filter_details  = False
    default filter_support  = True
    default filter_heal     = True
    default filer_buff      = True
    default filter_debuff   = True
    default log_tags        = set(['all', 'system', 'player', 'enemy', 'order', 'attack', 'detailed', 'laser', 'kinetic', 'missile', 'melee', 'support', 'heal', 'buff', 'debuff'])
    drag:
        xalign 1.0
        yalign 0.0
        frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            ypos 0.2
            xminimum 800
            xmaximum 900
            yminimum 100
            ymaximum 400
            background Solid((0,0,0,200))
            vbox:
                hbox:
                    xfill True
                    hbox:
                        # re-evaluation should update filter_all in case if all other are enabled
                        if filter_system and filter_attack and filter_details and filter_support and filter_order:
                            $filter_all = True
                        else:
                            $filter_all = False
                        label "Filters:":
                            right_padding 10
                        textbutton "all":
                            action If(filter_all, true=[ToggleScreenVariable("filter_all"),
                                                        SetScreenVariable("filter_system", False),
                                                        SetScreenVariable("filter_attack", False),
                                                        SetScreenVariable("filter_laser", False),
                                                        SetScreenVariable("filter_kinetic", False),
                                                        SetScreenVariable("filter_missile", False),
                                                        SetScreenVariable("filter_melee", False),
                                                        SetScreenVariable("filter_details", False),
                                                        SetScreenVariable("filter_support", False),
                                                        SetScreenVariable("filter_heal", False),
                                                        SetScreenVariable("filter_buff", False),
                                                        SetScreenVariable("filter_debuff", False),
                                                        SetScreenVariable("filter_order", False),
                                                        SelectedIf(filter_all)],
                                                 false=[ToggleScreenVariable("filter_all"),
                                                        SetScreenVariable("filter_system", True),
                                                        SetScreenVariable("filter_attack", True),
                                                        SetScreenVariable("filter_laser", True),
                                                        SetScreenVariable("filter_kinetic", True),
                                                        SetScreenVariable("filter_missile", True),
                                                        SetScreenVariable("filter_melee", True),
                                                        SetScreenVariable("filter_details", True),
                                                        SetScreenVariable("filter_support", True),
                                                        SetScreenVariable("filter_heal", True),
                                                        SetScreenVariable("filter_buff", True),
                                                        SetScreenVariable("filter_debuff", True),
                                                        SetScreenVariable("filter_order", True),
                                                        SelectedIf(filter_all)])
                        textbutton "system":
                            action [ToggleScreenVariable("filter_system")]
                        textbutton "order":
                            action [ToggleScreenVariable("filter_order")]
                        if filter_attack:
                            textbutton "attack":
                                action [ToggleScreenVariable("filter_attack"),
                                        SetScreenVariable("filter_laser", True),
                                        SetScreenVariable("filter_kinetic", False),
                                        SetScreenVariable("filter_missile", False),
                                        SetScreenVariable("filter_melee", False),
                                        SelectedIf(filter_attack)]
                        elif filter_laser:
                            textbutton "laser":
                                action [ToggleScreenVariable("filter_laser"), ToggleScreenVariable("filter_kinetic"), SelectedIf(filter_laser)]
                        elif filter_kinetic:
                            textbutton "kinetic":
                                action [ToggleScreenVariable("filter_kinetic"), ToggleScreenVariable("filter_missile"), SelectedIf(filter_kinetic)]
                        elif filter_missile:
                            textbutton "missile":
                                action [ToggleScreenVariable("filter_missile"), ToggleScreenVariable("filter_melee"), SelectedIf(filter_missile)]
                        elif filter_melee:
                            textbutton "melee":
                                    action [ToggleScreenVariable("filter_melee")]
                        else: #means attack is not selected
                            textbutton "attack":
                                action [ToggleScreenVariable("filter_attack"),
                                        SetScreenVariable("filter_laser", True),
                                        SetScreenVariable("filter_kinetic", True),
                                        SetScreenVariable("filter_missile", True),
                                        SetScreenVariable("filter_melee", True),
                                        SelectedIf(filter_attack)]
                        if filter_support:
                            textbutton "support":
                                action [ToggleScreenVariable("filter_support"),
                                        SetScreenVariable("filter_heal", True),
                                        SetScreenVariable("filter_buff", False),
                                        SetScreenVariable("filter_debuff", False),
                                        SelectedIf(filter_support)]
                        elif filter_heal:
                            textbutton "heal":
                                action [ToggleScreenVariable("filter_heal"), ToggleScreenVariable("filter_buff"), SelectedIf(filter_heal)]
                        elif filter_buff:
                            textbutton "buff":
                                action [ToggleScreenVariable("filter_buff"), ToggleScreenVariable("filter_debuff"), SelectedIf(filter_buff)]
                        elif filter_debuff:
                            textbutton "debuff":
                                    action [ToggleScreenVariable("filter_debuff")]
                        else: #means that support is not selected
                            textbutton "support":
                                action [ToggleScreenVariable("filter_support"),
                                        SetScreenVariable("filter_heal", True),
                                        SetScreenVariable("filter_buff", True),
                                        SetScreenVariable("filter_debuff", True),
                                        SelectedIf(filter_support)]
                        textbutton "details":
                            action [ToggleScreenVariable("filter_details")]

                    textbutton "X":
                        xalign 1.0
                        action [Hide('battle_log'), SetField(BM, 'show_battle_log', False)]

                side "c r":
                    viewport:
                        id 'battle log'
                        xmaximum 900
                        yinitial 1.0
                        yadjustment BM.battle_log_yadj
                        mousewheel True

                        vbox:
                            #if flag all is true then all tags are enabled
                            if filter_all:
                                $log_tags = set(['all', 'system', 'player', 'enemy', 'order', 'attack', 'detailed', 'laser', 'kinetic', 'missile', 'melee', 'support', 'heal', 'buff', 'debuff'])
                            else:
                                #otherwise we check which tags should be enabled
                                $log_tags = set([])
                                if filter_system:
                                    $log_tags.add('system')
                                if filter_order:
                                    $log_tags.add('order')
                                if filter_attack:
                                    $log_tags.update(set(['attack', 'laser', 'kinetic', 'missile', 'melee']))
                                else:
                                    if filter_laser:
                                        $log_tags.add('attack')
                                        $log_tags.add('laser')
                                    if filter_kinetic:
                                        $log_tags.add('attack')
                                        $log_tags.add('kinetic')
                                    if filter_missile:
                                        $log_tags.add('attack')
                                        $log_tags.add('missile')
                                    if filter_melee:
                                        $log_tags.add('attack')
                                        $log_tags.add('melee')
                                if filter_details:
                                    $log_tags.add('detailed')
                                if filter_support:
                                    $log_tags.update(set(['support', 'heal', 'buff', 'debuff']))
                                else:
                                    if filter_heal:
                                        $log_tags.add('support')
                                        $log_tags.add('heal')
                                    if filter_buff:
                                        $log_tags.add('support')
                                        $log_tags.add('buff')
                                    if filter_debuff:
                                        $log_tags.add('support')
                                        $log_tags.add('debuff')
                            for type, entry in BM.battle_log:
                                #To be printed log's tags should contain tags which are stored in filter
                                if log_tags.issuperset(set(type)):
                                    text entry

                    vbar:
                        value YScrollValue('battle log')
                        hovered SetField(BM, 'draggable', False)
                        unhovered SetField(BM, 'draggable', True)

transform gameovergimmick(x,y,t):
    # These control the position.
    xpos x ypos y
    easeout t xpos -0.1
    block:
        xpos 1.0
        easeout t xpos -0.1
        repeat

screen game_over_gimmick:
    zorder 50

    if BM.battlemode:
        for a in range(80):
            $randint = renpy.random.randint(50,150)
            $randx = renpy.random.random()
            $randy = renpy.random.random()
            $randt = renpy.random.randint(100,600) / 100.0
    #        text 'Game Over!' xpos randx ypos randy size randint at gameovergimmick(randx,randy, randt)
            add 'Battle UI/label_pactbattleship.png' xpos randx ypos randy zoom (randint / 300.0) at gameovergimmick(randx,randy, randt)

screen debug_window:
    zorder 100
    # modal True

    drag:
        xalign 0.5
        ypos 0.2
        frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            ypos 0.2
            xminimum 800
            xmaximum 900
            yminimum 100
            ymaximum 400
            background Solid((0,0,0,200))

            vbox:
                hbox:
                    xfill True
                    label 'debug log'
                    textbutton 'clear':
                        xalign 1.0
                        action SetField(BM,'debug_log',[])
                    textbutton "X":
                        xalign 1.0
                        action Hide('debug_window')

                side "c r":
                    viewport:
                        id 'debug log'
                        yinitial 1.0
                        vbox:
                            for entry in BM.debug_log:
                                text str(entry)
                    vbar:
                        value YScrollValue('debug log')
                        hovered SetField(BM, 'draggable', False)
                        unhovered SetField(BM, 'draggable', True)


screen debug_pships:
    #show a list all all player ships and as much relevant data about them as possible. useful for tracing weird behaviour. maybe.
    zorder 100
    drag:
        xalign 0.5
        ypos 0.2
        frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            ypos 0.2
            xmaximum 400
            ymaximum 600
            background Solid((0,0,0,200))
            vbox:
                textbutton "X":
                    xalign 1.0
                    action Hide('debug_pships')
                side "c r":
                    viewport:
                        id 'debug pship list'
                        yinitial 0
                        mousewheel True

                        vbox:
                            for pship in player_ships:
                                text pship.name size 12
                                vbox:
                                    xpos 20
                                    for entry in pship.__dict__:
                                        $ data = getattr(pship,entry)
                                        if not type(data) is dict and not type(data) is list:  #renpy can't deal with those at all
                                            text str(entry)+ ' : ' + str(data) size 12

                    vbar:
                        value YScrollValue('debug pship list')
                        hovered SetField(BM, 'draggable', False)
                        unhovered SetField(BM, 'draggable', True)

screen debug_eships:
    zorder 100
    drag:
        xalign 0.5
        ypos 0.2
        frame:
            xpadding 10
            ypadding 10
            xalign 0.5
            ypos 0.2
            xmaximum 400
            ymaximum 600
            background Solid((0,0,0,200))
            vbox:
                textbutton "X":
                    xalign 1.0
                    action Hide('debug_eships')
                side "c r":
                    viewport:
                        id 'debug eship list'
                        yinitial 0
                        mousewheel True

                        vbox:
                            for eship in enemy_ships:
                                text eship.name size 12
                                vbox:
                                    xpos 20
                                    for entry in eship.__dict__:
                                        $ data = getattr(eship,entry)
                                        if not type(data) is dict and not type(data) is list:
                                            text str(entry)+ ' : ' + str(data) size 12

                    vbar:
                        value YScrollValue('debug eship list')
                        hovered SetField(BM, 'draggable', False)
                        unhovered SetField(BM, 'draggable', True)
                        
screen bad_end_options:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        ypos 0.75

        vbox:
            xalign 0.5
            style "menu"
            spacing 2
            ypos 0.75

            textbutton "Try Again":
                action Jump('tryagain')
                xalign 0.5
                
            textbutton "Load Saved Game":
                action Jump ('loadsavedgame')
                xalign 0.5
                
screen gallery_achievements():
    zorder 1500
    tag page
    
    $achievement_count = len(persistent.achievements)
    $rowcount = (achievement_count /3) + (1 if achievement_count%3!=0 else 0)
    
    frame:
        area (245,265,980,700)
        background Solid((0,0,0,200))
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            # child_size (920,1386)
            
            grid 3 rowcount:
                
                xfill True
                yfill False
                
                $hidden_chivos = 0
                for chivo in persistent.achievements:
                    $achievement = persistent.achievements[chivo]
                    if not achievement.hidden:
                        vbox:
                            hbox:
                                $text_colour = '080' if achievement.cleared else 'fff'
                                add "Chivos/" + achievement.icon zoom 0.75
                                text achievement.name color text_colour size 22
                            $attr_text = 'by: '+achievement.attribution+'\n' if achievement.attribution is not None else ''
                            if achievement.stat_max is not None:
                                if achievement.tracked_value <= achievement.stat_max:
                                    text str(achievement.tracked_value) size 14 xpos int(achievement.tracked_value/float(achievement.stat_max) * 300)
                                bar:
                                    value achievement.tracked_value
                                    range achievement.stat_max
                            text attr_text + achievement.description size 18
                    else:
                        $hidden_chivos += 1
                
                $remaining_slots = 3*rowcount - len(persistent.achievements)
                for a in range(remaining_slots+hidden_chivos):
                    hbox:
                        text '' #placeholder
                
transform tr_chivotoast():
    yalign 1.0
    xpos 1920
    ease 1 xpos 1920 - 350
    pause 2
    ease 1 xpos 1920
                
screen achievement_toast(achievement):
    zorder 1000
    
    timer 240 repeat False action Hide('achievement_toast')
    
    frame:
        at tr_chivotoast
        background Solid((0,0,0,200))
        vbox:
            text "ACHIEVEMENT UNLOCKED!"
            hbox:
                add "Chivos/" + achievement.icon
                text achievement.name
                
# screen find_sprite():
    # default character = None
    # default posture = None
    
    # modal True
    
    # textbutton "return":
        # action [SetScreenVariable('character',None),SetScreenVariable('posture',None)]
        # xalign 0.5
        # yalign 0.0
    # key 'r':
        # action [SetScreenVariable('character',None),SetScreenVariable('posture',None)]
    
    # frame:
        # xalign 0.5
        # ypos 50
        # if character is None:
            # vpgrid:
                # cols 9
                # side_align 0.5
                # for i in range(9):
                    # if not i == 6:
                        # $sprite_name = get_sprite_combination(i*10000)
                        # if sprite_name in store.sprites:
                            # $displayable_sprite = store.sprites[sprite_name]
                            # imagebutton:
                                # idle Transform(displayable_sprite,zoom = 0.2)
                                # hover Transform(displayable_sprite,zoom = 0.2)
                                # action SetScreenVariable("character",i)
                            # key str(i+1):
                                # action SetScreenVariable("character",i)
        
        # if character is not None and posture is None:
            # vpgrid:
                # cols 9
                # side_align 0.5
                # draggable True
                # mousewheel True
                # for i in range(get_posture_count(character)):
                    # $sprite_name = get_sprite_combination(character*10000+i*1000)
                    # imagebutton:
                        # idle Transform(store.sprites[sprite_name],zoom = 0.2)
                        # hover Transform(store.sprites[sprite_name],zoom = 0.2)
                        # action SetScreenVariable("posture",i)
                    # if i+1 < 10:
                        # key str(i+1):
                            # action SetScreenVariable("posture",i)
                        
        # if character is not None and posture is not None:
            # vpgrid:
                # cols 6
                # draggable True
                # mousewheel True
                # side_align 0.5
                # for mouth_index in range(9):
                    # for eye_index in range(9):
                        # for eyebrow_index in range(9):
                            # $sprite_index = character*10000+posture*1000+mouth_index*100+eye_index*10+eyebrow_index
                            # $sprite_name = get_sprite_combination(sprite_index)
                            # if sprite_name in store.sprites:
                                # $displayable_sprite = store.sprites[sprite_name]
                                # $cropheight = 150 if character == 0 and posture == 3 else 0
                                # vbox:
                                    # add LiveCrop((0,cropheight,300,300) , Transform(displayable_sprite,zoom = 0.4))
                                    # text str(sprite_index):
                                        # ypos -200
                                        # outlines [(1,'000',0,0)]
                        
    