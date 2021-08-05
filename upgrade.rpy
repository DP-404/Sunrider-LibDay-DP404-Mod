screen upgrade:
    modal True
    zorder 101 #the say screen is 100 so this is just on top
    
    key "mousedown_4" action NullAction()

    if BM.selected is None:
        $ BM.selected = player_ships[0]
    $ ship = BM.selected
    
    default xadj = ui.adjustment()
    default yadj = ui.adjustment()
    
    if ship.name == "Sunrider":
        if store.legion_destroyed:
            add "upgrade/back_ava_eyepatch.jpg"
        else:
            add "upgrade/back_ava.jpg"
    elif ship.name == "Black Jack":
        add "upgrade/back_asaga.jpg"
    elif ship.name == "Phoenix":
        add "upgrade/back_phoenix.jpg"
    elif ship.name == "Liberty":
        add "upgrade/back_chigara.jpg"
    elif ship.name == "Paladin":
        add "upgrade/back_kryska.jpg"
    elif ship.name == "Seraphim":
        add "upgrade/back_sola.jpg"
    elif ship.name == "Bianca":
        add "upgrade/back_claude.jpg"        
        
    vbox:
        xalign 1.0 
        imagebutton:
            action Return(["return",None])
            idle "upgrade/button_return.png"
            hover hoverglow("upgrade/button_return.png")
        imagebutton:
            action Return(["store",None])
            idle "upgrade/button_store.png"
            hover hoverglow("upgrade/button_store.png")

    $ can_use_melee = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Melee':
            $ can_use_melee = True
    $ uses_kinetics = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Kinetic' or weapon.wtype == 'Assault':
            $ uses_kinetics = True
    $ uses_lasers = False
    for weapon in ship.weapons:
        if weapon.wtype == 'Laser' or weapon.wtype == 'Pulse':
            $ uses_lasers = True
    #dictionaries are inherently unsorted, so this is needed ;_;
    
    $ upgrade_list = []
    # $ upgrade_list.append(["BASIC -----------",None,None,None,None])
    $ upgrade_list.append(ship.upgrades['max_hp'])
    $ upgrade_list.append(ship.upgrades['max_en'])
    $ upgrade_list.append(ship.upgrades['evasion'])
