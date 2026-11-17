# Declare characters used by this game.
init offset = 2
init python:
    config.tag_zorder['sarah'] = 2
    config.tag_zorder['alice'] = 2
    config.tag_zorder['katie'] = 2
    config.tag_zorder['grace'] = 2
    config.tag_zorder['zoe'] = 2
    config.tag_zorder['jessica'] = 2
    config.tag_zorder['molly'] = 2
    config.tag_zorder['eve'] = 2

# Character definitions
define debug = Character(name = 'Debug', who_color='#b11919', what_color='#b11919')
define narrator = Character(what_italic=True)
define ofkeres = Character(name = 'ofkeres', who_color = '#045024', what_italic=True)
define unknown = Character(name = '?', who_color = '#36dacc')
define unknown2 = Character(name = '?', who_color = '#94232d')
define unknown3 = Character(name = '?', who_color = '#c9dd18')
define staff = Character(name = 'Staff', who_color = '#bba422')
define terry = Character(name = 'Terry', who_color = '#666666')

define sarah_unknown = Character(name = '?', who_color = '#523617')
define alice_unknown = Character(name = '?', who_color = '#9f9ca5')
define katie_unknown = Character(name = '?', who_color = '#d3b016')
define grace_unknown = Character(name = '?', who_color = '#ee4e56')
define zoe_unknown = Character(name = '?', who_color = '#562186')
define jessica_unknown = Character(name = '?', who_color = '#999016')
define molly_unknown = Character(name = '?', who_color = '#3d1922')
define eve_unknown = Character(name = '?', who_color = '#9eb439')

