# Setup for dynamic ship map
     
    # To make new buttons, add them to buttonlist
    # Syntax: ["name","image/image func", "hoverimage/func"]
    # If you want a changeable button, like ava's eyepatch then do a func that returns the string
    # It will automatically detect it and be used.
    
    # To add a new button, add it to talk_buttons
    # Syntax: ["Eval String","Name Code","Location","LabelName"]
    # It will show up WHENEVER the eval strings are met, to it is worth useing Btest("namecode") to check if it will overwrite an existing button.
    
    
init python:
    if not 'talk_buttons' in globals(): talk_buttons = [] # List used to gen them
    if not 'event_buttons' in globals(): event_buttons = [] # List for event buttons
    
    def setlabels(): # dynamicly sets labels to characters as required
        if talk_buttons != []: # if empty, skip
            for item in talk_buttons[:]: # for each entry, check if variables == True
                if eval(item[0]): # Set locations as needed + set events
                    globals()[item[1]+"_location"] = item[2] # Set location of char
                    globals()[item[1]+"_event"] = item[3] # Set char-event
                    
        if event_buttons != []:
            for item in event_buttons[:]:
                if eval(item[0]):
                    globals()[item[1]+"_location"] = item[2] # Set location of char
    
    def Btest(name_code):
        if globals()[name_code+"_location"] == None: return True
        return False
        
    def ava_img():
        if legion_destroyed:
            return "UI/ava_button_eyepatch.png"
        return "UI/ava_button.png"
        
    def ava_img2():
        if legion_destroyed:
            return tr_hoverglow("UI/ava_button_eyepatch.png")
        return tr_hoverglow("UI/ava_button.png")
        
    def btest(item):
        if callable(item): 
            return item()
        return item
        
    buttonlist = [["ava",ava_img,ava_img2],
                  ["asa","UI/asa_button.png",tr_hoverglow("UI/asa_button.png")],
                  ["chi","UI/chi_button.png",tr_hoverglow("UI/chi_button.png")],
                  ["ica","UI/ica_button.png",tr_hoverglow("UI/ica_button.png")],
                  ["cla","UI/cla_button.png",tr_hoverglow("UI/cla_button.png")],
                  ["sol","UI/sol_button.png",tr_hoverglow("UI/sol_button.png")],
                  ["kry","UI/kry_button.png",tr_hoverglow("UI/kry_button.png")],
                  ["pro","UI/pro_button.png",tr_hoverglow("UI/pro_button.png")],
                  ["gal","UI/gal_button.png",tr_hoverglow("UI/gal_button.png")],
                  ]
                  
    eventlist = [["cal","UI/button_store.png",tr_hoverglow("UI/button_store.png"),ShowStore,"UI/button_store_es.png",tr_hoverglow("UI/button_store_es.png")],
                 ["res","UI/button_research.png",tr_hoverglow("UI/button_research.png"),ShowUpgrades,"UI/button_research_es.png",tr_hoverglow("UI/button_research_es.png")],
                ]

label map_dispatch:

    window hide
    $setlabels()
    if captaindeck == 0:
        window hide
        $ renpy.transition(dissolve)
        show screen deck0
        $ ui.interact()

    if captaindeck == 1:
        window hide
        $ renpy.transition(dissolve)
        show screen deck1
        $ ui.interact()

    if captaindeck == 2:
        window hide
        $ renpy.transition(dissolve)
        show screen deck2
        $ ui.interact()
    
    jump map_dispatch
    return 


screen deck0: # Each frame can make imagebuttons

    tag ship_map
    key "mousedown_4" action NullAction()

    imagemap:
        ground "UI/deck0_inactive.jpg"
        hover "UI/deck0_hover.jpg"
        idle "UI/deck0.jpg"

        hotspot (1570, 855, 350, 76):
            action Show("deck1", dissolve)
        hotspot (1570, 957, 350, 76):
            action Show("deck2", dissolve)


    frame:##################################### CAPTAIN'S QUARTERS
        xmaximum 300
        xpos 500
        ypos 400
        background None
        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "captainsloft":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "captainsloft":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                    
    frame:######################HALLWAY
        xmaximum 400
        xpos 1040
        ypos 380
        background None

        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "hallway":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "hallway":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"

    frame:##################################### SICKBAY
        xmaximum 400
        xpos 750
        ypos 525
        background None

        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "sickbay":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "sickbay":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"


    frame:##################################### MESS HALL
        xpos 1150
        ypos 380
        background None

        vbox:
            xmaximum 600 ysize 400
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "messhall":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "messhall":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
screen deck1:

    tag ship_map
    key "mousedown_4" action NullAction()

    imagemap:
        ground "UI/deck1_inactive.jpg"
        hover "UI/deck1_hover.jpg"
        idle "UI/deck1.jpg"

        hotspot (1570, 755, 350, 76):
            action Show("deck0", dissolve)
        hotspot (1570, 957, 350, 76):
            action Show("deck2", dissolve)

    frame:##################################### BRIDGE
        xmaximum 300
        xpos 620
        ypos 440
        background None

        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "bridge":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "bridge":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"



    frame:##################################### ENGINEERING
        xmaximum 300
        xpos 1000
        ypos 350
        background None
        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "engineering":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "engineering":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"

    frame:##################################### LAB
        xmaximum 300
        xpos 1170
        ypos 440
        background None

        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "lab":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "lab":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"

screen deck2:

    tag ship_map
    key "mousedown_4" action NullAction()

    imagemap:
        ground "UI/deck2_inactive.jpg"
        hover "UI/deck2_hover.jpg"
        idle "UI/deck2.jpg"

        hotspot (1570, 755, 350, 76):
            action Show("deck0", dissolve)
        hotspot (1570, 855, 350, 76):
            action Show("deck1", dissolve)

    frame:##################################### Hangar
        xmaximum 300
        xpos 1170
        ypos 440
        background None
        vbox:
            for item in buttonlist:
                if globals()[item[0]+"_location"] == "hangar":
                    imagebutton:
                        action Jump(globals()[item[0]+"_event"])
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
                        
            for item in eventlist:
                if globals()[item[0]+"_location"] == "hangar":
                    imagebutton:
                        action item[3]()
                        idle btest(item[1])
                        hover btest(item[2])
                        activate_sound "Sound/beep1.ogg"
