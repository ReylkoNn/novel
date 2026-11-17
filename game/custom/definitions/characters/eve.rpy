init offset = 3
default eve = Person(Character(name='Eve', who_color='#9eb439', image = 'eve'), 'Eve', '', 'eve', 'female', 24)

label initialiseCharacter_eve:
    python:
        eve.currentLocation = location_town
        location_town.occupants.extend([eve])
        eve.availableEvents = []
        eve.blockedLocations = [location_bar]
        
    return

label updateCharacterStatics_eve:
    python:
        # Personal attributes
        eve.species = 'Mouse'
        eve.birthday = 8
        eve.job = 'Usher'
        eve.giftLoves = [item_chocolateBar, item_candles]
        eve.giftLikes = [item_dress, item_wine]
        eve.giftHates = [item_book]

        # Skill attributes

        # Sexual attributes
        eve.virgin = False

        # Personal effects

        # Event attributes
        eve.events = [eveFirstMeetingEvent, eveLikeEvent1, eveLikeEvent2, eveHEvent1, eveHEvent2, eveHEvent3, eveHEvent4, eveHEvent5]
        eve.specialEvents = []
        eve.selfieOptions = ['work1', 'beach1', 'changingroom1', 'bedroom1']  #TODO , 'homekitchen1'
        eve.wakeUpOptions = []
        eve.dateChats = ['Background', 'Job']
        eve.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = eve.events[-1]
        eve.maxLike = lastStoryEvent.requiredLike
        eve.maxLove = lastStoryEvent.requiredLove

        # World attributes
        eve.preferredMondaySchedule = [location_away, location_cafe, location_beach, location_away]
        eve.preferredTuesdaySchedule = [location_theater, location_theater, location_town, location_away]
        eve.preferredWednesdaySchedule = [location_away, location_theater, location_town, location_away]
        eve.preferredThursdaySchedule = [location_park, location_theater, location_theater, location_away]
        eve.preferredFridaySchedule = [location_shop, location_park, location_theater, location_away]
        eve.preferredSaturdaySchedule = [location_theater, location_theater, location_theater, location_away]
        eve.preferredSundaySchedule = [location_away, location_shop, location_diner, location_bar]

        eve.preferredMovedInMondaySchedule = [location_home, location_cafe, location_beach, location_home]
        eve.preferredMovedInTuesdaySchedule = [location_home, location_theater, location_shop, location_home]
        eve.preferredMovedInWednesdaySchedule = [location_home, location_theater, location_bar, location_home]
        eve.preferredMovedInThursdaySchedule = [location_home, location_theater, location_theater, location_home]
        eve.preferredMovedInFridaySchedule = [location_home, location_shop, location_theater, location_home]
        eve.preferredMovedInSaturdaySchedule = [location_home, location_theater, location_theater, location_home]
        eve.preferredMovedInSundaySchedule = [location_home, location_diner, location_home, location_home]
    return

# Sprites
screen eveClickable(xcenter):
    $ spriteload = eve.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = eve)
        at characterSpriteHover

# Character methods
label eveEvaluateAvailableInteractions:
    python:
        if eve.like >= 5 and eveLikeEvent2.unlocked:
            eve.availableActions = list(set(eve.availableActions + ['Spend time']))
        if eveHEvent3.unlocked:
            eve.availableActions = list(set(eve.availableActions + ['Invite over']))

        if eve.isDateable and eve.love >= 1:
            eve.availableActions = list(set(eve.availableActions + ['Date']))
        if eveHEvent1.unlocked:
            eve.availableActions = list(set(eve.availableActions + ['Affection']))
            eve.availableAffections.extend(['Pat'])
        if eveHEvent3.unlocked:
            eve.availableAffections.extend(['Boob Grab'])
        if eveHEvent4.unlocked:
            eve.availableAffections.extend(['Caress Butt'])
        if eveHEvent5.unlocked:
            eve.availableAffections.extend(['Hug', 'Kiss', 'Chin Scratch'])
        if eve.movedIn:
            eve.availableCommandsPrivate.extend(['Show Panties'])
            eve.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label eveChat:
    show eve smile talk
    return

label eveChat_beach:
    show eve smile talk
    eve.c "Эй~ Пойдёшь купаться?"
    return

label eveChat_park:
    show eve thinking
    eve.c "Фух... Перерыв... Присядешь?"
    return

label eveChat_shop:
    show eve tease talk
    eve.c "Ага~ Кинотеатр — такая обдираловка. Просто проноси еду с собой."
    return

label eveChat_diner:
    show eve neutral talk
    eve.c "О, привет. Просто готовить неохота, понимаешь?"
    show eve smile talk
    eve.c "О, ты тоже так себе готовишь? Ага~"
    return

label eveChat_cafe:
    show eve neutral talk
    eve.c "Я даже кофе особо не люблю."
    show eve smile talk
    eve.c "Но без кофеина я сдохну."
    return

label eveChat_town:
    show eve thinking
    eve.c "А? О, привет... Я тут на работу иду..."
    return

label eveChat_bar:
    show eve smile talk
    eve.c "Эй, здоровяк~ Я тут~"
    eve.c "За работу, ха-ха~"
    return

label eveChat_aquarium:
    show eve tease talk
    eve.c "Этот магазин... Тут даже рыбы нет..."
    show eve bashful talk
    eve.c "А? Нет, ничего не хочу..."
    return

label eveChat_theater:
    show eve neutral talk
    eve.c "За фильмом пришёл или меня достать?"
    show eve smile talk
    eve.c "Смотря что, могу с тобой прошмыгнуть внутрь~"
    return

label eveChat_homebedroom:
    if(timeOfDay == 'Morning'):
        show eve thinking
        eve.c "Ещё один день, ещё пара... центов..."
    elif(timeOfDay == 'Afternoon'):
        show eve smile talk
        eve.c "Хочешь чем-нибудь заняться? Только {i}не{/i} предлагай кино..."
    elif(timeOfDay == 'Evening'):
        show eve neutral talk
        eve.c "Я уже вырубаюсь, скоро усну..."
    elif(timeOfDay == 'Night'):
        show eve smile talk 2
        eve.c "Пойдём спать, милый~"
    return

label eveChat_homelounge:
    if(timeOfDay == 'Morning'):
        show eve tease talk
        eve.c "Рано уходишь? Ага~ Ну, удачи~"
    elif(timeOfDay == 'Afternoon'):
        show eve smile talk 2
        eve.c "До смены ещё есть время... Хочешь что-нибудь посмотреть?"
    elif(timeOfDay == 'Evening'):
        show eve thinking
        eve.c "Вот это денёк... Ничего не хочу..."
    elif(timeOfDay == 'Night'):
        show eve smile talk 2
        eve.c "Этот ужастик даже ничего. Посмотрим?"
    return

label eveChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show eve neutral talk
        eve.c "*Зевает*~ Эй, мне сегодня нужен кофе..."
    elif(timeOfDay == 'Afternoon'):
        show eve smile talk
        eve.c "Где все вкусняшки?"
    elif(timeOfDay == 'Evening'):
        show eve smile talk
        eve.c "Я бы помогла тебе приготовить, но... сам знаешь, ага~"
    elif(timeOfDay == 'Night'):
        show eve thinking
        eve.c "Дурацкая полка слишком высокая..."
    return

# Date topics
label eveChat_background:
    mc.c "Ну, расскажешь о себе?"
    show eve neutral talk
    eve.c "Обо мне?"
    show eve neutral
    mc.c "Ну, откуда ты, как росла, всё такое?"
    show eve neutral talk
    eve.c "...Я из этого дома."
    show eve neutral
    "..."
    mc.c "Э-э..."
    show eve smile talk
    eve.c "Ага~ Твоё лицо~"
    show eve thinking
    eve.c "Хм... Да нечего особо рассказывать."
    show eve neutral talk
    eve.c "Всю жизнь тут прожила..."
    eve.c "Тут всего пара школ. Училась в ближайшей, так себе..."
    eve.c "Нашла дерьмовую работу... Вот и вся история."
    show eve neutral
    mc.c "Ты же съехала от родителей. Давно живёшь там?"
    show eve neutral talk
    eve.c "Ага, родители всё ещё тут, но живут на окраине."
    eve.c "Я съехала вскоре после школы, когда нашла работу."
    show eve thinking
    eve.c "Зарплаты едва хватает... Но я точно знала, что хочу жить отдельно."
    show eve neutral talk
    eve.c "Уже пару лет... До этого я какое-то время жила в месте ещё похуже."
    show eve thinking
    eve.c "Хм... Чёрт, выходит, мне уже [eve.age]... Депрессивно..."
    mc.c "С семьёй видишься? Братья или сёстры есть?"
    show eve smile talk
    eve.c "Ага~ Несколько... Восемь штук..."
    show eve smile
    mc.c "Господи."
    show eve tease talk
    eve.c "Слышал выражение «размножаться, как крысы»? Ну вот, мыши тоже. Мама рожала одного за другим, хе-хе~"
    show eve tease
    mc.c "Наверное, приятно иметь большую семью?"
    show eve thinking
    eve.c "Ага, вроде ладим... Кто-то ещё в школе, кто-то уехал и завёл свою семью..."
    show eve smile talk 2
    eve.c "А пара неудачников болтается без дела, как я, ага~"
    return

label eveChat_job:
    mc.c "Как тебе работа в кинотеатре?"
    show eve thinking
    eve.c "Отстой."
    mc.c "Понятно..."
    show eve smile talk
    eve.c "Хе~ Да вроде не так плохо... Стоишь себе целыми днями, понимаешь..."
    show eve tease talk
    eve.c "{i}Добро пожаловать, сэр~ Добро пожаловать, мадам~ С вас 9,99~{/i}."
    show eve thinking
    eve.c "И дети..."
    mc.c "Дети?"
    eve.c "Детские фильмы... Хуже не бывает."
    show eve mad talk
    eve.c "А убирать потом... Почему люди раскидывают попкорн по всему залу после какой-то тупой хрени?"
    eve.c "Ты ведь так не делаешь?"
    show eve mad
    mc.c "Нет."
    show eve neutral talk
    eve.c "Вот и хорошо... А так всё бесконечно..."
    show eve neutral
    mc.c "Никаких бонусов? Бесплатных фильмов?"
    show eve thinking
    eve.c "Хм... Пару раз в месяц дают посмотреть... Но только в свободное время..."
    show eve smile talk
    eve.c "Да и хорошего ничего нет. Неделями крутят одно и то же. Скукотища~"
    show eve smile talk
    eve.c "Но я иногда таскаю попкорн или конфеты~"
    show eve smile
    mc.c "Тебе разрешают или просто не ловят?"
    show eve smile talk
    eve.c "Главное — не попасться~ Менеджер ничего не замечает. Он туповат~"
    show eve smile
    mc.c "Тогда в следующий раз угости меня чем-нибудь, когда я приду смотреть кино."
    show eve tease talk
    eve.c "Ага-ха~ Ладно, здоровяк~"
    return

#

label eveInteractionBathroom:
    eve.c "Кья~ Злой человек пришёл мной воспользоваться~"
    eve.c "Что же мне делать~?"
    return

label eveSpendTime(onDate):
    if(onDate):
        scene expression 'eve[mc.currentLocation.apiName]date'
    else:
        scene expression 'eve[mc.currentLocation.apiName]'
    with fade
    return

label eveReceiveGift(item, likeChange, loveChange):
    show eve smile
    eve.c "Хм?"
    if(loveChange > 0):
        show eve joy
        if(eve.movedIn):
            eve.c "Ого~ Спасибо, милый!"
        else:
            eve.c "Ого~ Спасибо, здоровяк~"
    elif(likeChange > 1):
        show eve smile talk
        eve.c "Йо, круто~ Спасибо."
    elif(likeChange < 1):
        show eve thinking
        eve.c "Хм... Мне это не нужно..."
    else:
        show eve smile talk
        eve.c "Эй, спасибо~"
    return

