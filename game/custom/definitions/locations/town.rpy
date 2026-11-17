label initialiseSuperstore:
    $ location_town.inventory = {'item_car': 1}
    return

label restockSuperstore:
    if (not 'item_car' in mc.inventory.keys()):
        $ location_town.inventory.update({'item_car': 1})

    $ numberOfGirlsMovedIn = len([character for character in characters if character.movedIn == True]) + girlsMovingIn
    if (numberOfGirlsMovedIn > 0 and not 'item_homeupgrade1' in mc.inventory.keys()):
        $ location_town.inventory.update({'item_homeupgrade1': 1})
    if (numberOfGirlsMovedIn > 3 and not 'item_homeupgrade2' in mc.inventory.keys()):
        $ location_town.inventory.update({'item_homeupgrade2': 1})
    return

label buyItem_homeupgrade1:
    $ hasHomeUpgrade1 = True
    $ homeCapacity += 2
    return

label buyItem_homeupgrade2:
    $ hasHomeUpgrade2 = True
    $ homeCapacity += 2
    return

screen town:
    zorder 2
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            button:
                hbox:
                    add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Superstore')
                action If(renpy.get_screen('superstoreBuyWindow'), true=Hide('superstoreBuyWindow'), false=Show('superstoreBuyWindow'))

screen superstoreBuyWindow:
    dismiss action Hide('superstoreBuyWindow')
    zorder 2
    style_prefix 'shopWindowOuter'
    frame:
        at shopRevealTransition
        vbox:
            frame:
                style_prefix 'shopWindowHeader'
                textbutton '{size=30}X':
                    style 'genericCircleButtonStyle'
                    text_align (0.5, 0.5)
                    action Hide('superstoreBuyWindow')
            frame:
                style_prefix 'shopWindowContents'
                viewport id "buyMenuViewport":
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    style_prefix 'shopWindowContentsItems'
                    hbox:
                        for itemName, stock in location_town.inventory.items():
                            $ item = getattr(renpy.store, itemName)
                            button:
                                frame:
                                    style_prefix 'shopWindowContentsItem'
                                    image item.apiName:
                                        if(stock == 0 or mc.money < item.value):
                                            alpha 0.3
                                        else:
                                            alpha 1.0
                                if(stock < 0):
                                    text '{font=DejaVuSans.ttf}\u221e' size 30 at topright yoffset -5
                                else:
                                    text str(stock) at topright
                                text "$[item.value]" at topleft
                                text _(item.name):
                                    at center
                                    if(item.apiName == 'homeupgrade1' or item.apiName == 'homeupgrade2'):
                                        size 17
                                if(stock > 0):
                                    hovered [CaptureFocus('shopItemHover'), Show('shopItemHint', item=item)]
                                    unhovered Hide('shopItemHint')
                                if(stock != 0 and mc.money >= item.value):
                                    background Frame('gui/itemcontainer.webp', 40, 40, 40, 40)
                                    hover_background Frame('gui/itemcontainerHover.webp', 40, 40, 40, 40)
                                    action [Hide('shopItemHint'), Call("mcBuyItem", location=location_town, itemName=itemName)]
                                else:
                                    action NullAction()


screen shopItemHint(item):
    zorder 100
    nearrect:
        focus 'shopItemHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericButtonBackground.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            padding (10,10)
            text item.description size 20

style shopWindowOuter_frame:
    modal True
    background None
    xalign 0.5 yalign 0.5
    xsize 0.45 ysize 0.5

style shopWindowHeader_frame:
    xsize 1.0 ysize 0.1
    background Frame('gui/genericUIBoxRoundedTop.webp', 40, 40, 40, 40)

style shopWindowContents_frame:
    xsize 1.0
    background Frame('gui/genericUIBoxRoundedBottom.webp', 40, 40, 40, 40)

style shopWindowContentsItems_hbox:
    spacing 10
    box_wrap True
    box_wrap_spacing 30

style shopWindowContentsItems_button:
    background "#818181"
    xsize 150 ysize 150

style shopWindowContentsItems_text:
    size 20

style shopWindowContentsItem_frame:
    xsize 100 ysize 100
    xalign 0.5 yalign 0.5
    background None

style shopWindowContentsItem_image:
    xalign 0.5 yalign 0.5
