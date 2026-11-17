# Declare locations used by this game.
init offset = 1

# Location class definition
init python:
    class Location:
        def __init__(self, name, apiName, imagePath, mapXPos, mapYPos, knownToMC, openTimes, isDateSpot, accessibleToNPCs, hasTimeOfDay = False):
            self.name = name
            self.apiName = apiName
            self.imagePath = imagePath
            self.mapXPos = mapXPos
            self.mapYPos = mapYPos
            self.knownToMC = knownToMC
            self.accessibleToNPCs = accessibleToNPCs
            self.occupants = []
            self.openTimes = openTimes
            self.closedDaysOfWeek = []
            self.inventory = {}
            self.hasTimeOfDay = hasTimeOfDay
            self.subLocations = []
            self.occupantLimit = -1

            # Date attributes
            self.isDateSpot = isDateSpot

        def go(self, withFade):
            renpy.scene()
            location = self
            eventToLaunch = Null
            for character in location.occupants: # if character triggering event is in parent location
                eventToLaunch = character.sceneEvaluator()
                if(eventToLaunch != Null and not eventToLaunch.mcInitiated):
                    break
            if(hasattr(self, 'subLocations') and self.subLocations != []):
                location = self.subLocations[0]
            location.showBackground(withFade)
            store.mc.currentLocation = location
            if(eventToLaunch == Null):
                for character in location.occupants:
                    eventToLaunch = character.sceneEvaluator()
                    if(eventToLaunch != Null and not eventToLaunch.mcInitiated):
                        break
            # Check if you need to cancel anything if an event is launching
            if(eventToLaunch != Null and not eventToLaunch.mcInitiated):
                if(len(mc.scheduledDates) > 0):
                    for date in mc.scheduledDates.copy():
                        if(date.day == day):
                            mc.scheduledDates.remove(date)
                            date.character.scheduledDates = []
                            mc.awaitingDate = False
                            renpy.notify('Свидание отменено. Всё в порядке, она поняла!')
                eventToLaunch.load()
            renpy.show_screen(location.apiName, zorder=2)
            bgsfxTrack = 'audio/bgsfx/' + target.apiName + '.ogg'
            if(renpy.music.get_playing('bgsfx') != bgsfxTrack):
                renpy.music.play(bgsfxTrack, 'bgsfx', fadein = 0.3, fadeout = 0.3)
            if(renpy.music.get_playing('music') != mainTheme):
                renpy.music.play(mainTheme, 'music', fadein = 0.5, fadeout = 0.5)
            return

        def showBackground(self, withFade = True):
            renpy.scene()
            location = self
            if(hasattr(self, 'subLocations') and self.subLocations != []):
                location = self.subLocations[0]
            if(location.hasTimeOfDay):
                renpy.show(location.imagePath + timeOfDay.lower())
            else:
                renpy.show(location.imagePath)
            if(withFade):
                renpy.with_statement(fade)

# Location definitions
default location_home = Location('Дом', 'home', 'home', 0.84, 0.16, True, ['Morning', 'Afternoon', 'Evening', 'Night'], True, False, True)
default location_home_bedroom = Location('Спальня', 'homebedroom', 'homebedroom', Null, Null, True, ['Morning', 'Afternoon', 'Evening', 'Night'], False, False, True)
default location_home_lounge = Location('Гостиная', 'homelounge', 'homelounge', Null, Null, True, ['Morning', 'Afternoon', 'Evening', 'Night'], False, False, True)
default location_home_kitchen = Location('Кухня', 'homekitchen', 'homekitchen', Null, Null, True, ['Morning', 'Afternoon', 'Evening', 'Night'], False, False, True)
default location_home_bathroom = Location('Ванная', 'homebathroom', 'homebathroom', Null, Null, True, ['Morning', 'Afternoon', 'Evening', 'Night'], False, False, True)

default location_map = Location('Карта', 'map', 'map', Null, Null, True, ['Morning', 'Afternoon', 'Evening', 'Night'], False, False, True)
default location_away = Location('Вдали', 'away', 'away', Null, Null, False, ['Morning', 'Afternoon', 'Evening', 'Night'], False, True, False)

#default location_alicesHome = Location('Дом Алисы', 'alicesHome', 'aliceshome', 0.1, 0.9, False, False, ['Morning', 'Afternoon', 'Evening', 'Night'], False, True, False)