# Person class definition
init python:
    class Person:
        def __init__(self, character, name, lastName, apiName, sex, age):
            self.c = character
            # Personal attributes
            self.name = name
            self.lastName = lastName
            self.apiName = apiName
            self.sex = sex
            self.age = age
            self.species = ''
            self.birthday = 30
            self.job = 'Unemployed'
            self.giftLoves = []
            self.giftLikes = []
            self.giftHates = []
            self.giftLovesKnownToMC = []
            self.giftLikesKnownToMC = []
            self.giftHatesKnownToMC = []
            self.married = False
            self.wage = 0

            # Skill attributes
            self.strength = 0
            self.intelligence = 0
            self.charisma = 0

            # Sexual attributes
            self.virgin = True
            self.virginityLossDate = '?'
            self.pregnancyChance = 0.00
            self.pregnant = False
            self.daysPregnant = 0
            self.timesGivenBirth = 0

            # Personal effects
            self.money = 0
            self.inventory = {}

            # Relationship to MC statistics
            self.knownToMC = False
            self.like = 0
            self.love = 0
            self.maxLove = 0
            self.maxLike = 0
            self.relationshipWithMC = 'Stranger'
            self.sexCountWithMC = 0
            self.textChain = []
            self.unreadTexts = False
            self.allowDateInvites = True
            self.textScrollYadjustment = ui.adjustment()
            self.polyamoryExplained = False
            self.knowsDating = []
            self.movedIn = False

            # Available action attributes
            #['Chat', 'Spend time', 'Gift', 'Affection', 'Date', 'Invite over', ...]
            self.availableActions = ['Chat', 'Gift']
            #['Pat', 'Hug', 'Kiss', ...]
            self.availableAffections = []
            self.actionsPerformedInTimePeriod = []
            self.affectionsPerformedInTimePeriod = []
            self.actionsPerformedToday = []
            self.pantiesOptions = 0
            self.pantiesWornIndex = 0
            self.availableCommandsPublic = []
            self.availableCommandsPrivate = []

            # Event attributes
            self.isDateable = False
            self.scheduledDates = []
            self.awaitingDate = False
            self.events = []
            self.availableEvents = []
            self.specialEvents = []
            self.availableSpecialEvents = []
            self.selfieOptions = []
            self.selfiesSent = []
            self.allowSelfieSends = True
            self.wakeUpOptions = []
            self.wakeUpOptionsSeen = []
            self.dateChats = []
            self.dateChatsDone = []

            # World attributes
            self.currentLocation = ''
            self.blockedLocations = []
            self.hidden = False # Character away for some period. Will only appear in away or trigger location.
            self.hiddenDays = 0
            self.disabled = False # Characters to avoid them showing up or events triggering, if player doesnt care for them

            # Morning, Afternoon, Evening, Night. % Chance of going there, otherwise random
            self.preferredMondaySchedule = []
            self.preferredTuesdaySchedule = []
            self.preferredWednesdaySchedule = []
            self.preferredThursdaySchedule = []
            self.preferredFridaySchedule = []
            self.preferredSaturdaySchedule = []
            self.preferredSundaySchedule = []

            self.preferredMovedInMondaySchedule = []
            self.preferredMovedInTuesdaySchedule = []
            self.preferredMovedInWednesdaySchedule = []
            self.preferredMovedInThursdaySchedule = []
            self.preferredMovedInFridaySchedule = []
            self.preferredMovedInSaturdaySchedule = []
            self.preferredMovedInSundaySchedule = []

        def startDay(self):
            self.actionsPerformedToday = []
            self.availableEvents = []
            self.availableSpecialEvents = []
            if(not self.disabled):
                self.evaluateAvailableEvents()
            self.startNewTimePeriod()
            if(self.hiddenDays > 0):
                self.hiddenDays -= 1
            if(self.hiddenDays == 0):
                self.hidden = False
            self.cleanUpTextChain()
            self.setDayPanties()
            return

        def startNewTimePeriod(self):
            character.actionsPerformedInTimePeriod = []
            character.affectionsPerformedInTimePeriod = []
            self.checkForExpiredTextMessages()
            return

        def checkForExpiredTextMessages(self):
            for message in [message for message in self.textChain if message.dateInvitation != Null]:
                date = message.dateInvitation
                if(date.day < day or (date.day == day and timesOfDay.index(date.time) <= timesOfDay.index(timeOfDay))):
                    message.dateInvitation = Null
            return

        # Prevent endless text chain arrays by having a limit
        def cleanUpTextChain(self):
            if(len(self.textChain) > 30):
                del self.textChain[:5]
            return

        # Move events to availableEvents if requiredEvent criteria is met
        def evaluateAvailableEvents(self):
            fullEventsList = self.events
            if(persistent.groupSex):
                fullEventsList = fullEventsList + self.specialEvents
            for event in [event for event in fullEventsList if (not event.unlocked and not event.scheduled)]:
                requiredEventsThatAreCompleted = [requiredEvent for requiredEvent in event.requiredEvents if requiredEvent.unlocked]
                charactersAreAvailable = [girl for girl in event.characters if not girl.disabled]
                if day >= event.triggerDay and event not in self.availableEvents and len(event.requiredEvents) == len(requiredEventsThatAreCompleted) and len(event.characters) == len(charactersAreAvailable):
                    if not event.requiresInvite:
                        self.availableEvents.extend([event])
                    elif ( # If the event is one that requires character interaction
                        day >= event.triggerDay
                        and self.love >= event.requiredLove
                        and self.like >= event.requiredLike
                        and event not in self.availableSpecialEvents
                        and len(event.requiredEvents) == len(requiredEventsThatAreCompleted)
                        # https://stackoverflow.com/questions/11093421/create-list-of-object-attributes-in-python
                        and set([("item_" + item.apiName) for item in event.requiredItems]).issubset(set([itemName for itemName in mc.inventory.keys()]))
                    ):
                        self.availableSpecialEvents.extend([event])
            return

        # Set the index of their wearing panties
        def setDayPanties(self):
            if(self.pantiesOptions > 0):
                self.pantiesWornIndex = renpy.random.randint(1, self.pantiesOptions)

        def moveCharacter(self):
            newTargetLocation = Null
            if(self.hidden):
                newTargetLocation = location_away
            self.awaitingDate = False
            # Check for if a date is scheduled
            for date in self.scheduledDates:
                # Remove date from schedule if date is now in past (missed)
                if(date.day < day or (date.day == day and timesOfDay.index(date.time) < timesOfDay.index(timeOfDay))):
                    self.scheduledDates.remove(date)
                    if(date in mc.scheduledDates):
                        mc.scheduledDates.remove(date)
                    self.addLike(-5)
                    self.addLove(-5)
                    mc.awaitingDate = False
                # Does character have a date right now
                elif(date.day == day and date.time == timeOfDay and not date.forced):
                    newTargetLocation = date.location
                    self.awaitingDate = True
                    mc.awaitingDate = True
                    renpy.notify("У тебя назначено свидание! Не пропусти!")
                break

            # Check if any available event can be triggered now
            if(newTargetLocation == Null):
                for event in self.availableEvents:
                    if(event.triggerDay <= day and character.like >= event.requiredLike and character.love >= event.requiredLove and event.triggerLocation != Null and timeOfDay in event.triggerLocation.openTimes and timeOfDay in event.triggerTimes and dayOfWeek in event.triggerDays):
                        if(not character.knownToMC):
                            # Force to location
                            newTargetLocation = event.triggerLocation
                        else:
                            # 50% chance to go to event trigger location instead
                            randInt = renpy.random.randint(1, 10)
                            if(randInt > 5):
                                newTargetLocation = event.triggerLocation
                                break

            # If target location was not pre-determined (by date etc), use schedule and random chance
            if(newTargetLocation == Null):
                daySchedule = []
                if(self.movedIn):
                    daySchedule = getattr(self, 'preferredMovedIn' + dayOfWeek + 'Schedule')
                else:
                    daySchedule = getattr(self, 'preferred' + dayOfWeek + 'Schedule')
                newTargetLocation = daySchedule[timesOfDay.index(timeOfDay)]
                pickRandom = False
                if(newTargetLocation in self.blockedLocations or not self.locationHasSpace(newTargetLocation)):
                    pickRandom = True

                # 20% chance to pick random location instead
                randInt = renpy.random.randint(1, 10)
                if(randInt > 8):
                    pickRandom = True
                if(pickRandom):
                    # Pick random open location
                    openLocations = [location for location in locations if (timeOfDay in location.openTimes and location.accessibleToNPCs and location not in self.blockedLocations and self.locationHasSpace(location))] # Inline list filter
                    newTargetLocation = openLocations[renpy.random.randint(0, len(openLocations)-1)]

            # Go to the selected location
            if(self.currentLocation != newTargetLocation):
                if(self.movedIn and newTargetLocation == location_home): # If target location is just "home", pick a random room
                    availableRooms = [homeRoom for homeRoom in location_home.subLocations if self.locationHasSpace(homeRoom)]
                    newTargetLocation = availableRooms[renpy.random.randint(0, len(availableRooms)-1)]
                elif(newTargetLocation.subLocations != []): # If undefined location with subrooms
                    newTargetLocation = newTargetLocation.subLocations[0]
                self.currentLocation.occupants.remove(self)
                self.currentLocation = newTargetLocation
                newTargetLocation.occupants.append(self)

        def locationHasSpace(self, location):
            return location.occupantLimit == -1 or len(location.occupants) < location.occupantLimit

        def debugMoveCharacterToLocation(self, location):
            if(self.currentLocation != location):
                self.currentLocation.occupants.remove(self)
                self.currentLocation = location
                location.occupants.append(self)

        def chat(self, onDate = False, topic = Null):
            self.actionsPerformedInTimePeriod = list(set(self.actionsPerformedInTimePeriod + ['Chat']))
            if(onDate):
                if(topic != Null):
                    store.dateActions[int(dateActionsCount)] = 'Topic'
                    store.dateScore += 20
                else:
                    store.dateActions[int(dateActionsCount)] = 'Chat'
                    store.dateScore += 10
                store.dateActionsCount += 1
            else:
                self.addLike(1)

            if(topic != Null):
                self.dateChatsDone.append(topic)
            renpy.call('characterChat', character = self, onDate = onDate, topic = topic)

        def addLike(self, value):
            if(value > 0):
                value = value * persistent.likeLoveMultiplier
            maxHit = False
            self.like += value
            if(self.like > self.maxLike):
                maxHit = True
                self.like = self.maxLike
            renpy.show_screen('statChangeIndicator', stat = 'Like', value = value, statNum = 0, maxHit = maxHit, _tag = self.apiName+'Like')

        def addLove(self, value):
            if(value > 0):
                value = value * persistent.likeLoveMultiplier
            maxHit = False
            self.love += value
            if(self.love > self.maxLove):
                maxHit = True
                self.love = self.maxLove
            renpy.show_screen('statChangeIndicator', stat='Love', value=value, statNum = 1, maxHit = maxHit, _tag=self.apiName+'Love')

        def spendTime(self, onDate = False):
            if(onDate):
                store.dateActions[int(dateActionsCount)] = 'Spend Time'
                store.dateActionsCount += 1
                store.dateScore += 10
            else:
                self.actionsPerformedToday = list(set(self.actionsPerformedToday + ['Spend time']))
                self.addLike(1)
            renpy.call('characterSpendTime', character = character, onDate = onDate)

        def sceneEvaluator(self):
            eventToLaunch = Null
            for event in self.availableEvents:
                inTriggerLocation = (self.currentLocation == event.triggerLocation) or (event.triggerLocation.subLocations != [] and self.currentLocation == event.triggerLocation.subLocations[0])
                if(day >= event.triggerDay and inTriggerLocation and self.like >= event.requiredLike and self.love >= event.requiredLove):
                    if(renpy.has_label(event.apiName)):
                        eventToLaunch = event
                    else:
                        renpy.say('debug', 'Event ' + event.apiName + ' doesn\'t exist!')
            return eventToLaunch

        def receiveGift(self, itemName, onDate = False):
            self.actionsPerformedToday = list(set(self.actionsPerformedToday + ['Gift']))
            if(onDate):
                store.dateActions[int(dateActionsCount)] = 'Gift'
                store.dateActionsCount += 1

            mc.inventory[itemName] -= 1
            if(mc.inventory[itemName] == 0):
                mc.inventory.pop(itemName)
            if(self.inventory.get(itemName) != None):
                self.inventory[itemName] += 1
            else:
                self.inventory.update({itemName: 1})

            item = getattr(renpy.store, itemName)
            likeChange = 1 # addLike(1)
            loveChange = 0
            if(any(giftLove.apiName == item.apiName for giftLove in self.giftLoves)):
                loveChange = 1 # addLove(1)
                store.dateScore += 30
                if(not(any(giftLovesKnown.apiName == item.apiName for giftLovesKnown in self.giftLovesKnownToMC))):
                    self.giftLovesKnownToMC.append(item)
            elif(any(giftLike.apiName == item.apiName for giftLike in self.giftLikes)):
                likeChange = 2 # addLike(2)
                store.dateScore += 20
                if(not(any(giftLikesKnown.apiName == item.apiName for giftLikesKnown in self.giftLikesKnownToMC))):
                    self.giftLikesKnownToMC.append(item)
            elif(any(giftHate.apiName == item.apiName for giftHate in self.giftHates)):
                loveChange = -1 # addLove(-1)
                likeChange = -3 # addLike(-3)
                store.dateScore -= 10
                if(not(any(giftHatesKnown.apiName == item.apiName for giftHatesKnown in self.giftHatesKnownToMC))):
                    self.giftHatesKnownToMC.append(item)
            else:
                store.dateScore += 10
            renpy.call('characterReceiveGift', character = character, item = item, likeChange = likeChange, loveChange = loveChange, onDate = onDate)

        def receiveAffection(self, action, onDate = False):
            self.affectionsPerformedInTimePeriod = list(set(self.affectionsPerformedInTimePeriod + [action]))
            if(onDate):
                store.dateScore += 15
                store.dateActions[int(dateActionsCount)] = action
                store.dateActionsCount += 1
            if(action == 'Kiss' or action == 'Snuggle'):
                self.addLove(1)
                store.dateScore += 25
            else:
                self.addLike(1)
            renpy.call('characterReceiveAffection', character = self, action = action, onDate = onDate)

        def initiateAffection(self):
            initiateableAffections = self.availableAffections.copy()
            if('Chin Scratch' in initiateableAffections):
                initiateableAffections.remove('Chin Scratch')
            if('Caress Butt' in initiateableAffections):
                initiateableAffections.remove('Caress Butt')
            if('Boob Grab' in initiateableAffections):
                initiateableAffections.remove('Boob Grab')
            if('Snuggle' in initiateableAffections and not (mc.currentLocation.apiName).startswith('home')):
                initiateableAffections.remove('Snuggle')
            randInt = renpy.random.randint(1, 20)
            #renpy.say('debug', 'initiateAffection ' + str(randInt))
            # 15% chance to initiate an affection
            if(self.currentLocation != location_home_bathroom and randInt > 17 and len(initiateableAffections) > 0):
                randInt2 = renpy.random.randint(0, len(initiateableAffections)-1)
                action = initiateableAffections[randInt2]
                self.affectionsPerformedInTimePeriod = list(set(self.affectionsPerformedInTimePeriod + [action]))
                if(action == 'Kiss' or action == 'Snuggle'):
                    self.addLove(1)
                else:
                    self.addLike(1)
                renpy.call('characterInitiateAffection', character = self, action = action)

        def receiveDateInvitation(self):
            renpy.call('characterReceiveDateInvitation', character = self)

        def startDate(self):
            mc.awaitingDate = False
            self.addLike(1)
            self.addLove(1)
            date = self.scheduledDates[0]
            self.scheduledDates.remove(date)
            mc.scheduledDates.remove(date)
            store.dateActions = []
            store.dateActionsCount = 0
            store.dateScore = 0
            for i in range(dateActionsMax):
                store.dateActions.append('')
            renpy.call('characterStartDate', character = self)

        def datePayFor(self, amount):
            dateActions[int(dateActionsCount)] = 'PayFor'
            store.dateActionsCount += 1
            store.dateScore += 25
            mc.money -= amount
            renpy.call('characterDatePayFor', character = self)

        def endDate(self):
            if(dateScore >= 80):
                self.addLike(2)
                self.addLove(2)
            elif(dateScore >= 60):
                self.addLike(1)
                self.addLove(1)
            elif(dateScore < 40):
                self.addLike(-2)
                self.addLove(-2)
            else:
                self.addLike(1)
            renpy.call('characterEndDate', character = self)

        def inviteOver(self):
            renpy.call('characterInviteOver', character = self)

        def setTextsToRead(self):
            self.unreadTexts = False
            for message in self.textChain:
                message.read = True

        def textDateAccepted(self, message):
            mc.scheduledDates.append(message.dateInvitation)
            self.scheduledDates.append(message.dateInvitation)
            message.dateInvitation = Null
            self.textChain.append(Message(message.fromCharacter, mc, 'Хорошо! Тогда увидимся!', Null, day, timeOfDay))

        def textDateRejected(self, message):
            message.dateInvitation = Null
            self.textChain.append(Message(message.fromCharacter, mc, 'Прости, у меня тогда не получится. В другой раз!', Null, day, timeOfDay))

        def inviteToSpecialEvent(self, event):
            renpy.call('inviteToSpecialEvent', character = self, event = event)

        def startSpecialEvent(self, event):
            renpy.call('startSpecialEvent', character = self, event = event)



