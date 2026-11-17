screen needInteraction:
    text ' ' ypos 100

# UI actions
screen mainUi:
    zorder 100
    use topBar
    use bottomBar

screen topBar:
    frame:
        padding(0, 0)
        xsize 1.0 ysize 0.05
        background None
        at mainUiRevealTransition

        add 'gui/topBar.webp'
        # Game state
        use dayIndicator
        use timeProgresser
        use timeIndicator
        use locationIndicator

        # Personal
        if(not renpy.get_screen('inventoryScreen')):
            use showInventory

        # Navigation buttons
        use viewMapButton
        use homeButton
        use moneyIndicator

        # Extra
        use viewTutorialButton

screen bottomBar:
    frame:
        xsize 1.0 ysize 0.05
        yalign 1.0
        background None
        if(not renpy.get_screen('phone')):
            use showPhoneButton

transform mainUiRevealTransition:
    on show:
        yoffset -200
        easein 0.6 yoffset 0
    on hide:
        easeout 0.6 yoffset -200

# UI top bar indicators
screen timeProgresser:
    imagebutton idle 'gui/timeIndicator.webp' action Call('progressTime'):
        anchor (0.5, 0.5)
        at iconButtonHover
        xpos 960 ypos 47
        at transform:
            rotate dayRotation

screen timeIndicator:
    text _(timeOfDay):
        size 20
        xalign 0.55 ypos 62

screen dayIndicator:
    text _('Day') + ' ' + str(day) + ': ' + _(dayOfWeek):
        size 22
        xpos 5 ypos 5

screen locationIndicator:
    text _(mc.currentLocation.name):
        size 20
        xalign 0.45 ypos 62


# UI top bar buttons
screen homeButton:
    imagebutton idle 'gui/homeIcon2.webp':
        anchor (0.5, 0.5)
        at iconButtonHover
        xpos 825 ypos 27
        if(mc.currentLocation != location_home):
            action Call('goToLocation', target=location_home)

screen viewMapButton:
    imagebutton idle 'gui/mapIcon.webp':
        anchor (0.5, 0.5)
        at iconButtonHover
        xpos 1087 ypos 27
        if(mc.currentLocation != location_map):
            action Call('goToLocation', target=location_map)

screen viewTutorialButton:
    imagebutton idle 'gui/helpicon.webp':
        anchor (0.5, 0.5)
        at iconButtonHover
        xpos 1800 ypos 22
        action Call('startTutorial')

transform iconButtonHover:
    on hover:
        easein 0.1 zoom 0.9
    on idle:
        easeout 0.1 zoom 1

screen showInventory:
    imagebutton idle 'gui/bagIcon.webp':
        anchor (0.5, 0.5)
        at iconButtonHover
        xpos 1220 ypos 27
        action [CaptureFocus('showInventoryButton'),If(renpy.get_screen('inventoryScreen'), true=Hide('inventoryScreen'), false=Show('inventoryScreen'))]

screen moneyIndicator:
    text "$[str(mc.money)]":
        size 30
        xpos 1270 ypos 8

default inventoryXPos = 1200
default inventoryYPos = 0
screen inventoryScreen(gifting = False, character = Null, onDate = False):
    dismiss action Hide('inventoryScreen')
    zorder 3
    python:
        parentCoords = GetFocusRect("showInventoryButton")
        if(parentCoords != None):
            inventoryXPos = int(parentCoords[0])
            inventoryYPos = int(parentCoords[1])
    frame:
        at inventoryRevealTransition
        modal True
        background None
        xpos inventoryXPos ypos inventoryYPos
        xsize 0.28 ysize 0.51
        vbox:
            frame:
                xsize 1.0 ysize 0.1
                background Frame('gui/genericUIBoxRoundedTop.webp', 40, 40, 40, 40)
                textbutton "{size=30}X":
                    style 'genericCircleButtonStyle'
                    text_align (0.5, 0.5)
                    action Hide('inventoryScreen')
                text '$' + str(mc.money) xalign 1.0
            frame:
                xsize 1.0
                background Frame('gui/genericUIBoxRoundedBottom.webp', 40, 40, 40, 40)
                viewport id "inventoryMenuViewport":
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    hbox:
                        spacing 10
                        box_wrap True
                        box_wrap_spacing 10
                        for itemName, stock in mc.inventory.items():
                            $ item = getattr(renpy.store, itemName)
                            button:
                                background Frame('gui/itemcontainer.webp', 40, 40, 40, 40)
                                xsize 150 ysize 150
                                frame:
                                    xsize 100 ysize 100
                                    xalign 0.5 yalign 0.5
                                    background None
                                    image item.apiName xalign 0.5 yalign 0.5
                                text str(stock):
                                    size 15
                                    at topright
                                text _(item.name):
                                    size 15
                                    at center
                                if(gifting and item.giftable):
                                    hover_background Frame('gui/itemcontainerHover.webp', 40, 40, 40, 40)
                                    action [Hide('inventoryScreen'), Function(character.receiveGift, itemName=itemName, onDate=onDate)]
