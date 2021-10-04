label dlc_prologue:
    $ dlc = True
    $add_achievements()
    $achievement.sync()
    if libday_mp.legion_destroyed is None:
        #it should be impossible to even start the DLC this way
        $store.legion_destroyed = renpy.random.choice([True,False]) #has to be either True or False or Ava will crash the game.
    else:
        $store.legion_destroyed = libday_mp.legion_destroyed
        
    scene bg black
    show screen quick_menu
    with dissolvemedium
    
    $ renpy.music.set_volume(1.0, delay=0, channel='music')
    $ renpy.music.set_volume(1.0, delay=0, channel='sound')
    $ renpy.music.set_volume(1.0, delay=0, channel='voice')

    play music "Music/Destinys_Path.ogg"
    
    window show
    
    "From the moment humanity began to unravel the mysteries of quantum theory, scientists and emperors alike became obsessed with a singular technology..."
    
    scene bg paradoxback
    with dissolve
    
    "During the search for this Holy Grail, countless other findings which would come to greatly aid - and terrorize - humanity were discovered. The warp drive. Warheads which could level entire continents. Faster than light communications. Even a massive doomsday weapon which could extinguish entire stars: The Paradox Core."
    "But all those powers were irrelevant next to what would be possible with the Holy Grail: A time machine."
    
    scene bg mindstream1
    with dissolve
    
    "In its most simple application, one could undo past mistakes. If an action ended up causing an adverse reaction later in time, one could simply travel to before when the action was made and react differently, with the benefit of hindsight."
    "The full implications of such a device were still far more awesome."
    
    scene bg mindstream2
    with dissolve
    
    "One could stop aging. Freeze time for everyone else but oneself and perform an unlimited number of actions while everyone else was frozen. Translocate other people and objects anywhere, at any time. Become older. Become younger. Given an infinite amount of time, one could become anyone, and accomplish anything."
    "By no exaggeration, someone with a time machine would not be a human, but a god."
    stop music fadeout 1.0
    
    #clone lab
    scene bg clonelab
    with dissolve
    $dshow(81311,ypos=1650)
    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5
    
    "Alice Ashada pondered those thoughts as she walked through the Diode Cloning Facility."
    "Her steps took her to a familiar location. Her old office."
    ali "(So even this detail has been recreated exactly as before...)"
    "It was here, where for the merest sliver of a second, she brushed her fingers against that almighty power..."
    "The Paradox Project..."
    "The galaxy's greatest and most dangerous minds had gathered here, in the furthest corner of the galaxy, to finally attain what had eluded humanity for so long."
    "They were exiled Alliance researchers and New Imperial scientists deemed too dangerous even for the tyrants of New Eden..."
    "But attempt after attempt, year after year, they had failed to produce results."
    "Computations done through their best super computers and artificial intelligences failed to yield breakthroughs."
    "It was then when they realized such knowledge was beyond the comprehension of mere humans. They needed to create a new race, capable of thought processes beyond the capacity of even the most gifted of homo sapiens."
    "First, a prototype was created. Alice Ashada."
    "They watched her. Raised her as a one of their own. Even gave her the surname of the director of the Paradox Project, who assumed the role of her father."
    
    $dshow(81000,ypos=1650)
    
    ali "(Tsch... But it was all a lie!)"
    ali "(Humans... created me for their own ends... And tossed me away the moment I fulfilled my use.)"
    "The Prototype produced some promising results. Accomplishing what super computers and the galaxy's best minds could not, Alice successfully translocated molecules by fractions of a second. A breakthrough, produced even before the artificial girl had turned sixteen."
    "Using the lessons learned from the Prototype, the Alpha was finally created."
    "Alice's teeth clenched."
    ali "(Those scum.. created my sister and I... just so we could be tools in their search to become gods.)"
    
    $dshow(81020,ypos=1650)
    
    ali "(But I stopped their plans... and saved the both of us.)"
    "The Prototype proved far more difficult to control than her creators believed."
    "She accidentally discovered the truth of her existence."
    "Her belief that she was a normal human girl who lived with her caring parents in a research station was shattered that day - the first of the many pieces of her sanity which would break following that day."
    ali "(Yes...)"
    ali "It was here... when I struck down my father... with my very hands."
    ali "What else could I do? I was merely a test run. They were going to toss me away, like an obsolete machine."
    ali "I had no choice! I was going to rescue my sister and escape this prison..."
    "But Alice's life did not have such a happy conclusion."
    
    show prototype_alpha:
        xpos 0.27 zoom 1.0
    with dissolve
    $dshow(81020,xpos=0.73,ypos=1650)
    
    alp "My sister..."
    "Alpha's voice disturbed Alice."
    "Her younger sister approached her."
    alp "A-ah...?"
    "Alpha touched Alice's eye with her index finger. A single droplet of tear ran down her finger as she wiped Alice's eye."
    alp "Your thoughts... They are... bleak."
    
    $dshow(81302,ypos=1650)
    
    "Alice turned around, putting her back to her sister. She closed off her mind so her younger sister would not see the depths of her madness."
    alp "Why do you retreat to the abyss so?"
    alp "Soon, we shall control all of humanity under our grasp. We will rule those who sought to control us."
    alp "Our spy continues to make great inroads into controlling the would-be savior of humanity: The mighty Captain Shields..."
    alp "If he continues to follow our plan, then both the Alliance and PACT will unify. And when the Ebon Fleet arrives, he will rally the galaxy against humanity's greatest threat. As a result of that conflict, he will become, not merely captain, but... something far more powerful..."
    alp "And with his greatest love... our proxy controlling him... We will rule the galaxy from the shadows... Constantly leading him down the path we desire..."
    alp "Such is our destiny, no? We were created to be greater than them."
    
    $dshow(81300,ypos=1650)
    
    ali "(No...)"
    ali "(Human filth... Savages...)"
    ali "(The galaxy would do better if every last trace of them were wiped from existence...!)"
    
    show prototype_alpha behind alice:
        xpos 0.38
    with dissolve
    
    "Suddenly, Alpha embraced her sister from behind."
    alp "It will not be long... my sister..."
    alp "You have suffered... but I seek to create a universe where we can finally be safe..."
    
    $dshow(81601,ypos=1650)
    
    ali "Y-yes..."
    ali "A galaxy. Where we can be safe..."
    "Alice stiffly touched her sister's hand."
    ali "I will go and create that."
    alp "... ... ..."
    ali "(This is the only way...)"
    ali "(My sister is yet naïve... She does not understand the threat the humans pose...)"
    
    hide prototype_alpha with dissolve
    
    "Alice took her sister's arms off her and walked away by herself."
    
    $dshow(81312,ypos=1650)
    
    ali "I will return to the frontlines. And I am taking that with me."
    
    show prototype_alpha:
        xpos 0.27
    with dissolve
    
    alp "That accursed machine..."
    
    $dshow(81512,ypos=1650)
    
    ali "I will need \"her.\" For what is to come."
    alp "Be safe, my sister..."
    ali "... ... ..."
    ali "I shall return. And when I do..."
    ali "The galaxy shall have changed."
    "With that, Alice Ashada walked into the shadows..."
    
    scene black with dissolvemedium
        
label dlc_begin:

    #Office
    scene black
    show bg captainscabin:
        alpha 0.5
    with dissolvemedium  #went with his cabin instead.
    
    "Shields tossed and turned in his sleep..."
    "Vivid images flashed in his mind."
    "This was different from the other nightmares. The ones he would have of blood soaked faces at Ongess. Where that young girl would die again and again..."
    "He would see her pick up the knife every time... But despite knowing what was going to happen... his body would be paralyzed..."
    "Then her face would morph... into his sister..."
    "Maray..."
    mar "\"You... killed me...\""
    "No... tonight's nightmare was different..."
    
    play sound "sound/static.ogg"

    #Liberation Day massacre cgs
    $image_speed = 0.2
    scene black
    show dronedrop1:
        xalign 0.5
        yalign 0.3
        pause image_speed
        "CG/dronedrop5.jpg"
        pause image_speed
        "CG/dronedrop6.png"
        pause image_speed
        "CG/dead2.jpg"
        pause image_speed
        "CG/swornenemies2.jpg"
        pause image_speed
        "CG/kaytoend2.jpg"
        pause image_speed
    
    pause image_speed*6
    scene black
    show bg captainscabin:
        alpha 0.5
        
    "Images flashed by... too quick to decipher... But... something horrible had happened...! N-no... WILL happen!"
    "He was... going to make a horrible mistake...!"
    
    scene white with dissolve
    scene bg captainscabin with dissolve
    stop music fadeout 1.5
    
    "Suddenly, he jolted awake."
    kay "...!"
    "He realized he was in his bed."
    "He shook his head, relieved he was just having a nightmare."
    "... ... ..."
    "Wait a minute..."
    "He felt... someone... sleeping beside him..."
    "What... the... hell...?"
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    "Shields spun around, and pulled the cover off his bed, revealing a certain pink haired doctor nestled up next to him..."
    kay "G-GUCK!!!"
    "Shields leaped out of his bed, and stood upright as a steel rod, eyeing Claude with outrage."
    "Certainly he had known the ship's doctor would go to any lengths to molest him, but to actually break into his quarters after hours...!?"
    "Besides, his room was locked with the strongest encryption protocol onboard the ship! Icari had seen to it that his door would not be broken into ever again! J-just how did this buffoon of a doctor get here!?"
    "For a moment, he tried to recall if he had been drinking heavily in the mess hall before arriving at his quarters. No doubt this lecherous doctor would have used such an lapse in his defenses to latch onto him into his bedside."
    "Thankfully, he recalled that he had merely been filling out paperwork the whole night, before finally deciding he had had enough and resigning himself to listening to Ava's lectures in the morning."
    "Claude opened her eyes with a yawn."
    
    $dshow(30010)
    
    cla "Eaaahh~ Good morning..."
    kay "Good morning?! How did you bypass security to get in here!?"
    cla "Ara."
    $dshow(34310)
    "Claude stood from the bed, her hair a mess."
    cla "Eaah, it was such a pitiful sight, captain... Looking at your sleep deprived face every day... As ship doctor, I had to do something to remedy your sleep disorder stat!"
    $dshow(32010)
    cla "Of course, the best remedy would be a contented deep sleep after pounding your white hot Vanguard into the woman of your dreams, and so I, Claude Trilleo, stepped up to the task! Sah, yes sah!"
    $dshow(34200)
    cla "You can use this body in however manner you desire! Your acting medical officer is ready to serve under, above, in front of, and behind you captain!"
    "Shields rubbed his face in irritation, the conversation obviously not going anywhere."
    kay "Hey... cut it out... I'm asking you to tell me what you're doing here..."
    $dshow(34001)
    cla "W-well, I'm sure it'll become clear soon enough..."
    kay "W-wha-?"
    
    play music "Music/Fallen_Angel_drone.ogg" fadeout 1.5
    
    $dshow(34210)
    "As if on cue, Shields heard the door to his cabin open."
    kay "The hell...?"
    "He quietly knelt down behind his bed."
    "If there was another intruder in his office, then it would mean that the security protocols on his door had failed entirely..."
    "He still had bad memories of what had happened the last time someone had broken into his room, and wasn’t about to take any chances this time. He quietly reached into his closet and withdrew a concealed pistol..."
    "He signaled to Claude to hide behind him."
    "Shields grimaced when Claude gripped onto him from the behind, her massive boobs leaving two impressions on his back."
    "She whispered into his ear."
    $dshow(30000)
    cla "A-ah... captain... A-Actually... the gun won't be necessary..."
    kay "How do you know that?"
    cla "B-because..."
    hide claude with dissolve
    "Suddenly, Shields heard Chigara's voice upstairs."
    chi "A-ah... Eh-heh..."
    "Chigara? What was she doing in his office at this time?"
    "Granted, someone as talented as her could easy crack Icari's security protocols, but why would she--"
    play music "Music/Fallen_Angel_Pt3.ogg" fadeout 1.5
    
    #Chigara on drone
    scene white with dissolve
    scene ondrone1 with dissolve
    scene bg captainscabin with dissolve
    
    "Suddenly, he felt something tear through his psyche, as if a bullet had just gone through his temple."
    "C-Chigara... S-she...!"
    "But what he saw next completely shattered the remaining bits of his mind."
    kay "Heh... Come on, before the commander sees us."
    "It was... HIM!!!"

    #Kayto with Chigara on desk
    scene chigaralap4 with dissolve
    "Shields watched, his jaws agape, as his identical clone took Chigara's hand, and plopped her on top of his lap on his desk."
    "What... was... going... on!?!?!"
    "Even though his first instinct was to barge into Chigara and his clone's little romantic rendezvous, gun in hand, and demand answers, his military training kept him firmly hidden behind his bed, looking for an escape route."
    "He racked his brain for a possible explanation for this bizarre turn of events. Could this be a PACT plot? Did they embed a spy wearing a holomask to impersonate him?"
    "N-no, that would never work... First off, anyone boarding the ship was subjected to a full DNA scan..."
    "Then could it be the Prototypes? That seemed a possibility, as they had a massive army of clones... Could they have acquired his DNA sample somewhere? All it would take to breed a second Kayto Shields would be a strand of his hair, left somewhere unwittingly by him..."
    "But it would still take a lifetime of training for a clone to successfully imitate him... And there was no way someone as intimate with him as Chigara would fall for a trick like that so easily..."
    "He had to calm his racing mind. For now, he had to escape detection and alert ship security... O-or something." 
    "He racked his brain for what the proper protocol for dealing with the doppelganger of the ship's captain was, but for some reason he couldn't remember being taught anything about it during his training at the Space Force Academy. Perhaps he had slept through that one."

    play music "Music/Anguish.ogg" fadeout 1.5

    #Captain's quarters
    scene bg captainscabin with dissolve
    $dshow(34210,xpos=0.2)
    "Of course, the ship's design had left open a number of secret escape routes he could use to leave his room."
    "A warship was an inherently dangerous locality, and so a large number of concealed passageways crisscrossed the ship so that the crew would not be stranded in the event the ship lost structural integrity."
    "Shields slowly opened his closet and tore off the carpeting below, exposing an access gate to a tunnel leading to deck 0. To his relief, the gate still accepted his commands after he swiped the ID chip located on his sleeve on the security scanner."
    $dshow(36000,xpos=0.2)
    "He opened the gate and motioned for Claude to follow him."

    #Hall way
    scene bg hallway with dissolve
    play music "Music/Destinys_Path.ogg" fadeout 1.5

    $dshow(34210,xpos=0.5)
    "After climbing down the tunnel, the pair dropped down from the ceiling, onto the floor of the hall way. Shields immediately turned to Claude and interrogated her for answers."
    kay "It seems like you have a better idea than I do about just what in hell's name is going on here... I want answers, doctor!"
    $dshow(34010)
    cla "T-teeheehee... W-well, this is a surprise... "
    cla "You really don't remember anything?"
    kay "I can remember everything just fine! I'm Captain Kayto Shields, of the assault carrier Sunrider! We arrived at Cera yesterday to take part in the critical operation to liberate our homeworld from PACT loyalist forces in conjunction with the Alliance Combined Fleet--"
    cla "A-ah... But can you remember what happened \"after\" that?"

    #CG mess hall party
    scene messhallparty1 with dissolve

    kay "Uhh... After we arrived at Cera... I spoke with the ryder team in the mess hall... Then I returned to my office to do some paperwork... And then the next thing I knew, I was in bed with you!"
    cla "Ara... So you have no memory of what happened after the operation?"
    kay "What the hell are you talking about!? How would I know what happened after! The operation hasn't even begun yet!"
    cla "Huu..."
    cla "It appears you're suffering some memory loss thanks to your first temporal translocation. But don't worry, in just a few hours, all your memories of what happened will return!"
    "Shields' brain spun at a disturbingly high frequency at what Claude was implying."
    "Temporal translocation? Memory loss?"
    "He had known Claude was a ditz, but this was on an entirely different level from her usual antics!"
    "There was no question something out of the galaxy was happening though. He had just witnessed his body double flirting with Chigara as if it was the most casual thing in the world."
    "He closed his eyes and tried his best to remember just how he had got here..."

    play sound "sound/static.ogg"

    #Liberation Day massacre CGs
    $image_speed = 0.2
    scene black
    show dronedrop1:
        xalign 0.5
        yalign 0.3
        pause image_speed
        "CG/dronedrop5.jpg"
        pause image_speed
        "CG/dronedrop6.png"
        pause image_speed
        "CG/dead2.jpg"
        pause image_speed
        "CG/swornenemies2.jpg"
        pause image_speed
        "CG/kaytoend2.jpg"
        pause image_speed
    
    pause image_speed*6
    scene bg hallway
    $dshow(34210)
    "Those images again..."
    "Bloody flashes of horror flashed in his head. He had no idea where they took place or when..."
    "But he knew Chigara was somehow involved..."
    kay "Those aren't just images... They're my memories... aren't they?"
    $dshow(34000)
    cla "Ah, did you remember something, captain?"
    $dshow(34110)
    kay "A... massacre..."
    kay "Everything we worked for... destroyed..."
    kay "Horror."
    $dshow(34310)
    cla "Ah..."
    cla "Mah... Knowing that much, I guess I can fill you in about the rest..."
    $dshow(32310)
    cla "Three days from now, a disaster will occur at Cera which will thrust humanity into a war so devastating it will make the Neutral Rim War look like a mere playground scuffle in comparison."
    cla "I'm sure you already have a premonition, but Chigara will be the catalyst who will spark that disaster."
    cla "I've brought you here to rewrite the past to prevent that disaster from occurring."
    $dshow(34110)
    "Once again, Shield's head received another bombshell of a revelation."
    "What was Claude even saying!? \"Bring him back to rewrite the past!?\" Something like that was impossible!"
    "Suddenly, more memories played back in his head."
    
    scene white with dissolve

    #Desert
    scene bg desert
    show black:
        alpha 0.5
    with dissolve
    
    $dshow("sola armhold neutral narrow sad",behind="black") #copied from script because flashback
    
    kay "You're telling me..." 
    kay "Claude is a... TIME TRAVELLER?"
    $dshow("sola armhold neutral neutral neutral")
    sol "No..."
    sol "Far more than that."
    sol "If such an entity could be given a name... Then the closest description of her would be..."
    sol "Claude is God."
    
    scene white with dissolve

    #Hallway
    scene bg hallway with dissolve
    $dshow(34110)
    "Shields rubbed his spinning head and fought back the mounting nausea."
    "While his understanding of what had... or \"will\" happen was still foggy, like trying to recall a dream he had seen months ago, Claude's seemingly impossible explanation seemed validated by what fragmentary memories he still retained."
    kay "Okay then... We alert ship security and then detain Chigara. Problem solved, right?"
    $dshow(34311)
    cla "Actually captain..."
    $dshow(34110)
    "He shook his head at his own naivety. Of course, resolving this wasn't going to be that simple."
    "For all intents and purposes, the Kayto Shields hitting on Chigara in his office right now was the captain everyone accepted in this timeline. If he just revealed himself now, he would be the one to get detained and questioned."
    "And given his doppelganger's infatuation with the chief, he doubted that convincing him that she was a spy would be so easy... especially from inside a brig cell."
    "The fact that he had less than 72 hours to stop the massacre meant he couldn't afford to risk getting confined in the brig for the duration of the coming battle. He had to take a more... covert approach."
    kay "No... The proper protocol in such a situation would be to confine the captain's doppelganger in the brig for further questioning. Which to everyone in this timeline, would be me."
    kay "We can't afford to blow our cover. We'll have to... approach this differently..."
    kay "We recruit one person to help us. Someone we can trust. Then the three of us work from the shadows to prevent the disaster from occurring."
    $dshow(34000)
    cla "Ooh, I see. 'Andastood, captain! Then, who shall we recruit to our cause?"
    "He gave that question a long thought..."
    "That person would have to be..."

    #show screen selecting "Asaga," "Ava," "Sola," or "Icari"
    #Player selects from one of four girls.
    $ menu_choices = [
                     ["Asaga","select_asaga","Asaga"],
                     ["Ava","select_ava","Ava"],
                     ["Sola","select_sola","Sola"],
                     ["Icari","select_icari","Icari"],
                     ]
    show screen decision
    pause

label select_asaga:
    
    $ girl = "Asaga"

    #Asaga

    kay "(Nobody else was going to believe a whacky story like this... Except for Asaga!)"
    "The ship's ace pilot, and self-proclaimed hero of justice would of course be more than eager to join this secret mission to save the galaxy. No other person in Shields' entourage had a bigger enthusiasm for crackerjack adventures."
    kay "(All right, I've my decision!)"
    kay "We're going to recruit Asaga. Come on, let's go find her!"
    $dshow(36011)
    cla "Oh! Okay, let's go~"
    stop music fadeout 1.0
    hide claude with dissolve

    #Hangar - "T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    
    scene bg hangar with dissolve
    
    "Knowing Asaga, she would most likely be in the hangar, practicing in the simulator."
    "Shields and Claude snuck onto the floor of deck 2, and headed to the Black Jack, hidden amongst the steel frames of the ryder bays."
    "Sure enough, they found Asaga hanging out around her ryder with a distant face."
    $dshow(514)
    asa "... ... ..."
    asa "(What was I doing... I've been losing my temper so easily lately... I hope Sola doesn't start hating me...)"
    asa "(I'll have to apologize to her later... A-after all, Sola's the only person I have left now...)"
    "Shields whispered to Asaga, cutting into her thoughts."
    kay "Psst! Asaga! Over here!"
    $dshow(1121)
    asa "E-eh? C-captain?"
    $dshow(234)
    asa "Is... something the matter?"
    kay "Yeah! I need your help! I-it's kind of... an emergency! The safety of the ship... no... the entire galaxy is at stake!"
    $dshow(2000)
    "Those were the only words needed to snap Asaga out of her doldrums."
    asa "O-oh! Right, I'll be right over!"

    #wipe
    scene black with horizontalwipe
    scene bg hangar with horizontalwipe
    $dshow(34210,xpos=0.3) #dshow now remembers previous sprite locations
    $dshow(2000,xpos=0.7)
    "Asaga joined the two time travelers in a secluded corner of the hangar. The trio whispered to each other."
    asa "So? What's the situation, capt'n?"
    "Shields thought to himself as to how best explain the obviously very convoluted situation to Asaga."
    kay "It turns out you were right after all, and Chigara really is a prototype. I had the doctor here run a more detailed biometric scan and there's no question about it anymore. She really was a spy all this time!"
    $dshow(2120)
    "Asaga's eyes lit up with excitement."
    asa "I-I... I knew it! S-somehow I could feel it in my gut, you know..."
    $dshow(432)
    asa "I'm glad... it wasn't just me going crazy..."
    asa "So, are you going to detain her?"
    kay "That's the problem... We can't do anything which will tip off the Prototypes that we're on to them."
    kay "Everything I've just said is top secret, spoken between just the three of us, okay? In fact, I'll just play along with Chigara like I've done in the past. We'll be working in the shadows to unravel their plot, but publically, we're all still being fooled."
    $dshow(2100)
    asa "U-understood, capt'n!"
    $dshow(630)
    asa "So, do you know what exactly the Prototypes plan to do?"
    kay "That is..."
    kay "(Now this was where things get really complicated...)"
    kay "Three days from now, we'll have defeated PACT and liberated Cera. But the whole thing's a trap to gather Admiral Grey and the entire Alliance military leadership all into a single victory celebration, where the Prototypes will spring their trap and massacre everyone. The ringleader of the trap will be Chigara."
    $dshow(430)
    asa "I see... I see..."
    asa "So basically, we have three days to stop this mass assassination from happenin', without tipping the Prototypes off that they've been found out?"
    kay "Yeah, that's basically the situation."
    $dshow(200)
    asa "All right! This sounds exactly like the plotline to some spy film! Sign me up, capt'n!"
    "Shields sighed in relief at how easily Asaga just accepted the situation. If it had been anyone else, no doubt they would have had a mountain of questions and doubts."
    "He was right in trusting that Asaga would be up to the task."
    $dshow(350)
    kay "All right..."
    "Now, he had to put their next course of action into motion. Unfortunately, he hadn't given this part much thought himself. It looked like he would just have to come up with something on the fly based on the fragmented memories he had of the chain of events which led to the Liberation Day Massacre."
    kay "According to our intel, Chigara will enter the Prototypes' mindstream tomorrow, during the Battle for Cera. It will be at that moment when she receives a neural message which will brainwash her into carrying out the assassination."
    kay "We must take every action to ensure that she does not enter the mindstream."
    kay "(Seems like a simple enough solution...)"
    kay "(From what I can remember, Chigara as she is now would be utterly incapable of killing a single insect, much less a room full of people. The sole cause of Chigara's actions that day was her body being controlled by the leader of the Prototypes, who we had all presumed to have died on the Nightmare Ascendant.)"
    kay "(If we were to simply prevent Chigara from being mind controlled, then the massacre would never happen...)"
    $dshow(240)
    asa "I see, I see..."
    asa "So right now, she's like a sleeper agent, who doesn't even realize she has a secret mission to assassinate the Alliance military leadership?"
    kay "Yeah, that's how it is."
    asa "Understood, captain! Then I'll keep my eye on her and make sure she doesn't try communicatin' with the other Prototypes!"
    $dshow(222)
    asa "... ... ..."
    asa "Eh-heh..."
    asa "I'm glad..."
    kay "Asaga?"
    asa "... ... ..."
    $dshow(33,blush=True)
    asa "All this time... I was... afraid. That Chigara was going to take you away forever..."
    
    $dshow(233,blush=True)
    
    asa "I thought for sure you were gonna get fooled by her... Aah, I guess I wasn't giving you enough credit, eh, capt'n? Hah-hahaha..."
    asa "... ... ..."
    asa "(All right.. Here's the big chance I've always been waiting for... Y-you can do it, myself!)"
    $dshow(3112,blush=True,ypos=1600)
    asa "Hey, capt'n... Does this mean you trust me?"
    kay "Asaga?"
    "Suddenly, more memories flashed by. This time, the images playing back in Shields' head didn't cause pain."
    "Instead, they filled his heart with ease."

    #Helives CG
    if legion_destroyed:
        show helives:
        show black:
            alpha 0.5
        with dissolve
    else:
        show helives_nopatch
        show black:
            alpha 0.5
        with dissolve

    "A warm embrace..."
    "The feeling of relief when he heard her voice over the comm in that lifepod..."
    "It was Asaga who had found him out there, drifting in space..."
    "Even though the details were still fuzzy... He could sense that this girl loved him the most out of all the girls on board this ship."

    hide helives
    hide helives_nopatch
    hide black
    with dissolve
    
    #Hangar
    kay "Of course I trust you, Asaga..."
    kay "You were always here, watching my back..."
    $dshow(635,blush=True)
    asa "A-ah... Eh-heh..."
    asa "(H-heeeehhhhh!?!?! What the hell is up with this sudden development!? It feels like the capt'n totally just forgot about Chigara!)"
    asa "(Man, does this mean that he was just acting lovey-dovey before with Chigara to mess with the Prototypes all this time? Uwa... He sure got me good with that act...)"
    $dshow(555,blush=True)
    asa "(I feel like a total idiot now...)"
    $dshow(251)
    asa "Eah, that sure is a ton off my back!"
    $dshow(421,blush=True)
    asa "Hey capt'n... After all of this over..."
    asa "Let's ride off into the sunset together... big kiss and all... just like in the movies. All right?"
    $dshow(34010)
    cla "Arara... Asaga's sure gotten bold, eh~"
    $dshow(34210)
    $dshow(4010)
    asa "O-of course I have! Besides, the capt'n said he trusts me, right!? So what's the big problem!? What, ya have a problem!? Eh!? Well, do ya!?"
    kay "Asaga..."
    $dshow(2121)
    play sound "sound/warning.ogg"
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    "But before he could answer Asaga's feelings, the klaxon sounded."
    "The hangar crew sprang to action as the ship went into condition red. Men and women readied the ryders for immediate action."
    kay "Shit... I forgot..."
    $dshow(2120)    
    asa "Ah, crap! Gotta sortie!"
    $dshow(513,cry='comiccry')
    asa "I just confessed my love too! Eeaaaahh!!! I just raised my own death flag!!!!"
    "Asaga looked around in a panic."
    $dshow(32311)
    cla "Forget about that now! Capt'n, we better make ourselves scarce!"
    kay "Okay! Asaga... Stay safe out there!"
    $dshow(2011)
    "Shields' words managed to calm Asaga down."
    asa "All right! I'll be back!"
    "With that, Claude and Shields tore away from the hangar."
    $reset_sprites() #reset xpositions to default. not required but useful
    
    jump firstbattleofcera

label select_ava:

    $ girl = "Ava"

    kay "(Naturally, the ship's XO would be the best person to turn to for help in this situation.)"
    kay "Okay, we're going to Ava."
    $dshow(34310)
    cla "Uh... Are you sure 'bout this, capt'n? Knowing that stick in the mud woman, she'd probably be the first person to report you to security and lock you up in the brig."
    kay "No... Out of everyone on board this ship, there's no one else I trust more. Besides, she's been trying to convince me the past month that Chigara is a spy, and now I'm going to go to her and tell her she's been right all this time."
    kay "We need Ava's help more than anyone else. She's the highest ranked officer onboard this ship, aside from me. Not to mention she's good at getting things done."
    cla "Well if you say so, captain... But just to be on the safe side, I think you should meet her without me."
    $dshow(34110)
    kay "That'll... probably be for the best."
    kay "(After all... seeing you would probably put her in a bad mood...)"
    "With that, Shields set off to the usual place to find Ava..."
    
    stop music fadeout 1.5

    #Bridge - "T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    scene bg bridge with dissolve
    
    $dshow(13000)
    "Sure enough, he found Ava working at the bridge."
    "He tried to walk into the bridge as casually as possible and approached her..."
    kay "Hey... uhh..."
    kay "Psst! Ava!"
    $dshow(10320)
    "Ava turned in irritation at Shields' unusual way to greeting her."
    ava "Is there a problem, captain?"
    kay "Yeah... uhh... come over here!"
    "Shields ushered Ava into a secluded corner of the bridge."
    $dshow(13000)
    ava "Captain. What appears to be the problem?"
    kay "Well uhh..."
    "Honestly, he had no idea where to even begin."
    kay "(Hello Ava, my glorious childhood friend-turned-executive officer, I have just traveled back in time to prevent a future massacre from happening! Oh, by the way, don't trust anything the other guy who looks identical to me says, because he's heading all of you guys off to a great big disaster!)"
    kay "(Yeah right... Like I could ever just say that...)"
    $dshow(13311)
    ava "Captain...? You appear to be in... a great amount of thought..."
    ava "I was in fact planning to visit you in your office sometime after finishing my shift to ensure that you were giving the battle plans due diligence."
    kay "(Ah yes... I still remember that little incident...)"
    kay "This is going to be difficult to believe. But I swear, upon that day in advanced academy when we tried to scrub the entire pool clean between just the two of us, that I am the Kayto Shields you grew up with from childhood, understood?"
    $dshow(10321)
    ava "I... see...?"
    $dshow(10010)
    "Shields took Ava's shoulders and whispered into her ears."
    kay "First Officer Crescentia, what I am about to tell you is a highly classified matter which directly affects the security of the entire galaxy. And as much as I would like to say this is a joke, I am being completely honest."
    kay "I have traveled in time, from the future, to warn you of an event which will occur shortly after our successful liberation of Cera."
    kay "During the victory ceremony, Chief Engineer Ashada will fall under the control of the Prototypes, and orchestrate the assassination of every major Alliance military leader at the ceremony, including Admiral Harold Grey. This event will spark an intergalactic war between the Solar Alliance and PACT, which will threaten the existence of humanity as we know it."
    kay "There is currently another Kayto Shields, frolicking with the Chief Engineer right now, in my office. This is the Kayto Shields that you know as your captain in this timeline."
    kay "You must do everything in your power to prevent the Liberation Day Massacre. Starting with the detention of Chief Engineer Ashada."
    "Ava swallowed every word without a hint of surprise in her eyes."
    "Yet Shields knew that every word of what he had just said sounded like a big prank."
    "Finally, Ava nodded."
    $dshow(13300)
    ava "Very well, captain. I roughly understand the situation."
    "Shields sighed in relief."
    kay "I'm... very glad you believe me. Honestly... if our positions had been reversed... I...."
    ava "Indeed. Your final order to detain the ship's Chief Engineer appears quite... difficult to carry out, as my current superior officer has flatly denied my request that the she be detained. That would be you."
    ava "If I go to him now and repeat the same demand, I doubt the outcome would be any different. And of course, if I unilaterally detain her, I imagine the fallout would be quite grave. As circumstances currently are, he may strip me of my rank for insubordination."
    $dshow(13000)
    "Ava certainly did have a point. As long as the highest ranked officer on board the ship protected Chigara, there wasn't anything the XO could do about it. Shields pulled his hair in frustration at his own past self's stubbornness."
    "For a moment, he was overcome with the desire to march up to his office and smack some sense into his other self."
    $dshow(13300)
    ava "First, I will head to Deck 0 and confirm whether there truly is another Kayto Shields in your office right now. You will escort me there and stand outside in the hallway while I speak to him inside. Once I have verified that there are indeed two copies of you in this universe, I will make what preparations I can to stop the Prototypes' plot."
    $dshow(13000)
    kay "All right, sounds like a plan."
    "For once, Shields' heart swelled at having such an effective executive officer. He should have appreciated the work she did for him..."
    "Upon looking back at how he had treated her, his heart ached with regret. She had been right all this time about Chigara, but he opposed her at every turn. He had even dredged up his past relationship with her as an excuse to defend Chigara..."
    "He... had to apologize. Only with the benefit of hindsight did he now know how wrong he was..."
    "The two of them entered the lift and headed up to Deck 0."

    #Hallway
    scene bg hallway with dissolve
    
    "Shields stood outside his office while Ava spoke with the other Shields inside."
    "After a brief moment, she emerged, her face grave."
    $dshow(10000)
    ava "... ... ..."
    $dshow(10310)
    ava "A part of me suspected that this was merely an elaborate prank."
    ava "But I see that you are the real deal, Kayto Shields."
    ava "... ... ..."
    ava "I imagine you will not tell me just how you managed to travel back in time?"
    kay "I'm afraid not..."
    kay "(You uhh... wouldn't want to know anyways...)"
    ava "Very well. Perhaps I am better off in the dark in regards to such dangerous matters."
    ava "But I believe you are telling the truth. There can be no other explanation as to why you would suddenly change your position on the Chief Engineer, aside from the fact that you are indeed from the future. And do not believe you are some body double impersonating the Kayto Shields I know either."
    ava "But the situation is no better, as I am utterly incapable of convincing the current captain of this ship to change his mind."
    $dshow(10010)
    kay "... ... ..."
    kay "About that... Ava..."
    kay "Uh... I'm not sure how much it means to you given the circumstances..."
    kay "But I'm sorry. For how I just treated you in the office right now. And before that too, when you tried to convince me to detain Chigara..."
    $dshow(13300)
    ava "Captain? It hardly makes sense to apologize for the actions of another individual you have no control over, regardless of the fact that he is your identical clone."
    $dshow(13000)
    kay "No... The guy in there is still me. And I feel ashamed to even look at him."
    kay "He lost too much... and just wants to keep hearing that he'll come back to Cera with a new family..."
    kay "I... shouldn't have treated you so poorly. I... hurt you."
    kay "I still can't believe some of the things I said... I... was emotional... I should never have accused you of being jealous or anything stupid like that..."
    kay "You'll always be a lot more than just my executive officer, Ava. I... can't put into words how much I regret saying anything else..."
    $dshow(13311)
    ava "Captain... While I appreciate your honesty in admitting you were wrong about the Chief Engineer, I believe there is a time and a place for anything further. And that moment is not now."
    ava "We appear to be in the midst of a conspiracy to murder the top Alliance military brass. First, we must unravel this plot before deciding on anything else."
    kay "(Heh... Spoken exactly like Ava...)"
    kay "All right... But after all of this is over..."
    $dshow(12023)
    ava "Then... I guess we will... talk."
    play sound "sound/warning.ogg"
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    "Suddenly, the klaxon sounded, interrupting Shields' moment."
    kry "Red alert! The PACT Fleet has made its move!"
    $dshow(13110)
    ava "Shit! Now of all times!?"
    "Shields sprang to action. His past self was going to come running out the door any moment now! He had to hide!"
    kay "We'll... be in touch!"
    "He ran down the hallway and vanished."
    
    scene black with horizontalwipe
    scene bg hallway with horizontalwipe

    "As soon as he turned around the corner, Claude joined him."
    $dshow(30000,ypos=1600)
    cla "So? How'd it go?"
    kay "She believes me. But my other self's not going to be letting Ava detain Chigara any time soon."
    $dshow(34011)
    cla "Eeh... So she didn't try to toss you into the brig?"
    kay "No..."
    kay "We're... too close to ever doubt each other again!"

    jump firstbattleofcera

label select_sola:

    $ girl = "Sola"

    kay "(The only person who would ever believe this crazy story would be a fellow time traveler: Sola!)"
    "She was the most knowledgeable about lost technology out of everyone on the ship. And from what he could remember, Sola was the one who told him the truth about Claude, meaning he had less to explain to Sola compared to the others."
    kay "We're going to our resident lost technology expert. Come on, let's go find Sola!"
    $dshow(36011)
    cla "Okay, captain!"
    
    stop music fadeout 1.5

    #Crew Quarters - "T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(("T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene bg crewcabin with dissolve
    $dshow(34210,xpos=0.3)
    
    "Shields peered into Sola's quarters to check whether she was alone."
    "Thankfully, he found her sitting by herself on a table, reading a holo."
    kay "Psst! Sola!"
    $dshow(71000,xpos=0.7)
    sol "Ah?"
    "She looked up with curiosity at her unexpected visitor."
    kay "Sorry for interrupting... but we kind of have an emergency here!"
    $dshow(70221)
    sol "...is that so?"
    kay "Yeah..."
    kay "Uhh... This is going to be sudden, but I already know that you and Claude are time travelers. In fact, I'm a time traveler myself now, and I've arrived from the future, after you've explained all of this. There's another Kayto Shields in my office right now, who's the captain you know in this timeline."
    kay "We've traveled back in time, from the future, to prevent a disaster from occurring. Three days from now, after we've successfully liberated Cera, a mass assassination will occur during the victory celebration, where the entire top Alliance military leadership will be murdered by Chigara, a prototype sleeper agent."
    kay "We have to do everything in our power to prevent that tragedy from occurring, or else it'll spark a war between the Solar Alliance and PACT so huge, it'll threaten to end humanity as we know it."
    sol "... ... ..."
    "Sola took in every he said wordlessly, not even a flicker of doubt on her face."
    sol "Understood. I shall aid you in this endeavor."
    "She closed her holo and stood."
    "Shields sighed in relief. He knew that Sola was cool headed, but to actually see her readily accepting his ridiculous story without a trace of doubt brought unspeakable relief to Shields' mind. Maybe they had a-"
    "Without warning, Sola, rolled to the floor, and reached under her bunk."
    
    play music "Music/Gore_and_Sand.ogg" fadeout 0.8
    
    $dshow(70020)
    $dshow(34310)
    "Before Shields could make a move, Sola faced Claude with a pistol in her hand."
    "Shields tensed. Shit! Had he relaxed too soon!? What was going on!?"
    sol "Captain... this woman is not who you think."
    kay "S-Sola...!?"
    sol "She is working with the Prototypes!"
    "Shields backed away from Claude upon hearing this latest revelation."
    kay "What!?"
    cla "Ara..."
    "Come to think of it, he knew next to nothing about Claude, except for what he could gleam from his fragmented memories of the future. Why did she send him back to the past, and what was her goal here?"
    kay "Doc... Is Sola telling the truth?"
    cla "Mah..."
    $dshow(32310)
    cla "Partially. The Claude Trilleo currently in this universe is aligned with the Prototypes, yes."
    cla "But that was me in the past! Poor Claude's turned a new leaf now... I'm fighting for the good guys!"
    kay "Wait... so you mean there's another Claude too?"
    $dshow(34310)
    cla "Yes, just like your doppelganger in your office, there's another Claude in the sickbay right now..."
    kay "(Well, that complicates things...)"
    kay "I need some answers, doctor... Why were you working for the Prototypes during this time period?"
    cla "A simple alignment of interests, that's all."
    cla "I sought to rally the galaxy around you, just like the Prototypes. But after the Liberation Day Massacre occurred, I realized our interests diverged. That's when I left the Prototypes and took matters into my own hands..."
    kay "The Prototypes wanted what!?"
    cla "Yes, they sought to make you the leader of humanity... and to control you as a puppet, so that they would rule in your stead. But..."
    cla "Let's just say that plan never quite panned out... due to division within the Prototypes themselves."
    kay "That's... quite a lot to take in..."
    $dshow(70210)
    sol "... ... ..."
    cla "I was fine with helping the Prototypes accomplish that. But then the massacre happened..."
    
    $ menu_choices = [
                 ["All right, I trust you Claude.","select_sola_trustclaude","De acuerdo, confío en tí, Claude."],
                 ["I don't trust you yet... but we're still going to have to work together.","select_sola_donttrustclaude","No confío en tí todavía, pero aún así vamos a tener que trabajar juntos."],
                 ]
    show screen decision
    pause
    
    
label select_sola_trustclaude:
    
    stop music fadeout 1.5
    
    #"All right, I trust you Claude."
    $trusted_claude = True
    
    $dshow(34010)
    cla "Captain! Y-you trust Claude..."
    kay "You're not the only person who changed thanks to the Liberation Day Massacre... Honestly... I'm the same way."
    kay "I was completely blind. It wasn't until I had the benefit of hindsight that I realized how wrong I was in this time period."
    kay "Maybe it's the same way with you, Claude..."
    $dshow(34000)
    cla "Y-yes, captain!"
    
    jump select_sola_afterclaude

label select_sola_donttrustclaude:

    #"I don't trust you yet... but we're still going to have to work together."
    $trusted_claude = False
    
    $dshow(34300)
    cla "Huu... The captain doesn't trust poor Claude..."
    kay "Doc... You've been mysterious from the moment you set foot on this ship. You're probably acting with an ulterior motive right now, just like you always have in the past."
    
    jump select_sola_afterclaude

label select_sola_afterclaude:
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
        
    kay "Sola, you can put the gun down. No matter the circumstances, we're going to have to solve this together... We don't have the time to fight amongst ourselves."
    $dshow(70210)
    sol "Understood."
    "Sola put the gun down, but kept it holstered just in case."
    if trusted_claude:
        $dshow(34210)
    else:
        $dshow(34110)
    kay "For now, our common goal is to prevent the Liberation Day Massacre from occurring. We can worry about who was working for who after the immediate crisis has been averted."
    "Now, he had to put their next course of action into motion. Unfortunately, he hadn't given this part much thought himself. It looked like he would just have to come up with something on the fly based on the fragmented memories he had of the chain of events which led to the Liberation Day Massacre."
    kay "Chigara will enter the Prototypes' mindstream tomorrow, during the Battle for Cera. It will be at that moment when the Prototypes' leader will embed herself into Chigara's mind in order to mind control her during the victory celebration."
    kay "We must take every action to ensure that Chigara does not enter the mindstream."
    kay "(Seems like a simple enough solution...)"
    kay "(From what I can remember, Chigara as she is now would be utterly incapable of killing a single insect, much less a room full of people. The sole cause of Chigara's actions that day was her body being controlled by the leader of the Prototypes, who we had all presumed to have died on the Nightmare Ascendant."
    kay "(If we were to simply prevent Chigara from being mind controlled, then the massacre would never happen...)"
    sol "I see."
    sol "Then we must capture her within 24 hours and ensure she does not enter the mindstream tomorrow."
    sol "However, the entire situation is not so elegant, as simply removing Chigara from action during the Battle of Cera may vastly alter the course of history as well."
    kay "(Sola has a point... In fact, our ultimate liberation of Cera hinged on Chigara entering the mindstream to release Fontana's fleet from the control of the Prototypes - which was precisely the thing which we are now trying to prevent!)"
    kay "(Meaning... we have to find another way to ensure that Fontana can retain control of his fleet tomorrow, without Chigara!)"
    kay "We'll just have to make up the plan as we go. Unfortunately, I was dropped into this timeline about 2 hours ago, so we haven't had much time to formulate a detailed course of action."
    sol "Very well. I shall see what can be done to limit the Chief's movements without rousing her suspicions."
    sol "First, we must head to research and development."
    kay "The lab? Why?"
    $dshow(70121,zoom=1.2,ypos=2220)
    "Sola leaned into him and whispered."
    sol "I merely sought to distract the doctor's attention a moment while I discussed a certain matter with you."
    sol "There is still a... large problem."
    kay "Problem? W-what kind of problem?"
    sol "The... future... cannot be changed so easily."
    kay "What do you mean...?"
    play sound "sound/warning.ogg"
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    "But before Sola could continue, the ship's klaxon sounded."
    kry "Red alert! The PACT Fleet has made its move!"
    $dshow(70222,zoom=0.9,ypos=1750)
    sol "Ah-- N-not now!"
    sol "Alas... I must sortie..."
    kay "Okay. We don't have a choice. You've got to protect this ship, Sola!"
    $dshow(34310)
    cla "Captain, we best make ourselves scarce! The real you's supposed to be on the bridge! If you get discovered anywhere else during the battle..."
    kay "All right, let's go!"
    "The three of them ran out the quarter."
    $dshow(70420)
    sol "F-fare-"
    sol "No."
    sol "I shall return."
    kay "Yeah!"
    kay "Sola... come back safely!"
    $reset_sprites()
    
    jump firstbattleofcera

label select_icari:
    
    $ girl = "Icari"
    
    kay "(When I think of covert operations... the first person who comes to my mind is Icari!)"
    kay "(Not only that, but she's this ship's chief of security! Exactly the kind of expertise we'll need in a situation like this!)"
    kay "We're going to recruit Icari. We'll need her technical knowhow to figure out how to stop the massacre."
    $dshow(36011)
    cla "Okay, captain!"
    kay "Come on, she's probably in the mess hall right now."

    #Crew Quarters - "T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 63 hours until the Liberation Day Massacre, 27 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    scene bg messhall with dissolve #I'm going to assume crew quarters was a misscopy
    
    $dshow(34210,xpos=0.2)
    $dshow(40101,xpos=0.5)
    $dshow(51202,xpos=0.8)
    "Sure enough, Shields found Icari chatting with Kryska in the mess hall as soon as he entered."
    kay "The Lieutenant too huh..."
    "He pondered whether to bring Kryska into their plot as well."
    kay "(We're trying to prevent the assassination of Alliance military leaders, so Kryska would be more than eager to help out... But on the flipside, I can't risk the Lieutenant leaking word of this plot to Alliance command either...)"
    kay "(That would be the first thing a dutiful soldier like her would do... And that'll cause complications for me, since then they'll then expect to coordinate a counter-intelligence operation to thwart the assassination with the real Kayto Shields, instantly blowing my cover...)"
    "For a moment, Shields weighed whether he should bring the Alliance into their effort to stop the massacre, but ultimately decided against it."
    kay "(No... The Alliance won't be able to move fast enough... And once the truth comes out that I'm not the real Kayto Shields, I'd be finished. I'll have to stake my chances on a small covert op...)"
    kay "(Looks like it'll have to be just Icari...)"
    "Shields casually walked over to the pair."
    kay "Well, well, chatting together again so soon?"
    $dshow(41010)
    ica "What's your problem, cap?"
    ica "Soldier Boy here was just telling me some stories. Heh, got any interesting ones yourself?"
    "He leaned in close to Icari and whispered into her ear."
    kay "Sorry to cut your date short, but I need your help."
    $dshow(41210)
    ica "D-date!? I-it's not like I--"
    $dshow(41310)
    kay "Ahem. Lieutenant, I must speak to my chief of security about a private matter. Sorry for interrupting your discussion."
    $dshow(52200)
    kry "Not at all, sir."
    "Kryska, being the perfect soldier she was, stood upright without hesitation, and walked out of the mess hall."
    kry "Captain."
    kry "Talk to you later, mercenary."
    hide kryska with dissolve
    $dshow(40022,xpos=0.7)
    ica "Oy, what was that about? Is something going on?"
    "Shields took a seat next to Icari and leaned into her ear so they could speak in whispers."
    kay "We've got a problem. It threatens the security of this ship. No... more like the security of the entire galaxy."
    kay "The doc and I have discovered our Chief Engineer is a prototype."
    $dshow(40323)
    ica "O-oy...! A-are you for real!?"
    ica "I thought those tests came back negative!"
    $dshow(40222)
    kay "Sorry... that was just a lie we made to make the Prototypes think they've still got us fooled."
    kay "In reality, Chigara's a spy who's been programmed to assassinate every Alliance military leader gathered at the victory celebration if we successfully liberate Cera. Kind of like the Prototypes' insurance policy."
    kay "We've got three days to stop her before it's too late."
    $dshow(40512)
    ica "Holy damn..."
    $dshow(40523)
    ica "A-are you all right?"
    ica "I-I know you were goin' through some tough times, right...? And Chigara was always the one rooting you on... But for her to turn out like that... Damn... You must be wrecked..."
    kay "Don't worry about me... "
    $dshow(40521)
    ica "All right... Just... uhh... hang in there, captain. We'll get through this together."
    $dshow(40421)
    kay "(I can't believe her first concern after hearing that is me... I guess Icari's really an old softie after all.)"
    kay "In about 20 hours, Chigara will enter the Prototypes' mindstream during the Battle of Cera. While Chigara's inside the mindstream, the Prototypes' leader will embed her own consciousness inside Chigara, and then assume control of Chigara in order to carry out the mass assassination."
    kay "We have to detain Chigara before that so she never enters the mindstream."
    $dshow(40520)
    ica "Hey, this isn't making any sense here... How do you even know all this?"
    ica "You're pretty much talking to me as if you've seen the future or something. C'mon, there's something you're not telling me, isn't there?"
    $dshow(40420)
    kay "(As expected of Icari... Looks like her experience as a mercenary wasn't for nothing.)"
    kay "All right... You're... gonna have a tough time believing me."
    kay "But I really am from the future."
    kay "Everything I've just laid out, I've experienced firsthand. Chigara will really enter the mindstream in about 20 hours. And she will be mind controlled by the leader of the Prototypes. And she really will assassinate the Alliance's top military leaders."
    $dshow(40102)
    ica "Hahahahaaha....!"
    ica "O-oh man, you really had me going there, captain! You almost convinced me that poor Chigara really was gonna back stab us all! Geez... And I even felt sorry for you and all..."
    kay "... ... ..."
    $dshow(40222)
    "Icari's grin slowly drained from her face when she saw the light fade from Shields' eyes."
    ica "Hah... haa.... ..."
    ica "... ... ..."
    ica "Holy shit."
    ica "... ... ..."
    $dshow(40020)
    "Icari sat wordlessly, the full gravity of the situation now crushing down on her chest."
    $dshow(40522)
    ica "You really are serious..."
    ica "You... uhh... gonna explain to me... just how you traveled back in time to tell me all this?"
    $dshow(40220)
    kay "... ... ..."
    $dshow(36010)
    "Shields pointed to Claude sitting across from the table. She waved back."
    cla "Teehee~"
    $dshow(34210)
    "Icari grabbed him by his shoulders and stared into his face."
    $dshow(41212)
    ica "A-are you serious!?"
    "He nodded."
    $dshow(41200)
    ica "I always knew Boob Rockets was suspicious, but I never would have imagined she was a time traveler!"
    ica "Ahh man, suddenly, I'm getting the feeling that this is all a weird dream and I'm just about to wake up..."
    kay "Wouldn't that be a thing..."
    $dshow(41110)
    ica "... ... ..."
    $dshow(41210)
    ica "I don't suppose you know how Boob Rocket's been travelling through time?"
    kay "You'd have to ask her... Because I'm not aware of the details myself."
    ica "Okay..."
    "Icari drew a deep breath of air."
    $dshow(41000)
    ica "All right, captain. I'm in."
    $dshow(41010)
    ica "It's been a while since I've got a job this crazy. But oh, don't worry, I've seen some pretty insane shit, so I'm not gonna back out now. I'm your girl for this, captain."
    "Icari held out her hand. Shields took it."
    kay "A pleasure hiring you, Ms. Isidolde. I'm afraid I'm a man of modest means though. Be gentle on this man's life savings."
    $dshow(41012)
    ica "Heh."
    ica "Captain... For you, I'll do this pro bono."
    ica "Now come on, let's go nab our Chief..."
    play sound "sound/warning.ogg"
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    "Before Icari could make another move, the klaxon sounded."
    kry "Red alert! The PACT Fleet has made its move!"
    $dshow(41210)
    ica "Ah hell, not now!"
    ica "Shit, change of plans, captain. Looks like I gotta go. I expect the best from you out there, all right? Once we've whooped some PACT ass, I'll come back and deal with the Chief."
    kay "A-actually--"
    kay "(Shit, no time to explain!)"
    kay "D-don't mention any of this to me during the battle!"
    $dshow(41110)
    ica "'Course! Confidentiality and all!"
    ica "Now, gotta go!"
    "Icari leaped over the table and sprinted towards the hangar."
    hide icari with dissolve
    $dshow(32310)
    cla "Captain, we best make ourselves scarce! The real you's supposed to be on the bridge! If you get discovered anywhere else during the battle..."
    kay "All right, let's go!"
    $reset_sprites()
    
    jump firstbattleofcera

label firstbattleofcera:

    if renpy.music.get_playing() is None: #useful when jumping back here
        play music "Music/Gore_and_Sand.ogg" fadeout 1.5

    scene bg hallway with dissolve
    "Shields' recollection was coming back..."
    "It was about this time when the PACT Fleet advanced, choosing to launch a frontal attack using their ryders to decimate the Alliance's shield cruisers, so that their battleships could whittle down the Alliance Fleet from a distance using laser attacks."
    "Everything was happening exactly as same as before..."

    #If not Ava
    if girl != "Ava":
        "He heard Ava's voice over the ship wide intercom."
        ava "All hands, battle stations! The PACT Fleet is approaching our position!"

    $dshow(34311)
    cla "Huu... We can't let the crew see you here!"
    "Claude opened a maintenance tunnel and crawled inside."
    cla "In here, hurry!"
    $dshow(34111)
    kay "Tsch..."
    "Despite knowing that another Kayto Shields was no doubt rushing to the bridge right now, he couldn't help but feel like a pathetic coward, crawling inside a maintenance tunnel to hide through the battle."
    kay "(No... My place was on the bridge... I... have to protect everyone...)"
    "Finally, his better senses reined in his emotions. No. He just had to leave that up to [girl] and the rest of the crew."
    "He wasn't going to protect anyone by marching to the bridge right now. Shields swallowed his pride and crawled into the maintenance shaft."
    "Claude shut the gate, swallowing the two of them in darkness."
    scene black with dissolve
    hide claude with dissolve
    "... ... ..."
    "... ..."
    "..."
    "All Shields could hear was the pounding of his heart. Sweat dripped down his eyebrows, tickling his nose, and filling his mouth with the taste of sulfur."
    "In a surreal moment, he heard his own voice over the intercom."
    kay "All hands, prepare for anti-ryder combat!"
    
    play sound "sound/flakguns_deep.ogg"
    
    "Shortly afterwards, the dull drumbeat of the Sunrider's flak guns echoed through the tunnel."
    "The hull creaked as shrapnel from intercepted missiles harmlessly bounced off the ship's armor."
    "Every passing moment felt like torture... Shields had grown so accustomed to being in command that the idea of being helpless, trapped inside a hole, churned his stomach..."

    #Change based on partner
    "He closed his eyes... and prayed that [girl] would be safe..."
    
    if girl == "Asaga":
        show asagacockpit:
            alpha 0.5
        with dissolve
        "He would always be able to see the Black Jack on the battle map... When things got too dicey, he would be able to order her to turn around..."
    if girl == "Icari":
        show icaricockpit3:
            alpha 0.5
        with dissolve
        "He would always be able to see the Phoenix on the battle map... When things got too dicey, he would be able to order her to turn around..."
    if girl == "Sola":
        show solacockpit1:
            alpha 0.5
        with dissolve
        "He would always be able to see the Seraphim on the battle map... When things got too dicey, he would be able to order her to turn around..."
        
    "But what would the Kayto Shields on the floor of the bridge right now do? Did he even care for her as he did?"
    scene bg tunnel with dissolve
    
    "Suddenly, Ava's shrill voice on the intercom broke his thoughts."
    ava "All hands, BRACE FOR IMPACT!!!"
    play sound "sound/quantumtorpedo.ogg"
    play sound1 "sound/explosion4.ogg"
    
    show layer master at tr_xshake
    
    "Shields did his best to grip the walls of the tunnel, but was still thrown completely to flat on his face against the massive shockwave."
    "The tunnel bent and fuses burst, covering him with sparks."
    "He knew this sensation... A hit that size could only mean that a PACT Battleship's quantum torpedo had gotten past their flak net and scored a direct hit."
    "Goddamnit... What the hell was that buffoon on the bridge doing!?"
    "He wiped the blood from his lips and pulled himself up."
    "Smoke seeped in from the gate, meaning that the hallway outside was now on fire. Shields cautiously opened the gate by a sliver and peeked outside, only to come face to face with a raging inferno."

    play sound "sound/fire.ogg"

    #Burning hallway
    scene bg hallway_damaged with dissolve
    
    "Crewmen pulled flame retardant hoses from the walls, and struggled to put out the fire."
    "Shields spotted a technician lying on the floor nearby, his uniform matted with blood. The fire approached him, threatening to swallow him whole."
    kay "(If I jump out now... I can still save him...)"
    kay "(I have to do something... but it would mean blowing my cover...!)"
    
    stop sound fadeout 1.5
    
    $ menu_choices = [
                     ["Save the crewman.","savethecrewman","Salvar al tripulante."],
                     ["Don't blow cover.","dontblowcover","No arruinar la cobertura."],
                     ]
    show screen decision
    pause
    
label savethecrewman:
    
    $ coverblown = True
    
    #Save the crewman
    kay "(I'm... still the captain of this ship!)"
    kay "(I can't hide in this hole like a coward when my crewmen are risking their lives out there!)"
    "With that, Shields pushed the gate open and left the tunnel."
    $dshow(34310,xpos=0.2)
    cla "A-ah--! Captain, where are you-"
    kay "I'm not going to let a member of this ship die!"
    $dshow(34311)
    cla "Ahh... Captain..."
    hide claude with dissolve
    "Ignoring Claude's protests, Shields pulled a hose from the wall and battled the flames which were fast approaching the wounded technician."
    "When Shields finally reached him, he knelt down and checked his vitals."
    kay "(Still alive... Good...)"
    "Shields hoisted the technician up and carried him towards the other crew."
    cre1 "C-Captain!?"
    "A deckhand's eyes widened in shock as the captain of the ship emerged from the flames and passed him an unconscious crewman."
    kay "Make sure he gets to sickbay! That's an order, sailor!"
    "The deckhand's training took control, and he snapped to attention."
    cre1 "Sir!"
    "Shields gritted his teeth. He had to lead the damage control operations here!"
    play sound "sound/chainsaw.ogg"
    "Without warning, the ship shook again. This time, he heard the sound of mechanical sawing, as if something was cutting through the hull of the ship..."
    kay "What the--"
    show drone_flames with dissolve
    play sound "sound/dronehitfloor.ogg"
    pause 0.3
    play sound "sound/gatlinggun.ogg"
    "Suddenly, the ceiling gave away, and a hunter drone dropped down, spraying the hall with bullets."
    "Shields barely had time to take cover behind some debris as two crewmen were cut down by bullets before his very eyes."
    kay "Hunter drones!? T-the hell!?"
    kay "Tsch..."
    
    play sound "sound/static.ogg"

    #CG Drones kill everyone at ceremony
    show dronedrop5:
        pause 0.3
        "CG/dronedrop6.png"
    pause 0.8
    scene bg hallway_damaged
    show drone_flames with dissolve
    
    "The arrival of the hunter drone triggered another memory..."
    "No! He couldn't afford to get distracted here!"
    "He had received some instruction about invasion drones during his training, but had figured they saw limited practical applications after never encountering one on the field. Indeed, this was the first time he had ever seen them deployed during ship-to-ship operations."
    kay "(Shit... This just makes my life that much more complicated...)"
    kay "(If I don't do something here, then that drone's going to massacre everyone on this deck! But right now, I'm totally unarmed...)"
    "Shields looked around, and saw a pistol lying beside a fallen crewman. It would take far more than that to down a mechanized hunter drone, but it was something..."
    
    $ menu_choices = [
                     ["Grab the pistol and attack the drone.","attackdronewithpistol","Tomar la pistola y atacar al dron."],
                     ["Grab the pistol and fall back.","grabpistolfallback","Tomar la pistola y retirarse."],
                     ]
    show screen decision
    pause
        
label attackdronewithpistol:
    $renpy.save("BAD END 1")
    #"Grab the pistol and attack the drone."
    "There were still crewmen here! He couldn't back down now!"
    "Shields gritted his teeth and rolled across the floor, picking up the pistol."
    play sound "sound/pulse2.ogg"
    pause 0.5
    play sound "sound/pulse2.ogg"
    pause 0.5
    play sound "sound/pulse2.ogg"
    "He sprayed the drone with bullets before taking cover behind the hallway's side support. They harmlessly bounced off the drone's armor plating, merely drawing its attention to Shields."
    kay "(Not enough, huh... But I've got another trick...)"
    "He remembered that the drones used a combination of thermal imaging and optical sensors to target their foes. With the raging fires, the drone's thermal sensors were probably fried and it was most likely relying solely on its optics..."
    "If he could just put up some smoke, then the drone would turn blind..."
    "He pointed his gun to a nearby pipe feeding a flame retardant hose, and took aim."
    play sound "sound/pulse2.ogg"
    "With a carefully aimed shot, he punctured the pipe, causing a stream of white gas to erupt and engulf the drone."
    kay "Here's my chance...!"
    "His confidence swelling, Shields leaped out and approached the drone, plastering it with bullets. But now that the hallway was filling with thick gas, he could no longer see either..."
    
    play sound "sound/punch.ogg"
    show layer master at tr_xshake
    
    "Suddenly, he was knocked off his feet by the drone's enormous leg. He collapsed to the floor, his ribs painfully cracking."
    kay "G-guhh!!"
    "The drone rotated in circles, clearing away the gas. Did the programmers of the drone already see through such a tactic and devise a counter measure!?"
    "Shields cursed the fool coder who made such a sadistic AI and desperately looked around for a bigger weapon..." #muhahaha
    "Despite his fractured rib cage, he painfully picked himself off the ground, his body flooded with adrenaline. He faced down the steel automaton like an naked ancient man facing down a panther..."
    "He leaped out of the way just as the drone's mini-gun started spinning, but it was too late."
    play sound "sound/gatlinggun.ogg"
    show dronedrop6 with dissolve
    kay "G-GAHH!!!"
    "In a moment of disbelief, he fell backwards, as his legs were reduced to the composition of salsa by a torrent of bullets."
    "He could only look up to see the drone approaching him..."
    
    scene white with dissolve
    play sound "sound/gatlinggun.ogg"
    "The last thing he saw was the drone's mini-gun beginning to spin once more..."
    #Auto gun sfx
    #BAD END
    scene black with dissolve
    play sound1 "sound/choirend.ogg"
    stop music
    $persistent.unlocked_endings["BAD END 1: GUNNED DOWN"] = True
    $check_for_all_endings()
    show screen bad_end1
    pause 3
    $dshow(34311)
    cla "Mou... Captain, if you had just listened to me and stayed inside the tunnel, this sort of thing wouldn't have happened!"
    cla "What's more, you seriously thought you could take on a mechanized hunter drone with just a pistol? I can't believe you passed officer's training like this..."
    cla "Try again, this time by either staying inside the tunnel, or choosing not to fight the drone!"
    hide claude
    hide screen bad_end1
    jump firstbattleofcera

label grabpistolfallback:
        
    #"Grab the pistol and fall back."
    "No matter how he considered this tactical scenario, a group of crewmen and a captain armed with nothing but pistols were no match for a mechanical hunter drone. They had to perform a tactical retreat."
    "Shields shouted orders to the other crewmen."
    kay "Everyone, fall back! Find cover! That drone'll tear you apart!"
    cre1 "S-sir!"
    "Shields and the repair crew quickly fell back, coming to an airlock gate."
    kay "(This should hold the drone back...)"

    #Hallway
    scene bg hallway_distort with dissolve
    $reset_sprites()

    play sound "sound/ghostfade.ogg"
    "Once everyone ran through the gate, Shields pounded the close button, dropping an eight inch thick wall of steel between themselves and the drone. Everyone dropped to their knees in relief."
    "Shields took the opportunity to survey the situation."
    scene bg hallway with dissolve
    kay "Any of you have heavy weapons?"
    cre1 "No sir! Fire Control Crew C, reporting for duty! All we have are side arms!"
    kay "The closest armory's 300 meters from here... Come on, let's go!"
    
    show layer master at tr_xshake
    
    play sound "sound/explosion4.ogg"
    "Just as Shields spoke those words, an ear shattering explosion shook the airlock. The steel gate dented inwards, as if it had just been pounded by a titan."
    "The drone was still armed with an anti-armor cannon... This gate wasn't going to hold it forever!"
    kay "Come on everyone! MOVE MOVE MOVE!!"
    "The crewmen and Shields ran as fast as their feet would carry them away from the gate, but it was too late...!"
    
    show layer master at tr_xshake
    
    play sound "sound/explosion4.ogg"
    "With another chest bursting explosion, the reinforced steel gate burst behind them in a massive fireball."
    kay "DUCK AND COVER!!!"
    play sound "sound/gatlinggun.ogg"
    show drone_hallway with dissolve
    "Shields slammed a young repairman who looked fresh out of school against the wall just as the drone sprayed the hall with lead."
    "He looked around. Was this their end?"
    "Tsch... If only... they had... a grenade or something...!"
    $dshow(34010,xpos=0.85)
    cla "C-CAPTAIN!!"
    "Suddenly, he saw Claude running down the hall with an enormous bazooka over her shoulder."
    kay "That's the way!"
    play sound "sound/pulse2.ogg"
    pause 0.5
    play sound "sound/pulse2.ogg"
    pause 0.5
    play sound "sound/pulse2.ogg"
    "Shields peppered the drone with small arms fire, drawing its attention away from Claude."
    "Claude knelt down to one knee to stabilize the bazooka and took aim."
    $dshow(34011)
    cla "T-they don't call me... Boob rockets... FOR NOTHING!!!"
    play sound "sound/missile.ogg"
    $dshow(34301)
    pause 0.4
    
    show layer master at tr_xshake
    
    play sound "sound/explosion3.ogg"
    "The rocket shot out from the front of the bazooka, the recoil knocking Claude flat on her back... and missed the drone spectacularly, digging a massive cavity into the ceiling of the hallway."
    "Shields hissed through his teeth."
    kay "Y-you idiot!!!"
    cla "H-huuu..."
    "Just then, a massive steel beam fell from the ceiling thanks to the force of the rocket's explosion and pinned the drone down."
    $dshow(34310)
    cla "E-eh!?"
    "Shields took the opening to roll to where Claude was lying on the floor and picked up the bazooka."
    play sound "sound/missile.ogg"
    "He took aim and scored a direct hit on the drone's control tower."
    
    show layer master at tr_xshake
    
    play sound "sound/explosion4.ogg"
    show drone_hallway
    show explosion:
        xalign 0.5
        yalign 0.5
        zoom 1.5
        easeout 1 alpha 0
    pause 1
    hide explosion
    hide drone_hallway
    with dissolve
    
    stop music fadeout 1.5
    
    "With a satisfying explosion, the drone's brain burst, spewing fire and steel in every direction. The husk of the now dead mechanical beast finally lost power and went limp."
    $dshow(34010)
    "With an enormous exhale, Shields dropped the bazooka to his side."
    
    play music "Music/Colors_main.ogg" fadeout 1.5
    
    "The other crewmen poked their heads out from cover in disbelief. Slowly, their expressions turned from white terror to exhilaration."
    cre1 "Captain! Y-you did it!!! You saved us all!!"
    cre3 "CAPTAIN! CAPTAIN! CAPTAIN!"
    "Shields suddenly realized that the crewmen chanting his name in the hallway may not be in his best interest..."
    cre1 "Anyways, what are you doing here, with Fire Crew C?"
    kay "Uhh..."
    "He looked around, now searching for the best way to beat a hasty exit."
    kay "I... have to get back to the bridge!"
    kay "G-good work, Fire Crew C!!!"
    cre1 "Did you hear that? The captain said we did good work!"
    cre2 "Of course he did, kid! We risk our necks every day to keep the ship safe!"
    cre3 "Hah! Hah! I'm gonna tell everyone in the mess hall about this!"
    hide claude with dissolve
    $reset_sprites()
    "Shields and Claude beat it while the crewmen laughed amongst themselves."
    "He looked back..."
    "Despite blowing his cover... He smiled in spite of himself."
    "He had no regrets."
    
    jump afterdefeatingdrone

label dontblowcover:
    
    $ coverblown = False
    
    if renpy.music.get_playing() is None: #useful when jumping back here
        play music "Music/Gore_and_Sand.ogg" fadeout 1.5
        
    scene black
    
    #Hide inside the tunnel
    kay "... ... ..."
    kay "(Tsch... I still had my mission to prevent the massacre... I can't afford to blow my cover here.)"
    "Shields shut the gate."
    kay "The hallway's on fire! We won't be going back out this way!"
    cla "F-follow me!"
    "Claude lead him further through the tunnel, to another gate."

    #Auxiliary control
    # show expression Text("Auxiliary control background not found",xalign=0.5,yalign=0.2,size=60) as debugtext #TODO
    scene bg engineroom with dissolve
    $dshow(34110,xpos=0.15)
    "The duo jumped off from the service tunnel, into Auxiliary Control Center C."
    "This was where redundant controls for most of the Sunrider's offensive countermeasures were located."
    kay "Tsch..."
    "A grim sight awaited Shields. Dead bodies of crewmen were scattered across the room, while consoles and machinery hissed steam."
    "The comm still echoed through the room."
    com "This is bridge, requesting helldarts at coordinates 92-19-27 stat! I repeat, this is bridge, requesting helldarts at coordinates 92-19-27! Auxiliary control, do you copy!?"
    "Even if all he could do right now was hide, he could still do this...!"
    "Shields ran over to the console and pounded in the coordinates."
    kay "One round of helldarts... coming up...!"
    "He pounded the fire button. From here, he had no idea whether his actions even did anything."
    "Did the helldarts hit? Were they all intercepted by enemy flak? Was this console even functional?"
    "His fist clenched. Without the battle map, he knew nothing!"
    "All this time, he had never realized how helpless most of the crew must feel during battle... Just performing their roles, completely blind to the overall tactical situation..."
    $dshow(32311,xpos=0.15)
    cla "C-captain, we've got a new problem..."
    "Claude opened the door to auxiliary control, revealing a gnarly sight."

    #Hallway
    scene bg hallway with dissolve
    $dshow(34110)

    "The bloody bodies of crewmen were strewn throughout the hall."
    kay "What in hell's..."
    kay "These men weren't killed by explosions. They were gunned down. What could have--"
    show drone_hallway behind claude with dissolve
    "Shields received the answer to his question when a mechanized hunter drone rolled into view."
    kay "Shit!"

    #Auxiliary control
    scene black with dissolve
    scene bg engineroom with dissolve
    $dshow(34110)
    # show expression Text("Auxiliary control background not found",xalign=0.5,yalign=0.2,size=60) as debugtext #TODO

    hide claude with dissolve
    "He slammed the door shut behind him, and threw himself and Claude on the floor."
    play sound "sound/gatlinggun.ogg"
    "Less than a moment later, the wall was punctured by a line of machine gun fire."
    kay "(Hunter drones!? Inside the ship!?)"
    "He had received some instruction about invasion drones during his training, but had figured they saw limited practical applications after never encountering one on the field. Indeed, this was the first time he had ever seen them deployed during ship-to-ship operations."
    kay "(Shit... This just makes my life that much more complicated...)"
    kay "Get baackk!!!"
    
    play sound "sound/explosion2.ogg"
    show drone_engineroom with dissolve
    show layer master at tr_xshake
    
    "Shields carried Claude back up and ran to the opposite end of the room, just as the drone fired its anti-armor cannon into the door, blowing a hole through the wall large enough for the drone to enter the Auxiliary Control Room. The force of the explosion blew the duo off their feet, their ear drums ringing."
    $dshow(34310)
    cla "C-captain...!!! H-how'd that thing get here!?"
    kay "Invasion drones! Some battleships fire torpedoes that drill through the hull of the ship, and then drop hunter drones in to take over the ship from the inside!"
    cla "I-I've never heard about this--!!"
    kay "Get down!"
    play sound "sound/gatlinggun.ogg"
    "The two clamored behind heavy consoles as the drone sprayed bullets towards them."
    kay "H-holy--!"
    "Against this onslaught of lead, two squishy humans like them were completely outmatched."
    kay "Wait a minute..."
    kay "You're... some kind of god, aren't you!? Can't you do something!?"
    $dshow(34311)
    cla "Just using my powers willynilly ain't such a good idea, capt'n!!"
    kay "Why not!?"
    cla "It's really hard to explain when a mechanized drone of death is raining down bullets on my head, okay!?"
    kay "Shit!"
    "Shields pounded the console in rage. At this rate, they were going to be turned into mincemeat!"
    kay "Isn't there something you can do!?"
    $dshow(32311)
    cla "H-huuu...! I-I can manage this much...!"
    "Claude reached into her cleavage and pulled out a small pistol. Whether she had materialized the gun using her powers, or had merely been packing heat between her boobs all this time, he had no idea."
    $dshow(34110)
    kay "Tsch..."
    "He took the pistol. A hand gun was obviously not going to even scratch the drone's armor, but it was something..."
    "Now armed, he surveyed the room for other tactical advantages..."
    "The service gate where they had entered the room was behind them... They could use it to retreat..."
    "He also noted canisters of liquid Ongessite stored on the opposite end of the room... If he could somehow get to those..."
    $ menu_choices = [
                    ["Fight the drone in the room.","fightdroneinroom","Luchar contra el dron dentro de la habitación."],
                    ["Escape back into the service tunnel.","escapeintotunnel","Escapar de vuelta dentro del túnel de servicio."],
                    ]
    show screen decision
    pause
    
label fightdroneinroom:
    #Fight the drone in the room
    
    "A plan formulated in his mind."
    kay "Stay here!"
    "He waited until the mini-gun on the drone began to glow bright red, and then rolled out from behind the console, to a generator. As he predicted, the drone momentarily paused to let its gun barrels cool off, allowing him to hide safely behind the generator when it began to spew out iron again."
    kay "Come 'ere, you piece of junk!"
    
    play sound "sound/pulse2.ogg"
    pause 1
    play sound "sound/pulse2.ogg"
    
    "He popped out from behind cover and taunted the drone closer into the room by sparkling it with small arms fire."
    "As planned, the drone's unwieldy legs got caught between the crisscross of consoles and generators as it closed in on him."
    "Shields used the opportunity to run across the room, onto an elevated catwalk, out of the firing arc of the mini-gun."
    kay "Claude, throw the Ongessite canisters onto the drone!"
    $dshow(36310)
    cla "O-okay...!"
    $dshow(34110)
    "Claude scrambled from cover now that the drone was jammed between heavy equipment and reached the storage rack."
    
    play sound "sound/mechchange.ogg"
    
    "Just as she grabbed the first canister, the drone retracted its wheels into its legs and then simply stepped over the obstacles in the room by walking around like a spider."
    kay "S-shit!!"
    
    play sound "sound/gatlinggun.ogg"
    
    "Shields ducked down as the drone spun around. Sparks sprayed all around him as the drone showered him with rounds."
    kay "(S-so much for that idea!!)"
    "He crawled away on the catwalk, using his elevated position to keep himself protected against the drone's assault."
    
    play sound "sound/punch.ogg"
    
    "Suddenly, a red canister hit the drone squarely on its control tower, making it spin its gun barrels away from him and towards its new assailant."
    $dshow(34011)
    cla "T-take that--"
    $dshow(34310)
    cla "O-ooh!!"
    "Claude realized she was standing in front of enough Ongessite to light a bonfire the size of a tree just as the drone prepared to gun her down."
    kay "Fuck!"
    "Shields drew his pistol."
    "He would only get one shot at this..."
    play sound "sound/explosion1.ogg"
    "His lips cracked into a smile when his shot penetrated the canister of Ongessite now sitting directly under the drone, imploding its softly armored underbelly with an bright explosion."
    "The drone partially collapsed as it suddenly suffered catastrophic system damage."
    kay "Claude, one more!"
    cla "Okay!"
    "She tossed another canister towards the drone."
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    "Shields shot at it in midair, forming an enormous aqua blue explosion directly next to its head."
    show drone_engineroom:
        easeout 0.5 alpha 0
        
    play music "Music/Posthumus_Regnum_Cut.ogg" noloop fadeout 1.5
        
    "The drone finally lost power, going limp while strewed across multiple consoles and generators like an enormous beached octopus."
    "Shields exhaled loudly as he dropped his pistol to the catwalk. He couldn't believe the two of them had downed a hunter drone using just a pistol and some Ongessite."
    kay "Hehheh... Hahaha...!"
    $dshow(34010)
    "They ran to each other and laughed as they embraced each other in relief."
    cla "W-we did it, captain!"
    kay "Yeah! We took that sucker down!"
    "All of a sudden, he realized what he was doing."
    kay "Ah. Ahem."
    "He awkwardly took his arms off of Claude."
    kay "Come on, let's get out of here before the repair crews show up!"
    
    jump afterdefeatingdrone

label escapeintotunnel:
    $renpy.save("BAD END 2")

    #Escape back into the service tunnel

    "He wasn't going to be able to do anything against that drone with just a hand gun! Their only option was to fall back!"
    kay "Tsch..."
    
    show white:
        alpha 0
        ease 0.2 alpha 1
        ease 0.2 alpha 0
    play sound "sound/explosion4.ogg"
    
    "Shields popped from cover and shot at the liquid Ongessite canisters. They erupted in a bright blue mushroom cloud, momentarily distracting the drone."
    kay "Come on, here's our chance!"
    
    scene black with dissolve
    
    "Shields opened the gate, only to receive a faceful of black smoke."
    "The fire on the other side of the tunnel had spread further than he anticipated! But they had no choice...!"
    "Before the drone could resume fire, Shields pushed Claude into the tunnel and climbed up himself."
    "His eyes immediately seared with pain. He covered his face with his hand, and crawled on, completely blind."
    "He had no idea where he was headed, or whether Claude was still even in front of him..."
    "Finally, he reached a gate..."
    "His consciousness fading from oxygen deprivation, he barely managed to spin it open..."
    
    play sound "sound/fire.ogg"
    scene bg hallway_damaged with dissolve
    "Instead of salvation, he only came face to face with hell fire."
    kay "G-g-gack..."
    scene black with dissolve
    "He retreated back into the tunnel, but could feel his life fading away..."
    "He no longer had any idea which direction was forwards, backwards, up, or down... All he could see was darkness everywhere. He grasped around with his free hand for a way out of the tunnel, but only felt walls all around him."
    play sound "sound/MechHeavy.ogg"
    "Suddenly, he heard the creaking of steel..."
    
    play sound "sound/explosion4.ogg"
    
    "The stress of the fire proving too much for the ship to handle, piles of steel beams buckled overhead, collapsing the tunnel with Shields still inside."
    "He was too weak to even scream when the roof of the tunnel fell down to crush him dead."

    #BAD END
    stop music fadeout 1.5
    
    play sound "sound/choirend.ogg"
    
    $persistent.unlocked_endings["BAD END 2: CRUSHED"] = True
    $check_for_all_endings()
    show screen bad_end2
    pause 3
    $dshow(32311)
    cla "Aah, this is what you get for running away into a tunnel you knew would lead straight into a fire, captain..."
    cla "I sure hope you don't become claustrophobic after reading this..."
    cla "Try again, this time by fighting the drone inside the Auxiliary Control Room!"
    stop music
    hide screen bad_end2
    jump dontblowcover
    
label afterdefeatingdrone:

    stop music fadeout 1.5
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 53 hours before the Liberation Day Massacre, 17 hours until Chigara enters the mind stream"),size=40) as tminus:
        xalign 0.5
        yalign 0.5
    pause 3
    hide tminus
    "... ... ..."
    "... ..."
    "..."
    kay "G-guuh...!"
    "Shields had enough of this... nightmarish situation!"
    "He stood and emerged from the cargo crate, taking in a huge breath of fresh air."
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5

    #Hallway - "T-minus 53 hours before the Liberation Day Massacre, 17 hours until Chigara enters the mind stream"
    scene bg hallway with dissolve
        
    "He had just spent the past six hours cooped up inside a small cargo crate with Claude."
    "The ship had shook and jostled as it engaged in evasive maneuvers and took hits, until he felt as if he was going to suffocate against Claude's voluminous body. For what seemed like an eternity, he suffered indignity after indignity while Claude seemed to thoroughly enjoy every moment of his suffering."
    "Feeling thoroughly violated, he stepped out into the outside world feeling like a man re-emerging into society after a long prison sentence."
    "The ship had now returned to condition yellow. For now, it appeared the battle had concluded."
    $dshow(30000)
    "After checking that the situation was clear, he pulled Claude from the crate."
    kay "Come on, the coast is clear."
    $dshow(34210)

    #If Asaga, Sola, or Icari
    if girl != "Ava":
        kay "Let's sneak back to the hangar to meet up with [girl]."
    if girl == "Ava":
        jump meetavaatbridge

    #Hangar
    "The two of them wandered into the hangar, lurking under the shadows of the ryder bays again."

    if girl == "Asaga":
        jump meetasagaathangar
    if girl == "Sola":
        jump meetsolaathangar
    if girl == "Icari":
        jump meeticariathangar

label meetasagaathangar:
    
    scene bg hangar with dissolve
    #Asaga
    $dshow(2000)
    "They found Asaga waiting for them beside the Black Jack's maintenance bay."
    asa "Asaga di Ryuvia, returnin' from duty, sah! Death flags have nuthin' on me!"
    kay "Heh... Welcome back. Good to see you in one piece."
    $dshow(231)
    asa "And I now have a lead, thanks to what happened during the battle!"
    "Shields remembered what Asaga was talking about. During the battle, the Liberty's shoulder maneuvering valve had fractured, sending it into an uncontrollable spin. While Chigara wasn't injured, his past self had sent her to the sickbay to be on the safe side."
    kay "We could nab Chigara while she's sleeping in sickbay... and hide her somewhere for the duration of the battle."
    kay "But we have another problem..."
    $dshow(635)
    asa "Eh? But I thought all we had to do was prevent her from entering the mindstream?"
    $dshow(35)
    kay "I... haven't quite explained the entire situation yet... Sorry."
    kay "The PACT forces under Fontana's command scheduled to reinforce the Combined Fleet tomorrow actually have been sabotaged by the Prototypes. There's a Trojan virus embedded deep in their ships' systems which will allow the Prototypes to hijack control of the ships using their hyper brain waves."
    kay "Chigara will enter the Prototypes' mindstream, attempting to disrupt their control over Fontana's ships. However, during that time, the leader of the Prototypes will embed herself into Chigara's mind, allowing her to assume control of Chigara during the award ceremony even in the case that she is defeated."
    kay "I honestly don't know the details of how the Prototypes' mindstream work, but from what I've heard from Lynn, their bodies can be controlled by their leaders at any time... Although the prototype being controlled can resist to a certain degree as well, with a strong enough force of will..."
    $dshow(3110,ypos=1600)
    asa "Eeh... I'm impressed! You're really knowledgeable 'bout the Prototypes, capt'n! I guess you've been studyin' your enemy!"
    $dshow(3010,ypos=1600)
    kay "(No... A-actually I've learned all of this through firsthand experience...)"
    kay "The problem is that if Chigara doesn't enter the mindstream... Then we'll all die tomorrow when the Prototypes assume command of all of Fontana's ships."
    kay "Unless..."
    kay "If we were somehow able to send an encrypted transmission to Fontana now, warning him of the Trojan... Then he could potentially start devising a counter measure right now... At the very least, he could pull his forces back so that the Prototypes can't use his ships against us..." #this is the same guy that swore to hunt fontana down to the ends of the galaxy?
    kay "There's an encrypted FTL communicator in my office. I could use that."
    $dshow(2000)
    asa "Oh! Then that's that problem solved, right?"
    "Shields couldn't help but feel guilty about leaving Asaga in the dark about the most important snippet of information: That he and Claude did not belong to this timeline, and so he couldn't just waltz into his office and use the comm whenever he felt like it."
    kay "(Looks like I'm also going to have to figure out a way to sneak into my office while my other self's occupied and have a little chat with Fontana...)"
    $dshow(634)
    asa "Oh, another thing..."
    asa "Uhh... So we gotta kidnap Chigara for nearly 24 hours, right?"
    asa "If we uhh... just nab her from sickbay... People are gonna realize that she's gone missing. And then, they'll come searching for her, which will just tip the Prototypes off that we're onto 'em..."
    $dshow(34)
    kay "(Asaga has a point... If Chigara just vanishes into thin air, people are going to start asking questions... We've got to keep the fact that we've kidnapped her a secret for as long as possible...)"
    kay "(How are we going to do that...)"
    
    $ menu_choices = [
                    ["We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste.","asaga_nobodyswap","Correremos ese riesgo. Tenemos que secuestrar a Chigara cuanto antes y no hay tiempo que perder."],
                    ["There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara...","asaga_bodyswap","*Hay* ciertamente un cuerpo doble que luce casi idéntico a Chigara..."],
                    ]
    show screen decision
    pause
            
label asaga_nobodyswap:
    
    $ body_swap = False
    
    #"We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste."
    $dshow(2000)
    asa "Understood, sah!"
    
    jump asaga_kidnapplan

label asaga_bodyswap:

    $ body_swap = True

    #"There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara..."
    $dshow(211)
    asa "Heheh... So we're gonna take Lynn from the brig, put her under, then swap out Chigara with Lynn in the sickbay so that nobody notices, eh? I like it!"
    
    jump asaga_kidnapplan

label asaga_kidnapplan:

    kay "(Now comes explaining the hard part... There's no other way to explain this plan out to Asaga without revealing the truth...)"
    kay "Asaga... There's also... something else I need to explain..."
    $dshow(2001)
    asa "Shoot!"
    kay "Uhh... There's... kind of... another Kayto Shields on board this ship right now..."
    $dshow(2111)
    asa "E-eh!? Ya-ya mean the Prototypes have a copy of you too!?"
    kay "Not... quite. I'm not actually the captain you know. I'm actually from the future."
    kay "That's how I know everything I just told you. To me, I'm just recounting what I've already lived through..."
    $dshow(2121)
    asa "... ... ..."
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    $dshow(1000)
    asa "EEEHHH!!!??? T-T-T-THAT'S LIKE TOTALLY AWESOME, CAPT'N!!!"
    $dshow(1021)
    asa "A real, life time traveler! Holeeee shite, I've dreamed of something like this happenin' but I never actually thought IT WOULD ACTUALLY HAPPEN!!!"
    "Asaga hopped up and down like a hyperactive girl upon receiving something she had always wanted for her birthday present."
    kay "(Ah... She's totally fine with it... There was no point in even keeping it a secret...)"
    $dshow(4000)
    asa "C-Can I get your autograph, capt'n!?"
    kay "I'm... not a celebrity, Asaga..."
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    $dshow(32310,xpos=0.2,behind="asaga")
    cla "Umm... A-actually... There's not quite the full situation either..."
    cla "There's also currently another Claude Trilleo in sickbay right now, tending to Chigara as we speak..."
    $dshow(1121)
    "Kayto and Asaga" "W-WHA---!?"
    $dshow(34110)
    kay "(Come to think of it, Claude's position in this universe is no different from me! Of course there'd also be another past Claude Trilleo wandering about in this timeline too!)"
    $dshow(34310)
    cla "So... We'll have to devise a plan... to kidnap Chigara out from under my nose without my past self realizing what's going on."
    $dshow(14)
    "Shields rubbed his head. So there was another wrinkle in this plan..."
    kay "Well, your past self's a time traveler too, right? So why don't you just walk up to her and explain the situation?"
    $dshow(34311)
    cla "Ah... Sorry capt'n... But... there are certain reasons why I can't do that... It might be related to the fabric of the universe tearing right in half. I-in fact..."
    cla "I think it'd be best if I remained out of sight of my past self for the duration of my stay here. For all our sakes."
    $dshow(34110)
    kay "(What the hell is Claude getting at here...)"
    kay "All right. Then here's what we're gonna do..."
    
    if body_swap == True:
        kay "Claude is going to go down to the brig, and pretend she's this timeline's doctor. She'll convince the guards that Lynn has contracted a nasty case of the Ceran measles and needs immediate medical attention. She'll then cart a sedated Lynn to Deck 0, handcuffed to a medical trolley."
        kay "Meanwhile, I'll go into the sickbay and distract this timeline's Claude... I'm... sure it'll be a piece of cake..."
        kay "Asaga will wait outside the sickbay, until Claude arrives with Lynn. While I'm distracting the other Claude, Asaga will sneak in, and swap Chigara with Lynn. Once you've grabbed Chigara, fall back to crew quarter 8, which is currently unoccupied. Secure Chigara there, and wait for me to arrive."

    if body_swap == False:
        kay "I'm going to go to the sickbay and distract this timeline's Claude, while Asaga sneaks in and wheels Chigara's medical trolley away. You two will take Chigara to crew quarter 8, which is currently unoccupied, and wait until I arrive."

    kay "I'll try to beat a hasty retreat as soon as I can. Once we've regrouped, Claude will use the floor access hatch to relocate Chigara to maintenance room D4, while Asaga runs to the mess hall and calls the other Kayto Shields out on the comm. I'll then use that chance to sneak into my office and send Fontana the encrypted call."
    kay "Do you get all that?"
    $dshow(36000)
    cla "Understood, capt'n!"
    $dshow(2000)
    asa "Let's roll!"
    kay "All right... Good luck!"
    
    #If blew cover and Ava's not on your side: Found out by other Kayto
    if coverblown == True and girl != "Ava":
        jump coverexposed

    #If chose to swap Lynn with Chigara: Claude goes to the brig
    if body_swap == True:
        jump kidnaplynn
        
    #If chose not to swap Lynn with Chigara: Proceed directly to Chigara's kidnapping
    if body_swap == False:
        jump distractingotherclaude


label meetsolaathangar:

    #Sola
    scene bg hangar with dissolve
    $dshow(71000,xpos=0.75)
    $dshow(34210,xpos=0.25)
    "They found Sola waiting for them beside the Seraphim's maintenance bay."
    $dshow(70111)
    sol "I have returned."
    sol "Unfortunately, I have already bungled my first opportunity to put the Chief out of commission. During the battle, the Liberty sustained a hit to its shoulder maneuvering valve, putting it in an uncontrollable path towards a PACT battleship."
    sol "While such an incident appeared a perfect opportunity to thwart the Prototypes' plans without rousing any unwanted attention, the other Claude of this timeline managed to use the Bianca's gravity gun at the very last moment to save the Liberty."
    sol "No doubt the Prototypes put the other Claude on board this ship to ensure that Chigara remains alive and can foster an intimate relationship with the other Kayto Shields."
    "I spun my head to Claude."
    kay "Is this true?"
    $dshow(34310)
    cla "Mah... Well... yes."
    cla "The old me's onboard this ship to ensure that Chigara gets as close as possible to the other Kayto Shields, so that the Prototypes figure out how to control him."
    cla "Like I said though, the whole part where Chigara guns down a roomful of people was due to infighting within the Prototypes' own ranks. That was never a part of my mission at all..."
    $dshow(34110)
    kay "All right... I understand."
    kay "Don't worry, Sola. Besides, I don't want to do something as drastic as arrange Chigara's untimely death right now. Our mission is to simply capture and hold her for the remainder of the battle so she can't enter the mindstream. We don't have to kill her."
    sol "Very well."
    sol "In that case, the situation from the battle presents an opportunity."
    kay "(I remember... After the battle, Chigara was admitted into the sickbay with minor injuries.)"
    kay "If we hurry... we could nab Chigara while she's still asleep in sickbay."
    kay "Now, Sola's still right that we can't just remove Chigara from the battle and expect everything to turn out the same way."
    "I explained to Sola my prior realization about the Trojan virus embedded in Fontana's ships."
    sol "I see. Then removing Chigara from the battle will all but guarantee our early demise at the hands of the Prototypes' fleet."
    kay "I've been giving it some thought. I could send an encrypted FTL message to Fontana warning him about the virus. That way, he can prepare a countermeasure right away to retain control of his ships. At the very least, he could pull back so the Prototypes can't use his ships against us."
    kay "To use the FTL comm though, I'll need to sneak into my office, while the other Kayto Shields is occupied somewhere else."
    $dshow(70213)
    sol "There is another matter."
    sol "If we were to simply kidnap Chigara from the sickbay, it would only be a matter of time until someone notices her disappearance."
    sol "Given the duration we must hold her, we must find a way to prevent anyone from realizing she has gone missing."

    $ menu_choices = [
                    ["We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste.","sola_nobodyswap","Correremos ese riesgo. Tenemos que secuestrar a Chigara cuanto antes y no hay tiempo que perder."],
                    ["There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara...","sola_bodyswap","*Hay* ciertamente un cuerpo doble que luce casi idéntico a Chigara..."],
                    ]
    show screen decision
    pause
        
label sola_nobodyswap:
    
    $ body_swap = False
    
    #"We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste."
    $dshow(70210)
    sol "Very well."
    kay "Okay, so here's the plan."
    kay "I'm going to go to the sickbay and distract this timeline's Claude, while Sola sneaks in and wheels Chigara's medical trolley away. You two will take Chigara to crew quarter 8, which is currently unoccupied, and wait until I arrive."

    jump sola_kidnapplan

label sola_bodyswap:
    
    $ body_swap = True

    #"There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara..."
    kay "We can put Lynn under and then swap her with Chigara in the sickbay. Unless someone were to take a really close look, nobody would be able to tell the difference until Lynn wakes up."
    $dshow(70221)
    sol "Understood."
    kay "Okay, so here's the plan."
    kay "Claude is going to go down to the brig, and pretend she's this timeline's doctor. She'll convince the guards that Lynn has contracted a nasty case of the Ceran measles and needs immediate medical attention. She'll then cart a sedated Lynn to Deck 0, handcuffed to a medical trolley."
    $dshow(36200)
    kay "Meanwhile, I'll go into the sickbay and distract this timeline's Claude... I'm... sure it'll be a piece of cake..."
    kay "Sola will wait outside the sickbay, until Claude arrives with Lynn. While I'm distracting the other Claude, Sola will sneak in, and swap Chigara with Lynn."
    kay "Once the two of you have Chigara, fall back to crew quarter 8, which is currently unoccupied. Secure Chigara there, and wait for me to arrive."

    jump sola_kidnapplan

label sola_kidnapplan:

    kay "I'll try to beat a hasty retreat as soon as I can. Once we've regrouped, Claude will use the floor access hatch to relocate Chigara to maintenance room D4, while Sola runs to the mess hall and calls the other Kayto Shields out on the comm. I'll then use that chance to sneak into my office and send Fontana the encrypted call."

    if body_swap == False:
        sol "Very well. Then the two of us shall head to the sickbay, while Claude stands by at crew quarter 8 for my arrival."

    if body_swap == True:
        sol "Very well. Then the two of us shall head to the sickbay, while Claude goes to the brig."

    kay "All right. Let's do this."

    #wipe
    $reset_sprites()
    scene bg hallway with horizontalwipe
    play music "Music/Anguish.ogg" fadeout 1.5
    $dshow(70211)

    "Sola and Shields made their way to the sickbay."
    kay "So... I'm guessing there's a reason why you sent Claude away?"
    $dshow(70210)
    sol "Indeed. There is more to this situation than you are likely aware of."
    sol "I only have an incomplete understanding of the complexities of time travel, but the thinkers of my time postulated that rewriting the course of history by traveling back in time was neither possible or advisable. For when history is changed by any appreciable degree by outside agents not belonging to the timeline, the universe they occupy will simply collapse."
    kay "W-what? Sola, that doesn't sound good..."
    sol "Indeed, our current mission appears futile, as even if we are successful in thwarting the Liberation Day Massacre, our efforts will be in vain, as this entire universe will simply cease to exist..."
    kay "But for what purpose did Claude bring me here, then!?"
    $dshow(70213)
    sol "I... do not know..."
    sol "But... perhaps... it would be best if we were to leave history unchanged."
    sol "While the Liberation Day Massacre certainly sounds like a horrific event, it simply does not compare in magnitude to the collapse of an entire universe."
    kay "Sola... But..."
    kay "(Shit...! What the hell is Claude thinking then!?)"
    kay "(Does she really have some ulterior motive for bringing me here!?)"
    $dshow(70123)
    sol "... ... ..."
    sol "I..."
    sol "I did not mean to disturb you. I am sorry."
    kay "No... Thanks for bringing this up."
    sol "... ... ..."
    $dshow(70221)
    sol "There is one more thing..."
    kay "What is it?"
    sol "I have had a vision... Of another universe..."
    sol "O-of course, leading me to speculate that there are an infinite number of other universes where the situation may be different, as it were..."
    kay "Sola?"
    kay "(I... have no idea what you're talking about...)"
    $dshow(70223,blush=True)
    sol "T-this is neither here or there... but in the particular universe I glanced at, it appeared we were--- ah..."
    $dshow(70203,blush=True)
    sol "... ... ..."
    kay "...Were?"
    $dshow(70210)
    sol "N-n-nothing at all."
    $dshow(70221)
    sol "But my translocation across two different universes does appear to suggest that perhaps even if this universe collapses, we could translocate into another universe... leading to a number of different possibilities..."
    kay "(I'm sorry... I'm not quite following this, Sola... Time travel really isn't my forte.)"
    kay "We still don't know everything about time traveling... Let's keep on, and see if we can discover what Claude's after here."
    sol "Understood..."

    #If blew cover and Ava's not on your side: Found out by other Kayto
    if coverblown == True and girl != "Ava":
        jump coverexposed

    #If chose to swap Lynn with Chigara: Claude goes to the brig
    if body_swap == True:
        jump kidnaplynn
        
    #If chose not to swap Lynn with Chigara: Proceed directly to Chigara's kidnapping
    if body_swap == False:
        jump distractingotherclaude

label meeticariathangar:

    #Icari
    scene bg hangar with dissolve
    $dshow(34210,xpos=0.25)
    $dshow(41011,xpos=0.75)
    
    "They found Icari waiting for them beside the Phoenix's maintenance bay."
    ica "I'm back. And looks like luck's on our side."
    ica "You saw what happened, right? Chigara's just been admitted to the sickbay. It'll be a piece of cake to take her in while she's sleeping for the night."
    $dshow(41411)
    "Shields remembered what Icari was talking about. During the battle, the Liberty's shoulder maneuvering valve had fractured, sending it into an uncontrollable spin. While Chigara wasn't injured, his past self had sent her to the sickbay to be on the safe side."
    kay "(The only problem is that Icari thinks I just saw all of this happening from the bridge, thanks to my prior explanation getting cut off by the battle.)"
    kay "All right. But I couldn't finish explaining the mission to you because of the interruption."
    kay "The real situation's actually more complicated. I'm actually not the only Kayto Shields in this universe. My old self is still acting as the captain of the ship right now, and he's convinced himself that Chigara is his most trusted partner."
    $dshow(40521)
    kay "Honestly, if I were the captain right now, I would have already detained Chigara myself. But the reality is that I can't afford to blow my cover, or else the other Kayto Shields will most likely throw me into the brig."
    $dshow(32310)
    cla "Ah, by the way, there's another Claude Trilleo in this universe too, tending to Chigara in the sickbay right now!"
    $dshow(34210)
    $dshow(40321)
    kay "W-wha--?"
    $dshow(34310)
    cla "Mou, isn't it obvious? My old self exists in this timeline as well, piloting the Bianca and serving as the ship's looney doctor. She wouldn't just disappear because I time warped here."
    $dshow(34210)
    $dshow(42000)
    ica "Oy, you're making my head hurt here... You mean the captain who just commanded me in battle, and the Claude I fought alongside with just a moment ago weren't you guys!?"
    kay "That's the situation, yeah..."
    $dshow(40010)
    ica "This job just keeps getting weirder and weirder... This might honestly be a new record on my \"bizarre as shit\" list."
    kay "Now you understand why secrecy is key..."
    kay "We also have another problem... We can't just kidnap Chigara and expect the battle tomorrow to play out the same way as it did in my timeline. In fact, I haven't told you why Chigara enters the Prototypes' mindstream yet."
    $dshow(40521)
    ica "Well, isn't it because she's actually a spy?"
    $dshow(40221)
    kay "No... I think Chigara isn't even aware herself that she will be used as a pawn in the Prototypes' plans."
    kay "The PACT forces under Fontana's command scheduled to reinforce the Combined Fleet tomorrow actually have been sabotaged by the Prototypes. There's a Trojan virus embedded deep in their ships' systems which will allow the Prototypes to hijack control of the ships using their hyper brain waves."
    kay "Chigara will enter the Prototypes' mindstream, attempting to disrupt their control over Fontana's ships. However, during that time, the leader of the Prototypes will embed herself into Chigara's mind, allowing her to assume control of Chigara during the award ceremony even after she is defeated."
    kay "I honestly don't know the details of how the Prototypes' mindstream work, but from what I've heard from Lynn, their bodies can be controlled by their leaders at any time... Although the prototype being controlled can resist to a certain degree as well, with a strong enough force of will..."
    kay "The problem is that if Chigara doesn't enter the mindstream... Then we'll all die tomorrow when the Prototypes assume command of all of Fontana's ships."
    kay "Unless..."
    kay "If we were somehow able to send an encrypted transmission to Fontana now, warning him of the Trojan... Then he could potentially start devising a counter measure right now... At the very least, he could pull his forces back so that the Prototypes can't use his ships against us..."
    kay "There's an encrypted FTL communicator in my office. I could use that."
    $dshow(41201)
    ica "All right. Capture Chigara so she doesn't enter the mindstream in about 14 hours. Send an encrypted FTL message to Fontana warning him about the virus. Avoid detection by the other Kayto Shields."
    $dshow(41211)
    ica "On top of all that, we've got to figure out a way to make sure nobody notices Chigara's gone missing until at least the battle begins. No doubt, the other Kayto Shields will launch a search as soon as he discovers that Chigara has vanished off the face of the ship."

    $ menu_choices = [
                    ["We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste.","icari_nobodyswap","Correremos ese riesgo. Tenemos que secuestrar a Chigara cuanto antes y no hay tiempo que perder."],
                    ["There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara...","icari_bodyswap","*Hay* ciertamente un cuerpo doble que luce casi idéntico a Chigara..."],
                    ]
    show screen decision
    pause
        
label icari_nobodyswap:
    
    #"We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste."
    
    $ body_swap = False
    
    $dshow(41411)
    ica "All right."
    kay "Okay, so here's the plan."
    kay "I'm going to go to the sickbay and distract this timeline's Claude, while Icari sneaks in and wheels Chigara's medical trolley away. You two will take Chigara to crew quarter 8, which is currently unoccupied, and wait until I arrive."
    
    jump icari_kidnapplan

label icari_bodyswap:
    #"There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara..."
    
    $ body_swap = True
    
    kay "We can put Lynn under and then swap her with Chigara in the sickbay. Unless someone were to take a really close look, nobody would be able to tell the difference until Lynn wakes up."
    $dshow(41411)
    ica "Understood."
    kay "Okay, so here's the plan."
    kay "Claude is going to go down to the brig, and pretend she's this timeline's doctor. She'll convince the guards that Lynn has contracted a nasty case of the Ceran measles and needs immediate medical attention. She'll then cart a sedated Lynn to Deck 0, handcuffed to a medical trolley."
    kay "Meanwhile, I'll go into the sickbay and distract this timeline's Claude... I'm... sure it'll be a piece of cake..."
    kay "Icari will wait outside the sickbay, until Claude arrives with Lynn. While I'm distracting the other Claude, Icari will sneak in, and swap Chigara with Lynn. Once you've grabbed Chigara, fall back to crew quarter 8, which is currently unoccupied. Secure Chigara there, and wait for me to arrive."

    jump icari_kidnapplan

label icari_kidnapplan:
    kay "I'll try to beat a hasty retreat as soon as I can. Once we've regrouped, Claude will use the floor access hatch to relocate Chigara to maintenance room D4, while Icari runs to the mess hall and calls the other Kayto Shields out on the comm. I'll then use that chance to sneak into my office and send Fontana the encrypted call."
    kay "Do you get all that?"
    $dshow(36200)
    cla "Understood, capt'n!"
    $dshow(41011)
    ica "Let's roll!"
    kay "All right... Good luck!"

    #If blew cover and Ava's not on your side: Found out by other Kayto
    if coverblown == True and girl != "Ava":
        jump coverexposed

    #If chose to swap Lynn with Chigara: Claude goes to the brig
    if body_swap == True:
        jump kidnaplynn
        
    #If chose not to swap Lynn with Chigara: Proceed directly to Chigara's kidnapping
    if body_swap == False:
        jump distractingotherclaude

label meetavaatbridge:

    #Ava

    kay "We need to regroup with Ava. Let's go."

    #wipe
    scene black with horizontalwipe
    scene bg hallway with horizontalwipe
    $dshow(34210,xpos=0.2)

    "The two of them made their way to the bridge."
    kay "(Crap... We better tread carefully... If the other Kayto Shields is still in the bridge, all hell will break loose when I wander in.)"
    kay "Claude, poke your head into the bridge and tell me if my other self is inside."
    $dshow(34000)
    cla "All right!"

    #bridge
    scene bg bridge with dissolve
    $dshow(30010)
    "Claude leaned into the bridge and looked around."
    "Sure enough, he saw Ava occupied while speaking with the other Shields."
    $dshow(36000)
    cla "No go, captain! The commander's busy talking with your other version!"
    kay "Damn..."
    $dshow(34210)
    "Shields pondered his options."
    kay "Ava would have foreseen something like this happening... Maybe she left us a clue somewhere else."
    kay "Come on, I have an idea where to search next."
    "Shields lead Claude back up to Deck 0."

    #Hall way
    scene bg hallway with dissolve
    $dshow(34210)
    
    "Shields stopped in front of the Executive Officer's quarters and swiped his command ID on the door's reader. To his relief, the gate opened."
    kay "(Good... Looks like Ava prepared ahead of time.)"
    "He snuck in and found a note on the opposite side of the door."
    ava "Pursuing a possible lead. Will rendezvous later. Godspeed."
    kay "(Ah... But Ava... you forgot to tell me just what this lead was! Tsch... This doesn't help me much...)"
    "He stepped back outside and spoke to Claude."
    kay "It looks like Ava's onto something, but doesn't quite know what yet. We'll have to proceed without her for now."
    $dshow(34310)
    cla "You know, I don't know about that woman, captain..."
    "Shields ignored Claude's doubts."
    $dshow(34111)
    kay "If I recall correctly, Chigara's in the sickbay right now."
    kay "The Liberty suffered a hit to its shoulder maneuvering valve during the battle in my timeline. If history is still playing back the same way as before, then the other Kayto Shields would have admitted her to the sickbay just to be on the safe side, despite Chigara not sustaining any major injuries."
    kay "This is the best chance we'll have at capturing her. We'll just go to sickbay right now, and take her."
    $dshow(32310)
    cla "Ah... Actually... there's another problem..."
    cla "There's also currently another Claude Trilleo in sickbay right now, tending to Chigara as we speak..."
    kay "W-wha--"
    $dshow(34311)
    cla "Mou, isn't it obvious? My old self exists in this timeline as well, piloting the Bianca and serving as the ship's looney doctor. She wouldn't just disappear because I time warped here."
    "Shields rubbed his head. So there was another wrinkle in this plan..."
    kay "Well, your past self's a time traveler too, right? So why don't you just walk up to her and explain the situation?"
    $dshow(34310)
    cla "Ah... Sorry capt'n... But... there are certain reasons why I can't do that... It might be related to the fabric of the universe tearing right in half. I-in fact..."
    cla "I think it'd be best if I remained out of sight of my past self for the duration of my stay here. For all our sakes."
    kay "(What the hell is Claude getting at here...)"
    $dshow(34311)
    cla "Captain... aren't you also forgetting about something else?"
    cla "If we remove Chigara from the battle tomorrow... Then we might not even be alive for the victory celebrations."
    $dshow(34111)
    kay "(Claude's right... If we prevent Chigara from entering the mindstream to restore control of Fontana's ships tomorrow, we'll effectively be signing our own death warrants when we're all slaughtered tomorrow by the very PACT ships which were supposed to reinforce us.)"
    kay "Unless..."
    kay "If we were somehow able to send an encrypted transmission to Fontana now, warning him of the Trojan... Then he could potentially start devising a counter measure right now... At the very least, he could pull his forces back so that the Prototypes can't use his ships against us..."
    kay "There's an encrypted FTL communicator in my office. I could use that."
    $dshow(32310)
    cla "One more thing... If Chigara just vanishes from the sickbay, it's only a matter of time until someone realizes what's happened. If the other Kayto Shields hears that his love has just up and vanished, he's going to launch a ship-wide search for her."
    $ menu_choices = [
                    ["We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste.","ava_nobodyswap","Correremos ese riesgo. Tenemos que secuestrar a Chigara cuanto antes y no hay tiempo que perder."],
                    ["There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara...","ava_bodyswap","*Hay* ciertamente un cuerpo doble que luce casi idéntico a Chigara..."],
                    ]
    show screen decision
    pause
            
label ava_nobodyswap:

    #"We'll just take that risk. We have to kidnap Chigara as soon as possible and there's no time to waste."
    
    $ body_swap = False
    
    $dshow(36311)
    cla "Understood, captain..."
    $dshow(34111)
    kay "Okay, so here's the plan."
    kay "I'm going to go to the sickbay and distract this timeline's Claude, while you sneak in and wheel Chigara's medical trolley away. You'll take her to crew quarter 8, which is currently unoccupied, and wait until I arrive."

    jump ava_kidnapplan

label ava_bodyswap:
    
    #"There *is* a certain body double sitting in our brig right now who looks almost identical to Chigara..."
    
    $ body_swap = True
    
    kay "We can put Lynn under and then swap her with Chigara in the sickbay. Unless someone were to take a really close look, nobody would be able to tell the difference until Lynn wakes up."
    $dshow(36311)
    cla "Understood, captain..."
    $dshow(34111)
    kay "Okay, so here's the plan."
    kay "You go down to the brig, and pretend you're this timeline's doctor. Convince the guards that Lynn has contracted a nasty case of the Ceran measles and needs immediate medical attention. Then cart a sedated Lynn to Deck 0, handcuffed to a medical trolley."
    kay "Meanwhile, I'll go into the sickbay and distract your other self... I'm... sure it'll be a piece of cake..."
    kay "While I'm doing that, sneak into the sickbay, and swap Chigara with Lynn. Once you've grabbed Chigara, fall back to crew quarter 8, which is currently unoccupied. Secure Chigara there, and wait for me to arrive."

    jump ava_kidnapplan

label ava_kidnapplan:

    kay "I'll try to beat a hasty retreat as soon as I can. Once we've regrouped, you'll run to the mess hall and call the other Kayto Shields out. Distract him, while I sneak into my office and contact Fontana on the FTL comm. We'll then regroup back at crew quarter 8, and relocate Chigara to maintenance room D4"
    kay "Do you get all that?"
    $dshow(36011)
    cla "Understood, capt'n!"
    kay "All right... Good luck!"
    
    #If blew cover and Ava's not on your side: Found out by other Kayto
    if coverblown == True and girl != "Ava":
        jump coverexposed

    #If chose to swap Lynn with Chigara: Claude goes to the brig
    if body_swap == True:
        jump kidnaplynn
        
    #If chose not to swap Lynn with Chigara: Proceed directly to Chigara's kidnapping
    if body_swap == False:
        jump distractingotherclaude

label coverexposed:
    
    ##IF SHIELDS EXPOSED HIS COVER BY SAVING THE CREW AND AVA IS NOT PARTNER

    #Office
    scene black with dissolve
    scene bg office with dissolve
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5

    "Meanwhile..."
    show kayto with dissolve:
        xpos 0.25
    "The other Kayto Shields sat in his office, trying to mind the battle plans for tomorrow's battle. However, his thoughts couldn't help but wander to Chigara, who was currently resting in sickbay."
    "Perhaps he should pay her a visit sometime before the battle..."
    
    play sound "sound/doorbell.ogg"
    
    "His doorbell rang."
    kay "Come in."
    $dshow(14000,xpos=0.7)
    ava "Captain."
    kay "Is something the matter, Ava?"
    $dshow(12013)
    ava "Ahem... I've come to report... a truly strange anomaly on board this ship..."
    kay "An anomaly? Of what sort?"
    $dshow(13300)
    ava "You're going to have a hard time believing this... But I heard rumors circulating amongst the crew that you were at Deck 2 during the previous battle."
    ava "...And that you singlehandedly took down a drone and saved an entire damage control team."
    kay "What? I've heard some crazy rumors, but that one's new..."
    ava "During the battle, we were indeed struck by an experimental PACT weapon which introduced a hunter drone within the ship. Security has examined the wreckage of the drone and have confirmed that it was PACT-made. I have summarized the incident in the latest report on your desk."
    "Ava eyed the large stack of unread reports sitting beside him."
    kay "(Crap... Haven't... gotten... to that one yet...)"
    ava "Concerned by the rumors circulating amongst the crew and the findings of our security team, I took the liberty of examining the drone on security footage. And I found this."
    show kayto yell with dissolve
    "Ava handed him a holo containing a video. His jaws dropped when he saw its contents."
    "It was... him! And Claude! Or at least two people who looked identical to themselves, wandering about the ship."
    kay "What in hell's name..."
    show kayto with dissolve
    $dshow(10300)
    ava "Indeed, I was shocked beyond words as well when I discovered this revelation."
    ava "It appears there are two intruders on board this ship, who have impersonated you, as well as our acting medical officer. Their purpose... appears unclear."
    "Shields stood from his chair, his heart now pounding."
    kay "It could be a Prototype plot. Apprehend these two intruders immediately."
    kay "Put security on high alert. Review all of our security logs in search of these... doppelgangers. I want our marines put on armed patrols throughout the ship, but they are to capture the intruders alive."
    $dshow(14110)
    ava "Sir!"
    
    if body_swap == True:
        jump kidnaplynn
        
    if body_swap == False:
        jump distractingotherclaude

label kidnaplynn:
    
    ##IF SHIELDS CHOSE TO SWAP CHIGARA WITH LYNN
    
    stop music fadeout 1.5

    #Brig 
    scene black with dissolve
    scene bg brig with dissolve

    "Claude crashed into the brig with a medical trolley, startling the guards."
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    $dshow(33311)
    cla "W-we've got a medical emergency!"
    cre1 "Wha- Is something the matter, doctor?"
    $dshow(35311)
    cla "It looks like our Prototype prisoner's contracted a severe case of the Ceran measles. We've got to get her to sickbay on the double... before she becomes contagious."
    cre1 "W-we weren't informed of-"
    cla "Mou, lookie here, this is an emergency! Do you think we have time to file the paperwork for that?"
    "Claude loomed over the security guard."
    cla "Do you even know what catching the Ceran measles is like, sergeant?"
    cla "First, you suddenly lose bowel control... You'll be experiencing the most explosive, uncontrollable diarrhea of your life for three days... But that's not even the worst of it..."
    cla "From the third day on, hives will break out all over your body... Puss and blood will slowly leak out everywhere... If left untreated, you'll suffer permanent muscle damage, and ultimately, death."
    cre2 "Shit... The doctor's right... My niece nearly died four years ago of the same thing..."
    cre3 "That's some nasty ass shit... You sure you want to keep the Prototype here, sarge?"
    cre1 "All right, all right, you've made your point, doctor. Get her quarantined into sickbay."
    $dshow(37011)
    cla "Roger!"
    show lynn1 with dissolve:
        xpos 0.85
    "Claude approached Lynn in her cell."
    $dshow(31000,ypos=1600)
    cla "Looks like you'll be coming with me. I'm afraid you've contracted a very, very serious virus..."
    hide lynn1
    show lynn2:
        xpos 0.85
    with dissolve
    lyn "W-what? I don't feel-"
    $dshow(31010,ypos=1600)
    cla "That's what they all say, but in a few hours, you'll be painting the walls with your ass! You'll be thanking me for this later~"
    cla "I'll just sedate you a bit..."
    lyn "W-what!? F-fool! I didn't-"
    $dshow(33000)
    
    play sound "sound/depressurize.ogg"
    
    hide lynn2 with dissolve
    "Claude pushed a few buttons on the cell's controls, releasing sleep gas into the cell. Lynn's eyes lost focus and she dropped down to the floor, unconscious."
    $dshow(35200)
    "The brig's security staff secured Lynn on top of the medical trolley, handcuffing her to the railing. Claude carted her out with a smile."
    cla "Nobody asks any questions when explosive diarrhea's involved~"
    
    jump distractingotherclaude

label distractingotherclaude:
    
    stop music fadeout 1.5

    ##SICK BAY - "T-minus 52 hours before the Liberation Day Massacre, 16 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 52 hours before the Liberation Day Massacre, 16 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    scene bg sickbay with dissolve
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    
    "Shields entered the sickbay. He had to distract this timeline's Claude long enough for his partner to nab Chigara out from under her nose."
    "He grimaced to discover that Chigara was sleeping just two beds away from where Claude was working in her office. This was going to be harder than expected..."
    "But he had an idea..."
    "He pretended to walk over to Chigara and stand over her, like he was concerned for her health. As expected, Old Claude sniffed out his presence like a canine and creeped up behind him."
    $dshow(31000,ypos=1600)
    cla "Huufufu..."
    "She wrapped her arms around him from behind and put her face on his shoulder, tickling his ear with her pink wavy hair."
    kay "(G-guh... T-this woman wears too much perfume...!)"
    $dshow(31010,ypos=1600)
    cla "Oh captain... I'm afraid Chigara's still sedated..."
    cla "You'll have to wait just a few more hours until she wakes up. Ah, I can understand why you'd want her back on her feet as soon as possible..."
    $dshow(33011)
    cla "The desperate look on the maiden's face as she sneaks into your quarters at the loneliest hours of the night for one last tryst before the final battle..."
    $dshow(35000,blush=True)
    cla " \"A-ah, C-Chigara doesn't know if she'll make it back... J-just in case... I want to feel Captain... inside... before...\""
    cla "Huuufufufufu... I can imagine it all playing out like I'm watching a movie..."
    kay "(Okay... Here's my chance.)"
    "Shields slumped down as if dejected and let out a long sigh."
    kay "I just don't know, doctor..."
    $dshow(35310)
    cla "E-eh? Don't know what?"
    kay "Well..."
    kay "I'm actually here for counseling. You're this ship's acting medical officer, right? So your duties also include looking after the mental health of the ship's crew, as well as their physical health."
    $dshow(35010)
    cla "Well, yes, that's certainly true..."
    kay "I've... been wanting to talk to you, doctor. It's about Chigara. But I can't talk about it here... In front of her."
    $dshow(35011)
    cla "A-ah, o-of course! Let me just get into my office and pull the cover closed!"
    $dshow(35000)
    cla "You can tell ol' Claude anything, captain!"
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    "Claude practically pushed Shields into her office and drew a sliding wall closed, giving the both of them privacy. "
    kay "(Yes... It worked!)"
    $dshow(35010)
    cla "Now, what's the nature of the counseling you need, captain?"
    $dshow(35210)
    kay "Well... it's just that things are moving so quickly..."
    kay "It's been just over a week since we kissed for the first time, and she's already talking about things like marriage and children..."
    kay "Whenever she talks about how many babies she wants to have... I have to wonder... Is this really the life I want for myself?"
    kay "Haa... I'm ashamed to even look at myself in the mirror, doctor. I can't believe I'm having these doubts right now..."
    $dshow(35000)
    cla "Oohh... Captain, don't you worry about a thing..."
    $dshow(35010)
    cla "It's completely normal to have unexpressed doubts when your partner advances a relationship too quickly. In fact, it's only inevitable, because of the enormous amount of stress you two are under right now."
    $dshow(35210)
    kay "All she cares about is her bakery..."
    kay "I... don't even know if I'm good at baking bread."
    kay "I'm a starship captain for crying out loud, doc! I worked my ass off for this commission! But to just up and retire early for a bakery..."
    kay "But whenever she talks about that ruddy bakery, she has that dreamy look on her face and I just... argghh... I just end up going along with it every time..."
    kay "Where're my input, doc!? Lately, I feel like I'm being railroaded down a certain path without any say in what I want! It's like all my choices have just up and vanished!" #roflmao xD
    kay "Before this... I used to be a free man. I used to be able to make command decisions! I used to be able to rip up rulebooks!"
    kay "But right now... I just feel like I've been chained to the doghouse."
    $dshow(35310)
    cla "Oh dear, oh dear... Uhh..."
    $dshow(35311)
    cla "After the battle... why don't you try talking to her about this, captain?"
    cla "The root cause of your problems with Chigara is most likely the stress of the coming battle. Because you're both instinctively afraid of what may happen, Chigara may be rushing things ahead of what she may normally be comfortable with as well."
    kay "All right doc... I'll try that..."
    cla "Mah..."
    $dshow(31000,ypos=1600)
    "Claude leaned in with a gentle smile and rubbed Shields' back."
    cla "You have a lot on your shoulders, captain."
    $dshow(31010,ypos=1600)
    cla "But don't forget, if things don't work out with Chigara, there's always a lovely doctor in your sickbay willing to... alleviate your worries. Teeheehee..."
    kay "(Casually hitting on your mentally distressed patient... Doc... You're absolutely the worst!)"
    kay "(Anyways, that should have been enough time for the distraction. I better beat a hasty exit out of here.)"
    
    stop music fadeout 1.5
    
    "Just as Shields was about to call it quits, he spotted a strange looking holo next to him on Claude's shelf."
    "All of the holos on board the ship were now standard issue Alliance stock. However, this holo clearly looked to be of a different make..."
    kay "(Now what do we have here...)"
    kay "(For some reason, I have a feeling there's something important on that holo... Maybe it's related to the memories I've temporarily lost.)"
    kay "(But do I risk blowing my cover by trying to steal it?)"
    $ menu_choices = [
                    ["Try to steal Claude's holo.","stealclaudeholo","Intentar robar el holo de Claude."],
                    ["Leave the sickbay without the holo.","dontstealclaudeholo","Dejar la bahía médica sin el holo."],
                    ]
    show screen decision
    pause

label stealclaudeholo:
    #Try to steal Claude's holo.
    
    $ have_holo = True
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
     
    kay "(That holo could contain something vital to restoring the rest of my memories. I've got to get my hands on it!)"
    "Shields suddenly leaned forward and buried his head into her bosom."
    kay "All right doctor... Thanks for the chat."
    kay "I feel a lot better now."
    kay "(Tsch... I can't believe I'm actually doing this...!)"
    $dshow(35000,blush=True)
    cla "O-oh! Captain..."
    "Claude smiled ear to ear as she took the opening to stroke his hair."
    "Her attention was thoroughly diverted as Shields reached backwards with one hand and swiped her holo off the desk."
    "He hid the holo behind him as he stood."
    
    jump donedistractingclaude

label dontstealclaudeholo:

    #Leave the sickbay without the holo.
    
    $ have_holo = False
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    kay "(I better not take any risks. Claude's still a time traveler, so who knows the full extent of her powers.)"
    kay "All right doctor... Thanks for the chat."
    kay "I feel a lot better now."
    
    jump donedistractingclaude

label donedistractingclaude:
    
    kay "I should head back to work. I'll uhh... see you around."
    $dshow(35010)
    cla "A-any time, captain! L-let me open the cover-"
    kay "No need, looks like you have a lot of work to do in your office."
    
    hide claude with dissolve
    
    "Shields opened the sliding door himself and left Claude in her office, closing the door behind him."
    "As he walked out, he confirmed that their operation was a success."
    "He marched out of the sickbay, a mischievous grin plastered all of his face."

    if have_holo == True:
        jump readthroughholo
    if have_holo == False:
        jump chigarakidnapped

label readthroughholo:
    
    #IF STOLE CLAUDE'S HOLO

    #Hallway
    scene bg hallway with dissolve
    stop music fadeout 2
    "As he walked to crew quarters 8, Shields activated the holo and searched through its contents."
    kay "(Now, let's see what our past doctor has been up to...)"
    play music "Music/Anguish.ogg" fadeout 1.5

    #IF NOT SOLA ARC
    if girl != "Sola":
        "His blood went cold when he saw what was inside."
        "From what he could deduce, there were hundreds of message logs inside the holo containing Claude's reports on what was occurring on board the Sunrider ever since she first came onboard, as well as detailed instructions from the Prototypes."
        "And a medical report, proving beyond the shadow of a doubt that Chigara was indeed a prototype."
        "Suddenly, more memories played back in Shields' head."

        #Desert
        scene bg desert
        show black:
            alpha 0.5
        with dissolve
        
        $dshow("sola back neutral neutral neutral",behind="black")

        sol "I have come to suspect there is a great deal of information that our chief medical officer is hiding..."
        kay "What do you mean?"
        sol "I believe Claude was actually the one who has been relaying our movements to the Prototypes."

        #Hallway
        scene bg hallway with dissolve

        kay "(Shit... I remember now...)"
        kay "(Claude's been working for the Prototypes all along!)"
        "He searched through the remaining data inside the holo."
        "Finally, he came upon a file which only contained a cryptic message."
        "\"THE FUTURE CAN ONLY BE SAVED... BY DESTROYING EVERYTHING\""
        kay "(Well that sure sounds ominous...)"
        kay "(But what exactly does it mean?)"
        kay "(I have to hurry back to the future Claude, and confront her about this!)"
        "With that, he quickened his pace to crew quarter 8."

    if girl == "Sola":
        #IF SOLA ARC

        "From what he could deduce, there were hundreds of message logs inside the holo, containing Claude's reports on what was occurring on board the Sunrider ever since she first came onboard, as well as detailed instructions from the Prototypes."
        "And a medical report, proving beyond the shadow of a doubt that Chigara was indeed a prototype."
        kay "(This must be the holo that the old Claude used to communicate with the Prototypes back when she was still aligned with them.)"
        kay "(Damn... I can't believe she managed to keep this hidden for so long.)"
        kay "(But seeing how she claims she stopped working with the Prototypes following the Liberation Day Massacre, this holo doesn't tell me anything new.)"
        "He searched through the remaining data inside the holo."
        "Finally, he came upon a file which only contained a cryptic message."
        "\"THE FUTURE CAN ONLY BE SAVED... BY DESTROYING EVERYTHING\""
        kay "(Well that sure sounds ominous...)"
        kay "(And it's in line with what Sola's already told me.)"
        kay "(I think it's high time I finally confronted Claude about the real reason why she brought me to the past.)"
        "With that, he quickened his pace to crew quarter 8."

label chigarakidnapped:

    #Hallway
    scene bg hallway with dissolve

    "Shields knocked on the ostensibly unoccupied crew quarters while the coast was clear. He tapped the intercom and whispered."
    kay "It's me. Open up."
    "The door opened, and Shields slipped inside."

    #Crew Quarters
    scene bg crewquarters with dissolve

    $dshow(34010,xpos=0.75)
    if girl == 'Sola':
        $dshow(70310,xpos=0.25)
    elif girl == 'Asaga':
        $dshow(330,xpos=0.25)
    elif girl == 'Icari':
        $dshow(41410,xpos=0.25)
    cla "You're back! As you can see, the plan went exactly as planned." #just as keikaku
    "He saw Chigara tied up to a chair, still unconscious from the sedation."
    
    #Split three ways
        #1. Have holo and not on Sola route
        #2. Have holo and on Sola route
        #3. Don't have holo
        
    if have_holo == True and girl != "Sola":
        #IF HAVE HOLO AND NOT SOLA ROUTE

        "Despite successfully kidnapping Chigara, Shields had no cause to celebrate."
        kay "Doc... You're gonna have to explain yourself."
        "He pulled out the holo."
        kay "I found this in your old self's office."

        #Variations
        if girl == "Asaga":
            $dshow(235,xpos=0.25)
            asa "Eh? What is it?"
        if girl == "Icari":
            $dshow(42000,xpos=0.25)
            ica "Hey, I know what that is. It's an off market holo that's popular in Denari space."

        kay "You've been communicating with the Prototypes all this time, haven't you? There's messages on this holo giving away all our movements to the enemy, and even a medical report which you wrote, completely invalidating the other report you gave us that Chigara was not a Prototype!"

        #Variations
        if girl == "Asaga":
            $dshow(2111)
            asa "E-eehh!?!?"
        if girl == "Icari":
            $dshow(41210)
            "Icari put her hand on her sidearm."
            ica "Tsch... So you were a spy all along too, then!?"
            $dshow(41110)
        
        $dshow(34310)
        cla "Ara..."
        cla "It's all true. I was aligned with the Prototypes during this timeframe."
        $dshow(32310)
        cla "But that was me in the past! Poor Claude's turned a new leaf now... I'm fighting for the good guys!"
        $dshow(34110)
        kay "Why were you working for the Prototypes during this time period?"
        $dshow(34310)
        cla "A simple alignment of interests, that's all."
        cla "I sought to rally the galaxy around you, just like the Prototypes. But after the Liberation Day Massacre occurred, I realized our interests diverged. That's when I left them and took matters into my own hands..."
        kay "The Prototypes wanted what!?"
        cla "Yes... They sought to make you the leader of humanity... but to control you as a puppet, so that they would rule in your stead. But..."
        cla "Let's just say that plan never quite panned out... due to division within the Prototypes themselves."
        kay "That's... quite a lot to take in..."
        cla "I was fine with helping the Prototypes accomplish that. But then the massacre happened..."
        $dshow(34110)

        if girl == "Asaga":
            $dshow(534)
            asa "So you're sayin' basically, that you used to work for the Prototypes, but now you don't?"
            $dshow(34)
        if girl == "Icari":
            $dshow(41200)
            ica "Ultimately, you're not working for the Prototypes right now then?"
            $dshow(41100)

        kay "That doesn't get you off the hook yet."
        kay "I also found this inside the holo."
        "Shields opened the final file and showed it to Claude."
        kay "\"The future can only be saved... by destroying everything...\""
        kay "What does this mean?"

    if have_holo == True and girl == "Sola":
        #IF HAVE HOLO AND SOLA ROUTE

        $dshow(32010)
        cla "We were waiting for you, captain. Come on, let's move onto phase two and relay that warning to Fontana."
        kay "Wait, wait, wait... There's something we need to resolve before that."
        $dshow(34110)
        "He pulled out the holo."
        kay "I found this in your old self's office."
        $dshow(34310)
        cla "Ah, that's just my old holo. I used it to communicate with the Prototypes while I was working with them."
        cla "Captain, I hope you're still not suspicious of poor ol' Claude..."
        $dshow(34110)
        kay "That's actually not what I'm worried about this time. It's this."
        "Shields opened the final file and showed it to Claude."
        kay "\"The future can only be saved... by destroying everything...\""
        kay "Actually, Sola already has a basic idea of how time travel works. And according to her, changing the future isn't possible."
        kay "So what does all of this mean for us?"
        
    if have_holo == False:
        #IF NOT HAVE HOLO

        $dshow(34000)
        cla "I hope my other self treated you all right. Teehee~"
        $dshow(34210)
        kay "Ugh... Yeah, she did..."
        kay "Okay, now that we've regrouped, let's move on to phase two."
        kay "We need to contact Fontana on the FTL comm. Let's get moving."
        $dshow(32311)
        cla "Ahem... Actually, there's something else I need to talk about first."
        cla "There's something about time traveling I haven't mentioned yet..."
        kay "(Uh oh... I don't like the sound of this.)"

        if girl == "Sola":
            kay "(Does this have something to do what Sola was saying earlier?)"
            $dshow(70122)
        if girl == "Asaga":
            $dshow(32)
        if girl == "Icari":
            $dshow(41110)
        $dshow(34310)
        play music "Music/Anguish.ogg" fadeout 1.5
        cla "Ahem... Unfortunately, time travel is nowhere as flexible as one would expect, or else I would use my powers more often. The main limitation of time travel is that when individuals and events get moved out of sequence in the timeline, a time paradox can occur..."
        kay "(Time... paradox... I've heard those words before...)"

        #Desert
        scene bg desert
        show black:
            alpha 0.5
        with dissolve
        
        $dshow("sola armhold neutral narrow sad",xpos=0.5,behind="black")

        kay "Slow down, Sola! I'm... not quite following!"
        kay "Why does you being here mean the universe is doomed!?"
        sol "A time paradox."
        sol "If the mislocation of an event in the timeline breaks the link of causality between a series of events, then the logical sequence of the entire chain of events will be broken."
        sol "For example, if I were to travel back in time and remove the Prototypes from existence, then all of the other events which resulted from their actions would no longer make sense."
        sol "Such a time paradox can potentially cause the entire space time continuum to collapse. Meaning, the effective end of the entire universe."

        #Crew quarters
        scene bg crewquarters with dissolve
        $dshow(34310)
        if girl == 'Sola':
            $dshow(70122,xpos=0.25)
        elif girl == 'Asaga':
            $dshow(32,xpos=0.25)
        elif girl == 'Icari':
            $dshow(41110,xpos=0.25)
        kay "What a minute. You mean the kind of time paradox which can destroy our entire universe!?"

    $dshow(34200)
    cla "Eh-heh... Ah, looks like you've finally discovered the hard part of this mission..."
    $dshow(34311)
    cla "It's pretty complicated to explain, but the skinny of it is, basically... if we were to succeed in this mission and thwart the Liberation Day Massacre, both this universe, and the past universe where we come from, will collapse and cease to exist."
    cla "As it turns out... the space time continuum's really sensitive to time paradoxes and resolves them quite forcefully..."
    kay "C-collapse!? You mean, we'll all die anyways even if we win!? Then what the hell's the point of any of this!?"
    $dshow(34111)
    cla "Mou, you're thinking like a human..."
    $dshow(32311)
    cla "No. You will simply be wiped from existence. Dying is a natural phenomena which must inevitably happen to all life forms, but is an entirely different concept from never existing at all."
    cla "You traveled here from a future in which the Liberation Day Massacre occurred in order to prevent it. But if you succeed in your mission, the Kayto Shields who traveled back in time would cease to exist, as the massacre now never takes place. So then, who would be the man who stopped the massacre? A true logical conundrum. In other words: A time paradox."
    kay "So... then is the future really impossible to change?"
    $dshow(34311)
    cla "The future CAN be changed. That's why I brought you here."
    $dshow(34310)
    cla "At the end of this journey, you must make a choice."
    cla "Either you stop the Liberation Day Massacre from occurring and avert the tragedy which befalls upon everyone... and destroy this universe and the universe you came from, and replace them with the new universe you create with your decision."
    cla "Or you let the Massacre occur. Accept the tragedy. Then this universe will remain untouched and connect with your timeline. The universe you know will continue to exist, for the better or worse."
    kay "You're telling me... If I go through with this, everyone I know will vanish from the face of the universe... but then a new universe with copies of those same people will be created?"
    cla "That's the gist of it, yes. And that is the reason why I brought you here."
    cla "The key here is that the law of causality does everything in its power to resolve time paradoxes. And it does that by deleting the universe where the paradox occurs, and then creating a new universe which can then logically continue to exist from that point on."
    cla "In this case, you, and everyone in this universe, as well as everyone in the universe where the massacre occurred, would be wiped from existence, thus eliminating the time paradox."
    cla "But then a new universe, where the massacre never occurred would be born. And everyone would still exist in that universe, completely oblivious to the fact a massacre even occurred, or that there was a desperate mission to prevent it."
    kay "Then... We can still save everyone. By creating a new universe, where the massacre isn't prevented, but simply never existed at all!"
    $dshow(34000)
    cla "Ah, now you're understanding how this all works, captain... Teehee..."

    if girl == "Asaga":
        $dshow(514)
        asa "Ah... I don't understand any of this... My head hurts..."
        $dshow(534)
        asa "But in the end... the me right now is gonna vanish from existence? But then, I'll still be another Asaga, who won't even know there was a mission to change the future? I'll just... live on, never knowing there even was an event like the Liberation Day Massacre?"

    if girl == "Icari":
        $dshow(40010)
        ica "Ah, this time travel still's hard to understand."
        $dshow(40522)
        ica "But if this mission's a success, we'll have destroyed the universe where the massacre occurs, and head down a different universe where the massacre simply never existed at all?"

    if girl == "Sola":
        $dshow(70111)
        sol "I am beginning to understand the nature of time travel."
        sol "If a time paradox occurs, the unbinding law of causality simply destroys the universe where the paradox occurs, and creates a new one without the paradox. A simple solution to dealing with a logical impossibility."

    cla "Basically~"
    $dshow(34010)
    cla "In this circumstance, I intentionally sought to create a time paradox, in order to manipulate the law of causality into destroying the universe you don't want, and into creating the one you do want. Well... it was pretty drastic, but it's not like there's anyone out there who can stop me, so... teehee~!"
    $dshow(34011)
    if girl == "Sola":
        $dshow(70020)
    if girl == "Asaga":
        $dshow(655)
    if girl == "Icari":
        $dshow(40523)
    cla "It's pretty convenient, this little quirk that the law of causality has. I've been using it to create and destroy universes for... ah, I forgot, I'm immortal! Who knows how long I've been doing this!"
    cla "Anyways... Now that your choices have been laid out in front of you... I want to watch you choose, Kayto Shields, Hero of the Galaxy. That's the entire reason why I brought you here."
    $dshow(30000,ypos=1600)
    cla "All of this is so I can watch you more. I want to watch you run around, fighting desperately against impossible odds. I want to see the tears in your eyes when you fail. The euphoria cursing through your veins when you're victorious. The bigger the stakes, the more tortured your dilemmas, the mightier your enemies, the more I want to see you fight. Because it brings me sooo much pleasure, seeing you in action... Hwaaahh---"
    $dshow(34000,blush=True)
    "Claude's entire body flushed bright red as she squirmed her legs."
    cla "I think I might have cum a little..."
    kay "(Claude... Y-you... bastard!)"
    kay "(She's toying with me. Just like always!)"
    kay "(C-come to think of it... Was there ever a moment when she wasn't playing me like a fiddle during the whole time I've known her!? Argghhh...!)"

    $ menu_choices = [
                    ["Claude, I'm through with being your plaything!","donttrustclaude","¡Claude, estoy cansado de ser  tu juguete!"],
                    ["We're in this too deep now. We have to keep working together.","trustclaude","Estamos demasiado profundo en esto ahora. Tenemos que seguir trabajando juntos."],
                    ]
    show screen decision
    pause
    
label donttrustclaude:
    #"Claude, I'm through with being your plaything!"
    
    $ trustclaude = False
    
    $dshow(34010)
    cla "O-oh, a-are you going to punish Claude? Are you going to call her a bad girl?"
    $dshow(34001)
    cla "Come at it, captain! Hit me!"
    kay "Tsch...!"
    
    show layer master at tr_yshake
    play sound "sound/punch.ogg"
    
    "Before he could act, Shields suddenly felt as if a 200 kilo weight had been dropped on his back."
    kay "G-GUH!"
    "He collapsed to the floor, unable to do anything except drool helplessly on the steel tile as all the air escaped from his chest."

    if girl == "Asaga":
        $dshow(1121)
        asa "C-Captain!"
    if girl == "Icari":
        $dshow(42000)
        ica "Tsch! CLAUDE!!"
    if girl == "Sola":
        $dshow(70423)
        sol "A-ah!"

    $dshow(32010)
    cla "Aah, you have to keep entertaining me, captain... Who knows what might happen if I get bored... Hufufufu..."
    if girl != 'Ava':  #she's not there... right?
        "Claude looked at [girl], who seemed just about ready to attack."
    $dshow(34001)
    cla "Relax, relax. I wouldn't harm my beloved captain. A girl can't help wanting to show off a little from time to time."
    "With a snap of her finger, Shields felt the weight lift from him. He picked himself back up."
    if girl == "Asaga":
        $dshow(153)
    if girl == "Icari":
        $dshow(40020)
    if girl == "Sola":
        $dshow(70021)
    kay "What... did you do?"
    cla "When you have an infinite amount of time, you can learn all sorts of ways to manipulate the laws of this universe."
    cla "Mah, I'd rather not use my powers for anything important though. It'd be a pain if I were to accidentally wipe out a universe or two from existence by causing an unintended time paradox myself."
    kay "(Fuck... She really is practically a God.)"
    kay "(At this rate... Looks like I'm stuck in this nightmarish box of Claude's making...)"
    kay "(And I won't be able to leave until either the massacre is thwarted, or I fail.)"
    
    jump chigarawakesup

label trustclaude:
    #"We're in this too deep now. We have to keep working together."

    $ trustclaude = True

    $dshow(34000)
    cla "Teeheehee... Good call, captain. I knew I could count on you."
    $dshow(34210)
    cla "Mah, it's not too bad. You have a once in a lifetime chance to change the future. Isn't Claude such a generous god? Teeheehee~"
    cla "Ah, but before you get excited with the knowledge that you have a deity on your side, you should now understand why I can't use my powers willynilly. It'd be a pain if I were to accidentally wipe out a universe or two from existence by causing an unintended time paradox myself."
    $dshow(34301)
    cla "Every use of my power must be carefully planned in advance so that they bring about consequences I want. The results otherwise..."
    cla "Would not be pretty."
    $dshow(34111)
    kay "(So basically, I can't count on her to pull me out of the fire using her powers anymore.)"
    kay "All right."
    kay "Nothing productive is going to come out of fighting amongst each other. Whatever it is that we're going to do from now, we have to work together to accomplish it."

    jump chigarawakesup

label chigarawakesup:
    
    chi "Mm..."
    "As if to make matters worse, Chigara began to stir in her sleep."
    "Shields sharply inhaled in concern."
    kay "Shit. Uhh... Doc, how much longer is Chigara going to be sedated for?"
    $dshow(34010)
    cla "Ara? Still another four hours. With a full dosage, Chigara's going to be sound asleep for a full eight hours."
    $dshow(34310)
    cla "Ah."
    "Suddenly, Claude froze."
    $dshow(34200)
    cla "Teehee~"
    $dshow(34210)
    cla "Nevermind."
    kay "Doctor. What do you mean, \"nevermind?\""
    $dshow(32000)
    cla "Eeah, I forgot that in this timeline, I actually gave Chigara a half dosage of sleep pills... S-so that she would wake up early enough to consummate her love for her captain the night before the final battle..."
    "Shields nearly collapsed at Claude's mistake."
    kay "What do you mean, YOU FORGOT!? I thought you were supposed to be a GOD!"
    $dshow(34010)
    cla "Eeaah, well, when you've lived for as long as I have, there's just soo much to remember! H-how could I be expected to recall such a tiny little detail like that? Eaahahahaha!"
    kay "Then how much longer do we ACTUALLY have until Chigara wakes up!?"
    $dshow(34201)
    cla "Ah... maybe... until... about now."
    kay "G-guck-"
    "As if on cue, Chigara sleepily opened her eyes."
    $dshow(34310,xpos=0.85)
    if girl == "Asaga":
        $dshow(53,xpos=0.15)
    if girl == "Icari":
        $dshow(40020,xpos=0.15)
    if girl == "Sola":
        $dshow(70121,xpos=0.15)
    $dshow(20000)
    chi "A-ah... C-capt--"
    $dshow(21020)
    chi "E-e-e-eh!?!?!?!"
    chi "W-what's going on, captain? Why am I tied up to this chair!?"
    
    if girl != "Ava":
        chi "C-Captain!? A-And the doctor!? A-a-and [girl]!?"
    "Chigara's eyes darted around the room while she struggled against the ropes in a panic."
    kay "(Shit, shit, shit! Uhh... For now, I've got to calm Chigara down!)"
    kay "Chigara, uhh... d-don't worry! I'm... here!"
    kay "I... uhh... I'll... protect you."
    "All of a sudden, Shields felt at a loss..."
    "His usual collected demeanor fell apart. Random words merely leaked from his mouth as he spoke to Chigara in a daze."
    kay "(Chigara...)"

    #CG Chigara's death
    show dead2:
        xalign 0.5
        yalign 0.5
    show black:
        alpha 0.5
    with dissolve

    "He had felt her die in his very arms. When her spark left her body... A demon had awakened in him. A demon willing to burn the entire galaxy in order to avenge her."
    "Despite being a spy... Despite betraying him... Despite murdering countless Alliance leaders..."
    "Shields had loved her with his entire heart."
    kay "(And that's... exactly how the Shields in this universe feels about her...)"

    #Crew quarters
    hide dead2
    hide black
    with dissolve

    $ ship_power = True

    kay "Chigara... Calm down... And listen to me..."
    $dshow(22320)
    chi "E-eh?"
    "Shields knelt down in front of her."
    "Despite waking up tied up to a chair, the sight of her lover's face managed to calm her fears."
    chi "... ... ..."
    
    $dshow(22201)
    
    chi "What is it, captain? E-eh heh... I admit, t-this is quite a strange way of waking up after a doctor's visit..."
    
    $dshow(21200)
    
    chi "But... you wouldn't do anything bad to Chigara, would you? I... trust you."
    kay "I'm about to tell you something important... But no matter what happens, I'll protect you... Because this time, I'm going to save everyone. Including you, Chigara!"
    kay "(All right.. Here I go...)"
    kay "The truth is... You're..." 
        
    ##SPLIT THREE WAYS
        #1. BLEW COVER AND NO BODY SWAP or ON AVA ROUTE AND NO BODY SWAP: Captured immediately by ship security, ship does not lose power, happy end still possible
        #2. ON AVA ROUTE AND BODY SWAP, OR PICKED EITHER BLEW COVER OR BODY SWAP BUT NOT BOTH: Captured by ship security after Chigara escapes, ship loses power, no happy end
        #3. DID NOT BLOW COVER AND PERFORMED BODY SWAP: Not captured by ship security but Chigara escapes, ship loses power, no happy end

    if girl == 'Ava': #keeping or blowing cover makes no difference. (or, talking to ava == blowing your cover)
        if not body_swap:
            #instantly caught
            jump capturedkidnapping
        else:
            #caught after chigara escapes
            $ captured = True
            jump shiplosespower
    else:
        if not body_swap and coverblown:     #the 'subtle like a brick to the face' route
            #instantly caught
            jump capturedkidnapping
        elif body_swap and not coverblown:  #the solid snake route
            #chigara escapes - Shields does not get caught.
            $ captured = False
            jump shiplosespower
        else:                                #the halfway route
            #caught after chigara escapes
            $ captured = True
            jump shiplosespower
       
            
    # if coverblown == True and body_swap == False and girl != "Ava":
        # jump capturedkidnapping
    # if girl == "Ava" and body_swap == False:
        # jump capturedkidnapping
        
    # if girl == "Ava" and body_swap == True:
        # $ captured = True
        # jump capturedkidnapping #capturedafternopower does not exist. seems like it was merged later
    # if body_swap == False and coverblown == False and girl != "Ava":
        # $ captured = True
        # jump capturedkidnapping
        
    # if body_swap == True and coverblown == True and girl != "Ava":
        # $ captured = True
        # jump shiplosespower
    # if body_swap == True and coverblown == False:
        # $ captured = False
        # jump shiplosespower
    
label capturedkidnapping:
    #1. BLEW COVER AND NO BODY SWAP or ON AVA ROUTE AND NO BODY SWAP
    
    #stop music fadeout 1.5
    if ship_power == True:
        
        play music "Music/Gore_and_Sand.ogg" fadeout 1.5
        play sound "sound/explosion4.ogg"
        scene white
        scene bg crewcabin with dissolve
        "Shields could never finish his sentence, as exactly at that moment, the gate to the crew quarters exploded into smithereens, momentarily blinding everyone inside."
        show mook as mook1:
            xpos 0
        show mook as mook2:
            xpos 0.5
        "In a flash, marines piled into the room. By the time Shields had recovered his vision, he was completely surrounded by a squad of armed troops pointing their rifles at him."
        kay "Shit..."
        if not girl=='Ava': #still not there, right? 
            "He slowly raised his hands over his head. In front of him, [girl] did the same."
        kay "(Wait a minute...)"
        "He looked around in confusion. Claude had somehow vanished from the room."
        kay "(Did she use her powers to escape?)"
        "Before he could produce another thought, the marines grabbed onto him and pushed him out into the hallway."
        
        $ renpy.music.set_volume(0, delay=1.0, channel='music')
        
        #Hallway - "T-minus 50 hours before the Liberation Day Massacre, 14 hours until Chigara enters the mind stream"
        scene black with dissolve
        
        play sound "sound/drum.ogg"

        show expression Text(_("T-minus 50 hours before the Liberation Day Massacre, 14 hours until Chigara enters the mind stream"),size=40):
            xalign 0.5
            yalign 0.5
        pause
        
        $ renpy.music.set_volume(1.0, delay=1.0, channel='music')
        
        scene bg hallway with dissolve
        show mook as mook1:
            xpos 0

    "Shields kept his hands on top of his head as a marine shoved him to his knees."
    "A wall of well-armed troopers in full body armor stood in front of him. The human wall parted to let a man through to face Shields. It was..."
    
    hide mook1
    hide mook2
    with dissolve
    
    show kayto:
        xpos 0.5
    with dissolve
    kayo "Well... I'll be damned."
    kay "Aaah crap..."
    "Kayto Shields clenched his teeth as he stared down... Kayto Shields."
    kayo "You... really do look like an identical copy."
    
    if ship_power == True:
        $dshow(22002,xpos=0.75,behind="kayto")
        "Just then, Chigara emerged from the room, escorted by a pair of crewmen. She immediately ran to the other Shields and embraced him."
    if ship_power == False:
        $dshow(22210,xpos=0.75,behind="kayto")
        "Just then, Chigara emerged from behind the other Shields, escorted by a pair of crewmen."
    
    chi "Huuu... Captain, I'm so glad you're here..."
    chi "Just what in the world's going on? I feel like the doctor accidentally prescribed me the wrong medication and I'm hallucinating..."
    kayo "Oh, trust me, this is real. The ship's security has been compromised by two intruders. One of them happens to look identical to me."
    kayo "This fellow, right here."
    kay "(Ah fuck... My cover's been blown, and now Chigara's playing along with my past self's suspicions... And on top of all that, does my voice seriously sound like that...!?)"
    kay "(I sound... so lame! I thought my voice was so much deeper... Argh... As if I don't already have enough problems...)"
    kayo "I don't know what he sought to gain by kidnapping you... but I intend to find out."
    chi "Yes..."
    
    if ship_power == True:
        kay "You're... making a mistake! That girl's not who you think she is! In just a few hours, she'll-"
    if ship_power == False:
        kay "You're... making a mistake! That girl's not who you think she is! She's being mind controlled right now-"
        
    "Shields lost his words when another face emerged from the wall of marines."

    if girl != "Ava":
        #IF NOT ON AVA ROUTE

        $dshow(13310,xpos=0.2)
        ava "Captain, we've secured [girl] as well."
        ava "As far as we can tell, she does not appear to be an imposter. She is insisting that all of this is a mistake, and that this man before us is the real Kayto Shields."
        $dshow(13000)
        kayo "So he's fooled [girl] too then. Get her to sickbay and make sure she's all right."
        kayo "Take him away, boys. We can find out what he's after once he's secured in the brig. Resume the search for the other imposter. Keep the ship on high alert until she has been found."
        $dshow(14110)
        ava "Understood, sir!"
        "As the marines pushed Shields towards the brig, he tried to face Ava."
        $dshow(10011)
        kay "Ava! You've got to trust me! I'm Kayto Shields!"
        kay "Chigara's a prototype, just as you said! If you don't stop her by tomorrow, everything we've worked for will be lost!"
        
        if have_holo == True:
            kay "You'll find a holo inside the room! Look at it, and the evidence it holds!"
            
        show layer master at tr_xshake
        play sound "sound/punch.ogg"

        "One of the marines pounded Shields' gut with the butt of his rifle."
        mrn "Shut up!"
        kay "G-ghg..."
        "He felt two strong hands grip his shoulders and drag him to the brig."
        
        jump detainedinbrig

    if girl == "Ava":
        #IF ON AVA ROUTE

        $dshow(13310,xpos=0.2)
        ava "We have secured the room, captain. However, still no trace of the other imposter."
        ava "She may have managed to escape using the ground access hatch."
        $dshow(13000)
        kay "(W-wha-!? AVA!?)"
        kay "(What's she doing!? Wasn't she supposed to be helping me!? Was she the one who set me up!?)"
        "Shields' head spun as the woman he had put his trust in apparently backstabbed him without a second thought."
        kayo "Take him away, boys. We can find out what he's after once he's secured in the brig. Resume the search for the other imposter. Keep the ship on high alert until she has been found."
        $dshow(14110)
        ava "Understood, sir!"
        hide kayto with dissolve
        hide chigara with dissolve
        $dshow(10000,xpos=0.75)
        "As the marines pushed Shields towards the brig, he tried to face Ava."
        kay "(Ava... did she... betray me?)"
        kay "(Was Claude right? Was she seriously so devoted to the rules that she assumed all this time that I couldn't be the real Kayto Shields!?)"
        kay "(Or is she seriously so devoted to protocol that she's just blindly obeying everything the other Kayto Shields' saying?)"
        kay "(No... wait...)"
        kay "(She said she was pursuing a lead. Could that mean that she's found something, and all of this is a part of her plan to stop Chigara?)"
        kay "(But if I'm wrong about that... I could end up locked in the brig for the remainder of the battle...)"
        kay "(What do I do...)"
        
        $ menu_choices = [
                        ["I'll just have to trust Ava...","immediatecapture_trustava","Solo tendré que confiar en Ava..."],
                        ["I can't get captured here! I'll have to try to escape!","immediatecapture_escape","¡No puedo ser capturado aquí! ¡Tendré que intentar escapar!"],
                        ]
        show screen decision
        pause
        
label immediatecapture_trustava:

    #"I'll just have to trust Ava..."
    "Shields decided to play along for now."
    
    if have_holo == True:
        #IF HAVE HOLO
        
        kay "(Just one more thing...)"
        $dshow(10011)
        kay "Ava! Check the holo inside the room!"
        
        show layer master at tr_xshake
        play sound "sound/punch.ogg"
        
        "One of the marines pounded Shields' gut with the butt of his rifle."
        mrn "Shut up!"
        kay "G-ghg..."

    "He felt two strong hands grip his shoulders and drag him to the brig."
    
    jump detainedinbrig

label immediatecapture_escape:
    #"I can't get captured here! I'll have to try to escape!"
        
    kay "(Argh... It's do or die time...!)"
    kay "(I can't afford to be imprisoned here! Looks like I've got to call Ava's bluff!)"
    
    show layer master at tr_xshake
    play sound "sound/punch.ogg"
    
    "As Shields was being escorted away by two armed marines, he ducked down and swiped his leg under one of his escort, knocking him off his feet."
    "In a connected movement, he tore the escort's rifle from his grasp as the escort fell, and dug the nozzle of the gun into the other escort's helmet like a bayonet."
    mrn "Arghh!!"
    hide mook1 with dissolve
    "Ava spun around to face Shields as the wall of marines readied their weapons."
    $dshow(13110)
    ava "Shit- NON-LETHALS ONLY!"
    ava "Don't kill--"
    
    hide ava with dissolve
    play sound "sound/pulse1.ogg"
    
    "Shields dived as the floor he was standing on a moment ago was pulverized with shock pellets."
    kay "(Fuck! I gotta get out of here!)"
    kay "Argghh!!"
    "He spun back to his feet and bolted down the hallway."
    kay "(I gotta... find cover!)"

    #Mess hall
    if ship_power == True:
        scene bg messhall with dissolve
    if ship_power == False:
        scene bg messhall_nopower with dissolve
    
    "Shields burst into the crowded mess hall, to the surprised looks of the crew."
    cre1 "C-captain?"
    "The crewman's eyes widened when Shields leaped over his table, thoroughly scattering his tray of roast beef and mashed potatoes across the table."
    "Just then, a squad of marines burst in after Shields."
    cre1 "HOLY---"
    "The crewman fell off his bench as the marines chased after Shields, thoroughly smashing the entire table he was previously eating on into little plastic fragments."
    cre1 "UNBELIEVABLE--!!"
    
    play sound "sound/pulse1.ogg"
    
    "Shields ducked behind a table as shock pellets bounced all around him, filling the air with the smell of burning wires."
    kay "Never thought I'd be hunted down in my own damned mess hall!"
    "He held up a large plastic tray like a shield and made his way towards the hallway opposite to where he had entered."
    kay "I've got to come up with an escape plan... I won't be able to run like this forever!"
    
    play sound "sound/guncock.ogg"
    
    show mook as mook1:
        xpos 0
    show mook as mook2:
        xpos 0.5
    with dissolve
    
    "Just as he reached the opposite end of the mess hall, a second squad of marines poured in in front of him."
    kay "(S-surrounded! I-is this-)"
    
    play sound "sound/pulse1.ogg"
    
    "Shields couldn't even finish his thought before he was sprayed with shock rounds from every direction."
    
    scene white with dissolve
    play sound "sound/spark.ogg"
    
    kay "G-GAARGGHHH!!!!"
    "His body convulsed on the floor as alternating electric currents coursed through his muscles."
    kay "(No...)"
    kay "A... va...."
    show mook as mook1 with dissolve:
        xpos 0
    show mook as mook2 with dissolve:
        xpos 0.5
    "He lost consciousness as the marines surrounded him."
    
    jump badend_trapped

label shiplosespower:
    
    $ ship_power = False

    $dshow(34110)
    kay "...A Prototype, Chigara..."
    $dshow(21022)
    chi "E-eh...!?"
    kay "Claude's initial report turned out to be incorrect. She did some more tests and found without a doubt that you're an artificial clone..."
    $dshow(21112)
    chi "No... way..."
    kay "Don't worry. I'll still make sure you're not harmed. But you have to stay put for a while, until the rest of the Prototypes are defeated. You could be mind controlled by their leader at any time, so this is for everyone's safety."
    $dshow(21003,cry='closedeyestears',blush=True)
    chi "... ... ..."
    
    $dshow(21013,cry='tears',blush=True)
    
    chi "but this means..."
    chi "I won't be able to start a bakery with Kayto..."
    chi "I won't be able to have children..."
    chi "No..."
    chi "ChigaraisanormalgirlChigaraisanormalgirlChigaraisanormalgirlChigaraisanormalgirl..."
    kay "Chi... gara...?"
    "Shields tensed with apprehension."
    "He knew this was going to be difficult to explain, but he had to make sure Chigara understood the situation..."
    "Suddenly, Chigara broke out into a scream."
    $dshow(21301)
    chi "EAAHH!!!! M-My---"
    "She fell unconscious as quickly as she entered her fit of frenzy. Then she snapped awake. Except this time, she was different."
    $dshow(20111)
    chi "Heh... You did well to see through my plot, Shields."
    "He stood in shock. Chigara had just been body jacked! This was now the Prototype leader he was talking to!"
    kay "You! You're--"
    $dshow(20101)
    chi "But don't think I didn't have a backup plan of my own!"
    
    play music "Music/Gore_and_Sand.ogg" fadeout 1.0
    
    play sound "sound/powerdown.ogg"
    scene black with dissolve
    "All the lights inside the room shut off. Or more accurately, every single light inside of the ship deactivated."
    "Shields heard the familiar soft droning of the ship's engines sputter out. With nothing running, eerie silence fell over the ship. Then the sound of a laser cutter, and the clatter of plastic hitting the ground as Chigara's chair split in half shattered the silence."
    kay "(I can't see a damned thing!)"
    kay "(I know, my holo!)"
    scene bg crewquarters_nopower with dissolve
    "Shields pulled his holo out and put it on maximum illumination, casting a weak light over the room. Long shadows surrounded him, filling his heart with dread."
    
    if girl != "Ava":
        "He confirmed that [girl] was still safe. However, Chigara was now nowhere to be found. All that remained were the broken fragments of the chair and cut rope on the floor."

    "A handheld laser cutter roughly the size of a cigarette continued to buzz on the floor, until Shields picked it up and shut it off."
    kay "Did you see which direction she took off!?"

    if girl == "Icari":
        $dshow(40022,behind='darkness')
        ica "Negative! It was pitch black and the sound of the cutter covered up all her movements!"
        
    if girl == "Asaga":
        $dshow(53,behind='darkness')
        asa "Sorry, I couldn't hear anything 'cause of that cutter!"
        
    if girl == "Sola":
        $dshow(70123,behind='darkness')
        sol "Negative. She moved with the movements of a trained soldier - silent, and swift."
        
    if girl == "Ava":
        "Nobody responded to his question. He looked around and realized that Claude had completely vanished."
        kay "(Did Chigara get her?)"
        kay "(No way, not even the Prototype leader is powerful enough to take Claude on. Then she must have vanished of her own will.)"
        kay "(Damnit... Now that she's explained all the rules of this game, she expects me to figure out the rest on my own, huh...)"
        kay "(She's probably still watching me... Eagerly waiting for my next plan of action...)"

    if girl != "Ava":
        kay "We've been had!"
        
    kay "(Shit! I made a mistake!)"
    kay "(I should have known that Chigara could be body jacked at any time! That's exactly what Lynn told me when we escaped on the lifepod together. All this talk about preventing her from entering the mindstream confused me into thinking we'd be safe as long as we got her before then!)"
    kay "(No... The reason why we have to prevent Chigara from entering the mindstream is to prevent the Prototype leader from body jacking her after the leader is dead! Chigara can be body snatched whenever the Prototypes want while their leader's still alive!)"
    
    if girl != "Ava":
        kay "Wait a minute..."
        "Shields looked around and realized that Claude was now nowhere to be found as well."
        kay "Claude!"
        kay "(Did Chigara get her?)"
        kay "(No way, Chigara isn't powerful enough to take Claude on, even while under the control of the Prototypes. Then Claude must have vanished of her own will.)"
        kay "(Damnit... Now that she's explained all the rules of this game, she expects me to figure out the rest on my own, huh...)"
        kay "(She's probably still watching me... Eagerly waiting for my next plan of action...)"
        
        if girl == "Icari":
            $dshow(41211,behind='darkness')
            ica "Claude's gone! Where'd she vanish to!?"
            $dshow(41111,behind='darkness')
            
        if girl == "Asaga":
            $dshow(655,behind='darkness')
            asa "Eeh!? Claude's vanished, like, into thin air!"
            
        if girl == "Sola":
            $dshow(70010,behind='darkness')
            sol "Tsch... Claude has chosen to leave us to our to our devices."

        kay "And now we have a new, huge problem..."
        kay "The Prototype leader laid out this trap for us. And we just stepped right into it."
        kay "The Sunrider's main reactor has been remotely shut off."
        kay "Without it, we won't be able to get a FTL transmission sent to Fontana. Even worse, we're essentially sitting ducks for the loyalist PACT Fleet now. Unless we can get power restored ASAP, this ship is going to be destroyed!"

        if girl == "Icari":
            $dshow(41101,behind='darkness')
            ica "Tsch... I can't believe we were fooled so easily..."
        if girl == "Asaga":
            $dshow(2121,behind='darkness')
            asa "Eh-EEEHH!! How're we gonna do that!?"
        if girl == "Sola":
            $dshow(71000,behind='darkness')
            sol "How can we restore the ship's power?"

        kay "If I can get to engineering... I might be able to restore the ship's power."
        kay "It's a long shot, but maybe I can undo whatever the Prototype has done to our systems."
        kay "But wait... The Sunrider also has an emergency FTL transmitter which operates on a separate battery pack. It's all the way down at Deck 2, section 37, but if we get to it, we could get a message sent to Fontana even without power."

        if girl == "Asaga":
            $dshow(11,behind='darkness')
            asa "Ah, but section 37's pretty far from here, and who knows how long it'll take to restore power..."
        if girl == "Sola":
            sol "Section 37 is far from here, while restoring the ship's power will undoubtedly prove time consuming as well..."

        if girl != "Icari":
            kay "([girl] has a point... I need to decide which task to prioritize over the other...)"
            kay "(If we can't restore the ship's power, then we're sitting ducks once PACT attacks... On the other hand, I doubt I can just waltz into Engineering and show my face to the entire crew without getting detained by ship security...)"
            kay "(And if I get captured before relaying the message to Fontana, then we have no choice but to allow Chigara to enter the mindstream, or else we'll all be killed when the Prototypes assume control of Fontana's fleet.)"
            kay "(Meaning, I damned better send Fontana the warning before revealing myself.)"
            kay "We go to the back up comm first. Then we go to Engineering and restore power."
        
            if girl == "Asaga":
                $dshow(2000,behind='darkness')
                asa "Understood, capt'n! Let's get that message sent off to Veniczar Fab!"
            
            if girl == "Sola":
                $dshow(70210,behind='darkness')
                sol "Understood."
                
        if girl == "Icari":
            $dshow(41210,behind='darkness')
            ica "Oy, section 37's too far from here! Here's what we should do. I can probably figure out what Chigara's done to our main reactor. I'm going to run to Engineering to restore power."
            ica "While I'm doing that, you can go to the emergency FTL transmitter and send Fontana the message."
            kay "Sounds like a plan. Glad to have you on my side, Icari."
            $dshow(41011,behind='darkness')
            ica "H-heh... Don't worry, I'll get the ship operational again!"
                
        if captured == True:

            scene bg hallway_np with dissolve
            show mook as mook1:
                xpos 0
            show mook as mook2:
                xpos 0.5
            with dissolve
            
            "The pair run out of the crew quarters, but only came face to face with a squad of marines."
            "They drew their rifles and held Shields and [girl] at gun point."
            "Shields squinted, the bright flashlights attached to the marines' rifles blinding him."
            kay "Shit..."
            kay "Ship security's finally caught up to us..."
            
            jump capturedkidnapping
            
        if captured == False:
            
            jump gotobackupftl

    if girl == "Ava":
        kay "(And now we have a new, huge problem...)"
        kay "(The Prototype leader laid out this trap for us. And we just stepped right into it.)"
        kay "(The Sunrider's main reactor has been remotely shut off.)"
        kay "(Without it, we won't be able to get a FTL transmission sent to Fontana. Even worse, we're essentially sitting ducks for the loyalist PACT Fleet now. Unless we can get power restored ASAP, this ship is going to be destroyed!)"
        kay "(If I can get to engineering... I might be able to restore the ship's power.)"
        kay "(It's a long shot, but maybe I can undo whatever the Prototype has done to our systems.)"
        kay "(But wait... The Sunrider also has an emergency FTL transmitter which operates on a separate battery pack. It's all the way down at Deck 2, section 37, but if we get to it, we could get a message sent to Fontana even without power.)"
        kay "(If we can't restore the ship's power, then we're sitting ducks once PACT attacks... On the other hand, I doubt I can just waltz into Engineering and show my face to the entire crew without getting detained by ship security...)"
        kay "(And if I get captured before relaying the message to Fontana, then we have no choice but to allow Chigara to enter the mindstream, or else we'll all be killed when the Prototypes assume control of Fontana's fleet.)"
        kay "(Meaning, I damned better send Fontana the warning before revealing myself.)"
        kay "(I don't have a choice! I better get to the back up comm first before going to Engineering!)"
        
        scene bg hallway_np
        show mook as mook1:
            xpos 0
        show mook as mook2:
            xpos 0.5
        with dissolve
            
        "Shields run out of the crew quarters, but only came face to face with a squad of marines."
        "They drew their rifles and held him at gun point."
        "Shields squinted, the bright flashlights attached to the marines' rifles blinding him."
        kay "Shit..."
        kay "(Ship security's finally caught up to me...)"
        
        jump capturedkidnapping
            
                
label detainedinbrig:
    #IF CAPTURED AND SENT TO THE BRIG
    #BRIG "T-minus 47 hours before the Liberation Day Massacre, 11 hours until Chigara enters the mind stream"
    
    stop music fadeout 1.0
    
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    # Ava sped up your interrogatory, no time to lose!
    if ship_power == False and girl == "Ava":
        show expression Text(_("T-minus 49 hours before the Liberation Day Massacre, 13 hours until Chigara enters the mind stream"),size=40):
            xalign 0.5
            yalign 0.5
        pause
    else:
        show expression Text(_("T-minus 47 hours before the Liberation Day Massacre, 11 hours until Chigara enters the mind stream"),size=40):
            xalign 0.5
            yalign 0.5
        pause
    
    play music "Music/Fallen_Angel_drone.ogg" fadeout 1.5
    
    if ship_power == True:
        scene bg brig with dissolve
        
    if ship_power == False:
        scene bg brig_nopower with dissolve
    
    show kayto:
        xpos 0.2
    with dissolve
    
    if ship_power == True:
        "Shields faced his doppelganger as he spoke through the intercom."
    if ship_power == False:
        "Shields faced his doppelganger as he was interrogated at gunpoint."
        
    kay "Listen to me, you dumb oaf... I really am you! Just from the future! I've come to warn you of a massacre which will happen--"
    "He had repeated his desperate warnings to his past self for the better part of the past two hours, but it was clear that he was not getting through."
    kay "Chigara is a prototype! If she enters the mind stream a few hours from now, she'll be mind controlled by the leader of the Prototypes and carry out--"
    "The other Shields cut him off, his voice cracking with impatience."
    kayo "All right, enough about Chigara. I want to know how you got onboard this ship and who you're actually working for."
    
    if ship_power == False:
        kayo "How did you shut off our ship's reactor? Is sabotage your mission? Or have you merely come here to spread subterfuge like Lynn?"
        kay "I'm telling you, I had nothing to do with the ship's reactor shutting off! That was Chigara's doing! Or rather, she was body jacked by the Prototypes' leader, thanks to her being a prototype herself!"
        kay "You've got to detain her, right now! She's not the Chigara you know any more! She's been mind controlled!"
    
    kayo "You're a Prototype, aren't you? Have you guys started generating clones of me too now?"
    kayo "Look, it was pretty weird when we discovered you Prototypes were making artificial clones of Chigara... But now me too? Just what is up with you guys and making clones of people on board this ship?"

    # Shields doesn't know Ava's working with you
    if girl != "Ava":
        kayo "What were you trying to gain by trying to recruit [girl] into your \"mission?\" And for what purpose did you kidnap Chigara?"
    else:
        kayo "What were you trying to gain with your \"mission?\" And for what purpose did you kidnap Chigara?"

    kay "(Arggh... It's hopeless...)"
    kay "(There's no way in hell I'm ever going to convince this blockhead that Chigara's going to cause the Liberation Day Massacre at this rate.)"
    kay "... ... ..."
    "The other Shields sighed in exasperation on the other side of the glass. Honestly, Shields was inclined to do the same."
    "He was one agonizingly stubborn individual to argue with. All of a sudden, he felt compelled to apologize to Ava for his personality once all of this was over. He had never known he was so stubborn until now."
    
    if ship_power == False:
        kayo "Doesn't look like this is going to go anywhere. Maybe a little time alone will make you more willing to cooperate."
        kayo "Lock him up."
        "Two marines grabbed Shields by the shoulders and shoved him into a cell."
        kay "Shit..."
        "The gate shut."
        "A solid layer of reinforced neoglass separated Shields from the outside world, making it impossible to hear anything outside of his little fish tank."
        "The other Shields turned and spoke with Ava."
        
    if ship_power == True:
    
        "Finally, the other Shields left the intercom with an irritated look on his face and spoke to Ava."
        "A solid layer of reinforced neoglass separated Shields from the outside world, making it impossible to hear anything outside of his little fish tank."
        
    kay "(If only I could hear what they were saying...)"
    kay "(Wait a minute... I remember reading a maintenance request form about this holding cell. Something about the cell door failing to seal completely. Maybe if I'm lucky, it hasn't been fixed yet...)"
    "Shields pretended to crumple to the floor in defeat, and put his ears up against the crack where the gate came down on the floor. Sure enough, he could now faintly hear the other Shields' and Ava's exchange."

    $dshow(13310,xpos=0.7)
    if girl != "Ava":
        ava "Captain, perhaps we should consider the prisoner's warning seriously. [girl] is convinced that this Kayto Shields is telling the truth."

    if girl == "Ava":
        ava "Captain, perhaps we should consider the prisoner's warning seriously. Given the gravity of what he is alleging, if it turns out that he is telling the truth, our victory at Cera would be meaningless if the top Alliance leadership is assassinated and a far greater conflict between the Alliance and PACT ignites."

    if have_holo == True:
        ava "Further, the holo we found within the room directly refutes our doctor's prior finding that Chigara is a human and throws grave a shadow on all of the doctor's actions for the entire duration of this voyage. In fact, I believe our next move should be to detain both the Chief Engineer and our acting medical officer under suspicion of espionage."
    $dshow(13010)
    kayo "... ... ..."
    kayo "No. First off, he's not \"Kayto Shields.\""
    kayo "Ava, you're still going on about that? How many times do I have to tell you, the Prototypes just want to sow division within our ranks. This imposter's probably just their latest attempt at the same strategy. In fact, everything here falls under the same pattern of them trying to get us to turn on each other."
    kayo "We're one family on board this ship. It's that bond which makes us strong. The Prototypes are trying to undermine it."
    kay "(No you idiot!!! It's you who's so fixated on your goddamn family that you can't see what's obvious to everyone else!!!)"
    "Shields nearly banged his head on the cell door in frustration at hearing himself talk."
    kay "(Someone... please give this man a good whomp to the head...)"
    $dshow(13311)
    ava "But captain-!"
    kayo "That's enough, commander."
    ava "Tsch..."
    kayo "Continue to interrogate the prisoner. Find out what the Prototypes are after. That's an order."
    $dshow(13000)
    ava "... ... ..."
    ava "Understood, sir!"
    
    #SPLIT FOUR WAYS
        #1. IF DON'T HAVE HOLO AND NOT ON AVA OR ICARI ROUTE: Shields trapped inside cell, BAD END
        #2. IF ON ICARI ROUTE: Shields rescued by Icari
        #3. IF ON AVA ROUTE: Shields rescued by Ava
        #4. IF HAVE HOLO: Shields rescued by Ava
    
    hide kayto with dissolve
    
    if girl != "Ava":
        #IF NOT ON AVA ROUTE
        "With that, the other Shields left the brig while Ava was left by herself trembling with anger."
        $dshow(10300)
        ava "Tsch... It is you who cannot see the truth, captain..."
        
        hide ava with dissolve
        
        "With that, she stormed off into the hallway as well."
        "Shields was left alone inside his cell. All he could hear was the sound of his own breathing inside the tiny glass cage."
        "He paced nervously inside the cell as time continued to tick by..."
        "Now that he was stripped of his uniform and was wearing nothing but a basic prisoner's jumpsuit, he had no way of telling the time anymore."
        kay "(Now what...?)"
        kay "(Do I wait for Claude to show up again? Just where did she go anyways...?)"
        kay "(Goddamnit...)"
                
    if girl == "Ava":
        #IF ON AVA ROUTE
        $dshow(10010)
        "With that, the other Shields left the brig. Ava merely sighed, as if she knew this outcome was inevitable but was disappointed it had come to pass anyways."
        "Ava looked around to check if the coast was clear, then approached the holding tank."
        
        $dshow(12413)
        
        "She merely held out her outstretched palm and put it up against the glass."
        kay "Ava...?"
        kay "(Of course! She's sending me a message not to worry!)"
        kay "(She's already come up with a plan to stop Chigara, and me getting captured was just part of that plan!)"
        "Shields outstretched his hand and put his palm up against hers. This was their oath. They would work together until the very end to avert the tragic future..."
        "The faintest trace of a smile appeared on Ava's face before she withdrew her hand. With a nod, she faced him one last time before leaving the brig."
        kay "(Now... let's see what Ava has planned...)"
        
        jump freedbyava

    if girl == "Icari":
        #not saved by ava so now Icari gets a chance to
        jump freedbyicari
        
    if have_holo == True:
        #not saved by Ava or Icari, but you're still okay with the holo
        jump freedbyava
        
    #not saved by Ava, Icari and you don't have the holo
    jump badend_trapped

label badend_trapped:
    if girl=="Ava":
        $renpy.save("BAD END 3")
    elif girl == "Asaga":
        $renpy.save("BAD END 4")
    elif girl == "Sola":
        $renpy.save("BAD END 5")
        
    #IF DON'T HAVE HOLO AND NOT ON ICARI OR AVA ROUTE

    #Wipe
    #BRIG "T-minus ??? hours before the Liberation Day Massacre, ??? hours until Chigara enters the mind stream"
    
    stop music fadeout 1.0
    
    scene black with horizontalwipe
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus ??? hours before the Liberation Day Massacre, ??? hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    if ship_power == True and girl != "Ava":
        scene bg brig with horizontalwipe
        play music "Music/Anguish.ogg" fadeout 1.5
    if ship_power == False and girl != "Ava":
        scene bg brig_nopower with horizontalwipe
        play music "Music/Anguish.ogg" fadeout 1.5
    if girl == "Ava":
        scene bg brig_damaged with horizontalwipe
        play music "Music/Camino.ogg" fadeout 1.5
        
    if girl != "Ava":

        "He paced for an unknown amount of time and finally crumpled down to the small bunk."
        kay "(Argghh!!! Where is Claude!? Where's... anyone!?)"
        kay "(Am I... really trapped in here!?)"
        "He tried to estimate how many hours had passed since he had been confined in the brig. Had it been seven hours? Ten? His panic began to get the better of him."
        kay "(But that would mean it's already too late to keep Chigara from entering the mind stream!!!)"
        kay "NO!!!! I have to get out of here!!!"
        "He stood and pounded the glass, but it was pointless."
        kay "LET ME OUT OF HERE!!!!!!!!!"
        kay "YOU'RE ALL MAKING A MISTAKE!!!!!!!!!!"

        #Wipe
        scene bg brig with horizontalwipe

        "... ... ..."
        "... ..."
        "..."
        "He had pounded the glass until his fists had become bloody stumps."
        "He sat face down on his bed, his expression vacant."
        "At least twenty hours must have passed since he was captured. Meaning he was now too late."
        kay "... ... ..."
        "What had happened outside? Why had nobody tried to rescue him? Had something happened to [girl]? And just where did Claude vanish to?"
        "Did Claude simply lose interest in this mission because he got captured?"
        kay "Ah... That's it..."
        kay "She only sent me here to watch me struggle... She honestly doesn't give a damn about the massacre or about liberating Cera... From the very beginning, the only reason she was on the ship was to laugh at my suffering..."
        kay "Now that I've been captured, she's just jumped to some other universe... She's probably already found some other space captain to laugh at now... I bet she's already settling into his sickbay, trying to give him a medical exam..."
        "Shields continued with his monologue, his mind slowly cracking."
        kay "Ah... I should have known Ava would just go along with what Bastard Shields wants... After all, all she's good for is just following orders..."

        if girl == "Asaga":
            kay "I wonder... what happened to Asaga... I bet she's still out there... Trying to convince Bastard Shields to let me out... Heh... But like he'd ever listen to that..."
        if girl == "Sola":
            kay "I wonder... what happened to Sola... She's probably taken it all upon herself to stop the massacre alone now...  I hope... she's all right..."

        kay "What was the point of this... In the end... I couldn't accomplish anything..."

        #Wipe
        scene black with dissolvemedium

        "... ... ..."
        "... ..."
        "..."
        
        play music "Music/Camino.ogg" fadeout 1.5
        play sound "sound/explosion4.ogg"
        scene bg brig_damaged with dissolvemedium
        
        "The sudden rumbling of the ship woke Shields from his slumber."
        kay "(What's... going on...?)"
        "All of a sudden, the ship shook violently, knocking him from his bed. He crashed onto the steel floor."
        kay "Ah... I guess it's finally all ending..."
        kay "I guess I really did mess up."
        "He raised his head to the sound of pounding on the other side of the glass."
        "The cell's door opened, and a figure crashed in..."
        
    if girl == "Ava":
        
        #IF SHIELDS WAS STUNNED IN MESS HALL

        #Brig, shut down "T-minus ??? hours before the Liberation Day Massacre, ??? hours until Chigara enters the mind stream"
        
        "Shields came to inside a holding tank in the brig."
        "The entire ship shook and swayed, as if taking kinetic hits from every direction."
        kay "U-ugh..."
        kay "(What... happened?)"
        "The ship had already lost most of its power. Another hit shook the floor, nearly throwing Shields off his feet."
        kay "Did the battle already begin!?"
        kay "No... Wait..."
        kay "This is....."
        "A dark realization dawned on him, spreading a black pool of horror throughout his body."
        "Ava crashed into the brig, clutching her bloody stomach. She dragged herself to his cell and punched the cell door's button."
        "She fell immediately as the door opened, into Shield's arms."
        $dshow(15310)
        kay "Ava!! W-what happened!?"
        "He applied pressure to Ava's wound."
        ava "T-tsch..."
        ava "I was too late... Chigara is dead, but the massacre still occurred as before..."
        ava "I took a hit from a hunter drone just after I managed to get Chigara... If I had just been a few seconds quicker..."
        kay "Ava!? But I thought you were--"
        ava "Heh..."
        ava "G-gngh... I... found out that our Chief Engineer had a backup plan in case her identity was ever discovered... She built a back door into our main reactor so she could shut down the entire ship remotely..."
        ava "I... had to stop you... from kidnapping Chigara... before she disabled the ship... I-it was the only way..."
        kay "N-no...."
        "Shields' face lost all pigmentation. Sweat dripped down his neck."
        "Ava had been on his side this whole time. It was actually him who was wandering towards a trap, and Ava who was desperately trying to stop his mistake..."
        kay "(Then... it's just like before... Last time, I didn't trust Ava when she warned me about Chigara... And now, all this happened because I failed to trust her again...)"
        kay "No... No..."
        kay "Everything... is my fault."
        kay "I... betrayed you. Again. And now..."
        ava "Get out of here... You know the other Kayto Shields' planning a suicide attack on Machiavelli Actual..."
        ava "There's... nothing more for you to do here..."
        kay "No... I..."
        "Shields looked down in defeat."
        kay "I'm... sorry. I should have trusted you..."
        ava "Heh... haha..."
        ava "You... only realize that now?"
        ava "G-ggack..."
        
        $dshow(15300)
        
        "Ava coughed up blood as her eyes lost focus."
        ava "...Idiot."
        ava "Leave me here..."
        ava "...and save... yourself..."
        "Her body stiffened as her spirit finally left."
        
        hide ava with dissolve
    
    if girl == "Asaga":

        $dshow(8422)
        asa "T-tsch... C-Captain..."
        "Asaga leaned against the cell's door frame while clutching her gut. Blood oozed out from a hole the size of a tennis ball on her stomach."
        kay "Asaga!"
        asa "G-ghnn..."
        "She collapsed into the cell. Shields rushed towards her and caught her into his arms."
        $dshow(8402)
        asa "You've... got to get out of here..."
        asa "Everything happened exactly the way you said... Chigara entered the mind stream, and then killed everyone at the victory celebration... I... I tried to stop her... But the hunter drones got to me first."
        "Shields applied pressure to Asaga's wound."
        kay "No! Asaga, hang on! I'm going to get you out of here!"
        "Suddenly, more memories played back in his head."
        
        play sound "sound/static.ogg"

        #Chigara death CG
        show dead1
        pause 1
        hide dead1

        kay "(No... Not again... This is exactly like last time...)"
        "The ship groaned as it took hits."
        asa "H-heh... The other captain's trying to stop the Alliance from nuking Cera now..."
        asa "I tried to convince him that you were the real Kayto Shields... But he wouldn't listen..."
        asa "Ah... What a shitty end... H-heh... ehehe... Y-you can barely even laugh at it... Despite everything we worked for... it had to end like this..."
        asa "Haa... haa..."
        "Asaga's breathes grew more ragged as she lost more of her strength."
        
        $dshow(8313,blush=True,cry="tears")
        
        asa "Haa... at least....."
        asa "Will you... kiss this maiden... before... she...."
        "Asaga's eyes began to lose focus."
        kay "No!!! ASAGA!!!"
        asa "I can... barely see you any..."
        "Shields bent down and locked their lips together."
        asa "Mm..."
        asa "Heh... heh..."
        asa "T-thanks..... I've wanted that for..."
        asa "Now I guess... I can.... be..... happy....."
        "Her body stiffened as Asaga's spirit finally left."
        kay "ASAGA!!!!!!!!!!!"
        
        hide asaga with dissolve
        
    if girl == "Sola":

        #IF SOLA ROUTE

        $dshow(74020)
        sol "H-hgn... C-captain..."
        "Sola leaned against the cell's door frame while clutching her gut. Blood oozed out from a hole the size of a tennis ball on her stomach."
        kay "Sola!"
        sol "G-ghnn..."
        "She collapsed into the cell. Shields rushed towards her and caught her into his arms."
        $dshow(74103)
        sol "You must... escape..."
        sol "It all came to pass as you said. Chigara entered the mind stream, and then killed everyone at the victory celebration... I attempted to stop her... but the hunter drones overpowered me."
        "Shields applied pressure to Sola's wound."
        kay "No! Sola, hang on! I'm going to get you out of here!"
        "Suddenly, more memories played back in his head."

        play sound "sound/static.ogg"

        #Chigara death CG
        show dead1
        pause 1
        hide dead1

        kay "(No... Not again... This is exactly like last time...)"
        "The ship groaned as it took hits."
        
        $dshow(74123)
        
        sol "The Alliance now seeks to destroy the entire PACT fleet as well as Cera with a new weapon..."
        sol "The other Kayto Shields leads a hopeless charge against Machiavelli Actual to stop them. Despite my best efforts, I could not convince him to detain Chigara..."
        sol "I... have failed... I... am sorry..."
        kay "No Sola! It was me who failed... I got captured like this... And couldn't help anyone..."
        sol "G-ghnngh! A-ah..."
        sol "I-it will not be long now... Get to the lifepod... I will merely slow you down..."
        kay "No! Don't worry, Sola! I'm going to get you out of here!"
        
        $dshow(74323,blush=True)
        
        sol "Ah..."
        sol "Captain..."
        sol "I... did not fear death... For I had accepted what awaited me at the end of my journey... Nothing but... darkness..."
        sol "But..."
        sol "That darkness was replaced... with..."
        sol "Haa... haa..."
        
        $dshow(74313,cry='tears',blush=True)
        
        "Sola's eyes grew dim as her breaths became ragged."
        sol "At least... at the very end... allow me one moment of selfishness..."
        kay "Sola!! D-don't talk as if this is the end!"
        sol "Ah... haha..."
        sol "Cradle me..."
        sol "Envelope me... I wish to feel nothing but your warmth... as I fade away..."
        kay "SOLA!!!"
        "Shields held Sola to his chest and held her tight."
        sol "... ... ..."
        sol "At last..."
        sol "I have... you..."
        "Her body went stiff as Sola's spirit finally left."
        
        hide sola with dissolve
        
    "Shields howled and pounded the floor."
    kay "Y-you can't..."
    kay "I came back to save everyone!!! What the hell is the point if you die too!?!?"
    kay "I... didn't want this!!!"
    "Tears streamed down his face as he realized that he had merely made the new future even worse."
    "His mission had been an abject failure. At least in his own timeline, [girl] was still alive."
    kay "(What will... happen now?)"
    "His mind went blank as despair flooded his mind."
    "The voice of his other self echoed through the brig..."
    kayo "...Today, the Sunrider stood her ground!"
    kayo "We did not run, but protected all those we hold dear until we fell into the black night!"
    kayo "We did not falter in our defense of our family!"
    kayo "Today, we perished to save our home!"
    kay "(No... In the end... I only fail once more...)"
    
    play sound "sound/explosion2.ogg"
    scene white with dissolve
    
    "He closed his eyes as a massive explosion engulfed the entire brig."
    kay "Everyone... I'm sorry..."
    "Shields felt his body vaporize as the Sunrider collided into Machiavelli Actual. The opposite end of the brig came flying towards him as the entire ship compressed from the force of the impact."
    "He died the instant the wall of fire crushed him."
    
    stop music fadeout 1.0

    #BAD END
    scene black with dissolve
    
    play sound "sound/choirend.ogg"
    
    if girl == "Ava":
        $persistent.unlocked_endings["BAD END 3: TRAPPED AVA VER"] = True
    if girl == "Asaga":
        $persistent.unlocked_endings["BAD END 4: TRAPPED ASAGA VER"] = True
    if girl == "Sola":
        $persistent.unlocked_endings["BAD END 5: TRAPPED SOLA VER"] = True
    $check_for_all_endings()    
    show screen bad_end_trapped
    pause 3
    $dshow(32310)
    
    if girl != "Ava":

        cla "Aah, looks like you messed up, captain... And you made the future even worse than before by getting [girl] killed!"
        cla "You need to find some evidence to get Ava to believe you when you're trapped in the brig. Or avoid getting captured by the other Kayto Shields in the first place."
        cla "Try again, this time by either stealing the holo from sickbay, or not blowing your cover!"
        
    if girl == "Ava":

        cla "Aah, looks like you messed up, captain... And you made the future even worse than before by getting Ava killed!"
        cla "Mou, you seriously thought you could escape from a squad of armed marines by yourself? Did you forget that you're not the one with super powers in this story, captain?"
        cla "Try again, and this time, choose to trust Ava!"
        
    $renpy.full_restart() 

label freedbyicari:

    #IF ON ICARI ROUTE
    
    stop music fadeout 1.0

    #BRIG "T-minus 45 hours before the Liberation Day Massacre, 9 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 45 hours before the Liberation Day Massacre, 9 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "Music/Destinys_Path.ogg" fadeout 1.5
    
    scene black with horizontalwipe
    
    if ship_power == True:
        scene bg brig with horizontalwipe
    if ship_power == False:
        scene bg brig_nopower with horizontalwipe
    $reset_sprites()
    

    $dshow(41011)
    "A short time later, he heard someone knock on the holding tank."
    "Shields looked up to see Icari on the opposite side of the glass, fiddling with the wiring of the brig door. After a few seconds, the gate raised open."
    "He ran out and met Icari."
    
    $dshow("icari armscrossed talk neutral confident")
    
    ica "Damn that was close... Boy am I glad to see you still in one piece, cap..."
    ica "Thankfully, your other self's convinced himself that you're a Prototype, so it was piece of cake to get him to let me go once I acted like I had been fooled too. Honestly, something's been really off with your other self lately..."
    ica "Tsch. I bet it's his new girlfriend... Guys sure change at the drop of a pin the moment they get hitched, huh..."
    kay "(Icari... please don't talk about my other self as if I'm not here...)"
    ica "After I fooled the other Shields into thinking I was totally normal, I hacked into the ship's security system and managed to sneak here. Everything else is history."
    kay "Thanks for busting me out."
    ica "Well, it's not like I busted you out of jail because I like you or anything, you know. You have a future to save, right?"
    ica "Anyways, it won't be long until security finds out what happened. Here, take this."
    "Icari passed him a new set of captain's uniforms."
    ica "Best I could get my hands on. It should still contain your old command clearance."
    kay "Thanks. Uhh..."
    "Shields looked around uncomfortably for a place to change, but didn't particularly find anywhere useful."
    kay "Turn your head."
    ica "U-urk!"
    "Icari covered her eyes with her hands moments before Shields quickly pulled down his jail trousers and slipped into his uniform."
    $dshow(41212,blush=True)
    ica "Y-Y-You idiot! Give me more advance notice before you start stripping!"
    kay "This is hardly to be the time to be worried about that!"
    
    $dshow("icari handonhip shout closed angry blush")
    
    ica "Huuu... I can't believe you..."
    "Shields finished putting on his uniform."
    kay "All right, show's over, let's move."
    $dshow(41311)
    ica "Into the maintenance tunnel! Come on!"
    "Icari swiped an strange looking device on the tunnel's gate, instantly unlocking it. Shields assumed it was some sort of improvised skeleton key and crawled into the tunnel without asking any questions."

     #Tunnel
    scene bg tunnel with dissolve
    $dshow(41311)

    "Once they were safely deep within the Sunrider's mechanical innards, the two of them paused to decide their next course of action."

    if ship_power == False:
        ica "Now that ship security's hunting you down, you can forget about emerging from these maintenance tunnels."
        ica "I'm going to head to Engineering and find out a way to restore power. Meanwhile, continue down the tunnel, and get to the backup FTL comm to relay the warning to Fontana."
        ica "Once we've done that, we'll rendezvous in Engineering maintenance shaft 5."
        kay "All right, sounds like a plan. Good luck."
        ica "You too."
        
        jump gotobackupftl

    if ship_power == True:
        kay "First order of business is to send the encrypted message to Fontana. Then we have to figure out a way to put Chigara out of commission."
        kay "But now that security's on high alert, getting into my room's not going to be a walk in the park. Think you can distract security for a bit?"
        ica "Heh. Leave that to me."
        kay "Okay, let's move!"
        
        jump officeftlfontana


label freedbyava:
    
    #wipe
    
    scene black with horizontalwipe
    
    if ship_power == True:
        scene bg brig with horizontalwipe
    if ship_power == False:
        scene bg brig_nopower with horizontalwipe    
    
    play music "Music/Destinys_Path.ogg" fadeout 1.5

    "A short time later, he heard someone knock on the holding tank."
    $dshow(13000)
    "Shields looked up to see Ava on the opposite side of the glass. She pressed the button to open the cell door."
    kay "Ava?"
    "She immediately handed him a new set of captain's uniforms."
    $dshow(13200)
    ava "Come on, I'm getting you out of here."
    ava "I've managed to get my hands on a new set of authorization codes to go along with that uniform. You'll be able to access the same parts of the ship as before with that."
    ava "It won't be long until security comes back. Escape through the emergency maintenance shaft, then meet me inside lifepod 15, where there are no cameras."
    ava "Do you understand?"
    kay "Yeah."
    "Ava spun around and left the brig as quickly as she appeared."
    scene bg tunnel with dissolve
    "With that, Shields quickly put on his uniform and escaped into the maintenance shaft as ordered."
    
    if girl == "Ava":
        
        scene bg escapepod with dissolve
        $dshow(13010,xpos=0.3)
        "He entered lifepod 15 as told by Ava, and found her waiting inside."
        "She stood and faced him."
        
        if ship_power == True:
            kay "What happened? Did the other Shields catch on to me?"
            $dshow(10000,xpos=0.5)
            ava "No. Your capture was actually my doing."
            kay "Really? Uhh... Then why'd you do that?"
            $dshow(10310)
            ava "Following what you told me about the Chief Engineer, I naturally investigated all of the modifications she made to our ship's systems to guard against the risk of sabotage. During the investigation, I discovered a logic bomb embedded in the main reactor's controls, wherein the Chief Engineer could remotely deactivate the entire ship."
            ava "No doubt yet another insurance policy the Prototypes prepared in case the Chief's identity was found out."
            ava "Shortly afterwards, I discovered that you were about to kidnap the Chief and step right into the Prototype trap. Given the circumstances, I had no choice but to assemble ship security and detain you before you made a fatal mistake."
            kay "O-oh... shit."
            kay "Then it sounds like you just saved my ass. U-uh... thanks."
            ava "I was merely doing my duty to protect the ship."
            kay "No..."
            kay "You're always the one doing all the work to keep the ship safe. Once again, I nearly fell for another Prototype trap. If it weren't for you, the mission would most likely have failed."

        if ship_power == False:
            #IF CAPTURED AFTER SHIP LOST POWER
            kay "What happened? Did the other Shields catch on to me?"
            $dshow(10000)
            "Ava let out a long sigh."
            $dshow(10310)
            ava "No. I'm afraid your capture was my doing."
            kay "What? Why'd you do that?"
            ava "Following what you told me about the Chief, I decided to do some research on the modifications she made to our ship. During the investigation, I discovered the logic bomb she left for us if her true identity was found out."
            ava "I rushed to prevent your mission to kidnap the Chief as soon as I realized what was going on, but it looks like I arrived too late. Now, the ship has been completely disabled and the Chief is once again at large."
            ava "I thought to lure the Chief into a false sense of security by having it appear as if you were detained by ship security before she could trigger the logic bomb, and then to let you out to foil her plans, but it appears that plan failed."
            "Shields rubbed his temple in frustration."
            kay "Arggh..."
            kay "Sorry. Looks like I bungled everything up. I shouldn't have acted until I rendezvoused with you."
            ava "No use regretting what has already happened."

        kay "Honestly... I'm disappointed in myself..."
        kay "Lately, it feels like I've been failing as this ship's captain."
        "In contrast to her usual angry demeanor, Ava smiled gently."
        $dshow(12414)
        ava "Please do not carry all the burden by yourself. Remember that I am by your side as well."
        kay "Yeah. Thanks for having my back all the time..."
        $dshow(14011)
        ava "Underst--"
        $dshow(12404)
        ava "Ahem. I guess you're not the ship's captain anymore."
        ava "Then... uhh..."
        $dshow(12412)
        ava "You're... welcome. Shields."
        kay "Heh."
        kay "A wild adventure to save the day once more. Just like old times."
        $dshow(12412,xpos=0.3)
        
    if girl != "Ava":
        
        #Lifepod "T-minus 46 hours before the Liberation Day Massacre, 10 hours until Chigara enters the mind stream"
        
        stop music fadeout 1.0
        
        scene black with dissolve
        
        play sound "sound/drum.ogg"

        show expression Text(_("T-minus 46 hours before the Liberation Day Massacre, 10 hours until Chigara enters the mind stream"),size=40):
            xalign 0.5
            yalign 0.5
        pause
        
        play music "Music/Colors_of_an_Orchestra_II.ogg" fadeout 1.5
        
        scene bg escapepod with dissolve
        "He entered lifepod 15 as told by Ava, and found her and [girl] waiting inside."

        if girl == "Asaga":
            #ASAGA
            $dshow(2021,xpos=0.25)
            asa "Captain!"
            $dshow(3002,ypos=1600)
            asa "Aaah, I nearly died of a heart attack when those muscle heads dragged you away like that! I woulda gone full Sharr mode on them if it weren't for the commander!"
            $dshow(30)
            asa "And geez, just what the hell is up with the other captain anyways!? Is he stupid or something? I can't believe he just locked you up in the brig and completely ignored everything you said!"
            kay "No Asaga... He's... uhh... just in love. And that's making him blind."
            $dshow(530)
            asa "Eeh?"
            $dshow(252)
            asa "Ah, whatever! I'm only gonna like you from now on! The other captain can go screw himself!"
            asa "Once this is all over, I think you should throw him into the brig and throw the keys away just to teach him a lesson!"
            "Shields shook his head, but laughed in spite of himself at Asaga's antics."

        if girl == "Sola":
            #SOLA
            $dshow(70323,xpos=0.25)
            sol "Captain..."
            sol "I feared for the worst when you were captured. Luckily, the commander saw reason once she examined the contents of the holo and hatched this plan to rescue you."
            sol "It is thanks to her that we are reunited here..."
            sol "Alas, seeing you safe brings such joy to my heart...  Ah... Dark torment that our times together are so fleeting..."
                        
    if ship_power == True:

        $dshow(30000,xpos=0.75)
        "Just then, a certain pink haired ditz poked her head out from the front of the escape pod as well."
        cla "Teeheehee... Looks like you made it out of the brig alive, captain..."
        kay "Claude!"
        kay "Damnit... Just where'd you vanish to!?"
        $dshow(32000)
        cla "Ah, ah, ah... Remember, I can't be put into a situation where I'll be forced to use my powers."
        $dshow(34010)
        cla "When the marines appeared, I activated my convenient cloaking device and temporarily fell back."
        cla "Mah... It's more fun for me if you figure things out for yourself, captain... Also safer for the space time continuum too."
        cla "Teehee... Please treat me like a normal girl. Using my powers to get out of this mess is strictly forbidden!"
        kay "(Damnit Claude... I bet she has some trick up her sleeve which would let us avert the massacre here and now!)"
        kay "(But I guess she has a point... Using her powers is outright dangerous, considering what we've learned about the Law of Causality. For now, we're stuck with what Claude can accomplish without time powers...)"

    if girl != "Ava":

        "Now that they were safely hidden away from the ship's various security features, Ava finally managed to relax. They sat down alongside each other inside the pod."
        $dshow(10000,xpos=0.5)
        kay "Uhh... thanks for busting me of the brig."
        ava "... ... ..."
        $dshow(10020)
        ava "You're... really Kayto. Aren't you?"
        kay "Heh. That I am."
        kay "I'm afraid I'm the same Kayto Shields who scrubbed the entire swimming pool with you during advance academy because all the other members of the student council quit."
        $dshow(10000)
        ava "Then... what you are saying about the future is indeed the truth."
        kay "I'm afraid so..."
        ava "... ... ..."
        $dshow(10310)
        ava "I have disobeyed a direct order from my superior officer by bringing you here. If I am caught, I expect I will be stripped of my rank and confined in the brig myself."
        ava "But the threat the Liberation Day Massacre presents to the safety of Cera... no... the entire galaxy, is so grave... that I can no longer in good conscience follow the other Captain Shields down his path. The evidence inside the holo proves without a question that our Chief is a Prototype."
        
        if ship_power == False:
            ava "Further, the Chief Engineer is the only member of the crew with easy access to the reactor core's controls. Most likely, she is the one behind the ship's loss of power as well."
        
        ava "We must detain her."
        ava "[girl] has filled me in about the details of the situation."
        ava "You must know this timeline better than anyone else, capt-- uh... Kayto. What are our options?"
        $dshow(10020)

    if girl == "Ava":

        $dshow(13300)
        ava "In any matter, the situation is as follows: We must still detain the chief engineer and warn Fontana so that we may survive the battle without her assistance. Further, now that ship security is on high alert and we know the Chief can remotely shut down the ship's reactor, we must avoid detection."
        ava "The biggest question is how we will capture Chigara without also shutting the ship down."
        ava "The best solution would be to invalidate the Chief's command ID. However, the only person capable of doing that is the ship's captain. Unfortunately, the new uniform I procured for you does not have the sufficient security clearance to lock the Chief out of the system."
        kay "So in other words... The only person who can detain Chigara without the ship shutting down is the other Kayto Shields?"
        ava "Correct."
        kay "But he's completely convinced that Chigara's on his side..."
        
    "Shields racked his brains for ideas..."
    kay "First things first... We have to warn Fontana about the virus before putting Chigara out of commission."
    
    if ship_power == False:

        #POWER OFF
        kay "Now that we've lost all power, the back up comm is our only option."
        kay "Not only that, but we have to get to Engineering and somehow get our reactor back online."
        
        if girl != "Ava":
        
            #If not Ava route
            ava "Then it appears that sending the transmission and restoring power are our two immediate priorities. I will return to my station and distract the other Kayto Shields and oversee the crew's efforts to restore power."
            ava "Meanwhile, you and [girl] will go to the backup comm and send the transmission."
            kay "All right, sounds like a plan. We can figure out a way to stop Chigara after we've sent the message and restored power."
        
        if girl == "Ava":
            #If Ava route
            ava "Then it appears that sending the transmission and restoring power are our two immediate priorities. We'll take a trip together to section 37 and use the back up comm to relay the message to Fontana."
            ava "After that, we can go to Engineering and try to restore the reactor."
            kay "All right, sounds like a plan. We can figure out a way to stop Chigara after we've sent the message and restored power."
            
        jump gotobackupftl

    if ship_power == True:
        kay "I could still sneak into my office to send the message, but now that the ship's on high alert, that's going to be nowhere as easy as before."
        ava "Judging from the fact that my security clearance has not been revoked yet, it appears that nobody has realized I have set you free. I could simply try issuing an order to security to distract them."
        kay "As for capturing Chigara, I'm almost out of options now that the prior kidnapping was a bust."
        kay "I could try convincing my other self that Chigara's a Prototype and get him to detain her. But that's a total longshot at this point!"
    
        if girl == "Sola" or girl == "Ava":

            kay "(Come to think of it... There's another option!)"

            #Flashback of Asaga going berserk
            
            play sound "sound/static.ogg"
            show asagacockpit3
            show black:
                alpha 0.5
            pause 1
            hide asagacockpit3
            hide black

            kay "(When Chigara enters the mind stream, Asaga goes berserk and nearly kills her in my timeline!)"
            kay "(If we just change the course of events a little, we can get this universe's Asaga to kill Chigara before she has a chance to commit the massacre.)"
            kay "(But this is murder we're talking about here...)"
            "Shields' chest chilled at his own thoughts."
            kay "(The safety of the entire galaxy is at stake... But... to actually arrange the murder of my own Chief Engineer!? Not to mention...)"
            "Once again, his memories of Chigara came flooding back to him."

            #Chigara CGs
            play sound "sound/heartbeat.ogg"
            show chigarabeach2
            pause 0.5
            hide chigarabeach2
            show chigara_tea3
            pause 0.5
            hide chigara_tea3
            show chigaralap4
            pause 0.5
            hide chigaralap4
            show shieldschigarahug
            pause 1.0
            hide shieldschigarahug
            hide black
            
            kay "G-ghck..."
            "His chest suddenly twitched at the thought of killing his former lover."
            "Granted, she had been a spy sent to win his affections from the very beginning... But Shields was still certain the massacre was not Chigara's doing. She had merely been mind controlled without her knowledge during that time. Certainly, she needed to be captured, but to be killed...?"
            "Not only that, but Asaga was merely a distraught girl in this timeline... Her attack on Chigara was a moment of desperation, brought on by mental fatigue after multiple awakenings..."
            "To use Asaga like a puppet to murder her former best friend in cold blood..."
            "He knew that if he went down this path, he would no longer be worthy of being this ship's captain. In his own eyes, at least."
            kay "(But... this is the safety of the entire galaxy we're talking about...)"
            kay "(What do I do...!)"
            
            if girl == "Sola":
            
                "At a loss, he decided to ask Sola for advice."
                kay "Tomorrow, Asaga will attack the Liberty while Chigara's inside the mindstream. If we just manipulate events a little, I think we could change the future by having Asaga kill Chigara."
                kay "What do you think, Sola?"
                $dshow(70222)
                sol "Indeed, the Queen's mental condition has deteriorated substantially due to her unrequited love for this universe's Kayto Shields, and her multiple powerful awakenings."
                sol "It would not strike me as odd at all if she were to attack Chigara during the battle."
                kay "No, I was asking about what you would think of me if I were to use Asaga to kill Chigara, Sola..."
                kay "Could... you still call me captain if I were to do such a thing?"
                $dshow(70212)
                sol "... ... ..."
                sol "It is ultimately Asaga's decision."
                sol "If that is what the Queen of Ryuvia desires... Then I shall accept it."
                sol "As for you, captain, your actions will avert a massacre, as well as spare the galaxy of a bloody war between the Alliance and PACT. I will look upon you as proudly as I have always done regardless of your decision."
                sol "A leader... must bear the weight of his decisions. No matter the burden."
                kay "All right... Thanks, Sola..."
                
                $ menu_choices = [
                    ["We kill Chigara: First, we sneak into my office and contact Fontana. Then we get Claude to swap with this universe's Claude on the Bianca tomorrow so that Asaga kills Chigara for us.","sola_killchigarawithasaga","Matamos a Chigara: Primero, nos escabullimos en mi oficina y contactamos a Fontana. Entonces hacemos que Claude se intercambie con la Claude de este universo en el Bianca mañana de forma que Asaga mate a Chigara por nosotros."],
                    ["We capture Chigara: First, we sneak into my office and contact Fontana. Then, we confront this universe's Kayto Shields together to convince him to detain Chigara.","sola_decideconfrontshields","Capturamos a Chigara: Primero, nos escabullimos en mi oficina y contactamos a Fontana. Entonces, confrontamos al Kayto Shields de este universo juntos para convencerlo de detener a Chigara."],
                    ] 
                show screen decision
                pause
                
            if girl == "Ava":

                kay "There's another option... In my timeline, Asaga's mind broke down from awakening too many times, and she attacked Chigara in a fit of jealous rage when Chigara entered the mindstream."
                kay "Even though Asaga was ultimately thwarted in my version of events, if we manipulate the timeline a bit, I think we could change the future by having Asaga kill Chigara."
                $dshow(10200)
                ava "I see... In that case, we would not need the other Kayto Shields to overturn the chief's command clearance."
                $dshow(10020)
                ava "But this option is all but certain to lead to the chief's death. Are you sure about this?"
                kay "... ... ..."
                ava "Granted, I do not know the likelihood of the chief's survival no matter which option we pick. Even if she survives, she would be imprisoned for the remainder of her life."
                kay "I know..."
                
                $ menu_choices = [
                    ["We confront the other Kayto Shields and convince him to detain Chigara.","ava_decideconfrontshields","Confrontamos al Kayto Shields de este universo juntos para convencerlo de detener a Chigara."],
                    ["We use Asaga to kill Chigara for us.","ava_killchigarawithasaga","Usamos a Asaga para que mate a Chigara por nosotros."],
                    ]
                show screen decision
                pause
                
        if girl == "Asaga":
        
            $ killchigara = False
        
            kay "(Come to think of it, when Chigara enters the mind stream, Asaga goes berserk and nearly kills her in my timeline...)"
            kay "(But uhh... Seeing how Asaga's now standing here right in front of me, it looks like I'm not going to be able to repeat my timeline's version of events.)"
            kay "(Could I somehow get Asaga on the Black Jack and take the Liberty out?)"
            kay "(No... I can't risk Asaga like that... My past self was willing to kill her to protect Chigara, and I doubt the situation's changed.)"
            kay "Tsch... In the end, it all comes down to convincing my other self to detain Chigara."
            kay "We don't have a choice. We're going to have to convince the captain of this ship that Chigara is a spy. In other words, my past self."
            $dshow(2000)
            asa "All right! I'll... do my best to help!"
            $dshow(13300)
            ava "Understood. Convincing the captain to change his mind will be difficult. I hope you're prepared, Kayto."
            kay "I know."
            kay "But... I know him better than anyone. Because... uhh... he's me."
            kay "First though, we'll have to send Fontana the FTL message ASAP so that his ships are ready to fight with us without Chigara's help."
            kay "Come on, let's go!"
            
            jump officeftlfontana
        
label sola_killchigarawithasaga:
    #"We kill Chigara: First, we sneak into my office and contact Fontana. Then we get Claude to swap with this universe's Claude on the Bianca tomorrow so that Asaga kills Chigara for us."
    
    $ killchigara = True
    
    sol "Understood."
    $dshow(34010)
    cla "Ara~ Do you have a plan, captain?"
    kay "Yeah."
    cla "Then, let's go~!"
    
    jump officeftlfontana
        
label sola_decideconfrontshields:
    #"We capture Chigara: First, we sneak into my office and contact Fontana. Then, we confront this universe's Kayto Shields together to convince him to detain Chigara.":

    $ killchigara = False

    sol "Understood."
    $dshow(10310)
    ava "Convincing the captain to change his mind will be difficult. I hope you're prepared, Kayto."
    kay "I know."
    kay "But... I know him better than anyone. Because... well uhh... he's me."
    kay "Come on, let's go."   
    
    jump officeftlfontana
    
label ava_decideconfrontshields:
    #"We confront the other Kayto Shields and convince him to detain Chigara."
    
    $ killchigara = False
    
    $dshow(10310)
    ava "Understood. Convincing the captain to change his mind will be difficult. I hope you're prepared, Kayto."
    $dshow(10010)
    kay "I know."
    kay "But... I know him better than anyone. Because... well uhh... he's me."
    kay "First though, we'll have to send Fontana the FTL message ASAP so that his ships are ready to fight with us without Chigara's help."
    kay "Come on, let's go."

    jump officeftlfontana

label ava_killchigarawithasaga:
    #"We use Asaga to kill Chigara for us."
    
    $ killchigara = True
    
    $dshow(10010)
    ava "Understood."
    $dshow(34010)
    cla "Ara~ Do you have a plan, captain?"
    kay "Yeah. First, we're going to have to send the FTL message to Fontana. And then we swap you out for this universe's Claude when the battle begins, putting you inside the Bianca instead."
    kay "And then you can let Asaga past this time, and she'll take care of the Liberty for us."
    cla "Then, let's go~!"

    jump officeftlfontana
    
label gotobackupftl:

    #SHIP LOST POWER, GOING TO BACKUP FTL COMM

    #Tunnel "T-minus 45 hours before the Liberation Day Massacre, 9 hours until Chigara enters the mind stream"
    
    stop music fadeout 1.0
    
    scene black with dissolve
    
    play sound "sound/drum.ogg"
    
    if captured == True:
        if girl == "Ava":
            show expression Text(_("T-minus 48 hours before the Liberation Day Massacre, 12 hours until Chigara enters the mind stream"),size=40):
                xalign 0.5
                yalign 0.5
            pause
        else:
            show expression Text(_("T-minus 45 hours before the Liberation Day Massacre, 9 hours until Chigara enters the mind stream"),size=40):
                xalign 0.5
                yalign 0.5
            pause
    else:
        show expression Text(_("T-minus 50 hours before the Liberation Day Massacre, 14 hours until Chigara enters the mind stream"),size=40):
            xalign 0.5
            yalign 0.5
        pause
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene bg tunnel with dissolve

    if girl != "Icari":
        "Shields and [girl] ran into the closest maintenance tunnel and headed down to Deck 2."
    if girl == "Icari":
        "Shields ran into the closest maintenance tunnel and headed down to Deck 2."
    
    if girl == "Ava":
    
        ##AVA GOING TO BACKUP COMM
        #Tunnel "T-minus 50 hours before the Liberation Day Massacre, 14 hours until Chigara enters the mind stream"

        $dshow(13010)
        kay "(The back up FTL's one of the few systems which keep operating under battery power when the ship loses power like this. Basically, when the ship's disabled, we need to be able to breathe and call for help. That's why life support and the FTL comm keep working.)"
        kay "(It's a lot more limited than the regular ones though. We can only transmit a text message less than 120 characters in length, and the message can only be broadcast on the intergalactic distress and rescue channel.)"
        kay "(Another problem is that the batteries are still nowhere powerful enough to power life support for the entire ship. The air's going to get really thin on deck 2 real fast.)"
        $dshow(13300)
        ava "Captain, wait."
        kay "Is something wrong?"
        ava "Here, we should get one of these first."
        "Ava removed the wall panel, revealing a toolbox stashed behind it."
        ava "The maintenance crew leaves their supplies here."
        kay "Good call, Ava."
        "They opened the toolbox, revealing a handheld welding kit, first aid equipment, a pair of oxygen masks, and knee and elbow pads for crawling through the tunnel."
        kay "Looks like we lucked out. Here."
        "He handed Ava the oxygen mask."
        kay "Air's gonna get real thin the further we get from the center of the ship. Probably gonna need to put this on."
        kay "I would never have known this toolbox was here."
        $dshow(13200)
        ava "Well captain, perhaps you should read the maintenance handbook for the ship."
        kay "I... uhh... sorry."
        "Shields looked down in embarrassment. He was desperately reliant on Ava where the day to day operations of the ship were concerned. In fact, unless they were in combat, Ava was more or less the captain of the ship."
        "Once again, he was reminded of how much he had taken her for granted."
        "After putting on the protective pads, Ava closed the toolbox and headed deeper into the tunnel."
        $dshow(13300)
        ava "Come on, let's go."
        "Shields chased after her, trying to keep up with her quick pace."
        kay "You know... I don't know if I've ever told you this..."
        kay "But... uhh... I owe you an apology. I don't think I've been taking good care of you lately..."
        ava "Kayto? What do you mean?"
        kay "Well... uhh... Honestly, meeting my other self for the first time really gave me a new perspective on things... He's... kind of an ass."
        kay "Stubborn as hell... And once he's decided something, nobody else can change his mind..."
        kay "Trying to reason with him is kind of like talking with a brick wall..."
        kay "You've been dealing with me for the better part of a year now... I... feel pretty ashamed by the way I've acted in front of you."
        
        $dshow(12420)
        
        ava "Heh."
        ava "Honestly, it takes me back."
        ava "Perhaps I'm only saying this because you're not my captain right now. But it feels like so little has changed from when we were in school. Remember all the arguments we would get into back then?"
        kay "That's right..."
        
        $dshow(12410)
        ava "Of course, I was the one in charge in the past. And you would always get so angry at how I would never budge on anything."
        ava "But despite that... you stayed by my side. Until the very end."
        ava "... ... ..."
        
        $dshow(12210,blush=True)
        ava "I've... always regretted how it ended."
        kay "Ava?"
        $dshow(10100)
        ava "Ah, nothing!"
        $dshow(10300)
        ava "Sigh... Anyways, what I'm saying is... Since you put up with me back then... I'll put up with being ignored by you now."
        $dshow(10310)
        ava "Like you said... having the roles reversed gives you a new perspective. I'm not going to quit just because you don't like my ideas. You never once did that to me."
        kay "I see..."
        kay "Anyways, Ava... Thanks for everything you do for me. I've... been taking it all for granted."
        ava "Heh."
        $dshow(10210)
        ava "You can thank me by diligently finishing some paperwork after all of this is through."
        kay "U-urk... Y-yes ma'am..."
        $dshow(10221)
        ava "Do you take your gratitude back now?"
        kay "(Speaking of that... Ava doesn't know about the whole universe collapsing if we succeed with this mission...)"
        kay "Uhh... speaking of that... There's another... wrinkle in the plan I forgot to mention..."
        kay "So Claude only told me this right before I got detained by security... But fixing the timeline isn't as simple as just averting the massacre and then living happily ever after..."
        "Shields spoke with Ava about the universe getting wiped from existence and being replaced with a new universe."
        $dshow(10011)
        ava "I see..."
        $dshow(13011)
        ava "So you're saying, once the massacre has been averted, we will all vanish from existence, but at the same time, we will all be recreated in a new universe where the massacre never occurred..."
        kay "Yeah... It's some heavy stuff..."
        ava "I'm afraid I cannot express much of an opinion on this matter. I... never even imagined we would find ourselves in a situation such as this."
        kay "No kidding..."
        kay "Really, becoming a time traveler? Fighting against a past version of myself? Changing the future?"
        ava "For now, averting the assassination of Admiral Grey and preventing an intergalactic war seems to be our goal. Existential dilemmas are honestly... above our paygrade, as it were."
        kay "Honestly, I decided the same myself..."
        kay "I'm here to prevent what happened in my timeline from repeating again... As long as a new universe will be created, I'll do whatever it takes to make sure that we can all live in peace in that new universe."
        ava "Indeed, that sounds like a good approach..."

        #wipe
        scene black with horizontalwipe
        scene bg tunnel with horizontalwipe
        $dshow(13000)
        "After some time, the two arrived at the backup comm."
        "The walls were now frozen solid with a thin layer of ice, and small icicles hung from the pipes running along the wall of the tunnel."
        "While their oxygen masks allowed them to keep breathing despite being so far away from the central life support system, their uniforms were no match for the frigid cold."
        "With trembling hands, Shields removed the wall panel, exposing the controls of the FTL comm."
        "Icicles hung from the comm's cables, while a thin layer of frost caked the steel casing."
        kay "Goddamnit... This thing had better still be working..."
        "His pressed the activation button, but the comm showed no signs of life."
        kay "Shit..."
        kay "What the hell's wrong with this thing...?"
        "He tried to troubleshoot the problem, making sure all the cables were connected. Finally, he came upon a single unplugged cable, dangling at the bottom of the case. Unfortunately, the cable's slot was now obstructed by a solid block of ice, making it impossible to plug back in."
        "He tried to force the cable's steel rod into the receptor, but the hole was completely filled with ice."
        "Frustration bubbled instead of him. Who had dropped the ball and left this cable unplugged!? Was it a member of the maintenance crew? A malfunctioning repair drone?"
        $dshow(13311)
        ava "What's wrong?"
        kay "Someone accidentally left a cable unplugged... I won't be able to turn the comm on without it. But the receptor's now frozen solid."
        $dshow(13300)
        ava "Use this."
        $dshow(13000)
        "Ava opened the toolbox and withdrew the handheld welder."
        kay "Good call."
        "He took the welder and activated it close to the frozen receptor. A blue laser emitted from the tip of the welder, quickly melting away the ice."
        "The cable now fit perfectly inside the receptor."
        kay "All right... Let's hope that did the trick..."
        "Shields turned the comm on again, and sighed a breath of relief when it activated."
        kay "We're in business!"
        kay "(Fontana, you better read this message after everything we went through to send it!)"
        "Shields used the comm's keypad to type out the warning to Fontana and relayed it."
        kay "Now... All we can do is pray someone on board Fontana's ship is watching the distress channel... And takes the message seriously enough to relay it to Fontana."
        "Shields reattached the wall panel, once again closing the comm."
        kay "Come on, we've done all we can here. We need to get deeper into the ship, before we freeze to death."

        #wipe
        scene black with horizontalwipe
        scene bg tunnel with horizontalwipe
        $dshow(13000)
        
        $ backup_comm = True
        "The duo made their slow return to the center of the ship."
        "Their extremities were now completely numb thanks to the cold. Worse still, now they had to climb up ladders instead downwards, making the return trip far more difficult."
        kay "Brrr..."
        kay "Damn..."
        kay "This cold really takes me back... Remember when I used to complain about the cold all the time back on Cera?"
        $dshow(13301)
        ava "How could I forget... In fact, you joined the student council to lobby for thermaweave uniforms, didn't you?"
        kay "Well, look at me now... I'm wearing one hella expensive thermaweave uniform right now and still freezing my ass off..."
        kay "Haha... What I would give for a thick alpaca blanket right now..."
        kay "I can't believe you can act so stoic all the time... Aren't you cold, Ava?"
        $dshow(10100)
        ava "I assure you, I am just as cold as you are right now. I... just don't bellyache."
        $dshow(10020)
        kay "Heh... That's definitely like you..."
        "The two of them came upon yet another ladder. Each of the frozen rungs on the ladder looked akin to daggers in Shields' mind."
        "He let out a long, exhausted sigh."
        kay "Let's... take a short break... I'm not sure if my hands are ready for another frozen ladder."
        
        play music "Music/Colors_of_an_Orchestra_II.ogg" fadeout 1.5
        
        "He collapsed down against the wall, and did a double take when Ava took a seat on his lap."
        kay "A-Ava?"
        $dshow(11010)
        ava "Quit struggling. The quickest method of warming ourselves up will be through exchanging our body heat."
        ava "Here, give me your hand."
        "She took his hands and intertwined their fingers."
        "While she remained completely nonchalant about their intimate position, Shields' heart couldn't help but beat faster."
        $dshow(12220)
        ava "We don't have a moment to spare. The ship's still completely without power. If PACT attacks now, we'll all be dead in a matter of minutes."
        kay "Uhhh..."
        kay "S-sorry, what were you saying again?"
        $dshow(12314)
        ava "Idiot."
        $dshow(12320)
        ava "Rub your body against mine. The friction will generate additional heat." #Oh My~!
        kay "R-rub!?"
        $dshow(12014)
        ava "Yes, rub! Can you not see that this is a life or death situation!?"
        kay "(This is just too much! Ava might think this is nothing more than a survival exercise, but there's no way a healthy guy like me's just gonna rub down a woman without getting all kinds of weird reactions!)"
        kay "U-uuh... Well, that's definitely gonna get me hotter all right, but probably not in the way that you think!"
        $dshow(12024,blush=True)
        ava "Idiot! What the hell are you saying!?"
        $dshow(13100)
        ava "Ah, nevermind! I see that you have not matured a day since advanced academy, Kayto!"
        kay "I'm just saying...! Ah for--!"
        ava "Unbelievable! Just unbelievable! The safety of the ship is at stake here, and you're too caught up in your juvenile fantasies to even employ basic survival tactics!"
        ava "Ah, I can't believe Command actually made you captain, Kayto! Obviously, we'd all be in better hands if I were in charge!"
        $dshow(13201)
        ava "... ... ..."
        $dshow(12100)
        "Ava suddenly started giggling."
        ava "Haha... Hahahaha....!"
        "Shields stared at her incredulously."
        kay "Damn... It must have been a decade since I've heard you laugh like that..."
        $dshow(12424)
        ava "...Idiot."
        ava "Sigh..."
        ava "I guess... it's been a while..."
        kay "Ava? A while since what?"
        ava "Since you actually relied on me..."
        kay "What are you talking about? I rely on you all the time."
        ava "Not merely for the paperwork, Kayto. But for something big."
        ava "I imagine the talented girls we've found throughout the galaxy are the cause of my obsolescence..."
        ava "The truth is that you've actually grown."
        ava "I'm... still not quite used to the new you. You're a leader now. A far more capable one than me. And... sometimes I fear you will soon have no need of me at your side."
        kay "Ava..."
        $dshow(12414)
        ava "Ahem. Of course, you are not the captain of this ship, so this in no way means I intend to change the way I handle my professional relationships. But..."
        kay "Heh. What are you saying..."
        kay "Just look at the past few hours. Where would I be without my high performing childhood friend?"
        kay "If it weren't for you... I'd probably be passed out cold in this tunnel right now. Hell, I probably would never even have managed to send the transmission to Fontana."
        kay "I still need you, Ava."
        $dshow(12402)
        ava "Then... I guess I don't have anything to worry about..."
        "Ava finally peeled herself off Shields. The two of them shivered as the icy air hit them nearly as sharply as the loneliness of being separated."
        ava "I'm feeling better. Let's get a move on."
        kay "All right."
        "They once again returned to their ascent back to Deck 1..."
        
        jump restoringpower

    if girl == "Asaga":
        $dshow(54)
        asa "Hey, so what's up with this backup comm anyways? I didn't know we had something like that..."
    if girl == "Sola":
        $dshow(70220)
        sol "Explain to me the specifics of the backup comm."

    if girl != "Icari":
        kay "It's one of a few systems which keep operating under battery power when the ship loses power like this. Basically, when the ship's disabled, we need to be able to breathe and call for help. That's why life support and the FTL comm keep working."
        kay "It's a lot more limited than the regular ones though. We can only transmit a text message less than 120 characters in length, and the message can only be broadcast on the intergalactic distress and rescue channel."
        kay "Another problem is that the batteries are still nowhere powerful enough to power life support for the entire ship. The air's going to get really thin on deck 2 real fast."
    if girl == "Icari":
        kay "(The back up comm's one of a few systems which keep operating under battery power when the ship loses power like this. Basically, when the ship's disabled, we need to be able to breathe and call for help. That's why life support and the FTL comm keep working.)"
        kay "(It's a lot more limited than the regular ones though. We can only transmit a text message less than 120 characters in length, and the message can only be broadcast on the intergalactic distress and rescue channel.)"
        kay "(Another problem is that the batteries are still nowhere powerful enough to power life support for the entire ship. The air's going to get really thin on deck 2 real fast.)"

    if girl == "Asaga":
        asa "I'm sure it won't be any tougher than flying a ryder... But basically, this isn't going to be as easy as just crawling to the comm room and sending a message?"
    if girl == "Sola":
        sol "I have endured worse. However, the road ahead looks long."

    if girl != "Icari":
        kay "Yeah. All the lifts and trams are offline as well, so we'll be crawling through about 300 meters of maintenance tunnels."
    if girl == "Icari":
        kay "(All the lifts and trams are offline as well, so I'll be crawling through about 300 meters of maintenance tunnels.)"

    if girl == "Asaga":
        asa "All right, lead the way, capt'n!"
    if girl == "Sola":
        sol "Then let us hurry."

    #Tunnel
    scene black with horizontalwipe
    scene bg tunnel with horizontalwipe
    "After roughly half an hour of climbing down ladders and crawling through maintenance shafts hardly wider than sewage pipes, Shields could begin to see his breaths turn into frost vapors. The air was no longer as rich with oxygen, making the trek all the more arduous."
    "The outer most sections of the ship were quickly dissipating heat into space, and life support was slowly losing the battle to keep the extremities of the ship fit for human life."
    
    if girl != "Icari":
        "He looked back."
        kay "[girl], how're you holding up?"
        
        if girl == "Asaga":
            $dshow(230)
            "Asaga still looked to be in good condition."
            asa "A 'lil cold's no prob! Better cold than too hot, 'cause I'd be drenched with sweat otherwise!"
        if girl == "Sola":
            $dshow(70020)
            "Sola's teeth was chattering, but she otherwise did not exhibit any signs of hypothermia."
            sol "I can still carry on."

        kay "All right. We're... about halfway there. It's only going to get colder from here on out. Keep your body moving, and tell me if you lose sensation to your extremities."

        if girl == "Asaga":
            asa "Understood!"
        if girl == "Sola":
            sol "Understood."

    #Wipe
    scene black with horizontalwipe
    scene bg tunnel with horizontalwipe
    
    if girl != "Icari":
        "Another forty minutes later, they nearly arrived at their destination. Unfortunately, the latter half of the trip took longer than expected thanks to the bitter cold."

    if girl == "Icari":  
        "The walls were now frozen solid with a thin layer of ice, while small icicles hung from the pipes running along the wall of the tunnel."
    
    "Shields's head spun thanks to the lack of oxygen, which only made the numbness in his fingers and toes  worse."
    kay "(Shit... I completely forgot how much I hated the cold...!)"
    kay "(I remember I used to complain to Ava every day during the winter about our school uniforms...)"

    if girl != "Icari":

        kay "(The military uniforms we have now are of course made from thermaweave and can retain body heat much better than wool, but we'd need something closer to a plugsuit to keep us protected against elements like this...)"
    
    if girl == "Icari":
        kay "(The military uniforms we have now are of course made from thermaweave and can retain body heat much better than wool, but I'd need something closer to a plugsuit to keep myself protected against elements like this...)"

    if girl == "Asaga":
        $dshow(532)
        asa "Brrr... Aahhh it's shit cold, capt'n! It's even more shit cold than the winters at Ryuvia! Aahhh!!!"
        asa "Let's finish up here as soon as we can and get outta here!"
        asa "I can hardly even talk 'cause all the snot in mah nose's frozen! Uggghhh!"

    if girl == "Sola":
        $dshow(70000)
        sol "H-ggnnbrbh..."
        "Sola's face was even paler than usual as she trembled weakly in the cold."
        kay "Are you all right, Sola?"
        sol "Y-yes... U-u-unfo-fortunately-"
        sol "F-Far P-Port is a... h-hot w-w-world..."
        kay "You're right, you were born there, weren't you?"
        sol "Y-y-yes... I-I-'m afraid t-the c-c-cold is an a-a-alien exper-ience..."
        kay "(I didn't think that section 37 would get this cold... Sola looks like she's in pretty bad shape...)"
        kay "We're almost there, Sola! Just hang on a bit longer."
        sol "U-u-und-erstood..."

    "Finally, Shields arrived at a tiny alcove in the tunnel. With trembling hands, he removed the wall panel, exposing the controls of the FTL comm."
    "Icicles hung from the comm's cables, while a thin layer of frost caked the steel casing."
    kay "Goddamnit... This thing had better still be working..."
    "His pressed the activation button, but the comm showed no signs of life."
    kay "Shit..."
    kay "What the hell's wrong with this thing...?"
    "He tried to troubleshoot the problem, making sure all the cables were connected. Finally, he came upon a single unplugged cable, dangling at the bottom of the case. Unfortunately, the cable's slot was now obstructed by a solid block of ice, making it impossible to plug back in."
    "He tried to force the cable's steel rod into the receptor, but the hole was completely filled with ice."
    "Frustration bubbled instead of him. Who had dropped the ball and left this cable unplugged!? Was it a member of the maintenance crew? A malfunctioning repair drone?"
    "His head spun thanks to oxygen deprivation, making it impossible to think logically."
    kay "(Tsch... No... I have to remain focused...)"
    kay "(Put. Plug. Into receptor.)"
    kay "(That's what you're here to do...)"

    if girl == "Asaga":
        $dshow(551)
        asa "Is something the matter?"
        
    if girl == "Sola":
        $dshow(70020)
        sol "I-i-is s-something... t-the matter?"

    kay "Someone accidentally left a cable unplugged... I won't be able to turn the comm on without it. But the receptor's now frozen solid."

    if girl == "Asaga":
        $dshow(602)
        asa "Eeeh!? Ah, c'mon, why's nothing going as planned today of all days!?"
    if girl == "Sola":
        $dshow(70010)
        sol "Alas... P-perhaps m-m-my l-l-lifelong misfortune is s-sabotaging the mission..."

    kay "Shit... Uhh..."
    "Shields racked his brain for a way to thaw the ice inside the receptor. The plug was hardly larger than a pen. It wouldn't take much heat to melt the ice inside, but without the proper tools..."
    "Argh, he wasn't thinking properly. He should have come prepared with a blow torch or something..."
    kay "(Hindsight is always 20/20...)"
    kay "Tsch. There's only one option."
    kay "I'm going to cross the charges on the battery. It'll make the power cables overheat and melt the ice away."

    if girl == "Asaga":
        $dshow(542)
        asa "But won't that also burn out the comm too?"
    if girl == "Sola":
        sol "B-but the comm itself may get damaged..."

    if girl != "Icari":
        kay "It's the only option we have left!"
        
    "Thanks to the oxygen deprivation and his grim realization that they would not last much longer in the cold, Shields immediately unplugged the two power cables and crossed the charges without a second thought. As expected, the power connections from the batteries to the comm unit began to emit smoke."
    "The smell of acid burned Shields' nose as the power cables suddenly became extremely hot."
    
    play sound "sound/spark.ogg"
    show white
    pause 0.1
    hide white
    
    "Suddenly, sparks flew from the comm box as a conduit burst."

    if girl == "Asaga":
        $dshow(655)
        asa "Stop, stop!!!"
    if girl == "Sola":
        $dshow(70422)
        sol "A-ah!"

    "Shields uncrossed the charges in panic. On the bright side, the ice was now melted from the receptor. That is, if he didn't just blow up the comm. He grabbed the cable and successfully plugged it in."
    kay "(Did it... work? Or did I just melt the only comm we could use to warn Fontana's fleet?)"
    "He took a deep breath and turned the comm on."
    "He breathed out in relief when it amazingly activated."
    kay "We're in business!"

    if girl == "Asaga":
        $dshow(2020)
        asa "All right!"
    if girl == "Sola":
        $dshow(70103)
        sol "Haa..."

    kay "(Damn... I can't believe I actually did a thing like that... If Ava were here, she'd probably murder me...)"
    kay "(But looks like my luck's still holding. Fontana, you better read this message after everything we went through to send it!)"
    "Shields used the comm's keypad to type out the warning to Fontana and relayed it."
    kay "Now... All we can do is pray someone on board Fontana's ship is watching the distress channel... And takes the message seriously enough to relay it to Fontana."
    
    if girl != "Icari":
        "The look of relief on [girl]'s face deflated. True enough, even if they sent the message, there was no guarantee anyone would read it. This was still a long shot..."
    
    "Shields reattached the wall panel, once again closing the comm."
    
    $ backup_comm = True
    
    if girl != "Icari":
        kay "Come on, we've done all we can here. We need to get deeper into the ship, before we freeze to death."

    if girl == "Asaga":
        $dshow(112)
        asa "No kidding..."
    if girl == "Sola":
        sol "Y-yes..."

    if girl != "Icari":
        "The duo made their agonizingly slow return to the center of the ship."
        "Their extremities were now completely numb and their consciousness faded in and out because of the thin air. The return trip proved far more difficult than their first expedition. Worse still, since they were heading to deck 1, they now had to climb up frozen ladders, instead of climbing downwards."

    if girl == "Icari":
        
        play music "Music/Anguish.ogg" fadeout 1.5
        
        "Shields made his agonizingly slow return to the center of the ship."
        "His extremities were now completely numb and his consciousness faded in and out because of the thin air. The return trip proved far more difficult than his first expedition. Worse still, since he was heading to deck 1, he now had to climb up frozen ladders, instead of climbing downwards."

    if girl == "Asaga":
        #ASAGA
        play music "music/Love_Theme.ogg" fadeout 1.5
        asa "U-ugh... T-this is nuts..."
        asa "Aaahh... I remember the time I had to hike up Mount Destiny for my baptism... But this is even worse..."
        kay "Baptism?"
        $dshow(10)
        asa "Ah, a dumb ritual the Church expected me to perform... Honestly, nobody believes any more that the Emperor is God or anything... I had to climb up the whole mountain... and soak myself with water at the peak inside a temple... It was completely televised throughout the planet..."
        $dshow(11)
        asa "Maybe the Ryuvian media companies keep pressing the royal family to continue the tradition because tons of geezers tune in to watch the princess suffer while hiking a ten kilometer long trail, and then upon reaching the top, they get prime time coverage of a girl dumping a bucketful of water on her nubile young body... I bet they make millions off advertising revenue alone..."
        kay "Err... B-body? This sounds a little risque for national holovision..."
        $dshow(31)
        asa "Ah, well... I was fully clothed in my ceremonial gown, obviously. I still got soaked though..."
        asa "Anyways, I'm getting bad flashbacks..."
        kay "Must have been hard. I forget sometimes that you're royalty."
        $dshow(51)
        asa "Eh... honestly, I'd prefer if you just forgot all together."
        asa "I'm... not really looking forward to going back. In fact... lately... it's been my greatest fear."
        asa "... ... ..."
        $dshow(31)
        asa "I'm not the princess any more. I'm supposed be the leader of my people now."
        asa "Whenever that realization sinks in... I never want to leave this ship. I... just want to keep flying the Black Jack, and go on adventures with you..."
        
        $dshow(32)
        
        asa "If I go back... I'm going to be chained. Even though I'll be the most powerful person on Ryuvia Prime... The throne's going to become my prison."
        asa "I won't be able to fly the Black Jack any more. I won't be able to be the hero."
        asa "I'll just have to sit on a fancy chair for the rest of my life... And watch Ryuvia waste away. Just like the prior rulers before me. Until eventually I grow old too, and I die."
        kay "Asaga..."
        "They rounded the corner and came upon yet another ladder. Asaga doubled down and panted, obviously in no condition to climb up."
        $dshow(532)
        asa "Let's take a short break, capt'n... Dunno if I can climb up another ladder without slipping."
        kay "All right. I need a break too."
        "The two of them crumpled down beside each other."
        $dshow(31)
        asa "... ... ..."
        asa "Hey capt'n, ya suppose what Claude's saying is right?"
        asa "If we really succeed with this mission, then none of this will ever have happened?"
        kay "I don't know... From what she said, even though this mission will be wiped from history, a new universe where the outcome is the same, but where the time paradox has now been resolved, will be created..."
        asa "So... in the end... whatever we accomplish here will carry on to the next universe?"
        kay "I think that's the gist of it."
        $dshow(444,blush=True)
        asa "... ... ..."
        asa "Hey capt'n... I'ma cold..."
        
        $dshow(3012,blush=True,ypos=1600)
        
        asa "Aren't you supposed to be hugging the girl in situations like this? \"I've gotta save her with my body heat!\" You know?"
        kay "Heh... Haha..."
        "Shields offered Asaga his hand."
        $dshow(422,blush=True)
        "Their ice cold hands touched each other, fingers intertwined."
        "They rubbed their fingers against each other, trying to restore colour to their deathly white hands. The desperate situation robbed the moment of the intimacy Asaga had hoped for."
        "She inched closer to Shields."
        $dshow(434,blush=True)
        asa "Hey capt'n... So... uhhh..."
        asa "Ahem."
        "In an out of character moment, Asaga suddenly lost her words and stared at the ground."
        kay "That's unusual. This is the first time I've seen the proverbial cat catch your tongue."
        $dshow(614,blush=True)
        asa "Aaah, mou, capt'n! You know what I'm gonna ask!"
        $dshow(643,blush=True)
        asa "Do you... uhh... still... like Chigara?"
        kay "... ... ..."
        $dshow(43,blush=True)
        asa "... ... ..."
        asa "Sorry."
        asa "I know I it's a dumb thing to ask."
        asa "And you know what? It's all right if you still have feelings for her, somewhere down there. That's only expected." 
        $dshow(252,blush=True)
        asa "Eh-heh... It's not a deal breaker for me, as long as you only go out with me from now on..."
        $dshow(434,blush=True)
        kay "... ... ..."
        kay "I trusted her."
        kay "For a moment, she was the only person I lived for."
        kay "And that was my downfall."
        kay "Now I'm here... to stop her."
        kay "If I have any feelings for her... I need to control them. For the sake of this mission. The lives of billions are at stake now."
        kay "I'm not going to make the same mistake twice."
        $dshow(425,blush=True)
        asa "... ... ..."
        asa "Eh-heh... Somehow, I'm glad to hear that..."
        "Asaga leaned against Shields, their bodies finally touching."
        $dshow(422,blush=True)
        asa "In both this universe and the one you came from... I'm always on your side, captain."
        asa "If you need someone you can depend on... I'll always be here. I... won't ever stop protecting you. I'll fight alongside you to the bitter end."
        kay "Don't say ominous things like that, Asaga... I think you've raised enough death flags in a single day."
        kay "... ... ..."
        kay "We're all going to get out of this alive."
        $dshow(452)
        asa "Eh-heh... Mah, I guess that's a given, with you here."
        asa "Fighting for a better future, huh..."
        asa "Even if the future changes... I know for sure that my feelings for you will stay the same."
        asa "Eh-heh... You'll still be waiting for me, right?"
        kay "...Yeah."
        kay "(Asaga...)"
        kay "(The mission's my number one priority... But this girl's always had feelings for me... I can't ignore her any more...)"
        kay "I was in the wrong. If there is a better future waiting for us... Let's spend it together. We still have many adventures ahead of us. It's too soon to retire. Not when we still have villains to defeat."
        kay "The Sunrider still needs us. The Black Jack still needs you."
        kay "After all, who's going to save the day without the Sunrider's ace?"
        $dshow(222)
        asa "Heh-heh..."
        $dshow(230)
        asa "Yeah!"
        "With that, Asaga warmed herself by falling into Shields' lap."
        $dshow(321)
        asa "Mmm... lemme just warm up..."
        asa "Ufufu... Your lap pillow ain't so bad..."
        kay "Heh... I guess you could borrow my lap if it's for the sake of the mission..."
        $dshow(533)
        asa "Eeh? That's the only reason? So stingy..."
        kay "Sorry. Space captain first. Boyfriend second."
        $dshow(612)
        asa "Lame..."
        kay "A lesson learned from past experience."
        asa "Meh..."
        $dshow(432)
        asa "Ah well. I guess I'll have to be satisfied with just this much for now then..."
        asa "Mmm..."
        $dshow(442,blush=True)
        "Asaga closed her eyes. In complete contrast against her usual fiery attitude as the Sunrider's CAG, she now looked completely defenseless on his lap." #deresaga!
        "For a moment, Shields couldn't help but wonder if he should be doing this. While his memories of the past haven't perfectly crystalized yet, he remembered enough to know that his feelings had been his downfall..."
        kay "(Well... I guess I can trust Asaga. I know for sure she's not a spy, at least.)"
        "With that, Shields put his arms around her."
        "The two of them spent the next few minutes warming themselves..."
        
        if captured == True:
            jump badend_deathbydecompression #that escalated quickly!
        if captured == False:
            jump restoringpower
        
    if girl == "Sola":
        
        #SOLA
        
        stop music fadeout 1.5
        
        "Shields could hear Sola's raspy breathes behind him."
        "His chest began to pound. While he was no doctor, it was clear she was suffering from hypothermia. He had to get her out of here soon!"
        hide sola with dissolve
        
        play sound "sound/punch.ogg"
        show layer master at tr_yshake
        
        "His worst fears came to pass when he heard a thud behind him."
        
        play music "Music/Anguish.ogg" fadeout 1.5
        
        "Shields turned around to see Sola passed out on the steel flooring of the maintenance tunnel."
        kay "SOLA!!"
        "He rushed over to her and checked her vitals. Thankfully, she was still breathing, but her palms were icy cold and she was hyperventilating due to exhaustion and oxygen deprivation."
        kay "(Shit... I should never have brought Sola here...)"
        kay "(Her body's not accustomed to cold... I should have remembered she's from Far Port...)"
        $dshow(70000)
        sol "Haa... haaa..."
        "Her stomach was twitching as she gagged for air, saliva bubbling at the corner of her mouth. At this rate, she was going to suffer brain damage due to the lack of oxygen or lose her limbs when her body water froze."
        "In desperation, Shields tore his coat off and wrapped it around Sola. He gasped as the wintery air assaulted his body."
        kay "(Shit! Shit! That's not going to work!)"
        kay "(Without my coat, we're both going to freeze to death!)"
        kay "(Ah, I don't have any other choice! I'm sorry, Sola!)"
        "He lifted Sola's trembling body up against him, straddling her legs around his waist and wrapping their arms against each other. He then used his coat as a makeshift blanket, wrapping both of them inside."
        "His personal embarrassment be damned, he had to warm Sola up before her life was in danger."
        "Thankfully, Sola's slender body was small enough to fit inside his coat and not too heavy to hold in his lap."
        kay "(Come on Sola... Live!!)"

        #wipe
        scene black with horizontalwipe
        scene bg tunnel with horizontalwipe
        play music "music/Love_Theme.ogg" fadeout 1.5

        "... ... ..."
        "... ..."
        "..."

        "After over an hour of being wrapped around Shields' body, Sola's breathing finally normalized."
        $dshow(70112)
        "She opened her eyes again."
        sol "Ah..."
        "Shields sighed in relief."
        kay "You collapsed because of hypothermia. I managed to warm your body back up, but we should still take the return trip slowly."
        kay "Can you still feel your hands and feet?"
        $dshow(70122)
        sol "Y-yes... It appears you have saved me from the worst case scenario."
        sol "... ... ..."
        sol "You have my gratitude."
        kay "No... Protecting your life is my responsibility as captain."
        kay "It was my mistake bringing you here. I should have known you weren't used to the cold."
        $dshow(70103)
        sol "No... Who knows what may have happened if you undertook this mission alone."
        $dshow(70210)
        sol "I... proved to be nothing but dead weight. Because of my weakness, we have lost valuable time..."
        sol "You should have merely left me behind... It would have been the sound decision, as your mission is far too great to be compromised by a single person."
        kay "(This again? How many times do I have to repeat myself...)"
        kay "Stop that, Sola! For the last time, you're not a pawn to be sacrificed."
        kay "I'm... not going to throw you away!"
        $dshow(70203,blush=True)
        sol "A-ah... I-I am... sorry..."
        sol "... ... ..."
        "Sola's face blushed as I cradled her."
        "She spoke softly, her words barely a whisper."
        $dshow(70303,blush=True)
        sol "... ... ..."
        sol "You are... warm..."
        kay "You can stay like this as long as you want. Your body still hasn't regained its full strength yet."
        sol "Understood..."
        "Shields could feel her body relax."
        $dshow(70103,blush=True)
        sol "H-holding me like this... i-in such a scandalous position..."
        sol "H-huuu..."
        kay "Hahaha. Don't worry about a thing, Sola. This is for our survival. I won't take this the wrong way."
        $dshow(70110)
        sol "W-won't t-take in the wrong way...?"
        sol "... ... ..."
        "All of a sudden, Sola pouted in his arms."
        $dshow(70102)
        kay "(Ah... So she wanted me to take it in the wrong way then?)"
        kay "(Women... are so complicated...)"
        sol "... ... ..."
        kay "(What's this sudden awkward mood?)"
        kay "(Urk... She's so close to me that I can feel her heart pounding. W-was it always pounding that quickly before...?)"
        $dshow(70221)
        sol "... ... ..."
        "Sola raised her hand and put it around his back."
        sol "Then...it's for survival only..."
        kay "Uhh... yeah...! Rest up, Sola! We've still got a long way back!"
        $dshow(70301,blush=True)
        sol "Yes captain..."
        sol "... ... ..."
        sol "I understand now..."
        kay "Sola? What do you understand?"
        sol "...a great many things."
        $dshow(70322,blush=True)
        sol "How we came to be together. Why Asaga yearns for your other self. Why my heart beats so terribly right now."
        kay "Sola..."
        sol "... ... ..."
        $dshow(70210)
        sol "I am sorry. I have overstepped my position."
        sol "We still have the mission. I... cannot afford to distract you. Not until the massacre has been averted."
        sol "Then... perhaps in the next universe... we will finally..."
        kay "... ... ..."
        "Somewhere in his heart, he wanted this situation to continue. But his duty to the mission came first. For now, he would have to swallow his feelings."
        $dshow(70221)
        sol "I am ready to continue. Let us hurry. We have already lost too much time."
        kay "All right. Keep close, and let me know if you need to take another break."
        sol "Understood."
        "Sola finally peeled herself off Shields. The two of them shivered as the icy air hit them nearly as sharply as the loneliness of being separated."
        "They once again returned to their slow crawl back to Deck 1..."
        
        if captured == True:
            jump badend_deathbydecompression
        if captured == False:
            jump restoringpower

    if girl == "Icari":
        if not trustclaude:
            $renpy.save("BAD END 6")
        
        #ICARI

        "Shields carried on by himself, his ragged breaths freezing into vapor clouds in front of him."
        "His knees and hands burned from hours of crawling through the Sunrider's frozen maintenance tunnels. He knew he had to head deeper into the ship quickly, before his body gave out on him."
        "If he fell unconscious here, he would surely freeze to death before anyone could find him."
        kay "(Come on... I can't give up... Not when I finally managed to send the message to Fontana...)"
        "He came upon a ladder roughly fifteen meters high. With a deep breath, he clambered up, desperate not to lose any more time."
        "His throat burned with each step upwards. His fingers were trembling."
        
        play sound "sound/hit.ogg"
        
        "His feet unexpectedly gave out halfway up the ladder, making him tumble down and bang his other knee on the ladder's step."
        kay "U-ugck...!"
        "Agony shot up his thighs."
        "He begged his arms to hang on to the ladder, but his fingers were now frozen solid."
        
        show black:
            alpha 0.5
        with dissolve
        hide black with dissolve
        
        "The corners of his vision blacked out as his lungs screamed for more oxygen."
        "The pain finally proved too much to bear and his foot slipped off the frozen step. Shields flailed as he fell down the rest of the ladder... until he hit the ground flat on his back."
        
        play sound "sound/gore.ogg"
        show layer master at tr_yshake
        
        kay "G-GACK--!!"
        "He felt as if he had been impaled upon a spike. With a gasp, he expulsed a final pitiful breath of air before darkness descended upon him..."
        scene black with dissolve
        
        ##IF DID NOT TRUST CLAUDE
        if trustclaude == False:

            kay "S-someone..."
            "Shields gasped for help, his consciousness ebbing away on  the floor of the frozen corridor..."
            "But nobody answered his call."
            "His arms flopped to the ground as he lost consciousness."
            "... ... ..."
            "Not a soul came to Shields' rescue as his body gradually lost all of its heat."
            "The maintenance tunnel became Shields' icy grave as his body finally gave out."
            "By the time ship security found him, his body was nothing more than a block of frozen flesh."

            #BAD END
            stop music fadeout 1
            play sound1 "sound/choirend.ogg"
            $persistent.unlocked_endings["BAD END 6: FROZEN"] = True
            $check_for_all_endings()
            show screen bad_end6
            pause 3
            $dshow(34111)
            cla "Hmph... Captain, you made a very pivotal mistake here..."
            cla "You chose NOT to trust poor ol' Claude when she worked day and night to bring you back into this timeline!!!"
            $dshow(34301)
            cla "Mou, I can't even look at you any more..."
            cla "Go back to when you kidnapped Chigara and chose to trust me instead! Then maybe I'll help you... Hmph!"  #where the hell is Thor when you need him?
            hide claude
            pause
            $renpy.full_restart()

        "... ... ..."
        "... ..."
        "..."
        
        
        scene bg tunnel with dissolve
        "He woke up, enveloped in warmth."
        kay "(Ugh... What's... going on...?)"
        kay "(The last thing I remember is falling off the ladder...)"
        kay "(I am... dead?)"
        play music "music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5 #hehe
        "One look around revealed that he was still in the Sunrider's maintenance tunnels. So he was most certainly not dead."
        "He groped around for his surroundings, and grabbed a large, squishy mass floating over his head."
        kay "What the--"
        $dshow(30000,ypos=1600,xpos=0.5)
        cla "Ara..."
        kay "G-guck!"
        "Shields pulled himself up, only to receive a face full of Claude's massive mammies. She seemed completely unfussed by his accidental feel, however."
        $dshow(30010,ypos=1600)
        cla "Aah, captain! You're finally awake! Claude was worried you were about to hit another bad end!"
        kay "C-Claude!? How'd you get here!?"
        "Shields realized he already knew the answer to that question and decided to replace it with a more helpful one."
        kay "Err... I mean, why'd you come here?"
        $dshow(34000)
        cla "Mou, isn't it obvious? To rescue my poor darling, of course!"
        $dshow(34010)
        cla "I can't have you die in such an anti-climatic fashion. Aaaand, it was my lucky chance to nurse you back to health... using nothing more than my... body warmth. Hufufu..."
        "Shields shuddered and checked himself to make sure everything was still as he had left it."
        $dshow(34110)
        cla "Claude's here to help! Even though the captain thinks I'm nothing but a nuisance... Sniffle..."
        kay "Look here, Claude... You vanished on me at a pretty important moment... Just what are you doing, disappearing and reappearing on a whim like that?"
        kay "Can't you at least be a little more helpful?"
        $dshow(34310)
        cla "Ah... well..."
        cla "It'd actually be for the best if I kept my power usage to a minimum..."
        cla "As I said... The law of causality's quite a forceful man when it comes to treating naughty time paradoxes like myself... If I become too noticeable..."
        $dshow(34011)
        cla "Iyaaa... I'm afraid the Law will grab poor Claude by the hair and push her down and pound her until she... vanishes off the face of the universe."
        $dshow(34000)
        cla "Usually things are all right as long as I don't touch the time machine... But the more I flick my secret time button... Huufuufu... You get my drift, captain..."
        "Shields rubbed his face in frustration. That seemed like a common occurrence whenever he was speaking with Claude."
        "Before he could get off her lap, she wrapped her arms around his face."
        $dshow(34311)
        cla "Your body was almost frozen solid when I found you..."
        $dshow(34000)
        cla "Iyaa... Claude had to strip off everything and envelop you with my love to restore your HP..."
        cla "It was a long process... But gradually your HP bar began to fill back up with blood..."
        cla "Until it stood on end, about to burst from all the love that this maiden was giving to restore her beloved back to health...!"
        $dshow(34211)
        cla "It was at this point that this maiden was confronted with a true dilemma. Do I let the HP gauge burst and start over from zero? Or do I keep it at maximum strength? Ah, it was truly a nightmarish choice..."
        kay "All right, all right..."
        "Shields shuddered at what may have happened while he was unconscious."
        "For the better or worse, his body felt restored to health at least."
        "Whatever Claude had done to him, he felt light as a feather, as if he had just woken up from a refreshing sleep."
        kay "Uhh..."
        kay "Thanks for saving me then."
        $dshow(34010)
        cla "Oooh... This is quite rare. The captain, actually thanking ol' Claude?"
        "He sighed."
        kay "I would have died out here if you hadn't come. So I guess I at least owe you my thanks."
        $dshow(34211)
        cla "Uufufufu... I could think of a whole lot of other ways you could repay this debt..."
        cla "How 'bout a quickie, right here?"
        "Any trace of gratitude vaporized from Shields' mind at Claude's outrageous suggestion."
        kay "Like we could do it in the middle of a frozen maintenance shaft, you dork!"
        $dshow(34001)
        cla "For a chance with you, captain, Claude will move the mountains and create new stars!"
        $dshow(34210)
        kay "Aaah, I was the fool."
        kay "Like anything would come out of being grateful to you. Let's... just get a move on."
        $dshow(34211)
        cla "Mou, I don't appreciate the sudden tsundere act, captain... This ship already has plenty of those..."
        kay "Do I look like Icari to you!?"
        $dshow(34201)
        cla "Aaah, lame... Looks like you just lost your chance at holding these godly boobs in your palms, captain..."
        "Claude winked as she jiggled her chest."
        "Shields finally managed to peel Claude off of him and sit back up."
        kay "So, are you planning on sticking around this time?"
        $dshow(34210)
        cla "Of course, captain! Unless another sticky situation happens where I might be forced to use my powers, of course..."
        kay "Right."
        kay "Well uhh... I'll try to stay out of trouble then."
        kay "So how long was I out?"
        cla "For about an hour."
        kay "Tsch. We better move. We've wasted too much time here."
        kay "The ship's still without power. We need to head to engineering and figure out a way to turn the reactor back on."
        $dshow(36000)
        cla "Undastood, capt'n! Now uhh... Teehee."
        $dshow(30010,ypos=1600)
        cla "Shall Claude go uppy the ladder first?"
        kay "Uhhh... no."
        kay "I'll take point. Follow me."
        $dshow(34111)
        cla "Booo... And I took the extra effort to wear my special panties for you today..."
        kay "(You see, that's exactly what I was afraid of...)"
        kay "Now's not the time to fool around, Claude. Let's move."
        $dshow(36010)
        cla "Sah!"
        $dshow(34200)
        
        if captured == True:
            jump badend_deathbydecompression
        if captured == False:
            jump restoringpower
        
label badend_deathbydecompression:
    $renpy.save("BAD END 7")
    
    #IF NOT ON AVA ROUTE AND CAPTURED

    #TUNNEL "T-minus 43 hours before the Liberation Day Massacre, 7 hours until Chigara enters the mind stream"
    
    stop music fadeout 1.0
    
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 43 hours before the Liberation Day Massacre, 7 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
        
    scene bg tunnel with dissolve
    "The pair continued their slow return to Deck 1. Gradually, the air thickened with oxygen and the temperature increased the further away they got from the ship's extremities."
    kay "Looks like we're almost safe..."
    stop music fadeout 2
    kay "Next up, we need to get to Engineering and find a way to restore power. If we don't get the ship operational again before the next battle, sending the transmission to Fontana won't even matter because we'll just all-."
    show layer master at shake1
    play sound "sound/explosion2.ogg"
    play music "Music/MarduksWrath.ogg" fadeout 1.5
    "Before Shields could finish, the ship shook as a massive explosion bent the hull."
    kay "A-argh! Damn!"
    kay "What was that!?"

    if girl == "Asaga":
        $dshow(1121)
        asa "Eah! There's only one thing that coulda been! We're under attack!"
        
    if girl == "Sola":
        $dshow(71000)
        sol "Tsch. The Sunrider is under attack."
        
    if girl == "Icari":
        $dshow(34310)
        cla "Ooh! The ship's under attack!"

    kay "(Shit... This didn't happen in my time line...)"
    kay "(Of course... We've altered the course of history by revealing ourselves to the Prototype leader before the final battle... Is she now going to use this opportunity kill us all here?)"
    kay "Come on! To Engineering, double time!"

    if girl == "Asaga":
        $dshow(2100)
        asa "Roger!"
    if girl == "Sola":
        sol "Understood."
    if girl == "Icari":
        $dshow(36010)
        cla "Sah!"

    "They scrambled to Engineering as quickly as their knees would take them."

    #Engineering
    scene bg engineering_np
    if girl == "Asaga":
        $dshow(32,xpos=0.25)
    elif girl == "Sola":
        $dshow(70122,xpos=0.25)

    "Crewmen scrambled as the ship shook. Pipes burst throughout the room, spewing clouds of vapor. Without any power, the ship was both toothless and blind!"
    kay "(Shit! I should have seen this coming... Of course the Prototypes would exploit an opportunity like this to sink the ship!)"
    "Shields screamed to a crewman."
    kay "What's the situation!?"
    cre1 "Sir! Crows' nest reports that the PACT fleet has advanced on our position! The Combined Fleet is trying to hold PACT back, but they are getting decimated by a new enemy ryder, unlike anything we've ever seen before!"
    kay "(New enemy ryder...? Shit... That can only mean...)"

    #Nightmare Ascendant CG
    show nightmare_approach
    show black:
        alpha 0.5
    with dissolve
    "Shields still vividly remembered the terrifying power of the Nightmare Ascendant. Only with the Combined Fleet, Fontana's ships, and the Sunrider at full capacity, acting together did they manage take it down in his timeline..."
    hide nightmare_approach
    hide black
    with dissolve
    "But now, he had no idea whether Fontana's ships were even operational, while his own vessel was completely shut down."
    "In other words, unless he found a way to restore power, they were all going to be dead in moments."
    "Shields ran to the reactor's controls and found Icari furiously pounding away on the console."
    kay "Icari! What's the situation!"

    if girl != "Icari":
        $dshow(41210,xpos=0.75)
        ica "What are you doin' here, cap!? Aren't you supposed to be on the bridge!?"
        kay "No use! Without power, there's nothing we can do!"
        $dshow(40520)
        ica "Tsch... I don't really know what's going on either... But the reactor's somehow been completely shut off. But now that you're here, I might be able to trick the system into doing a manual reboot."

    if girl == "Icari":
        $dshow(41111,xpos=0.75)
        ica "There you are! Did you manage to send the message!?"
        kay "Yeah! How're things on this end!?"
        $dshow(41112)
        ica "I've been trying to hack through the logic bomb Chigara set up for us for the last few hours... Luckily, I think I found a weakness!"

    show layer master at shake1
    play sound "sound/explosion2.ogg"
    "The ship took another hit, knocking the two of them off their feet."
    $dshow(41211)
    ica "Damnit!"
    "Overhead, Shields heard the groaning of steel. Shields looked to the ceiling just in time to see a massive steel beam give out."
    kay "Icari, look out!"
    
    play sound "sound/punch.ogg"
    show layer master at tr_yshake
    hide icari with dissolve
    "Shields tackled Icari to the ground and covered her with his body, as metal plating and rods rained down."
    "Dust filled the air as the two were buried in rubble. Miraculously, they somehow avoided becoming impaled in the hailstorm of rods. Shields stood and shook off the pain and dust."
    "He checked Icari's status. Aside for minor scrapes, she still appeared fine."
    kay "Are you all right!?"
    $dshow(40523)
    ica "Y-yeah! Thanks!"

    if girl == "Asaga":
        $dshow(632)
        asa "Capt'n, we gotta restore power now!!! The ship's getting torn apart!"
    if girl == "Sola":
        $dshow(70420)
        sol "We must restore power! The Sunrider is breaking apart!"

    kay "Icari, how do we restore power!?"
    $dshow(40522)
    ica "Inside the reactor... There's an internal control relay! You need to swipe your command ID on it. Then I can trick the system into performing a manual restart!"
    kay "I-INSIDE the reactor!?"
    ica "You heard me right!"
    kay "Tsch..."
    show layer master at shake1
    play sound "sound/explosion4.ogg"
    "The ship took another hit, sending Shields tumbling to the floor."
    
    play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
    
    hide icari with dissolve
    "Suddenly, the floor underneath him began to crack."
    kay "Oh shit!!"
    "The ship bent as it took a hit to its frontal underbelly, violently shoving its neck upwards. Shields rolled out of the way moments before a massive seam split the floor of Engineering in half. In horror, he saw a cross section of the ship below him as the entire room cleaved in two."
    
    if girl == "Asaga":
        $dshow(2110)
        asa "Captain! The ship's..."
    if girl == "Sola":
        $dshow(70423)
        sol "Captain!"
    if girl == "Icari":
        $dshow(41211)
        ica "Captain!!"

    kay "[girl]!!!"
    "He could barely stand up before the floor simply crumbled away around him. He backed up against the wall and looked for a way around the enormous crevasse now running through Engineering."
    
    play sound "sound/explosion2.ogg"
    
    "Suddenly, the piping running along the walls burst, spraying him with superheated vapor."
    kay "Arrghghh!!!"
    "Shields collapsed to the floor in agony, the skin of his arms peeled off by the steam."
    kay "T-tsch..."
    "He saw [girl] running towards him, intending to leap across the chasm to rescue him."
    kay "No! Don't---!!"

    if girl == "Asaga":
        asa "HOOYYAAHH!!!!"
    if girl == "Sola":
        sol "HEAH!!"
    if girl == "Icari":
        ica "EEAHH!!!"

    "Shields's heart plunged in terror as [girl] jumped across the chasm of jagged steel and wiring. If she couldn't make the distance, she would surely fall over thirty meters and be impaled against a nest of broken steel rods."
    "Using all of her effort, she somehow landed on the other side, and rolled back to her feet."
    "[girl] ran to him, concern for Shields' health the only thing in their eyes."

    if girl == "Asaga":
        $dshow(533)
        asa "How bad is it, capt'n!?"
    if girl == "Sola":
        $dshow(70022)
        sol "How badly are you hurt?"
    if girl == "Icari":
        $dshow(41212)
        ica "How bad is it, captain!?"

    kay "You idiot... You shouldn't have come for me..."
    "Shields grimaced as he held his burned arm, now nothing more than a mess of blood and charred muscle."
    
    if girl == "Asaga":
        asa "Hang on! We gotta get you to sickbay!"
    if girl == "Sola":
        sol "A-ah... We must get you to sickbay!"
    if girl == "Icari":
        ica "Shit, forget getting to the reactor! Only way to treat this is to get you to sickbay!"

    kay "No! We've got to restore power first!"
    kay "I'm not gonna die from a burnt arm! But we ARE all going to die if there's no power!"

    if girl == "Asaga":
        $dshow(650)
        asa "No wait--"
    if girl == "Sola":
        $dshow(70423)
        sol "No wait--"
    if girl == "Icari":
        $dshow(42000)
        ica "No wait--"

    scene white with dissolve
    play sound "sound/explosion4.ogg"
    "Before [girl] could finish, she was enveloped in a white flash."
    scene black with dissolve
    "Shields looked on helplessly as the wall in front of him vanished in a massive fireball. Behind the wall was nothing but a massive black void."
    
    scene spaced with dissolve
    
    "Space."
    kay "No.....!"
    "All the air rushed out of Engineering in an instant through the massive hole which the Nightmare Ascendant just blew into the ship."
    "Shields gasped when his mouth involuntarily opened and violently expelled all the air from his lungs."
    "Suddenly, everything was silent. He could no longer even scream, as he and [girl] were sucked out of Engineering and into the vast, empty sea of space."
    "Everything spun. In a surreal moment, he saw the battle scarred Sunrider from the outside..."
    "She was completely ruined, her proud hull punctured with craters, her frontal section now completely missing, nothing more than a mass of twisted black steel."
    "Shields screamed for [girl], but no words came from his mouth."
    "For a moment, [girl] stared at him... her eyes wide with terror."
    "A moment later, her flesh bloated like a grotesque corpse as all the dissolved oxygen in her blood stream reached boiling point and turned to gas."
    
    play sound "sound/gore.ogg"
    
    show white
    pause 0.2
    hide white
    
    "Her body exploded in a massive spray of frozen blood and guts in front of his face."
    "He couldn't even react, as a fraction of a second later, the same thing happened to him."

    #BAD END
    stop music fadeout 1
    scene black with dissolve
    
    play sound "sound/choirend.ogg"
    
    $persistent.unlocked_endings["BAD END 7: EXPLOSIVE DEPRESSURIZATION"] = True
    $check_for_all_endings()
    show screen bad_end7
    pause 3
    $dshow(32310)
    cla "Eeah, what a gory end you met there... Explosive depressurization sure is a gnarly way to go..."
    $dshow(34311)
    cla "If only you had restored power sooner... Then you wouldn't have ended up like this..."
    cla "Next time, avoid getting captured by ship security so you don't waste time locked up in the brig, or find a way to reach the back up comm faster."
    
    $renpy.full_restart()
    
label restoringpower:

    #IF NOT CAPTURED
    #TUNNEL "T-minus 47 hours before the Liberation Day Massacre, 11 hours until Chigara enters the mind stream"
    
    stop music fadeout 1.0
    
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 47 hours before the Liberation Day Massacre, 11 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    scene bg tunnel with dissolve
    play music "music/Colors_main.ogg"  fadeout 1.5
    "After what seemed like an eternity, the pair finally returned to the ship's core. They sighed in relief as the air once again became thick with oxygen and the frost on the tunnels gradually disappeared."
    kay "All right, now that we got the message sent, we still need to restore the ship's power."
    kay "The only way to do that is to head to engineering and figure out just what Chigara's done to the main reactor. Looks like there's no way around revealing ourselves to the crew for this."

    if girl == "Asaga":
        $dshow(2010)
        asa "All right. I'll keep a lookout and make sure the other Kayto Shields doesn't show up."
    if girl == "Sola":
        $dshow(70121)
        sol "Understood. I shall keep a lookout and warn you if the other Kayto Shields makes his appearance."
    if girl == "Icari":
        $dshow(34200)
        cla "Eh-heh... Mah, I guess to be on the safe side, I should stay hidden in the tunnel... I wouldn't want to risk the crew realizing that the doctor is at two places at once."
        $dshow(34210)
        cla "I'll keep watch and warn you if the other Kayto Shields shows up."
    if girl == "Ava":
        $dshow(13010)
        ava "All right. I'll stay by you and pretend you're the other Kayto Shields. Hopefully that'll be enough to keep security off of us."

    stop music fadeout 2
    kay "Okay. I'll go down there and see-"
    play sound "sound/explosion2.ogg" 
    show layer master at shake1
    play music "music/Danger.ogg"  fadeout 1.5
    "Before Shields could finish, the ship shook as a massive explosion bent the hull."
    kay "A-argh! Damn!"
    kay "What was that!?"

    if girl == "Asaga":
        $dshow(1120)
        asa "Eah! There's only one thing that coulda been! We're under attack!"
    if girl == "Sola":
        $dshow(70010)
        sol "Tsch. The Sunrider is under attack."
    if girl == "Icari":
        $dshow(32311)
        cla "Ooh! The ship's under attack!"
    if girl == "Ava":
        $dshow(13310)
        ava "Tsch. The explosion came from the exterior of the ship. That can only mean one thing..."

    kay "(Shit... This didn't happen in my time line...)"
    kay "(We've already altered the course of history by revealing ourselves to the Prototype leader before the final battle... Is she now going to use this opportunity kill us all here?)"
    kay "Come on! Let's find out what's going on!"
    "Shields opened the tunnel's gate and entered Engineering."

    #Engineering
    scene bg engineering_np with dissolve
    if girl == "Asaga":
        $dshow(32,xpos=0.25)
    elif girl == "Sola":
        $dshow(70122,xpos=0.25)

    "Crewmen scrambled as the ship shook. Pipes burst throughout the room, spewing clouds of vapor. Without any power, the ship was both toothless and blind!"
    kay "(Shit! I should have seen this coming... Of course the Prototypes would exploit an opportunity like this to sink the ship!)"

    if girl == "Ava":
        $dshow(13100)
        ava "Change of plans! I've got to get to the bridge! You stay here and find a way to restore power, while I find out the tactical situation!"
        kay "All right! Good luck!"
        "With that, Ava ran out of Engineering and headed to the bridge."
        hide ava with dissolve

    $dshow(41110,xpos=0.75 if girl == "Asaga" or girl == "Sola" else 0.5) #only now do I realize I should have made dshow auto-adjust sprites locations.
    "Shields ran to the reactor's controls and found Icari furiously pounding away on the console."
    kay "Icari! What's the situation!"
    
    if girl != "Icari":
        $dshow(41210)
        ica "What are you doin' here, cap!? Aren't you supposed to be on the bridge!?"
        kay "No use! Without power, there's nothing we can do!"
        $dshow(40520)
        ica "Tsch... I don't really know what's going on either... But the reactor's somehow been completely shut off. But now that you're here, I might be able to trick the system into doing a manual reboot."

    if girl == "Icari":
        $dshow(40122)
        ica "There you are! Did you manage to send the message!?"
        kay "Yeah! How're things on this end!?"
        $dshow(40222)
        ica "I've been trying to hack through the logic bomb Chigara set up for us for the last few hours... Luckily, I think I found a weakness!"

    play sound "sound/explosion2.ogg"
    show layer master at shake1
    "The ship took another hit, knocking the two of them off their feet."
    $dshow(41211)
    ica "Damnit!"
    "Shields screamed to a crewman."
    kay "What's the situation!?"
    cre1 "Sir! Crows' nest reports that the PACT fleet has advanced on our position! The Combined Fleet is trying to hold PACT back, but they are getting decimated by a new enemy ryder, unlike anything we've ever seen before!"
    kay "(New enemy ryder...? Shit... That can only mean...)"

    #Nightmare Ascendant CG
    show nightmare_approach
    show black:
        alpha 0.5
    with dissolve
    "Shields still vividly remembered the terrifying power of the Nightmare Ascendant. Only with the Combined Fleet, Fontana's ships, and the Sunrider at full capacity, acting together did they manage take it down in his timeline..."
    
    hide black
    hide nightmare_approach
    with dissolve
    
    "But now, he had no idea whether Fontana's ships were even operational, while his own vessel was completely shut down."
    "In other words, unless he found a way to restore power, they were all going to be dead in moments."
    $dshow(40522)
    ica "Cap, as I was saying, there's a way to turn the reactor back on. But uhh... Problem is, you're going to have to go inside the reactor first."
    kay "Ooh boy. I'm already not liking the sound of this."
    ica "I don't know how, but whoever shut the ship down managed to get his hands on Chigara's command ID. The only two people who have higher access clearances are you and the commander."
    ica "I've managed to rewire the engineering bay's security grid to permit an override... Only problem is that the hack requires you to swipe your command ID on the reactor's internal control relay."
    kay "Why the hell is that INSIDE the reactor!?"
    ica "Uhhh... The console's just used for maintenance tasks when the reactor's been shut off, but basically, that's the only console in Engineering the perpetrator of this attack didn't have access to. Thanks to that, I was able open up a back door to regain control over the reactor's systems through it."
    $dshow(40523)
    ica "D-don't worry! You'll have... 20 seconds after you swipe your command ID on the slot before the reactor turns back on! Just uhhh... climb back up once it's done!"
    kay "You've... gotta be kidding me."
    play sound "sound/explosion4.ogg"
    show layer master at shake1
    "However, when the Sunrider took another massive hit, causing a beam to drop down from the ceiling and smash a row of consoles, Shields realized he didn't have any time to complain."
    kay "Goddamnit!!"
    "He gritted his teeth and pulled himself over to the other side of the railing which blocked off the reactor shaft. In reality, the steel column in front of him was merely the tip of the reactor. Below him, a massive chasm actually housed the majority of the Sunrider's fusion reactor, which was shaped like an enormous sprouting onion. He jumped off the ledge onto a ladder leading down into the reactor's bulb-like bottom."
    play sound "sound/explosion3.ogg"
    show layer master at shake1
    "Just as he grabbed onto the ladder, the ship took another hit."
    kay "Oh shit! Oh shit!!"
    "He lost his footing and hung onto the ladder for dear life as his legs flailed below him."
    kay "Argghh!!!"
    "He managed to regain his balance amidst his curses."
    kay "Worst day ever!"
    "He climbed down and spun a steel wheel which opened the reactor's gate."
    "However, the next thing he saw when he entered the reactor made his jaws drop."
    scene bg reactor_np with dissolve
    "An enormous cavern of steel, surrounded by all sides by enormous spires."
    kay "Where the hell is the console!?"
    "He scanned the spherical dome for anything resembling a work station to no avail. Finally, he gave up and poked his head back outside."
    kay "ICARI!! WHERE THE HELL IS THE CONSOLE!?"
    "Icari looked down and hollered back." #should she be on screen? no idea
    ica "HUH!? IT SHOULD BE RIGHT THERE!!"
    kay "IT'S A STEEL JUNGLE IN HERE!! I DON'T KNOW WHAT'S WHAT!!"
    ica "AH FOR THE LOVE OF---!!"
    ica "AREN'T YOU THE SHIP'S CAPTAIN!?"
    kay "CAPTAIN! NOT ENGINEER!"
    play sound "sound/explosion4.ogg"
    show layer master at shake1
    "Icari nearly fell down the chasm herself when another enormous explosion shook the ship."
    "Shields heard screaming and the crashing of steel above him."
    kay "WHAT JUST HAPPENED?!"
    ica "NOTHING! HALF OF ENGINEERING JUST COLLAPSED, THAT'S ALL!!"
    ica "LOOK FOR TWO RED STRIPES! THE CONSOLE WILL BE BETWEEN THEM!"
    kay "Two red stripes! Got it!"
    "Shields re-entered the reactor core and desperately looked around for the red stripes."
    kay "Red stripes, red stripes..."
    kay "(There it is! I see it!)"
    "He ran across the core as the entire ship rattled."
    "Shields swiped the command ID located on the cuff of his wrist against console's reader."
    "The console's screen came to life and displayed various glyphs beyond Shields' comprehension."
    "However, he understood clearly what the countdown timer from 20 meant."
    kay "I think that means I have to haul ass outta here!!!"

    play sound "sound/chargeup.ogg"

    "The reactor began to hum back to life. Sparks began to fly from the top of the spires as Shields sprinted across the core."
    show expression "ReTurn/reactor_power.jpg" with dissolve: #experimentation!
        xalign 0.5 yalign 0.5 alpha 0.1
    kay "HOOAAAHH!!!!!!!!!"
    "Suddenly, the entire spherical interior began to revolve around the middle circlet where the exit was bored through."
    show expression "ReTurn/reactor_power.jpg" with dissolve:
        xalign 0.5 yalign 0.5 alpha 0.2
    kay "What... In..."
    "Shields's sprint suddenly became futile as the entire room began to revolve the opposite direction of where he was running."
    kay "GAAHH!!! Wrong way!!"
    show expression "ReTurn/reactor_power.jpg" with dissolve:
        xalign 0.5 yalign 0.5 alpha 0.3
    "Shields turned around and ran the other direction."
    "The gate fast approached him as the revolving floor now added to his speed."
    show expression "ReTurn/reactor_power.jpg" with dissolve:
        xalign 0.5 yalign 0.5 alpha 0.4
    "He had to jump at exactly the right time and grab onto the exit passage!"
    kay "U-urggh!!!"
    "He jumped and grabbed onto the ledge of the gate as the entirety of the reactor core revolved around him. The sparks of energy at the tip of the spires began to glow brighter and brighter."
    "With the last of his strength, he heaved himself through the gate and clambered onto the ladder, shutting the gate behind him and spinning the wheel as quickly as he could muster."
    scene bg reactor with dissolve
    "Just as the gate locked, the ship hummed back to life."
    kay "Power's... BACK!!!"
    "He heard the satisfying thumping of the Sunrider's AA guns as they woke from their slumber."
    
    scene bg engineering with dissolve
    
    "Grinning with triumph, Shields climbed up the ladder and grabbed onto Icari's hand."
    $dshow(41012,xpos = 0.25 if girl == "Asaga" or girl == "Sola" else 0.5)
    ica "Hahaah!!! You did it!!!"
    "Overcome with joy, Icari and Shields embraced."
    
    if girl == "Asaga":
        $dshow(14,xpos=0.75)
        asa "Ummm..."
        
    if girl == "Sola":
        $dshow(71000,xpos=0.75)
        sol "Hmm..."

    "Shields suddenly realized what he was doing and pulled himself off the mercenary."
    kay "Oh uhh... yeah."
    kay "Good job with the fix, Icari."
    $dshow(40210,blush=True)
    ica "Y-you too, captain!"
    $dshow(42000,blush=True) #best sprite
    ica "W-what!? I-it's not like I hugged you because I like you or anything! I was just... relieved, that's all! Hah! Hah!"

    if girl == "Asaga":
        $dshow(3210,ypos=1600)
        asa "All right, all right. Thank you for your participation in this little operation, Icari."
        asa "But don't you have a certain lieutenant to go back to?"
        $dshow(40020)
        ica "Oy, what's your prob? Too many awakenings getting to your head or something?"
        $dshow(3200,ypos=1600)
        asa "Hmph!"
        $dshow(40220)
        ica "Anyways, it looks like turning our reactor back on scared PACT back for now..."
        
    if girl == "Sola":
        $dshow(70310)
        sol "Ahem. In any matter, I am relieved the ship is now operational again."
        sol "Thankfully, the attack seems to have subsided for now... Perhaps the PACT Fleet has fallen back."

    play music "music/Posthumus_Regnum.ogg" fadeout 1.5
    
    if girl == "Ava":
        jump engineering_ava

    "Their celebration was abruptly cut short when a squad of marines suddenly burst into Engineering."
    show mook as mook1:
        xpos -0.25
    show mook as mook2:
        xpos 0.15
    show mook as mook3:
        xpos 0.55
    with dissolve
    ica "What the---"
    "To their dismay, a wall of rifles formed in front of the group."
    mrn "FREEZE!"
    
    if girl != "Icari":
    
        $dshow(41211)
        ica "Oy! What's the big idea!?"
        ica "Who ordered this!? The captain and I just saved the ship from getting blown up, and you grunts decide to point your guns at us!?"
        $dshow(41302)
        ica "Oh man, you guys are all gonna be fired for this..."
        hide mook1
        hide mook2
        hide mook3
        with dissolve
        show kayto with dissolve:
            xpos 0.5
        "Icari's grin was still plastered on her face when the wall of marines split in half to reveal a familiar face..."
        kayo "That's not the captain, Icari! That's the spy who turned off our reactor in the first place!"
        $dshow(41212)
        "Icari's grin vaporized as her jaws dropped and her eyes darted from one Kayto Shields to the other."
        ica "WHHHAAA!?"
        $dshow(41001)
        ica "Ha... hahh... hahaha... I must be dreaming."
        ica "Yep. This has all got to be a dream."
        
        if girl == "Asaga":
            $dshow(2100)
            asa "It's not a dream! But the person beside you is the real Kayto Shields, Icari! He's the one who just saved the ship, remember!?"
        if girl == "Sola":
            $dshow(70210)
            sol "Alas, this is real. But you must believe in the Kayto Shields standing beside you. He has just defended the ship from doom and will save us all from a grim future..."

        kayo "[girl]? I don't know what that imposter's been telling you, but there's no question I'm the real Kayto Shields here..."
        kayo "Don't worry... You're just confused right now. But you'll be safe soon."
        
        if girl == "Asaga":
            asa "No way! Ah, look, other capt'n, I don't even like ya any more! I think I'll stick with just this Kayto Shields, thank you very much!"
        if girl == "Sola":
            $dshow(70420)
            sol "No... It is you who is being deceived! You must believe us!"
            
    if girl == "Icari":
        $dshow(40010)
        ica "Shit... I was afraid of this..."
        "Shields looked around desperately for an escape route."
        "Incidentally, he realized that Claude had once again vanished into thin air. Not that her vanishing act even came as a surprise any more."

    #god damnit so many sprites!
    
    if girl != "Icari":
        $dshow(40420,xpos=0.1)
    if girl == "Icari":
        $dshow(40420,xpos=0.65)
    show kayto with dissolve:
            xpos 0.3
    $dshow(21221,xpos=0.5,behind="kayto")
    if girl == "Asaga":
        $dshow(33,xpos=0.7)
    if girl == "Sola":
        $dshow(71000,xpos=0.7)
    "Just then, Chigara appeared beside the other Shields." 
    kay "(Ah... great... So there's the reason why my other self thinks I'm the one who sabotaged the reactor...)"
    chi "That's the one, captain... He's a Prototype... there's no doubt about it..."
    chi "He kidnapped me and forced me to shut the ship's reactors down... It was all a plot to render us defenseless so PACT could launch their surprise attack..."
    kayo "You see? There's no reason for you guys to get caught up in this too. Just let security take in the imposter. In fact, you all need to sortie now to defend the ship."
    kay "(Arggghhh!!!! Come on, myself!!! Don't just lap up Chigara's words so easily without a second thought!!)"
    "While the other Shields' attention was diverted, Chigara... no, Chigara's body sneered at him."
    chi "Heh-heh..."
    kay "(Chigara's still under the Prototypes' control... Shit...!)"
    kay "(Everything's still going according to their plan...)"
    "The marines approached, rifles drawn."
    kay "(Do I make a break for it while I still can?)"
    kay "(Shit... But if we hide inside the ship, it's only a matter of time until the other Shields captures me again... And now that we've bungled our first kidnapping attempt, there's no way I'm going to be able to capture Chigara again before she sorties for the final battle...)"
    kay "(I could try escaping the ship with [girl] on her ryder, and hatch a new plan to incapacitate Chigara after the battle, but before the massacre...)"
    $dshow(14100,xpos=0.9) #Full House or Royal Flush?
    "Just then, another familiar face appeared."
    ava "Captain! The Nightmare Ascendant is coming back for another pass!"
    $dshow(10320)
    ava "And I've got even worse news..."
    kayo "What could be worse than this?"
    ava "Veniczar Fontana has just contacted us. He has discovered a Trojan embedded in his ships' systems. If he enters the battle now, the Prototypes will assume control of his fleet using their quantum brain waves at the decisive moment of our battle plan."
    ava "His best minds are working to remove the virus, but he cannot be sure that his ships will be ready in time. Meaning, we must assume that the allied PACT Fleet will be unable to assist us in the coming battle!"
    kayo "Tsch..."
    kay "(Well, it looks like my message got through, at least... But the message still came too late for Fontana to devise a countermeasure...)"
    kayo "What are our options?"
    $dshow(21211)
    chi "Captain, I believe I know a way to defeat the virus!"
    chi "I can use the Liberty's comm dishes to directly enter the Prototypes' mindstream while they're emitting the brain waves! I'll cause so much interference in their thoughts that they'll be unable to control the allied ships!"
    kayo "Can you really do that, Chigara?"
    $dshow(20111)
    chi "Yes! You have to trust me, captain!"
    $dshow(11310)
    ava "Captain, proceeding with this plan with full knowledge that the allied PACT ships have been sabotaged places the Combined Fleet in grave danger. If our Chief Engineer is unable to disturb the Prototypes' brain waves, then our total destruction is all but guaranteed."        
    $dshow(10000)
    kayo "No. Chigara can do it."
    kayo "We'll just have to trust her."
    kay "(Are you fucking---! Argh! Despite every damned thing I've done to change the past, my other self still decides to go down the exact same path as before!)"
    "Frustration bubbled in Shields' veins."
    kay "Shields... You're making a mistake! It's Chigara who's the Prototype! She's being controlled as we speak, right now!"
    kay "If she enters the mindstream, everything you've worked for will be destroyed!"
    "Shields glared down Shields."
    kayo "That's enough of your lies, Prototype."
    kayo "You guys have been trying to tear this ship apart from the moment Lynn set foot in our brig. But your lies have no power here."
    kayo "We're one family on board this ship. We're not going to begin to question each other."
    kayo "The ties that bind us... is something you Prototypes will never understand!"
    kay "Nice speech, captain... But you're the one completely blind to the truth!"
    "The marines trained their rifles on Shields as he stared at his other self with anguish."
    "Yes... Only he could understand what his other self was feeling at this moment..."
    "The sorrow... The emptiness..."
    "This man had lost his entire family and hedged all his bets on his new one. And that bet was about to burn everything else he had left to ash." #I don't think that's what 'hedging your bets' means...

    if girl == "Sola":
        jump engineering_sola
        
    if girl == "Asaga":
        jump engineering_asaga
        
    if girl == "Icari":
        jump engineering_icari
        
label engineering_ava:
    
    ##IF AVA ROUTE

    $dshow(13110,xpos=0.8)
    "Their celebration was abruptly cut short when Ava burst into Engineering."
    ava "You've got to get out of here!"
    kay "W-wha?"
    "Shields looked behind her into the hallway, where a squad of well-armed marines was marching towards Engineering."
    kay "Shit! Sorry, Icari, gotta go!"
    $dshow(41212)
    ica "What the--"
    "Shields tore himself off the tsundere merc and split towards the nearest maintenance tunnel with Ava."
    "The marines descended upon Icari and held her at gun point."
    mrn "FREEZE!"
    ica "Oy! What's the big idea!?"
    "The last thing Shields saw was Icari angrily confronting the marines as he dived back into the tunnel."
    kay "(Icari... I'm sorry...)"
    kay "(Don't do anything stupid and get yourself shot!)"
    scene bg hallway with dissolve
    $dshow(13010,xpos=0.25)
    "Shields kicked the gate on the opposite end of the tunnel open, and scrambled out into the hallway."
    "It would be seconds until security was on top of him again."
    kay "All right... The power's back, and the message to Fontana's been sent! The only thing left is to put Chigara out of commission, and we'll have averted the massacre!"
    $dshow(13310)
    ava "But how will we manage to detain Chigara with practically the entire ship against us?"
    $dshow(13010)
    kay "(Come to think of it... There is another option!)"

    #Flashback of Asaga going berserk
    show asagacockpit3
    show black:
        alpha 0.5
    with dissolve
    kay "(When Chigara enters the mind stream, Asaga goes berserk and nearly kills her in my timeline!)"
    hide asagacockpit3
    hide black
    with dissolve
    kay "(If we just change the course of events a little, we can get this universe's Asaga to kill Chigara before she has a chance to commit the massacre.)"
    kay "(But this is murder we're talking about here...)"
    "Shields' chest chilled at his own thoughts."
    kay "(The safety of the entire galaxy is at stake... But... to actually arrange the murder of my own Chief Engineer!?)"
    "Once again, his memories of Chigara came flooding back to him."

    play sound "sound/heartbeat.ogg"
    show chigarabeach2
    pause 0.5
    hide chigarabeach2
    show chigara_tea3
    pause 0.5
    hide chigara_tea3
    show chigaralap4
    pause 0.5
    hide chigaralap4
    show shieldschigarahug
    pause 0.5
    hide shieldschigarahug
    
    kay "G-ghck..."
    "His chest suddenly twitched at the thought of killing his former lover."
    "Granted, she had been a spy sent to win his affections from the very beginning... But Shields was still certain the massacre was not Chigara's doing. She had merely been mind controlled without her knowledge during that time. Certainly, she needed to be captured, but to be killed...?"
    "Not only that, but Asaga was merely a distraught girl in this timeline... Her attack on Chigara was a moment of desperation, brought on by mental fatigue after multiple awakenings..."
    "To use Asaga like a puppet to murder her former best friend in cold blood..."
    "He knew that if he went down this path, he would no longer be worthy of being this ship's captain. In his own eyes, at least."
    kay "(But... this is the safety of the entire galaxy we're talking about...)"
    "Just then, marines appeared around the corner of the hallway."
    
    play sound "sound/pulse1.ogg"
    
    "The two of them ran for it as they opened fire, sending shock rounds bouncing off the walls."
    kay "Shit! Doesn't look like we have a choice now!"
    kay "Claude! Are you there!?"
    "As if on cue, Claude materialized beside him."
    $dshow(36010)
    cla "Yes, captain!"
    kay "Good, I was hoping you were watching all this!"
    kay "I'm going to need your help!"
    $dshow(34210)
    cla "Ah well, as long as it doesn't involve my powers!"
    kay "I don't need teleportation or anything like that! Just... figure out a way to get to the Bianca! Pretend you're this universe's Claude and sortie!"
    $dshow(34310)
    cla "O-okay! I'll see what I can do!"
    kay "Tsch..."
    kay "Ava, this is where we make our stand."
    $dshow(10021)
    ava "Kayto?"
    kay "We're going to distract the marines so Claude can escape."
    $dshow(10000)
    ava "Very well. Give me your gun."
    kay "Ava? D-don’t do anything stu-"
    
    play sound "sound/guncock.ogg"
    
    "Before he could speak another word, Ava snatched Shields' pistol and held it up against his head."
    kay "A-ah..."
    kay "(Figures... And here I thought she was planning to make some heroic last stand...)"
    $dshow(13110)
    ava "I've captured the imposter!"
    hide claude with dissolve
    "Behind them, Claude sprinted off as quickly as her feet would carry her to the hangar."
    kay "(Claude... Good luck...!)"
    show mook as mook1 with dissolve:
        xpos 0.15
    "The marines approached, rifles drawn."
    show kayto:
        xpos 0.7
    with dissolve
    "A familiar face broke through the wall of rifles."
    kayo "End of the line, Prototype."
    kayo "Commander, you damn well have a good explanation as to what you were doing with him... And how he escaped the brig."
    $dshow(14110)
    ava "Captain!"
    "Despite her cool exterior, Shields knew that Ava was currently racking her brain for a logical explanation for her actions."
    "Before she could think of one, more bad news appeared."
    hide mook1 with dissolve
    $dshow(23010,xpos=0.9,behind='kayto')
    chi "Umm... It appears someone used the commander's security credentials to unlock the imposter's cell..."
    chi "O-of course, I am not accusing the commander of setting the prisoner free... but..."
    kayo "... ... ..."
    ava "Captain. The Chief speaks the truth."
    kay "(Shit... So she couldn't think of anything...)"
    $dshow(13300)
    ava "It was I who set the other Kayto Shields free. In fact, I believe his words are the truth, and it is the Chief Engineer who is the true spy."
    ava "You must revoke her security clearance and detain her. Or else she may very well disable this entire ship right now."
    $dshow(13000)
    kayo "I don't know what you're trying to pull here, Prototype... But to think you've actually managed to turn my own executive officer again me..."
    kayo "Commander... You are effectively relieved of your rank and your duties. You are to be confined for the duration of this operation."
    kayo "Take both of them in boys."
    kay "Shit...!!"
    kay "(I've... got to do something drastic!)"
    play sound "sound/explosion2.ogg"
    show layer master at shake1
    "Before anyone could move, the ship took a massive hit, nearly knocking everyone off their feet."
    kay "You felt that!? That's the Nightmare Ascendant! It's come back for another round!"
    kay "You're... right! I am a Prototype!"
    kay "But in exchange for my safety, I'm willing to talk! I can tell you about the Ascendant's systems! Its abilities! You'll need me to survive this battle!"
    kayo "Hmph... Is that so?"
    play sound "sound/explosion2.ogg"
    show layer master at shake1
    "The other Shields pondered his options. Another direct hit helped him come to a quick decision."
    kayo "All right. Take the Prototype to the bridge!"
    kayo "Everyone, man your stations!"
    
    jump endgame_asagakillschigara
    
label engineering_icari:
    
    kay "(Shit... We've managed to restore power and send Fontana the warning, but as long as Chigara remains at large, the massacre's still going to happen anyways...)"
    kay "(Did Icari already figure out a way to stop Chigara?)"
    kay "(Looks like I'll just have to trust her for now...)"
    $dshow(40322)
    ica "Oy, so you're tellin' me that this Kayto Shields was just an imposter? But he just helped me restore power to the ship! In fact, if it weren't for him, we'd all be dead by now! None of this adds up, captain!"
    kayo "He did what?"
    kay "You heard her. I just saved this entire ship. But you're not out of the woods yet. I can still help you."
    $dshow(40521)
    ica "I think he's telling the truth. We should trust him for now."
    $dshow(11310)
    ava "Captain, perhaps the imposter seeks to become an enemy turncoat by working for us. If we turn him into a double agent, we could gain a tactical advantage in the battle..."
    $dshow(13000)
    kayo "Yeah, but if a spy turns traitor once... there's nothing to say he won't turn traitor again."
    play sound "sound/explosion4.ogg"
    show layer master at shake1
    "Just then, the ship shook as it took a hit."
    kay "Did you hear that!? It's the Nightmare Ascendant! You're not going to last long against it!"
    kay "I know its systems! And its capabilities! You need my help!"
    kayo "...Tsch."
    $dshow(13310)
    ava "Captain, we're out of time. We must return to the bridge!"
    $dshow(13010)
    kayo "All right. Looks like we don't have a choice."
    kayo "Very well, Prototype. Let's see if you have anything insightful to offer. But if you try to pull anything, my marines will gun you down on the spot."
    kay "All right..."
    kayo "Take him in boys."
    "With that, the marines rushed forward and handcuffed Shields."
    "Icari leaned in and whispered to him."
    $dshow(41310)
    ica "Good luck... I'm taking off on the Phoenix and finishing this..."
    kay "Okay... Good luck..."
    
    jump endgame_asagakillschigara

label engineering_sola:

    #IF SOLA

    kay "(I need to figure out a way to end this...)"
    kay "(I managed to warn Fontana and restore power to the ship... meaning incapacitating Chigara's the only thing left...)"
    kay "(Come to think of it... There is another option!)"

    #Flashback of Asaga going berserk
    show asagacockpit3
    show black:
        alpha 0.5
    with dissolve
    kay "(When Chigara enters the mind stream, Asaga goes berserk and nearly kills her in my timeline!)"
    hide asagacockpit3
    hide black with dissolve
    with dissolve
    kay "(If we just change the course of events a little, we can get this universe's Asaga to kill Chigara before she has a chance to commit the massacre.)"
    kay "(But this is murder we're talking about here...)"
    "Shields' chest chilled at his own thoughts."
    kay "(The safety of the entire galaxy is at stake... But... to actually arrange the murder of my own Chief Engineer!?)"
    "Once again, his memories of Chigara came flooding back to him."

    play sound "sound/heartbeat.ogg"

    #Chigara CGs
    show chigarabeach2
    pause 0.5
    show chigara_tea3
    pause 0.5
    show chigaralap4
    pause 0.5
    show shieldschigarahug
    pause 1.0
    hide shieldschigarahug
    hide chigarabeach2
    hide chigara_tea3
    hide chigaralap4
    
    kay "G-ghck..."
    "His chest suddenly twitched at the thought of killing his former lover."
    "Granted, she had been a spy sent to win his affections from the very beginning... But Shields was still certain the massacre was not Chigara's doing. She had merely been mind controlled without her knowledge during that time. Certainly, she needed to be captured, but to be killed...?"
    "Not only that, but Asaga was merely a distraught girl in this timeline... Her attack on Chigara was a moment of desperation, brought on by mental fatigue after multiple awakenings..."
    "To use Asaga like a puppet to murder her former best friend in cold blood..."
    "He knew that if he went down this path, he would no longer be worthy of being this ship's captain. In his own eyes, at least."
    kay "(But... this is the safety of the entire galaxy we're talking about...)"
    kay "(And an entirely different problem is that in my timeline Claude managed to stop Asaga in time...)"
    kay "(The old Claude will probably do the same thing... Unless we somehow put the Bianca out of commission...)"
    
    if girl == "Sola": #how could it not be?
        kay "(The other option is making a run for it right now and escaping the ship with Sola. We could then regroup and come up with a new plan to dispatch Chigara before the massacre. Then we wouldn't need to dirty Asaga's hands. But escaping and coming up with a new plan isn't going to be a walk in the park either...)"
        kay "(What do I do...?)"
    $ menu_choices = [
                    ["Get Asaga to kill Chigara","engineering_asagakillschigara","Hacer que Asaga mate a Chigara."],
                    ["Escape the ship with Sola","engineering_escapewithsola","Escapar de la nave con Sola."],
                    ]
    show screen decision
    pause    
        
label engineering_asagakillschigara:
    #Get Asaga to kill Chigara

    kay "(With a squadron of marines in front of me, escape isn't a feasible option. Looks like I don't have a choice!)"
    "Shields swallowed and accepted the unavoidable. Chigara had to be stopped at all costs, or else humanity will be thrust into a pointless bloody war."
    "He turned to Sola and whispered new instructions to her."
    kay "I'm going to turn myself in. Pretend I took you hostage and tricked you into doing everything."
    kay "Sortie on the Seraphim. Asaga will attempt to kill Chigara during the battle. Make sure she succeeds."
    $dshow(70122)
    "She nodded."
    sol "Understood."
    "With that, Shields put his hands on top of his head."
    kay "All right, I surrender! But I'm willing to talk!"
    kay "I know everything the Prototypes are planning to do for the remainder of the battle! You need me if you're going to survive!"
    kayo "... ... ..."
    $dshow(11310)
    ava "Captain, while this Prototype could certainly be trying to deceive us... he has just saved the ship by restoring power to the reactor. Perhaps he seeks to become a double agent and betray the Prototypes in the end."
    ava "We could at least hear out what he has to say."
    $dshow(13000)
    kayo "...All right. If he has something useful to say, we could use all the help we can get."
    kayo "We're taking you captive, Prototype! Surrender peacefully and we won't harm you. We will escort you to the bridge in handcuffs where you'll help us defeat the Prototypes. If you try to pull anything, my marines will not hesitate to kill you on the spot."
    kay "All right!"
    "With that, the marines ran to Shields, rifles at the ready, and bound his wrists."
    $dshow(41210)
    ica "O-oy... I have no idea what just happened!"
    $dshow(70112)
    sol "I-it appears we have been deceived... This captain was merely a Prototype imposter..."
    $dshow(40000)
    ica "Ah, this is messed up in almost every possible way!"
    kayo "We just have to accept it for now. Come on, get to the hangar, you two! Defend this ship from PACT!"
    $dshow(40022)
    ica "All right, I'm on my way!"
    sol "Acknowledged."
    
    jump endgame_asagakillschigara

label engineering_escapewithsola:
    
    play music "Music/The_Bladed_Druid.ogg" fadeout 1.5

    kay "(No... I can't dirty Asaga's hands like that...)"
    kay "(Changing the future is my responsibility and mine alone. I can't offload that burden onto someone else out of convenience.)"
    "Shields whispered to Sola."
    kay "We're going to make a run for it. We need to escape the ship on the Seraphim. Think you can do that for me?"
    $dshow(70210)
    sol "Yes."
    "Even in this life or death situation, Sola's eyes betrayed not a flicker of hesitance. She had already decided she would follow Shields into whatever hellfire may come his way a long time ago."
    kay "All right... Stay safe... Sola!"
    sol "Fear not."
    sol "Today, it shall be I who protects you."
    
    play sound "sound/heartbeat.ogg"
    
    $dshow("sola armhold clench zawakennarrow mad")
    
    "Sola took a deep breath as her eye began to glow." #On days like these, mooks like you should be
    kay "W-wha--?"
    
    play sound "sound/pulse2.ogg"
    pause 0.3
    play sound1 "sound/pulse2.ogg"
    pause 0.3
    play sound2 "sound/pulse2.ogg"
    pause 0.3
    play sound3 "sound/pulse2.ogg"
    pause 0.3
    play sound4 "sound/pulse2.ogg"
    pause 0.3
    
    "She suddenly shoved Shields down to the floor. Before the marines could react, she had already drawn her holstered pistol. Within the span of a blink, she unloaded the entire clip into each of the marines' shins."
    
    play sound "sound/laser1.ogg"
    
    "She rolled behind a console as the surviving marines took their aims off Shields and sprayed her with stun rounds."
    "Sparks flew as the rounds impacted against the console."
    $dshow(13101)
    ava "Shit! Captain, this way!"
    
    play sound "sound/warning.ogg"
    
    "Ava grabbed hold of the other Kayto Shields before he could protest and shoved him out of Engineering. Overhead, the klaxon rang."
    hide ava
    hide kayto
    hide chigara
    hide icari
    with dissolve
    "Shields crawled to the console beside Sola and drew his own pistol."
    kay "Sola! We're gonna be overwhelmed with reinforcements soon!"
    $dshow(70010)
    sol "Unfortunately, that was all the ammo I had."
    kay "Damn!"
    "Shields peered over the console and saw a hoard of marines in the hallway outside of Engineering coming in to reinforce the injured squad. Way too many for them to handle."
    
    jump escapefromengineering
    
label escapefromengineering:
    
    $dshow(41210,xpos=0.35)
    ica "Ahhh shit, this is nuts!"
    
    play sound "sound/warning.ogg"
    
    "Icari pounded the console. Fire retardant sprays activated throughout the room, and the Engineering gate sealed shut, locking the reinforcements out."
    kay "Icari... You're..."
    $dshow(41111)
    ica "I dunno what the hell's going on... But I just saw you save the ship!"
    ica "And from what I just saw of the logic bomb that shut down the reactor... I'm thinking what you're saying about the Chief's actually right!"
    ica "So looks like you can count me in on this, cap!"
    kay "All right! Help us escape the ship!"
    $dshow(41412)
    ica "Copy!"
    
    hide icari
    hide sola
    hide asaga
    with dissolve
    
    "The trio entered the thick cloud of fire retardant now spreading through the floor of Engineering."
    kay "The nearest maintenance tunnel leading to the hangar's on the second floor. C'mon, we gotta get up to the catwalks!"
    
    play sound "sound/laser1.ogg"
    
    "Their luck ran out when stun rounds whizzed past them and ricocheted off the wall."
    "Shields grimaced as a round grazed his face, burning a gash across his cheek."
    "The stun rounds were the security team's primary non-lethal weapon. With a maximum range of 40 meters, the rounds could be fired from a standard issue rifle at low velocities to embed itself inside the target's tissue and deliver an incapacitating electric shock, while still not usually penetrating internal organs."
    kay "(Key word: Usually...)"
    
    play sound "sound/pulse1.ogg"
    
    "Shields saw two marines clad in full body armor approaching their position, their rifles firing."
    
    play sound "sound/punch.ogg"
    show layer master at tr_xshake
    
    "Suddenly, Icari emerged from the clouds beside them and delivered a flying kick to the right marine's helmet."
    
    play sound "sound/pulse1.ogg"
    
    "The other marine spun around to face her and pump her full of stun rounds, but in a single well practiced maneuver, Icari unbuckled the first marine's vest and held him in front of her. The unfortunate marine gasped as he was pelted with stun rounds and crumpled to the ground twitching as ten thousand volts of electricity coursed through his body."
    
    play sound "sound/punch.ogg"
    show layer master at tr_xshake
    
    "Icari performed a forward flip, kicking the other marine's rifle to the floor while he was still recoiling from shooting his compatriot. She then dropped to the ground and blew his shin out using the fallen marine's rifle."
    "He howled and fell to his knees. He was swiftly knocked out when Icari pounded the back of his head with the butt of her new rifle."
    kay "Holy-- Icari wasn't kidding about being a contract assassin..."
    $dshow(41410)
    ica "Cap, catch!"
    
    play sound "sound/guncock.ogg"
    
    "Icari tossed the second rifle to Shields. He grabbed it and checked its ammo."
    "20 stun rounds and 3 bullets."
    ica "Be careful, the stun rounds won't penetrate their armor!"
    "Despite that, he only loaded the stun rounds. He was still the captain of the ship. He wasn't about to start gunning down his own security team."
    $dshow(41010)
    ica "I'll cover you while you climb the ladder! Don't worry 'bout me!"
    ica "They're coming in to capture us, not kill!"
    kay "All right. Good luck, Icari."
    ica "No prob! I'll... see you later!"
    hide icari with dissolve
    "With that, Shields and [girl] left Icari on the floor of Engineering and clambered up the ladder."
        
    play sound "sound/pulse1.ogg"
    
    "They ran across the catwalk as stun rounds pelted their position, bouncing off the walls and the railings."
    kay "Damnit!!"
    "Shields shot shock rounds back as he ran, at least trying to force the marines back into cover."
    play sound "sound/explosion4.ogg"
    show layer master at shake1
    "Just then, the entire ship lurched as a massive explosion reverberated throughout the hull, sending Shields and [girl] tumbling to their faces."
    kay "(Shit... That can only mean that the Nightmare Ascendant's back for another round...)"
    kay "(But maybe... we could use this chance as an opening!)"
    "Shields picked himself and [girl] back up and sprinted across the catwalk. The sudden explosion proved an unexpected blessing, as the shock rounds momentarily ceased."
    "Below him, Shields heard the firing of a rifle and groans, as Icari dispatched more marines under the cover of the fire retardant."
    kay "Come on, [girl]! Here's our chance!"
    "The two of them reached the maintenance tunnel and leaped through the gate."
    "They scrambled down to the hangar as the entire ship rumbled and rattled."

    if girl == "Sola":
        jump escapehangersola
    if girl == "Asaga":
        jump escapehangerasaga

label escapehangersola:

    #Hallway
    scene bg hallway with dissolve
    "Shields and Sola emerged from the maintenance tunnel, one deck below. They scrambled to the hangar as fast as their feet would carry them."

    #Hangar
    scene bg hangar with dissolve
    $dshow(70110)
    "They arrived at the Sunrider's enormous hangar."
    kay "Come on, let's hitch a ride on this thing!"
    "Shields climbed onboard a small buggy. Sola hopped on behind him and put her arms around his chest."
    
    play music "Music/Danger.ogg" fadeout 1.5
    
    "Just then, marines burst into the hangar."
    kay "Shhhitt!!! Hang on!"
    
    play sound "sound/carengine.ogg"
    
    "He put the pedal to the metal just as they opened fire. The buggy's wheel screeched as the two took off, shock rounds streaming past them."
    mrn "Stop them!"
    "The entire floor of the hangar was approximately 200 meters across, and the crew frequently used motor vehicles to quickly traverse across the distance. However, never before in the Sunrider's history did the ship's captain race across the floor of the hangar in a buggy with a girl wrapped around him while being chased by half the ship's security team."
    
    play sound "sound/tire_skid.ogg"
    
    "Shields turned hard when a forklift carrying a crate of ryder munitions pulled out in front of him, nearly causing both of them to fall off."
    "Behind them, a half dozen marines managed to commandeer buggies of their own and took off after them."
    kay "Hang on!!"
    $dshow(70003)
    sol "A-ah...!"
    
    $dshow("sola armhold clench zawakennarrow mad")
    "Sola's eye once again illuminated as she grabbed Shields' combat rifle." #You're gonna have a Bad Time.
    
    play sound "sound/pulse1.ogg"
    play sound1 "sound/car_crash.ogg"
    
    "She took aim and opened fire. The shock round struck a marine directly on his exposed arm, embedding itself and delivering its electric payload. He fell off his buggy in convulsions, sending it flying into a supply crate."
    "In another beat, Sola fired once more, striking another marine down."
    "She gave no pause, bringing providence to all who chased them."
    "Shields pulled over beside the Seraphim."
    kay "Come on, we're here! Let's go!"
    sol "Understood."
    
    play sound "sound/pulse1.ogg"
    
    "With a final shot which knocked the nearest marine off his buggy and sent him spinning across the floor, Sola hopped off her seat and ran towards the Seraphim."
    hide sola with dissolve
    play sound "sound/pulse1.ogg"
    
    "Shock rounds pelted the loading mechanism as the two scrambled into the ryder's cockpit."
    kay "I sure hope this thing can accommodate two! Get us outta here, Sola!"
    
    scene cg_sola_cockpit_hanger with dissolve
    
    "Sola shut the cockpit and activated the Seraphim." #cockpit background would be pretty sweet right now
    "Icari's voice came through the launch tower."
    ica "Heh. I've managed to clear out the control crew manning this place. Seraphim, you're cleared for launch."
    kay "Okay..."
    kay "We owe you one, Icari..."
    ica "Seriously..."
    ica "Once this is all over, I think you're gonna owe me some drinks... As well as a damned good explanation. Until then... I'll be waiting!"
    kay "Godspeed."
    play sound "sound/warning.ogg"
    "The hangar alarm rang and the crew scrambled out as the main airlock opened."
    "The Seraphim locked onto the linear rail."
    sol "Ah."
    sol "It appears we are not wearing plugsuits."
    sol "Please hang on. The g-force of the launch will be... quite powerful."
    kay "Ooh gre--"        
    
    play sound "sound/chargeup.ogg"
    
    "Shields braced himself against the cockpit's spherical wall as the linear rail flung the Seraphim out the hangar. Everything became a blur as all the blood in his body flowed to the back of his body."
    
    scene cg_sola_cockpit_neutral with dissolve
    
    "The Seraphim emerged out of the front of the ship, into a field of fire. Flak rounds exploded all around them, while lasers beams split the black void of space like thunder."
    "Alliance and PACT ships were tangled at dagger range, pounding each other with kinetic rounds. Ships exploded around them, as swarms of ryders spiraled around ships, bombers trying to take down larger ships with missiles, while interceptors cut down the bombers with assault rounds."
    sol "I will use the chaos of the battle to withdraw."
    sol "Please hang on in case of unexpected turbulence."
    
    play sound "sound/mech_boost2.ogg"
    
    "Sola spun the Seraphim around sharply, sending Shields tumbling to the opposite end of the cockpit sphere."
    
    show layer master at tr_xshake
    
    kay "Argghh!!"
    "She narrowly avoided getting clipped by a stray laser. On the opposite side, a homing missile headed straight towards them."
    "With another emergency maneuver, Sola spun the Seraphim and dived. The missile adjusted its course after them, directly into a wall of flak."
    "The cockpit shook as pieces of the missile struck the ryder, causing no damage except to Shields' already battered body."
    "He felt nausea building up within him, as the sphere shook and revolved around the Seraphim's evasive maneuvers."
    
    scene cg_sola_cockpit_talk with dissolve
    
    sol "I am... sorry..."
    kay "D-don't worry about me... Just focus on getting us out of here!"
    sol "Understood."
    
    scene cg_sola_cockpit_neutral with dissolve
    
    "Shields saw a PACT Prototype Unit making a beeline for their position."
    
    play sound "sound/Sola Sniper.ogg"
    
    "The Seraphim opened fire, clipping its right rear thruster with a well placed snipe. The Prototype Unit spun in circles as it lost control."
    kay "Two more, coming from above!"
    sol "Tsch...!"
    
    play sound "sound/Sola Sniper.ogg"
    
    "The Seraphim revolved above and loosed another round, catching one of the Prototype Units directly in the gut. Its reactor exploded in a blue fireball, sending its limbs flying."
    
    play sound "sound/pulse1.ogg"
    
    "The second Prototype Unit opened fire, spraying the Seraphim with pulse bolts."
    
    play sound "sound/mech_boost2.ogg"
    
    "Sola slammed the thruster, sending Shields flying to the roof of the cockpit. The bolts sailed safely past behind them."
    kay "Argh!"
    
    scene cg_sola_cockpit_talk with dissolve
    
    sol "I am--"
    kay "Don't worry!"
    sol "U-understood..."
    
    scene cg_sola_cockpit_neutral with dissolve
    
    play sound "sound/missile.ogg"
    
    "The Prototype Unit loosed a rack of missiles. They streamed towards the Seraphim like a hoard of raptors."
    "Sola twisted the control stick, sending the Seraphim into a spiraling dive, straight into the flak wall of an Alliance Battleship."
    
    play sound "sound/heartbeat.ogg"
    
    scene cg_sola_cockpit_awakenedfocus with dissolve
    show cg_sola_cockpit_awakenedfocus1:
        xalign 0.5 yalign 0.5 alpha 1
        ease 0.5 zoom 1.5 alpha 0
    "She gritted her teeth as her eye ignited blue." #Maybe try the mercy button?
    sol "Hang on!"
    
    play sound "sound/flakguns_deep.ogg"
    
    "She weaved the Seraphim through the battleship's flak rounds, explosions popping all around the ryder, but never hitting it." #wait, Awakening doesn't buff evade!
    
    play sound "sound/explosion2.ogg"
    
    "The missiles were nowhere as skilled at dodging the flak, and imploded behind the Seraphim."
    "Sola spun her ryder once more and took aim."
    
    play sound "sound/Sola Sniper.ogg"
    
    "The third Prototype Unit disappeared in a brilliant flash of blue as Sola once again bulls eyed its reactor."
    sol "Haa..."
    "Shields peeled himself from the cockpit's wall, bruised but still conscious."
    kay "Did we get the last of them?"
    
    play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
    scene nightmare_approach with dissolve
    
    "His heart sank when a new, massive ryder appeared before them. One which struck terror into Shields' heart."
    kay "Shit--!"
    
    scene alice_cockpit1 with dissolve
    
    ali "Haha... So this is where you were hiding..."
    ali "But this is where you mission ends!"
    "The Nightmare Ascendant raised its particle gun and took aim."
    
    play sound "sound/explosion2.ogg"
    
    "But before it could fire, it was enveloped in explosions."
    
    scene icaricockpit with dissolve
    
    ica "Phoenix and Paladin, coming in to assist!" #sprites of them in uniform would be weird here
    
    scene kryska_cockpit1 with dissolve
    
    kry "Hiyaah!! I'm your enemy, Prototype!"
    "The Phoenix raced ahead and came at the Nightmare Ascendant, katana drawn."
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Nightmare Ascendant met the Phoenix's blade with its own. In a grand display of its overwhelming strength, the Ascendant shoved the Phoenix away like a titan pushing back the valiant hero who had dared stand against it."
    
    scene icaricockpit with dissolve
    
    ica "Tsch... We'll distract it!"
    ica "Sola... You know what you have to do!"
    
    scene cg_sola_cockpit_awakenedsad with dissolve
    
    sol "Yes."
    "Shields' heart pounded as the Seraphim hit its thrusters, leaving the Nightmare Ascendant to Icari and Kryska."
    kay "(You two... Don't die...!)"
    kay "Tsch..."
    "Shields balled his hand into fists. He desired with all his heart to remain with the others for the battle, but his own mission was too great to abandon."
    kay "(I can only trust in the other girls...)"
    kay "(Come on my other self... You had better pull through!)"
    "With that, the Seraphim left the battle behind and vanished into the abyss of space..."
    
    jump endgame_awardhall
    
label engineering_asaga:

    #IF ASAGA

    kay "(I need to figure out a way to end this...)"
    kay "(I managed to warn Fontana and restore power to the ship... meaning incapacitating Chigara's the only thing left...)"
    kay "(Come to think of it... There is another possiblity...)"

    #Flashback of Asaga going berserk
    show asagacockpit3
    show black:
        alpha 0.5
    with dissolve
    kay "(In my timeline, when Chigara entered the mindstream, Asaga went berserk and nearly killed her.)"
    hide asagacockpit3
    hide black
    with dissolve
    kay "(Given how much I've changed this timeline, it's obvious that Asaga's not going to attack Chigara in a fit of jealousy again... But we could still stage a repeat of that incident by having Asaga attack the Liberty.)"
    kay "(Ah but that's ignoring the fact that Asaga's attempt fails in my timeline...)"
    kay "(This universe's Claude has been tasked by the Prototypes with protecting Chigara... Meaning the old Claude will stop Asaga again if Chigara's mission is ever threatened...)"
    kay "(And seeing how we're all standing at gun point right now, I don't think I'll be able to do anything to put old Claude or the Bianca out of commission...)"
    kay "(If only the other Claude was here...!)"
    kay "(Getting Asaga to attack the Liberty is too much of a longshot at this rate...)"
    kay "(I've already altered the timeline too much. This Asaga's not going to be able to repeat history.)"
    kay "(We need to escape from the ship and rethink our approach. From this point on, I can't assume that things will proceed the same way as in the past...)"
    "Shields whispered to Asaga."
    kay "We're going to make a run for it. We need to escape the ship on the Black Jack. Think you can do that for me?"
    $dshow(630)
    asa "A-all right, capt'n! Leave it to me!"
    "But despite that, escape was not going to be easy. Not with a row of rifles trained on Shields."
    $dshow(2100)
    asa "Today, I'm finally gonna become the hero!"
    
    play sound "sound/heartbeat.ogg"
    $dshow("asaga excited yell zawakened angry")
    
    asa "Hooyyaaahh!!!"
    #need new sprite
    
    show layer master at tr_xshake
    play sound "sound/punch.ogg"
    
    "Asaga's eyes glowed bright blue as she awakened. She bull rushed towards the marines, throwing them off guard."
    kay "Oh shit!"
    
    play sound "sound/pulse2.ogg"
    pause 0.3
    play sound1 "sound/pulse2.ogg"
    pause 0.3
    play sound2 "sound/pulse2.ogg"
    
    "The marines took their rifles off Shields and aimed at Asaga. He took the moment to draw his pistol and unload his clip on the marines' shins."
    
    show layer master at tr_xshake
    play sound "sound/punch.ogg"
    
    "Running with super human speed, Asaga slid into the nearest marine's legs with her foot, knocking him to the ground. She rolled out of the way just as shock rounds shattered against the floor where she was sitting just a second ago."
    
    play sound "sound/pulse1.ogg"
    
    "More marines trained their rifles on her and loosed shock rounds, but Asaga dodged them with ease, her super charged brain processing information ten times quicker than usual."
    "To her burning blue eyes, all of the marines' movements appeared sluggish and the shock rounds swam towards her in slow motion."
    asa "Hiiyaah!!!"
    
    show layer master at tr_xshake
    play sound "sound/punch.ogg"
    
    "Asaga crashed into a marine, knocking him down. Super power notwithstanding, she was still an untrained girl. CQC was not her strong suit."
    $dshow(13101)
    ava "Shit! Captain, this way!"
    
    play sound "sound/warning.ogg"
    
    "Ava grabbed hold of the other Kayto Shields before he could protest and shoved him out of Engineering. Overhead, the klaxon rang."
    hide ava
    hide kayto #so what does icari do?
    hide chigara
    hide icari
    with dissolve
    
    play sound "sound/pulse1.ogg"
    
    "Shields dived behind a console as shock rounds pounded his position. He peered over the console and saw a hoard of marines in the hallway outside of Engineering coming in to reinforce the injured squad."
    "Way too many for them to handle."
    
    jump escapefromengineering

label escapehangerasaga:

    #Hallway
    scene bg hallway with dissolve
    "Shields and Asaga emerged from the maintenance tunnel, one deck below. They scrambled to the hangar as fast as their feet would carry them."

    #Hangar
    scene bg hangar with dissolve
    $dshow(532)
    "They arrived at the Sunrider's enormous hangar."
    asa "Eah, the Black Jack's too far away! Come on, let's grab that!"
    "Asaga pointed to a row of small buggies near the entrance. The entire floor of the hangar was approximately 200 meters across, necessitating the use of motor vehicles to quickly traverse the distance."
    
    play sound "sound/pulse1.ogg"
    
    "Just then, a hoard of marines appeared running down the hallway. They trained their rifles and sent shock rounds ricocheting past Shields."
    
    play music "Music/Danger.ogg" fadeout 1.5
    
    kay "Gogogogogo!!!"
    "The two of them scrambled to the buggy."
    $dshow(630)
    asa "I drive! You shoot!"
    
    play sound "sound/carengine.ogg"
    
    "Asaga put the pedal to the metal as Shields wrapped his arm around Asaga's chest while holding his rifle in the other."
    "Behind them, a half dozen marines managed to commandeer buggies of their own and took off after them."
    "Once the buggy finished accelerating, Shields spun around and trained his rifle on the nearest marine burning rubber behind them."
    
    play sound "sound/laser1.ogg"
    
    "He unloaded shock rounds at him, to no effect."
    kay "Shit!"
    "He gritted his teeth and loaded the bullets into the rifle. As long as he aimed for their buggies, the marines would probably survive."
    
    play sound1 "sound/sniperrifle.ogg"
    play sound "sound/car_crash.ogg"
    
    "He took aim and shot the other buggy's tire out. It went into a screeching spin, throwing the marine off and sending him spinning across the hangar floor."
    kay "One down!"
    "Suddenly, a forklift carrying a crate of ryder munitions pulled out in front of him."
    $dshow(602)
    asa "Ooah!! HANG ON!!!"
    
    play sound "sound/tire_skid.ogg"
    
    "Shields wrapped his arms around Asaga and hung on for dear life as Asaga swerved around the forklift."
    "They passed, the steel frame of the forklift no further than a few centimeters from their faces."
    kay "G-geez...!"
    $dshow(423,blush=True)
    asa "Eh-heh... capt'n?"
    "Shields realized that his hands were clenched on Asaga's boobs. He immediately let go and spun around."
    $dshow(211,blush=True)
    asa "Copping a feel in a moment like this... ya perv. Heheh."
    kay "It was just--"
    
    play sound "sound/pulse1.ogg"
    
    "He was cut off when shock rounds flew by close enough to graze his hair."
    kay "AA-ARGHH!!!!!"
    "He raised his rifle. Just two bullets left!"
    
    play sound "sound/sniperrifle.ogg"
    
    "He opened fire. Sparks flew from the front grate of the nearest enemy buggy, but otherwise had no effect."
    kay "Damn!"
    #more awakened sprites
    $dshow("asaga excited yell zawakened angry")
    asa "How 'bout this?"
    "Asaga awakened once more, and directed their buggy into the steel latticework of the Paladin's maintenance bay."
    $dshow(1000) #lol
    asa "Hoooyyaahh!!!"
    kay "A-are you CRAZY!?!?"
    
    play sound "sound/tire_skid.ogg"
    $dshow("asaga excited yell zawakened angry")
    
    "Steel frames flew past Shields as Asaga weaved the buggy through the maintenance bay, narrowly avoiding colliding into hangar crew and cargo crates."
    "None of the marines dared follow them into the maintenance bays and opened fire behind them, the shock rounds bouncing harmlessly off the steel jungle."
    "Shields put his head down as their buggy roared through the Phoenix's maintenance bay and arrived beside the Black Jack."
    $dshow(3010,ypos=1600)
    kay "Ugh... That was insane...!"
    "The two of them jumped off the buggy and sprinted up the Black Jack's loading platform while shock rounds pelted their position."
    kay "I sure hope this thing can accommodate two! Get us outta here, Asaga!"
    
    scene cg_asaga_cockpit_hanger with dissolve
    
    "Asaga shut the cockpit and activated the Black Jack."
    "Icari's voice came through the launch tower."
    ica "Heh. I've managed to clear out the control crew manning this place. Black Jack, you're cleared for launch."
    kay "Okay..."
    kay "We owe you one, Icari..."
    ica "Seriously..."
    ica "Once this is all over, I think you're gonna owe me some drinks... As well as a damned good explanation. Until then... I'll be waiting!"
    kay "Godspeed."
    
    play sound "sound/chargeup.ogg"
    
    "The hangar alarm rang and the crew scrambled out as the main airlock opened."
    "The Black Jack locked onto the linear rail."
    asa "Ooh! I forgot to put on mah plug suit!"
    asa "Hang on! The g's are gonna be crazy!"
    kay "Ooh gre--"
    "Shields braced himself against the cockpit's spherical wall as the linear rail flung the Black Jack out the hangar. Everything became a blur as all the blood in his body flowed to the back of his body."
    
    scene cg_asaga_cockpit_shout with dissolve
    
    "The Black Jack emerged out of the front of the ship, into a field of fire. Flak rounds exploded all around them, while lasers beams split the black void of space like thunder."
    "Alliance and PACT ships were tangled at dagger range, pounding each other with kinetic rounds. Ships exploded around them, as swarms of ryders spiraled around ships, bombers trying to take down larger ships with missiles, while interceptors cut down the bombers with assault rounds."
    asa "Let's get outta here while everyone's too busy trying to kill each other!"
    asa "Uhh... Heh."
    asa "You might want to hang on."
    
    scene cg_asaga_cockpit_focused with dissolve
    
    "Asaga spun the Black Jack around sharply, sending Shields tumbling to the opposite end of the cockpit."
    kay "Argggh!"
    
    play sound "sound/Laser 1.ogg"
    
    "A beam of laser cut through where the Black Jack was located a split second before."
    "Alarms blared throughout the cockpit as seven Prototype Ryders approached the Black Jack in a flying V."
    
    scene cg_asaga_cockpit_shout with dissolve
    
    asa "Aah, looks like your ex's friends are hot on our tail!!"
    kay "T-they are not my ex's friends!!"
    asa "Goin' out with the most popular guy in the galaxy sure a pain!! Gnnghh!!"
    
    play sound "sound/mech_boost2.ogg"
    scene cg_asaga_cockpit_focused with dissolve
    
    "Asaga jammed her joystick forward and sent the Black Jack on a dive as laser beams surrounded the cockpit."
    "Shields flew to the roof, then did somersaults around the circumference of the cockpit sphere when Asaga spun the Black Jack into a barrel roll."
    kay "Ar-gharghh!!"
    
    play sound "sound/Laser 1.ogg"
    
    "Spears of light flew between the Black Jack's legs, tails, and arms, but somehow never once struck the ryder."
    
    play sound "sound/warning.ogg"
    
    "Suddenly, all the lights in the cockpit turned red and a shrill alarm blared."
    
    scene cg_asaga_cockpit_shout with dissolve
    
    asa "Missile lock! S-shit!"
    
    play sound "sound/mech_boost2.ogg"
    
    "Shields rolled to the floor and felt his face get pancaked downwards as Asaga pulled into a high-g loop and spun the Black Jack around."
    "A swarm of over fifty angry missiles streamed towards them."
    #moar new sprites needed
    
    play sound "sound/heartbeat.ogg"
    scene cg_asaga_cockpit_awakenedshout with dissolve
    show cg_asaga_cockpit_awakenedshout1:
        xalign 0.5 yalign 0.5 alpha 1
        ease 0.5 zoom 1.5 alpha 0
    
    asa "Hooyaah!!!"
    "Asaga's eyes once again ignited blue as she flew the Black Jack in reverse between two opposing battleships exchanging kinetic rounds at dagger range."
    
    play sound "sound/Flak.ogg"
    
    "She sprayed assault rounds at the missiles, lighting the skies with explosions, all the while weaving her ryder backwards through the battleships' flak nets."
    
    play sound "sound/explosion1.ogg"
    
    "The rest of the missiles blew as they hit the battleships' flak wall. A pair of ambitious Prototype Units gave chase, while the other five split into two groups and circled around outside of the battleships' flak radius."
    asa "We gonna shake these gals! C'mon baby, dance!"
    "She kicked her foot pedal upwards, hitting the reverse boosters. The Prototype Ryder came flying towards the Black Jack as it rapidly decelerated."
    
    play sound "sound/Sword Shing 2.ogg"
    
    "At the last moment, Asaga flipped the joystick and activated the beam saber, turning the Black Jack into a whirlwind of blades as the Prototype Unit sailed past."
    
    play sound "sound/mech_boost2.ogg"
    play sound1 "sound/explosion4.ogg"
    
    "Like a buzz saw, the Black Jack's beam saber sliced the Prototype Unit into three sections. Asaga punched the boosters as the remains of the enemy exploded into a fireball behind them."
    
    play sound "sound/heartbeat.ogg"
    
    asa "G-guck..."
    "Blood dripped down her nose."
    
    scene cg_asaga_cockpit_awakenedclench with dissolve
    
    asa "Runnin' outta juice... Been awakenin' too much..."
    play sound "sound/explosion3.ogg"
    show layer master at shake1
    "Explosions rattled the cockpit as the second Prototype Unit sprayed them with pulse rounds. Asaga pulled upwards, sending the Prototype Unit chasing after her."
    asa "Look behind you..."
    "Completely focused on the Black Jack, the second unit never realized that Asaga had lured it directly in front of the Alliance battleship's kinetic turret."
    
    play sound "sound/cannon.ogg"
    
    "Not even a shred of the Prototype Unit survived when the Alliance battleship blew its load at point blank range, completely vaporizing the ryder."
    asa "Hehehe..."
    "The remaining five ryders converged and rushed for the Black Jack at the same time, attempting to overwhelm their adversary with sheer numbers."
    
    play sound "sound/pulse1.ogg"
    
    "They unleashed pulse rounds, scraping the paint off the Black Jack's armor."
    asa "E-eah!"
    
    show cg_asaga_cockpit_shout
    pause 0.2
    hide cg_asaga_cockpit_shout
    pause 0.2
    show cg_asaga_cockpit_shout
    pause 0.2
    hide cg_asaga_cockpit_shout

    "The light in Asaga's eyes flickered on and off as she began to reach her limit."
    asa "Capt'n! Imma need ya help!"

    play sound "sound/mech_boost2.ogg"

    "She rolled the Black Jack, sending Shields tumbling across the cockpit, and then pulled into a dive, tossing him onto her lap."
    kay "E-eh!?"
    asa "Need moar juice!"
    "Shields' head spun from being tossed about in the cockpit."
    "Before he know what was happening, Asaga picked his face off her lap and pressed their lips together." #oi
    
    play sound "sound/heartbeat.ogg"
    
    kay "W-wahgnn!!!"
    asa "M-mmm!!"
    "Their tongues crossed each other. Asaga's taste filled Shields' mouth."
    "Asaga gasped as they separated."
    
    play sound "sound/chargeup.ogg"
    
    asa "Energy restored!! HHOOYAAHH!!!"
    "The flame in her eyes burst into a fireball." #OI!
    "The Black Jack rapidly accelerated. Shields wrapped his body around Asaga and hung on for dear life."
    
    play sound "sound/pulse1.ogg"
    
    "The five Prototype Units shot towards them in a ring formation, spewing pulse rounds."
    
    play sound "sound/mech_boost2.ogg"
    
    "He clenched every muscle in his body as the Black Jack accelerated, pointed exactly at the center of the ring of hostiles. At the very last moment, Asaga pulled into a barrel roll and shot the Black Jack's shoulder mounted particle guns."
    
    play sound "sound/Laser 1.ogg"
    
    "Shields' jaws dropped when four laser beams emerged from the spinning Black Jack, slicing all five Prototype Ryders apart simultaneously as the Black Jack barrel rolled through their ring formation."
    
    play sound "sound/explosion4.ogg"
    
    "Light lit the rear of the cockpit as they exploded in a massive ring of fire."
    asa "Penta-kill!"
    kay "T-that was i-i-insane!!! How come you never do shit like that when I'm commanding you!?"
    asa "A-ah... well, that was a make out bonus."
    "Asaga smiled coyly."
    asa "...ya won't believe what a headjob will get you." #!!!
    kay "Idiot! Get us outta here, before more of 'em show up!"
    
    play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
    scene nightmare_approach with dissolve
    
    "His heart sank when a new, massive ryder appeared before them. One which struck terror into Shields' heart."
    kay "Shit--!"
    
    scene alice_cockpit1 with dissolve
    
    ali "Haha... So this is where you were hiding..."
    ali "But this is where your mission ends!"
    "The Nightmare Ascendant raised its particle gun and took aim."
    
    play sound "sound/explosion2.ogg"
    
    "But before it could fire, it was enveloped in explosions."
    
    scene icaricockpit with dissolve
    
    ica "Phoenix and Paladin, coming in to assist!"
    
    scene kryska_cockpit1 with dissolve
    
    kry "Hiyaah!! I'm your enemy, Prototype!"
    "The Phoenix raced ahead and came at the Nightmare Ascendant, katana drawn."
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Nightmare Ascendant met the Phoenix's blade with its own. In a grand display of its overwhelming strength, the Ascendant shoved the Phoenix away like a titan pushing back the valiant hero who had dared stand against it."
    
    scene icaricockpit with dissolve
    
    ica "Tsch... We'll distract it!"
    ica "Asaga... You know what you have to do!"

    scene cg_asaga_cockpit_awakenedclench with dissolve
    
    asa "Tsch..."
    "Shields' heart pounded as the Black Jack hit its thrusters, leaving the Nightmare Ascendant to Icari and Kryska."
    asa "You guys... better whack that thing good for me!"
    kay "(You two... Don't die...!)"
    "Shields balled his hand into fists. He desired with all his heart to remain with the others for the battle, but his own mission was too great to abandon."
    kay "(I can only trust in the other girls...)"
    kay "(Come on my other self... You had better pull through!)"
    "With that, the Black Jack left the battle behind and vanished into the abyss of space..."

    jump endgame_awardhall

label endgame_awardhall:

    #Black
    
    stop music fadeout 1.0
    
    scene black with dissolve
    "... ... ..."
    "... ..."
    "..."

    #Award hall - "T-minus 3 hours until the Liberation Day Massacre"
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 3 hours before the Liberation Day Massacre"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "music/Anguish.ogg" fadeout 1.5
    
    scene bg awardhall_snipe with dissolve
    if girl=='Asaga':
        $dshow(31)
    if girl=='Sola':
        $dshow(70110)
    
    "Shields waited with [girl] on the upper balcony of the award hall..."
    "They had waited at this position for the better part of the past 20 hours."
    "Shields had the advantage of knowing where the celebration party was going to be held in advance. Thanks to his dramatic escape from the Sunrider, security at the celebration would certainly be on the lookout for him, but they would never expect that he had already arrived at the site hours before when the battle, much less the party location, was even decided."
    "News of the liberation of Cera had finally hit the holonet."
    "After a night of desperate fighting, the tide of the battle had finally turned when Chigara devised a method to interfere with the Prototypes' brain waves by entering their mindstream."
    "This allowed Veniczar Fontana to regain control of his ships, and launch a devastating pincer attack on the remaining loyalist PACT Forces. When the Prototype Leader fell on the Nightmare Ascendant, all remaining PACT vessels surrendered unconditionally."
    "Veniczar Fontana, newly instated leader of PACT, shortly thereafter announced his intent to sign a peace treaty with the Solar Alliance, wherein PACT relinquished all military control over the Neutral Rim. A victory celebration wherein Chigara would be awarded with the Fereldin Cross was announced as well."
    kay "(Basically... Nothing's changed from the past...)"
    kay "(Everything we did up to this point was meaningless...)"
    kay "(But... now is the time when we can make everything right.)"
    kay "The time's... finally come..."
    "Shields looked down to the stage from the balcony. A perfect sniper's perch."
    "He was approximately 150 meters from where Chigara would stand at the stage to accept the medal... and then drop a pair of hunter drones into the hall."
    "Too far for shock rounds. But more than close enough to snipe her dead."
    "Shields closed his eyes."
    "This was the only option he had left."
    "Everything else had failed."
    kay "(Chigara...)"
    "His heart pounded. Sweat matted his uniform."
    "This would be where he would kill the former love of his life."
    kay "... ... ..."
    
    if girl == "Sola":
        "Sola wrapped her arms around him."
        $dshow(70201)
        sol "... ... ..."
        "He put his hand on hers."
        $dshow(70221)
        kay "Just a bit more... Then... we'll be through with this mission."
        sol "I am the better marksman. I shall take the shot."
        kay "... ... ..."
        kay "No."
        kay "From this distance, not even I can miss with a scope."
        kay "This... is my mission."
        kay "It's the reason why I was sent here."
        kay "I'm going to be the only one to bear this burden. It... is mine to carry."
        $dshow(70301)
        "Doing his best to force a smile on his face, Shields put his hand on top of Sola's head and patted her soft hair."
        kay "You just stand guard. Make sure our position isn't detected."
        $dshow(70321)
        sol "U-understood..."
        "The two of them once again sat down and waited..."
    
    if girl == "Asaga":
        
        $dshow(22)
        "Asaga wrapped her arms around him."
        asa "... ... ..."
        $dshow(32)
        asa "We're... finally here..."
        asa "Oy capt'n... We're here to kill Chigara, aren't we? It's... the only way we can stop her now."
        kay "... ... ..."
        "Shields swallowed."
        kay "I'll be the one to do it."
        kay "This... is my mission."
        kay "It's the reason why I was sent here."
        kay "I'm going to be the only one to bear this burden. It... is mine to carry."
        "Doing his best to force a smile on his face, Shields put his hand on top of Asaga's head and patted her soft hair."
        kay "You just stand guard. Make sure our position isn't detected."
        asa "All right..."
        "The two of them once again sat down and waited..."
        
    play music "Music/Camino.ogg" fadeout 1.5

    scene black with horizontalwipe
    scene bg awardhall_snipe with horizontalwipe
    if girl=='Asaga':
        $dshow(31)
    if girl=='Sola':
        $dshow(70110)
    "... ... ..."
    "... ..."
    "..."
    "Finally, the moment came."
    "The award hall was filled with guests."
    "Shields grabbed the rifle and looked down through his scope. Sure enough, he could see himself and Chigara sitting in the front table."
    "Chigara stood and walked towards the stage."
    kay "This... is... it...!!!"
    "Sweat dripped down his nose, despite the air conditioned hall."
    "He could hear his temples pounding as blood coursed through his head. If his heart pounded any louder, he feared he would go deaf."
    "He trained the cross hairs between Chigara's eyes."
    "All he would have to do is pull the trigger. Then none of the nightmares of the past would happen."
    "The Admiral would not be shot before his very eyes. The Alliance officers would not be gunned down. The Alliance would not attempt to unleash the Tactical Paradox Core upon his home world. The galaxy would not be thrust into a massive war to the bitter end. His ship would not be lost in a final, suicide attack."
    "He would instead, return home, at the end of a hard fought war. He would finally return to that mountain... and bury his sister. Bury her so deep that her ghost would no longer haunt him in his nightmares."
    kay "...I..."
    "Memories flashed by in his head."
    
    show chigarabeach2
    show black:
        alpha 0.5
    with dissolve
    
    "He had loved her. He would have dropped everything else in his life to open her bakery."
    "He had promised her... That he would burn the very galaxy if it meant protecting her... Yet... He found himself here, breaching that very promise."
    
    hide chigarabeach2
    show chigara_tea1 behind black
    with dissolve
    
    "His eyes began to water."
    "He had imagined they would get married. That they would have children. That the scars of the past would heal as he lived out the remainder of his life with her in peacetime."
    
    hide chigara_tea1
    show shieldschigarahug behind black
    with dissolve
    
    "Her voice echoed in his head. It was the only voice which soothed his agony."
    "Every time he heard Maray's voice... accusing him of abandoning her... Chigara would tell him that he had done his very best. That his sister did not resent him for abandoning her to her fate."
    
    hide shieldschigarahug
    show chigaralap1 behind black
    with dissolve
    
    "She would call him a hero. Hero. Hero. Hero..."
    "And yet... that hero... had his finger upon the very trigger which would end her life."
    kay "(Tsch... No...)"
    kay "It was... all a lie...!!"
    "Tears streamed down his cheeks."
    kay "She... said all those things... just to control me...!!"
    kay "In the end... she was... nothing... but a PROTOTYPE!!!"
    kay "She... betrayed me...!! Betrayed... everyone!!"
    "Yet, his heart twisted so... He could no longer breathe."
    "He had to end this now. Or else he would choke upon his regrets and drop dead."
    
    hide chigaralap1
    hide black
    with dissolve
    
    $ menu_choices = [
                    ["Pull the trigger.","pullthetrigger","Tirar del gatillo."],
                    ["Don't pull the trigger","dontpulltrigger","No tirar del gatillo."],
                    ]
    show screen decision
    pause
            
label pullthetrigger:
    
    #Pull the trigger.

    if girl=='Asaga':
        $renpy.save("ASAGA ALTERNATIVE END")
        hide asaga with dissolve
    if girl=='Sola':
        $renpy.save("SOLA ALTERNATIVE END")
        $dshow(70123)
    kay "EAAHH!!! CHIGARA!!!!"
    "Shields peeled his eyes open, and summoned all the strength in his body. Or else he knew he would back out at the last moment."
    "He channeled everything he had within him to his finger... and pulled the trigger."
    
    play sound "sound/sniperrifle.ogg"
    show white
    pause 0.2
    hide white
    
    "The single, sharp crack of the rifle echoed through the hall."
    "Chigara took the bullet directly to the head."
    "Shields kept his eyes open."
    "The back of her skull burst open, splattering the floor with her brain and blood."
    "She crumpled to the floor, her face contorting with pain."
    "Finally... her face came to rest... upon an expression of relief."
    "Alice had finally died, leaving Chigara with just a split second of knowledge that Alice's final, desperate plan to destroy all that they had accomplished had failed."
    "The light faded from Chigara's eyes as she relished Alice's defeat..."
    "With that, Alliance servicemen burst into the room and evacuated the Alliance dignitaries. Everyone else ran from the room, crouched down and covering their heads. Except for the other Shields, who ran to the stage and cradled Chigara's dead body."
    "The massacre was thwarted. The future was saved."
    "Shields crumpled down to the floor, sobbing."
    "He had succeeded."
    kay "I... did... it..."
    kay "I... changed... history...!"
    kay "I... won...!"
    "And yet, he felt nothing but an black void in his heart."
    
    if girl == "Sola":
    
        $dshow(70113,blush=True)
        "Sola embraced him with all her heart, trying to comfort him in his darkest moment."
        sol "Yes captain... You... have won. This is... our victory."
        sol "Everyone has been saved."
        kay "Sola....!!!"
        "He sobbed into her shoulder."
        $dshow(70103,blush=True,cry="tears")
        kay "I killed her... I... killed... Chigara..."
        kay "And... in the end... she was... relieved..."
        sol "Shhh..."
        sol "You... needn't worry about that..."
        sol "I... am here... am I not...?"
        
        $dshow(70313,blush=True)
        
        sol "Eh-haha... From now... I shall provide whatever she did..."
        $dshow(70203,blush=True)
        sol "You mustn't cry, captain... You are my hero."
        $dshow(70320,blush=True)
        sol "You are... everyone's hero."
        "Shields merely sobbed in horror at what he had just done..."
        scene white with Dissolve(3)
        "The world around him faded to white..."
        "A time paradox now triggered, this universe ended... And a new universe was born in its place."
        "A mostly happy universe, where the Liberation Day Massacre did not exist. But also one where Shields never got over the scars he received throughout his desperate mission to liberate Cera..."

    if girl == "Asaga":
        $dshow(422)
        "Asaga embraced him with all her heart, trying to comfort him in his darkest moment."
        asa "You... did it captain!! You... saved everyone! We won!!"
        kay "Asaga....!!"
        "He sobbed into her shoulder."
        $dshow(434)
        kay "I killed her... I... killed... Chigara..."
        kay "And... in the end... she was... relieved..."
        $dshow(534,blush=True)
        asa "Oy... Captain... S-stop it..."
        asa "S-stop... crying like that..."
        $dshow(634,blush=True)
        asa "We're supposed to be happy, all right? We... won! We won! We WON!!!"
        asa "Why... are you crying like that...!?"
        $dshow(524,blush=True)
        asa "If you don't stop... Then I'll..."
        kay "I still... Chigara....!!"
        $dshow(524,blush=True,cry="closeeyetears")
        asa "She... was... my..."
        asa "Friend..."
        "Asaga's face crumpled. She fell to the floor in tears."
        "Shields sobbed in horror at what he had just done..."
        scene white with Dissolve(3)
        "The world around him faded to white..."
        "A time paradox now triggered, this universe ended... And a new universe was born in its place."
        "A mostly happy universe, where the Liberation Day Massacre did not exist. But also one where Shields never got over the scars he received throughout his desperate mission to liberate Cera..."

    call dlc_credits
    
    play music "Music/Love_Theme.ogg" fadeout 1.5
    
    scene bg room_day with dissolve  #TODO apartment BG
    
    "Shields sat on his bed in his apartment."
    "Five years had passed since he thwarted the Prototypes' plan to assassinate Admiral Grey and the Alliance military leaders."
    "In the universe which resulted from his actions, the timeline was as follows: Kayto Shields discovered that his Chief Engineer was a Prototype spy thanks to a misplaced holo left by her accomplice, the ship's doctor. He managed to thwart the mass assassination by sniping her dead during the award ceremony, moments before she carried out the attack."
    "While he was briefly detained by the Alliance after he turned himself in, the ensuing investigation uncovered undeniable evidence of Chigara's plot, completely vindicating Shields. In the end, he ended up being the one to receive a medal."
    "Yet... killing Chigara changed Shields forever." 
    "Shortly after the restoration of Cera High Command, Shields transferred himself to a minor desk job, far away from galactic fame. Instead, he lived out the following years as a recluse, never once setting out to space again."
    "Every night, he struggled through nightmares, where he was visited by the rotting corpses of Chigara and his dead sister... Every night, their ghosts reminded him of a single truth: That he had failed to save them. Eventually, he became an insomniac and had to be medicated to be able to function normally."
    
    if girl == "Sola":
        $dshow(70321)
        "His sole source of comfort was his loving wife, Sola, who vanished from the galactic stage along with him, and endeavored to singlehandedly heal his wounds."
        "While Shields fell deeper into depression, she watched over him with nothing but a gentle smile. Every night, she stroked his head, until he finally pretended to be asleep."
        "However, seeing Sola trapped in a relationship with him only fueled his guilt."
        "Yet he didn't have the motivation to do something as drastic as kill himself. Instead, he merely felt an enormous numbness."
        "The numbness of no longer having a purpose."
        "For the rest of his life, he would merely wander on, working as a civil servant, picking up the usual paycheck, and grow old with Sola, until they finally disappeared from the face of the planet..."

        #ALTERNATE SOLA END: "FUTURE WON WITH BLOOD"
        $persistent.unlocked_endings["SOLA ALTERNATIVE END: FUTURE WON WITH BLOOD"] = True
        $chivo_process('Sola Alternate Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolve
        show screen alternate_end
        #show expression Text("ALTERNATE SOLA END:\nFUTURE WON WITH BLOOD",yalign=0.5,size=90,color="fff")
        pause 3

    if girl == "Asaga":
        $dshow(432)
        "His sole source of comfort was his loving wife, Asaga."
        "Yet, their relationship was far from easy either. When they first eloped, rumors spread throughout Ryuvia Prime that their queen had abandoned her people in pursuit of romance."
        "In the end, she was scandalized in the press, forcing her to abdicate the throne. Shortly thereafter, she vanished from public view, and settled down with Shields on Cera."
        "Asaga's once cheerful personality vanished, and she became quiet and distant in adulthood."
        "While Shields fell deeper into depression, Asaga watched over him with nothing but a sad smile. Every night, she stroked his head, until he finally pretended to be asleep."
        "Seeing Asaga's reputation get torn up because of him only fueled Shields' guilt."
        "Yet he didn't have the motivation to do something as drastic as kill himself. Instead, he merely felt an enormous numbness."
        "The numbness of no longer having a purpose."
        "For the rest of his life, he would merely wander on, working at his civil servant job, picking up the usual paycheck, and grow old with Asaga, until they finally disappeared from the face of the planet..."

        #ALTERNATE ASAGA END: "FUTURE WON WITH BLOOD"
        $persistent.unlocked_endings["ASAGA ALTERNATIVE END: FUTURE WON WITH BLOOD"] = True
        $chivo_process('Asaga Alternate Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolve
        show screen alternate_end
        #show expression Text("ALTERNATE ASAGA END:\nFUTURE WON WITH BLOOD",yalign=0.5,size=90,color="fff")
        pause 3

    $dshow(32210)
    cla "Aah, well, looks like you managed to thwart the massacre... But you still mostly screwed up in the end, 'cause Chigara ended up escaping when you kidnapped her, the ship lost all power, and the warning wasn't relayed to Fontana in time!"
    $dshow(34310)
    cla "If you hadn't shot Chigara at the very end, things would pretty much have ended exactly the same as the main story!"
    cla "Try again, and this time, don't waste time trying to restore the Sunrider's main reactor. Instead, find a way to prevent Alice from assuming control of Chigara during the kidnapping attempt. Then the reactor won't be shut down in the first place."
    $dshow(30000,ypos=1600)
    cla "Teehee, I'm sure you'll be able to figure it out, captain!"
    $renpy.full_restart()
        
label dontpulltrigger:
    
    #Don't pull the trigger
    if girl == "Sola":
        $renpy.save("SOLA NORMAL END")
    if girl == "Asaga":
        $renpy.save("ASAGA NORMAL END")
    kay "No... Chigara...!!"
    "Shields' eyes clenched shut."
    "He could not do this. He could not take Chigara's life, no matter what may happen to the galaxy."
    "Voices echoed in his head."
    scene cg_shieldschigarahug
    show black:
        alpha 0.5
    with dissolve
    chi "Shh... You have me, captain."
    chi "You have your ship. Your crew."
    chi "We're your family."
    kay "... ... ..."
    chi "You... never cried when your sister died..."
    kay "... ... ..."
    chi "It's all right captain... Your secret will be safe with me."
    chi "I know I'll never be able to replace everything you lost..."
    chi "But... I'll always be here for you."
    scene bg awardhall_snipe with dissolve
    if girl=='Asaga':
        $dshow(31)
    if girl=='Sola':
        $dshow(70110)
    kay "(Chigara...)"
    
    play music "Music/Colors_Chigara.ogg" fadeout 1.5
    
    kay "She may have been a spy... But in the end... She loved me just the same."
    kay "It was the Prototypes who caused the massacre... Not her... Chigara was just an unwitting pawn."
    kay "And I cannot kill an innocent. Even if that decision will indirectly lead to the death of billions. For that is a moral imperative no captain ought cross."
    "He put the rifle down and stood."
    kay "The past is the past."
    kay "And I'm... not going to commit murder to change what happened."
    kay "It's... our experiences which define us."
    kay "If a man gained the power to rewrite his past... then he would cease to become human."
    kay "And... I am still human."
    kay "No matter how great the tragedies of the past..."
    kay "I have to live with them."
    kay "So that I may work for a better tomorrow."
    "Shields made his decision."
    kay "Come on, [girl]. We're leaving."
    kay "We only have seconds until the massacre begins."
    
    if girl == "Sola":
        $dshow(70111)
        sol "... ... ..."
        "Sola's eyes flickered with doubt. But she swallowed her regrets and followed Shields out of the award hall."
        $dshow(70311)
        sol "Understood..."
        sol "Whichever path you take... I shall be beside you."
        kay "I know..."
        "He smiled and took her hand."
        kay "I'll see you..."
        sol "Yes..."
        sol "We shall meet... again."
        scene white with Dissolve(3)
        "The two of them opened the door out of the hall, and stepped into a blinding white void."
        "Everything faded to nothingness, as the universe resolved Shields' time translocation and returned him to his own timeline..."

    if girl == "Asaga":
        $dshow(3222,ypos=1600)
        asa "Hey, but---"
        kay "We're through here."
        "Asaga knew from the tone of Shields' voice that he would accept no argument against his decision."
        $dshow(53)
        "She bit her tongue."
        asa "... ... ..."
        $dshow(654)
        asa "If you're sure 'bout this... then I guess I can go along with it... but..."
        kay "The future is not for us to change."
        kay "We would never be heroes if we murdered Chigara today."
        $dshow(433)
        "Asaga reluctantly smiled."
        asa "All right..."
        "He smiled and took her hand."
        kay "This isn't the end."
        kay "I'm counting on you... to rescue me again."
        $dshow(543)
        asa "Huh?"
        kay "You'll know when the time comes."
        scene white with Dissolve(3)
        "The two of them opened the door out of the hall, and stepped into a blinding white void."
        "Everything faded to nothingness, as the universe resolved Shields' time translocation and returned him to his own timeline..."

    call dlc_credits
    
    if girl == "Sola":
        scene bg desert with dissolve
        
        play music "music/Colors_of_an_Orchestra_II.ogg" fadeout 1.5

        "Shields woke up beside his cabin, deep within the Tydarian desert."
        "A full month had passed since he arrived here. Ava, Asaga, and Claude were still presumably at Ryuvia Prime, trying to acquire a new vessel. They had not heard back from Icari ever since she left for uncivilized space, but he was confident she was doing fine. As for Kryska, news of her arrest had now hit the holonet."
        "She was imprisoned and was to stand trial before a military tribunal."
        "However, her plan was not a total failure, as the mass media shortly thereafter uncovered evidence of the Alliance's plan to destroy Cera."
        "While the military denied any knowledge of the plot, the Progressive Party now intended to use the testimony which will be uncovered during Kryska's trial to unravel the United Universalists' control over the war."
        "In other words, Kryska was at least right about one thing: The Alliance did find the truth of what happened at Cera. In the end, that may have been the only reason why she turned herself in."
        "Sola appeared on a hover bike, towing a cart full of clear plastic plating behind her."
        $dshow(70321)
        sol "I have returned from my expedition to the settlement."
        sol "There is still no word of any developments at Ryuvia Prime. As such, we should take measures to ensure we can sustain ourselves for the long term. I have acquired these materials to construct a greenhouse next to our cabin, wherein we will be able to grow produce."
        kay "(Sola's planning to settle in here for the long term...)"
        kay "(She... might be right...)"
        kay "(After all... Acquiring a new ship comparable to the Sunrider is pretty unlikely...)"
        kay "(No... I have to keep such thoughts from my head...)"
        "He had to remain optimistic... But with each passing day, he became more despondent. A second prototype assault carrier was not simply going to fall on their laps."
        "Shields blinked. What had he been doing out here, standing in the dry desert heat by himself?"
        "He vaguely recollected an urgent mission... to prevent something. But what?"
        kay "Hey Sola, do you remember something weird happening during your trip? Like, you lost consciousness for a moment?"
        $dshow(70221)
        sol "No... Does your health ail you? Continued exposure to the desert heat could easily lead to momentary loss of consciousness as well as hallucinations. You should return to the cabin."
        kay "All right..."
        "He started walking back indoors."
        "Sola must be right. He was constantly sweltering in the heat now. No wonder his memories were becoming murky."
        "However, he looked back and looked at Sola."
        "Somehow... she looked much prettier than he last remembered."
        kay "(Heh... must be the heat, making my hormones all jumpy...)"
        $dshow(70212,blush=True)
        sol "... ... ..."
        sol "W-why do you stare at me so?"
        kay "... ... ..."
        kay "Nothing."
        kay "I'm just glad we could still be together."
        $dshow(70323,blush=True)
        sol "Yes... as am I..."
        kay "No matter what happens... We'll face it together, Sola."
        sol "... ... ..."
        $dshow(70320)
        sol "Understood..."
        sol "I shall..."
        sol "See you later..."
        kay "Yeah."
        kay "See you later, Sola."
        "With that, Shields entered the cabin, any last memory of his little trip through time completely wiped from his mind."

        #NORMAL SOLA END: "STILL TOGETHER"
        $persistent.unlocked_endings["SOLA NORMAL END: STILL TOGETHER"] = True
        $chivo_process('Sola Normal Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolve
        show screen normal_end
        #show expression Text("NORMAL SOLA END:\nSTILL TOGETHER",yalign=0.5,size=90,color="fff")
        
        pause 3
        
        
    if girl == "Asaga":
        
        play music "Music/Cracking_the_Code.ogg" fadeout 1.5
        
        #Escape pod
        scene bg escapepod with dissolve

        "Shields woke up, his memories a blur."
        "He took in his surroundings and realized he was in an escape pod with Lynn. He remembered this place."
        "This was after he had somehow escaped going down with the ship when he set it on a collision course with Machiavelli Actual."
        "Shields blinked in confusion. He could have sworn this had happened before..."

        play sound "sound/warning.ogg"

        "His overwhelming sense of déjà vu was interrupted when the escape pod's alarm went off. He pulled himself to the pod's controls and saw an enormous PACT Fleet approaching his position."
        kay "(I can't remember how I got here... But all of this feels familiar... )"
        "Words echoed in his head."
        kay "{i}I'm counting on you... to rescue me again.{/i}"
        asa "{i}Huh?{/i}"
        kay "{i}You'll know when the time comes.{/i}"
        "The pod's comm crackled to life."
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
        "The cabin \"thunked\" as the Black Jack shot a magnetic tow cable at the pod while performing a close flyby."
        asa "Hitting after burners!"
        asa "Let's out run these guys before they can get shots off at us!"

        #wipe
        
        stop music fadeout 1.5
        scene black with horizontalwipe
        scene bg escapepod with horizontalwipe
        "... ... ..."
        "... ..."
        "..."
        "The escape pod's gate hissed open after it docked at the small cargo runner."
        scene bg cargohangar with dissolve
        $dshow(6021)
        "Shields emerged."
        asa "Captain...!"
        
        play music "Music/Colors_Loop.ogg" fadeout 1.5
        
        if legion_destroyed:
            show helives with dissolve
        else:
            show helives_nopatch with dissolve
        "He ran out of the escape pod and embraced Asaga. Somehow, he felt as if he had longed for this moment forever."
        "Unexpected tears began to run down his eyes."
        kay "Asaga..."
        kay "I... thought I'd never see you again..."
        asa "What are you talking about, captain...? Of course I'd come back and rescue you..."
        asa "Somehow... I knew you were alive. I knew you couldn't have died on the Sunrider!"
        asa "I... I'll keep protecting you, captain! I won't ever let you go!"
        kay "Yeah..."
        kay "I know..."
        "Somewhere deep in his sub consciousness, he felt as if he had held onto Asaga before. His arms were wrapped around her so tightly they nearly melded together. And then they had kissed."
        "It was a moment of happiness."
        kay "Despite everything... I'm glad that I still ended up here, with you."
        kay "(No matter the scars we carry... We can't keep regretting the past.)"
        kay "(Because humans do not carry redo buttons. And we are better off for it.)"
        kay "(All we can do is march forward, for a brighter future.)"
        kay "Asaga..."
        kay "Thank you... for always having my back."
        "Tears rolled down Asaga's cheeks."
        asa "Yeah!"
        "With that, all but one memory of Shields' little trip through time completely vanished from his mind."
        "All but the sweet taste of Asaga's kiss."

        #NORMAL ASAGA END: "STILL TOGETHER"
        $persistent.unlocked_endings["ASAGA NORMAL END: STILL TOGETHER"] = True
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolve
        show screen normal_end
        #show expression Text("NORMAL ASAGA END:\nSTILL TOGETHER",yalign=0.5,size=90,color="fff")
        $chivo_process('Asaga Normal Ending')        
        pause 3
        
    $dshow(34311)
    cla "Eehh... So in the end, you decided to keep the past exactly the same? After all the work poor ol' Claude went through to send you back in time!?"
    $dshow(34101)
    cla "You're really hopeless, captain..."
    $dshow(32311)
    cla "To see a better outcome, find a way to prevent Alice from assuming control of Chigara during the kidnapping attempt. That way, the ship won't lose power."
    $dshow(32210)
    cla "Now get to it! You have a future to change, and a god to entertain!"
    $renpy.full_restart()
        
label endgame_asagakillschigara:
    
    if girl == "Ava":
        $renpy.save("AVA NORMAL END")
    if girl == "Sola":
        $renpy.save("SOLA WORST END")
    
    ##IF BACK UP COMM USED
    if backup_comm == True:

        #Bridge
        scene bg bridge with dissolve
        show mook as mook1:
            xpos -0.25
        show mook as mook2:
            xpos 0.15
        show mook as mook3:
            xpos 0.55
        show kayto:
            xpos 0.33
        with dissolve
        $dshow(10000,xpos=0.66)
        "The marines marched Shields to the bridge at gunpoint."
        kay "(I never thought that I'd become a captive on my own bridge...)"
        "He could tell the battle situation was already tense. Thanks to the Sunrider losing power, the chronology of events he was familiar with had been forever altered."
        "Instead of the Sunrider re-entering the battle after finishing its resupply operation, the loyalist PACT Fleet had advanced and launched an offensive while the ship was powered down."
        "In other words, the timing of events had now moved forward. By now, most of the Sunrider's ryders had already sortied. Within moments, Chigara would likely enter the mindstream to restore Fontana's control over the allied PACT Fleet."
        kay "(This is the pivotal moment...)"
        kay "(I have to end this now. I won't get another shot at this...)"
        "He heard Kryska's voice crackle through the comm."
        $dshow(10010)
        
        kry "Sunrider, the Nightmare Ascendant's coming around for another pass!"
        kry "We've been hitting it with everything we've got, but our weapons are ineffective!"
        kayo "Prototype. What do you know about the Nightmare Ascendant?"
        kay "... ... ..."
        kay "It's an ancient Ryuvian ryder used by Sharr Myren, who vanished millennia ago. Defeating it won't be easy, but if you stick it with enough lead, it'll go down like anything else."
        kay "But be careful. The Prototype Leader piloting it can also awaken, just like Asaga and Sola."
        kayo "I see..."
        kayo "The only way we're going to down that monstrosity is if the entire Combined Fleet and the allied PACT Fleet hits it with everything they've got."
        kayo "Chigara, how soon can you begin to restore control to Fontana's ships?"
        chi "I can begin any time, captain!"
        kay "No, wait!"
        kay "If Chigara enters the mindstream... Then you will assure your own destruction. The Prototype Leader will transfer her consciousness to Chigara's body and use it to perpetrate the assassination of Admiral Grey and every single Alliance military leader gathered at the victory celebration!"
        $dshow(11300)
        ava "Captain..."
        ava "We must consider the risk--"
        kayo "Prepare to enter the mind stream, Chigara."
        hide chigara with dissolve
        $dshow(13100)
        ava "Captain!"
        kayo "Commander, if we don't get Fontana's ships into the battle right now, then the entire Combined Fleet will be lost!"
        $dshow(13010)
        kayo "Does the Prototype have any other ideas on how to win?"
        kay "T-tsch..."
        kay "(Come on... There's... got to be some way we can win without Fontana...)"
        play sound "sound/explosion3.ogg"
        show layer master at shake1
        "The Sunrider shook as it took more hits."
        "In front of them, the Nightmare Ascendant's flier drones danced around an Alliance Carrier as they carved it to pieces."
        "The entire Carrier burst into a massive fireball, sending a piece of its launch platform flying through the gut of a cruiser. The smaller vessel listed sideward as its fuel tanks lit on fire, burning its crew alive."
        kayo "We... have to trust Chigara!"
        show kayto yell:
            xpos 0.33
        with dissolve
        kayo "I know she's not a Prototype! She's one of us."
        kayo "She's our trump card! She can turn this battle around in our favor!"
        kay "That's exactly what the Prototypes want you to do! We have to continue without Fontana's fleet!"
        kayo "And face certain defeat!?"
        $dshow(13100)
        ava "Captain, the prisoner's words do have merit. The Chief Engineer of this vessel could easily have embedded the logic bomb which shut down our ship. Further, if she is indeed a Prototype spy, then it stands to reason that she could be mind controlled as suggested by our prisoner."
        ava "A sound course of action may be to permit her to enter the mindstream to undo the Prototypes' control over the allied fleet for now, but then to detain her after the danger has passed."
        "Burning embers glowed inside the other Shields' eyes."
        kayo "She isn't a spy! There's no way she would be working for the enemy!"
        kay "(It's just like when...)"

        #CG: SWORN ENEMIES 2
        show swornenemies2
        show black:
            alpha 0.5
        with dissolve

        kayo "I'll... damn the entire galaxy if it means protecting Chigara..."
        kayo "S-she was there for me... when..."
        kayo "While you... weren't...!!!"

        hide swornenemies2
        hide black
        with dissolve
        "Sweat dripped down Shields' face as he heard his past self rave in madness."
        "He closed his eyes."
        kay "(Yes... This was the me of the past...)"
        kay "(A fool. A dangerous fool.)"
        ava "Captain, you have become emotionally compromised!"
        ava "You are failing to appraise this situation rationally! I cannot permit you to lead this ship when you are basing your decisions solely on your-"
        $dshow(13000)
        kayo "ENOUGH!"
        kayo "I will not allow you to slander our Chief Engineer!"
        kayo "Commander... To think I once called you my friend..."
        kay "(Shit... He's completely lost his mind!)"
        kay "(Just what kind of lies have Chigara been feeding him lately? For all intents and purposes, he's fallen completely under the Prototypes' control!)"
        kay "(There's no hope of ever convincing him now!)"
        
        if girl == "Icari":
            jump claude_end
        
        "Icari's voice cut through the comm."
        ica "O-oy, captain, A-Asaga's gone berserk!!! W-what are we supposed to do!?"
        kayo "What!?"
        
        show asagacockpit4 with dissolve
        
        asa "... ... ..."
        asa "I'm sorry captain..."
        asa "But you're being tricked..."
        asa "I'm... doing this for the good of the ship...!!!"
        asa "Chigara.... is the traitor!!!!"
        ava "The Black Jack is on a intercept course for the Liberty!"
        kayo "ASAGA!!!!"
        asa "Captain..."
        asa "I've... always loved you!"
        asa "I'M GOING TO PROTECT YOU!!!!!!!!!"
        kay "(This is happening exactly like my own timeline!)"        
        
        hide asagacockpit4 with dissolve
        
        if girl == "Sola":
            kayo "Sola! Can you snipe down the Black Jack!?"
            
            show solacockpit1 with dissolve
            
            sol "I'm afraid I cannot do that." #, dave
            kayo "What...?"
            sol "The captain I know would never ignore the advice of his crew. It is the other Kayto Shields I choose to follow."
            kayo "You're... betraying me... too...?"
            sol "No. This is for your sake as well."
            sol "With these hands, I will send you back home to Cera, the massacre averted."
            kayo "Claude! Use the grav gun to stop Asaga!"
            cla "O-ok-"
            "The Seraphim took aim at the Bianca's arm."
            cla "E-ee!!!"
            sol "I will not hesitate to fire."
            
            hide solacockpit1 with dissolve
            
        if girl == "Ava":
            kayo "Claude! Use the grav gun to stop Asaga!"
            cla "Teeheeehee... Sorry, captain... But I'm afraid your other version's managed to outmaneuver you."
            show claudecockpit_orb1 with dissolve
            "Claude's face appeared on the main monitor."
            cla "I won't be listening to your orders any more."
            "Shields sighed in relief."
            kay "Claude! You made it!"
            cla "Of course!! Fooling my other self was a piece of cake!"
            cla "Now... This is the pivotal moment..."
            cla "What is your order?"
            kay "(It's too late for second thoughts now...)"
            kay "(Getting Asaga to kill Chigara for us really is the only option!!!)"
            kay "Let Asaga through and let her destroy the Liberty!"
            cla "All right, if that's your choice..."
            hide claudecockpit_orb1 with dissolve
        
        kayo "YOU!!"
        "The other Shields grabbed him by the scruff of the throat and lifted Shields off his feet."
        kayo "What have you done to Asaga!? Why's she attacking the Liberty!?"
        kay "Nothing! If you had been paying more attention to your crew, then you would have found out about Asaga's feelings for you yourself!"
        "For a moment, they faced off against each other in front of the bridge, their backs illuminated by the giant main monitor. Man to Man."
        "Shields gritted his teeth."
        "This would be where he would defeat his past self... and rewrite the future."
        "He would dirty his hands in the process by murdering Chigara... And turn Asaga into her murderer... But it was a small price to pay..."
        "The security of the entire galaxy hinged on this moment."
            
    if backup_comm == False:
        scene bg bridge with dissolve
        show mook as mook1:
            xpos -0.25
        show mook as mook2:
            xpos 0.15
        show mook as mook3:
            xpos 0.55
        with dissolve
        
        "The pair of marines escorting him dropped Shields to the floor upon arriving at the front of the bridge, making him tumble flat on his face."
        "He looked up to see..."
        show kayto:
            xpos 0.33
        with dissolve
        kayo "I see you've finally regained consciousness..."
        kay "Kayto... Shields..."
        "Once again, he faced himself. His greatest nemesis." #2 deep 4 me
        "Shields tried to throw himself at his past self, but found that he was completely bound at the foot and wrists. He only struggled in futility against his captor."
        kayo "You son of a bitch..."
        
        if girl == "Sola":
        
            kayo "Sola's now in sickbay thanks to your actions... Along with three of my marines..."
            kayo "And I see you've even turned my XO against me."
        if girl == "Ava":
            kayo "I see you've even turned my XO against me."
        $dshow(10000,xpos=0.66)
        "Shields looked around to see Ava standing beside him, now in handcuffs as well."
        $dshow(10110)
        ava "Captain, you're making a mistake. That's still the real Kayto Shields in front of you."
        ava "You still have one last chance to stop the Prototypes' plot. I implore you to take it."
        $dshow(10010)
        kayo "Commander... No... Ex-commander."
        kayo "After all we've been through... You disobeyed my orders... Worked behind my back..."
        show kayto yell:
            xpos 0.33
        with dissolve
        kayo "We're through!" 
        kayo "To think I once called you my friend..."
        kay "(Shit... He's completely lost his mind!)"
        kay "(Just what kind of lies have Chigara been feeding him the past couple of hours? For all intents and purposes, he's fallen completely under the Prototypes' control!)"
        kay "(There's no hope of ever convincing him now!)"
        $dshow(10120)
        ava "Tsch..."
        ava "Captain... You are blind. The Kayto Shields struggling on the floor now is a far better captain than you are!"
        ava "He has worked the past two days to thwart the Prototypes' plot, while you have done nothing but play according to their script! You must come to your senses!"
        ava "This is your final chance!"
        kayo "ENOUGH!"
        kayo "I will not be questioned in my own bridge!"
        "Burning embers glowed inside the other Shields' eyes."
        kay "(No... it's just like when...)"

        #CG: SWORN ENEMIES 2
        show swornenemies2
        show black:
            alpha 0.5
        with dissolve
        kayo "I'll... damn the entire galaxy if it means protecting Chigara..."
        kayo "S-she was there for me... when..."
        kayo "While you... weren't...!!!"
        hide swornenemies2
        hide black
        with dissolve
        
        "Sweat dripped down Shields' face as he heard his past self rave in madness."
        "He closed his eyes."
        kay "(Yes... This was the me of the past...)"
        kay "(A fool. A dangerous fool.)"
                
        play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
        
        "Just then, he heard Icari's voice on the comm."
        ica "A-Asaga's gone berserk!!!"
        ica "O-oy, captain!? W-what are we supposed to do!?"
        ica "A-are we actually gonna shoot her down!?"
        kayo "... ... ..."
        kay "(The battle has already begun...!)"
        kay "(No... Has Claude gotten into position? Was our plan a success!?)"
        kry "Captain!! Your orders!"
        kayo "Charge the Sunrider's trinities. Lock on to the Black Jack."
        kay "(SHIT!!! DON'T DO IT!!!)"
        kay "SHIELDS!!!"
        $dshow(10121)
        asa "Watch me, captain!!!"
        asa "O-one day... You're going to realize I was right!!!!"
        kay "TRUST IN ASAGA!!!! SHE'S RIGHT!!!"
        
        if girl == "Sola":
            "An alert sounded throughout the bridge."
            cre1 "Captain, we've got an unauthorized launch in the hangar!"
            kayo "What!?"
            cre1 "It's the Seraphim!"
            "Sola's voice crackled through the comm."
            sol "I apologize for my late arrival."
            sol "Orders, captain."
            "Suddenly, Shields realized that Sola was talking to him instead of the other Kayto Shields."
            kayo "What the- Sola, what are you-"
            kay "PROTECT THE BLACK JACK!!!"
            sol "Understood."
            "Just then, another voice cut through the channel."
            cla "Teeheeehee..."
            show claudecockpit_orb1 with dissolve
            "Claude's face appeared on the main monitor."
            cla "Looks like you've managed to get here in time for the main event, captain."
            "Shields sighed in relief."
            kay "Claude! You made it!"
            cla "Of course!! Fooling my other self was a piece of cake!"
            cla "Now... This is the pivotal moment..."
            cla "What is your order, captain?"
            kay "(It's too late for second thoughts now...)"
            kay "(Getting Asaga to kill Chigara for us really is the only option!!!)"
            kay "Proceed with the plan! Let Asaga through and let her destroy the Liberty!"
            cla "If that's your choice..."
            hide claudecockpit_orb1 with dissolve
            
        if girl == "Ava":
            kayo "Claude! Use the grav gun to stop Asaga!"
            cla "Teeheeehee... Sorry, captain... But I'm afraid your other version's managed to outmaneuver you."
            show claudecockpit_orb1 with dissolve
            "Claude's face appeared on the main monitor."
            cla "I won't be listening to your orders any more."
            "Shields sighed in relief."
            kay "Claude! You made it!"
            cla "Of course!! Fooling my other self was a piece of cake!"
            cla "Now... This is the pivotal moment..."
            cla "What is your order?"
            kay "(It's too late for second thoughts now...)"
            kay "(Getting Asaga to kill Chigara for us really is the only option!!!)"
            kay "Let Asaga through and let her destroy the Liberty!"
            cla "All right, if that's your choice..."
            hide claudecockpit_orb1 with dissolve
            
        kayo "W-WHAT!?"
        kayo "YOU!!"
        "The other Shields grabbed him by the scruff of the throat and lifted Shields off his feet."
        "For a moment, they faced off against each other in front of the bridge, their backs illuminated by the giant main monitor. Man to Man."
        "Shields gritted his teeth."
        "This would be where he would finally defeat his past self... and rewrite the future."
        "He would dirty his hands in the process by murdering Chigara... And turn Asaga into her murderer... But it was a small price to pay..."
        "The security of the entire galaxy hinged on this moment."
        
        if girl == "Sola":
            "Sola's words echoed in his mind."
            sol "A leader... must bear the weight of his decisions. No matter the burden."
            kay "(I'll... live with this...)"
            kay "(I... have to...!)"
        
    if girl == "Ava":
        kayo "...FIRE ON-"
        "At that moment, Ava broke free of the marines and head butted the other Shields' gut."
        $dshow(11100)
        ava "HOLD YOUR FIRE!!!"
        ava "The captain's gone insane! As executive officer, I am taking command!"
        kayo "SILENCE! You will obey me! I am the ship's captain!"
        $dshow(13100)
        ava "A captain corrupted by an enemy spy! You are no longer worthy of this ship!"
        ava "Whatever lies the Chief's fed you... You must snap out of it!"
        kayo "NO! At this rate Chigara will--"
        "The marines could only dart their eyes from the captain and the commander of the ship, at a complete loss as to whose order to obey, as the two of them struggled on the floor."

    "The Black Jack sailed past the Bianca, the past now altered."
    show asagacockpit4 with dissolve
    asa "HIIYYEEAAHHH!!!!"
    show icaricockpit with dissolve
    ica "Captain, what the hell's going on!?!?"
    ica "A-Asaga's putting way too much stress on the Black Jack's engines!! It's like she's gone insane!!!!"
    ica "At this rate---!!!"
    hide icaricockpit with dissolve
    
    play music "Music/Camino.ogg" fadeout 1.5
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    
    "Suddenly, two of the Black Jack's tail thrusters exploded. Somehow, Asaga managed to maintain the Black Jack's course, sending it spiraling towards the Liberty."
    
    hide asagacockpit4 with dissolve
    
    kay "(W-what...!?)"
    kay "(Oh no.......!!!)"
    "A realization dawned on Shields."
    "From this point on... He had no idea how events were going to unfold himself!!!"
    "Just... what was going on!?!?"
    
    show asagacockpit4 with dissolve
    asa "Hahahaha... HAAHAHAHA!!"
    asa "Chigara..."
    asa "We're... both going to die... TOGETHER!!!"
    hide asagacockpit4 with dissolve
    "Shields' blood went cold."
    kay "No... No...!!"
    kay "(This... isn't what I thought would happen!!)"
    
    if girl == "Sola":
        kayo "...FIRE ON THE BLACK JACK!!!"
        "Shields could only watch as the Sunrider's trinities charged."
        "In just a fraction of a second, the Black Jack would be..."
        "Suddenly, the Seraphim appeared from out of nowhere."
        show solacockpit2 with dissolve
        sol "Captain..."
        sol "I shall--"
        "The Sunrider's trinities fired, but the Seraphim moved precisely between the Black Jack and the Sunrider."
        "The laser beam tore the Seraphim in half."
        hide solacockpit2
        show solacockpit3
        with dissolve
        sol "I..."
        sol "love---"
        
        play sound "sound/explosion4.ogg"
        
        show white with dissolve
        hide white
        hide solacockpit3
        with dissolve
        "The Seraphim exploded. Sola vanished from the Sunrider's screen."
        "Simultaneously, the Black Jack collided into the Liberty."
        
    show asagacockpit5 with dissolve
    asa "Captain... I've done it---"
    asa "I... loved you..."
    asa "This... is for the best. Now everyone will be safe...!"
    
    play sound "sound/explosion4.ogg"
    
    show white with dissolve
    hide white
    hide asagacockpit5
    with dissolve
    
    if girl == "Sola":
        
        play music "Music/Camino.ogg" fadeout 1.5

        "Shields collapsed to his knees as both the Black Jack and the Liberty exploded."
        "Three massive explosions surrounded the ship."
        "Three deaths."
        "Three lives that Shields had just sent to their deaths."
        "He wanted to scream, but nothing emerged from his throat."
        "Instead, he was filled with the overwhelming desire to die himself."
        "He would... never be able to live with this burden... No matter what he had accomplished today... He had suffered a catastrophic defeat..."
        kay "No..........."
        kay "What.... have I... done.......!?"
        scene white with Dissolve(4)
        "His world turned to white."
        "The timeline had been rewritten. A time paradox now triggered, the entire universe collapsed..."
        "But the new universe which would be born in its place... was only filled with different sorrows for Shields."
        "In the end..."
        "He had only managed to trade one tragic universe for another."
        
    if girl == "Ava":
        
        "Shields collapsed to his knees as the Black Jack collided into the Liberty, vaporizing both ryders in a massive fireball."
        kay "No... Asa... ga...!!!"
        "The marines finally snapped out of their confusion and rushed to detain Shields and Ava. But it was already too late."
        "The timeline had already been rewritten. A time paradox now triggered, the entire universe collapsed."
        scene white with Dissolve(4)
        "Shields looked at the twisted debris of the Black Jack on the main screen as the world faded to white."
        kay "I... didn't.. mean to kill you too..."
        kay "I'm sorry..."
        kay "But... The galaxy is saved now."
        kay "You... saved everyone... even though you had no idea..."
        "In the end, he had decided he would sacrifice the lives of his family to fulfill his mission. And this was the logical outcome of that decision."
        "He... would simply have to live with the knowledge that he had sent Asaga and Chigara to their deaths."
        "Shields hung his head and closed his eyes as he faded into nothingness."
        kay "(This is the end... It's... finally over...)"
        kay "(This is the price we paid for peace...)"

    call dlc_credits
    
    if girl == "Sola":
        #Park
        scene bg park with dissolve

        "Who knew how many years had passed since that day..."
        "In the universe which emerged, Shields had discovered that the Chief Engineer of the Sunrider was a Prototype sleeper agent and embarked on a secret mission to stop her. Unfortunately, in their efforts to thwart her mission, Asaga and Sola tragically lost their lives."
        "Following the death of Chigara, Fontana managed to regain control of his ships in time thanks to Shields' early discovery of the Trojan virus."
        "Together, the Combined Fleet and the forces loyal to Fontana defeated the remaining PACT loyalist forces and successfully liberated Cera. Instead of Chigara, it was Shields who received a medal for thwarting her plot to assassinate the Alliance leadership."
        "However... the only thing which mattered to Shields were the deaths of Sola and Asaga."
        "The last time anyone saw him was at their state memorial services. After that, he vanished, never to be seen again..."

        "... ... ..."
        "Shields sat at his usual spot at the Cera National Park."
        "He was now merely a homeless veteran from the Neutral Rim War. Nobody remembered his name any more. In fact, people merely adverted their eyes as they passed him at the park. Hardly surprising, as his face was now wrinkled with alcoholism, and his hair was matted and long. He looked a full three decades older than his actual age."
        "He looked on, to the pond..."
        "Peace... had been won... but at such a tremendous cost..."
        "Everyone milled about, completely oblivious to the sacrifice which had to be paid to bring about this peace..."
        "Suddenly, anger began to twist his heart."
        "They all took this for granted. They had no idea what everyone went through to win the war!"
        "He took deep breathes. No. He mustn't get angry again..."
        "The local police force was already well acquainted with him, and had to remove him from the park on a number of prior occasions..."
        "Instead, he took another swig of his vodka..."
        "This was the only happiness he had left in the world..."
        "Shields continued to drink, until the depressing world faded away..."
        "... ... ..."
        "He kept drinking... and drinking..."
        $dshow(71000)
        "Until Sola finally appeared beside him again..."
        sol "Kayto..."
        sol "You mustn't drink so much..."
        sol "After all, you're the hero of Cera..."
        "Shields spoke in ragged sobs."
        kay "No... I'm not the hero!!!"
        kay "I failed...! I failed everyone!!!"
        $dshow(70322,blush=True)
        sol "Shhh..."
        "He felt Sola's warm embrace."
        $dshow(70322,blush=True)
        sol "You... will always be a hero in my eyes."
        sol "Captain. I am proud of you..."
        kay "Sola...!!!"
        "Shields wrapped his arms around her and sobbed into her chest."
        "At last... he was with her again..."
        "... ... ..."
        "The passerby's all averted their eyes as Shields continued to sob and rave to himself, drowning his sorrows away with nothing but more alcohol..."

        ##WORST SOLA END: "WHAT HAVE I DONE"
        $persistent.unlocked_endings["SOLA WORST END: WHAT HAVE I DONE"] = True
        $chivo_process('Sola Worst Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolve
        show screen worst_end
        #show expression Text("WORST SOLA END:\nWHAT HAVE I DONE",yalign=0.5,size=90,color="fff")
        pause 3
        $dshow(34311)
        cla "Aaah, you sure bungled this one up... Good going, \"hero!\" you managed to avert the massacre, but lost half your pilots in the process!"
        $dshow(34110)
        cla "This sure makes the end of Liberation Day look pretty tame in comparison, eehh..."
        $dshow(34200)
        cla "Well, put those tissues away because you still have a future to save!"

        if backup_comm == False:
            
            $dshow(32110)
            cla "All this happened because you couldn't convince the other Kayto that Chigara was a Prototype in time."
            cla "Try again, and this time, confront the other Kayto Shields with the holo you got from sickbay!"
            
        if backup_comm == True:
            
            $dshow(32110)
            cla "All this happened because you decided to use Asaga to kill Chigara."
            cla "Try again, and this time, see what happens if you choose to escape the Sunrider with Sola!"
        $renpy.full_restart()
        
    if girl == "Ava":
        
        scene bg shrine with dissolve #grave/memorial background? no? okay.
        
        play music "Music/Colors_sad.ogg" fadeout 1.5
        
        $dshow(12322,xpos=0.5)
        "Shields and Ava stood in front of Asaga's grave."
        "While a more grand memorial was constructed back at Ryuvia Prime, the two of them had decided to make a small shrine of their own, beside the resting places of their families."
        "Shields knelt down and placed a package of the spiciest curry he could find on the planet in front of Asaga's alter."
        kay "Asaga..."
        kay "It's been two years since we liberated Cera..."
        kay "Everything happened the way you said... Chigara really was a spy. I... should have listened to you sooner..."
        kay "If I had done that... then you would still be alive today."
        "In the universe which emerged from Shields' mission through time, Shields had chosen to believe Ava's suspicions that Chigara was a Prototype. While they worked together to thwart the Prototypes' plan to commit a mass assassination after the battle, Asaga had endeavored to stop Chigara on her own."
        "In the end, Asaga collided the Black Jack into the Liberty during the battle, killing both of them. Thanks to Shields warning Fontana about the virus prior to the battle, the Combined Fleet and the allied PACT Fleet then managed to defeat the Nightmare Ascendant, upon which the remaining PACT loyalist forces unconditionally surrendered."
        "Newly instated Veniczar S. Fontana declared his intent to sign a peace treaty with the Solar Alliance, wherein PACT gave up all military claim to the Neutral Rim, bringing an end to the war."
        "Ultimately, they lived in a mostly happy future, where the billions of lives which would have been lost had the massacre took place were spared."
        "However, the guilt of sending Asaga to kill Chigara would weigh on Shields' heart for the rest of his life."
        kay "(In the end... I used Asaga to murder her best friend... Who in turn was simply being mind controlled by the Prototypes... Neither of them deserved their fates...)"
        kay "(This peace was won... with their blood.)"
        "As he stared at Asaga's tombstone, Shields wished with all his heart that it had been his blood which had paid for their victory. In the end, his heart was ravaged with regret."
        kay "I... should have been the one to die. It was my responsibility."
        kay "I was a coward. I sent my pilots to die, when preventing the massacre was my mission. Not Asaga's."
        ava "Ahem..."
        "Ava knelt down beside him."
        $dshow(12022)
        ava "Kayto..."
        ava "Her death saved the lives of Admiral Grey as well as a dozen other Alliance officials. And even that  pales in comparison to the billions she saved by preventing an all-out war between the Alliance and PACT."
        ava "I could not imagine a better hero's death than that."
        ava "In the end... I think she would be proud. She will always be remembered as the savior the galaxy."
        $dshow(12222)
        kay "(No... The real reason why she died... Wasn't that...)"
        kay "(It was because... I never returned her feelings.)"
        "Indeed, he was haunted by the guilt of having had ignored Asaga's affections to the very moment of her death."
        "It was a truth which only Shields knew. Asaga had not died a hero's death meaning to sacrifice her life for the galaxy. She had died in sorrow, her mind torn apart by her awakening, and her heart broken from her unrequited love."
        "But Shields would never tell anyone else the truth."
        "Instead, he would take it to his grave, so that Asaga would forever live on, larger than life, as a mythic war hero."
        "That was the only thing he could do for her now."
        
        play music "Music/Destinys_Path.ogg" fadeout 1.5
        
        "He made his decision."
        "He would keep marching forward. That would be his punishment for sending two of his pilots to their deaths."
        kay "No matter what... We'll keep living."
        kay "Regrets are here to make us stronger."
        kay "In the end... We can't redo our past."
        
        $dshow(14000)
        
        "He stood and saluted to Asaga's grave. Ava joined in with a crisp salute of her own."
        "Shields faced Ava."
        kay "The Sunrider sets port tomorrow at 0800 hours."
        kay "Command's received reports from the Alliance that entire colonies have begun to vanish near the Mnemosyne Abyss. We are to join the Alliance task group and investigate."
        kay "Let's move out."
        $dshow(14100)
        ava "Sir! I once again look forward to being your XO on this new voyage."
        "Shields left the grave yard with Ava behind him."
        "His mission was not yet over."
        "With that, Captain Kayto Shields and Commander Ava Crescentia returned to space..."

        #NORMAL AVA END: "MAIDEN'S SUICIDE"
        $persistent.unlocked_endings["AVA NORMAL END: MAIDEN’S SUICIDE"] = True
        $chivo_process('Ava Normal Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolve
        show screen normal_end
        #show expression Text("NORMAL AVA END:\nMAIDEN'S SUICIDE",yalign=0.5,size=90,color="fff")
        pause 3
        $dshow(34110)
        cla "Well... You managed to prevent the massacre, but both Asaga and Chigara ended up dead."
        $dshow(34200)
        cla "Aah, and it doesn't look like you managed to score with your childhood friend either. Teehee, too bad, captain!"
        $dshow(34000)
        cla "If you're feeling too lonely, I, Claude Trilleo, shall more than make up for your kuudere XO! That is, if you can find my ending... Huufufufu..."
        
        if backup_comm == True:
            $dshow(32210)
            cla "Things went wrong this time because you fell for Alice's trap and the ship lost power during Chigara's kidnapping."
            cla "Try again, and this time, find a way to interrupt Alice before she takes over Chigara's body!"
        if backup_comm == False:
            $dshow(32310)
            cla "All this happened because you couldn't convince the other Kayto that Chigara was a Prototype."
            cla "Try again, and this time, confront the other Kayto Shields with the holo you got from sickbay!"
        $renpy.full_restart()
        
label officeftlfontana:
    
    ##SNEAKING INTO KAYTO'S OFFICE TO CONTACT FONTANA
    
    $ backup_comm = False
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5

    #Hallway
    $reset_sprites()
    scene bg hallway with dissolve
    
    #ffs this is getting complicated
    if girl != "Icari":
        $dshow(34200,xpos=0.2)
        if girl=="Ava": #only ava and claude with Kayto
            $dshow(13000,xpos=0.4)
            "The two of them climbed out of the service tunnel and dropped down near the captain's office."
        else: # girl, ava and claude
            if girl=="Asaga":
                $dshow(30,xpos=0.5)
            if girl=="Sola":
                $dshow(70221,xpos=0.5)
            $dshow(13000,xpos=0.8)
            "The trio climbed out of the service tunnel and dropped down near the captain's office."
        
    if girl == "Icari": #only Kayto and Icari
        $dshow(41111)
        "Icari and Shields climbed out of a service tunnel and dropped down near the captain's office."

    "As expected, a pair of marines stood in front of their destination, rifles held at the ready."
    kay "We're going to have to figure out a way to get them out of there."
    
    if girl != "Icari":
        $dshow(11300)
        ava "It won't be long now until they figure out you've escaped..."
        $dshow(13210)
        ava "For now, I can do this..."
        "Ava pulled out her holo and used her command credentials to create a false sighting of intruders in the sickbay."
        "The guards immediately heard the alert and ran opposite down the hall."
        kay "Ah, nice... I guess it pays to have the commander on your side."
        ava "Let's move."
        
    if girl == "Icari":
        ica "It won't be long now until they figure out you've escaped..."
        $dshow(41411)
        ica "For now, I can do this..."
        "Icari pulled out her holo and hacked into the Sunrider's security information network in an instant."
        ica "Cracking the system's a cinch if you know all the backdoors..."
        $dshow(41011)
        ica "And I'm the one who built this system so..."
        "Icari created an alert on the network that intruders had been sighted in the sickbay."
        kay "Ah, nice... I guess it pays to have the chief of security on your side."
        ica "Let's go."

    #Office
    scene bg office with dissolve
    if girl != "Icari":
        $dshow(34200,xpos=0.2)
        if girl=="ava":
            $dshow(13000,xpos=0.4)
        else:
            if girl=="Asaga":
                $dshow(30,xpos=0.4)
            if girl=="Sola":
                $dshow(70221,xpos=0.4)
            $dshow(13000,xpos=0.6)
    else:
        $dshow(41411,xpos=0.4)
    
    "Shields breathed in relief as he entered his office."
    kay "(But just because I'm home doesn't mean I can afford to relax!)"
    "He ran to his desk and activated the FTL comm. He put in a request to contact Fontana, on board the PACT Assault Carrier Vae Victus."

    play sound "sound/beep3.ogg"

    "The transmission kept beeping, waiting for a response."
    "Shields tapped his desk in impatience as the beeps continued."
    kay "(Come on you blasted pretty boy, what the hell are you doing!?)"
    kay "(Pick up the damned phone!!!)"
    "Shields' chest felt as if it was going to burst as the transmission kept beeping."
    kay "What the hell is taking so long, Fontana!!"
    kay "Taking a bath!? Preening in front of the mirror!? What!?"
    kay "Don't tell me it takes a full hour for you to get dressed and groomed for a goddamn phone call!"
    kay "Y-you goddamn... girly boy... bastard!"
    show fontana with wipeup:
        xpos 0.85
    "Just as Shields uttered those words, Fontana's face appeared above his desk. Or maybe more like just *before* he uttered those words."
    "Fontana stared at Shields with a decidedly annoyed look on his face."
    hide fontana with wipedown
    "He then cut the transmission."
    kay "Shit, shit, shit, shit!!"

    play sound "sound/beep3.ogg"

    "Shields furiously tapped the button to resend the transmission request. Finally, Fontana appeared once more."
    show fontana with wipeup:
        xpos 0.85
    fon "WHAT IS IT, SHIELDS!?"
    fon "Surely, you did not call me in the depths of the night merely to comment about my face!"
    kay "No, no, no!"
    kay "Listen to me, Fontana! This is goddamn important!"
    kay "Your ships have been--"
    "Just then, he heard the door to his office open."
    if girl == 'Icari':
        $dshow(41112)
    else:
        $dshow(34310)
        $dshow(13301)
        if girl == 'Sola':
            $dshow(70110)
        if girl == 'Asaga':
            $dshow(534)
    "A lone marine wandered in."
    kay "S-shi--!"
    kay "Fontana, duck!"
    fon "W-wha--!?"

    if girl != "Icari":
        "Shields and his co-conspirators all dived behind his desk. Fontana instinctively ducked down as well upon seeing everyone react the same way."
    if girl == "Icari":
        $dshow(41111)
        "Shields and Icari dived behind his desk. Fontana instinctively ducked down as well upon seeing everyone react the same way."
    
    "Fontana and Shields grimaced when they realized they were practically sitting on top of each other, Fontana's hologram partially merged with Shields' body."
    if girl!='Icari':
        $dshow(12022)
        $dshow(34210)
        "Ava couldn't help but notice their compromising position."
        ava "Ah..."
    fon "A-are you making a-"
    kay "Shhh!!!"
    kay "Quiieett...!"
    kay "Listen, your ships have been hacked with a Prototype virus! Tomorrow, they'll use it to assume full control of your ships and attack the Combined Fleet! You have to do everything in your power to undo the virus!"
    fon "W-what!? Shields, if you speak these words in jest-"
    kay "I'm not joking! But I've got to go!"
    kay "Do it! Or else we're all going to die tomorrow!"
    hide fontana with wipedown
    "With that, Shields cut the transmission."
    kay "(Well, that went about as bad as it possibly could...)"
    kay "(Let's hope he doesn't just brush it off as a joke... No, a man like Fontana would be far too careful to just blow off a warning like that.)"
    
    if girl != "Icari":
        $dshow(13310)
        ava "Kayto, one bogie, coming our way."
        kay "Just one? I think we can take him. Just me and Ava."
        $tempgirl = 'Ava'
    if girl == "Icari":
        $dshow(41211)
        ica "Cap, one bogie, coming our way."
        kay "Just one? I think we can take him."
        $tempgirl = 'Icari'
        
    kay "Okay... On the count of three..."
    kay "One... two..."
    kay "Three!"
    
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    
    "The two of them leaped over the desk at the same time, sending a pile of unfinished paperwork into the air. Unfortunately, a rogue sheet of paperwork landed right in front of Shields' face and obscured his vision."
    kay "Shit!"
    
    play sound "sound/punch.ogg"
    show layer master at tr_xshake
    
    "The marine tossed [tempgirl] aside and raised his rifle simultaneously as Shields tore the sheet of paper from his face and lunged for him."
    "They collided and fell to the floor. Shields immediately put his hand over the marine's mouth and tried to strangle him. Unfortunately, with a swift knee to Shields' gut, the marine managed to regain the upper hand."
    
    play sound "sound/hit.ogg"
    show layer master at tr_xshake
    
    "Just as the marine raised his gun to finish Shields off, [girl] appeared behind the marine and smashed his head in with Shields' prized teapot."
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5

    if girl == "Asaga":
        $dshow(2120)
        asa "Gyaah!!"
    if girl == "Sola":
        $dshow(70423)
        sol "Gyaah!!"
    if girl == "Icari":
        $dshow(41211)
        ica "Gyaah!!"
    if girl == "Ava":
        $dshow(13110)
        ava "Gyaah!!"

    kay "Guck!!"
    "He cringed, expecting his prized heirloom to now be in a million pieces."
    "To his utter surprise, the teapot remained completely unharmed, and judging from the unconscious marine, apparently hit harder than reinforced steel."
    kay "(Wait a minute... Chigara reinforced that pot for me...)"
    kay "(Damn... That girl really must have done something incredible to it for it to still be in one piece after being smashed up against someone's skull like that... I wonder if it's pretty much indestructible...)"
    "Still, Shields took the teapot away from [girl] and returned it to his shelf."
    kay "Be... careful with that."
    
    if girl == "Asaga":
        $dshow(13)
        asa "Huh..."
    if girl == "Sola":
        $dshow(70113)
        sol "I'm sorry."
    if girl == "Icari":
        $dshow(40223)
        ica "Uhh... All right."
    if girl == "Ava":
        $dshow(12314)
        ava "Right."
        
    if girl != "Icari":

        $dshow(10020)
        "Ava looked around in dismay at the mountain of paperwork now scattered around Shields' desk."
        ava "Sigh..."
        kay "Get that look off your face. I came this close today to being killed thanks to paperwork."
        kay "See? Told you this stuff was deadly."
        ava "Only because you allow it to accumulate."
        kay "Ah come on, we have bigger things to worry about!"

    "They ran out of the office before any more marines could show up."
    
    if girl == "Icari":
        jump confrontationwithfate
    
    if killchigara == True:
        jump gettingclaudetobianca
        
    if killchigara == False:
        jump confrontationwithfate

label gettingclaudetobianca:

    #IF CHOSE TO USE ASAGA TO KILL CHIGARA
    stop music fadeout 1.0

    #Tunnels "T-minus 44 hours before the Liberation Day Massacre, 8 hours until Chigara enters the mind stream"
    scene black with dissolve
    
    play sound "sound/drum.ogg"

    show expression Text(_("T-minus 44 hours before the Liberation Day Massacre, 8 hours until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene bg tunnel with dissolve
    
    if girl != "Icari":
        $dshow(34210,xpos=0.2)
        if girl=="Ava": 
            $dshow(13000,xpos=0.4)
        else:
            if girl=="Asaga":
                $dshow(30,xpos=0.4)
            if girl=="Sola":
                $dshow(70221,xpos=0.4)
            $dshow(13000,xpos=0.6)
    else:
        $dshow(41411,xpos=0.4)
        
    "They ran out the hallway and made a beeline back into the maintenance tunnels."
    kay "Okay, we took care of the transmission. Now all we've got to do is put Chigara out of commission."
    kay "We need to get Claude into the Bianca for the coming battle. Any ideas how we're going to do that?"
    $dshow(34010)
    cla "Mah, I'm sure I could figure something out. The Claude of this timeline has still chosen to play the role of the buffoon doctor. Once I take off on the Bianca, I don't think she'll do anything drastic like rewind time..."
    cla "Drop me off at the hangar, and I'll hide inside the Bianca until the sortie order comes."
    kay "All right. Security's still on high alert. Be careful."
    $dshow(36200)
    cla "Roger!"
    "They crawled through the tunnels once more and made their way down to Deck 2..."

    #Hangar
    scene bg tunnel with dissolve

    if girl != "Icari":
        $dshow(34210,xpos=0.2)
        if girl=="Ava": 
            $dshow(13000,xpos=0.5)
        else:
            if girl=="Asaga":
                $dshow(30,xpos=0.7)
            if girl=="Sola":
                $dshow(70221,xpos=0.7)
            $dshow(13000,xpos=0.5)
    else:
        $dshow(41411,xpos=0.5)
        
    "Shields poked his head out from the maintenance gate and checked that the coast was clear."
    kay "All right, let's go!"
    
    scene bg hangar with dissolve
    
    "They descended onto the catwalk and ran towards the Bianca."
    "Shields gulped. Now that Claude was going to be stuck inside the Bianca, the remainder of this mission would now be entirely in his hands."
    kay "(There'll be no more second chances from this point on...)"
    kay "(Claude... We're... counting on you!)"
    
    play music "Music/Danger.ogg" fadeout 1.5
    play sound "sound/warning.ogg"
    
    "Just as he finished those thoughts, the alarm rang overhead."
    "PA" "Warning! Intruder detected!" #don't think this exists yet
    kay "Shit!"
    "Shields covered his eyes as a spotlight fell on their position. The marines patrolling the floor of the hangar rushed up the catwalk."
    kay "Come on, let's go! Move!"
    
    if girl == "Sola":
    
        $dshow(70020)
        sol "Tsch!"
        "Sola drew her pistol and took aim."
        kay "Sola, non-lethals only!"
        sol "Understood."
        
        play sound "sound/heartbeat.ogg"
        $dshow("sola armhold neutral zawakennarrow mad")
        
        "Sola's eye glowed blue as her powers activated."
        "The marines split into two groups in an effort to surround them. One group rushed forward across an elevating bridge used to load pilots onto their ryders, while the other group continued on the catwalk running along the wall of the hangar."
        
        play sound "sound/pulse2.ogg"
        
        "Sola shot her pistol and hit the button to raise the bridge as the marines were running across. They fell to the ground as the bridge suddenly lurched upwards, towards the Phoenix's cockpit."
        
        play sound "sound/pulse2.ogg"
        
        "With another shot, she pushed forward a control lever, moving a ryder rifle attached to cables hanging from ceiling rails up against the wall, temporarily blocking off the catwalk behind them."
        kay "Good shot!"
        $dshow("sola armhold smile zawakennarrow mad")
        sol "Y-yes..."
        
        play sound "sound/pulse1.ogg"
        
        "Their success was short lived, when stun rounds peppered their position. Another group of marines opened fire below them from the floor of the hangar."
        "They ducked down, sparks bouncing off the steel rails all around them."
        "Shields could feel his skin tingling as electric currents passed through the catwalk, through his body."
        kay "Come on! The Bianca's -"
        
        play sound "sound/pulse1.ogg"
        
        "Behind them, the hangar crew managed to return the bridge to the proper position and move the rifle out of the way. More rounds pelted their position."
        "The group ducked down, and sprinted towards the Bianca with all their might."
        
        play sound "sound/laser1.ogg"
        
        $dshow(70403)
        sol "A-ah!!"
        "Shields spun around to see Sola get hit squarely in the back. She fell to the floor in a flash of electricity, her body convulsing."
        kay "SOLA!!!"
        "He looked forward, where the Bianca was waiting... And behind him, where Sola was writhing in pain with a squad of marines approaching..."
        
        $ menu_choices = [
                    ["Get Claude into the Bianca.","getclaudebianca","Hacer que Claude entre al Bianca."],
                    ["Rescue Sola.","rescuesola","Rescatar a Sola."],
                    ]
        show screen decision
        pause
        
    if girl == "Ava":
        
        #AVA
        kay "Uhh... Claude! Isn't there anything you can do!?"
        $dshow(34111)
        cla "Sorry, captain! But you know the rules!"
        kay "Argh!"
        "He drew his pistol."
        "The marines split into two groups in an effort to surround them. One group rushed forward across an elevating bridge used to load pilots onto their ryders, while the other group continued on the catwalk running along the wall of the hangar."
        "Just then, Ava grabbed hold of him and threw him to the ground."
        $dshow(13301)
        ava "Sorry!"
        kay "What the--"
        ava "Doctor, use this chance to escape!"
        $dshow(34310)
        cla "U-understood!"
        
        play sound "sound/guncock.ogg"
        
        "She tore the pistol from his grasp and held it to his head."
        ava "I've captured the imposter!"
        "Claude sprinted towards the nearest maintenance shaft. Unfortunately, she realized too late that the shaft was actually nothing more than an oversized air duct."
        $dshow(34101)
        cla "H-huu!!"
        "She grabbed a nearby blow torch and burned the vent open and tried to squeeze herself in. Unfortunately, she proved too top heavy to fit through the gate."
        $dshow(34311)
        cla "E-eeeh!! I can't fit, captain!!"
        kay "Suck your boobs in, you idiot!"
        "Shields looked in panic as marines surrounded their position."
        $dshow(34301)
        cla "I knew I shoulda gone on a diet!!!"
        hide claude with dissolve
        "Claude squeezed her boobs flat and managed to wiggle through the gate. She vanished into darkness as she crawled deeper into the air shaft."
        "Ava led Shields down the catwalk and to the floor of the hangar at gunpoint."
        $dshow(10010)
        ava "Tsch..."
        kay "Don't worry... We'll... just have to count on Claude pulling through."
        "The marines handcuffed Shields as Ava turned him in."
        
        play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5
        
        show kayto with dissolve:
            xpos 0.2
        "A familiar face walked into the hangar." #always with the familiar face
        kayo "End of the line, Prototype. Commander, you damn well have a good explanation as to what you were doing with him... And how he escaped the brig." #always so quick to arrive
        $dshow(14000)
        ava "Captain!"
        "Despite her cool exterior, Shields knew that Ava was currently racking her brain for a logical explanation for her actions."
        "Before she could think of one, more bad news appeared."
        $dshow(21121,xpos=0.8)
        chi "Umm... It appears someone used the commander's security credentials to unlock the imposter's cell..."
        $dshow(21123)
        chi "O-of course, I am not accusing the commander of setting the prisoner free... but..."
        kayo "... ... ..."
        $dshow(10320)
        ava "Captain. The Chief speaks the truth."
        kay "(Shit... So she couldn't think of anything...)"
        ava "It was I who set the other Kayto Shields free. In fact, I believe his words are the truth, and it is the Chief Engineer who is the true spy."
        ava "You must revoke her security clearance and detain her. Or else she may very well disable this entire ship right now."
        kayo "I don't know what you're trying to pull here, Prototype... But to think you've actually managed to turn my own executive officer again me..."
        kayo "Commander... You are effectively relieved of your rank and your duties. You are to be confined for the duration of this operation."
        $dshow(10000)
        kayo "Take both of them in boys."
        kay "Shit...!!"
        kay "(I've... got to do something drastic!)"
        kay "All right... I admit it! I really am a Prototype! You've... got me!"
        kay "But I'm willing to talk! I know everything they're planning! You'll need my help to win this battle!"
        kayo "Oh?"
        kayo "We'll see about that."
        play sound "sound/laser1.ogg"    
        "With that, a marine shot him with a stun round."
        scene white with Dissolve(2)
        "Shields' world faded to white as fifty thousand volts of alternating currents coursed through his muscles, sending him tumbling to the ground..."
        
        jump endgame_asagakillschigara

label getclaudebianca:
    
    $ rescue_sola = False
    
    #Get Claude into the Bianca.
    kay "(I... have to complete my mission!)"
    kay "(Claude can figure something out once she's inside the Bianca! For now, all we can do is just push forward!)"
    kay "(Sola... I'm sorry...)"
    hide sola with dissolve
    "Shields tore his eyes away from her and ran towards the Bianca."

    jump reachbianca

label rescuesola:
    
    $ rescue_sola = True

    #Rescue Sola
    kay "(It's too late to carry out our mission now that we've been busted anyways!)"
    kay "(I've... just got to rescue Sola!)"
    "Shields abandoned the rest of his compatriots and ran to Sola."
    "Electric currents coursed through her body, the shock bullet embedded inside her flesh. Of course, the rounds were designed to dig into the flesh, but not penetrate so deeply as to cause serious injury."
    "He knew that if he were to touch her now, he would be shocked by the electric currents too. But he didn't have a choice!"
    "With a cry, he grabbed Sola and slung her across his shoulders, electricity coursing through his body."
    kay "G-GARGGHH!!!"
    "While nowhere as debilitating as it would have been if the round been embedded inside his own flesh, Shields's body burned with agony as the secondary currents from Sola's body ran through him."
    "He fought through the pain and tried to catch up with the rest of the team."
    
    jump reachbianca

label reachbianca:

    scene bg hangar with horizontalwipe
    show mook as mook1:
        xpos -0.25
    show mook as mook2:
        xpos 0.15
    show mook as mook3:
        xpos 0.55
    with dissolve
    "Just as the team reached the Bianca's maintenance bay, they were completely surrounded by a circle of over thirty marines. They came at Shields, rifles at the ready."    
    
    if rescue_sola == False:
        "Shields looked around desperately."
    if rescue_sola == True:
        $dshow(70001,xpos=0.33)
        "Shields put Sola down and looked around desperately."

    kay "(Is... this the end...?)"
    kay "(Did I fail...?)"
    "Suddenly, he realized that Claude had vanished once more."
    kay "(Wait a minute... Claude's now nowhere to be found...)"
    kay "(She must have somehow managed to escape again!)"
    kay "(That means she still has another chance to take control of the Bianca...)"
    kay "(I just... need to distract the ship's security long enough for her to do that!)"
    "With that, Shields raised his hands and faced the marines."
    kay "We surrender!"
    kay "Take me to your leader! I'm willing to talk now!"
    mrn "Take him down!"
    
    play sound "sound/laser1.ogg"
    
    "With that, a marine shot him with a stun round."
    scene white with Dissolve(2)
    "Shields' world faded to white as fifty thousand volts of alternating currents coursed through his muscles, sending him tumbling to the ground..."

    play music "Music/Fallen_Angel_Pt1.ogg" fadeout 1.5

    #Hallway -  "T-minus 36 hours before the Liberation Day Massacre, 10 minutes until Chigara enters the mind stream"
    scene black with dissolve

    show expression Text(_("T-minus 36 hours before the Liberation Day Massacre, 10 minutes until Chigara enters the mind stream"),size=40):
        xalign 0.5
        yalign 0.5
    pause
    scene bg hallway with dissolve
    "Shields groggily woke up... He felt himself being dragged along the hallway of the ship..."
    "He looked around, his consciousness still fading in and out..."
    
    jump endgame_asagakillschigara
    
label claude_end:  #secrats!
    
    #IF ICARI ROUTE
    $renpy.save("CLAUDE SECRET END")

    "Just then, he heard Icari's voice on the comm."
    
    play music "Music/Fallen_Angel_Pt3.ogg" fadeout 1.5
    
    show icaricockpit with dissolve
    ica "A-Asaga's gone berserk!!!"
    ica "O-oy, captain!? W-what are we supposed to do!?"
    ica "A-are we actually gonna shoot her down!?"
    hide icaricockpit with dissolve
    kay "(Shit... I almost forgot about this event...)"
    kay "(During the battle, Asaga goes berserk from awakening too many times and tries to kill Chigara...)"
    kay "(But can we use this to our advantage?)"
    kay "(No... We can't use it to take Chigara out on the Liberty... Asaga's attempt ultimately fails when Claude stops her using the Bianca's grav gun.)"
    kay "(But... Icari could use this opportunity to...)"
    kay "(Of course...! This is our chance to disable the Liberty while everyone's distracted by Asaga!)"
    kay "I know what's going on."
    kayo "What's wrong with Asaga!?"
    kay "Temporary insanity, due to mental exhaustion. She's been utilizing too many awakenings during the battle." #damn now I want to make that into a battle mechanic.
    kay "At this rate, she's going to kill Chigara in a fit of jealous paranoia."
    kayo "Tsch... Put me through the Black Jack."
    kayo "Asaga, what's wrong!?"
    show asagacockpit4 with dissolve
    asa "... ... ..."
    asa "I'm sorry captain..."
    asa "But you're being tricked..."
    asa "I'm... doing this for the good of the ship...!!!"
    asa "Chigara.... is the traitor!!!!"
    hide asagacockpit4 with dissolve
    $dshow(13000)
    ava "The Black Jack is on a intercept course for the Liberty!"
    kayo "What...!? E-even you--!?"
    kayo "Asaga, listen to me... I don't know what you've been told... But that's only a filthy lie spread by the Prototypes to get us to doubt each other!"
    kayo "Defend the Liberty! Chigara's the only hope we have to win this battle!"
    show asagacockpit4 with dissolve
    asa "No...! I... I can sense it... Chigara's... definitely...!!"
    asa "I've got to stop her!!!"
    hide asagacockpit4 with dissolve
    ava "The Black Jack has cut the channel!"
    kayo "Shit!"
    kay "Move in the Phoenix to intercept the Black Jack!"
    kayo "I'm in charge here!"
    ica "But he's got a point! Asaga's coming in fast!"
    kayo "Tsch... Do what he says."
    ica "Copy!"
    show solacockpit4 with dissolve
    sol "Captain. I have a lock on the Black Jack's cockpit."
    sol "I shall take full responsibility."
    hide solacockpit4 with dissolve
    kayo "... ... ..."
    "Every single pair of eyes on the bridge focused on the Black Jack as it sped towards the Liberty."
    kay "(This is it... The decisive moment...)"
    show solacockpit4 with dissolve
    sol "I can only maintain a lock for four more seconds..."
    sol "Two..."
    hide solacockpit4 with dissolve
    kay "T-tsch......."
    kay "Pull the t-"
    show bjbiancastop_back with dissolve
    show bjbiancastop_bianca:
        xpos 1.0
        ease 0.5 xpos -0.4
    play sound "sound/chargeup.ogg"
    cla "Hooaaahh!!!"
    "Just like in Shields' timeline, the Bianca maneuvered in front of the Liberty at the very last second and overloaded its grav gun, forming a massive gravity eddy. Caught in the current, the Black Jack spun past the Bianca, almost clipping its shoulder guns against the Bianca."
    play sound1 "sound/explosion1.ogg"
    "Under the massive strain of moving the Black Jack, the Bianca's grav gun exploded in a blossom of blue sparks, causing the entire ryder to lose power. It rotated powerlessly through space."
    asa "E-eaaahh!!!!"
    kayo "W-what the--"
    kayo "C-Claude!? A-Are you all right!?"
    hide bjbiancastop_bianca
    hide bjbiancastop_back
    show claudecockpit2
    with dissolve
    cla "U-ugh... Y-yes, captain..."
    hide claudecockpit2
    show bianca_damaged1
    with dissolve
    cla "N-not so sure 'bout the Bianca though..."
    asa "W-what are you doing!?"
    play music "Music/Love_Theme.ogg" fadeout 1.5
    hide bianca_damaged1
    show claudecockpit3
    with dissolve
    cla "Now you listen to me... And listen to me good..."
    cla "There isn't a girl on board the Sunrider who likes how things turned out...!"
    cla "Especially me! Who's loved the captain more than any of you!"
    cla "J-just how do you think poor Claude feels...? Completely forgotten by everyone!"
    kay "(I remember this entire speech... Poor Claude... Getting gunned down like...)"
    kay "(Oh well. I guess she'll be fine.)"
    
    play music "Music/Danger.ogg" fadeout 1.5
    
    "Just then, an entirely different voice interrupted Claude's big moment."
    
    hide claudecockpit3
    show icaricockpit3
    with dissolve
    ica "Sorry Claude, but I'm gonna have to cut to the chase here..."
    "The Phoenix decloaked, now seconds away from reaching the Liberty."
    kayo "W-WHAT!? Phoenix, what are you--"
    ica "Heh. Sorry 'bout this, cap. But I decided to side with your other version."
    ica "Now, let's get future saved!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Phoenix swooped down with its katana drawn, surgically removing the Liberty's ECM dishes but leaving all of it's other essential systems untouched."
    chi "W-What!?"
    ica "End of the line, Chigara! Or should I say, Prototype!"
    chi "T-Tsch...!"
    
    hide icaricockpit3 with dissolve
    
    kayo "YOU!!"
    "The other Shields grabbed Shields by the scruff of the throat and lifted him off his feet."
    kayo "You planned this!"
    "For a moment, they faced off against each other in front of the bridge, their backs illuminated by the giant main monitor. Man to Man."
    "Shields gritted his teeth."
    kay "It's over! Without the ECM dishes, Chigara won't be able to enter the mindstream!"
    kay "Now look at Chigara."
    kay "This is the reality!"
    kayo "What...!?"
    "Chigara's menacing laughter echoed through the bridge."
    chi "Hufufufu..."
    chi "You did well, Shields..."
    chi "I don't know how you managed to loop through time to get here... But I'm guessing that wanderer had something to do with this..."
    
    play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
    
    show nightmare_approach with dissolve
    "The Nightmare Ascendant appeared beside the Liberty."
    ava "Captain, new transmission! Coming from the Ascendant!"
    kayo "Put it on screen!"
    hide nightmare_approach
    show alice_cockpit1
    with dissolve
    ali "Heh..."
    ali "But it's still too late! Thanks to your Chief shutting down your ship, you couldn't get the warning sent to Fontana's fleet in time!"
    ali "You will all be dead by my hands, long before his ships arrive to save you!"
    
    hide alice_cockpit1 with dissolve
    
    "With both Chigara and Alice now simultaneously on the screen, everyone could see that their lips were synched as they spoke together, their voices intermixed."
    "The other Shields' looked on in horrified disbelief."
    kayo "C-Chigara..."
    kayo "W-what have you done to her...!?"
    ali "Done?"
    ali "She's been under my control ever since she joined the ship!"
    ali "Everything was done so that we could control you. And how easy it was, to convince you that this little doll loved you! Hahaha... We had you eating out of our hands practically your entire voyage!"
    ali "If the wanderer hadn't interfered... Then I would have..."
    kayo "... ... ..."
    "The other Shields' eyes twitched."
    kayo "Then... I've been..."
    kayo "All this time... Everyone else was right..."
    kay "Open your eyes, Shields! I'm... you! From the future! I've come to warn you about Chigara!"
    kayo "... ... ..."
    kayo "Im... possible...!"
    "The other Shields held himself up against the tactical map."
    show alice_cockpit2 with dissolve
    ali "Hahaha! If I can't spark an intergalactic war, I'll just have to be satisfied with seeing the look on your face when your ship sinks!"
    hide alice_cockpit2
    show nightmare_approach
    
    show nightmare_attack
    
    $ renpy.movie_cutscene("3DCG/nightmareattack.webm",stop_music=False) 
    pause    
    
    "The Nightmare Ascendant's flier drones detached and screamed towards the Sunrider."
    
    hide nightmare_approach
    hide nightmare_attack
    with dissolve
    
    $dshow(13110)
    ava "Captain!"
    kayo "... ... ..."
    
    hide kayto with dissolve
    
    kay "I'm taking command! Return fire!"
    $dshow(13100)
    ava "A-aye aye!"
    kay "Get in contact with Fontana! How much longer until his ships are functional!?"
    scene asagacockpitsurprise_space with dissolve
    asa "H-holy---!"
    
    play sound "sound/Flak.ogg"
    
    "The Black Jack sprang back into action and sprayed fire on the drones as they whizzed past."
    asa "Ya see! Ya see! I told ya guys that Chigara was up to no good!"
    asa "D-didn't think that you guys would actually believe me though..."
    scene icaricockpit3 with dissolve
    ica "Heh, you have our new captain to thank for that."
    ica "Claude, how are things over there!"
    scene claudecockpit2 with dissolve
    cla "O-ooh! I've finished restoring power to the Bianca! But the grav gun's shot though..."
    scene cg_claudecockpit2 with dissolve
    cla "Teeheehee... Aside from that, it looks like I've wandered into something reeaalllyyy interesting..."
    
    scene bg bridge with dissolve
    
    "Shields gripped the tactical map as the Sunrider took fire."
    asa "The Ascendant's defenses are too good! Without Chigara's ECM, nothing we have's gonna get through!"
    
    show fontana with wipeup
    
    fon "Tsch... My ships are still not operational. It could still be another 20 minutes..."
    kay "You're gonna have to hurry it up!"
    
    play sound "sound/explosion4.ogg"
    
    "A nearby Alliance cruiser took a hit through its central tower from a flier drone's laser and began to list towards the Sunrider."
    
    show layer master at tr_xshake
    $dshow("ava handonhip shout narrow angry",xpos=0.75)
    
    ava "Hard to port!!"
    "Everyone braced themselves as the Sunrider narrowly avoided colliding into the crippled cruiser."
    kay "We might all be dead in 10 minutes!"
    "The Sunrider's side thrusters stopped firing, allowing everyone to regain their footing."
    sol "Seraphim locked on. Dispensing fire."
    
    scene alice_cockpit3 with dissolve
    
    ali "Hahaha! Pathetic!"
    
    play sound "sound/Sola Sniper.ogg"
    pause 0.3
    play sound1 "sound/Sword Shing 2.ogg"
    
    "Alice's eyes ignited in a blue fireball as Sola rained down judgment. The Ascendant swung its sword and deflected each of Sola's rounds."
    ali "As long as Sharr Myren's ghost courses through my veins, I am invincible!"
    
    scene solacockpit4 with dissolve
    
    sol "T-tsch... D-defiler...!"
    
    play sound "sound/legion_laser.ogg"
    play sound "sound/mech_boost2.ogg"
    
    "The Ascendant returned fire, suppressing the Seraphim. Sola hit the thrusters, narrowly avoiding getting sliced by particle fire."
    
    scene icaricockpit with dissolve
    
    ica "Hiiyaahh!!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "Icari used the opening to lunge at the Ascendant's reactor cores on its back, but the Ascendant spun and met the Phoenix's katana with its greatsword."
    
    scene alice_cockpit3 with dissolve
    
    ali "Heh!"
    "The Ascendant shoved the Phoenix away as if it was but a child. With another swing, their blades met."
    
    play sound "sound/shatter.ogg"
    
    "Icari's eyes widened when the Phoenix's katana shattered like glass against the Ascendant's blade."
    ica "S-shit!"
    
    play sound "sound/mech_boost2.ogg"
    
    "The Phoenix dived, narrowly avoiding getting sliced in half."
    
    scene kryska_cockpit1 with dissolve
    
    kry "I'm your opponent! Eaaah!!!"
    
    play sound1 "sound/shotgun.ogg"
    pause 0.2
    play sound "sound/shotgun.ogg"
    pause 0.2
    play sound2 "sound/shotgun.ogg"
    
    "The Paladin soared inbound and slugged round after round of black iron from its back mounted cannons."
    ali "Heh..."
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Ascendant spun, dodging the rounds, and then lazily sliced the last round as if to just show off its prowess."
    
    scene icaricockpit with dissolve
    
    ica "We're gonna need options, cap! That thing's not gonna go down easy!"
    
    play sound "sound/mech_boost2.ogg"
    scene asagacockpit7 with dissolve
    
    asa "HIIYAAHH!!!"
    "As if to answer Icari's call, Asaga appeared, both eyes blazing with light."
    asa "You're... not the Sharr!!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Black Jack and the Ascendant met."
    
    scene bg bridge with dissolve
    
    "Shields racked his head for a way to take the Ascendant down."
    kay "(Shit... Last time, I had all of Fontana's ships helping me out...)"
    kay "(The Combined Fleet's already stretched thin as it is against the rest of the PACT Loyalist Fleet...)"
    "The Sunrider's comm crackled to life."
    unp "This is the Cera Underground Resistance! We've got our hands on some gunboats and are ready to assist!"
    kay "The Resistance?"
    "Before he could respond, a swarm of 20 gunboats buzzed past the Sunrider and sprayed fire on the Ascendant."
    
    scene alice_cockpit3 with dissolve
    
    ali "Beh! Mere flies!"
    unp "We'll distract her! Hit her with everything you've got!"
    kay "Load all torpedo tubes!"
    ava "Sir!"
    kay "Everyone, hit the Ascendant with everything you've got!"
    asa "Understood!"
    
    scene white with dissolve
    
    play sound "sound/Flak.ogg"
    
    "All of the Sunrider's ryders loosed ordinance on the Ascendant, revolving in a circle around it."
    "The gunboats strafed the Ascendant, unleashing a torrent of lead as they flew by."
    
    play sound "sound/explosion4.ogg"
    
    "For a moment, the Ascendant was completely enveloped in fire, as round after round of ammo struck it without pause."
    kay "Fire quantum torpedoes!"
    
    play sound "sound/missilelaunch.ogg"
    
    "A pair of torpedoes escaped from the belly of the ship and made their way to the Ascendant. Shields held his breath as they slowly cut through the battlefield."
    
    play sound "sound/quantumtorpedo.ogg"
    
    "Both pairs struck home, blossoming into two micro black holes. Sparks of energy shot from where the Ascendant once stood, as everything nearby was crushed when the warheads detonated."
    kay "Tsch... Did that get it?"
    
    scene nightmare_approach with dissolve
    
    "Shields' hope flickered out when the Ascendant emerged, completely untouched."
    ali "Hahahaha...! You thought your toys would affect the Nightmare Ascendant?"
    kay "Shit!"
    ali "Now... witness despair!"
    
    play sound "sound/missile.ogg"
    
    "The Ascendant's shoulder missile racks opened, spreading a tidal wave of fire from the accursed mech."
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    pause 0.5
    play sound1 "sound/explosion5.ogg"
    pause 0.5
    play sound2 "sound/explosion2.ogg"
    
    "Shields gripped onto the tactical table as the Sunrider shook. The entire space around the ship was transformed into a sea of fire as each missile split into more missiles and detonated."
    "The Ceran gunboats weren't nearly as well armored as the Sunrider. Shields looked on helplessly as all 20 heroic gunboats instantly melted away."
    "Their systems exploded on by one, and they spun wildly out of control and eventually vanished into twisted debris."
    kay "No...!"
    
    scene alice_cockpit3 with dissolve
    
    ali "Hahaha!!"
    
    play sound "sound/legion_laser.ogg"
    
    "The Ascendant fired its particle gun, catching the Seraphim's rifle."
    sol "A-ah!"
    
    play sound "sound/explosion4.ogg"
    
    "The rifle and the Seraphim's backup reactors burst, sending it spiraling out of control."
    sol "U-uggnnhh!!"
    kay "SOLA!!!"
    ali "You've still failed, Shields!"
    ali "All your friends will still die!"
    ali "Because the Nightmare Ascendant is indestructible!"
    
    scene asagacockpit7 with dissolve
    
    asa "Like hell it is--!!"
    "The Black Jack rushed towards the Ascendant."
    
    scene alice_cockpit3 with dissolve
    
    ali "Hahaha!!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Ascendant swung its sword quicker than the human eye could perceive."
    asa "E-eh...?"
    
    play sound "sound/explosion4.ogg"
    
    "Asaga looked on in disbelief as the Black Jack's shoulder particle guns flew away, sliced clean from the ryder's body."
    "Before the Black Jack could move, the Ascendant gripped its head with its clawed gauntlets."
    ali "How does it feel to be defeated, Sharr of Ryuvia?"
    ali "Hahahaha... You will never awaken to the fullest extent I have unless you have tasted true despair...!"
    ali "You couldn't even call me human any more. Hahaha! Actually, I was never human to begin with!"
    ali "I was... a monster from the instant I was born... and that's all that awaits."
    ali "You've tasted it... What lies at the end of your awakenings!"
    asa "S-shut... up...!"
    
    play sound "sound/explosion4.ogg"
    
    "The Ascendant threw the Black Jack away, detaching its head piece in the process."
    asa "E-eaahh!!!"
    "Asaga's cockpit went dark as all of the onboard optics failed."
    asa "No!!!"
    
    scene bg bridge with dissolve
    
    kay "Is... it... really hopeless...?"
    "Just then, a squad of twelve Alliance battleships appeared from all directions, completely surrounding the Ascendant."
    
    show grey with wipeup
    
    adr "I apologize for our late appearance captain... But let my men deal with this... abomination!"
    kay "Admiral--!"
    "Alice only sneered hungrily at the newest entries."
    ali "Useless!!"
    "Swarms of Alliance infantry ryders approached in twelve columns, surrounding the Ascendant."
    ali "Hahaha... HAHAHAHA!!!"
    "The Ascendant's reactors glowed bright red as all three reactors fed maximum power to the particle gun."
    
    play sound "sound/legion_laser.ogg"
    
    "A torrent of crimson death shot from the particle gun, spearing infantry after infantry, the beam never losing strength no matter the distance or number of ryders maimed."
    
    play sound "sound/explosion1.ogg"
    pause 0.2
    play sound1 "sound/explosion2.ogg"
    pause 0.2
    play sound2 "sound/explosion4.ogg"
    
    "The Ascendant swung the gun into an arc, spearing hundreds of enemy ryders, and splitting an Alliance battleship in two halves."
    "Shields stood wordlessly as over a hundred Alliance ryders and a battleship fell in a heart beat."
    
    play sound "sound/cannon.ogg"
    
    "The Machiavellis' opened fire using their main railguns, but the Ascendant nimbly dodged each shot. It was bombed again and again with missiles, but each explosion bounced harmlessly off its armor."
    
    play sound "sound/legion_laser.ogg"
    play sound3 "sound/explosion1.ogg"
    pause 0.2
    play sound1 "sound/explosion2.ogg"
    pause 0.2
    play sound2 "sound/explosion4.ogg"

    "With another swing of its particle gun, a hundred more ryders and two more battleships vanished."
    kay "No..."
    
    play music "Music/Love_Theme.ogg" fadeout 1.5
    scene icaricockpit with dissolve
    
    ica "Hiyyaahh!! Phoenix, rising from the ashes!"
    "The Phoenix launched from the hangar with a new katana and flew to the Ascendant."
    kay "Icari!!!"
    ica "Heh... It's been a wild ride, cap... But someone's gotta save all our asses..."
    ica "HIIYYAAHHH!!!"
    "Sweat poured down Shields' back, drenching his uniform, as Icari made her one woman charge towards the Ascendant."
    "The Phoenix drew both blades as shot towards at maximum speed."
    ali "Heh... This is the end!!!"
    
    play sound "sound/mech_boost2.ogg"
    
    "The Ascendant took off, greatsword in hand, and flew towards the Phoenix at even greater speed."
    "Shields could only stand as the two ryders screamed towards each other, blades at the ready."
    
    scene alice_cockpit3 with dissolve
    
    ali "EEAAHHH!!!!"
    
    scene icaricockpit with dissolve
    
    ica "EEEAAAAAAAHHHHH!!!!"
    ica "One cut...."
    ica "ONE KILL!!!!!"
    
    stop music fadeout 1.5
    play sound "sound/Sword Shing 2.ogg"
    scene white with dissolve
    
    "The two ryders flew past each other, their blades moving quicker than anyone could see."
    "For a moment, silence fell on the battlefield as both ryders came to a stop."
    ali "... ... ..."
    ica "... ... ..."
    
    scene alice_cockpit3 with dissolve
    
    ali "Hufufufu..."
    ali "HHAAAHAHAHAHAHA!!!"
    
    play sound "sound/explosion4.ogg"
    
    "The Phoenix's wing thrusters broke apart and one of its legs exploded."
    ica "A-ARGGHghhhg!!!"
    
    play music "Music/Camino.ogg" fadeout 1.5
    
    "The Ascendant turned around, completely unharmed, and slowly flew towards the Phoenix."
    ali "Now do you see..."
    ali "The Ascendant... is immortal."
    ali "The Ascendant... is... GOD!!!"
    
    play sound "sound/explosion3.ogg"
    
    "It raised its sword to deliver the coup de grace, but was tackled away by the Paladin."
    
    play sound "sound/mech_boost2.ogg"
    scene kryska_cockpit1 with dissolve
    
    kry "HOYAAH!!!"
    ica "S-Soldier boy!!"
    kry "I will not let you harm the mercenary!"
    ica "No... don't...! You'll--!!"
    kry "Heh... A warrior does not fear death when her comrades are in danger!"
    kry "Now face me, worm!"
    "The Paladin banged its rifle against its shield and faced the Ascendant."
    ali "Heh... What's a slow ryder like that gonna do against the Ascendant!!!"
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    
    "The Paladin took cover behind its shield as the Ascendant swung its sword downwards, only to have its shield be split in half."
    ica "No!!!"
    kry "Tsch!!"
    
    play sound "sound/Flak.ogg"
    
    "The Paladin stuck its rifle into where the Ascendant's cockpit block was located and unloaded at point blank range."
    "All it received for its efforts was a kick to its gut after the rifle's rounds bounced harmlessly off the Ascendant's armor."
    ali "Now, say good bye to your friend!"
    "The Ascendant raised its sword over the Paladin."
    kry "Arghh!!"
    ica "KRYSKA!!!"
    
    play sound "sound/explosion3.ogg"
    
    "The Phoenix attempted to fly to the Paladin's aid, but its remaining wing thrusters blew and sputtered to death."
    ica "No.... It... can't end like this..."
    
    scene kryska_cockpit1 with dissolve
    
    kry "Heh... D-don't worry 'bout a thing..."
    ali "Heh. Any last words?"
    kry "A soldier's death... is nothing to be ashamed of..."
    
    scene alice_cockpit3 with dissolve
    
    ali "Good words. As expected from a loyal soldier of the Alliance Fleet."
    ali "Now, met your end!"
    "The Ascendant swung its sword down on the Paladin's cockpit block..."
    
    play sound "sound/shotgun.ogg"
    show layer master at tr_xshake
    
    "But was caught off guard when it was hit with a kinetic slug which bounced off its head."
    "The Ascendant unintentionally gave Kryska a momentary reprieve as it sought to find the source of the insult."
    ali "What? What manner of imbecile dares interrupt--"
    
    scene claudecockpit1 with dissolve
    
    cla "H-huuuu!!"
    "The Bianca stood alone, only a shotgun at its side, its grav gun completely busted."
    ali "Y-you?"
    cla "I..."
    cla "I may be good for nothing but comic relief..."
    cla "But today..."
    cla "Today..."
    cla "CLAUDE will stop you!!!"
    ali "HAHAHAHAHA!!! You?"
    ali "Without your powers, you are nothing!"
    ali "And you can't use them right now, can you?"
    ali "Not without also ending history as we know it!"
    cla "T-t-that may be so!! But... I'll still stop you!"
    
    scene bg bridge with dissolve
    
    kay "... ... ..."
    kay "There's... nothing in our arsenal which can match that... god."
    kay "God... God..."
    kay "G-GOD!!!"
    kay "Psst... Other Claude... Are you there!?"
    
    $dshow("claude salute happy neutral neutral")
    
    "Just then, a second Claude materialized beside Shields."
    cla "Yes~ Interstellar goddess Claude Trilleo at your service..."
    kay "I... uhh... thought you couldn't show yourself in front of your other self."
    
    $dshow("claude boobs happy closed neutral",ypos=1600)
    
    cla "Ah. Sorry. That was actually a lie. Teehee~"
    cla "I just wanted to avoid any situations where I might be forced to use my powers to directly change the timeline..."
    kay "Well... Uhh... I need you to use your powers now."
    kay "That's honestly the only way we're gonna take that Nightmare down!"
    
    $dshow("claude neutral neutral neutral upset")
    
    cla "Mou... Captain..."
    cla "How many times must I warn you?"
    cla "The consequences of recklessly using my powers are too dire for most human brains to even comprehend. Lookie here, I can get away with just one or two universes collapsing if I get someone else to do the dirty work for me, but if I were to directly cause a time paradox using the temporal manipulator..."
    
    $dshow("claude fingerup smile closed upset")
    
    cla "Mah... I guess not even I know what would happen!"
    kay "Look... This is an emergency!"
    kay "If you don't do something... Everyone's going to die here!"
    
    play sound "sound/legion_laser.ogg"
    
    "Just then, the Ascendant shot the Bianca's already damaged grav gun off with its particle gun, toying with it."
    cla "Kyaaahh!!!"
    ali "Hahaha!! I think I'll make your death slow..."
    kay "Look, your other self is gonna die too! Won't that cause problems for you too!?"
    
    $dshow("claude neutral smile closed neutral")
    
    cla "Eh, don't worry too much... I'm sure she'll be fine. A 'lil explosion and  depressurization's kind of old hat by now...!"
    "Shields put his hands on Claude's shoulders."
    kay "Claude... I'm... begging you...!"
    kay "I... can't watch everyone die again!"
    kay "Not when I've come this far...!"
    kay "Please..."
    "He knelt down to his knees and dug his nose into the floor, truly desperate."
    kay "Goddess...!"
    kay "Please... save us from defeat..."
    "He put his hands together in prayer."
    kay "Please... bring... us... victory...!"
    kay "Save... my crew. Save my girls."
    kay "I'll... do... anything!! ANYTHING!!!"
    
    $dshow("claude neutral talk neutral upset")
    
    cla "A-ah... mou..."
    cla "I-if you put it like that... A-ah... I guess..."
    "Claude awkwardly laughed."
    
    $dshow("claude boobs happy closed neutral",ypos=1600)
    
    cla "All right... But I'm actually not the one you need to convince here..."
    cla "It's that one."
    "She pointed towards the other Claude, desperately fighting against the Nightmare Ascendant on the Bianca."
    cla "Open a channel with her... and just tell her this."
    "Claude whispered a few words into Shields' ears."
    kay "(G-GUCK!!! I-IS SHE---!!)"
    
    $dshow("claude fingerup happy closed neutral blush")
    
    cla "Eh-heh... Just say that secret phrase! And then voila! Everyone will be saved!"
    kay "(Holy... shit...)"
    kay "(But to actually do this... T-this could... truly be the end...!)"
    kay "(I... don't have a choice!!! I'M GONNA HAVE TO DO THIS!!!! HIYAAHH!!!!)"
    
    hide claude with dissolve
    
    "Shields put his hand on the console and opened a channel with the Bianca."
    kay "Claude... This is Kayto..."
    
    scene claudecockpit1 with dissolve
    
    cla "E-eh? Captain?"
    cla "I'm s-sorry, I'm kind of busy--"
    kay "I've... got something... really important to tell you..."
    cla "Eh?"
    kay "You've... got... to... defeat... the Nightmare... Ascendant...!!"
    kay "Because when you get back..............."
    
    stop music fadeout 1.5
    show layer master at tr_xshake
    
    kay "WE'RE GONNA FUCK ALL NIGHT LONG!!!!"
    
    scene bg bridge with dissolve
    
    "The entire bridge crew nearly collapsed in dismay."
    
    $dshow("ava handonhip neutral narrow angry")
    
    "Ava faced him while gripping a speakerphone in her hand, in the middle of coordinating damage control efforts."
    
    play sound "sound/punch.ogg"
    
    "The speakerphone shattered in her grip."
    "The protestations of the other girls flooded the channel."
    asa "Hey! What the hell is this, captain!?"
    ica "Y-y-you idiot!!! I can't believe you'd actually make a joke like that right now!!"
    sol "D-disgraceful..."
    kry "Captain, this violates so many protocols--"
    "But soon, another voice flooded out all the protests."
    
    play music "Music/The_Final_Battle.ogg" fadeout 1.5
    
    show white:
        alpha 0
        ease 0.5 alpha 1
        ease 0.5 alpha 0
    
    cla "OOOAAAHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!"
    cla "AS YOU COMMAND... CAPTAIN!!"
    kay "Claude...!!!"
    kay "(She's... GONNA DO IT!!!)"
    
    scene cg_claudecockpit with dissolve
    
    cla "Today's Claude... Is DIFFERENT!!!"
    ali "W-what!? B-but--"
    cla "Teehee. Sorry. But mah man says I'm takin' you out!"
    
    scene alice_cockpit4 with dissolve
    
    ali "T-tsch!"
    "For the first time during the battle, fear appeared in Alice's eyes - fear that she was now facing an opponent far greater than even the Ascendant."
    
    play sound "sound/legion_laser.ogg"
    scene nightmare_fire2 with dissolve
    
    "The Ascendant raised its particle rifle and opened fired on the Bianca. However, the Bianca dematerialized before the particles reached."
    
    play sound "sound/large_warpout.ogg"
    
    "Before anyone even knew what happened, it materialized behind the Ascendant."
    
    play sound "sound/shotgun.ogg"
    pause 0.2
    play sound1 "sound/shotgun.ogg"
    pause 0.2
    play sound2 "sound/shotgun.ogg"
    pause 0.2
    play sound3 "sound/shotgun.ogg"
    
    "Shots rang out from its shotgun quicker than an assault rifle."
    "Everyone stared in disbelief as the shotgun dispensed slug after slug quicker than a mini-gun with no signs of strain or overheating."
    
    scene alice_cockpit4 with dissolve
    
    ali "A-argghh!!!"
    
    play sound "sound/large_warpout.ogg"
    
    "The Ascendant spun and sliced the space where the Bianca occupied with its sword, but it once again vanished and rematerialized, this time in front."
    
    play sound "sound/shotgun.ogg"
    pause 0.2
    play sound1 "sound/shotgun.ogg"
    pause 0.2
    play sound2 "sound/shotgun.ogg"
    pause 0.2
    play sound3 "sound/shotgun.ogg"
        
    "More slugs sprayed from the Bianca's shot gun, in a massive BRRRRTTT."
    "Alice swung the Ascendant's blade around wildly, but from Claude's perspective, the blade moved slower than a sloth. In fact, she was firing her shotgun at its natural pace, but from everyone else's perspective, it appeared as if everything was happening a thousand times quicker."
    ali "G-God or not---!!"
    ali "T-the slugs still cannot penetrate my armor!!"
    
    scene cg_claudecockpit2 with dissolve
    
    cla "Aahh... I hope you're not thinking this is the only thing I can do..."
    
    play sound "sound/large_warpout.ogg"
    
    "Suddenly, a second Bianca appeared. The two of them blinked in and out around the Ascendant, spraying it with lead."
    ali "W-what....!? I-Impo-"
    
    play sound "sound/large_warpout.ogg"
    pause 0.4
    play sound1 "sound/large_warpout.ogg"
    pause 0.4
    play sound2 "sound/large_warpout.ogg"
    pause 0.4
    play sound3 "sound/large_warpout.ogg"

    "The clone was merely a precursor to what was to come. A stream of Biancas emerged and surrounded the Ascendant."
    
    play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
    
    "Tens... Hundreds of Biancas materialized and circled around the Ascendant, spraying it with a stream of lead."
    cla "Stopping and slowing down time's not the only thing I can do you know... I can also jump backwards to create an unlimited amount of copies of myself."
    cla "Teehee~ Isn't it time we put an end to this show?"
    "All the Biancas activated their grav guns."
    
    play sound "sound/chargeup.ogg"
    
    cla "Ah, by the way, I spent the past month repairing my grav gun. Of course, nobody else noticed because time was frozen for everyone during that entire span."
    "The Nightmare Ascendant froze in place, its limbs outstretched, as they were pulled apart by the strength of a hundred Biancas."
    
    scene alice_cockpit4 with dissolve
    
    ali "Y-YOU... MONSTER!!!"
    cla "Ah ah ah... Isn't it a little hypocritical for you to be calling me that?"
    cla "Now, it's over!"
    
    play sound "sound/large_warpout.ogg"
    
    "An enormous time rift opened above the Ascendant. A massive chunk of molten rock flew out, directed by the gravity eddies of a thousand Biancas."
    "The cheerful chanting of a thousand Claudes echoed through the channel as they heaved the molten mountain towards the Ascendant."
    "They sent it hurtling towards the Nightmare Ascendant."
    
    scene alice_cockpit5 with dissolve
    
    "Alice could only stammer in panic as the massive mountain of magma headed towards her."
    ali "W-What...!? No!!"
    ali "Y-you can't! If you do this, the space time continuum will-"
    
    scene cg_claudecockpit2 with dissolve
    
    cla "Mmm... You certainly do have a point about that."
    cla "Oh well! Who cares 'bout a borin' thing like that! That just means I can have the captain all to myself!"
    
    scene alice_cockpit5 with dissolve
    
    ali "YOU'RE INSANNEE!!!!"
    cla "The pot doth call the kettle black..."
    
    play sound "sound/explosion4.ogg"
    scene alice_cockpit6 with dissolve
    
    "The Nightmare Ascendant vanished in a bright flash of light as it smashed against the molten rock and sank deep within its core."
    "Even if it somehow survived within, it would be encrusted in solid stone once the asteroid cooled. It was a burial mound from which Alice could never emerge."
    "Shields and the entire bridge crew stared in disbelief."
    "They had just witnessed something beyond the comprehension of humans."
    
    stop music fadeout 1.5
    scene white with dissolvemedium
    
    "Just then, the entire universe began to fade to white."
    cla "Oops! Can't let this happen so soon~"
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    
    "... ... ..."
    "... ..."
    "..."
    "Shields' consciousness faded as his world unraveled."
    kay "(Was this... the right decision...?)"
    kay "(I have no idea what's going to happen now... The universe as we know it will cease to exist...)"
    
    $dshow("claude zboobs_naked happy neutral neutral",ypos=1600)
    
    cla "Teeheeheee..."
    "Claude emerged besides Shields in the great white nothingness, as naked as when she was born."
    "Suddenly, he realized he was stark naked as well."
    kay "Claude!"
    kay "What... happened!?"
    
    $dshow("claude zfingerup_naked talk neutral neutral")
    
    cla "Mou... It's just as I warned you. My victory over the Nightmare Ascendant triggered a massive time paradox, the likes of which the Law of Causality has never seen... Ah, if I were to explain it as simply as possible..."
    cla "Time paradoxes caused by regular actions cause the local universe to collapse, and then get recreated without the paradox. Unfortunately, a paradox caused while I'm in the middle of using my time device is quite a different matter..."
    cla "In the latter case... the paradox will propagate through all of space time via the open time device... and cause the entire space time continuum to collapse!"
    cla "So far, I've been jumping back in time and causing small scale paradoxes to delete certain universes and remake new ones with better outcomes. You can consider myself a demolition woman who travels through time and blows up unwanted realities while leaving the good realities untouched..."
    cla "Unfortunately, this latest demolition didn't quite go as planned... Instead of blowing up just a single building, you could say... I accidentally blew up the entire universe!"
    
    $dshow("claude zneutral_naked talk neutral upset")
    
    cla "Mou... This is why relying on my powers to magically fix problems is a bad idea, captain... Didn't I warn you about this already?"
    kay "Yeah, that sounds bad! Like, really bad! But the only reason why you went along with it is because there's a way to fix it, right!?"
    
    $dshow("claude zboobs_naked happy closed neutral",ypos=1600)
    
    cla "Teeheeeheee... Mah, I guess you could say that."
    cla "Don't worry! Claude's come up with a brilliant plan to prevent the end of existence as we know it!"
    "Shields gingerly grimaced as Claude's hands wandered between his legs, all the while explaining with a carefree grin that the very fabric of reality was splitting apart at the seams."
    kay "A-and that would be...?"
    cla "Teehee..."
    cla "First, isn't it time for the captain to live up to his side of the bargain?"
    
    $dshow("claude zneutral_naked smile closed neutral blush")
    
    cla "Moouu, Claude's confidence is sinking... To think she would bare all in front of the captain and he wouldn't even bother to take a few polite squeezes..."
    
    $dshow("claude zfingerup_naked neutral neutral upset blush")
    
    cla "Fan service is the only thing poor ol' Claude has going for her! Y-you can't take that away too...!"
    cla "Teehee~"
    kay "Oy, you can't just tell me the space time continuum is going to collapse and expect me to stay calm!"
    
    $dshow("claude zneutral_naked neutral neutral upset blush")
    
    cla "Captain, do you trust me?"
    kay "Trust...?"
    cla "Do you... believe that Claude can fix this? Can you count on Claude's word?"
    kay "Well... yeah..."
    kay "I trust your word."
    kay "You've... always been a member of my family."
    kay "And... honestly... I have you to thank for even getting the chance to do over my past... If you hadn't been here, then I would have just had to live with letting the Liberation Day Massacre happen..."
    kay "I owe you my life. If you hadn't used your power, then we would certainly all be dead."
    kay "So yes. I trust you, Claude."
    
    $dshow("claude zneutral_naked happy neutral neutral blush")
    
    cla "Ah, captain... My heart flutters at your words of appreciation! Truly the efforts of this pure and innocent maiden have paid off!"
    kay "(...pure maiden. Yeah.)"
    
    $dshow("claude zneutral_naked neutral closed upset blush")
    
    cla "Hmph. You're thinking bad thoughts about your patron goddess aren't you?"
    "Shields sighed as Claude playfully twisted and jerked his equipment."
    kay "Pure!? Innocent!? Listen, if you expect me to believe that, I would suggest you get your hands off my balls first!"
    
    $dshow("claude zneutral_naked smile neutral upset blush")
    
    cla "Eeah, I can't help it. You're floating buck naked in front of me after all~"
    cla "Oh captain, that magnificent length! The impressive girth! Truly you possess the cannon rod of the stars!"
    kay "... ... ..."
    "Shields let out a breath. But for some reason, he felt inclined to believe Claude had a way out of this latest mess."
    kay "So? What is this place anyways?"
    "Claude wrapped her fingers around him and continued her work as she lazily explained the situation."
    cla "A little pocket of subspace I reserved for some alone time. I've frozen time everywhere else, so you don't have to worry about the universe unravelling for now."
    cla "Huufuufuu... We could literally make love here for the rest of eternity if that's what you want. In fact, the space time continuum will be saved if I just hold time forever while we populate this realm with our offspring!"
    kay "(But that would just cause a whole new set of issues!)"
    
    $dshow("claude zneutral_naked smile closed neutral blush")
    
    cla "Mah... I guess you'd want to venture off and save everyone again though... I guess that's just a part of who you are."
    
    $dshow("claude zfingerup_naked smile closed neutral blush")
    
    cla "By the way, I've always liked that part about you, captain!"
    kay "So... seriously. Tell me how we're gonna fix this."
    
    $dshow("claude zneutral_naked neutral neutral upset blush")
    
    cla "Moouu... Impatient men aren't popular with the girls..."
    "Claude bent down and gave the tip of his now rock hard rod a kiss."
    cla "Huufuufuu... Your words are all business, but I see your body is ready..."
    
    hide claude with dissolve
    
    "She wrapped her lips around it and gave it a suck."
    "Ignoring the fact that he was floating in subspace with the space time continuum about to collapse, he would say that Claude definitely appeared ready and able to deliver an exquisite blow job. But that was clearly neither here or there!"
    kay "Oy... Claude...! This is hardly--"
    cla "Relax, captain! Relax! I'll send ya off on your little mission to save existence as we know it soon enough! But right now, it's time for you to serve your goddess!"
    cla "I'm not gonna use my god powers for any shmuck! Only the faithful shall receive!"
    kay "For crying--"
    
    if CENSOR == True:
        scene black with dissolvemedium
    if CENSOR == False:
        call censor_claudehscene
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene bg captainscabin with dissolve
    
    "He pulled himself up."
    kay "All right, all right. That's only assuming that there is a tonight."
    kay "So. What's the big plan to save the day?"
    cla "Aah, you had to ruin the mood..."
    cla "Oh well."
    "With a snap of her finger, the cum on Claude's face vanished. By now, such tricks didn't even make Shields flinch."
    
    $dshow("claude zneutral_naked happy neutral neutral blush")
    
    cla "Hufufu... Were you hoping that I would keep the cum on? Or perhaps wipe it off with my fingers and put it in my mouth?"
    kay "Uhh... No."
    
    $dshow("claude zneutral_naked talk neutral upset")
    
    cla "Beh."
    cla "Eh, anyways, here, you'll need this."
    "A small stop watch materialized in Claude's palm. She handed it to Shields."
    
    play music "Music/Destinys_Path.ogg" fadeout 1.5
    $dshow("claude zboobs_naked happy neutral neutral",ypos=1600)
    
    cla "Tada~! I present to you, Ticktock Version 3.0! Your key to becoming a Time Lord!"
    kay "W-wha?"
    
    $dshow("claude zfingerup_naked talk neutral neutral")

    cla "It's real simple to use. You see the gear running across the outside of the device? Rotate clockwise to speed things up or counterclockwise to slow things down, and then put things in reverse!"
    kay "You mean... This tiny thing is the time device!?"
    cla "Mou, of course not, captain... The real deal's hidden away somewhere in subspace, where nobody would ever find it. This little gadget is simply a remote control."
    cla "Mah, of course, the time device can be used for a lot of other applications aside from just fast forwarding and rewinding time, but just this should be enough for a beginner. Once you've got the hang of it, you'll figure out all the other tricks eventually..."
    kay "Why are you giving this to me...?"
    
    $dshow("claude zfingerup_naked talk closed neutral")
    
    cla "To travel back in time and prevent the paradox from occurring, of course!"
    cla "Meanwhile, Claude will stay here, and keep this universe frozen so that the paradox doesn't spread to the others."
    kay "Wait a minute... Who knows how long it'll take for me to do that! I can't just leave you here!"
    
    $dshow("claude zfingerup_naked talk neutral neutral")
    
    cla "Mou... Captain, did you forget that you're a time traveler now?"
    cla "It doesn't matter if your mission takes a day, a month, a year, or even a century. After you're done, just jump back to this time frame and pick me back up. From my point of view, you'll just have been gone for a few seconds, even if years may have gone by from your point of view."
    kay "O-oh... right. I... guess I can do that now."
    "He wrapped his fingers around the time device."
    kay "Any hints as to how to prevent the paradox?"
    
    $dshow("claude zboobs_naked happy closed neutral",ypos=1600)
    
    cla "'Fraid not! Everything's in your hands from this point on."
    cla "I'm sure you'll be able to figure out the rest. After all, you are practically playing on god mode if you can control the flow of time."
    cla "If something goes wrong, just.... rewind time. Or leap to another universe. I'm sure you'll do fine!"
    kay "(Something tells me this isn't going to be as easy as Claude's suggesting.)"
    kay "(But I don't have a choice. This is the only way to prevent all of existence from ending!)"
    
    $dshow("claude zfingerup_naked talk neutral neutral")
    
    cla "Ah. One more thing."
    cla "If you run into myself... Eh-heh..."
    cla "You'll take good care of her, right?"
    kay "Yeah. Of course!"
    
    $dshow("claude zboobs_naked happy closed neutral",ypos=1600)
    
    cla "Eaah, as expected of our captain. Taking responsibility is a man's duty!"
    
    $dshow("claude zsalute_naked happy neutral neutral")
    
    cla "Sah! Good luck with your mission, sah!"
    
    $dshow("claude salute happy neutral neutral")
    
    "With another snap of her finger, their clothes reappeared."
    kay "All right."
    kay "Don't worry. I'll be back in a flash."
    
    $dshow("claude neutral smile closed neutral blush")
    
    "Claude leaned in and pressed her lips against his."
    cla "That one's for luck."
    kay "Yeah."
    "Shields reached for the remote."
    kay "Then... I'll be seeing you."
    "Claude smiled."
    
    $dshow("claude neutral happy closed neutral blush")
    
    cla "Because... today's Claude's lucky day!"
    "With a grin, he spun it counterclockwise."
    
    scene white with dissolvemedium
    
    play music "Music/Sora_no_Kodoh.ogg" fadeout 1.0

    call dlc_credits
    
    play music "Music/Destinys_Path.ogg" fadeout 1.5
    scene black with dissolve

    "... ... ..."
    "Nearly a decade had passed since he became a time traveler, and Shields was still no closer to resolving the paradox."
    "The past proved far more difficult to change than anticipated, as Shields soon realized that while he could use his powers to observe and manipulate others into acting for him, he could not take matters into his own hands without risking tearing the fabric of reality a second time."
    "He finally understood the weight of Claude's awesome power. He was near omnipotent, able to observe anything, move anywhere, and do anything. But yet, every use of his power had to be carefully planned out, or he would bring about certain doom, not only for himself, but all life as he knew it."
    "After nearly a decade of research, he had finally devised a plan to avert the end of existence. But first, he needed a partner who understood the nature of time travel, but who was not a time god herself. Yet."
    "He had traveled through millennia of history in search for her. He had dug into top secret Ryuvian archives and manipulated technologists who wielded powers beyond what his past self could even have imagined."
    "But the Shields of today was different. He was, for all intents and purposes, immortal and timeless. He existed everywhere, and yet existed nowhere. Even the most powerful of the Sharrs were mere toddlers in his eyes, playing around with toys."
    "His research had led him to a derelict space station in the edges of the Ryuvian Empire, nearly three thousand years before Shields' former time."
    "He materialized inside, and came upon an old, dusty lab."
    "A woman's voice cried out."    
    cla "W-who's there!?"
    "Shields emerged from the shadows."
    kay "I am Kayto Shields. I have come from the future."
    kay "Claude Trilleo. I need your help."

    $persistent.unlocked_endings["CLAUDE SECRET END: TIME LORD"] = True
    $chivo_process('Claude Secret Ending')
    $check_for_all_endings()
    stop music fadeout 1
    scene black with dissolve
    show screen secret_end
    #show expression Text("SECRET CLAUDE END:\nTIME LORD",yalign=0.5,size=90,color="fff")
    pause 3
    
    $dshow("claude boobs happy neutral neutral",ypos=1600)
    
    cla "Congratulations captain, you've just got the best ending in the game!"
    
    $dshow("claude neutral talk neutral upset")
    
    cla "What? You thought you were on the Icari route? Mou, captain, you're the worst..."
    cla "Doing this and that to poor ol' Claude, and then just throwing her away the instant you're finished with her! Hmph! I'm not going to give you any more hints!"
    "... ... ..."
    
    $dshow("claude neutral talk neutral neutral")
    
    cla "Eh? You're sorry? You'll definitely play my route first in the next game?"
    
    $dshow("claude boobs happy neutral neutral",ypos=1600)
    
    cla "Teehee... I knew you would be reasonable, captain..."
    cla "Well, I guess I can give away this much... If you want to see a different outcome, find a way to interrupt Alice before she takes over Chigara's body for the first time during the kidnapping attempt."
    cla "That's all the help I'm going to give! Good luck, captain!"
    
    $renpy.full_restart()    

label confrontationwithfate:
    
    #IF CHOSE TO CONFRONT THE OTHER SHIELDS
    
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    scene bg hallway with dissolve
    
    show mook as mook1:
        xpos -0.25
    show mook as mook2:
        xpos 0.15
    show mook as mook3:
        xpos 0.55
    with dissolve
    
    if girl != "Icari":
        "However, as soon as they left Shields' office, the trio came face to face with a squad of marines."
    if girl == "Icari":
        "However, as soon as they left Shields' office, the duo came face to face with a squad of marines."

    kay "Shit!"
    mrn "Freeze!"
    "Completely outnumbered and surrounded by rifles, Shields had no choice but to put his hands on top of his head."
    kay "(Tsch... Not quite what I was hoping for...)"
    kay "(But we could actually use this to our advantage.)"
    
    if girl != "Icari":
        "He faced his companions, but found that Claude had once again vanished into thin air."
        kay "(Looks like Claude's decided to hide for now...)"
        
    "He motioned for [girl] to follow his lead. She slowly put her hands on top of her head as well."
    kay "Alright, we surrender!"
    kay "But... I'm willing to talk! Take me to your leader!"
    
    show kayto:
        xpos 0.25
    with dissolve
    
    kayo "No need."

    if girl != "Icari":
        "The other Shields emerged from behind the squad of marines."
        
    if girl == "Icari":
        "The other Shields emerged from behind the squad of marines with the commander."

    kayo "You've got some guts breaking into my office. What were you trying to pull in there?"
    kay "I just saved your ass by warning Fontana that the Prototypes sabotaged his ships. You'll thank me for it later."

    if girl != "Icari":
        
        $dshow("ava armscrossed talk narrow angry",xpos=0.75)

        ava "Captain, he is telling the truth. I saw him contact Fontana with my own eyes."
        kayo "Commander, you violated a direct order by setting the imposter free. And worse, I see that you're actively helping him sow dissention on board this ship. Have you lost your damned mind?"
        ava "No..."
        ava "Lately, I fear it is you who has been acting strange..."
        kayo "What?"
        ava "Sir. I do not know what words the chief used to sway you, but you have put the ship at risk by putting your blind faith in her."
        ava "I implore that you examine all the evidence at hand and detain the chief until this matter has been fully investigated."
        "The other Shields' face contorted in rage."
        
        show kayto yell with dissolve
        
        kayo "Y-you... you turned my own XO against me!"
        kayo "After all we've been through... You'd trust a Prototype spy over me!?"
        ava "Sadly, I was about to say the same."
        kayo "Commander... No... Ex-commander Crescentia. I am relieving you of your command. You are to be confined to quarters until the battle is over so that you can be tried for insubordination."
        kayo "As for you, Prototype... The brig!"
        
    if girl == "Icari":
        
        $dshow("icari armscrossed shout neutral angry",xpos=0.75)

        ica "Hey uhh... O-other captain! He's telling the truth! I saw him contact Fontana myself!"
        ica "You gotta believe us... 'Cause you're being fooled big time by Chigara!"
        kayo "Icari... I don't know what's going on... but you helped this imposter escape by hacking into our security system."
        kayo "When I brought you onboard this ship... you swore that you would play by my rules. What happened to that?"
        
        $dshow("icari point shout neutral angry")
        
        ica "H-hey, snap out of it! Y-you're... not acting like yourself!"
        
        hide icari with dissolve
        $dshow("ava armscrossed talk narrow angry",xpos=0.75)
        
        ava "Captain, I am inclined to agree. The past few days, you have exhibited strange symptoms whenever we broach the topic of our chief engineer. Now, even our chief of security believes that Chigara seeks to sabotage our mission. Should we not re-evaluate our approach given these new developments?"
        kayo "I don't see any new developments. Just the same old Prototype plot to split this ship apart!"
        kayo "Commander, you are out of line..."
        ava "With all due respect, captain-"
        kayo "Enough!"
        
    if girl == "Asaga":
        #Asaga
        
        $dshow("asaga leanforward yell neutral angry",xpos=0.5,ypos=1600)
        
        asa "Hey capt'n, just wait a minute here! Your other version and the commander have been working all this time to save the ship! You're actin' real stupid right now!"
        asa "Aah, I don't know you any more! I can't believe I actually liked ya at one point! It's over between us! I'll... uhh... just stick with the other captain!"
        kayo "You too, [girl]? What's..."

    if girl == "Sola":

        $dshow("sola armhold frown neutral sad",xpos=0.5)
        sol "Captain... I fear you have become corrupted by the Prototypes' influence. You must open your eyes and listen to the advice of your comrades."
        sol "We are... here to help you."
        sol "We do not wish to see you in pain again."
        kayo "You too, [girl]? What's..."

    if girl == "Icari":
        
        $dshow("icari point shout neutral angry",xpos=0.5)
        
        ica "Oy, this is definitely weird! The captain's acting like he's been mind controlled or something!"
        
        $dshow("icari handonhip shout neutral angry")
        
        ica "Tsch... Was this what the Prototypes were hoping for? To use Chigara to control him?"
        ica "Shields, you've gotta do something to make him snap out of it! Or else we're all gonna be sharing a cell with Lynn!"
        
    $dshow("ava handonhip shout narrow angry")

    ava "It's useless... He's fallen completely under the control of the Prototypes."
    kay "([girl]'s right... It's do or die time!)"
    
    play sound "sound/guncock.ogg"
    
    "Shields slowly lowered his hands from his head to the sound of the marines locking and loading their rifles."
    kay "Shields... How about we settle this, man to man?"
    kay "I'm... you. You're... me."
    kay "Believe me, I've stood in your shoes before... I was so damned cocky that I couldn't see the truth dangling right in front of my eyes."
    
    play music "Music/Camino.ogg" fadeout 1.5
    show kayto yell with dissolve
    
    kayo "Marines, hold your fire!"
    
    hide mook1
    hide mook2
    hide mook3
    hide ava
    hide icari
    hide sola
    hide asaga
    with dissolve
    
    show kayto:
        xpos 0.5
    with dissolve
    
    "The other Shields marched up to his mirror image. They stood face to face."
    kayo "All right. I'll bite."
    kayo "If you really are me, you should know all that Chigara has done for us."
    kayo "She's had hundreds of opportunities to kill us before. And yet, each time, she has defended this ship!"
    kayo "To question her now... Would be tantamount to betraying my family."
    kay "That's because she's a sleeper spy! Right now, all she's doing is winning your influence, but when the time comes, she'll lose control of her body and destroy all that you've worked for!"
    kayo "If so, what would you have me do? Kill her? Imprison her for life?"
    kay "Protect her! From being controlled by the Prototypes!"
    kay "This is for Chigara's sake as well! And for the lives of everyone on board this ship, and the billions who will be saved if this war ends now!"
    kay "You don't know what my future's like... If you think you're protecting Chigara right now... You're gonna be in for a hell of a shock."
    kay "You've got to do this for her!"
    
    show kayto yell with dissolve
    
    kayo "All lies!"
    kayo "Chigara... Chigara will save us! She's... all that matters!"
    kayo "I won't betray her! SHE..."
    kayo "Is... everything...!"
    
    show kayto yell:
        zoom 1.4 ypos 0
    with dissolve
    
    "The other Shields grabbed Shields by the scruff of the collar. Staring deep within his past self's eyes, Shields only saw a massive, empty void, as deep as the darkest trench."
    kayo "All I need is her...!"
    "Shields struggled against his other self's grip as he raved with madness."
    kay "You've... been corrupted!!"
    kay "(Ava was right! This version of myself has become a slave to the Prototypes! At this rate... reasoning with him is completely useless!)"
    kay "(What has... Chigara done to him!?)"
    
    $dshow("ava handonhip shout narrow angry",xpos=0.75,behind="kayto")
    
    ava "Marines, hold your fire! I'm taking command of this situation!"
    ava "The captain has gone... insane!"
    "The marines looked around in a panic, at a loss as to what to do."

    if girl != Icari:
        "On one hand, the captain of the ship had just relieved the commander of her authority, but it was clear from his mad raving that their captain was no longer fit to lead them."

    if girl == Icari:
        "On one hand, the captain of the ship was the highest ranked officer, hence they had to obbey his orders, but it was clear from his mad raving that their captain was no longer fit to lead them."

    kay "Y-YOU MORON!!!"
    "Shields clenched his teeth."
    kay "WAKE UP!!!!!"
    
    stop music fadeout 1.5
    play sound "sound/punch.ogg"
    show layer master at tr_xshake
    scene cg_kaytopunch with dissolve
    
    "Shields shoved his past self away and delivered an almighty punch right to his other version's kisser."
    kayo "G-GUGH!!"
    "The other Shields fell flat on his back against the floor."
    "Shields stood over him and bellowed."
    "He bellowed the truth which he only knew. For he was not speaking to an adversary or a Prototype puppet."
    "He was speaking to himself."
    
    play music "Music/Colors_Loop.ogg" fadeout 1.5
    
    kay "This... isn't about Chigara! This was never about her!"
    kay "All of it is to exorcise the ghost which haunts you by the bedside every night."
    kay "The ghost of the one person you regret failing the most."
    kayo "T-tsch..."
    kay "I know..."
    kay "I tried to move on, by finding a new future. A future far from war, surrounded by my children... But all of that was a lie... A deception, used by the enemy to control me! ME!!"
    kay "Nothing I do will ever return Maray to me... Nor will it absolve me of the crime of abandoning millions to die that day..."
    kay "But such is war!"
    kay "In war, scars are opened. Scars which may never close. Scars which we must wear for the remainder of our lives..."
    kay "But... I'll be damned if I let more of my crew die because I could not face the truth."
    kay "The dead are gone. Some battles end in nothing but defeat."
    kay "It's... time for you to face the truth. Both eyes open."
    kayo "... ... ..."
    "Tears ran from both their eyes."
    "Those were the words both men lived by. No matter the torment, no matter the comforts Chigara may offer, Kayto Shields would not close his eyes to the galaxy he needed to defend."
    
    scene bg hallway with dissolve
    $reset_sprites()
    show kayto:
        zoom 1.0 xpos 0.5 ypos 0
    with dissolve
    
    "His other self's face returned to normal."
    kayo "... ... ..."
    kayo "Commander..."
    kayo "Revoke... the Chief Engineer's security access..."
    kayo "And have her detained."
    "The tension finally deflated. The marines put down their rifles, all parties exhaling in relief."
    
    $dshow("ava salute shout neutral angry",xpos=0.75)
    
    ava "Sir!"
    kayo "... ... ..."
    kayo "The ghost which spawned from that wretched day will never leave my side..."
    kayo "... ... ..."
    kayo "All the more reason she should not gain new friends in the afterlife."
    "With that, the other Kayto Shields stood up and straightened his uniform."
    kayo "I am convening an emergency staff meeting. We will have to devise a new battle plan without Chigara's participation."
    kayo "Commander, get the lieutenant."
    kayo "As for my other self... I am sure his insight will be most valuable in the coming battle."
    kayo "Heh. After all, he's at least as smart as I am."
    "Despite the two men being at each other's throats a second ago, Shields could not help but chuckle at his own joke."
    
    if girl == "Asaga":
        jump asagahscene
        
    if girl == "Ava":
        jump avahscene
        
    if girl == "Sola":
        jump solakiss
        
    if girl == "Icari":
        jump icarikiss
        
label asagahscene:

    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene black with dissolvemedium
    scene bg crewquarters with dissolvemedium

    "Shields collapsed in an empty bunk after the end of the staff meeting."
    "He had told his future self everything he knew of the enemies' capabilities. Meanwhile, Fontana informed them that his best minds were working around the clock to restore control over their ships. However, it would be another two hours before the fixes were completed."
    "Chigara was safely detained in the brig. So far, there were no signs of the Prototype Leader assuming control over her."
    "In other words, Shields had done everything he possibly could to avert the Liberation Day massacre. Now all that remained was to wait and see if his efforts bore fruit."
    "He realized that he had not slept for over 24 hours. After a long mission of crawling through maintenance tunnels and narrowly escaping death on multiple occasions, his body was exhausted."
    kay "(The danger has not yet passed... But from this point on, the future is in the hands of this ship's crew...)"
    kay "(Everyone... do your best!)"
    
    play music "Music/Colors_of_an_Orchestra_II.ogg" fadeout 1.5
    
    $dshow("asaga armscrossed smile narrow up")
    
    "The door opened, interrupting Shields' thoughts."
    asa "Eehh... So there you are, capt'n..."
    "Shields faced Asaga, leaning up against the head of the bunk."
    kay "Something the matter, Asaga?"
    
    $dshow("asaga armscrossed smile closed2 up")
    
    asa "Eh-heh... Nah, for once, things seem to be going pretty good."
    "Asaga plopped down beside him."
    
    $dshow("asaga armscrossed smile narrow up")
    
    asa "I don't know what happened in your timeline... But I get the feeling things turned out better this time around."
    asa "So? What exactly did happen anyways?"
    kay "... ... ..."
    "Shields didn't particularly want to sour the mood with his dark recollections."
    kay "None of that exists any more. If we were hypothetically riding the Sunrider down space time, I'd say our course has been so thoroughly diverted that we'd jump through entirely different systems now."
    kay "Well... I guess that's just a roundabout way of saying I don't feel like recounting what happened."
    kay "Those are... events which I never want to live through again."
    
    $dshow("asaga armscrossed frown narrow down")
    
    asa "I... see..."
    asa "Sorry. I didn't mean..."
    kay "Don't worry."
    kay "With these hands, I changed the course of history. Heh, makes me pretty full of myself right now. I guess... I don't want to ruin my good mood."
    kay "Even in my version of events... you never gave up, Asaga."
    kay "You... saved my life."
    kay "I'm only here right now because of you. Of course, none of that has happened to the you standing there right now. But..."
    kay "Thanks for always having my back. No matter what timeline I end up in, you'll always be my ace."
    "With a laugh, Shields gave the top of Asaga's head a rub down."
    
    $dshow("asaga leanforward yell closed sad")
    
    asa "A-ahh...! Mou, treatin' your CAG like some kid... Ya got some nerve, capt'n..."
    kay "Heh."
    kay "I'm afraid I'm not the captain of this ship right now. Just a... surprise guest."
    
    $dshow("asaga armscrossed smile narrow down blush")
    
    asa "... ... ..."
    "Asaga fell to her side beside him, resting her head on his chest."
    asa "Then... it won't be a problem if I do this, huh..."
    kay "... ... ..."
    
    $dshow("asaga armscrossed smile narrow2 sad blush")
    
    asa "Ever since you rescued me from the fake marriage at Ryuvia Prime... My body gets so hot whenever I think 'bout you... Ah, mou, this is unfair!"
    
    $dshow("asaga armsup shout arrow angry blush")
    
    asa "You've probably done it already with a bunch of women, haven't you!? That's the only reason why you can stay calm like that!"
    asa "Tell the truth! You're actually quite the player, aren't you?"
    kay "P-player...?"
    
    $dshow("asaga armscrossed frown2 narrow2 sad2 blush")
    
    asa "Hmph."
    asa "So. How many different women have you already done it with?"
    kay "Ah... hahaha... Y-you know, you're not supposed to ask stuff like that..."
    kay "(I keep forgetting... This girl has one hell of a strong jealous streak...)"
    
    $dshow("asaga excited yell neutral angry blush")
    
    asa "I wanna know!!"
    "Asaga pounded her fists against Shields' chest."
    asa "You've already done it with the commander, haven't you!? Aaahh, I knew it, it was obvious from when she was drunk at the beach!! And probably even Chigara, haven't you!?"
    kay "Asaga... please...! T-that was all in the past!!"
    asa "So it's all true! Ya beast! Even Chigara!!! I can't believe you!!!"
    kay "L-look, that hasn't even happened in this timeline! So you can hardly even count that against me!"
    
    $dshow("asaga armscrossed frown2 closed sad2 blush comiccry")
    
    asa "H-huuu... And to think... I... haven't even made out with anyone yet..."
    asa "Well... I guess I tried practicing with Chigara a few years back... B-but... ugh... All that proved was that we don't swing that way..."
    kay "Oy... Don't tell me you've never..."
    
    $dshow("asaga leanforward yell closed angry blush",ypos=1600)
    
    asa "Isn't it obvious!? I'm flipping royalty, ya know! What, ya think the royal family of Ryuvia would just let any shmuck deflower the crown princess!?"
    asa "Mou! Capt'n, I don't like ya!"
    
    play sound "sound/hit.ogg"
    
    "Asaga stood back up, only to bang her head on the top of the bunk."
    
    $dshow("asaga armsup shout arrow angry blush")
    
    asa "Hiyyaahh!!! It hurts it hurts...!"
    kay "Ack, are you all right?"
    
    $dshow("asaga armscrossed frown2 closed sad2 blush comiccry")
    
    asa "No, I'm not all right at all. Mou..."
    
    $dshow("asaga armscrossed uu narrow sad2 blush")
    
    asa "My heart's pounding so crazy that I'm about to go full Sharr mode. And uhh... You don't want to see what I'll be like then..."
    kay "H-heh heh... Probably not..."
    
    $dshow("asaga armscrossed frown closed2 sad blush",zoom=1.3,ypos=2400)
    
    asa "Sigh..."
    "Shields laid Asaga down on top of him and stroked her head."
    kay "There, there."
    asa "Huuu..."
    kay "Sorry. I won't look at other girls from now on."
    kay "Especially Prototype spies. Lesson learned there."
    
    $dshow("asaga armscrossed smile narrow2 sad blush",zoom=1.3,ypos=2400)
    
    asa "Good."
    asa "... ... ..."
    "Asaga's body was burning with heat. She wrapped her arms around Shields' neck and pressed her lips against his."
    
    $dshow("asaga armscrossed smile closed2 sad blush",zoom=1.3,ypos=2400)
    
    asa "Mm..."
    "He stroked the back of her head as Asaga's scent enveloped him. Shields forced Asaga's mouth open and sampled the taste of her tongue. Slightly sweet, but the taste was too distant. They wanted to get closer for something more intense."
    "Their tongues intertwined, Asaga repositioned herself, her legs straddling his waist."
    "They kissed for as long as Asaga could hold her breath. She detached, gasping for air."
    
    $dshow("asaga armscrossed yell narrow2 sad blush",zoom=1.3,ypos=2400)
    
    asa "Pah... pah..."
    kay "You can breathe through your nose you know."
    asa "Mou, shaddup, this is mah first time! I dunno what I'm doin'!"
    asa "Huu... T-things aren't lookin' so swell down there..."
    "Shields raised her skirt, revealing her soaking wet panties."
    kay "Holy shit."
    kay "(I-it practically looks like she wet herself!)"
    "Her juices had seeped through her panties and formed a big dark circle on his trousers. He reached in and sampled some with his fingers."
    
    $dshow("asaga armscrossed yell closed sad blush",zoom=1.3,ypos=2400)
    
    asa "H-huugu...!"
    "Judging from the sticky and slippery feeling between his fingers, he definitely knew that all of it was her juices and that she had not had an unfortunate accident."
    kay "You... made so much!"
    
    $dshow("asaga leanforward yell narrow sad blush",zoom=1.3,ypos=2000)
    
    asa "Aah, I can't help it! I've been waitin' for this forever! Whaddaya expect! M-mah pussy turns into one giant swimming pool whenever I think 'bout doin' this!"
    asa "I can't even think straight no more! Aaah, we're finally gonna fuck! Aaahh Holy Ryuvia! Mah pussy's gonna get stretched! Dear Emperor in Heaven, your daughter is about to became a woman!!"
    "Shields put his finger on Asaga's mouth."
    kay "I don't think all those words are necessary."
    asa "Well, I'm nervous! This is a big moment, ya know!"
    kay "You look more than ready down there... Here we go."
    "He raised her legs and slipped off her panties, thick strings of juice stretching from the cloth to her gloryhole."
    "Unfortunately, the bunk was too short for him to position himself for penetration."
    kay "Aah shit, this is a problem..."
    kay "Hang on, lemme..."
    
    hide asaga with dissolve
    
    "Shields stood and went over to a nearby panel. He opened it and pressed a button."
    "Everything in the room began to levitate, as the artificial gravity deactivated."
    asa "E-eh!? W-what are ya...?"
    kay "Bunk's too small. We're doing it like this."
    
    if CENSOR == True:
        scene black with dissolvemedium
    if CENSOR == False:
        call censored_asagahscene
    
    scene bg crewquarters with dissolve
    
    "After the drone finished its work, Shields positioned himself under Asaga and returned the gravity to normal."
    kay "Ommpf..."
    "He grabbed Asaga in his arms as everything dropped to the floor."
    kay "Here you go."
    "With a final slap on her ass, he set her back up."
    kay "The fight's not over yet. Still... one more."
    
    $dshow("asaga armsup shout excited surprise")
    
    asa "E-EAAHHH!!!!"
    kay "W-what!? Something the matter!?"
    
    $dshow("asaga armsup shout arrow surprise")
    
    asa "Aahhh crap, crap, crap! I totally forgot, having sex right before the final battle's like an ultra-mega death flag! Huuu... W-what am I gonna do, captain..."
    
    $dshow("asaga armscrossed yell closed down comiccry")
    
    asa "I dun wanna die... There's still lots of other positions I wanted to try..."
    kay "(That's your reason for living!?)"
    kay "Oy... This is real life here! Not some kind of mecha eroge. I'm sure you'll be fine."
    asa "Huu... I can still keep goin' captain... M-maybe we should try the other positions first..."
    kay "Idiot! Focus on the battle!"
    asa "U-understood..."

    jump thefinalbattle
    
label avahscene:
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    scene black with dissolvemedium
    scene bg hallway with dissolvemedium

    "Shields left the staff meeting, thoroughly exhausted."
    "He had told his future self everything he knew of the enemies' capabilities. Meanwhile, Fontana informed them that his best minds were working around the clock to restore control over their ships. However, it would be another two hours before the fixes were completed."
    "Chigara was safely detained in the brig. So far, there were no signs of the Prototype Leader assuming control over her."
    "In other words, Shields had done everything he possibly could to avert the Liberation Day massacre. Now all that remained was to wait and see if his efforts bore fruit."
    
    $dshow("ava handonhip neutral neutral neutral",xpos=0.5)

    ava "Kayto."
    kay "Ava? Need something more?"
    ava "No..."
    ava "I was merely going to invite you for a meal in my office. It's... not every day when I can speak to you."
    kay "Come to think of it, I was thinking the same. It'd be nice to have a chat for once..."

    play music "Music/Love_Theme.ogg" fadeout 1.5

    scene black with horizontalwipe
    scene bg xooffice with horizontalwipe
    
    "A short time later, the two of them were in the XO's quarters with plates of food from the mess hall."
    "Ava cut into her steak."
    
    $dshow("ava handonhair neutral neutral neutral")
    
    ava "I'm afraid I'm still having a hard time believing that you're here from the future, much less that there are two Kayto Shields in this universe, one who captains this ship, and another from the future."
    kay "No kidding... It's not any easier for me to get used to either."
    kay "To me... This is still my ship. But there's another guy captaining it. But that guy's still me. But not me. I better not think about it too long or else it's just going to drive me crazy."
    kay "Tell the truth though... I'm not sure if I have the right to call the Sunrider my ship any more. In my timeline, I'm the one who got it sunk."
    kay "Maybe it's better that the other guy's in charge. He might be a stubborn shit face, but in the end, he realized that Chigara was a spy. It's something I would never have been able to do myself."
    ava "No. He only made the right call thanks to your assistance."
    ava "Still, it certainly is reassuring that you have matured a bit in the future. War truly does make men grow old early."
    kay "Heh, I'm not sure about that. I'm still the old Kayto Shields. Just... armed with the benefit of hindsight."
    kay "Any fool knows what he should have done in retrospect. I'm not doing anything special."
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "In any matter, talking about your timeline seems moot, as our actions have effectively ended that universe. Now... we head towards a future which is yet unwritten."
    ava "One which we steer with our decisions."
    kay "Hey Ava... This is kind of changing the subject... But uhh..."
    kay "You know, in my version of events, you uhh... told me that you lied about not remembering our promise... You know, that promise we made after we uhh... did it in advanced academy a week before your graduation?"
    
    $dshow("ava armscrossed neutral closed angry")
    
    ava "Kayto..."
    "Ava rubbed her brow in frustration, obviously displeased with the course the conversation was taking."
    kay "Look Ava... Resolving the situation with Chigara's not the only thing I need to do in this universe. What about us?"
    kay "We... left a lot of things hanging. And maybe I was just running away from it all, into Chigara's arms. Maybe that's what the Prototypes were counting on."
    
    $dshow("ava armscrossed neutral neutral neutral")
    
    ava "We both ran away."
    
    $dshow("ava armscrossed neutral closed neutral")
    
    ava "Sigh..."
    ava "But since you're not the captain... I suppose I can talk about it."
    
    $dshow("ava handonhair neutral narrow neutral")
    
    ava "This time, I'm afraid I'm not your XO. Merely your friend."
    kay "I'm more than happy with that."
    
    $dshow("ava handonhair disgust narrow neutral")
    
    ava "The day we abandoned Cera scarred everyone on board this ship. It's a day which we will not... cannot... forget. Even if we wished we could."
    ava "My father was presumably killed the instant the Legion reduced Command to a charred crater. Even though I was always distant from that man... He molded me into who I am today. I imagine I am his spitting image now. Professional. Detached."
    ava "Whenever I look at myself in the mirror... I see him staring back at me."
    ava "Will I... ever measure up to his expectations? Likely not, as my most vivid memories of him are when he disciplined me. That stern face, which always only said, \"You must work harder,\" is the only expression I see in my own reflection now. It is the only face I am capable of making."
    ava "His ghost will not permit me to entertain any girlish fantasies of becoming reunited with my academy sweetheart or any such like rubbish. Such delusions have no place in the mind of an XO. My duty to you was to remain professionally detached and provide you with rational counsel. Nothing more."
    kay "Ghost... huh..."
    kay "Ghost..."
    "Shields looked beside him."
    
    show maray lean sad:
        alpha 0.7 xpos 0.85
    with dissolve
    
    mar "Kayto... What are you doing talking to Avvy without me?"
    
    show maray excited angry with dissolve
    
    mar "Mou, you're eating steak too? Unfair! Big brother's unfair! I want some too!"
    kay "... ... ..."
    kay "Phantoms are only the projections of the livings' regrets..."
    
    hide maray with dissolvemedium
    
    "He put his fork down, suddenly feeling queasy."
    ava "You see them too."
    kay "Of course. Not a night goes by."
    kay "I regret surviving that day. Perhaps... if I had died too, then I would be with her now..."
    kay "Heh. What am I saying."
    kay "Can't say I'm actually religious enough to actually believe that. Hahaha."
    "Ava stood from her seat and knelt beside Kayto."
    
    $dshow("ava handonhair neutral narrow sad blush",zoom=1.3,ypos=2400)
    
    ava "Kayto... I am sorry."
    ava "For never saying it then."
    ava "When I was the only one who could understand half the weight you carry on your back..."
    
    $dshow("ava handonhair smirk narrow sad blush",zoom=1.3,ypos=2400)
    
    ava "But I will say it now."
    ava "You did not let anyone down that day. In the eyes of the crew, you are a hero."
    ava "In my eyes..."
    ava "You are the very same Kayto I grew fond of... all those years back. The very same Kayto who never left my side, no matter how unreasonable my orders."
    
    $dshow("ava handonhair smirk closed sad blush",zoom=1.3,ypos=2400)
    
    ava "And so I, Ava Crescentia, will do the very same. If you wish to march to the center of the sun, then I shall accompany you by your side, to the very end."
    kay "I know, Ava..."
    "Shields put his hand on Ava's head and stroked her long, flowing hair."
    "He leaned down and approached her lips. She raised her face and closed her eyes."
    "Their lips met again for the first time in so many years."
    ava "... ... ..."
    
    $dshow("ava handonhair disgust narrow sad blush",zoom=1.3,ypos=2400)
    
    ava "I guess... just this one time's all right... After all... I don't know when I'll be able to stand before you as just a friend again..."
    kay "Ava?"
    ava "Ah, mou!"
    
    if CENSOR == True:
        scene black with dissolvemedium
    if CENSOR == False:
        call censor_avahscene
        
    jump thefinalbattle

label solakiss:
    
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene black with dissolvemedium
    scene bg hallway with dissolvemedium
    
    "Shields walked to the mess hall for some food and drink, thoroughly exhausted after the staff meeting."
    "He had told his future self everything he knew of the enemies' capabilities. Meanwhile, Fontana informed them that his best minds were working around the clock to restore control over their ships. However, it would be another two hours before the fixes were completed."
    "Chigara was safely detained in the brig. So far, there were no signs of the Prototype Leader assuming control over her."
    "In other words, Shields had done everything he possibly could to avert the Liberation Day massacre. Now all that remained was to wait and see if his efforts bore fruit."

    
    $dshow(71000)
    "Just as he was about to enter the mess hall, he saw Sola lurking behind the gate, peering into the hall."
    kay "Uhh... Sola?"
    $dshow(70322)
    sol "Ah... Captain."
    kay "Not quite. It's me, future Shields. Can't say I'm the captain of this ship at this particular moment."
    $dshow(70301)
    sol "To me, you will always be the captain in any timeline."
    kay "What're you doing, hiding here? Is something the matter?"
    $dshow(70320)
    sol "No. I was merely observing a certain encounter."
    kay "Encounter?"
    "Shields leaned his face into the mess hall as well. He saw the other Kayto Shields talking with Asaga."
    sol "A certain maiden seeks to confess her feelings."
    kay "Wait. You mean that Asaga's telling the other Kayto Shields that she likes him?"
    $dshow(70321)
    sol "That is so."
    sol "No matter his response, this is something she must do before this battle. For the sake of the future."
    kay "(In my version of events, Asaga never could confess her feelings to me until it was too late...)"
    kay "(I'm glad things turned out this way instead...)"
    "In the end, the other Kayto Shields merely smiled and patted Asaga on the head before walking away."
    kay "(Eeehh... She got rejected huh...)"
    kay "(But I guess it's only the logical outcome... After all, this universe's Kayto Shields was head over heels for Chigara up until just a few hours ago, and was never rescued by Asaga...)"
    "Asaga put on a brave smile, despite being no doubt heartbroken, and marched out of the mess hall towards the lift to deck 2, no doubt to practice more on the simulator before the final battle."
    $dshow(70211)
    sol "Unfortunate. Yet, such may be life."
    sol "Now, Asaga's feelings have reached resolution. While this may not be the outcome she desired, she is strong enough to accept his answer."
    sol "I am sure she will find happiness. One day."
    $dshow(70223)
    sol "Ah. I am sorry. I did not mean to take your time."
    kay "Nah, I was just here to grab something to eat. Are you hungry?"
    sol "P-perhaps I am in need of some refreshments as well. Then, let us dine together."
    kay "All right, let's go."
    scene bg messhall with dissolve
    $dshow(70221)
    "No doubt, rumors of the captain's doppelganger had already spread to the four corners of the ship. When Shields entered, the mess hall went completely silent as every single pair of eyes turned to him."
    "Shields just laughed and waved."
    kay "Ah, hey everyone. I'm the second Kayto Shields you've heard so much about."
    kay "Relax. I'm not in command, so you can keep eating without coming to attention. But it's not like you lot even do that in the first place."
    "With laughter, the crew returned to their conversations, the atmosphere instantly returning to normal."
    $dshow(70223)
    sol "I... did not expect the crew to accept you so readily..."
    kay "Don't worry. These are still my men and women. Hell, the past year, we've crashed a royal wedding, rescued a two thousand year old Ryuvian, and now learned the Chief Engineer was a Prototype. Nobody's even gonna bat an eyelash at a future Kayto Shields..."
    $dshow(70211)
    sol "I... see..."
    "Shields went to the bar and looked through the day's menu."
    kay "Huh, Ryuvian cuisine. Looks like you're in luck for some home cooking."
    sol "... ... ..."
    kay "Heh. Probably not quite as good as you remember, huh?"
    kay "I'm afraid it's all thoroughly Cera-fied Ryuvian food. Probably tastes nothing like the real deal..."
    kay "Maybe you should help out the mess staff? Help make the taste more authentic."
    $dshow(70223)
    sol "No... I'm afraid I am a poor chef. I have no culinary knowledge beyond what Far Port berries are edible and how to roast fish and wildlife."
    kay "Sounds like a pretty tough life... We thought the Ryuvians all had advanced technology beyond what we can imagine. Sounds like that wasn't really the case though."
    $dshow(70221)
    sol "That is the truth. The Ryuvians' empire was far from monolithic. Instead, it was a cobblestone of thousands of conquered nations and vassals. In order to retain power, technology was held by the powerful. I have no doubt the average Ryuvian was far worse off than today's Alliance citizen."
    sol "I provided for myself for most of my life. Until I was taken in by the royal family, I gathered my food from the wild, like the majority of the peasants."
    kay "Doesn't sound easy. Uhh... The Versta cod stew's not bad. Pretty sure the Union delivered us a live batch last week."
    $dshow(70321)
    sol "Then... I shall partake."
    "The two of them received their food and sat down on a table."
    kay "So... How exactly did you find out Claude was a time traveler? You mentioned something about a vision earlier, right?"
    $dshow(70210)
    sol "Yes..."
    $dshow(70200)
    sol "Recently, I had a strange dream. No... Perhaps more of a vision, as it was far too real."
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    
    sol "I saw another version of myself... as well as you, captain. I speculate I may have fallen into another universe, far different from our own. Most likely, an episode orchestrated by our doctor, for purposes I do not fully understand..."
    $dshow(70222,blush=True) #this is one of those times I'd like her to look away
    sol "Ahem... T-the experience was... quite illuminating... On a number of different matters..."
    kay "Sounds like it. It does explain quite a number of things about Claude."
    $dshow(70223,blush=True)
    sol "Y-yes... Precisely so!"
    kay "Uhh... Sola? Something the matter? Your face is kind of red..."
    sol "Ah, the stew is exceptionally hot, no? I-it makes perspiration form all over my face... A-and down my b-back..."
    kay "Oy... Sola..."
    kay "You saw something in the vision, didn't you?"
    $dshow(70201,blush=True)
    sol "H-hugu!"
    $dshow(70422,blush=True)
    sol "W-what I saw was of no consequence whatsoever to the security of the ship. Certainly not a matter we need ruminate on..."
    $dshow(70220,blush=True)
    kay "Sigh... It's obviously bothering you. Hmmm... Come to think of it, you've been acting strange around me recently in my timeline too."
    kay "(Although this Sola has no idea, she's been acting unusually friendly ever since my rescue and in the desert...)"
    kay "Anyways... uhh... You know, you're free to say the things you want now. We don't live in a military dictatorship any longer. In fact, every Ceran is proud of the freedoms we won from the New Empire. Our civil liberties were won only through the blood of the martyrs. Those liberties won't exist unless we chose to exercise them."
    sol "Understood..."
    $dshow(70113,blush=True)
    sol "I am afraid this matter is far baser than such lofty ideals, however."
    "Sola took a large bite out of her cod."
    sol "... ... ..."
    sol "T-the truth of the matter is..."
    $dshow(70002,blush=True)
    sol "Is..."
    $dshow(70023)
    sol "A-alas... I nearly committed..." #sudoku
    sol "I am sorry!"
    hide sola with dissolve
    "With that, Sola beat a hasty escape, leaving her half eaten soup on the table."
    kay "Hey, Sola!"
    "Sola marched out of the mess hall and disappeared down the hallway."
    kay "(Ah, unbelievable...! Why can't she be more honest about her feelings!)"
    "Shields stood and followed after her."
    kay "(Tsch... I gotta go after her!)"
    
    play music "Music/Love_Theme.ogg" fadeout 1.5

    #Observation deck
    scene bg observationdeck with dissolve
    "After narrowing down the most likely places where Sola would go to collect herself, Shields ended up taking the lift to the Sunrider's observation deck."
    "This was the highest point of the ship, and surrounded by neoglass windows. From here, lookouts and optical equipment could navigate the stars and detect ships even if the ship lost power. Of course, the whole deck was sealed during battle so that it would not pose a threat to hull integrity." #so romantic.
    "Stars surrounded Shields as he looked around for Sola. On the opposite end of the observation deck was Cera, a glistening blue orb."
    "He spotted Sola staring off into space. As expected, she found tranquility here, surrounded by the enormous blankness of space."
    kay "Ahem..."
    $dshow(71000)
    sol "Ah... You have followed me."
    kay "I have. After all, you wanted me to chase after you, right?"
    sol "... ... ..."
    $dshow(70113)
    sol "I am sorry. It appears I have become a difficult woman..."
    sol "While I have always sought to be a cool headed and reasonable individual my whole life... I'm afraid this is the one matter which makes my heart waver and my mind run in circles..."
    $dshow(70123,blush=True)
    sol "My heart ached so much I could no longer face you..."
    sol "Yet... my feelings are a betrayal of my Queen... And ultimately moot, as this timeline will be erased from existence upon our mission's end."
    sol "I... am merely wasting our time and endangering the mission... b-by even pondering these possibilities... A-ah, these thoughts will merely make my aim falter... Will cloud my awakenings... I must s-strive to be as pure as the --"
    "Shields lunged for Sola and wrapped his arms around her."
    $dshow(70422,zoom=1.3,ypos=2400)
    sol "A-ah...!"
    "He pushed Sola's chin up."
    $dshow(70223,blush=True,zoom=1.3,ypos=2400)
    sol "... ... ..."
    $dshow(70201,blush=True,zoom=1.3,ypos=2400)
    "She closed her eyes and slightly parted her lips."
    "He leaned in. Their lips met." #so lewd!
    sol "... ... ..."
    kay "It's not like you to talk so much."
    kay "Eah, and I don't really see the problem anyways..."
    kay "Asaga properly confessed her feelings to my other self and received a rejection. In this timeline, her feelings received a clear answer before they twisted into hate. Besides, isn't her romance with the other Kayto Shields anyways?"
    kay "And morever, Claude told us that this universe will be recreated once our mission's over. It doesn't necessarily mean everything will be lost. In fact, we could just as likely re-emerge in the next universe together with our feelings intact."
    sol "... ... ..."
    $dshow(70223,blush=True)
    sol "I... am sorry... I... am merely complicating your situation..."
    sol "To thrust my emotions upon you... When you have so recently been wounded by the one you loved... I am truly a weak woman..."
    sol "Such a being... is undeserving of standing at your side..."
    kay "No."
    kay "I got a second chance to make everything right."
    kay "And I'm going to save Chigara this time too. She may be a spy, and she may have been sent to play with my feelings... But I know she was never aware of her directives herself."
    kay "Chigara's completely innocent as well. Everything was the Prototypes' doing."
    kay "So I'm not going to be on the floor, rolling in despair. Not when I have a chance to make things right again. So you don't have to worry about me, Sola!"
    kay "I'm... fine! Actually, I'm doing better than fine! Right now, I feel like I'm standing on the top of the world! Because I have a pretty girl like you by my side!"
    $dshow(70323,blush=True)
    sol "A-ah..."
    sol "S-speaking such shameless words... Y-you truly know how to embarrass me..."
    kay "Hah! Hah! Hah! Well, your captain was never one for subtlety!"
    sol "Indeed, it is so..."
    sol "Then... If the matter is settled..."
    "Sola stood on her tippy toes and closed her eyes again. Shields wrapped his arm around her back and pressed their lips together once more."
    "The two kissed, silhouetted by the faint blue light of a million stars."
    sol "Ah..."
    "Sola's body untensed, her pent up emotions finally released."
    "The two of them stared at the stars..."
    
    jump thefinalbattle

label icarikiss:
    
    #Hallway
    play music "Music/Cracking_the_Code.ogg" fadeout 1.5
    
    scene black with dissolvemedium
    scene bg hallway with dissolvemedium
    
    "Shields walked to the mess hall for some food and drink, thoroughly exhausted after the staff meeting."
    "He had told his future self everything he knew of the enemies' capabilities. Meanwhile, Fontana informed them that his best minds were working around the clock to restore control over their ships. However, it would be another two hours before the fixes were completed."
    "Chigara was safely detained in the brig. So far, there were no signs of the Prototype Leader assuming control over her."
    "In other words, Shields had done everything he possibly could to avert the Liberation Day massacre. Now all that remained was to wait and see if his efforts bore fruit."

    #Mess hall
    scene bg messhall with dissolve
    $dshow(41302)
    "He saw Icari sitting at a bar stool, sipping on a mug of beer. He leaned down against the counter."
    kay "Regulation strictly forbids the consumption of alcohol on yellow alert status. Looks like you're in quite a bit of trouble, merc..."
    $dshow(41411)
    ica "Heh. Looks like you're outta luck. You can't order me around when you're not the captain of this ship."
    ica "Who are you, the commander? C'mon, at least let me celebrate your victory."
    kay "Heh. It's still too soon to celebrate, Icari. We might have managed to send the transmission to Fontana and detain Chigara, but the battle still has to be won."
    "Icari took a long chug of her drink."
    ica "Heh..."
    $dshow(41412)
    ica "Relax, cap. It's non-alcoholic."
    "Icari motioned the bartender to pour Shields a mug as well."
    ica "Cheers. To changing the future."
    kay "I can drink to that."
    "The two of them clinked their glasses together and took a sip."
    $dshow(40212)
    ica "Well... uhh... You did pretty good, Shields. I admit, even I got a little jittery when you delivered that whooper right to your clone's face, what with the wall of marines surrounding us. But uhh... That was a pretty gutsy move. And looks like it paid off too."
    $dshow(40421)
    ica "Mah, I guess I can give you that much credit. I'm not saying I like you or anything but... heh. You're not half bad."
    kay "Just another day at the job."
    $dshow(40413)
    ica "Heh. You can say that again."
    $dshow(40522)
    ica "Say, so... uh... What do you suppose will happen after this? Will this universe really completely be re-written?"
    kay "I'd bet the full details are too complicated for the human brain to even comprehend. In the end though... We'll all continue to exist, completely oblivious to the fact that I traveled back in time to rewrite the future. In the end, as long as the massacre never occurs, that outcome is within acceptable mission parameters."
    ica "Yeah... But... I guess a part of me's still scared if everything will just continue the way things are now... What if something weird happens?"
    kay "Weird?"
    $dshow(40523,blush=True)
    ica "W-well... uhh... Just using this as a hypothetical, but let's say uhh... I were to get really drunk and make out with you or something... Would that event still be in the next universe? Or will it be as if it never happened?"
    kay "What the hell!? Oy, what are you saying!?"
    $dshow(40320)
    ica "Idiot, I said it's just a hypothetical! I'm providing a \"what if!\" Ah, nevermind! Forget I even said anything!"
    $dshow(40313)
    ica "Aaah, I should have known a schoolboy like you would lose his marbles at even the passing mention of scoring with a girl! This is why I can't count on you for anything! Tsch!"
    kay "Oy..."
    $dshow(40520)
    ica "Tsch, bartender, I need another!"
    kay "What's even the point of drinking more non-alcoholics..."
    $dshow(40410)
    "... ... ..."
    "... ..."
    "..."
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    "And yet, three more jugs later..."
    $dshow(41311,blush=True)
    ica "Ya know Shields, I've been wantin' to know for a while..."
    ica "You're on a boatful of eligible women, right? So just which one of us has the most brownie points on your list?"
    kay "I'm afraid that information's classified."
    $dshow(41101,blush=True)
    ica "Tsch."
    $dshow(41111,blush=True)
    ica "Ya know, the quicker you get over the Chief, the better. Ah, well, it's pretty sad that she turned out bein' a Prototype spy n' all, but you can't let it get to you... Sometimes stuff just doesn't work out..."
    ica "Your personalities clash... Turns out you like your instant ramen cooked through, but she wants it hard... You can only work in the mornings, while she wants to stay up all night... Or she's actually an enemy sleeper agent. Irreparable shit like that happens all the time."
    kay "The fuck!? One of those things is not like the others!"
    $dshow(41012,blush=True)
    ica "Aaah shadup, I'm just tryin' to give you some life advice here..."
    kay "Well, how 'bout you, Icari? Are you and the lieutenant... uhh..."
    $dshow(41411,blush=True)
    ica "Trying to change the subject? 'Sides don't be an idiot... Soldierboy turned out bein' not bad... But seriously, goin' out with a straight lace like her? Aah, I bet we'd get tired of each other in less than a day..."
    $dshow(41412,blush=True)
    ica "Aah, it just can't be helped huh... Looks like I've gotta have a one night stand with you, just so you can get over the chief. Ah, wanna do it right now? Hmph! A schoolboy like you should just be grateful I'm offering!"
    kay "Oy... You're always trying to act so cool... But I bet if I actually take that offer seriously, you'll just collapse like a big house of cards."
    $dshow(41201,blush=True)
    ica "H-hmph! W-why would I be scared! 'Sides, don't get the wrong idea!"
    $dshow(41211,blush=True)
    ica "I-it's not like I've ever liked you! This is just a favor! Consider it a 'lil fixer upper so you can go back to full combat status. All for the sake of the ship!"
    $dshow(41001,blush=True)
    ica "Aaah, all guys are so easy to deal with. Pretty much any male ailment can be fixed by waking up with a naked girl the morning. Heh, if only women worked that way..."
    $dshow(41011,blush=True)
    ica "C'mon, let's go! We can take care of it right now!"
    kay "(I can't believe this girl is actually trying to pull this little gag on me...)"
    kay "(I bet as soon as I accept, she's gonna just say \"psych!\" and act all high and mighty that I fell for her little play hook, line, and sinker...)"
    kay "(Hah! Let's see just how far she can keep going with this prank until her façade crumbles apart!)"
    kay "All right, Icari."
    "Suddenly, Shields put both his hands on her shoulders."
    $dshow(41112,blush=True)
    ica "Oy, what's with the serious look all of a sudden..."
    kay "I've made up my mind. It's you who I love."
    $dshow(41212,blush=True)
    ica "E-ehh!?"
    kay "I... love you, Icari. I've always loved you. That's why I chose you to help me in this mission."
    $dshow(42000,blush=True)
    ica "I-i-idiot! I-I never said anything about l-l-love! W-what are you doin', bringing feelings into this?"
    $dshow(41310,blush=True)
    ica "I-I... ain't gonna fall for this so easily! Hah, you're just tryin' to play along, aren't you?"
    kay "W-what...? You mean everything you said was... just a joke...!?"
    $dshow(41012,blush=True)
    ica "O-o-of course...! Oy, Shields..."
    kay "G-guck...! I..."
    kay "This is..."
    "Shields face twisted as if Icari had just impaled him with her katana."
    $dshow(41112,blush=True)
    ica "Oy, oy... P-pull yourself together...!"
    $dshow(40223,blush=True)
    ica "I'm sorry, all right! D-damn, uhh..."
    kay "I... won't accept this, Icari!"
    kay "You're... just being tsundere, aren't you!? I know you actually have feelings for me!"
    "He pushed her closer and raised her chin with a finger."
    kay "This is the only way we can confirm our feelings for each other!"
    $dshow(40323,blush=True,zoom=1.3,ypos=2400)
    ica "O-ooy!!!"
    "He came in, lips puckered."
    "Icari's eyes bulged and twitched as she trembled."
    ica "I... uhh... uhh...."
    ica "H-hhuuuuuu..........."
    "Just a second before their lips met, Shields stopped his approach."
    kay "(I guess this is enough to teach her a lesson...)"
    kay "(Hah! If only she could see the look on her face right now!)"
    $dshow(40201,zoom=1.3,ypos=2400,blush=True)
    "Except at that moment, Icari leaned forward, pressing their lips together."
    kay "!!!!"
    kay "What are you doing!?"
    $dshow(40523,blush=True)
    ica "B-but... I thought... you... we..."

    $dshow("icari armscrossed frown neutral sad blush tears")

    "Icari stared at Shields, tears slowly pooling up in her eyes." 
    kay "O-oy... Don't tell me..."
    $dshow(40022,blush=True,cry="tears")
    "Icari's face slowly turned the same colour as the side of a PACT warship as she realized Shields was actually just pranking her."
    kay "(She... ended up falling for MY prank!? Right after when she tried to get me with the same joke!?)"
    "Icari shot up off her stool."
    $dshow(42000,blush=True,cry="tears")
    ica "Y-y-y-you... IDIOT!!!"
    ica "Aaahhh!!! I hate you!"
    hide icari with dissolve
    "With that, she stormed away."
    kay "(Ah... Great...)"
    kay "(So... in the end, she tries to act all cool and prank me, but as soon as I one-up her joke, she falls for it instantly and then gets pissed off it was all a joke...)"
    kay "(This woman... Truly is a mess of contradictions...)"
    kay "H-hey, Icari, wait!"
    "Shields ran off after her."

    #Hallway
    scene bg hallway with dissolve

    $dshow(41210)
    ica "Don't follow me! Get lost!"
    kay "Oy, now is not the time for the tsun act..."
    ica "Would you stop!? I... I'm not acting tsun! There is no tsun! There is no dere!"
    kay "Ay... You know, when a tsundere screams, \"Don't follow me,\" isn't that pretty much a demand that I follow?"
    $dshow(41110)
    ica "Y-y-you...!"
    "Icari spun around and faced Shields, her face contorting with humiliation and fury."
    $dshow(41211)
    ica "What the hell are you trying to pull!? P-p-pretending to make out with me as... some kinda sick joke...!"
    kay "Like you can talk! You're the one who started it!"
    kay "One night stand? Hah! You can barely even handle a kiss! Aah, I guess after all that, you're the real schoolgirl here!"
    $dshow(42000,blush=True)
    ica "Y-yoooouuuu.....!!"
    ica "I... am not a schoolgirl! A k-kiss isn't even a big deal! Hah! Had so many kisses before it's... nothing special! I could kiss you right now without batting an eyelash!"
    kay "Oh yeah!? Let's see it!"
    $dshow(40320,blush=True)
    ica "T-tsch... A kiss is nothing!!! I've... killed dozens of guys while seducing them w-w-w-with my body! H-hah! Y-you better prepare yourself!!! Who knows, I might just decide to stick a knife into the back of your head while we're making out! Hah! Hah! "
    ica "H-hah, all guys are such pigs! Just a little strip show, and you all drop your guard! Must be 'cause all the blood drains out your brains and into your dicks!"
    kay "You're... stalling for time, aren't you?"
    $dshow(40000,blush=True)
    ica "H-hugu!"
    $dshow(42000,blush=True)
    ica "A KISS IS NOTHING!!!"
    kay "(She's screaming that mostly for her sake...)"
    $dshow(40201,blush=True,zoom=1.3,ypos=2400)
    "Icari marched forward and pressed her mouth against Shields', wrapping her arms around his neck. Their tongues sloshed against each other, lapping up each other's taste. She wrapped her lips around his tongue and sucked it deep into her mouth."
    kay "(She's... actually... not bad...)"
    "The slippery warmth of her mouth relaxed his mind and made his crotch tingle."
    "They finally disengaged, panting for breath."
    $dshow(41410,blush=True)
    ica "S-see!? Hah! A kiss is nothing!"
    "Just then, a third voice spoke, bringing vapid horror to Icari's face."
    
    stop music fadeout 1.5
    
    $dshow("kryska neutral neutral surprise neutral",xpos=0.75)
    kry "M-mercenary!?"
    $dshow(41212,blush=True,xpos=0.25)
    ica "E-EEEEE!!!!"
    ica "T-t-t-this isn't what it looks like! I-I swear!!!!"
    kry "You know fraternization with your fellow servicemen is highly unprofessional. Of course, that is exactly the sort of disregard for the rules that I've come to expect from a civilian contractor such as yourself..."
    
    $dshow("kryska neutral neutral surprise angry")
    
    kry "But to actually... display wanton acts of physical affection in public... and with the ship's highest ranking officer, no less...! This is reproachable conduct of the highest order!"
    kay "Actually, Kryska... Uhh... I'm not the captain. I'm the new Kayto Shields. "
    $dshow(51022)
    kry "O-oh! I... see!"
    kry "Then..."
    kry "... ... ..." 
    
    play music "Music/Monkeys_Spinning_Monkeys.ogg" fadeout 1.5
    
    $dshow("kryska fistup happy neutral angry")
    kry "I believe congratulations are in order! Hah! Hah! Hah! If there are no violations of protocol, then what is the problem?"
    $dshow(40323)
    ica "E-EHH!?"
    kay "(What a sudden 180 change in opinion!)"
    $dshow(50000)
    kry "Eah, to think that my comrade Icari would finally fall in love! Hah, I feared that after the war, Icari would elect to raise a household of felines instead of finding a romantic partner, but I see that my worries were ill founded!"
    kry "To think that she was capable of showing such affection to a fellow human being! Hah! My concerns for her future have all but evaporated!"
    kry "This is wonderful news! I must go tell everyone!"
    $dshow(42000,blush=True)
    ica "W-w-w-wait!!! I-i-i-i-i-i-i-it's... NOT LIKE I LIKE THIS LOSER!!! I was... just.... AHHHH!!!!!!!"
    $dshow(51201)
    kry "Why, I must prepare to serve my duties as the maid of honor at once!"
    kay "(We're already getting married...?)"
    hide kryska with dissolve
    "With that, Kryska marched off with a proud look on her face, resembling a mother who had just learned that her daughter had found her ideal match."
    $dshow(40020)
    "Icari stared on, her face devoid of life."
    "Shields waved his hand in front of her."
    kay "Oooy... Are you all right?"
    $dshow(40102)
    ica "Heh... Hehehe..."
    "She could only twitch as she emitted hollow laughs..."
    
    jump thefinalbattle

label thefinalbattle:
    
    stop music fadeout 1.5
    
    #Black
    scene black with dissolvemedium

    "... ... ..."
    "... ..."
    "..."
    
    play music "Music/Fallen_Angel_Pt2.ogg" fadeout 1.5
    
    "While Shields had momentarily caught a respite thanks to his actions, he had no idea that his biggest crisis was still yet to come."
    "Shortly after spending time with [girl], he received a summons to the bridge."
    
    scene bg bridge with dissolve
    
    show kayto:
        xpos 0.25
    with dissolve
    $dshow("ava armscrossed neutral narrow angry",xpos=0.75)
    
    "He arrived to see the tense faces of the command crew."
    kay "What happened?"
    kayo "Chigara's escaped. We don't know how, but she managed to open her cell."
    kay "And security?"
    kayo "Eight marines, all in serious condition when a nearby conduit blew. Obviously not a coincidence."
    kayo "I've already got security turning the ship inside out to find her, but she somehow managed to manipulate all our cameras too. Took us a good half hour until we realized that all the footage was fake."
    kay "We're up against a Prototype here... Her brain's been artificially augmented to perform feats beyond our imagination..."
    kay "Her objective's got to be escape. We need to disassemble the Liberty, now."
    ava "We've already placed it in lockdown-"
    kay "That won't be enough. Start by removing the fusion reactor, and then take off all the limbs."
    kayo "Damn... We could have used it during the battle... To think we have to take apart our own ryder..."
    kay "Without a pilot, there's no point in keeping it. We need to avoid the worst case scenario of having it used against us."
    kayo "Tsch. Do what he says, commander. You have authorization to remove the Liberty's reactor. Do it immediately."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Sir!"
    kayo "Just disassembling the Liberty won't be enough though... She could still escape on a shuttle... or a lifepod... or any of the other ryders."
    kay "(Still plenty of holes in the plan, huh...)"
    
    play sound "sound/warning.ogg"
    
    "Everyone's anxiety peaked when the ship's alarm went off."
    kay "(What now?)"
    
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5
    $dshow("ava handonhip shout narrow angry")
    
    ava "Contacts!"
    kayo "Red alert! Cease the resupply operations and man battle stations!"
    ava "A PACT Loyalist fleet, headed our way! Approximately 300 strong."
    kayo "How did they get past the Alliance's defensive line!?"
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "Tsch... We are getting reports of a single PACT ryder decimating their forces. The Combined Fleet has been split into two, allowing a PACT strike fleet to pass through and approach the rear lines."
    kay "A single PACT ryder... That can only be one thing..."
    
    show nightmare_approach
    show black:
        alpha 0.5
    with dissolve
    
    "Shields still vividly remembered the grotesque power of the Nightmare Ascendant. In the previous timeline, they had only just barely defeated it thanks to the power of the Combined Fleet and Fontana's forces. But this time, the conditions of the battle were completely different..."
    "Instead of fighting in the front lines with the full support of the Alliance, they now faced the Nightmare Ascendant in an ambush. Further, Fontana's fleet was still not operational."
    
    hide nightmare_approach
    hide black
    with dissolve
    
    kay "It's the Nightmare Ascendant. An ancient Ryuvian ryder now controlled by the leader of the Prototypes. On top of overwhelming firepower and defenses, the Prototype Leader can somehow awaken just like Asaga and Sola, making it nigh invincible."
    kayo "And you say you defeated it in your timeline?"
    kay "Yeah... But only with the help of the Combined Fleet and Fontana's allied forces..."
    kayo "Tsch. Sounds like you were playing on easy mode when you went through this."
    "The other Shields turned towards the tactical map."
    kayo "We should have seen this ambush coming. With their spy onboard the Sunrider exposed, and Fontana onto their sabotage efforts, the Prototypes' best bet is to kill us all before Fontana's ships enter into play."
    kay "(That means you've already thought of a plan, right?)"
    kayo "Unfortunately, our counter tactics are limited... The Sunrider still hasn't completed its resupply, while the Liberty is out of commission. Even knowing the ambush was going to occur, our only option was to meet it head on..."
    
    $dshow("ava handonhip talk narrow angry")
    
    ava "The Combined Fleet is still tangled with a sizable remainder of PACT ships... The Alliance will not be able to spare many ships to come to our aid."
    ava "If we fall here, the PACT strike fleet will completely rout the resupply line... Meaning, the Combined Fleet will then face an attack from the rear, with no fall back position..."
    kayo "Put Fontana on the line."
    ava "Sir."
    
    hide ava with dissolve
    show fontana:
        xpos 0.75
    with wipeup
    
    fon "Tsch. Looks like Alice has made her move."
    fon "We are still an hour away from removing the virus from our ships. You'll have to hold out until then."
    kayo "We don't have an hour, Fontana. I don't care if you leave half your ships behind. Get your forces in order and assist us with whatever you can muster."
    fon "Tsch. Very well. The sabotage is most extensive on our assault carriers. If we prioritize repairing our fast cruisers only, then we could be by your side in 15 minutes."
    kayo "All right. No choice."
    
    hide fontana with wipedown
    
    "After Shields cut the channel with Fontana, Asaga's voice crackled through the comm."
    asa "This is the ryder squad! Standing by!"
    kayo "Good. Begin sortie immediately! The map filling up with red all around us."
    kayo "Watch out for the new PACT ryder. Target designation Ascendant. It's lost technology, and its pilot can awaken, just like you."
    asa "Underst--"
    asa "What the--"
    
    play sound "sound/mech_boost1.ogg"
    
    "Suddenly, the roaring of a ryder's thrusters peaked the comm's output."
    asa "EEEHHH!?!? T-the Black Jack's takin' off without me!!!!"
    kay "Shit!"
    kayo "Close the hangar gate!"
    
    $dshow("ava handonhip shout narrow angry")
    
    ava "Negative! If we use the emergency override now, we won't be able to launch any of the other ryders either!"
    "Shields tore himself from the tactical map and ran towards the hangar."
    kayo "Where are you going?"
    kay "No point in having two Kayto Shields on the bridge!"
    kay "I'm... leaving the battle to you. You're still the captain of this ship..."
    kay "I'm going to stop Chigara!"
    kayo "All right."
    kayo "Good luck... partner!"
    kay "Yeah. Good luck."
    "With that, Shields entered the lift and went down to deck 2."
    
    scene black with horizontalwipe
    scene bg hanger_noryders with horizontalwipe

    "Shields entered the hangar to see the deck crew desperately trying to keep the Black Jack from launching."
    "They had somehow managed to attach a ceiling mounted electromagnetic clamp onto one of the shoulder particle guns, while a spare rifle jammed the launch rail."
    kay "Shit...! No, GET BACK!"
    
    play sound "sound/mech_boost2.ogg"
    
    "The Black Jack leaned down and fired its engines, sending the crew scattering in every direction. The hangar groaned as the ceiling superstructure holding the clamp slowly bent against the Black Jack."
    "Asaga arrived on a buggy."
    
    play sound "sound/carengine.ogg"
    $dshow("asaga zexcited_plugsuit yell neutral angry")
    
    asa "Capt'n! We've got a situation!"
    kay "No kidding. Come on, we've got to figure out a way to keep Chigara from escaping with your ride!"
    
    show layer master at tr_xshake
    play sound1 "sound/flakguns_deep.ogg"
    play sound "sound/explosion2.ogg"
    
    "The ship's flak guns echoed through the hangar. The ship shook as a missile impacted, sending Shields to the floor."
    kay "Shit... As if that wasn't enough, looks like the battle's begun..."
    "Steel groaned overhead. Shields looked up just in time to see the steel supports holding the clamp finally give out."
    kay "Watch out!!"
    
    show layer master at tr_xshake
    play sound "sound/kinetichit.ogg"
    hide asaga with dissolve
    
    "He dived on top of Asaga as steel and concrete rained around them. Luckily, the debris fell a short distance away, covering both of them in dust, but not causing any injuries."
    "Finally loose, the Black Jack hit its thrusters and flew across the hangar."
    kay "(No! It's gonna get away!)"
    "At the last second, the Paladin stepped out of its maintenance bay and blocked the exit."
    
    scene kryska_cockpit_orb1 with dissolve
    
    kry "Halt!"
    
    play sound "sound/mech1.ogg"
    
    "The Black Jack stopped and drew its assault rifle."
    
    scene bg hanger_noryders with dissolve
    $dshow("asaga zneutral_plugsuit talk neutral up")
    
    kay "No...!"
    "He grabbed Asaga by the elbow and sprinted for cover."
    
    play sound "sound/Flak.ogg"
    play sound1 "sound/gore.ogg"
    
    show white:
        alpha 0.5
    pause 0.1
    hide white
    pause 0.1
    show white:
        alpha 0.5
    pause 0.1
    hide white
    pause 0.1
    show white:
        alpha 0.5
    pause 0.1
    hide white
    
    "The Black Jack unleashed a torrent of bullets inside the hangar, sending shrapnel ricocheting throughout the hangar. An unlucky crewman took a brick sized fragment to the shoulder, cleaving a foot long opening down his chest. Instantly killed, his body sprayed blood as it fell to the ground."
    "Shields suppressed his nausea as shrapnel bounced all around him."
    
    play music "Music/Danger.ogg" fadeout 1.5
    scene kryska_cockpit_orb1 with dissolve
    
    kry "Fool!!"
    
    play sound "sound/mech_boost2.ogg"
    
    "The Paladin, unaffected by the small caliber fire thanks to its armor, shot forward and collided with the Black Jack. The two steel behemoths struggled against each other like two enormous sumo warriors."
    "The Black Jack opened its missile pods."
    kay "Ooohh...!!!"
    kay "(If it fires off its missiles in here, the whole ship's gonna blow!!)"
    
    play sound "sound/mech_boost2.ogg"
    
    "Just then, the Phoenix shot forth, katana drawn."
    
    scene icaricockpit_orb with dissolve
    
    ica "Hiyaahh!!!"
    
    play sound "sound/mechfligh.ogg"
    
    "The Black Jack shot its reverse thrusters, narrowly avoiding getting cleaved in half. It spun its pulse gun into sword mode and activated its laser beam."
    ica "Heh... Never thought I'd be fighting the Black Jack in the ship's hangar..."
    "The Black Jack hit its wing thrusters, boosting forward."
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    
    "The Phoenix nimbly moved out of the way, sending the Black Jack crashing into a maintenance bay. Shields braced his head against the cacophony of collapsing steel. The Black Jack turned around and swiped its laser beam, but the Phoenix once again proved too fast, spinning out of the way."
    ica "Tsch... This place is too damned small... And I can't use my assault guns either..."
    
    play sound "sound/mech_boost2.ogg"
    
    "The Phoenix shot upwards, skimming against the ceiling, and came down in a powerful helm crusher."
    
    play sound1 "sound/explosion2.ogg"
    play sound "sound/Sword Shing 2.ogg"
    
    "The Black Jack deflected the Phoenix's katana with its black iron blade. The Phoenix ducked as the Black Jack's beam sword slashed laterally, cutting through another maintenance bay."
    ica "Too slow!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "Its beam sword still moving on its own momentum, and its black iron sword too heavy to raise in time, the Phoenix shot forward and deftly dug its sword into the Black Jack's shoulder."
    ica "Tsch... Can't... get enough momentum going on here...!"
    ica "Not to mention this gravity's killing my speed...!"
    
    scene bg hanger_noryders with dissolve
    
    "Shields grabbed a handheld microphone."
    kay "Icari! The missile pods!"
    ica "Crap!"
    "Just as Icari realized the Black Jack could destroy the entire ship at any moment, the Black Jack tumbled to the floor."
    
    play sound "sound/chargeup.ogg"
    
    "Shields saw the Bianca approaching it, its grav gun active."
    
    scene claudecockpit_orb2 with dissolve
    
    cla "I-I've got this!"
    kay "Claude! Pull the reactor out!"
    cla "U-understood!"
    "Just then, Shields realized he had made a huge mistake."
    kay "(Wait a minute...! E-entrust Claude with pulling out a highly explosive fusion reactor with a grav gun!?)"
    "Before Shields could retract his order, sparks flew from the back of the Black Jack as its reactor was torn out."
    
    scene white with dissolve
    
    "He squeezed his eyes shut and pressed himself flat on the floor, expecting the worst."
    
    scene bg hanger_noryders with dissolve
    
    "Miraculously, when he slowly opened his eyes, the reactor was safely on the floor, and everyone was still alive."
    "The flight crew flooded the hangar to contain the situation."
    "With a breath of relief, he ran towards the now deactivated Black Jack as well."
    kay "All right everyone! Don't open the cockpit until ship security arrives! Put the reactor into cold sleep!"
    cre1 "Sir!"
    
    $dshow("asaga zarmscrossed_plugsuit frown neutral sad")
    
    asa "Huuu... I-is the Black Jack all right?"
    kay "Looks like its arm's gonna have to be replaced with a spare... And it also needs a new reactor. But it's nothing we can't handle."
    kay "Everyone else, you're needed outside! Sortie and protect the ship!"
    "Pilots" "Copy!"
    "With most of the hangar destroyed, the remaining ryders had no choice but to slowly file out of the gate instead of using the linear rail."

    scene black with horizontalwipe
    scene bg bridge with horizontalwipe
    
    show kayto:
        xpos 0.3
    with dissolve
    $dshow("ava handonhip shout narrow angry",xpos=0.7)
    
    "Meanwhile, the other Kayto Shields was caught in the middle of another life or death struggle..."
    ava "Three PACT battleships, approaching! Torpedo lock detected!"
    "Shields looked at the tactical map. The bulk of the Combined Fleet was still tied up with the main PACT Fleet. Roughly a hundred Alliance cruisers and two dozen battleships were stationed at the resupply line, but more than half of them were already damaged the prior day and locked down for repairs, or in the middle of resupply operations."
    "Meaning, he was both hopelessly outnumbered and outgunned."
    kay "Fire ventral thrusters!"
    "The Sunrider shook as it descended, coming alongside a trio of Alliance cruisers."
    kay "(They won't be firing their main guns, but their flak guns should still be operational...)"
    ava "Torpedoes, incoming! Three, from above!"
    
    play sound "sound/flakguns_deep.ogg"
    
    "The Sunrider's flak guns burst around the ship, lighting the black void of space up with a million explosions."
    kay "Come on... come on..."
    
    play sound "sound/flakguns_deep.ogg"
    
    "He exhaled when the flak guns on the cruisers activated, adding to the Sunrider's wall of fire."
    
    play sound "sound/explosion2.ogg"
    
    "The nose of the forward torpedo fragmented as soon as it entered the flak shield, and spun wildly before getting pulled apart by the g-forces."
    kay "(One down...)"
    "The second torpedo stubbornly continued through the vortex of explosions, sprayed with shrapnel but still not losing structural integrity."
    "Sweat poured down Shields' forehead."
    "All he could do was pray."
    
    play sound "sound/explosion1.ogg"
    
    "Finally, the torpedo gave away to the relentless assault of shrapnel, splintering into a million shreds."
    "But Shields' luck had run out. The final torpedo survived the flak and headed on a direct course for the Sunrider's tower."
    ava "All hands, brace for impact!"
    
    play sound "sound/explosion4.ogg"
    show layer master at tr_xshake
    
    "Shields gripped the table as the bridge shook."
    ava "Hit on deck 1! Fires reported on section 14. Lose of pressure at section 15!"
    ava "No damage to core systems!"
    "The PACT battleships were still too far away for the Sunrider to engage. Their missiles would be instantly shot down by flak, while their lasers were useless against the enemy's shields."
    kay "Where are our ryders!?"
    ava "The linear rail is inoperative! They are still attempting to sortie!"
    "Just then, the Phoenix shot out from the mouth of the ship."
    ica "Sorry for being late. Had to walk out."
    "The rest of the ryders flew out, one by one."
    kay "What about the Black Jack?"
    ica "Temporarily out of commission. Crew's trying to put it back together as quick as they can!"
    kay "Tsch... Outnumbered... And now lacking both the Liberty and the Black Jack..."
    "Shields racked his head for a strategy."
    ava "Power surge detected from enemy battleships!"
    
    play sound "sound/Laser 1.ogg"
    
    "Crimson beams of light shot from the battleships, burning trails of fire across the hull of the Sunrider."
    
    play sound "sound/explosion1.ogg"
    
    "Shields hung on as the bridge swayed. He heard the groaning of steel as the ship's structural latticework melted away."
    kay "(Without the Liberty's shields, we're toast!)"
    
    play sound "sound/Laser 1.ogg"
    play sound1 "sound/explosion2.ogg"
    
    "More lasers cut through the ship. A console burst, flinging a crewman to the ground with facial burns."
    kay "Tsch... Is this... the end?"
    
    play sound "sound/large_warpout.ogg"
    
    "Just then, the space around the battleships distorted. A battlegroup of 50 PACT fast cruisers emerged from warp."
    
    play sound "sound/railgun2.ogg"
    pause 0.4
    play sound1 "sound/railgun2.ogg"
    pause 0.4
    play sound2 "sound/railgun2.ogg"
    pause 0.4
    play sound3 "sound/railgun2.ogg"
    
    "The daggers dropped down above the battleships and loosed kinetic round after kinetic round as they dived towards the enemy's huge profile."
    "The battleships attempted to return fire, but from the front, the fast cruisers were hardly larger than corvettes. The battleships' rounds shot past as fire rained down from above."
    "Shields sighed in relief as the battleships fragmented from the relentless hailstorm of steel."
    
    hide ava with dissolve
    show fontana smirk:
        xpos 0.7
    with wipeup
    
    fon "My apologies for keeping you waiting, Shields."
    kay "I never thought I'd actually be glad to see your face, Fontana..."
    fon "Now is not the time to jest. The situation is still dire."
    
    hide fontana with dissolve
    $dshow("ava handonhip shout narrow angry")
    
    "Without a moment's break, Ava turned to Shields."
    ava "Captain! Incoming enemy! It's the--"
    
    play music "Music/Posthumus_Regnum.ogg" fadeout 1.5
    scene nightmare_approach with dissolve
    
    "The Nightmare Ascendant appeared before the Sunrider, its wings proudly outstretched."
    kay "So you're the enemy leader I've heard so much about..."
    
    scene alice_cockpit2 with dissolve
    
    ali "Shields... I have no idea how you managed to intercept our spy... Or discover the sabotage done to Fontana's ships..."
    ali "But all of that will be meaningless if you and the Alliance fleet are destroyed!"
    ali "All units, destroy the Sunrider! ATTACK!!!"
    
    scene bg bridge with dissolve
    show kayto:
        xpos 0.3
    with dissolve
    $dshow("ava handonhip shout narrow angry",xpos=0.7)
    
    "A swarm of Prototype units launched from PACT carriers."
    ava "Contacts!"
    ali "Hahahahaha!!"
    
    scene nightmare_attack
    
    $ renpy.movie_cutscene("3DCG/nightmareattack.webm",stop_music=False) 
    pause
    
    "The Ascendant's wing fliers detached and darted towards the Sunrider."
    
    scene icaricockpit with dissolve
    
    ica "Tsch! We'll hold the line here!"
    
    play sound "sound/Flak.ogg"
    
    "The Phoenix opened fire and sprayed the fliers with assault rounds, but they nimbly flew out of the Phoenix's firing arc."
    ica "Fast little buggers!"
    
    play sound1 "sound/dronefly.ogg"
    play sound "sound/Laser 1.ogg"
    
    "Two fliers circled around and shot forth spears of light. The Phoenix fired two of its wing thrusters, narrowly dodging the beams in a high g corkscrew."
    
    scene solacockpit1 with dissolve
    
    sol "Providence awaits..."
    
    play sound "sound/heartbeat.ogg"
    scene solacockpit2
    show solacockpit2b:
        alpha 1
        ease 0.5 zoom 1.5 alpha 0
    with dissolve
    
    "Sola's right eye ignited as she awakened. The movement of the drones suddenly slowed to Sola's senses, as if they were swimming underwater."
    
    play sound "sound/Sola Sniper.ogg"
    
    "Focusing on her target, she lined up a shot and fed the Seraphim's rifle with power. A flash later, Sola's shot tore a hole into the drone's midsection, before erupting it into fireball."
    
    scene icaricockpit with dissolve
    
    ica "Thanks!"
    
    play sound "sound/dronefly.ogg"
    
    "The other drone spun around and came at the Phoenix for another pass. But this time, Icari was prepared."
    
    play sound "sound/mech_boost2.ogg"
    
    "She stepped on her foot pedals, feeding maximum energy to the engines. The Phoenix shot forward, on an intercept vector for the drone."
    ica "HIYAH!!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "With near inhuman finesse, the Phoenix shot past the drone, katana drawn, and sliced it from front to end."
    
    play sound "sound/explosion1.ogg"
    
    "The rear of Icari's cockpit illuminated as the drone exploded behind her."
    ica "Two down!"
    "Before Icari could celebrate, a dark shadow stretched across her ryder."
    ica "Shit!"
    
    play sound "sound/mech_boost2.ogg"
    
    "She spun out of the way seconds before the Ascendant descended upon the Phoenix and cleaved it apart with its great sword."
    ica "That's one helluva huge sword!"
    
    scene alice_cockpit2 with dissolve
    
    ali "Haha!"
    "The Ascendant swaggered towards the Phoenix, sword raised above its head."
    
    play sound "sound/Sword Shing 2.ogg"
    
    "Icari barely managed to block the Ascendant's blade in time. Despite its titanic size, the Ascendant moved quick as a viper."
    ica "(Tsch... T-that thing has three reactor cores! No matter how you look at it, I'm out matched here!)"
    
    play sound "sound/Sword Shing 2.ogg"
    play sound1 "sound/shatter.ogg"
    
    "The Ascendant merely shoved the Phoenix out of the way. With another mighty downwards strike, the Phoenix's katana shattered into a million pieces."
    
    scene icaricockpit with dissolve
    
    ica "Shit!"
    
    play sound "sound/dronefly.ogg"
    
    "Icari fired her wing thrusters in a panic, but her moment of carelessness allowed a drone to line up a shot."
    
    show layer master at tr_xshake
    play sound "sound/Laser 1.ogg"
    play sound1 "sound/explosion2.ogg"
    
    "The beam tore through one of the Phoenix's wing thrusters, sending it spiraling out of control."
    ica "A-arggh!!!"
    
    scene solacockpit2 with dissolve
    
    sol "Providing assistance."
    
    play sound "sound/Sola Sniper.ogg"
    
    "Sola rained down shots. Alice's eyes ignited blue as she awakened and deflected the bullets with two swings of the great sword."
    sol "I-impossible...!"
    
    scene cg_nightmarefire1_nodamage with dissolve
    play sound "sound/legion_laser.ogg"
    scene cg_nightmarefire2_nodamage with dissolve
    
    "The tip of Ascendant's particle gun glowed red as it let forth a scarlet lance, cutting into the Seraphim's leg and slicing apart its scanner dish."
    sol "H-hygnn!!"
    kay "Sola! Are you all right!?"
    
    scene solacockpit3 with dissolve
    
    sol "Y-yes... But the Seraphim is no longer fit to fight..."
    sol "Returning to base."
    
    scene icaricockpit with dissolve
    
    ica "T-the Phoenix is out too, capt! Without a sword, I can't do anything out here!"
    
    scene kryska_cockpit1 with dissolve
    
    kry "Hiyah! I'll hold it back while you two escape!"
    ica "Tsch... Don't do anything crazy while I'm gone, soldierboy!"
    kry "Of course!"
    "The Paladin banged its rifle against its shield and moved in to cover the two ryders' escape."
    
    play sound "sound/shotgun.ogg"
    pause 0.4
    play sound1 "sound/shotgun.ogg"
    pause 0.4
    play sound2 "sound/shotgun.ogg"
    pause 0.4
    play sound3 "sound/shotgun.ogg"
    
    "Its rear cannons rotated forward and shot high density black iron towards the Ascendant."
    ali "Useless!"
    
    play sound "sound/mech_boost2.ogg"
    
    "The Ascendant fired one of its knee thrusters, corkscrewing towards the Paladin."
    kry "Tsch!"
    
    play sound "sound/missile.ogg"
    
    "All of the Paladins' missile pods opened, sending streams of smoke spiraling outwards. The Ascendant nimbly dodged through the missiles. The missiles which did impact put nary a scratch the ancient ryder's frame."
    
    scene cg_claudecockpit with dissolve
    
    cla "Hooyah!!!"
    
    play sound "sound/chargeup.ogg"
    
    "At that moment, the Bianca used its gravity gun to immobilize the Ascendant."
    cla "Now!"
    kry "Thanks!"
    
    play sound4 "sound/missile.ogg"
    play sound "sound/shotgun.ogg"
    pause 0.4
    play sound1 "sound/shotgun.ogg"
    pause 0.4
    play sound2 "sound/shotgun.ogg"
    pause 0.4
    play sound3 "sound/shotgun.ogg"
    play sound5 "sound/machinegun.ogg"
    
    "The Paladin unloaded all of its munitions into the Ascendant at point blank range. Smoke and fire enveloped the Ascendant as it received volley after volley of cannon fire, a swarm of missiles, and even a stream of assault rounds for good measure."
    kry "Tsch... It would seem too good to be true if Ascendant went down so easily..."
    "Kryska's blood went cold when she sensed movement behind her."
    
    scene alice_cockpit3 with dissolve
    
    ali "Heh."
    "Alice licked her lip as the Ascendant struck from the Paladin's blind spot. Somehow, it had managed to escape from the Bianca's gravity well and circle around behind the Paladin."
    kry "Argh!!"
    
    play sound "sound/Sword Shing 2.ogg"
    
    "The Paladin barely deflected the Ascendant's sword with its ablative shield. The Paladin's entire arm bent from the strike, sending sparks flying from its joints."
    ali "Say goodnight!"
    "Just as the Ascendant was about to deliver the coup de grace, a cross guard of laser and steel blocked its sword from reaching the Paladin."
    
    scene asagacockpit7 with dissolve
    
    asa "Hiyaaahh!!!!"
    ali "Tsch! The so called Sharr of Ryuvia!"
    asa "Sorry for bein' late! Had to fit the Liberty's reactor into the Black Jack before it could move again!"
    "Asaga hit the reverse thrusters moments before the Ascendant over powered its defenses."
    
    play sound "sound/legion_laser.ogg"
    play sound1 "sound/dronefly.ogg"
    
    "The Black Jack whirled out of the way as the Ascendant fired its particle gun. Its remaining drones spiraled towards the Black Jack like hounds onto prey."
    
    play sound "sound/pulse1.ogg"
    play sound1 "sound/explosion1.ogg"
    play sound2 "sound/mech_boost2.ogg"
    
    "In a flurry of pulse bolts, Asaga took two more of the drones out, before ducking and weaving through a cobweb of lasers."
    
    play sound "sound/Laser 1.ogg"
    
    "Spinning in a wild dance, it shot a stream of particles from its shoulder guns, cutting through a third drone. The tip of the particle guns began to char black and rapidly overheat."
    asa "(Crap... The Liberty's reactor's feeding way more power than usual...)"
    asa "(Chigara must have modified it to generate a lot more energy to power her ECM suite.)"
    "All of the Black Jack's movements felt jerky, like a wild bull. One false move could cause the Black Jack to spiral out of control, or worse, cause a thruster to burst. But for some reason, Asaga's face broke into a grin."
    asa "(This power... I like it!!)"
    
    scene blackjack_attack with dissolve
    play music "Music/The_Final_Battle_Cut.ogg" fadeout 1.5
    play sound2 "sound/mech_boost2.ogg"
    
    "She slammed down her foot pedals, sending the Black Jack forward with explosive speed."
    "Asaga clenched her teeth as she was plastered against her seat."
    asa "Hiyaahh!!!"
    "She shot towards the Nightmare Ascendant, her blade drawn."
    
    scene alice_cockpit3 with dissolve
    
    ali "Heh. Fool!"
    "The Ascendant raised its sword high and shot forward as well."
    "Shields put his hands together in prayer as he saw the two streaks of light close in on each other on the bridge."
    kay "(Asaga...!)"
    kay "(Please... come back alive...!!)"
    
    scene asagacockpit7 with dissolve
    
    asa "I'll show you... What a true Sharr can do!!!"
    
    scene alice_cockpit3 with dissolve
    
    ali "Hahaha!! Your toy is nothing against the might of the Ascendant!!!"
    
    scene asagacockpit7 with dissolve
    
    asa "HIYYAAHHH!!!!"
    
    scene alice_cockpit3 with dissolve
    
    ali "EEAAHHH!!!!!"
    "The two warriors' eyes burned with azure fire as they accelerated towards destiny."
    
    stop music fadeout 1.5
    scene white with dissolve
    play sound "sound/Sword Shing 2.ogg"
    
    "In an infinite instant, the two ryders crossed each other, their swords moving quicker than what the universe could accept."
    "The space time continuum rippled as the swords tore through the universe's laws."
    asa "... ... ..."
    ali "... ... ..."
    
    play music "Music/Camino.ogg" fadeout 1.5
    play sound "sound/explosion4.ogg"
    
    "The Black Jack's joints gave out, causing explosions throughout the ryder. Sparks of electricity ran through its frame."

    play sound "sound/gore.ogg"
    show layer master at tr_xshake
    scene cg_asaga_cockpit_hurt2 with dissolve    
    
    "Asaga's cockpit burst, impaling her with shrapnel."
    asa "Ggurrckkk!!!"
    "Blood dripped down her face. She looked down in disbelief to see a thin steel rod sticking out from her belly."
    "Suddenly, the pain struck her all at once. She collapsed in agony, her eyes losing focus."
    asa "(N-no way... I lost...? T-that quickly...?)"
    "The Ascendant approached the Black Jack and grabbed it by its head, completely untouched."
    ali "Hahaha...!"
    ali "Now do you understand, \"princess...?\" You will never become as powerful as I..."
    ali "For the truth of our power is that it feeds upon our dark emotions... Twists and corrupts our minds... Brings out the absolute evil, lurking deep inside our hearts..."
    ali "Without hatred, you will never wield the power of Sharrs! Without tasting the true horror of the blackest defeat, you have no place in war!"
    ali "Only when you are destroyed in mind and body, stripped naked, and stomped on until every ember of hope has been extinguished can you truly hold the power of Sharrs...!"
    ali "Foolish girl! You sought to kill me? I have already died... years ago... This woman is but an empty husk, kept alive by this monstrous machine called the Ascendant..."
    
    scene cg_asaga_cockpit_hurt1 with dissolve    
    
    asa "You're... wrong..."
    "Asaga looked up, blood dripping down her mouth, the fire in her eyes extinguished."
    asa "I..."
    asa "Learned something the past few days..."
    asa "Power... brings arrogance... It makes you start thinking that you deserve to have stuff that doesn't belong to you... Twists up your insides... whenever you get jealous..."
    asa "But you know, true power isn't about getting things! You can have all the love, wealth, and influence in the galaxy and still be weak!"
    asa "'Cause power ain't about the stuff you have!! It's the stuff you can give that makes you powerful!!"
    "Alice's eyes changed. She looked down coldly upon Asaga, like a disappointed matron about to punish her young daughter."
    ali "Foolish girl."
    ali "If you take this path, then all that awaits you will be a long, miserable death. As I found, all those millennia ago..."
    ali "The throne of Ryuvia will bring certain doom to the unprepared."
    ali "Abandon all pretenses of hope and destroy your enemies. Before they destroy you."
    asa "Wait... You're... not...!"
    "At that moment, Alice snapped back to attention."
    ali "Tsch... Not again..."
    ali "(I better end this quick... before...)"
    ali "I think it's time we said good-bye... Sharr of Ryuvia!"
    asa "No..."
    asa "I'm afraid... It's your loss."
    ali "What? Have you lost your mind?"
    asa "No... because I managed to buy the captain enough time...!"

    play music "Music/The_Final_Battle.ogg" fadeout 1.5
    scene bg bridge with dissolve
    show kayto:
        xpos 0.2
    with dissolve
    $dshow("ava handonhip shout narrow angry",xpos=0.8)

    ava "Captain, the Combined Fleet has broken through the PACT Fleet! They are coming to assist!"
    kay "About time."
    
    show grey with wipeup
    
    adr "You have my apologies for our late arrival, captain..."
    adr "But thanks to their reinforcements not arriving, the enemy is running low on munitions. It will not be long until the tide turns to our favor."
    
    hide ava with dissolve
    show fontana:
        xpos 0.8
    with wipeup
    
    fon "Heh. And I have further good news..."
    
    play sound "sound/large_warpout.ogg"
    
    "A fleet of fresh PACT Assault Carriers appeared from behind Cera's moon."
    fon "Thanks to your early warning, my engineers have now restored full control over our ships. My fleet is now back on the field!"
    kay "Yes!"
    "Shields pumped the air, unable to contain his joy."
    "His future self's gambit had worked. Even without Chigara's help, they had managed to restore Fontana's fleet."
    adr "Now, I understand a certain ryder has been giving you trouble..."
    kay "I'm afraid so, admiral. Not only that... but its pilot's also the spitting image of my ex-girlfriend... Kind of gives me the creeps."
    
    scene allshipsfire1 with dissolve
            
    adr "Oh? Well, do please hold back any unsightly tears as we end her. All ships, open fire!"
    fon "All ahead full! All ships, open fire on the Nightmare Ascendant once you are in range!"

    play sound "sound/legion_laser.ogg"
    play sound1 "sound/cannon.ogg"
    play sound2 "sound/railgun.ogg"
    scene allshipsfire2 with dissolve

    ali "A-argh!!"
    "The Ascendant hit its thrusters, but the renewed stream of firepower was too thick to dodge."
    cla "O-ooh!! C-careful Asaga!"
    "The Bianca used the moment to shoot tow cables at the Black Jack and fall back towards the Sunrider."
    asa "T-thanks doc..."
    cla "N-no worries!"
    
    scene bg bridge with dissolve
    $dshow("ava handonhip shout neutral angry")

    ava "Captain. Our line of fire is now clear."
    ava "On your word."
    kay "No matter how many times, this never gets old..."
    
    scene white
    
    if legion_destroyed == True:
        $ renpy.movie_cutscene("3DCG/vanguard_eyepatch.webm",stop_music=False)  
    if legion_destroyed == False:
        $ renpy.movie_cutscene("3DCG/vanguard_nopatch.webm",stop_music=False)  
    pause

    play sound "sound/explosion2.ogg"
    play sound1 "sound/vanguard cannon laser.ogg"
    scene alice_cockpit5 with dissolve

    ali "T-tsch...!! A-AARGGHH...!!!"
    "The Nightmare Ascendant was completely enveloped in fire as ships struck it from every direction."
    "With the unexpected entry of Fontana's fleet, the tide of the battle had reversed. Everywhere around Alice, her ships lit on fire and broke apart against the onslaught of Fontana's assault carriers and advanced ryders. At this rate, they would be completely annihilated."
    ali "(T-this wasn't how I planned this....!!)"
    ali "(How... was I foiled...? How did that fool Shields see through my sister's spy...!? He was completely under our control....!!)"
    ali "(Wait... His actions are not consistent... Could... he have had assistance... From some outside... meddler...?)"
    ali "(Tsch... The wanderer....!!! So you have betrayed us!)"
    ali "But that means..."
    ali "I may yet win!!"
    "With the remaining energy remaining in the Ascendant, Alice spun her ryder around."
    
    play music "Music/Gore_and_Sand.ogg" fadeout 1.5

    scene bg bridge with dissolve
    $dshow("ava armscrossed shout narrow angry")

    ava "Captain! It's the Ascendant!"
    kay "What the---"
    "The flaming hulk of the Ascendant emerged from the Vanguard's beam, and shot towards the Sunrider."
    ava "It's on a collision course for the ship!!"
    kay "FIRE!!!"
    
    play sound "sound/flakguns_deep.ogg"
    play sound1 "sound/Laser 1.ogg"

    "The Sunrider unloaded everything in its arsenal against the flaming comet streaking towards the ship, but it was too late."
    ava "All hands, brace for impact!!!"
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    
    "Ava threw herself on top of Shields. The two pressed themselves against the ground as the entire ship tumbled from the force of the collision."
    
    show layer master at tr_xshake
    play sound "sound/explosion4.ogg"
    
    "The hull around the bridge bent, sparks exploding from every direction as power cords snapped. Vapor shot out and covered the bridge as pipes shattered from the force of the impact."
    
    play sound "sound/explosion4.ogg"
    scene white with dissolve
    scene bg bridge_damaged with dissolve
    show kayto:
        xpos 0.25
    with dissolve
    
    "Instruments hidden inside the walls blew in fireballs, sending wall panels flying. The crew burst open the emergency lockers and grabbed fire extinguishers to combat the flames."
    kay "Report!"
    
    $dshow("ava armscrossed shout narrow angry",xpos=0.75)
    
    ava "The Nightmare Ascendant has crashed near Engineering! All systems are catastrophically damaged!"
    ava "The reactor core's cooling system has been destroyed! If we do not restore the auxiliary system within ten minutes, we will have a full scale meltdown on our hands!"
    kay "Order engineering to fix the reactor, double time!"
    ava "Unfortunately, we have lost all contact with engineering!"
    kay "Shit..."
    
    play sound "sound/warning.ogg"
    
    ava "Captain! Intruder alert!"
    kay "What?"
    "Security footage of the Ascendant's cockpit opening and Alice entering the twisted hull of the ship inside an environmental suit appeared on the main screen."
    kay "Shit... She's headed straight to engineering..."
    kay "Alert security! Stop her!"
    
    $dshow("ava salute shout neutral angry")
    
    ava "Sir!"

    scene bg hallway_damaged with horizontalwipe

    "Meanwhile, the future Kayto Shields pushed through the burning corridor to get to engineering. The injured and dead were strewed throughout the floor, but he had no choice but to march on and complete his mission."
    kay "(Tsch... If the Prototype gets to our reactor core, then it's game over...!)"
    
    scene bg engineering_fire with dissolve

    "He finally arrived at the burning engineering hall. Vapor streamed out from over a dozen broken pipes and flames licked at the walls."
    "At his feet were the bullet ridden bodies of half a dozen marines."
    kay "(Shit... I was too late...)"
    
    play music "Music/MarduksWrath.ogg" fadeout 1.5
    play sound "sound/machinegun.ogg"
    
    "He ducked for cover seconds before a stream of bullets riddled his position."
    "Alice's voice echoed through engineering."
    
    $dshow("zalice plugsuit shout narrow angry",xpos=0.8,ypos=1650)
    
    ali "You're too late, Shields!"
    ali "Once the reactor melts down, you will die. And with that, this timeline shall revert to its original chronology!"
    ali "I don't know how you got the wanderer to help you... But even she is not infallible! Just as I thwarted her plans in your timeline, I shall thwart her here yet again!"
    kay "Surrender, Prototype! You should know that you die if the original timeline is restored! This is for your own good too!"
    
    $dshow("zalice plugsuit smirk narrow angry",xpos=0.8,ypos=1650)
    
    ali "Heh. Death means nothing to a walking corpse such as I..."
    
    play sound "sound/machinegun.ogg"
    
    "Alice opened fire once more, pinning Shields down."
    
    hide zalice with dissolve
    
    kay "Damn..."
    "He drew his pistol. Gauging from the sound of her weapon, Shields surmised she had commandeered one of the marines' rifles. In other words, he was outmatched in terms of firepower."
    kay "(But she's still wearing nothing but her plugsuit. All it'll take is one good shot to bring her down.)"
    kay "(Now if only I can figure out where she's hiding...)"
    "Shields kept talking, trying to use the Prototype's voice to discern her position."
    kay "Your fleet's defeated! And Fontana has control of PACT now!"
    kay "What do you have to gain by triggering total war between the Alliance and Fontana's forces? All that'll happen is the destruction of all that you've worked for!"
    
    $dshow("zalice plugsuit shout narrow angry",xpos=0.8,ypos=1650)
    
    ali "All that I've worked for? Hahaha...!"
    ali "Do not think for a moment I had any notions of ruling the galaxy as Veniczar, Empress, or some other meaningless title."
    ali "I have no intention of raising you worms from your wretched existence! All I sought was doom for your species!"
    
    hide zalice with dissolve
    
    kay "(Good... Keep talking...)"
    kay "(She's over there!)"
    
    play sound "sound/pulse2.ogg"
    pause 0.3
    play sound "sound/pulse2.ogg"
    pause 0.3
    play sound "sound/pulse2.ogg"
    
    "Shields popped from cover and unloaded his pistol into a shadowy catwalk. Sparks flew as the already damaged supports fell apart, bringing the elevated path crashing down into a slope."

    $dshow("zalice plugsuit shout narrow angry",xpos=0.5,ypos=1650)

    ali "A-arggh...!!"
    "Alice rolled down the collapsed catwalk, losing her grasp on her rifle. Shields used the opportunity to charge at her position."
    
    play sound "sound/gunclick.ogg"
    
    "He aimed his pistol and pulled the trigger, but received a feeble click. Out of ammo."
    
    $dshow("zalice plugsuit shout narrow angry",zoom=1.2,ypos=2100)
    
    "In frustration, he tossed the pistol aside and bull rushed into Alice's gut just as she got back to her feet."
    
    show white:
        alpha 0.5
        pause 0.1 alpha 0
    show layer master at tr_xshake
    play sound "sound/shieldhit.ogg"
    
    "Unexpectedly, excruciating pain shot down his spine."
    kay "ARGGHH....!!!"
    "He ran headfirst into what felt like solid steel. He looked up just in time to see an energy barrier flicker in front of Alice."
    
    $dshow("zalice plugsuit laugh wide angry",zoom=1.2,ypos=2100)
    
    ali "Hahahaha! Fool!"
    
    play sound "sound/shieldhit.ogg"
    
    "Shields mustered his strength and delivered a round of punches into Alice's chest, but his fists bounced off the energy field surrounding Alice."
    
    show layer master at tr_xshake
    play sound "sound/gore.ogg"
    
    "With a single backhand, Alice knocked Shields down to the floor, driving an explosion of blue sparks to his jaws."
    "Shields spat blood from his mouth."
    kay "G-ugh...."
    ali "Did you think I would come here without a personal shield? Heh..."
    
    show layer master at tr_xshake
    play sound "sound/gore.ogg"
    
    "Alice stepped on his prone body. Sparks of energy shot from her heel as it dug into Shields' ribs."
    kay "A-AHGGH!!!"
    "Shields could only howl helplessly as his flesh seared off."
    "He desperately looked to the Sunrider's reactor. Steam was pouring from its sides as the remaining coolant rapidly evaporated."
    "If he did not defeat Alice within minutes, the reactor would melt down and completely destroy the entire ship."
    ali "I won't kill you yet, Shields... I want you to be there with me when the ship's reactor finally blows..."
    ali "We'll die together, you and I... Hahahahaha!!!"
    "The reactor's side panel burst in an explosion of vapor, ruffling Alice's hair."
    ali "How long have I waited for this moment... To finally sink into the black void of death..."
    ali "I know... I shall never see him where I am headed... But know that I, Alice Ashada, has saved the galaxy from humanity! Like a festering nest of roaches, humanity will breed until it has consumed the galaxy. Then you will eat each other, until nations fall and civilization ends."
    ali "Humanity is but a sea of moaning naked bodies, wretched and poor... When one dares to rise above the crowd to bring about everyone's salvation... it will not be the rich and powerful in their ivory towers who bring about the hero's downfall... But the very masses the hero sought to liberate!"
    ali "For the wretched cannot bear to see one of them rising above them! For that only reminds them that they are pitiful, pathetic, scum! They will rather keep festering in their holes than be saved!! One day, you too will be betrayed, Shields! By the very galaxy you sought to protect!!"
    kay "No...."
    kay "Even then..."
    kay "Even then... heroes must be born..."
    kay "The masses may turn against us... But within that crowd... There will always be ones who cheer us on... when this happens...!"
    
    show layer master at tr_xshake
    play sound "sound/punch.ogg"
    
    "With the final reserves of his strength, Shields delivered a kick to Alice's gut, knocking her off balance."
    "He shoved her off and rolled to his feet."
    
    $dshow("zalice plugsuit shout wide angry")
    
    "Alice drew her sabre and came at him."
    ali "Shields!! You must have a death wish!"

    if girl == "Asaga":
        
        play sound1 "sound/shieldhit.ogg"
        play sound "sound/machinegun.ogg"
        
        "Before she could reach him, bullets impacted against Alice's energy barrier."
        
        $dshow("asaga zexcited_plugsuit yell neutral angry",xpos=0.75)
        
        asa "Captain!"
        "Asaga ran into Engineering, a rifle slung around her neck."
        
        $dshow("zalice plugsuit clench wide angry",ypos=1650)
        
        ali "Tsch!"
        
        $dshow("asaga zexcited_plugsuit yell zawakened angry",xpos=0.75)
        
        "Alice sheathed her sabre and picked up her rifle. Asaga's eyes ignited as she sprayed Alice with more rounds before diving behind a console."
        
        play sound "sound/machinegun.ogg"
        
        "Sparks sprayed from the console as Alice riddled it with bullets."
        kay "Hyah!!!"
        "Shields picked himself up and grappled Alice's rifle, giving Asaga a chance to circle around behind her."
        
        play sound1 "sound/shieldhit.ogg"
        play sound "sound/machinegun.ogg"
        
        "Alice kicked Shields away and pointed his rifle at him, but received a renewed spray of bullets from the rear."
        "Her energy shield began to flicker as it crumbled away against Asaga's assault."
        
        $dshow("asaga zneutral_plugsuit talk zawakened down")
        
        asa "Get outta there, capt'n! You can't do anything against that shield!"
        "Shields nodded and scrambled away while Alice was distracted by the withering stream of lead flying towards her. He desperately scavenged the bodies of the downed marines for a weapon."
        kay "(Need... heavy... explosives...)"
        kay "(Grenade... grenade...)"
        "Unfortunately, he was going to find no such assistance in Engineering, where security was expressly banned from using explosives."
        
        play sound "sound/warning.ogg"
        
        "The klaxon sounded above him as the last of the reactor's coolant vaporized. Sweat drenched his uniform as the reactor heated to critical levels."
        kay "(Shit... Forget that... The reactor's the priority here!)"
        
        play sound "sound/gunclick.ogg"
        
        "While Shields scrambled for the reactor's controls, Asaga popped out of cover and pulled the trigger. Her rifle merely clicked."
        
        $dshow("asaga zexcited_plugsuit yell zawakened angry")

        asa "Tsch.."
        "Alice sneered and tossed away her empty rifle as well. She drew her sabre and held it in front of her."
        "The two women circled each other."
        asa "(She's... not awakening...)"
        asa "(Does that mean she's out of energy? Or... is it a trap?)"
        asa "Hiyaah!!!"
        "Asaga charged for Alice, her eyes flaming with blue fire. Alice swiped her blade laterally, but Asaga deftly ducked under the blade. Before Asaga could grapple her, Alice spun backwards, and brought her sword down again." 
        
        show white:
            alpha 0.5
            pause 0.1 alpha 0
        play sound "sound/Sword Shing 2.ogg"
        
        "Once again, Asaga dodged with super human speed, the tip of the sword cutting a tear down the shoulder of her plugsuit."
        asa "Tsch..."
        ali "Eah!!!"
                
        "Asaga jumped to the left as Alice jabbed the sabre forward. However, this time Alice was prepared. She delivered a kick to Asaga's gut where she had previously been impaled with the steel rod, sending her spinning across the floor."
        
        show white:
            alpha 1
            pause 0.1 alpha 0
        play sound "sound/gore.ogg"
        
        asa "G-ah...!"
        
        hide asaga with dissolve
        
        "She had fallen for Alice's trap. Despite super human abilities, Asaga was still a neophyte when close quarters combat was concerned. No match for a war veteran such as Alice."
        
        show white:
            alpha 1
            pause 0.1 alpha 0
        play sound "sound/gore.ogg"
        
        "Asaga could barely clamber to her knees when Alice delivered a crushing kick to her neck."
        asa "G-ghaackk!!!"
        "Blood dripped down her mouth as her diaphragm collapsed."
        "She could only gag in ragged gasps as Alice pulled her up by her hair."
        
        $dshow("zalice plugsuit grin wide angry",ypos=1650)
        
        ali "In the end... You are merely a girl..."

    if girl == "Sola":
        
        play sound "sound/sniperrifle.ogg"
        play sound1 "sound/shieldhit.ogg"

        "Before she could reach him, a bullet impacted against Alice's energy barrier."
        
        $dshow("zalice plugsuit shout wide angry",ypos=1650)
        
        ali "What!?"
        
        $dshow("sola zarmhold_plugsuit neutral zawaken mad",xpos=0.75)
        
        "Hidden above the catwalk, Sola aimed down her scope and loosed another round."
        
        play sound "sound/sniperrifle.ogg"
        play sound1 "sound/shieldhit.ogg"
        
        "Alice flinched as another bullet struck her squarely between the eyes."
        kay "Sola, watch out!"
        
        play sound "sound/machinegun.ogg"
        
        "Alice sheathed her sabre and picked up her rifle. Gunshots echoed through Engineering as Alice laid down suppressive fire."
        "Sola rolled to her feet and sprinted across the catwalk, bullets ricocheting off the guard rails."
        kay "Hargghh!!!"
        
        hide sola with dissolve
        show layer master at tr_xshake
        play sound "sound/shieldhit.ogg"
        
        "Shields grappled Alice, giving Sola a chance to find cover. The two struggled as Shields tried to wrest the rifle from Alice's grasp."
        
        show layer master at tr_xshake
        play sound "sound/hit.ogg"
        
        "She suddenly released her grip on the gun and swept her leg across Shields' knees. He lost his balance and fell flat on his face, the rifle still slung around Alice's neck."
        kay "(Shit...!)"
        
        play sound "sound/guncock.ogg"
        
        "He looked up to come face to face with a gun barrel."
        
        $dshow("zalice plugsuit grin wide angry",ypos=1650)
        
        ali "Amateur."
        
        play sound "sound/sniperrifle.ogg"
        
        "Shields flinched when a gunshot echoed through Engineering, but realized he was yet alive. Alice's rifle flew from her hands, now an enormous jagged hole bored through its chamber."
        
        $dshow("sola zarmhold_plugsuit neutral zawaken mad",xpos=0.75)
        
        sol "Target neutralized."
        "Shields capitalized the opportunity to escape."
        kay "(Fisticuffs aren't going to even dent that energy barrier... All I can do is keep the reactor from melting down!)"
       
        play sound "sound/sniperrifle.ogg"
        play sound1 "sound/shieldhit.ogg"
        pause 0.5
        play sound "sound/sniperrifle.ogg"
        play sound1 "sound/shieldhit.ogg"
        
        "Sola took aim and sprayed lead on Alice, lighting her energy barrier up with sparks."
        
        $dshow("zalice plugsuit clench wide angry",ypos=1650)
        
        ali "Arggh!!!"
        "Shields pounded the reactor's console, desperately trying to find the auxiliary cooling system's controls. "
        
        play sound "sound/warning.ogg"
        
        "The klaxon sounded above him as the last of the reactor's coolant vaporized. Sweat drenched his uniform as the reactor heated to critical levels."
        kay "Come on...!"
        
        play sound "sound/gunclick.ogg"
        
        "Sola's rifle clicked as she ran out of ammo. Alice's energy barrier momentarily flickered as if shutting down, then dashed Sola's hopes by reappearing."
        
        $dshow("sola zarmhold_plugsuit clench zawaken mad",xpos=0.75)
        
        sol "Tsch..."
        
        $dshow("zalice plugsuit smirk wide angry",ypos=1650)
        
        "With a bloodthirsty grin tearing apart her face, Alice marched towards the reactor's controls."
        sol "Captain!"
        
        play sound1 "sound/spark.ogg"
        play sound "sound/explosion2.ogg"
        
        "Shields barely spun out of the way moments before Alice's sabre smashed against the console."
        kay "Argh!"
        
        $dshow("sola zarmhold_plugsuit yell zawaken mad",xpos=0.75)
        play sound1 "sound/shieldhit.ogg"
        
        "Sola sprinted to their position and smashed the butt of her rifle against Alice's energy shield. In an explosion of sparks, the shield repulsed Sola's attack, sending her staggering backwards."
        
        $dshow("zalice plugsuit shout wide angry",ypos=1650)
        
        ali "Pretender!"
        "Alice's face contorted with wicked pleasure as she thrusted her blade towards Sola's heart."
        "Sola's eye ignited, her body twisting out of the way. But it was too late."
        
        show white:
            alpha 1
            pause 0.1 alpha 0
        play sound "sound/gore.ogg"
        
        
        $dshow("sola zarmhold_plugsuit clench closed mad")
        
        sol "G-uck...."
        ali "Hahahaha!!!"
        "Sola fell to her knees, skewered by Alice's blade under her collarbone."
        
        play sound "sound/gore.ogg"
        
        "Alice twisted and turned the blade as Sola's eyes widened with agony."
        
        $dshow("zalice plugsuit grin wide angry",ypos=1650)
        
        ali "You are... but a mockery of the Sharrs of Ryuvia...!"
        ali "Now die like the mongrel you are!"

    if girl == "Icari":
        
        $dshow("icari zpoint_plugsuit shout neutral angry",xpos=0.75)
        
        "Before she could reach him, Icari charged into Engineering, a katana in one hand and a wakizashi in the other."
        ica "HIYAAHH!!!"
        
        play sound "sound/Sword Shing 2.ogg"
        
        "She flipped into the air and met Alice's blade with her own."
        ali "Tsch!"
        
        $dshow("zalice plugsuit clench narrow angry",ypos=1650)
        
        "Alice readied her sabre as the two women circled each other."
        
        play sound "sound/Sword Shing 2.ogg"
        
        "Quicker than lightning, Alice jabbed her blade forward. Icari nimbly back away, then stepped forward with a powerful sweep of her katana in an attempt to break Alice's center."
        "While lacking power, Alice's slender blade proved too quick. Alice charged forward as Icari's katana went wide and brought her blade down on Icari's head."
        
        play sound "sound/Sword Shing 2.ogg"
        
        "Icari barely deflected her attack in time with her shorter blade, then used the momentum of her katana to spin in a whirlwind. Alice held her blade to the side as their steel edges met, sending sparks flying."
        kay "Careful! She's shielded!"
        
        $dshow("icari zhandonhip_plugsuit smile neutral confident",xpos=0.75)
        
        ica "Don't worry..."
        "Icari eyed Alice's rifle resting on the ground."
        "Whoever grabbed the rifle first would gain a decisive advantage..."
        "Alice went on the offensive, using her blade's speed to attack in a flurry."
        "Icari blocked, each of her blades dancing in front of her. She spun, her ponytail flying behind her, and cut her wakizashi across where Alice's neck would have been had she not ducked down in time."
        
        $dshow("icari zpoint_plugsuit shout neutral angry",xpos=0.75)
        
        ica "You're... not bad...!"
        ali "First thing I learned as a Compact fighter..."
        
        $dshow("zalice plugsuit laugh narrow angry",ypos=1650)
        
        ali "Never fight fair!"
        
        play sound "sound/Sword Shing 2.ogg"
        
        "Alice charged forward and swept her sword across Icari's eyes. Icari barely managed to pull back in time, the blade cutting across the tip of her nose."
        ica "Right back at you!"
        "Icari tossed her wakizashi like a throwing dagger at Alice. The knife darted for Alice quicker than Shields' eye could track, but Alice still somehow managed to deflect it with her blade."
        "Icari used the momentary distraction to charge, both hands wrapped around her katana."
        
        show white:
            alpha 1
            pause 0.1 alpha 0
            
        play sound "sound/Sword Shing 2.ogg"
        
        "In a renewed fury of attacks, Icari pushed Alice back. With a final mighty downwards smash, Alice staggered backwards against the wall."
        
        $dshow("icari zhandonhip_plugsuit shout neutral confident",xpos=0.75)
        
        ica "Now, captain!"
        
        play sound "sound/machinegun.ogg"
        
        "While Alice's attention was diverted, Shields had grabbed ahold of her rifle. He unleashed the rifle's entire clip against Alice the moment Icari rolled out of the way."
        "Sparks flew from her personal shield as bullets ricocheted in every direction."
        kay "(Did we... get her?)"
        "Alice's shields flickered as if deactivating, then restored itself."
        kay "Damn!"
        "Shields ran towards the downed marines in search of a second clip, but Alice leapt forward and blocked his path."
        ica "Hiyah!"
        "Icari brought her katana down on her head, but was deflected by Alice."
        ali "EAH!"
        
        play sound "sound/gore.ogg"
        show white
        pause 0.1
        hide white
        
        "With a swift lateral swipe, Alice slashed Icari across her chest."
        ica "G-gyn..."
        "Icari stepped backwards, clutching her wound. While it wasn't deep, it would be a handicap in an already desperate match."
        
        show layer master at tr_xshake
        play sound "sound/gore.ogg"
        
        "Exploiting Icari's loss of balance, Alice smashed the hilt of her blade against her head."
        ica "Argh!"
        
        hide icari with dissolve
        
        "Shields rummaged through the bodies of the marines, desperately trying to find ammo. He exhaled when he found a spare clip of ammo in a fallen marine's pouch."
        "He locked and loaded and turned, only to come face to face with Alice. With a upwards kick, she sent his aim wide."
        
        play sound "sound/gore.ogg"
        show white
        pause 0.1
        hide white
        
        "Shields twisted out of the way as her blade shot towards him, but it was too late. Agony shot through his shoulder as Alice sank her sabre through his flesh. He fell to his knees, losing his grip on his rifle."
        kay "Aargh!!"
        "She pulled the blade out and prepared to deliver the coup de grace."
        
        play sound "sound/Sword Shing 2.ogg"
        play sound1 "sound/shieldhit.ogg"
        
        $dshow("icari zhandonhip_plugsuit shout neutral confident",xpos=0.75)
        
        "With the last of her strength, Icari slammed her blade down on Alice's back, but now lacked the strength to cut through her barrier."
        ica "H-yaaahhh!!!"
        
        play sound "sound/explosion1.ogg"
        show layer master at tr_xshake
        hide icari with dissolve
        
        "In a massive explosion, Icari went flying backwards as Alice's barrier repelled her, sending her katana clattering against the floor."
        "Icari panted in exhaustion, blood seeping down her chest."
        
        $dshow("zalice plugsuit laugh wide angry",ypos=1650)
        
        ali "You are defeated!"
        
        play sound "sound/machinegun.ogg"
        
        "Suddenly, gunshots ran from across Engineering."
        
        $dshow("kryska neutral surprise neutral angry",xpos=0.75)
        
        kry "Hiyaahh!!!"
        
        play sound "sound/machinegun.ogg"
        
        "Kryska appeared with a rifle and laid down fire from above."
        
        play sound1 "sound/shieldhit.ogg"
        
        "Alice's shields began to flicker once more as bullets bounced off. Shields struggled to his feet and went for his rifle, only to have it snatched from his hand."
        
        $dshow("zalice plugsuit clench wide angry",ypos=1650)
        play sound "sound/machinegun.ogg"
        
        "Alice took aim and sprayed fire on Kryska's position. Kryska dropped prone as bullets ricocheted around her. The catwalk collapsed under the fire, sending Kryska tumbling to the floor."
        
        play sound "sound/sniperrifle.ogg"
        play sound1 "sound/shieldhit.ogg"
        
        "Kryska rolled up, and with a final shot, Alice's shields finally flickered out."
        kry "(Just another---!!)"
        
        play sound "sound/gunclick.ogg"
        
        "But her weapon clicked. She had already expended all her ammo laying down suppressive fire."
        
        show white:
            alpha 0.5
            pause 0.1 alpha 0
            alpha 0.5
            pause 0.1 alpha 0
            alpha 0.5
            pause 0.1 alpha 0

        play sound "sound/machinegun.ogg"
        
        hide kryska with dissolve
        
        "Alice unleashed her remaining rounds on Kryska, tearing her uniform apart. Kryska dropped to the floor, her final mission complete."
        
        $dshow("icari zarmscrossed_plugsuit shout closed embarass",xpos=0.75)
        
        ica "NO!!!"
        "Icari pushed herself up and rushed for Alice in blind fury, but was kicked down."
        
        $dshow("zalice plugsuit grin wide angry",ypos=1650)
        
        ali "Haa... haa..."
        "Alice's chest heaved with exhaustion as she stood triumphantly over Icari."
        ali "Your friend is dead! And the reactor shall soon explode, killing the rest of you!"
        "Alice dropped her now empty rifle and drew her sabre."

    if girl == "Ava":
        
        play sound "sound/pulse2.ogg"
        play sound1 "sound/shieldhit.ogg"
        
        "Before she could reach him, a bullet impacted against Alice's energy barrier."
        
        $dshow("ava handonhip shout neutral angry",xpos=0.75)
        
        ava "Kayto!"
        "Ava ran into Engineering, a pistol in hand."
        "Shields used the opening to scramble into cover, while Alice ducked back and grabbed her rifle."
        
        play sound "sound/machinegun.ogg"
        
        "Ava and Shields pressed themselves against a workstation as Alice returned fire."
        kay "Where's the rest of security!?"
        ava "Already all dispatched! The rest are tied up below deck!"
        "Ava handed Shields a fresh pistol."
        ava "I'll take her! You've got to activate the auxiliary cooling system!"
        kay "All right!"
        
        play sound "sound/pulse2.ogg"
        pause 0.3
        play sound1 "sound/pulse2.ogg"
        pause 0.3
        play sound2 "sound/pulse2.ogg"
        
        "Ava popped out of cover and peppered Alice's shields with bullets as Shields ran towards the reactor's controls."
        
        $dshow("zalice plugsuit grin narrow angry",ypos=1650)
        
        ali "Useless!"
        
        play sound "sound/shieldhit.ogg"
        
        "With the personal shield still active, Ava's shots only bounced harmlessly off Alice."
        
        play sound "sound/machinegun.ogg"
        
        "Bullets ricocheted against the floor as Alice opened fire on Shields. He rolled away into the adjacent room, unable to reach the completely exposed reactor's console."
        kay "No good!"
        
        $dshow("ava armscrossed neutral narrow angry",xpos=0.75)
        
        ava "Tsch..."
        "Ava slipped her now empty clip out and reloaded. However, she would need heavier weaponry to cut through Alice's barrier."
        
        play sound "sound/pulse2.ogg"
        pause 0.3
        play sound1 "sound/pulse2.ogg"
        pause 0.3
        play sound2 "sound/pulse2.ogg"
        
        "Alice merely paced toward Ava as she popped more rounds."
        ali "Hahahahaha...!!!"
        
        $dshow("zalice plugsuit smirk narrow angry",ypos=1650)
        
        "A sadistic sneer sliced Alice's face as the barrier deflected all of Ava's shots."
        ava "Tsch..."
        "Alice wrapped her hand around Ava's throat and lifted her off her feet."
        
        play sound1 "sound/shieldhit.ogg"
        play sound "sound/spark.ogg"
        hide ava with dissolve
        
        ava "G-gg-aaakk...!!"
        "Sparks flew from Alice's hand as her barrier crushed Ava's throat."
        kay "AVA!!"
        ali "Pathetic! Is that all you've got!?"
        "Alice tossed Ava to the floor like a rag doll."
        
        show white:
            alpha 0.5
            pause 0.15 alpha 0
            pause 0.15 alpha 0.5
            pause 0.15 alpha 0
            pause 0.15 alpha 0.5
            
        play sound "sound/gore.ogg"
        pause 0.3
        play sound1 "sound/gore.ogg"
        pause 0.3
        play sound2 "sound/gore.ogg"
        pause 0.3
        hide white
        "She stomped on Ava's back with her plugsuit's padded soles."
        ali "HAHAHAHA!!!"
        
    hide icari
    hide asaga
    hide sola
    with dissolve

    kay "You've..."
    
    if girl != "Icari":
        play sound1 "sound/shieldhit.ogg"
    play sound "sound/hit.ogg"
    
    "Shields brought down a pipe on Alice's head, sending her sabre clattering to the floor."
    kay "Really gotta cut down on the speeches!"
    
    if girl != "Icari":
        
        $dshow("zalice plugsuit clench wide serious",ypos=1650)
        
        "The pipe crashed against the energy shield, sending feedback jolting through his arm. But Shields mustered his strength. He wrapped himself around Alice, putting her into a sleeper hold as her energy barrier sheared through his uniform and flesh."

    if girl == "Icari":
        
        $dshow("zalice plugsuit shout wide angry",ypos=1650)
        
        ali "H-urgh!!"
        "Now without the protection of her shields, blood dripped down her skull."

    play music "Music/Camino.ogg" fadeout 1.5

    "The two of them struggled as Shields dragged her towards the flaming hot reactor core..."
    
    $dshow("zalice plugsuit shout wide angry",ypos=1650)
    
    ali "Y-YOUU!!!"
    kay "Tsch..."
    "Shields squeezed his eyes shut. He would drop Alice into the reactor shaft, even if he had to fall off with her himself."
    "This would be the only way he could finally defeat Alice and save the future..."
    "If his life was the price to pay to save everyone... then he would gladly sacrifice himself!"
    kay "(Once this is all over, the timeline's going to be fixed anyways... I'll just return to being the ship's captain... So it's no big loss...)"
    "Behind him, [girl] raised her hand and gasped desperately as Shields lifted Alice off her feet."
    kay "(I'm sorry, [girl]... But... I'll see you in the next universe...!)"
    kay "HIYAAHHH!!!"
    
    play music "Music/Camino_end.ogg" fadeout 1.5
    
    play sound "sound/explosion4.ogg"
    play sound1 "sound/fire.ogg"
    scene white with dissolve
    scene bg engineering_fire2 with dissolve
    $dshow("zalice plugsuit shout wide angry",ypos=1650)
    
    "The reactor burst into a column of blue flame behind them, the outer panels melting away in the extreme heat."
    "This would be their funeral pyre..."
    "The two of them arrived at the edge of the shaft. Beyond the safety rail was a sheer drop into a furnace of hell fire."
    
    $dshow("zalice plugsuit shout wide angry",ypos=2300,zoom=1.3)
    
    ali "SHIELDS!!!!"
    "He gritted his teeth and took another step towards into the sea of fire, his arms wrapped around Alice. This would be the end."
    kay "Sorry 'bout this... But-"
    
    play sound "sound/gore.ogg"
    show white
    pause 0.1
    hide white
    
    "Suddenly, excruciating pain cut through his back."
    kay "G-GUGH...!!!"
    "Shields dropped to his knees in disbelief."
    kay "What............"
    
    $dshow("chigara handonface smile neutral neutral",xpos=0.8,behind="zalice")
    
    chi "Eh-heh..."
    "His consciousness began to slip away as he realized there was now a combat dagger stuck to his back."
    kay "No.... Chi... gara...."
    
    $dshow("zalice plugsuit laugh wide angry",ypos=2300,zoom=1.3)
    
    ali "EAAAHHHAHAHA!!!"
    "Alice roared triumphantly."
    ali "I HAVE WON SHIELDS!!!"
    "She pounded her chest."
    ali "Even in this universe, my little doll proved your undoing!!!"
    ali "Ironic, is it not? For you to have come so far... and accomplished so much... only to fall in the same manner!!!"
    
    play sound "sound/gore.ogg"
    
    "Shields collapsed to the floor when Chigara violently pulled the dagger from his back, tearing out muscle and blood."
    "He saw Chigara's empty face hovering above him."
    kay "(That's... not... Chigara's face...)"
    kay "(She... used to... smile... so gently...)"
    ali "Now, my doll..."
    ali "Kill him."
    
    $dshow("chigara holdinghands ztalk neutral neutral")
    
    chi "Eh-heh... hehehe..."
    kay "Chi... gara..."
    "A wicked grin slashed apart Chigara's face as she thrusted the dagger downwards."
    kay "!!!!"
    "... ... ..."
    "Shields opened his eyes... and realized that Chigara's other arm had stopped the arm holding the dagger from penetrating his chest."
    "For but a flicker, lucidity returned to her eyes."
    
    $dshow("chigara handonchest yell closed focus")
    
    chi "Now's... your chance..."
    
    show layer master at tr_xshake
    $dshow("chigara handonchest yell neutral focus")
    
    chi "Get her, captain...!!!"
        
    "Shields tore the dagger from Chigara's hand and dug it into Alice's gut with all his might."
    
    if girl != "Icari":
        
        play sound "sound/shieldhit.ogg"
        "Electricity surged through his entire body as the dagger cut into her shields. At last, the barrier shattered to pieces."
        
    play sound "sound/gore.ogg"
    show white:
        0.5
    pause 0.2
    hide white
    play sound1 "sound/gore.ogg"
    show white:
        0.5
    pause 0.2
    hide white
    play sound2 "sound/gore.ogg"
    show white:
        0.5
    pause 0.2
    hide white
    
    $dshow("zalice plugsuit shout wide serious",ypos=2250,zoom=1.3)
    
    ali "G-gurk....!"
    "Alice's face froze in shock as Shields repeatedly jabbed the dagger into her belly, forming a dozen new slots into her womb."
    kay "I think it's time you died a second time...!"
    
    show layer master at tr_yshake
    play sound "sound/hit.ogg"
    
    "With that, he kicked her down the Sunrider's reactor shaft."
    
    scene black with dissolve
    $dshow("zalice plugsuit shout wide serious",ypos=2250,zoom=1.3)
    
    "For a second, Alice floated in midair..."
    ali "(Ah.......)"
    ali "(At... last.......)"
    ali "(This... nightmare ends.......)"
    ali "(Arcadius....)"
    ali "(If only.....)"
    ali "(We could have died together....)"
    
    scene white with dissolve
    
    "The second passed, and Alice fell down the shaft."
    
    play sound1 "sound/explosion4.ogg"
    play sound "sound/fire.ogg"
    
    "Chigara covered Shields' body as Alice's body erupted in an enormous pillar of fire."
    "The stench of burning flesh filled the room."
    
    scene bg engineering_fire2 with dissolve
    
    kay "Chigara... The... reactor...!"
    
    $dshow("chigara surprise yell narrow focus",xpos=0.5)
    
    chi "Understood!"
    "Chigara scrambled to the controls and furiously inputted commands."
    
    stop music fadeout 1.5
    play sound "sound/firecontrol.ogg"
    
    "Streams of foam shot from every direction, lathing the reactor in coolant. The flames around the reactor hissed and eventually fizzled out."
    
    scene bg engineering_fire3 with dissolvemedium
    $dshow("chigara handonchest yell closed embarass")
    
    chi "Haa...."
    "With a long sigh of relief, Chigara collapsed to the floor."
        
    hide chigara with dissolve
    
    if girl != "Icari":
        
        play music "Music/Epic_Action_Hero.ogg" fadeout 1.5
        
        if girl == "Asaga":
            $dshow("asaga zarmscrossed_plugsuit happy narrow sad",zoom=1.3,ypos=2400)
        if girl == "Sola":
            $dshow("sola zarmhold_plugsuit smile narrow sad",zoom=1.3,ypos=2400)
        if girl == "Ava":
            $dshow("ava handonhair smirk narrow laugh",zoom=1.3,ypos=2400)
            
        
        "Shields crawled over to [girl]. Despite being covered with wounds, she nodded and gave a thumbs up."
        kay "[girl]...!!"
        "He wrapped his arms around her."
        kay "We... did... it...!!"

    if girl == "Icari":
        
        play music "Music/Colors_sad.ogg" fadeout 1.5
        
        $dshow("icari zarmscrossed_plugsuit shout neutral sad blush tears",xpos=0.7)

        "Icari crawled over to where Kryska had fallen, tears running down her face."
        ica "No... Y-you idiot...!!!"
        ica "You didn't... have to try and be the goddamn hero!!"
        "Icari's face froze in shock when Kryska groaned."
        
        $dshow("kryska neutral neutral neutral neutral",xpos=0.3)
        
        kry "Ugh..."
        ica "E-eh...?"
        kry "Please do not hold me so tight, mercenary... My body... is already quite battered..."
        "Kryska shook herself awake and tore open her uniform, revealing a black mesh around her body."
        
        play music "Music/Epic_Action_Hero.ogg" fadeout 1.5
        $dshow("kryska neutral smirk neutral surprise")
        
        kry "Heh... Alliance made body armor... None of that cheap crap you use in the Neutral Rim... Can stop assault rounds dead in their tracks."
        kry "Just another way the Alliance leads the galaxy in superior technology!"
        
        $dshow("icari zarmscrossed_plugsuit shout closed sad blush tears")
        
        ica "H-hhhuuuuu...........!!!"
        "Icari's face twisted and contorted until she resembled a newborn pug."
        "Big fat tears dripped from her eyes as she buried herself inside Kryska's bosom."
        ica "WAAHHHHH!!!!!!!!!!!"
        "Shields laughed in spite of the pain shooting through his body."
        kay "We did it..."
        "He wrapped his arms around the two of them."
        kay "We... WON!!!"
        
        hide kryska with dissolve
        
    $dshow("claude boobsnurse happy neutral neutral",xpos=0.25,ypos=1600)

    "Just then, old Claude burst into Engineering, escorted by ship security."
    cla "O-oohh!!! C-Captain...!!"
    "Despite their injuries, the two of them struggled to their feet."
    "With grins on their blood stained faces, Shields and [girl] waved."
    "Soon, they were both on stretchers, while ship security detained Chigara, who had already surrendered peacefully."
    "With Alice dead, and Chigara never having entered the mindstream, there was no risk of Alice's ghost ever reasserting control over her again."
    
    hide claude with dissolve
    hide asaga with dissolve
    hide sola with dissolve
    hide ava with dissolve
    hide icari with dissolve
    hide kryska with dissolve
    
    "The crew rushed to contain the damage in Engineering as Shields was ferried towards sickbay."
    "Between the moving bodies of the crew, he saw a familiar locket of pink hair."
    
    $dshow("claude neutral smile neutral neutral")
    
    cla "Teehee. Looks like you pulled it off, captain..."
    "A second Claude watched the events unfold from the shadows."
    
    $dshow("claude neutral smile closed neutral")
    
    cla "Mah... I guess this is the end."
    cla "If you ever need me... You know where to find me."
    
    hide claude with dissolve
    
    "But a blink later, she completely vanished from the universe."
    
    scene white with dissolvemedium
    
    "Shields closed his eyes."
    "The past had been rewritten. The future had been saved."
    "The Liberation Day Massacre was averted."
    "The world began to fade to white, as the Law of Causality reconfigured the universe based on what he had accomplished."
    "In the universe which will be created... The Sunrider would emerge triumphant during the Battle of Cera. Chigara, the Prototypes' spy, would be apprehended safely. And Shields would have prevented an intergalactic war between the Alliance and PACT."
    "... ... ..."
    "... ..."
    "..."
    kay "Not bad for a day's work..."
    kay "But next time... Let's try to get it right the first time around."

    play music "Music/Sora_no_Kodoh.ogg" fadeout 1.0
    call dlc_credits

label epilogue_start:
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    
    scene black with dissolvemedium
    scene bg shrine with dissolvemedium
    
    $dshow("ava handonhair neutral narrow neutral",xpos=0.3)

    "Shields knelt before Maray's grave."
    "At long last... He had put her soul to rest, up in that mountain of their childhoods."
    "Beside him, Ava laid a bouquet of flowers next to a headstone marking her father's final resting place."
    kay "Maray..."
    kay "I'm... sorry..."
    kay "You were... so proud... to hear I had finally become a captain. You told all your friends I would protect Cera the instant you found out..."
    kay "But... I let you down. I... let everyone down..."
    kay "Ever since that day... I swore to myself... I would come back here. That I will take back what we lost that day..."
    kay "And after so many trials... Here I am... Finally home."
    
    show maray lean sadsmile:
        xpos 0.7
    with dissolve
    
    mar "Kayto..."
    "Maray put her hand on his shoulder."
    mar "You never had to blame yourself..."
    "Upon hearing her voice, tears dripped down his eyes."
    
    show maray excited happy with dissolve
    
    mar "Ever since you told me you were going to follow Avvy... I knew you could do it! I knew you could become the biggest space captain there ever was and win against impossible odds!"
    
    show maray lean narrowsmileblush with dissolve
    
    mar "I'm... not sad I came to see you off that day... Even though I would still be alive... I wouldn't be able to call myself your sister if I missed a thing like that."
    mar "Don't worry about me...!"
    mar "Now... I can watch over you from this mountain..."
    mar "No matter where you go... I'll look up to the night skies... and find you somewhere, amongst the stars."
    mar "I know... you will always be the mightiest captain who ever lived... who will defeat the biggest villains... and save the galaxy over and over... because..."
    
    show maray lean sadhappy with dissolve
    
    mar "You're... my big brother, Kayto. You can do anything!"
    mar "You never let me down! Not even once!"
    kay "Mar... ay....!!"
    "Shields gripped his fist and sobbed into her grave."
    kay "I swear... I'll never betray your trust... For as long as I live... I'll defend everyone..."
    kay "No matter what may face me... No matter the odds... I'll fight on..."
    kay "So that I can return here... and keep you company..."
    kay "I'll tell you stories of adventures... of narrow escapes and victories snatched from the jaws of defeat... You'll be on the edge of your seat each time."
    kay "Maray... Your brother's going to keep fighting...!"
    kay "Cera's... not safe yet! There's... more work to do!"
    kay "I'm... not ready to quit being Captain Kayto Shields... Not yet."
    kay "I'm... going to return to space. And this time... I'll be leaving you here."
    
    show maray lean smileblush with dissolve
    
    mar "Mm. I'll keep watch from this mountain."
    mar "Good luck, Kayto! And... have a safe trip."
    kay "Yeah... Of course..."
    kay "Nobody's going to take down your big brother!"
    mar "Eh-heh..."
    
    show maray lean smileblush:
        ease 0.5 alpha 0.5
    
    "With that, Maray's apparition slowly faded away."
    "She wrapped her arms around Kayto's head."
    mar "I... love big brother...!"
    mar "Keep us all safe, okay?"
    kay "Yeah..."
    kay "It's a promise!"
    mar "Mm!"
    
    play music "Music/Colors_Loop.ogg" fadeout 1.5
    hide maray with dissolvemedium
    
    "Maray vanished into the fall wind. The leaves in the forest rustled as her spirit echoed through the mountain before finally dispersing into the great beyond."
    "Instead of lamenting her final disappearance, Shields stood with a tear soaked grin."
    kay "I'll... be back, Maray!"
    
    $dshow("ava handonhair neutral neutral sad",xpos=0.5)
    
    ava "Kayto? Are you ready?"
    kay "Yeah. How'd things go on your end?"
    
    $dshow("ava handonhair smirk narrow sad")
    
    ava "My father always was a man of few words."
    ava "I am sure he would merely nod and accept my return if he were still alive."
    ava "But..."
    ava "Perhaps deep underneath his cool and rational exterior... he would be pleased to see me return alive, my mission a success. I may even venture as to say he might feel a tinge of pride in his old heart."
    
    $dshow("ava handonhair smirk closed laugh")
    
    ava "Heh. Hahaha..."
    ava "I'm making an idiot of myself, no?"
    kay "No."
    kay "You... take after him in many ways."
    kay "And I can tell from your smile right now... He would definitely be overjoyed as well."
    
    $dshow("ava handonhair smirk neutral neutral")
    
    ava "Heh. I... must have gone soft, no thanks to your influence."
    kay "Well... never hurts to smile every now and then. Heard it helps offset the effects of aging."
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "Captain..."
    kay "Haha... Hahahaha!!"
    
    hide ava with dissolve
    
    "From the mountain, they could see that most of Cera City was still an enormous crater..."
    "The Legion's attack had bored a scar into their beautiful city... One that they may never forget..."
    "But reconstruction efforts were already underway. The Alliance had already brought money, workers, and resources to restore the city, while Fontana has likewise pledged to make amends for PACT's wanton actions."
    "Shields looked to the remains of the city he once called home..."
    "There was still work to do... But for the first time in his life... He felt victorious. Not a fleeting sense of accomplishment after winning a small skirmish, but an overwhelming sense of having won something important. It resounded through his entire body, giving him strength."
    "With that, the two of them hiked back down the mountain..."

    scene black with horizontalwipe
    play music "Music/Colors_main.ogg" fadeout 1.5
    scene bg park with horizontalwipe    


    "The sun set over Cera National Park. The Liberation Day celebration had just ended."
    "It was a grand affair, where Admiral Grey took to the stage to commend the fighting spirit of Cera's only surviving assault carrier and presented Kayto Shields with the Feraldan cross. There were parades, a full orchestra, as well as enough Alliance and PACT dignitaries to last a lifetime."
    "In reality, Kayto Shields did not care too much about receiving honors or trying to find influence by befriending powerful Alliance figures."
    "Instead, his only thoughts were about..."

    if girl == "Asaga":
        jump asaga_epilogue
    if girl == "Sola":
        jump sola_epilogue
    if girl == "Icari":
        jump icari_epilogue
    if girl == "Ava":
        jump ava_epilogue
        
label asaga_epilogue:
    
    $reset_sprites()
    $dshow("asaga leanforward happy neutral neutral",ypos=1600)

    asa "Oh! There ya are, capt'n!"
    asa "Eh-heh... Mah, congratulations on your medal."
    
    $dshow("asaga leanforward grin closed neutral",ypos=1600)
    
    kay "Eh, you mean this thing? Heh, you wanna bite into it later?"

    $dshow("asaga armscrossed yell neutral up")

    asa "Eeehh... It's your precious award, captain... I couldn't..."
    kay "Or maybe you'll be biting into me later."
    
    $dshow("asaga leanforward grin closed neutral blush",ypos=1600)
    
    asa "That... can be arranged. Hufu."
    "Despite the old universe being destroyed, Asaga and Shields' feelings for each other remained."
    "Not even the end of the universe could change the feelings Asaga had for her captain. From the moment they met, Asaga had been the defender of the Sunrider and the ace of the ryder wing."
    "Asaga put her arms around Shields."
    
    $dshow("asaga armscrossed happy neutral up")
    
    asa "So... The evil empire is defeated... Our home worlds are liberated..."
    asa "What's next?"
    "Shields looked up."
    kay "We're not done yet."
    kay "According to the intel we've got from Lynn, there's still a Prototype greater than the one we killed."
    kay "We can't rest until she has been defeated as well."
    asa "... ... ..."
    asa "I..."
    
    $dshow("asaga excited yell neutral angry")
    
    asa "I'm going to stay onboard the Sunrider!"
    asa "I've already told the Council that they can rule Ryuvia Prime in the interim... Right now, there's another battle waiting for me!"
    asa "In the end... that's the duty of the Sharr. To defend Ryuvia from all threats."
    asa "Anyways, it's obvious I'm going to accomplish a lot more inside a ryder than on a cushy ol' throne at least!"
    asa "I'll always protect you, captain! Until the day we've finally restored peace to the galaxy!"
    kay "Heh..."
    "Shields smiled and stroked Asaga's head."
    kay "Yeah..."
    kay "You and I... Together."
    kay "The next big bad better be shaking in their boots. 'Cause we've got our hero of justice right here..."
    
    $dshow("asaga armscrossed uu closed sad comiccry")
    
    asa "Huu... Captain, you're still not taking me seriously at all... are you...?"
    kay "Hah! Hah! Hah!"
    
    $dshow("asaga point happy closed neutral")
    
    asa "Ah mou! You go and make me into a woman, but still have the gall to treat me like a kid! You better take responsibility and look at only me from now on!"
    kay "Understood!"
    "Shields saluted."
    
    $dshow("asaga armscrossed uu neutral sad2")
    
    asa "Huu..."
    
    $dshow("asaga armscrossed kitty closed sad2")
    
    asa "Oh well."
    
    $dshow("asaga leanforward happy neutral neutral",ypos=1600)
    
    asa "Captain..."
    asa "Let's... kick some ass together, all right?"
    kay "Yeah..."
    kay "All for one..."
    
    $dshow("asaga point happy neutral neutral")
    
    asa "One for all!!"
    "Shields put his hand on Asaga's cheek."
    "He brought her to his face and locked their lips together."
    
    $dshow("asaga armscrossed happy narrow2 down blush")
    
    asa "... ... ..."
    
    hide asaga with dissolve
    show black:
        alpha 0.5
    with dissolve
    window hide
    
    nar "As the two of them kissed, the first stars of the coming night shone in the pink navy blue sky..."
    nar "Many unresolved questions still lingered in Asaga's heart."
    nar "One day, she would have to return to Ryuvia Prime and finally accept her position as Queen."
    nar "When that day came, would her relationship with Shields be allowed to continue? Or will she be caught in a new game of political intrigue?"
    nar "What was the truth of her powers, and why did the Prototypes view her with such interest?"
    nar "Lynn's words echoed in Asaga's heart. One day, she would wield the Sharr'Lac and conquer the known galaxy. Asaga had no idea whether Lynn was merely trying to toy with her mind or if she had spoken the truth."
    nar "Such a prophecy seemed implausible, as all the Sharr'Lacs had been destroyed millennia past, and Ryuvia was now but a minor backwater planet."
    nar "Asaga closed these questions away and put them aside for another day."
    nar "In the meantime, she was more than content to be at Shields side, fighting alongside him to protect the galaxy."

    jump theendfornow
    
label sola_epilogue:
    
    $dshow("sola back neutral neutral neutral")

    sol "Alas... The clamor of parties ill suits me..."
    "Sola awkwardly hid out of sight behind a tree, far away from the din of the crowd."
    "Despite the old universe being destroyed, Sola and Shields' feelings for each other remained."
    "There was still much Shields had not yet discovered about Sola's past. He still had none of the specifics of how she had become Sharr, or how she had been flung from time, two thousand years into the future."
    "In fact, so much of the girl he now liked was shrouded in mystery..."
    kay "There you are..."
    sol "I remember attending many similar functions in my timeline... They were thoroughly exhausting events, where men and women alike maneuvered to manipulate me."
    sol "A single wrong word could very well mean my death... By the end, I was more drained after a social gathering than I would have been if I had fought a thousand of my uncle's ships..."
    kay "I wish I could say that things have changed... but..."
    "Shields leaned against the tree, joining Sola in her hiding spot."
    
    $dshow("sola armhold neutral neutral neutral",xpos=0.5)
    
    sol "In any matter, drawing attention to myself here would only cause complications for you, so I shall refrain from taking actions which may expose my true identity to the Alliance."
    kay "All right. Honestly, I beat a hasty exit as soon as I could too."
    kay "Heh, I'd hate to waste an evening at the park with a bunch of cruddy politicians and reporters when I have you to spend it with."
    
    play music "Music/Colors_sad.ogg" fadeout 1.5
    $dshow("sola armhold smile narrow sad blush")
    
    sol "A-ah..."
    sol "M-must you always keep speaking such outrageous words..."
    kay "I've always dreamed of coming back here. When I was a child, I went to this park with my family almost every weekend."
    kay "We'd all sit right over there... My dad would grill meat on the barbecue, while I ran around with my sister, our dog chasing after us..."
    "Shields held back the tears which began to form in his eyes."
    kay "Heh..."
    kay "Even though that's now a thing of the past... Being here with you feels almost the same, Sola."
    sol "Yes..."
    sol "Perhaps humans are not meant to be alone."
    sol "While the silence it brings has its own merits... sometimes..."
    sol "It hurts."
    sol "To bear your troubles by your lonesome."
    sol "... ... ..."
    "Sola stood silently. Shields knew that she was in deep reminiscence."
    "No doubt, her story was a long and complicated one. One which had caused her unspeakable grief."
    "He knew that he may never fully heal the scars of Sola's past. But he still felt compelled to stand by her and help lift the burden she carried."
    kay "Sola... You're not going to be alone any more. Because from now on, I'll always be with you..."
    sol "Is that... the truth?"
    kay "Yes."
    
    $dshow("sola armhold smile closed sad blush")
    
    sol "Ah-haha..."
    
    $dshow("sola armhold frown narrow sad blush")
    
    sol "Captain, you mustn't make promises you cannot keep."
    sol "Misfortune has always been my shadow. No doubt, many more sorrows await me..."
    "Sola's lips trembled."
    sol "Are you truly prepared to face what may come?"
    kay "Sola..."
    "Shields lifted her chin with his finger and sealed his promise with a kiss."
    
    $dshow("sola armhold smile closed sad blush")
    
    sol "Ah..."
    kay "... ... ..."
    
    $dshow("sola armhold smile narrow sad blush")
    
    sol "You are a troublesome man..."
    sol "T-to pluck the flower off a virgin's lips so casually..."
    kay "Haha."
    "Shields put his arm around her."
    kay "Look, we've liberated Cera and beat back PACT. What else could possibly happen?"
    
    $dshow("sola armhold frown narrow sad blush")
    
    sol "Captain... please refrain from jinxing the happy ending..."
    sol "Ah, I truly cannot live with an uncouth man like you..."
    sol "I fear my sensibilities will be torn asunder in a matter of days..."
    kay "Ah, sorry, Sola! I promise, I'll behave from now on! A true gentleman, I swear!"
    "Sola buried herself into his chest."
    
    $dshow("sola armhold smile closed neutral blush")
    
    sol "But... it is that bold side which I like the best about my captain..."
    sol "As expected... ah... I am truly in love with you... There is no helping it..."
    "She closed her eyes as Shields stroked her soft hair."
    kay "Yeah..."
    "Shields felt as if he had gained something very valuable. A precious treasure, which he now needed to protect with all his life."
    "No matter what happened... He would make sure the tragedies of Sola's past never repeated themselves."
    "He swore it with all his heart..."

    #Night Street
    
    scene bg city with dissolve

    "Night fell and the two of them returned to their hotel."
    
    $dshow("sola armhold smile narrow sad blush")
    
    sol "... ... ..."
    kay "Well, here we are."
    "Shields leaned down and gave a kiss good bye."
    kay "Well then... uhh... I'll see you tomorrow?"
    sol "... ... ..."
    "Sola hung onto the cuff of Shields' sleeve."
    sol "A-ah..."
    kay "... ... ..."

    play music "Music/Colors_Loop.ogg" fadeout 1.5
    scene black with dissolvemedium
    scene bg hotelroom with dissolvemedium
    
    $dshow("sola armhold smile narrow sad blush")
    
    "Sola leaned against Shields' door, her body trembling with apprehension. To calm her down, Shields wrapped his arms around her and locked their mouths together."
    sol "Ah..."
    
    $dshow("sola armhold smile closed sad blush")
    
    "Their tongues gently glided against each other. At first, Sola hardly moved her tongue at all, but Shields gradually coaxed it from her mouth."
    "As their mouths pressed together, Shields was overwhelmed with Sola's bittersweet taste. The aftertaste of distant sadness lingered in his mouth."
    "Determination to wipe away her sorrows welled up in him, making him run his arms into her back and touch her all over, showering her with affection."
    
    if CENSOR == False:
        call censor_solahscene
        
    show black:
        alpha 0.5
    with dissolvemedium
    
    window hide
    
    nar "In the end, Shields knew nothing of what Sola was talking about."
    nar "Her past was shrouded in mystery. And her future was still uncertain."
    nar "Shields had believed that her suffering had ended. That she had escaped her life of being a pawn when she escaped her timeline. Little did he know of how wrong he was..."
    nar "Even in this timeline... a dark future awaited her."
    nar "Ryuvia was only big enough for a single Sharr."
    nar "Sola would once again become a political tool in a new deadly game..."
    nar "In the end... she was an existence which broke the natural order of the galaxy. And one day... the she would be confronted with the ultimate decision..."
    nar "But that day was not today."
    nar "Because today, for the first time in her life, Sola felt happiness swell through her body."
    nar "Even though she knew her happiness would be fleeting... and accepted in her heart that her ending would be bittersweet at best..."
    nar "She was glad to have been loved by Kayto Shields."

    jump theendfornow

label icari_epilogue:
    
    $reset_sprites()
    $dshow("icari armscrossed talk neutral angry")

    ica "What? Why are you staring at me like that for?"
    kay "Nothing..."
    kay "Just thinking... uhh... you up for something after this? I know some places around here..."
    
    $dshow("icari handonhip smile neutral neutral")
    
    ica "Heh. I thought you'd never ask. Honestly, I can't wait to blow this joint. Aah, these media events really aren't my thing..."
    "Despite the old universe being destroyed, Icari and Shields' feelings for each other remained."
    "Even though she had started as his enemy, Icari proved to be the ship's stalwart defender in the end. Without her help, Shields would never have been able to thwart the Prototypes."
    "Now, if only she could become more honest about her feelings..."
    
    $dshow("icari armscrossed talk confident embarass")
    
    ica "Well, I guess things turned out pretty well. The war's over and Cera's been liberated. Maybe you're not just a schoolboy after all."
    ica "Hmph! Be grateful! I-I might even call you \"captain\" properly from now on. Ah, don't get all excited though! You've still got a long way to go before I like you!"
    kay "Sure, you say all that, but you still gave me quite a passionate kiss before the battle..."
    
    $dshow("icari point shout neutral angry blush")
    
    ica "T-that was just to make a point! Ah, don't get all high and mighty just 'cause of that one kiss, cap! H-hmph! I'll have you know, I kissed with captains a lot more impressive than you! I-i-in fact, I've broken hearts all across the galaxy! S-so hah! Y-you're just a cherryboy to my eyes!"
    kay "Oh really..."
    
    $dshow("icari point shout neutral angry blush",xpos=0.3)
    $dshow("kryska fistup happy neutral angry",xpos=0.7)
    
    kry "Ah, there you are, mercenary! Hah! I see you are once again with your husband to be!"
    ica "E-eehh!?"
    kry "You best resolve your feelings before we return to active duty! No doubt, paperwork will have to be filed before the higher ups approve of a relationship between a civilian contractor and an officer of the armed forces. But if you ever need a character reference, I shall always be glad to provide assistance!"
    ica "Oy, I'm... not going out with this... loser!!"
    kry "Ah, but just the other night, I saw you staring at a holograph of the captain for ten minutes, before finally sighing wistfully and rubbing it into your face!"
    kry "I can see it in your face! This is definitely first love!"
    
    $dshow("icari armscrossed shout closed embarass blush",xpos=0.3)
    
    ica "F-f-f-f-f-f-f-f-first.... LOVE!?!?"
    "Icari's face glowed so red it looked like it was going to melt like paraffin wax."
    kay "Hahaha! That really does sound a lot like Icari, doesn't it?"
    kry "Indeed, captain! Hah! Hah! Hah!"
    kay "Hah! Hah! Hah!"
    ica "Huuuuuuuuuu.........!!!"
    
    show layer master at tr_xshake
    $dshow("icari point shout neutral angry blush",xpos=0.3)
    
    ica "IT'S NOT LIKE I LIKE YOU OR ANYTHING-----!!!!"

    play music "Music/Colors_sad.ogg" fadeout 1.5
    scene black with horizontalwipe
    scene bg beach2_night with horizontalwipe

    "Later that evening, Shields took his date to a secluded beach."
    "He had discovered this cove many years ago. It was a spot he had spent with Maray on numerous occasions, collecting sea shells and diving into the clear waters."
    "The fresh air coming from the ocean felt cool against his chest. He took a deep breath, the familiar sight and smells warming him with nostalgia."
    "Icari clambered down some rocks and met him."
    
    $dshow("icari zarmscrossed_swimsuit talk neutral embarass blush",xpos=0.5)
    
    ica "It's been a while since you've seen me like this... W-well...?"
    kay "I couldn't ask for a better sight. Ten out of ten, Icari."
    
    $dshow("icari zarmscrossed_swimsuit talk confident embarass blush")
    
    ica "W-what are you saying... Idiot..."
    ica "Aah, smiling your face off just because I'm wearing a swim suit... You're really a pervert, aren't you?"
    ica "Just so you know, this is a special service, all right? Reserved for only captains who really impress me! So y-you better be grateful, you cherryboy! H-hmph!"
    kay "All right, all right..."
    "The two of them walked along the beach."
    
    $dshow("icari zarmscrossed_swimsuit frown neutral embarass blush")
    
    ica "... ... ..."
    ica "... ..."
    ica "Huuu..."
    "Icari trembled with irritation."
    
    $dshow("icari zhandonhip_swimsuit shout neutral confident blush")
    
    ica "Well? A-aren't you going to hold my arm...?"
    kay "Heh."
    "Shields took her up on the offer."
    "She leaned in, squeezing the side of her boob against him."
    
    $dshow("icari zarmscrossed_swimsuit frown neutral embarass blush")
    
    ica "... ... ..."
    kay "You know... Sometimes I wonder if your whole tsundere routine's just an act... You really do take it too far..."
    ica "Eeh? What are you talking about?"
    ica "I can't help acting like this... This is just the way I am..."
    ica "Whenever something bothers me... I just can't stop thinking about it... and it just makes me wanna throw myself onto the floor and pound my fists and feet on the ground like a brat..."
    ica "But getting all emotional's pointless... Crying isn't going to do anything to fix my problems..."
    ica "My emotions always get the better of me... They're things that a mercenary don't need. So... I boxed them away, somewhere..."
    ica "And ever since then... I've forgotten how to be honest with my feelings..."
    
    $dshow("icari zarmscrossed_swimsuit frown closed embarass blush")
    
    ica "... ... ..."
    ica "Ah mou, I get it! You think I'm just annoying, don't you!? I bet you're wishing you were with the commander right now! \"I knew my childhood friend was the superior tsundere!\" That's probably what you're thinking, isn't it?!"
    kay "Icari..."
    "Shields turned to face her."
    kay "No. You're the only one I care about."
    
    $dshow("icari zarmscrossed_swimsuit neutral neutral sad blush")
    
    ica "E-eh...?"
    
    $dshow("icari zarmscrossed_swimsuit neutral closed sad blush")
    
    ica "Y-you idiot... If you say things like that....."
    "Shields leaned in and plucked a kiss from her lips."
    ica "Ah..."
    
    $dshow("icari zarmscrossed_swimsuit neutral neutral sad blush")
    
    ica "Mou..."
    ica "Stupid captain..."
    
    play music "Music/Colors_Loop.ogg" fadeout 1.5
    $dshow("icari zarmscrossed_swimsuit neutral closed sad blush")
    
    "Icari leaned in and pressed her lips against Shields, her tongue gently caressing his."
    "Shields wrapped his arms around her back, bringing her against his chest. He ran his palms against her smooth back."
    "The floodgates of Icari's hesitation broke apart and their kisses intensified. Their hands ran against their skin, marveling at each other's physiques."
    "They separated, panting."
    
    $dshow("icari zarmscrossed_swimsuit neutral neutral sad blush")
    
    ica "Ah... crap... I'm... totally gonna regret this..."
    "Icari's lips trembled as Shields stroked her back."
    ica "S-stupid captain... Y-you're already hard in your trousers... M-mou..."
    ica "G-getting like that from just a kiss... You're... really just a horny schoolboy after all!"
    "Shields' hand slid down Icari's back and came to rest on her ample ass, his fingers between her legs."
    kay "Cheater. I bet you're secretly soaking wet here..."
    
    $dshow("icari zhandonhip_swimsuit shout closed confident blush")
    
    ica "A-as if...! H-hmph! L-l-like you could turn me on in a million years!"
    ica "Heh! G-go ahead and check yourself if you want! Then you'll see that it's dry as a desert!"
    kay "That was an invitation."
    ica "Aah mou...! Shadup!"
    "Shields pushed aside Icari's bikini panties and examined her opening."
    
    if CENSOR == False:
        call censor_icarihscene
    
    show black:
        alpha 0.5
    with dissolvemedium

    nar "And so the two became lovers that day..."
    nar "Many secrets still laid deep inside Icari's heart..."
    nar "How had she become a mercenary after her parents' death? What was the story of the day she chose to lock her true emotions away for good, and live guided only by the cold, hard facts?"
    nar "But those were tales Shields would have to discover another day... Because right now, she was crying tears of happiness into his arms."
    nar "For a brief moment, she had opened her heart to him and showed him her true emotions."
    nar "While the very next morning, she would return to acting the part of the cool mercenary who definitely didn't have any feelings for the stupid captain, Shields knew that he would one day discover the true Icari..."
    nar "But when that day came..."
    nar "Just how would their feelings for each other change?"
    
    jump theendfornow
    
label ava_epilogue:
    $reset_sprites()
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "Captain, please do not stare at me with those eyes."
    kay "Ava?"
    ava "Sigh... Can you not see that we are surrounded by the most powerful men and women of the Alliance right now? And under the lens of virtually the entire galaxy's press corps."
    
    $dshow("ava fingerup talk neutral angry")
    
    ava "If word got out about our... relationship... our reputations would surely be dragged through the mud in every tabloid from Solaris to New Eden."
    kay "Hahah! Don't worry too much! It's not like Command can fire me at this point!"
    
    $dshow("ava handonhip talk neutral angry")
    
    ava "Captain... You are far too lackadaisical about this whole affair. Ah... Even your uniform is wrinkled! Ah mou..."
    "Ava did her best to straighten his jacket."
    ava "T-this is how the galaxy is going to see Captain Kayto Shields...?"
    kay "I'm not interested in presentation, I'm afraid... I'm just here to get the job done."
    "Ava sighed in hopelessness."
    
    $dshow("ava armscrossed shout closed angry")
    
    ava "Yes captain. I am painfully aware of that fact."
    "Despite the old universe being destroyed, Ava and Shields' feelings for each other remained."
    "Even if they ruffled each other's feathers from time to time, Ava would always stand watch over the captain, ever the loyal advisor and partner."
    "In a way, the two of them were destined from the very beginning to stay together. A partnership where each one covered for the other. Standing alone, neither Shields or Ava could be described as perfect, but together, they formed a complementary whole."
    "In the end, they were respectively the father and mother of the Sunrider."
    kay "You know Ava..."
    kay "One time... I thought about settling down on Cera after all of this was over..."
    kay "Just living the rest of my life out in peaceful retirement, far away from danger."
    kay "But... do you suppose we could ever do that?"
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "... ... ..."
    ava "Captain. My place is onboard the Sunrider."
    
    $dshow("ava handonhair neutral neutral sad")
    
    ava "I was never too attached to this place. All it brings me are memories of my childhood."
    ava "I can hardly remember my mother. But ever since she left, I remember a desolate household. And a father who never deigned to show a moment of affection during the few times of year when he was home."
    ava "In fact, I quite enjoy the thought of traveling the galaxy. I would rather not sink my roots too deep anywhere."
    kay "I see..."
    "Shields looked at the damaged skyline of the city. Many of the buildings he remembered were now demolished, and replaced with structural struts as reconstruction work commenced."
    kay "I've... always wanted to return to this place. But..."
    kay "I guess home will always be where your family lives."
    kay "There's... nothing more for me to do here."
    kay "I've concluded my business here. I think it's time for me to return to space too."
    kay "There's... still a lot we have left to accomplish together."
    kay "What say we continue... as captain and XO? No..."
    kay "As... partners."
    
    $dshow("ava salute neutral neutral angry")
    
    ava "Sir!"
    
    $dshow("ava handonhair neutral narrow neutral")
    
    "Ava began to salute, but caught herself."
    ava "... ... ..."
    kay "I... don't mean it like that, Ava."
    kay "I've... always loved you. I want to stay by your side."
    kay "Wherever you are... will always be my home now. You're... all I have left."
    ava "... ... ..."
    ava "No..."
    ava "That is far from the truth."
    "Ava turned, to where the crew of the Sunrider was chatting at the banquet table."
    ava "We have them now."
    "Shields looked at the girls he had gathered from across the galaxy."
    "Asaga was busy trying to get Sola to socialize with the others, filling her plate with more food than she could eat."
    "Icari and Kryska were already busy arguing about Alliance ryder equipment. Meanwhile, it looked like Claude was being eye ogled by a circle of important Alliance men. Seriously, what was she doing, chatting up with those guys...? Did she have some kind of geezer fetish?"
    kay "Heh... You're right..."
    "Shields put his arms around Ava."
    kay "We'll protect them together. Our crew."
    
    $dshow("ava handonhair neutral narrow neutral blush")
    
    ava "... ... ..."
    kay "Let's return. To our home."
    ava "Yes... Kayto..."
    
    show black:
        alpha 0.5
    with dissolve
    
    nar "But doubt creeped into Ava's heart."
    nar "Did she truly love the man called Kayto Shields? Was she capable of loving someone at all?"
    nar "Or was she but a calculating machine, capable only of crunching numbers and deducing detached conclusions from the cold hard data?"
    nar "She knew that one day, Shields' feelings for her would prove his downfall. And she would have to be there to save him when that day came."
    nar "She made a resolution deep in her heart. She would always protect Shields. Even from himself. And to do that, she could not let his love for her blind him from what had to be done."
    ava "(I... will always be your XO... Above everything else.)"
    ava "(Perhaps... that is the best gift I could give you...)"
    ava "(My days here were empty... devoid of colour... Merely an endless repetition of the same, pointless movements...)"
    ava "(Save for one thing...)"
    ava "(The sound of your laugh, whenever I was frustrated... It would drive me up the wall... But... it was what got me through those times.)"
    ava "In the end... it was... you..."
    
    hide black with dissolve
    
    kay "What? Did you say something, Ava?"
    
    $dshow("ava handonhip neutral neutral neutral")
    
    ava "No."
    ava "I was merely murmuring to myself. Please disregard my sudden flight of fancy."
    ava "In any matter, let us not stand here by our lonesome. We have much work to do, no?"
    
    $dshow("ava fingerup talk neutral angry")
    
    ava "I personally intend to speak with the Alliance finance minister, so that we can acquire more funding for the reconstruction efforts. As the man of the hour, I fully expect you to do the same, captain!"
    kay "W-wha... Ava, you know I'm not good at stuff like that..."
    ava "Not buts, captain! The security of Cera is at stake here!"
    kay "U-understood..."
    
    hide ava with dissolve
    
    "With that, Ava pushed Shields away."
    "Despite that, he secretly smiled to himself. He still remembered the look on Ava's face that night, when they..."
    "That was certainly not the look of a woman with no sexual appetite for him."
    kay "Heh..."
    "No matter how cold she acted towards him... Shields knew that she wanted him with all her heart."
    kay "(What a complicated woman...)"
    kay "(Ah well! I'm sure this will sort itself out... eventually.)" 
    
    jump theendfornow

label theendfornow:
    
    if girl == "Asaga":
        $renpy.save("ASAGA HAPPY END")
    if girl == "Ava":
        $renpy.save("AVA HAPPY END")
    if girl == "Sola":
        $renpy.save("SOLA HAPPY END")
    if girl == "Icari":
        $renpy.save("ICARI HAPPY END")
    
    play music "Music/Colors_of_an_Orchestra_II.ogg" fadeout 1.5

    scene black with dissolvemedium
    scene bg brig with dissolvemedium

    "One month later..."
    "After a much deserved period of R&R, Shields had finally returned to his trusty ship. While his days on Cera went by in a flash, in the end, Shields could not rest easy until he had returned to what had become his new home."
    "And on top of that, Shields had managed to transfer a certain prisoner to his ship, ostensibly for \"field counter-intelligence purposes.\""
    "He pressed the intercom and spoke with Chigara."
    
    $dshow("chigara handonchest smile neutral neutral")
    
    chi "Ah... Captain..."
    kay "Chigara..."
    kay "Sorry about the small cell... We're actually trying to build you a better one as we speak. For now... Uhh... Please bear with it..."
    
    $dshow("chigara armsbehindback smile neutral embarass")
    
    chi "Don't worry, it doesn't bother me at all."
    
    $dshow("chigara armsbehindback frown neutral embarass")
    
    chi "In fact... It's Chigara who's sorry for everything..."
    chi "I know you have no reason to believe me... And I don't expect you to ever forgive me for what I've done... But I never knew myself that the Prototypes had planted me onboard the ship..."
    
    $dshow("chigara handonchest neutral narrow sad")
    
    chi "All this time... I thought I was the sole survivor of the Diode Catastrophe... And that I was the ship's chief engineer... But... it looks like I was fooled too, wasn't I?"
    chi "Chigara... was just a fool all the time. Playing right into the Prototypes' plans..."
    chi "I... wouldn't be surprised if the captain hates me now..."
    kay "No."
    kay "You're just a victim in this too, Chigara. You never knew what the Prototypes were planning either. You were just an unwitting pawn..."
    kay "Honestly, I'd be damned glad to have you as the ship's chief again..."
    kay "But as long as the Alpha Prototype still lives... She can assume control of your body... So we can't let you out."
    kay "Not yet. Not until we've finally found the Alpha and destroyed her."
    kay "Then... you'll finally be free again."
    kay "I promise... I'll get you out of that cell, Chigara... and make sure the Prototypes never take control of your body ever again."
    kay "You have my word."

    $dshow("chigara handonface smile closed sad blush")

    chi "M-my..."
    chi "I see the captain certainly has not lost his touch..."
    
    $dshow("chigara handonface smile neutral neutral blush")
    
    chi "Eh-heh... Chigara's happy to hear that..."
    chi "But please do not make [girl] too jealous, okay?"
    kay "H-huh...?"
    
    $dshow("chigara holdinghands frown neutral embarass")
    
    chi "In the end... I hurt you, captain..."
    chi "I don't mind you finding someone else..."
    
    $dshow("chigara holdinghands smile closed embarass")
    
    chi "As long as the captain pays her some visits from time to time. Okay?"
    kay "Yeah... Let me know if you need anything."
    chi "Understood!"

    scene black with horizontalwipe
    scene bg office with horizontalwipe

    "Shields entered his old office..."
    "He had spent countless hours in here, agonizing over plans to lead a one ship war against PACT and liberate Cera..."
    "After every victory, he felt as if he stood at the top of the world. He had somehow won against an overwhelming enemy..."
    "While some nights, the weight of commanding the ship crushed down on his back. He would realize the futility of his mission and despair he would most likely never survive to see a liberated Cera."
    "Now that his mission had been accomplished, he felt surreal walking through all the memories he had of this office."
    "His thoughts were interrupted by an unexpected noise."
    
    show dog with dissolve
    play sound "sound/dog.ogg"
    
    "Dog" "Arf!"
    kay "What the-"
    "Someone had placed a basket beside his desk. A dog popped its head out from the top and panted friendlily at Shields."
    kay "Well, what do we have here..."
    
    $dshow("ava handonhip smile neutral neutral",xpos=0.4)
    
    "As if on cue, Ava slipped inside the office."
    ava "Ahem..."
    kay "Hey Ava, are you the one behind this?"
    ava "Indeed, captain..."
    "She straightened herself."
    ava "In light of recent events... I thought animal companionship may help keep your nerves smooth during our next voyage."
    ava "As such, I have arranged for the transfer of a... erm... K9 unit to serve on board the ship."
    kay "Well, you definitely know me too well. In fact, I used to have a dog which looked just like him... Don't you remember?"
    ava "I recall him quite well. I hope his protégé proves as reliable as Fleet Admiral."
    kay "Well hell....."
    kay "Hardly a day onboard the ship, and the damned mutt already outranks me."
    "Shields shook his head and delivered a salute to his new pet."
    kay "Captain Kayto Shields at your service... Admiral."
    play sound "sound/dog.ogg"
    "Admiral" "Arf!"
    "He gave Admiral a scratch behind his ears and turned to Ava."
    kay "Well then commander."
    kay "Shall we get underway?"

    play music "Music/The_Final_Battle.ogg" fadeout 1.5
    scene bg bridge with horizontalwipe
    
    $dshow("ava handonhip smile neutral neutral",xpos=0.5)

    "Shields and Ava strode into the bridge of the Sunrider."
    kay "What's the situation?"
    
    $dshow("ava handonhip talk neutral angry")
    
    ava "Three days ago, PACT forces raided the Alpha Prototype's cloning facility at Diode, but by then, it was already abandoned."
    ava "Her current whereabouts are unknown. Our primary objective is the capture or destruction of the final leader of the Prototypes."
    ava "Not only that, but we are needed for an urgent mission from the Alliance."
    ava "Entire colonies have begun to vanish near the Mnemosyne Abyss. We are to join a combined Alliance-PACT investigatory fleet and find out what's going on."
    
    $dshow("ava handonhip neutral neutral angry")
    
    kay "Ah, I know this plot line... Obviously an alien race from another galaxy intent on destroying all of humanity... before we get too powerful and destroy ourselves... or something."
    
    $dshow("ava armscrossed neutral narrow angry")
    
    ava "Captain, please refrain from unnecessary speculation."
    ava "Besides, that idea makes no sense whatsoever. Most likely it's pirates raiding colonies and nothing more."
    kay "Ah Ava... When will you ever learn..."
    kay "Wherever the Sunrider goes... there will never be a dull mission."
    "Ava faced palmed."
    
    $dshow("ava armscrossed talk closed angry")
    
    ava "Unbelievable..."
    kay "Heh..."
    kay "Get us underway, commander."
    
    $dshow("ava handonhip shout neutral angry")
    
    ava "Understood! Helmsman, one tenth impulse! Ease us out of port!"
    "Shields took one last look at Cera on the main screen. This was the home he had liberated with his own hands."
    "No. Not merely by his hands. He had help from men and women across the galaxy in accomplishing his mission."
    "No matter how difficult their next voyage... He swore he would come back and see it again."
    ava "We are to test our systems by launching all our ryders and making one lap around the moon before entering warp."
    kay "Sounds good. Girls?"
    
    scene asagacockpit_orb with dissolve
    
    asa "Black Jack, ready to go!"
    
    scene icaricockpit_orb with dissolve
    
    ica "Heh... Let's get this outta the way."
    
    scene kryska_cockpit_orb1 with dissolve
    
    kry "Sir! It is my privilege to continue to serve as your Alliance liaison officer!"
    
    scene solacockpit_orb with dissolve
    
    sol "Standing by."
    
    scene claudecockpit_orb1 with dissolve
    
    cla "Captain... You can order me to do anything..."
    
    scene bg bridge with dissolve
    
    "Voice" "Liberty is standing by!"
    "A female voice he had never heard before sounded through the comm."
    kay "Eh?"
    kay "Who's that?"
    
    $dshow("ava armscrossed talk neutral neutral")
    
    ava "Captain... Command has transferred a new pilot to our wing now that Chigara is our prisoner. Not only that, but she will serve as the ship's new Chief Engineer going forward."
    
    $dshow("ava armscrossed talk narrow angry")
    
    ava "All of this should have been in the report I left on your desk a week ago..."
    kay "Ah..."
    "Ava stared daggers into Shields' face."
    kay "I uhh... must have missed that."
    kay "Ahem..."

    scene bg hangar with dissolve
    
    "Meanwhile in the hangar..."
    
    scene asagacockpit_orb with dissolve
    
    "The new girl's voice sounded through Asaga's comm."
    "Voice" "It's my greatest honor to serve under the world famous Sunrider Valkyries squadron!"
    "Voice" "While I am still inexperienced... Please take good care of me!"
    asa "Eh? I never knew we had a nickname like that!"
    
    scene icaricockpit_orb with dissolve
    
    ica "Heh. It fits though, doesn't it? All right, rook. First things first..."
    ica "The captain's already taken, so give up your dreams of becoming his sweetheart!"
    "Voice" "E-excuse... me? I-I never...!!"
    ica "Heh."
    
    play sound "sound/chargeup.ogg"
    
    "Precisely at that moment, the linear rail activating, flinging the Liberty out of the hangar."
    "Voice" "H-yguggnnn!!"
    ica "Welcome aboard the team!"

    scene bg bridge with dissolve
    $dshow("ava handonhip talk neutral angry")
    
    ava "Captain, all of our ryders have launched."
    "Shields stood at the front of the bridge, his eyes gazing at the vast sea of stars before him. Who knew what adventures awaited him out there..."
    
    scene allryders_launch with dissolve
    
    "The Sunrider proudly sailed out of Cera, her ryders flying in front of her."
    "While Shields had given it his all to return home, he knew his destiny laid amongst the stars, fighting against impossible odds to save the galaxy from every manner of doom."
    "As long as villains existed in the galaxy, Shields and his girls would fight to stop them."
    "He grinned."
    kay "Set course..."
    kay "For our greatest adventure yet."
    
    if girl == "Asaga":
    
        $persistent.unlocked_endings["ASAGA HAPPY END: OUR GREATEST ADVENTURE YET"] = True
        $chivo_process('Asaga Happy Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolvemedium
        show screen happy_end
        #show expression Text("HAPPY ASAGA END:\nOUR GREATEST ADVENTURE",yalign=0.5,size=90,color="fff")
        pause 3
    if girl == "Sola":
    
        $persistent.unlocked_endings["SOLA HAPPY END: OUR GREATEST ADVENTURE YET"] = True
        $chivo_process('Sola Happy Ending')
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolvemedium
        show screen happy_end
        #show expression Text("HAPPY SOLA END:\nOUR GREATEST ADVENTURE",yalign=0.5,size=90,color="fff")
        pause 3
    if girl == "Ava":
        $persistent.unlocked_endings["AVA HAPPY END: OUR GREATEST ADVENTURE YET"] = True
        $chivo_process('Ava Happy Ending')        
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolvemedium
        show screen happy_end
        #show expression Text("HAPPY AVA END:\nOUR GREATEST ADVENTURE",yalign=0.5,size=90,color="fff")
        pause 3
    if girl == "Icari":    
        $persistent.unlocked_endings["ICARI HAPPY END: OUR GREATEST ADVENTURE YET"] = True
        $chivo_process('Icari Happy Ending')        
        $check_for_all_endings()
        stop music fadeout 1
        scene black with dissolvemedium
        show screen happy_end
        #show expression Text("HAPPY ICARI END:\nOUR GREATEST ADVENTURE",yalign=0.5,size=90,color="fff")
        pause 3
        
    $renpy.full_restart()
    
label dlc_credits:
    
    scene black with dissolvemedium
    
    show bg bridge:
        alpha 0.5 
    show dlccredit 1:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg engineering:
        alpha 0.5
    show dlccredit 2:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg sickbay:
        alpha 0.5
    show dlccredit 3:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg hangar:
        alpha 0.5
    show dlccredit 4:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)

    scene black
    show bg captainscabin:
        alpha 0.5
    show dlccredit 5:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg airlock:
        alpha 0.5
    show dlccredit 6:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg awardhall:
        alpha 0.5
    show dlccredit 7:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg reactor:
        alpha 0.5
    show dlccredit b7:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg hallway:
        alpha 0.5
    show dlccredit 8:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg crewcabin:
        alpha 0.5
    show dlccredit 9:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)

    scene black
    show bg messhall:
        alpha 0.5
    show dlccredit 10:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)

    scene black
    show bg clonelab:
        alpha 0.5
    show dlccredit 11:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg escapepod:
        alpha 0.5
    show dlccredit b11:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show bg brig:
        alpha 0.5
    show dlccredit 12:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    
    scene black
    show allryders_launch:
        alpha 0.5
    show dlccredit 13:
        yalign 0.5 xalign 0.5
    with dissolve
    $renpy.pause(5)
    show dlccredit 14 with dissolve
    $renpy.pause(5)
    
    return
    
    
    