# Character methods
label initialiseCharacters:
    call initialiseCharacter_mc from _call_initialiseCharacter_mc
    call initialiseCharacter_sarah from _call_initialiseCharacter_sarah
    call initialiseCharacter_alice from _call_initialiseCharacter_alice
    call initialiseCharacter_katie from _call_initialiseCharacter_katie
    call initialiseCharacter_grace from _call_initialiseCharacter_grace
    call initialiseCharacter_zoe from _call_initialiseCharacter_zoe
    call initialiseCharacter_jessica from _call_initialiseCharacter_jessica
    call initialiseCharacter_molly from _call_initialiseCharacter_molly
    call initialiseCharacter_eve from _call_initialiseCharacter_eve
    $ characters.extend([sarah, alice, katie, grace, zoe, jessica, molly, eve])
    return

label updateCharacterStatics:
    call updateCharacterStatics_mc from _call_updateCharacterStatics_mc
    call updateCharacterStatics_sarah from _call_updateCharacterStatics_sarah
    call updateCharacterStatics_alice from _call_updateCharacterStatics_alice
    call updateCharacterStatics_katie from _call_updateCharacterStatics_katie
    call updateCharacterStatics_grace from _call_updateCharacterStatics_grace
    call updateCharacterStatics_zoe from _call_updateCharacterStatics_zoe
    call updateCharacterStatics_jessica from _call_updateCharacterStatics_jessica
    call updateCharacterStatics_molly from _call_updateCharacterStatics_molly
    call updateCharacterStatics_eve from _call_updateCharacterStatics_eve
    return