default location_town = Location('Город', 'town', 'town', 0.38, 0.2, True, ['Morning', 'Afternoon', 'Evening', 'Night'], False, True, True)
default location_park = Location('Парк', 'park', 'park', 0.82, 0.5, True, ['Morning', 'Afternoon', 'Evening'], True, True, True)
default location_cafe = Location('Кафе', 'cafe', 'cafe', 0.17, 0.21, True, ['Morning', 'Afternoon', 'Evening'], True, True, True)
default location_bar = Location('Бар', 'bar', 'bar', 0.6, 0.23, True, ['Afternoon', 'Evening', 'Night'], True, True, False)
default location_shop = Location('Магазин', 'shop', 'shop', 0.55, 0.47, True, ['Morning', 'Afternoon', 'Evening'], False, True, True)
default location_beach = Location('Пляж', 'beach', 'beach', 0.75, 0.75, True, ['Morning', 'Afternoon', 'Evening', 'Night'], True, True, True)
default location_diner = Location('Закусочная', 'diner', 'diner', 0.28, 0.45, True, ['Morning', 'Afternoon', 'Evening'], True, True, False)
default location_aquarium = Location('Аквариум', 'aquarium', 'aquarium', 0.25, 0.13, True, ['Morning', 'Afternoon', 'Evening'], True, True, False)
default location_theater = Location('Театр', 'theater', 'theater', 0.32, 0.32, True, ['Morning', 'Afternoon', 'Evening'], True, True, False)

# Starts hidden / unknown
default location_library = Location('Библиотека', 'library', 'library', 0.1, 0.7, False, ['Morning', 'Afternoon', 'Evening'], False, True, False)
default location_college = Location('Колледж', 'college', 'college', 0.7, 0.1, False, ['Morning', 'Afternoon', 'Evening', 'Night'], False, True, True)
default location_offices = Location('Офисы', 'offices', 'offices', 0.5, 0.3, False, ['Morning', 'Afternoon', 'Evening'], False, True, False)

label initialiseLocations:
    call updateLocationStatics from _call_updateLocationStatics
    call initialiseShop from _call_initialiseShop
    call initialiseSuperstore from _call_initialiseSuperstore

    $ locations = []
    # Known
    $ locations.extend([location_home, location_home_lounge, location_home_bedroom, location_home_kitchen, location_home_bathroom])
    $ locations.extend([location_away, location_map, location_town, location_park, location_cafe, location_bar, location_shop, location_beach, location_diner, location_aquarium, location_theater])
    # Unknown
    $ locations.extend([location_library, location_college, location_offices])
    return

label updateLocationStatics:
    python:
        locations = []
        locations.extend([location_home, location_home_lounge, location_home_bedroom, location_home_kitchen, location_home_bathroom])
        locations.extend([location_away, location_map, location_town, location_park, location_cafe, location_bar, location_shop, location_beach, location_diner, location_aquarium, location_theater])
        locations.extend([location_library, location_college, location_offices])
        location_map.hasTimeOfDay = True
        location_home.mapXPos = 0.84
        location_home.mapYPos = 0.16
        location_home.subLocations = [location_home_bedroom, location_home_lounge, location_home_kitchen, location_home_bathroom]
        location_home.hasTimeOfDay = True
        location_home_bathroom.occupantLimit = 1
        location_town.mapXPos = 0.38
        location_town.mapYPos = 0.2
        location_town.hasTimeOfDay = True
        location_park.mapXPos = 0.82
        location_park.mapYPos = 0.5
        location_park.hasTimeOfDay = True
        location_cafe.mapXPos = 0.17
        location_cafe.mapYPos = 0.21
        location_cafe.hasTimeOfDay = True
        location_bar.mapXPos = 0.6
        location_bar.mapYPos = 0.23
        location_bar.hasTimeOfDay = False
        location_shop.mapXPos = 0.55
        location_shop.mapYPos = 0.47
        location_shop.hasTimeOfDay = True
        location_beach.mapXPos = 0.75
        location_beach.mapYPos = 0.75
        location_beach.hasTimeOfDay = True
        location_diner.mapXPos = 0.28
        location_diner.mapYPos = 0.45
        location_diner.hasTimeOfDay = False
        location_aquarium.mapXPos = 0.25
        location_aquarium.mapYPos = 0.13
        location_aquarium.hasTimeOfDay = False
        location_theater.mapXPos = 0.32
        location_theater.mapYPos = 0.32
        location_theater.hasTimeOfDay = False
        location_theater.knownToMC = True
    return
