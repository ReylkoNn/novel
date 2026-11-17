label initialiseShop:
    call restockShop from _call_restockShop
    return

label restockShop:
    $ location_shop.inventory = {'item_chocolateBar': 2, 'item_book': 2, 'item_flowers': 2, 'item_videogame': 2, 'item_candles': 2, 'item_wine': 2, 'item_dress': 2, 'item_perfume': 2, 'item_goldRing': 1}
    return

screen shop:
    zorder 2
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            button:
                hbox:
                    add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Buy')
                action If(renpy.get_screen('shopBuyWindow'), true=Hide('shopBuyWindow'), false=Show('shopBuyWindow'))

screen shopBuyWindow:
    dismiss action Hide('shopBuyWindow')
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
                    action Hide('shopBuyWindow')
                text _('Shop restocks weekly!') size 20 xalign 0.5
            frame:
                style_prefix 'shopWindowContents'
                viewport id "buyMenuViewport":
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    style_prefix 'shopWindowContentsItems'
                    hbox:
                        for itemName, stock in location_shop.inventory.items():
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
                                text _(item.name) at center
                                if(stock != 0 and mc.money >= item.value):
                                    background Frame('gui/itemcontainer.webp', 40, 40, 40, 40)
                                    hover_background Frame('gui/itemcontainerHover.webp', 40, 40, 40, 40)
                                    action Call("mcBuyItem", location=location_shop, itemName=itemName)

transform shopRevealTransition:
    on show:
        xoffset -2000
        easein 0.4 xoffset 0
    on hide:
        easeout 0.4 xoffset -2000