label moveCharacterLocations:
    call hideInSceneCharacters(True) from _call_hideInSceneCharacters
    python:
        for character in [character for character in characters if not character.disabled]:
            character.moveCharacter()
    return

label resetCharactersWhenTimeProgresses:
    python:
        for character in characters:
            character.startNewTimePeriod()
    call chanceToSendText from _call_chanceToSendText
    return

label chanceToSendText:
    $ i = 0
    while i < len(characters):
        $ character = characters[i]
        $ randInt = renpy.random.randint(1, 100)
        # 3% chance to send a date invite
        if(not character.disabled and character.allowDateInvites and randInt < 4 and renpy.has_label(character.apiName + 'SendDateText') and character.isDateable and character.scheduledDates == [] and not character.hidden):
            $ proposedDate = Null
            python:
                proposedDayOfWeek = ''
                if(daysOfWeek.index(dayOfWeek) == len(daysOfWeek) - 1):
                    proposedDayOfWeek = daysOfWeek[0]
                else:
                    proposedDayOfWeek = daysOfWeek[daysOfWeek.index(dayOfWeek) + 1]

                randDayIndex = renpy.random.randint(0, len(timesOfDay)-1)
                proposedDateTime = timesOfDay[randDayIndex]

                availableLocations = [location for location in locations if (location.knownToMC and location.isDateSpot and proposedDayOfWeek not in location.closedDaysOfWeek and proposedDateTime in location.openTimes and location.accessibleToNPCs)]
                randLocationIndex = renpy.random.randint(0, len(availableLocations)-1)
                proposedLocation = availableLocations[randLocationIndex]

                proposedDate = Date(character, proposedLocation, (day + 1), proposedDayOfWeek, proposedDateTime)

                character.unreadTexts = True
                character.textScrollYadjustment.value = character.textScrollYadjustment.range + 1000
                renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
            if(proposedDate != Null):
                call expression characters[i].apiName + 'SendDateText' pass (proposedDate = proposedDate) from _call_expression_1

        # 4% chance to send a selfie
        #debug "[character.name] [randInt]"
        if(not character.disabled and character.allowSelfieSends and randInt > 96 and renpy.has_label(character.apiName + 'SendSelfie') and not character.hidden):
            call expression characters[i].apiName + 'GetSelfieOptions' from _call_expression_2
            if(_return != []):
                python:
                    selfieOptions = _return
                    previouslySentOptions = character.selfiesSent.copy()
                    unsentOptions = [selfie for selfie in selfieOptions if selfie not in previouslySentOptions]
                    selfieRand = 0
                    selfieName = ''
                    if(len(unsentOptions) == 0): # If every option has already been sent, send randomly
                        selfieRand = renpy.random.randint(0, len(selfieOptions)-1)
                        selfieName = selfieOptions[selfieRand]
                    else: # Otherwise, wend a random one from the unsent options
                        selfieRand = renpy.random.randint(0, len(unsentOptions)-1)
                        selfieName = unsentOptions[selfieRand]
                call expression characters[i].apiName + 'SendSelfie' pass (selfieName = selfieName) from _call_expression_3
                python:
                    if(selfieName not in character.selfiesSent):
                        character.selfiesSent.append(selfieName)
                    character.unreadTexts = True
                    character.textScrollYadjustment.value = character.textScrollYadjustment.range + 1000
                    renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
        $ i += 1
    return

