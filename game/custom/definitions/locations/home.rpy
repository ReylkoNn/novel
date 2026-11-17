default homeCapacity = 3
default girlsMovingIn = 0
default hasHomeUpgrade1 = False
default hasHomeUpgrade2 = False

# Location screens
screen home:
    zorder 2

screen homebedroom:
    zorder 2
    for character in location_home_bedroom.occupants:
        $ imagepath = location_home_bedroom.apiName + character.apiName
        if(character.apiName == 'molly' and dayOfWeek in ['Saturday', 'Sunday']):
            $ imagepath = imagepath + 'casual'
        imagebutton:
            idle imagepath
            focus_mask True
            action Call('startCharacterInteraction', character = character)
            at characterInSceneSpriteHover

    # secret button shh
    button:
        background None
        anchor (0.5, 0.5)
        xsize 0.02 ysize 0.04
        xpos 1430 ypos 300
        action [ToggleVariable('persistent.cheatsEnabled'), SetVariable('persistent.cheatMode', True), SetVariable('persistent.likeLoveMultiplier', 1)]

    # Bedroom actions
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        yoffset 250
        vbox:
            button:
                hbox:
                    add 'clockicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Wait')
                action Call('progressTime')
            button:
                hbox:
                    add 'baricon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Manage Bar')
                action Show('barOverview')
            button:
                hbox:
                    add 'conversationicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Change Name')
                action Call('nameInput')
            if(not persistent.cheatsEnabled):
                button:
                    hbox:
                        add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                        text _('Cheats')
                    action Call('cheatInput')
            button:
                hovered [CaptureFocus('saveFileFixerHover'), Show('saveFileFixerTooltip')]
                unhovered Hide('saveFileFixerTooltip')
                hbox:
                    add 'saveicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Save File Fixer')
                action Call('saveFileFixer')
            button:
                hbox:
                    add 'bedicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Sleep')
                action Call('goToSleep')
    use sublocationPicker(location_home)

label goToSleep:
    $ movedInGirls = [character for character in  characters if (character.movedIn)]
    if(len(movedInGirls) > 0):
        call hideAllScreens from _call_hideAllScreens_4
        hide screen mainUi
        $ renpy.say("",_("Who do you want to sleep with tonight?"), interact=False)
        call screen goToSleepWithGirlSelector(movedInGirls)
    jump startNewDay

screen goToSleepWithGirlSelector(movedInGirls):
    zorder 5
    modal True
    style_prefix "choice"
    vbox:
        at choicesMenuReveal
        for character in movedInGirls:
            textbutton character.name action [Function(character.addLove, value = 1), Call('characterSleepover', character = character)]
        textbutton _('Alone') action Return()

screen saveFileFixerTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'saveFileFixerHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _("Use if you have any issues with your game.\n(Events not available, exceptions when progressing, updating, etc)\nThis may unschedule a scheduled date or event, so only use when neccessary.")

screen homelounge:
    zorder 2
    for character in location_home_lounge.occupants:
        $ imagepath = location_home_lounge.apiName + character.apiName
        if(character.apiName == 'molly' and dayOfWeek in ['Saturday', 'Sunday']):
            $ imagepath = imagepath + 'casual'
        imagebutton:
            idle imagepath
            focus_mask True
            action Call('startCharacterInteraction', character = character)
            at characterInSceneSpriteHover
    use sublocationPicker(location_home)

screen homekitchen:
    zorder 2
    for character in location_home_kitchen.occupants:
        $ imagepath = location_home_kitchen.apiName + character.apiName
        if(character.apiName == 'molly' and dayOfWeek in ['Saturday', 'Sunday']):
            $ imagepath = imagepath + 'casual'
        imagebutton:
            idle imagepath
            focus_mask True
            action Call('startCharacterInteraction', character = character)
            at characterInSceneSpriteHover
    use sublocationPicker(location_home)

screen homebathroom:
    zorder 2
    for character in location_home_bathroom.occupants:
        $ imagepath = location_home_bathroom.apiName + character.apiName
        imagebutton:
            idle imagepath
            focus_mask True
            action Call('startCharacterInteraction', character = character)
            at characterInSceneSpriteHover
    use sublocationPicker(location_home)

screen sublocationPicker(location):
    zorder 3
    style_prefix None
    frame:
        background None
        align (0.0, 1.0)
        margin (30, 30)
        hbox:
            spacing 15
            for subLocation in location.subLocations:
                use sublocationIndicator(subLocation)

screen sublocationIndicator(location):
    frame:
        background None
        yalign 1.0
        xsize 220
        vbox:
            hbox:
                box_wrap True
                $ knownCharacterFilteredList = [character for character in location.occupants if character.knownToMC]
                for character in knownCharacterFilteredList:
                    use locationOccupantIcon(character)
            frame:
                padding (3,3)
                background '#ffffff'
                imagebutton idle location.imagePath + timeOfDay.lower() at sublocationIndicatorZoom:
                    if(not location.apiName == mc.currentLocation.apiName):
                        action Call('goToLocation', target=location)

transform sublocationIndicatorZoom:
        zoom 0.1

label nameInput:
    call hideAllScreens from _call_hideAllScreens_5
    python:
        mcNameInput = renpy.input(prompt=_('Input name:'), default = mc.name, length=20)
        mcNameInput = mcNameInput.strip()
        mc.name = mcNameInput
        mc.c.name = mcNameInput
    call goToLocation(target=location_home) from _call_goToLocation_5

label saveFileFixer:
    hide screen saveFileFixerTooltip
    call hideAllScreens from _call_hideAllScreens_6
    ofkeres "Эта кнопка попробует исправить повреждённые настройки или события в сохранении."
    ofkeres "Запланированные свидания и события могут отмениться — тогда их придётся запустить заново."
    menu:
        "Are you sure you want to continue?"
        "Yes":
            call updater from _call_updater
        "No":
            pass
    call goToLocation(target=location_home) from _call_goToLocation_6

label cheatInput:
    call hideAllScreens from _call_hideAllScreens_7
    "Чтобы открыть режим читов и полную галерею."
    python:
        cheatCodeInput = renpy.input(prompt=_('Code:'))
        cheatCodeInput = cheatCodeInput.strip()
    if(cheatCodeInput == 'indirectambition'):
        "Код принят! Режим читов включён. Он доступен в телефоне и переключается в настройках."
        $ persistent.cheatsEnabled = True
        $ persistent.cheatMode = True
    else:
        "Неверный код. Код доступен подписчикам определённых уровней Patreon. {a=[patreonLink]}>>>Patreon<<<{/a}"
    call goToLocation(target=location_home) from _call_goToLocation_7