transform inventoryRevealTransition:
    on show:
        yoffset -1000
        easein 0.4 yoffset 50
    on hide:
        easeout 0.4 yoffset -1000

screen statChangeIndicator(stat, value, statNum, maxHit):
    zorder 3
    timer 2.0 action Hide('statChangeIndicator')
    if(value != 0):
        frame:
            background None
            at statChangeIndicatorTransform
            xsize 200
            xalign 0.0 yalign 0.1+(statNum/20)
            hbox:
                if(stat == 'Like'):
                    add 'gui/smile.webp' fit "contain" ysize 45
                elif(stat == 'Love'):
                    add 'gui/heart.webp' fit "contain" ysize 45
                style_prefix 'statTextOutlines'
                if(maxHit):
                    text " MAX"
                else:
                    if(value > 0):
                        text ' +'
                    else:
                        text ' '
                    text "[str(value)]"

style statTextOutlines_text:
    color '#ffffff'
    outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]

transform statChangeIndicatorTransform:
    on show:
        xoffset -300
        easeout 0.4 xoffset 0
    on hide:
        easeout 0.4 xoffset -300

screen characterInteractionScreen(character):
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    python:
        roomActions = []
        for index, action in enumerate(character.availableActions):
            if(character.currentLocation.apiName in action):
                roomActions = action.get(character.currentLocation.apiName)
        availableCommands = character.availableCommandsPublic.copy()
        isSubroomOfHome = (mc.currentLocation.apiName).startswith('home')
        if(isSubroomOfHome):
            availableCommands += character.availableCommandsPrivate.copy()
    frame:
        at characterInteractionMenuReveal
        vbox:
            if('Chat' in character.availableActions):
                button:
                    hbox:
                        add 'conversationicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Chat')
                    if('Chat' not in character.actionsPerformedInTimePeriod):
                        action Function(character.chat)
            if(not isSubroomOfHome): # Phase out over time?
                if('Spend time' in character.availableActions):
                    button:
                        hbox:
                            add 'clockicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                            text _('Spend time')
                        if('Spend time' not in character.actionsPerformedToday):
                            action Function(character.spendTime)
            if('Gift' in character.availableActions):
                button:
                    hbox:
                        add 'gifticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Gift')
                    if('Gift' not in character.actionsPerformedToday):
                        action Show('inventoryScreen', gifting=True, character=character)
            if('Affection' in character.availableActions):
                button:
                    hbox:
                        add 'hearticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Affection')
                    action [CaptureFocus('affectionButton'), Show('characterInteractionAffectionMenu', character=character), Hide('characterInteractionScreen')]
            if(character.movedIn and isSubroomOfHome):
                button:
                    hbox:
                        add 'hearticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Sex')
                    action Call('characterHomeStartSex', character=character)
            for roomAction in roomActions:
                button:
                    hbox:
                        add 'hearticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _(roomAction)
                    action [Call('characterActionInRoom', character=character, location=character.currentLocation, action=roomAction)]
            if('Date' in character.availableActions):
                button:
                    hbox:
                        add 'calendaricon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Date')
                    if( len(character.scheduledDates) == 0):
                        action [Hide('characterInteractionScreen'), Hide('characterInteractionAffectionMenu'), Function(character.receiveDateInvitation)]
            if(not isSubroomOfHome and 'Invite over' in character.availableActions):
                button:
                    hbox:
                        add 'homeicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Invite over')
                    if('Invite over' not in character.actionsPerformedToday):
                        action Function(character.inviteOver)
            if(len(character.availableSpecialEvents) > 0):
                button:
                    hbox:
                        add 'hearticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('{b}Special{/b}')
                    action [Show('characterInteractionSpecialMenu', character=character), Hide('characterInteractionScreen')]
            if(len(availableCommands) > 0):
                button:
                    hbox:
                        add 'conversationicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Commands')
                    action [CaptureFocus('commandsButton'), Show('characterInteractionCommandsMenu', character=character), Hide('characterInteractionScreen')]
            button:
                hbox:
                    add 'returnicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Back')
                action [Hide('characterInteractionScreen'), Hide('characterInteractionAffectionMenu'), Call('endCharacterInteraction', character = character)]

