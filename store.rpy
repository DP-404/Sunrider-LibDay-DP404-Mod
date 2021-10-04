label initStore:
    #I now use a custom Action to do include this. see ShowStore class.

    python:
        store_items = []

        store_items.append(NewWarhead())
        store_items.append(RocketUpgrade())
        store_items.append(NewRepairDrone())
        store_items.append(SunriderShieldUpgrade())
        store_items.append(SunriderVanguardUpgrade())
        store_items.append(ContractAllianceCruiser())
        store_items.append(ContractUnionFrigate())
        store_items.append(SellWishallArtifact())
        store_items.append(RepairUpgrade())
        store_items.append(GravityGunBooster())
        store_items.append(BlackJackThrusters())        

        if hasattr(store,'mod_items'):
            for moditem in store.mod_items:
                store_items.append(moditem())

    return

screen store_union:
    modal True
    tag storyscreen
    zorder 101 #the say screen is 100 so this is just on top

    add "store/back.jpg"
    use store_info
    
    key "mousedown_4" action NullAction()

    # imagebutton: #return button
        # xpos 0.05 ypos 0.8
        # action [ Hide('store_union') , SetField(BM,'hovered',None) , Jump("dispatch") ]
        # idle "Menu/return.jpg"
        # hover "Menu/return_hover.jpg"
    vbox:
        xalign 1.0 
        imagebutton:
            action Return(["return",None])
            idle "store/button_return.png"
            hover hoverglow("store/button_return.png")
        imagebutton:
            action Return(["upgrades",None])
            idle "store/button_upgrade.png"
            hover hoverglow("store/button_upgrade.png")        

    vbox:
        area (98, 287, 1158, 448)
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (1158,2000)

            frame:
                xmaximum 1158
                xpos 10
                ypos 270
                background None
                vbox:
                    spacing 1
                    for item in store_items:
                        if item.isVisible():
                            imagebutton:
                                action If(BM.money >= item.cost and (eval(item.variable_name) is None or eval(item.variable_name) < item.max_amt),[Play('sound1','Sound/kaching.ogg'),Return(['buy',item])],NullAction())
                                idle item.background_image
                                hover hoverglow(item.background_image)
                                hovered SetField(BM,'hovered',item.id)
                                unhovered SetField(BM,'hovered',None)
                
                $item_text_size = 33
                $item_line_spacing = 5
                
                vbox:
                    # ypos 12
                    for item in store_items:
                        if item.isVisible():
                            text item.display_name size item_text_size first_indent 50 line_spacing item_line_spacing color "fff" outlines [(2,'000',0,0)]
                                
                vbox:
                    # ypos 12
                    for item in store_items:
                        if item.isVisible():
                            text (str("[[{!s}]".format(eval(item.variable_name))) if eval(item.variable_name) is not None else "") size item_text_size first_indent 850 line_spacing item_line_spacing color "fff" outlines [(2,'000',0,0)]
                
                vbox:
                    # ypos 12
                    for item in store_items:
                        if item.isVisible():
                            text str(item.cost) size item_text_size first_indent 1005 line_spacing item_line_spacing color "fff" outlines [(2,'000',0,0)]

    text '{!s}$'.format(BM.money):
        size 50
        xalign 0.5
        yalign 0.5
        xpos 1460
        ypos 34
        color 'fff'
        outlines [(4,'000',0,0)]

screen store_info:
    zorder 10

    frame:
        xmaximum 1195
        background None
        xpos 86
        ypos 814

        for item in store.store_items:
            if BM.hovered == item.id:
                text item.display_name size 35  color 'fff' outlines [(2,'000',0,0)]
                text item.tooltip ypos 50 size 25  color 'fff' outlines [(2,'000',0,0)]



# screen store_missile:
    # add "Menu/unionstore_missiles.png" xpos 1170 ypos 200

# screen store_rocket:
    # add "Menu/unionstore_rocket.png" xpos 1170 ypos 200