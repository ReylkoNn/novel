init python:
    # If an object doesn't have an attribute add it set to value.
    #
    # obj       - the object
    # attrName  - the attribute name to check
    # value     - the value if the attribute is not known
    # return    - Boolean: if the attribute needed to be added
    def condAddAttr(obj, attrName, value):
        attributeNeedsAdding = not hasattr(obj, attrName)
        if attributeNeedsAdding:
            setattr(obj, attrName, value)
        return attributeNeedsAdding

label updater:
    $ renpy.block_rollback()
    "Сохранение создано в другой версии ([store._version]). Попытка обновления до [config.version]..."
    $ renpy.block_rollback()
    "Если появится сообщение «Произошла ошибка», обычно помогает нажать «Игнорировать»."
    python:
        persistent.cheatsEnabled = False
        persistent.likeLoveMultiplier = 1
        persistent.debugMode = False
        persistent.cheatMode = False
    if grace not in characters:
        call initialiseCharacter_grace from _call_initialiseCharacter_grace_1
        python:
            characters.extend([grace])
    
    if zoe not in characters:
        call initialiseCharacter_zoe from _call_initialiseCharacter_zoe_1
        python:
            characters.extend([zoe])

    if jessica not in characters:
        call initialiseCharacter_jessica from _call_initialiseCharacter_jessica_1
        python:
            characters.extend([jessica])

    if molly not in characters:
        call initialiseCharacter_molly from _call_initialiseCharacter_molly_1
        python:
            characters.extend([molly])

    if eve not in characters:
        call initialiseCharacter_eve from _call_initialiseCharacter_eve_1
        python:
            characters.extend([eve])
            
    call updateCharacterStatics from _call_updateCharacterStatics
    call updateLocationStatics from _call_updateLocationStatics_1
    python:
        allCharacters = characters.copy()
        allCharacters.append(mc)
        datesToUpdate = []
        for character in allCharacters:
            condAddAttr(character, 'maxLike', 999)
            condAddAttr(character, 'maxLove', 999)
            if(len(character.events) > 0):
                lastStoryEvent = character.events[-1]
                character.maxLike = lastStoryEvent.requiredLike
                character.maxLove = lastStoryEvent.requiredLove
            if(character.like > character.maxLike): character.like = character.maxLike
            if(character.love > character.maxLove): character.love = character.maxLove
            condAddAttr(character, 'giftLovesKnownToMC', [])
            condAddAttr(character, 'giftLikesKnownToMC', [])
            condAddAttr(character, 'giftHatesKnownToMC', [])
            condAddAttr(character, 'textChain', [])
            condAddAttr(character, 'unreadTexts', False)
            condAddAttr(character, 'hidden', False)
            condAddAttr(character, 'hiddenDays', 0)
            condAddAttr(character, 'textScrollYadjustment', ui.adjustment())
            condAddAttr(character, 'selfieOptions', [])
            condAddAttr(character, 'selfiesSent', [])
            condAddAttr(character, 'allowDateInvites', True)
            condAddAttr(character, 'allowSelfieSends', True)
            condAddAttr(character, 'wakeUpOptions', [])
            condAddAttr(character, 'wakeUpOptionsSeen', [])
            condAddAttr(character, 'blockedLocations', [])
            condAddAttr(character, 'dateChats', [])
            condAddAttr(character, 'dateChatsDone', [])
            condAddAttr(character, 'polyamoryExplained', False)
            condAddAttr(character, 'knowsDating', [])
            condAddAttr(character, 'specialEvents', [])
            condAddAttr(character, 'availableSpecialEvents', [])
            condAddAttr(character, 'disabled', False)
            condAddAttr(character, 'movedIn', False)
            condAddAttr(character, 'preferredMovedInMondaySchedule', [])
            condAddAttr(character, 'preferredMovedInTuesdaySchedule', [])
            condAddAttr(character, 'preferredMovedInWednesdaySchedule', [])
            condAddAttr(character, 'preferredMovedInThursdaySchedule', [])
            condAddAttr(character, 'preferredMovedInFridaySchedule', [])
            condAddAttr(character, 'preferredMovedInSaturdaySchedule', [])
            condAddAttr(character, 'preferredMovedInSundaySchedule', [])
            condAddAttr(character, 'pantiesOptions', 0)
            condAddAttr(character, 'pantiesWornIndex', 1)
            condAddAttr(character, 'availableCommandsPublic', [])
            condAddAttr(character, 'availableCommandsPrivate', [])

            condAddAttr(character, 'events', [])
            eventsList = character.events.copy()
            eventsList.extend(character.specialEvents.copy())
            for event in eventsList:
                condAddAttr(event, 'extraNotes', '')
                condAddAttr(event, 'triggerDay', 0)
                condAddAttr(event, 'scheduled', False)
                event.scheduled = False
                condAddAttr(event, 'cost', 0)
                condAddAttr(event, 'requiredItems', [])
                condAddAttr(event, 'requiresInvite', False)
                condAddAttr(event, 'mcInitiated', False)
            for text in reversed(character.textChain):
                if(text.dateInvitation != Null): # Update any pending date invitations
                    datesToUpdate.append(text.dateInvitation)
                if(text.image != Null and (".webp" in text.image or ".png" in text.image)): # Remove selfie texts that still use path
                    character.textChain.remove(text)

        datesToUpdate.extend(mc.scheduledDates)
        for date in datesToUpdate:
            condAddAttr(date, 'forced', False)
            condAddAttr(date, 'event', Null)
        
        for location in locations:
            condAddAttr(location, 'hasTimeOfDay', False)
            condAddAttr(location, 'subLocations', [])
            condAddAttr(location, 'occupantLimit', -1)
        
        # Version specific updates
        # -> v1.2 / v1.4
        sarahVacation.requiresInvite = True
        aliceVacation.requiresInvite = True
        katieVacation.requiresInvite = True
        graceVacation.requiresInvite = True
        zoeVacation.requiresInvite = True
        jessicaVacation.requiresInvite = True
        mollyVacation.requiresInvite = True

        # -> v1.5 item refactor. Convert all dictionaries of items to dictionaries of defined item_[name] strings
        for item, stock in mc.inventory.copy().items():
            if(hasattr(item, 'apiName')):
                if(hasattr(renpy.store, 'item_' + item.apiName)):
                    newItem = getattr(renpy.store, 'item_' + item.apiName)
                    mc.inventory.update({'item_' + item.apiName: stock})
                mc.inventory.pop(item)
        for item, stock in location_town.inventory.copy().items():
            if(hasattr(item, 'apiName')):
                if(hasattr(renpy.store, 'item_' + item.apiName)):
                    newItem = getattr(renpy.store, 'item_' + item.apiName)
                    location_town.inventory.update({'item_' + item.apiName: stock})
                location_town.inventory.pop(item)
        for item, stock in location_shop.inventory.copy().items():
            if(hasattr(item, 'apiName')):
                if(hasattr(renpy.store, 'item_' + item.apiName)):
                    newItem = getattr(renpy.store, 'item_' + item.apiName)
                    location_shop.inventory.update({'item_' + item.apiName: stock})
                location_shop.inventory.pop(item)
    call restockShop from _call_restockShop_1
    call restockSuperstore from _call_restockSuperstore
    "...Обновление завершено!"
    return