screen characterInteractionScreenBathroom(character):
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    python:
        bathroomActions = []
        for index, action in enumerate(character.availableActions):
            if('homebathroom' in action):
                bathroomActions = action.get('homebathroom')
    frame:
        at characterInteractionMenuReveal
        vbox:
            for bathroomAction in bathroomActions:
                button:
                    hbox:
                        add 'hearticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _(bathroomAction)
                    action [Call('characterActionInRoom', character=character, location=location_home_bathroom, action=bathroomAction)]
            button:
                hbox:
                    add 'returnicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Back')
                action [Hide('characterInteractionScreen'), Hide('characterInteractionAffectionMenu'), Call('endCharacterInteraction', character = character)]

transform characterInteractionMenuReveal:
    on show:
        xoffset 800
        easein 0.4 xoffset 0
    on hide:
        xoffset 0
        easeout 0.4 xoffset 800

screen characterInteractionAffectionMenu(character):
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        $ parentCoords = GetFocusRect("affectionButton")
        #xpos int(parentCoords[0]) ypos int(parentCoords[1])
        #anchor (0.0, 0.0)
        python:
            availableAffections = character.availableAffections
            isSubroomOfHome = (mc.currentLocation.apiName).startswith('home')
            if('Snuggle' in availableAffections and not isSubroomOfHome):
                availableAffections.remove('Snuggle')
        vbox:
            for affectionInteraction in availableAffections:
                button:
                    hbox:
                        add '[affectionInteraction!l]icon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _(affectionInteraction)
                    if(affectionInteraction not in character.affectionsPerformedInTimePeriod):
                        action [Hide('characterInteractionAffectionMenu'), Function(character.receiveAffection, action = affectionInteraction)]
            button:
                hbox:
                    add 'returnicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Back')
                action [Hide('characterInteractionAffectionMenu'), Show('characterInteractionScreen', character=character)]

screen characterInteractionSpecialMenu(character):
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            for specialEvent in character.availableSpecialEvents:
                button:
                    hbox:
                        add 'hearticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        if(specialEvent.cost > 0):
                            text _(specialEvent.name) + ' ($' + str(specialEvent.cost) + ')'
                        else:
                            text _(specialEvent.name)
                    if(mc.money >= specialEvent.cost):
                        action [Hide('characterInteractionSpecialMenu'), Function(character.inviteToSpecialEvent, event = specialEvent)]
            button:
                hbox:
                    add 'returnicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Back')
                action [Hide('characterInteractionSpecialMenu'), Show('characterInteractionScreen', character=character)]

screen characterInteractionCommandsMenu(character):
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        $ parentCoords = GetFocusRect("affectionButton")
        #xpos int(parentCoords[0]) ypos int(parentCoords[1])
        #anchor (0.0, 0.0)
        python:
            availableCommands = character.availableCommandsPublic.copy()
            isSubroomOfHome = (mc.currentLocation.apiName).startswith('home')
            if(isSubroomOfHome):
                availableCommands += character.availableCommandsPrivate.copy()
        vbox:
            for command in availableCommands:
                $ commandTrimmed = command.replace(" ", "")
                button:
                    hbox:
                        add '[commandTrimmed!l]icon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _(command)
                    action [Hide('characterInteractionCommandsMenu'), Call('characterCommand' + commandTrimmed, character=character)]
            button:
                hbox:
                    add 'returnicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Back')
                action [Hide('characterInteractionCommandsMenu'), Show('characterInteractionScreen', character=character)]

screen map:
    zorder 2
    if (store._version == config.version):
        for location in locations:
            if(location.mapXPos != Null and location.knownToMC):
                use locationMarker(location)

screen locationMarker(location):
    vbox:
        xpos location.mapXPos ypos location.mapYPos
        box_align True
        frame:
            anchor (0.5, 0.0)
            padding (0, 0)
            background None
            style_prefix 'genericButtonStyle'
            button:
                xalign 0.5
                hbox:
                    add '[location.apiName]icon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _(location.name)
                if(timeOfDay in location.openTimes):
                    action Call('goToLocation', target=location)
        if(persistent.knowCharacterLocations):
            frame:
                anchor (0.5, 0.0)
                padding (0, 0)
                background None
                hbox:
                    $ knownCharacterFilteredList = [character for character in location.occupants if character.knownToMC]
                    if(hasattr(location, 'subLocations') and location.subLocations != []):
                        for subLocation in location.subLocations:
                            $ knownCharacterFilteredList.extend([character for character in subLocation.occupants if character.knownToMC])
                    for character in knownCharacterFilteredList:
                        use locationOccupantIcon(character)

