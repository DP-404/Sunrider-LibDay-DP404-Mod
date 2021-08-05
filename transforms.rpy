init -2:

    transform tr_fadein(ddelay):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1
        on hide:
            pause ddelay
            ease 0.3 alpha 0

    transform tr_menubutton(ddelay,xxpos):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1  xpos xxpos
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos (xxpos+300)
    
    transform tr_menubutton_onshow(ddelay,xxpos):
        alpha 0
        pause ddelay
        ease 0.3 alpha 1  xpos xxpos
        on hide:
            pause ddelay
    
    transform tr_menubutton_onhide(ddelay,xxpos):
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos (xxpos+300)
            
    transform tr_shake:
        xpos 0.5
        ease 0.04 xpos 0.5
        ease 0.04 xpos 0.51
        ease 0.08 xpos 0.49
        repeat 4

    transform tr_battlestations:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.35 zoom 10
        ease 0.75 zoom 1.0
        
    transform tr_yshake:
        ease 0.04 ypos 0.02
        ease 0.08 ypos -0.02
        ease 0.04 ypos 0
        repeat 4
        
    transform tr_xshake:
        ease 0.02 xpos -0.02
        ease 0.04 xpos 0.02
        ease 0.02 xpos 0.0
        repeat 4
        
    transform tr_sidemenu(endpos):
        ypos -80 xpos 1645
        ease 0.3 ypos endpos
        on hide:
            ease 0.3 ypos -80
            
    transform tr_decision(ddelay):
        alpha 0 xpos 860
        pause ddelay
        ease 0.3 alpha 1  xpos 960
        on hide:
            pause ddelay
            ease 0.3 alpha 0 xpos 860
            
    transform tr_inactive(img1):
        im.MatrixColor(img1,im.matrix.brightness(-0.4))
        
    transform tr_hoverglow(img1):
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.2))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.15))
        pause 0.1
        im.MatrixColor(img1,im.matrix.brightness(.10))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(.0))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.15))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.10))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(-0.05))
        pause 0.05
        im.MatrixColor(img1,im.matrix.brightness(0.0))
        pause 0.05
        repeat
    
    transform sprite_default(xx,yy,zz):
        yanchor 1.0 xanchor 0.5
        ypos yy xpos xx zoom zz 
        
    transform tr_center:
        xalign 0.5 yalign 0.5
    transform tr_zoomout:
        xalign 0.5 yalign 0.5
        ease 10 zoom 0.5

    transform tr_dontmissit:
        zoom 10
        ease 0.5 zoom 1

    define dissolvelong = Dissolve(4.0)
    define dissolvemedium = Dissolve(2.0)
    define dissolve = Dissolve(0.5)