# Show character screen/imageButtons at location
label showInSceneCharacters:
    $ occupantsToShow = [character for character in mc.currentLocation.occupants if character.knownToMC and not mc.currentLocation.apiName.startswith('home')]
    if(len(occupantsToShow) > 0):
        pause(0.1)
        $ i = 0
        while i < len(occupantsToShow):
            show screen expression occupantsToShow[i].apiName + 'Clickable' pass (xcenter = 1.0 / (len(occupantsToShow) + 1) * (i + 1))
            $ i+=1
        with Dissolve(0.4)
    return

# Hide character screen/imageButtons at location
label hideInSceneCharacters(withFade = False):
    if(len(mc.currentLocation.occupants) > 0):
        $ i = 0
        while i < len(mc.currentLocation.occupants):
            hide screen expression mc.currentLocation.occupants[i].apiName + 'Clickable'
            $ i+=1
        if(withFade):
            with Dissolve(0.4)
    return

label startCharacterInteraction(character):
    call hideAllScreens from _call_hideAllScreens
    call hideInSceneCharacters(True) from _call_hideInSceneCharacters_1
    if(character.awaitingDate):
        $ character.startDate()
    python: # If character is waiting for an event where mcInitiated = True
        eventToLaunch = character.sceneEvaluator()
        if(eventToLaunch != Null):
            if(len(mc.scheduledDates) > 0):
                for date in mc.scheduledDates.copy():
                    if(date.day == day):
                        mc.scheduledDates.remove(date)
                        date.character.scheduledDates = []
                        mc.awaitingDate = False
                        renpy.notify('Ты отменил свидание. Ничего страшного, она всё поняла!')
            eventToLaunch.load()
    $ character.initiateAffection()
    if(character.currentLocation == location_home_bathroom):
        call startCharacterInteractionBathroom(character) from _call_startCharacterInteractionBathroom
    else:
        if(character.currentLocation.apiName.startswith('home')):
            # 12.5% chance to ask for sex
            $ randInt = renpy.random.randint(1, 8)
            if(randInt == 1):
                call expression character.apiName + 'InitiateHomeSex' from _call_expression_4
                menu:
                    "Yes":
                        call characterStartSex(character) from _call_characterStartSex
                    "No":
                        call expression character.apiName + 'InitiateHomeSexDeny' from _call_expression_5
        $ renpy.show(character.apiName + ' neutral', tag=character.apiName)
        with Dissolve(0.4)
    call screen characterInteractionScreen(character)

label startCharacterInteractionBathroom(character):
    $ renpy.show(character.apiName + ' smile nude', tag=character.apiName)
    with Dissolve(0.4)
    call expression character.apiName + 'InteractionBathroom' from _call_expression_6
    call screen characterInteractionScreenBathroom(character)

label characterChat(character, onDate, topic = False):
    if(topic != Null):
        $ topic = topic.lower()
        if(renpy.has_label(character.apiName + 'Chat_' + topic)):
            call expression character.apiName + 'Chat_' + topic from _call_expression_7
        else:
            call wipDateInteraction(character = character, interactionType = character.apiName + ' Chat_' + topic) from _call_wipDateInteraction
        jump expression character.apiName + 'DateInteraction'
    elif(onDate):
        if(renpy.has_label(character.apiName + 'ChatDate_' + mc.currentLocation.apiName)):
            call expression character.apiName + 'ChatDate_' + mc.currentLocation.apiName from _call_expression_8
        elif(renpy.has_label(character.apiName + 'ChatDate')):
            call expression character.apiName + 'ChatDate' from _call_expression_9
        else:
            call wipDateInteraction(character = character, interactionType = character.apiName + ' Chat') from _call_wipDateInteraction_1
        jump expression character.apiName + 'DateInteraction'
    else:
        if(renpy.has_label(character.apiName + 'Chat_' + mc.currentLocation.apiName)):
            call expression character.apiName + 'Chat_' + mc.currentLocation.apiName from _call_expression_10
        elif(renpy.has_label(character.apiName + 'Chat')):
            call expression character.apiName + 'Chat' from _call_expression_11
        else:
            call wipCharacterInteraction(character = character, interactionType = character.apiName + ' Chat') from _call_wipCharacterInteraction
        "Мы хорошо поболтали."
        call startCharacterInteraction(character) from _call_startCharacterInteraction

label characterSpendTime(character, onDate):
    if(renpy.has_label(character.apiName + 'SpendTime')):
        hide screen mainUi
        call expression character.apiName + 'SpendTime' pass (onDate = onDate) from _call_expression_12
        "Хорошо провели время."
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' Spend time') from _call_wipCharacterInteraction_1
    if(onDate):
        $ mc.currentLocation.showBackground()
        jump expression character.apiName + 'DateInteraction'
    call endScene(character = character) from _call_endScene_1