screen locationOccupantIcon(character):
    frame:
        padding(0,0)
        background None
        hbox:
            $ characterIconPath = character.apiName + ' icon'
            imagebutton idle characterIconPath at mapCharacterIconZoom
            if (character.awaitingDate):
                frame:
                    padding(0,0)
                    xoffset -7
                    background '#68f373'
                    add 'calendaricon' fit "contain" xsize 15
            $ launchableEvent = character.sceneEvaluator()
            if (launchableEvent != Null and (hasattr(launchableEvent.triggerLocation, 'subLocations') and character.currentLocation == launchableEvent.triggerLocation or (launchableEvent.triggerLocation.subLocations != [] and character.currentLocation == launchableEvent.triggerLocation.subLocations[0]))):
                add 'notif' fit "contain" xsize 15 xoffset -7

transform mapCharacterIconZoom:
    zoom 0.2

screen cafe:
    zorder 2

screen park:
    zorder 2

screen beach:
    zorder 2

screen diner:
    zorder 2

screen aquarium:
    zorder 2

screen theater:
    zorder 2

default dateActionsMax = 5
default dateActionsCount = 0
default dateActions = []
default dateScore = 0
screen dateUi(character):
    zorder 2
    frame:
        xalign 0.5 yalign 0.0
        xsize 800 ysize 100
        background Frame('gui/genericUIBoxRoundedBottom.webp', 40, 40, 40, 40)
        at mainUiRevealTransition
        hbox:
            frame:
                xsize 0.5 ysize 1.0
                background None
                hbox:
                    box_reverse True
                    xalign 0.5 yalign 0.5
                    for dateAction in dateActions:
                        if(dateAction == ''):
                            add 'gui/dateActionAvailable.webp' fit "contain" ysize 60
                        else:
                            add 'gui/dateActionUsed.webp' fit "contain" ysize 60
            frame:
                xsize 1.0 ysize 1.0
                background None
                bar:
                    ysize 60
                    left_bar Frame('gui/genericButtonBackgroundHover.webp', 40, 40, 40, 40)
                    right_bar Frame('gui/genericButtonBackground.webp', 40, 40, 40, 40)
                    left_gutter 10
                    yalign 0.5
                    value dateScore
                    range 100
                #text str(dateScore) yalign 0.5 xpos 10
                add 'gui/smile.webp' fit "contain" ysize 30 yalign 0.5 xpos 0.35
                add 'gui/heart.webp' fit "contain" ysize 30 yalign 0.5 xpos 0.75

screen dateInteractionScreen(character, location = mc.currentLocation):
    zorder 2
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            button:
                hbox:
                    add 'conversationicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Chat')
                if(dateActionsCount < dateActionsMax):
                    action Show('characterChatTopicMenu', character=character), Hide('dateInteractionScreen')
            button:
                hbox:
                    add 'holdinghandsicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Hang Out')
                if(dateActionsCount < dateActionsMax):
                    action Function(character.spendTime, onDate = True)
            if(location.apiName == 'bar'):
                button:
                    hbox:
                        add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Pay for drinks ($30)')
                    if(dateActionsCount < dateActionsMax and mc.money >= 30 and 'PayFor' not in dateActions):
                        action Function(character.datePayFor, amount = 30)
            if(location.apiName == 'cafe'):
                button:
                    hbox:
                        add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Pay for coffee ($15)')
                    if(dateActionsCount < dateActionsMax and mc.money >= 15 and 'PayFor' not in dateActions):
                        action Function(character.datePayFor, amount = 15)
            if(location.apiName == 'diner'):
                $ meal = _('Breakfast') if timeOfDay == 'Morning' else _('Lunch') if timeOfDay == 'Afternoon' else _('Dinner')
                button:
                    hbox:
                        add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Pay for [meal] ($40)')
                    if(dateActionsCount < dateActionsMax and mc.money >= 40 and 'PayFor' not in dateActions):
                        action Function(character.datePayFor, amount = 40)
            if(location.apiName == 'beach'):
                button:
                    hbox:
                        add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Pay for ice cream ($10)')
                    if(dateActionsCount < dateActionsMax and mc.money >= 10 and 'PayFor' not in dateActions):
                        action Function(character.datePayFor, amount = 10)
            if(location.apiName == 'aquarium'):
                button:
                    hbox:
                        add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Pay for tickets ($30)')
                    if(dateActionsCount < dateActionsMax and mc.money >= 30 and 'PayFor' not in dateActions):
                        action Function(character.datePayFor, amount = 30)
            button:
                hbox:
                    add 'gifticon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Gift')
                if(dateActionsCount < dateActionsMax and 'Gift' not in dateActions):
                    action Show('inventoryScreen', gifting = True, character = character, onDate = True)
            for affectionInteraction in character.availableAffections:
                button:
                    hbox:
                        add '[affectionInteraction!l]icon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _(affectionInteraction)
                    if(dateActionsCount < dateActionsMax):
                        action Function(character.receiveAffection, action = affectionInteraction, onDate = True)
            button:
                hbox:
                    add 'clockicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('End Date')
                action Function(character.endDate)