label eveReceiveDateInvitation:
    show eve smile talk
    eve.c "Куда-нибудь сходить? Ладно. Когда?"
    show eve smile
    call dateInvitationSelector(eve) from _call_dateInvitationSelector_1
    show eve smile talk
    eve.c "[proposedDateLocation.name] — [proposedDateDayOfWeek], [proposedDateTime]? Круто."

    python:
        scheduledDate = Date(eve, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        eve.scheduledDates.append(scheduledDate)
    return

label eveStartDate:
    if(mc.currentLocation == location_home):
        show eve smile talk with dissolve
        eve.c "Йо."
    else:
        show eve smile talk 2 with dissolve
        eve.c "Как обычно?"
    return

label eveDateInteraction:
    show eve smile with dissolve
    show screen dateUi(eve) with dissolve
    call screen dateInteractionScreen(eve, mc.currentLocation)

label eveChatDate:
    show eve tease talk
    eve.c "Лучше, чем торчать на работе~ Ага~"
    return

label eveChatDate_beach:
    show eve thinking
    eve.c "Хм... Купальник мне тесноват..."
    show eve neutral talk
    eve.c "Хочешь посмотреть?"
    return

label eveChatDate_park:
    show eve smile talk
    eve.c "Приятный ветерок..."
    show eve smile talk 2
    eve.c "Принесёшь мне выпить? Пожалуйста~"
    return

label eveChatDate_diner:
    show eve tease talk
    eve.c "Ты платишь, да~?"
    show eve bashful talk
    eve.c "А, да? Спасибо... не обязательно было..."
    return

label eveChatDate_cafe:
    show eve neutral talk
    eve.c "Возьми бабл-ти, вкусный."
    show eve tease talk
    eve.c "И мне тоже, раз уж идёшь~ Ага~"
    return

label eveChatDate_bar:
    show eve smile talk 2
    eve.c "Ещё? Давай, почему нет?"
    show eve tease talk
    eve.c "У тебя есть план~?"
    return

label eveChatDate_aquarium:
    show eve smile talk
    eve.c "Ага~ Они такие смешные~"
    show eve thinking
    eve.c "Делать нечего... Блин, завидую..."
    return

label eveChatDate_theater:
    show eve smile talk
    eve.c "Приперлась ко мне в выходной, придурок~"
    show eve smile talk 2
    eve.c "У меня там знакомые работают... Устроят нам скидку."
    return

label eveDatePayFor:
    show eve tease talk
    eve.c "Круто, я совсем на мели~"
    return

label eveEndDate:
    if(dateScore < 40):
        show eve thinking
        eve.c "Хмф... Пойду домой..."
    else:
        if(eve.movedIn):
            show eve joy
            eve.c "Разве уже пора заканчивать?"
            eve.c "О, можем просто пойти домой~ Ага~"
        else:
            show eve tease talk
            eve.c "Весело было~"
    return

label eveContinueDateAtHome:
    scene expression 'eve[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(eveHEvent5.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label eveHomeStartSex:
    show eve tease talk
    eve.c "Собираешься мной воспользоваться~?"
    eve.c "Что же мне делать~?"
    show eve tease
    return

label eveHomeSexJoinIn(character):
    show eve neutral talk at twoPersonLeft with dissolve
    eve.c "Я уже завелась... Можно с вами?"
    show eve neutral
    return

label eveEndDateAtHome:
    eve.c "Мне обязательно тащиться {i}так{/i} далеко домой? Донеси меня~"
    return

image eve pat animated = Movie(play="images/characters/eve/affections/evePat.webm", side_mask=True, loop=True)
label eveReceivePat:
    hide eve with dissolve
    show eve pat animated with dissolve
    pause
    eve.c "Да ладно, как скажешь..."
    eve.c "Я не ребёнок..."
    return

image eve chinscratch animated = Movie(play="images/characters/eve/affections/eveChinscratch.webm", side_mask=True, loop=True)
label eveReceiveChinScratch:
    hide eve with dissolve
    show eve chinscratch animated with dissolve
    pause
    eve.c "Ты такой странный~"
    eve.c "Что в этом весёлого?"
    return

image eve caressbutt animated = Movie(play="images/characters/eve/affections/eveCaressButt.webm", side_mask=True, loop=True)
label eveReceiveCaressButt:
    hide eve with dissolve
    show eve caressbutt animated with dissolve
    pause
    eve.c "Ты всегда делаешь что хоче— А-а!"
    eve.c "Блин, горячо~"
    return

image eve boobgrab animated = Movie(play="images/characters/eve/affections/eveBoobGrab.webm", side_mask=True, loop=True)
label eveReceiveBoobGrab:
    hide eve with dissolve
    show eve boobgrab animated with dissolve
    pause
    eve.c "Такие же, как в прошлый раз, здоровяк~"
    eve.c "Хочешь ещё раз их попробовать?"
    return

image eve snuggle animated = Movie(play="images/characters/eve/affections/eveSnuggle.webm", side_mask=True, loop=True)
label eveReceiveSnuggle:
    "Ева устроилась на краю дивана."
    show eve smile talk
    eve.c "Эй. Ты чего...?"
    hide eve with dissolve
    show eve snuggle animated with dissolve
    pause
    "Я устраиваюсь за Евой, усаживаю её к себе на колени и крепко обнимаю."
    eve.c "Ага~ Вот оно что? Приятно~"
    pause
    return

label eveReceiveHug:
    hide eve with dissolve
    show eve hug with dissolve
    pause
    eve.c "М-м~ Сжимаешь меня~"
    eve.c "Мне нравится~"
    return

label eveReceiveKiss:
    hide eve with dissolve
    show eve kiss with dissolve
    eve.c "М-м-м~"
    eve.c "Подними меня~"
    return

label eveInitiatePat:
    show eve smile talk 2 with dissolve
    if(eve.movedIn):
        eve.c "Эй, милый?"
        eve.c "Я была хорошей девочкой~"
    else:
        eve.c "Эй, [mc.name]..."
    "Ева прижимается грудью к моему торсу, и я смотрю сверху на её макушку."
    hide eve with dissolve
    show eve pat animated with dissolve
    pause
    eve.c "М-м-м~ Хе-хе~"
    return

label eveInitiateHug:
    show eve smile talk with dissolve
    eve.c "[mc.name]~"
    hide eve with dissolve
    show eve hug with dissolve
    "Ева бросается мне на грудь и крепко обнимает."
    pause
    if(eve.movedIn):
        eve.c "Люблю тебя, милый."
    else:
        eve.c "М-м~ Такой сильный~"
    return

label eveInitiateKiss:
    show eve joy with dissolve
    if(eve.movedIn):
        eve.c "Милый!"
    else:
        eve.c "[mc.name]!"
    hide eve with dissolve
    show eve kiss with dissolve
    eve.c "М-м~"
    pause
    hide eve with dissolve
    show eve tease talk with dissolve
    eve.c "Не игнорируй меня~"
    return

label eveInitiateSnuggle:
    show eve neutral
    "Я сижу на диване. Ева заходит и замечает меня."
    show eve neutral talk
    eve.c "Сиди там."
    hide eve with dissolve
    show eve snuggle animated with dissolve
    pause
    "Она плюхается ко мне на колени, скрещивает ноги и откидывается на мою грудь."
    eve.c "Обними меня, милый~"
    pause
    return

label eveInitiateHomeSex:
    show eve smile talk
    eve.c "Милый~"
    eve.c "Секс~"
    show eve smile
    return

label eveInitiateHomeSexDeny:
    show eve neutral talk
    eve.c "Э-э...? Почему?"
    return

label eveSeesAffection(affection):
    show eve bashful with dissolve
    "Ева мнётся рядом и косится на нас. Для неё нехарактерно стесняться."
    mc.c "Ну ладно~"
    call expression 'eveReceive' + affection from _call_expression_38
    hide eve with dissolve
    return

label eveInviteOver:
    show eve smile talk
    eve.c "О, да~?"
    return

label eveInitiateInviteOver:
    show eve tease talk
    eve.c "Не хочешь... {i}зависнуть{/i} у тебя дома~?"
    show eve tease
    menu:
        'Yes':
            show eve smile talk
            eve.c "Супер~"
            return True
        'No':
            show eve neutral talk
            eve.c "А... Ладно."
    return False

label eveInviteGoHomeTogether:
    show eve smile talk
    eve.c "Конечно, милый, пошли."
    show eve smile talk 2
    eve.c "Может, чем-нибудь займёмся...?"
    return

label eveInitiateGoHomeTogether:
    show eve tease talk
    eve.c "Эй, милый~ Пойдём домой~"
    show eve tease
    menu:
        'Yes':
            show eve smile talk
            eve.c "Ура~"
            return True
        'No':
            show eve smile talk 2
            eve.c "Без проблем, увидимся дома."
    return False

label eveShowPanties(pantiesIndex = 1):
    show eve neutral talk
    eve.c "Ладно, как хочешь."
    $ renpy.show(eve.apiName + ' panties ' + str(pantiesIndex), tag=eve.apiName)
    with dissolve
    if(pantiesIndex == 1):
        eve.c "Они шли в комплекте с носками."
    elif(pantiesIndex == 2):
        eve.c "Эти мне немного в задницу впиваются."
    elif(pantiesIndex == 3):
        eve.c "Я подумала, тебе понравятся эти~ Ага~"
    return

label eveSendDateText(proposedDate):
    python:
        timeText = {'Morning': 'утром', 'Afternoon': 'днём', 'Evening': 'вечером', 'Night': 'ночью'}.get(proposedDateTime, proposedDateTime.lower())
        locationPhrase = {'beach': 'на пляж', 'park': 'в парк', 'town': 'в город', 'cafe': 'в кафе', 'library': 'в библиотеку', 'diner': 'в закусочную', 'bar': 'в бар', 'aquarium': 'в океанариум', 'theater': 'в театр', 'shop': 'в магазин'}.get(proposedLocation.apiName, 'в «' + _(proposedLocation.name).lower() + '»')
        eve.textChain.append(Message(mc, eve, 'скучно лол', Null, day, timeOfDay))
        eve.textChain.append(Message(mc, eve, 'может, сходим ' + locationPhrase + '? Типа завтра ' + timeText + '?', Null, day, timeOfDay, proposedDate))
    return

label eveGetSelfieOptions:
    $ eveSelfieOptions = []
    if(eveLikeEvent2.unlocked):
        $ eveSelfieOptions.extend(['work1'])
    if(eveHEvent1.unlocked):
        $ eveSelfieOptions.extend(['beach1'])
    if(eveHEvent3.unlocked):
        $ eveSelfieOptions.extend(['changingroom1'])
    if(eveHEvent5.unlocked):
        $ eveSelfieOptions.extend(['bedroom1'])
    # if(eve.movedIn): # TODO
    #     $ eveSelfieOptions.extend(['homekitchen1'])
    return eveSelfieOptions

label eveSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'work1':
                potentialResponses.append({'text': "Сочувствую", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Удачный ракурс", 'statChange': 'love', 'statChangeAmount': 1})
                eve.textChain.append(Message(mc, eve, 'это отстой лол', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'beach1':
                potentialResponses.append({'text': "Отдохни", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Огонь", 'statChange': 'love', 'statChangeAmount': 1})
                eve.textChain.append(Message(mc, eve, 'наконец-то выходной', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'changingroom1':
                potentialResponses.append({'text': "Наверное, тяжело", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Вот это да!", 'statChange': 'love', 'statChangeAmount': 1})
                eve.textChain.append(Message(mc, eve, 'мой размер, повезло-о-о', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom1':
                potentialResponses.append({'text': "ахах", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Безумно горячо", 'statChange': 'love', 'statChangeAmount': 1})
                eve.textChain.append(Message(mc, eve, 'ахах', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homekitchen1':
                potentialResponses.append({'text': "Оденься", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Сейчас накажу...", 'statChange': 'love', 'statChangeAmount': 1})
                eve.textChain.append(Message(mc, eve, 'устроила беспорядок лол', selfieName, day, timeOfDay, responses = potentialResponses))
    return

label eveSexSelect:
    hide screen mainUi
    scene black with fade
    image eve sex waiting = Movie(play="images/characters/eve/hscenes/sexWaiting.webm")
    show eve sex waiting with fade

    call screen eveSexSelectScreen
    if(eveHEvent5.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(eve.movedIn):
            menu eveSleepTogether:
                "Переспать с Евой?"
                'Yes':
                    eve.c "Я и так никуда не собиралась, милый~"
                    eve.c "Обними меня~"
                    call characterSleepover(eve) from _call_characterSleepover_2
                'No':
                    pass
        else:
            menu eveStayTheNight:
                "Пригласить Еву остаться на ночь?"
                'Yes':
                    $ eve.addLove(1)
                    eve.c "Круто~"
                    call characterSleepover(eve) from _call_characterSleepover_3
                'No':
                    eve.c "Было горячо, здоровяк~ Пока~"
    
    call endScene(character = eve, targetLocation = location_home) from _call_endScene_9

screen eveSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(eveHEvent1.unlocked or persistent.debugMode):
                textbutton 'Handjob' keysym str(1):
                    action [Jump('eveHandjob')]
            else:
                textbutton 'Locked'
            if(eveHEvent3.unlocked or persistent.debugMode):
                textbutton 'Shower Boobjob' keysym str(2):
                    action [Jump('eveShowerBoobjob')]
            else:
                textbutton 'Locked'
            if(eveHEvent4.unlocked or persistent.debugMode):
                textbutton 'Couch Missionary' keysym str(3):
                    action [Jump('eveCouchMissionary')]
            else:
                textbutton 'Locked'
            if(eveHEvent4.unlocked or persistent.debugMode):
                textbutton 'Lifting' keysym str(4):
                    action [Jump('eveLifting')]
            else:
                textbutton 'Locked'
            if(eveHEvent5.unlocked or persistent.debugMode):
                textbutton 'Doggy Style' keysym str(5):
                    action [Jump('eveDoggy')]
            else:
                textbutton 'Locked'
            if(eveHEvent5.unlocked or persistent.debugMode):
                textbutton 'Choking Missionary' keysym str(6):
                    action [Jump('eveChokingMissionary')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(7):
                action [Hide('eveSexSelectScreen'), Return()]

label eveSleepover:
    scene evesleepover with fade
    pause
    return

label eveMorningBedInteraction:
    scene evehomemorning with fade 
    pause
    if(eve.movedIn):
        eve.c "М-м~ Доброе утро, милый~"
        eve.c "Не вставай... Просто обними меня~"
    else:
        eve.c "*Зевает*~"
        eve.c "Эй, здоровяк~ Вчера было классно~"
        eve.c "Пока не хочу вставать..."
    return

label eveMorningBedInteractionSex(event):
    # TODO eve morning animation
    return

# Sex scenes
label eveHandjob:
    image eveHandjob1 = Movie(play="images/characters/eve/hscenes/handjob/handjob1.webm")
    scene eveHandjob1 with fade
    pause
    image eveHandjob2 = Movie(play="images/characters/eve/hscenes/handjob/handjob2.webm")
    scene eveHandjob2 with fade
    pause
    image eveHandjob3 = Movie(play="images/characters/eve/hscenes/handjob/handjob3.webm")
    scene eveHandjob3 with fade
    pause
    scene evehandjobfinish1 with fadewhite
    pause
    scene evehandjobfinish2 with fade
    pause
    jump eveSexSelect

label eveShowerBoobjob:
    scene black with fade
    image eveShowerBoobjob1 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part1.webm")
    scene eveShowerBoobjob1 with fade
    pause
    image eveShowerBoobjob2 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part2.webm")
    scene eveShowerBoobjob2 with fade
    pause
    image eveShowerBoobjob3 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part3.webm")
    scene eveShowerBoobjob3 with fade
    pause
    image eveShowerBoobjob4 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part4.webm")
    scene eveShowerBoobjob4 with fade
    pause
    image eveShowerBoobjob5 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part5.webm")
    scene eveShowerBoobjob5 with fade
    pause
    scene eveshowerboobjobfinish1 with fadewhite
    pause
    scene eveshowerboobjobfinish2 with fade
    pause
    jump eveSexSelect

label eveCouchMissionary:
    scene evecouchmissionarystart with fade
    pause
    image eveCouchMissionary1 = Movie(play="images/characters/eve/hscenes/couchMissionary/part1.webm")
    scene eveCouchMissionary1 with fade
    pause
    image eveCouchMissionary2 = Movie(play="images/characters/eve/hscenes/couchMissionary/part2.webm")
    scene eveCouchMissionary2 with fade
    pause
    jump eveSexSelect
    
label eveLifting:
    image eveLiftingFacing1 = Movie(play="images/characters/eve/hscenes/liftingFacing/part1.webm")
    scene eveLiftingFacing1 with fade
    pause
    image eveLiftingFacing2 = Movie(play="images/characters/eve/hscenes/liftingFacing/part2.webm")
    scene eveLiftingFacing2 with fade
    pause
    scene eveliftingfacingfinish1 with fadewhite
    pause
    scene eveliftingfacingfinish2 with fade
    pause
    jump eveSexSelect

label eveDoggy:
    image eveDoggyTease = Movie(play="images/characters/eve/hscenes/doggy/teasing.webm")
    scene eveDoggyTease with fade
    pause
    image eveDoggy1 = Movie(play="images/characters/eve/hscenes/doggy/part1.webm")
    scene eveDoggy1 with fade
    pause
    image eveDoggy2 = Movie(play="images/characters/eve/hscenes/doggy/part2.webm")
    scene eveDoggy2 with fade
    pause
    jump eveSexSelect

label eveChokingMissionary:
    image eveChokingMissionary1 = Movie(play="images/characters/eve/hscenes/chokingMissionary/part1.webm")
    scene eveChokingMissionary1 with fade
    pause
    image eveChokingMissionary2 = Movie(play="images/characters/eve/hscenes/chokingMissionary/part2.webm")
    scene eveChokingMissionary2 with fade
    pause
    scene evechokingmissionaryfinish1 with fadewhite
    pause
    scene evechokingmissionaryfinish2 with fade
    pause
    jump eveSexSelect

# Events
default eveFirstMeetingEvent = Event('First meeting', 'eveFirstMeetingEvent', [eve], 0, 0, [], location_home, ['Evening', 'Night'], triggerDay = 10)
# Known to MC
default eveLikeEvent1 = Event('When lucid', 'eveLikeEvent1', [eve], 0, 0, [eveFirstMeetingEvent], location_home)
# Dateable
default eveLikeEvent2 = Event('New neighbours', 'eveLikeEvent2', [eve], 5, 0, [eveLikeEvent1], location_bar, ['Evening', 'Night'])
# Licking handjob
default eveHEvent1 = Event('Too much to handle', 'eveHEvent1', [eve], 15, 5, [eveLikeEvent2], location_diner, ['Evening', 'Night'])
# Fingering
default eveHEvent2 = Event('Girl at work', 'eveHEvent2', [eve], 25, 10, [eveHEvent1], location_theater)
# Shower boobjob
default eveHEvent3 = Event('Water\'s out', 'eveHEvent3', [eve], 35, 15, [eveHEvent2], location_home, ['Afternoon', 'Evening', 'Night'])
# First sex Lifting
default eveHEvent4 = Event('Make use', 'eveHEvent4', [eve], 45, 20, [eveHEvent3], location_bar)
# Choking / Kiss / Sleepover
default eveHEvent5 = Event('The situation', 'eveHEvent5', [eve], 55, 25, [eveHEvent4], location_home, ['Evening', 'Night'])

label eveFirstMeetingEvent(fromGallery):
    call playMusic(barTheme) from _call_playMusic_38
    scene apartmentshallway with fade
    "Возвращаясь домой, я иду по коридору своего жилого комплекса."
    "Думаю, не начать ли общаться с соседями. Или хотя бы дать им возможность узнать меня."
    "Я видел, как люди входят и выходят из квартир, и встречали они меня по-разному."
    "Кто-то удивлённо замечал нового человека в доме, потом вежливо кивал или здоровался, пытаясь понять, кто я."
    "Но большинство держится особняком. Для современного общества это нормально: у каждого своя жизнь."
    "Если честно, я никогда особо не заводил дружбу с соседями. Раньше я подолгу нигде не задерживался."
    "Но когда подхожу к своему ряду дверей, замечаю незнакомку."
    scene evefirstmeetingi1 with fade
    pause
    "Девушка медленно плетётся к двери неподалёку от моей."
    "Большие уши, длинный тонкий голый хвост, короткая острая мордочка и розовый нос... Похожа на какого-то грызуна. Мышь или крыса?.."
    "Интересно, они обижаются, если перепутать?"
    "В любом случае рост у неё подходящий для обоих вариантов. Худенькая и невысокая, если не считать... двух... внушительных исключений..."
    "Ни хрена себе сиськи. Не хочу пялиться, но, блядь, пропорции у неё вообще сумасшедшие. У мышки?"
    "С маленьким пластиковым пакетом в руке она тянется к ручке; плечи опущены, глаза слипаются."
    "Кажется, она замечает меня и смотрит в мою сторону по коридору."
    "Глаза едва приоткрыты, чтобы разглядеть меня. Она выглядит... уставшей."
    eve_unknown "..."
    eve_unknown "...Э-э?.."
    scene apartmentshallway with fade
    show eve thinking with dissolve
    eve_unknown "Хе~ Плохо дело..."
    call playMusic(funnyTheme) from _call_playMusic_39
    eve_unknown "Галлюцинации... Да пошла эта работа..."
    "Она заметила меня, пробормотала что-то себе под нос и снова отвернулась."
    "Она ухмыляется и вздыхает, слегка пошатываясь и пытаясь повернуть ручку двери."
    mc.c "Э-э, ты в порядке?"
    show eve neutral
    "Она удивлённо оглядывается на меня."
    eve_unknown "...?"
    show eve neutral talk
    eve_unknown "Оно разговаривает... Совсем плохо..."
    eve_unknown "Меня упекут в дурку..."
    show eve neutral
    "Пьяная? Под кайфом? Или просто немного странная? Если она моя соседка, надеюсь, проблем не будет."
    "Похоже, на ней рабочая форма. Может, после длинной смены?"
    mc.c "Прости, но я настоящий."
    eve_unknown "..."
    show eve tease talk
    eve_unknown "Хе~ Здесь нет людей... Давай лучше, мозг..."
    show eve bashful talk
    eve_unknown "Это было бы слишком круто..."
    show eve tease talk
    eve_unknown "Большой... сильный... человек..."
    eve_unknown "Который мог бы поднять меня... Делать со мной что захочет~"
    eve_unknown "А я ничего не смогла бы сделать~"
    show eve tease
    "Господи. Похоже, у неё бред. Может, забуду это."
    mc.c "Э-э..."
    show eve neutral talk
    eve_unknown "В следующий раз придумай что-нибудь поубедительнее..."
    show eve neutral
    "Она снова отворачивается, будто отгоняя меня, ухмыляется и наконец открывает дверь."
    mc.c "Постой..."
    "Она закидывает пакет внутрь и неопределённо машет мне рукой."
    show eve thinking
    eve_unknown "Спокойной... ночи..."
    hide eve with dissolve
    "Она пошатываясь заходит и закрывает за собой дверь."
    "...Что это вообще было?"
    "Она живёт в моём крыле. Наверняка ещё пересечёмся. Буду присматривать за ней..."

    if(not fromGallery):
        $ eve.addLike(1)
    
    return

label eveLikeEvent1(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_40
    scene apartmentshallway with fade
    "Возвращаясь из магазина, я иду по коридорам жилого комплекса."
    "Скучные серые стены без единой детали... Дом даже не такой старый, но выглядит потрёпанным."
    "Хоть внутри квартиры уютные."
    "Проходя мимо, слышу, как за спиной открывается соседняя дверь. Ну вот, сейчас будет неловкое знакомство..."
    "Я оглядываюсь и вижу..."
    show eve neutral with dissolve
    "Ого, да это та самая грызунья."
    "Значит, в тот день она заходила именно в эту дверь... Странная была ситуация — она явно была не в себе, по какой-то причине."
    "Интересно, сегодня она будет такой же?"
    "Закрыв дверь, она смотрит на меня."
    eve_unknown "..."
    mc.c "..."
    "Она оборачивается ещё раз, будто только сейчас меня заметила."
    eve_unknown "..."
    show eve thinking
    eve_unknown "Хм..."
    mc.c "Привет."
    show eve neutral
    eve_unknown "..."
    show eve neutral talk
    eve_unknown "Эй..."
    show eve neutral
    "Мы молча стоим. Она разглядывает меня с ног до головы."
    show eve neutral talk
    eve_unknown "Мы... знакомы?"
    show eve neutral
    mc.c "Мы встречались на днях, здесь. Ты как раз заходила к себе."
    show eve thinking
    eve_unknown "Хм-м... Правда?.."
    eve_unknown "Что-то знакомое..."
    mc.c "Ну, толком мы не познакомились. Ты была совсем не в себе."
    show eve neutral talk
    eve_unknown "Не в себе?.."
    show eve neutral
    mc.c "Да, ты меня увидела и, похоже, решила, что галлюцинируешь."
    mc.c "Наверное, устала или что-то такое. Бормотала себе под нос и, кажется, не думала, что я настоящий."
    show eve thinking
    eve_unknown "Хм..."
    "Она хмурится, но вдруг, кажется, что-то вспоминает."
    show eve surprise
    eve_unknown "Погоди... Тот человек?.."
    mc.c "Э-э, да, наверное."
    eve_unknown "Ты... там был?"
    eve_unknown "Кто ты? Почему... ты здесь?"
    mc.c "Я здесь живу."
    "Я указываю на свою дверь."
    show eve neutral talk
    eve_unknown "Э-э-э~? С каких пор?"
    show eve neutral
    mc.c "Недавно. Только переехал в город."
    mc.c "Я [mc.name]. Прости, тогда не представился. Ты была вымотана."
    show eve neutral talk
    eve.c "Э-э... Ева. Я здесь живу..."
    show eve thinking
    eve.c "Значит, ты и правда существуешь... Хм..."
    mc.c "Вроде того."
    show eve bashful talk
    eve.c "Сорян... Работы много... Еле домой доползла... Не ожидала..."
    eve.c "Я странно себя вела?.."
    show eve bashful
    mc.c "Ты смеялась сама с собой, бормотала, будто не верила, что я настоящий. И ещё сказала: «Да пошла эта работа»."
    "Остальное не буду упоминать, раз она толком не помнит. Не нужно лишний раз напоминать."
    show eve neutral talk
    eve.c "Хе~ Ну, это на меня похоже..."
    show eve thinking
    eve.c "Хорошо... А то я подумала, что..."
    "На секунду она смущённо отводит взгляд, но потом немного расслабляется."
    show eve smile talk
    eve.c "Тут нечасто встретишь людей..."
    show eve smile
    mc.c "Я сюда по работе переехал. Взял бар в конце улицы. Знаешь тот обшарпанный? Раньше им владел другой человек."
    show eve neutral talk
    eve.c "А, кажется, знаю... Помню одного..."
    eve.c "Он ведь был уже пожилой?"
    show eve smile talk
    eve.c "Не то что ты, ты такой~"
    show eve thinking
    eve.c "Кхм... Я хотела сказать..."
    show eve neutral talk
    eve.c "Что значит «взял»?.."
    show eve neutral
    mc.c "Терри вышел на пенсию и продавал заведение. Он был знаком с моим бывшим начальником, а я раньше работал в баре, вот он и дал мне шанс."
    show eve smile talk
    eve.c "Э-э-э~? То есть ты типа владеешь всем баром?"
    show eve smile
    mc.c "Ага. Пока осваиваюсь, если честно."
    show eve tease talk
    eve.c "Ничего себе~ Наверное, ты теперь богатый и всё такое~"
    show eve tease
    mc.c "Да я просто свожу концы с концами. Сейчас пабам трудно приносить прибыль, но пока дела идут неплохо."
    show eve tease talk
    eve.c "Твоя квартира намного больше, да?"
    show eve smile talk 2
    eve.c "А у меня одна комната... в секции для нищебродов, ха-ха~"
    show eve smile
    mc.c "Да, повезло. Я переехал сюда, даже не видя квартиру заранее."
    mc.c "А ты кем работаешь?"
    show eve neutral talk
    eve.c "В кинотеатре."
    eve.c "Ничего особенного. Работа отстой."
    show eve thinking
    eve.c "Пришлось подменять коллегу... Вот почему я тогда была... такой..."
    mc.c "Не переживай. Рад, что сейчас мы познакомились, когда ты немного пришла в себя."
    show eve smile talk
    eve.c "Хе-хе, да..."
    show eve smile
    "Она смотрит на телефон."
    show eve sad talk
    eve.c "Блин... Мне пора..."
    show eve sad
    mc.c "Извини, не хотел задерживать."
    show eve smile talk
    eve.c "Ничего, я часто опаздываю..."
    show eve tease talk
    eve.c "Можешь задерживать меня {i}когда угодно~{/i}"
    show eve tease
    "..."
    "Это была шутка? Забавная она всё-таки."
    mc.c "Удачи. Как-нибудь загляни в бар, угощу новую соседку выпивкой."
    show eve smile talk
    eve.c "О-о~? Э-э... может быть..."
    show eve smile talk 2
    eve.c "Ну... увидимся, [mc.name]~"
    hide eve with dissolve
    "Она ухмыляется и не спеша идёт по коридору."
    "Любопытно... Рад, что она всё-таки нормальнее, чем при нашей первой встрече. Не хотелось бы иметь чокнутую соседку."
    "Вообще она вроде милая. Интересно, воспользуется ли она моим приглашением?"

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.knownToMC = True
    
    return

label eveLikeEvent2(fromGallery):
    call playMusic(barTheme) from _call_playMusic_41
    $ location_bar.showBackground()
    "Вот и [_(timeOfDay)] — я снова на смене."
    "Обычный вечер: кто-то из постоянных и случайных посетителей. Я уже запоминаю местные лица."
    "Открывается дверь, и заходит один из новых посетителей."
    show eve neutral with dissolve
    "В дверном проёме виднеется маленькая фигурка. Это моя соседка Ева."
    "Она нерешительно заходит, оглядывается и замечает меня."
    show eve smile
    "Её лицо чуть светлеет, и она медленно ковыляет ко мне."
    mc.c "Эй, Ева! Добро пожаловать!"
    "Она подходит к стойке, и её грудь комично едва-едва выглядывает над краем."
    show eve neutral talk
    eve.c "Йо... Только что со смены."
    eve.c "Ты говорил... угостишь выпивкой...?"
    show eve neutral
    mc.c "Конечно! Рад, что пришла."
    mc.c "Что тебе налить?"
    show eve smile talk
    eve.c "Хе... Э-э... Сидр есть?"
    show eve smile
    mc.c "Яблочный или фруктовый?"
    show eve smile talk
    eve.c "Хе~ Тогда фруктовый."
    show eve smile
    mc.c "Сейчас принесу. Можешь пока присесть."
    show eve smile
    eve.c "М-м."
    "Она забирается на барный стул чуть сложнее, чем можно ожидать, и почти не становится выше."
    "Я ставлю перед ней напиток, и она делает маленький глоток."
    show eve thinking
    eve.c "Фух~"
    mc.c "Как работа? Тяжёлый день?"
    show eve neutral talk
    eve.c "Э-э... Типа того... Обычный..."
    show eve thinking
    eve.c "Не хочу тебя утомлять... Всё как всегда, ничего интересного..."
    show eve neutral talk
    eve.c "Мне больше интересно узнать про твоё заведение. Классное место."
    show eve neutral
    mc.c "Спасибо. Я ещё привыкаю, да и ремонт требовался, но вроде дела идут неплохо."
    show eve neutral talk
    eve.c "Я тут бывала... Давно. В последнее время времени не было..."
    eve.c "Кажется, кое-кто из моих знакомых сюда иногда заглядывает."
    show eve neutral
    mc.c "Наверное, ты не приходила с тех пор, как я тут работаю. В доме я бы тебя сразу узнал."
    show eve smile talk 2
    eve.c "Э-э~? Меня~?"
    show eve smile
    "Сам не знаю, зачем это сказал, но, если честно, её фигуру трудно не запомнить..."
    mc.c "Я просто стараюсь познакомиться с посетителями, понимаешь?"
    mc.c "Я здесь чужой, откуда я родом почти нет антропоморфов, так что стараюсь запоминать людей."
    show eve smile talk
    eve.c "Да и у нас вас нечасто встретишь~"
    show eve smile
    mc.c "Вот именно. Хочу подружиться с местными и завсегдатаями, чтобы они знали: я не собираюсь угробить это место."
    mc.c "Я новый человек в городе и забрал у местных их заведение. Не хочу никого задевать, понимаешь?"
    show eve smile talk
    eve.c "Ну, я не жалуюсь~ Аха~"
    show eve smile
    "Она прищуривается и хитро улыбается. В её словах есть что-то забавное."
    "Списываю это на странное знакомство. Это просто неловкие шутки или что-то другое?"
    "К стойке подходит другой посетитель. Нельзя забывать, что я всё ещё на работе."
    mc.c "Извини, Ева, я вернусь, когда закончу с другими клиентами, ладно?"
    show eve neutral talk
    eve.c "Ладно..."
    scene black with fade
    "Ева остаётся ещё ненадолго, а короткие всплески работы прерывают наши разговоры."
    "Она выпивает ещё и время от времени болтает со мной."
    "Понемногу узнаю о ней. Пока ничего слишком личного: работа, квартира, бар..."
    "Она не особо разговорчивая, но приятная компания."
    $ location_bar.showBackground()
    show eve smile with dissolve
    "Проходит пара часов, уже поздно, а она всё ещё не ушла."
    "Жаль, что я не мог уделить ей всё внимание. Она забавная."
    mc.c "Ещё одну?"
    show eve smile talk 2
    eve.c "Э-э~ Стоит~?"
    show eve smile talk
    eve.c "Но... Не, хватит. Я уже наотдыхалась."
    show eve smile
    "Она стала мягче и раскрепощённее, может, слегка захмелела. Такая маленькая — алкоголь, наверное, быстро на неё действует."
    show eve tease talk
    eve.c "Я обычно не пью. Но иногда... становлюсь немного... игривой~"
    show eve tease
    "Игривой? Не могу представить. Она такая спокойная, неторопливая девушка."
    "Она естественно прижимается пышной грудью к барной стойке, которая почти достаёт ей до груди."
    "Я забираю последний бокал, чтобы вымыть. Она смотрит на меня с лёгкой улыбкой."
    show eve smile talk
    eve.c "Тебе нравятся пушистые жители?"
    show eve smile
    mc.c "Прости?"
    show eve smile talk 2
    eve.c "Хе~ Ну, эти антро вокруг тебя. Странные? Пугают? Или {i}интересуют~{/i}?"
    show eve smile
    mc.c "Ха, нет, не пугают. Сначала всё было немного неожиданно, но большинство встреченных мной людей отнеслись ко мне нормально."
    mc.c "Я всё ещё привыкаю к разным видам."
    show eve tease talk
    eve.c "Есть любимчики~?"
    show eve tease
    "Не совсем понимаю, к чему она клонит. В её голосе чувствуется озорство... Может, дразнит меня."
    mc.c "Да нет, все довольно интересные. Почти каждый день встречаю кого-то нового."
    show eve thinking
    eve.c "Хм..."
    "Кажется, мой ответ её немного разочаровал. Она чего-то ждала?"
    show eve smile talk
    eve.c "Ладно, я пойду. Спасибо за вечер."
    show eve smile
    mc.c "Мне было приятно. Заходи в любое время."
    show eve smile talk
    eve.c "Может, зайду~"
    show eve thinking
    eve.c "Хм..."
    call stopMusic from _call_stopMusic_4
    show eve neutral talk
    eve.c "Это было свидание~?"
    show eve neutral
    call playMusic(chillTheme) from _call_playMusic_42
    "Вот так она меня озадачила. Хм... а было ли?"
    "Вряд ли. Я пригласил её как новую знакомую, тем более мы соседи. После нашей странной первой встречи она показалась милой."
    "Мы приятно поговорили, но я всё время работал и не мог уделить ей всё внимание."
    "Кажется, я ей нравлюсь... Она ведь всё-таки пришла. Думаю, мы хорошо провели время."
    "Она немного со мной флиртовала, да? И последнее замечание — точно {i}намёк{/i}..."
    "Она... интересная. И милая. Я точно хочу увидеться снова."
    mc.c "Извини, наверное, это не совсем было свидание. Я всё время работал и не знал, когда ты придёшь."
    show eve neutral talk
    eve.c "А, ладно... Я ведь сама просто зашла."
    show eve neutral
    "Она немного расстроилась? Пора рискнуть."
    mc.c "Но... Может, я заглажу вину и приглашу тебя на настоящее свидание как-нибудь?"
    show eve smile
    "Её лицо немного светлеет."
    show eve smile talk
    eve.c "Ха-ха~ Не знаю, а получится~?"
    eve.c "С такой маленькой мышкой, как я~?"
    show eve smile
    "Вот эта её забавная манера..."
    mc.c "Может, кофе? Или как-нибудь пообедаем? Или снова выпьем?"
    show eve smile talk 2
    eve.c "И это всё~?"
    show eve smile
    "Что это значит?"
    show eve smile talk
    eve.c "Дай мне свой номер~"
    show eve smile
    "Я протягиваю ей телефон, она вбивает свои контакты и хитро улыбается."
    "Она спрыгивает со стула и подмигивает мне."
    show eve smile talk
    eve.c "Пока, здоровяк~"
    show eve smile
    hide eve with dissolve
    "Ну, вроде неплохо. Она хочет как-нибудь сходить со мной."
    "Я пока не до конца её понял, но интерес у неё точно есть."

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.addLove(1)
        $ eve.blockedLocations.remove(location_bar)
        $ eve.isDateable = True
        "Теперь ты можешь приглашать Еву на свидания."

    return

label eveHEvent1(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_43
    $ location_diner.showBackground()
    show eve neutral with dissolve
    "Ева согласилась сходить со мной поужинать."
    "Ужин — довольно серьёзное приглашение для такого раннего этапа, но не думаю, что она будет против. Пока она кажется лёгкой на подъём и беззаботной."
    "Мы уже несколько раз пересекались, в том числе на паре свиданий — если их можно так назвать. Пока всё легко и непринуждённо."
    "Я всё ещё не до конца её раскусил. Не понимаю, это у неё такое чувство юмора или за ним что-то скрывается."
    "Она тихая и расслабленная, но под этим чувствуется лёгкий флирт..."
    "Стараюсь не торопить события, но между нами что-то назревает."
    "Даже если останемся просто друзьями, тоже неплохо. Будет милая соседка."
    "Мы встретились после её смены."
    show eve smile talk
    eve.c "М-м... Вкусно."
    show eve smile
    "Она жадно уплетает жирный фастфуд. Выбрала обычную закусочную, она не привередливая."
    "Ей хватает простых радостей."
    mc.c "Ничего себе, ты быстро управилась."
    show eve thinking
    eve.c "Хм... Я проголодалась."
    eve.c "Работа... Мф... Долгая..."
    mc.c "Ха, ладно. Но куда всё это помещается? Ты же такая маленькая."
    show eve smile talk 2
    eve.c "В сиськи."
    show eve smile
    "О. Это она сказала, не я."
    "Она поднимает взгляд и ухмыляется."
    show eve smile talk
    eve.c "Что? Я же вижу, как ты пялишься."
    show eve smile
    mc.c "Нет, я..."
    "Я ведь и правда пялился..."
    show eve neutral talk
    eve.c "Расслабься... Всё нормально."
    show eve smile talk 2
    eve.c "Знаю, парням такое нравится..."
    show eve bashful talk
    eve.c "Только спина от них болит..."
    show eve bashful
    mc.c "Спина болит?"
    show eve smile talk
    eve.c "Хе~ Ага."
    show eve smile talk 2
    eve.c "Мне бы такие бёдра или что-нибудь в этом духе..."
    show eve smile
    "Ладно, мы просто непринуждённо обсуждаем её сиськи... Она совсем не стесняется."
    "Фигура у неё и правда что надо... Настоящая пышечка."
    "Я уже привыкаю к телам антро... Но она определённо из самых экстремальных."
    "Не то чтобы меня это отталкивало..."
    "Мы доедаем и собираемся домой."
    mc.c "Я за это заплачу."
    show eve neutral talk
    eve.c "Уверен? Я не заставляю..."
    show eve neutral
    mc.c "Да ладно, всё нормально. Я же пригласил."
    show eve smile talk
    eve.c "Мило... До зарплаты ещё неделя, так что... сам понимаешь..."
    show eve tease talk
    eve.c "Спасибо, богач~"
    show eve tease
    mc.c "Я не богач... Просто бизнес пока кое-как держится на плаву... Расходов куча, знаешь ли..."
    show eve tease talk
    eve.c "Бедненький~"
    show eve smile talk
    eve.c "Но... спасибо. Как-нибудь я угощу тебя."
    show eve smile
    $ location_town.showBackground()
    "Мы выходим на улицу в воздух [_(timeOfDay)]. Уже позднее, чем я думал."
    show eve neutral with dissolve
    mc.c "Домой, да?"
    show eve neutral talk
    eve.c "Ага, пока."
    hide eve with dissolve
    "Она разворачивается и уходит. Она знает, что мы живём рядом?.."
    mc.c "Э-э... Ева."
    show eve smile talk with dissolve
    eve.c "Шучу~"
    show eve smile talk
    eve.c "Пошли."
    show eve smile
    "Ну и девушка..."
    scene black with fade
    "Мы вместе идём к своим квартирам, перебрасываясь пустяками."
    "Из-за её коротких шажков путь занимает чуть больше времени."
    scene apartmentshallway with fade
    "Подойдя к дверям, мы останавливаемся."
    show eve neutral with dissolve
    mc.c "Спасибо за сегодня, мне понравилось."
    show eve smile talk 2
    eve.c "М-м. Мне тоже."
    show eve smile
    mc.c "Ты свободна на этой неделе?"
    show eve thinking
    eve.c "Хм... Наверное... Несколько смен..."
    mc.c "Тогда я тебе напишу."
    show eve neutral talk
    eve.c "Ладно..."
    show eve neutral
    "Настроение понемногу рассеивается. Мы неловко топчемся на месте. Может, я всё не так понял?"
    "Ева стоит рядом и смотрит на меня."
    call stopMusic from _call_stopMusic_5
    show eve neutral talk
    eve.c "Ты меня не пригласишь?"
    show eve neutral
    "О... Я не был уверен... Не хотел давить."
    mc.c "А, конечно, заходи, если хочешь!"
    mc.c "Не хотел ничего предполагать..."
    call playMusic(barTheme) from _call_playMusic_44
    show eve smile talk
    eve.c "Предполагать что~?"
    show eve smile
    "А... Она меня подловила."
    "Я совсем растерялся. Она просто играет со мной?"
    mc.c "Ладно... Заходи."
    "Я открываю дверь, и мы входим."
    $ location_home_bedroom.showBackground()
    "Сняв обувь, мы заходим внутрь, и Ева сразу начинает оглядываться."
    show eve surprise with dissolve
    eve.c "Ничего себе~"
    eve.c "Тут намного просторнее..."
    "Ева удивлённо оглядывает комнаты, заглядывая в них, пока я провожу ей экскурсию."
    mc.c "Ага... Как я и говорил, мне повезло. До переезда у меня здесь вообще не было знакомых."
    show eve smile talk
    eve.c "Круто... Хорошее место."
    show eve smile
    mc.c "Выпить?"
    eve.c "М-м."
    "Я достаю из холодильника пару банок. Мы направляемся к дивану, но Ева остаётся стоять и разглядывать комнату."
    show eve neutral talk
    eve.c "Эй, [mc.name]."
    call stopMusic from _call_stopMusic_6
    eve.c "...Ты встречаешься с антро?"
    show eve neutral
    "Э-э... Интересный вопрос. Она проверяет, встречаюсь ли я вообще с кем-нибудь?"
    "Или спрашивает, интересна ли ей мне именно в этом смысле..."
    "Если первое, вопрос вполне резонный. Мы только познакомились, это ожидаемо, да? Я даже не уверен, что мы встречаемся."
    "Скажу честно."
    mc.c "Да, бывало."
    show eve smile talk
    eve.c "Ого~?"
    show eve smile
    mc.c "Я недавно переехал, никого здесь не знаю и пытаюсь познакомиться с людьми, прощупываю почву, понимаешь?"
    mc.c "Прости. Я не знал, серьёзно ли у нас всё. Если хочешь, я—"
    show eve tease talk
    eve.c "Любитель пушистых~"
    show eve tease
    mc.c "А?"
    show eve tease talk
    eve.c "Извращенец по пушистикам~"
    show eve tease
    "Она громко смеётся и ухмыляется, почти издеваясь надо мной. Забавно, что она смотрит на меня снизу вверх."
    show eve smile talk 2
    eve.c "Какие тебе нравятся? Большие? Маленькие? Пушистые~? Чешуйчатые~?"
    show eve smile
    mc.c "Э-э..."
    "Она смеётся мне прямо в лицо. Ну, скорее, в грудь..."
    show eve smile talk
    eve.c "Ладно, теперь знаю~"
    eve.c "Значит, ты не просто из вежливости со мной общаешься~"
    show eve smile
    mc.c "Я... э-э..."
    "Что происходит? Чего она добивается?"
    "Пытается понять, нравится ли мне? Или просто водит меня за нос?"
    "Наверное, у меня сейчас растерянное и напряжённое лицо. Она смотрит на меня и немного успокаивается."
    show eve smile talk
    eve.c "Расслабься... Просто спросила..."
    show eve smile
    "Ева подходит ко мне и тянется, чтобы заглянуть в лицо."
    call playMusic(sexyTheme) from _call_playMusic_45
    scene evehevent1i1 with fade
    pause
    "Она кладёт маленькую ладонь мне на пояс."
    eve.c "Эй, спасибо за ужин..."
    eve.c "Позволишь мне... отблагодарить тебя?"
    "По виску скатывается капля пота. Её рука медленно скользит и задевает мой член."
    mc.c "Я ничего не жду..."
    eve.c "Позволь мне~ К тому же..."
    eve.c "Хочу узнать, каково это."
    mc.c "Каково что?"
    eve.c "Член человека."
    "Я теряюсь и не знаю, что ответить."
    "Она легонько поглаживает мой член сквозь штаны. Он твердеет..."
    eve.c "Ага~ Чувствую~"
    eve.c "Дай посмотреть~"
    scene evehevent1i2 with fade
    pause
    "Я не возражаю, и ей даже не приходится приседать. Она расстёгивает ширинку, и мой член вываливается из штанов."
    eve.c "Ух ты..."
    "Ева с похотливым восхищением разглядывает мой член. Почти облизываясь, она широко раскрывает глаза и ухмыляется мне."
    eve.c "Чёрт~"
    eve.c "Ты и правда {i}большой парень~{/i}"
    image eveHandjob1 = Movie(play="images/characters/eve/hscenes/handjob/handjob1.webm")
    scene eveHandjob1 with fade
    pause
    "Она нерешительно протягивает руку и осторожно берёт мой член."
    "Её пальцы медленно скользят вверх-вниз, и приятная дрожь пробегает по всему телу."
    eve.c "Вот это будет..."
    eve.c "Эй, ты уже трахал антро~?"
    mc.c "Я... э-э..."
    eve.c "Уверена, тебе хочется~"
    "Она опирается маленькой ладонью мне на пояс и медленно водит мягкой стороной пальцев по члену."
    eve.c "Я вообще-то собиралась отсосать тебе, но, блядь..."
    "Ничего себе... Она такая похотливая. Дрочит мне и чуть ли не пускает слюни."
    eve.c "Не знаю... Он слишком большой~"
    image eveHandjob2 = Movie(play="images/characters/eve/hscenes/handjob/handjob2.webm")
    scene eveHandjob2 with fade
    pause
    eve.c "Я не могу взять его в рот~"
    "Она слегка приседает и подносит кончик своей маленькой мордочки к головке моего члена."
    "Она трётся губами о головку, быстрее дрочит мне и щекочет её своей шерстью."
    eve.c "М-м~ Такой твёрдый~"
    eve.c "Чёрт, он меня порвёт~"
    eve.c "М-м-м~"
    "Господи... Она совсем разошлась. От каждого её слова я вздрагиваю."
    "Она высовывает язык, проводит им по нижней стороне головки и трётся ртом о мой член."
    "Выступает предэякулят, и она размазывает его языком."
    mc.c "Блядь... Ева..."
    eve.c "М-м~"
    image eveHandjob3 = Movie(play="images/characters/eve/hscenes/handjob/handjob3.webm")
    scene eveHandjob3 with fade
    pause
    "Она обхватывает мой член и второй рукой, ускоряя дрочку и крепче сжимая ствол."
    "Её руки двигаются всё энергичнее, она старается обработать всю длину."
    eve.c "Такой большой~ Такой толстый~"
    eve.c "Он почти размером с мою голову~"
    eve.c "Ты мог бы прижать меня к кровати~ Я бы ничего не смогла сделать~"
    eve.c "О боже~"
    "Её маленькие пальцы танцуют по моему члену, сжимают и проворачивают его, сводя меня с ума."
    "Я чувствую, как удовольствие нарастает..."
    mc.c "Ах... Я сейчас кончу."
    eve.c "Можешь~ Прямо мне на лицо~"
    scene evehandjobfinish1 with fadewhite
    pause
    "Она крепко сжимает мой член маленькими ладонями, и я бурно кончаю ей на лицо."
    eve.c "А-а-а~"
    "Она смотрит мне в глаза и открывает рот, позволяя густым струям покрыть лицо и язык."
    scene evehandjobfinish2 with fade
    pause
    "Из меня вырывается ещё несколько мощных струй; член дрожит от экстаза."
    "Её лицо всё в моей сперме, она тяжело дышит и довольно улыбается, глядя на результат."
    eve.c "Чёрт возьми... Сколько же её~"
    mc.c "Боже мой..."
    eve.c "Похоже, тебе понравилось~"
    mc.c "Ещё бы."
    eve.c "Ага~"
    $ location_home_bedroom.showBackground()
    "Ева вытирает лицо салфетками. Я тоже привожу себя в порядок и убираю член."
    show eve smile with dissolve
    "Ева улыбается мне как обычно, будто произошедшее её совсем не смутило."
    "Я не знаю, что сказать... Совершенно не ожидал такого сегодня. И что теперь?"
    show eve thinking
    eve.c "Хм..."
    show eve neutral talk
    eve.c "Я устала... Пойду домой."
    show eve neutral
    "О боже, неужели она жалеет?"
    show eve smile talk
    eve.c "Но за ужин спасибо. Мне понравилось."
    show eve smile
    "У нас... всё нормально?"
    show eve smile talk 2
    eve.c "Пока, здоровяк~"
    show eve smile
    mc.c "А... ну ладно..."
    hide eve with dissolve
    "И вот так Ева уверенно выходит в коридор."
    "Ни хрена себе..."
    "Не ожидал такого. Она просто дикая. И я всё ещё не понимаю, кто мы друг другу..."
    "С ней будет непросто."

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.addLove(1)

    return

label eveHEvent2(fromGallery):
    call playMusic(barTheme) from _call_playMusic_46
    $ location_town.showBackground()
    "Идя через город, я оказываюсь у кинотеатра."
    "Сразу вспоминаю Еву."
    "Мы уже несколько раз куда-то ходили, но я не совсем понимаю, кто мы друг другу."
    "Всё-таки мы поели, а потом она практически {i}сама{/i} пригласила себя ко мне и подрочила мне. А её слова..."
    "Я думал, после этого будет неловко, но ничего подобного."
    "Она всё такая же забавная и расслабленная. Немного флиртует, но она всегда такая."
    "Так что я продолжаю с ней видеться. Для меня это свидания, но считает ли она нас просто случайной интрижкой? Меня бы это не смутило, но..."
    "Интересно, неужели это всё, что между нами было? Весёлое развлечение для соседей."
    "Раз уж я здесь, стало любопытно..."
    $ location_theater.showBackground()
    "Я захожу внутрь и оглядываюсь."
    "Несколько человек прохаживаются по холлу, но сейчас не особо людно."
    "Осматриваясь, замечаю нашу девочку за стойкой. Она обмякла и выглядит до смерти скучающей."
    show eve thinking with dissolve
    "Решаю подойти поздороваться. Она едва замечает, что я рядом."
    "Моя тень падает на стойку, и это наконец заставляет её пошевелиться."
    eve.c "{b}*Вздох*~{/b} Добро пожаловать. Чем могу вам {i}служить{/i}..."
    show eve neutral
    "Наконец она поворачивается и смотрит на меня."
    eve.c "Хм?"
    call playMusic(funnyTheme) from _call_playMusic_47
    show eve smile talk
    eve.c "А, это всего лишь ты."
    show eve smile
    mc.c "Ой. «Всего лишь я»?"
    show eve smile talk
    eve.c "Хе~"
    show eve thinking
    eve.c "То есть, блядь. Ещё один клиент — и я бы сдохла..."
    mc.c "Что случилось?"
    show eve neutral talk
    eve.c "Да ничего... Всё та же хрень."
    show eve thinking
    eve.c "Просто устала..."
    show eve smile talk
    eve.c "Хоть ты меня немного развлекаешь."
    eve.c "Или пришёл надо мной поиздеваться?"
    show eve smile
    mc.c "Проходил мимо, решил заглянуть — проверить, такая ли ты тут несчастная, как рассказываешь."
    show eve smile talk
    eve.c "Хе~ Ну вот, полюбуйся на всю эту красоту."
    show eve thinking
    eve.c "Дыра дырой."
    mc.c "Что-нибудь хорошее показывают?"
    show eve neutral talk
    eve.c "Не-а. Уже несколько недель ничего не меняется."
    eve.c "{i}Может быть{/i}, раз в пару месяцев покажут что-то стоящее..."
    show eve neutral
    mc.c "Ты так говоришь. Ты всё уже видела? Не суди книгу по обложке..."
    show eve neutral talk
    eve.c "Почти всё. Когда прячусь на пару часов и делаю вид, что «убираюсь»."
    show eve neutral
    "Я смотрю на афишу. Она не внушает доверия. Сейчас столько отстоя... Но пара фильмов выделяется."
    mc.c "А как насчёт {i}«Фургартхи»{/i}? Ты смотрела?"
    show eve neutral talk
    eve.c "...Нет. {i}Этот{/i} хотя бы новый..."
    show eve neutral
    mc.c "Может, он хороший? Сможешь улизнуть на сеанс?"
    show eve smile talk
    eve.c "Ага~ Не думала, что ты на такое способен, здоровяк."
    show eve smile talk 2
    eve.c "Начальника сегодня нет, так что ладно. Мне всё равно надо отсюда выбраться~"
    scene black with fade
    "Ева с энтузиазмом, которого я от неё почти не видел, бросает работу, и мы идём в зал."
    "Я всё-таки уговариваю её позволить мне купить билет. И без того втягиваю её в шалости..."
    "Мы проскальзываем в зал, как раз начинается сеанс."
    call playMusic(barTheme) from _call_playMusic_48
    scene evehevent2i1 with fade
    pause
    "Мы устраиваемся в тёмном углу почти пустого зала — Ева выбрала самые дальние места."
    "Фильм оказывается приятным сюрпризом."
    "История одинокого мужчины-человека среди антропоморфных зверей. Ну надо же, какое совпадение."
    "Однажды главный герой просыпается и решает, что все вокруг превратились в антро."
    "Когда сюжет раскрывается, Ева толкает меня локтем и ухмыляется."
    eve.c "Понятно... Ты специально это выбрал~"
    mc.c "Честно, я не знал! Просто повезло."
    mc.c "Но ведь неплохо, правда?"
    eve.c "Ладно, да. Неплохо."
    "Постепенно фильм становится... довольно откровенным."
    "Между героями завязывается роман, который вскоре разгорается."
    mc.c "Такое днём показывать можно?"
    eve.c "Для этого и нужны возрастные рейтинги. Если не забываю на них посмотреть..."
    "На экране разыгрывается почти откровенная секс-сцена между главным героем и лисицей-антро."
    scene evehevent2i2 with dissolve
    "Ева ухмыляется и наклоняется ко мне."
    eve.c "Тебе такое нравится, да~?"
    "Не буду врать, нравится. Но я не ожидал увидеть такое во время внезапного похода в кино."
    mc.c "Поймала. Хотя я не планировал..."
    eve.c "Ого~ Понятно~"
    "Она тихонько фыркает."
    call stopMusic from _call_stopMusic_7
    eve.c "Могу снова тебе подрочить~"
    "...Вот это внезапно. Она совсем не стесняется."
    "После прошлого раза я уже понял: секса она не стыдится. Даже если я не уверен, что мы пара или вообще по-настоящему встречаемся."
    "Друзья с привилегиями...? Что-то вроде того?"
    mc.c "Ты что тут... Собираешься...?"
    eve.c "Мы сидим сзади, никто не смотрит."
    eve.c "Я знаю, что тебе хочется~"
    "Ну и проказница... Перспектива заманчивая, но устраивать беспорядок в общественном месте мне не хочется..."
    "Вместо этого я думаю, что всё ещё должен отплатить ей за прошлый раз..."
    mc.c "Хм... А если вот так?"
    call playMusic(sexyTheme) from _call_playMusic_49
    image eve theater fingering 1 = Movie(play="images/characters/eve/hscenes/theaterFingering/part1.webm")
    show eve theater fingering 1 with fade
    pause
    "Я протягиваю руку между её ног и забираюсь под юбку."
    eve.c "Ч-что?"
    "Я касаюсь пальцем ткани её трусиков. Ева вздрагивает на сиденье."
    eve.c "Ты... эй..."
    mc.c "Тс-с~ Фильм же идёт."
    "Через трусики чувствую её маленькую щёлку. Между ног у неё тепло."
    "Она ёрзает, но не пытается оттолкнуть мою руку."
    eve.c "Хм~"
    eve.c "Так ты тоже... умеешь развлекаться, да?"
    mc.c "Кажется, тебе полагается небольшая расплата..."
    "Она не сопротивляется, а откидывается на спинку, слегка раздвигает ноги и наслаждается ласками."
    eve.c "Хе~ М-м~ Приятно~"
    "На экране становится жарче: наш герой вовсю обрабатывает женщину-антро."
    "Мы оба смотрим вперёд. Я чувствую, как трусики у неё намокают..."
    image eve theater fingering 2 = Movie(play="images/characters/eve/hscenes/theaterFingering/part2.webm")
    show eve theater fingering 2 with fade
    pause
    "Я отодвигаю тонкую ткань и провожу пальцами вверх-вниз по её голой щёлке."
    eve.c "М-м~ Хм-м~"
    "Она почти никак не реагирует, только тихонько постанывает. Полностью позволяет мне это делать."
    "Мягкие пушистые губки обрамляют горячую влажную пизду; её вход слегка подрагивает, пока я дразню её."
    "Жаль, что не могу увидеть её лицо, но ощущения восхитительные. Мягкая, но тугая киска с пухлыми губами~"
    eve.c "М-м~ Блядь~"
    "Она тихонько стонет. Рядом никого нет, но сдержать эти маленькие стоны она не может."
    "Она не отрывает взгляда от эротической сцены и глубже сползает на сиденье, приглашая меня прижать руку к ней."
    "Она подёргивает ногами, пока я скольжу по её складкам и слегка ввожу палец внутрь."
    eve.c "А-а~ Вот так~ Блядь~"
    eve.c "...Ещё..."
    "Кто я такой, чтобы отказать? Она сама хотела устроить шалости — получай..."
    image eve theater fingering 3 = Movie(play="images/characters/eve/hscenes/theaterFingering/part3.webm")
    show eve theater fingering 3 with fade
    pause
    "Я ввожу два пальца, и Ева слегка подпрыгивает."
    eve.c "А-а-а~!"
    eve.c "Б-блядь~"
    "Я ритмично двигаю пальцами туда-сюда в её тугой, истекающей соками киске."
    "Она впивается коготками в меня, а её тугие внутренние мышцы пульсируют вокруг моих пальцев, пока она извивается на сиденье."
    eve.c "М-м~ М-м~"
    eve.c "Ах~ Да~ Так~ М-м~"
    "Она приподнимает ногу и широко раскрывается, позволяя мне глубже ласкать её киску пальцами."
    "Она стонет всё громче, уже не в силах сдерживаться. Ей едва удаётся не привлечь внимание остальных."
    eve.c "Ха-а~"
    eve.c "[mc.name]~ Я сейчас~ Ха-а~ Я..."
    eve.c "Я сейчас, блядь, кончу~"
    "Она может закричать на весь зал. Это огромный риск, но..."
    "Слишком горячо, чтобы остановиться. Я должен заставить её кончить прямо здесь, в кресле."
    "Я чувствую, как её киска пульсирует, пока в последний раз яростно трахаю её пальцами."
    scene evetheaterfingeringfinish1 with fadewhite
    pause
    eve.c "М-М-М-М-М~"
    "Ева задыхается рядом и обхватывает мою руку, сжимая её между влажных бёдер."
    "Она едва сдерживается, чтобы не устроить сцену; дрожит и извивается на кресле."
    "Её маленькие пальцы впиваются мне в руку, а из киски на ладонь брызжут соки."
    eve.c "Ха-а~ Ха-а~"
    scene evetheaterfingeringfinish2 with fade
    pause
    "Через несколько мгновений хватка Евы слабеет, и она опускает ноги на пол."
    "Я вытаскиваю руку — она вся в её соках."
    eve.c "Ого~ Это было..."
    mc.c "Вот это да. Прямо в кинотеатре?"
    eve.c "Сам напросился..."
    mc.c "Тебе, похоже, фильмы такого жанра нравятся."
    eve.c "Хе~ Нечестно..."
    call stopMusic from _call_stopMusic_8
    scene black with fade
    "Ева поправляет одежду и молча устраивается на своём месте. Мы снова смотрим фильм."
    "Вскоре фильм заканчивается."
    call playMusic(chillTheme) from _call_playMusic_50
    $ location_theater.showBackground()
    "Выйдя в ослепительно яркий по сравнению с залом холл, Ева отряхивается."
    show eve smile with dissolve
    "Выходя вместе с другими зрителями, Ева ухмыляется мне."
    show eve smile talk
    eve.c "Не думала, что ты... такой ловкий."
    show eve smile
    mc.c "Эй!"
    mc.c "Вообще-то это была просто расплата."
    show eve smile talk
    eve.c "Расплата, значит?"
    show eve tease talk
    eve.c "Хм... Ждать продолжения~?"
    show eve smile
    "Ева возвращается за стойку; каким-то чудом никто не удивляется, что она только что отлучалась."
    mc.c "Кстати, кажется, в том зале остался небольшой беспорядок."
    show eve neutral talk
    eve.c "А?"
    show eve smile talk 2
    eve.c "О-о~ Ха-ха~ Чёрт~"
    show eve smile
    mc.c "Напомни мне никогда больше не садиться на это место."
    mc.c "Удачи с остатком смены."
    show eve thinking
    eve.c "Да, ага, что угодно..."
    show eve smile talk
    eve.c "Пока."
    scene black with fade
    "Я выхожу, мы машем друг другу на прощание, и она возвращается к работе."
    "И всё же на её лице остаётся смущённая улыбка."
    "Хороший фильм."

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.addLove(1)

    return

label eveHEvent3(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_51
    $ location_home_lounge.showBackground()
    "Блин, сегодня вообще ничего не хочется делать..."
    "Хвала богам за свободу работать когда вздумается, но если бизнес открыт семь дней в неделю, дела найдутся всегда."
    "В соседней комнате опять копятся бумаги... Хм... не сейчас."
    "Вот бы по телевизору шло что-нибудь интересное..."
    "{b}*Динь-дон*{/b}"
    "А, звонок в дверь. Ко мне редко заходят без предупреждения."
    scene homehallway with fade
    "В многоквартирном доме хотя бы реже ходят уличные торговцы. Кто там?"
    "Я открываю дверь..."
    scene evehevent3i1 with fade
    pause
    "На уровне глаз никого. Опускаю взгляд и вижу свою забавную маленькую соседку."
    eve.c "Йо~"
    "Любопытно. Она не писала заранее, но теперь, когда думаю об этом, она первый человек, с которым я по-настоящему сблизился по-соседски."
    mc.c "Эй, Ева, что случилось?"
    eve.c "Я... э-э... У меня воды отошли."
    mc.c "Что?! Ты беременна?!"
    eve.c "...А? Нет?"
    mc.c "Но... что?"
    eve.c "Воды... В душе нет..."
    "Реакция у меня была совершенно искренняя. Я понял, как глупо это прозвучало, сразу после слов. Но она же сама так сказала."
    mc.c "А-а... Понял... Ты так выразилась... Ладно, неважно."
    eve.c "Э-э..."
    "Мы неловко молчим в коридоре."
    mc.c "Прости, заходи."
    scene homehallway with fade
    "Я приглашаю Еву внутрь."
    show eve neutral with dissolve
    mc.c "Так что случилось?"
    show eve neutral talk
    eve.c "Вода не работает."
    show eve neutral
    mc.c "Хм... Я не сантехник, но пару раковин чинил."
    show eve neutral talk
    eve.c "Нет, нет... Мне нужно принять душ, а хозяин сможет прислать мастера только завтра."
    eve.c "Можно воспользоваться твоим?"
    show eve neutral
    mc.c "О-о! Да, конечно."
    show eve smile talk
    eve.c "Спасибо."
    show eve smile
    "Мы знакомы не так давно, но приятно, что она считает нас достаточно близкими, чтобы обратиться по-соседски."
    "Полезное {b}преимущество{/b} дружбы."
    mc.c "Сюда."
    show eve neutral
    eve.c "Хм."
    $ location_home_bathroom.showBackground()
    "Я провожаю Еву по коридору в ванную."
    show eve neutral talk with dissolve
    eve.c "Она больше моей спальни..."
    show eve neutral
    mc.c "Извини."
    show eve smile talk
    eve.c "Ага~"
    show eve smile
    mc.c "Полотенца вон там, бери любое. Если что понадобится — позови."
    show eve smile talk 2
    eve.c "Спасибо, я быстро."
    show eve smile
    mc.c "Без проблем."
    "Я ещё даже не успеваю отвернуться, как она начинает снимать рубашку."
    scene homehallway with fade
    "Я пулей вылетаю из комнаты. Не знаю, задумалась она или что. Забавная она."
    "Ладно, оставлю её в покое."
    $ location_home_lounge.showBackground()
    "Я возвращаюсь в гостиную и сажусь. Убавляю громкость и задумываюсь: что между нами происходит?"
    "Мы больше чем друзья? В каком-то смысле? Не знаю, у нас всё ещё ничего не определено."
    "Свидания и иногда секс. Может, мы просто друзья с привилегиями — соседи, которые время от времени развлекаются."
    "Неплохо иметь друга-соседа, к которому можно обратиться, когда что-нибудь ломается."
    eve.c "{size=20}[mc.name]?{/size}"
    "А? Она меня зовёт?"
    mc.c "Да?"
    eve.c "{size=20}Я не понимаю.{/size}"
    "Не понимает? Вода ведь не работает. Может, не разобралась, как включить душ."
    scene homehallway with fade
    "Я подхожу к двери ванной."
    mc.c "Помочь? Можно войти?"
    eve.c "Ага."
    "Я захожу внутрь."
    call playMusic(barTheme) from _call_playMusic_52
    scene evehevent3i2 with fade
    eve.c "Как он включается?"
    "...О боже."
    "У входа в душ стоит совершенно голая Ева, будто ничего особенного не происходит."
    mc.c "Ох, блядь, прости, я..."
    eve.c "А?"
    "Она приподнимает бровь и опускает взгляд на себя."
    eve.c "Да ладно, здоровяк, ничего страшного, правда?"
    mc.c "Э-э... Раз ты так говоришь."
    eve.c "Ага~ Видел бы ты своё лицо..."
    eve.c "Но я не шучу... Я правда не понимаю."
    mc.c "А, точно, душ. Да, это немного странно."
    scene evehevent3i3 with fade
    pause
    "Я осторожно протискиваюсь мимо голой Евы и захожу в душевую. Она совершенно не смущается."
    "Отворачиваю душевую лейку от нас и показываю, как повернуть ручки."
    mc.c "Эта — горячая, эта — холодная..."
    eve.c "А-а..."
    "Ева наклоняется из-за моей спины, чтобы разглядеть. Её совершенно не смущает, что она стоит здесь голая со мной."
    "Впервые вижу их... вот так, в открытую. Не считая попытки прикрыть их тем крошечным бикини на пляже."
    "Её невероятные изгибы... На таком маленьком теле..."
    "Ева смотрит на мой пах, а затем на меня — выражение лица почти не меняется."
    eve.c "Стояк, здоровяк?"
    "Похоже, скрыть эрекцию всё равно не удалось."
    mc.c "Прости."
    eve.c "Не за что... Это из-за моих сисек, да?"
    mc.c "..."
    eve.c "Можешь их использовать, если хочешь."
    mc.c "Использовать...?"
    eve.c "Потрахай их. Ты ведь разрешил мне воспользоваться душем и всё такое..."
    "Господи..."
    eve.c "Давай, снимай одежду."
    call playMusic(sexyTheme) from _call_playMusic_53
    scene black with fade
    "Я не спорю и позволяю всему случиться. Голова уже кружится от желания. Раздеваюсь перед ней."
    "От одной мысли у меня встаёт колом. Она подходит, почти не приседая, и прижимает грудь к моему паху."
    image eveShowerBoobjob1 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part1.webm")
    scene eveShowerBoobjob1 with fade
    pause
    "Она медленно подаётся вперёд и останавливается совсем близко, прижимая сиськи к пульсирующему члену."
    "Ей почти не приходится приседать: мой член ложится прямо на её декольте."
    eve.c "Ага~ Смотри, как удобно по высоте."
    "Она покачивается из стороны в сторону, зажимая мой член между огромных сисек."
    eve.c "Ты такой твёрдый."
    mc.c "А как иначе?"
    eve.c "Приятно знать..."
    "Она продолжает ухмыляться мне снизу вверх, наслаждаясь тем, как одни её дразнящие движения отражаются у меня на лице."
    eve.c "Не знаю, получится ли у меня полностью обхватить его..."
    eve.c "Но можем попробовать~"
    image eveShowerBoobjob2 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part2.webm")
    scene eveShowerBoobjob2 with fade
    pause
    "Она поднимает свои огромные груди, раздвигает их и зажимает мой каменный член между ними."
    "Прикосновение гладкой шерсти тут же посылает дрожь по спине."
    mc.c "О боже..."
    eve.c "Ага~ Какой твёрдый~"
    eve.c "Я закрываю его едва ли наполовину... Ничего себе..."
    "Мягкость... тепло... тяжесть... Я чувствую всё это, когда она двигается."
    "Она двигает грудью вверх-вниз, нежно скользя по мне."
    "Большие красивые розовые соски покачиваются, пока она водит ими по всей длине моего члена."
    eve.c "Приятно?"
    mc.c "Невероятно."
    eve.c "Давай доведу тебя до оргазма."
    image eveShowerBoobjob3 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part3.webm")
    scene eveShowerBoobjob3 with fade
    pause
    "Она меняет ритм, несинхронно покачивая сиськами и двигая мой член из стороны в сторону."
    "Мягкая плоть полностью обхватывает мой член, укутывая его тёплым пушистым теплом."
    "Она то ухмыляется, глядя на меня, то любуется своей работой: с головки моего члена уже капает предэякулят."
    eve.c "Хм... Забавно торчит."
    eve.c "Если задуматься, правда странно."
    mc.c "Нисколько не странно... Хм... Совсем."
    eve.c "Ага~"
    image eveShowerBoobjob4 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part4.webm")
    scene eveShowerBoobjob4 with fade
    pause
    "Её огромные сиськи так колышутся, что органы чувств просто в шоке."
    "Она раскачивается из стороны в сторону, а хвост виляет за спиной."
    eve.c "М-м..."
    "Она изо всех сил двигает своей грудью, сжимая и прижимая меня со всех сторон."
    eve.c "Скоро кончишь?"
    mc.c "Ага... Если ты просто..."
    image eveShowerBoobjob5 = Movie(play="images/characters/eve/hscenes/showerBoobjob/part5.webm")
    scene eveShowerBoobjob5 with fade
    pause
    "Она ускоряется, сдавливает грудь с боков и крепче зажимает мой член."
    "Усиленное трение от давления терзает член, двигая меня взад-вперёд."
    eve.c "Ха-а... Ха-а..."
    eve.c "Чувствую, как ты дёргаешься."
    "Я двигаюсь в такт. Столько мягкой плоти... Это не просто титьки — я будто по-настоящему трахаю её грудь."
    mc.c "Ох, блядь..."
    eve.c "Давай, кончай~"
    "Я уже на пределе."
    scene eveshowerboobjobfinish1 with fadewhite
    pause
    mc.c "Ах!"
    "Я толкаюсь вперёд. По телу пробегает разряд, мышцы напрягаются, и из меня вырывается огромная порция спермы."
    eve.c "Ик!"
    "Сперма вылетает с такой силой, что попадает Еве прямо в лицо. Она может только щуриться, пока её заливает. Кажется, она даже тихонько пискнула."
    scene eveshowerboobjobfinish2 with fade
    pause
    "Из меня вырываются густые струи, покрывая её лицо и сиськи."
    "Капли стекают с члена на грудь и собираются на её вздымающемся торсе."
    eve.c "Ух ты~"
    eve.c "Чёрт... Её столько."
    mc.c "Блядь... Это было невероятно."
    "Она вытирает щёку и смотрит на себя и на тот беспорядок, который я устроил."
    eve.c "Хорошо, что мы в ванной, да?"
    mc.c "Ага."
    eve.c "Можешь идти. Или сам хочешь в душ?"
    mc.c "Я... в порядке."
    scene evehevent3end with fade
    pause
    "Я выхожу, а она спокойно подходит и включает душ."
    eve.c "Хм~"
    mc.c "Ну, э-э... Полотенца там. И..."
    "Замечаю, что чистой одежды у неё с собой нет..."
    mc.c "Ты не взяла сменную одежду?"
    eve.c "А, точно... Не взяла. Я просто зашла спросить, а потом вошла."
    mc.c "А..."
    eve.c "Надену просто полотенце. Тут идти всего через коридор."
    mc.c "...Ладно."
    scene black with fade
    "Я возвращаюсь в гостиную и жду, пока она закончит мыться."
    "Когда она заканчивает, высовывается из-за угла, благодарит и прощается."
    "Полотенце на удивление хорошо всё прикрывает. Я провожаю её до двери, и она своими маленькими ножками перебегает через коридор к себе."
    "Ух ты."

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.addLove(1)

    return

label eveHEvent4(fromGallery):
    call playMusic(barTheme) from _call_playMusic_54
    $ location_bar.showBackground()
    "Сегодня в баре тихо, пока только я и ещё один сотрудник."
    "В углах слышны лишь тихие разговоры."
    unknown "Ладно, [mc.name]. Я закончил в подсобке."
    mc.c "А, хорошо. Спасибо, отлично поработал."
    "Работник на полставки разбирает запасы в подвале. Скоро заканчивает, а сменщик ещё не пришёл."
    mc.c "Ты уже уходишь?"
    unknown "Ага, всё нормально? Кажется, Майк скоро придёт."
    mc.c "Ладно, конечно. Всё будет хорошо."
    "Я оглядываю бар. Большую часть дня было тихо. Какое-то время я легко справлюсь один."
    "Но потом точно заскучаю."
    mc.c "Эй, не радуйся так, что уходишь. Я тут один заскучаю."
    unknown "Хе-хе, справишься. Уверен, какая-нибудь милашка зайдёт поболтать с тобой... почему-то."
    unknown "Пока."
    "Он ухмыляется и уходит, не дав мне ответить."
    mc.c "А?"
    "Что это значит?"
    "..."
    "Я вытираю стакан. Делать нечего..."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Сообщение..."
    eve.c "ты на работе"
    "Ну надо же..."
    "Хм, это вопрос или утверждение?"
    mc.c "Ага"
    eve.c "ок"
    "Коротко и ясно, как обычно. Проверяет, как у меня дела?"
    "Я не знаю её расписания. Смены в кинотеатре, и там ей поручают всякое. Может, она хочет встретиться?"
    "Я думаю об этом несколько минут, но, только собираясь ответить, замечаю, как приоткрывается входная дверь."
    show eve neutral with dissolve
    "Вот она — пытается протолкнуть дверь. Не зря помещение рассчитано на антро любого размера."
    show eve smile
    "Она слегка улыбается, увидев меня, и ковыляет ко мне."
    show eve smile talk
    eve.c "Здоров."
    show eve smile
    mc.c "Эй, Ева. Я как раз думал, что означало сообщение."
    show eve neutral talk
    eve.c "Только что со смены. Всё равно шла мимо, вот..."
    show eve neutral
    mc.c "Ну, я польщён. Для меня, такого старичка?"
    mc.c "День не такой паршивый? Обычно ты говоришь, что после смены валишься и сразу ложишься спать."
    show eve neutral talk
    eve.c "Ага... Сегодня нормально. Обычно да..."
    eve.c "Не знаю, просто скучно стало. Решила проверить, не занят ли ты."
    show eve neutral
    mc.c "Рад, что заглянула. Сейчас здесь только я, бывает скучновато."
    show eve smile talk
    eve.c "Да уж, вижу."
    show eve smile
    mc.c "Эй, это моё любимое заведение."
    show eve smile talk
    eve.c "Ага~"
    show eve smile
    mc.c "Тогда выпьешь?"
    show eve neutral talk
    eve.c "Давай пиво."
    show eve smile talk
    eve.c "Я даже сама заплачу, богатенький. Мне на днях выдали зарплату."
    show eve smile
    mc.c "Молодец, денежный мешок. Я халявой не промышляю."
    show eve neutral talk
    eve.c "О? После всего, что я для тебя {i}сделала{/i}?"
    show eve neutral
    "Что она сделала для..."
    "А-а... вот это... Погоди, она серьёзно?"
    mc.c "Я..."
    show eve tease talk
    eve.c "Ага-ха~ Тебя так легко поддеть~"
    show eve tease
    mc.c "Господи... Я тебя совсем не понимаю..."
    show eve neutral talk
    eve.c "И хорошо."
    show eve smile talk 2
    eve.c "Кстати, напомнила: сегодня кое-что произошло, расскажу."
    show eve smile
    mc.c "И что-то интересное правда случилось?"
    show eve smile talk
    eve.c "Помнишь тот фильм, который мы... э-э... тогда {i}смотрели{/i}?"
    show eve smile
    mc.c "Как забыть. Хотя не уверен, что ты хоть что-то из него {i}посмотрела{/i}."
    show eve bashful talk
    eve.c "Ага, ага~"
    show eve smile talk
    eve.c "Короче, сегодня на фильм пожаловались. Я была в холле, меня позвали разобраться."
    show eve smile
    mc.c "Пожаловались на шум?"
    show eve neutral talk
    eve.c "Ага. Иногда такое бывает. Обычно кто-нибудь сидит в телефоне или вроде того, но..."
    show eve smile talk
    eve.c "Захожу в зал, а там какая-то девушка сосёт парню член~"
    show eve smile
    "В баре вдруг становится так тихо. Вот бы я чуть погромче включил музыку."
    "Похоже, никто не прислушивается."
    mc.c "Ох, блядь..."
    show eve smile talk 2
    eve.c "Ага~ Вот именно. Это могли бы быть мы."
    show eve smile
    mc.c "Фильм явно слишком горячий для кинотеатра."
    mc.c "Хорошо хоть ты смогла сдержаться..."
    show eve smile talk
    eve.c "Хе~ Ага~"
    show eve smile talk 2
    eve.c "А если бы всё было наоборот... Ты бы смог не шуметь~?"
    show eve smile
    "Хороший вопрос... Не уверен, что смог бы."
    "И рад, что никто тут не подслушивает..."
    mc.c "И что ты сделала?"
    show eve tease talk
    eve.c "Просто посветила им в лицо. Он сразу спрятал член~"
    show eve tease
    mc.c "Ты их не выгнала?"
    show eve thinking
    eve.c "Хм... Наверное, стоило... Но это же возиться надо..."
    "Я бы, наверное, сделал так же."
    scene black with fade
    "Ева ещё немного сидит со мной за парой напитков, пока я не заканчиваю смену и не приходят остальные."
    "Я мог бы остаться, но Ева собирается домой, и я решаю проводить её."
    $ location_home_bedroom.showBackground()
    "Мы идём домой, и, наученный прошлым опытом, я зову Еву к себе."
    "Она беззаботно кивает, и мы заходим."
    show eve neutral with dissolve
    "Я до сих пор не понимаю, что у неё на уме."
    "Не знаю, к чему ведёт сегодняшний вечер. Но даже если ничего не случится, я рад просто провести с ней время."
    "Мы садимся с напитками и включаем телевизор."
    show eve thinking
    eve.c "Хм..."
    mc.c "Что такое?"
    call stopMusic from _call_stopMusic_9
    show eve neutral talk
    eve.c "Когда ты уже меня трахнешь?"
    show eve neutral
    "Ну вот, теперь всё ясно."
    mc.c "Я... э-э..."
    mc.c "Ты хочешь?"
    show eve smile talk
    eve.c "Ну да... После всего, что мы делали?"
    show eve smile
    mc.c "Если честно, я не понимал, тебе просто нравится меня дразнить или что-то ещё..."
    show eve thinking
    eve.c "Хм... Я пыталась намекнуть, чтобы ты..."
    mc.c "Чтобы я...?"
    show eve neutral talk
    eve.c "Ты должен был... Не сдерживаться."
    eve.c "Наброситься на меня..."
    show eve neutral
    "Хм... Может, дело было не в «когда мы уже трахнемся», а в том, когда {b}я{/b} наконец {b}её{/b} трахну?"
    "Может... ей нравится подчиняться? Нет, вряд ли... Она же такая инициативная..."
    mc.c "Прости, я правда считаю тебя... милой. Э-э... И горячей."
    mc.c "Я слишком медлил?"
    show eve thinking
    eve.c "Хм... Ты романтик, да~"
    mc.c "Виноват. Это у меня почти основное качество."
    show eve smile talk 2
    eve.c "Ага~ Ладно, скажу прямо."
    eve.c "Хочу, чтобы ты просто... взял меня."
    show eve smile talk
    eve.c "Ты большой парень~ Мог бы просто... делать со мной что угодно~"
    show eve smile
    "О боже."
    "Этот взгляд... Едва заметно похотливый, полный намёка... Она смотрит на меня с вожделением."
    "Может, я её разочаровал... Я обычно так не поступаю, но... не против попробовать."
    "Я тянусь к её руке."
    call playMusic(sexyTheme) from _call_playMusic_55
    scene evehevent4i1 with fade
    pause
    "Я наклоняюсь к Еве, нависая над ней и закрывая собой свет."
    "Я беру её за руки и прижимаю их к спинке дивана. Её руки такие тонкие и лёгкие."
    "Она не вскрикивает и не сопротивляется. Смотрит мне в глаза так, будто только сейчас очнулась. Она этого хочет."
    mc.c "Это можно устроить."
    eve.c "Ага~ Ой, нет~"
    "Она слегка удивлённо смотрит на меня, но с лица не сходит эта дерзкая улыбка..."
    "Она всё это время намекала, что мне пора действовать."
    "Я начинаю снимать с неё рубашку через голову. Она помогает, покачиваясь."
    scene black with fade
    "Мы быстро раздеваемся прямо на месте."
    scene evecouchmissionarystart with fade
    pause
    "Я прижимаю эрегированный член между её ног, беру её за бёдра и подтягиваю к краю дивана."
    "Она похотливо смотрит вниз, любуясь тем, что перед ней."
    "И зрелище что надо... Как она вообще сможет принять его? Её это, похоже, не волнует."
    eve.c "Наконец-то..."
    mc.c "Готова?"
    eve.c "Неважно, готова ли я~"
    "С этими словами я направляю член и вхожу в неё."
    image eveCouchMissionary1 = Movie(play="images/characters/eve/hscenes/couchMissionary/part1.webm")
    scene eveCouchMissionary1 with fade
    pause
    "Она невероятно тугая. Мягкая шерсть и влага помогают мне скользнуть внутрь, но её мышцы крепко сжимают член."
    "Сначала я двигаюсь только наполовину и чувствую, как её тело вздрагивает и сокращается, когда я проникаю."
    eve.c "Ха-а~ Ха-а~ М-м-м~"
    eve.c "Ох, блядь~ М-м~ Такой большой... Ты ещё даже не весь вошёл~"
    "Она прикрывает глаза не от боли, а от удовольствия."
    "Её ноги обхватывают мои бёдра, направляя меня ближе к ней."
    mc.c "Блядь, ты такая тугая."
    eve.c "Вот так... М-м~ Достаточно~"
    eve.c "Продолжай~ Ха-а~ Ещё~"
    "Мы двигаемся ровно и плавно. Чувствую, как ей хочется большего."
    "Похоже, она и правда хочет пожёстче."
    image eveCouchMissionary2 = Movie(play="images/characters/eve/hscenes/couchMissionary/part2.webm")
    scene eveCouchMissionary2 with fade
    pause
    "Я крепко обхватываю её за талию. Мои руки закрывают большую часть её туловища."
    "Я грубо поднимаю её, прижимаю к бёдрам и насаживаю на весь член."
    eve.c "Ха-а~! Ха-а~! Ах-х~"
    eve.c "Да-а~ М-м~ Жёстче~ Ещё~"
    "Её тихий голос срывается на довольный писк — обычно она такая монотонная."
    "Её большие сиськи подпрыгивают, диван скрипит, а по комнате разносятся влажные шлепки."
    "Её киска сжимает мой член, растягиваясь, чтобы принять его. Не знаю, куда он там весь помещается."
    mc.c "И это ты говорила, что мой член слишком большой..."
    eve.c "Я это... М-м~ сказала, чтобы ты завёлся~ Чтобы ты взял меня силой~"
    eve.c "Я хотела, чтобы ты... М-м~ поднял меня~ Ха-а~ Оттрахал до потери мозгов~"
    "Поднять её? Думаю, я смогу..."
    image eveLiftingFacing1 = Movie(play="images/characters/eve/hscenes/liftingFacing/part1.webm")
    scene eveLiftingFacing1 with fade
    pause
    "Я обхватываю её за талию, поднимаю и не разъединяюсь с ней, пока несу к кровати."
    "Её маленькие лапки вцепляются мне в плечи, пока я насаживаю её на член."
    eve.c "Ха-а~ Ха-а~ Да, блядь!"
    eve.c "Бери меня~ М-м~ Используй~ Трахай своим огромным членом~"
    "Я впиваюсь большими пальцами ей в живот и подбрасываю её на члене, как игрушку."
    "Её восхитительная грудь подпрыгивает у меня перед глазами, а каждый толчок сопровождается тихим стоном."
    mc.c "Ох, блядь~ Ева... Ты этого хотела?"
    eve.c "М-м~ Ха-а~ Я хотела... М-м~"
    eve.c "Ещё~"
    "Ещё? Её лицо перекосило от похоти, она пристально смотрит мне в глаза."
    "Это разжигает во мне желание продолжать."
    image eveLiftingFacing2 = Movie(play="images/characters/eve/hscenes/liftingFacing/part2.webm")
    scene eveLiftingFacing2 with fade
    pause
    "Собрав все силы, я крепко обхватываю её и с размаху насаживаю на член."
    eve.c "Ха~ Ха-а~ Ах~ А-а~~ М-м!"
    eve.c "Блядь, блядь~ Да-а-а!"
    "Наши бёдра сталкиваются с громкими непристойными шлепками плоти и соков. Мы оба задыхаемся."
    "Мышцы горят, удовольствие нарастает внутри."
    eve.c "Ха-а~ Ха-а~! А-а-а~!"
    "Её сиськи беспорядочно болтаются. Она изо всех сил держится за мои плечи, пока я полностью контролирую её тело."
    "Я на полной скорости врезаюсь в неё и уже близок к пределу."
    mc.c "Я сейчас..."
    eve.c "Кончи~ М-м~ В меня~~"
    scene eveliftingfacingfinish1 with fadewhite
    pause
    "Я сильно толкаюсь вверх, прижимая её к бёдрам, и заливаю киску Евы огромной порцией спермы."
    eve.c "А-а-а-а~!"
    "Мы впиваемся ногтями друг в друга, пытаясь не разъединиться. Её тело дрожит и извивается, когда она кончает."
    "Она выгибает спину, содрогаясь и взрываясь от удовольствия."
    "Я двигаю бёдрами и выжимаю из себя последние капли."
    scene eveliftingfacingfinish2 with fade
    pause
    "Мышцы начинают отказывать. Я снимаю её с члена и укладываю на кровать."
    "Из её тугой маленькой киски вытекает река спермы, заливая простыни."
    eve.c "Ха-а~ Ха-а~ М-м~"
    "Ева тяжело дышит и едва фокусирует взгляд. Я и сам с трудом держусь на ногах."
    "Я нависаю над ней и любуюсь результатом."
    "Через несколько мгновений мы приходим в себя и смотрим друг другу в глаза."
    mc.c "Э-э, Ева... Я кончил внутрь... Это нормально?"
    eve.c "Ха-а~ Ой..."
    eve.c "Я просто... М-м~ сказала всякое. Наверное, не стоило... Да?"
    eve.c "Если только... Ты хочешь наплодить от меня мышат~ Ага~ Помнишь, я рассказывала про мышей..."
    mc.c "Наверное... нет..."
    "...Пока?"
    eve.c "Ха-а~ Просто шучу, здоровяк~ Всё нормально, выпью таблетку."
    "Фух. А то я чуть не залетел на свою соседку. Мы знакомы всего ничего."
    call playMusic(barTheme) from _call_playMusic_56
    scene evepillowtalk with fade
    pause
    "Ноги наконец подкашиваются, и я падаю на кровать."
    "Ева собирается с силами, забирается рядом и тоже покачивается."
    "Мы ещё немного лежим, наслаждаясь послевкусием бурного секса."
    eve.c "Теперь я и правда вымоталась..."
    mc.c "Я не настолько, как ты... Я ведь не тяжелоатлет."
    eve.c "О чём ты? Такой большой и сильный парень... Тебе легко управиться с маленькой мышкой~"
    mc.c "Да уж. Может, всё дело в весе твоих сисек."
    eve.c "Ага-ха~ Заткнись~"
    "Мы прикрываем глаза, наслаждаясь послевкусием и понемногу приходя в себя."
    eve.c "Хорошо было..."
    mc.c "Ещё как."
    eve.c "Я вся в сперме... Можно я помоюсь?"
    mc.c "Конечно. Ты уже знаешь, как включать душ."
    eve.c "Хм~"
    scene black with fade
    "Маленькие ступни Евы шлёпают по полу и скрываются за углом в коридоре."
    "Я слышу, как включился душ. Ещё немного лежу, потом тоже привожу себя в порядок."
    "Через несколько минут Ева возвращается в спальню, оглядывается и собирает одежду."
    $ location_home_bedroom.showBackground()
    "К моему удивлению, она надевает верхнюю часть одежды, в которой пришла, и прижимает к себе нижнее бельё."
    show eve smile with dissolve
    "Она уже оделась... Собирается уходить?"
    show eve smile talk 
    eve.c "Было весело."
    show eve smile
    mc.c "Да... Можно и так сказать."
    show eve smile talk
    eve.c "Увидимся? Можем повторить как-нибудь~"
    show eve smile
    mc.c "А... да."
    "Я немного разочарован. Наверное, ожидал, что она вернётся в постель... останется со мной."
    show eve smile talk
    eve.c "Пока, здоровяк."
    hide eve with dissolve
    "С этими словами она выходит за дверь, прежде чем я успеваю встать."
    "Не жалуюсь, это было охрененно горячо."
    "Но чего-то всё же не хватает..."
    "Кто мы друг другу?"

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.addLove(1)

    return

label eveHEvent5(fromGallery):
    call playMusic(barTheme) from _call_playMusic_57
    $ location_home_bedroom.showBackground()
    "Что вообще сказать об отношениях с Евой...?"
    "Для кого-то это воплощение мечты."
    "Милая соседка. Спокойная, смешная, безумно сексуальная и готовая трахаться."
    "А недавно выяснилось, что она давно на меня запала и пыталась довести до того, чтобы я сорвался и взял её силой — в каком-то смысле."
    "Я дурак. Удивительно, что не всё испортил."
    "В общем, у нас что-то вроде свободных отношений с сексом."
    "Как сегодня. Перечитываю нашу недавнюю переписку..."
    eve.c "секс сегодня? после смены"
    "Мы соседи, так что нам обоим легко договориться встретиться и повеселиться."
    "Сижу и жду её. Она может прийти с минуты на минуту."
    "{b}*Динь-дон*{/b}"
    "Странно ждать назначенного времени и места, чтобы потрахаться."
    show eve neutral with dissolve
    mc.c "Привет."
    show eve smile talk
    eve.c "Йо~"
    show eve smile
    "Я впускаю Еву. Она бросает сумку и вздыхает."
    show eve thinking
    eve.c "Ха-а..."
    mc.c "Всё нормально?"
    show eve neutral talk
    eve.c "Ага, просто день паршивый."
    show eve neutral
    mc.c "Выглядишь уставшей. Ты точно хочешь... сегодня?"
    show eve smile talk 2
    eve.c "Ага~ Конечно, здоровяк. По дороге купила перекусить. Сахар поможет продержаться."
    show eve smile talk
    eve.c "Ни за что не пропущу... Мне нужно хорошенько получить~"
    show eve smile
    "Романтика..."
    mc.c "Я к твоим услугам."
    show eve smile talk
    eve.c "Хорошо~ Разнеси мне голову~"
    show eve smile
    "Ева начинает раздеваться прямо на месте. Прелюдии почти нет, но от одних мыслей я уже готов немедленно наброситься на неё."
    call playMusic(sexyTheme) from _call_playMusic_58
    image eveDoggyTease = Movie(play="images/characters/eve/hscenes/doggy/teasing.webm")
    scene eveDoggyTease with fade
    pause
    "Она сбрасывает юбку и наклоняется над краем кровати."
    "Она виляет маленькой задницей, подзывая меня."
    eve.c "Доставай, здоровяк~"
    "Кто устоит перед таким зрелищем? Маленькая Ева на четвереньках, лицом вниз, задницей вверх."
    image eveDoggy1 = Movie(play="images/characters/eve/hscenes/doggy/part1.webm")
    scene eveDoggy1 with fade
    pause
    "Как обычно, сразу переходим к самому жёсткому."
    "Я сразу вхожу в неё до основания и врезаюсь бёдрами в её задницу."
    eve.c "О-о-ох~ Блядь~"
    eve.c "Вот так~ М-м-м~ Да-а~"
    "Кровать скрипит от наших резких движений. Каждый толчок с силой прижимает Еву к матрасу."
    "Она уже насквозь мокрая и каким-то образом принимает весь мой член."
    eve.c "М-м~ Ещё~ Ещё~"
    "Она продолжает просить ещё и хочет пожёстче."
    image eveDoggy2 = Movie(play="images/characters/eve/hscenes/doggy/part2.webm")
    scene eveDoggy2 with fade
    pause
    "Я крепко хватаю её за задницу и толкаюсь ещё сильнее."
    "Мокрая плоть и шерсть шлёпают друг о друга, складки её киски хлопают по моему стволу."
    eve.c "А-а-а~ А-а~ М-м-м~"
    "Я впиваюсь пальцами в её шерсть, чтобы удержаться, а огромная грудь болтается от наших движений."
    "Я чувствую её тихие визги удовольствия через киску; вибрация её тела невероятно ощущается на моём члене."
    eve.c "Ха-а~ Ха-а~ М-м~ [mc.name]~"
    mc.c "Что? Слишком?"
    eve.c "Н-нет~ М-м~"
    eve.c "Ха-а~ Переверни меня~ Ах~ Переверни~"
    eve.c "Хочу тебя~ Ах~ Души меня~"
    "...Душить её?"
    "Это продолжение её любви к жёсткому сексу? Она хочет, чтобы я пользовался ею? Такая динамика власти?"
    mc.c "Ч-что? Ты...?"
    eve.c "М-м~ Пожалуйста~ М-м~"
    "Я не уверен..."
    image eveChokingMissionary1 = Movie(play="images/characters/eve/hscenes/chokingMissionary/part1.webm")
    scene eveChokingMissionary1 with fade
    pause
    "Я переворачиваю её на спину."
    "Она берёт мою руку и направляет к своей маленькой шее."
    eve.c "Вот так~ М-м~"
    "Мои пальцы обхватывают её крошечную шею. Такая маленькая и хрупкая. Я чувствую её стоны через горло."
    "Большой палец ложится поперёк шеи, но я сжимаю совсем чуть-чуть. Даже так кажется слишком сильно."
    "Я невольно замедляюсь, беспокоясь за неё. Напряжение спадает."
    eve.c "Ага~ Сильнее, здоровяк~ Сжимай~"
    mc.c "Но..."
    eve.c "Пожалуйста~ М-м~ Я тебе доверяю~"
    "Похоже, она знает, чего хочет. Ей это нужно."
    "Я сжимаю лишь немного сильнее. Она закатывает глаза от удовольствия."
    eve.c "М-м~ Сильнее~"
    "Я сомневаюсь, но... глядя на неё, извивающуюся от удовольствия, теряю самообладание."
    image eveChokingMissionary2 = Movie(play="images/characters/eve/hscenes/chokingMissionary/part2.webm")
    scene eveChokingMissionary2 with fade
    pause
    "Я полностью обхватываю её шею и сжимаю так сильно, как только решаюсь."
    eve.c "Х-ха-а~ М-м-м~"
    eve.c "О-ох~ Блядь~ Ха-а~"
    eve.c "Да-а-а~"
    "Сквозь тяжёлое, прерывистое дыхание она подтверждает, что именно этого хочет."
    "Чем крепче я сжимаю, тем сильнее она извивается. Я жёстко трахаю её маленькое тело."
    "Она совсем потеряла контроль. Её тело в моей власти. Я могу делать с ней что угодно."
    eve.c "Ха-а~ Ха-а~ Ха-а~ М-м~ М-м-м~ М-м~"
    "Но по её лицу всё ясно: она на седьмом небе."
    "Глаза закатываются. Она вздрагивает всё сильнее. Сейчас кончит."
    "Я тоже уже близко."
    mc.c "Блядь!"
    scene evechokingmissionaryfinish1 with fadewhite
    pause
    eve.c "М-М-М-м-м~"
    "Ева сдавленно вскрикивает — больше ничего не может выговорить, пока моя рука сжимает ей шею."
    "Её тело сжимается вокруг меня, и я заливаю её матку огромной порцией спермы."
    eve.c "А-а-кх~ А-кх~"
    "Она кашляет и задыхается, всё ещё содрогаясь от экстаза."
    "Моё тело сотрясает оргазм, и я замечаю, как сильно сжимал её шею."
    scene evechokingmissionaryfinish2 with fade
    pause
    "Я тут же отпускаю и выхожу. Она жадно глотает воздух; огромная грудь быстро вздымается."
    eve.c "Ха-а~ Ха-а-а~ Ха-а-а-а~"
    mc.c "Блядь, прости! Ты в порядке?!"
    eve.c "Ха-а~ Ах~"
    eve.c "Так... хорошо~"
    "Фух... Похоже, я не перегнул. Она получила то, чего хотела..."
    eve.c "Это было... Ха-а~ замечательно~ Ха-а~"
    "Её глаза полуприкрыты, она тяжело дышит, но на лице сияет довольная улыбка."
    "Это было... невероятно. Никогда бы не подумал..."
    call playMusic(heartTheme) from _call_playMusic_59
    scene evepillowtalk with fade
    "Через некоторое время я помогаю Еве устроиться на подушке."
    "Мы немного лежим, приходя в себя."
    eve.c "Эй, у тебя какое-то... странное лицо."
    mc.c "А? Да нет, всё нормально."
    eve.c "Тебе не было слишком тяжело? Я ведь даже не спросила, нравится ли тебе такое..."
    mc.c "Нет, нет. Я понимаю."
    eve.c "М-м..."
    mc.c "Ладно, обычно это не совсем моё, но если тебе нравится, я не против. Просто не хочу причинить тебе боль."
    mc.c "Я не был уверен, насколько сильно могу..."
    eve.c "Вообще-то должно быть {i}немного{/i} больно~"
    eve.c "Но это мило... Спасибо, что поддержал меня."
    eve.c "В итоге всё было идеально. Тебя точно ничего не смутило?"
    "Если это так заметно, наверное, стоит признаться: кое-что меня и правда беспокоит."
    "Не это. Просто... после секса мне немного пусто."
    "Это секс. Хороший секс. Но... и всё."
    "Уверен, она скоро встанет, приведёт себя в порядок, перекусит и уйдёт за дверь."
    "А сейчас хочется прижаться к ней, крепко обнять, чтобы она устроилась у меня на руках, целовать её..."
    "Но мы ведь не такие, да?"
    mc.c "Есть одна вещь. Не хочу всё испортить, но..."
    eve.c "Эй, ты делаешь всё, о чём я прошу. Уверена, я могу пойти тебе навстречу и в {i}чём-нибудь{/i} ещё."
    eve.c "Если только это не какая-нибудь совсем уж извращённая хрень?"
    mc.c "Ха-ха, нет, ничего такого... Даже близко."
    mc.c "Просто мы не... целуемся. Не обнимаемся. Не... ну, не прижимаемся друг к другу."
    eve.c "..."
    "Ева смотрит на меня пустым взглядом и слегка приподнимает бровь."
    eve.c "...Погоди, и это всё?"
    mc.c "Ага. Прости, если это слишком сентиментально."
    eve.c "Чувак... Я уже боялась, что всё становится странным. Если хочешь что-то делать..."
    scene evehevent5i1 with fade
    eve.c "Просто бери меня."
    "Ева поворачивается и забирается ко мне на грудь."
    "Её огромная грудь мягко разъезжается, когда она укладывается на меня и кладёт маленькие лапки мне на кожу."
    "Она спокойно смотрит мне в лицо. Похоже, её это совсем не смущает."
    mc.c "О-ох..."
    mc.c "Хм, я думал, ты хотела, чтобы всё было просто и без обязательств."
    eve.c "Ну, так и было, да? Но..."
    eve.c "Я думала... Если бы ты хотел чего-то {i}такого{/i}, давно бы уже сделал."
    mc.c "Обычно так и было бы. Просто {i}я{/i} решил, что мы только друзья по сексу."
    eve.c "Ну да, но..."
    eve.c "Хм..."
    "Мы ненадолго замолкаем, улыбаемся друг другу и тихо смеёмся."
    "Я обнимаю её, притягивая к себе."
    eve.c "Ага~"
    mc.c "Мы плохо умеем разговаривать, да?"
    eve.c "Ну, не особо. Но я вообще ни с {i}кем{/i} нормально не разговариваю."
    mc.c "Это правда."
    eve.c "Эй..."
    mc.c "Зато для работы с клиентами самое то."
    eve.c "Заткнись~"
    mc.c "Значит, я могу тебя поцеловать?"
    eve.c "Хватит спрашивать разрешения на каждую мелочь. Просто делай, здоровяк~"
    scene evehevent5i2 with dissolve
    pause
    "Я кладу ладонь ей на затылок и нежно притягиваю к себе."
    "Она закрывает глаза, чуть улыбается и приоткрывает губы навстречу моим."
    eve.c "М-м~"
    "Она обнимает меня за плечи, её лёгкое тело прижимается ко мне."
    "Мы приоткрываем рты, языки касаются и щекочут друг друга. Наш первый поцелуй."
    scene evehevent5i1 with dissolve
    "Ева отстраняется и смотрит на меня с той же улыбкой."
    eve.c "Извращенец..."
    mc.c "Плохой, да?"
    eve.c "Ага~"
    mc.c "Ладно, теперь я уже получил многое из того, чего хотел. А теперь могу попросить ещё кое о чём..."
    eve.c "Что {i}теперь{/i}?"
    mc.c "Останься сегодня у меня."
    eve.c "...О-ох..."
    "Похоже, предложение немного застало её врасплох. Она на секунду задумывается."
    eve.c "Хм... Завтра на работу, но дом всего через коридор."
    mc.c "Значит, останешься?"
    eve.c "Ладно~"
    scene black with fade
    "Мы ещё немного отдыхаем, приводим себя в порядок и проводим вечер вместе."
    "Позже ложимся спать."
    call eveSleepover from _call_eveSleepover
    "Ева прижимается ко мне, согреваясь о моё тело."
    eve.c "М-м~"
    mc.c "Спасибо."
    eve.c "Нет, это тебе {i}спасибо{/i}."
    mc.c "Спокойной ночи."
    eve.c "Спокойной."
    scene black with fade
    "Мы засыпаем в объятиях друг друга."
    pause
    "..."
    pause
    scene evehomemorning with fade
    "Я просыпаюсь, чувствуя голову у себя на плече и маленькую ладонь на груди."
    "Глаза привыкают к свету, и я вижу, как Ева улыбается мне. Теперь она кажется совсем другой — в буквальном смысле, при дневном свете."
    eve.c "Привет~"
    mc.c "Доброе утро. Как спалось?"
    eve.c "Я ночевала у парня~"
    mc.c "А у меня была милая девушка."
    eve.c "...Мне понравилось."
    mc.c "Спасибо, что поддержала мои извращённые фантазии."
    eve.c "Ага~ Не такие уж они и плохие. Я бы повторила."
    eve.c "Если и ты не против..."
    mc.c "Когда угодно, Ева."
    scene black with fade
    "Мы ещё немного лежим, но потом Ева возвращается к себе, чтобы собраться на работу."
    "У нас тут неплохая договорённость. Классно."
    "Думаю, теперь мы больше чем друзья."

    if(not fromGallery):
        $ eve.addLike(1)
        $ eve.addLove(1)

    return {'time':'Morning'}


# As useless as tits on a mouse