label characterReceiveAffection(character, action, onDate):
    $ action = action.replace(" ", "")
    if(renpy.has_label(character.apiName + 'Receive' + action)):
        call expression character.apiName + 'Receive' + action from _call_expression_13
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' Receive' + action) from _call_wipCharacterInteraction_2
    if(onDate):
        jump expression character.apiName + 'DateInteraction'

    $ i = 0
    while i < len(mc.currentLocation.occupants):
        $ adjacentCharacter = mc.currentLocation.occupants[i]
        if(action != 'Snuggle' and adjacentCharacter in character.knowsDating):
            # 50% chance of adjacent character wanting in on the action
            $ randInt = renpy.random.randint(0, 1)
            if(randInt == 1 and character in adjacentCharacter.knowsDating):
                $ renpy.hide(character.apiName)
                call expression adjacentCharacter.apiName + 'SeesAffection' pass (action) from _call_expression_14
        $ i += 1

    call startCharacterInteraction(character) from _call_startCharacterInteraction_1

label characterInitiateAffection(character, action):
    $ action = action.replace(" ", "")
    if(renpy.has_label(character.apiName + 'Initiate' + action)):
        call expression character.apiName + 'Initiate' + action from _call_expression_15
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' Initiate' + action) from _call_wipCharacterInteraction_3
    return

label characterReceiveGift(character, item, likeChange, loveChange, onDate):
    if(renpy.has_label(character.apiName + 'ReceiveGift')):
        call expression character.apiName + 'ReceiveGift' pass (item = item, likeChange = likeChange, loveChange = loveChange) from _call_expression_16
        $ character.addLike(likeChange)
        $ character.addLove(loveChange)
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' ReceiveGift') from _call_wipCharacterInteraction_4
    if(onDate):
        jump expression character.apiName + 'DateInteraction'
    call startCharacterInteraction(character) from _call_startCharacterInteraction_2

label characterReceiveDateInvitation(character):
    if(renpy.has_label(character.apiName + 'ReceiveDateInvitation')):
        call expression character.apiName + 'ReceiveDateInvitation' from _call_expression_17
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' ReceiveDateInvitation') from _call_wipCharacterInteraction_5
    call startCharacterInteraction(character) from _call_startCharacterInteraction_3

label characterInviteOver(character):
    hide screen mainUi
    hide screen dateUi
    if(character.movedIn):
        call characterInviteGoHomeTogether(character) from _call_characterInviteGoHomeTogether
    else:
        $ renpy.music.stop('bgsfx', fadeout=0.5)
        call stopMusic from _call_stopMusic_3
        if(renpy.has_label(character.apiName + 'InviteOver')):
            $ mc.currentLocation = location_home
            call expression character.apiName + 'InviteOver' from _call_expression_18
            call characterContinueDateAtHome(character) from _call_characterContinueDateAtHome
        else:
            call wipCharacterInteraction(character = character, interactionType = character.apiName + ' InviteOver') from _call_wipCharacterInteraction_6
            return
        call endScene(character = character, targetLocation = mc.currentLocation) from _call_endScene_2

label characterInviteGoHomeTogether(character):
    call expression character.apiName + 'InviteGoHomeTogether' from _call_expression_19
    call goHomeTogether(character) from _call_goHomeTogether
    return

label characterStartDate(character):
    hide screen mainUi
    hide screen dateUi
    if(renpy.has_label(character.apiName + 'StartDate')):
        call playMusic(chillTheme) from _call_playMusic_35
        call expression character.apiName + 'StartDate' from _call_expression_20
        window hide
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' StartDate') from _call_wipCharacterInteraction_7
    call expression character.apiName + 'DateInteraction' from _call_expression_21

label characterDatePayFor(character):
    if(renpy.has_label(character.apiName + 'DatePayFor')):
        call expression character.apiName + 'DatePayFor' from _call_expression_22
    else:
        call wipDateInteraction(character = character, interactionType = character.apiName + 'DatePayFor') from _call_wipDateInteraction_2
    call expression character.apiName + 'DateInteraction' from _call_expression_23

label characterEndDate(character):
    hide screen dateUi
    if(dateScore >= 80):
        if(mc.currentLocation == location_home_bedroom):
            call characterContinueDateAtHome(character) from _call_characterContinueDateAtHome_1
        else:
            menu characterContinueDateToHome:
                "Продолжить свидание у себя дома?"
                'Yes':
                    call characterContinueDateAtHome(character) from _call_characterContinueDateAtHome_2
                'Завершить свидание':
                    pass
    call expression character.apiName + 'EndDate' from _call_expression_24
    call endScene(character = character, targetLocation = mc.currentLocation) from _call_endScene_3

label characterContinueDateAtHome(character):
    scene black with fade
    $ mc.currentLocation = location_home
    $ renpy.music.stop('bgsfx', fadeout=0.5)
    call expression character.apiName + 'ContinueDateAtHome' from _call_expression_25
    if(_return == True):
        menu characterContinueDateToSex:
            "Перейти в постель?"
            'Yes':
                $ character.addLove(1)
                call characterStartSex(character) from _call_characterStartSex_1
            'Завершить свидание':
                pass
    if(not character.movedIn):
        call expression character.apiName + 'EndDateAtHome' from _call_expression_26
    call endScene(character = character, targetLocation = mc.currentLocation) from _call_endScene_4

