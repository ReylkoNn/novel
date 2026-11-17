default phoneScreenSelected = ''
default phoneMessagesCharacter = ''

screen showPhoneButton:
    zorder 100
    imagebutton:
        xalign 0.92 yalign 1.0
        yoffset 30
        at phoneButtonPeep
        idle 'gui/phoneButton.webp'
        action If(renpy.get_screen('phone'), true=Hide('phone'), false=Show('phone'))
    if(mc.awaitingDate):
        add 'images/gui/timenotif.webp' fit "contain" ysize 40 xalign 0.89
    if(getattr(sarah,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(alice,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(katie,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(grace,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(zoe,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(jessica,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(molly,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92
    if(getattr(eve,'unreadTexts', Null)):
        add 'images/gui/notif.webp' fit "contain" ysize 40 xalign 0.92

screen phone:
    dismiss action Hide('phone')
    zorder 100
    frame:
        modal True
        padding (0, 0)
        xsize 576 ysize 892
        add 'gui/phone.webp' xalign 0.9 yalign 1.0
        background None
        at phoneRaiseTransition
        xalign 0.9 yalign 1.0
        frame:
            padding (0, 0)
            xalign 0.5 yoffset 35
            xsize 555 ysize 850
            background None
            frame:
                padding (0, 0)
                xsize 1.0 ysize 0.93 yalign 0.0
                background None
                if(phoneScreenSelected == 'phoneHome' or phoneScreenSelected == ''):
                    use phoneHome
                if(phoneScreenSelected == 'phoneContacts'):
                    use phoneContacts
                if(phoneScreenSelected == 'phoneMessages'):
                    use phoneMessages
                if(phoneScreenSelected == 'phoneSchedule'):
                    use phoneSchedule
                if(phoneScreenSelected == 'phoneDebug'):
                    use phoneDebug
            frame:
                padding (0, 0)
                xsize 1.0 ysize 0.07 yalign 0.997
                background '#2b2b2b'
                hbox:
                    textbutton _('Home'):
                        text_color '#ffffff'
                        text_size 30
                        text_idle_color '#5c5c5c'
                        text_selected_idle_color '#ffffff'
                        action ToggleVariable('phoneScreenSelected', 'phoneHome', '')
                    text '|'
                    textbutton _('Contacts'):
                        text_color '#ffffff'
                        text_size 30
                        text_idle_color '#5c5c5c'
                        text_selected_idle_color '#ffffff'
                        action ToggleVariable('phoneScreenSelected', 'phoneContacts', '')
                    text '|'
                    textbutton _('Schedule'):
                        text_color '#ffffff'
                        text_size 30
                        text_idle_color '#5c5c5c'
                        text_selected_idle_color '#ffffff'
                        action ToggleVariable('phoneScreenSelected', 'phoneSchedule', '')
                    if(persistent.debugMode or persistent.cheatMode):
                        text '|'
                        textbutton _('Cheats'):
                            text_color '#ffffff'
                            text_size 30
                            text_idle_color '#5c5c5c'
                            text_selected_idle_color '#ffffff'
                            action ToggleVariable('phoneScreenSelected', 'phoneDebug', '')
                if(mc.awaitingDate):
                    add 'images/gui/timenotif.webp' fit "contain" ysize 25 xalign 0.7
                textbutton 'X':
                    style 'genericCircleButtonStyle'
                    text_align (0.5, 0.5)
                    xalign 1.0 yalign 1.0
                    xoffset -10 yoffset -10
                    action [If(phoneScreenSelected == 'phoneMessages',ToggleVariable('phoneScreenSelected', 'phoneContacts', '')), Hide('phone')]
        add 'gui/phoneFrame.webp' xalign 0.9 yalign 1.0

screen phoneHome:
    frame:
        background None
        margin (10,10)
        xfill 1.0
        viewport id "phoneHomeViewport": # Assign an ID for the scrollbar to reference
            draggable True # Allows dragging to scroll
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            vbox:
                xfill 1.0
                text _('Help support the project!'):
                    color '#ffffff'
                    xalign 0.5
                text ''
                grid 3 1:
                    xalign 0.5
                    spacing 20
                    imagebutton idle 'images/menu/patreonIcon.svg':
                        at phoneIconLogo
                        action OpenURL(patreonLink)
                    imagebutton idle 'images/menu/itchIcon.svg':
                        at phoneIconLogo
                        action OpenURL(itchLink)
                    imagebutton idle 'images/menu/discordIcon.svg':
                        at phoneIconLogo
                        action OpenURL(discordLink)
                text ""
                text _('Thank you to my supporters:'):
                    color '#ffffff'
                    xalign 0.5
                text ""
                style_prefix 'splashScreenPatrons'
                text "{b}[patronTopSupporterTitle]:{/b}":
                    color '#71368a'
                    size 41
                for supporter in patronTopSupporters:
                    text supporter:
                        color '#71368a'
                        size 41
                text ""
                text "{b}[patronSuperSupporterTitle]:{/b}":
                    color '#e74c3c'
                    size 38
                for supporter in patronSuperSupporters:
                    text supporter:
                        color '#e74c3c'
                        size 38
                text ""
                text "{b}[patronExtraSupporterTitle]:{/b}":
                    color '#c27c0e'
                    size 35
                for supporter in patronExtraSupporters:
                    text supporter:
                        color '#c27c0e'
                        size 35
                text ""
                text "{b}[patronSupporterTitle]:{/b}":
                    color '#206694'
                    size 30
                for supporter in patronSupporters:
                    text supporter:
                        color '#206694'
                        size 30

transform phoneIconLogo:
    zoom 0.15
    on hover:
        linear 0.2 alpha 0.5
    on idle:
        linear 0.2 alpha 1.0

screen phoneContacts:
    viewport id "phoneContactsViewport": # Assign an ID for the scrollbar to reference
        draggable True # Allows dragging to scroll
        vbox:
            spacing 8
            for character in characters:
                use phoneCharacterStats(character)

screen phoneCharacterStats(character, debugMode = False):
    button:
        # Bug?
        at phoneContactTransform
        if(not character.disabled):
            idle_background Frame("gui/phoneContact.webp")
            hover_background Frame("gui/phoneContact_hover.webp")
        else:
            idle_background Frame("gui/phoneContact_disabled.webp")
            hover_background Frame("gui/phoneContact_disabled.webp")
        ysize 90 xfill 1.0
        if(debugMode):
            action Show('characterInfoDisplay', None, character = character, debugMode = True)
        else:
            action Show('characterInfoDisplay', None, character = character)
        style_prefix 'phoneCharacterStats'
        if(character.knownToMC):
            $ characterIconPath = character.apiName + ' icon'
            imagebutton idle characterIconPath at phoneCharacterIconZoom:
                anchor (0.5, 0.5)
                ypos 0.5
                #yoffset 1
                xpos 0.077
            text character.name anchor (0, 0) xpos 0.16 ypos 0.0
            if(not character.disabled):
                if(debugMode):
                    textbutton _(character.currentLocation.name) anchor (0, 1.0) xpos 0.16 ypos 1.0:
                        action [CaptureFocus('characterDebugLocationSelect'), Show('characterDebugLocationSelect', character = character)]
                else:
                    if(persistent.knowCharacterLocations):
                        if(character.currentLocation.knownToMC):
                            text _(character.currentLocation.name) anchor (0, 1.0) xpos 0.16 ypos 1.0
                        else:
                            text _('Unknown') anchor (0, 1.0) xpos 0.16 ypos 1.0
                hbox:
                    xalign 1.0 yalign 0.0
                    xoffset -80
                    text _('Like: [character.like]')
                    if(debugMode):
                        textbutton '[[-]' xalign 0.6 yalign 0.0:
                            padding (0,0)
                            action IncrementField(character, 'like', -5)
                        textbutton '[[+]' xalign 1.0 yalign 0.0:
                            padding (0,0)
                            action IncrementField(character, 'like', 5)
                    else:
                        if(character.like == character.maxLike):
                            text _(' (Max)')
                hbox:
                    xalign 1.0 yalign 1.0
                    xoffset -80
                    text _('Love: [character.love]')
                    if(debugMode):
                        textbutton '[[-]' xalign 0.6 yalign 1.0:
                            padding (0,0)
                            action IncrementField(character, 'love', -5)
                        textbutton '[[+]' xalign 1.0 yalign 1.0:
                            padding (0,0)
                            action IncrementField(character, 'love', 5)
                    else:
                        if(character.love == character.maxLove):
                            text _(' (Max)')
                if(not debugMode):
                    imagebutton idle 'gui/phoneMessaging.webp' hover 'gui/phoneMessaging_hover.webp':
                        at phoneMessagingIconZoom
                        xalign 1.0
                        action [SetVariable('phoneMessagesCharacter', character), ToggleVariable('phoneScreenSelected', 'phoneMessages', ''), Function(character.setTextsToRead)]
                    if(character.unreadTexts):
                        add 'images/gui/notif.webp' fit "contain" ysize 25 xalign 1.0
            else:
                text _('Disabled') xalign 0.5 yalign 0.5 size 40
        else:
            text '?' size 60 align (0.5, 0.5)
            if(persistent.eventHints):
                hovered [CaptureFocus('phoneContactHover'), Show('phoneContactHint', character=character)]
                unhovered Hide('phoneContactHint')
                action NullAction()

transform phoneContactTransform:
    zoom 1.0

transform phoneMessagingIconZoom:
    zoom 0.15

screen phoneContactHint(character):
    zorder 100
    nearrect:
        focus 'phoneContactHover'
        preferred_side 'left'
        frame:
            background Frame('gui/genericButtonBackground.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            $ lockedEvents = [event for event in character.events if event.unlocked == False]
            $ event = lockedEvents[0]
            vbox:
                text _('Character locked') size 20
                if(event.triggerDay > 1):
                    text _('Day >= [event.triggerDay]') size 20
                text _(event.triggerLocation.name) size 20
                if(len(event.triggerTimes) != 4):
                    text str([_(time) for time in event.triggerTimes]) size 20
                if(len(event.triggerDays) != 7):
                    text str([_(dayName) for dayName in event.triggerDays]) size 20
                if(len(event.requiredEvents) != 0):
                    python:
                        requiredEventNames = ''
                        for requiredEvent in event.requiredEvents:
                            if(requiredEvent.unlocked):
                                requiredEventNames += '{color=#2ec453}'
                            requiredEventNames += _(requiredEvent.name)
                            if(requiredEvent.unlocked):
                                requiredEventNames += '{/color}'
                            requiredEventNames += ', '
                        requiredEventNames = requiredEventNames.rstrip(', ')
                    text _('Requires Events: [requiredEventNames]') size 20
                if(event.extraNotes != ''):
                    text _(event.extraNotes) size 20

screen phoneMessages:
    $ character = phoneMessagesCharacter
    vbox:
        spacing 1
        frame:
            style_prefix 'phoneMessagesHeader'
            background '#7bd383'
            xsize 1.0 ysize 30
            text [character.name]
            hbox:
                xalign 1.0
                text _('Date Invites:')
                text ' '
                if(character.allowDateInvites):
                    textbutton _('On') padding(0, 0) margin (0, 0):
                        action ToggleField(character, 'allowDateInvites')
                else:
                    textbutton _('Off') padding(0, 0) margin (0, 0):
                        action ToggleField(character, 'allowDateInvites')
                text '  '
                text _('Selfies:')
                text ' '
                if(character.allowSelfieSends):
                    textbutton _('On') padding(0, 0) margin (0, 0):
                        action ToggleField(character, 'allowSelfieSends')
                else:
                    textbutton _('Off') padding(0, 0) margin (0, 0):
                        action ToggleField(character, 'allowSelfieSends')

        $ scroll_adjustment = character.textScrollYadjustment
        viewport id "phoneMessagesViewport": # Assign an ID for the scrollbar to reference
            draggable True # Allows dragging to scroll
            yadjustment scroll_adjustment
            vbox:
                spacing 10
                for message in character.textChain:
                    use phoneMessage(message)

style phoneMessagesHeader_text:
    size 20
    color '#f5f5f5'

style phoneMessagesHeader_button_text:
    size 20
    color '#f5f5f5'
    hover_color '#292929'

screen phoneMessage(message):
    if(message.fromCharacter == mc):
        hbox:
            xfill True
            frame:
                xalign 1.0
                xsize 0.7
                background Frame('gui/genericButtonBackgroundHover.webp', 30, 30, 30, 30)
                padding(10, 10)
                text message.message size 25
    else:
        hbox:
            frame:
                yalign 0.0
                background None
                $ phoneIconPath = message.fromCharacter.apiName + 'phoneicon'
                add phoneIconPath fit "contain" ysize 40
            frame:
                xsize 0.7
                background Frame('gui/genericButtonBackground.webp', 30, 30, 30, 30)
                padding(10, 10)
                vbox:
                    hbox:
                        xfill True
                        text message.fromCharacter.name size 14
                        hbox:
                            xalign 1.0
                            text _('Day [str(message.sentDay)] ') size 14
                            text message.sentTime size 14
                    text message.message size 25
                    if(message.image != Null):
                        $ imagePath = 'images/characters/' + message.fromCharacter.apiName +'/selfies/' + message.image + '.webp'
                        imagebutton idle imagePath at phoneCharacterSelfieZoom:
                            action Show('phoneSelfieView', selfiePath = imagePath)
    if(message.dateInvitation != Null):
        hbox:
            spacing 10
            xalign 1.0
            textbutton _('Yes'):
                padding(10,10)
                text_size 25
                background Frame('gui/genericButtonBackgroundHover.webp', 30, 30, 30, 30)
                action [Function(message.fromCharacter.textDateAccepted, message=message)]
            textbutton _('No'):
                padding(10,10)
                text_size 25
                background Frame('gui/genericButtonBackgroundHover.webp', 30, 30, 30, 30)
                action [Function(message.fromCharacter.textDateRejected, message=message)]
    if(getattr(message,'responses', []) != [] and message.respondedTo == False):
        hbox:
            box_wrap True
            spacing 10
            xalign 1.0
            for response in message.responses:
                textbutton response['text']:
                    xmaximum 0.5
                    padding(10,10)
                    text_size 25
                    background Frame('gui/genericButtonBackgroundHover.webp', 30, 30, 30, 30)
                    action [Function(message.respond, response=response)]


transform phoneCharacterSelfieZoom:
    zoom 0.17

transform phoneCharacterSelfieZoom2:
    xcenter 0.5 ycenter 0.5
    zoom 0.85

transform phoneCharacterSelfieZoom3:
    xcenter 0.5 ycenter 0.5
    zoom 0.12

transform phoneCharacterIconZoom:
    zoom 0.33

transform profileCharacterIconZoom:
    zoom 0.42

screen phoneSelfieView(selfiePath):
    modal True
    zorder 100
    imagebutton idle selfiePath at phoneCharacterSelfieZoom2:
        action Hide('phoneSelfieView')

screen characterInfoDisplay(character, debugMode = False):
    dismiss action Hide('characterInfoDisplay')
    zorder 100
    frame:
        modal True
        background None
        xcenter 0.5 ycenter 0.5
        xsize 0.86 ysize 0.95
        vbox:
            # Header
            frame:
                xsize 1.0 ysize 0.12
                background Frame('gui/genericUIBoxRoundedTop.webp', 40, 40, 40, 40)
                textbutton "X":
                    style 'genericCircleButtonStyle'
                    text_align (0.5, 0.5)
                    xalign 1.0 ypos 0.0
                    action Hide('characterInfoDisplay')
                frame:
                    background None
                    xalign 0.0 yalign 1.0
                    xsize 0.9 ysize 1.0
                    hbox:
                        xfill True
                        frame:
                            padding (0, 0)
                            background None
                            $ characterIconPath = character.apiName + ' icon'
                            add characterIconPath at profileCharacterIconZoom
                        frame:
                            yalign 0.5
                            background None
                            text '[character.name]':
                                size 40
                        frame:
                            background None
                            vbox:
                                hbox:
                                    text _('Like: [character.like]') size 25
                                    if(debugMode):
                                        textbutton '[[-]':
                                            text_size 25
                                            padding (0,0)
                                            action IncrementField(character, 'like', -5)
                                        textbutton '[[+]':
                                            text_size 25
                                            padding (0,0)
                                            action IncrementField(character, 'like', 5)
                                    else:
                                        if(character.like == character.maxLike):
                                            text _(' (Max)') size 25
                                hbox:
                                    text _('Love: [character.love]') size 25
                                    if(debugMode):
                                        textbutton '[[-]':
                                            text_size 25
                                            padding (0,0)
                                            action IncrementField(character, 'love', -5)
                                        textbutton '[[+]':
                                            text_size 25
                                            padding (0,0)
                                            action IncrementField(character, 'love', 5)
                                    else:
                                        if(character.love == character.maxLove):
                                            text _(' (Max)') size 25
                        frame:
                            background None
                            vbox:
                                hbox:
                                    text _('Loves:') size 25
                                    for item in character.giftLovesKnownToMC:
                                        add 'images/items/[item.apiName].webp' fit "contain" ysize 30
                                hbox:
                                    text _('Likes:') size 25
                                    for item in character.giftLikesKnownToMC:
                                        add 'images/items/[item.apiName].webp' fit "contain" ysize 30
                                hbox:
                                    text _('Hates:') size 25
                                    for item in character.giftHatesKnownToMC:
                                        add 'images/items/[item.apiName].webp' fit "contain" ysize 30
                        frame:
                            background None
                            vbox:
                                hbox:
                                    text _('Age: [character.age]') size 25
                                hbox:
                                    text _('Species: [character.species]') size 25
                                hbox:
                                    text _('Occupation: [character.job]') size 25
                        if(debugMode):
                            frame:
                                background None
                                vbox:
                                    style_prefix 'characterdebugstats'
                                    hbox:
                                        text _('Known to MC: ')
                                        textbutton str(character.knownToMC) action ToggleField(character, 'knownToMC')
                                    hbox:
                                        text _('Is Dateable: ')
                                        textbutton str(character.isDateable) action ToggleField(character, 'isDateable')
                                    hbox:
                                        text _('Hidden: ')
                                        textbutton str(character.hidden) action [ToggleField(character, 'hidden'), ToggleField(character, 'hiddenDays', 999, 0)]
                                    if(persistent.debugMode):
                                        hbox:
                                            text _('Moved In: ')
                                            textbutton str(character.movedIn) action ToggleField(character, 'movedIn')
                if(not character.disabled):
                    textbutton _('Enabled'):
                        text_align (0.5, 0.5)
                        xalign 1.0 yalign 0.9
                        idle_background Frame('gui/genericButtonBackground.webp', 40, 40, 40, 40)
                        hover_background Frame('gui/genericButtonBackgroundHover.webp', 40, 40, 40, 40)
                        hovered [CaptureFocus('characterDisableHover'), Show('disableCharacterTooltip')]
                        unhovered Hide('disableCharacterTooltip')
                        action [ToggleField(character, 'disabled'), Function(character.debugMoveCharacterToLocation, location_away)]
                else:
                    textbutton _('Disabled'):
                        text_align (0.5, 0.5)
                        xalign 1.0 yalign 0.9
                        idle_background Frame('gui/genericButtonBackgroundDisabled.webp', 40, 40, 40, 40)
                        hover_background Frame('gui/genericButtonBackgroundHover.webp', 40, 40, 40, 40)
                        hovered [CaptureFocus('characterDisableHover'), Show('disableCharacterTooltip')]
                        unhovered Hide('disableCharacterTooltip')
                        action [ToggleField(character, 'disabled')]
            # Details box
            frame:
                xsize 1.0 ysize 1.0
                background Frame('gui/genericUIBoxRoundedBottom.webp', 40, 40, 40, 40)
                viewport id "characterDebugEventsWindow":
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    vbox:
                        xfill True
                        text _('Events') size 28:
                            xalign 0.5 yalign 0.0
                        hbox:
                            spacing 12
                            box_wrap True
                            box_wrap_spacing 5
                            for event in character.events:
                                use characterDebugEventDisplay(character = character, event = event, debugMode = debugMode)
                        if(len(character.specialEvents) > 0 and persistent.groupSex):
                            text _('Group Events') size 28:
                                xalign 0.5 yalign 0.0
                            hbox:
                                spacing 12
                                box_wrap True
                                box_wrap_spacing 5
                                for event in character.specialEvents:
                                    use characterDebugEventDisplay(character = character, event = event, debugMode = debugMode)
                        text _('Selfies') size 28:
                            xalign 0.5 yalign 0.0
                        hbox:
                            spacing 10
                            box_wrap True
                            box_wrap_spacing 10
                            for selfie in character.selfieOptions:
                                use characterSelfiePreview(character = character, selfie = selfie, debugMode = debugMode)
                        text _('Morning Events') size 28:
                            xalign 0.5 yalign 0.0
                        hbox:
                            spacing 10
                            box_wrap True
                            box_wrap_spacing 10
                            for wakeUpOption in character.wakeUpOptions:
                                use characterWakeupPreview(character = character, event = wakeUpOption, debugMode = debugMode)

screen phoneDebug:
    viewport id "phoneDebugViewport": # Assign an ID for the scrollbar to reference
        draggable True # Allows dragging to scroll
        vbox:
            spacing 5
            frame:
                background '#71c2db'
                ysize 60 xfill 1.0
                text mc.name xalign 0.0 yalign 0.0
                textbutton '[[-]' xalign 0.45 yalign 0.0:
                    action IncrementField(mc, 'money', -1000)
                text _('Money: [mc.money]') xalign 0.8 yalign 0.0
                textbutton '[[+]' xalign 1.0 yalign 0.0:
                    action IncrementField(mc, 'money', 1000)
            for character in characters:
                use phoneCharacterStats(character, True)

screen characterDebugLocationSelect(character):
    dismiss action Hide('characterDebugLocationSelect')
    zorder 100
    nearrect:
        focus 'characterDebugLocationSelect'
        preferred_side 'left'
        frame:
            modal True
            vbox:
                for location in locations:
                    textbutton _(location.name):
                        action [Function(character.debugMoveCharacterToLocation, location = location), Hide('characterDebugLocationSelect')]

screen characterDebugEventDisplay(character, event, debugMode = False):
    button:
        if(event.unlocked or debugMode):
            background Frame('eventPreviews/' + event.apiName + '.webp')
        else:
            background Frame(im.Blur('eventPreviews/' + event.apiName + '.webp', 5.0))
        xsize 150 ysize 150
        style_prefix 'eventDisplay'
        text _(event.name)
        if(event.unlocked):
            text _('Complete') size 20 yalign 1.0
        if(persistent.eventHints):
            hovered [CaptureFocus('eventHintHover'), Show('eventHintBox', event=event, character=character, debugMode=debugMode)]
            unhovered Hide('eventHintBox')
        if(event.unlocked or debugMode):
            action [Hide('eventHintBox'), Function(event.load, fromGallery = True)]
        else:
            action NullAction()

screen characterSelfiePreview(character, selfie, debugMode = False):
    $ selfiePath = 'images/characters/' + character.apiName + '/selfies/' + selfie + '.webp'
    if(selfie in character.selfiesSent or debugMode):
        imagebutton idle selfiePath at phoneCharacterSelfieZoom3:
            action Show('phoneSelfieView', selfiePath = selfiePath)
    else:
        imagebutton idle 'images/gui/unknownselfie.webp' at phoneCharacterSelfieZoom3

screen characterWakeupPreview(character, event, debugMode = False):
    button:
        xsize 150 ysize 150
        style_prefix 'eventDisplay'
        if(persistent.eventHints):
            hovered [CaptureFocus('morningEventHintHover'), Show('morningEventHintBox')]
            unhovered Hide('morningEventHintBox')
        if(event in character.wakeUpOptionsSeen or debugMode):
            background Frame('eventPreviews/' + character.apiName + event + '.webp')
            action [Hide('morningEventHintBox'), Call('characterWakeupSex', character = character, event = event, fromGallery = True)]
        else:
            background Frame(im.Blur('eventPreviews/' + character.apiName + event + '.webp', 5.0))
            action NullAction()

style eventDisplay_text:
    color '#78e7aa'
    size 15
    outlines [ (absolute(2), "#2c5730", absolute(0), absolute(0)) ]

screen eventHintBox(event, character, debugMode):
    zorder 100
    nearrect:
        focus 'eventHintHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            vbox:
                text _(event.name) size 20
                if(debugMode):
                    text event.apiName size 20
                if(event.triggerDay > 1):
                    text _('Day: [event.triggerDay]') size 20:
                        if(day >= event.triggerDay):
                            color '#2ec453'
                if(event.requiredLike > 0):
                    text _('Like >= [event.requiredLike]') size 20:
                        if(character.like >= event.requiredLike):
                            color '#2ec453'
                if(event.requiredLove > 0):
                    text _('Love >= [event.requiredLove]') size 20:
                        if(character.love >= event.requiredLove):
                            color '#2ec453'
                if(event.triggerLocation != Null):
                    text _(event.triggerLocation.name) size 20
                if(len(event.triggerTimes) != 4):
                    text str([_(time) for time in event.triggerTimes]) size 20
                if(len(event.triggerDays) != 7):
                    text str([_(dayName) for dayName in event.triggerDays]) size 20
                if(len(event.requiredEvents) != 0):
                    python:
                        requiredEventNames = ''
                        for requiredEvent in event.requiredEvents:
                            if(requiredEvent.unlocked):
                                requiredEventNames += '{color=#2ec453}'
                            requiredEventNames += _(requiredEvent.name)
                            if(requiredEvent.characters != [character] and len(requiredEvent.characters) == 1):
                                requiredEventNames += ' (' + requiredEvent.characters[0].name + ')'
                            if(requiredEvent.unlocked):
                                requiredEventNames += '{/color}'
                            requiredEventNames += ', '
                        requiredEventNames = requiredEventNames.rstrip(', ')
                    text _('Requires Events: [requiredEventNames]') size 20
                if(len(event.requiredItems) != 0):
                    python:
                        requiredItemNames = ''
                        for requiredItem in event.requiredItems:
                            mcHasItem = False
                            if('item_' + requiredItem.apiName in mc.inventory.keys()):
                                mcHasItem = True
                            if(mcHasItem):
                                requiredItemNames += '{color=#2ec453}'
                            requiredItemNames += _(requiredItem.name)
                            if(mcHasItem):
                                requiredItemNames += '{/color}'
                            requiredItemNames += ', '
                        requiredItemNames = requiredItemNames.rstrip(', ')
                    text _('Requires Items: [requiredItemNames]') size 20
                if(event.extraNotes != ''):
                    text _(event.extraNotes) size 20

screen morningEventHintBox():
    zorder 100
    nearrect:
        focus 'morningEventHintHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            padding (10,10)
            vbox:
                text _('Random after spending the night.') size 20

screen phoneSchedule:
    viewport id "phoneScheduleViewport": # Assign an ID for the scrollbar to reference
        draggable True # Allows dragging to scroll
        if(len(mc.scheduledDates) == 0):
            text _('No dates!'):
                xfill True
                xsize 1.0 ysize 1.0
                xalign 0.5 yalign 0.5
                color '#ffffff'
        vbox:
            spacing 20
            for date in mc.scheduledDates:
                use phoneScheduleDate(date)

screen phoneScheduleDate(date):
    frame:
        background '#9f7ab8'
        ysize 100 xfill 1.0
        $ characterIconPath = date.character.apiName + ' icon'
        imagebutton idle characterIconPath at phoneCharacterIconZoom
        text date.character.name anchor (0, 0) xpos 0.2 ypos 0.0
        text _(date.location.name) anchor (0, 1.0) xpos 0.2 ypos 1.0
        text _('Day') + ' [str(date.day)]: ' + _(date.dayOfWeek) xalign 1.0 yalign 0.0
        text _(date.time) xalign 1.0 yalign 1.0
        if(date.event != Null):
            text _('Special!') xalign 0.5 yalign 0.5

screen disableCharacterTooltip:
    zorder 100
    nearrect:
        focus 'characterDisableHover'
        preferred_side 'left'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            padding (10,10)
            vbox:
                text _('Enable / Disable this character from appearing and triggering events') size 20

# Phone animations
transform phoneButtonPeep:
    on hover:
        easein 0.1 yoffset -10
    on idle:
        easeout 0.1 yoffset 0

transform phoneRaiseTransition:
    on show:
        yoffset 1000
        easein 0.4 yoffset 0
    on hide:
        easeout 0.4 yoffset 1000

# Styles
style phoneCharacterStats_text:
    size 33

style phoneCharacterStats_button_text:
    size 33

style characterdebugstats_text:
    size 20

style characterdebugstats_button:
    margin (0,0)
    padding (0,0)

style characterdebugstats_button_text:
    size 20