#    $ upgrade_list.append(ship.upgrades['move_cost'])  #probably should be set individually in design

    if uses_kinetics:
        $ upgrade_list.append(["",None,None,None,None])
        if _preferences.language == "spanish":
            $ upgrade_list.append(["KINÉTICO",None,None,None,None])
        else:
            $ upgrade_list.append(["KINETIC",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['kinetic_dmg'])
        $ upgrade_list.append(ship.upgrades['kinetic_acc'])
        $ upgrade_list.append(ship.upgrades['kinetic_cost'])

    if uses_lasers:
        $ upgrade_list.append(["",None,None,None,None])
        if _preferences.language == "spanish":
            $ upgrade_list.append(["ENERGÍA",None,None,None,None])
        else:
            $ upgrade_list.append(["ENERGY",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['energy_dmg'])
        $ upgrade_list.append(ship.upgrades['energy_acc'])
        $ upgrade_list.append(ship.upgrades['energy_cost'])

    if ship.max_missiles > 0:
        $ upgrade_list.append(["",None,None,None,None])
        if _preferences.language == "spanish":
            $ upgrade_list.append(["MISILES",None,None,None,None])
        else:
            $ upgrade_list.append(["MISSILE",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['missile_dmg'])
        $ upgrade_list.append(ship.upgrades['missile_eccm'])
        $ upgrade_list.append(ship.upgrades['missile_cost'])
        $ upgrade_list.append(ship.upgrades['max_missiles'])

    if can_use_melee:
        $ upgrade_list.append(["",None,None,None,None])
        $ upgrade_list.append(["MELEE",None,None,None,None])
        $ upgrade_list.append(ship.upgrades['melee_dmg'])
        $ upgrade_list.append(ship.upgrades['melee_acc'])
        $ upgrade_list.append(ship.upgrades['melee_cost'])

    $ upgrade_list.append(["",None,None,None,None])
    if _preferences.language == "spanish":
        $ upgrade_list.append(["DEFENSA",None,None,None,None])
    else:
        $ upgrade_list.append(["DEFENSE",None,None,None,None])

    if ship.shield_generation > 0:
        $ upgrade_list.append(ship.upgrades['shield_generation'])
        $ upgrade_list.append(ship.upgrades['shield_range'])

    if ship.flak > 0:
        $ upgrade_list.append(ship.upgrades['flak'])

    $ upgrade_list.append(ship.upgrades['base_armor'])

    if ship.repair > 0:
        $ upgrade_list.append(ship.upgrades['repair'])

    # Upgrade backgrounds moved to their individual classes in the library
    # add ship.upgrade_menu

    $ funds_text = '{!s}'.format(BM.intel) if BM.mission!='skirmish' else 'ILIMITADO'
    text funds_text:
        size 50
        xanchor 0.5
        yanchor 0.5
        xpos 1464
        ypos 37
        color 'fff'
        outlines [(4,'000',0,0)]

    ## show icons of all the player ships in player_ships
    $ count = 0
    $ xposition = 80  
    for iconship in player_ships:
        if not iconship.mercenary:
            ## upgrade icons and hovericons are now in the library
            $ icon = iconship.icon
            $ hovericon = iconship.hovericon
            $ yposition = 180 + count * 64

            imagebutton:
                xpos xposition
                ypos yposition
                action [ SetField(BM,'selected',iconship) , Play('sound1','Sound/research_changeunit.ogg') , SetField(yadj,'value',0) ]
                idle icon
                hover hovericon
                focus_mask True

            $ count += 1
            
            
    ## STATS window
    text ship.pilot.upper():
        xalign 0.5
        xpos 156
        ypos 678
        outlines [(2,'000',0,0)]
        size 24
    text str(ship.max_hp):
        xalign 0.5
        xpos 156
        ypos 728
        outlines [(2,'000',0,0)]
        size 24   
    text str(ship.max_en):
        xalign 0.5
        xpos 156
        ypos 778
        outlines [(2,'000',0,0)]
        size 24 
    text str(ship.move_cost):
        xalign 0.5
        xpos 156
        ypos 830
        outlines [(2,'000',0,0)]
        size 24  
    text str(ship.evasion):
        xalign 0.5
        xpos 156
        ypos 882
        outlines [(2,'000',0,0)]
        size 24
    text str(ship.base_armor):
        xalign 0.5
        xpos 156
        ypos 934
        outlines [(2,'000',0,0)]
        size 24
    text str(ship.flak):
        xalign 0.5
        xpos 156
        ypos 984
        outlines [(2,'000',0,0)]
        size 24
    
    text ship.__class__.__name__.upper(): #take the class of the instance, take its name and then capitalize it. methodception. fuck I love OOP
        xpos 253
        ypos 680
        outlines [(2,'000',0,0)]
        size 24 
        

                
            
    $stats_kinetic = "NA"
    $stats_assault = "NA"
    $stats_laser = "NA"
    $stats_pulse = "NA"
    $stats_missile = "NA"
    $stats_torpedo = "NA"
    $stats_melee = "NA"
        
    for weapon in ship.weapons:
        if weapon.wtype == "Kinetic":
            $stats_kinetic = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count),str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]
        elif weapon.wtype == "Assault":
            $stats_assault = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count),str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]
        elif weapon.wtype == "Laser":
            $stats_laser = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count),str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]
        elif weapon.wtype == "Pulse":
            $stats_pulse = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count),str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]
        elif weapon.wtype == "Missile":
            $stats_missile = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count)+' ('+str(BM.selected.max_missiles)+'max)',str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]
        elif weapon.wtype == "Rocket":
            $stats_torpedo = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count)+' ('+str(BM.selected.max_rockets)+'max)',str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]
        elif weapon.wtype == "Melee":
            $stats_melee = [ str(get_modified_weapon_damage(weapon))+'x'+str(weapon.shot_count)+'='+str(get_modified_weapon_damage(weapon)*weapon.shot_count),str(get_modified_accuracy(weapon)),str(weapon.energy_cost(ship)) ]

    $stats_weapons = [ stats_kinetic,stats_assault,stats_laser,stats_pulse,stats_missile,]
    if stats_melee != "NA":
        $stats_weapons.append(stats_melee)
    else:
        $stats_weapons.append(stats_torpedo)
    
    $count = 0
    $xposition = 283
    $yposition = 733
    $y_increment = 51
    for sweapon in stats_weapons:
        if type(sweapon) is str:
            text sweapon:
                xpos xposition
                ypos yposition + count * y_increment
                outlines [(2,'000',0,0)]
                size 24
        else:
            $a,b,c = sweapon
            text a:
                xpos xposition-30
                ypos yposition + count * y_increment
                outlines [(2,'000',0,0)]
                size 24 
            text b:
                xpos xposition + 180
                ypos yposition + count * y_increment
                outlines [(2,'000',0,0)]
                size 24                 
            text c:
                xpos xposition + 260
                ypos yposition + count * y_increment
                outlines [(2,'000',0,0)]
                size 24                         
        $count += 1

    vbox:
        area (684, 205, 390, 580)

        viewport id "upgrade_list":
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (150,2000)
            xadjustment xadj #not directly manipulated
            yadjustment yadj

            vbox:
                spacing 1
                
                $ subgroup = None 

                for upgrade in upgrade_list:
                    if upgrade[1] == None:
                        $ subgroup = upgrade[0]
                        #if not subgroup == "DEFENSE":
                        $ subgroup_underlined = "{u}" + subgroup + "{/u}"
                        text subgroup_underlined:
                            color 'fff'
                            outlines [(2,'000',0,0)]
                            size 20
                    else:
                        $ name,level,increase,cost,multiplier = upgrade
                        $ attribute = ""
                        for key in ship.upgrades:
                            if ship.upgrades[key][0] == name:
                                $ attribute = key
                        $ current = getattr(ship,attribute)
                        #$ name = "{u}" + name + "{/u}"
                        
                        if subgroup is not None:
                            if subgroup.lower() in name.lower():
                                $ name = name.lower().replace("{u}"+subgroup.lower(),"   {u}",1)

                        if _preferences.language == "spanish":
                            if name == 'Hull Plating':
                                $ name = 'Dureza del Casco'
                            if name == 'Energy Reactor':
                                $ name = 'Reactor de Energía'
                            if name == 'Movement Cost':
                                $ name = 'Coste de Movimiento'
                            if name == 'Evasion':
                                $ name = 'Evasión'
                            if 'Damage' in name:
                                $ name = 'Daño'
                            if 'Accuracy' in name:
                                $ name = 'Precisión'
                            if 'EN Cost' in name:
                                $ name = 'Coste de EN'
                            if 'Flak Resist' in name:
                                $ name = 'Resistencia'
                            if 'Storage' in name:
                                $ name = 'Almacén'
                            if name == 'Shield Power':
                                $ name = 'Escudo: Poder'
                            if name == 'Shield Range':
                                $ name = 'Escudo: Rango'
                            if name == 'Flak':
                                $ name = 'Torretas Antiaéreas'
                            if name == 'Armor':
                                $ name = 'Armadura'
                            if name == 'Repair Crew':
                                $ name = 'Tripulación de Reparación'
                        else:
                            if name == 'Hull Plating':
                                $ name = 'Hull Plating'
                            if name == 'Energy Reactor':
                                $ name = 'Energy Reactor'
                            if name == 'Movement Cost':
                                $ name = 'Movement Cost'
                            if name == 'Evasion':
                                $ name = 'Evasion'
                            if 'damage' in name:
                                $ name = 'Damage'
                            if 'accuracy' in name:
                                $ name = 'Accuracy'
                            if 'en cost' in name:
                                $ name = 'EN Cost'
                            if 'flak resist' in name:
                                $ name = 'Flak Resist'
                            if 'storage' in name:
                                $ name = 'Storage'
                            if name == 'Shield Power':
                                $ name = 'Shield Power'
                            if name == 'Shield Range':
                                $ name = 'Shield Range'
                            if name == 'Flak':
                                $ name = 'Flak'
                            if name == 'Armor':
                                $ name = 'Armor'
                            if name == 'Repair Crew':
                                $ name = 'Repair Crew'
                        
                        hbox:
                            text name:
                                color 'fff'
                                min_width 250
                                size 20
                                outlines [(2,'000',0,0)]

                            if level <= 19:
                                text str(cost):
                                    color 'f55'
                                    size 20
                                    xanchor 0.5
                                    min_width 80
                                    outlines [(2,'000',0,0)]
                            else:
                                text ' -':
                                    color 'fff'
                                    min_width 80                                

                            if level <= 19:
                                if BM.intel >= cost or BM.mission=='skirmish':
                                    imagebutton:
                                        xpos -30
                                        idle "upgrade/button_purchase.jpg"
                                        hover hoverglow("upgrade/button_purchase.jpg")
                                        action Return(["process_upgrade",attribute]) #Function(process_upgrade,ship,attribute)
                                        hovered SetField(BM,'active_upgrade',upgrade)
                                        unhovered SetField(BM,'active_upgrade',None)
                                else:
                                    textbutton 'X':
                                        xpos -30
                                        text_color 'c00'
                                        action Play('chivoice','sound/Voice/chi_Others_03.ogg')
                                        hovered SetField(BM,'active_upgrade',upgrade)
                                        unhovered SetField(BM,'active_upgrade',None)
                            else:
                                textbutton 'X':
                                    xpos -30
                                    text_color 'c00'
                                    action NullAction()
                                    hovered None
                                    unhovered None

                            if level > 1:
                                imagebutton:
                                    xpos -30
                                    idle "upgrade/button_sell.jpg"
                                    hover hoverglow("upgrade/button_sell.jpg")
                                    action Return(["reverse_upgrade",attribute]) #Function(reverse_upgrade,ship,attribute)
                                    hovered SetField(BM,'active_upgrade',upgrade)
                                    unhovered SetField(BM,'active_upgrade',None)
                                    
    vbox:
        pos (675,866)
        if ship.shield_generation > 0:
            if _preferences.language == "spanish":
                text "Escudo:    " + str(ship.shield_generation)+"%x"+str(ship.shield_range)+"hex        N/A           N/A":
                    outlines [(2,'000',0,0)]
                    size 22        
            else:
                text "Shielding:  " + str(ship.shield_generation)+"%x"+str(ship.shield_range)+"hex        N/A           N/A":
                    outlines [(2,'000',0,0)]
                    size 22        
        if stats_missile != "NA":
            if _preferences.language == "spanish":
                text "Misil Res.:       " +str(BM.selected.missile_eccm):
                    outlines [(2,'000',0,0)]
                    size 22
            else:
                text "Flak Res.:        " +str(BM.selected.missile_eccm):
                    outlines [(2,'000',0,0)]
                    size 22