label characterHomeStartSex(character):
    call expression character.apiName + 'HomeStartSex' from _call_expression_27
    python:
        completedMultiGirlHEvents = [event for event in character.specialEvents if event.unlocked == True and "hevent" in event.apiName.lower()]
        otherGirls = []
        otherGirl = Null
        for event in completedMultiGirlHEvents:
            otherGirls.extend([otherGirl for otherGirl in event.characters if otherGirl != character and otherGirl.currentLocation.apiName.startswith('home')])
        if(len(otherGirls) > 0):
            randInt = renpy.random.randint(0, len(otherGirls)-1)
            otherGirl = otherGirls[randInt]
            #renpy.say("", "Other girl detected: " + otherGirl.name)
    if(otherGirl != Null and persistent.groupSex):
        $ renpy.show(character.apiName + ' tease', at_list=[twoPersonRight])
        $ renpy.with_statement(ease)
        call expression otherGirl.apiName + 'HomeSexJoinIn' pass(character = character) from _call_expression_28
        menu:
            extend ""
            "Конечно!":
                call characterStartThreesome(character, otherGirl) from _call_characterStartThreesome
            "Сегодня только мы":
                pass
    call characterStartSex(character) from _call_characterStartSex_2

label characterStartSex(character):
    hide screen mainUi
    scene black with fade
    call playMusic(sexyTheme) from _call_playMusic_36
    jump expression character.apiName + 'SexSelect'

label characterStartThreesome(girl1, girl2):
    hide screen mainUi
    scene black with fade
    call playMusic(sexyTheme) from _call_playMusic_37
    if(renpy.has_label(girl1.apiName + girl2.apiName + 'SexSelect')):
        jump expression girl1.apiName + girl2.apiName + 'SexSelect'
    elif (renpy.has_label(girl2.apiName + girl1.apiName + 'SexSelect')):
        jump expression girl2.apiName + girl1.apiName + 'SexSelect'
    return

label characterActionInRoom(character, location, action):
    $ action = action.replace(" ", "")
    if(renpy.has_label(character.apiName + location.apiName + action)):
        hide screen mainUi
        call expression character.apiName + location.apiName + action from _call_expression_29
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + location.apiName + action) from _call_wipCharacterInteraction_8
    call endScene(character = character) from _call_endScene_5

label characterSleepover(character):
    call expression character.apiName + 'Sleepover' from _call_expression_30
    scene black with fade
    pause
    call characterWakeup(character) from _call_characterWakeup
    call endScene(character = character, targetLocation = location_home, targetTime = 'Morning') from _call_endScene_6

label characterWakeup(character):
    $ randInt = -1
    if(len(character.wakeUpOptions) > 0):
        $ randInt = renpy.random.randint(-1, len(character.wakeUpOptions)-1)
        $ eventName = character.wakeUpOptions[randInt]
    if(randInt == -1 or not(renpy.has_label(character.apiName + 'MorningBedInteractionSex'))):
        if(renpy.has_label(character.apiName + 'MorningBedInteraction')):
            call expression character.apiName + 'MorningBedInteraction' from _call_expression_31
    else:
        call characterWakeupSex(character, eventName) from _call_characterWakeupSex
    return

label characterWakeupSex(character, event, fromGallery = False):
    call hideAllScreens from _call_hideAllScreens_1
    hide screen mainUi
    if(renpy.has_label(character.apiName + 'MorningBedInteractionSex')):
        call expression character.apiName + 'MorningBedInteractionSex' pass (event = event) from _call_expression_32
    if(fromGallery):
        call goToLocation(mc.currentLocation, True) from _call_goToLocation
    python:
        if(event not in character.selfiesSent):
            character.wakeUpOptionsSeen.append(event)
    return

label wipCharacterInteraction(character, interactionType):
    debug "WIP [interactionType]"
    call startCharacterInteraction(character) from _call_startCharacterInteraction_4

label wipDateInteraction(character, interactionType):
    debug "WIP [interactionType]"
    $ renpy.call(character.apiName + 'DateInteraction')

label endCharacterInteraction(character):
    call evaluateAvailableInteractions(character) from _call_evaluateAvailableInteractions
    call characterInitiateInviteOver(character) from _call_characterInitiateInviteOver
    window hide
    $ renpy.hide(character.apiName)
    with Dissolve(0.3)
    call goToLocation(mc.currentLocation) from _call_goToLocation_1