label debugCharacterUnlocker:
    python:
        for character in characters:
            for event in character.events:
                event.unlocked = True
            for event in character.specialEvents:
                event.unlocked = True
            character.availableEvents = []
            character.like = character.maxLike
            character.love = character.maxLove
            character.knownToMC = True
            character.isDateable = True
        zoe.job = 'Bartender'
        mc.polyamoryExplained = True
        mc.inventory = {'item_car': 1}
        mc.money = 10000

        sarah.polyamoryExplained = True
        alice.polyamoryExplained = True
        sarah.knowsDating = [alice]
        alice.knowsDating = [sarah]

        zoe.polyamoryExplained = True
        jessica.polyamoryExplained = True
        zoe.knowsDating = [jessica]
        jessica.knowsDating = [zoe]

        grace.polyamoryExplained = True
        jessica.polyamoryExplained = True
        grace.knowsDating = list(set(grace.knowsDating + [jessica]))
        jessica.knowsDating = list(set(jessica.knowsDating + [grace]))

        katie.polyamoryExplained = True
        molly.polyamoryExplained = True
        katie.knowsDating = list(set(katie.knowsDating + [molly]))
        molly.knowsDating = list(set(molly.knowsDating + [katie]))

        grace.polyamoryExplained = True
        molly.polyamoryExplained = True
        grace.knowsDating = list(set(grace.knowsDating + [molly]))
        molly.knowsDating = list(set(molly.knowsDating + [grace]))

        katie.polyamoryExplained = True
        zoe.polyamoryExplained = True
        katie.knowsDating = list(set(katie.knowsDating + [zoe]))
        zoe.knowsDating = list(set(zoe.knowsDating + [katie]))

        katie.movedIn = True
        molly.movedIn = True
        grace.movedIn = True
        alice.movedIn = True
        jessica.movedIn = True
        sarah.movedIn = True
        zoe.movedIn = True
    $ i = 0
    while i < len(characters):
        $ character = characters[i]
        call evaluateAvailableInteractions(character) from _call_evaluateAvailableInteractions_2
        $ i += 1
    return
    
label addAllToLocation:
    python:
        for character in characters:
            character.debugMoveCharacterToLocation(location_home_lounge)

label setAllMaxStats:
    python:
        for character in characters:
            character.like = character.maxLike
            character.love = character.maxLove
