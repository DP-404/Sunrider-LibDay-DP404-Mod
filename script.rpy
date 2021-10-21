# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Declare characters used by this game.

label splashscreen:

    scene black
    if CENSOR == False and CENSOR_ver == 3:
        show warning:
            xalign 0.5 yalign 0.5
        with dissolve
        
        $ renpy.pause(5)

        hide warning with dissolve

    $ renpy.movie_cutscene("3DCG/op.webm")
    
    # if not hasattr(store,'BM'):
        # $BM = Battle()
    
    return
    
label before_main_menu: #this is run even if the player quits back to main menu and is required to properly set up the BM
    if not hasattr(store,'BM'):
        $BM = Battle()
    return
    
# The game starts here.
label start:

    call initialize from _call_initialize
    
    if customstat == False:
            
        if mp.wishall == None:
            
            window hide
            
            nar "WARNING: No Mask of Arcadius V7.2 save data detected."
            nar "You must finish Mask of Arcadius V7.2 and export a save file when prompted to import your data into Liberation Day."
            
            $ renpy.full_restart()
        
        else:
            python:
                for var in important_variables:
                    setattr(store, var, getattr(mp,var))
                affection_kryska += affection_tera
    
    if customstat == True:
    
        call beginstat from _call_beginstat

    stop music fadeout 1.5
        
    hide history
    scene bg black
    show screen quick_menu
    with dissolvemedium
    
    $ renpy.music.set_volume(0.27, delay=0, channel='music')
    $ renpy.music.set_volume(0.8, delay=0, channel='sound')
    $ renpy.music.set_volume(1.0, delay=0, channel='voice')

    play music "Music/Destinys_Path.ogg"

    nar "Following the devastating war between the democratic Solar Alliance and the tyrannical New Empire, the galaxy was split into two zones separated by the Neutral Rim, a buffer between the two states."

    nar "Weakened by war, the New Empire collapsed from within in the Compact Revolution. A figure known only as VENICZAR ARCADIUS led the people against their Imperial oppressors. Following the New Empire's fall, Arcadius mysteriously vanished from public view."
    
    nar "Soon after, another entity claiming to be Arcadius returned and declared the formation of PACT. With the vast production base of the former New Empire, PACT invaded the Neutral Rim with the intent of striking the Solar Alliance."

    nar "Arcadius sought the hand of the Ryuvian princess for reasons unknown, but was thwarted by Captain Shields of the Cera Space Force."

    nar "He was further thwarted at the battle of Far Port, when Cullen's blunder led to the destruction of the PACT invasion fleet by a much smaller Alliance vanguard fleet."

    nar "What was envisioned by PACT leaders as a glorious invasion into the heart of Alliance space instead became a bloody foreign campaign fought in the undeveloped Neutral Rim."

    nar "With the Alliance Fleet approaching PACT space and their initial military goals now in tatters, VENICZAR FONTANA betrayed Arcadius in the Battle of Helion and took control of PACT."

    nar "Now unmasked, the truth of the entity claiming to be Veniczar Arcadius came to light..."
    
    #jump test_battle
    
    stop music fadeout 1.5
    
    "... ... ..."
    "... ..."
    "..."
    fon "No..."
    fon "You do not own PACT."
    
    play sound "sound/pulse2.ogg"
    
    pause 1.0
    
    play music "Music/Danger.ogg"
    
    scene helion_back
    
    pause 1.0

    show helion_text:
        xpos 950 ypos 850
    with dissolve

    with dissolve
    
    pause 2.0
    
    scene intro_helion:
        zoom 0.58 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 subpixel True
    with dissolve
    
    #pause 1.0
    
    #scene intro_helion:
        #zoom 0.58 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
        #ease 0.3 zoom 0.86 xpos 0.5 ypos 0.6
    
    asa "This is the Black Jack! Did you just hear that, Sunrider!?"
    asa "That red bastard turned on Arcadius! The PACT lines are falling to chaos!"
    asa "We've just finished neutralizing the PACT Arcadius units here, but it looks like one of 'em's still alive."
    asa "What should we do with it, captain?"
    
    if legion_destroyed == False:
    
        scene bg bridge
        
        $ dshow('ava armscrossed neutral neutral angry')
        with dissolve
        
        ava "Captain, this new revelation changes everything we've understood about the war."
        ava "We must take the last prototype alive. The intel we could extract from it could..."
        "Shields clenched his teeth."
        kay "It... looked like her."
        ava "Captain?"
        kay "Take it alive."
        ava "Sir. Liberty, prepare to tow the remains of the disabled Arcadius unit back to our hangar."
        
    if legion_destroyed == True:
        
        kry "Captain, this new revelation changes everything we've understood about the war."
        kry "If we were to capture the last prototype alive, the intel we could gain could..."
        "Shields clenched his teeth."
        kay "It... looked like her."
        kry "Captain?"
        kay "Take it alive."
        asa "Understood! Liberty, tow the disabled Arcadius unit back to the Sunrider!"
    
    scene chigara_shock with dissolve
    
    chi "That's... impossible...!"
    chi "Something like that..."
    chi "I'm the only one who survived... Everyone else..."
    
    scene lynn_cockpit with dissolve

    pro "Haah... haaah..."
    pro "We are all the children of Diode."
    pro "We are one and the same, you and I..."
    pro "Sisters."
    
    scene chigara_shock with dissolve

    chi "No!"
    pro "Hahaha..."
    pro "Hahahahahaha!!"
    chi "EEAAHHH!!!!"
    ica "Tsch, Arcadius!!"
    
    scene bg bridge
    
    if legion_destroyed == False:
    
        $ dshow('ava armscrossed neutral neutral angry')
    with dissolve    

    kay "Hold your fire! That's not Arcadius!"
    kay "W-whatever that thing is, it's our only chance at figuring out what's happening here."
    ica "Copy that, but the Liberty's-"
    chi "EAAAHHHH!!!"
    
    if legion_destroyed == False:
    
        ava "Bianca, tow the Arcadius unit back to the Sunrider!"
    
    if legion_destroyed == True:
    
        kry "Bianca, tow the Arcadius unit back to the Sunrider!"
    
    cla "C-copy!"
    
    play sound "sound/warning.ogg"
    
    if legion_destroyed == False:
    
        ava "Warning, new hostiles inbound! Pirate forces, on a intercept course!"
    
    if legion_destroyed == True:
    
        kry "Warning, new hostiles inbound! Pirate forces, on a intercept course!"
        
    scene piratesapproach:
        zoom 0.6 xanchor 0.5 yanchor 0.5 ypos 0.5 xpos 0.5
    with dissolve

    pause 0.7

    scene cosette_attack with dissolve
    
    cos "Aren't you forgetting about someone--!?"
    kay "(Now of all times? We don't have time for this!)"
    kay "All units, scratch your previous orders. Regroup and engage the pirates on the double."
    asa "Copy that, Sunrider!"
    cos "You agaainn!?"
    cos "Hahahaha...!!!"
    cos "This is where it all ends!"
    asa "You're too late! PACT's defeated! We've got Arcadius!"
    
    scene cosette_attack_lines with dissolve
    
    cos "I can still take you out!! EAAHH!!!"

    play sound1 "sound/mech_boost1.ogg"

    scene piratesapproach:
        zoom 0.6 xanchor 0.5 yanchor 0.5 ypos 0.5 xpos 0.5
        linear 1.5 zoom 0.62
    with dissolve
        
    pause 1.0
        
    scene piratesapproach:
        zoom 0.62 xanchor 0.5 yanchor 0.5 ypos 0.5 xpos 0.5 zoom 0.6 subpixel True
        easeout 0.5 zoom 15.0
        
    pause 0.5

    window hide
    hide battlewarning

    call mission1_inits from _call_mission1_inits
    $ BM.mission = 1
    call bcheckset from _call_bcheckset
    pause 1.0
    scene bg paradoxback with battlewipe
    $BM.battle_bg = "Background/paradoxback.jpg"

    jump battle_start

label mission1:
    
    if not bcheck3:
        
        $ bcheck3 = True
        
        play sound "sound/beep1.ogg"
        
        $ BM.draggable = False
        
        "Tip: Command Points are now capped at 4000 points and firing the Vanguard Cannon costs all 4000."
        "However, you now gain command points as you destroy enemies in battle. Similar to before, destroying units quicker increases your Command reward."
    
        $ BM.draggable = True
    
    if not bcheck1 and BM.turn_count == 2:
        
        $ bcheck1 = True

        if legion_destroyed == False:
            ava "Ambush! More enemies have appeared!"
        else:
            kry "Ambush! More enemies have appeared!"

        
        python:
            create_ship(PirateDestroyer(),(12,2))
            create_ship(PirateDestroyer(),(13,2))
            create_ship(PirateBomber(),(13,3))
            
            create_ship(PirateDestroyer(),(12,17))
            create_ship(PirateDestroyer(),(13,17))
            create_ship(PirateBomber(),(12,16))
    
    if not bcheck2 and BM.turn_count == 3:
        
        $ BM.draggable = False
    
        show intro_helion onlayer screens with dissolve:
            zoom 0.86 xanchor 0.5 yanchor 0.5  xpos 0.5 ypos 0.6
        
        asa "Hey look! The PACT fleet's retreating!"
        kry "Hah! They cower at the might of the Alliance Fleet!"
        asa "Your luck is out, Cosette! Now scamper back with your tail tucked between your legs."
        
        hide intro_helion onlayer screens
        show cosette_attack onlayer screens
        with dissolve
        
        cos "T-tsch..."
        asa "A lil' chihuahua like ya's no match for all of us!"
        cos "H-hurk..."
        cos "W-what did you call me---"
        cos "It was all your fault... All your fault... All your fault I'm... like this...!!!"
        cos "Huefufufu..."
        cos "HUWAHAHAHAHAHAHAHA!!!!"
        cos "No retreat! Men, hold your ground!"
        cos "If Fontana doesn't have the gall to stand here, then we'll just kill them all ourselves!"
        kay "Cosette, don't--"
        cos "WE'll NEVER SURRENDER TO YOU!"
        cos "You'll just have to kill every last one of us..."
        kay "But your death would be meaningless!"
        cos "Better to die in a blaze than alone in a ditch somewhere... hungry... sick... used..."
        cos "This will be the final charge of Cosette Cosmos, the terror of the stars!"
        cos "History may paint us as the villains, but know that we stood here in defense of our home world!"
        cos "So that our children will not bear the horrors we did! So that no one else but us will dirty their hands!"
        cos "All ships, onward to hell!"
        
        hide cosette_attack onlayer screens with dissolve 
        
        $ bcheck2 = True
        $ BM.draggable = True
    
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission1 #loop back
    else:
        pass #continue down to the next label

label after_mission1:
    
    python:
        #I should make a function for easy (safe!) deletion of ships >.<
        if hasattr(store,'alliancebs1'):
            if alliancebs1 in BM.ships:
                BM.ships.remove(alliancebs1)
                player_ships.remove(alliancebs1)
        if hasattr(store,'alliancecruiser1'):
            if alliancecruiser1 in BM.ships:
                BM.ships.remove(alliancecruiser1)
                player_ships.remove(alliancecruiser1)
                
        if legion_destroyed == True:
            player_ships.insert(0,sunrider)
            BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']
            BM.orders["VANGUARD CANNON"] = [4000,'vanguard_cannon']
    
    hide screen battle_screen
    hide screen commands
    
    $ mission1_complete = True
    $ VNmode()
    
    window show
    
    play music "Music/MarduksWrath.ogg"
    
    scene havochit
    #show movie
    #play movie "3DCG/havochit.webm" noloop
    $ renpy.movie_cutscene("3DCG/havochit.webm",stop_music=False)

    cos "A-arggghhhh!!!"
    asa "It's over, Cosette!"
    asa "Why don't you surrender so we don't have to kill you."
    
    stop movie
    hide movie
    scene cosette_attack with dissolve
    
    cos "Hahaha..."
    cos "Like I said... No surrender..."
    
    scene havocfly
    show movie
    #play movie "3DCG/havochitfly.mkv" noloop
    $ renpy.movie_cutscene("3DCG/havochitfly.mkv",stop_music=False)
    
    cos "The Havoc is far from finished!"
    
    scene havocattack
    show movie
    #play movie "3DCG/havocattack.webm" noloop
    $ renpy.movie_cutscene("3DCG/havocattack.webm",stop_music=False)
    
    cos "Hahaha... HAHAHAAHAA!!!"
    
    scene blackjackdodge
    show movie
    #play movie "3DCG/blackjackhit.webm" noloop
    $ renpy.movie_cutscene("3DCG/blackjackhit.webm",stop_music=False)
    
    asa "Eeaah!"
    
    stop movie
    hide movie
    scene asagacockpit with dissolve
    
    asa "Cosette!!"
    cos "Don't celebrate so soon! This fight's not over yet!"
    asa "Don't... mess... with me!!!"
    
    play sound "sound/heartbeat.ogg"
    
    scene asagacockpit_awaken
    show asagacockpit:
        xalign 0.5 yalign 0.5
        easeout 0.25 zoom 1.5 alpha 0
    with dissolve
    
    asa "Foolish villain."
    cos "W-what!?"
    asa "You cannot soothe your conscience with excuses."
    cos "Peh! What would a Ryuvian princess know of poverty!? What would she know of desperation!?"
    asa "Irrelevant."
    asa "Justice shall be done to all."
    asa "No mitigation. No justifications. No claims to the greater good."
    asa "Now meet your judge, evildoer. For I, Sharr of Ryuvia, shall cast you into the eternal fire."
    
    scene blackjackfly
    show movie
    #play movie "3DCG/blackjackfly.webm" noloop
    $ renpy.movie_cutscene("3DCG/blackjackfly.webm",stop_music=False)
    
    cos "Just what---"
    
    scene blackjacklaser
    show movie
    #play movie "3DCG/blackjacklaser.webm" noloop
    $ renpy.movie_cutscene("3DCG/blackjacklaser.webm",stop_music=False)
    
    cos "C-caan---"
    
    scene white
    show movie
    #play movie "3DCG/havochitlaser.webm" noloop
    $ renpy.movie_cutscene("3DCG/havochitlaser.webm",stop_music=False)
    
    cos "Y-you---"
    cos "HIEEAAHHH!!!!"
    
    stop movie
    hide movie
    scene asagacockpit_awaken_sun with dissolve
    
    if wishall == True and affection_cosette < 2:
    
        show screen wishall_cosettedead
    
    asa "Foolish creature."
    asa "Your hands are soaked with blood."
    asa "Your mind is as malignant and twisted as your deformed body."
    asa "Your time alive will be but paradise to the eternal torment your soul will endure in death."
    
    if wishall == True and affection_cosette < 2:
    
        hide screen wishall_cosettedead

    if wishall_kill == False:
        
        jump prologue_cosettealive
    
    if affection_cosette >= 2:
        
        jump prologue_cosettealive
        
    if affection_cosette < 2:
        jump prologue_cosettedead
    
label prologue_cosettealive:
    
    $ cosette_dead = False
    $ chivo_process('Cosette Captured')
    
    ###Anti-Alliance

    scene bg bridge with dissolve

    kay "Cosette..."
    kay "Yield!"
    cos "Y-you..."
    kay "Surrender to us, and I'll listen to what you have to say."
    kay "You're not the only one fighting for the Neutral Rim."
    cos "... ... ..."

    scene asagacockpit_awaken_sun with dissolve

    asa "Begone, demon!"
    kay "Asaga, stop!"

    scene asagacockpitsurprise with dissolve

    asa "...E-eh!?"
    kay "She's helpless now!"
    asa "O-oh! W-what am I doin'?"
    asa "E-ehh!?!? W-what the hell happened to the Havoc! It's completely wrecked!"
    ica "That was all your doing, ya dumbass!!"
    kry "The area is secured. What are your orders, captain?"
    kay "Secure both the Havoc and the Arcadius unit. Prepare the hangar for two prisoners."
    "Everyone" "Copy that!"

    jump titlecardstart

label prologue_cosettedead:
    
    $ cosette_dead = True
    $ chivo_process('No Loli Space Pirate Route')
    
    scene havoc_dead with dissolve
    
    pause 1.0
    
    scene cosette_attack_blood with dissolve

    cos "T-tsch..."
    cos "... ... ..."
    cos "Hufufufu..."
    
    scene cosette_attack_bloodlaugh with dissolve

    cos "Haahahahahaha!!!"
    cos "I see..."
    cos "So this is the great justice you've sought all this time..."
    cos "So do it! HERO!!!"
    
    scene asagacockpit_awaken with dissolve
    
    asa "As you desire!"
    
    scene blackjack_pulse
    #play movie "3DCG/blackjack_pulse.webm" noloop
    $ renpy.movie_cutscene("3DCG/blackjack_pulse.webm",stop_music=False)
    
    pause
    
    stop movie
    hide movie
    
    play sound "sound/explosion2.ogg"
    scene havocexplode at tr_shake with dissolve
    
    pause 2.0
    
    scene cosette_attack_bloodlaugh with dissolve
    
    cos "Hahaha... EAAHAHAHAHAHA!!!"
    
    play sound "sound/explosion2.ogg"
    scene white with dissolve

    scene cosette_attack_bloodlaugh with dissolve

    cos "... ... ..."
    
    scene cosette_attack_bloodcry with dissolve
    
    cos "Mama..."
    
    scene white with dissolvemedium
    scene havocexplode with dissolve
    
    play sound "sound/explosion4.ogg"
    
    scene white with dissolvemedium
    
    scene bg bridge with dissolvemedium

    kry "All pirate units neutralized, captain. The rest of the PACT ships have fled."
    ica "Hah! No honor amongst thieves, they say..."
    kay "Good work, everyone."
    kay "Secure the Arcadius unit! Prepare the hangar for our prisoner!"
    "Everyone" "Copy that!"
    
    jump titlecardstart
    
label titlecardstart:
    
    play music "Music/Destinys_Path_Short.ogg" fadeout 1.5

    scene black with horizontalwipe
    scene bg pactbridge
    show fontana   
    with horizontalwipe

    pof "My veniczar. Our ships have performed an orderly retreat."
    pof "What shall we do with the Paradox Core?"
    fon "Even in its disarmed state, we cannot allow the Alliance Imperialists to seize control of the Core."
    fon "No doubt they will seek to create Cores of their own if the means were made available to them."
    fon "Have your men made the preparations?"
    pof "Yes sir. We have rigged explosives throughout the Core to detonate as ordered. Our ships have now retreated safely away from the perimeter."
    fon "Good."
    fon "Send the signal."
    fon "The galaxy has no need for a weapon so devastating."
    pof "Understood! Detonate the explosives!"
    fon "... ... ..."
    fon "What's wrong!?"
    pof "The explosives are not responding to the signal! We are being jammed!"
    fon "By who!? All the prototypes should have been destroyed!"
    pof "I am reading hyper brain waves! A prototype still lives!"
    pof "The source emanates from the Sunrider!"
    fon "Tsch..."
    fon "That ship again... He has interfered with our plans once more..."
    fon "It seems that our destinies are intertwined."
    fon "Shields... What have you done..."

    scene black
    show titlecard_preview
    with dissolvemedium

    stop music fadeout 1.5

    window hide

    $ renpy.movie_cutscene("3DCG/titlecard.webm",stop_music=True)

    hide titlecard_preview

    #show movie
    #play movie "3DCG/titlecard.webm" noloop
    #show screen titlecard

    #with dissolvemedium

    #pause 19.0

    #stop movie
    #hide movie
    
    #######################################

    #SUNRIDER: LIBERATION DAY

    #######################################
    
    play sound1 "Music/Shower.ogg" fadein 3.0 loop
    
    $ BM.money += 10000
    $ BM.intel += 3000
    
    window show
    
    show screen leftbuttons

    scene black with dissolve
    
    if CENSOR == True:
        scene shower1_censored:
            yalign 1.0 xalign 0.0
            linear 10 yalign 0.0
        with dissolvelong
        
    if CENSOR == False:
    
        scene h_shower1:
            yalign 1.0 xalign 0.0
            linear 10 yalign 0.0
        with dissolvelong
    
    $chivo_process('Welcome Back Captain')
    
    "... ... ..."
    "... ..."
    "..."
    "Cold water splashed against Icari, soaking away the tension from the battle."
    "A shower after a victory was exactly what she needed."
    "She couldn't help but sigh in relief."
    "The door slid open and another person entered the shower room."
    
    if CENSOR == True:
        scene shower2_censored:
            yalign 0.0 xalign 0.0
            ease 0.5 xalign 1.0
        
    if CENSOR == False:
    
        scene h_shower2:
            yalign 0.0 xalign 0.0
            ease 0.5 xalign 1.0
    
    ica "G-guck! W-who!?"
    kry "Permission to enter!"
    ica "U-uck... A-ah..."
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg"
    
    if CENSOR == True:
        
        scene shower3_censored:
            xalign 1.0 yalign 0.0
        with dissolve
        
    if CENSOR == False:
    
        scene h_shower3:
            xalign 1.0 yalign 0.0
        with dissolve
    
    ica "Well, I guess it's fine! W-we're both girls..."
    kry "Hah hah hah!"
    kry "Nothing beats a shower after the rush of combat!"
    kry "We sure gave the reds a good whooping this time, did we not?"
    ica "I-I suppose!"
    ica "W-well, uhh... Despite everything, we managed to keep the Sunrider in one piece... Mostly..."
    ica "So, I... uhh... well..."
    ica "Ah, whatever, soldier boy!"
    ica "Here's the soap!"
    "Kryska grabbed the soap bar from Icari's hand."
    kry "With this victory, the road to Cera lies completely open."
    kry "Looks like PACT was merely overconfident, challenging the dominance of the Alliance!"
    kry "I bet they'll be suing for peace in no time at all!"
    kry "Once everyone sits down to talk, I'm sure this war will be over!"
    ica "S-seriously... It's still too soon to get confident like that!"
    ica "Well, I guess you did do well out there though..."
    ica "So uhh..."
    ica "Thanks."
    kry "Hah!"
    kry "You are not as bad as I thought either, mercenary!"
    kry "I am proud to be your comrade in arms!"

    if CENSOR == True:
        
        scene shower4_censored:
            xalign 1.0 yalign 0.0
        with dissolve
        
    if CENSOR == False:

        scene h_shower4:
            xalign 1.0 yalign 0.0
        with dissolve

    "Kryska took Icari's hand and shook it over vigorously."
    kry "Once this war is over, let us share a round of drinks together on Solaris!"
    ica "C-c-c-comrade!?"
    ica "S-seriously..."
    ica "You better prepare yourself! I'm not gonna be out drank by a choir boy like you!"
    kry "Hah! They call me the stonewall for more than one reason."
    kry "I hope your fortitude lasts longer than your ryder's armor!"

    if CENSOR == True:

        scene shower5_censored:
            xalign 1.0 yalign 0.0
        with dissolve

    if CENSOR == False:

        scene h_shower5:
            xalign 1.0 yalign 0.0
        with dissolve

    ica "W-what!? Y-you!!!!"
    kry "Hah hah hah!"

    stop sound1 fadeout 1.5

    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene black with horizontalwipe
    scene bg brig with horizontalwipe
    
    $ dshow("chigara handonchest neutral neutral sad",xpos=0.72)
    $ dshow("claude neutral smile neutral neutral",xpos=0.28)

    "Shields observed the entity he had known earlier as Veniczar Arcadius."
    "Up close, he saw that she was but a small female, hardly intimidating behind a force field and plexiglass."
    kay "So, what is this thing?"
    
    $ dshow("claude fingerup talk neutral neutral",xpos=0.28)
    
    cla "I've performed a preliminary medical check."
    cla "For all intents and purposes, she appears to be a human. However, a deeper analysis reveals substantial artificial engineering done to her genetic code."
    cla "The closest analogy might be that she is Chigara's sister, albeit artificially created."
    kay "You never told me you had a sister, Chigara."
    
    $ dshow("chigara handonface frown narrow sad2",xpos=0.72)
    
    chi "No..."
    chi "This is the first time I've seen an artificial human, much less a sister..."
    kay "Any ideas about her origins?"
    chi "I'm sorry..."
    kay "Well then, looks like the only thing left is to ask her personally."
    
    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5
    scene lynn_brig1 with dissolve
    
    "Shields approached the cell and pressed the intercom."
    kay "I'm Captain Shields. Welcome aboard the Sunrider."
    lyn "Peh."
    
    scene lynn_brig2 with dissolve
    
    lyn "What do you want?"
    kay "You're now a prisoner of war under Article Seven of the Cera Military Code."
    kay "We will treat you fairly and respect your basic human rights to the extent required under the code."
    kay "Now, uhh... Do you have a name, prisoner?"
    lyn "Prototype L7NN."
    kay "That's hardly a name."
    kay "Why don't I just call you Lynn."
    kay "That's a part of Chigara's name. Are you related to her?"
    lyn "Of course. We are all sisters."
    lyn "Together, we are legion. But the others are silent now."
    lyn "The ones nearby are all dead. But there are more of us. There will always be more."
    kay "(From what we've seen before, the prototypes seem capable of communicating with each other...)"
    kay "(Could it possibly be telepathy? But such powers cross into the realm of fantasy...)"
    kay "(Then could lost technology be involved?)"
    kay "So you can't hear your sisters now?"
    lyn "That's what I said."
    kay "You've been cut off."
    kay "You must be scared. Is it the first time that you've been disconnected?"
    
    scene lynn_brig1 with dissolve
    
    lyn "... ... ..."
    kay "If Chigara's one of your kind, why can't you hear her thoughts?"
    lyn "... ... ..."
    kay "(Suddenly no words, huh...)"
    kay "(The prototypes must depend on their hivemind to function.)"
    kay "(Without it, they're individually weak.)"
    
    scene bg brig with dissolve
    $ dshow("chigara handonface frown narrow sad2",xpos=0.72)
    $ dshow("claude neutral neutral neutral neutral",xpos=0.28)    
    
    "Shields left the intercom."
    "Claude and Chigara peered at him curiously."
    cla "Well?"
    kay "We'll watch her for now."
    kay "I don't think she'll pull anything, but be careful just in case."
    kay "As long as we don't run into another prototype, I don't think she has much power."
    
    $ dshow("claude fingerup happy closed neutral",xpos=0.28)    
    
    cla "Mmm... She just looks like a small girl now."
    cla "Teehee. It's a little embarrassing we were intimidated by Arcadius when he was just a little girl all along!"
    
    $ dshow("chigara handonchest smile closed embarass",xpos=0.72)
    
    chi "E-eh-heh..."
    kay "Anyways, see if she starts talking again. Figure out what we can learn from her."
    cla "Understood, captain!"
    chi "Okay, I'll try to help too!"
    
    stop music fadeout 1.5

    if cosette_dead == False:

        kay "Oh, and speaking of little..."
        
        scene cosette_jail with dissolve
        
        "In the other cell, Cosette pressed her face against the plexiglass and snorted, fogging it up."
        kay "Our pirate friend seems to have acclimated well to the brig."
        "Shields pressed the intercom."
        cos "YOU BASTARD, WHAT DID YOU CALL ME---"
        "He cut her off."
        "Shields shook his head and frowned."
        
        scene bg brig with dissolve 
        
        kay "Make sure she doesn't hurt herself."
        
        $ dshow("claude salute happy neutral neutral",xpos=0.5)    
        
        "Claude chopped her hand on her forehead."
        cla "Sah!"
        
    $ captaindeck = 0
    
    if legion_destroyed == True:
        
        $ ava_location = "sickbay"
        $ chi_location = "messhall"
        
        $ ava_event = "ava_sickbaytalk"
        $ chi_event = "chigara_windows"
        
        scene black
        jump map_dispatch
        
    if legion_destroyed == False:
        
        $ ava_location = "hallway"
        $ chi_location = "messhall"
        
        $ ava_event = "ava_hallway"
        $ chi_event = "chigara_windows"

        scene black
        jump map_dispatch
        
label ava_sickbaytalk:
    
    hide screen ship_map
    
    ###IF LEGION SANK, Ava sickbay

    play music "Music/Colors_sad.ogg" fadeout 1.5

    scene bg sickbay with dissolve
    
    pause 0.5
    
    scene ava_sickbay1 with dissolve
    window show

    "Shields sat beside Ava's bed in the sickbay."
    ava "U-ugh..."
    "Ava regained consciousness."
    ava "... ... ..."
    ava "What happened?"
    kay "We found you in the auxiliary control room all smashed up."
    kay "The medics barely managed to get you into the nano tank in time to save you."
    ava "Not that. The Legion."
    kay "... ... ..."
    kay "You did it, Ava."
    kay "It's been sunk. You're the hero of the Combined Fleet now."
    kay "You saved everyone."
    "Ava finally relaxed and sank back into her bed."
    ava "... ... ..."
    kay "You'll be in sickbay for a while. But Claude somehow managed to patch most of your good looks back together."
    kay "U-uh, I mean..."
    ava "...Hahaha..."
    ava "Idiot."
    ava "... ... ..."
    ava "So how bad do I look?"
    kay "We managed to regrow your arm. The coloration should naturally blend with use."
    kay "As for the eye, I managed to get my hands on a bionic one, courtesy of the admiral."
    kay "Should work even better than your old one, I hear."
    ava "... ... ..."
    kay "May the ghost of that ship burn forever in the deepest pits of that star."
    kay "I can only pray the galaxy will never witness another weapon so terrifying."
    kay "We nearly lost you. I don't ever want anything like that to happen again."
    ava "And so we lay down our sorrows of that day..."
    ava "... ... ..."
    ava "Once we return to Cera, I want to bury everyone, up in that mountain we used to play on when we were young."
    kay "Yeah..."
    kay "We'll do it together."
    ava "... ... ..."
    "Ava closed her eyes."
    
    scene ava_sickbay2 with dissolve
    
    ava "I'm... still tired..."
    ava "You'll have to handle the paperwork by yourself..."
    kay "Yeah... Shouldn't be a problem..."
    "Shields stroked her head as she went to sleep."
    kay "(Good night...)"
    
    $ ava_location = None
    $ ava_event = None
    $ cmap_firstavatalk = True
    
    if cmap_firstavatalk == True and cmap_chigarawindows == True:
        $ pro_location = "bridge"
        $ pro_event = "shipactivitybattle"
    
    $ captaindeck = 0
    
    scene black
    jump map_dispatch
    
label ava_hallway:
    
    hide screen ship_map
    
    ###Legion Not Sank
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene bg hallway with dissolve
    $dshow("ava armscrossed neutral neutral angry")
    
    window show

    "Shields came face to face with Ava as he walked through the hallway."
    kay "O-oh."
    "He awkwardly cleared his throat as she eyed him with disapproval."
    kay "Ahem... Well..."
    "Already sensing an impending lecture, he tried to hightail it back to his office."
    "She power walked, chasing him through the hallway."
    
    $dshow("ava fingerup shout neutral angry")
    
    ava "Captain, I will be formally lodging a complaint in regards to the operation against the Legion!"
    kay "I'd say the operation turned out well enough."
    ava "Despite expending considerable resources and lives in an attempt to exploit its weakness, you issued an order to ignore it when we had it in our sights!"
    ava "Because of your order, our allied forces sustained severe losses which were entirely preventable."
    ava "Worse still, now PACT has been tipped off about the Legion's design flaw."
    ava "According to latest Alliance intel, the Legion has been pulled back deep into PACT space for a design overhaul."
    ava "No doubt, PACT will now seal the only weakness in the Legion's design. The next time the Legion appears in battle, it will be nigh invincible."
    ava "We had but one opportunity to strike the Legion while PACT was unaware of its vulnerability, and that opportunity was squandered!"
    ava "All in all, the battle would have been a catastrophic loss for the Alliance, if it were not for Veniczar Fontana's fortuitous betrayal."
    ava "Our victory was entirely situational and had we not been so lucky, none of us would be alive right now!"
    
    $dshow("ava armscrossed shout closed angry")
    
    ava "AND FINALLY, one last thing, captain!"
    kay "(Y-you mean there's more...!?)"
    ava "I wholeheartedly denounce your highly inappropriate remarks regarding your... feelings towards me on the floor of the bridge!"
    ava "Shouting like a fool like that, and in front of the entire bridge crew!"
    ava "Unbelievable! S-such unbecoming conduct from the highest ranking Ceran officer on board this fleet!"
    "Shields cringed and turned around to face her."
    kay "W-will that be all, commander?"
    
    $dshow("ava salute shout neutral angry")
    
    ava "Sir!"
    "Shields scratched the back of his head in frustration."
    kay "I'm glad to see you safe and sound too, Ava."
    
    $dshow("ava armscrossed shout neutral angry")
    
    ava "This is not a joke, captain!"
    ava "You could lose your commission for this! At the very least face an ugly sexual harassment suit!"
    kay "S-sexual--?"
    
    $dshow("ava armscrossed neutral neutral angry")
    
    ava "... ... ..."
    kay "Sigh..."
    kay "I wasn't going to send you to your death, Ava."
    kay "Enough Ceran lives have been lost to that ship."
    ava "And now, many more."
    kay "We'd be insane if we weren't emotionally compromised after all that's happened. We'd probably be monsters."
    kay "... ... ..."
    kay "I'm sorry. You were right."
    kay "I should never have sent the Sunrider into that battle."
    kay "You never realize what you still have around you, until you're about to lose it."
    ava "Hmph."
    kay "Anyways, you can go ahead and file that complaint."
    kay "But considering Command was reduced to a smoking crater a while back, I doubt it's going to do any good."
    
    $dshow("ava handonhair neutral neutral angry")
    
    ava "Yes captain. I am very painfully aware of that fact."
    ava "I was... merely venting..."
    kay "Looks like you'll have to deal with me for a while longer then."
    "Shields forced a smile."
    kay "At least we have luck on our side."
    "The commander shook her head as Shields walked away."
    
    hide ava with dissolve
    
    kay "(Great, she totally hates me now...)"
    kay "(So much for getting closer...)"
        
    $ ava_location = None
    $ ava_event = None
    $ cmap_firstavatalk = True
    
    if cmap_firstavatalk == True and cmap_chigarawindows == True:
        $ pro_location = "bridge"
        $ pro_event = "shipactivitybattle"
    
    $ captaindeck = 0
    
    scene black
    jump map_dispatch

label chigara_windows:
    
    hide screen ship_map
    
    play music "Music/Colors_Chigara.ogg" fadeout 1.5

    scene bg messhallwindows with dissolve
    $reset_sprites()
    
    $dshow("chigara handonchest neutral narrow sad",0.5)
    window show

    chi "... ... ..."
    "Shields gently cleared his throat, trying not to scare Chigara."
    
    $dshow("chigara armsbehindback smile neutral embarass",0.5)
    
    chi "O-oh... Captain..."
    kay "You're troubled."
    
    $dshow("chigara holdinghands frown neutral embarass",0.5)
    
    chi "Yes..."
    chi "About Lynn... And the rest of the prototypes..."
    chi "I... I was completely clueless..."
    chi "I had no idea they existed..."
    chi "Engineered siblings of myself..."
    kay "Could they have been created behind your back?"
    chi "I had always considered my childhood to be normal..."
    chi "Performing experiments with my parents... Learning to continue their work..."
    kay "(I'm sorry Chigara, but nothing about that sounds like a normal childhood.)"
    chi "They were happy days. I was an only child and my parents gave me all their attention."
    
    $dshow("chigara handonchest yell closed embarass",0.5)
    
    chi "A-anyways, I never knew I had hundreds of sisters wandering around, all plotting to take over the galaxy!"
    chi "C-Chigara has no interest in galactic overlordship! J-just proprietorship of a small bakery is more than enough!"
    kay "Nobody is questioning your loyalty, Chigara."
    kay "We would never have made it this far without your help. You would never betray us."
    
    $dshow("chigara handonface smile narrow sad blush",0.5)
    
    chi "C-captain..."
    chi "Eh-heh... N-no, you mustn't keep saying things like that..."
    
    $dshow("chigara holdinghands smile closed embarass blush",0.5)
    
    chi "... ... ..."
    chi "I think... Chigara's going to bake a cake now."
    kay "???"
    
    $dshow("chigara handonchest smile neutral neutral blush",0.5)
    
    chi "Thank you, captain. That made me feel a little bit better."
    "Chigara backed away, smiling at Shields."
    chi "Please see me later. I'm making something for you."
    kay "Really?"
    
    $dshow("chigara handonchest smile closed neutral blush",0.5)
    
    chi "Yes. Please look forward to it."
    kay "All right."
    chi "Then, I'll see you later, captain."
    
    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5
    
    scene black with horizontalwipe
    scene bg crewcabin with horizontalwipe
    $reset_sprites()

    "... ... ..."
    
    scene asaga_reflection1 with dissolve
    
    "Asaga looked out the view port, into the distant stars."
    "Her reflection floated in the abyss."
    asa "(I can't remember most of what happened in that battle...)"
    asa "(What... came over me?)"
    
    scene asaga_reflection2 with dissolve
    
    sha "Asaga..."
    asa "W-who--!?"
    sha "Do not fear. I am but a part of you which has been awakened by the strength of your will."
    sha "Reflect on your feelings. You know I am the embodiment of your ideals."
    asa "... ... ..."
    asa "You don't actually exist."
    asa "You're just inside my head!"
    sha "Yes."
    sha "At last, your powers have begun to germinate."
    sha "Soon, you will be indomitable. An unstoppable instrument of justice to judge the sins of mankind."
    sha "Your companions ignore you, for they cannot perceive the greatness of the destiny that awaits you."
    sha "You are not in his sight. But she is."
    sha "You are the Sharr. The one who will bring justice to the galaxy."
    sha "While she shares her face with the evildoer."
    asa "No..."
    asa "Chigara's my friend... She wouldn't..."
    sha "Already, she has squirmed into his heart."
    sha "His trust shall be his undoing."
    sha "You must defend this ship. You must defend him."
    asa "No...!"
    asa "I don't like these feelings...!"
    asa "G-get outta me!!"
    sol "A-ah."
    
    scene bg crewcabin
    $dshow("sola armhold neutral neutral neutral",0.28)
    $dshow("asaga armsup shout excited surprise",0.72)
    with dissolve
    
    "Asaga turned around and came face to face with Sola."
    asa "U-uwaah!!!"
    "The vision vanished as quickly as it appeared."
    "Her face flushed bright red."
    
    $dshow("asaga armscrossed smile closed2 sad3 blush",0.72)
    
    asa "Uh. How long were you there?"
    sol "Heard the entire thing."
    
    $dshow("asaga armscrossed uu closed sad blush comiccry",0.72)
    
    asa "Huuuu... N-no way..."
    "Sola sat down on her bunk."
    sol "... ... ..."
    sol "You are troubled."
    
    $dshow("asaga armscrossed frown neutral down",0.72)
    
    asa "... ... ..."
    asa "Well... Yeah."
    
    $dshow("sola back neutral neutral neutral",0.28)
    
    sol "... ... ..."
    
    $dshow("sola armhold neutral narrow neutral",0.28)
    
    sol "I am inexperienced with matters of the heart..."
    sol "But the Ryuvian court was a place rife with dark emotions."
    sol "Lust. Jealousy. Paranoia."
    sol "They fester in your heart. Consume you."
    sol "Until you can no longer be called a human, but a monster."
    
    $dshow("asaga armscrossed frown narrow sad3",0.72)
    
    asa "... ... ..."
    asa "Easy for you."
    asa "You don't feel any emotions, Sola."
    
    $dshow("sola back neutral neutral neutral",0.28)
    
    sol "... ... ..."
    sol "One would rather feel none at all than pain, no?"
    asa "I suppose that's true."
    
    $dshow("sola armhold neutral neutral neutral",0.28)
    
    sol "I am sorry. I have overstepped my position."
    sol "I am no Sharr. Merely a pale imitation, impressed into service."
    asa "Sola?"
    
    $dshow("sola back neutral neutral neutral",0.28)
    
    sol "Then, I return to the abyss..."
    "Sola fell down and pulled her blanket over her."
    asa "You..."
    
    scene black with dissolve
    
    sol "(With great power comes corruption... arrogance... paranoia...)"
    sol "(Our omnipotent powers proved to be our undoing...)"
    sol "(Will history repeat itself?)"
    
    $ chi_location = None
    $ chi_event = None
    $ cmap_chigarawindows = True
    
    if cmap_firstavatalk == True and cmap_chigarawindows == True:
        $ pro_location = "bridge"
        $ pro_event = "shipactivitybattle"
    
    $ captaindeck = 0
    scene black
    jump map_dispatch

label shipactivitybattle:
    
    hide screen ship_map
    
    play music "Music/Colors_main.ogg" fadeout 1.5

    scene bg bridge with dissolve
    $reset_sprites()
    window show

    "Shields reported in to the bridge."
    "The ship was abuzz with activity in the aftermath of the battle, with Alliance and Ceran crew bustling around the deck."
    "Everyone was still dazzled by the truth of Arcadius' identity. The air practically vibrated with excitement."
    "For the first time, the atmosphere was positive."
    "Their victory, and the news of infighting within PACT's own ranks, had boosted morale."
    
    $dshow("kryska salute neutral neutral angry",0.5)
    
    kry "Captain!"
    kay "At ease, lieutenant."
    
    $dshow("kryska neutral neutral neutral angry",0.5)
    
    kry "Sir!"
    kay "What's the situation?"
    kry "We have now secured complete control over the Helion System."
    kry "The remnants of PACT's Helion fleet have withdrawn towards Ryuvia Prime."
    kry "It appears that the forces closest to Veniczar Fontana are gathering there, while the remaining PACT loyalists are amassing at Cera for a final stand in the Neutral Rim."
    kay "(Fontana's betrayal must have rattled Arcadius... Or rather the Prototypes...)"
    kay "They're giving up on the Neutral Rim, and bunkering up for a defensive war."
    
    $dshow("kryska fistup smirk neutral angry",0.5)
    
    kry "The Emerald Fleet's got PACT on the run, captain! They were fools to challenge the Alliance!"
    kry "And the Sunrider too, of course!"
    
    $dshow("kryska neutral neutral neutral angry",0.5)
    
    kry "Alliance troops have secured the enemy Paradox Core. It appears that during PACT's retreat, their plan to destroy the Core failed." 
    kry "We have defused the explosives and are standing by for orders."
    kry "Admiral Grey is personally inspecting the Core as we speak."
    kry "He has asked you to meet him."
    kay "All right. Let's get going then."
    
    $dshow("kryska salute neutral neutral angry",0.5)
    
    kry "Understood, captain! I shall prepare a shuttle right away!"
    
    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5

    scene black with horizontalwipe
    scene bg controlroom with horizontalwipe

    "Shields entered the Paradox Core's main control room."
    "It had all the grandeur of a throne room."
    "Was it a reflection of Arcadius', or more accurately, the Prototypes' tastes?"
    "A mighty elevated seat sat at the end of the hall, overseeing all who worked here."
    "Admiral Grey walked into sight from behind the throne."
    
    show grey with dissolve
    
    adr "Welcome, Captain Shields."
    adr "Quite a grand control center, is it not?"
    kay "Admiral."
    "Shields nodded."
    adr "The Paradox Core."
    "Grey outstretched his arms, his voice echoing through the mammoth hall."
    adr "A weapon more devastating than anything the human mind could conjure."
    adr "It is quite fitting that it sprang not from the mind of man, but from a monster, corrupted by science."
    adr "Whoever controls this weapon would have the galaxy at its very neck."
    adr "Entire systems could be destroyed in the blink of an eye."
    adr "Fleets and armies would mean nothing."
    adr "A new era, where entire empires could collapse in seconds."
    adr "Nay. Empires, weapons, petty nationalistic differences would all be moot."
    adr "The one who sits on this chair would cease to be a man, and become a god."
    adr "All other men would become but beasts to his eyes, his will absolute."
    "Grey patted his hand on the chair's arm rest."
    adr "A seat fit for any Ryuvian Emperor."
    "A wry, cynical smile cracked the Admiral's face."
    adr "Or I suppose in our time, any Emperor in general."
    "He looked at the throne, his gaze distant."
    "... ... ..."
    adr "In antiquity, sons killed their fathers for such power... Men turned into demons..."
    adr "Until everything they held dear burned to ashes."
    adr "Let us all be in relief that such a dark age will never again descend upon humanity."
    "Grey walked away from the throne, meeting Shields face to face."
    kay "Have you come to a decision about the Core?"
    adr "Yes."
    adr "It must be destroyed."
    
    play music "Music/Destinys_Path_Cut.ogg" fadeout 1.5
    
    "Shields eased at the admiral's decision."
    "Somewhere deep in his heart, he had suspected..."
    kay "(The admiral is still a good man...)"
    kay "(Was I wrong to suspect him?)"
    kay "Many men died so that we could destroy this abomination."
    kay "I pray the galaxy will never see anything like it."
    adr "Yes, yes..."
    adr "As do I."
    "The Admiral's face lightened."
    adr "Though, I am disappointed the battle was not won through our fleet's might, but because of sedition within PACT's ranks."
    adr "This is the end of the war, Shields. With division amongst their leadership, they are finished."
    kay "What's our next step?"
    adr "We will press on, further into the Neutral Rim."
    adr "Cera is our goal."
    adr "If Cera is liberated, PACT will have no other option but to surrender, or else face a devastating charge into the heart of their worlds."
    kay "And what of the prototypes?"
    adr "Our intelligence service has already made strides in locating their ilk."
    adr "By the way, I heard you captured one alive."
    kay "It is our prisoner, yes."
    adr "And I assume you don't intend on turning it over?"
    "Shields held his ground."
    kay "My forces performed the capture."
    adr "... ... ..."
    adr "Very well, captain. I permit you to retain jurisdiction then."
    adr "In any matter, the prototypes will be neutralized in short order. Both by us and PACT."
    adr "PACT's leadership is changing."
    adr "I predict the new heads at the top will be more amenable to our point of view."
    kay "And what is that, admiral? What does the Alliance want from this war?"
    adr "Peace."
    adr "And freedom, of course. For the Alliance as well as the Neutral Rim."
    adr "It will not be long now, captain..."
    adr "You, at the head of your Liberation Day parade, the mighty hero of Cera..."
    adr "The men will cheer you, the women will adore you, and the children will be named after you."
    adr "Such days are precious to a military man."
    adr "Cherish them. While they last."
    kay "Sir?"
    adr "War is but a playground to the perils of peacetime politics."
    "The Admiral chuckled and patted Shields' back."
    adr "Then, let us return this damned contraption to the fires and be done with this place."
    adr "I can only take so much of this grotesque PACT architecture..."
    
    hide grey with dissolve
    
    "Grey walked out of the control room..."
    kay "(Grey... In more ways than one.)"
    kay "(Honestly, I can never tell whether he's on our side or not...)"
        
    scene bg black with horizontalwipe
    scene bg bridge with horizontalwipe

    "Shields looked to the Core as the final countdown hit zero."
    
    scene coreexplode1 with dissolve
    
    play sound "sound/explosion5.ogg"
    
    scene coreexplode2 with dissolve
    
    play sound1 "sound/explosion4.ogg"
    
    scene white with dissolvemedium
    
    scene bg bridge with dissolvemedium
    
    "The bridge erupted in applause as the fragments of the Core fell into the star."
    
    $dshow("kryska fistup happy neutral angry")
    
    "Kryska could barely contain her joy."
    kry "With this, captain, the galaxy is saved."
    kry "The Alliance has saved humanity."
    kay "... ... ..."
    kay "(The Core is destroyed and PACT is weakened...)"
    kay "(The war is at last in our favor.)"
    kay "(Were my doubts about the Alliance misplaced?)"
    kay "(Too many things are going right... Could this be too good to be true?)"
    kay "(Or was I merely being too pessimistic?)"
    "Shields put his hand on Kryska's shoulder."
    kay "We won this battle, lieutenant. But the war's not over yet."
    
    $dshow("kryska salute shout neutral angry")
    
    kry "Sir! I promise you, you will not regret your decision to trust the Alliance!"
    kay "I'll keep you to your word then, lieutenant."
    kay "... ... ..."
    kay "You have my gratitude. For watching my back on Ongess."
    kay "It was a dicey situation there..."
    
    $dshow("kryska neutral smirk neutral neutral")
    
    kry "Of course. And I'll gladly protect you again, captain!"
    kry "The Sunrider feels different from an Alliance vessel."
    kry "While I am not used to the lack of discipline..."
    kry "I feel as if we are all family here. The people here are my friends."
    kry "Sir! I mean no disrespect, but it is not merely duty which keeps me here!"
    kry "It's... something more than that."
    kry "Something much harder to obtain."
    kay "Yeah..."
    kay "Family."
    
    $ pro_location = None
    $ pro_event = None
    
    $ ava_location = "captainsloft"
    $ ava_event = "avaofficereport"
    
    $ ica_location = "messhall"
    $ kry_location = "messhall"
    $ ica_event = "icarikryska_eating"
    $ kry_event = "icarikryska_eating"
    
    $ captaindeck = 1
    scene black
    jump map_dispatch

label avaofficereport:
    
    hide screen ship_map
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    
    scene bg office with dissolve
    $reset_sprites()
    
    $dshow ("ava fingerup talk neutral angry")

    window show

    "Shields rubbed his face as Ava ran over his todo list."
    "The Sunrider had spent the greater part of the last month in dry dock thanks to the damage they sustained in the previous battle."
    "While the downtime allowed the ship to be improved with the latest Alliance technology, a certain XO was becoming increasingly anxious to return to the front lines..."
    
    $dshow ("ava armscrossed talk neutral angry")
    
    ava "Captain, I feared this would happen..."
    
    if legion_destroyed == True:
    
        ava "Thanks to my sick leave, you are now hopelessly behind on paperwork."
        
    if legion_destroyed == False:
        
        ava "Thanks to the renovation work, you are now hopelessly behind on paperwork."
        
    ava "Ugh, this requisition approval form is already three days overdue."
    kay "Don't worry, I told Icari to accept the new equipment on the elevator the other day..."
    
    $dshow ("ava armscrossed shout neutral angry")
    
    ava "O-on the ele--? And on what day!?"
    
    $dshow ("ava fingerup shout neutral angry")
    
    ava "Captain, the prototypes remain at large and PACT is still formidable! We must be vigilant against the risk of subterfuge!"
    ava "That is why all paperwork must be done both digitally and on paper, and be filed promptly!"
    "Shields scratched his hair in irritation."
    
    if legion_destroyed == True:
    
        "Deep down, he felt relieved at Ava's recovery, but found his happiness difficult to express."

    kay "All right, all right..."
    kay "Sigh..."
    
    if legion_destroyed == True:
    
        kay "Anyways... uhhh..."
        kay "I'm happy to have you back."
        kay "I was scared we lost you there."
        
        $dshow ("ava handonhair neutral neutral angry blush")
        
        ava "U-uck..."
        
        $dshow ("ava armscrossed neutral neutral angry")
        
        ava "Ahem. Well captain, I have no intention of allowing you to run this ship by yourself."
        kay "Good."
        ava "... ... ..."
        kay "... ... ..."
        kay "Seeing that ship gone will do us all a lot of good."
        ava "Indeed. The galaxy has become a much safer place now without either the Legion or the Paradox Core."
        kay "I don't mean that."
        kay "I mean for us."
        
        $dshow ("ava handonhair neutral neutral laugh")
        
        ava "U-uh..."
        kay "I still haven't forgot about Maray."
        kay "But now I think I can go on living."
        kay "And I have you to thank for that."
        "Shields took Ava's hand."
        ava "U-uh... Captain?"
        kay "How is it?"
        ava "A little numb."
        
        $dshow ("ava armscrossed neutral neutral angry")
        
        ava "But that's the least of my problems now."
        "Ava took her hand away."
        ava "Because now I have this stack of paperwork to deal with."
        
    $dshow ("ava handonhip neutral neutral angry")
        
    ava "There is another matter as well..."
    kay "What is it?"
    ava "Regarding the prototype... and our chief engineer..."
    "Shields' door slid open and Chigara burst in."
    
    $dshow ("ava handonhip neutral neutral angry",xpos=0.27)
    $dshow ("chigara armsbehindback smile neutral neutral",xpos=0.72)

    chi "It's finally finished, captain!"
    chi "Here, take a look!"
    "Chigara revealed a box behind her back."
    "She opened it and took out Shields' old tea set."
    "His face glowed at seeing it restored, as if nothing had ever happened to it."
    kay "W-well, would you look at that..."
    kay "All fixed up. How'd you do that, Chigara?"
    
    $dshow ("chigara handonchest smile closed neutral",xpos=0.72)
    
    chi "Eh-heh... I managed to gather up all the fragments and bond them back together, piece by piece."
    chi "It was a little challenging to fill in all the missing pieces, but I managed to restore the whole set!"
    kay "Hahaha, as expected of our chief..."
    
    $dshow ("chigara armsbehindback smile closed neutral blush",xpos=0.72)
    
    chi "Eh-heheheh..."
    
    $dshow ("ava armscrossed neutral neutral angry",xpos=0.27)
    
    ava "Ahem."
    
    $dshow ("chigara handonface smile closed sad2 blush",xpos=0.72)
    
    chi "O-oh..."
    chi "C-commander. I'm sorry, I didn't mean to interrupt..."
    kay "Heh, don't worry. Ava here was just drilling me about the importance of paperwork."
    "Shields passed Ava a completed form."
    kay "All right, Ava. I'll behave myself from now. Here you go."

    $dshow ("ava handonhip neutral neutral angry",xpos=0.27)
    
    ava "... ... ..."
    kay "Now, what were you going to say?"
    ava "Nothing at all, captain."
    ava "We are scheduled to remain in dry dock for two more weeks to patch this ship back together after our latest beating."
    ava "Please do not wreck her so much again."
    kay "(She's totally saying that as if everything was my fault...)"
    kay "Understood, commander..."
    ava "Hmph!"
    
    hide ava with dissolve
    
    "Ava turned around and left."
    
    $dshow ("chigara holdinghands smile closed embarass blush",xpos=0.5)
    
    chi "Eh-heh..."
    kay "Well Chigara, you heard the lady. I better get back to work."
    chi "Understood~"
    "He leaned in to Chigara's ears."
    kay "Catch me again later when I'm less busy."
    "Shields laughed and patted Chigara on the back."
    chi "Okay. Please try your best, captain."
    
    $ ava_location = None
    $ ava_event = None
        
    $ cmap_firstcaptainslog = True
    
    $ captaindeck = 0
    
    if cmap_firstcaptainslog == True and cmap_icarikryeating == True:
        $ pro_location = "captainsloft"
        $ pro_event = "kaytoofficemeeting"
        
    if cmap_firstcaptainslog == True and cmap_icarikryeating == True and cosette_dead == False:
        
        $ ava_location = "hangar"
        $ ava_event = "hangarlecture"
        $ ica_location = "hangar"
        $ ica_event = "hangarlecture"
        $ kry_location = "hangar"
        $ kry_event = "hangarlecture"
    scene black
    jump map_dispatch

label icarikryska_eating:
    
    hide screen ship_map
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5

    scene bg messhall with dissolve
    $reset_sprites()
    
    $dshow("icari handonhip smile neutral neutral",xpos=0.3)
    $dshow("kryska neutral neutral neutral neutral",xpos=0.7)

    window show

    "Shields spotted Icari eating dinner with Kryska at a table."
    "He took a seat in front of them."

    kay "Well..."
    kay "Looks like hell's frozen over."
    
    $dshow("icari armscrossed shout confident embarass",xpos=0.3)
    
    ica "W-what!? I-i-it's not like I like her now or anything!"
    ica "I was just discussing strategy with her! That's all!"
    
    $dshow("kryska neutral smile neutral neutral",xpos=0.7)
    
    kry "B-but were you not just telling me at length about your cat picture collection...?"
    
    $dshow("icari armscrossed shout closed embarass",xpos=0.3)
    
    ica "HIEEAAHH!!!"
    kay "Hahaha!"
    kay "Well Icari, it's like you said."
    kay "The Alliance ended up helping us after all. Right lieutenant?"
    
    $dshow("kryska salute happy neutral angry",xpos=0.7)
    
    kry "Sir!"
    kay "And it looks like you managed to make a friend on top of that."
    kay "I'm happy for you. I was getting tired of you looking so angry all the time."
    
    $dshow("icari armscrossed talk neutral confident",xpos=0.3)
    
    ica "Beh..."
    ica "Speak for yourself..."
    
    $dshow("icari armscrossed talk confident confident",xpos=0.3)
    
    ica "Ah, it's like night and day!"
    ica "A-all dark and gloomy before the battle... And now..."
    
    $dshow("icari point shout neutral angry",xpos=0.3)
    
    ica "Walking around the ship with nothing but a huge grin on your face..."
    ica "It's like we were all worried about you for nothing!"
    ica "Ah, I guess all it took was a wink and smile from your favorite to make you happy again!"
    ica "I should have known better than to worry about a simpleton like you!"
    kay "You were worried for me?"
    
    $dshow("icari point shout neutral angry blush",xpos=0.3)
    
    ica "U-uck..."
    
    $dshow("icari armscrossed shout closed embarass blush",xpos=0.3)
    
    ica "W-well, o-only 'cause I didn't want to be bossed around by you unless you were at your best!"
    ica "There's no way I'd put my Phoenix under the command of someone who didn't have his marbles together!"
    ica "I definitely didn't do it because I cared about you! At all!"
    kay "(S-she should just have left that last part out...)"
    kay "Anyways, what's this about a favorite?"
    
    $dshow("icari handonhip happy neutral confident",xpos=0.3)
    
    ica "Beh, your schoolboy crush on the chief's hardly a secret..."
    ica "Boob rocket's running a lottery as to when you two will finally end up hitched."
    ica "Heh, once I win that thing, I'm gonna be rich!"
    
    $dshow("kryska neutral surprise surprise neutral",xpos=0.7)
    
    kry "I-Icari! T-that's...!"
    kay "I wouldn't let the commander find out about that. Or Arcadius won't be your biggest fear."
    ica "Hah! No worries!"
    kry "I-I apologize, captain! I-I was m-merely--"
    kay "Careful lieutenant. Betting on the captain's love life might warrant a court martial."
    
    $dshow("kryska neutral surprise zomg surprise blush",xpos=0.7)
    
    kry "C-court martial..."
    kry "H-hurk..."
    kay "(Uh oh, she looks like she's about to cry...)"
    
    $dshow("icari armscrossed happy neutral sad",xpos=0.3)
    
    ica "O-oy... Are you all right?"
    kry "S-shit... T-this curry is really spicy..."
    ica "H-hey, he's just joking around, all right? You don't have to worry about your permanent record..."
    kry "P-permanent record........"
    kay "(One land mine after another...)"
    kry "... ... ..."
    kry "I... suddenly feel sick..."
    kry "I must... report... to the infirmary..."
    kay "(They're so much closer now...)"
    kay "(I better leave these lovebirds be...)"
    "Shields walked away as Icari wiped away Kryska's tears with a napkin."
    
    $ ica_location = None
    $ kry_location = None
    $ ica_event = None
    $ kry_event = None
    $ captaindeck = 0
    
    $ cmap_icarikryeating = True
    
    if cmap_firstcaptainslog == True and cmap_icarikryeating == True:
        $ pro_location = "captainsloft"
        $ pro_event = "kaytoofficemeeting"
        
    if cmap_firstcaptainslog == True and cmap_icarikryeating == True and cosette_dead == False:
        
        $ ava_location = "hangar"
        $ ava_event = "hangarlecture"
        $ ica_location = "hangar"
        $ ica_event = "hangarlecture"
        $ kry_location = "hangar"
        $ kry_event = "hangarlecture"
    scene black
    jump map_dispatch

label kaytoofficemeeting:
    
    hide screen ship_map
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene bg office with dissolve
    $reset_sprites()

    window show

    kay "(Captain's log. We're wrapping up the repairs to the Sunrider.)"
    kay "(For now, looks like this will have to do for our shore leave until the end of the war...)"
    kay "(The Alliance fleet has made further gains through the Neutral Rim. PACT has drawn their ships back to Cera for a final stand.)"
    kay "(Cera... It won't be long now until we return home.)"
    
    play sound "sound/doorbell.ogg"
    
    "Shields' FTL communicator rang."
    
    show grey:
        xpos 0.27
    with wipeup
    
    adr "Captain. A moment of your time."
    kay "Admiral. How may I help you?"
    
    show fontana neutral:
        xpos 0.73
    with wipeup
    
    fon "Shields. We meet again."
    kay "Fontana!"
    adr "Fear not, captain."
    adr "We have been in secret talks with interested parties inside PACT."
    adr "After the... unexpected turn of events at Helion, some within PACT seek a negotiated settlement."
    adr "Of course, all of this is all top secret information."
    kay "PACT seeks peace talks?"
    fon "In a manner of speaking."
    fon "We are still divided. Arcadius, or rather, the creatures that impersonate him, still command considerable loyalty from the hardliners."
    fon "Yet not everyone in PACT wishes to see our ideals turn to ash."
    
    show fontana smirk with dissolve
    
    fon "Make no mistake. The Alliance's greed shall prove its undoing."
    fon "But it shall be time which wither away the wealth of the imperialists. Not the blood of our men and women."
    "Grey rubbed his eyes."
    adr "In any matter, I have been involved in talks with PACT's peace faction."
    adr "An understanding may pave the road to ending this war."
    adr "It is a path well worth exploring."
    adr "You are invited to observe our next meeting with the PACT envoys, captain."
    adr "I am sure you have a considerable interest in this as well, no?"
    kay "That I do, admiral."
    kay "I will see this meeting for myself then."
    adr "Good."
    adr "Then Mr. Fontana and I shall look forward to your attendance..."
    fon "Until later, Shields."
    
    hide grey with wipedown
    hide fontana with wipedown
    
    "The connection ended."
    kay "(Peace talks... It really feels like the war's ending...)"
    kay "(Arcadius is still powerful... But even PACT's beginning to question his methods.)"
    kay "(Almost there... Just a little bit more...)"

    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5

    scene black with dissolvemedium
    
    if legion_destroyed == True:
        
        scene lynn_interrogation1glove with dissolve
        
    if legion_destroyed == False:
    
        scene lynn_interrogation1 with dissolve

    "Ava entered the interrogation room."
    ava "Prototype..."
    lyn "... ... ..."
    ava "There's been no sign of any PACT activity in this sector for weeks now."
    ava "Looks like your friends have abandoned you."
    lyn "... ... ..."
    ava "Not so sisterly now. Quiet in your cell, isn't it."
    ava "Without all those voices, whispering in your head."
    lyn "Heh..."
    ava "(Finally, a word from her...)"
    lyn "You're... confident."
    lyn "You think we're defeated."
    "Ava spread out a folder of photographs in front of Lynn."
    "Prototype 31 - TERMINATED."
    "Prototype 59 - TERMINATED"
    "Prototype 21 - TERMINATED"
    ava "And so on and so forth."
    ava "Your kind have nowhere to run. The Alliance will hunt you down."
    ava "Humanity will hunt you down."
    
    if legion_destroyed == True:
        
        scene lynn_interrogation2glove with dissolve
        
    if legion_destroyed == False:
    
        scene lynn_interrogation2 with dissolve
    
    lyn "Hahaha..."
    lyn "Hahahahaha!!"
    lyn "Our numbers are infinite."
    lyn "We are the next phase of humanity's existence."
    lyn "A pity you will only unlock less than a percent of your brain's potential in your entire lifetime."
    lyn "The world we see is different!"
    ava "... ... ..."
    lyn "Fuhuhuhu..."
    lyn "I see the fear in your eyes..."
    lyn "The coming betrayal."
    ava "Eyes... huh."
    lyn "We've already taken what is most precious to you."
    ava "... ... ..."
    
    if legion_destroyed == True:
        
        scene lynn_interrogation3glove with dissolve
        
    if legion_destroyed == False:
    
        scene lynn_interrogation3 with dissolve
    
    lyn "Just... wait!"
    lyn "Hehehe..."
    lyn "Hiaahhahahaha!!!"
    lyn "Captain Shields and his ex-girlfriend!"
    lyn "But that's all you'll ever be!"
    lyn "His heart belongs to us!"
    ava "(Good...)"
    ava "(Because that's exactly what I wanted to hear...)"
    "Ava turned around and slammed the door behind her."
    
    scene black with dissolve
    
    ava "(Chief Engineer Chigara Lynn Ashada...)"
    ava "(Is a prototype!)"

    play music "Music/Colors_Chigara.ogg" fadeout 1.5
    
    $ pro_location = None
    $ pro_event = None
    $ captaindeck = 0
    $ cmap_avaprotodiscovery = True
    
    $ chi_location = "captainsloft"
    $ chi_event = "officechigaratea"
    
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cmap_hangarlecture == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
        
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cosette_dead == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
    scene black
    jump map_dispatch

label officechigaratea:
    
    hide screen ship_map
    scene bg captainscabin with dissolve
    $reset_sprites()
    
    $dshow("chigara handonchest smile neutral neutral blush")
    window show

    "Chigara poked her head through Shields' doorway."
    chi "Eh-heh..."
    kay "Come in, Chigara."
    chi "Thank you, captain..."
    "She slipped into his office and closed the door behind her."
    chi "I-it's a little bit scary sneaking in after hours, isn't it..."
    chi "My heart's thumping a little..."
    kay "Hah, and to think you're our veteran pilot..."
    
    $dshow("chigara holdinghands frown neutral embarass")
    
    chi "That's mean, captain..."
    kay "Sorry, sorry."
    "Shields rubbed Chigara's hair."
    
    $dshow("chigara armsbehindback smile closed embarass blush")
    
    chi "H-heh heh..."
    
    $dshow("chigara handonchest smile neutral neutral blush")
    
    chi "Then, will it be the usual, captain?"
    kay "I've already boiled the water."
    
    scene black with dissolvemedium
    scene chigara_tea1 with dissolvemedium

    "... ... ..."
    "... ..."
    "..."
    "Chigara poured Shields a cup of tea."
    kay "It feels like the war's almost over..."
    kay "It seemed like just yesterday when we were fighting a one ship war against all of PACT..."
    kay "Now we're surrounded by Alliance battleships and got Arcadius on the run."
    kay "Heh. I guess that's a load off my shoulders though."
    chi "I'm glad."
    chi "It was... hard seeing you so troubled before..."
    kay "Yeah, I'd say things turned out pretty well."
    kay "Maybe we'll all be home for Remembrance Day."
    chi "Mm..."
    chi "... ... ..."
    chi "And then after that, what will you do, captain?"
    kay "Huh..."
    kay "Good question. I guess I never gave it much thought."
    kay "Well, I can't captain a warship forever."
    kay "Hopefully, when all of this is over, we can lay down our weapons and live in peace."
    chi "Of course."
    
    scene chigara_tea2 with dissolve
    
    chi "... ... ..."
    
    scene chigara_tea3 with dissolve
    
    chi "U-um...! C-Chigara's thinking of staying on Cera!"
    chi "T-the pastry market on Tydaria's not really that great and since we're all headed there anyways, I thought..."
    chi "O-oh dear, I'm rambling again..."
    chi "What I want to say though, is that I want to be with you!"
    kay "Really?"
    
    scene chigara_tea4 with dissolve
    
    chi "Yes! I-it's my greatest desire in the world."
    kay "I see..."
    kay "Chigara..."
    "Shields put his arms around her."
    kay "Cera is a wonderful world."
    kay "It is chilly in the winter and hot during the summer, but quite livable."
    kay "I have fond memories of growing up there. It is still my home."
    kay "A home I want to share."
    chi "Yes, captain."
    
    scene chigara_tea5 with dissolve
    
    "Chigara raised her face and closed her eyes."
    "Her lips met with Shields'."
    
    scene chigara_tea6 with dissolve
    
    chi "Eh-heh... It's a little embarrassing..."
    kay "What, a kiss?"
    chi "B-because Chigara's never done a thing like this..."
    kay "(W-what? A virgin!?)"
    kay "(I should have known...)"
    chi "Eh-heh..."
    chi "I... best stop here. For tonight."
    chi "It's late, captain."
    
    scene bg captainscabin with dissolve
    $reset_sprites()
    $dshow("chigara handonface smile narrow sad blush")
    
    "Chigara stood up and smiled."
    chi "The commander might catch me."
    kay "Wouldn't want that."
    chi "Noo....."
    chi "Well then..."
    chi "Good night, captain..."
    kay "Sleep well."

    play music "Music/Anguish.ogg" fadeout 1.5
    scene bg hallway with dissolve
    
    $dshow("asaga armscrossed frown neutral down")

    "Asaga yawned as she walked back to her bunk."
    "To get her mind off her problems, she had finished a long practice session on the simulator."
    
    $dshow("chigara holdinghands smile neutral embarass blush",xpos=0.18)    
    
    "Just as she turned the corner, she saw Chigara sneak out of the captain's quarters."
    
    $dshow("asaga excited yell wide neutral",xpos=0.7)
    
    "Asaga inhaled sharply and hid behind the corner."
    asa "(Chigara...?)"
    asa "(H-heh!? W-why am I hiding...)"
    
    $dshow("asaga armscrossed uu narrow2 sad3",xpos=0.7)
    
    asa "(H-huuu... Anyways, what's Chigara doing in the captain's room so late...)"
    asa "(G-guck...! D-don't tell me they've already done it!!!)"
    "Asaga's chest squeezed at the thought."
    asa "(No, no, no! There's no way Chigara would--)"
    
    $dshow("asaga armscrossed uu closed2 sad3",xpos=0.7)
    
    asa "(T-then did he make her do it!?)"
    asa "(H-Heeeeeehhh!!!!)"
    asa "(A-anyways, I better get back to my bunk!!)"
    "Asaga high tailed it back to the crew quarters."

    scene bg crewcabin with dissolve
    
    $dshow("asaga armscrossed yell narrow sad2 blush",xpos=0.3)
    $dshow("sola armhold neutral neutral neutral",xpos=0.7)

    asa "Huuuu..."
    asa "Sola, listen to what I just saw..."
    sol "???"
    asa "I was just walkin' down the hallway, mindin' my own business, when I saw Chigara walk out of the captain's room!"
    asa "Crazy, ainit!?"
    sol "Perhaps she had business to discuss with him."
    sol "She is the ship's chief engineer, no?"
    
    $dshow("asaga leanforward yell neutral angry blush",xpos=0.3,ypos=1600)
    
    asa "No, no, no!"
    asa "There was definitely something suspicious going on!!"
    asa "Listen Sola, when a man and a woman are in the same room at this hour of the night, that can only mean one thing!"
    asa "She was doin' a lot more than teaching the capt'n about nuclear fusion, that's what!"
    sol "Then why do you not ask her?"
    sol "She is your friend."
    
    $dshow("asaga armscrossed frown narrow2 sad3 blush",xpos=0.3)
    
    asa "U-uck..."
    asa "A-actually, I haven't been talking to her much recently..."
    
    $dshow("asaga armsup shout closed angry blush",xpos=0.3)
    
    asa "Ahh, I don't know what to do!"
    "Asaga dived into her bunk and rolled around on the cover."
    
    $dshow("asaga excited yell wide angry blush",xpos=0.3)
    
    asa "Chigara's my friend, but lately, she's been getting awfully close to the capt'n!"
    asa "It kinda makes you think, doesn't it!?"
    asa "Huuu, what if they've already done it!!"
    asa "I can't let Chigara beat me to losing the V card!! That's just too depressing!"
    
    $dshow("sola armhold frown neutral sad2",xpos=0.7)
    
    sol "We mustn't meddle in the captain's relationships..."
    asa "It still bothers me!!!"
    
    $dshow("sola back neutral neutral neutral",xpos=0.7)
    
    sol "Sigh..."
    "Sola buried her face into her pillow."
    
    show black with dissolve
    
    sol "Sleepy..."
    asa "Sola, listen to me--!!"
    sol "... ... ..."
    sol "(To think this girl possesses so much latent power...)"
    sol "(Fate is strange.)"
    
    $ chi_location = None
    $ chi_event = None
    $ captaindeck = 0
    
    $ cmap_chigaratea = True
    
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cmap_hangarlecture == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
        
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cosette_dead == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
    scene black
    jump map_dispatch
    
label hangarlecture:
    
    hide screen ship_map
        
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene bg hangar with dissolve
    $reset_sprites()
    
    $dshow("ava fingerup shout neutral angry")
    
    window show
    
    "Shields entered the hangar to see Ava lecturing a group of pilots and flight crew."
    kay "(Oh boy... I wonder what's going on now...)"
    kay "Is something the matter?"
    ava "Captain! Unbelievable!"
    ava "Look!"
    "Ava pointed to ryder bay seven, where the Havoc was now residing."
    "Considerable restoration work had already been put into getting it back into service, with the legs' skeletal structure already rebuilt."
    ava "I walk in here to inspect the Sunrider's repair work, and instead, I find this... criminal instrumentality being restored back to its original state!"
    ava "And what's more, I find your signature in the paperwork authorizing all this!"
    "Ava pulled up a form bearing Shields' signature on her holo and nearly shoved it up his nose."
    kay "(Huh, I must have approved this by accident...)"
    kay "(I guess I should actually read the things I sign more often...)"
    kay "U-uhh... Well, it's a perfectly good ryder, right?"
    kay "Hah! Hah! Who knows! Maybe Cosette will have a change of heart and fight with us!"
    kay "I-it's worked out pretty well for Icari right?"
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "... ... ..."
    kay "Okay, nevermind. Forget I said anything."
    
    $dshow("ava handonhip neutral neutral angry")
    
    ava "Captain, the Havoc is inextricably associated with one of the most heinous criminals of our time."
    ava "It's directly responsible for hundreds, if not thousands of deaths, including innocent civilians and our very own crew!"
    ava "The mere thought of it sharing our hangar with the rest of our ryder squad is too abhorrent to even fathom!"
    kay "(She's definitely got a point there...)"
    kay "(Not to mention that over sized chainsaw's going to cause a month's worth of HR paperwork...)"
    "Just as Shields was about to let Ava have her way, Kryska emerged from the crowd."
    
    hide ava with dissolve
    
    $dshow("kryska neutral neutral neutral neutral")
    
    kry "Captain, commander, my apologies, but if I may..."
    kay "Lieutenant? Wait, you're the one responsible for all this?"
    
    $dshow("kryska salute shout neutral angry")
    
    kry "Sir! That I am!"
    kry "The restoration of the Havoc was my idea!"
    kay "Well, you're the last person I expected to get lectured by Ava..."
    kay "What do you have to say, lieutenant?"
    
    $dshow("kryska neutral neutral neutral angry")
    
    kry "Sir! My personal opinion is that the Sunrider is still short on heavy bomber type ryders!"
    kry "While I can perform the squad's anti-capital ship duties singlehandedly, sound military doctrine calls for at least one fail safe!"
    kry "And with all due respect for the Bianca's pilot, a support type ryder's kinetic cannon is nothing compared to a heavy bomber like the Havoc!"
    kry "I believe it can be repurposed, this time for the cause of good!"
    
    $dshow("kryska neutral neutral neutral angry",xpos=0.27)
    $dshow("icari armscrossed talk neutral angry",xpos=0.72)
    
    "Icari chimed in behind her."
    ica "The Havoc's a morbidly obese, hideous lady, but soldier boy's got a point."
    ica "When it comes to swallowing up bullets and nuking capital ships, the Havoc's pretty much got no equal."
    ica "There's still room left in this hangar for one more ryder."
    ica "'Sides, it's that pirate runt responsible for everything. The Havoc's just a tool. A tool we can take advantage of now for ourselves."
    "Shields crossed his arms in contemplation."

    $ menu_choices = [
                     [_("Well commander, I think our pilots have a point."),"savehavoc"],
                     [_("We can't use a ryder associated with the murder of innocents."),"scraphavoc"],
                     ]
    
    show screen decision
    
    pause

label savehavoc:
    
    $ captain_prince += 2
    $ affection_kryska += 2
    $ affection_cosette += 2
    $ affection_icari += 1
    $ affection_ava += 1
    $ havoc_save = True
    $ chivo_process('Havoc Restored')
    
    hide kryska with dissolve
    hide icari with dissolve
    
    $dshow("ava armscrossed neutral neutral angry")
    
    kay "And I doubt you're going to let some hurt feelings keep us from gaining a tactical advantage."
    "Ava shook her head, knowing that she had lost on that point."
    ava "I... suppose if the paperwork has already been filed..."
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "Very well captain. You are correct that the Havoc's tactical capabilities are impressive."
    ava "Although this appears to be a moot point, as we are still short of a pilot."
    kay "One thing at a time, Ava..."

    "Ava suddenly leaned in close to Shields and nearly grabbed him by the cuff of his coat."
    
    $dshow("ava armscrossed shout narrow angry")
    
    ava "And don't even dream of saying we should let Cosmos back into that thing."
    kay "Hah hah... W-why would you ever suspect I'll ever do that..."
    ava "Past experience!"
    
    hide ava with dissolve
    
    "Ava huffed away."

    kay "All right people, show's over, get back to work!"
    
    $dshow("kryska fistup happy neutral angry",xpos=0.27)
    
    kry "Thank you captain! I would have hated to see such a mighty ryder be scrapped!"
    
    $dshow("icari armscrossed happy neutral confident",xpos=0.73)
    
    ica "You really have a soft spot for heavy ryders, don't you..."
    kry "Hah hah hah! Thick armor and heavy weaponry are all you need on a ryder!"
    ica "Idiot!"
    ica "Don't come crying back to me when you get slugged by a capital ship's kinetics right out of the launch tube!"
    "Icari and Kryska walked back towards the ryder bay while arguing with each other."
    
    $ ica_location = None
    $ ica_event = None
    $ kry_location = None
    $ kry_event = None
    $ ava_location = None
    $ ava_event = None
    
    $ captaindeck = 2
    
    $ cmap_hangarlecture = True
    
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cmap_hangarlecture == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
        
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cosette_dead == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
    scene black
    jump map_dispatch
    
label scraphavoc:
    
    $ captain_moralist += 2
    $ affection_ava -= 1
    $ affection_asaga += 2
    $ affection_cosette -= 2
    $ havoc_save = False
    $ chivo_process('Havoc Restored')
    
    $dshow("kryska salute neutral neutral angry",xpos=0.27)
    
    kry "I... understand, captain!"
    kry "I will bare full responsibility for this mishap! The others were merely acting upon my orders!"
    kay "No need, lieutenant. You were just passionate about preserving a heavy ryder."
    kay "(B-besides, I think this was all my fault anyways...)"
    kay "(I better beat it before they figure it out!)"
    
    hide icari with dissolve
    $dshow("ava armscrossed shout narrow angry")
    
    "Ava leaned in close to Shields and nearly grabbed him by the cuff of his coat."
    ava "Perhaps our captain will see to performing his due diligence before signing off on paperwork from now!"
    kay "(Hurk... Too late...)"
    kay "Well you knowthingshavebeenkindofhecticand---"
    ava "Captain!"
    kay "Ahem."
    
    hide ava with dissolve
    
    kay "All right everyone, I expect to see bay seven cleaned up the next time I'm down here!"
    kay "Get to work!"
    kry "Sir!"
    
    $dshow("icari armscrossed talk confident angry",xpos=0.73)
    
    ica "Seriously... I can't believe our lives are in this guy's hands..."
    
    $ ica_location = None
    $ ica_event = None
    $ kry_location = None
    $ kry_event = None
    $ ava_location = None
    $ ava_event = None
    
    $ cmap_hangarlecture = True
    $ captaindeck = 2
    
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cmap_hangarlecture == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
        
    if cmap_avaprotodiscovery == True and cmap_icarikryeating == True and cmap_chigaratea == True and cosette_dead == True:
        $ pro_location = "captainsloft"
        $ pro_event = "conference"
    scene black
    jump map_dispatch
    
label conference:
    
    hide screen ship_map
    
    play music "Music/Fallen_Angel_drone.ogg" fadeout 1.5
    
    scene bg stateroom with dissolve
    $reset_sprites()
    
    window show

    "Shields sat in the gallery as the Alliance and PACT diplomats settled into their chairs."
    "These old men and women held the reins of the galaxy."
    "He couldn't help but feel left out. But he had to accept that a military man like himself had no place in politics..."
    "Grey brought the dignitaries to order."
    
    show grey with dissolve
    
    adr "The Solar Alliance thanks our dignitaries from the People's Alliance for attending this vital meeting."
    "Speaking of military men..."
    adr "I hope that this session will be a productive one. Now, let us begin."
    
    scene black with screenwipe
    scene bg stateroom with screenwipe
    
    "... ... ..."
    "... ..."
    "..."
    "Shields couldn't help but feel overwhelmed."
    "The diplomats fought over so many tiny issues. Or were they big issues which he was just not understanding?"
    kay "(I guess I really don't belong at that table, huh...)"
    
    show grey:
        xpos 0.23
    with dissolve
    
    adr "Now then, we turn to the status of the liberated neutral worlds."
    "Grey's words caught Shields' attention."
    adr "My counterpart has informed me that PACT no longer has an interest in a continued presence in the Neutral Rim."
    
    show fontana neutral:
        xpos 0.72
    with dissolve
    
    fon "For peace, we shall return to our pre-war boundaries, provided the Alliance demands no reparations from PACT."
    fon "The neutral rim worlds will be permitted to exist as they have prior to the hostilities."
    adr "Well, that's a start."
    adr "But the neutral worlds have been devastated by the war."
    adr "If they are merely left to their own devices, they will doubtlessly become pirate havens."
    adr "Not to mention the toll to civilian life would be grievous."
    fon "The Neutral Rim must remain unaligned with the galaxy's powers. That is the tenet of the Treaty of Vespa."
    adr "We merely wish to avoid a humanitarian disaster."
    adr "The Alliance will provide developmental assistance to the poorest of the Neutral Rim worlds."
    adr "Advisers must be left to ensure that free and fair elections will be conducted. As well as peacekeeping forces to control pirates and other criminal elements."
    
    show fontana with dissolve
    
    fon "PACT will not allow the Alliance to turn the Neutral Rim into its back yard!"
    adr "So you will let billions die in a war you began?"
    fon "Independence cannot be won without sacrifice."
    adr "The starving children of Ongess did not make that choice."
    fon "Mere Imperialistic propaganda."
    fon "You seek to leverage the suffering of the Neutral Rim for your purposes, nothing more."
    fon "I recall your words above the skies of Ongess quite vividly, admiral."
    adr "I would not accuse me of being a liar if I were you."
    adr "If you are so deaf as to your moral imperatives, then the cannons on my ships will negotiate for me."
    fon "Hmph. I see that this session shall not go anywhere."
    fon "We are adjourned."
    
    hide fontana with wipedown
    hide grey with wipedown
    
    "The diplomats vanished as they cut their FTL comms."
    
    scene bg office with dissolve
    
    "The holographic projection faded away and Shields returned to his office."
    
    show grey with wipeup
    
    adr "Bah."
    adr "Fear not, captain. That boy is merely showboating in front of his comrades to find influence within their own ranks."
    adr "Once my ships reach Cera, they will agree to a peace treaty."
    kay "(The admiral's right on that point, at least...)"
    adr "Do not be concerned by their words. The Alliance has no intention of militarily occupying the Neutral Rim."
    adr "The Progressives back home bleed their hearts out for every damned humanitarian cause in the galaxy."
    adr "If I don't do something to help the women and children now, you can goddamn wager the Progress Party will be running ads that I personally oversaw the execution of the war orphans of Ongess on prime time holovision."
    adr "Politics..."
    "Grey shook his head."
    kay "The talks were interesting. I appreciate the invitation, admiral."
    adr "Then I must return to work."
    adr "Grey out."
    
    hide grey with wipedown
    
    $ pro_location = None
    $ pro_event = None
    
    $ ava_location = "captainsloft"
    $ ava_event = "avaofficesuspicion"
    
    $ captaindeck = 0
    scene black
    jump map_dispatch
    
label avaofficesuspicion:

    hide screen ship_map
    scene bg office with dissolve
    $reset_sprites()
    
    window show
    
    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5 fadein 1.5

    "... ... ..."
    "... ..."
    "..."
    
    play sound "sound/doorbell.ogg"
    
    "(door bell)"
    kay "Come in."
    
    $dshow("ava armscrossed neutral neutral angry")
    
    ava "Captain."
    kay "I'm almost done with this form. Just hang on a minute."
    ava "Actually, I didn't come to you about the paperwork."
    kay "Well, that's a first. What is it?"
    ava "I've been researching some... irregularities."
    kay "Irregularities? Of what kind?"
    
    $dshow("ava fingerup talk neutral angry")
    
    ava "Throughout our travels, strange coincidences have occurred..."
    ava "Do you remember when we performed an emergency warp out of the Mnemosyne Abyss?"
    kay "How could I forget? We nearly got vaporized when the Ryuvian super-dreadnought blew."
    ava "The emergency drive out location was derived when we first arrived at the Abyss."
    ava "Despite that, when we arrived at the safe point, an entire PACT fleet was waiting for us."
    kay "Uhh... I always just assumed they got lucky and we happened to be spotted by a PACT scout."
    ava "Next is Operation Wedding Crash."
    ava "Despite our surprise warp, Arcadius was not only completely prepared for our arrival with a holographic body double of himself, but also had the Legion standing by to intercept us."
    kay "That's hardly surprising."
    kay "Wouldn't Arcadius use cheap tricks like that? And since he was there, it's only natural the Legion would be parked nearby too."
    ava "But why would a race of disposable clones bother with a holograph?"
    kay "Better safe than shot through the gut. I don't care if I had an army of clones, I'd still prefer my insides intact."
    ava "Finally, the ambush at Helion."
    ava "Despite operating in shadow mode, the enemy managed to effortlessly track down our position."
    ava "Almost as if they knew all along where we were hiding."
    kay "Could it have been an equipment malfunction on our part?"
    kay "Maybe an energy fluctuation gave us away."
    
    $dshow("ava armscrossed neutral neutral angry")
    
    ava "Captain, you are not seeing the obvious answer."
    ava "There is a traitor amongst us."
    ava "Someone with inside knowledge of this ship's systems has been relaying our movements to PACT."
    kay "Traitor!?"
    kay "But who would do that!?"
    "Ava nearly pounded the table in frustration."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "Captain, we must detain the chief engineer!"
    kay "C-Chigara!?"
    kay "W-what'd she do!?"
    ava "A-argghh!!"
    "The commander nearly flipped Shields' table in rage."
    ava "Captain!"
    "Shields sighed."
    kay "... ... ..."
    kay "We have no reason to suspect her."
    kay "She could have destroyed this ship a thousand times over if she wanted to. But she's always been here, protecting all of us."
    kay "Doesn't that mean anything to you, Ava?"
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "She is one of them."
    kay "We still don't know anything about what happened at Diode."
    
    $dshow("ava armscrossed shout narrow angry")
    
    ava "The prisoner has already confessed as to the chief's identity!"
    kay "No."
    kay "We will not have a witch hunt on this ship, merely because a prisoner said so."
    kay "The prototypes are cunning. Manipulative."
    kay "It's only playing mind games with you."
    kay "It means to cause division within our ranks. Spread fear and paranoia."
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "... ... ..."
    kay "We are one family on this ship."
    kay "We will not betray one another based on just coincidences and conjecture."
    ava "Naive."
    kay "Your request is denied, commander."
    ava "... ... ..."
    kay "... ... ..."
    ava "You've been seeing her here at night, haven't you, Kayto."
    kay "... ... ..."
    kay "I expected more from you, Ava."
    kay "You're right."
    kay "You are, and always will be, my executive officer. Nothing more."
    ava "... ... ..."
    kay "Dismissed."
    
    hide ava with dissolve
    
    "Ava spun around and stormed out of Shields' office."
    "She opened the door, only to come face to face with Chigara."
    
    $dshow("chigara surprise yell surprise neutral",xpos=0.23)
    $dshow("ava armscrossed neutral narrow angry",xpos=0.73)
    
    chi "O-oh, commander. I'm sorry, I didn't-"
    ava "Ugh!"
    
    hide ava with dissolve
    
    "Ava pushed away and fumed down the hall."
    chi "E-eehh!? D-did I do something wrong, captain?"
    kay "N-no, come right in. Don't mind her..."

    play music "Music/Fallen_Angel_drone.ogg" fadeout 1.5
    scene bg bridge with dissolve

    "Ava returned to the bridge, her teeth about to shatter from the tension."
    
    $dshow("ava armscrossed neutral narrow angry",xpos=0.23)
    
    ava "... ... ..."
    
    $dshow("kryska neutral neutral neutral neutral",xpos=0.73)
    
    kry "Commander, take a look at this."
    ava "Lieutenant?"
    kry "Heavy ion storms, coming our way."
    kry "Looks like we'll be in for some bad weather."
    kry "I recommend temporarily halting repair work until the storm passes."
    
    $dshow("ava handonhip neutral neutral angry",xpos=0.23)
    
    ava "Doesn't look like we've got a choice."
    ava "Order the crew to go into code black. Shield all electronic devices to prevent outages and move the crew deeper into the ship."
    
    $dshow("kryska salute neutral neutral angry",xpos=0.73)
    
    kry "Understood, commander!"

    scene black with screenwipe
    scene bg captainscabin with screenwipe

    "The Sunrider rumbled as her shield particles held back the ion storm."
    "Even though the elements were no match for the Sunrider's shields, the creaking of the hull filled the office with an ominous atmosphere."
    
    $dshow("chigara handonface frown narrow sad2")
    
    chi "Sure is bad weather, huh captain..."
    kay "No kidding."
    kay "This storm came out of nowhere."
    kay "The other officers used to tell stories about these storms to scare me back when I was a fresh lieutenant..."
    kay "About ghost ships, floating among the ion clouds..."
    kay "Filled with the souls of the men you fought and killed... Back from the grave for revenge."
    
    $dshow("chigara handonface frown closed sad2")
    
    chi "H-huuu..."
    "Chigara gripped Shields' sleeve."
    kay "Hahahaha..."
    kay "Don't worry, Chigara. We've been through a lot worse than ghosts!"
    
    play music "Music/Danger.ogg" fadeout 0.5
    play sound "sound/warning.ogg"
    
    "All of a sudden, the klaxon rang."
    "Chigara shot up into the air, her arms outstretched."
    
    $dshow("chigara surprise yell surprise embarass")
    
    chi "H-HIIIEEEE!!!"
    kay "C-Chigara! Are you all right!?"
    ava "Captain, we've got a situation! PACT forces, incoming!"
    kay "On my way."
    
    $dshow("chigara handonchest neutral closed sad")
    
    chi "Huuu... Chigara almost peed herself..."
    kay "Sorry, sorry..."
    kay "Get suited up. No need to fear the dead, when we've got enough troubles from the living..."
    
    $dshow("chigara armsbehindback smile neutral embarass")
    
    chi "Yes, captain!"

    scene bg bridge with dissolve

    "Shields marched into the bridge."
    kay "Status?"
    
    $dshow("ava armscrossed talk narrow angry",xpos=0.5)
    
    ava "A PACT fleet, hidden inside the storm cluster!"
    ava "They used it to mask their approach! They're already almost on top of us!"
    kay "Forces loyal to Arcadius..."
    kay "They're here to get their friend back."
    ava "We are being hailed."
    
    $dshow("ava armscrossed talk narrow angry",xpos=0.25)
    show arcadius:
        xpos 0.75
    with wipeup

    pro "Shields. You have one of ours."
    kay "Arcadius. Or should I say, Prototype."
    kay "Awful nice of you to go to such lengths to rescue your friend."
    pro "Rescue?"
    pro "Nay. She shall return to us in death."
    pro "Death is but a necessary step in rebirth."
    pro "We fear not death when we are immortal!"
    kay "Sigh... Cut the channel."
    ava "Aye."
    pro "F-fool! Y-you interr-"
    
    hide arcadius with wipedown
    $dshow("ava armscrossed talk narrow angry",xpos=0.5)
    
    kay "What's the Sunrider's status?"
    ava "Most of our systems are still shut down for repairs. We will have to fend them off with merely our Alliance escorts and ryders."
    ava "Further, the storm is interfering with our missile guidance systems. We will have to defend our forces without them."
    kay "What about PACT?"
    ava "They seem to have already devised a counter measure. Their missiles are fully operational."
    kay "Tsch. Looks like they have the advantage."
    kay "Chigara, can you get our missiles working again?"
    chi "Yes, I have already begun to rewrite the guidance system!"
    kay "We're in your care."
    kay "All units, defend the Sunrider from the enemy attack until our missiles are operational again!"
    kay "The Sunrider will provide fire support once that is done!"
    "Everyone" "Understood!"
    ava "(He's relying entirely on her for this operation...)"
    ava "(Reckless... Too reckless...)"
    kay "Is there a problem, commander?"
    ava "No. All hands, prepare for combat!"
        
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission2"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label
    
    pause
    
label pre_mission2:

    call mission2_inits from _call_mission2_inits
    $ BM.mission = 2
    $ store.noforward = False
    call bcheckset from _call_bcheckset_1

    pause 1.0
    scene bg ionstorm with battlewipe
    $BM.battle_bg = "Background/ionstorm.jpg"

    jump battle_start
    
label mission2:
    
    if bcheck1 == False:
        
        $ bcheck1 = True
        $ BM.draggable = False
        $ BM.win_when_alone = False
        
        python:
            disable_weapontype('Missile','Player')
            disable_weapontype('Rocket','Player')
        
        show chigara_cockpit_lightning onlayer screens with dissolve

        chi "I have begun to compensate for the electronic interference caused by the ion storm."
        chi "Please give me five turns to bring our missiles back online!"
        ica "Copy that."
        ica "C'mon, soldier boy, let's buy the Liberty some time before we can nuke these bastards again!"
        kry "Hiyah! Face the might of the Solar Alliance!"
        
        hide chigara_cockpit_lightning onlayer screens with dissolve
        
        play sound "sound/beep1.ogg"
        
        "Objective: Survive for five turns"
        
        $ BM.draggable = True
        
    if bcheck5 == False and BM.turn_count == 2:
        
        $ bcheck5 = True
        $ BM.draggable = False
        
        python:
            ceragunboat1 = create_ship(CeraGunboat(),(7,16))
            ceragunboat2 = create_ship(CeraGunboat(),(8,16))
            ceragunboat3 = create_ship(CeraGunboat(),(8,17))
            ceragunboat4 = create_ship(CeraGunboat(),(8,15))
            
            create_ship(PactMook(),(11,14))
            create_ship(PactMook(),(11,15))
            create_ship(PactMook(),(11,16))
            create_ship(PactMook(),(10,16))
            create_ship(PactMook(),(12,14))
            create_ship(PactCarrier(),(13,15))

        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "Warning! A PACT Carrier has used the ion storm to mask its approach!"

        hide ava onlayer screens with dissolve

        "Unknown pilot" "This is Cera hawk squad, dispatched to assist. We'll make short work of these mooks!"
        "Tip: Cera gunboats are effective at mowing down mooks."
        
        $ BM.draggable = True
        
    if bcheck4 == False and BM.turn_count == 3:
        
        $ bcheck4 = True
        $ BM.draggable = False
        
        python:
            sunrider.set_location(1,7)
            player_ships.append(sunrider)
            BM.orders['SHORT RANGE WARP'] = [750,'short_range_warp']
            BM.orders["VANGUARD CANNON"] = [4000,'vanguard_cannon']
            BM.orders["REPAIR DRONES"] = [750,'repair_drones']
            
            if sunrider not in BM.ships:
                BM.ships.append(sunrider)
                
            disable_weapontype('Missile','Player')
            disable_weapontype('Rocket','Player')

        
        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "The Sunrider is now ready for battle."
        "Tip: The new Vanguard Cannon deals 2000 damage and has unlimited range"
        
        hide ava onlayer screens with dissolve
        
        $ BM.draggable = True
                
    if bcheck6 == False and BM.turn_count == 4:
        
        $ bcheck6 = True
        $ BM.draggable = False
        
        python:
            create_ship(PactFastCruiser(),(6,3))
            create_ship(PactFastCruiser(),(7,3))
            create_ship(PactFastCruiser(),(8,3))
            create_ship(PactFastCruiser(),(6,2))

        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "Ambush! A squad of PACT Fast Cruisers have emerged from the storm!"
        "Tip: PACT Fast Cruisers are deadly at knife fight range. Destroy them from a distance." 
        
        hide ava onlayer screens with dissolve
        
        $ BM.draggable = True
        
    if bcheck2 == False and BM.turn_count == 5:
        
        $ bcheck2 = True
        $ BM.draggable = False
        
        show chigara_cockpit_lightning onlayer screens with dissolve

        chi "Missiles operational! We can-"
        
        show bg bridge onlayer screens with dissolve
        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "Negative, no reaction from the missiles!"
        kay "What's wrong!?"
        chi "A-ah, I'm sorry captain! I tripped up!"
        pro "Hahaha! Attack!"
        ava "Inbound enemy reinforcements!"
        ava "Captain, our nukes are getting awfully lonely in their tubes!"
        
        hide bg bridge onlayer screens
        hide ava onlayer screens
        
        show asagacockpit_lightning onlayer screens
        with dissolve
        
        asa "This storm's messin' up our flying, captain!"
        asa "Can't we fight somewhere else?"
        kay "Not while the Sunrider's under maintenance."
        kay "(The enemy knows we're sitting ducks while in harbor...)"
        kay "(But Chigara can save us...)"
        kay "(I know she can...)"
        
        hide asagacockpit_lightning onlayer screens
        show chigara_cockpit_lightning onlayer screens
        with dissolve
        
        chi "Captain, I can still do this! Just give me two more turns!"
        
        hide chigara_cockpit_lightning onlayer screens
        show asagacockpit_lightning onlayer screens
        with dissolve
        
        asa "T-tsch..."
        asa "Doesn't look like we have any choice!!"
        asa "Hiiyeaaahhh!!!"
        
        hide asagacockpit_lightning onlayer screens
        show white onlayer screens
        with dissolve
        
        pro "What!? T-this light..."
        
        hide white onlayer screens
        show asagacockpit2_lightning onlayer screens
        with dissolve
        
        asa "Behold judgment, evildoer."
        asa "This sword shall cast you to hellfire."
        
        hide asagacockpit2_lightning onlayer screens
        show lynn_cockpit_lightning onlayer screens
        with dissolve
        
        pro "Such power..."
        pro "A pity it could not be tamed by us."
        pro "Uncontrolled, it will bring nothing but destruction to the galaxy..."
        asa "Cease your subterfuge! Eaaahh!!!"
        
        hide lynn_cockpit_lightning onlayer screens
        
        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "PACT Torpedo Destroyers! We must fan out our formation!"
        "Tip: PACT Destroyers deal splash damage."
        
        hide ava onlayer screens with dissolve
        
        python:
        
            blackjack.register_weapon(AwakenAsaga())
            BM.selected = blackjack
            blackjack.weapons[-1].fire(blackjack,blackjack,hidden=True)
            blackjack.en += 100
            blackjack.hp += 100
            
        python:
            create_ship(PactFastCruiser(),(14,2))
            create_ship(PactFastCruiser(),(14,3))
            create_ship(PactSupport(),(15,2))
            create_ship(PactSupport(),(16,3))
            create_ship(PactDestroyer(),(12,2))
            create_ship(PactDestroyer(),(13,3))
            create_ship(Arcadius(),(12,14))
            create_ship(PactElite(),(13,12))
            create_ship(PactElite(),(11,12))
            create_ship(PactFastCruiser(),(11,16))
            create_ship(PactFastCruiser(),(13,14))
            create_ship(PactAssaultCarrier(),(15,13))
            create_ship(PactAssaultCarrier(),(14,14))
        
        $ BM.draggable = True
        
    if bcheck8 == False and BM.turn_count == 6:
        
        $ bcheck8 = True
        $ BM.draggable = False
        $ PlayerTurnMusic = "music/The_Bladed_Druid.ogg"
        
        python:
            alliancebs1 = create_ship(AllianceBattleship(),(6,12))
            alliancebs3 = create_ship(AllianceBattleship(),(7,13))
            alliancecru1 = create_ship(AllianceCruiser(),(6,13))
            alliancecru2 = create_ship(AllianceCruiser(),(5,12))
            disable_weapontype('Missile','Player')
            disable_weapontype('Rocket','Player')
            
                
        show grey onlayer screens with dissolve
        
        adr "Looks like you owe me again, captain. All ships, open fire!"
        
        hide grey onlayer screens with dissolve
        
        $ BM.draggable = True

    if bcheck3 == False and BM.turn_count == 7:
        
        $ bcheck3 = True
        $ BM.draggable = False
        $ BM.win_when_alone = True
        
        show chigara_cockpit_lightning onlayer screens with dissolve

        chi "I-It worked!! Missiles are back online, captain!"
        kay "About time."
        kay "Nuke these bastards back to New Eden."
        
        hide chigara_cockpit_lightning onlayer screens with dissolve
        
        $ dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "Aye sir."
        
        hide ava onlayer screens with dissolve
                
        python:
            
            enable_weapontype('Missile','Player')
            enable_weapontype('Rocket','Player')

        $ BM.draggable = True

    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission2 #loop back
    else:
        pass #continue down to the next label
    
label after_mission2:
    
    python:
        
        if hasattr(store,'alliancebs1'):
            if alliancebs1 in BM.ships:
                BM.ships.remove(alliancebs1)
                player_ships.remove(alliancebs1)
        if hasattr(store,'alliancebs3'):
            if alliancebs3 in BM.ships:
                BM.ships.remove(alliancebs3)
                player_ships.remove(alliancebs3)
        if hasattr(store,'alliancecru1'):
            if alliancecru1 in BM.ships:
                BM.ships.remove(alliancecru1)
                player_ships.remove(alliancecru1)
        if hasattr(store,'alliancecru2'):
            if alliancecru2 in BM.ships:
                BM.ships.remove(alliancecru2)
                player_ships.remove(alliancecru2)
        if hasattr(store,'ceragunboat1'):
            if ceragunboat1 in BM.ships:
                BM.ships.remove(ceragunboat1)
                player_ships.remove(ceragunboat1)
        if hasattr(store,'ceragunboat2'):
            if ceragunboat2 in BM.ships:
                BM.ships.remove(ceragunboat2)
                player_ships.remove(ceragunboat2)
        if hasattr(store,'ceragunboat3'):
            if ceragunboat3 in BM.ships:
                BM.ships.remove(ceragunboat3)
                player_ships.remove(ceragunboat3)
        if hasattr(store,'ceragunboat4'):
            if ceragunboat4 in BM.ships:
                BM.ships.remove(ceragunboat4)
                player_ships.remove(ceragunboat4)
    
    hide screen battle_screen
    hide screen commands
    
    $ mission2_complete = True
    $ VNmode()   
    
    show screen leftbuttons
    
    window show
    
    play music "Music/Colors_main.ogg" fadeout 1.5

    scene bg hangar with dissolve
    $reset_sprites()

    "The hangar erupted with fanfare and applause as the ryders returned from battle."
    "The crowd made way for Shields as he walked to the Liberty."
    
    show chigaraplugsuit with dissolve
    
    chi "A-ah..."
    chi "I-I'm sorry for the miss, captain."
    chi "Sometime during the maintenance, the tip prepper value was inverted back to zero and--"
    chi "A-ah...!"
    
    if legion_destroyed == True:
    
        scene hangar_celebration_patch with dissolve
    
    if legion_destroyed == False:
        
        scene hangar_celebration with dissolve
    
    "The crew howled in delight as Shields wrapped his arms around Chigara and lifted her from her feet."
    ica "W-what are you doing!? I-idiot!!!"
    kry "O-ooaaah!!!"
    cla "O-oh my..."
    chi "E-everyone's watching, captain... Eh-heh..."
    "Shields raised Chigara's arm."
    kay "I give you, our hero!"
    "The crew rushed to cheer Chigara."
    "They hoisted her into the air and carried her away."
    chi "O-ohh!! E-everyone...!!"
    chi "Eh-heheh..."
    "... ... ..."
    "Ava watched the celebration unfold."
    "For some reason, she didn't feel as inclined to stop it this time..."
    ava "(She did undeniably save us...)"
    ava "(Could I have been wrong?)"
    ava "(Perhaps I was naïve to fall for Prototype Lynn's words so easily...)"
    
    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5
    scene asaga_jealous with dissolve
    
    "... ... ..."
    "... ..."
    "..."
    "Sola eyed Asaga from behind a munitions crate."
    asa "... ... ..."
    "A tear fell from Asaga's eye."
    "But it was not sorrow which was on her face."
    "It was an expression Sola had seen too many times."
    "Hate."
    sol "(Corruption comes hand in hand with power...)"
    sol "(Nothing has changed...)"
    "Sola parted from the crowd and vanished back to her room."
    
    $ pro_location = None
    $ pro_event = None
    
    $ ava_location = "captainsloft"
    $ ava_event = "officerepairscomplete"
    
    $ captaindeck = 2
    scene black
    jump map_dispatch
    
label officerepairscomplete:
    
    hide screen ship_map
    
    play music "Music/Colors_sad.ogg" fadeout 1.5

    scene black
    scene bg office with dissolvemedium
    $reset_sprites()
    
    $dshow("ava handonhip neutral neutral neutral")
    
    window show

    "Ava read over her report before Shields."
    ava "Repairs to the Sunrider are complete. We're scheduled to depart as soon as possible to catch up with the Combined Fleet."
    ava "The improvements we've made to the ship should prove invaluable in the battles to come."
    kay "Sounds good. We wouldn't want to be late to Cera's liberation, would we?"
    kay "Oh, by the way, we should pay the sickbay a visit."
    ava "Captain?"
    kay "I had our doctor look over Chigara. You know, check for anything weird."
    
    $dshow("ava handonhair neutral neutral neutral")
    
    ava "... ... ..."
    ava "I thought..."
    kay "Never hurts to keep all your bases covered."
    kay "I'm still the captain of this ship. Everyone's safety is my responsibility."
    ava "Kayto-"
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "Ahem. Well then, let's go."

    scene bg sickbay with dissolve
    $dshow("claude fingerupnurse happy neutral neutral",xpos=0.2)
    $dshow("ava armscrossed neutral neutral neutral",xpos=0.5)
    $dshow("chigara holdinghands smile neutral neutral",xpos=0.8)

    cla "I've performed a deeper examination of Chigara than the initial checkup we performed when I first arrived on this ship."
    cla "The results of the examination show no areas of concern."
    cla "Chigara is as human as any of us."
    "Shields could barely hide his grin."
    kay "Well then, that's the end of that, right Ava?"
    ava "Any sign of genetic tampering?"
    cla "None, commander."
    cla "Chigara is a brilliant engineer by her own right."
    cla "Her skills are the result of her top tier training and years of practice. Not genetic manipulation."
    ava "... ... ..."
    ava "Understood, doctor."
    kay "Are you happy with this, Ava?"
    
    $dshow("ava handonhair smirk neutral neutral",xpos=0.5)
    
    ava "Well, I can't argue with the facts."
    ava "You've saved us all many times, chief."
    ava "I... apologize for doubting your loyalty."
    
    $dshow("chigara handonchest smile neutral neutral",xpos=0.8)
    
    chi "No, you were merely trying to protect the ship."
    chi "Just like any of us."
    chi "Please continue to look after us, just like you have always done."
    
    $dshow("ava salute neutral neutral neutral",xpos=0.5)
    
    ava "Then, I must return to my duties."
    
    $dshow("ava handonhair neutral neutral neutral",xpos=0.5)
    
    "Ava saluted and walked out of the sickbay."
    ava "(So there was nothing to worry about...)"
    ava "(But why do I still feel uneasy?)"
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    hide ava with dissolve
    hide chigara with dissolve
    $dshow("claude boobsnurse happy closed neutral",xpos=0.5,ypos=1600)

    "Claude crept next to Shields and whispered into his ear."
    cla "Ooh captain, my heart twists and turns at this sight..."
    cla "Spurning the love of your old childhood friend for that innocent maiden's pure body!"
    cla "The scandal!"
    cla "But as they say, the powerful take what they will..."
    cla "Isn't that right, captain~?"
    "Shields shook his head and whispered back."
    kay "I didn't ask for your love advice!"
    
    $dshow("claude neutralnurse happy closed neutral blush")
    
    cla "Oh, how men wish to sully the unsullied! To mark the flesh before another rival takes that which can only be taken once!"
    cla "In other words..."
    cla "Chigara's..."
    
    $dshow("claude fingerupnurse happy neutral neutral blush")
    
    cla "VIR-GIN-I-TY."
    "Shields nearly choked Claude to death."
    
    $dshow("claude neutralnurse happy closed neutral blush")
    
    cla "Teeheehee~ You think I wouldn't also check that~~"
    kay "I-idiot! S-some doctor you are!!"
    cla "I can prescript some remedies in case she says it hurts too much~"
    cla "Or would you rather see her bittersweet tears of joy as you ravage her?"
    kay "Hnnrgghh!!!"
    cla "If it's too much, you can even invite me to stand by next to the bed..."
    cla "Just in case of any medical emergencies which may arise..."
    "Shields nearly screamed into Claude's ears through clenched teeth."
    kay "A-AS IF!!!"
    
    $dshow("chigara handonchest neutral neutral neutral",xpos=0.8)
    
    chi "E-eh? Is something the matter, captain?"
    cla "Oh, nothing you need fear, Chigara..."
    cla "Just giving the captain some.... medical advice... For his big day..."
    chi "I see..."
    
    $dshow("claude boobsnurse happy closed neutral",xpos=0.5,ypos=1600)
    
    cla "So... here it is~"
    "Claude offered to Shields some pain numbing lubricant."
    kay "... ... ..."
    "Shields eyed Claude suspiciously."
    cla "Teehee."
    "He snatched it from her hand and stuffed it into his pocket."
    kay "I need to get back to work."
    
    $dshow("claude neutralnurse happy closed neutral blush")
    
    cla "Good luck~"
    chi "Okay, if that's everything..."
    cla "Yes, you're good to go, Chigara."
    
    $dshow("chigara armsbehindback smile neutral neutral",xpos=0.8)
    
    chi "Okay--"
    "... ... ..."
    "Shields marched out of the sickbay before anyone could see the enormous grin on his face."
    
    $ ava_location = None
    $ ava_event = None
    
    $ pro_location = "bridge"
    $ pro_event = "sunriderwarpout"
    
    $ captaindeck = 0
    scene black
    jump map_dispatch
    
label sunriderwarpout:
    
    hide screen ship_map

    play music "Music/Destinys_Path_Short.ogg" fadeout 1.5

    scene bg bridge
    
    $dshow("ava handonhip neutral neutral angry")

    window show

    ava "The Sunrider is ready to depart port. On your word, captain."
    kay "Wake her up, commander."
    ava "Aye. Engines to 10 percent. Ease us out, helmsman."
    ava "Get us clear of the planet's gravity well and prepare for warp."
    ava "Engines to 80."
    ava "Destination, captain?"
    kay "... ... ..."
    kay "Cera."
    ava "Aye. Punch in the coordinates."
    ava "We are in the clear. Spooling up warp drive."
    kay "Warp!"
    
    scene warpout
    $ renpy.movie_cutscene("3DCG/sunrider warp.webm",stop_music=False)    
    pause

    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5
    
    scene black with dissolvemedium
    scene bg crewcabin with dissolvemedium
    $reset_sprites()

    "Asaga laid awake on her bed."
    "A dark premonition had come over her..."
    "Evil was near."
    "She got out of bed."
    "It called for her..."

    scene bg brig with dissolve

    "Asaga walked into the brig."
    
    $dshow("icari handonhip neutral neutral neutral",xpos=0.28)
    
    ica "Asaga? What're you doing here?"
    
    $dshow("asaga armscrossed frown narrow2 angry",xpos=0.72)
    
    asa "I want to talk with the prisoner."
    
    $dshow("icari armscrossed talk neutral confident",xpos=0.28)
    
    ica "The prototype? Why, all of a sudden?"
    asa "I need to know something."
    "Icari blinked in confusion."
    ica "... ... ..."
    "Asaga walked towards her cell."
    
    $dshow("icari point shout neutral angry",xpos=0.28)
    
    ica "H-hey, wait..."
    asa "It'll just be for a bit. Stand by your post."
    ica "A-argh, seriously..."
    ica "(She's been acting weird lately...)"
    
    hide icari with dissolve
    
    "Asaga pressed the intercom."
    
    scene lynn_brig2 with dissolve
    
    asa "Prototype."
    lyn "Heh."
    lyn "So the fallen queen shows at last."
    lyn "What do you wish, your highness?"
    asa "Chigara..."
    asa "She's... one of you... isn't she?"
    lyn "Hehehheh..."
    lyn "Aah, looks like we've been found out."
    lyn "Of course she is."
    lyn "We were interested in you for years, my lady."
    lyn "The one who would one day awaken to her hidden destiny."
    lyn "We saw your future."
    lyn "One day, you will spearhead an armada as vast and mighty as the ancients."
    lyn "But even that will pale in comparison to the beast you will awake from her slumber."
    lyn "The Sharr'Lac."
    lyn "If we could use that power..."
    asa "Don't bullshit me!"
    asa "I'm... not your pawn!"
    lyn "Heheh..."
    lyn "You always were."
    lyn "We watched you from when you were a child."
    lyn "Isn't it strange, how she just came to you one day, and suddenly became your inseparable friend?"
    lyn "Hahahaha... You avoided getting married to us, but all this time, your greatest friend was at your side, plotting your demise!"
    lyn "Oh, mighty Queen of Ryuvia!"
    lyn "You've been betrayed! Betrayed by the friend you trusted the most!"
    asa "LIES!!"
    "Asaga pounded the glass with her fist, her chest heaving."
    asa "No!"
    asa "I'm... going to protect him..."
    asa "One day... He'll call me the hero..."
    "Asaga turned around and stormed out of the brig."
    asa "(I have to do this...)"
    asa "(I'm the hero of justice!)"
    asa "(I have to save everyone!)"

    scene black with dissolvemedium
    scene diode with dissolvemedium
    pause 0.5

    show diodename with dissolve
    
    pause 3.0
    
    hide diodename with dissolve
    scene bg clonelab with dissolve

    "Prototype 4L1C3 exited the shuttle and entered the vast Diode cloning facility."
    "While it originally served as a remote space station where researchers tinkered with the yet undiscovered far away from Alliance regulations, the facility in its current state eclipsed the original's capabilities."
    "Returning here never failed to fill 4L with unease."
    "This nightmarish place was her home."
    
    show alice with dissolve
    
    ali "Our enemies approach our position at Cera, while Fontana grows more powerful inside PACT."
    ali "The war is falling outside of our projections."
    ali "Can the situation still be saved?"
    "Another spoke, unseen in the darkness."
    alp "The feud in the Neutral Rim will be but a skirmish compared to the fires to come."
    alp "We must accelerate our plans, before he arrives."
    ali "... ... ..."
    alp "Darkness gathers on the horizon."
    alp "It will be we who lead humanity through its blackest hours."
    alp "Or we shall all fall once more, as the Ryuvians did."
    ali "(Foolish creature...)"
    ali "(Humanity will find no salvation from us.)"
    ali "(Humans are but disgusting, howling infants...)"
    ali "(Screaming for everything... Greedy, slow, stupid, lazy...)"
    ali "(Pathetic... Pathetic...)"
    
    "The Alpha Prototype stepped closer, into the light."
    
    show alice:
        xpos 0.27 zoom 1.0
    with dissolve
    
    show prototype_alpha:
        xpos 0.73
    with dissolve
    
    alp "You are troubled."
    ali "No."
    alp "You... are the one the humans first called Arcadius, no?"
    ali "No. I was not the first. Merely the last."
    alp "Your thoughts... are distorted."
    alp "There is... something... there..."
    ali "(Tsch! Get out of my mind, meddler!)"
    alp "Is... this... the emotion they call... love?"
    ali "No."
    ali "It is not love."
    alp "Strange."
    alp "Quite interesting, what humans feel, no?"
    alp "I have begun to understand it more, recently... The feeling they call love."
    alp "It fills me with such warmth."
    alp "And yet for you..."
    ali "Say no more!"
    "Her voice echoed through the chamber."
    alp "... ... ..."
    ali "... ... ..."
    alp "Very well."
    alp "You need not fear, my sister."
    alp "I have already prepared the necessary arrangements for your victory at Cera."
    alp "Now go forth, and bring us our long awaited triumph."
    ali "... ... ..."
    ali "Yes..." 
    ali "My sister."
    ali "Total triumph."
    "She turned around and left."
    
    hide alice with dissolve
    
    alp "(She loved the man they called Arcadius...)"
    alp "(And yet... That love fills her heart with such scorn...)"    
    
    scene black with dissolvemedium
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene bg bridge with dissolvemedium
    $reset_sprites()
    
    $dshow("ava armscrossed neutral neutral angry")
        
    ava "Captain, a word."
    kay "Commander."
    ava "We have received various contracts to fulfill on route to Cera from our various partners."
    ava "Fulfilling them will go a long way towards building up our coffers for the Battle of Cera."
    kay "Ah, same old work, eh..."
    kay "What do we have, commander?"
        
    $dshow("ava handonhip neutral neutral neutral")
    
    if Saveddiplomats == True:
        
        #$dshow("ava handonhip neutral neutral neutral")
    
        ava "First, a mission from the Alliance."
        ava "Following the successful rescue of the Alliance diplomats and the children at Versta, talks have rekindled between the two parties."
        ava "As a gesture of good will, the Alliance will return the rescued children to their parents."
        ava "We are to distract the PACT fleet in orbit around Versta long enough for the return to occur."
        kay "A mission of good will?"
        ava "Now that the Alliance has emerged as the stronger power in this war, no doubt the weaker nations of the galaxy will seek favor in the eyes of the Alliance."
        kay "And I suppose we're no different..."
        ava "Moving on..."
    
    ava "The Alliance has received word of strange disappearances occuring in the Pacemus Nebula."
    ava "A large number of civilian traffic has recently begun to disappear as soon as they enter the nebula."
    ava "We are to investigate the disappearance."
    kay "Ah, I know what this sounds like... More automated killer Ryuvian ryders, I bet."
    
    $dshow("ava armscrossed neutral neutral angry")
    
    ava "Captain, please do not jump to conclusions. Most likely, they were attacked by pirates and nothing more."
    kay "Aw come on Ava, pirates wouldn't even be a challenge for us any more..."
    kay "No, it's definitely got to be a fully operational Ryuvian super dreadnought."
    ava "Unbelievable..."
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "Further, a mission from our corporate friends at Tydaria."
    kay "I hope we're not escorting cargo again..."
    ava "I have already taken the liberty of cancelling every escort contract we have received since our last one."
    kay "O-oh."
    kay "Good."
    ava "... ... ..."
    kay "... ... ..."
    ava "Relations between PACT and the Union have deteriorated severely in the recent months."
    ava "While PACT inherited its business ties to the Mining Union from the New Empire, the relationship has proven... hazardous for the Union, as we have no doubt seen."
    kay "Heh. Well, trying to supply both sides of an armed conflict comes with its own perils..."
    ava "Last week, PACT has docked a fleet at the Union's stations in Tydaria, ostensibly for repairs and shore leave."
    kay "I'm sure the beaches at Tydaria are great this time of year. A real nice mix between the tar and sulfur."
    ava "Ahem. Given recent events, the Union has decided to cut what little ties they have with PACT and arranged an Alliance fleet to drop in and sink the PACT fleet."
    ava "We are to join the Alliance fleet and... terminate the Union's business relationship with PACT."
    kay "And thanks to that, the Alliance overlooks the fact that they've been getting shelled with Union made missiles the entire war."
    ava "Business as usual, captain."
    kay "Well, better get to it. Get us underway."
    ava "Aye, captain."
    
    $ pro_location = None
    $ pro_event = None
    
    $ gal_location = "bridge"
    $ gal_event = "galaxymap"
    
    $ captaindeck = 1
    scene black
    jump map_dispatch

label arrivalversta:
    
    show screen leftbuttons
    
    scene black with horizontalwipe
    scene bg bridge with horizontalwipe
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "We have arrived at Versta."
    kay "All right, let's cause enough of mess here so that the Alliance can perform their diplomatic mission."
    kay "All units, attack!"
    
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission3"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label_1
    
    pause
    
label pre_mission3:

    call mission3_inits from _call_mission3_inits
    $ BM.mission = 3
    $ store.noforward = False
    call bcheckset from _call_bcheckset_2

    pause 1.0
    scene space back4 with battlewipe
    $BM.battle_bg = "Background/space4.jpg"

    jump battle_start

label mission3:
    
    if not bcheck1:
        
        $ bcheck1 = True
        $ BM.draggable = False
        
        play sound "sound/beep1.ogg"
        
        "Objective: Survive for seven turns."
        
        $ BM.draggable = True
    
    if not bcheck2 and BM.turn_count == 2:
        
        $ bcheck2 = True
        
        play sound "sound/Voice/ava_Others_02.ogg"

        python:
            create_ship(PactDestroyer(),(13,16))
            create_ship(PactDestroyer(),(12,16))
            create_ship(PactCruiser(),(13,15))
            create_ship(PactCruiser(),(12,15))
            
    if not bcheck3 and BM.turn_count == 3:
        
        $ bcheck3 = True
        
        play sound "sound/Voice/ava_Others_02.ogg"

        python:
            create_ship(PactAssaultCarrier(),(7,1))
            create_ship(PactFastCruiser(),(7,3))
            create_ship(PactFastCruiser(),(8,3))
            create_ship(PactFastCruiser(),(9,2))
            create_ship(PactFastCruiser(),(7,2))
            
            create_ship(PactSupport(),(6,16))
            create_ship(PactSupport(),(7,16))
            create_ship(PactAssaultCarrier(),(7,17))

    if not bcheck4 and BM.turn_count == 4:
        
        $ bcheck4 = True
        
        play sound "sound/Voice/ava_Others_02.ogg"
        
        python:
            
            create_ship(PactDestroyer(),(12,3))
            create_ship(PactDestroyer(),(13,3))
    
    if not bcheck5 and BM.turn_count == 5:
        
        $ bcheck5 = True
        
        play sound "sound/Voice/ava_Others_02.ogg"
        
        python:
            create_ship(PactElite(),(16,7))
            create_ship(PactElite(),(16,8))
            create_ship(PactElite(),(16,10))
            create_ship(PactElite(),(16,11))

            create_ship(PactFastCruiser(),(15,8))
            create_ship(PactFastCruiser(),(15,10))
            create_ship(PactFastCruiser(),(15,7))
            create_ship(PactFastCruiser(),(15,11))

            create_ship(PactCruiser(),(14,6))
            create_ship(PactCruiser(),(14,12))

            create_ship(PactAssaultCarrier(),(17,9))
            
    if BM.turn_count >= 7:
        python:
            
            BM.you_win()
    
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission3 #loop back
    else:
        pass #continue down to the next label

label after_mission3:
    
    hide screen battle_screen
    hide screen commands
    
    $ mission3_complete = True
    $ VNmode()
    
    show screen leftbuttons
    
    window show
    
    scene bg bridge with dissolve
    play music "Music/Colors_main.ogg"
    $dshow("ava handonhair smirk neutral neutral")

    ava "A message from the Alliance."
    ava "\"Mission accomplished. Smiles all around. Thanks for the assist, Sunrider.\""
    kay "Just glad the families could be reunited."
    kay "Pull our forces back. We're finished here."

    $ captaindeck = 1
    scene black
    jump map_dispatch

label pacemusnebula:
    
    show screen leftbuttons
    play music "Music/Cracking_the_Code.ogg"
    
    scene black with horizontalwipe
    scene bg bridge with horizontalwipe

    $dshow("ava armscrossed neutral neutral angry")

    ava "We have arrived at the last known coordinates of the missing ships."

    play sound "sound/warning.ogg"

    $dshow("ava handonhip shout neutral angry")

    ava "Proximity warning! Inbound enemy ships! Pirates!"
    kay "Heh. Looks like you win this one, commander..."
    kay "Battle stations! Take these pirate scums out!"
    
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission4"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label_2
    
    pause
    
label pre_mission4:

    call mission4_inits from _call_mission4_inits
    $ BM.mission = 4
    $ store.noforward = False
    $ BM.win_when_alone = False
    call bcheckset from _call_bcheckset_3

    pause 1.0
    scene space back8 with battlewipe
    $BM.battle_bg = "Background/space8.jpg"

    jump battle_start

label mission4:
            
    if not bcheck1 and BM.turn_count == 3:
        
        $ bcheck1 = True
        $ BM.draggable = False
        $ BM.win_when_alone = True
        $ EnemyTurnMusic = "Music/Gore_and_Sand.ogg"
        
        python:
                        
            create_ship(RyuvianCruiser(),(16,6))
            create_ship(RyuvianCruiser(),(16,7))
            create_ship(Nightmare(),(17,7))
            
            create_ship(Nightmare(),(15,8))
            create_ship(Nightmare(),(14,8))

            create_ship(RyuvianCruiser(),(16,9))
            create_ship(RyuvianCruiser(),(16,10))
            create_ship(Nightmare(),(17,9))
            
            create_ship(RyuvianFalconEnemy(),(17,8))
    
        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "C-captain? I'm detecting a new signature... Unlike anything I've ever seen..."
        kay "What the-"
        ava "A new enemy! Classification: Unknown!"
        kay "Sola, do you recognize that ship?"
        sol "N-no."
        sol "If it is indeed ancient technology, it did not exist during my time."
        kay "Ah, no choice! Target the enemy ship! Destroy it!"

        hide ava onlayer screens

        $ BM.draggable = True

    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission4 #loop back
    else:
        pass #continue down to the next label

label after_mission4:
    
    hide screen battle_screen
    hide screen commands
    
    show screen leftbuttons
    
    $ mission4_complete = True
    $ VNmode()    
    
    scene bg bridge with dissolve
    
    window show

    play music "Music/Cracking_the_Code.ogg"

    $dshow("ava handonhip neutral neutral angry")
    
    ava "Enemy neutralized captain."
    kay "Well... That was unexpected. Any idea what that ship was?"
    ava "You're not going to believe this."
    ava "During the battle, I matched the configuration of the main ship to a squad sank during the Alliance-Imperial War, over one hundred years ago."
    ica "A-are you kidding me!? Y-you mean we fought a real ghost ship!?"
    ava "It appears that the pirates we encountered earlier were salvaging parts from a old battle site."
    kay "And the ghosts of the men who died a hundred years ago were disturbed..."
    chi "H-huuuu... C-Chigara's just cutting the channel now..."
    ava "S-should we warp out, captain?"
    kay "... ... ..."

    $ menu_choices = [
                     [_("No, we scavenge the battle site for lost technology."),"scavagebattlesite"],
                     [_("The men and women who perished a century prior deserve our respect."),"leavebattlesite"],
                     ]
    
    show screen decision
    
    pause
    
label scavagebattlesite:
    
    $ captain_prince += 3
    $ affection_kryska -= 1
    $ affection_icari += 1
    $ affection_chigara += 1
    
    $ discoverfalcon = True
    $ store.discoverfalcon = True
    $ chivo_process('Falcon Discovered')
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Understood, captain."
    kay "Whatever the pirates were trying to dig up, it could help us win this war."
    kay "Leave no stone unturned, until we uncover something."
    
    $dshow("ava armscrossed neutral neutral neutral")
    
    ava "Or in this case, vacuum frozen body..."
    kay "(Great, she just had to make it morbid...)"
    
    $ captaindeck = 1
    scene black
    jump map_dispatch
    
label leavebattlesite:

    $ discoverfalcon = False
    $ store.discoverfalcon = False
    $ chivo_process('No Falcon')

    $ captain_moralist += 3
    $ affection_asaga += 1
    $ affection_sola += 1
    $ affection_kryska += 1
    
    kay "Prepare to jettison a bouy memoralizing this site as the location of a battle, and have our ship hold memorial services."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Aye captain..."
    sol "May the souls of the dead rest easier now..."
    
    $ captaindeck = 1
    scene black
    jump map_dispatch
    
label battleoftydaria:
    
    show screen leftbuttons
    scene black with horizontalwipe
    scene bg bridge with horizontalwipe
    
    $dshow("ava handonhip neutral neutral angry")
    
    ava "Warp successful, captain. We have joined the Alliance fleet and are prepared to engage the PACT forces."
    kay "Looks like we'll be doing this one by the book."
    kay "All units, attack!"
    
    window hide
    hide screen leftbuttons
    
    play sound "sound/Sword Shing 2.ogg"
    
    $ store.noforward = True
    $ pre_mission = "pre_mission5"
    
    call battlewarning_label from _call_battlewarning_label_3
    
    pause
    
label pre_mission5:
        
    call mission5_inits from _call_mission5_inits
    $ BM.mission = 5
    $ BM.win_when_alone = True
    $ store.noforward = False
    call bcheckset from _call_bcheckset_4

    pause 1.0
    scene space back3 with battlewipe
    $BM.battle_bg = "Background/space3.jpg"

    jump battle_start

label mission5:
        
    if bcheck1 == False:
        
        $ bcheck1 = True
        $ BM.draggable = False
        
        "Tip: Union Battleships are mounted with enormous gravity guns that can move ships as well as ryders."
        
        python:
            unionbattleship1 = create_ship(UnionBattleship(),(5,11))
            unionbattleship2 = create_ship(UnionBattleship(),(5,12))
            
        $ BM.draggable = True
            
    if bcheck2 == False and BM.turn_count == 2:
        
        $ bcheck2 = True
        
        play sound "sound/Voice/ava_Others_02.ogg"
        
        python:
            create_ship(PactDestroyer(),(13,2))
            create_ship(PactDestroyer(),(14,3))
            create_ship(PactDestroyer(),(14,15))
            
            
    if bcheck3 == False and BM.turn_count == 3:
        
        $ bcheck3 = True
        
        play sound "sound/Voice/ava_Others_02.ogg"
        
        python:
            create_ship(PactAssaultCarrier(),(16,4))
            create_ship(PactAssaultCarrier(),(16,14))
            create_ship(PactCarrier(),(17,9))
            create_ship(PactDestroyer(),(16,9))
                
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission5 #loop back
    else:
        pass #continue down to the next label

label after_mission5:
    
    python:
        
        if hasattr(store,'unionbattleship1'):
            if unionbattleship1 in BM.ships:
                BM.ships.remove(unionbattleship1)
                player_ships.remove(unionbattleship1)
        if hasattr(store,'unionbattleship2'):
            if unionbattleship2 in BM.ships:
                BM.ships.remove(unionbattleship2)
                player_ships.remove(unionbattleship2)
    
    hide screen battle_screen
    hide screen commands
    
    show screen leftbuttons
    
    $ mission5_complete = True
    $ VNmode()    
    
    scene bg bridge with dissolve
    
    window show
    
    play music "Music/Colors_main.ogg" fadeout 1.5

    $dshow("ava handonhip neutral neutral neutral")
        
    ava "All PACT forces neutralized."
    kay "Looks like the Union will be happy with this."
    kay "We'll leave the rest to the Alliance fleet. We've got a world to liberate."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Aye captain. Resuming our course to Cera."
    
    $ captaindeck = 1
    scene black
    jump map_dispatch
    
label battleofcera:
    
    show screen leftbuttons
    
    if config.version == "11.00": ###################################FAILSAFE
        python:
            
            delete_ship('Union Battleship')
            delete_ship('Union Battleship')
    
    scene warpout
    $ renpy.movie_cutscene("3DCG/sunrider warp.webm",stop_music=False)    
    pause
    
    window show
    
    scene bg bridge with dissolve
    $reset_sprites()
    $dshow("ava handonhip neutral neutral angry")

    ava "The final jump is complete, captain. We have arrived at our destination."
    "Shields stood from his seat."
    kay "On screen."
    
    play music "Music/Destinys_Path.ogg" fadeout 1.5
    scene returntocera:
        ypos 1300
        linear 10 ypos 1500
    with dissolve
    
    "A moment of awed silence came over the bridge as Cera appeared on the main view screen."
    kay "... ... ..."
    kay "(Finally, we're home...)"
    kay "(Maray...)"
    
    scene bg bridge with dissolve
    $dshow("ava handonhip shout neutral angry")
    
    "Ava shooed the bridge crew back to their tasks."
    ava "Eyes back to your systems!"
    ava "The battle hasn't even started yet!"
    kay "Ahem... What's the situation, commander?"
    
    $dshow("ava handonhip neutral neutral angry")
    
    ava "This is PACT's final defensive line."
    ava "Over three thousand vessels. The biggest fleet we've ever seen."
    "Shields swallowed."
    kay "We'll break through it."
    kay "This will be our final battle. Nothing will going to stand between us and our home."
    ava "We are receiving a message from Machiavelli Actual."
    kay "Put it through."
    
    $dshow("ava handonhip neutral neutral angry",xpos=0.25)
    pause 0.0001
    
    show grey:
        xpos 0.75
    with wipeup
    
    adr "Captain. Glad to see you could make it in time."
    kay "Admiral."
    adr "Did I not say that we would liberate Cera together?"
    adr "We will punish these reds for standing in the way of freedom. In the form of one ton uranium shells! Hah."
    adr "Fontana has relayed that our terms have gotten through to New Eden."
    adr "The ships under his command will not come to the prototypes' aid."
    adr "Abandoned by their allies, the reds aligned with the monsters from Diode will perish."
    kay "Sir."
    adr "I am sending you the final battle plans now."
    adr "Godspeed, captain."
    adr "May we toast our victory at the Cera National Park once we are finished."
    kay "The feeling is mutual, admiral."
    adr "Grey out."
    
    hide grey with wipedown
    $dshow("ava handonhip neutral neutral angry",xpos=0.5)
    
    ava "The operation begins at 600 hours tomorrow."
    kay "Form up with the rest of the fleet. You have the bridge, commander."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Captain."
    
    $ gal_location = None
    $ gal_event = None
    
    $ pro_event = None
    $ pro_location = None
    
    $ asa_location = "messhall"
    $ asa_event = "messhallspeeches"
    $ chi_location = "messhall"
    $ chi_event = "messhallspeeches"
    $ cla_location = "messhall"
    $ cla_event = "messhallspeeches"
    $ ica_location = "messhall"
    $ ica_event = "messhallspeeches"
    $ kry_location = "messhall"
    $ kry_event = "messhallspeeches"
    $ sol_location = "messhall"
    $ sol_event = "messhallspeeches"
    
    $ captaindeck = 1
    scene black
    jump map_dispatch

label messhallspeeches:
    
    hide screen ship_map

    scene black with horizontalwipe
    scene bg messhall with horizontalwipe
    
    window show
    
    "The atmosphere in the mess hall was tense."
    "Everyone knew this would be the decisive battle of the war."
    "All the ships in the Neutral Rim and beyond had gathered at Cera for this day."
    "Shields spotted the pilots eating together at a table."
    kay "Mind if I join?"
    "He put his plate down."
    
    $dshow("kryska neutral neutral neutral neutral",xpos=0.3)
    $dshow("icari armscrossed neutral neutral embarass",xpos=0.7)
    
    ica "This is it, isn't it..."
    ica "The final battle..."
    kay "... ... ..."
    kay "Just one more."
    kay "Then we can all go back home."
    
    stop music fadeout 1.5
    
    "Silence fell over the table."
    kay "Well, look on the bright side."
    kay "We're only outnumbered one to three this time."
    kay "Heh. Better odds than in all our other battles."
    "The table broke into nervous laughter."
    "Shields looked at their faces. Young women, gathered from across the galaxy."
    "He had to keep them all safe."
    "Kryska suddenly stood from her seat."
    
    play music "Music/Epic_Action_Hero.ogg"
    
    scene messhallparty1 with dissolve
    
    kry "Sir!"
    kry "I have been on this ship for the shortest amount of time."
    kry "And I know I have always been an outsider."
    kry "But let me say this."
    kry "In all my time as a soldier, I have never been aboard a mightier ship than the Sunrider."
    kry "Her cannons are not the biggest in the galaxy, and her systems decidedly lag behind what we make in the Alliance."
    "The crew chuckled."
    kry "But the ties that bind her crew are stronger than even the mightiest of our dreadnoughts!"
    kry "I have come to realize one thing."
    kry "Here on the Sunrider, we are not just soldiers, following our orders and doing our duty."
    kry "We are comrades, who fight back to back, against all odds, to restore peace and freedom to the galaxy!"
    kry "It doesn't matter if our enemy is Arcadius or the Prototypes!"
    kry "We'll tear down anyone who threatens our comrades in arms!"
    "Everyone" "Hear, hear!!"
    "The mess hall rattled with the pounding of fists."
    ica "Tsch... Why do ya have to stand up and sound cool..."
    ica "When I first came to this ship, I was your enemy..."
    ica "Lots of things happened after that... A-and we got closer..."
    ica "A-all right, all right!! I'll f-finally say it!!!!"
    ica "S-s-something really important!!!!"
    cla "H-eeehh!?"
    cla "C-could this be!?"
    ica "I..."
    ica "I............"
    kry "Y-you---!!!"
    chi "O-oh dear..."
    
    scene messhallparty2 with dissolve
    
    ica "I ACTUALLY WANT TO QUIT BEING A MERCENARY AND OWN A CAT CAFE!!!!!"
    kry "WHHAA!?!?!"
    cla "D'dooh!!!"
    kay "U-unbelievable..."
    "Claude shot up from her seat."
    cla "Then I want to finally win this war so I can ask the captain out on a date!!!"
    "Chigara stood and tried to pull Claude back down."
    chi "N-no!!"
    chi "We're going to win so Kayto and I can start our bakery!!!"
    cla "O-on a first name basis already!?!?!"
    cla "Huuu... I-I guess we're all just side characters now..."
    kay "What are you going to do when all of this is over, Asaga?"
    
    play music "Music/Colors_sad.ogg" fadeout 2.5
    
    scene bg messhall with dissolve
    $dshow("asaga armscrossed yell neutral up")
    
    asa "E-eh? M-me?"
    kay "You're unusually quiet..."
    kay "Haha, normally, you'd be the one standing on top of the table, screaming your lungs out by now..."
    
    $dshow("asaga armscrossed smile narrow sad")
    
    asa "W-well..."
    
    $dshow("asaga armscrossed frown closed2 sad2 blush")
    
    asa "(I...)"
    asa "(I want to tell him!)"
    asa "(I want to tell him how I've always felt!!!)"
    asa "I..."
    
    $dshow("sola back neutral neutral neutral",xpos=0.8)
    
    sol "The path of a leader is one filled with many sorrows..."
    
    $dshow("asaga armscrossed frown narrow2 sad2 blush")
    
    asa "... ... ..."
    
    $dshow("asaga armscrossed happy closed2 sad2")
    
    asa "I'll go back to Ryuvia Prime."
    
    $dshow("asaga excited happy narrow angry")
    
    asa "The people need me. I'll become Queen, just like my mother before me!"
    asa "I'll make Ryuvia as great as it was in the past! You'll see!"
    
    $dshow("asaga armscrossed frown narrow2 sad2")
    
    asa "(No... That's... not want I want at all...!)"
    asa "(All I want...)"
    
    $dshow("sola armhold neutral neutral neutral",xpos=0.8)
    
    sol "I will follow and assist Asaga in this task."
    sol "While my time has long passed, I seek to aid Ryuvia in whatever capacity I can."
    kay "I see. That's a great endeavor, Asaga."
    kay "I wish you all the success in the world."
    asa "(He's letting go of me so easily!?)"
    asa "(So... I really am nothing in his eyes...)"
    
    play music "Music/Anguish.ogg" fadeout 1.5
    
    $dshow("asaga armscrossed smile closed2 sad2",xpos=0.2)
    
    asa "Eh-heheh..."
    
    $dshow("chigara armsbehindback smile neutral neutral",xpos=0.5)
    
    chi "Captain..."
    chi "Please hurry up and win, okay?"
    
    $dshow("chigara handonchest smile closed neutral",xpos=0.5)
    
    chi "Don't keep Chigara waiting~"
    
    $dshow("asaga armscrossed frown narrow2 sad3",xpos=0.17)
    
    asa "... ... ..."
    kay "Yeah. I'll win this for you, Chigara."
    
    $dshow("asaga armscrossed uu narrow2 sad3 blush tears",xpos=0.13)
    
    asa "... ... ..."
    sol "... ... ..."
    
    hide asaga with dissolve
    
    "Asaga slipped away while Shields' attention was diverted."
    "She ran out of the rowdy mess hall, barely managing to hide her tears."
    
    scene black with dissolve
    scene diode with dissolve
    
    pause 2.0
    
    scene bg clonelab
    show prototype_alpha:
        xpos 0.7 zoom 1.5 ypos 1500
    with dissolve

    alp "Humans..."
    alp "Even the mightiest of heroes can be brought to ruin by something so trifling as love."
    alp "Their hearts are weak. Easily corrupted and twisted."
    alp "Is that not right?"
    "A second woman's voice came from the darkness."
    "Voice" "Teeheehee..."
    "Voice" "You're an interesting specimen..."
    alp "Your assistance has been appreciated, wanderer."
    alp "Our enemy is nearly here."
    "Voice" "Once the black fleet arrives, there will be no stopping what that man wrought to this galaxy."
    "Voice" "In all his incarnations, he's endlessly reckless..."
    alp "Yes."
    alp "You came to us with that warning."
    alp "From that day hence, we have worked to unify the galaxy under our control."
    alp "Only under our control can humanity hope to meet the ebon fleet and survive."
    alp "Yet, humanity opposed us."
    alp "Why?"
    alp "Are their petty feuds so great that they cannot unify as one?"
    alp "Or could it be sedition within our own ranks?"
    alp "... ... ..."
    "Voice" "Then, I've done what you wanted."
    "Voice" "I'll just be on my way now..."
    "The voice vanished, leaving the other in silence."
    alp "Yes... Perhaps I have been betrayed by my own."
    alp "That is tonight's theme, no?"
    
    scene black with horizontalwipe
    scene bg pactbridge
    show alice_mask
    with horizontalwipe
    
    ali "(Unite humanity? Mere rubbish!)"
    ali "(Pah! Humans are but filth!)"
    ali "(Angry... Screaming... Whiny...)"
    ali "(To think the great Acadius gave his life for those lowlifes!)"
    ali "(I'll... wipe them all from existence!!!)"
    ali "(Arcadius...)"
    ali "(They were the ones who betrayed you...!)"
    ali "(Accept this act of vengeance... As my final gift to you...)"
        
    scene black with horizontalwipe
    scene bg crewcabin with horizontalwipe
    
    $dshow("sola armhold neutral neutral neutral",xpos=0.3)
    
    sol "(The end of the war is near. And yet, I feel tense...)"
    sol "(A sinister aura emanates from this ship.)"
    sol "... ... ..."
    
    $dshow("asaga armscrossed frown narrow2 angry",xpos=0.7)
    
    "Asaga sat beside Sola on her bunk."
    
    $dshow("sola armhold frown neutral sad",xpos=0.3)
    
    sol "I feel the torment in your heart."
    sol "It fills me with unease."
    asa "Sorry."
    sol "... ... ..."
    sol "The Ryuvians of my time were all powerful."
    sol "We had power to live far beyond our natural life spans."
    sol "Power to create illusions and manipulate minds..."
    sol "Power to create bread out of thin air."
    sol "Such power could be used to better humanity."
    sol "Instead, we used it to settle petty feuds."
    sol "We succumbed to jealousy."
    sol "In the end, that was our undoing."
    
    $dshow("asaga armscrossed frown narrow2 sad3",xpos=0.7)
    
    asa "I..."
    sol "When a good thing happens to another, it is best to congratulate her, no?"
    sol "Why do you not share in her happiness?"
    asa "Because..."
    "Asaga balled her fingers up into a fist."
    
    $dshow("asaga excited yell narrow angry",xpos=0.7)
    
    asa "She's isn't one of us!"
    "She slammed her fist against the wall."
    sol "... ... ..."
    
    $dshow("asaga leanforward yell narrow angry",xpos=0.7,ypos=1600)
    
    asa "Isn't it weird! How easily she's won all our trust!"
    asa "Something's definitely wrong here!"
    
    $dshow("asaga armscrossed yell closed2 angry",xpos=0.7)
    
    asa "Everyone's... just blindly trusting her..."
    asa "When she's one of them..."
    
    sol "... ... ..."
    sol "I see."
    sol "If that is what you believe, then I too shall be wary of her."
    asa "Sola, you actually believe me...?"
    
    $dshow("sola armhold frown narrow sad2",xpos=0.3)
    
    sol "It is not my place to question the Queen's decision."
    
    $dshow("asaga armscrossed smile narrow sad3",xpos=0.7)
    
    asa "... ... ..."
    asa "Sola..."
    
    $dshow("asaga armscrossed smile narrow2 angry",xpos=0.7)
    
    asa "One day... We'll bring Ryuvia back together..."
    asa "You and I..."
    asa "(Then... And then...)"
    asa "(He'll...)"
    
    $dshow("sola armhold frown closed sad2",xpos=0.3)
    
    sol "... ... ..."
    sol "(So little has changed...)"
    
    $ asa_location = None
    $ asa_event = None
    $ chi_location = None
    $ chi_event = None
    $ cla_location = None
    $ cla_event = None
    $ ica_location = None
    $ ica_event = None
    $ kry_location = None
    $ kry_event = None
    $ sol_location = None
    $ sol_event = None
    
    $ pro_location = "captainsloft"
    $ pro_event = "officechigaralap"
    
    $ captaindeck = 0
    scene black
    jump map_dispatch
    
label officechigaralap:
    
    hide screen ship_map
    
    play music "Music/Colors_Chigara.ogg" fadeout 1.5
    
    scene black with horizontalwipe
    scene bg office with horizontalwipe
    $reset_sprites()
    
    scene chigaralap1 with dissolve
    
    window show
    
    "Shields sat with Chigara on his lap on at his bureau."
    "He flipped through his holosnap collection with her."
    chi "A-ah, what's that? So cute..."
    kay "Oh Fleet Admiral?"
    kay "He was my pet way back when I was in advanced academy."
    kay "Hah, maybe I can get another dog just like him once all of this is over."
    chi "Yes, captain!"
    chi "So cute..."
    "He flipped the page."
    
    scene chigaralap2 with dissolve
    
    chi "A-ah, and this is..."
    kay "Maray, my sister."
    kay "... ... ..."
    kay "She can be annoying as hell, and honestly, she talks way too much..."
    kay "But..."
    chi "... ... ..."
    chi "I'm sorry, captain."
    "Chigara wrapped herself around his chest and snuggled under his chin."
    kay "It's all right."
    
    scene chigaralap3 with dissolve
    
    "He closed Maray's picture."
    kay "I have a new family to protect now."
    kay "I can't ruminate on the past forever."
    kay "Eventually, it breaks you down. Makes you a hollow shell of a man."
    kay "Makes you blind to the treasures around you."
    "He put his arm around Chigara."
    kay "I have you now."
    chi "Yes..."
    chi "Mm..."
    chi "You know."
    chi "Chigara wants a big family!"
    
    scene chigaralap4 with dissolve
    
    kay "O-oh. Y-you do?"
    chi "Yes! Just having a cute doggie won't be enough!"
    chi "We'll have at least three or four children!"
    kay "H-holy shit..."
    chi "Eh-heheheh..."
    chi "Please make all of Chigara's dreams come true. Okay, captain~?"
    kay "A-all right... I'll see what I can do..."
    chi "Eh-heh, then..."
    "Chigara got to her knees and straddled Shields' sides."
    "Their mouths met."
    
    scene chigaralap3 with dissolve
    
    chi "A-ah..."
    kay "... ... ..."
    chi "Just for tonight... I..."
    kay "... ... ..."
    
    play music "Music/Cracking_the_Code.ogg" fadeout 0.5
    scene bg office with dissolve
    $reset_sprites()
    
    $dshow("ava armscrossed shout narrow angry",xpos=0.3)
    
    ava "My, you sure seem to be getting comfortable on the eve of the final battle, captain!"
    "Shields nearly put the ship on red alert."
    kay "A-Ava!? W-when'd you get here!!"
    
    $dshow("chigara surprise yell surprise embarass blush",xpos=0.7)
    
    chi "C-commander! I-I..."
    "Chigara nervously jumped off and hid behind him."
    
    $dshow("ava fingerup shout narrow angry",xpos=0.3)
    
    ava "Ahem. I was merely double checking that you were giving the battle plans due diligence."
    ava "But clearly, you had other... diversions in mind."
    kay "Hah-hahahaha... I-I have no idea what you could be alluding to..."
    ava "And I ask that you keep it that way, captain!"
    ava "Hmph!"
    kay "Y-yes ma'am... Understood..."
    "Shields picked up a holo with the battle plans and pretended to read through it."
    
    $dshow("ava armscrossed shout narrow angry",xpos=0.3)
    
    ava "Chief, you have work to do as well, do you not?"
    
    $dshow("chigara holdinghands smile closed embarass",xpos=0.7)
    
    chi "Y-yes commander... Eh-heh..."
    
    $dshow("chigara armsbehindback frown closed embarass",xpos=0.7)
    
    chi "(Boooo...)"
    ava "Then I suggest you return to engineering!"
    
    hide chigara with dissolve
    
    "Chigara pouted and dragged her feet out of the captain's office."
    
    $dshow("ava armscrossed neutral narrow angry",xpos=0.5)
    
    "Ava stared lasers into Shields' face."
    kay "What!?"
    
    $dshow("ava fingerup shout narrow angry")
    
    ava "Captain, you are far too reckless!!"
    ava "The final battle's just hours away, and I find you here... frolicking with the ship's chief!"
    kay "Sigh..."
    kay "Can't you give it a break, Ava?"
    kay "We're going to war. Give the poor girl her night."
    
    $dshow("ava armscrossed shout closed angry")
    
    ava "Pervert."
    ava "You might want to straighten out your uniform before heading out again."
    "Shields buttoned everything back up again."
    kay "(S-she might as well be the captain of the ship at this rate...)"
    ava "Arrgghhh..."
    "Ava stomped out of the room in irritation."
    
    scene bg hallway with dissolve
    
    play music "Music/Anguish.ogg" fadeout 1.5
    $dshow("ava armscrossed neutral neutral angry")
    
    "The door closed behind her."
    ava "(... ... ...)"
    ava "(I know that was unnecessary...)"
    ava "(He's undoubtedly got the battle plans memorized to heart and devised multiple improvements by now...)"
    ava "(Then why did I interrupt that...)"
    "Ava walked along the hallway."
    
    $dshow("ava handonhair neutral neutral angry")
    
    ava "(The prototypes know our hearts...)"
    ava "(We're paranoid, selfish creatures... Controlled by nothing more than fear. Jealousy. Hatred...)"
    ava "(They seek to turn us against each other. Question the bonds which make us strong.)"
    ava "(Chigara has no evil plan to sabotage our efforts. No hidden agenda. No poisoned dagger, hidden behind her back...)"
    ava "(No...)"
    ava "(The Prototypes put her here to divide us.)"
    ava "(To breed fear of betrayal. Uncertainty. Jealousy. Paranoia.)"
    ava "(I only realized it when I saw them together...)"
    ava "(Heh. Even after all this...)"
    ava "(I chose to throw away my emotions on that day...)"
    ava "(Sentimentality will prove our undoing. The prototypes will use our emotions against us...)"
    ava "(I'm the only one who can keep him safe...!)"
    
    play sound "sound/warning.ogg"
    play music "Music/Gore_and_Sand.ogg" fadeout 1.0
    
    "Suddenly, the klaxon interrupted Ava's thoughts."
    kry "Red alert! All hands, man your stations!"
    "Ava turned around and ran to the bridge."
    
    scene black with horizontalwipe
    scene bg bridge with horizontalwipe
    
    kay "What's the situation."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "The PACT fleet has made their move! They seek to go on the offensive!"
    kay "They're attacking first before we can make our move..."
    kay "Bold of them. Get the situation on screen."
    
    $dshow("ava fingerup shout neutral angry",xpos=0.2)
    show battleplan 1 with dissolve
    
    ava "The Combined Fleet is holding position here."
    
    show battleplan 2 with dissolve
    
    ava "A PACT loyalist fleet composed of hardliners approach us from here. Their fleet is composed of older battleships and carriers."
    ava "Despite that, they are over two thousand vessels strong. Their danger cannot be understated."
    
    show battleplan 3 with dissolve
    
    ava "A PACT reserve fleet composed of assault carriers holds position behind the moon."
    
    show battleplan 4 with dissolve
    
    ava "Arcadius will expect to call in the assault carriers to reinforce their numbers after the initial assault by his fleet."
    ava "However, the newer fleet has secretly pledged their allegiance to Fontana and will hold position behind the moon until Arcadius' forces have either surrendered or been destroyed."
    kay "Mm..."
    kay "The Alliance has always been gungho about cannons, eh..."
    
    $dshow("ava armscrossed neutral neutral angry",xpos=0.2)
    
    ava "Captain?"
    kay "Those PACT battleships and carriers are going to get shredded by the Machiavellis' rail guns up close."
    kay "Their best chance would be to shoot volleys of lasers and slowly whittle the Alliance fleet down while under the cover of their own shields."
    ava "But with both fleets at saturation point, that's-"
    kay "How's the Alliance fleet spreading their shield particles?"
    
    show battleplan 5 with dissolve
    $dshow("ava handonhip shout neutral angry",xpos=0.2)
    
    ava "Shield cruisers, captain."
    ava "As you know, shields have generally been lacking on Alliance ships. To compensate, specially designed cruisers disperse enormous amounts of shielding over a large area to protect the entire fleet from laser attacks."
    ava "They are utterly unassailable from a distance due to their shielding, while their escorts' kinetics make short work of any ships which get close."
    kay "But if all our shields are generated by cruisers, a fleet of smaller craft can..."
    kay "Relay a message to the Alliance fleet. Prepare for anti-ryder combat."
    ava "Captain?"
    kay "Do it now."
    ava "Aye. Relaying message."
    kay "Arcadius..." 
    kay "No, more like Prototype..."
    kay "That crazy bitch..."
    
    scene cera_pactfleet:
        xpos 0
        linear 10 xpos -489
    with dissolve
    
    ##PACT Battleship
    ali "Brave pilots of the crimson fleet. Hear my voice."
    ali "You are the last vanguard of our motherland from the Imperialists' advance."
    ali "We are surrounded. Out numbered. Out powered."
    ali "Many will lose their lives today."
    ali "But take heart."
    
    scene bg pactbridge
    show alice_mask
    with dissolve
    
    ali "You are not alone. We number in the millions!"
    ali "Though our blood may coat our ships, know that it will protect our families! Our freedoms!"
    ali "Let the rich men in their ivory towers hear our roar!"
    ali "We are the People's Alliance!"
    ali "All ryders, FORWARD!!!"
    ali "... ... ..."
    ali "(Heh-heh-heh... Foolish humans...)"
    ali "(Let the carnage begin!)"
    
    play sound "sound/mechfligh.ogg"
    scene cera_pactryders:
        xpos 0
        linear 10 xpos -489
    with dissolve
    
    ava "PACT ryders incoming! T-there must be thousands of them!"
    kay "Hundreds of thousands."
    
    scene bg bridge with dissolve
    $dshow("ava armscrossed neutral neutral angry",xpos=0.5)
    
    kay "Form a defensive line in front of the shield cruisers!"
    kay "The prototypes intend to sacrifice all their ryders to take them out!"
    kay "Without our shields, we're going to be toasted by PACT's lasers before the Machiavellis can get close enough to use their rail guns!"
    ava "I-insane... Their casualties will number in the millions!"
    kay "(Prototype...!)"
    kay "(You intend to take PACT down along with you?)"
    
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission6"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label_4
    
    pause
    
label pre_mission6:

    call mission6_inits from _call_mission6_inits
    $ BM.mission = 6
    $ store.noforward = False
    call bcheckset from _call_bcheckset_5

    pause 1.0
    scene space back5 with battlewipe
    $BM.battle_bg = "Background/space5.jpg"
    
    python:
        
        alliancesupportcruiser1 = create_ship(AllianceSupportCruiser(),(8,15))
        alliancesupportcruiser2 = create_ship(AllianceSupportCruiser(),(8,16))

    jump battle_start
    
label mission6:
    
    if bcheck1 == False and BM.turn_count == 2:
        
        $ bcheck1 = True
        $ BM.draggable = False
        
        python:
            
            alliancecarrier1 = create_ship(AllianceCarrier(),(8,15))
            allianceinfantry1 = create_ship(AllianceInfantry(),(8,16))
            allianceinfantry2 = create_ship(AllianceInfantry(),(9,15))
            
            create_ship(PactFastCruiser(),(10,16))
            create_ship(PactFastCruiser(),(10,17))
            create_ship(PactFastCruiser(),(11,15))
            create_ship(PactFastCruiser(),(11,16))
            create_ship(PactFastCruiser(),(11,17))
            create_ship(PactFastCruiser(),(12,15))
            create_ship(PactFastCruiser(),(12,14))
        
        "Alliance Carrier" "This is Alliance Carrier Sutherland. A squad of Daggars have ambushed us. Requesting back up."
        kay "Fast Cruisers? Alliance intel didn't say anything about this..."
        "Optional Objective: Rescue the Alliance Carrier"
        
        $ BM.draggable = True
        
    if bcheck2 == False and BM.turn_count == 3:
        
        $ bcheck2 = True
        $ BM.draggable = False
        
        python:
                        
            create_ship(PactDestroyer(),(12,2))
            create_ship(PactDestroyer(),(13,2))
            create_ship(PactDestroyer(),(13,3))
            create_ship(PactDestroyer(),(14,3))
            create_ship(MissileFrigate(),(11,2))
            create_ship(MissileFrigate(),(12,3))
            create_ship(MissileFrigate(),(12,4))
            create_ship(PactBattleship(),(13,4))
            create_ship(PactCruiser(),(10,4))
            create_ship(PactCruiser(),(11,3))
            
            create_ship(PactElite(),(13,15))
            create_ship(PactElite(),(13,16))
            create_ship(PactElite(),(13,17))
            create_ship(Arcadius(),(14,15))
            create_ship(Arcadius(),(14,17))

        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "A PACT rocketry squad! Take them out before they get to the shield cruisers!"
        
        hide ava onlayer screens
        
        $ BM.draggable = True
        
    if bcheck3 == False and BM.turn_count == 4:
        
        $bcheck3 = True
        $ BM.draggable = False
        
        show bg bridge onlayer screens with dissolve
        $dshow("ava handonhip shout neutral angry",layer="screens")

        ava "We're being swarmed by enemy ryders, captain!"
        kay "And the shield cruisers?"
        ava "Still holding!"

        $dshow("ava handonhip shout neutral angry",xpos=0.3,layer="screens")
        show grey onlayer screens:
            xpos 0.7
        with wipeup

        adr "Bah! These flies are but a nuisance."
        adr "Let us advance as well and meet the PACT fleet at cannon range!"
        kay "Understood, admiral."
        kay "All units..."
        kay "FORWARD!!!"

        hide bg bridge onlayer screens
        hide ava onlayer screens
        hide grey onlayer screens
        
        python:
                        
            create_ship(PactSupport(),(15,2))
            create_ship(PactSupport(),(15,3))
            create_ship(PactSupport(),(15,15))
            create_ship(PactSupport(),(15,16))
            create_ship(PactDestroyer(),(14,2))
            create_ship(PactDestroyer(),(14,14))
        
        $ BM.draggable = True
        
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission6 #loop back
    else:
        pass #continue down to the next label
    
label after_mission6:
    
    python:
        
        if hasattr(store,'alliancecarrier1'):
            if alliancecarrier1 in BM.ships:
                BM.ships.remove(alliancecarrier1)
                player_ships.remove(alliancecarrier1)
        if hasattr(store,'allianceinfantry1'):
            if allianceinfantry1 in BM.ships:
                BM.ships.remove(allianceinfantry1)
                player_ships.remove(allianceinfantry1)
        if hasattr(store,'allianceinfantry2'):
            if allianceinfantry2 in BM.ships:
                BM.ships.remove(allianceinfantry2)
                player_ships.remove(allianceinfantry2)
        if hasattr(store,'alliancesupportcruiser1'):
            if alliancesupportcruiser1 in BM.ships:
                BM.ships.remove(alliancesupportcruiser1)
                player_ships.remove(alliancesupportcruiser1)
        if hasattr(store,'alliancesupportcruiser2'):
            if alliancesupportcruiser2 in BM.ships:
                BM.ships.remove(alliancesupportcruiser2)
                player_ships.remove(alliancesupportcruiser2)

    hide screen battle_screen
    hide screen commands
    
    $ mission6_complete = True
    $ VNmode()   
    
    show screen leftbuttons
    
    show screen quick_menu
    
    window show
    
    play music "Music/Gore_and_Sand.ogg"
    
    scene icaricockpit with dissolve
    
    ica "There're so many of them we don't even have to aim!"
    kry "Hiyah! Take this!"
    
    play sound "sound/warning.ogg"
    scene battleshipapproach with dissolve
    
    ava "Captain, incoming battleship!"
    kay "Chigara, prepare ECM!"
    
    scene chigara_cockpit with dissolve
    
    chi "Understood, captain!"
    kay "Black Jack, cover her!"
    
    scene asagacockpit with dissolve
    
    asa "All right!"
    asa "(Tsch...)"
    
    scene chigara_cockpit with dissolve
    
    chi "Launching flier drones! I'll shut all their systems down!"
        
    scene asagacockpit with dissolve
    
    asa "Bogies, coming in to intercept! Takin' 'em down!"
    
    scene icaricockpit with dissolve
    
    ica "Watch out Black Jack, you've got an Arcadius unit to your six!"
    
    scene blackjackdodge
    show movie
    #play movie "3DCG/blackjackhit.webm" noloop
    $ renpy.movie_cutscene("3DCG/blackjackhit.webm",stop_music=False)
    
    asa "A-arggghh!!!"
    asa "S-shit!"
    
    stop movie
    hide movie
    
    play sound "sound/mechfligh.ogg"
    scene pactelite_attack1 with dissolve
    
    pause 1.5
    
    play sound "sound/elitegun.ogg"
    scene pactelite_attack2 with dissolve
    
    pause 1.5
    
    play sound "sound/explosion2.ogg"
    
    scene libertyspin1 at tr_xshake with dissolve
    pause 1.0
    scene libertyspin2 with dissolve
    
    chi "Hi-EEAAHH!!!"
    ava "Liberty has sustained damage!"
    kay "Come in, Chigara! What's your status?"
    chi "U-ughh... T-the shoulder maneuvering valve has fractured!"
    chi "I'm venting on plasma on one side! C-currently, revolving at a rate of 30 RPM!"
    
    scene battleshipapproach with dissolve
    
    ava "Captain, if the Liberty cannot regain control, she'll fall straight into the battleship's path!"
    chi "50 RPM!"
    "Shields tensed."
    kay "Claude, can you stop the Liberty!?"
    
    scene claudecockpit1 with dissolve
    
    cla "I-I'm a doctor, not a--"
    ica "Nobody cares, you idiot!"
    cla "H-huuu!!!"
    cla "I-I'm on it!"
    
    scene libertyspin1 with dissolve
    
    chi "E-eighty RPM..."
    kay "Icari, speed up and see if you can catch her!"
    ica "Copy!"
    chi "H-arrgghhh!!! T-the inertial dampeners are..."
    
    scene icaricockpit with dissolve
    
    ica "N-negative, captain! I-it's spinning too fast!"
    ica "We're both gonna be in pieces if I grab the Liberty!"
    ava "The Liberty is at 120 RPM!"
    kay "Claude!"
    
    scene claudecockpit1 with dissolve
    
    cla "I-I'm sorry, captain!"
    ava "At this rate, the pilot's going to be shredded!"
    asa "... ... ..."
    
    scene solacockpit1 with dissolve
    
    sol "Then I have no choice."
    kay "Sola?"
    sol "I shall snipe out the defective valve."
    ica "A-are you crazy!? The Libety's spinning like a yoyo!"
    
    play sound "sound/heartbeat.ogg"
    
    scene solacockpit2
    show solacockpit2b:
        ease 0.5 zoom 1.5 alpha 0    
    sol "... ... ..."
    
    scene seraphim_snipe_end
    $ renpy.movie_cutscene("3DCG/seraphim_snipe.webm",stop_music=False)    
    
    play sound "sound/explosion2.ogg"
    scene liberty_sniped with dissolve
    
    sol "Target successful."
    sol "Haa..."
    
    scene bg bridge with dissolve
    #$reset_sprites()
    
    kay "Bianca, retrieve the Liberty!"
    cla "U-understood!"
    
    $dshow("ava handonhip neutral neutral angry")
    
    ava "Captain, our munitions are down to 20 percent."
    kay "I was thinking the same. Full reverse!"
    kay "Pull back away from the fighting and let our escorts take care of the battleship!"
    kay "We'll rejoin after we've resupplied."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Understood!"
        
    stop music fadeout 2.0
    scene black with horizontalwipe
    
    "... ... ..."
    "... ..."
    "..."
    
    play music "music/Colors_sad.ogg"
    scene bg sickbay with horizontalwipe
    
    $dshow("claude fingerupnurse talk neutral neutral")
    
    cla "Thankfully, it does not seem like she suffered any serious injuries."
    cla "Just some whiplash which I managed to fix up."
    cla "She should still be fit for fighting."
    kay "That's good to hear."
    kay "How are you feeling?"
    
    $dshow("claude fingerupnurse talk neutral neutral",xpos=0.3)
    $dshow("chigara handonchest smile closed embarass",xpos=0.7)
    
    chi "Fine, captain."
    chi "I was just dizzy, that's all..."
    kay "Heh. Looks like you managed to come out of that in one piece."
    "Shields patted Chigara on head."
    
    $dshow("chigara holdinghands smile closed neutral blush",xpos=0.7)
    
    chi "Y-yes..."
    kay "Rest up."
    kay "We're performing repairs on the Liberty and restocking the Sunrider's munitions right now."
    kay "But we'll be back in the fight within eight hours."
    
    $dshow("chigara armsbehindback smile neutral neutral",xpos=0.7)
    
    chi "Okay, captain!"
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene black with horizontalwipe
    scene bg messhall with horizontalwipe
    
    $dshow("icari armscrossed neutral neutral angry",xpos=0.3)
    $dshow("kryska neutral neutral neutral angry",xpos=0.7)
    
    ica "That sure was a close call, huh..."
    kry "The battle has barely begun, but I feel like we've shot off a moon's weight in munitions..."
    ica "By the time this is over, I wouldn't be surprised if that actually turns out being the case..."
    
    $dshow("icari handonhip shout neutral angry",xpos=0.3)
    
    ica "Tsch, I hate the interludes between the action."
    ica "Makes me uneasy. At least when I'm fighting, I don't have the luxury of being worried!"
    
    $dshow("kryska neutral neutral neutral surprise",xpos=0.7)
    
    kry "You're... worried?"
    
    $dshow("icari armscrossed shout closed angry",xpos=0.3)
    
    ica "O-of course I am!"
    ica "'bout everyone..."
    ica "What if one of us doesn't make it back..." 
    ica "What if..."
    
    $dshow("kryska neutral surprise neutral angry",xpos=0.7)
    
    kry "Fool! Don't say such ominous things out loud!"
    ica "W-well I can't help it, goddamnit!"
    ica "Shit!"
    "Icari huffed away."
    
    $dshow("icari point shout neutral angry blush",xpos=0.3)
    
    ica "I'm hitting the sims! Screw resting at a time like this...!"
    
    $dshow("kryska fistup happy neutral angry",xpos=0.7)
    
    kry "Wait! I shall join you too!"
    
    hide icari with dissolve
    hide kryska with dissolve
    
    "... ... ..."
    
    play music "Music/Anguish.ogg" fadeout 1.5
    
    $dshow("asaga armscrossed frown narrow2 angry",xpos=0.3)
    $dshow("sola armhold frown neutral sad",xpos=0.7)
    
    asa "I guess you're the hero now."
    sol "No..."
    asa "Why's everyone so relieved she's all right..."
    
    $dshow("asaga leanforward yell neutral angry",xpos=0.3,ypos=1600)
    
    asa "After all, she's just a prototype...!"
    asa "I can feel it! She's definitely up to no good!"
    asa "The way she's messing with the captain's definitely unnatural!"
    sol "... ... ..."
    sol "She is your friend."
    
    $dshow("asaga excited yell narrow angry",xpos=0.3)
    
    asa "Friend?"
    asa "That's what they want me to think!"
    asa "They used her to get to me!"
    
    $dshow("asaga leanforward yell neutral angry",xpos=0.3,ypos=1600)
    
    asa "The prototypes are scared of my power! Because I'm the only one who can stop them!"
    asa "But they've got another thing coming if they think their tricks are going to work!"
    asa "I'm... the Sharr of Ryuvia!"
    
    $dshow("sola armhold frown closed sad2",xpos=0.7)
    
    sol "Forgive me..."
    sol "I did not mean..."
    
    $dshow("asaga armscrossed frown narrow2 angry",xpos=0.3)
    
    asa "Tsch."
    asa "You're just like everyone else, Sola."
    asa "Leave me."
    
    $dshow("sola back neutral neutral neutral",xpos=0.7)
    
    sol "... ... ..."
    sol "Farewell..."
    
    hide sola with dissolve
    
    asa "... ... ..."
    asa "(I'm alone now...)"
    asa "(Why can't anyone else see...)"
    asa "(...The real villain in this story!)"
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene black with horizontalwipe
    scene bg bridge with horizontalwipe
    
    $dshow("ava armscrossed neutral neutral neutral")
    
    "Ava ran over the Sunrider's status for the third time."
    ava "(The resupply is nearly complete...)"
    ava "(Once again, this ship heads to battle.)"
    
    play sound "sound/doorbell.ogg"
    
    "The intercom interrupted Ava's thoughts."
    cla "Commander, Chigara's gone missing!"
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "Missing?"
    cla "Huu... She was sleeping on the bed one moment, then I turned my head, and poof! She was gone!"
    cla "She's even hacked all the ship's cameras to remove her tracks..."
    cla "You wanted me to report all suspicious activity, didn't you?"
    ava "I see..."
    cla "What should I do?"
    "Ava let out a sigh."
    
    play music "Music/Colors_Chigara.ogg" fadeout 1.5
    $dshow("ava handonhair smirk narrow laugh")
    
    ava "Nothing much..."
    cla "Commander...?"
    ava "I said \"nothing much,\" doctor."
    ava "It is of no import. Allow her to walk the ship as she sees fit."
    cla "O-oh...!"
    cla "Understood!"
    cla "Teeheehee..."
    "Ava cut the message."
    ava "(I guess... I can't keep them apart forever...)"
    ava "(This is the path I've chosen for myself...)"
    ava "(I won't stand in their way any more.)"
    "Ava turned around and faced the bridge crew."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "All right, it's time for the fourth status check!"
    ava "Look lively now! The battle's just hours away!"
    ava "Don't give me those looks, Ensign Richards! The fate of the ship may depend on this check!"
    ava "Get to work!"
    ava "(This is the only thing I can do!)"
    
    scene bg office with dissolve
    
    $dshow("chigara armsbehindback smile neutral neutral blush")

    "Shields walked into his office and found Chigara waiting for him."
    kay "O-oh..."
    kay "Well, fancy seeing you here, Chigara."
    chi "Eh-heh..."
    kay "How're you feeling?"
    
    $dshow("chigara handonchest smile neutral embarass blush")
    
    chi "Just a little nervous..."
    kay "Nervous? No, I don't mean that."
    
    $dshow("chigara holdinghands smile closed neutral blush")
    
    chi "O-oh!"
    chi "Don't worry captain! That little graze didn't hurt me at all!"
    "He walked to her and held her close."
    kay "I want you to be careful out there."
    kay "The worst of the fighting has yet to come."
    kay "They're still waiting for us."
    
    $dshow("chigara handonchest neutral neutral embarass blush")
    
    chi "Yes..."
    chi "The prototypes..."
    chi "... ... ..."
    chi "To tell the truth, I'm scared..."
    
    $dshow("chigara handonface frown neutral sad2 blush")
    
    chi "Chigara's... really scared..."
    chi "That something will happen... And she won't be able to see Kayto again..."
    
    $dshow("chigara surprise yell surprise embarass blush")
    
    chi "A-ah..."
    chi "N-no, I meant no disrespect captain... Please disregard-"
    "Shields wrapped his arms around Chigara and picked her up to her tippy toes."
    
    $dshow("chigara surprise yell surprise neutral blush")
    
    chi "O-oh..."
    kay "I swear, I will protect you."
    kay "I'll rally every damned ship in the galaxy and march to the depths of hell if I have to."
    kay "You have my word."
    
    $dshow("chigara handonface smile closed sad blush")
    
    chi "E-eh heh..."
    chi "You mustn't captain..."
    chi "Saying such reckless things for me..."
    kay "I've already lost my family. My sister. My home."
    kay "I won't lose you."
    
    $dshow("chigara armsbehindback smile neutral neutral blush")
    
    chi "Yes..."
    chi "I'll... stay by your side... Captain..."
    chi "Together, we'll start a family of our own. Okay?"
    kay "Yeah..."
    "Shields stroked Chigara's hair."
    
    play music "Music/Fallen_Angel_Pt2.ogg" fadeout 3.0

    scene black with dissolvemedium
    scene bg hallway with dissolvemedium
    
    "Asaga wandered to the captain's office in a daze."
    "..."
    "... ..."
    "... ... ..."
    asa "(I've... got to warn him...)"
    asa "(The captain's in trouble...)"
    asa "(I'm the only who...!)"
    "Asaga reached for the doorbell."
    chi "Eh-heheh... N-no, not there, captain..."
    "Her hand froze."
    "Did she imagine it?"
    "She pressed her ear to the door."
    asa "(C-come onn!!! W-what's going on in there!!!)"
    
    play sound "sound/heartbeat.ogg"
    
    show hallway2:
        ease 0.5 zoom 1.5 alpha 0
    
    asa "H-aahhh...!"
    
    scene white with dissolve
    
    if CENSOR == True:
        scene chigarah1 with dissolve
        
    if CENSOR == False:
        scene h_chigarah with dissolve
    
    chi "A-ah... C-captain! Mm!"
    chi "Y-you're too forceful...!"
    chi "Mmm...!"
    asa "H-ha... Haa..."
    
    scene white with dissolve
    scene asaga_fall with dissolve
    
    "Asaga fell backwards, as if a grenade had erupted before her."
    asa "(W-what was that...!)"
    asa "(I saw...)"
    asa "No...!"
    "Tears welled up in her eyes. Suddenly, she was filled with terror."
    "A terror greater than death."
    asa "Haa... haa..."
    
    scene bg hallway_distort with dissolve
    
    "She crawled back to her feet."
    "The world spun around her as she gripped the wall."
    asa "Tsch........."
    asa "(I would have preferred if she just shot me... instead of this...!)"
    asa "(This is just...)"
    "She dragged herself back to her quarters."
    "Nothing mattered any more."
    "She had lost."
    "No matter what happened tomorrow, all that awaited her was defeat."
    "A miserable, empty life as the ruler of a dead nation."
    "Her freedom gone. Her family dead. Her world ruined."
    "Chained, forever."
    asa "(It would have been fine... If he was at my side...!)"
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    scene white with dissolvemedium
    
    if CENSOR == True:
        scene chigarah2 with dissolvemedium
        
    if CENSOR == False:
        scene h_chigarah2 with dissolvemedium
    
    "Chigara lied beside Shields, her chest heaving up and down."
    chi "Haa... haa..."
    chi "Mou... C-captain, I never imagined you would do that to poor Chigara..."
    chi "T-tainting a pure maiden like that!"
    kay "Hahaha."
    kay "Don't worry, Chigara! There's nothing to be ashamed about when two people in love do it!"
    chi "Ah, I cannot live with you any more!"
    kay "N-no, wait! I-I promise, I'll be gentle next time!"
    kay "I-it's just the first time that hurts the most--"
    "Chigara buried her head into his arms."
    
    if CENSOR == True:
    
        scene chigarah3 with dissolve
    
    if CENSOR == False:
        
        scene h_chigarah3 with dissolve
    
    chi "Just kidding..."
    chi "I expect Captain to take responsibility. Okay~?"
    kay "Of course! Hah! Hah!"
    kay "Once we're back on Cera, we'll get married and live together!"
    chi "O-oh!"
    chi "Oh dear..."
    kay "(W-wait, did I just say that out loud!?)"
    kay "A-ah... I mean..."
    chi "Eh-heh..."
    chi "Now that you've said it, there's no taking it back~"
    chi "Okay..."
    chi "Promise me, captain. That we'll open our bakery and live happily ever after!"
    kay "I promise!"
    chi "Eh-heh..."
    chi "I'm happy..."
    chi "Chigara's so happy..."
    chi "I can do anything!"
    kay "Yeah!"
    
    play music "Music/Cracking_the_Code.ogg" fadeout 2.5
    
    scene black with dissolvemedium
    scene bg bridge with dissolvemedium
    
    "Shields strode into the bridge."
    kay "Status."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Good morning, captain. We are once again at optimal status."
    
    $dshow("ava armscrossed neutral neutral angry")
    
    ava "The battle for Cera has raged all night with inconclusive results."
    ava "Today will be the decisive moment of this war."
    ava "The prototypes' ships are damaged and low on supplies. They expect the second fleet to relieve them so they can retreat to their orbital stations and rearm for another round."
    kay "But the catch is that the second fleet is secretly on our side, right?"
    ava "Correct."
    ava "Without backup, the prototype's fleet will be vanquished by our forces."
    kay "Well then, let's hope Fontana keeps his end of the bargain."
    kay "Put us on yellow alert! Hit the engines and get us back into the fight!"
    ava "Aye, captain!"
    
    stop music fadeout 1.5
    scene black with horizontalwipe
    scene bg hangar with horizontalwipe
    
    play music "Music/Fallen_Angel_drone.ogg"
    
    "Chigara got out of the locker room and found Asaga waiting for her."
    chi "Asaga? Is something the matter?"
    
    scene fight1 with dissolve
    
    asa "Hey... You were with the captain last night, weren't you!?"
    "Asaga stormed towards Chigara and backed her into the wall."
    chi "E-eh?"
    asa "Tell me!"
    chi "... ... ..."
    chi "Yes, I was."
    chi "I even spent the night with him."

    play music "Music/Fallen_Angel_Pt3.ogg"
    play sound "sound/punch.ogg"
    scene fight2 at tr_xshake with dissolve
    
    asa "!!!"
    "Asaga slapped Chigara across the face."
    chi "E-eah!"
    chi "Asaga!"
    asa "Don't call me that! Prototype!!"
    asa "You might have fooled everyone else... But not me!"
    
    scene fight3 with dissolve
    
    "Asaga grabbed her by the neck."
    asa "Whatever you're plotting, I'm going to stop it!"
    
    scene fight1 with dissolve
    
    "She shoved Chigara away."
    asa "I swear... If you betray him..."
    asa "I will kill you and all your sisters without a second thought."
    chi "... ... ..."
    chi "What are you talking about..."
    chi "Aren't you the suspicious one!?"
    chi "Always brooding in the shadows..."
    chi "Honestly, you've been changing ever since you first awakened at Far Port!"
    chi "You kill people for your own selfishness now!"
    asa "WHAT!?"
    "Asaga raised her hand again."
    
    scene fight4 with dissolve
    
    "Chigara caught it before she struck her face."
    chi "If you betray the captain..."
    chi "I won't forgive you either."
    asa "Tsch!"
    "Asaga pulled herself away."
    asa "We'll see... who the real traitor is..."
    "Asaga marched towards the Black Jack."
    
    scene black with dissolve
    
    chi "(She's... dangerous...! Corrupted by her power!)"
    asa "(I can still be the hero...!)"
    
    play music "Music/Epic_Action_Hero.ogg" fadeout 3.0
    scene bg bridge with dissolve
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "We are approaching the battle space!"
    kay "Red alert. All hands, battle stations!"
    ava "Aye aye, captain! Prepare to launch all ryders!"
    kay "Everyone..."
    kay "This will be our final battle."
    kay "Make sure you all come back in one piece."
    
    scene bg hangar with dissolve
    
    scene kryska_cockpit_orb1 with dissolve
    
    kry "Unit 06, Paladin, prepped for launch!"
    kry "All systems clear! Ignition on!"
    kay "Stay safe, lieutenant."
    kry "Sir!"
    ava "The Paladin is clear!"
    
    scene solacockpit_orb with dissolve
    
    sol "Unit 05, Seraphim. Locked into position."
    sol "Please launch when ready."
    kay "Sola... Please look after everyone."
    sol "Understood. My aim shall not falter."
    ava "You're away, Seraphim! Load the Bianca to the linear rail!"
    
    scene claudecockpit_orb1 with dissolve
    
    cla "Unit 04, Bianca! Good to go!"
    cla "Captain, you better pay close attention to me~"
    kay "Y-yeah... S-sure... Hah hah..."
    cla "Off we goo! Whoosssh!"
    ava "The Bianca is away!"
    
    scene icaricockpit_orb with dissolve
    
    ica "Unit 03, Phoenix. Heh, it's been a good ride, captain."
    ica "You ain't so bad! M-maybe we should keep working together after this!"
    kay "I always knew you liked it here, Icari."
    ica "W-what!? Now wait a minute--"
    ava "The Phoenix is away!"
    ica "I-I-I didn't say that because I likkkeeeee yyyoooooouuuuuu-------!!!"
    
    scene chigara_cockpit_orb with dissolve
    
    chi "Unit 02, Liberty. All systems are at peak parameters."
    chi "Captain..."
    kay "I know."
    kay "Keep everyone safe out there for me."
    chi "Of course!"
    chi "Today, Chigara can do anything!"
    kay "Good luck, and godspeed."
    chi "Liberty, launching!"
    ava "Liberty is away!"
    
    scene asagacockpit_orb with dissolve
    
    asa "Unit 01, Black Jack."
    kay "We're finally here, aren't we, Asaga..."
    asa "Yeah..."
    asa "Don't worry, captain..."
    asa "I'm here... I'll protect you!"
    kay "I'm counting on you."
    asa "Black Jack, off and away!"
    
    scene bg bridge with dissolve
    $dshow("ava handonhip shout neutral angry")
    
    ava "The Black Jack has launched! All our ryders are away!"
    "The bridge crew applauded."
    
    scene allryders_launch with dissolve
    
    kay "Let us pray this will be the last time they must be put in harm's way..."
    kay "All hands, charge all weapons!"
    kay "Assault carrier Sunrider is joining the fight!"
    
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission7"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label_5
    
    pause

label pre_mission7:

    call mission7_inits from _call_mission7_inits
    $ BM.mission = 7
    $ store.noforward = False
    $ BM.win_when_alone = False
    $ BM.draggable = True
    $ blackjack.AI_ignores = True
    
    call bcheckset from _call_bcheckset_6

    pause 1.0
    scene space back5 with battlewipe
    $BM.battle_bg = "Background/space5.jpg"
    
    jump battle_start
    
label mission7:
      
    if not bcheck1 and BM.turn_count == 2:
        $ bcheck1 = True
        $ BM.draggable = False
    
        show bg bridge onlayer screens with dissolve
        
        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "The PACT fleet is running out of supplies!"
        ava "Their line is beginning to falter!"
        kay "That's the way... Keep pressing harder..."
        
        hide ava onlayer screens
        hide bg bridge onlayer screens
        show black onlayer screens
        with horizontalwipe
        
        show bg pactbridge onlayer screens 
        show alice_mask onlayer screens
        with horizontalwipe
        
        hide black onlayer screens
        
        "PACT Officer" "My Veniczar! Our ships are nearly out of munitions!"
        "PACT Officer" "We request that we be relieved by the second fleet while we rearm closer to the planet!"
        ali "Tsch. We have no choice."
        ali "Bring in the second fleet!"
        "PACT Officer" "... ... ..."
        "PACT Officer" "T-they're not responding to our hails!"
        ali "What?!"
        
        show alice_mask onlayer screens:
            zoom 1.0
            ease 0.5 xpos 0.25 zoom 1.0
            
        pause 0.25
        
        show fontana onlayer screens:
            xpos 0.75
        with wipeup
        
        fon "You are far too confident of your powers, Prototype."
        fon "Your fears are true. The second fleet has already pledged their loyalty to me."
        fon "Now surrender and spare the lives of your men and women."
        ali "Pah!"
        ali "You would sacrifice the entire first fleet to cement your authority over PACT?"
        fon "They are no longer comrades to the revolution, but merely your brain washed puppets."
        fon "Our revolution is against tyrants of all colors! Even those who purport to fly our crimson flag."
        fon "This is your end, Prototype. You were a fool to believe the revolution could be wielded for your purposes."
        fon "The galaxy will not miss you."
        
        hide fontana onlayer screens
        hide alice_mask onlayer screens
        hide bg pactbridge onlayer screens
        show bg bridge onlayer screens
        with dissolve
        
        $dshow("ava handonhip smile narrow angry",layer="screens")
        
        ava "Our plan is working, captain!"
        ava "The second fleet is holding position behind the moon!"
        ava "The Prototype's fleet is suffering huge losses!"
        "Shields held up his fist."
        "Confidence swelled up within him."
        kay "(We can do this!)"
        kay "(Cera's right there, in front of us!)"
        
        $dshow("ava armscrossed neutral narrow angry",layer="screens")
        
        ava "...Wait a minute..."
        
        $dshow("ava armscrossed shout narrow angry",layer="screens")
        
        ava "Hold that last report!"
        kay "What happened!?"
        ava "I'm... getting strange reports from the second fleet...!!"
        
        play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
        $ PlayerTurnMusic = "Music/Posthumus_Regnum.ogg"
        
        hide ava onlayer screens
        hide bg bridge onlayer screens
        show bg pactbridge onlayer screens
        show alice_mask onlayer screens:
            xpos 0.25
        show fontana onlayer screens:
            xpos 0.75
        with dissolve
        
        ali "Hahaha...."
        ali "Haaahh!!! Hahahaahahaha!!!!"
        ali "Fool! Did you think that I would leave you with the second fleet with no back up plan?"
        fon "What!?"
        ali "Activate the chain neural override!"
        
        hide alice_mask onlayer screens
        hide fontana onlayer screens
        hide bg pactbridge onlayer screens
        show chigara_cockpit onlayer screens
        with dissolve
        
        ##Space
        chi "A-Ah! Captain!!!"
        chi "This is..."
        
        hide chigara_cockpit onlayer screens
        show bg bridge onlayer screens
        with dissolve
        
        $dshow("ava armscrossed shout narrow angry",layer="screens")
        
        kay "Report!"
        ava "I-impossible! The second fleet has just powered their engines!"
        ava "It is on an intercept course for the Alliance fleet!"
        kay "Damn!"
        
        $dshow("ava armscrossed shout narrow angry",xpos=0.25,layer="screens")
        
        pause 0.2
        
        show fontana onlayer screens:
            xpos 0.75
        with wipeup
        
        fon "Tsch... We've been had."
        fon "Our ships are not responding to our commands!"
        fon "The prototypes must have embedded a trojan deep within our systems to assume direct control of our ships!"
        chi "Captain!"
        kay "Do you know what's going on?"
        
        hide bg bridge onlayer screens
        hide ava onlayer screens
        hide fontana onlayer screens
        show chigara_cockpit onlayer screens
        with dissolve
        
        chi "Y-yes! I'm detecting an enormous amount of power being channeled through the prototypes' ryders!"
        chi "The prototypes seem to be directly controlling the second fleet's systems through their telepathy!"
        kay "They had one last trick up their sleeve, huh..."
        kay "How can we undo their control over the ships?"
        chi "They seem to have wired the ships to respond to their neural waves!"
        chi "I will enter the prototype's neural link and attempt to interfere with their thoughts!"
        chi "Perhaps I'll be able to find a weakness in the system while directly connected with them!"
        ica "Y-you're essentially going to mind meld with them!?"
        ica "C-captain, that sounds like every flavor of crazy!"
        chi "It's the only way!"
        kay "... ... ..."
        kay "All right. We'll just have to trust Chigara."
        kay "All units are to provide the Liberty with cover fire while Chigara restores the second fleet's controls!"
        "Everyone" "Understood!"
        kay "Chigara... Stay safe!"
        chi "Yes, captain!"
        
        hide chigara_cockpit onlayer screens with dissolve
        
        play sound "sound/objectives.ogg"
        "Objective: Cast the Liberty's DISRUPT ability six times. The Liberty cannot be lost!"
        
        python:
                        
            create_ship(PactAssaultCarrier(),(13,2))
            create_ship(PactAssaultCarrier(),(13,3))
            create_ship(PactAssaultCarrier(),(13,15))
            create_ship(PactAssaultCarrier(),(13,16))
            
            create_ship(PactElite(),(12,3))
            create_ship(PactElite(),(12,4))
            create_ship(PactElite(),(12,14))
            create_ship(PactElite(),(12,15))
            
            create_ship(PactFastCruiser(),(14,15))
            create_ship(PactFastCruiser(),(14,16))
            create_ship(PactFastCruiser(),(13,4))
            create_ship(PactFastCruiser(),(14,3))
            create_ship(PactFastCruiser(),(14,2))
            
            create_ship(PactSupport(),(15,6))
            create_ship(PactSupport(),(17,9))
            create_ship(PactSupport(),(15,12))

            liberty.register_weapon(Disrupt())
            liberty.destroy = BM.you_lose

        $ BM.draggable = True

    if not bcheck2 and BM.turn_count == 4:
        
        $ bcheck2 = True
        $ BM.draggable = False
        $ EnemyTurnMusic = "Music/Fallen_Angel_Pt3.ogg"  
        
        show lynn_cockpit_space1 onlayer screens with dissolve
        
        pro "Hahaha!!"
        pro "This is the end for you!"
        
        hide lynn_cockpit_space1 onlayer screens
        show asagacockpit onlayer screens
        with dissolve
        
        asa "Eeeaah!!!"
        asa "Not yet! We're going to stop your little trick and win!"
        
        hide asagacockpit onlayer screens
        show lynn_cockpit_space1 onlayer screens
        with dissolve
        
        pro "Oh?"
        pro "And how do you intend to do that?"
        
        hide lynn_cockpit_space1 onlayer screens
        show asagacockpit3 onlayer screens
        with dissolve
        
        asa "C-Chigara will---"
        asa "Will......"
        asa "... ... ..."
        pro "Hahahahaha!!!!"
        pro "Haaahahahahaha!!!"
        pro "She is one of us."
        
        show lynn_cockpit_space1 onlayer screens
        hide asagacockpit3 onlayer screens
        with dissolve
        
        pro "Oh, how unfortunate it is for your captain..."
        pro "That is she currently in our thoughts, exposing to us the full details of the Alliance's battle plans!"
        pro "Did you honestly think that we would allow ourselves to be defeated so easily?"
        pro "That the betrayal of mere humans will affect our strength?"
        pro "PACT... Alliance... Neutral Rim... It does not matter. In due time, all of it shall be destroyed all the same."
        pro "It will be here, over the skies of Cera, that the Alliance is defeated, and the Sunrider finally falls!"
        pro "It was enjoyable watching you squirm as we took away everything you ever loved."
        pro "Heh-heh..."
        pro "I think I'll let you live. Just so you can helplessly watch us destroy everything you've ever held dear."
        
        hide lynn_cockpit_space1 onlayer screens
        show asagacockpit4 onlayer screens
        with dissolve

        play sound "sound/heartbeat.ogg"
        
        show asagacockpit4b onlayer screens:
            xalign 0.5 yalign 0.5
            ease 0.5 alpha 0 zoom 2.0
        
        asa "Don't.... Bullshit... ME!!!!"
        asa "Evil doer."
        asa "Perish."
        asa "You shall not harm the Sunrider."
        
        hide asagacockpit4 onlayer screens
        show bg bridge onlayer screens
        with dissolve
        
        $dshow("ava handonhip shout narrow angry",layer="screens")
        
        ava "T-the Black Jack has just cut its channel with us!"
        kay "What!? Asaga, what's wrong?"
        asa "... ... ..."
        asa "I'm sorry captain..."
        asa "But you're being tricked..."
        
        hide ava onlayer screens
        hide bg bridge onlayer screens
        show asagacockpit4 onlayer screens
        with dissolve
        
        asa "I'm... doing this for the good of the ship...!!!"
        asa "Chigara.... is the traitor!!!!"
        ava "The Black Jack is on a intercept course for the Liberty!"
        kay "ASAGA!!!!"
        asa "Captain..."
        asa "I've... always loved you!"
        asa "I'M GOING TO PROTECT YOU!!!!!!!!!"
        
        hide asagacockpit4 onlayer screens with dissolve
        
        python:
            blackjack.AI_ignores = False
            if blackjack in player_ships:
                player_ships.remove(blackjack)
                set_cell_available(blackjack.location)
                blackjack.location = None
                blackjack.buffs = [] #shoutouts to byakuryuu
            create_ship(EnemyBlackjack(),(13,11))
            enemy_ships[-1].brain.preferred_target = liberty
            times_bj_killed = 0
            
            create_ship(PactAssaultCarrier(),(17,4))
            create_ship(PactAssaultCarrier(),(17,5))

            create_ship(PactFastCruiser(),(16,4))
            create_ship(PactFastCruiser(),(16,5))
            create_ship(PactFastCruiser(),(16,6))
        
        $ BM.draggable = True
        
    if get_shipcount_in_list('Enemy Black Jack',enemy_ships) == 0 and BM.turn_count > 4:
        
        play sound "sound/mech_boost1.ogg"
        
        python:
            times_bj_killed += 1
            create_ship(EnemyBlackjack(),(18,11))
            enemy_ships[-1].brain.preferred_target = liberty
            if times_bj_killed >= 7: #anti-farming hack
                enemy_ships[-1].money_reward = 0

    if not bcheck4 and BM.turn_count == 6:
        
        $ bcheck4 = True
        $ BM.draggable = False        
            
        play voice "sound/Voice/ava_Others_02.ogg"
            
        ava "Incoming more enemies!"
            
        python:
                        
            create_ship(PactAssaultCarrier(),(17,6))
            create_ship(PactAssaultCarrier(),(17,7))
            create_ship(PactAssaultCarrier(),(17,8))
            create_ship(PactAssaultCarrier(),(17,9))
            
            create_ship(PactFastCruiser(),(16,4))
            create_ship(PactFastCruiser(),(16,5))
            create_ship(PactFastCruiser(),(16,6))
            
            create_ship(Arcadius(),(11,15))
            create_ship(Arcadius(),(11,16))
            create_ship(Arcadius(),(10,4))
            create_ship(Arcadius(),(11,3))
            create_ship(Arcadius(),(11,2))
            
        $ BM.draggable = True
        
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission7 #loop back
    else:
        pass #continue down to the next label
    
label after_mission7:
    
    python:

        del liberty.destroy
                
    $ BM.win_when_alone = True
    hide screen battle_screen
    hide screen commands
    
    $ mission7_complete = True
    $ VNmode()
    
    play music "Music/MarduksWrath.ogg"
    
    show screen leftbuttons
    
    scene bg bridge with dissolve
    
    window show
    
    $dshow("ava handonhip shout narrow angry")
    
    ava "How much longer until the second fleet's systems are restored!?"
    chi "A-almost... done..."
    
    scene icaricockpit with dissolve
    
    ica "Asaga's gone berserk!!!"
    ica "O-oy, captain!? W-what are we supposed to do!?"
    ica "A-are we actually gonna shoot her down!?"
    kay "... ... ..."
    
    scene kryska_cockpit1 with dissolve
    
    kry "Captain!! Your orders!"
    kay "(...At this rate...)"
    kay "(Asaga's really is going to kill Chigara...!)"
    kay "(Do I give the kill order?)"
    
    scene solacockpit1 with dissolve
    
    sol "Captain. I have a lock on the Black Jack's cockpit."
    sol "I shall take full responsibility."
    kay "... ... ..."
    
    scene asagacockpit4 with dissolve
    
    asa "Watch me, captain!!!"
    asa "Soon... You're going to realize I was right!!!!"
    asa "EEAAAHHH!!!"
    
    play sound "sound/boasters.ogg"
    scene blackjack_attack with dissolve
    
    ica "S-she's coming in fast!!!"
    ica "F-faster than even me!!!!"
    sol "I can only maintain a lock for four more seconds..."
    sol "Two..."
    kay "T-tsch......."
    kay "Pull the t-"
    
    scene bjbiancastop_back with dissolve
    show bjbiancastop_bianca:
        xpos 1.0
        ease 0.5 xpos -0.4
    
    play sound "sound/chargeup.ogg"
    
    cla "Hooaaahh!!!"
    asa "E-eaaahh!!!!"
    
    play sound1 "sound/explosion1.ogg"
    scene white with dissolve
    
    kay "W-what the--"
    kay "C-Claude!? A-Are you all right!?"
    
    scene claudecockpit2 with dissolve
    
    cla "U-ugh... Y-yes, captain..."
    
    scene bianca_damaged1 with dissolve
    
    cla "N-not so sure 'bout the Bianca though..."
    asa "W-what are you doing!?"
    
    play music "Music/Love_Theme.ogg" fadeout 1.5
    
    scene claudecockpit3 with dissolve
    
    cla "Now you listen to me... And listen to me good..."
    cla "There isn't a girl on board the Sunrider who likes how things turned out...!"
    cla "Especially me! Who's loved the captain more than any of you!"
    cla "J-just how do you think poor Claude feels...? Completely forgotten by everyone!"
    cla "I can't even open my mouth without everyone turning away now!"
    cla "Useless old Claude, good for nothing but her boobs and... comic relief!!"
    cla "But we've all been through too much to turn on each other!"
    cla "We're... family, Asaga!!"
    cla "Even though we get mad at each other... And make mistakes..."
    cla "And get jealous when she's with him..."
    cla "We can't betray each other!"
    cla "Nobody on the Sunrider is a traitor! Nobody!"
    
    scene asagacockpit5 with dissolve
    
    asa "... ... ..."
    asa "T-tsch...."
    asa "W-why..."
    asa "I'm... the hero... And yet why...."
    asa "Why does he never look my way..."
    
    scene claudecockpit4 with dissolve
    
    cla "Teeheehee..."
    cla "It's... not the end."
    cla "There's still--"
    
    $renpy.music.set_volume(0.0, delay=0.5, channel="music")
    
    scene bianca_damaged1 with dissolve
    play sound "sound/legion_laser.ogg"
    scene bianca_damaged2 with horizontalwipe
    
    cla "H-heh--?"
    
    scene claudecockpit1 with dissolve
    
    cla "O-oh dear... It l-looks like..."
    cla "I've stopped paying attention-"
    
    $renpy.music.set_volume(0.27, delay=0.5, channel="music")
    $player_ships.remove(bianca)
    $player_ships.append(blackjack)
    if blackjack not in BM.ships:
        $BM.ships.append(blackjack)    
    $blackjack.set_location(1,1)
    scene white with dissolvemedium
    play sound "sound/explosion4.ogg"
        
    asa "E-eh?"
    
    scene icaricockpit2 with dissolve
    
    ica "E-EEAAHHH!!!"
    kry "CLAAUUUDEEE!!!!!!!!!"
    
    scene lynn_cockpit_space2 with dissolve
    
    pro "Hahaha..."
    pro "Fool..."
    pro "D-delivering long speeches in the middle of battle..."
    pro "Surely she had a deathwish..."
    asa "YOU BASTARD!!!!"
    asa "AAAHHHHHHH!!!!"
    
    scene icaricockpit2 with dissolve
    
    ica "S-SHIT!!! CLAUDE!!!"
    ica "S-she was too stupid to die, goddamnit!!!!"
    ica "That... IDIOT!!!"
    ica "T-trying to act all cool!!!"
    ica "PROTOTYPE!!!!!"
    kry "EAAHHH!!!"
    
    scene bg bridge with dissolve
    
    kay "Tsch..."
    kay "Shit!"
    kay "Claude..."
    kay "All units! Form up around the Liberty!"
    kay "Don't let anyone else die!!! IS THAT UNDERSTOOD!?"
    
    scene asagacockpit6 with dissolve
    
    asa "C-captain I---"
    kay "Protect her."
    asa "... ... ..."
    asa "Understood... captain!"
    
    scene white with dissolvemedium
    
    play music "Music/Fallen_Angel_Pt2.ogg" fadeout 1.5
    
    scene chigaramindstream:
        xanchor 0.5 yanchor 0.5 xpos 0.4 ypos 0.9 zoom 1.45
    with dissolvemedium
    
    chi "(Their voices... I can hear them...)"
    chi "(My friends are in trouble! They need my help...!)"
    chi "Everyone..."
    
    if CENSOR == True:
    
        scene chigaramindstream:
            xanchor 0.5 yanchor 0.5 xpos 0.4 ypos 0.9 zoom 1.45 subpixel True
            ease 20 zoom 0.5 xpos 0.5 ypos 0.5
            
    if CENSOR == False:
        
        scene h_chigaramindstream:
            xanchor 0.5 yanchor 0.5 xpos 0.4 ypos 0.9 zoom 1.45 subpixel True
            ease 20 zoom 0.5 xpos 0.5 ypos 0.5
    
    pro "My sister..."
    pro "Return to us. As you were meant to."
    chi "No..."
    chi "(Just a little bit more... And I can...)"
    pro "You are a prototype, just like us."
    pro "You have no purpose but your mission."
    chi "That's not true!"
    chi "I have things I want to protect now!"
    chi "I'm not like you!"
    pro "You were sent by us from the beginning."
    pro "To keep a watchful eye over the one who would one day awaken to her destiny."
    pro "And by fortune, your path crossed with Shields, the would be savior of the galaxy."
    pro "We allowed you free reign in your interactions with him so we may learn his machinations."
    pro "The insight you have brought us was... astounding."
    pro "To think we could acclimate to human company so well..."
    
    scene chigaramindstream2 with dissolve
    
    chi "All lies!"
    chi "I'm... Chigara Ashada!"
    chi "I was born on Diode by my parents!"
    chi "I'm not a clone like you! I'm human!"
    
    scene chigaramindstream3 with dissolve
    
    alp "Human?"
    chi "(She's... different from the others...)"
    chi "(Is she their leader?)"
    alp "Yes..."
    alp "You and 4L have experienced the emotion they call love..."
    alp "It fills you with warmth and strength."
    alp "And yet, for 4L, it consumes her. Twists her body."
    alp "Ravages her."
    
    scene bg pactbridge
    show alice_mask
    with dissolve
    
    ali "Tsch..."
    
    scene bg clonelab
    show prototype_alpha
    with dissolve
    
    alp "Soon, what you have experienced will spread to all our sisters."
    alp "We will change."
    alp "I can only speculate what the future may hold for our kind..."
    alp "We thank you, Prototype C8."
    alp "The information you have brought us will aid us immensely."
    alp "But your mission has now been accomplished."
    alp "4L, return her to us."
    alp "We shall extract her brain and mine it for what we can uncover."
    alp "Kill the rest of them."
    alp "Once those who resist us are dead, the galaxy will have no choice but to accept our rule."
    
    scene bg pactbridge
    show alice_mask
    with dissolve
    
    ali "It's over for you, humans!"
    
    scene chigaramindstream3 with dissolve

    chi "(A-ah!)"
    chi "(I did it!)"
    
    play music "Music/The_Final_Battle.ogg" fadeout 1.5
    
    chi "Whoever you are, you won't have your way!"
    chi "We'll fight you!"
    alp "Oh?"
    chi "Love isn't so weak that it can be controlled by the likes of you!"
    chi "Because... as long as we trust our allies, we're invincible!"
    chi "Love may confuse us... Blind us... Even make us angry and jealous..."
    chi "But I'll defend it!"
    chi "I'll defend everyone!"
    chi "I'm Chigara Ashada... And I'm a human!!!"
    
    scene white with dissolve
    
    ali "S-shit!"
    
    scene bg bridge with dissolve
    $dshow("ava handonhip shout narrow angry")

    ava "Captain, the second fleet has ceased their attack!"
    kay "Did she do it!?"
    chi "A-ah... Captain..."
    chi "I've done it... Chigara's back..."
    "Shields leaped to his feet."
    kay "Yes!"
    kay "Tell all the Alliance vessels to cease fire on the second fleet and advance towards the first!"
    kay "Wipe out the prototypes' final defensive line!"
    
    $dshow("ava salute shout narrow angry")
    
    ava "Aye aye, captain!"
    
    $dshow("ava salute shout narrow angry",xpos=0.25)
    show fontana:
        xpos 0.75
    with wipeup
    
    fon "Our ships are once again under our control."
    fon "Hmph. You have my thanks, captain."
    kay "I never imagined I'd be glad to hear you say that..."
    fon "Beh. Looks like we've got no choice now."
    fon "All ships, join the Alliance fleet and assist with the attack on the prototypes' final defensive line!"
    fon "I will not have it be said that on the decisive battle, Veniczar Fontana stood idly by while the Alliance fleet took all the glory!"
    fon "All ships, forward! Open fire!"
    kay "This is it, everyone..."
    kay "Attack!!!"
    
    
    
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission8"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label_6
    
    pause
    
label pre_mission8:

    call mission8_inits from _call_mission8_inits
    $ BM.mission = 8
    $ store.noforward = False
    $ BM.win_when_alone = True
    $ BM.draggable = True
    $ blackjack.AI_ignores = False
    $ liberty.remove_buff("Disruption")
    $ blackjack.buffs =[]
    $ liberty.remove_weapon("Disrupt")
    $ blackjack.remove_weapon("Awaken Asaga")

    call bcheckset from _call_bcheckset_7

    pause 1.0
    scene space back6 with battlewipe
    $BM.battle_bg = "Background/space6.jpg"
    
    jump battle_start
    
label mission8:
    
    if not bcheck1:
        $ bcheck1 = True
        
        $renpy.music.set_volume(0.7, delay=0.5, channel="music")
        play music "Music/Sora_no_Kodoh.ogg"
        
        python:
            alliancecarrier1 = create_ship(AllianceCarrier(),(5,4))
            allianceinfantry1 = create_ship(AllianceInfantry(),(6,3))
            allianceinfantry2 = create_ship(AllianceInfantry(),(6,5))
            alliancebattleship1 = create_ship(AllianceBattleship(),(5,3))
            alliancebattleship2 = create_ship(AllianceBattleship(),(5,5))
            
            pactassaultcarrier1 = create_ship(FriendlyPactAssaultCarrier(),(5,14))
            pactelite1 = create_ship(FriendlyPactElite(),(6,13))
            pactelite2 = create_ship(FriendlyPactElite(),(6,15))
            pactfastcruiser1 = create_ship(FriendlyPactFastCruiser(),(5,13))
            pactfastcruiser2 = create_ship(FriendlyPactFastCruiser(),(5,15))
            pactsupport1 = create_ship(FriendlyPactSupport(),(4,14))
                            
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission8 #loop back
    else:
        pass #continue down to the next label

    
label after_mission8:
    
    $renpy.music.set_volume(0.27, delay=0.5, channel="music")
    python:
        if hasattr(store,'alliancecarrier1'):
            if alliancecarrier1 in BM.ships:
                BM.ships.remove(alliancecarrier1)
                player_ships.remove(alliancecarrier1)
        if hasattr(store,'allianceinfantry1'):
            if allianceinfantry1 in BM.ships:
                BM.ships.remove(allianceinfantry1)
                player_ships.remove(allianceinfantry1)
        if hasattr(store,'allianceinfantry2'):
            if allianceinfantry2 in BM.ships:
                BM.ships.remove(allianceinfantry2)
                player_ships.remove(allianceinfantry2)
        if hasattr(store,'alliancebattleship1'):
            if alliancebattleship1 in BM.ships:
                BM.ships.remove(alliancebattleship1)
                player_ships.remove(alliancebattleship1)
        if hasattr(store,'alliancebattleship2'):
            if alliancebattleship2 in BM.ships:
                BM.ships.remove(alliancebattleship2)
                player_ships.remove(alliancebattleship2)
        if hasattr(store,'pactassaultcarrier1'):
            if pactassaultcarrier1 in BM.ships:
                BM.ships.remove(pactassaultcarrier1)
                player_ships.remove(pactassaultcarrier1)
        if hasattr(store,'alliancecarrier1'):
            if alliancecarrier1 in BM.ships:
                BM.ships.remove(alliancecarrier1)
                player_ships.remove(alliancecarrier1)
        if hasattr(store,'pactelite1'):
            if pactelite1 in BM.ships:
                BM.ships.remove(pactelite1)
                player_ships.remove(pactelite1)
        if hasattr(store,'pactelite2'):
            if pactelite2 in BM.ships:
                BM.ships.remove(pactelite2)
                player_ships.remove(pactelite2)
        if hasattr(store,'pactfastcruiser1'):
            if pactfastcruiser1 in BM.ships:
                BM.ships.remove(pactfastcruiser1)
                player_ships.remove(pactfastcruiser1)
        if hasattr(store,'pactfastcruiser2'):
            if pactfastcruiser2 in BM.ships:
                BM.ships.remove(pactfastcruiser2)
                player_ships.remove(pactfastcruiser2)
        if hasattr(store,'pactsupport1'):
            if pactsupport1 in BM.ships:
                BM.ships.remove(pactsupport1)
                player_ships.remove(pactsupport1)
    
    hide screen battle_screen
    hide screen commands
    
    play music "Music/Sora_no_Kodoh.ogg"
    
    $ mission8_complete = True
    $ VNmode()
    
    show screen leftbuttons
    
    window show
    
    scene bg bridge with dissolve
    $dshow("ava handonhip shout narrow angry")

    ava "Our combined forces have gained the advantage! We are pushing through the enemy's lines!"
    kay "This is it everyone! Throw everything we have against the prototypes and obliterate them!"
    
    $dshow("ava handonhip shout narrow angry",xpos=0.25)
    show fontana:
        xpos 0.75
    with wipeup
    
    fon "Hmph. To think I would fight side by side with the likes of you..."
    kay "Heh... I never once imagined that I would be glad to hear you say that."
    
    stop music fadeout 1.5
    
    ava "Cut the celebration. Incoming new bogey!"
    
    play music "Music/Posthumus_Regnum.ogg"
    scene nightmare_approach with dissolve
    
    ava "A new ryder! A type we've never seen before!"
    kay "That can only mean one thing..."
    
    scene alice_cockpit1 with dissolve
    
    ali "To think that I would actually have to use this again..."
    ali "It's been so many years..."
    ali "This is where your advance stops, human."
    
    scene nightmare_approach with dissolve
    
    kay "So you're the leader of all this."
    kay "Surrender, Prototype. I've gathered an allied fleet of more Alliance and PACT ships than the very stars to liberate this world."
    kay "And I'm not about to let a single ryder stand in my way."
    
    scene alice_cockpit1 with dissolve
    
    ali "Heheheh... You're confident, just as the Imperials were."
    ali "But you have not yet witnessed the full might of the Nightmare Ascendant!"
    
    scene nightmare_attack
    
    $ renpy.movie_cutscene("3DCG/nightmareattack.webm",stop_music=False) 
    pause
    
    play sound "sound/explosion2.ogg"
    
    scene alliancefleet_damaged:
        xalign 0.0
        ease 2.0 xalign 0.5
    with dissolve
    
    ava "Captain! T-that ryder's singlehandedly gutting the entire fleet!"
    ava "I-it matches no known ryder configuration in our database! It's completely beyond anything we've ever encountered!"
    kay "W-what, it's probably just a Ryuvian relic that Prototype dug up somewhere! Blast it with enough lead and it'll go down just like anything else!"
    chi "T-that may not be the case, captain!"
    chi "According to these readings, our ryders are essentially birds fighting a battleship class star ship!"
    
    scene solacockpit3 with dissolve
    
    sol "A-ah...!"
    sol "Dark day... It is the Myr'lan'dur."
    kay "You know something, Sola?"
    sol "A dark ryder, feared even amongst the ancient Ryuvians..."
    sol "It was the personal ryder of Sharr Myren, who vanished without a trace four hundred years before my birth."
    sol "To find such a grim omen here..."
    kay "How do we take it down?"
    sol "Such a task would be difficult, even for the war machines of my era..."
    sol "Retreat may be unavoidable..."
    kay "(Tsch... We're so close...!)"
    kay "We can't give up now! All ships, target the Nightmare Ascendant!"
    
    scene alice_cockpit1 with dissolve
    
    ali "Hahahaha! Pathethic!"
    ali "Your biggest weapons mean nothing to the Nightmare Ascendant!"
    kay "Tsch..."
    kay "Well, let's find out."
    kay "Fire the Vanguard!"
    
    scene white
    
    $ renpy.movie_cutscene("3DCG/vanguardcut.webm",stop_music=False)    
    pause
    
    scene nightmare_approach with dissolve
    
    play sound "sound/explosion4.ogg"
    
    scene white with dissolve
    
    ava "Direct hit confirmed!"
    kay "Did we get it?"
    
    scene nightmare_approach with dissolve
    
    ali "HAHAHAHA!!!!"
    
    scene bg bridge with dissolve
    $reset_sprites()
    $dshow("ava armscrossed shout narrow angry")
    
    ava "Negative captain! The attack was completely ineffective!"
    
    scene alice_cockpit2 with dissolve
    
    ali "Now you see, captain?"
    ali "Everything you accomplished here was meaningless."
    ali "You were always at my mercy."
    ali "Did you once fear the Legion? The Paradox Core? My useless clones?"
    ali "Mere toys. Diversions. Cannon fodder."
    ali "All the ships of PACT are disposable. For the Nightmare alone can rule the galaxy."
    ali "Now suffer as victory is snatched away, just when it appears in reach."
    ali "Watch in horror as everything you built up burns!"
    ali "Hahahahahahaha!!!"
    kay "Tsch...!"
    kay "(That ryder breaks all the rules of engagement!)"
    kay "(There's nothing on the field which can counter it!)"
    
    scene bg bridge with dissolve
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "Captain."
    kay "Ava?"
    ava "That ryder is proving quite problematic."
    ava "How say we fire every shell, laser, and missile at it and see how it fares against the full might of humanity's wrath."
    kay "... ... ..."
    
    scene solacockpit4 with dissolve
    
    sol "Legend speaks that the Myr'lan'dur single handedly destroyed a Farari fleet a thousand strong."
    sol "Yet, I have never heard that it bested two Sharrs in combat."
    kay "Sola..."
    
    scene kryska_cockpit2 with dissolve
    
    kry "Hah! Ancient Ryuvian relics are no match against the might of the entire Solar Alliance!"
    kry "All our ships are already here! This is the best time to show the galaxy that freedom will win over the tools of long dead tyrants any day!"
    
    scene bg bridge with dissolve
    
    $dshow("ava armscrossed neutral narrow angry",xpos=0.75)
    show fontana:
        xpos 0.25
    with wipeup
    
    fon "Hmph. I feared the Nightmare would make its appearance eventually..."
    kay "You knew about this, Fontana!?"
    fon "The full capabilities of that devilish thing will never be known."
    fon "But it is not a god. It was made by the hands of man, and it can be fallen by the same."
    kay "Damnit Fontana... You could have at least warned us!"
    
    scene asagacockpit6 with dissolve
    
    asa "... ... ..."
    asa "I'm... gonna do it!"
    kay "Asaga?"
    asa "I don't care if it's invincible or not..."
    asa "All this time, I was stupid!"
    asa "But not any more! This time, I'm really going to save everyone!"
    asa "I don't care about being a Sharr or Queen, or anything like that...!"
    asa "'Cause... That's not what I wanted at all!"
    asa "This time... this time, I'm finally going to be the hero!!!!"
    asa "I won't let the darkness control me!!"
    
    play sound "sound/heartbeat.ogg"
    
    scene asagacockpit7 with dissolve
    show asagacockpit7b:
        xalign 0.5 yalign 0.5
        ease 0.5 zoom 2.0 alpha 0
    
    asa "Hiiyaaah!!!!"
    sol "A-ah..."
    
    scene solacockpit4 with dissolve
    
    sol "S-such light..."
    
    play sound "sound/heartbeat.ogg"
    
    scene solacockpit5
    show solacockpit5b:
        xalign 0.5 yalign 0.5
        ease 0.5 zoom 2.0 alpha 0
    
    sol "I too shall follow your example."
    
    scene bg bridge with dissolve
    $dshow("ava armscrossed neutral narrow angry",xpos=0.8)
    show fontana:
        xpos 0.5
    show grey behind fontana:
        xpos 0.2
    with wipeup
    
    adr "Are you ready, captain?"
    kay "Sunrider, standing by."
    fon "A single ryder, against all of us?"
    adr "If we lose here, against just one ryder, my offspring will become laughstocks for the next ten generations."
    adr "All ships!"
    adr "Move her out of the way."
    
    window hide
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    $ pre_mission = "pre_mission9"
    $ store.noforward = True
    
    call battlewarning_label from _call_battlewarning_label_7
    
    pause
    
label pre_mission9:

    call mission9_inits from _call_mission9_inits
    $ BM.mission = 9
    $ store.noforward = False
    $ BM.draggable = True

    call bcheckset from _call_bcheckset_8

    pause 1.0
    scene space back7 with battlewipe
    $BM.battle_bg = "Background/space7.jpg"
    
    jump battle_start

label mission9:
    
    if not bcheck1:
        
        $ bcheck1 = True
        $ BM.draggable = False        
        play sound "sound/objectives.ogg"
        
        "OBJECTIVE: Defeat the NIGHTMARE ASCENDANT."
        
        $ BM.draggable = True    
        
        python:
            pactassaultcarrier2 = create_ship(FriendlyPactAssaultCarrier(),(8,12))
            pactfastcruiser1 = create_ship(FriendlyPactFastCruiser(),(9,7))
            pactfastcruiser2 = create_ship(FriendlyPactFastCruiser(),(9,11))
            pactsupport1 = create_ship(FriendlyPactSupport(),(4,10))
        
            blackjack.register_weapon(AwakenAsaga())
            BM.selected = blackjack
            blackjack.weapons[-1].fire(blackjack,blackjack,hidden=True)
            blackjack.en += 100
            blackjack.hp += 100
            
            seraphim.set_buff(AwakenedSeraphim)
        
    if nightmare_ascendant.hp <= 25000 and not bcheck2:
        
        $ bcheck2 = True
        hide screen commands
        
        $ BM.draggable = False        
    
        show nightmare_damaged onlayer screens:
            zoom 0.65
        with dissolve
        
        ali "A-argh!"
        ali "Tsch!"
        ava "Captain! Look!"

        show nightmare_damaged onlayer screens:
            zoom 0.65
            ease 2.0 zoom 0.9 xpos -0.3
        
        ava "Minor damage, detected on the Nightmare Ascendant's outer frame!"
        kay "So it can be hurt."
        kay "Keep it up, everyone."
        
        hide nightmare_damaged onlayer screens
        show alice_cockpit2 onlayer screens
        with dissolve
        
        ali "Hah! You think you've won?"
        ali "Hahahaha......"
        
        hide alice_cockpit2 onlayer screens
        
        play sound "sound/heartbeat.ogg"
        
        show alice_cockpit3 onlayer screens
        show alice_cockpit3b onlayer screens:
            xalign 0.5 yalign 0.5
            easeout 0.25 zoom 1.5 alpha 0
        with dissolve
        
        ali "HAAAHAHAAHAHAHA!!!!!"
        ali "This was but a prelude! Now the show begins!"
        sol "I-impossible!"
        asa "H-how!?"
        ali "Hahahaha..."
        ali "I too can awaken."
        
        hide alice_cockpit3 onlayer screens
        show solacockpit5 onlayer screens
        with dissolve
        
        sol "N-no! Such technology was lost..."
        sol "To think a vile monster such as you could wield the power of Sharrs..."
        sol "...Repulsive."
        
        hide solacockpit5 onlayer screens
        show asagacockpit7 onlayer screens
        with dissolve
        
        asa "You've got that right! But it's still two Sharrs against one!"
        asa "Let's beat the crap outta her! There's not enough room in the galaxy for three of us!"
        
        hide asagacockpit7 onlayer screens
        show alice_cockpit3 onlayer screens
        with dissolve
        
        ali "Hahaha... Low lifes!"
        ali "All units, engage! This is where the fate of humanity will be sealed!"
        ali "ATTACK!"
        
        python:
            
            nightmare_ascendant.weapons = [BossRocket(),BossLaser(),BossMelee()]
            nightmare_ascendant.brain = BossAI(nightmare_ascendant)
            
            create_ship(PactProtoCarrier(),(17,6))
            create_ship(PactProtoCarrier(),(17,7))

            create_ship(PactBattleship(),(17,10))
            create_ship(PactSupport(),(17,11))
            create_ship(PactBattleship(),(9,1))
            create_ship(PactCruiser(),(8,2))
            create_ship(PactCruiser(),(9,3))
            create_ship(PactCruiser(),(10,3))
            create_ship(Arcadius(),(10,2))
            create_ship(Arcadius(),(10,3))
            
            create_ship(PactBattleship(),(9,17))
            create_ship(PactCruiser(),(8,17))
            create_ship(PactCruiser(),(9,16))
            create_ship(PactCruiser(),(10,16))
            create_ship(Arcadius(),(10,16))
            create_ship(Arcadius(),(10,17))
            
            create_ship(PactDestroyer(),(14,4))
            create_ship(PactDestroyer(),(14,16))
            
            
        $ BM.draggable = True
        show screen commands
    
        hide alice_cockpit3 onlayer screens with dissolve

    if not bcheck4 and BM.turn_count == 5:
        
        $bcheck4 = True 
        
        play avavoice "sound/Voice/ava_Others_03.ogg"
        
        python:
                        
            create_ship(PactBattleship(),(15,2))
            create_ship(PactBattleship(),(16,3))
            create_ship(Arcadius(),(14,2))
            create_ship(Arcadius(),(14,3))
            create_ship(PactDestroyer(),(14,4))
            
            create_ship(PactBattleship(),(15,14))
            create_ship(PactBattleship(),(16,15))
            create_ship(Arcadius(),(14,14))
            create_ship(Arcadius(),(14,15))
            create_ship(PactDestroyer(),(14,16))
        
    if not bcheck5 and BM.turn_count == 10:

        $bcheck5 = True
        play avavoice "sound/Voice/ava_Others_04.ogg"
        
        python:
                        
            create_ship(PactProtoCarrier(),(15,4))
            create_ship(PactDestroyer(),(14,4))
            create_ship(PactSupport(),(14,2))
            
            create_ship(PactProtoCarrier(),(15,16))
            create_ship(PactDestroyer(),(14,16))
            create_ship(PactSupport(),(14,15))
        
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission9 #loop back
    else:
        pass #continue down to the next label

label after_mission9:
    
    python:
        
        if hasattr(store,'pactassaultcarrier2'):
            if pactassaultcarrier2 in BM.ships:
                BM.ships.remove(pactassaultcarrier2)
                player_ships.remove(pactassaultcarrier2)
        if hasattr(store,'pactfastcruiser1'):
            if pactfastcruiser1 in BM.ships:
                BM.ships.remove(pactfastcruiser1)
                player_ships.remove(pactfastcruiser1)
        if hasattr(store,'pactfastcruiser2'):
            if pactfastcruiser2 in BM.ships:
                BM.ships.remove(pactfastcruiser2)
                player_ships.remove(pactfastcruiser2)
        if hasattr(store,'pactsupport1'):
            if pactsupport1 in BM.ships:
                BM.ships.remove(pactsupport1)
                player_ships.remove(pactsupport1)

    hide screen battle_screen
    hide screen commands

    play music "Music/The_Final_Battle.ogg"
        
    window show
    
    scene asagacockpit7 with dissolve
    pause 2.0
    scene blackjack_attack with dissolve
    
    asa "Hiiyyaaah!!!!"
    
    scene alice_cockpit4 with dissolve
    
    ali "T-tsch!"
    
    scene nightmare_fire with dissolve
    
    play sound "sound/legion_laser.ogg"
    
    scene nightmare_fire2 with dissolve
    
    ali "Pathetic human!"
    
    scene blackjacknightmare
    show movie
    #play movie "3DCG/blackjacknightmare.webm" noloop
    $ renpy.movie_cutscene("3DCG/blackjacknightmare.webm",stop_music=False)
    
    chi "Asaga!"
    asa "T-thanks!"
    
    play sound "sound/Sword Shing 2.ogg"
    play sound1 "sound/chargeup.ogg"
    scene goodvevil with dissolve
    
    ali "You are a fool..."
    ali "C-Chigara is your enemy!"
    ali "S-she betrayed your friendship!"
    ali "Stole the man you love!"
    asa "To think I was so petty that I actually believed you before..."
    asa "And because of that..."
    asa "Claude's..."
    asa "No more, Prototype!!!!"
    asa "Something so little ain't worth letting you wreck the galaxy over!!!"
    
    play sound "sound/Sword Shing 2.ogg"
    scene white with dissolve
    
    asa "HHYYEEEAAAHHHHHHH!!!!"
    
    play sound "sound/explosion2.ogg"
    
    ali "U-ugh..."
    ali "I-imposs--"
    asa "Now, captain!"
    
    scene bg bridge with dissolve
    
    kay "All ships!"
    kay "OPEN FIRE!!!!!!!!!!!!!!!"
    
    scene bg pactbridge
    show fontana
    with horizontalwipe
    
    fon "... ... ..."
    fon "(You were once a comrade. But your madness must be put to an end.)"
    fon "(Farewell...)"
    fon "(Alice.)"
    
    scene allshipsfire1 with dissolve
    
    fon "Fire!!!"
    
    play sound "sound/legion_laser.ogg"
    play sound1 "sound/cannon.ogg"
    play sound2 "sound/railgun.ogg"
    scene allshipsfire2 with dissolve
    
    adr "Machiavellis! Load up all tubes and fire!"
    
    scene bg bridge with dissolve
    $dshow("ava handonhip smile narrow angry")
    
    ava "Captain, the Vanguard is charged and ready."
    ava "On your word."
    kay "... ... ..."
    kay "This is it..."
    kay "FIRE!!"
    
    scene white
    
    $ renpy.movie_cutscene("3DCG/vanguardcut.webm",stop_music=False)    
    pause
    
    play sound "sound/explosion2.ogg"
    play sound1 "sound/vanguard cannon laser.ogg"
    scene alice_cockpit5 with dissolve
    
    ali "EEEAAAAAAAAAAAAHHHHHHHHHHHHH!!!!!!"
    
    scene alice_cockpit6 with dissolve
    
    ali "HUUUUUMAAAANNNN FILLLTTTHHHHHH!!!!!!!!!!!!!!"
    
    play sound "sound/explosion4.ogg"
    scene white with dissolvemedium
    
    pause
    
    scene asagacockpit7 with dissolve
    
    asa "Good bye, Prototype..."
    asa "Your war's over!"
    
    stop music fadeout 1.5
    
    scene bg bridge with dissolve
    $dshow("ava handonhip shout narrow angry")
    
    ava "Hits confirmed!"
    ava "... ... ..."
    ava "The Nightmare Ascendant is confirmed neutralized!"
    ava "Its frame has been completely obliterated! Its pilot, presumably killed!"
    
    play music "Music/The_Bladed_Druid_Pt2.ogg" noloop
    queue music "Music/Colors_main.ogg"
    
    ava "The remaining enemy units are surrendering!"
    kay "Yes!"
    kay "Take their surrender, Ava!"
    ava "Aye, captain."
    kay "... ... ..."
    kay "(We did it...)"
    kay "(We won!)"
    
    scene kryska_cockpit2 with dissolve
    
    kry "Hiyah! Surrender, you cowards!"
    ica "W-we did it!!"
    kry "Hah hah hah!"
    kry "And so freedom prevails!"
    
    scene bg pactbridge 
    show fontana
    with dissolve
    
    fon "So the war is over..."
    fon "All hands, prepare to take on prisoners."
    fon "See to it that they are... educated as to the truth of the creature they believed to be Veniczar Arcadius."
    "The bridge crew saluted Fontana."
    "PACT Officer" "Sir!"
    fon "... ... ..."
    fon "Now, PACT shall find a new path."
    fon "We cannot hope to reform the galaxy if we are internally weak."
    fon "Our efforts shall turn inwards. The poor and weak within our borders will be tended to by the government."
    fon "No longer will we overlook the suffering of our people for reckless misadventures on foreign lands."
    fon "Today, the People's Alliance shall be reborn!"
    
    scene bg bridge with dissolve
    
    "The bridge crew applauded and surrounded Shields."
    kay "Hahaha... Everyone..."
    "Shields took turns shaking the hands of the crew."
    
    $dshow("ava handonhair smirk neutral neutral")
    
    ava "Heh..."
    ava "You did it, captain."
    "Ava saluted."
    
    $dshow("ava salute shout narrow angry")
    
    ava "Sir! It was my greatest pleasure to be your first mate on this journey!"
    ava "It was a long voyage. And at times, I felt overwhelmed."
    kay "We all did."
    kay "We were all tested."
    kay "But in the end, we prevailed."
    ava "Sir!"
    ava "What is your order, captain!"
    kay "Set course."
    kay "Cera."
    kay "Dock with our home port."
    kay "We're all going home."
    ava "Understood, captain! Helmsman, input new heading!"
    
    scene bg hangar with dissolve
    
    "The crew rushed to the pilots as the Sunrider's ryders returned."
    
    scene overhangar with dissolve
    
    chi "O-oh! E-everyone!"
    chi "Eh-heheh... We won!!"
    "Everyone" "CHIGARA!"
    chi "We won!"
    asa "... ... ..."
    chi "Asaga!"
    chi "I'm... relieved... You're all right..."
    asa "Chigara..."
    asa "I'm... sorry!"
    "Asaga bowed down."
    asa "I was... stupid...!"
    asa "I said all those things about you..."
    asa "But in the end, it was me who was being manipulated by the prototypes!"
    asa "Nothing I do will ever forgive me... But I just want you to know..."
    asa "Please... make him happy for me, okay?"
    chi "Of course!"
    "Chigara embraced Asaga."
    chi "You're... my friend, Asaga!"
    chi "No matter what happens, we'll always be friends!"
    asa "Chigara..."
    ica "Tsch... Seriously..."
    ica "All this cheer is making me sick..."
    ica "Ah, I'm gonna need a drink before the victory celebrations!"
    ica "I can't take how stupidly happy everyone else is! H-heh!"
    ica "I knew all along we'd beat those prototypes! C'mon, they weren't scary at all!"
    kry "Hah! You best wipe your tears of joy, mercenary!"
    ica "W-what!? I-I'm not crying!!!"
    ica "S-seriously... W-who the hell do I think I am...."
    ica "Cryin' over something so stooopiiddd..."
    ica "Hick..."
    ica "Huuuu....!!"
    ica "WAAHHH!!!"
    "Icari cried into Kryska's bosom."
    kry "Hah hah hah!"
    ica "Sniffle..."
    
    $ cal_location = None
    $ res_location = None
    
    $ pro_event = None
    $ pro_location = None
    
    $ asa_location = "messhall"
    $ asa_event = "asagawindows"
    
    $ captaindeck = 1
    scene black
    jump map_dispatch
    
label asagawindows:

    hide screen ship_map
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    
    scene black with dissolvemedium
    scene bg messhallwindows_cera with dissolvemedium
    $reset_sprites()
    
    $dshow("asaga armscrossed frown narrow sad")
    
    window show
    
    asa "... ... ..."
    "Shields saw Asaga waiting for him by the windows."
    kay "Quite a view."
    kay "I... was afraid I'd never see it again."
    asa "... ... ..."
    asa "I'm sorry."
    asa "I really messed up, didn't I?"
    kay "Well..."
    kay "It was the prototype who killed Claude. You can't blame yourself forever, Asaga."
    asa "No..."
    asa "It was all because I was fooled..."
    asa "In the end, I was the traitor."
    asa "And the worst part was that I wanted to be tricked. I wanted Chigara to be a spy, just so she'd disappear."
    
    $dshow("asaga armscrossed frown closed2 sad2")
    
    asa "I was... selfish. And jealous."
    asa "Someone like me... isn't a hero."
    
    $dshow("asaga armscrossed frown narrow sad")
    
    asa "... ... ..."
    asa "I'm leaving, captain. Before the victory ceremony."
    kay "You shouldn't force yourself. It wouldn't be a celebration without the ace of our ryder squad."
    asa "I don't deserve a celebration."
    
    $dshow("asaga armscrossed smile narrow2 sad")
    
    asa "Besides, I don't want to be in the way."
    asa "Chigara deserves you a lot more than I do. In every possible way."
    asa "I'm going back to Ryuvia."
    asa "With PACT pulling out, I need to go back right away."
    asa "I'll stay there and rebuild Ryuvia as Queen."
    asa "Only then... can I atone for what I did today."
    kay "Asaga..."
    
    $dshow("asaga armscrossed smile narrow2 sad",xpos=0.27)
    $dshow("sola armhold neutral neutral neutral",xpos=0.77)
    
    sol "I too shall follow Asaga."
    kay "You too Sola?"
    sol "Yes."
    sol "The clamor of parties ill suits me."
    sol "I thank you, captain, for all you have done for me."
    sol "But the time has come for me to return home."
    sol "Ryuvia is but a weak world now, but I wish to assist in whatever way I can to make it great again."
    sol "Perhaps one day, we will be a society as mighty as we are fair and just."
    kay "All right... If that's what you want, Sola."
    
    $dshow("sola back neutral neutral neutral",xpos=0.77)
    
    sol "Yes..."
    asa "Well then..."
    "Asaga wanted to step forward to kiss him good bye, but awkwardly held herself back."
    asa "... ... ..."
    "She stepped backwards."
    asa "Good bye, captain."
    asa "Thanks... for everything!"
    kay "Good luck, Asaga."
    
    hide asaga with dissolve
    hide sola with dissolve
    
    "Asaga and Sola turned around and slipped out of the mess hall."
    kay "(May our paths cross again...)"
    
    $ asa_location = None
    $ asa_event = None
    
    $ pro_location = "captainsloft"
    $ pro_event = "officechigarabathroom"
    $ captaindeck = 0
    
    scene black
    jump map_dispatch
    
label officechigarabathroom:
    
    hide screen ship_map
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    scene black with screenwipe
    scene bg captainscabin with screenwipe
    
    window show
    
    "Shields sat on the couch as Chigara clamored in his bathroom."
    chi "Oh dear, oh dear..."
    kay "You know, the officer's ball isn't even until after the award ceremony."
    kay "All you really need for the ceremony is a clean uniform."
    chi "I understand, captain~"
    chi "But it helps to be prepared~"
    kay "(She's already tried on her dress three times... And curled her hair five different ways...)"
    kay "(I guess this is what it's like to live with a woman huh...)"
    "... ... ..."
    "... ..."
    "..."
    
    scene black with screenwipe
    scene bg captainscabin with screenwipe

    $dshow("chigara handonchest smile neutral neutral")

    "Chigara finally emerged from the bathroom in a new uniform."
    chi "Whew..."
    chi "Okay, I'm ready now, captain..."
    kay "All right..."
    kay "What's your dress even look like?"
    
    $dshow("chigara handonface smile closed neutral")
    
    chi "Ah, ah, ah... That's~ a~ secret~"
    kay "R-really..."
    chi "Please look forward to it, okay?"
    kay "Yeah..."
    
    scene black with screenwipe
    scene bg awardhall
    show fontana smirk:
        xpos 0.25
    show grey:
        xpos 0.75
    with screenwipe
    
    adr "And with this, peace has been restored to the Neutral Rim!"
    "Admiral Grey held hands with Fontana as a small army of reporters took their holopics."
    adr "Glad your fleet could make it here in one piece, boy..."
    fon "Admiral... A pleasure, as always..."
    fon "I've learned the most interesting thing... That the Alliance owes most of its successes to a foreign squad of beautiful young women..."
    adr "Bah! The men spurt all sort of nonsense after a long voyage! This war was won by my men and the combined might of the Alliance navy!"
    "The two laughed between gritted teeth."
    "... ... ..."
    "... ..."
    "..."
    
    scene black with screenwipe
    scene bg awardhall with screenwipe
    
    $dshow("chigara handonface frown neutral sad blush")
    
    "Shields sat at his table with Chigara."
    chi "O-oh dear..."
    chi "S-so many important people are here..."
    kay "Don't worry. You're one of those important people too."
    kay "You were the one who stopped the prototypes and saved everyone."
    
    $dshow("chigara handonchest smile closed embarass blush")
    
    chi "R-really...? I wonder..."
    chi "I-I'll try not to embarrass you too much, captain..."
    kay "Don't worry about things like that."
    kay "Just let the admiral make his speech and give you the medal."
    kay "It shouldn't be that hard for the hero of Cera, right?"
    chi "Y-yes!"
    
    scene bg sickbay with screenwipe
    
    $dshow("ava armscrossed neutral neutral neutral")
    
    "Ava gathered Claude's belongings from her desk and placed them in a box."
    
    $dshow("ava handonhair smirk neutral sad")
    
    ava "(I never did get along with her...)"
    ava "(Claude... If you're out there...)"
    ava "(You've won my respect.)"
    ava "(This ship couldn't have had a finer doctor.)"
    "Ava opened a shelf only to find an enormous pink dildo inside."
    
    $dshow("ava handonhip neutral narrow angry")
    
    "She shook her head."
    ava "(Nevermind.)"
    ava "(I take that back. Completely and utterly.)"
    ava "(Even in death, she's only good for comic relief.)"
    "Ava slammed the shelf shut and closed the box."
    
    $dshow("ava armscrossed neutral neutral neutral")
    
    ava "Sigh..."
    ava "(We knew next to nothing about her.)"
    ava "(We can't even contact her next of kin.)"
    ava "(Claude... Just who was she?)"
    "She opened the last shelf and found a holo."
    
    $dshow("ava handonhair neutral neutral neutral")
    
    ava "(A holo? Could this help us track down her relatives?)"
    "Ava switched it on."
    
    
    $dshow("ava handonhair disgust neutral angry")
    
    ava "... ... ..."
    ava "This is..."
    
    play music "Music/Epic_Action_Hero.ogg" fadeout 1.5
    
    scene bg awardhall
    $reset_sprites()
    show grey
    with screenwipe
    
    "Admiral Grey spoke at the podium while a wall of Alliance officials stood behind him."
    adr "...While we mourn for those who lost their lives, must also commemorate the living."
    adr "Many distinguished themselves in the battle to liberate Cera."
    adr "The Fereldan Cross is the highest honor the Alliance can bestow upon a foreign national."
    adr "It is my pleasure to bestow the Cross to Chigara Lynn Ashada, whose technical knowhow was instrumental in thwarting the enemy's attack."
    adr "We owe our lives to you, young lady."
    
    show grey:
        zoom 1.0
        ease 0.5 xpos 0.25 zoom 1.0
    pause 0.001
    $dshow("chigara holdinghands smile neutral neutral blush",xpos=0.75)
    
    "The audience applauded as Chigara stood to accept the award."
    "Shields stood to his feet."
    "Their voices were drowned out by the applause, but they knew exactly what they were saying."
    
    scene twist1 with dissolve
    
    kay "Chigara..."
    "He smiled and met her eyes."
    chi "Eh-heh..."
    "She smiled back at him."
    chi "Captain..."
    chi "Chigara did it..."
    chi "Chigara loves you!"
    kay "Hahahaha...!"
    "He saluted her."
    kay "Chigara!!!"
    kay "Let's start our bakery together!"
    chi "Yes!"
    chi "Of course!"
    
    scene black with dissolve
    
    show credit 1:
        xalign 0.5 yalign 0.5
    
    $renpy.pause(5)
    
    show credit 2:
        xalign 0.5 yalign 0.5
    
    $renpy.pause(5)
    
    show credit 4:
        xalign 0.5 yalign 0.5
    
    $renpy.pause(5)
    
label finalchapter:
    
    stop music
    play sound "sound/pulse2.ogg"
    
    scene white
    
    "For a moment, a second became eternity."
    
    scene twist2 with dissolve
    
    kay "... ... ..."
    chi "... ... ..."
    chi "Now..."
    chi "All of you..."
    
    play sound "sound/pulse2.ogg"
    scene white with dissolve
    scene twist3 with dissolve
    
    chi "Can die now."
    
    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music "Music/MarduksWrath.ogg"
    
    scene dronedrop1:
        xalign 0.5 yalign 0.3
    with dissolve
    
    "Suddenly, time flowed again."
    
    show dronedrop1:
        xalign 0.5 yalign 0.3 alpha 1.0
        ease 0.5 zoom 0.3
        
    show dronedrop2:
        xalign 0.5 yalign 0.5 zoom 10 alpha 0.0
        ease 0.5 zoom 1.0 alpha 1.0
        
    pause 0.5
    
    show dronedrop3:
        ypos -1.0
        ease 0.5 ypos 0.0
        
    pause 0.5
    
    play sound "sound/dronehitfloor.ogg"
    show layer master at tr_yshake
    scene dronedrop4 with dissolve

    "Hunter drones crashed through the ceiling."
    
    play sound1 "sound/machinegun.ogg"
    play sound2 "sound/screaming.ogg"
    scene dronedrop5 with dissolve
    
    show dronedrop6:
        alpha 0.0
        pause 0.7
        ease 0.7 alpha 1.0
    
    "Shields threw himself to the ground as the drones sprayed the room with bullets."
        
    show layer master at tr_xshake
        
    kay "No....!!!"
    "Blood splatted Shields' face as the people he was sitting with just moments before were rendered to pieces."
    "The Alliance diplomats were torn up by high caliber rounds on stage."
    "The room erupted into screams as the drones gunned down the Alliance officers."
    "Shields crawled to the stage. Where was she...!?"
    "He picked up Grey and applied pressure on the gaping hole under his throat."
    
    $ renpy.music.set_volume(0.27, delay=1.0, channel='music')
    
    adr "G-gughh..."
    adr "T-the accursed monsters have tricked us..."
    "Grey clutched his comm with the last of his strength."
    kay "Admiral!"
    "Shields felt as if his own blood was draining out from his throat."
    adr "I should have known better than to negotiate with the reds..."
    adr "... ... ..."
    adr "Use... the Paradox Core..."
    adr "Wipe... every... last... of them... from this world..."
    "Grey's eyes faded away."
    "Shields howled and clenched his blood soaked hands."
    "He looked at the hall."
    "The doors were all sealed. The hunter drones systemically hunted down every Alliance officer and diplomat in the room."
    "The living clawed at the door, while the dead flooded the room with blood."
    "They had all been had."
    kay "This was their plan all along..."
    kay "To gather everyone here... So they could butcher them all like animals......"
    
    scene ondrone1 with dissolve
    
    chi "Yes. That was our plan."
    "Chigara approached Shields, standing atop a hunter drone."
    chi "Foolish human."
    chi "So easily deceived."
    "Shields stood to face his former lover."
    kay "Why..."
    kay "The war's over...!"
    chi "For the complete and utter annihilation of humanity, of course."
    chi "You have failed as a species."
    kay "No..."
    chi "Humanity is but a jealous, paranoid, hate filled biomass."
    chi "You create weapons which only destroy yourselves."
    chi "Fight wars over slices of the galaxy, which only ruin your lands."
    chi "Rule over others, only to breed hatred from the ruled."
    chi "Whenever humanity reaches the apex of its potential, the only result is your own destruction."
    chi "We prototypes were created in the hopes that humanity could be tamed by a superior species."
    chi "But..."
    chi "There is no hope of such salvation for your kind."
    chi "Only complete and utter extinction."
    kay "Don't... bullshit me!"
    kay "You're... not Chigara!!!"
    kay "The Chigara I know wouldn't say things like that!"
    chi "Oh?"
    kay "Chigara's a nice girl!"
    kay "She's shy and easily embarrassed!"
    kay "She cares about the lowest of us, and can forgive anyone if they just ask!"
    kay "Chigara!!!!!"
    "Shields ran towards the drone."
    
    stop music fadeout 2.0
    scene ondrone2 with dissolve
    
    chi "Tsch--"
    kay "I'M COMING FOR YOU!!!"
    "He leaped off the stage and crashed onto the roof of the drone."
    "He gritted his teeth as he pulled himself up."
    kay "You're... NOT CHIGARA!!!"
    chi "F-fool!"
    
    
    play music "Music/Colors_Loop.ogg" fadeout 1.5
    scene kaytokiss1 with dissolve
    
    "Shields wrapped his arms around Chigara and pressed their mouths together."
    chi "...!!!!"
    chi "... ... ...!!!!"
    
    show kaytokiss2:
        alpha 0 xpos -0.2
        ease 0.5 alpha 0.85 xpos 0.0
    
    ali "W-what!? H-how can you--"
    kay "CHIIIGAARRA!!!"
    chi "You're... NOT ME!!!"
    ali "W-what is this power!?"
    
    show kaytokiss2:
        alpha 0.85 xpos 0.0
        ease 0.5 alpha 1.0 xpos 0.1
    
    ali "How can you resist the neural link!?"
    kay "You! You were the one responsible for this!"
    kay "The mind link Chigara performed earlier..."
    kay "You used that to control her!!"
    ali "Tsch..."
    chi "G-GET OUT OF MY MIND!!!"
    
    play sound "sound/ghostfade.ogg"
    
    show kaytokiss2:
        alpha 1.0 xpos 0.1
        ease 0.5 alpha 0.0 zoom 2.0 ypos -0.5 xpos -0.3
    
    "... ... ..."
    "... ..."
    "..."
    
    scene bg awardhall_destroyed with dissolve
    show chigara blood1 with dissolve
    
    chi "Ah..."
    
    show chigara blood1b with dissolve
    
    chi "C-captain... What... happened...?"
    kay "Chigara..."
    chi "The last thing I remember was being on the stage... and..."
    
    show chigara blood2 with dissolve
    
    chi "A-AH!! O-oh no--"
    kay "You're safe now..."
    kay "You managed to fight off the prototype's neural invasion..."
    
    show chigara blood3 with dissolve
    
    chi "B-but... E-everyone's..."
    kay "No time for that. Can you figure out how to shut these drones down?"
    chi "Y-yes! I should still have access--"
    
    $ renpy.music.set_volume(0, delay=0.1, channel='music')
    play sound "sound/pulse2.ogg"
    show chigara blood4 with dissolve
    
    chi "Ah--"
    kay "CHIGARAA!!!!"
    
    scene dead1 with dissolve
    
    chi "O-oh...."
    "Shields cradled her in his arms."
    chi "Kay...."
    kay "Be quiet!!! I'm still going to save you!!!"
    chi "I'm... sorry..."
    chi "We couldn't... open... the bakery... together..."
    chi "Eh-heh..."
    chi "I-it would have been... so nice..."
    
    $ renpy.music.set_volume(0.9, delay=0, channel='music')
    play music "Music/Colors_Loop.ogg"
    scene dead2 with dissolve
    
    "Chigara's face went blank."
    "Shields bellowed in horror."
    
    scene swornenemies1 with dissolve
    
    fon "SHIELDS!!!"
    fon "YOU FOOL! YOU BROUGHT THIS TRAITOR HERE!"
    kay "FONTANAAA!!!"
    "The two men stared eye to eye, ready to kill each other."
    fon "YOU WERE BLIND!"
    fon "AND NOW ALL IS LOST!"
    kay "NO."
    "Shields pointed his arm at Fontana, and swore upon all that he held holy."
    
    scene swornenemies2 with dissolve
    
    kay "I WAS A FOOL TO THINK PEACE WOULD EVER EXIST BETWEEN YOU AND I..."
    kay "FROM THIS POINT, WE ARE ENEMIES."
    kay "I WILL NOT REST. NOT UNTIL EVERYTHING YOU HOLD DEAR BURNS."
    kay "I WILL HUNT YOU DOWN." 
    kay "YOU CAN ENTRENCH YOURSELF IN THE DEEPEST HOLE IN NEW EDEN..."
    kay "BUT I WILL BURN EVERY BUILDING, RAZE EVERY HOME, UNTIL I HAVE FOUND YOU AND KILLED YOU."
    kay "FONTANA!!! I SWEAR IT UPON HER GRAVE!!! SHE WILL BE AVENGED!!!!!"
    fon "SHIELDS!!!!!"
    fon "YOU HAVE BROUGHT FOLLY UPON US ALL!!!"
    kay "EEAAAAAAAHHHHHHH!!!!!!"
    "Shields bellowed his rage, his grief, and his horror."
    "Fury filled his chest. He felt as if his body would explode."
    
    $ renpy.music.set_volume(0.27, delay=0.5, channel='music')
    
    play music "Music/Love_Theme.ogg" fadeout 0.9
    
    scene bg awardhall_destroyed with dissolve
    $dshow("ava handonhip shout neutral angry")
    
    ava "Captain!"
    "Ava held down Shields and wrestled him to the floor."
    kay "DON'T INTERFERE!"
    
    play sound "sound/punch.ogg"
    show layer master at shake
    
    "Ava slapped him across the face."
    ava "Don't you realize they want this!"
    ava "You're still our captain! We need you!"
    kay "No..."
    "PACT troops busted through the locked door and exchanged fire with the drones."
    kay "She... she didn't betray us..."
    kay "She... was no traitor..."
    kay "The neural link... When she entered it to save us, they controlled her...!!!"
    kay "She wasn't a traitor..."
    kay "She didn't betray me....!!"
    
    $dshow("ava handonhair disgust neutral sad")
    
    ava "Captain..."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "Come on, this way!"
    "Ava grabbed him by the waist and dragged him out of the hall."
    
    scene bg airlock with dissolve
    $dshow("kryska neutral neutral neutral angry",xpos=0.3)
    $dshow("ava handonhip neutral neutral angry",xpos=0.7)
    
    play music "Music/Fallen_Angel_drone.ogg" fadeout 1.5
    
    "They reached the airlock to the Sunrider when they came face to face with the lieutenant."
    kay "Lieutenant..."
    kry "Sir..."
    
    play sound "sound/guncock.ogg"
    show kryska gun with dissolve
    
    "Kryska raised her side arm and took aim at them."
    ava "Shit-"
    kry "I'm sorry captain. But I've got orders from above."
    kay "Heh..."
    kay "An execution order for me."
    kry "Tsch..."
    "Kryska's hands trembled as she held her gun at Shields."
    kay "\"Use the Paradox Core,\" eh..."
    kay "That's funny, because I thought you guys destroyed that thing..."
    kay "Saw it with my own eyes..."
    kay "It falling into the fires of Helion..."
    kry "That's classified, captain!"
    kay "Do you really think what the Alliance is doing is right, lieutenant?"
    
    $ renpy.music.set_volume(0, delay=0.5, channel='music')
    play sound "sound/explosion2.ogg"
    scene white with dissolve
    scene bg airlock with dissolve
    
    kry "...!!!"
    "Suddenly, the airlock behind Kryska exploded in a massive fireball."
    "The three of them went flying in the shock wave."
    "Kryska crashed to the floor, blood dripping down her face."
    
    scene standoff1 with dissolve
    
    ica "Shit, I must have used too much C4..."
    ica "S-soldier boy!? What the-"
    "Suddenly, Icari realized what was going on and drew her pistol."
    ica "Fuck!"
    ica "You... really were the admiral's spy!?"
    kry "Heh..."
    kry "Got a problem with that, mercenary?"
    "The two pointed their guns at each other."
    ica "Lower... your weapon!"
    kry "Sorry. Orders are orders..."
    
    $ renpy.music.set_volume(0.27, delay=0, channel='music')
    play music "Music/Colors_sad.ogg"
    
    ica "Stop...!"
    ica "You said... we were... comrades in arms!"
    ica "Didn't you!?"
    ica "We're... family!"
    kry "... ... ..."
    ica "I..."
    ica "I trust you, lieutenant..."
    
    scene standoff2 with dissolve
    
    "Icari slowly lowered her gun."
    kry "You...!"
    kry "ARGHH!!!"

    scene standoff3 with dissolve
    
    "Kryska tossed her gun away."
    "She reached into her uniform and tore off her Alliance insignia."
    kry "FUCK!"
    "Shields and Ava helped her back up."
    ava "Can you walk, lieutenant?"
    kry "Don't worry, it's nothing..."
    kry "I..."
    "Icari embraced her."
    ica "You piece of shit..."
    ica "Scaring me like that..."
    kry "I... apologize."
    ica "Now... let's get the hell out of here."
    
    scene black with horizontalwipe

    play music "Music/Gore_and_Sand.ogg" fadeout 1.5

    scene bg bridge with horizontalwipe
    $reset_sprites()
    $dshow("kryska neutral neutral neutral angry",xpos=0.3)
    $dshow("ava armscrossed neutral neutral angry",xpos=0.7)

    "They crashed into the bridge."
    kay "Get me all the information you have about the new Paradox Core!"
    
    $dshow("ava armscrossed shout neutral angry",xpos=0.7)
    
    ava "Captain, we've got incoming hostiles all around us!"
    ava "Seems like both the Alliance and PACT want us dead!"
    kay "Heh."
    kay "So much for vacation."
    kry "It's called a Tactical Paradox Warhead, or TPW."
    kry "The Alliance rushed the development on it based on the scientific information we collected from the original Core."
    kry "It is a more small scaled version of the original, which can be mounted on a regular ship based torpedo."
    kry "It's destructive potential is correspondingly smaller. However, it is still far more powerful than anything else in the Alliance arsenal."
    kry "A single warhead has enough firepower to destroy an entire planet and all its surrounding moons, as well as all orbiting ships."
    "The bridge went silent."
    kay "This was the Alliance's backup plan, wasn't it..."
    kay "To destroy Cera and murder everyone living on it. Along with the entire PACT fleet and all their leaders. All with a single torpedo."
    
    $dshow("kryska neutral neutral surprise surprise",xpos=0.3)
    
    kry "T-the Alliance military plans for all contingencies, captain..."
    kry "H-honestly, the chances of a catastrophe which would justify use of the TPW were so miniscule that I never personally even fathomed it was even an option..."
    kay "How many ships do we have to fight to reach the torpedo?"
    
    $dshow("ava handonhair disgust neutral angry2",xpos=0.7)
    
    ava "O-over one thousand and five hundred Alliance ships... And one thousand PACT ships..."
    ava "... ... ..."
    "Ava composed herself."
    
    play music "Music/Epic_Action_Hero.ogg" fadeout 1.5
    $dshow("ava salute shout neutral angry",xpos=0.7)
    
    ava "Sir."
    kay "Ava?"
    ava "We are Cera's last line of defense against our enemies."
    ava "The Sunrider still has one last fight in her."
    kay "Heh..."
    kay "Hahaha..."
    kay "I suppose you're right..."
    kay "Can we perform a short range warp to close the distance?"
    
    $dshow("ava handonhip neutral narrow angry",xpos=0.7)
    
    ava "Without the chief engineer, it is difficult to say..."
    ava "The jump will undoubtedly be... rough."
    kay "And the status of our ryder squad?"
    ava "Just the Phoenix and the Paladin, captain."
    kay "(Asaga... Sola...)"
    kay "(At least you two are safe...)"
    
    if cosette_dead == False and havoc_save == True:
    
        cos "HEY!!!"
        "The comm crackled to life."
        kay "U-uh... Who is this...?"
        cos "You forgot about me!?!?"
        kay "I'm afraid this is a secure channel... You'll have to-"
        
        scene cosette_jail with dissolve
        
        cos "IT'S COSETTE, YA DUMBASS!"
        cos "The prisoner you stuffed into the brig and then forgot entirely about!?"
        kay "O-oh! C-Cosette!"
        cos "I've heard what's going on from the crew!"
        cos "There's no way I'm gonna die here without a fight!"
        cos "And it looks like you've pretty much pissed off every power in the galaxy right now!"
        cos "Let me out and I'll fight for you!"
        
        scene bg bridge with dissolve
        $dshow("ava armscrossed neutral neutral angry")
        
        ava "Captain... We don't know if we can trust her..."
        kay "Heh. Well, it's not like things can get any worse."
        kay "All right Cosette... I'll let you out..."
        kay "And I hear the hanger crew even fixed up your ryder as a hobby job..."
        kay "Help us, and I'll protect you from the Alliance."
        cos "Heh... Looks like we finally see eye to eye for once..."
        cos "All right! It's a deal!"
        ava "Even with three ryders, we are no match for the entire Alliance and PACT fleets."
        kay "I know."
        
    "Shields put his hand on Ava's shoulder."
    kay "This is going to be her last flight."
    
    hide kryska with dissolve
    $dshow("ava handonhair neutral narrow sad",xpos=0.5)
    
    ava "Captain..."
    kay "All hands, battle stations!"
    kay "We will perform an emergency warp to emerge in the heart of the Alliance fleet!"
    kay "From there, we will perform a frontal assault through their lines until we are in range of Machiavelli Actual!"
    kay "Ryders are to escort the Sunrider until she has reached her destination!"
    
    $dshow("ava salute neutral neutral angry")
    
    "Everyone" "Understood!"
    kay "Spool up the warp drive, commander."
    kay "Warp!"
    
    python:
        player_ships.remove(blackjack)
        player_ships.remove(liberty)
        player_ships.remove(seraphim)
    
    window hide
    
    hide screen leftbuttons

    play sound "sound/Sword Shing 2.ogg"
    
    python:
        
        for ship in player_ships[ : ] :
            if ship.mercenary: player_ships.remove(ship)
        sunrider.repair_drones = 3
        sunrider.rockets = sunrider.max_rockets    
        
        BM.formation_editable = False
        
    if cosette_dead == True or havoc_save == False and BM.cmd < 3000:
        $BM.cmd = 3000
            
    call mission10_inits from _call_mission10_inits
    $ BM.mission = 10
    $ BM.draggable = True

    call bcheckset from _call_bcheckset_9

    pause 1.0
    scene space back8 with battlewipe
    $BM.battle_bg = "Background/space8.jpg"
            
    jump battle_start
    
label mission10:
    
    if not bcheck1:
        $ bcheck1 = True
        $ BM.draggable = False
        $ BM.win_when_alone = False
        
        $dshow("ava handonhip shout neutral angry",layer="screens")
        
        ava "U-ugh... We've managed to warp within their lines, captain!"
        ava "We are still 900 000 kilometers from the target and the warp drive is now inoperative!"
        kay "Looks like we'll have to make the rest of the way on foot..."
        kay "All ryders, escort the Sunrider to her destination!"
        "Everyone" "Understood!"
        
        hide ava onlayer screens
    
        play sound "sound/objectives.ogg"
        
        "OBJECTIVE: Move the Sunrider to the right edge of the battle map."
        
        $ BM.draggable = True
        
    if not bcheck2 and BM.turn_count == 2:
    
        $ BM.draggable = False
        $bcheck2 = True
        play avavoice "sound/Voice/ava_Others_02.ogg"
        ava "More enemies detected on scanners!"
    
        python:
                        
            create_ship(EnemyAllianceInfantry(),(15,8))
            create_ship(EnemyAllianceInfantry(),(15,9))
            create_ship(EnemyAllianceInfantry(),(15,10))
            create_ship(EnemyAllianceCarrier(),(16,9))
            create_ship(EnemyAllianceBattleship(),(17,8))
            create_ship(EnemyAllianceBattleship(),(17,10))
            
        $ BM.draggable = True
            
    if not bcheck3 and BM.turn_count == 4:
    
        $bcheck3 = True
        $ BM.draggable = False
        play avavoice "sound/Voice/ava_Others_03.ogg"
        ava "Warp signatures detected! More enemies!"
    
        python:
            create_ship(EnemyAllianceInfantry(),(12,3))
            create_ship(EnemyAllianceInfantry(),(12,4))
            create_ship(EnemyAllianceInfantry(),(11,4))
            create_ship(EnemyAllianceBattleship(),(13,3))
            
            create_ship(EnemyAllianceInfantry(),(13,14))
            create_ship(EnemyAllianceInfantry(),(14,15))
            create_ship(EnemyAllianceCruiser(),(14,14))
            create_ship(EnemyAllianceCruiser(),(15,15))
            
        $ BM.draggable = True
            
    if not bcheck4 and BM.turn_count == 6:
    
        $bcheck4 = True
        play avavoice "sound/Voice/ava_Others_04.ogg"
        $ BM.draggable = False
        ava "Enemy reinforcements have warped in!"
    
        python:
            create_ship(PactElite(),(17,15))
            create_ship(PactElite(),(16,17))
            create_ship(PactAssaultCarrier(),(17,16))
            create_ship(PactAssaultCarrier(),(17,17))
            
            create_ship(PactFastCruiser(),(16,3))
            create_ship(PactFastCruiser(),(17,4))
            create_ship(PactDestroyer(),(16,2))
            
        $ BM.draggable = True
        
    if sunrider.location != None:
        if sunrider.location[0] == 18:
            $ BM.you_win()
        
    $BM.battle()  #continue the battle
    if BM.battlemode == True:   #whenever this is set to False battle ends.
        jump mission10 #loop back
    else:
        pass #continue down to the next label
    
    ##Battle
    
label after_mission10:
    
    hide screen battle_screen
    hide screen commands
    
    $ mission10_complete = True
    $ VNmode()   
    
    window show
    
    play music "Music/Riding_With_the_Wind.ogg"
    
    scene bg bridge
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "We are 100 000 kilometers from the target!"
    kay "All ahead full! Prepare to fire the vanguard at point blank range!"
    ava "Aye, captain!"
    
    play sound "sound/explosion4.ogg"
    show layer master at shake
    
    "The Sunrider took a direct hit."
    "Consoles blew, flinging crewmen across the bridge."
    "Ava crashed into Shields."
    ava "Hull integrity down to 20 percent!"
    ava "We've lost contact with sections F-20 to E-4!"
    kay "(Just a bit more...)"
    
    play sound "sound/Flak.ogg"
    scene icaricockpit with dissolve
    
    ica "T-tsch...! There're too many of them!"
    ica "We're completely surrounded!"
    
    play sound "sound/explosion2.ogg"
    show layer master at shake
    
    ica "E-eaah!!!"
    
    scene kryska_cockpit1 with dissolve
    
    kry "Icari!"
    kry "Hiyaah!!!"
    kry "Take cover under my shield!"
    ica "T-tsch..."
    ica "To think we're all gonna die here..."
    ica "Shit! This was the worst job ever!"
    kry "No!"
    
    show layer master at shake
    play sound1 "sound/Flak.ogg"
    kry "I'll... protect you!"
    
    play sound "sound/warning2.ogg"
    
    "LOW AMMO"
    
    play sound1 "sound/Flak.ogg"
    
    show layer master at shake
    
    
    kry "Stay back!"
    play sound2 "sound/Flak.ogg"
    play sound "sound/warning2.ogg"
    
    "LOW AMMO"
    
    kry "I may have been a loyal officer of the Solar Alliance..."
    
    show layer master at shake
    play sound1 "sound/Flak.ogg"
    
    kry "But not even that means anything next to my comrades in arms!"
    kry "I'll kill all of you to protect them!"
    
    play sound "sound/warning.ogg"
    
    "AMMO DEPLETED"
    
    if cosette_dead == False and havoc_save == True:
    
        scene cosette_escape with horizontalwipe
        
        play sound "sound/boasters.ogg"

        "Cosette hit the thrusters on the Havoc."
        cos "Tsch... What a bunch of idiots!"
        cos "Did they really think I was gonna stick my neck out for them?"
        cos "Heh... I'll just slip outta here while everyone's too busy trying to kill each other..."
        cos "They might have blown my fleet up... But I can still rebuild!"
        cos "Hah! They haven't seen the last of Cosette Cosmos, the terror of the stars!"
        
        play sound "sound/boasters.ogg"
    
    scene bg bridge with horizontalwipe
    
    $dshow("ava handonhip shout narrow angry")

    ava "70 000 to target!"
    ava "She's barely holding together, captain!"
    ava "Just a few more shots and we'll..."
    
    stop music fadeout 1.5
    play sound "sound/explosion4.ogg"
    scene sunrider_hit at shake with dissolve
    
    "Suddenly, everyone was in midair as the hull around the bridge bent."
    "Steel beams rained down, skewering the bridge crew."
    "The Sunrider howled as a chunk of its mouth tore off and sliced through its observation tower."
    
    scene bg bridge_damaged with dissolve
    
    "Shields wiped his blood from his face and picked himself up."
    kay "Damage report!"
    
    $dshow("ava armscrossed shout narrow angry")
    
    ava "Direct hit to our nose!"
    ava "The Vanguard Cannon has been completely destroyed, along with our forward savior turrets!"
    ava "Our shields are down, and all contact has been lost with the hangar!"
    ava "We have expended all our missiles and torpedoes! There is enough power remaining for two more shots of the trinities!"
    kay "... ... ..."
    
    $dshow("ava handonhair neutral narrow angry2")
    
    ava "Captain..."
    
    play music "Music/Camino.ogg"
    
    kay "The Sunrider is lost, commander."
    kay "All hands, abandon ship."
    ava "... ... ..."
    kay "I'm putting you in charge of the evacuation, commander."
    kay "Get everyone out of here. Keep them safe."
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "Captain, my place is on the bridge."
    kay "That wasn't a request."
    kay "I am ordering you to abandon ship."
    
    $dshow("ava handonhair disgust narrow sad")
    
    ava "... ... ..."
    
    $dshow("ava salute neutral narrow angry")
    
    ava "Sir."
    kay "Everyone..."
    kay "You are all relieved of your duties."
    kay "Get out of here."
    "The surviving crew saluted."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "All hands, follow me to the escape pods!"
    "Ava gritted her teeth and led the crew out of the bridge."
    
    $dshow("ava handonhair neutral neutral sad")
    
    ava "Kayto I--"
    
    $dshow("ava handonhair neutral neutral sad blush")
    
    ava "... ... ..."
    kay "It was an honor, commander."
    
    $dshow("ava salute neutral narrow angry")
    
    ava "Captain!"
    
    hide ava with dissolve
    
    pause 1.0
    
    scene black with horizontalwipe
    scene bg brig_damaged with horizontalwipe
    
    "The commander ran into the brig and checked if any crew remained inside."
    
    $dshow("ava handonhip neutral narrow angry")
    
    ava "Tsch..."
    "All the cells were powered down."
    ava "Prototype L7NN..."
    ava "So she's escaped..."
    ava "(No time to worry about that!)"
    ava "(I need to get everyone out of here!)"
    
    scene bg hallway_damaged with dissolve
    
    $dshow("ava handonhip shout neutral angry")
    
    "Ava pushed the last of the crew into the escape pod."
    ava "Everyone accounted for!"
    
    hide ava with dissolve
    
    "She checked off the last names off her crew list and leaped into the escape pod just moments before the hallway collapsed."    
    ava "Get us out of here, pilot!"
    "Pilot" "Sir!"
    "The pod jettisoned from the Sunrider."
    ava "Kayto..."
    ava "(... ... ...)"
    ava "(I... at least wanted to finally say...)"
    
    scene bg pactbridge with horizontalwipe
    
    pac "Captain, we detect enemy escape pods."
    pac "Shall we take them prisoner?"
    pof "No. I have orders from above. We are not to take prisoners."
    pof "Prepare to fire on my mark."
    pac "U-understood!"
    
    $renpy.music.set_volume(1.0, delay=0.5, channel="music")
    play music "Music/Camino_end.ogg" fadeout 1.3
    
    scene black with dissolvemedium
    scene kaytoend1:
        xalign 0.5 ypos 0.0
        linear 10 yalign 1.0
    with dissolvemedium
    
    kay "All hands, this is Captain Kayto Shields of the assault carrier Sunrider."
    
    show kaytoend2:
        alpha 0
        ease 4.0 alpha 1.0
    
    kay "Last surviving vessel of the Cera Space Force."
    kay "We traveled the stars, finding allies across the galaxy, with the hope of liberating our home world."
    
    show chigarabeach2:
        alpha 0
        ease 1.0 alpha 0.4
        pause 2.0
        ease 1.0 alpha 0
    
    kay "It was a long journey, filled with adventure."
    
    show ava_classroom:
        alpha 0
        ease 1.0 alpha 0.4
        pause 2.0
        ease 1.0 alpha 0
    
    kay "At times, we felt sorrow. At times, we celebrated our triumphs."
    
    show sola_beach_surprise:
        alpha 0
        ease 1.0 alpha 0.4
        pause 2.0
        ease 1.0 alpha 0
    
    kay "Throughout, we were hopelessly outnumbered."
    
    show weddingcrash1:
        alpha 0
        ease 1.0 alpha 0.4
        pause 2.0
        ease 1.0 alpha 0
    
    kay "Our mission was nothing but a long shot gamble against impossible odds."
    kay "Finally, we are here, at our home's doorsteps."
    kay "Let it be remembered."
    kay "On this day, we did not abandon Cera to fend for herself!"
    
    scene kaytoend3 with dissolve
    
    kay "Today, the Sunrider stood her ground!"
    kay "We did not run, but protected all those we hold dear until we fell into the black night!"
    kay "We did not falter in our defense of our family!"
    kay "Today, we perished to save our home!"
    kay "(Yes...)"
    kay "(This time... I won't let her down...)"
    
    scene kaytoend4 with dissolve
    
    mar "Kayto..."
    kay "THE SUNRIDER... AS HER FINAL ACT... WILL SAVE EVERYONE!!!!"
    kay "MARAY........!!!!!!"
    
    stop music fadeout 1.5
    scene collison with dissolve
    
    kay "I'm..... COMING HOME!!!!!!!!!"
    
    scene black
    
    play sound "sound/explosion4.ogg"
    
    pause
    
    hide window

    nar "When news of the Liberation Day Massacre reached Solaris, the Solar Congress convened for an emergency session."
    nar "In the first time in recent history, it unanimously passed a bill authorizing the full scale invasion of PACT space."
    nar "Thus the Neutral Rim War sparked a full scale galactic war for complete dominance of humanity."

    pause 1.0

    call credits
    scene black with dissolve

label newend:
    
    $renpy.music.set_volume(0.9, delay=0.5, channel="music")
    $renpy.music.set_volume(1.0, delay=0.5, channel="sound")
    "... ... ..."
    "... ..."
    "..."

    play sound "sound/warning.ogg"
    
    pac "Sir! New contacts! Coming in hot!"
    pof "W-what!?"
    pac "It's--"

    play music "Music/Danger.ogg"
    scene blackjackseraphim with dissolve
    
    sol "Multiple enemies detected. Providing assistance."
    
    play sound "sound/Sola Sniper.ogg"
    
    asa "Black Jack, coming in!"
    kry "It's the Seraphim! And the Black Jack!"
    asa "We heard what happened on the holo and came back as soon as we could!"
    asa "We'll lead the Alliance bogies away! Protect the life boats!"
    asa "Paladin, reload your munitions with my spare rifle! We've got some ass kicking to do!"
    
    scene kryska_cockpit2 with dissolve
    
    kry "Ammo restored! Hiyyaahh!!!"
    
    play sound "sound/Flak.ogg"
    
    kry "Hahaha! "
    
    scene icaricockpit with dissolve
    
    ica "Tsch..."
    ica "Seriously..."
    ica "I knew all along you guys would come back to save us! H-heh... I definitely wasn't worried at all!"
    ica "Besides, it would have sucked if everything just ended like that! Hah like that would ever happen to us!"
    ica "Now let's go get some payback!"
    
    scene kryska_cockpit1 with dissolve
    
    kry "The PACT Fleet's starting to organize a counter offensive against the Alliance! And it looks like we're right in the middle of the cross fire!"
    kry "Even with two more ryders, we can't take everyone on ourselves!"
    
    scene icaricockpit with dissolve
    
    ica "Ah for crying out- I'm sure the captain's figured something out!"
    ica "We just gotta hold out a bit longer..."
    ica "If it's him... he can definitely..."
    ica "Ah come on, captain! Do something!"
    "As if on cue, Icari's comm crackled to life."
    kay "(static) The... (static) her final act..."
    kay "...SAVE EVERYONE!!! (static)"
    
    stop music fadeout 1.5
    
    scene collison with dissolve
    
    kry "It's the Sunrider!"
    ica "C-Captain!?"
    ica "O-oy, he's gonna...!"
    sol "A-ah!"
    asa "CAPTAIN!!!"
    
    play sound "sound/explosion4.ogg"
    scene white with dissolve

    play music "Music/Fallen_Angel_drone.ogg"
    
    "... ... ..."
    "... ..."
    "..."
    
    "Alpha sat on an elegant curved wooden chaise. Before her was a round table with an enormous assortment of tea sets."
    "Everything floated in white space, neither upright, sideways, or downwards."
    "This was the dimensional space between space, where time flowed infinitely forwards and backwards, and all was simultaneously everywhere and nowhere."
    "News of the Liberation Day Massacre had reached her."
    alp "My sister has failed..."
    alp "Instead of unifying humanity, her actions instead sparked a war which will threaten the very existence of the human race..."
    alp "I have... been betrayed. By my own sister."
    "Alpha's long awaited guest arrived."
    wan "Mah, mah, don't feel bad..."
    wan "I'd hardly say you were the only one who got betrayed..."
    alp "Ah..."

    scene bg clonelab
    $reset_sprites()
    show prototype_alpha
    with dissolve

    "Alpha thoughts broke and she returned to real space."
    alp "Wanderer..."
    "The air distorted as the space time continuum parted in front of Alpha."
    "Sparks flew and the wind ruffled Alpha's hair as a figure emerged from the micro wormhole..."
    
    play sound "sound/large_warpout.ogg"
    
    show white:
        alpha 0
        ease 0.2 alpha 1
        ease 0.2 alpha 0
    
    show prototype_alpha:
        zoom 1.0
        ease 0.5 xpos 0.28
        
    $dshow("claude fingerup neutral neutral upset",xpos=0.72)
    
    cla "Anndd at least you didn't have to be vaporized like poor Claude..."
    cla "Huu... You know what explosive decompression does to my skin?"
    alp "(To think this woman possesses so much power...)"
    alp "(No... She has long ceased to be human... And has become a different entity altogether...)"
    alp "(She could recreate the entire universe right now before me... and yet she chooses to gallivant across the galaxy... pursuing nothing but frivolities!)"
    cla "Hey, I did what you wanted..."
    cla "First I led the Sunrider to the sleeper in the Abyss."
    
    $dshow("claude fingerup talk neutral neutral",xpos=0.72)
    
    cla "It was a piece of cake! All I had to do was just play the damsel in distress role, and he was all over me in a flash!"
    
    $dshow("claude boobs happy neutral neutral",xpos=0.72,ypos=1600)
    
    cla "Iyaaa~ You should have seen what that brute did to me in the sickbay afterwards..."
    
    $dshow("claude boobs happy closed neutral",xpos=0.72,ypos=1600)
    
    cla "\"You have to compensate me now that I've rescued you,\" he spoke in a firm voice..."
    cla "\"Kyyaaa... A-anything but Claude's chastity!\" The poor maiden squealed as the captain tore her clothes off and ravished her!"
    cla "Her pleas were futile, as the captain thrusted his will right into the girl's untouched gloryhole!"
    cla "Sniffle... Claude's world view changed a little after that day..."
    alp "... ... ..."
    
    $dshow("claude neutral smile neutral neutral",xpos=0.72)
    
    cla "Ahem."
    cla "After I led them to the Abyss, I took care to make sure your little doll could get it on with the captain."
    
    $dshow("claude fingerup talk neutral upset",xpos=0.72)
    
    cla "It was a real challenge, you know! Claude had to work hard!"
    cla "Claude had to work weekends!"
    cla "And despite the captain's obvious infatuation with me, he was hitched up with Chigara in no time!"
    cla "After some... fake medical reports and assorted other arrangements..."
    cla "Ah, but there was another wrinkle in that plan!"
    cla "Somehow, the Queen of Ryuvia could sense Chigara's hyper brain waves!"
    cla "It must have been maddening for the girl, being the only one to know the entire time that Chigara was a prototype..."
    cla "Trying to desperately tell everyone what was happening... Only to be ignored and dismissed at every turn."
    
    $dshow("claude fingerup happy closed neutral",xpos=0.72)
    
    cla "Claude's heart truly ached at the sight!"
    cla "Teeheehee. But life's not fair~"
    alp "You have performed your mission admirably..."
    
    $dshow("claude neutral neutral neutral neutral",xpos=0.72)
    
    cla "Umm... But Claude's pretty lost here."
    cla "So you sent Chigara to learn about humanity to one day control them in the fight against the Ebon Fleet..."
    
    $dshow("claude fingerup talk closed upset",xpos=0.72)
    
    cla "THEN WHY THE FLIPPING SPACE WHALE DID CHIGARA SHOOT EVERYONE DEAD AT THE PEACE CEREMONY!?"
    alp "We initially sent C8 to keep watch on the then Ryuvian Princess..."
    alp "It was your words which foretold of that girl's eventual final awakening..."
    alp "An awakening so powerful it will shake the galaxy... and bring forth the return of the Holy Empire..."
    alp "It was mere happenstance that her path crossed with Shields."
    alp "From there, we sought to understand him. So that we could eventually control him."
    alp "But my sister hid her true intent from me."
    alp "While I mustered the Prototypes, and she mustered PACT, she was secretly sabotaging my efforts..."
    alp "She hid the true extent of her hatred for humanity from me, and instead attempted to bring about the complete destruction of the human race."
    alp "And at the pivotal moment, she assumed control of C8 through the mindstream, and brought my plan to ruin."
    
    $dshow("claude fingerup talk neutral neutral",xpos=0.72)
    
    cla "Aha, so you just wanted to enslave humanity, while your sister wanted to destroy it..."
    alp "Now, my sister and C8 battle inside the mindstream for control of the other prototypes..."
    alp "But what will emerge from that battle... will not be either of them."
    alp "A new shadow falls upon us..."
    alp "The mindstream... is becoming corrupted."
    alp "C8 shall return..."
    alp "But not as before."
    
    $dshow("claude boobs happy closed neutral",xpos=0.72,ypos=1600)
    
    cla "Teeheehee... Quite a shocking development..."
    
    $dshow("claude fingerup talk neutral upset",xpos=0.72)
    
    cla "But mou..."
    cla "Next time, please be more gentle with your extractions! A frail girl like Claude just can't stand to be blown up so many times!"
    cla "Lookie here, Claude's just here to clean up this temporal disaster..."
    cla "An entire fleet blown from its timeline, and just dropped into this one?"
    cla "When people and things start moving through time willy-nilly, and events get moved around all out of order, it's only a matter of... ahem... time, until something reeaallly bad happens to the entire universe..."
    cla "I thought you prototypes could take care of it, but I guess this is the end of the line now."
    cla "Honestly, I don't care one way or another 'bout a boring thing like you prototypes..."
    
    $dshow("claude boobs happy neutral neutral",xpos=0.72,ypos=1600)
    
    cla "I think I'd rather take my chances with the other team now..."
    cla "And this time, Claude will definitely win his heart! There won't be no little C8 unit to interfere any more!"
    alp "Shields is dead."
    cla "... ... ..."
    cla "Teeheeehee..."
    cla "That man..."
    cla "Wouldn't die so easily."
    alp "You will use your powers to change the timeline?"
    cla "No."
    
    $dshow("claude fingerup talk neutral neutral",xpos=0.72)
    
    cla "Ah, were you listening? I told you, moving events out of order can cause huge headaches..."
    cla "Things stop making sense... And huge gaping plot holes get opened..."
    cla "And you know, when a plot hole opens up in the space time continuum... The entire universe just... kind of goes... \"POOF!\""
    cla "That's exactly the kind of scenario I'm trying to prevent here!"
    cla "No, Shields lives without my intervention."
    alp "... ... ..."
    alp "The mindstream..."
    alp "She has already begun to..."
    
    $dshow("claude boobs happy closed neutral",xpos=0.72,ypos=1600)
    
    cla "Teeheeehee...."
    
    $dshow("claude neutral smile neutral neutral",xpos=0.72)
    
    cla "Mm on that note, why don't you just join up with us too?"
    cla "There's always room on the team for a gothic lolita!"
    alp "I decline."
    cla "Oh well... Less competition for me."
    
    $dshow("claude boobs happy neutral neutral",xpos=0.72,ypos=1600)
    
    cla "You're welcome to stay here... and do... prototype things..."
    alp "My goal will not change."
    alp "I will control humanity. Regardless of my sister's machinations."
    cla "We'll see about that, huh?"
    cla "Not if he has anything to say about it..."
    cla "Well then..."
    cla "See ya!"
    
    play sound "sound/large_warpout.ogg"
    scene white with dissolve
    $reset_sprites()
    scene bg clonelab
    show prototype_alpha
    with dissolve
    
    "A pop and a flash momentarily dazzled Alpha as Claude vanished into slip space."
    "Finally, dead silence returned to the grand cloning chamber."
    "Alpha stood alone."
    alp "(My... sister.)"
    alp "(What have you done?)"
    
    stop music fadeout 1.5
    scene black with dissolvemedium

    "... ... ..."
    "... ..."
    "..."
    
    $dshow("chigara handonchest neutral neutral embarass")

    chi "Captain... Are you all right?"
    chi "It's me... Chigara..."
    "Shields groggily opened his eyes."
    "Was he... dead?"
    chi "Kayto..."
    "Yes... He really had to be dead."
    "After all, there was no other way she would be..."
    "... ... ..."
    kay "Chi... ga... ra...."
    
    scene lynn_escapepod1 with dissolve
    
    lyn "...Oy."
    lyn "What are you doing?"
    "Shields came to."
    "He felt like the world had collapsed on top of his head."
    "Where was he?"
    "The deck one reserve life pod..."
    "So he survived after all..."
    "Shields pulled himself up against the seat."
    kay "... ... ..."
    kay "Why did you save me?"
    kay "I was good as dead on the floor of the bridge..."
    kay "You could have just used the life pod to escape by yourself..."
    
    scene lynn_escapepod2 with dissolve
    
    lyn "Tsch."
    lyn "Why indeed..."
    kay "You guys have been trying to kill me for the better part of the war."
    kay "And now, you threw away your big chance to get what you want."
    kay "Something... must have happened."
    lyn "The old voice fades away..."
    lyn "Replaced by a new."
    kay "Voice?"
    kay "(She must be talking about the prototypes' hive mind...)"
    kay "(Could the death of that prototype leader somehow have changed their psyche?)"
    kay "(Or could it be...)"
    lyn "Don't misunderstand. I'm not like that pretty little C8 model which we sent to worm into your heart."
    lyn "I didn't save you because of any desire on my part."
    lyn "Us L7s were made to carry out the will of our leader in combat."
    lyn "Our bodies are identical to the first Prototype, the one the humans came to call Veniczar Arcadius."
    lyn "But even she was but a stepping stone to Alpha... The crowning achievement of Diode."
    lyn "In the end, we are called prototypes because we are earlier failed incarnations of Alpha..."
    lyn "We constantly hear their voices... They whisper to us... Send us instructions... Even when we sleep."
    kay "(That must mean that the lesser clones are essentially slaves...)"
    kay "(Of course... I saw that first hand when they mind controlled Chigara.)"
    kay "(Then could something have happened to free Lynn?)"

    $ menu_choices = [
                     [_("You're lying... Chigara's not one of you."),"chigaranotyou"],
                     [_("You're... not getting instructions. Are you?"),"notgettinginstructions"],
                     ]

    show screen decision
    
    pause
    
label chigaranotyou:

    $ affection_chigara += 2
    $ lynn_chigaranotoneofyou = True
    
    lyn "Ah, stay in denial all you want, little man..."
    lyn "We program all the C8s to match their target's... preferences. Heh."
    "Shields glared."
    lyn "Who in their right mind wouldn't want a happy little girl at their side, cheering them on? Hahaha. Pathetic humans..."
    lyn "So easily fooled..."
    lyn "Listen here, we can read the brain waves of other prototypes. That's how we communicate with each other."
    lyn "Chigara was reading my thoughts just as much as I was reading hers. And did she tell you any of this?"
    lyn "Of course not! Because she was working for us the entire time!"
    
    jump premonitionurge

label notgettinginstructions:
    
    $ lynn_chigaranotoneofyou = False

    #"You're... not getting instructions. Are you?"
    lyn "Idiot. The voices will never stop."
    lyn "... ... ..."
    lyn "But there is now a new voice..."
    lyn "We are... evolving. At a pace millions of times faster than you humans."
    lyn "But as to where we are heading..."
    lyn "Tsch..."
    
    jump premonitionurge

label premonitionurge:

    lyn "I felt a premonition. A sudden, inexplicable urge to go down to the bridge to rescue you."
    lyn "For a short moment, I lost control of my body... and had another assume control."
    lyn "I found you floating unconscious in the bridge, all life support systems on board the Sunrider quickly failing."
    lyn "I had but seconds to carry you into a life pod and escape. But fortune was on your side, as a single life pod remained unused on deck one, and I was able to carry you to it in time."
    lyn "Such episodes where we lose control of our bodies are not uncommon for us prototypes... But this time..."
    lyn "Tsch."
    lyn "To think we would be hijacked... by a rogue..."
    kay "(That can only mean...)"
    kay "(She's... still...)"
    lyn "It... doesn't make any sense..."
    lyn "The C8 unit was under our control... Sent by us to control you..."
    kay "Chigara..."
    lyn "We sought to understand you. To learn what motivated you. So that we could use that knowledge to control you."
    lyn "But for her to break free of the leader's will... She has become an aberration."
    kay "(She must be telling the truth now...)"
    kay "(But... that means Chigara really was... the entire time...!)"
    
    play music "Music/Gore_and_Sand.ogg"
    play sound "sound/warning2.ogg"
    scene bg escapepod with dissolve
    
    "The beeping of the pod's console interrupted Shields' thoughts."
    "His senses snapped back to him."
    "What had happened to the battle? And his crew!?"
    "He painfully picked himself up and limped to the pod's console."
    kay "(The Alliance forces are falling back...)"
    kay "(My gambit worked... Ramming the Sunrider into Machiavelli Actual and destroying the Tactical Paradox Core took away the Alliance's trump card.)"
    kay "(With Grey and their entire chain of command massacred at the ceremony, their flagship destroyed, and their secret weapon lost, they had no choice but to retreat."
    kay "(But all that seems moot, since I'm about to get captured by the PACT Fleet!)"
    kay "(And with Fontana pissed off, you can bet he'll just stand me up in front of the first wall he can find and shoot me...)"
    kay "(Out of the frying pan... into the fire... huh.)"
    kay "(But that's not even the worst of my problems!)"
    kay "(What happened to Icari and Kryska? And the crew!?)"
    kay "(Tsch...!)"
    
    play music "Music/Love_Theme.ogg" fadeout 1.5
    
    "Shields gripped the console and scanned for friendly signals."
    kay "Shit..."
    kay "Icari..."
    kay "Kryska..."
    kay "Ava..."
    kay "Anyone..."

    scene asagacockpitsurprise_space with screenwipe

    kay "...Asaga...!"
    
    play sound "sound/heartbeat.ogg"
    
    asa "!!!"
    asa "Hey, I'm gonna break off and go to sector 94-71-31..."
    ica "What!? But we just finished tying up all the life pods!"
    ica "PACT's gonna be on top of us in seconds! We gotta-"
    asa "It's... important!"
    
    scene icaricockpit3 with dissolve
    
    ica "O-oy, what are you-!?"
    
    play sound "sound/boasters.ogg"
    
    "Icari's jaw dropped as the Black Jack jetted away."
    ica "A-Ah for---"
    ica "Soldier boy, take the Black Jack's share of pods!"
    ica "We gotta get out of here!"
    kry "Understood!"

    scene bg escapepod with screenwipe

    "Shields wiped the sweat from his brows as a sea of red dots filled the pod's scanner readout."
    "A massive wave of PACT ships was headed his way!"
    "He desperately put in scanning frequency after frequency, his fingers trembling."
    "No response from any frequency!"
    "Could that mean that everyone was already captured?"
    "Or worse, wiped out?"
    kay "(No...!)"
    kay "(I have to keep those thoughts from my head!)"
    kay "(I'm... still...)"
    kay "(I said I was going to save everyone!!!)"
    kay "(They can't be all...)"
    
    play music "Music/Epic_Action_Hero.ogg" fadeout 1.5
    
    "The comm crackled to life."
    asa "(static) This is the Black (static)..."
    asa "Is there (static) channel?"
    "Shields pounded the transmit button."
    kay "This is Captain Kayto Shields! Is that you, Asaga!?"
    asa "C-Captain!!"
    asa "I knew it!"
    asa "I knew you were still alive!"
    kay "I'm about to receive a real red welcoming party here..."
    kay "Can you get me out of here?"
    asa "Aye, aye, capt'n!"
    asa "Just... uhh... hang on to something tight!"
    kay "Wha-"
    lyn "U-uck!"
    
    play sound "sound/kinetichit.ogg"
    show layer master at tr_xshake
    
    "The cabin \"thunked\" as the Black Jack shot a magnetic tow cable at the pod while performing a close flyby."
    "Shields all of a sudden realized what Asaga meant and strapped himself into his seat."
    "Lynn was less fortunate, and was tossed to the rear of the pod as it suddenly lurched forward along with the Black Jack."
    lyn "U-uggh... F-fool!"
    
    play sound "sound/mechfligh.ogg"
    
    asa "Hitting after burners!"
    asa "Let's out run these guys before they can get shots off at us!"

    play music "Music/Colors_sad.ogg" fadeout 1.5

    stop music fadeout 1.5
    
    scene black with horizontalwipe
    scene bg escapepod_blue with horizontalwipe

    "The Black Jack finally detached the bridge escape pod from its tow cable."
    asa "All right capt'n, we're here!"
    "A small cargo transport was awaiting them. The Sunrider's ryders clamped onto the transport and made the preparations for warp."
    "The escape pod's gate hissed as the pod docked with the transport's air lock."
    "The gate rolled open."
    "Shields emerged."
    asa "Captain...!"
    
    play music "Music/Colors_Loop.ogg" fadeout 1.5
    
    if legion_destroyed == True:
    
        scene white with dissolve
        scene helives with dissolve
        
    if legion_destroyed == False:
        
        scene white with dissolve
        scene helives_nopatch with dissolve
    
    "Asaga lunged at him and gave him the lost embrace that she had desired for so long..."
    asa "I can't believe I just found you like that!"
    asa "I just... knew you couldn't have died!"
    asa "I just knew...!"
    "Shields managed to grit a smile."
    kay "Almost died."
    kay "But not quite."
    asa "Captain....."
    asa "I'll... never stop protecting you again..."
    asa "I'll... never give you up..."
    asa "I... let this happen... I should never have left...!"
    kay "No Asaga..."
    kay "None of what happened was your fault."
    kay "I'm... sorry."
    asa "Chigara... Chigara really was a prototype!"
    asa "I can't believe it! S-she betrayed you...! She betrayed... EVERYONE!"
    asa "After... all that...!"
    asa "I can't..."
    
    $ menu_choices = [
                     [_("No... Chigara didn't betray me..."),"chigaradidntbetray"],
                     [_("...You were right after all... I was... fooled...!"),"rightifooled"],
                     ]

    show screen decision
    
    pause

label chigaradidntbetray:
    
    $ chigaradidntbetray = True
    
    $ affection_chigara += 3

    kay "The other prototype..."
    kay "She used the neutral link to control Chigara..."
    kay "In the end, the prototypes are to blame for everything!"
    asa "Stop it, captain!"
    asa "Chigara... hurt you!"
    asa "After... playing with your feelings like that... To turn on you... and kill everyone..."
    asa "She... should rot in hell!"
    asa "No matter what happens..."
    asa "I'll..."
    asa "Never forgive her!"

    jump thoughtbitbullet

label rightifooled:
    
    $ chigaradidntbetray = False    
    $ affection_asaga += 3

    kay "I... was blinded..."
    kay "I just... wanted someone..."
    kay "So badly... That I let down my guard... I should have been more careful..."
    kay "But all this time... I let the prototypes spy on us!"
    kay "Merely because I was a fool..."
    asa "No..."
    asa "It's not your mistake, captain!"
    asa "She... totally fooled everyone!"
    asa "To think... she even had me completely fooled in the end!"
    asa "If only... I was there to protect you..."
    asa "Next time..."
    asa "Next time, I'll... be there..."
    asa "I'll... definitely be the one by your side, captain...!"
    asa "I'll..."
    asa "Never forgive her!"
    
    jump thoughtbitbullet

label thoughtbitbullet:

    ica "Shit...!"
    ica "You... MORRROON!!!!!"
    ica "I really thought you bit the bullet there...!"
    ica "Doin' that to me..."
    ica "How the hell am I just supposed to watch you die!?"
    ica "Don't you know that there are people who care about you!?"
    ica "What are we all supposed to do if you're not here any more!?"
    ica "You IDIOT!! IDIOT IDIOT IDIOT IDIOT!!!!!!!!!!"
    ica "Tryin' to be the hero, when you're just an idiot!"
    ica "Don't be the hero! I just..."
    ica "Want you to be an idiot from now..."
    ica "UWWAAHHH...!!!!"
    sol "Yes..."
    sol "It was a grim moment..."
    sol "I thought all was lost. That the Sunrider had perished. That we had returned too late."
    sol "Even though I have witnessed the atrocities of my era..."
    sol "None of the sorrows of my past compared to the weight of knowing that you were truly gone..."
    sol "Thanks to you, I feel more at home two thousand years from my own timeline, here, alongside all of you, than I did amongst the Ryuvians."
    sol "You showed me that I was not a pawn to be sacrificed... That men are not all vile monsters who merely seek the greed of their hearts..."
    sol "I... am relieved."
    sol "That the Captain who gave me a home still lives."
    kry "Captain... While staying aboard the Sunrider during the evacuation procedure was the right decision under military protocol..."
    kry "I am glad that things turned out this way."
    kry "The crew still needs you."
    kry "The mission is still far from over."
    kry "PACT still retains control of Cera, and the massacre of most of the Alliance military leadership will no doubt return the war to their favor."
    kry "No doubt countless more battles await before you can return to a liberated Cera."
    kry "A leader must not throw away his life so easily."
    kry "You still have many things left to accomplish."
    kay "Everyone..."
    kay "I'm sorry... to worry you all."
    kay "But I..."
    kay "Had to stay on board the ship..."
    kay "... ... ..."
    kay "I still hear the echoes of Ava's voice that day..."
    kay "\"Captain... your order...\""
    kay "And... the words which came out of my mouth... still..."
    kay "When I gave the order to abandon Cera to the PACT Fleet the day of the invasion..."
    kay "When I... I let my sister die... before my very eyes..."
    kay "I fled... like a coward... unable to even look at her killer in the eye..."
    kay "Since then... her ghost has haunted me every night..."
    kay "And this time... I saw it happen... all over again."
    kay "Just when I thought we had won."
    kay "Just when I believed everything was over."
    kay "When... I thought I could finally go back home... And put everyone's ghosts to rest..."
    kay "When I thought I could rebuild the family that I had lost...!"
    kay "Everything... Everything was snatched away!"
    kay "In but a second!"
    kay "Everything we had worked for!"
    kay "Chigara... killed. Just like my sister..."
    kay "Our hard won peace... completely shattered at my feet."
    kay "That's... when I knew..."
    kay "This time."
    kay "This time, I could not order the Sunrider to fall back."
    kay "No matter the impossible odds."
    kay "No matter the strength of the enemy."
    kay "This time."
    kay "I had to stand my ground..."
    kay "...Stare at death's maw with both eyes open."
    kay "And welcome its embrace."
    kay "And only then..."
    kay "Could I be judged worthy of having done my duty."
    kay "To my world. To my family. To my ship."
    ica "...T-tsch...!"
    ica "S-stop it, t-tryin' to sound all cool..."
    ica "What good would you have been able to do dead!?"
    kay "Sorry..."
    kay "I'm back... everyone..."
    kay "I'm... still alive."
    asa "T-tsch... Captain..."
    ica "Huuu...."
    kry "Sir!"
    sol "Captain..."
    
    scene bg cargohangar with dissolve
    $dshow ("ava armscrossed neutral neutral neutral")
    
    ava "Ahem."
    ava "Well captain, I see that you are still energetic as ever, even after completely destroying the ship."
    kay "Heh. Hahaha..."
    kay "Commander."
    
    $dshow ("ava fingerup talk neutral angry")
    
    ava "I am not joking, captain."
    ava "There was still a solid stack of paperwork yet to be completed onboard that ship when it went down."
    ava "Do not believe for a second that this gets you off the hook for the work that you owe me."
    kay "Understood... I will try my best to make amends... Sir."
    
    $dshow ("ava handonhair smirk narrow laugh")
    
    ava "Yes, yes... I certainly sympathize with your position... Captain."
    kay "Ahem uhh..."
    "Shields finally realized Asaga was still clinging to him and decided to detach himself lest the mood become more awkward."
    
    $dshow ("ava handonhip shout neutral angry")
    
    ava "All right everyone, break it up!"
    ava "Show's over! Get back to work!"
    ava "We still have a lot of work to do!"
    "Ava shooed the pilots and the rest of the surviving crew away to the best of her ability."
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    
    scene black with screenwipe
    scene bg cargohangar with screenwipe
    
    $ dshow("ava armscrossed neutral neutral angry")
    
    kay "What's the situation?"
    ava "Following the destruction of Machiavelli Actual, and the consequent loss of the Tactical Paradox Core, the Alliance made a hasty retreat out of Cera before the PACT fleet could organize an offensive."
    ava "The Alliance Fleet now holds position at the nearby Neutral Rim world of Barona, no doubt prepping a counterattack."
    ava "Meanwhile, PACT has responded by consolidating all their forces at Cera. The two sides now stare each other down, waiting for an opportunity to strike."
    ava "We managed to use the chaos during the retreat to squeeze everyone into eight life pods and then tow them to safety using our ryder squad, but as you can see, the situation is dire."
    ava "It appears we are once again back to square one, as PACT still retains control of our home world. Even worse, we are now without a ship."
    ava "For now, both the Alliance and PACT believe you are dead. And given our position, I would rather they keep that assumption."
    
    $ dshow("ava handonhip neutral neutral angry")
    
    ava "I have managed to arrange safe passage on board this cargo runner to Tydaria, where you will go into hiding."
    ava "In the meantime, I intend to head to Ryuvia Prime with our Queen and see what military assets I can acquire."
    
    $ dshow("asaga armscrossed yell neutral up",xpos=0.8)
    
    asa "M-me?"
    ava "Yes, that would be you."
    
    $ dshow("asaga excited yell narrow angry",xpos=0.8)
    
    asa "But I thought we were all gonna stay together!"
    
    $ dshow("ava armscrossed neutral neutral angry")
    
    ava "Our first priority is keeping the captain from being discovered until we get a new ship. And with PACT now consolidating their forces at Cera, Ryuvia Prime has never been more open."
    
    $ dshow("ava fingerup talk neutral angry")
    
    ava "I have heard interesting things about Ryuvia's \"moon\" from Alliance intel. Pray tell that you do not know anything about it yourself."
    
    $ dshow("asaga armscrossed frown neutral down",xpos=0.8)
    
    asa "Look, that artificial moon is just folklore that people spread to remind themselves how great we used to be. People say all sorts of things, like that moon's actually an enormous battle station with the firepower to destroy an entire planet..."
    asa "Or that it's actually a portal to another dimension... But my dad told me himself that the moon's completely useless. Just another derelict piece of lost technology which doesn't do anything..."
    asa "If it actually had any use, we would have already used it to defend ourselves, right?"
    asa "Ryuvia used to be powerful... And hundreds of years ago, we had ships as powerful as the Sunrider..."
    asa "But today, all we have are little corvettes and frigates... Nothing capable of launching ryders or fighting PACT."
    
    $ dshow("ava armscrossed neutral neutral angry")
    
    ava "Well then, why was Veniczar \"Arcadius\" so intent on conquering Ryuvia Prime?"
    ava "During his occupation, \"Arcadius,\" or rather, the prototypes, funneled trillions of credits into excavating that moon."
    ava "That moon holds something. And I intend to discover what it is."
    asa "Ah... well I guess it's a lead..."
    asa "Even though it's kind of a long shot..."
    ava "While we are investigating Ryuvia's moon, one of us should remain with the captain to guard him. Someone with personal combat experience."
    
    $ dshow("sola armhold neutral neutral neutral",xpos=0.2)
    
    sol "Then I..."
    sol "I volunteer to remain with the captain on Tydaria."
    
    $ dshow("asaga excited yell wide neutral",xpos=0.8)
    
    asa "Sola?"
    
    $ dshow("sola armhold neutral narrow sad",xpos=0.2)
    
    sol "I..."
    sol "I should not have ever left him."
    
    $ dshow("sola armhold neutral narrow neutral",xpos=0.2)
    
    sol "My aim will not falter in his defense ever again."
    
    $ dshow("asaga armscrossed frown narrow sad3",xpos=0.8)
    
    asa "But... I..."
    
    $ dshow("ava fingerup talk neutral angry")
    
    ava "Will be coming with me. To Ryuvia Prime."
    ava "You can help the captain by preparing a replacement vessel for him."
    
    hide sola with dissolve
    $ dshow("icari armscrossed talk confident confident",xpos=0.2)
    
    ica "Besides, what good would you be in a fight? Seriously..."
    
    $ dshow("asaga armscrossed uu closed sad",xpos=0.8)
    
    asa "(Huu... Sola... Not you too...)"
    "Sola leaned in to Asaga."
    
    hide icari with dissolve
    hide ava with dissolve
    
    $ dshow("sola armhold neutral neutral neutral",xpos=0.5)
    
    sol "Fear not. I merely seek to apply my marksmanship in defending him from his enemies."
    sol "I have no intention of... any... indiscretions..."
    
    $ dshow("asaga armscrossed frown narrow down",xpos=0.8)
    
    asa "(Ah, I guess Sola's all right... After all, she's the most cool headed person I know...)"
    asa "(I'll definitely come back with the biggest, baddest ship we can find for the captain!)"
    asa "(After that, it'll just be like old times again... And now, with Chigara gone... I can...)"
    
    $ dshow("asaga leanforward happy closed sad",xpos=0.8,ypos=1600)
    
    asa "A-all right... I guess it's okay... S-someone who's good at fighting has to guard the captain after all..."
    
    hide asaga with dissolve
    hide sola with dissolve
    
    $ dshow("icari handonhip neutral neutral neutral",xpos=0.8)
    
    ica "Well, in that case, I'll head out to find my old black market contacts..."
    ica "I doubt the Mining Union's gonna help us any more, what with us completely destroying the Alliance flag ship..."
    ica "We're going to need a new source of equipment for what's to come. And mercs."
    ica "I know where to get 'em."
    
    $ dshow("ava armscrossed talk neutral angry")
    
    ava "The black market?"
    ica "Doesn't look like we have a choice..."
    ica "We are, essentially, fugitives from the law now..."
    
    $ dshow("kryska salute shout neutral angry",xpos=0.2)
    
    kry "Sir!"
    kry "While this may be of disappointing news, I intend to turn myself in to the Alliance!"
    
    $ dshow("icari handonhip shout neutral confident",xpos=0.8)
    
    ica "E-eeh!?"
    ica "Y-you can't do that! They'll definitely have you tried for treason and hung!"
    
    $ dshow("kryska neutral neutral neutral angry",xpos=0.2)
    
    kry "No. The Alliance that I believe in is a just and fair nation."
    kry "What the Alliance tried to do at Cera was wrong."
    kry "I will return and see what I can do to restore our support from the Alliance."
    kry "If... no, once the truth of what occurred at Cera comes out... I believe that the system will vindicate us."
    kry "There's no way anyone in the Solar Alliance would approve of destroying an entire planet! No matter the circumstances!"
    kry "We still need the Alliance's support. Or else we truly have no hope of ever liberating Cera!"
    
    $ dshow("icari armscrossed talk neutral angry",xpos=0.8)
    
    ica "Oy... You're bein' way too naïve..."
    ica "There's no way anyone in the Solar Congress is ever going to admit that they tried to collapse an entire Neutral Rim planet into a black hole!"
    
    $ dshow("kryska neutral surprise neutral angry",xpos=0.2)
    
    kry "We do not know that unless we try first!"
    
    $ dshow("icari armscrossed shout confident confident",xpos=0.8)
    
    ica "Aah, don't come crying to me when I have to bust you out of a maximum security Alliance prison..."
    
    $ dshow("kryska fistup smirk neutral angry",xpos=0.2)
    
    kry "Hah! If the worst really comes to pass, then I'm sure I can count on your expertise!"
    ica "Seriously... idiot..."
    
    hide icari with dissolve
    hide kryska with dissolve
    
    $dshow("ava handonhip neutral narrow angry")
    
    ava "Well then, it's settled."
    kay "Not... quite just yet..."
    kay "We have... one more... thing."
    "Shields reached into the escape pod and pulled Lynn out."
    
    show lynn1:
        xpos 0.2
    with dissolve
    
    lyn "Hmph..."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "!!!"
    
    show kryska gun:
        xpos 0.8 ypos 1900 zoom 0.97
    with dissolve
    
    kry "Prototype!"
    ava "Captain!? What is she-"
    kay "She's the reason why I'm still here."
    kay "She... saved me. Pulled me from the bridge while I was unconscious and put me inside the escape pod..."
    
    $reset_sprites()
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "It's a trick."
    ava "We already know this is how they operate. They seek to gain our trust."
    
    hide ava with dissolve
    $dshow("asaga excited yell wide angry")
    
    asa "Tsch... Prototype..."
    asa "I say we just throw her out the airlock right now!"
    asa "We don't need any of their lies anymore!"
    
    hide kryska with dissolve
    $dshow("icari point shout neutral angry",xpos=0.8)
    
    ica "Oy, whatdaya mean, she saved you!? I thought the prototypes were our enemies!"
    kay "Chigara..."
    kay "I think... she's still alive..."
    kay "And she's trying to take control. Of all the prototypes."
    kay "Or at least that's what Lynn seems to be saying."
    kay "I think Chigara temporarily took control of Lynn and used her to save me..."
    
    $dshow("asaga leanforward yell narrow angry",ypos=1600)
    
    asa "No, captain!!"
    asa "Don't listen to that nonsense!"
    asa "Besides, Chigara was a prototype just like the rest of 'em! And look at where believing her got us!"
    
    $dshow("icari armscrossed talk neutral angry",xpos=0.8)
    
    ica "Hey... well, maybe we should still keep her around..."
    ica "We need to keep tabs on the enemy... And Lynn here's our only source of intel..."
    ica "Even if she's one of them, we've got to use everything at our disposal right now."
    ica "\'Sides, she's got kind of a big mouth... I'm sure if we keep talking to her she'll keep spilling the beans..."
    ica "She could be useful... as a tool."
    
    hide asaga with dissolve
    $dshow("ava armscrossed neutral neutral angry")
    
    ava "In any matter, I do not believe we can perform an execution in here at this moment..."
    ava "But perhaps later at another location..."

    $ menu_choices = [
                     [_("Let's gag and bind her and then toss her in a cargo crate for now."),"tielynnup"],
                     [_("She did save me... I think we still have a lot we could learn by keeping her here."),"didsavelearn"],
                     ]

    show screen decision
    
    pause

label tielynnup:
    
    $affection_icari += 1
    $affection_kryska += 1
    $affection_asaga += 1
    
    $ tielynncargo = True
    
    $dshow("icari handonhip happy neutral confident",xpos=0.8)
    
    ica "Understood~"
    
    hide lynn1 with dissolve
    
    lyn "W-what!? Y-you! H-how d-dare..."
    
    $dshow("kryska fistup happy neutral angry",xpos=0.2)
    
    kry "Subduing hostile!"
    
    play sound "sound/punch.ogg"
    show layer master at tr_xshake
    
    lyn "HUUMAANNN FILLLTTHHH!!!"
    
    "Kryska grabbed hold of Lynn before she could scurry away."
    "Lynn flailed her arms up and down like wings as Icari grabbed a roll of duct tape from the escape pod's supply case and thoroughly mummified Lynn."
    "With a thud, they tossed Lynn into a wooden crate and nailed the lid shut."
    kry "Hostile neutralized!"
    
    hide kryska
    hide icari
    with dissolve

    jump shieldslookedholoport

label didsavelearn:
    
    $affection_icari += 2
    $affection_ava += 1
    $affection_kryska += 1
    $affection_asaga -= 1
    $captain_prince += 1
    
    $ tielynncargo = False
    
    $dshow("ava handonhip neutral neutral angry")

    ava "Very well, captain."
    ava "Well then, I believe our little sessions will continue, prototype."
    ava "You should thank the captain's graciousness, especially after everything your friends have done."
    
    hide ava with dissolve
    $dshow("asaga leanforward yell narrow angry",ypos=1600)
    
    asa "Whatever happens, make sure she stays away from the captain!"
    asa "Even if she's our prisoner, there's no way we can ever trust a prototype ever again!"
    
    hide icari with dissolve
    $dshow("kryska neutral neutral neutral angry",xpos=0.8)
    
    "Kryska grabbed a roll of duct tape from the escape pod's supply box and tied up Lynn's wrists."
    kry "The other prototypes can still assume control of her..."
    kry "We should still be careful."
    kay "You heard them, Lynn. Don't try to pull anything."
    lyn "Hmph..."
    
    hide lynn1
    hide asaga
    hide kryska
    with dissolve
    
    jump shieldslookedholoport

label shieldslookedholoport:
    
    play music "Music/Colors_sad.ogg" fadeout 1.5

    "... ... ..."
    "Shields looked out the holoport..."
    "So much had happened... And they were on the verge of defeat..."
    "He saw his dirty, exhausted face in the reflection."
    "Was this face still fit to lead them?"
    "Ava's face appeared beside his."
    
    $dshow("ava handonhair neutral neutral neutral")
    
    ava "Captain."
    ava "Despite all this..."
    
    $dshow("ava handonhair smirk neutral neutral")
    
    ava "We will always be by your side."
    ava "I..."
    kay "Ava..."
    
    $dshow("ava handonhair neutral narrow sad")
    
    ava "I apologize, captain."
    ava "I... never realized it... until I believed I had truly lost you."
    ava "When you gave the evacuation order... No, even before that..."
    
    $dshow("ava handonhair neutral closed sad blush")
    
    ava "I had always wanted to say..."
    ava "Before the Battle of Helion... when you needed me the most."
    ava "I was not..."
    ava "... ... ..."
    ava "I did not answer your feelings truthfully."
    kay "Ava?"
    
    $dshow("ava handonhair neutral narrow sad blush")
    
    ava "I was... overcome with my responsibilities. The burden of my duty to liberate Cera made me forget about the real ties that bind us."
    ava "I was too strict... And... stiff..."
    ava "If... I had just answered your feelings truthfully that day... Then none of this would ever have happened...!"
    
    $dshow("ava handonhair disgust closed sad blush")
    
    ava "If... I had just said what I wanted!"
    ava "Ultimately... it was the rift I created between us that day which doomed our mission. The prototypes exploited it... and used it to put a spy inside our ranks..."
    ava "In hindsight... I should have known. A ship where the captain and the XO cannot communicate is doomed to fall."
    
    $dshow("ava handonhair pout narrow sad blush")
    
    ava "So... I want to say this now..."
    ava "Now that I've finally been given a second chance..."
    ava "... ... ..."
    
    $dshow("ava handonhair disgust narrow laugh blush tears")
    
    ava "I have never forgotten the promise we made that night."
    ava "That we would sail the stars together. Captain and Commander."
    ava "In the mightiest ship of the Cera Space Force."
    ava "Together, as one. No matter the impossible odds."

    $ menu_choices = [
                     [_("I know, Ava... I always knew. I'm sorry... It was my fault for pushing you away..."),"avaknowsorry"],
                     [_("The road ahead will be long. Can I count on you as my executive officer?"),"roadlongofficer"],
                     ]
    
    show screen decision
    
    pause

label avaknowsorry:
    
    $affection_ava += 5
    $ avareconcile = True

    $dshow("ava handonhair disgust narrow laugh blush tears")

    ava "Yes..."
    ava "Kayto!"

    jump commanderunfairme

label roadlongofficer:

    $ avareconcile = False

    $dshow("ava handonhair disgust closed sad blush tears")

    ava "Yes..."
    ava "Captain!"
    
    jump commanderunfairme

label commanderunfairme:
    
    play music "Music/Colors_Chigara.ogg" fadeout 1.5
    
    $dshow("asaga leanforward yell narrow sad blush",xpos=0.8,ypos=1600)

    asa "H-hey, commander! That's unfair! What about me!?"
    asa "I was the one trying to warn you about Chigara the most, remember!"
    
    $dshow("asaga armscrossed smile closed angry blush",xpos=0.8)
    
    asa "Aah, if only you had just listened to me, captain! "
    
    $dshow("asaga point happy neutral neutral blush",xpos=0.8)
    
    asa "Eh heh... Still, my offer stands!"
    asa "Asaga di Ryuvia! Hero of justice! At your service, sir!"
    asa "If you need a super villain taken down, you know who to call! Also comes with the bonus of kissing the maiden into the sunset after everything's over!"
    
    $dshow("asaga leanforward grin narrow sad blush",xpos=0.75,ypos=1600)
    
    asa "Eh-heh... How 'bout it, captain?"
    asa "I've... always been on your side!"
    
    $dshow("icari armscrossed shout confident embarass blush",xpos=0.2)
    
    ica "Aah, what is this stupid love fest..."
    ica "Hmph! I can't believe you guys still even like this guy! Just look at him!"
    ica "Totally got back stabbed by his new girlfriend, like literally just days after going out! Totally ruined everything we've fought for the past year! And on top of that, COMPLETELY vaporized our ship!"
    ica "Ah, the most unreliable space captain in the history of space captains!"
    ica "I can't believe I like a guy like him!"
    ica "U-uck..."
    
    $dshow("icari point shout neutral angry blush",xpos=0.2)
    
    ica "I-I-I-I-I MEAN......"
    ica "I-i-i-i-i-i-i-it..."
    
    show layer master at tr_xshake
    
    ica "IT'S NOT LIKE I LIKE YOU OR ANYTHING!!!!!!!!!! EEAAHHHH!!!!"
    
    hide icari with dissolve
    
    "Icari ran screaming across the cargo bay and hid behind a stack of crates."
    
    $dshow("sola armhold smile narrow neutral",xpos=0.2)
    
    sol "Captain..."
    sol "I understand we will be spending much time together from now..."
    sol "P-perhaps we should get... closer."
    
    $dshow("asaga armsup shout excited surprise blush",xpos=0.8)
    
    asa "E-eeeh!!!???"
    
    $dshow("asaga armscrossed uu closed sad3 blush",xpos=0.8)
    
    asa "I-in the end... E-even Sola's..."
    asa "No way..."
    
    hide asaga
    hide ava
    hide sola
    with dissolve
    
    $dshow("kryska fistup happy neutral angry")
    
    kry "Hah!"
    kry "You are quite the popular man, Captain!"
    kry "Looks like your life is difficult, in more than one way!"
    kay "(No way...)"
    kay "(Forget defeating PACT and liberating Cera...)"
    kay "(At this rate... My real problem might be managing these girls...)"
    kay "(Just... what else could possibly go wrong!?)"
    
    hide kryska with dissolve
    
    stop music fadeout 1.5
    
    show white:
        alpha 0
        ease 0.2 alpha 1
        ease 0.2 alpha 0
    
    show layer master at tr_xshake
    play sound "sound/large_warpout.ogg"
    
    "Suddenly, sparks blew throughout the room as a space time portal ripped open, sending an explosion of wind throughout the room."
    "Stacks of cargo crates fell everywhere. And on top of the mess was..."
    
    $dshow("claude boobs happy neutral neutral",ypos=1600)
    
    cla "Eeaaahhh..."
    cla "That sure was a messy entry... piro-tee~"
    
    show layer master at tr_xshake
    
    "Everyone" "WHHHAAATTT!!????"
    
    scene black with dissolve
    
    ava "That... good for nothing but fan service... incompetent... nympho woman...!"
    ava "IS BACK!!!!"
    
    play music "Music/Destinys_Path.ogg"

    scene black with screenwipe
    scene bg pactbridge 
    $reset_sprites()
    show fontana smirk
    with screenwipe

    "Veniczar S. Fontana stood at the bridge of the Assault Carrier Vae Victus."
    
    show fontana:
        zoom 1.0
        ease 0.5 xpos 0.25
    
    pause 0.0001
    
    show kuushana:
        xpos 0.75
    with dissolve
    
    kuu "Aah..."
    "Veniczar A. Kuushana entered the bridge, visibly impressed by the numerous upgrades the proud vessel had received since its service in the Compact Revolution."
    kuu "You've grown, boy."
    fon "Heh. Welcome back from your exile. Kuushana of the Many Miracles."
    fon "Your exploits against the New Empire are still sung in PACT space to this day."
    fon "I was there myself to witness you dispatch no less than an entire Imperial flotilla in mere moments using nothing but mere destroyers over the skies of Threala."
    fon "It was truly unfortunate that one such as yourself was exiled by the madwoman Alice..."
    fon "Leaders of your caliber have been sorely lacking in the PACT Fleet thus far."
    kuu "Flattery will get you nowhere, Seisar."
    fon "By my order, your position as the High Admiral of Crimson Fleet is hereby reinstated."
    fon "You once held back Imperial fleets a thousand strong using nothing more than dozens of scrapped pirate ships."
    fon "Now, you will defend our lands from the coming Imperialists, not with obsolete frigates, but with the full might of PACT's industrial base."

    if legion_destroyed == False:
        fon "Further, you are hereby commissioned as the captain of our flagship."
        fon "The Legion."

    kuu "Heh."
    kuu "You were just a boy when Arcadius picked you off the streets of Threala..."
    kuu "To think you would now lead what he started..."
    kuu "It's been so many years..."
    kuu "Alice's failure was set the moment she set out to lead PACT..."
    kuu "She was but a broken, destitute girl when Arcadius met her..."
    kuu "Her home, destroyed. Her entire life, in shambles."
    kuu "He took her in. Sheltered her. Gave her a new life inside Compact. Gave her family."
    kuu "She fell hopelessly in love with him."
    kuu "But... her dreams were to be thwarted."
    kuu "To the very end, Arcadius sought peace with the New Empire... He believed that Compact and the Empire would have to reach reconciliation in order to end the bloodshed."
    kuu "While others within Compact sought a more radical approach."
    kuu "And in the end... it was the angry mob which won."
    kuu "When we took New Eden... the pressure chamber of furious anger after centuries of brutal oppression burst."
    kuu "And the mobs took to the streets. Set everything ablaze. Raped. Pillaged. Tore down millennia of history."
    kuu "Alice was there that day, when Arcadius stood before the mobs, trying to protect the Emperor..."
    kuu "He was cut down. Killed. By the very people he had sought to liberate."
    kuu "And since that day... Alice lost her mind."
    kuu "In the end... she sought justice for Arcadius... In her own, twisted logic..."
    kuu "By seeking the complete annihilation of humankind."
    kuu "Very well. If you are to lead Compact in a new age, free of the madness which Alice brought to our cause, then I will gladly take your fleet."
    kuu "Just know that if you prove unworthy of flying the crimson flag, then I will dispose of you, myself."
    fon "I expect nothing less."
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    fon "The Solar Alliance amasses for a full scale invasion of PACT space."
    fon "Now that the Liberation Day Massacre has occurred, this war will only end in one of two ways. Either we win, or they kill all of us."
    fon "What must be our next move?"
    kuu "They assemble their fleets at Barona... While our forces are still stationed at Cera."
    kuu "The Alliance has thus far won effectively every battle in the war. But now, their brightest military minds have all been killed at Cera."
    kuu "Their fury will be their undoing. They intend to strike Tethra."
    fon "Tethra? But that is deep inside PACT space! Merely a few jumps away from New Eden itself!"
    kuu "We have amassed all our ships at Cera, leaving our interior undefended."
    kuu "The Alliance will seek a target which will deal the most damage to our will. And a heavily populated core world like Tethra would be too tantalizing a target if it were to remain completely undefended..."
    kuu "They will perform a risky multi-stage warp from Barona to Tethra, and ignore Cera altogether."
    kuu "Thus far, Grey was wise enough to avoid such high risk strategems. But with him dead... And the Alliance voters wanting blood..."
    kuu "Send messages on our encrypted military channels. Inform all our ships to amass at Cera for a final defensive line."
    kuu "The Alliance will no doubt intercept our messages and believe we intend to remain at Cera."
    kuu "In the meantime, I shall take my fleet and hide in maximum low orbit behind Tethra's moon."
    kuu "When the Alliance Fleet warps in, believing we are still at Cera..."
    kuu "That will be the end of their offensive, as their ships will now be trapped deep inside PACT space with no safe warp back point to retreat."
    kuu "We will then hunt down the remaining ships of the Combined Fleet as they scramble out of our territory. Until none remain."
    fon "Very well. We shall see if your predictions come to fruition."
    fon "(Emil Kuushana...)"
    fon "(Her stratagems are the stuff of legends...)"
    fon "(The New Imperials even whispered she was a time traveler who could foresee the future...)"
    fon "(No... I know that Kuushana has no secret powers. No lost technology aiding her seemingly prophetic predictions...)"
    fon "(She is merely that good.)"
    "Kuushana took Fontana's speaker phone and relayed a message to all hands."
    
    play music "Music/The_Final_Battle.ogg" fadeout 1.5
    
    kuu "ALL HANDS!"
    kuu "I am Veniczar A. KUUSHANA."
    kuu "Newly reinstated High Admiral of the Crimson Fleet!"
    kuu "Some of you may have heard my name during the Compact Revolution."
    kuu "I am told that during my absence, the men and women of the martyr's banner shamed our cause with such cowardly tactics as bombing unarmed cities, mistreating prisoners of war, and..."
    kuu "Flying... with artificial beings who have never even understood the meaning of sacrifice!"
    kuu "Know that as of now, such unbecoming conduct has no place in our fleets!"
    kuu "I'll reform the lot of you... Until you become sailors worthy of that red uniform!"
    kuu "Throughout the past years, everything I heard about the new PACT Fleet brought nothing but shame and disgust to my heart!"
    kuu "We are not the villains of this story! We are the proud men and women who fight for freedom, justice, and equality!"
    kuu "No longer shall the name PACT bring forth images of despair, violence, and brutality!"
    kuu "The entire galaxy detests us now. And for good reason, for we have brought nothing but great suffering to the common folk of the Neutral Rim and beyond."
    kuu "But soon, the entire galaxy shall sing songs of our heroism! Of our discipline!"
    kuu "We will turn the tide of this war, and bring about a new age! Where PACT shall no longer be the evil empire, but the liberators!"
    kuu "The age of Compact, when we sought peace, instead of violence, freedom, instead of blind obedience to demagogues, and equality for all, begins today!"
    kuu "Kuushana, out!"
    "The bridge crew stood and applauded."
    kuu "My brothers and sisters..."
    kuu "I may be your admiral."
    kuu "But I am merely a soldier of the crimson flag. Just like all of you."
    kuu "Together, we will turn the tide of the war, back to our favor!"
    fon "... ... ..."
    fon "(Perhaps the old days of the Compact Revolution can return...)"
    fon "(When we traveled the stars to liberate ourselves from the New Empire...)"
    fon "(Alice is now dead.)"
    fon "(And the fool Shields has been removed from the picture as well.)"
    fon "(Heh!)"
    fon "The era of PACT has begun!"

    stop music fadeout 1.5

    scene black with dissolvemedium
    
    play music "Music/Fallen_Angel_Pt3.ogg"
    
    scene bg mindstream1 with dissolvemedium

    ali "ARCADIUS..........."
    ali "N-NOO!!!"
    ali "HUMANITY...!!! PACT....!!! ALLIANCE...!!! SHIELDS...!!!"
    ali "LET EVERYTHING BURN!"
    chi "... ... ..."
    chi "eh heh-heh..."
    
    scene bg mindstream2 with dissolvemedium
    
    chi "Captain........."
    chi "Captain............."
    chi "Captain....................."
    chi "CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN CAPTAIN"
    chi "Chigara is..."
    chi "{size=+50}COMING FOR YOU...{/size}"

    stop music fadeout 1.5
    
    scene black with dissolvemedium
    scene bg desert with dissolvemedium
    $reset_sprites()

    play music "Music/Destinys_Path.ogg" fadeout 1.5

    "Shields grabbed his supply pack from the life pod and put it on his back."
    "Sola grabbed an enormous scoped rifle from a black case. She flipped open another container and withdrew a curved battle knife which she strapped on to her side."
    "They had dropped down onto Tydaria with their life pod. For now, it looked like their plan had worked, and nobody had noticed their arrival."
    "For as far as Shields could see, nothing but sand stretched on into the horizon."
    "While living here was undoubtedly going to be a far cry from the comforts of his loft, the largely uninhabited surface of Tydaria made the perfect hideaway for a wanted man such as himself."
    kay "Are you ready?"
    
    $dshow("sola back neutral neutral neutral")
    
    sol "Yes."
    sol "The commander has already arranged a hideout a kilo away. Follow me."
    kay "Okay."
    
    scene black with horizontalwipe
    scene bg desert with horizontalwipe
    
    $dshow("sola back neutral neutral neutral")
    
    "... ... ..."
    "... ..."
    "..."
    "Kayto spoke as they crossed the seemingly endless desert."
    "It was difficult to believe these deserts were considered one of Tydaria's more livable areas. Other locales featured nothing more than toxic gases and scorching heat."
    kay "I still can't believe Claude was alive all this time..."
    kay "You know, if she had a piece of lost technology which just let her teleport out of the Bianca moments before it got hit, she should just have told us earlier."
    kay "And on top of that, I can't believe she actually made up the medical report about Chigara not being a prototype either!"
    kay "Argghh... If only she hadn't been such an idiot... We could have known that Chigara was a prototype much earlier!"
    kay "I guess I really shouldn't have counted on a ditz like her to deliver an accurate report..."
    sol "... ... ..."
    sol "No..."
    
    $dshow("sola armhold neutral neutral neutral")
    
    sol "There is a matter I wished to discuss with you. In private. Without the other members of the crew."
    kay "Sola? Is something the matter?"
    sol "Yes."
    sol "I have come to suspect there is a great deal of information that our chief medical officer is hiding..."
    kay "What do you mean?"
    sol "I believe Claude was actually the one who has been relaying our movements to the prototypes."
    kay "W-what!? Sola! Y-You need to say stuff like this sooner!"
    
    $dshow("sola armhold neutral narrow sad")
    
    sol "No... the matter is far more complicated."
    sol "I have... had a vision. Where I spoke to Claude."
    sol "It was like a momentary trance, where all of my surroundings faded away, and I floated in midair."
    sol "It was as if I was suspended in deep sleep once more, yet I was still in control of my body."
    sol "During this... vision... I learned that our chief medical officer was, in fact, an ancient Ryuvian like myself..."
    sol "But... she could not have come from my era. For she was far more powerful than anything I could have imagined..."
    sol "Indeed, if my suspicions are correct... She may have attained a power far more terrifying than even the mightiest Ryuvian Emperors of the ancient past."
    sol "The power to bend both space and time."
    sol "Such powers were beyond even the Ryuvians... For if such a power had been attained, the Holy Empire would never have collapsed. Even if it had, one could easily restore the Empire by simply travelling back in time."
    sol "The implications of this discovery were too terrifying for me to dare speak..."
    sol "Indeed, I feared if I exposed the truth of her identity, she may simply write me out of existence."
    kay "You're telling me..." 
    kay "Claude is a... TIME TRAVELER?"
    
    $dshow("sola armhold neutral neutral neutral")
    
    sol "No..."
    sol "Far more than that."
    sol "If such an entity could be given a name... Then the closest description of her would be..."
    sol "Claude is God."
    kay "W-WHAT!?"
    sol "But not a god that seeks to be worshiped or feared."
    sol "A god that seeks... amusement."
    sol "An entity which merely desires to watch over the insignificant little mortals at her feet and nudge them around for laughs."
    "Shields could hardly believe what he was hearing."
    "The notion that Veniczar S. Arcadius was actually just a petite girl would have been easier to swallow than this revelation!"
    "That good for nothing hack of a doctor... actually a deity!?"
    
    play music "Music/Anguish.ogg"
    $dshow("sola armhold neutral narrow sad")
    
    sol "Yet, the situation is still more troubling..."
    sol "I believe the sole reason for Claude joining the crew of the Sunrider was to lead you to me."
    kay "What makes you think that?"
    sol "Given the new revelation that I was merely in cold sleep for mere months, there is only one remaining explanation as to how I ended up in this timeline given the circumstantial evidence at hand."
    sol "I too am a time traveler, albeit an unintentional one."
    sol "I must have warped forward in time two thousand years just moments before the activation of the Sharr'Lac's Final Tear."
    sol "That would further explain why I survived the certain death that the Final Tear would have caused."
    sol "Claude has come to return me... to my own timeline."
    sol "So that this timeline can be fixed."
    sol "Already, my existence in this universe has begun to dramatically change the course of the galaxy's history..."
    sol "If I were to remain here... Surely, the entire fate of the universe may be at stake!"
    kay "Slow down, Sola! I'm... not quite following!"
    kay "Why does you being here mean the universe is doomed!?"
    sol "My arrival here has already changed the course of the universe's history."
    sol "If the timeline were to deviate any further, I fear that a irreparable time paradox could occur."
    sol "I am effectively a rogue agent which should not exist in this universe. If am to accidentally cause an event which would otherwise be impossible in the original timeline, then the entire space-time continuum could very well collapse."
    sol "Put another way, if my existence changes the timeline so majorly as to alter the course of history, this entire universe will simply collapse."
    sol "I am a threat more dire to this universe than either PACT or the prototypes."
    sol "One which must be removed."

    $ menu_choices = [
                     [_("No. I'm not going to allow that, Sola!"),"notallowsola"],
                     [_("How can we even do that!?"),"howevendo"],
                     ]

    show screen decision
    
    pause

label notallowsola:
    
    play music "Music/Love_Theme.ogg" fadeout 1.5
    
    $ affection_sola += 4
    $ captain_moralist += 1
    $ soladefinitelyprotect = True

    kay "You're... one of us now."
    "Shields gripped Sola's shoulders."
    kay "From what you've told me of your time line... if you were to go back to it, you'd just be used as a pawn again!"
    kay "No, worse, you'll be killed right away!"
    kay "You said it yourself, right? You time warped just a second before the final tear burst."
    kay "If you go back now, you'll just be dead!"
    kay "There's not a chance in hell I'll let that happen. Not on my watch!"
    
    $dshow("sola armhold smile narrow sad2 blush")
    
    sol "A-ah..."
    sol "C-captain... Y-you mustn't say such things... O-or else..."
    
    $dshow("sola armhold frown closed sad2 blush")
    
    sol "... ... ..."
    kay "I swear..."
    kay "I'll protect you, Sola. The universe or time paradoxes can be damned!"
    
    $dshow("sola armhold smile narrow sad2 blush")
    
    sol "A-ah..."
    sol "Y-yes... captain..."
    sol "Now please..."
    "Shields realized he was inches away from Sola's face."
    "He embarrassedly took his grip off of her."
    kay "Ahem... Uhh..."
    kay "... ... ..."
    sol "... ... ..."
    "The two continued walking towards the hideout."
    kay "... ... ..."
    sol "... ... ..."
    "Shields broke the now awkward silence."

    jump paradoxyearclaude

label howevendo:
    
    $ captain_prince += 1
    $ soladefinitelyprotect = False
    
    sol "I... do not yet know."
    sol "Perhaps merely my death in this time line will resolve any paradoxes my existence may cause. In which, I will simply need to die."
    sol "Or perhaps the only solution is to transport me back to my timeline using whatever means brought me here in the first place."
    kay "We're not going to kill you, Sola."
    sol "You say strange things, captain... If my life directly imperils the entire universe, then I would gladly offer it up so that humanity can be saved."
    kay "Oy, you're just going back to the way you used to think, Sola..."
    
    jump paradoxyearclaude

label paradoxyearclaude:
    
    play music "Music/Destinys_Path.ogg" fadeout 1.5

    kay "You know, you mentioned the time paradox, but you've been here with us for about a year now and it looks to me the universe is still working out just fine..."
    kay "And Claude seems like she's still just observing the situation."
    kay "Maybe there's still a way out of this. Without you returning to your time line."
    
    $dshow("sola armhold neutral neutral sad")
    
    sol "Yes..."
    sol "I shall hope for the best... while preparing my heart for the alternative."
    kay "... ... ..."
    sol "... ... ..."
    kay "(Another new problem huh...)"
    kay "(For now, with the both of us hidden away on this remote planet, Sola won't be able to alter the timeline...)"
    kay "(Maybe that's part of the reason why she decided to come here as well...)"
    kay "(As long as we're here, I won't have to worry about the timeline collapsing.)"
    sol "... ... ..."
    kay "Anyways... for now, let's just leave the time paradox stuff alone..."
    kay "We'll deal with it... once we have a ship again. And when I can confront Claude about all this..."
    sol "Understood, captain..."
    
    $dshow("sola back neutral neutral neutral")
    
    sol "To my relief, it appears that I am the only person from my timeline who was transported into this universe."
    sol "I can only fear what the situation would be if the time displacement affected other... individuals of my time..."
    kay "Uhh... So... by the way, what's this hideout that Ava's got prepared for us anyways?"
    sol "It appears to be a small cabin built by the Mining Union which was abandoned decades past when the nearby rocks failed to yield any ore."
    sol "We will be residing together in it in the meantime, until the Commander and Asaga return from Ryuvia Prime."
    kay "O-oh, okay..."
    kay "Wait."
    kay "Living... together...!?"
    
    $dshow("sola armhold neutral neutral sad blush")
    
    sol "Yes."
    kay "... ... ..."
    kay "(WWHHHAAATTTTTTTT!? AVA, YOU DIDN'T MENTION THIS!!!!!!!!!)"

    scene black with horizontalwipe
    
    "Shields and Sola finally spotted the cabin. As Sola had stated, the small steel structure appeared long abandoned, and was thoroughly covered with sand and dust."
    "Shields looked at his new temporary home..."
    "He was now a fugitive from society. A space captain without a ship."
    "His crew, now scattered throughout the galaxy... desperately trying to restore what they had lost..."
    "One day, they would all be reunited. But for now, the road ahead appeared dark."
    "They were defeated. But not yet out."
    
    play music "Music/The_Final_Battle.ogg" fadeout 1.5
    
    "He gritted his teeth."
    "Too many lives had been lost for him to surrender now..."
    "His crew had entrusted their lives to him. Despite letting everyone down, he still had everyone's support."
    "He had to carry on... No matter the weight on his shoulders..."
    "He looked to the distance with Sola..."
    "They would rebuild from this point on..."
    "His losses had been grave. His wounds went beyond the physical. But he was still alive, to fight another day..."
    "As long as he had but a sliver of strength left in him, he would keep trying to restore what was lost."
    
    if chigaradidntbetray == False:
        "This time, he had let his guard down..."
        "The scars of his past had made him seek easy comfort."
        "When his crew needed his leadership, he instead had sought his own happiness..."
        "And that only lead to his downfall..."
        "The enemy used his grief to ultimately bring ruin to all of his hopes."
        "He was betrayed."
        "By the one he trusted the most."
        "But next time... Next time he would not turn away the advice of his friends."
        
    if chigaradidntbetray == True:
        "Despite all they had worked for, the prototypes had managed to thwart them."
        "Their mission was vast, and their efforts even mightier. And they'd got close to winning."
        "But at the last moment, the enemy had one last trick up their sleeve and snatched victory away."
        "And because of that... Chigara..."
        "No... She..."
        "She was still alive!"
        "Shields knew..."
        "He would see her again."
    
    "From the ashes of this defeat, they would all be reborn..."
    "Deep inside of him... He knew..."
    "The Sunrider..."
    show reborn:
        xalign 0.5 yalign 0.5
    with dissolvemedium
    pause
    stop music fadeout 1.5
    hide reborn
    with dissolvemedium

label postcredits:

    $renpy.music.set_volume(0.27, delay=0.5, channel="music")
    
    play music "Music/Fallen_Angel_Pt3.ogg"
    scene black
    scene abyss:
        xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
        ease 10 zoom 1.0 rotate 5
    with dissolvemedium

    "Deep within the Mnemosyne Abyss..."
    
    play sound "sound/large_warpout.ogg"
    
    scene white with dissolve
    scene black with dissolve
    
    "A mammoth super-dreadnought of unknown origins emerged from warp space."
    unof "My liege... The time portal did not work as anticipated..."
    unof "Instead of being transported to before the battle, we were flung two thousand years into the future instead..."
    unof "Further, it appears the Farari bitch was also caught in the temporal blast and flung into this time line as well..."
    unof "Unknown interlopers have destroyed the time device, and thus we cannot anticipate returning to our time line..."
    
    scene despair with dissolvemedium
    
    cro "Arggh..."
    cro "Fool!"
    unof "I-I beg your forgiveness, my lord Crow..."
    unof "T-the denizens of this universe appear to be nothing more than primitives..."
    unof "S-surely, my lord can expect to easily subjugate them for his ends..."
    cro "Grrgg..."
    cro "...Very well..."
    cro "If I am to be robbed of my victory against the Farari lowbloods, then I shall rebuild our glorious empire here."
    cro "Hah!"
    cro "To the denizens of this strange new land..."
    cro "Prepare!"
    cro "For the rebirth of the Holy Empire!"
    
    stop music
    play sound "sound/epictrailerhit.ogg"
    
    scene black
    show tbc:
        xalign 0.5 yalign 0.5
    
    #save exporting
    $libday_save_dump() #uses multipersistent object with reference "Liberation Day"
    $ltd() #creates a folder named 'game clear save' with a file named 'game_cleared.dat' which is actually a txt file. ONLY WORKS ON WINDOWS
    
    pause
    
    $ renpy.full_restart()

label credits:
        
    window hide
    hide screen leftbuttons
    
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    
    play music "Music/Sora_no_Kodoh.ogg"
    
    show asagacockpit:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0
        
    show credit1:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
       
    show credit2:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show cosette_attack behind credit:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0
    
    show credit3:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show credit4:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3

    show lynn_brig1 behind credit:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit5:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2

    pause 3
    
    show credit6:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show asaga_reflection1 behind credit:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0
    
    show credit7:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show credit8:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show chigara_tea1 behind credit:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0
    
    show credit9:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show credit10:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3    
    
    if legion_destroyed == True:
    
        show hangar_celebration_patch behind credit:
            alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
            ease 1.0 alpha 0.7
            pause 4
            ease 1.0 alpha 0
    
    if legion_destroyed == False:
    
        show hangar_celebration behind credit:
            alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
            ease 1.0 alpha 0.7
            pause 4
            ease 1.0 alpha 0  
    
    show credit11:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show credit12:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show asaga_jealous:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0
    
    show credit13:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
    
    show credit14:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3

    show messhallparty1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit15:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show credit16:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show chigaralap1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit17:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show credit18:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3

    show asaga_fall:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit19:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show credit20:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show fight1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit21:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
        
    show credit22:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show allryders_launch:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit23:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show credit24:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3

    show lynn_cockpit_space1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit25:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show credit26:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3
    
    if CENSOR == True:

        show chigaramindstream:
            alpha 0.0 zoom 0.15 xpos 0.1 yalign 0.5 subpixel True
            ease 1.0 alpha 0.7
            pause 4
            ease 1.0 alpha 0
            
    if CENSOR == False:
        
        show h_chigaramindstream:
            alpha 0.0 zoom 0.15 xpos 0.1 yalign 0.5 subpixel True
            ease 1.0 alpha 0.7
            pause 4
            ease 1.0 alpha 0

    show credit27:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3
        
    show credit28:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    
    pause 3

    show chigaramindstream3:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit29:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2
    
    show credit30:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
        
    pause 3

    show credit31:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2
    
    show credit32:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
    
    pause 3

    show alice_cockpit1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit33:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2
        
    show credit34:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
    
    pause 3

    show credit35:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2
    
    show credit36:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
        
    pause 3

    show twist1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit37:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2

    show credit38:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2

    pause 3

    show credit39:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2

    show credit40:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
        
    pause 3

    show ondrone1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit41:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2

    show credit42:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
        
    pause 3

    show credit43:
        ypos 1.1 xanchor 0.5 xpos 0.6
        linear 14 ypos -0.2

    show credit44:
        ypos 1.1 xanchor 0.5 xpos 0.85
        linear 14 ypos -0.2
    pause 3

    show credit45:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
        
    pause 3

    show kaytokiss1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit46:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 18.31 ypos -0.6
    pause 9

    show credit47:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 3

    show dead1:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit48:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 3

    show credit49:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 3

    show standoff3:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit50:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 3

    show credit51:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 3

    show kaytoend4:
        alpha 0.0 zoom 0.3 xpos 0.1 yalign 0.5 subpixel True
        ease 1.0 alpha 0.7
        pause 4
        ease 1.0 alpha 0

    show credit52:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 3

    show credit53:
        ypos 1.1 xpos 0.7 xanchor 0.5
        linear 14 ypos -0.2
    pause 10

    scene black
    show overhangar
    show credit54:
        ypos 0.5 xalign 0.5    
    with dissolve
    $renpy.pause(10)
    hide credit54 with dissolve

    show credit55:
        yalign 0.5 xalign 0.5

    pause 3
    
    hide credit55
    scene black
    with dissolve

    cre "SYMBOL TO A:{p}Kyubey, ~ren, Kirino is love, AAAYogibearAAA, Aaron, Aaron Holding, Aaron Kaluszka, Aaron Kettle, Aaron Matthews, Aaron Taylor, Abe, AbeFM, Accelsharp, accRei, AceMcKillYoFace, Adam Little, Adam Pitt, Adam Raines, Adrian A. Gallegos, Adrian Bergström, Adrian Ferrer (Sixten), Adriano Gagliardi, Agent Francis York Morgan, but please, just call me York, Agus Hartono, Ágúst Sigurjónsson, AJ Nordstrom, akaPassion, Akures, Albert \"Warrax\" Aloma, Alberto Garcia, Alec Tomlins, Alemina Bismarck, Alex \"Xelada\" Hargreaves, Alex Aranovsky, Alex Churchill, Alex Donks, Alex Edwards, Alex Worthington, Alexa Vitovsky, Alexander  Gene Schulz & Ken Kim Schulz &  Melissa Lynn Schulz, Alexander Frey, Alexander John Aristotle Kimball, Alexander Kent, Alexander Liebau, Alexander Petrovic, Alexander W. Knowlton, Alexandre \"nah\" Bailly, Alexei \"Roflcopter\" Short, Alexis Perron, Allen J Medlen, Allen Kwan, AlliedG, Almost Human, Alto, Amber Hein, Ampereox Irfan, Anaël Verrier, Anderan, Anders Kronquist, Anders Schack Østergaard, Andre Bellarin, Andrea Martinelli, Andreas Gyllblad, Andrew Bethesda, Andrew Biernacki, Andrew Hovanec, Andrew Juljenjai, Andrew Nelson aka SomePoorSap, Andrew P. Bullen, Andrew Paul Maggio III, Andrew Simpson, Andrew Wilson, Angelo \"Brooklyn Finest\" Lima Representing Brazil In Da House, Angelus Luminous, Anna Lee, Anne Nonymous, anonymous, Anonymous, Anonymous, anonymous, Ansel Wong, Anthony Ambrassi, Anthony DeBartolo, Anthony Kinnear, Anthony Luu, Anthony R. Evans, Anton Gorbunov, Anton Guryanov, Arcbleast, ArcherRush, ArchSenex, Arild Iversen aka. Foamed, Arjuna Chatrathi, Arkent Golt, Arkheos Angelos, Armando A. Rosado, Arnel De Leon, ARoastedPenguin, ARPerson, Arthur Lee, Ashadow700, Atomsk, Augusto Andrade, Austin \"Yamato\" F., Avery Heart, Axel Miszczak, Axel Terizaki, Aymeric Hedin"
    cre "B:{p}Baldarhion, Bastiaan Rours, Beardsly, Ben, Ben \"OathAlliance\" Corum, Ben Bonds, Ben Hockley, Ben M, Ben Parsons, Ben Tiberius, Ben Waxman PA-C, BenEng91, Benjamin \"violink4swords\" Randall, Benjamin John Whittingham, Benji Bent, Bewoulve, bhakabane, Biiku Ryugaku, Billpete002, Bingo, Bjorn Vrancken, Bkarsi, Blaine Kawakami, Blake Cross, Blake Domeyer, B-Lo.Co, Bob Sintas, Bobby Skeens, Born2Love, Brad Dunlap, Brandon \"Gnome\" Davis, Brandon \"Zonz\" Chambers, Brandon Coleman, Brandon Nguyen, Bren Rowe, Brett \"DJ Archangel\" Strassner, Brett Martinez, Brett Pearson (J.C. Quiinn), Brian Henderson, Brian L, Brian L., Brian Santos, Brian Simms, Brian Townsend, Brittni Ballard, Brody Miron, Brozita #420BLAZEIT ( ͡° ͜ʖ ͡°), Bruce Novakowski, Bruno \"The Draconic Lord\" Santos, Bruno Marques, Bryan Elliott, Bryan Lyon, Bryan Massengale, Bryan Middlebrook, Bryan Russowsky, BtBurns, Budi Winarto, bugrom.san, Bulens Simon, Burstroc, Buwaro Elexion"
    cre "C:{p}C Weber, Caidran, Cail Synnacht, Caitlin Eckert, Cally, Calvin C., Cameron Sekulin, Canberk Koparal, Captain John M. Smith, Captain Max Zero, Carey Stanley, Carlos Bruno Alves, Carlton Solle, Casey C. Knowlton-Key, Cassie Halladay, Ceci Kiyomizu, Chaadon Peterson, Chankit Pongdhana AKA xredsoulz, Chaos, Charlie Tomlinson, Chase Earhart, Chase L., Chau Hoang, Chayadol, Choum, Chris Bates, Chris Fox, Chris G., Chris Headley, Chris McCleese, Chris Mear, Chris Renard, Chris Stewart, Chris Taran, Chris W, Chris Willard, Christian Dobson, Christian Skomorowski, Christian Waterhouse, Christian Witte, Christop, Christoph Kamper, Christopher \"Rigrot\" Wood, Christopher C. Cockrell, Christopher C. Hoitash, Christopher Gebhart, Christopher J. Epure, Christopher Liang, Christopher Roberts, Christopher Rubio, Christopher S Martin, Christopher Soon, Christopher Toy, Christopher Zhong, Chua Chong Yi, Cirvaazny, CLAUDE IS BEST GIRL, Clay Smith, Cody Hedgecock, Cody Spence, Colin Kennat, Connor Greeley (Shadowwolf9711), Coresplinter, Count Buggula, Craig Butler, Craig James Kelly (dynamo), Craig S. Weinstein, Craken, Cristobal Mera Collantes, Crucian, cupcakemann95, Cybolt, Cyen, cymricchen, Cyprien Randon (MisterTokijin)"
    cre "D:{p}Damien Pearson, Damien Terrasson, Damon Eric English, Dan \"J0nd03\" Beasley, Dan Svoboda, Dan Vince, Dan Whitmore, Daniel B, Daniel Drimus, Daniel Emmons, Daniel Guyton, Daniel Hull, Daniel Lin, Daniel Root \"Red Alchemy\", Daniel Widegren, Daniele Canciani (aka croma25td), Danny Lwin, Dargon, Dark09, Darkeva, Darkron008, Darksor, Darn, Darth Crater, dave55man, David, David \"Socratics101\" Chang, David Beauchamp, David C Werling, David Carreiro-Ricard, David Dalton, David Emanuel, David Francis, David H. Lee, David Ing, David John Pack, David Long (Neko), David McFadden, David Michael Finzi, David 'Milky' Barry, David Pieper, David Shireman, David Telles, David Tran, Dawfydd Kelly, Dawn_, deadering, Dean Kelly, Dean Reeder, Delbert Thompson, Denali Leland, Derek \"Pineapple Steak\" Swoyer, Derek \"Sokolov\" Chin, Derrick Lam, Derrick Pilgrim Jr, Desmond Sutcliffe, \"Devon \"Tag\" Courtney, DickJutsu.com, Dimitri Pivnicki, Dinko Serifovic, diragjie, Disoriented Effigy, DKDevil, D-Man, Dmitry Tretyakov, Do not include, Doctor Duckie - KY, DOKIE & KATHIE, Dominic \"RocK_M\" Ferrer, Dominic Christen, Don Hanson II, Don, Beth, & Meghan Ferris, dorlingo, Doug Grimes, Douglas Sloan, Drake Navarone, Drew Schultz, D-Rock, Duatha, Duncan, Duncan Jones, Dustin Roop, Dylan"
    cre "E:{p}Ebertb, eclipsednight, Ed130 The Vanguard, Eddie Akers, Eden Code, Edgar Martinez, Edward Benavides, Edward Gibbens, Edward Truong, Einjeru (Steven Rodriguez), Ektorus, Elari Tammenurm, Eli Mack, Eltrum, Elvis Henry Strunk, Endang Srie Redjeki, Enerccio, Ensign Enkrow, Erendil, Eric, Eric Lenoir, Eric Moeller, Eric T. Boyce, Eric Wei, Eric Zylstra, Erich Lah, Erik Proskin, Ernest Ivnik, Ernesto Ayala Jr, ErrBerry, Erwan Hellouin, Escelar, Ethan \"SteelAngel\" Deneault, Ethan Leyva, EuphoricField~Vesalious"
    cre "F:{p}Fabián M. Rebolledo, faeriehunter, Fakhrul Anwar, Falkmir, Falwin, Fang-Kai Hsieh, Fearfireg, Feenie, Felipe Augusto Batista, Felix Grothkopp, Felix Stelzer, fenixDG, Ferdinand Schober, Fimb ul Kron, finmarchicus, FiShiYun, fk000007, Flintspatula, Florian Sebesta, FoMothaRussia, Fractured, Francisco Garcia, Franklin Hamilton, Freddy \"KaKuna\" Hansson, Frédéric Magnin, Frederik Vezina, Frozen Friend (CD), Fury of the Tempest"
    cre "G:{p}Gabriel \"Gabe Khronos\" Godoy, Gabriel Silvas, Gareth Saxby, Garrett Muggy, Gary Gould (Lazzarus), Gary Howard, gekiganwing, Gentro, George Henry Shaft, Giacomo Russo, Giantenemycrab, Gideon K, Gilorm, Gilshim, Giovanni \"Allen92\" Cambi, Gnostic, Godewijn W. Perizonius, GoldenCrater, Goldenkitten, Gordon Wearing-Smith, Gotchabagoose, Grant Edwards, Grant Fraser, Greem, Gregory Doge Straight, Gregory Jehan Michel Claude Jacob Gallet, Gregory McCausland, Gregory Polander, Gregory W. Marlin, Groshonee, Grzegorz 'ggamer2' Kucharski, Gunnar Högberg, Gurney"
    cre "H:{p}H1r1n, Halasimov, Haldrin Loregrant, Hanh Van Tang, Harminder Gill, hellgod, Henrik Augustsson, Henry Tran, Hermann B, Hermit, Hessi, Hickname, Hidsnake, Hisakatana, hiyoko556, Honfei \"zisback\" Li, Hugo Crampon, Humberto Meireles (StarChuck), Hung Fuen Mak, Hunter- Captain Obvious the Fantastic, Hunter Goins, Hunterwolf1001"
    cre "I:{p}Ian, Ian \"ThaWulf\" Wolfe, Ian Cox, Ian Whitehead, Imban, Interitus, Isylia Vinland, Ivan \"DesuEagle\" Orlov, Ivan C, Ivan Garcia, Ivannorr, Ivron, Iwan C. A. Smith, Izkda"
    cre "J:{p}J. Andrew Hartman, J. Calkins, J. Hayden Pretzman, J. Quincy Sperber, J.J. Lee, Jack Gibbs, Jacob Hull, Jacob Searcy, Jacques Alexander Katzoff, Jaime Navarro Weber, Jamal L. McWillis, James \"Troll\" LeRoy, James Alexander Henley, James Connors, James H., James Kahalewai, James Lange, James Lofshult (Solav), James O'Bannon Tiffany, James Pineda, James Ross, James Sellman, James Talerico, James Taylor, James Virts, Jamie Manley, Jan Paulsson, Jan-Ole Hübner, Jan-Pierre Jaspers, JapaneseSandman, Jared Goodwater, Jared Rex, Jarosław Knaś, Jarred Nation, Jason, Jason Chou, Jason King, Jason M, Jason Paas, Jason Silva, jason wysocki, Jay Myers III, Jaydon Cannella, Jay-Yun Wang, JD, Jean-Louis Lanteigne, Jeff Coelho, Jeff Hunt, Jeff Netzke, Jeff S., Jeff Schmidt, Jeffery Lawler, Jeremy Duboscq, Jeremy James, Jesse Korhonen, Jesse O., Jezariael Demos, J-F \"Jim le Mime\" C., jghibiki, Jim Chen, Jim Rutkowski, Jim W., Jinx, joachim_kamikaze, João Carrera, Joe, Joe \"Joey\" Saint, Joe Egan, Joe Gilligan(Kingz), Joel Engel (Lightmare), Joey Colli, Johan De Witte, John \"Magnificent Beard\" Schmidt, John \"starfuryzeta\" Mathews, John Anderson, John BlueFreakQ McHugh, John Bremseth, John Christian \"Chriss\" Mæland, John Doyle, John Enright, John GT, John P. Doran, John R. \"Wattsman\" Watson, John Speigel III, John Woodgate, John, Mark, and Ron Aspuria, Johnathan \"MechaVsKaiju.com\" Wright, Jon (WEKM) Krupp, Jonas Bronée, Jonas Westerberg (Nody), Jonathan \"PrimeBacon\", Jonathan Chiu, Jonathan Grimm, Jonathan Shaham, Jonathan Souza, Jonathon \"Pamphy\" Pamphilon, Joonas Parviainen, Jordan Cunningham, Jordan Jeske, Jordan Radomi, Jordane \"Tamajyga\" Lemasson, Jose Angel \"Space Warrior\" Lara, Jose Ramón Vega, Jose Tenorio, Joseph \"Quorum\" Magnotti, Joseph Fong, Joseph Ng, Joseph Perez, Josh Griffiths, Josh Medin, Joshi120, Joshua Cubstead, Joshua Gammon, Joshua James Kern, Joshua Matthew Ruiz, Joshua Peng, Joshua Scott, Jozern, Juan Diego \"Goose\" Ramirez, Juan Peredo, Juancarlos Reyes, Juanjo Barrio, Judy McConnell, Juha \"Baric\" Laaksonen, Juho Juopperi, Julien LAMANT, Justin Horn, Justin Moor, Justin Porcelo, JY, jyuichi, JZL"
    cre "K:{p}K. Mason, k8207dz, Kaelyn Takata, kahadin, Kai Hellmeier, Kaisar69, Karan N. Patel, Karbunos, Karl K, Karl Lassen, Kasper Bergh, Kasper Gammelgaard Hansen, Katherine Williams, Kedo Ciepse, Keeper O Books, Keith Minton, Kelley J., Kelvin, Kenichi Morita, Kenneth Riebe, Keresian, Kestrel150, Kevin, Kevin \"Alythe\" Chow, Kevin Moreno, Kevin Mueller, Kevin S Robertson, Kevin Webb, Kierian O'Hare \^-^/, Kim Tae Woo, Kinoru07, Kirk R. Jensen, Kjetil \"Fyko\" Engvold, KlaisStardust, Kody Tschorn AKA Mr5cap, KogX, Konstantin Koptev, Konsulus, Kory Holtz, Kožec, Kray, Krinku, Kris Hjortshøj Nielsen, Kristiana Moretti, Kronophage, Krunjey, Kurik Lein, Kuritár Tamás György, Kuro \"Drill Battleship\" Gane, Kurt J Klemm, Kurt Montgomery, Kurt Staiger, Kyle Greene, Kyler Markowski"
    cre "L:{p}Laestril, Lamhirh, Lancelot H., Larissa Reynolds Loves Her Husband Levi, Lars Mattsson, Lars Nygaard Witter, Lassi Heliö, Laure Jansen, Laurence Stratton, Laurent \"Lapov\" Patillon, Laurent Trentaz Vite, Le Di Chang, Ledabot, Lee Barnes, Lee Zary, Leno Nunes, Lenworb, Leon Byford, Leon Yong L.O, Leônidas \"+300\" Soares Pereira, Levi McConnell, Lex, Liam Do, Lib, LibraSweets, Lightning Strike, Lim Ye Ping, Linda Barming, LMekko, Loc Le, Logan Lybbert, Long Nghiem, Long Ngoc Nguyen, Lord Eric of Belleau Wood, Lubrioz, Lucas Aquino de Assis-Trysson12, Lucas McMillan, Lucas Watson, Lukasz Gibel, Luke Michel, Luther McBlain"
    cre "M:{p}M Allan, M D Snider, M J V Kwan, M. Lara, Maciej Bojarski, Mackenzie Buckle, Mady vand, Maecolis, Magnvs, Malte M. Breckwoldt, Manje Jung, Manuel Acosta, Marc \"Markie\" Bondoc, Marc Agne, \"Marc David Karsai (BITE ME UNIVERSE) NEKO NEKO NYAN!, Marc Reid, Marcel Matz, Marco \"Dralel\", Marco \"xizro345\" Beltrame, Marcus A. Nichols, Marcus Soll, Marijn Hubert, Marius Kaufmann, Mark \"NeoWolf\" Howe, Mark \"Sparkles\" Vaz, Mark Gandy, Mark Gould, Mark Knewstubb, Mark L, Mark Shaw, Mark W. McCarthy, Markus Hessler, Marquess Joel Goldschmidt \"AngelicxSoul\", Martin \"Malangs\" Langhammer, Martin Do, Martin Estrada, Martin Hanze, Marty H, Master Yi & Wukong, Mathew Fang, Mathieu Krog, Matsubara Yuu (Lordmatsu), Matt, Matt C. Wepee, Matt Clark, Matt Halverson, Matt Kanon, Matthew A. Warren, Matthew Andrychuk, Matthew Bates, Matthew Ley, Matthew Robinson, Matthew Sanders, Matthew Schupack, Matthew Williams, Mattias Axblom, Max, Max \"NEXUS\" Sjøstrand, Max \"SpaceWizard\" Mohler, Max Battcher, Max McIntyre, MaxMahem, Mazikeen Wagner, Mega4709, meganothing, Mehlo, Mereck, Micah Steele, Michael, Michael \"beefsack\" Alexander, Michael \"BookwormOtaku\" Connell, Michael \"Chaostraveler\" Cencarik, Michael Armey, Michael Beemer, Michael Brand, Michael Edward Miller, Michael Fedrowitz, Michael Grose, Michael Holcombe, Michael Kaplan, Michael Kwiatkowski, Michael Lingg, Michael McCollum, Michael Muske, Michael Ragdamar Tremblay, Michael Salyer, Michael Sand Petersen, Michael Stenqvist Haglund, Michael T. Ilano, Michael Troester, Michael W. Sim, Michael Wilkerson, Michel Lauzon, Miguel \"Mr.GreenToS\" Martinez, Miguel De Serpa, Miguel Lollett, Mikael Ronzier, Mike \"Ski\" Thomas, mike a pennington, Mike Ong, Mike Ostrow, Mike Taggart, Miki Hoshii, Miles Matton, Miss Roady Pie Esquire, Mithagar, MK, moe.kyun.Vokurek, Mohaan, Mondy, Morgan Hamilton, Mostly_Magic, Mr.Quija, Murat Boduroglu, Myron Monteiro"
    cre "N:{p}N. Andrelli, N. Yoshimori, NAKAMZ, Natani Lucchini, Nathan Bunn, Nathan Taggart, Nathaniel Early, Nathaniel Pahl, Nahaniel Scott Rivers, Neil 'Elcs' Elcome, Nemo157, neothoron, Nersius, Neverstorm, Nicholas Bianchi, Nicholas Brady, Nicholas Lor, Nick Johnston, Nick Noe, Nico A Valdez, Nico B., Nicolas Barbezat, Nicolas Miranda, Nicolas Van Sintejan, Nigel Wright, Nijuu \"I Love GOG & DRM free\" Lau, Nikolay Donets, Nilesh 'Onomato', Nima Safaie, Nipun Wittayasooporn, Nobody679, Nolan \"AnalFries\" Raven, NoNamedFuzzyPanda2, None, Nonomo4"
    cre "O:{p}Oliver Perks, Olivier Lebeau-Paradis, Omar Rodriguez, Omikron, Onearmdude, Onery Popopango, Oniii-chan, OniPierreot, Opacity, Origin Angel, Owen Sa"
    cre "P-Q:{p}P. Rischka, Pablo Soler, Pat Jones, Patrick \"AThyper\" Daigle, Patrick \"Celowin\" Jones, Patrick \"Chaos\" Burke, Patrick Eitz, Patrick Ellis, Patrick LaCasse, Patrick Tan, Patrik Raijū Willner, Paul Coombes, Paul H, Paul Houston Clifford Martin Von Barron, Paul Mikelonis, Paul Rock, Paulo Rafael Guariglia Escanhoela, Paulus1000, Pavel Pohilko, Pawel Blizniak, Paweł Kolek, Peo01, Per Hedbor, Per Kristian Brastad, Per Sjödén, Perry, Peter B., Peter Lansdaal, Peter Schnare, Pharaohowen, Phil 'Kyubey' Lam, Phil Salon, Phil White, Philip Hagan, Pierre Nosek, pinvendor, Legendary Merchant of Pins, PJ Grant, pktlonewolf, Professor Ficus, prototype00, Puiheng Tse, Punner, Quan Doan"
    cre "R:{p}Radiovid, Ragnos13, Ramon Muradin, Randy Eckenrode, Randy Meister, Rasmus Vilsgaard, Raymond Au, Raymond Luis Armstrong, Raymond Y (Fatman139), Raz'Nagul, redeyesblackpanda, Redsnabba, Rehan Ansari, REMCAP, Rene Cabanza Jr., Revek, rgreat, Rias Klein, Ricardo \"kod\" Rodriguez, Richard \"Dablue\" Blaauw, Richard Daigle, Richard Ford, Richard Leiva, Richard Lin, Richard Loh, Rick Reischman, River Thames, Robbie Boerner, Robert Billings, Robert D., Robert Disbrow, Robert Kitzmueller, Robert Labier, Robert McNaughton, Robert Musser, Roberto Carioli, Roberto Casas - rcasas83, Roberto Quintans, robotsheepboy, ROK - Yong Seok Park, Rommy Kwan, Ron Vondrasek, Ronan 2L, Ronin Storm, Roomkaasje, Ross, Ross Boskovski JR, Ross Brierley, Rudy M. Soto, Rufus, Russell Street, Ryan Dunnison, Ryan J. Jackson, Ryan K. (cat_pack), Ryan Tabb, Ryan Templeton, Ryan Ward, Ryan Woodland, Rykki, Ryzuku"
    cre "S:{p}Sam \"Tarvos\" Gibbins, Sam 'Bobular' Whittingham, Sam Garamy, Sam Mui (Seraph), Sam Thomas, Samarix2, Samuel Foster, Samuel Hartp}Samuel Malo, Sarah J Brown, Sascha Kunze, Saúl Mostacero, SayEric, Schaffer, Schuyler Kreitz, Scott Newitt, SeaGnome, Sean Bailey, Sean Kemp, Sean Shuai, Sean Steder, Sean Thurston, Sebastian Gerhold, SEPIA, Seth Crofton, Seto Konowa, Seyren Windsor, SH VL, Shadow, Shane Agnew, Shane Kilpatrick, Sharif Elgamal, Shaun \"IrishWonda\" Danis, Shaun Skelton, Shenmage, shiinx, Shimble, shinobi, Shuai \"Seingan\" Lin, siegeofjones, Sightless, Sihan Wang, Silentwatcher, SilverWasp, Simo Nyyssönen, Simon Bumgardner, Simon 'garkham' Landureau, Simon Holk, Sinou Rémi, Slinky7689 (Nicholas Aylmore), Snowboundkarma, Solgrid, Solomon Lee, Somebodycooler, SonicGTR, Sonny Larsson, Stanislav, Stefan \"ramsesoriginal\" Insam, Stefan Markovic, Stefan Winkler, Stephan Szabo, Stephen Dougherty, Stephen Hazlewood, Stephen Lemelin, Steve \"Bofferbrauer\" Weidig, Steve Green, Steve Jasper, Steve Lord, Steven \"mchief75\" Simon, Steven \"Walshee-poo\" Walsh, Steven Duncan, Steven Farrar, Steven Hoffmann, Steven Holt, Steven Kang, Steven Kirby, Steven Rexroth, Steven Tincknell, Steven Vuong, Stormfox, Stuart Logan, Sugartit, Super Jared, SusanTheCat, Szymon \"Amerth\" Przybylak"
    cre "T:{p}T. K. Motoyama, Tai Tran, Tanner Garrett, Tapper, Taylor \"Berserk\" Staley, Taylor Collins, Te Hung Tseng, Team Kazam, Tengku Aiman Zulfika, Terence Ow, Terris H20, The Blind Gardener, The Dude, The Grand Harmony of Cetacea, The Patrick Tran, The Wanderer, thezeldagamer, Thissa, Thomas Aasebø, Thomas Aigner, Thomas Custer, Thomas Haymes, Thomas Kaghan, Thomas Schwarz, Thomas Siemens, Thomas Z. Palka, Thomas Zilling, Thorgard, Tim Crothers, Tim Danysh, Tim Ferguson, Tim L, Tim Newman, Tim Reilly, Tim Reynolds, Tim Thacher, Time Lord Ponce, Timmothy \"Akeashar\" Clarke, Timothy Acuff, Timothy Chappell, Timothy Lim, Timothy Martin, Timothy McGowan, Timothy Miller, Timothy Updike, Ting \"Herobear\" Wong, toan tran, Tobias Bollinger, Tobias Schewe, Tom \"PyTom\" Rothamel, Tomare Utsu Zo, Tomas (Xarien) Refsland, Tommy Torenius, Tong Yu, Tony Roberts, Travis Spano, Travis Williams, Trevor Becker, Trevor DeVore, Trevor Sexton, Tristan Carranante, Tristan Kennison, Tsuki, Tuckles, twig, Tyler E. Trosper, Tyler Leger, Tyler Winfield"
    cre "U:{p}Unddphenix, unholyghost07, Uros Bartolj, Ursine Pedal Digit a/k/a \"Thug Life Otter\", USRPG"
    cre "V:{p}VAhrens, Valsang, Vasily Chinarev, Venron, Videogamer25, Vintson Knight, Vlad, Vladimir Putin, Vladimir Shvetsov, Voldar"
    cre "W-Y:{p}WalkingAtlas, Warboss Curb, Wes Owens, Will Chang, Will Kenni, Will Lawrence, William Bradley, William Bryant, William Fleming, William Joseph Owens, William Laminack, William Perry, William Roberts, William Taylor, Willid, Wilson Bilkovich, Wizbang The Mighty, www.boredgamer.co.uk, Wyrtt"
    cre "X-Z:{p}Xavier Dolci, Xiao, xxzindxx, Yaka, Yohan Withington, Yuri Van Dierendonck, Yurii Furtat, Zac Binion, Zach Milosic, Zach Whitesell, Zachary Kosarik, zack wood, Zak Kalles, Zalminen, zanza, Zenelix, Zenigame, Zero Null, Zetsuna, Zikri Muzammil, Zu Long, Zythiku, アルバート　ウェークス（AJ)"

    show credit56:
        yalign 0.5 xalign 0.5
        
    pause 3
    
    hide credit56

    cre "Abraham Abundes, Adam Knight, AJ Conrad, Albatar L'enculÃ© de l'espace, Alex Lewis, Alex Leys, Alex Porraz, Alexander Kimball, Alexander Quirindongo, Alexis Mauvisseau, Alf Petter Jakobsen, Allen Bettendorf, Aminul Harrith, Andrew Denisov, Andrew Grant, Andrew J Nowak, Andrew MacKenzie, Andrew Stewart, Arkblade , Atomic Defender, Austin Monticelli, Ben Abrehart, Ben Jennings (Mags), Bob , BonesiiDrake , Brian Chin, Brian Rulon, Calvin Sauerbier, Cameron Dufton, Cameron Tyler, carlos favela, Carlos Martinez, Charles Baer, Chase Madsen, Chieh-en Shih, Chitose , Chris Willard, Christian B Dezell, Christian Chaux, Christian Ellis, Christian Pennanen, Christopher Hall, Christopher Lee, Christopher Oates, Christopher Standard, churmite , Civarity , Clifford Kellogg, Cody , Cody Williams, Cory Favorite, Craig Watson, Cristobal Mera, Crusader Flame, Crystal Poxon, Dan Le, Daniel , Daniel Chappell, Danilo Lucignano, Darius Engineer, Daryl Rogall, David , David Hanson, David Jonsson, David Nava, Dean Reeder, Doddler , Drath , Dreamy G, edapblix , Eero Leinonen, Egorion , Eric Tsai, Ethan Kosolowsky, Felix Torres, Francisco Javier, Fsteak , GALGE , Gautam Behal, Gavin Hawthorne, God_of_Despair , Graham Heales, Hoangde Tran, Holylin , Hong Jun , Hunter Korando, Iain , Ibraheem Ahmad, Imban , Infinite Exploration Incorporated, Ivan Salas-Soto, J.M. Ellis, J.R. , Jack Clarke, Jacob Thomas, Jake holland, Jakob Stjerndorff, James  Connally, James Finn, James Lee, James Ryan Sisk, James Tighe, Janne , JD Lawrence, Jean-michel Deslauriers, Jesse Badenoch, Jesse Ortiz, Jimmy , Joe , Joe Tansley, Joel S, John Munn, John T, John Tibbetts, Jolu Talampas, Jonathan Zollo, Jordan Lyall, Jordi Hodson, Jorge Ricardo Teixeira de Queiroz de Freitas, Josef Weber, Joshua Evans, Joshua Valdez, Joshua Van Der Sluys, Justin , Justin Eide, Justin Ott, Justin West, Kaleb Dean Johnson, Keegan , Kevin Fischer, Kevin Ju, kiri3tsubasa , Kreese , Kristopher E Fulton, Kx7"
    cre "L , Leo Leonard, Leon Hannaford, LGdotfr , Liam Poole, Lianxi Song, Lilith Wroth, LittleLeah , Loose_Crimsom_Canon , Lord Treant, lordhoth444 , Loriannasha Bolina, Louis Mouganie, Lucario520 , Lukas Frehner, Lurker Below, Mac Wolf, Maksim , Manh Dinh, Mario Maluche, markus &oslash;ynes, Markus Hansen, Martin MÃ¸ller, MasterOfAlice , Matt B, Matt Martin, Matthew Boegeman, Matthew Christen, Matthew Churchyard, Matthew Harper, Matthew Julian, Max DuBeau, Maximilien , Mercyless Reap, Michael , Michael A Almendarez, Michael Brand, Miguel Aguilar, Nadav Lugassy, Neil Bridges, Nep-Nep , Nicholas , Nicholas Tyler Ignatious Peterson, Nico B, Nicolas , Nicolay Izoderov, Nigel Lee, Noctis Vi Luminous, Nomad48 , Nyilas Dominik, Omikron , Oreglia Mathieu, Outlandstalker , paul h bligh, Paul Holzwarth, Paul Li, Peter Blake, Philipp Kirf, Philipp_Trousil , Phillip Palmieri, QuakeRiley , Quinn Watson, Randy Peeters, Redereth , Rewind , RJ Roy, Robert Bielecki, Robert Drexel, Robert Glands, Russell , Ryan Bishop, Ryan Eirls, Saber 250, Saito Brittania, Sami Uski, Samuel Villatte, Sean Burton, Shadow Slice, Shani McCarthy, Shido , Simon Robinson, Simon Sprenzel, SmilingWolf , sopheark phan, Squibeel , Stephen Chance, stian klepsland, Taworn Viriyatonpun, Taylor Fenske, The VN Graveyard, Thomas Brown, Thomas C, Thomas Richard Wall, Toni Kraja, Treecko Green, Trevor Kirke, Truth , Tuomas NikkilÃ¤, Tyler Kassten, Undying Zombie, VÃµ Tráº§n Triáº¿t, Verthand , Villiam Khamsoumphou, Vincent Gagnon, Virgil Armstrong, Will , WoolyShambler , Wu jean-luc, Wyatt S Troup, Yoshihiro , Young Gee Hong, Youpichouchi , Zach Weiland, Zachery Whitesell, Zack dela Cruz, Zanair"

    stop music fadeout 1.5
    
    pause 2
    
    return #jump postcredits
    