label characterInitiateInviteOver(character):
    if(not character.currentLocation.apiName.startswith('home') and 'Invite over' in character.availableActions and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        # 20% chance to ask to come over tonight
        $ randInt = renpy.random.randint(1, 10)
        if(randInt < 3 and renpy.has_label(character.apiName + 'InitiateInviteOver')):
            if(character.movedIn):
                call characterInitiateGoHomeTogether(character) from _call_characterInitiateGoHomeTogether
            else:
                call expression character.apiName + 'InitiateInviteOver' from _call_expression_33
                if(_return == True):
                    hide screen mainUi
                    $ mc.currentLocation = location_home
                    call characterContinueDateAtHome(character) from _call_characterContinueDateAtHome_3
    return

label characterInitiateGoHomeTogether(character):
    call expression character.apiName + 'InitiateGoHomeTogether' from _call_expression_34
    if(_return == True):
        call goHomeTogether(character) from _call_goHomeTogether_1
    return

label goHomeTogether(character):
    scene black with fade
    $ character.debugMoveCharacterToLocation(location_home_lounge)
    call goToLocation(location_home_lounge, withFade = True) from _call_goToLocation_2
    return

label endScene(character = Null, fromEvent = False, targetTime = Null, targetLocation = mc.currentLocation):
    if(character != Null):
        call evaluateAvailableInteractions(character) from _call_evaluateAvailableInteractions_1
    call progressTime(returnToLabel = True, targetTime = targetTime) from _call_progressTime
    call goToLocation(targetLocation, True) from _call_goToLocation_3

label evaluateAvailableInteractions(character):
    python:
        character.availableActions = ['Chat', 'Gift']
        character.availableAffections = []
        character.availableCommandsPublic = []
        character.availableCommandsPrivate = []
    if(renpy.has_label(character.apiName + 'EvaluateAvailableInteractions')):
        call expression character.apiName + 'EvaluateAvailableInteractions' from _call_expression_35
    return

label dateInvitationSelector(character):
    python:
        unavailableCurrentDayTimes = timesOfDay
        unavailableCurrentDayTimes = unavailableCurrentDayTimes[:timesOfDay.index(timeOfDay)+1]
        proposedDateDay = ''
        proposedDateTime = ''
    menu dateDateSelect:
        'Сегодня' if len(unavailableCurrentDayTimes) != len(timesOfDay):
            $ proposedDateDay = day
        'Завтра':
            $ proposedDateDay = day + 1
        '[daysOfWeek[(daysOfWeek.index(dayOfWeek) + 2) %% len(daysOfWeek)]]': # % modulus on list allows looping around to start of array. %% to escape character
            $ proposedDateDay = day + 2
        '[daysOfWeek[(daysOfWeek.index(dayOfWeek) + 3) %% len(daysOfWeek)]]':
            $ proposedDateDay = day + 3
        '[daysOfWeek[(daysOfWeek.index(dayOfWeek) + 4) %% len(daysOfWeek)]]':
            $ proposedDateDay = day + 4
        '[daysOfWeek[(daysOfWeek.index(dayOfWeek) + 5) %% len(daysOfWeek)]]':
            $ proposedDateDay = day + 5
        '[daysOfWeek[(daysOfWeek.index(dayOfWeek) + 6) %% len(daysOfWeek)]]':
            $ proposedDateDay = day + 6
        'Не сейчас':
            call startCharacterInteraction(character) from _call_startCharacterInteraction_5

    if(proposedDateDay != day):
        $ unavailableCurrentDayTimes = []
    menu dateTimeSelect:
        set unavailableCurrentDayTimes
        'Morning':
            $ proposedDateTime = 'Morning'
        'Afternoon':
            $ proposedDateTime = 'Afternoon'
        'Evening':
            $ proposedDateTime = 'Evening'
        'Night':
            $ proposedDateTime = 'Night'
        'Back':
            jump dateDateSelect
    $ proposedDateDayOfWeek = [daysOfWeek[(proposedDateDay-1) % len(daysOfWeek)]][0]

    call screen dateInvitationLocationSelector(character)

    return

label inviteToSpecialEvent(character, event):
    call expression event.apiName + 'Invitation' pass (fromGallery = False) from _call_expression_36
    python:
        mc.money -= event.cost
        daysUntilEvent = 3
        for existingScheduledEventDates in [date for date in mc.scheduledDates if date.forced == True]:
            daysUntilEvent += 1
        specialEventDate = Date(character, location_home, day + daysUntilEvent, '', 'Morning')
        specialEventDate.forced = True
        specialEventDate.event = event
        mc.scheduledDates.append(specialEventDate)
        character.scheduledDates.append(specialEventDate)
        event.scheduled = True
        character.availableSpecialEvents.remove(event)
    call endScene(character = character, targetLocation = mc.currentLocation) from _call_endScene_7

label startSpecialEvent(character, event):
    python:
        if(len(mc.scheduledDates) > 0):
            for date in mc.scheduledDates.copy():
                if(date.day == day):
                    mc.scheduledDates.remove(date)
                    date.character.scheduledDates = []
                    mc.awaitingDate = False
                    renpy.notify('Ты отменил свидание. Ничего страшного, она всё поняла!')
    $ event.load()
    call endScene(character = character, targetLocation = location_home) from _call_endScene_8

label characterCommandShowPanties(character):
    if(renpy.has_label(character.apiName + 'ShowPanties')):
        call expression character.apiName + 'ShowPanties' pass (pantiesIndex = character.pantiesWornIndex) from _call_expression_37
    else:
        call wipCharacterInteraction(character = character, interactionType = character.apiName + ' ShowPanties') from _call_wipCharacterInteraction_9
    call startCharacterInteraction(character) from _call_startCharacterInteraction_6

label endOfCharacterStory:
    ofkeres "К сожалению, на этом пока заканчивается история персонажа!"
    ofkeres "Tails on the Rocks всё ещё в разработке. Впереди ещё много нового, и нам очень нужна ваша поддержка!"
    ofkeres "Поддержать проект можно на {a=[patreonLink]}>>>Patreon<<<{/a}.\nВ числе преимуществ — ранний доступ, участие в опросах о разработке, эксклюзивные иллюстрации и специальные заказы на рендеры!"
    ofkeres "Также присоединяйтесь к обсуждению на {a=[discordLink]}сервере Discord{/a}."
    ofkeres "Надеюсь, вам нравится Tails on the Rocks. Возможно, впереди вас ждут и другие девушки!"
    return

screen dateInvitationLocationSelector(character):
    python:
        availableLocations = [location for location in locations if (location.knownToMC and location.isDateSpot and proposedDateDayOfWeek not in location.closedDaysOfWeek and proposedDateTime in location.openTimes and location.accessibleToNPCs)]
        if('Invite over' in character.availableActions):
            availableLocations.append(location_home)
    style_prefix "choice"
    vbox:
        at choicesMenuReveal
        for location in availableLocations:
            textbutton _(location.name) action [SetVariable('proposedDateLocation', location), Return()]
        textbutton 'Back' action Jump('dateTimeSelect')


# Character sprite animations
transform characterSpriteHover:
    on hover:
        linear 0.1 zoom 1.01
    on idle:
        linear 0.1 zoom 1.0

transform characterInSceneSpriteHover:
    on hover:
        ease 0.1 ypos -3
    on idle:
        ease 0.1 ypos 0

transform twoPersonRight:
    xalign 0.75
    yalign 1.0

transform twoPersonLeft:
    xalign 0.25
    yalign 1.0

# Character sprite styles
style characterClickable:
    yalign 1.0
    yoffset 10

# Custom Transitions
define fadewhite = Fade(0.5, 0.5, 1, color="#FFFFFF")
