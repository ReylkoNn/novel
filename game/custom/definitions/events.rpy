default inEventReplay = False

# Event class definition
init python:
    class Event:
        def __init__(self, name, apiName, characters, requiredLike, requiredLove, requiredEvents, triggerLocation, triggerTimes = ['Morning', 'Afternoon', 'Evening', 'Night'], triggerDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], extraNotes = '', triggerDay = 0, cost = 0, requiredItems = [], requiresInvite = False, mcInitiated = False):
            self.name = name
            self.apiName = apiName
            self.characters = characters
            self.unlocked = False
            self.requiredLike = requiredLike
            self.requiredLove = requiredLove
            self.requiredEvents = requiredEvents
            self.triggerLocation = triggerLocation
            self.triggerTimes = triggerTimes
            self.triggerDays = triggerDays
            self.extraNotes = extraNotes
            self.triggerDay = triggerDay
            self.scheduled = False
            self.cost = cost
            self.requiredItems = requiredItems
            self.requiresInvite = requiresInvite # MC has to use dialogue options to initiate
            self.mcInitiated = mcInitiated # MC has to click on their person in scene to start

        def load(self, fromGallery = False):
            if(not fromGallery):
                for character in self.characters:
                    if(self in character.availableEvents):
                        character.availableEvents.remove(self)
            renpy.music.stop(channel='bgsfx', fadeout=0.5)
            renpy.music.stop(channel='music', fadeout=0.5)
            renpy.call('playEvent', event = self, fromGallery = fromGallery)

    class Date:
        def __init__(self, character, location, day, dayOfWeek, time):
            self.character = character
            if(hasattr(location, 'subLocations') and location.subLocations != []):
                self.location = location.subLocations[0]
            else:
                self.location = location
            self.day = day
            self.dayOfWeek = dayOfWeek
            self.time = time
            self.completed = False
            self.missed = False
            self.forced = False
            self.event = Null

label playEvent(event, fromGallery):
    call hideAllScreens from _call_hideAllScreens_2
    hide screen mainUi
    $ inEventReplay = False

    # Play the event and return
    $ playInvitation = False
    $ event.scheduled = False
    if(fromGallery):
        $ inEventReplay = True
        if(renpy.has_label(event.apiName + 'Invitation')):
            menu:
                "Проиграть приглашение или событие?"
                "Приглашение":
                    $ playInvitation = True
                "Событие":
                    pass
    if(playInvitation):
        call expression event.apiName + 'Invitation' pass (fromGallery) from _call_expression_45
    else:
        call expression event.apiName pass (fromGallery) from _call_expression_46
    $ returnVariables = _return

    # Return back to mc location if was from gallery
    if(fromGallery):
        $ inEventReplay = False
        call goToLocation(mc.currentLocation, True) from _call_goToLocation_4

    $ event.unlocked = True

    # End of character story message
    if(len(event.characters) == 1):
        $ lockedEvents = [event for event in event.characters[0].events if not event.unlocked]
        if(len(lockedEvents) == 0):
            call endOfCharacterStory from _call_endOfCharacterStory

    # End scene
    $ targetTime = Null
    $ targetLocation = mc.currentLocation
    if(returnVariables != None):
        if('time' in returnVariables):
            $ targetTime = returnVariables.get('time')
        if('location' in returnVariables):
            $ targetLocation = returnVariables.get('location')
    call endScene(character = event.characters[0], fromEvent = True, targetTime = targetTime, targetLocation = targetLocation) from _call_endScene_16