screen characterChatTopicMenu(character):
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    python:
        numberOfTopicActions = len([action for action in dateActions if action == 'Topic'])
    frame:
        at characterInteractionMenuReveal
        vbox:
            button:
                hbox:
                    add 'conversationicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Chat')
                if(dateActionsCount < dateActionsMax):
                    action [Hide('characterChatTopicMenu'), Function(character.chat, onDate = True)]
            for dateChat in character.dateChats:
                    button:
                        if(dateChat in character.dateChatsDone):
                            background Frame('gui/genericButtonBackgroundDisabled.webp', 40, 40, 40, 40)
                            hover_background Frame('gui/genericButtonBackgroundHover.webp', 40, 40, 40, 40)
                        hbox:
                            add 'conversationicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                            if(dateChat not in character.dateChatsDone):
                                text _(dateChat)
                            else:
                                text _(dateChat) + ' (' + _('Done') + ')'
                        if(numberOfTopicActions <= 1):
                            action [Hide('characterChatTopicMenu'), Function(character.chat, onDate = True, topic = dateChat)]
            textbutton _('Back'):
                action [Hide('characterChatTopicMenu'), Show('dateInteractionScreen', character=character)]

# Screen actions
label hideAllScreens:
    hide screen sarahClickable
    hide screen aliceClickable
    hide screen katieClickable
    hide screen graceClickable
    hide screen zoeClickable
    hide screen jessicaClickable
    hide screen mollyClickable
    hide screen eveClickable

    hide screen home
    hide screen homebedroom
    hide screen homelounge
    hide screen homekitchen
    hide screen homebathroom
    hide screen map
    hide screen town
    hide screen cafe
    hide screen park
    hide screen shop
    hide screen beach
    hide screen diner
    hide screen aquarium
    hide screen bar
    hide screen barOverview

    hide screen shopBuyWindow
    hide screen superstoreBuyWindow
    hide screen inventoryScreen
    hide screen phone
    hide screen characterInfoDisplay
    hide screen characterDebugDisplay
    hide screen eventHintBox

    hide screen characterInteractionScreen
    hide screen characterInteractionAffectionMenu
    hide screen characterInteractionSpecialMenu

    hide screen dateUi
    return

# Styles
style characterInteractionMenuStyle_frame:
    padding(0,0)
    xalign 1.0 yalign 0.5
    background None

style characterInteractionMenuStyle_vbox:
    spacing 5

style characterInteractionMenuStyle_button:
    background Frame('gui/genericButtonBackgroundRight.webp', 40, 40, 40, 40)
    hover_background Frame('gui/genericButtonBackgroundRightHover.webp', 40, 40, 40, 40)
    insensitive_background Frame('gui/genericButtonBackgroundRightDisabled.webp', 40, 40, 40, 40)
    xminimum 400
    size_group 'characterInteractionMenuStyle_button'

style characterInteractionMenuStyle_button_text:
    xoffset 30

style characterInteractionMenuStyle_text:
    color '#707070'
    hover_color '#336600'

style characterInteractionMenuStyle_hbox:
    spacing 25

style locationOptionButtonContainer_frame:
    anchor (0.0, 0.0)
    padding(5, 5)
    background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
    xpos 192 ypos 200

style locationOptionButtonContainer_vbox:
    spacing 10

style genericButtonStyle_button:
    xpadding 10
    idle_background Frame('gui/genericButtonBackground.webp', 40, 40, 40, 40)
    hover_background Frame('gui/genericButtonBackgroundHover.webp', 40, 40, 40, 40)
    insensitive_background Frame('gui/genericButtonBackgroundDisabled.webp', 40, 40, 40, 40)

style genericButtonStyle_text:
    color '#707070'
    hover_color '#336600'

style genericButtonStyle_hbox:
    spacing 15

style genericCircleButtonStyle:
    xsize 40 ysize 40
    idle_background Frame('gui/genericButtonBackgroundCircle.webp')
    hover_background Frame('gui/genericButtonBackgroundCircleHover.webp')

style customChoices:
    color '#ffffff'
    background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
