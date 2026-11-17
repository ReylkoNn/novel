init offset = 3
default sarah = Person(Character(name='Sarah', who_color='#523617', image = 'sarah'), 'Sarah', '', 'sarah', 'female', 21)

label initialiseCharacter_sarah:
    python:
        sarah.currentLocation = location_park
        location_park.occupants.extend([sarah])
        sarah.availableEvents = [sarahFirstMeetingEvent]

    return

label updateCharacterStatics_sarah:
    python:
        # Personal attributes
        sarah.species = 'Domestic dog'
        sarah.birthday = 1
        sarah.job = 'Student'
        sarah.giftLoves = [item_goldRing]
        sarah.giftLikes = [item_videogame]
        sarah.giftHates = [item_chocolateBar, item_dress]

        # Skill attributes

        # Sexual attributes
        sarah.virgin = False

        # Personal effects

        # Event attributes
        sarah.events = [sarahFirstMeetingEvent, sarahLikeEvent1, sarahLikeEvent2, sarahHEvent1, sarahLikeEvent3, sarahHEvent2, sarahHEvent3, sarahHEvent4, sarahHEvent5, sarahHEvent6, sarahVacation, sarahLikeEvent4, sarahLikeEvent5, sarahHEvent7]
        sarah.specialEvents = [sarahAliceDuoStoryEvent1, sarahAliceDuoStoryEvent2, sarahAliceDuoHEvent1, sarahAliceDuoHEvent2]
        sarah.selfieOptions = ['beach1', 'changingroom1', 'bedroom1', 'bedroom2', 'homebathroom1']
        sarah.wakeUpOptions = ['handjob']
        sarah.dateChats = ['Background', 'Studies', 'Hobbies']
        sarah.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = sarah.events[-1]
        sarah.maxLike = lastStoryEvent.requiredLike
        sarah.maxLove = lastStoryEvent.requiredLove

        # World attributes
        sarah.preferredMondaySchedule = [location_park, location_college, location_town, location_away]
        sarah.preferredTuesdaySchedule = [location_college, location_college, location_beach, location_away]
        sarah.preferredWednesdaySchedule = [location_college, location_college, location_diner, location_town]
        sarah.preferredThursdaySchedule = [location_park, location_cafe, location_town, location_away]
        sarah.preferredFridaySchedule = [location_shop, location_college, location_bar, location_bar]
        sarah.preferredSaturdaySchedule = [location_park, location_beach, location_bar, location_bar]
        sarah.preferredSundaySchedule = [location_town, location_cafe, location_beach, location_beach]

        sarah.preferredMovedInMondaySchedule = [location_home, location_college, location_home, location_home]
        sarah.preferredMovedInTuesdaySchedule = [location_college, location_college, location_home, location_home]
        sarah.preferredMovedInWednesdaySchedule = [location_college, location_college, location_home, location_home]
        sarah.preferredMovedInThursdaySchedule = [location_home, location_home, location_home, location_home]
        sarah.preferredMovedInFridaySchedule = [location_home, location_college, location_bar, location_home]
        sarah.preferredMovedInSaturdaySchedule = [location_home, location_home, location_bar, location_home]
        sarah.preferredMovedInSundaySchedule = [location_home, location_home, location_beach, location_home]
    return

# Sprites
screen sarahClickable(xcenter):
    $ spriteload = sarah.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = sarah)
        at characterSpriteHover

# Character methods
label sarahEvaluateAvailableInteractions:
    python:
        if sarah.like >= 5:
            sarah.availableActions = list(set(sarah.availableActions + ['Spend time']))
        if sarah.like >= 20 and sarahHEvent2.unlocked:
            sarah.availableActions = list(set(sarah.availableActions + ['Invite over']))

        if sarah.isDateable and sarah.like >= 1:
            sarah.availableActions = list(set(sarah.availableActions + ['Date']))
        if sarah.love >= 3:
            sarah.availableActions = list(set(sarah.availableActions + ['Affection']))
            sarah.availableAffections.extend(['Pat'])
        if sarah.love >= 6:
            sarah.availableAffections.extend(['Hug', 'Chin Scratch'])
        if sarah.love >= 10 and (sarahLikeEvent3.unlocked or sarahHEvent1.unlocked):
            sarah.availableAffections.extend(['Kiss'])
        if sarahHEvent4.unlocked:
            sarah.availableAffections.extend(['Caress Butt'])
        if sarahHEvent5.unlocked:
            sarah.availableActions.extend([{'homebathroom': ['Doggy Style']}])
        if sarahHEvent6.unlocked:
            sarah.availableAffections.extend(['Boob Grab'])
        if sarahHEvent7.unlocked:
            sarah.availableActions.extend([{'homelounge': ['Reverse Cowgirl']}])
        if sarah.movedIn:
            sarah.availableCommandsPrivate.extend(['Show Panties'])
            sarah.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label sarahChat:
    show sarah smile talk
    return

label sarahChat_beach:
    show sarah joy
    sarah.c "Эй! Купаться собралась?"
    return

label sarahChat_park:
    show sarah smile talk
    sarah.c "Решила прогуляться."
    return

label sarahChat_shop:
    show sarah tease talk
    sarah.c "Тут самые вкусные шашлычки."
    return

label sarahChat_diner:
    show sarah bashful talk
    sarah.c "Не могу часто себе это позволить..."
    show sarah joy
    sarah.c "Но сегодня я это заслужила!"
    return

label sarahChat_cafe:
    show sarah tease talk
    sarah.c "Ого... Какие булочки..."
    return

label sarahChat_town:
    if (sarahHEvent3.unlocked):
        show sarah joy
        sarah.c "Привет! [mc.name]! Чем занимаешься?" 
    else:
        show sarah smile talk 2
        sarah.c "Вот это встреча!"
    return

label sarahChat_bar:
    show sarah thinking
    sarah.c "Хм... Что бы мне взять?"
    show sarah joy
    sarah.c "Может, удивишь меня, [mc.name]?"
    return

label sarahChat_aquarium:
    show sarah smile talk 2
    sarah.c "Ха-ха, да посмотри на них!"
    show sarah sad talk
    sarah.c "Наверное, сейчас не стоит думать о еде..."
    return

label sarahChat_theater:
    show sarah smile talk 2
    sarah.c "О, привет, чувак!"
    show sarah smile talk
    sarah.c "Захотелось в кино. Что собираешься смотреть?"
    return

label sarahChat_homebedroom:
    if(timeOfDay == 'Morning'):
        show sarah smile talk 2
        sarah.c "Ну что, соня?"
    elif(timeOfDay == 'Afternoon'):
        show sarah tease talk
        sarah.c "У меня сейчас нет занятий. Может, куда-нибудь сходим?"
    elif(timeOfDay == 'Evening'):
        show sarah tease talk 
        sarah.c "Это? Э-э... Исследования! Точно!"
    elif(timeOfDay == 'Night'):
        show sarah surprise
        sarah.c "Ого, уже так поздно? Чёрт. Ляжем спать?"
    return

label sarahChat_homelounge:
    if(timeOfDay == 'Morning'):
        show sarah smile talk 2
        sarah.c "Доброе утро! Ну конечно, я уже встала! Я не всегда валяюсь до обеда..."
    elif(timeOfDay == 'Afternoon'):
        show sarah joy
        sarah.c "Поиграй со мной! Помоги пройти этот уровень..."
    elif(timeOfDay == 'Evening'):
        show sarah smile talk
        sarah.c "Чёрт, по телевизору ничего интересного. Есть идеи?"
    elif(timeOfDay == 'Night'):
        show sarah tease talk
        sarah.c "Погоди, дай ещё немного поиграть..."
    return

label sarahChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show sarah tease talk
        sarah.c "Привет, чувак! Я уже встала раньше тебя! О, это последнее молоко~"
    elif(timeOfDay == 'Afternoon'):
        show sarah smile talk 2
        sarah.c "Надо купить ещё еды для микроволновки, [mc.name], она всё время куда-то пропадает!"
    elif(timeOfDay == 'Evening'):
        show sarah bashful talk
        sarah.c "Готовь каждый вечер, ладно? Ты же знаешь, какая я..."
    elif(timeOfDay == 'Night'):
        show sarah tease talk
        sarah.c "Эй, я просто забыла поесть, ясно? Была занята~"
    return

# Date topics
label sarahChat_background:
    show sarah thinking
    sarah.c "Хм... Что бы рассказать?"
    show sarah neutral talk
    sarah.c "Ну... Я из соседнего городка. Выросла там, а сюда переехала только из-за колледжа."
    sarah.c "Семья у меня небольшая: я, родители и младший брат. Самое обычное детство в семье со скромным достатком."
    show sarah thinking
    sarah.c "Я их люблю, но всё-таки рада, что наконец съехала. Знаешь, захотелось самостоятельности."
    mc.c "Очень тебя понимаю."
    show sarah surprise
    sarah.c "Да, ты ведь издалека переехал? С другого конца страны!"
    mc.c "Ага. Как и ты, почувствовал, что пора что-то менять."
    show sarah smile talk
    sarah.c "Да, понимаю. Начать следующий этап жизни. Немного вытолкнуть себя в большой мир."
    show sarah bashful talk
    sarah.c "Иногда скучаю по ним. Езжу домой на праздники или они приезжают ко мне."
    show sarah smile talk
    sarah.c "Мой младший брат на шесть лет младше, всё ещё учится в школе. По нему я скучаю больше всего."
    show sarah smile talk 2
    sarah.c "Но в целом мне здесь очень нравится. Подружилась с ребятами в колледже, город классный, есть чем заняться."
    show sarah smile
    mc.c "Например, выпивать у меня в баре!"
    show sarah tease talk
    sarah.c "Ха-ха, это точно."
    return

label sarahChat_hobbies:
    show sarah thinking
    sarah.c "Ну-у-у..."
    show sarah smile talk
    sarah.c "В основном спортом. Не бегаю или вроде того. Люблю долгие прогулки, походы и всё такое."
    show sarah smile talk 2
    sarah.c "Знаешь, недалеко от центра есть отличные природные места. Удивишься."
    show sarah smile
    mc.c "Не знал. Я не так много исследовал окрестности, как стоило бы."
    show sarah smile talk
    sarah.c "Тебе точно надо. Может, как-нибудь сходим вместе. Тут неподалёку хорошие холмы и леса."
    show sarah smile
    mc.c "Сейчас я, наверное, совсем не в форме, но с радостью составлю тебе компанию."
    show sarah tease talk
    sarah.c "Ну ладно, тогда не буду тебя звать."
    show sarah tease
    mc.c "П-погоди..."
    show sarah tease talk
    sarah.c "Хе-хе~ Не переживай. Чтобы стать выносливее, надо просто начать. Может, тебе понравится."
    show sarah tease
    mc.c "...Ладно."
    show sarah thinking
    sarah.c "В общем, э-э..."
    show sarah smile talk
    sarah.c "А видеоигры считаются? В детстве я много играла, так что и сейчас иногда."
    show sarah smile
    mc.c "Конечно."
    show sarah thinking
    sarah.c "Я не прямо геймер, но люблю некоторые классические игры. Наверное, больше всего — файтинги."
    mc.c "Наверняка играл в какие-то из тех, о которых ты думаешь. Как-нибудь сразимся."
    show sarah tease talk
    sarah.c "Уверен? Я могу надрать тебе задницу."
    show sarah tease
    mc.c "Ладно, теперь точно должны как-нибудь сыграть... Не могу это так оставить."
    show sarah tease talk
    sarah.c "Посмотрим..."
    show sarah thinking
    sarah.c "Вот, наверное, и всё. Немного смотрю телевизор, люблю боевики, попробую любой спорт хотя бы раз..."
    show sarah tease talk
    sarah.c "Ну и хожу выпивать с друзьями, но ты это уже знаешь."
    show sarah tease
    mc.c "О да, мои любимые посетители."
    show sarah tease talk
    sarah.c "Пока что... Подожди, пока кто-нибудь опозорится. Такое обязательно случится."
    return

label sarahChat_studies:
    show sarah smile talk 2
    sarah.c "Ну, я учусь в колледже, изучаю географию. Точнее, физическую географию и экологию."
    sarah.c "Климат, рельеф, геология и всё такое."
    show sarah smile
    mc.c "Здорово. И кем хочешь стать? Есть цель или работа мечты?"
    show sarah bashful talk
    sarah.c "Э-э... Не особо..."
    show sarah neutral talk
    sarah.c "Звучит ужасно, но... Я просто плыла по течению."
    show sarah neutral
    mc.c "Плыла по течению — и поступила в университет?"
    show sarah bashful talk
    sarah.c "Ну, типа того... Большинство друзей после школы делали так же, вот и я..."
    show sarah smile talk
    sarah.c "Не подумай, мне нравится учёба. Я отношусь к ней {b}более-менее{/b} серьёзно."
    show sarah bashful talk
    sarah.c "Но я не горела этой специальностью и не строила планов на будущее..."
    sarah.c "Когда говорю это вслух, звучит глупо."
    show sarah bashful
    mc.c "Но сейчас тебе нравится?"
    show sarah joy
    sarah.c "Да! Очень! Почти как в школе, только свободы больше."
    show sarah smile talk 2
    sarah.c "Денег только мало, ха-ха."
    show sarah smile
    mc.c "Тогда, думаю, всё здорово. Просто наслаждайся..."
    show sarah joy
    sarah.c "Вот именно!"
    mc.c "...Пока можешь."
    show sarah sad talk
    sarah.c "Эх... Не надо было напоминать..."
    show sarah sad
    mc.c "Прости... Просто горький опыт взрослой жизни."
    show sarah tease talk
    sarah.c "Да я шучу, чувак. И перестань говорить как старик."
    show sarah tease
    mc.c "Ладно, а почему география?"
    show sarah smile talk
    sarah.c "Я не знала, куда поступать, понятно же. В школе я не представляла, кем хочу работать..."
    sarah.c "Просто выбрала предмет, который лучше всего давался. Один из немногих, что мне правда нравились."
    show sarah smile talk 2
    sarah.c "К тому же люблю природу: гулять, ходить в походы, смотреть на пейзажи и двигаться."
    show sarah thinking
    sarah.c "Хотя за это оценки не ставят."
    return

#

label sarahInteractionBathroom:
    sarah.c "Чувак, я тут!"
    sarah.c "Видишь что-нибудь интересное?"
    return

label sarahSpendTime(onDate = False):
    if(onDate):
        scene expression 'sarah[mc.currentLocation.apiName]date'
    else:
        scene expression 'sarah[mc.currentLocation.apiName]'
    with fade
    return

label sarahReceiveGift(item, likeChange, loveChange):
    show sarah neutral talk
    sarah.c "Для меня?"
    if(loveChange > 0):
        show sarah surprise
        sarah.c "Ого, правда? Мне очень нравится!"
        sarah.c "Огромное спасибо!"
        if(sarahVacation.unlocked):
            sarah.c "Люблю тебя!"
    elif(likeChange > 1):
        show sarah joy
        sarah.c "Как мило! Спасибо!"
        if(sarahVacation.unlocked):
            sarah.c "Люблю тебя!"
    elif(likeChange < 1):
        show sarah mad talk
        sarah.c "А? Ты шутишь, что ли?"
    else:
        show sarah smile talk
        sarah.c "Спасибо!"
        if(sarahVacation.unlocked):
            sarah.c "Люблю тебя!"
    return

label sarahReceiveDateInvitation:
    show sarah neutral talk
    sarah.c "Конечно! Когда хочешь пойти?"
    show sarah neutral
    call dateInvitationSelector(sarah) from _call_dateInvitationSelector_6
    show sarah neutral talk
    sarah.c "Ладно! Значит, [proposedDateDayOfWeek] в [proposedDateTime] в [proposedDateLocation.name]? До встречи!"

    python:
        scheduledDate = Date(sarah, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        sarah.scheduledDates.append(scheduledDate)
    return

label sarahStartDate:
    if(mc.currentLocation == location_home):
        show sarah tease with dissolve
        sarah.c "Хочешь, чтобы я была только твоей?"
    else:
        show sarah joy with dissolve
        sarah.c "Ты пришёл!"
    return

label sarahDateInteraction:
    show sarah smile with dissolve
    show screen dateUi(sarah) with dissolve
    call screen dateInteractionScreen(sarah, mc.currentLocation)

label sarahChatDate:
    show sarah smile talk 2
    sarah.c "Мне это сегодня было нужно, спасибо!"
    return

label sarahChatDate_beach:
    show sarah joy
    sarah.c "Кто последний в воде — тот лох!"
    show sarah surprise
    sarah.c "А? Моя одежда? Ой, точно!"
    return

label sarahChatDate_park:
    show sarah thinking
    sarah.c "Хочешь взять что-нибудь в автомате?"
    return

label sarahChatDate_diner:
    show sarah joy
    sarah.c "Блин, как вкусно!"
    show sarah tease talk
    sarah.c "О-о~ Но и у тебя выглядит аппетитно. Дай попробовать..."
    return

label sarahChatDate_cafe:
    show sarah surprise
    sarah.c "Чёрт, крепкая штука!"
    sarah.c "Сегодня всю ночь не усну."
    return

label sarahChatDate_bar:
    show sarah tease talk
    sarah.c "Ещё по одной, бармен!"
    show sarah tease
    sarah.c "Не смотри на меня так. Давай, [mc.name]!"
    return

label sarahChatDate_aquarium:
    show sarah joy
    sarah.c "Ого, сколько их!"
    show sarah surprise
    sarah.c "Смотри на этого! Какой странный!"
    return

label sarahChatDate_theater:
    show sarah joy
    sarah.c "Ой-ой! Я давно хотела посмотреть этот фильм!"
    show sarah tease talk
    sarah.c "Попкорн возьмём, да?"
    return

label sarahDatePayFor:
    show sarah joy
    sarah.c "Спасибо, чувак!"
    show sarah smile talk 2
    sarah.c "Не обязательно за всё платить, знаешь ли."
    return

label sarahEndDate:
    if(dateScore < 40):
        show sarah sad 
        sarah.c "День сегодня так себе... Прости..."
    else:
        if(sarah.movedIn):
            show sarah joy
            sarah.c "Я бы не отказалась чаще ходить с тобой на свидания, [mc.name]!"
        else:
            show sarah joy
            sarah.c "Давай скоро повторим, ладно?"
        if(sarahVacation.unlocked):
            sarah.c "Люблю тебя!"
    return

label sarahContinueDateAtHome:
    scene expression 'sarah[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(sarahHEvent1.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label sarahHomeStartSex:
    show sarah tease talk
    sarah.c "Чёрт, чувак, когда ты уже остановишься?"
    sarah.c "Ладно... Я тоже хочу~"
    show sarah tease
    return

label sarahHomeSexJoinIn(character):
    show sarah smile talk 2 at twoPersonLeft with dissolve
    sarah.c "Эй... Можно я тоже присоединюсь~?"
    show sarah smile
    return

label sarahEndDateAtHome:
    sarah.c "Спасибо, что пригласил! Увидимся!"
    return

image sarah pat animated = Movie(play="images/characters/sarah/affections/sarahPat.webm", side_mask=True, loop=True)
label sarahReceivePat:
    hide sarah with dissolve
    show sarah pat animated with dissolve
    pause
    if(sarahHEvent3.unlocked):
        sarah.c "Хе-х~ [mc.name]!"
        sarah.c "Не останавливайся..."
    else:
        sarah.c "Эй, кто разрешил тебе так делать..."
        sarah.c "Ну, я не особо против..."
    return

image sarah chinscratch animated = Movie(play="images/characters/sarah/affections/sarahChinscratch.webm", side_mask=True, loop=True)
label sarahReceiveChinScratch:
    hide sarah with dissolve
    show sarah chinscratch animated with dissolve
    pause
    sarah.c "О-о-о~"
    sarah.c "На самом деле очень приятно."
    return

image sarah caressbutt animated = Movie(play="images/characters/sarah/affections/sarahCaressButt.webm", side_mask=True, loop=True)
label sarahReceiveCaressButt:
    hide sarah with dissolve
    show sarah caressbutt animated with dissolve
    pause
    sarah.c "Что, чувак, нашёл там что-то интересное?"
    sarah.c "Хе-х~ Ладно, но тогда и мне достанется такое же удовольствие~"
    return

image sarah boobgrab animated = Movie(play="images/characters/sarah/affections/sarahBoobGrab.webm", side_mask=True, loop=True)
label sarahReceiveBoobGrab:
    hide sarah with dissolve
    show sarah boobgrab animated with dissolve
    pause
    sarah.c "О-о~ Что это? А кто сказал, что за грудь можно хватать?"
    sarah.c "Боже, ну ты и мужик~"
    return

image sarah snuggle animated = Movie(play="images/characters/sarah/affections/sarahSnuggle.webm", side_mask=True, loop=True)
label sarahReceiveSnuggle:
    "Я откидываюсь на диван и раскрываю объятия, приглашая Сару."
    show sarah smile talk
    sarah.c "Ленишься, чувак?"
    hide sarah with dissolve
    show sarah snuggle animated with dissolve
    pause
    "Сара плюхается мне на грудь и кладёт голову."
    sarah.c "Ладно, полежу с тобой. Ты вообще-то удобный~"
    pause
    return

label sarahReceiveHug:
    hide sarah with dissolve
    show sarah hug with dissolve
    pause
    sarah.c "Обними меня, здоровяк."
    if(sarahVacation.unlocked):
        sarah.c "М-м-м~ Крепче~"
    else:
        sarah.c "Ты такой сентиментальный, знаешь?"
    return

label sarahReceiveKiss:
    hide sarah with dissolve
    show sarah kiss with dissolve
    pause
    sarah.c "*Чмок*"
    if(sarahHEvent3.unlocked):
        sarah.c "Как мило~"
    if(sarahVacation.unlocked):
            sarah.c "Люблю тебя, [mc.name]~"
    else:
        sarah.c "Немного неловко..."
    return

label sarahInitiatePat:
    show sarah bashful talk with dissolve
    sarah.c "Можешь... ну, ты знаешь..."
    sarah.c "Сделать эту штуку?"
    "[sarah.name] ёрзает на месте и не слишком тонко кивает в мою сторону."
    hide sarah with dissolve
    show sarah pat animated with dissolve
    pause
    sarah.c "М-м-м..."
    sarah.c "Не знаю почему, но... когда ты так делаешь, мне очень хорошо."
    return

label sarahInitiateHug:
    show sarah joy with dissolve
    if(sarahVacation.unlocked):
        sarah.c "[mc.name]~ Обними меня!"
    else:
        sarah.c "Эй, чувак! Давай сюда!"
    hide sarah with dissolve
    show sarah hug with dissolve
    pause
    return

label sarahInitiateKiss:
    show sarah tease talk with dissolve
    sarah.c "Эй..."
    hide sarah with dissolve
    show sarah kiss with dissolve
    sarah.c "*Чмок*"
    pause
    hide sarah with dissolve
    show sarah smile with dissolve
    sarah.c "Попался!"
    return

label sarahInitiateSnuggle:
    show sarah tease talk
    sarah.c "[mc.name]~ Удобно устроился?"
    show sarah tease
    "Сара присаживается рядом и прижимается ко мне."
    hide sarah with dissolve
    show sarah snuggle animated with dissolve
    pause
    "Она беззаботно укладывается на меня всем телом."
    sarah.c "А-а~ Вот это кайф. Ты отличная подушка~"
    pause
    return

label sarahInitiateHomeSex:
    show sarah tease talk
    sarah.c "[mc.name]~?"
    sarah.c "Хочешь перепихнуться?"
    show sarah tease
    return

label sarahInitiateHomeSexDeny:
    show sarah mad talk
    sarah.c "А? Парень, потом я тебе устрою..."
    return

label sarahSeesAffection(affection):
    show sarah smile talk with dissolve
    sarah.c "Эй, я тоже хочу присоединиться!"
    show sarah smile
    mc.c "Иди сюда..."
    call expression 'sarahReceive' + affection from _call_expression_43
    hide sarah with dissolve
    return

label sarahInviteOver:
    show sarah tease
    sarah.c "О-о-о~? Чем займёмся у тебя?"
    return

label sarahInitiateInviteOver:
    show sarah smile talk 2
    sarah.c "Эй, ты занят? Можно я зайду к тебе?"
    show sarah smile
    menu:
        'Да':
            show sarah smile talk
            sarah.c "Класс!"
            return True
        'Нет':
            show sarah neutral talk
            sarah.c "Ладно, без проблем."
    return False

label sarahInviteGoHomeTogether:
    show sarah smile talk 2
    sarah.c "Конечно, пошли!"
    show sarah tease talk
    sarah.c "Может, поиграем, когда вернёмся? Хе-х~"
    return

label sarahInitiateGoHomeTogether:
    show sarah smile talk 2
    sarah.c "Я уже вымоталась. Пойдём домой?"
    show sarah smile
    menu:
        'Да':
            show sarah joy
            sarah.c "Класс~!"
            return True
        'Нет':
            show sarah smile talk 2
            sarah.c "Без проблем, увидимся дома~"
    return False

label sarahShowPanties(pantiesIndex = 1):
    show sarah tease talk
    sarah.c "О-о~? Хочешь посмотреть? Знаешь, я даже не помню."
    hide sarah with dissolve
    $ renpy.show(sarah.apiName + ' panties ' + str(pantiesIndex), tag=sarah.apiName)
    with dissolve
    if(pantiesIndex == 1):
        sarah.c "Да это обычные трусики... Не понимаю, почему тебя так волнует."
    elif(pantiesIndex == 2):
        sarah.c "А, эти... Э-э... Я взяла их для особого случая... Наверное..."
    elif(pantiesIndex == 3):
        sarah.c "Ой, чёрт! Кажется, это были самые несвежие трусики, что нашлись!"
        sarah.c "Не знаю, зачем я их купила... Такие неудобные..."
    return

label sarahSendDateText(proposedDate):
    python:
        sarah.textChain.append(Message(mc, sarah, 'Эй, чувак, хочешь завтра погулять?', Null, day, timeOfDay))
        sarah.textChain.append(Message(mc, sarah, 'Я подумала... ' + proposedDateTime.lower() + ' @ ' + proposedLocation.name.lower() + '?', Null, day, timeOfDay, proposedDate))
    return

label sarahGetSelfieOptions:
    $ sarahSelfieOptions = []
    if(sarahLikeEvent2.unlocked):
        $ sarahSelfieOptions.extend(['beach1'])
    if(sarahHEvent1.unlocked):
        $ sarahSelfieOptions.extend(['changingroom1'])
    if(sarahHEvent2.unlocked):
        $ sarahSelfieOptions.extend(['bedroom1', 'bedroom2'])
    if(sarah.movedIn):
        $ sarahSelfieOptions.extend(['homebathroom1'])
    return sarahSelfieOptions

label sarahSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'beach1':
                potentialResponses.append({'text': "Отлично выглядишь!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Вот бы я был сейчас рядом", 'statChange': 'love', 'statChangeAmount': 1})
                sarah.textChain.append(Message(mc, sarah, 'Пляжный денёк, знаю, тебе нравится ;)', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'changingroom1':
                potentialResponses.append({'text': "Выглядит здорово! Не стесняйся!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Вот это да! Давай, давай, давай!", 'statChange': 'love', 'statChangeAmount': 1})
                sarah.textChain.append(Message(mc, sarah, 'Пошла за бельём. Слишком много, да?', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom1':
                potentialResponses.append({'text': "Ну ты и дразнилка...", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Не заставляй меня туда приезжать", 'statChange': 'love', 'statChangeAmount': 1})
                sarah.textChain.append(Message(mc, sarah, 'Скучно.', Null, day, timeOfDay))
                sarah.textChain.append(Message(mc, sarah, 'Я тоже голая ;р', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom2':
                potentialResponses.append({'text': "ГРУДЬ ГРУДЬ ГРУДЬ", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Опусти камеру... ещё чуть-чуть...", 'statChange': 'love', 'statChangeAmount': 1})
                sarah.textChain.append(Message(mc, sarah, 'Вышла из душа. Подумала, тебе захочется взглянуть', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homebathroom1':
                potentialResponses.append({'text': "У туалета, красотка", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Я тебя помою", 'statChange': 'love', 'statChangeAmount': 1})
                sarah.textChain.append(Message(mc, sarah, 'Чувак, нужен ещё шампунь', selfieName, day, timeOfDay, responses = potentialResponses))
    return

label sarahSexSelect:
    hide screen mainUi
    scene black with fade
    image sarah sex waiting = Movie(play="images/characters/sarah/hscenes/sexWaiting.webm")
    show sarah sex waiting with fade

    call screen sarahSexSelectScreen
    if(sarahHEvent3.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(sarah.movedIn):
            menu sarahSleepTogether:
                "Переспать с Сарой?"
                'Да':
                    sarah.c "Фух~ Я вымоталась~"
                    sarah.c "Спокойной ночи."
                    call characterSleepover(sarah) from _call_characterSleepover_12
                'Нет':
                    pass
        else:
            menu sarahStayTheNight:
                "Предложить [sarah.name] остаться на ночь?"
                'Да':
                    $ sarah.addLove(1)
                    sarah.c "Да, было бы здорово."
                    call characterSleepover(sarah) from _call_characterSleepover_13
                'Нет':
                    sarah.c "Пока, здоровяк!"
    
    call endScene(character = sarah, targetLocation = location_home) from _call_endScene_14

screen sarahSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(sarahHEvent1.unlocked or persistent.debugMode):
                textbutton 'Mutual masturbation' keysym str(1):
                    action [Jump('sarahMutualMasturbation')]
            else:
                textbutton 'Locked'
            if(sarahHEvent2.unlocked or persistent.debugMode):
                textbutton 'Blowjob' keysym str(2):
                    action [Jump('sarahBlowjob')]
            else:
                textbutton 'Locked'
            if(sarahHEvent3.unlocked or persistent.debugMode):
                textbutton 'Doggy Style' keysym str(3):
                    action [Jump('sarahDoggyStyle')]
            else:
                textbutton 'Locked'
            if(sarahHEvent5.unlocked or persistent.debugMode):
                textbutton 'Shower Sex' keysym str(4):
                    action [Jump('sarahShowerSex')]
            else:
                textbutton 'Locked'
            if(sarahHEvent6.unlocked or persistent.debugMode):
                textbutton 'Makeout' keysym str(5):
                    action [Jump('sarahMakeout')]
            else:
                textbutton 'Locked'
            if(sarahHEvent6.unlocked or persistent.debugMode):
                textbutton 'Missionary' keysym str(6):
                    action [Jump('sarahMissionary')]
            else:
                textbutton 'Locked'
            if(sarahVacation.unlocked or persistent.debugMode):
                textbutton 'Cowgirl' keysym str(7):
                    action [Jump('sarahCowgirl')]
            else:
                textbutton 'Locked'
            if(sarahVacation.unlocked or persistent.debugMode):
                textbutton 'Petting / Spooning' keysym str(8):
                    action [Jump('sarahPettingSpooning')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(9):
                action [Hide('sarahSexSelectScreen'), Return()]

label sarahSleepover:
    scene sarahsleepover with fade
    pause
    return

label sarahMorningBedInteraction:
    scene sarahhomemorning with fade 
    pause
    if(sarah.movedIn):
        sarah.c "*Зевает*~ Уже встал, чувак?"
        sarah.c "Я ещё немного посплю..."
        sarah.c "Хорошего дня. Люблю тебя."
    else:
        sarah.c "*Зевает*~"
        sarah.c "А-а~ Доброе утро, [mc.name]..."
        sarah.c "Дай мне ещё... пару минут..."
    return

label sarahMorningBedInteractionSex(event):
    if(event == 'handjob'):
        image sarah morning handjob 1 = Movie(play="images/characters/sarah/hscenes/morning/handjob1.webm")
        show sarah morning handjob 1 with fade
        pause
        sarah.c "Йо!"
        mc.c "Чем занимаешься?"
        sarah.c "Твой дружок проснулся раньше тебя."
        sarah.c "Он выглядел одиноким, вот я и решила с ним пообщаться."
        mc.c "Вот как? Изменяешь мне?"
        sarah.c "По твоему лицу видно, что ты не против."
        mc.c "Ну... ладно."
        image sarah morning handjob 2 = Image("images/characters/sarah/hscenes/morning/handjob2.webp")
        show sarah morning handjob 2 with fadewhite
        pause
        sarah.c "Чёрт, чувак, с самого утра!"
        sarah.c "Ты когда-нибудь останавливаешься?"
        mc.c "И кто в этом виноват?"
        sarah.c "Хе-хе~"
    return

# Sex scenes
label sarahMutualMasturbation:
    image sarah handjob part 1 = Movie(play="images/characters/sarah/hscenes/mutualMasturbation/part1.webm")
    show sarah handjob part 1 with fade
    pause
    image sarah handjob part 2 = Movie(play="images/characters/sarah/hscenes/mutualMasturbation/part2.webm")
    show sarah handjob part 2 with dissolve
    pause
    image sarah handjob end = Image("images/characters/sarah/hscenes/mutualMasturbation/end.webp")
    show sarah handjob end with fadewhite
    pause
    jump sarahSexSelect

label sarahBlowjob:
    image sarah blowjob part 1 = Movie(play="images/characters/sarah/hscenes/blowjob/part1.webm")
    show sarah blowjob part 1 with dissolve
    pause
    image sarah blowjob part 2 = Movie(play="images/characters/sarah/hscenes/blowjob/part2.webm")
    show sarah blowjob part 2 with dissolve
    pause
    image sarah blowjob part 3 = Movie(play="images/characters/sarah/hscenes/blowjob/part3.webm")
    show sarah blowjob part 3 with dissolve
    pause
    image sarah blowjob end = Image("images/characters/sarah/hscenes/blowjob/end.webp")
    show sarah blowjob end with fadewhite
    pause
    jump sarahSexSelect

label sarahDoggyStyle:
    image sarah doggy start1 = Movie(play="images/characters/sarah/hscenes/doggyStyle/start1.webm")
    show sarah doggy start1 with fade
    pause
    image sarah doggy start2 = Movie(play="images/characters/sarah/hscenes/doggyStyle/start2.webm")
    show sarah doggy start2 with fade
    pause
    image sarah doggy part1 = Movie(play="images/characters/sarah/hscenes/doggyStyle/part1.webm")
    show sarah doggy part1 with fade
    pause
    image sarah doggy part2 = Movie(play="images/characters/sarah/hscenes/doggyStyle/part2.webm")
    show sarah doggy part2 with fade
    pause
    image sarah doggy part3 = Movie(play="images/characters/sarah/hscenes/doggyStyle/part3.webm")
    show sarah doggy part3 with fade
    pause
    image sarah doggy end = Image("images/characters/sarah/hscenes/doggyStyle/end.webp")
    show sarah doggy end with fadewhite
    pause
    jump sarahSexSelect

label sarahShowerSex:
    image sarah shower doggy start 1 = Image("images/characters/sarah/hscenes/showerSex/start1.webp")
    show sarah shower doggy start 1 with fade
    pause
    image sarah shower doggy start 2 = Image("images/characters/sarah/hscenes/showerSex/start2.webp")
    show sarah shower doggy start 2 with fade
    pause
    image sarah shower doggy part 1 = Movie(play="images/characters/sarah/hscenes/showerSex/part1.webm")
    show sarah shower doggy part 1 with fade
    pause
    image sarah shower doggy part 2 = Movie(play="images/characters/sarah/hscenes/showerSex/part2.webm")
    show sarah shower doggy part 2 with fade
    pause
    image sarah shower doggy part 3 = Movie(play="images/characters/sarah/hscenes/showerSex/part3.webm")
    show sarah shower doggy part 3 with fade
    pause
    image sarah shower doggy part 4 = Movie(play="images/characters/sarah/hscenes/showerSex/part4.webm")
    show sarah shower doggy part 4 with fade
    pause
    image sarah shower doggy part 5 = Movie(play="images/characters/sarah/hscenes/showerSex/part5.webm")
    show sarah shower doggy part 5 with fade
    pause
    image sarah shower doggy part 6 = Movie(play="images/characters/sarah/hscenes/showerSex/part6.webm")
    show sarah shower doggy part 6 with fade
    pause
    image sarah shower doggy finish = Image("images/characters/sarah/hscenes/showerSex/finish.webp")
    show sarah shower doggy finish with fadewhite
    pause
    jump sarahSexSelect

label sarahMakeout:
    image sarah makeout part 1 = Movie(play="images/characters/sarah/hscenes/makeout/part1.webm")
    show sarah makeout part 1 with fade
    pause
    image sarah makeout part 2 = Movie(play="images/characters/sarah/hscenes/makeout/part2.webm")
    show sarah makeout part 2 with fade
    pause
    jump sarahSexSelect

label sarahMissionary:
    image sarah missionary start = Image("images/characters/sarah/hscenes/missionary/start.webp")
    show sarah missionary start with fade
    pause
    image sarah missionary part 1 = Movie(play="images/characters/sarah/hscenes/missionary/part1.webm")
    show sarah missionary part 1 with fade
    pause
    image sarah missionary part 2 = Movie(play="images/characters/sarah/hscenes/missionary/part2.webm")
    show sarah missionary part 2 with fade
    pause
    image sarah missionary part 3 = Movie(play="images/characters/sarah/hscenes/missionary/part3.webm")
    show sarah missionary part 3 with fade
    pause
    image sarah missionary part 4 = Movie(play="images/characters/sarah/hscenes/missionary/part4.webm")
    show sarah missionary part 4 with fade
    pause
    image sarah missionary part 5 = Movie(play="images/characters/sarah/hscenes/missionary/part5.webm")
    show sarah missionary part 5 with fade
    pause
    image sarah missionary end 1 = Image("images/characters/sarah/hscenes/missionary/end1.webp")
    show sarah missionary end 1 with fadewhite
    pause
    image sarah missionary end 2 = Image("images/characters/sarah/hscenes/missionary/end2.webp")
    show sarah missionary end 2 with fade
    pause
    jump sarahSexSelect

label sarahCowgirl:
    image sarah cowgirl 1 = Movie(play="images/characters/sarah/hscenes/cowgirl/part1.webm")
    show sarah cowgirl 1 with fade
    pause
    image sarah cowgirl 2 = Movie(play="images/characters/sarah/hscenes/cowgirl/part2.webm")
    show sarah cowgirl 2 with fade
    pause
    image sarah cowgirl 3 = Movie(play="images/characters/sarah/hscenes/cowgirl/part3.webm")
    show sarah cowgirl 3 with fade
    pause
    scene sarahcowgirlfinish with fadewhite
    pause
    jump sarahSexSelect

label sarahPettingSpooning:
    image sarah petting 1 = Movie(play="images/characters/sarah/hscenes/pettingSpooning/petting.webm")
    show sarah petting 1 with fade
    pause
    image sarah spooning 1 = Movie(play="images/characters/sarah/hscenes/pettingSpooning/spooning.webm")
    show sarah spooning 1 with fade
    pause
    jump sarahSexSelect

label sarahhomeloungeReverseCowgirl:
    image sarahFloorReverseCowgirl1 = Movie(play="images/characters/sarah/hscenes/floorReverseCowgirl/part1.webm")
    scene sarahFloorReverseCowgirl1 with fade
    pause
    image sarahFloorReverseCowgirl2 = Movie(play="images/characters/sarah/hscenes/floorReverseCowgirl/part2.webm")
    scene sarahFloorReverseCowgirl2 with fade
    pause
    image sarahFloorReverseCowgirl3 = Movie(play="images/characters/sarah/hscenes/floorReverseCowgirl/part3.webm")
    scene sarahFloorReverseCowgirl3 with fade
    pause
    scene sarahfloorreversecowgirlfinish1 with fadewhite
    pause
    scene sarahfloorreversecowgirlfinish2 with fade
    pause
    return

label sarahhomebathroomDoggyStyle:
    image sarah shower doggy start 2 = Image("images/characters/sarah/hscenes/showerSex/start2.webp")
    show sarah shower doggy start 2 with fade
    pause
    image sarah shower doggy part 1 = Movie(play="images/characters/sarah/hscenes/showerSex/part1.webm")
    show sarah shower doggy part 1 with fade
    pause
    image sarah shower doggy part 2 = Movie(play="images/characters/sarah/hscenes/showerSex/part2.webm")
    show sarah shower doggy part 2 with fade
    pause
    image sarah shower doggy part 3 = Movie(play="images/characters/sarah/hscenes/showerSex/part3.webm")
    show sarah shower doggy part 3 with fade
    pause
    image sarah shower doggy part 4 = Movie(play="images/characters/sarah/hscenes/showerSex/part4.webm")
    show sarah shower doggy part 4 with fade
    pause
    image sarah shower doggy part 5 = Movie(play="images/characters/sarah/hscenes/showerSex/part5.webm")
    show sarah shower doggy part 5 with fade
    pause
    image sarah shower doggy part 6 = Movie(play="images/characters/sarah/hscenes/showerSex/part6.webm")
    show sarah shower doggy part 6 with fade
    pause
    image sarah shower doggy finish = Image("images/characters/sarah/hscenes/showerSex/finish.webp")
    show sarah shower doggy finish with fadewhite
    pause
    return

# Events
default sarahFirstMeetingEvent = Event('Первая встреча', 'sarahFirstMeeting', [sarah], 0, 0, [], location_park, triggerDay = 1)
default sarahLikeEvent1 = Event('Первый раунд за мой счёт', 'sarahLikeEvent1', [sarah], 10, 0, [sarahFirstMeetingEvent], location_bar)
# Makes her dateable
default sarahLikeEvent2 = Event('День на пляже', 'sarahLikeEvent2', [sarah], 20, 0, [sarahLikeEvent1], location_beach, ['Morning', 'Afternoon', 'Evening'])
# Mutual masturbation
default sarahHEvent1 = Event('Немного веселья', 'sarahHEvent1', [sarah], 25, 5, [sarahLikeEvent2], location_bar)
# First kiss
default sarahLikeEvent3 = Event('Поход', 'sarahLikeEvent3', [sarah], 30, 10, [sarahHEvent1], location_town, ['Morning', 'Afternoon'])
# Blowjob
default sarahHEvent2 = Event('Навеселе', 'sarahHEvent2', [sarah], 40, 15, [sarahLikeEvent3], location_bar)
# First sex (doggy). First stay the night.
default sarahHEvent3 = Event('Признание', 'sarahHEvent3', [sarah], 50, 20, [sarahHEvent2], location_home, ['Evening', 'Night'])
# Footjob under diner table
default sarahHEvent4 = Event('Довести до конца', 'sarahHEvent4', [sarah], 60, 25, [sarahHEvent3], location_diner)
# Shower sex
default sarahHEvent5 = Event('Слишком соблазнительно', 'sarahHEvent5', [sarah], 70, 30, [sarahHEvent4], location_beach, ['Morning', 'Afternoon'])
# Kissing missionary
default sarahHEvent6 = Event('Традиционные качества', 'sarahHEvent6', [sarah], 80, 35, [sarahHEvent5], location_town, ['Morning', 'Afternoon', 'Evening'])
# Hiking camping vacation
default sarahVacation = Event('Ночь в лесу', 'sarahVacation', [sarah], 90, 40, [sarahHEvent6], Null, extraNotes = 'Организуй отпуск. Специальный пункт в меню взаимодействия.', cost=500, requiredItems = [item_car], requiresInvite = True)
# Children talk
default sarahLikeEvent4 = Event('Малыш', 'sarahLikeEvent4', [sarah], 100, 45, [sarahVacation], location_home)
# Move in invite + event
default sarahLikeEvent5 = Event('Переезд', 'sarahLikeEvent5', [sarah], 110, 50, [sarahLikeEvent4], Null, extraNotes = 'Отношения становятся серьёзными. Готовы ли мы к следующему шагу?\nСпециальный пункт в меню взаимодействия.', requiredItems = [item_car], requiresInvite = True)
# Lounge strip gaming cowgirl
default sarahHEvent7 = Event('Здоровое соперничество', 'sarahHEvent7', [sarah], 120, 60, [sarahLikeEvent5], location_home_lounge, mcInitiated = True)

label sarahFirstMeeting(fromGallery):
    $ location_park.showBackground()
    $ sarah.knownToMC = True
    hide sarah
    "В свободное время я много гулял без особой цели."
    "И это приятно. По городу хорошо гулять. Даже обычные жилые улицы красивые и чистые. Центр не похож на забитую людьми дыру, как в некоторых местах."
    "Тут много парков, как этот. Одни зеленее других, но за всеми ухаживают, и в них приятно спокойно посидеть."
    "Я часто гуляю здесь. Рядом пляж, отсюда приятно идти домой или в бар. Хорошее место, чтобы отключиться от всего."
    "Завернув за угол, я замечаю знакомое лицо, идущее навстречу."
    show sarah smile talk with dissolve
    call playMusic(funnyTheme) from _call_playMusic_206
    sarah.c "О, привет! Ты же из бара. Э-э..."
    mc.c "[mc.name]."
    sarah.c "Точно! [mc.name]! Как дела?"
    mc.c "Хорошо, спасибо. Просто осматриваюсь."
    show sarah smile talk 2
    sarah.c "Ага? Ты тут неподалёку живёшь?"
    mc.c "Не совсем рядом, но в свободное время много гуляю по городу. Изучаю местность, да и помогает расслабиться."
    mc.c "А ты? Живёшь неподалёку?"
    sarah.c "Да, недалеко. Обычно хожу этой дорогой в колледж и обратно."
    mc.c "А, точно. Терри говорил, что вы учитесь. На кого?"
    show sarah bashful talk
    sarah.c "На географа. Не сказала бы, что у меня всё хорошо или что я этим сильно увлечена. Выбрала, потому что люблю природу, походы и всё такое."
    show sarah smile talk 2
    sarah.c "Просто нужно было чем-то заняться. А остальное мне нравится: одногруппники классные, есть кружки и всякое такое."
    show sarah smile talk
    sarah.c "Ты ведь недавно приехал? Откуда ты вообще?"
    mc.c "Из Ренсала, он на другом конце страны."
    show sarah smile talk 2
    sarah.c "Кажется, слышала о нём. Далеко, да? И теперь ты управляешь баром?"
    mc.c "Мой прежний начальник был знаком с Терри. Я какое-то время работал у него, а когда Терри решил уйти, тот замолвил за меня словечко."
    show sarah surprise
    sarah.c "Ничего себе! Для такого молодого человека это впечатляет. И ты переехал ради работы..."
    mc.c "Сначала сомневался, но хотел больших перемен. Дома стало скучно. Решил, что это шанс начать всё сначала."
    show sarah thinking
    sarah.c "Понимаю. Хорошая возможность, наверное."
    show sarah neutral talk
    sarah.c "Ну что, нравится здесь?"
    mc.c "Пока всё хорошо. И квартира за такую цену отличная. Дома очень дорого, поэтому и пришлось переехать."
    mc.c "Я пока не успел толком всё осмотреть. Здорово, что здесь есть пляж."
    show sarah joy
    sarah.c "Ага, он классный! Одно из моих любимых мест."
    show sarah neutral talk
    sarah.c "Ты уже кого-нибудь здесь знал?"
    mc.c "К сожалению, нет. Немного знакомлюсь с сотрудниками бара, Терри помогает с разными делами, но это всё."
    show sarah smile talk 2
    sarah.c "Не переживай, мы будем время от времени заходить. В следующий раз познакомлю тебя со всеми как следует."
    sarah.c "В нашем колледже почти нет людей, так что будет здорово, если ты не против."
    show sarah bashful talk
    sarah.c "Ой, прозвучало странно. Не хочу, чтобы казалось, будто мы на тебя глазеем."
    mc.c "Не переживай, понимаю. Дома я тоже почти не видел антро. В любом случае буду рад познакомиться со всеми, спасибо."
    mc.c "И я хочу заботиться о постоянных гостях, так что скажи, если что-то в баре стоит изменить."
    show sarah joy
    sarah.c "Класс! Обещаю, они все хорошие."
    show sarah smile talk 2
    sarah.c "Ладно, мне уже пора, надо заняться делами по колледжу. Рада была тебя увидеть."
    mc.c "И я, [sarah.name]. Приятно было встретиться. Ещё увидимся?"
    sarah.c "Конечно! Пока, [mc.name]!"

    if(not fromGallery):
        $ sarah.addLike(1)
    
    return

label sarahLikeEvent1(fromGallery = False):
    $ location_bar.showBackground()
    "Ещё один обычный день в баре. Дела идут медленно, а я всё ещё осваиваю тонкости управления."
    "Зато сотрудники молодцы. Они обслуживают гостей, а я могу заняться бухгалтерией."
    "Но иногда всё же беру смены. С такими дружелюбными посетителями приятно поболтать."
    "Кстати, в бар заходит знакомая компания молодых ребят."
    show sarah smile with dissolve
    call playMusic(funnyTheme) from _call_playMusic_207
    "[sarah.name] и несколько её друзей из колледжа заходят в бар."
    show sarah smile talk 2
    sarah.c "[mc.name]!"
    "Девушка подбегает к стойке, пока её компания устраивается за большим столом."
    sarah.c "Говорила же, что мы вернёмся!"
    mc.c "Рад вас снова видеть. Здорово, что пришла такая шумная компания. Что вам принести?"
    sarah.c "Да неважно, пойдём, я тебя со всеми познакомлю."
    show sarah smile
    "Она почти тащит меня к их столику. Некоторые лица знакомы с нашей первой встречи, но есть и новые."
    show sarah smile talk
    sarah.c "Это [mc.name]. Он занял место Терри и теперь всем баром управляет!"
    unknown "Привет."
    unknown "Здравствуй!"
    unknown "Йо."
    "Несколько человек приветствуют меня. Немного неловко, будто я новенький в школе."
    show sarah smile talk
    sarah.c "Он переехал сюда издалека, никого не знает, вот я и решила, что надо с ним подружиться!"
    show sarah smile
    "Если задуматься, довольно грустно."
    unknown "Добро пожаловать! [sarah.name] говорила, что вы познакомились. С тех пор всё уговаривала нас снова сюда прийти."
    unknown2 "Не переставала об этом говорить!"
    show sarah bashful talk
    sarah.c "Эй, я не так уж много об этом говорила..."
    "За столом раздаётся смех. Похоже, у неё репутация немного рассеянной и гиперактивной."
    show sarah smile
    mc.c "Спасибо всем, приятно познакомиться. Слышал, вы часто сюда ходите, так что спасибо, что заглянули сегодня."
    mc.c "Меня немного внезапно поставили на место Терри, так что давайте отметим — первый раунд за мой счёт."
    unknown2 "Ура!"
    unknown "Отлично!"
    show sarah joy
    sarah.c "Класс, спасибо!"
    "Я приношу этой компании их обычный заказ — пару кувшинов. Хочу подружиться с местными, ведь я здесь новенький."
    unknown "Спасибо, [mc.name]. Добро пожаловать в наш район."
    unknown2 "За тебя!"
    "Компания наливает напитки и чокается."
    show sarah smile talk 2
    sarah.c "Ага, спасибо, [mc.name], но тебе не стоило!"
    mc.c "Мне в радость. Хочу быть хорошим хозяином. Оставлю вас, отдыхайте."
    sarah.c "Ладно, но заходи к нам, когда будет время. Думаю, все будут рады с тобой познакомиться."
    mc.c "Обязательно, спасибо, [sarah.name]. Хорошего вечера."
    hide sarah with dissolve
    scene black with fade
    "В течение дня я успеваю поболтать с кем-то из компании. Некоторые учатся с [sarah.name], другие — друзья её друзей."
    "Кажется, компания хорошая. Рад, что они будут заходить, но просто познакомиться с ровесниками тоже приятно."
    $ location_bar.showBackground()
    "После хорошего вечера компания начинает расходиться. За столом остаются лишь несколько человек, включая [sarah.name]."
    "Мы встречаемся взглядами, и она подходит."
    show sarah joy with dissolve
    sarah.c "Классные ребята, да? Некоторые строят из себя крутых, но, думаю, кому-то просто интересно познакомиться с человеком."
    mc.c "Да, все кажутся хорошими. Спасибо, что позвала меня к вам. Приятно познакомиться с местными."
    show sarah smile talk
    sarah.c "Я не только ради бесплатной выпивки тебя позвала, честно. Но ты очень добрый, всем понравилось. Мы же студенты, иногда денег в обрез."
    mc.c "Мне не сложно, понимаю. Я и сам недавно был студентом."
    show sarah bashful
    "[sarah.name] на мгновение задумывается."
    show sarah neutral talk
    sarah.c "Некоторые из нас иногда ходят на пляж. Не все, и я иногда гуляю там одна, когда есть свободное время."
    sarah.c "Как-нибудь пойдём вместе. Ты любишь плавать?"
    mc.c "Конечно, хотя дома у меня редко была такая возможность."
    show sarah smile talk
    sarah.c "Здорово, будет весело! Погуляем, когда будет хорошая погода."
    mc.c "Отличная идея, спасибо за приглашение."
    show sarah joy
    sarah.c "Ага, класс! Ещё увидимся!"
    mc.c "Увидимся!"
    hide sarah with dissolve
    "Последние ребята выходят, оставляя после себя заряд энергии. Делать особо нечего, пора заканчивать смену."
    "Похоже, я буду чаще видеться с [sarah.name]."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)

    return

label sarahLikeEvent2(fromGallery = False):
    $ location_beach.showBackground()
    call playMusic(heartTheme) from _call_playMusic_208
    "Прекрасный день. Самое время расслабиться на пляже."
    "Послушать волны, почувствовать бриз и тепло солнца на коже."
    "Блаженство."
    "Ища место подальше от кромки воды, я замечаю знакомую собачью фигуру."
    "[sarah.name] сидит, обняв колени, и смотрит на море. Больше никого рядом нет."
    "Она говорила, что часто приходит сюда с друзьями, но сегодня, похоже, одна."
    mc.c "[sarah.name]! Привет."
    show sarah surprise with dissolve
    sarah.c "О, привет!"
    mc.c "Не хотел тебя пугать."
    show sarah smile talk
    sarah.c "Ничего страшного, просто задумалась. Как дела? Купаться собираешься?"
    show sarah smile
    mc.c "Не сегодня, просто хочу отдохнуть и насладиться видом."
    mc.c "А ты? Пришла с друзьями?"
    show sarah neutral talk
    sarah.c "Не, сегодня все заняты заданиями."
    mc.c "А ты нет?"
    show sarah bashful talk
    sarah.c "Ага... Наверное, надо бы. На следующей неделе сдавать работу, но я не могла сосредоточиться."
    sarah.c "Устала от этой учёбы. Решила всё равно прийти, чтобы немного от неё отвлечься."
    mc.c "Не возражаешь, если я присоединюсь?"
    show sarah smile talk 2
    sarah.c "Конечно! Садись."
    show sarah smile
    "Я устраиваюсь рядом с [sarah.name], на песчаном склоне подальше от воды."
    mc.c "Ты сама не купаешься?"
    show sarah smile talk
    sarah.c "Не, пришла спонтанно, без полотенца. Потом вся испачкаюсь, пока домой доберусь."
    show sarah tease talk
    sarah.c "Но соблазн велик..."
    show sarah smile
    "Её глаза блестят, когда волна накатывает на берег. Может, её так тянет к морю из-за каких-то глубоких собачьих инстинктов? Лучше не спрашивать."
    mc.c "Как учёба, если не считать это задание?"
    show sarah neutral talk
    sarah.c "Вроде нормально. На проходной балл хватит, но мне всё равно."
    sarah.c "Ничего из того, чем я занимаюсь, меня особо не увлекает. Справиться могу, но устаю и иногда думаю, зачем вообще этим занимаюсь."
    show sarah neutral
    mc.c "Понимаю тебя."
    show sarah neutral talk
    sarah.c "Ты говорил, что тоже учился в колледже?"
    show sarah neutral
    mc.c "Да, но бросил после первого курса."
    mc.c "Поступил, потому что не был готов сразу идти работать на полный день."
    mc.c "Думал, будет легче, чем оказалось. Учёба отнимала много времени, а я ещё подрабатывал барменом, чтобы заработать."
    mc.c "В итоге выбрал что-то общее про бизнес, но мне было неинтересно. В конце концов бросил."
    show sarah neutral talk
    sarah.c "Хм. Понимаю."
    show sarah neutral
    mc.c "Не говорю, что всем стоит бросать. Мне повезло со старой работой и возможностью получить бар. Очень повезло."
    show sarah neutral talk
    sarah.c "Не думаю, что брошу. Такое настроение проходит. В целом мне нравится проводить время, даже если просто с друзьями."
    show sarah neutral
    pause
    "Мы какое-то время обсуждаем наши впечатления от колледжа."
    "Похоже, ей просто нужно было выговориться."
    pause
    show sarah smile talk 2
    sarah.c "Хватит хандрить, я просто драматизирую. Мне нужна была передышка."
    sarah.c "Приятно было выговориться. Спасибо, [mc.name]."
    show sarah smile
    "Я оглядываюсь и замечаю киоск с прохладительными напитками."
    mc.c "Всё нормально. Хочешь мороженого?"
    call playMusic(funnyTheme) from _call_playMusic_209
    show sarah surprise
    sarah.c "Ты читаешь мои мысли!"
    "Мы встаём и идём к киоску за двумя порциями мороженого."
    mc.c "Я угощаю."
    show sarah joy
    sarah.c "Не откажусь. Спасибо, чувак! В следующий раз я угощаю."
    "[sarah.name] облизывает рожок, и большая капля мороженого остаётся у неё на кончике носа."
    show sarah smile talk 2
    sarah.c "Ой!"
    "Она пытается слизать каплю языком, но не дотягивается."
    mc.c "Ха-ха-ха."
    show sarah tease talk
    sarah.c "Чего смеёшься?"
    mc.c "Ты такая милая."
    show sarah bashful
    pause
    "..."
    "Я выпалил это немного невпопад. Не перегнул ли?"
    show sarah joy
    "[sarah.name] стирает остатки указательным пальцем и тут же вытирает их обо мне."
    sarah.c "Получай!"
    mc.c "Холодно!"
    sarah.c "Ха-ха-ха!"
    scene black with fade
    call stopMusic from _call_stopMusic_38
    pause
    $ location_beach.showBackground()
    "Мы доедаем мороженое и болтаем о всяких пустяках."
    "Кажется, между нами исчезла какая-то неловкость. Мы уже скорее друзья, чем просто знакомые."
    "Хотя с [sarah.name] это неудивительно — она очень дружелюбная."
    show sarah smile talk 
    sarah.c "Мне уже пора, но было здорово. Надо чаще встречаться."
    mc.c "Конечно. Может, как-нибудь сходим поесть или выпьем кофе? И в бар всегда можешь заглянуть."
    show sarah bashful
    sarah.c "Да, было бы здорово."
    show sarah smile talk 2
    sarah.c "Давай скорее!"
    mc.c "Обязательно."
    "[sarah.name] бежит вверх по песчаному склону и машет мне через плечо."
    "Кажется, сегодня мы стали ближе."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
        $ sarah.isDateable = True
        "Теперь можно приглашать [sarah.name] на свидания."

    return

label sarahHEvent1(fromGallery = False):
    call playMusic(barTheme) from _call_playMusic_210
    $ location_bar.showBackground()
    show sarah smile talk 2 with dissolve
    sarah.c "...преподаватель сильно разозлился на всю группу, а никто не хотел признаваться."
    sarah.c "Я не собиралась сдавать Майка, никто не собирался, но не понимаю, чего они так разозлились..."
    "[sarah.name] заглянула ко мне в бар, на этот раз одна — приятный сюрприз. Сказала, что просто хочет пообщаться."
    "Это моё рабочее место, и она, наверное, об этом не подумала, но мне всё равно. Это мой бар, и я здесь сам устанавливаю правила."
    "Она перекусила и поболтала со мной у стойки, пока я разливал напитки. Приятное разнообразие, да и компания у неё отличная."
    "Когда разговорится, её не остановить. Сегодня рассказывает о проделках, которые они с друзьями устраивают в колледже."
    "Я не осуждаю. По собственному опыту знаю, что иногда меньше всего на кампусе хочется учиться."
    "В последнее время мы часто проводим время вместе. Кажется, мы довольно сблизились."
    "Я точно испытываю к ней романтические чувства, но не хочу испортить дружбу, поторопившись."
    "Она со всеми очень дружелюбна. Возможно, дело только в этом — она просто такая."
    show sarah smile
    mc.c "Я уже почти закончил здесь. Не хочу торчать весь день."
    show sarah neutral talk
    sarah.c "О, ты домой?"
    show sarah sad talk
    sarah.c "Эх, и чем же мне теперь заниматься весь день?"
    show sarah sad
    mc.c "Чем захочешь. Я ещё не закрываюсь, могу налить тебе ещё, если хочешь."
    show sarah sad talk
    sarah.c "Эх... Мне было так хорошо..."
    show sarah bashful
    call playMusic(heartTheme) from _call_playMusic_211
    sarah.c "..."
    show sarah neutral talk
    sarah.c "Тебе нужно куда-то?"
    mc.c "Не, просто пойду домой. День был долгий. Может, почитаю или поиграю во что-нибудь."
    show sarah bashful
    pause
    "О чём она думает?"
    show sarah sad talk
    sarah.c "Ты ведь живёшь недалеко? Может, ты не против, если..."
    "...У неё ужасно получается строить из себя скромницу."
    mc.c "Хочешь зайти ко мне? Ты ведь ещё не видела мою квартиру?"
    show sarah smile talk
    sarah.c "Д-да, можно? Просто немного посидим?"
    mc.c "Конечно. Дай мне тут прибраться, и пойдём."
    show sarah joy
    sarah.c "Класс!"
    scene black with fade
    "Я передаю дела остальным сотрудникам, и мы выходим."
    $ location_home.showBackground()
    show sarah surprise with dissolve
    sarah.c "Ничего себе, у тебя очень здорово, [mc.name]!"
    "[sarah.name] оглядывается. Квартира не очень большая, но места достаточно, а состояние отличное."
    sarah.c "Всё такое современное. Наверное, аренда дорогая, да?"
    mc.c "Да, довольно, но бар приносит достаточно, так что справляюсь."
    mc.c "По крайней мере, здесь аренда дешевле, чем дома. Раньше я бы не смог позволить себе такое жильё."
    show sarah tease talk
    sarah.c "И неожиданно чисто, хе-хе-хе."
    show sarah tease
    mc.c "Да-да, я поддерживаю порядок. А что, у тебя дома разгром?"
    show sarah bashful talk
    sarah.c "Не настолько... Но жить вчетвером с соседями — так себе."
    show sarah bashful
    "[sarah.name] снимает жильё вместе с другими студентами. Я знаю, каково это: условия бывают ужасными."
    "Наверное, поэтому я ещё ни разу не был у неё."
    mc.c "Хочешь выпить?"
    show sarah smile
    sarah.c "Да, спасибо!"
    scene black with fade
    "Мы сидим перед телевизором, обсуждаем всякую ерунду на экране и просто болтаем о жизни."
    "Постепенно разговор затихает, и в комнате остаётся лишь тихое бормотание телевизора."
    $ location_home.showBackground()
    "В комнате повисает напряжение. Я поглядываю на [sarah.name]."
    show sarah bashful with dissolve
    "Кажется, она чего-то ждёт, но я слишком нервничаю, чтобы действовать. А вдруг я неправильно всё понял?"
    "Её рука лежит на диване рядом с моей."
    "Что у неё на лице написано?"
    "Собираюсь с духом и решаюсь."
    "Я медленно кладу несколько пальцев поверх её руки. Пути назад уже нет."
    sarah.c "..."
    "Неужели я?.."
    show sarah smile
    "Это хороший знак?"
    show sarah smile talk
    sarah.c "Ты мне тоже нравишься, [mc.name]."
    sarah.c "Просто я... плохо умею такое говорить. Прости... и спасибо..."
    show sarah smile
    mc.c "Э-э, да, понимаю..."
    "Между нами повисает неловкая пауза, но [sarah.name] убирает руку. Сначала я думаю, что она отстраняется, но..."
    "Она кладёт руку мне на бедро."
    show sarah smile talk
    sarah.c "Ты... хочешь?.."
    call playMusic(sexyTheme) from _call_playMusic_212
    show sarah tease talk
    sarah.c "Немного повеселиться?"
    show sarah bashful talk
    sarah.c "Я давно этого хотела..."
    show sarah bashful
    "Я на седьмом небе, но не знаю, что сказать. Кажется, нам проще выразить всё действиями."
    "Я тоже кладу руку ей на бедро, и мы решаемся сделать следующий шаг."
    "Она скользит рукой к моей промежности и нежно ласкает меня сквозь штаны."
    show sarah tease
    "Она озорно улыбается — ей явно нравится дразнить меня."
    "Я отвечаю тем же: провожу рукой между её ног и ласкаю сквозь короткие джинсовые шорты."
    sarah.c "О-о~"
    "После недолгих ласк я уже твёрдый и готов вырваться наружу."
    "Почувствовав, как всё накаляется, [sarah.name] расстёгивает ширинку."
    window hide
    image sarah handjob part 1 = Movie(play="images/characters/sarah/hscenes/mutualMasturbation/part1.webm")
    show sarah handjob part 1 with fade
    pause
    sarah.c "Ничего себе..."
    sarah.c "Это..."
    "Она на мгновение ошарашена. Надеюсь, размером, а не чем-то ещё..."
    "Но, кивнув, она берёт мой член в руку и нежно водит по нему вверх-вниз."
    "Ощущения ни с чем не сравнить: мягкая шерсть и фактура подушечек лап."
    "Даже её коготки выглядят соблазнительно — словно игра с опасностью."
    "Мы начинаем медленно и нежно ласкать друг друга, впервые исследуя тела и переходя границы."
    mc.c "У тебя такая приятная рука..."
    sarah.c "А у тебя т-тоже..."
    "Жар между её ног обволакивает мою руку. Иногда шерсть на её животе касается моего предплечья, и по спине бегут мурашки."
    "Мы какое-то время ласкаем себя друг перед другом, порой встречаясь взглядами и неловко хихикая."
    sarah.c "М-м-м..."
    sarah.c "Мне это было нужно."
    mc.c "Я тоже не отказался бы от такого предложения."
    "Желая большего, я ускоряюсь."
    image sarah handjob part 2 = Movie(play="images/characters/sarah/hscenes/mutualMasturbation/part2.webm")
    show sarah handjob part 2 with dissolve
    pause
    "Мы ускоряемся, наслаждение нарастает, и мы стонем от удовольствия."
    "Её грудь прижимается к моему предплечью, когда она наклоняется и хватается другой рукой за моё колено."
    sarah.c "А-а, вот так... быстрее..."
    "Под её шортами становится всё жарче и влажнее; она ёрзает ногами, прижимая мои пальцы."
    "[sarah.name] водит рукой по моему члену, касаясь кончиками пальцев удивительно нежно."
    "Удовольствие неописуемо."
    sarah.c "Да... Да-а-а..."
    window hide
    pause
    mc.c "Я сейчас..."
    sarah.c "И я... почти... не останавливайся."
    sarah.c "{b}А-а-а-а-а-а!{/b}"
    image sarah handjob end = Image("images/characters/sarah/hscenes/mutualMasturbation/end.webp")
    show sarah handjob end with fadewhite
    pause
    sarah.c "*Тяжело дышит*"
    mc.c "Ха... ха..."
    "Мы оба достигаем пика наслаждения и откидываемся на диван, хватая ртом воздух."
    sarah.c "Ха-а, а-а..."
    "Несколько мгновений мы просто прислушиваемся, как утихает волна наслаждения. Наши руки всё ещё лежат у друг друга на коленях."
    "Я нежно взъерошиваю шерсть на бедре [sarah.name], а она коготком рисует круги у меня на ноге."
    mc.c "Это было потрясающе."
    sarah.c "Д-да... точно."
    "Мы переглядываемся с виноватыми улыбками. Неловкость ещё осталась, но теперь она общая."
    pause
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_213
    show sarah tease talk with dissolve
    sarah.c "Здорово, да?"
    mc.c "Ещё бы. Похоже, тебе тоже понравилось."
    sarah.c "Очень~"
    "Мы наслаждаемся моментом, а [sarah.name] поглядывает на часы."
    show sarah bashful talk
    sarah.c "Наверное, мне пора. Я и так отняла у тебя достаточно времени."
    mc.c "Отняла? Ни капли."
    show sarah tease talk
    sarah.c "Ну, в итоге мы хорошо провели время, правда?"
    mc.c "С тобой всегда хорошо. Но это уже новый этап."
    show sarah bashful talk
    sarah.c "Ох, какой ты сладкоречивый..."
    show sarah neutral talk
    sarah.c "Ты классный. Надеюсь, тебе не кажется странным то, что мы сделали."
    show sarah neutral
    mc.c "Да брось! Что ты такое говоришь? Я только за."
    show sarah neutral talk
    sarah.c "Может, это... когда-нибудь повторится?"
    show sarah neutral
    mc.c "Буду ждать."
    show sarah tease talk
    sarah.c "Я тоже."
    show sarah tease
    "День выдался суматошным. Утром я ещё гадал, нравлюсь ли [sarah.name]."
    "Всё закрутилось так быстро. Мы часто проводили время вместе, но скорее по-дружески."
    "И вместо признания или поцелуя мы ласкаем друг друга?"
    "Может, это просто несерьёзный роман. Возможно, попытка построить что-то серьёзное всё испортит."
    show sarah tease talk
    sarah.c "Скоро увидимся, ладно?"
    show sarah tease
    mc.c "Конечно, [sarah.name]. В следующий раз сыграем вместе — я видел, как ты поглядывала на мою приставку."
    show sarah tease talk
    sarah.c "Хе-хе, ага."
    sarah.c "Пока, чувак."
    hide sarah with dissolve
    "Я закрываю дверь за [sarah.name], и на лице у меня глупая улыбка."
    "Вот это да."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return {'location':location_home}

label sarahLikeEvent3(fromGallery = False):
    if(sarahHEvent2.unlocked):
        ofkeres "Если вы читаете это, значит, вы прошли будущие события в этом сохранении."
        ofkeres "Теперь это событие происходит раньше — между событиями «Немного веселья» и «Навеселе»."
        ofkeres "Из-за этого некоторые моменты могут казаться не по порядку. Но так история лучше воспринимается с самого начала."
        ofkeres "В предыдущем событии «Немного веселья» тоже есть небольшие изменения. Возможно, стоит переиграть его через телефон."
        ofkeres "Приятной игры!"

    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_214
    "Просто гуляю по городу, заняться нечем."
    "Дома было скучно, в баре и без меня всё в порядке. Сегодня работать тоже не хотелось."
    "За покупками сходил, с делами разобрался..."
    "Чем бы заняться..."
    "..."
    "О, глянь!"
    show sarah thinking with dissolve
    "[sarah.name] только что прошла мимо. Гуляет? Она меня не заметила."
    mc.c "[sarah.name]!"
    show sarah surprise
    sarah.c "А?"
    show sarah joy
    sarah.c "О, [mc.name]! Привет!"
    show sarah smile talk 2
    sarah.c "Как дела? Чем занимаешься?"
    show sarah smile
    mc.c "Э-э, просто гуляю. Честно говоря, скучно, не знаю, чем заняться."
    show sarah tease talk
    sarah.c "Большой начальник жалуется, что ему нечего делать, пока его рабы пашут в баре?"
    show sarah tease
    "Хм, тут она меня подловила. Но сегодня совсем не хочется обслуживать посетителей..."
    mc.c "Ну..."
    show sarah tease talk
    sarah.c "Да шучу я, чувак. Можешь взять выходной, если хочешь."
    show sarah tease
    mc.c "А у тебя сегодня лекции?"
    show sarah smile talk
    sarah.c "Вообще-то нет. Решила немного расслабиться, знаешь?"
    show sarah thinking
    sarah.c "Ну, я могла бы поработать над одной работой..."
    show sarah smile talk 2
    sarah.c "Но сегодня мне нужен день для себя. Понимаешь?"
    show sarah smile
    mc.c "Ещё бы."
    show sarah smile talk 2
    sarah.c "Я собираюсь в лес, знаешь, туда, недалеко отсюда."
    "Она неопределённо машет рукой куда-то вдаль. Лес? Я нечасто выбирался за пределы центра."
    mc.c "Кажется, я там не был."
    show sarah surprise
    sarah.c "Серьёзно? Ты что, совсем никуда не выбираешься?"
    mc.c "Эй, я тут не так давно."
    show sarah smile talk
    sarah.c "Тебе стоит съездить. Я время от времени хожу туда в походы. Лес, холмы — можно от всего отвлечься."
    show sarah thinking
    sarah.c "..."
    show sarah smile talk
    sarah.c "Слушай, пойдёшь со мной? Обычно я хожу одна, но..."
    show sarah smile talk 2
    sarah.c "Похоже, тебе не помешает компания, да?"
    show sarah smile
    "Звучит отлично. Что-то новое, да ещё и проведу время с [sarah.name]."
    mc.c "Ты не против? Было бы здорово!"
    show sarah smile talk
    sarah.c "Конечно, почему нет? Пошли!"
    show sarah smile
    "Она легонько подталкивает меня, и мы направляемся туда, куда она шла."
    mc.c "Если мы идём в поход, мне ничего с собой не нужно взять?"
    show sarah thinking
    "Она оглядывает мою одежду. Не совсем туристическая экипировка, но и не такая уж неудобная."
    show sarah smile talk 2
    sarah.c "Да нормально всё, это же не глушь какая-нибудь."
    sarah.c "Давай, пошевеливайся!"
    "Она ещё раз игриво толкает меня в спину, и мы отправляемся."
    scene black with fade
    "Идти неожиданно недолго: городская застройка быстро сменяется редкими пригородными домами."
    "А сразу за ними..."
    scene forest with fade
    pause
    "Тот самый «лес»."
    "Высокие деревья, кое-как протоптанные тропинки, небольшая речка. Для такого городского жителя, как я, — в самый раз."
    "Скорее большой парк или заповедник, но здесь уже ощущается настоящая природа."
    show sarah smile talk with dissolve
    sarah.c "Видишь?"
    show sarah smile
    mc.c "Вижу. Классно! И не знал, что тут такое есть."
    show sarah smile talk 2
    sarah.c "Настоящий уголок природы. Лучшее, что можно найти в пешей доступности."
    show sarah thinking
    sarah.c "Мне бы тоже стоило когда-нибудь научиться водить."
    show sarah smile talk
    sarah.c "Здесь так тихо. Редко встретишь кого-нибудь ещё."
    show sarah smile
    mc.c "Да, здорово. Надо почаще сюда выбираться."
    "Пытаюсь не подавать виду, но даже дорога сюда оказалась для меня длиннее, чем я привык. Я уже устал."
    "А впереди виднеются холмы. О нет..."
    show sarah smile talk 2
    sarah.c "[mc.name], сюда."
    hide sarah with dissolve
    "Она сворачивает на подъём. Именно этого я и боялся."
    mc.c "Туда... наверх?"
    "Надо мной нависает холм, а чуть дальше между деревьями начинается протоптанная тропа."
    show sarah neutral talk with dissolve
    sarah.c "Что значит «туда»? Конечно, наверх."
    show sarah surprise 
    sarah.c "Ты уже устал?!"
    mc.c "Нет, я в порядке, просто..."
    show sarah joy
    sarah.c "Ахаха!"
    show sarah smile talk 2
    sarah.c "Давай, оттуда отличный вид. Не пожалеешь."
    show sarah tease talk
    sarah.c "Доведу тебя туда, городской мальчик, хочешь ты того или нет."
    show sarah tease
    "Она берёт меня за руку и тащит за собой."
    "Не хочу портить ей настроение, так что надо потерпеть."
    scene black with fade
    "Изнурительный подъём по извилистой грязной тропе..."
    "К концу я изо всех сил стараюсь не задыхаться, чтобы сохранить лицо."
    "Но всё и так очевидно."
    "Она могла бы раздражаться, что я её задерживаю, но ей просто смешно."
    sarah.c "Смотри, [mc.name], мы почти на месте."
    "Вот и вершина."
    scene hilltop with fade
    "Подъём заканчивается, и перед нами открывается небо."
    "С вершины виден город, который мы только что покинули."
    "Только отсюда понимаешь его размеры. Он небольшой, но плотный. Мне правда стоит ценить это место."
    show sarah joy with dissolve
    sarah.c "Ты справился! Молодец!"
    sarah.c "Ну как? Я же говорила, что оно того стоит."
    show sarah smile
    "[sarah.name] подпрыгивая подбегает к ограде."
    "А я остаюсь, уперев руки в колени и хватая ртом воздух."
    scene sarahlikeevent3i1 with fade
    "Она смотрит на пейзаж с довольным видом."
    "Она на редкость молчит, разглядывая окрестности. Улыбка не сходит с лица, но выражение становится мягче."
    "Наконец отдышавшись, я подхожу к ней."
    "Она ходит сюда, чтобы отвлечься и привести мысли в порядок."
    "Немного сбежать от шума. И она позволила мне составить ей компанию."
    "Пустила в своё убежище. Наверное, для неё это многое значит. Меня это трогает."
    scene hilltop with fade
    mc.c "Спасибо, что взяла меня с собой, [sarah.name]."
    show sarah smile talk with dissolve
    sarah.c "Да не за что. Всегда пожалуйста."
    mc.c "Прости, если задерживал. Похоже, я не в такой уж хорошей форме."
    show sarah joy
    sarah.c "Да брось, чувак, ты не так уж плохо справился."
    show sarah tease talk
    sarah.c "Но если будем ходить сюда чаще, тебе придётся начать тренироваться."
    show sarah tease
    "Чаще..."
    "Сегодняшняя прогулка... больше походила на настоящее свидание. На что-то более душевное."
    "Подойдя к ней, я протягиваю руку."
    show sarah smile
    "Она слегка вздрагивает и смотрит вниз, но всё же берёт меня за руку."
    "..."
    "Мы молча стоим рядом и любуемся видом. Тихий миг только для нас двоих."
    "Я вспоминаю тот вечер у меня дома. Мы просто дружески проводили время, а потом всё переросло в нечто большее."
    "Это было просто мимолётное исследование? Друзья просто выпустили пар?"
    "Или неловкий всплеск более глубоких чувств? Мы выразили их телом, а не словами?"
    "Не хочу, чтобы всё закончилось случайной интрижкой. Может, я и рискую, но хочу попробовать построить что-то большее."
    mc.c "Кажется, мы пропустили один этап, да?"
    show sarah neutral talk
    sarah.c "А?"
    show sarah neutral
    "Я поворачиваюсь к [sarah.name] и смотрю ей в глаза."
    "Медленно приближаю к ней лицо."
    "Её глаза блестят на солнце, но она не отводит взгляда."
    window hide
    hide sarah with dissolve
    show sarah kiss with dissolve
    "*Чмок*"
    hide sarah with dissolve
    show sarah hug with dissolve
    mc.c "Я давно хотел это сделать."
    sarah.c "Хе... Я тоже..."
    hide sarah with dissolve
    show sarah smile with dissolve
    mc.c "Не хочу, чтобы ты думала, будто тот раз был просто интрижкой. На этом всё не обязано закончиться."
    mc.c "По крайней мере, я этого не хочу."
    show sarah bashful talk
    sarah.c "Правда? Я думала, тебе и так нормально, но..."
    sarah.c "Что-то серьёзнее? То есть... с такой девушкой, как я?"
    show sarah bashful
    mc.c "Именно с такой девушкой, как ты, [sarah.name]. Ты особенная."
    show sarah bashful talk
    sarah.c "Не знаю насчёт этого..."
    show sarah bashful
    mc.c "Поверь мне."
    "Я снова притягиваю её к себе, давая понять, что настроен серьёзно."
    hide sarah with dissolve
    show sarah kiss with dissolve
    "*Чмок*"
    hide sarah with dissolve
    show sarah hug with dissolve
    sarah.c "Значит... в этот раз это было настоящее свидание..."
    mc.c "Наверное. Хотя я не произвёл особенно хорошего впечатления."
    sarah.c "Нет, я... мне понравилось, что ты пошёл со мной."
    sarah.c "Но тебе придётся постараться, чтобы не отставать от меня."
    mc.c "Только не загоняй меня."
    scene black with fade
    "Мы ещё какое-то время остаёмся на вершине, наслаждаясь новой близостью."
    "Наконец мы спускаемся. Когда я немного отдышался..."
    "Обратный путь оказался лишь чуточку легче..."
    
    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return {'location':location_town}

label sarahHEvent2(fromGallery = False):
    call playMusic(funnyTheme) from _call_playMusic_215
    $ location_bar.showBackground()
    "Похоже, сегодня [sarah.name] снова пришла выпить с друзьями."
    "Я уже начинаю узнавать некоторых из них и со многими в хороших отношениях — они регулярно выбирают наш бар."
    "Постепенно разбираюсь, кто есть кто: какие у них характеры, кто с кем дружит и кто явно встречается."
    "Похоже, они отмечают окончание экзаменов или что-то вроде того, так что сегодня все очень веселы."
    "Иногда я перекидываюсь с кем-нибудь парой слов, когда принимаю заказ или убираю столы, но в основном не мешаю им."
    "Мы с [sarah.name] тоже время от времени дружелюбно переглядываемся, хотя она отвечает немного застенчиво."
    "Может, при друзьях она стесняется. Похоже, никто из них не знает о наших отношениях."
    "Меня это устраивает. Пусть отдыхают."
    scene black with fade
    pause
    $ location_bar.showBackground()
    "Они уже пару часов здесь и сегодня выпили немало. Должно быть, повод для праздника и правда серьёзный."
    "Я собирался скоро домой — меня должны подменить сотрудники следующей смены."
    "Компания понемногу редеет: люди расходятся."
    "Один из ребят подходит к стойке, чтобы отнести пустые стаканы."
    show man with dissolve
    unknown "Эй, [mc.name]! Ты такой хороооший парень, чувак."
    "Парень уже здорово набрался. Но он молодец — похоже, хорошо повеселился."
    mc.c "Всегда рад вас видеть. Заходите ещё. Хорошего вечера."
    "Он наваливается локтями на стойку и манит меня пальцем."
    unknown "Эй, чувак, есть секрет для тебя."
    "Я наклоняюсь к нему. Может, он расскажет шутку, а может, просто несёт пьяную чушь."
    mc.c "Ну, рассказывай."
    unknown "Тссс, тебе никто не говорил, но слушай."
    unknown "Та девчонка вон там, [sarah.name]..."
    "Я навостряю уши. Сплетни о [sarah.name]? Честно говоря, не уверен, что хочу это слышать."
    call stopMusic from _call_stopMusic_39
    unknown "...по уши в тебя влюблена. Очень-очень."
    "Я на секунду замираю. Тут столько всего подразумевается, что я не знаю, как реагировать."
    "[sarah.name] всё ещё за столом прощается с теми, кто задержался. Сама она выглядит слегка навеселе."
    unknown "Мы все поняли. Она постоянно сюда нас тащит и всё время о тебе говорит."
    "Обо мне говорит? Может, они знают больше, чем показывают."
    call playMusic(funnyTheme) from _call_playMusic_216
    unknown "Между нами, приятель. Думаю, её тянет к людям вроде тебя — к людям."
    mc.c "Вот как?"
    unknown "Ты раньше встречался с девушкой-собакой?"
    "Что ответить? Мы уже какое-то время встречаемся."
    "К счастью, долго думать не приходится."
    show man at twoPersonRight with ease
    show sarah mad at twoPersonLeft with dissolve
    sarah.c "Хватит приставать к [mc.name], ты же говорил, что тебе пора домой."
    "К счастью, у парня хватает ума замолчать, когда [sarah.name] подходит поближе."
    mc.c "Не беспокойся, [sarah.name]. Хорошо провели время?"
    show sarah joy
    sarah.c "Ещё бы, спасибо, [mc.name]."
    unknown "Ага, спа-сибо, друган."
    "Он разворачивается, чтобы уйти, но оглядывается через плечо."
    unknown "Не забудь, о чём я тебе говорил!"
    "Он подмигивает так выразительно, что едва не падает, и пошатываясь выходит за дверь."
    hide man with dissolve
    show sarah smile talk 2 at center with ease
    sarah.c "Что он имел в виду? Что он тебе сказал?"
    "Думаю, она выдержит шутку. Да и я мог бы обидеться, что она скрывает наши отношения от друзей."
    mc.c "Да так, сказал, что кто-то из вашей компании в меня влюблён."
    show sarah surprise
    sarah.c "Чт-что? Кто?!"
    "Я самодовольно улыбаюсь [sarah.name]."
    call playMusic(heartTheme) from _call_playMusic_217
    sarah.c "Погоди, что? К-как? Почему?"
    show sarah bashful
    mc.c "Похоже, они ничего не знают. Он просто предположил. Что-то про то, будто тебя «тянет к людям»."
    show sarah surprise
    sarah.c "Вот чёрт! Я такого никогда не говорила..."
    mc.c "А он прав?"
    show sarah bashful
    sarah.c "Эй... Да ладно тебе..."
    "[sarah.name] так легко смутить. Хватит её дразнить."
    mc.c "Ха-ха-ха, не переживай, я просто шучу. Это было забавно."
    show sarah bashful talk
    sarah.c "Эх... Прости, мне стоило им что-то рассказать? Про нас?"
    show sarah bashful
    mc.c "Только если сама хочешь. Серьёзно, я не против."
    show sarah sad talk
    sarah.c "Просто я не знала... Понимаешь... Значу ли я для тебя что-нибудь? То есть... именно я..."
    show sarah sad
    "Я ошарашен. Похоже, она сомневается, что я относился ко всему этому серьёзно."
    mc.c "Я думал, что ясно дал это понять, но, может, придётся тебя убедить."
    sarah.c "А?"
    "Я обхожу стойку, беру её за руки и притягиваю к себе."
    hide sarah with dissolve
    show sarah kiss with dissolve
    "Мы несколько секунд целуемся, и [sarah.name] явно не ожидала этого."
    "Я отстраняюсь, она распахивает глаза и оглядывается на столик компании."
    hide sarah with dissolve
    show sarah surprise with dissolve
    sarah.c "П-погоди!"
    mc.c "Ха-ха, не волнуйся, они уже ушли. Я видел."
    show sarah bashful talk
    sarah.c "Ой, боже... Ну ты и дразнила."
    mc.c "Прости, ты такая милая, когда я тебя поддеваю."
    sarah.c "Наверное, я заслужила. Не хочу причинить тебе боль, будто скрываю тебя или что-то такое."
    mc.c "Всё хорошо, правда. Не торопись, я не против. Главное, чтобы я знал, что значу для тебя."
    show sarah smile
    sarah.c "Думаю, ты и так знаешь..."
    "Она успокаивается, и мы улыбаемся друг другу. Может, хватит её дразнить."
    mc.c "Я уже собираюсь домой. Ты тоже?"
    "Она явно выпила несколько бокалов — слегка покачивается и раскраснелась. Но глаза её не лгут."
    show sarah bashful talk
    sarah.c "Ну... планов вроде нет..."
    "Думаю, больше ничего говорить не надо. Я беру её за руку, и мы уходим."
    call stopMusic from _call_stopMusic_40
    scene black with fade
    "Немного пошатываясь, мы добираемся домой..."
    $ location_home.showBackground()
    "Мы оказываемся у меня. По дороге [sarah.name] прижималась ко мне чуть ближе. Кажется, я знаю, к чему всё идёт."
    show sarah hug with dissolve
    mc.c "Эй, кто тебя сюда пригласил?"
    sarah.c "Хе-хе, заткнись..."
    call playMusic(sexyTheme) from _call_playMusic_218
    hide sarah with dissolve
    show sarah kiss with dissolve
    "[sarah.name] страстно целует меня, и мы ласкаем друг друга."
    hide sarah with dissolve
    show sarah hug with dissolve
    sarah.c "Я хочу кое-что попробовать."
    mc.c "Да?"
    sarah.c "Думаю, тебе понравится. Не переживай."
    "Мне начинает нравиться эта чуть более напористая [sarah.name]. Пара бокалов явно раскрепостила её."
    scene black with fade
    "Мы продолжаем целоваться и раздеваемся. Я как следует ощупываю её упругую пушистую грудь."
    "Она почти сталкивает меня на край кровати и устраивается между моих ног."

    image sarah blowjob part 1 = Movie(play="images/characters/sarah/hscenes/blowjob/part1.webm")
    show sarah blowjob part 1 with dissolve
    pause
    "[sarah.name] медленно ласкает мой член, и он быстро становится твёрдым."
    "Вид её висячих ушей, красивой груди и виляющего хвоста невероятно возбуждает."
    sarah.c "В первый раз я толком не успела оценить, но у тебя огромный член, да?"
    mc.c "Ну, это не очень-то по-женски."
    sarah.c "Хе, заткнись. Хочешь, я остановлюсь и уйду?"
    mc.c "Ни за что. Тебе ведь тоже этого хочется."
    sarah.c "Тут ты прав. Но мы уже делали это... Я хотела..."
    "[sarah.name] придвигается и опускает голову, а в её глазах пылает желание."
    image sarah blowjob part 2 = Movie(play="images/characters/sarah/hscenes/blowjob/part2.webm")
    show sarah blowjob part 2 with dissolve
    pause
    "Её тёплый рот обхватывает мой член: сначала головку, а потом она медленно опускается почти до основания."
    sarah.c "*Хлюп* *Хлюп-хлюп*"
    "В мягком ритме она опускает вес тела на мой член, "
    "Время от времени я чувствую её острые клыки. Немного пугает, но невероятно заводит."
    mc.c "Ох, чёрт... Как же хорошо."
    sarah.c "*М-м-м* *М-м-м*"
    "Её тихое гудение вибрирует вокруг меня — невероятное ощущение."
    "Слюна скользит по моему члену вверх-вниз и стекает к яйцам."
    "Она нежно поглаживает мою ногу; в этом поровну разврата и ласки."
    "Её упругая грудь слегка покачивается, а милый хвост ходит из стороны в сторону вслед за бёдрами."
    mc.c "А-а, не останавливайся..."
    sarah.c "*Хр-р-м*"
    pause
    "Даже в таком медленном темпе я долго не продержусь. Её язык кружит вокруг моего члена, приближая меня к краю."
    mc.c "[sarah.name]... помедленнее... я сейчас кончу."
    "Но вместо того чтобы остановиться и тоже насладиться моментом, она..."
    pause
    image sarah blowjob part 3 = Movie(play="images/characters/sarah/hscenes/blowjob/part3.webm")
    show sarah blowjob part 3 with dissolve
    pause
    "...с приятным хлопком отстраняется от головки, залитой слюной, и тут же снова берёт мой член в руку."
    sarah.c "Хорошо~"
    "Она начинает двигать рукой ещё быстрее."
    mc.c "А-а-а... А-а-а-а..."
    "Я думал, мы переключимся на что-нибудь другое до того, как я кончу, но, похоже, именно этого она и хотела."
    "Я замечаю, как другой рукой она забирается себе в трусики."
    "Она пристально смотрит мне в глаза — в её взгляде страсть и желание. Я никогда не видел у неё такого выражения."
    sarah.c "*Ах* Я хочу попробовать~ *Ах* Твою сперму..."
    "Она открывает рот и высовывает язык, приглашая кончить ей прямо в рот."
    mc.c "Я сейчас...!"
    sarah.c "А-а-а~"
    "Волна дрожи прокатывается из глубины моего тела и взрывается от движений руки [sarah.name]."
    image sarah blowjob end = Image("images/characters/sarah/hscenes/blowjob/end.webp")
    show sarah blowjob end with fadewhite
    pause
    "Из меня вырывается, возможно, самый мощный оргазм в жизни. Меня всего трясёт от удовольствия."
    "Она пытается направить струю себе в рот, но сперма разлетается повсюду и заливает её прежде невинное лицо."
    "Всё её лицо в сперме, и от силы оргазма часть, должно быть, попала ей глубоко в горло."
    sarah.c "*Бле-е-е*"
    "Она снова открывает рот, показывая, чем я её наградил."
    "Сперма закрывает один глаз и стекает на ладонь, подставленную, чтобы собрать капли."
    "Никогда бы не представил такую соблазнительную картину с милой, рассеянной, пацанистой [sarah.name]."
    mc.c "Вот чёрт, это было потрясающе."
    sarah.c "Н-н-не за что~"
    scene black with fade
    "[sarah.name] отворачивается за салфетками, чтобы привести себя в порядок."
    "Но я не видел, чтобы она что-то выплюнула... Неужели она?.."
    "Я откидываюсь на кровать, чтобы отдышаться. [sarah.name] возвращается и ложится рядом."
    scene sarahpillowtalk with fade
    call playMusic(chillTheme) from _call_playMusic_219
    mc.c "Ничего себе. Не знал, что ты на такое способна."
    sarah.c "Взаимно."
    mc.c "Ты уверена, что хотела только этого?"
    sarah.c "Только этого? Намекаешь, что у тебя есть ещё кое-что? Хи-хи."
    mc.c "Хе, не то чтобы. Просто кончил только я."
    sarah.c "Да ты точно не только кончил, здоровяк..."
    sarah.c "Мило, но сегодня я хотела именно этого. Остальное — в другой раз."
    "Мы лежим рядом, постепенно переводя дыхание."
    "Когда волна оргазма отступает, мы смущённо улыбаемся друг другу и наслаждаемся послевкусием."
    pause
    $ location_home.showBackground()
    "[sarah.name] уходит привести себя в порядок и вскоре возвращается."
    show sarah tease talk with dissolve
    sarah.c "Мне понравилось. Тебе тоже, да?"
    show sarah tease
    mc.c "Даже не представляешь насколько."
    show sarah tease talk
    sarah.c "Кажется, представляю..."
    sarah.c "Мне пора. Голова всё ещё немного кружится. Какое-то время больше не буду пить..."
    show sarah tease
    mc.c "Тебе не обязательно уходить, знаешь?"
    show sarah bashful talk
    sarah.c "Спасибо, но нет... Сегодня не останусь. Но обязательно как-нибудь в другой раз."
    mc.c "Обязательно."
    hide sarah with dissolve
    show sarah kiss with dissolve
    hide sarah with dissolve
    scene black with fade

    if(not fromGallery):
        $ sarah.addLove(1)
    
    return {'location':location_home}

label sarahHEvent3(fromGallery = False):
    $ location_home.showBackground()
    "[sarah.name] собирается прийти ко мне в гости."
    "Она сказала, что один из соседей приведёт к ним друзей, поэтому ей хочется оттуда сбежать и провести время у меня."
    "Мне очень приятно, что она предпочла провести вечер со мной."
    "Наши отношения всё ещё где-то между несерьёзным романом и чем-то серьёзным."
    "Кажется, нас обоих это устраивает. Думаю, она неуверенно относится к своим чувствам и стесняется говорить о них. Ещё одна черта её пацанского характера."
    "Меня это устраивает. Не хочу оттолкнуть её, пытаясь навязать нам отношения."
    "В любом случае, скоро она будет здесь. Я приготовил приставку и закуски, она принесёт напитки. Просто проведём время как обычно и посмотрим, что будет."
    "Дзынь-дон."
    call playMusic(funnyTheme) from _call_playMusic_220
    "Она пришла!"
    show sarah joy with dissolve
    sarah.c "Привет, чувак!"
    mc.c "Как дела, «чувак»?"
    show sarah tease talk
    sarah.c "Да ладно, будь повежливее. Я принесла пиво. Оно недешёвое, знаешь ли, особенно на мой студенческий бюджет."
    show sarah tease
    mc.c "Я мог бы сегодня купить его сам, если у тебя туго с деньгами. Если что, всегда могу помочь."
    show sarah tease talk
    sarah.c "Ой, заткнись, хватит говорить такие серьёзные вещи."
    sarah.c "Лучше выпей."
    show sarah tease
    "Она кидает мне банку и плюхается на диван. У меня ей уже так удобно, будто она здесь живёт."
    mc.c "Ну что, сыграем в «Бойня: Бой 4»?"
    show sarah joy
    sarah.c "Ещё бы! Давно хотела попробовать. У меня пока нет консоли нового поколения."
    show sarah tease talk
    sarah.c "Предупреждаю: раньше я здорово играла в «Бойню 2»."
    show sarah tease
    mc.c "Посмотрим. Это уже совсем другая игра, знаешь ли. Я немного потренировался..."
    show sarah tease talk
    sarah.c "Давай."
    hide sarah with dissolve
    "Мы устраиваемся перед телевизором, вокруг напитки и закуски, в руках контроллеры — словно мы подростки."
    "Не такой жизни я ожидал в свои двадцать, но не променял бы её ни на что."
    scene black with fade
    $ location_home.showBackground()
    show sarah tease talk
    sarah.c "Ну как тебе, неудачник? Ты даже ударить меня толком не смог."
    show sarah tease
    "Она хорошо играет. Будет нелегко."
    mc.c "Чёрт... Ты не врала. Давай ещё раз..."
    scene black with fade
    $ location_home.showBackground()
    show sarah surprise with dissolve
    sarah.c "Ничего себе, крутой приём! Как ты это сделала?"
    mc.c "Я выучил несколько приёмов этого персонажа. Знала бы, если бы у тебя была игра."
    show sarah mad talk
    sarah.c "Гр-р... Дешёвый удар, чувак. Ладно, следующий раунд..."
    scene black with fade
    $ location_home.showBackground()
    show sarah joy
    sarah.c "Да! Получай!"
    show sarah smile talk 2
    sarah.c "Едва выиграла. Ты уже втянулся, слабак."
    mc.c "Как ты каждый раз парируешь мои удары?!"
    show sarah tease talk
    sarah.c "Просто стань получше, чувак."
    scene black with fade
    "После напряжённой игровой сессии..."
    $ location_home.showBackground()
    show sarah smile talk
    sarah.c "Игра классная, могу долго в неё играть..."
    show sarah smile
    mc.c "Мне нужен перерыв, пальцы уже стёрлись об стики."
    show sarah smile talk
    sarah.c "Ага, понимаю. Раньше у меня, наверное, мозоли были."
    sarah.c "Может, теперь что-нибудь посмотрим?"
    mc.c "Да, конечно. Что хочешь."
    "Я кидаю [sarah.c] пульт. Она часто включает какую-нибудь ерунду, над которой можно иронизировать. Мне всё равно."
    show sarah thinking
    sarah.c "Так, посмотрим..."
    call stopMusic from _call_stopMusic_41
    scene black with fade
    "Мы отдыхаем на диване, запасы быстро заканчиваются, а мы в основном болтаем поверх какой-то ерунды по телевизору."
    "Вечер тянется дальше, свет становится тусклее, и мы устраиваемся поудобнее."
    $ location_home.showBackground()
    call playMusic(heartTheme) from _call_playMusic_221
    "[sarah.name] лежит на боку, положив голову на подлокотник и глядя в телевизор."
    "Раз уж она так удобно устроилась, она почти интимно упирается ногами в меня."
    "Мы допили напитки, оба слегка захмелели, но разговор затихает, а телевизор становится всё скучнее."
    show sarah neutral with dissolve
    "Я смотрю на [sarah.name]. Она выглядит задумчивой и умиротворённой, будто её что-то тревожит."
    "Уже поздно. Интересно, куда она собиралась сегодня."
    mc.c "Завтра у тебя лекции или занятия? Уже поздно, не хочу задерживать, если тебе пора домой."
    show sarah neutral talk
    sarah.c "М-м, нет, завтра ничего важного."
    show sarah neutral
    "..."
    show sarah neutral talk
    sarah.c "Слушай, [mc.name]..."
    show sarah neutral
    "Кажется, она давно хотела что-то сказать. Что такое? Надеюсь, ничего плохого."
    mc.c "Да?"
    "Она немного приподнимается и поворачивается ко мне."
    show sarah neutral talk
    sarah.c "Помнишь тот раз в баре, когда я пришла с друзьями из колледжа, и мы засиделись допоздна?"
    show sarah neutral
    mc.c "Такое случалось несколько раз."
    show sarah neutral talk
    sarah.c "Тот раз, когда некоторые из них сильно напились, и один парень подошёл к тебе в конце вечера. Конь. Помнишь?"
    show sarah neutral
    mc.c "Да, помню. Он был совсем пьян. Что-то случилось? Он нормально добрался домой?"
    show sarah neutral talk
    sarah.c "Да, всё хорошо. Через несколько дней он вспомнил, что наговорил, и рассказал мне."
    show sarah bashful talk
    sarah.c "Я думала, ты меня дразнишь, но он правда это сказал, да? Что-то про меня..."
    show sarah bashful
    mc.c "Что тебя тянет к людям."
    show sarah sad talk
    sarah.c "...Ага..."
    show sarah sad
    mc.c "Я подумал, это забавно. Он что, чувствовал себя виноватым?"
    show sarah sad talk
    sarah.c "Да, но не перед тобой, а передо мной. Потому что... он был прав."
    show sarah bashful talk
    sarah.c "Похоже, друзья что-то поняли. Я не особо умею скрывать чувства."
    show sarah bashful
    mc.c "Похоже, ему надо извиниться перед тобой, если он в пьяном виде ляпнул что-то личное."
    show sarah mad talk
    sarah.c "Он извинился... Я очень разозлилась."
    show sarah sad talk
    sarah.c "Но я подняла эту тему, потому что мне кажется, что теперь я должна извиниться перед тобой."
    show sarah sad
    mc.c "Почему? Я не обиделся. Могу спокойно относиться к разговорам о видах."
    show sarah bashful talk
    sarah.c "Знаю, что можешь... Просто... Мне не нравится, когда ты так говоришь."
    sarah.c "Не хочу, чтобы ты думал, будто я воспринимаю тебя как фетиш."
    "Я ещё не слышал большей чепухи."
    mc.c "Ха-ха, что? Мне что, полагается обидеться, что я тебе нравлюсь? Я польщён! Разве это не очевидно?"
    show sarah neutral talk
    sarah.c "Нет, правда. Тебе может показаться, что я подошла к тебе только из-за того, что ты человек."
    sarah.c "Должна признаться, ты сразу меня заинтересовал... из-за этого..."
    sarah.c "...но со временем ты мне по-настоящему понравился. Очень понравился... такой, какой ты есть..."
    show sarah neutral
    mc.c "[sarah.name], разве первое впечатление не всегда играет роль в симпатии?"
    mc.c "Когда я впервые увидел тебя, подумал: «Чёрт, какая милая!»"
    show sarah bashful talk
    sarah.c "Ой, да замолчи..."
    show sarah bashful
    mc.c "Серьёзно, меня это не беспокоит. Не нужно себя изводить."
    mc.c "Ты мне нравишься, может, и я тебе. Не стоит всё усложнять."
    show sarah sad
    sarah.c "М-м..."
    "Она, кажется, не до конца убеждена. Сама себя накрутила, и непонятно почему. Надо разрядить обстановку и показать, что она зря переживает."
    mc.c "Слушай, можешь даже подыграть, если хочешь. Буду твоим человеком."
    "Я уже начинаю её дразнить. Весь этот разговор — сущая нелепость. Не верится, что она так себя накрутила."
    show sarah bashful
    sarah.c "Ой, боже... Ты же идиот, знаешь?"
    mc.c "По-моему, тут глупо себя вела ты."
    "Её милый, растроганный взгляд смягчается. Надеюсь, ей стало легче от того, что я спокойно отнёсся к этому разговору. Не знаю, чего она ожидала."
    "Странное напряжение между нами нарастает. В этом разговоре промелькнули признания в чувствах — для [sarah.name] это редкость."
    "Я наклоняюсь к [sarah.name], которая всё ещё лежит, прислонившись к подлокотнику."
    mc.c "Я и правда имел в виду то, что сказал. Ты мне тоже нравишься."
    hide sarah with dissolve
    show sarah kiss with dissolve
    "Я мягко прижимаюсь к ней, и мы целуемся, почти лёжа на диване."
    sarah.c "М-м-м..."
    "Я провожу руками по её ногам и обнимаю за талию, чувствуя тепло и мягкую шерсть под майкой."
    hide sarah with dissolve
    show sarah hug with dissolve
    sarah.c "Прости, что я такая... странная."
    mc.c "Не за что извиняться. Если тебе нужно что-то рассказать, знай, что со мной можно быть откровенной, ладно?"
    sarah.c "[mc.name]..."
    call playMusic(sexyTheme) from _call_playMusic_222
    mc.c "Кстати о том, чтобы снять с тебя одежду..."
    "Я запускаю руку под её майку и стягиваю её с плеч, обнажая красивую упругую грудь."
    sarah.c "Хе-хе~ Ну ты и шутник..."
    "[sarah.name] отвечает тем же и быстро снимает с меня футболку."
    hide sarah with dissolve
    show sarah kiss with dissolve
    image sarah doggy start1 = Movie(play="images/characters/sarah/hscenes/doggyStyle/start1.webm")
    show sarah doggy start1 with fade
    pause
    "Я обнимаю её за тонкую талию и притягиваю к себе для глубокого поцелуя."
    "Мы целуемся глубже и страстнее, чем когда-либо прежде."
    sarah.c "М-м-м, [mc.name]~"
    "Её упругие соски нежно касаются моей груди, когда я наклоняюсь к ней."
    "Наши ноги переплетаются."
    "Я провожу рукой по её шортам и расстёгиваю верхнюю пуговицу. Надеюсь, сегодня мы зайдём до конца."
    mc.c "Я хочу этого."
    sarah.c "Да... Я тоже."
    sarah.c "Дай мне встать."
    scene black with fade
    "[sarah.name] встаёт и снимает шорты, впервые полностью обнажаясь передо мной."
    "Мы неловко молчим, пока я разглядываю её тело."
    sarah.c "Я ведь говорила, что в прошлый раз хотела продолжения?"
    "Она поворачивается и упирается руками в кровать..."
    image sarah doggy start2 = Movie(play="images/characters/sarah/hscenes/doggyStyle/start2.webm")
    show sarah doggy start2 with fade
    pause
    "Она соблазнительно покачивает передо мной красивой попкой."
    "Хвост нетерпеливо виляет, в её глазах смешались тревога и желание."
    sarah.c "...Пожалуйста, [mc.name]..."
    "Будто я мог отказать. Но это слишком лёгкая мишень, и я не удерживаюсь от озорной ухмылки."
    mc.c "{b}Раком{/b}, [sarah.name]? Серьёзно?"
    sarah.c "О боже, [mc.name], заткнись! Ну зачем ты это сказал?"
    "Она смущённо отворачивается, но не может скрыть улыбку — глупые шутки всегда её веселят."
    "Кто бы отказался от такого приглашения? Я снимаю штаны, больше не скрывая возбуждения, и крепко обхватываю её округлые ягодицы."
    "Мой член входит в её горячую, влажную от ожидания киску..."
    image sarah doggy part1 = Movie(play="images/characters/sarah/hscenes/doggyStyle/part1.webm")
    show sarah doggy part1 with fade
    pause
    sarah.c "М-м-м-м~!"
    "Мой член целиком погружается в её киску, уже залитую соком."
    "Я сразу начинаю двигаться, ощущая каждую складочку."
    sarah.c "А-а-а~ А-а-а~"
    sarah.c "Чёрт... Ты такая... большая~"
    "Каждый толчок заканчивается звонким шлепком по её пышным ягодицам."
    "Она стонет с каждым движением, чувствуя, как мои бёдра ударяются о её."
    sarah.c "Ох, чёрт~ Так хорошо~"
    mc.c "А-а, [sarah.name], ты потрясающая."
    "Я обхватываю обе её ягодицы и уверенно вхожу в неё."
    "Её хвост виляет у меня перед лицом, а [sarah.name] дышит всё чаще и громче."
    sarah.c "*Ах* *Ах* Да~ [mc.name]~"
    mc.c "*Ах* [sarah.name]... *Ах*"
    mc.c "Можно быстрее?"
    sarah.c "Давай... Я хочу~"
    image sarah doggy part2 = Movie(play="images/characters/sarah/hscenes/doggyStyle/part2.webm")
    show sarah doggy part2 with fade
    pause
    "Я кладу руку ей на поясницу и мягко наклоняю её к кровати."
    "Я прижимаюсь к краю кровати, меняю угол и вхожу глубже и сильнее."
    "Я хватаю её за основание хвоста, направляя бёдра, а он безудержно виляет от удовольствия."
    sarah.c "А-а-а~ Боже мой~"
    "Кровать скрипит с каждым толчком, её бёдра упираются в край."
    mc.c "Ах, чёрт, ты такая горячая..."
    sarah.c "Да, да, да! Да-а-а~!"
    sarah.c "Трахай меня своим большим человеческим членом! *Ах* Жёстче, по-собачьи!"
    "Мы стонем и выкрикиваем слова страсти, теряя самообладание в пылу момента."
    image sarah doggy part3 = Movie(play="images/characters/sarah/hscenes/doggyStyle/part3.webm")
    show sarah doggy part3 with fade
    pause
    "[sarah.name] оглядывается через плечо и смотрит мне в глаза. Её лицо пылает животным желанием."
    sarah.c "*Ах* Мне так нравится, так нравится! *Ах*"
    sarah.c "Мне *Ах* так *М-м* нра-*А-а*~"
    "Я уже на пределе... Мы даже не предохранялись."
    mc.c "[sarah.name], я сейчас..."
    sarah.c "И я~ Да-а~"
    mc.c "*Ах* К-куда мне..."
    sarah.c "Кончи в меня! Давай! *Ах* Я что-то принимаю..."
    "Что бы она ни принимала, разберёмся потом. Сейчас я уже не смогу остановиться."
    mc.c "А-а-а-а."
    sarah.c "М-м-м-м~!"
    image sarah doggy end = Image("images/characters/sarah/hscenes/doggyStyle/end.webp")
    show sarah doggy end with fadewhite
    pause
    "Я мощно кончаю глубоко внутри [sarah.name], прижимая её бёдра к кровати. Мы оба дрожим от наслаждения."
    "Она прогибает спину и запрокидывает голову, задыхаясь."
    sarah.c "А-а-а-а-а~~~!"
    "Я замираю в этой позе, пытаясь отдышаться и прийти в себя после невероятного оргазма."
    "Я смотрю на спину [sarah.name], которая лежит лицом вниз и тяжело дышит. Я только что наполнил её спермой."
    pause
    scene black with fade
    "Наконец мы падаем на кровать, хватая ртом воздух."
    "Через некоторое время [sarah.name] подползает ко мне."
    scene sarahpillowtalk with fade
    call playMusic(heartTheme) from _call_playMusic_223
    sarah.c "Это было потрясающе..."
    mc.c "Да, это было... Совсем нечто..."
    sarah.c "Кажется, я немного потеряла голову... Я не сказала ничего странного?"
    mc.c "Это было чертовски горячо."
    sarah.c "Чёрт... Я бы сказала, что не знаю, что на меня нашло, но, кажется, знаю."
    mc.c "Не переживай, мне понравилось. Я и сам ужасно говорю непристойности."
    sarah.c "Ой, заткнись."
    "Она игриво толкает меня в бок и устраивается рядом."
    "Мы просто наслаждаемся обществом друг друга."
    mc.c "Можешь... остаться на ночь, если хочешь? Уже поздно."
    sarah.c "...Да... пожалуйста... Спасибо, [mc.name]."
    call sarahSleepover from _call_sarahSleepover
    "Мы обнимаемся. [sarah.name] впервые остаётся у меня на ночь."
    "Комната завалена пивными банками, упаковками и одеждой."
    "Уберём завтра." 
    
    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return {'location':location_home, 'time':'Morning'}

label sarahHEvent4(fromGallery = False):
    scene diner with fade
    call playMusic(funnyTheme) from _call_playMusic_224
    show sarah smile talk with dissolve
    sarah.c "...И преподаватель так разозлился, что проектор показывал всё вверх ногами, а он не знал, что делать!"
    sarah.c "Он снова и снова всё подключал и отключал, окна на экране крутились во все стороны, а он всё время ворчал."
    show sarah smile talk 2
    sarah.c "Потом всё свернулось, и на ноутбуке появилось милое розовое цветочное изображение! Совсем на него не похоже."
    sarah.c "Клянусь, он покраснел и запаниковал, а потом..."
    show sarah joy
    sarah.c "Опрокинул кофе прямо на пол лекционного зала! Ха-ха!"
    show sarah smile talk 2
    sarah.c "Боже, чувак, надо было видеть! Все изо всех сил сдерживались, чтобы не рассмеяться."
    show sarah smile
    "Сегодня мы с Сарой пошли поесть. С ней всегда весело."
    "Она рассказывает истории о прошедшей неделе в колледже. Удивляюсь, в какие передряги она попадает. Я помню, как мне было ужасно скучно в колледже."
    "Сегодня она особенно энергичная, тараторит без умолку."
    show sarah smile talk
    sarah.c "Бедняга. Ему так стыдно было. Удивительно, что он вообще сумел дочитать лекцию до конца."
    show sarah surprise
    sarah.c "О, выглядит вкусно. Дай кусочек."
    "Не раздумывая, она отрезает кусок от моей тарелки."
    mc.c "Эй..."
    show sarah joy
    sarah.c "М-м-м~ Вкусно!"
    "Она съедает его, пока я и глазом моргнуть не успеваю. С ней надо быть начеку..."
    mc.c "Моя курица..."
    show sarah tease talk
    sarah.c "Кто не успел, тот опоздал, дружок."
    show sarah smile talk 2
    sarah.c "Ой, не грусти, чувак. Вот, можешь взять кусочек..."
    "Она смотрит на свою уже почти пустую тарелку."
    show sarah surprise
    sarah.c "Э-э..."
    "Поняв, что придётся отдать последние кусочки, она быстро съедает их сама."
    show sarah tease
    sarah.c "Ой, тебе ничего не осталось~"
    "Она довольно ухмыляется с набитым ртом, не оставляя мне ничего."
    mc.c "Не могу поверить, что ты так со мной поступила..."
    "Обычный день с Сарой: весело, легко, будто мы просто приятели."
    "Только она ещё и горячая, и я могу с ней переспать. Чёрт, мне повезло."
    show sarah tease talk
    sarah.c "*Глотает* Фу~"
    "Она за это поплатится... Я слегка толкаю её ногой, выражая недовольство."
    show sarah surprise
    sarah.c "Эй!"
    "Она пинает меня в ответ."
    show sarah tease talk
    sarah.c "Не будь ребёнком. Ну правда~"
    show sarah tease
    mc.c "Я тебе ещё отомщу."
    show sarah tease talk
    sarah.c "Да ничего ты мне не сделаешь, мягкотелый."
    show sarah tease
    "Такие дни и такая компания — вот ради чего стоит жить."
    "Я снова слегка толкаю её, признавая своё поражение."
    show sarah smile talk 
    sarah.c "Не затевай драку, которую не сможешь закончить, [mc.name]."
    show sarah smile
    "Я готовлюсь к ответному пинку, но вместо этого чувствую, как чья-то нога скользит вверх по внутренней стороне моей ноги."
    call playMusic(sexyTheme) from _call_playMusic_225
    image sarah footjob part1 = Movie(play="images/characters/sarah/hscenes/footjob/part1.webm")
    show sarah footjob part1 with fade
    pause
    "Похоже... босая ступня ласкает меня между ног."
    "Я смотрю вниз и убеждаюсь, что так и есть."
    "Сначала я озадаченно смотрю на Сару."
    image sarah footjob part2 = Movie(play="images/characters/sarah/hscenes/footjob/part2.webm")
    show sarah footjob part2 with fade
    pause
    "Но в ответ вижу её самодовольную улыбку. Её ступня водит кругами по моей выпуклости."
    mc.c "Играешь со мной?"
    sarah.c "А? Ты о чём?"
    "Ладно, теперь она действительно меня дразнит."
    image sarah footjob part3 = Movie(play="images/characters/sarah/hscenes/footjob/part3.webm")
    show sarah footjob part3 with fade
    pause
    "Она уже трёт пальцами мою выпуклость сквозь штаны и продолжает самодовольно улыбаться."
    "Чего она добивается?"
    "Необычно, но... приятно."
    "Мы в кабинке, стол низкий, должно быть безопасно..."
    sarah.c "Что с тобой, чувак? Ты как-то странно выглядишь."
    "Наверное, у меня на лице всё написано. Мне начинает нравиться."
    "Прошло совсем немного времени, а я уже твёрдый. Понимаю: она дразнит меня, зная, что здесь я ничего не могу сделать."
    "Ладно, если она хочет так играть, у меня есть идея..."
    image sarah footjob part4 = Image("images/characters/sarah/hscenes/footjob/part4.webp")
    show sarah footjob part4 with fade
    pause
    "Когда она проводит ногой вниз, я не слишком незаметно расстёгиваю ширинку — я и так уже готов вырваться."
    "Проведя ногой обратно вверх, она явно чувствует, что там что-то изменилось."
    sarah.c "!"
    mc.c "О, что такое, Сара? Всё в порядке?"
    "Сначала она удивляется, а потом смущённо отворачивается."
    sarah.c "..."
    mc.c "И что там было про «не начинай драку, если не сможешь её закончить»?"
    "Теперь она попалась. Либо отступит, и я победил, либо..."
    sarah.c "..."
    image sarah footjob part6 = Movie(play="images/characters/sarah/hscenes/footjob/part6.webm")
    show sarah footjob part6 with fade
    pause
    "Вместо того чтобы остановиться, она другой ногой стягивает носок и продолжает."
    "Она водит пальцами вверх-вниз по моему члену."
    "У неё это неожиданно ловко получается..."
    "Она не может смотреть мне в глаза и смущённо прикрывает лицо, но не останавливается."
    "И, боже, как же приятно."
    "Эти мягкие подушечки создают такое трение..."
    "Мы стараемся не выдать себя выражением лица, но со стороны наше молчание, наверное, тоже выглядит подозрительно."
    "Как бы хорошо ни было, так я, пожалуй, не кончу."
    mc.c "Так мы весь день просидим, Сара."
    sarah.c "Ой, боже..."
    image sarah footjob part7 = Movie(play="images/characters/sarah/hscenes/footjob/part7.webm")
    show sarah footjob part7 with fade
    pause
    "Она принимает вызов и подключает вторую ногу."
    "Зажав мой член между ступнями, она скользит ими вверх и вниз по всей длине."
    "Сочетание пушистых подошв и подушечек лап... Просто рай."
    "Её пальчики скользят вверх-вниз по моему члену... Боже мой."
    "После моей самоуверенной бравады я уже не могу придумать, что сказать: слишком сосредоточен, чтобы не кончить раньше времени."
    image sarah footjob part8 = Movie(play="images/characters/sarah/hscenes/footjob/part8.webm")
    show sarah footjob part8 with fade
    pause
    "Она ускоряется и наконец смотрит мне в глаза. Похоже, ей тоже начинает нравиться."
    "Я уже на пределе. Что же мне делать?"
    "Да плевать, сейчас кончу."
    image sarah footjob finish = Image("images/characters/sarah/hscenes/footjob/finish.webp")
    show sarah footjob finish with fadewhite
    pause
    "Я кончаю, кажется, прямо под стол."
    "Странно кончать, когда ничего не видно. Даже не знаю, куда всё попало."
    "Я пытаюсь сохранить невозмутимое лицо, но Сара понимает, что я только что кончил."
    "Она снова ухмыляется, довольная тем, в каком состоянии меня оставила."
    sarah.c "Хе-хе~"
    call playMusic(funnyTheme) from _call_playMusic_226
    scene diner with fade
    show sarah tease talk with dissolve
    sarah.c "Я закончила начатое, как ты и сказал. Похоже, я победила~"
    show sarah tease
    mc.c "Думаю, мне досталось больше удовольствия. Значит, я победил?"
    show sarah tease talk
    sarah.c "М-м~ Как скажешь, чувак."
    show sarah tease
    mc.c "...Надо отсюда уходить."
    show sarah bashful talk
    sarah.c "Э-э, да."
    scene black with fade
    "Мы поспешно уходим, а я оплачиваю счёт."
    "По дороге наружу Сара смущённо хихикает."
    "Мне неловко, что пришлось оставить там весь этот беспорядок."
    "Пожалуй, какое-то время туда лучше не возвращаться."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return {'location':location_town}

label sarahHEvent5(fromGallery = False):
    $ location_beach.showBackground()
    call playMusic(chillTheme) from _call_playMusic_227
    "Ах, побережье."
    "Для такого красивого места здесь никогда не бывает слишком людно. В этом городе так почти везде."
    "Чем дольше я здесь живу, тем больше радуюсь, что переехал."
    "Переезжать было страшно. Я сам решил начать всё сначала, но всегда могло что-то пойти не так."
    "Бизнес мог не пойти, здесь не было ни друзей, ни родных — можно было легко стать одиноким и замкнуться."
    "Я даже не знал, как здесь относятся к людям. К счастью, всё оказалось лучше, чем я мог представить."
    "Эти люди приняли меня в своё сообщество и помогли почувствовать себя как дома."
    "Я завёл друзей, в том числе..."
    show sarah smile with dissolve
    "...и кое-кого больше, чем друга."
    "Я не знал, получится ли у меня построить отношения с антро. Но переживать было не о чем."
    "С такой замечательной девушкой, как Сара, я счастлив как никогда."
    "Чудаковатая, смешная, игривая — идеальная милая пацанка."
    "Мы часто приходим сюда вместе: отдыхать, болтать, плавать или бегать."
    "А когда она отряхивает шерсть... Боже, это так мило."
    "Кажется, я... влюбляюсь..."
    "..."
    "Нам хорошо вместе. Есть и страсть, и романтика. Наши отношения не должны вызывать сомнений, но..."
    "Я так и не произнёс эти важные слова. И она тоже."
    "Меня раньше не отвергали, но я слышал, что признание в любви может всё испортить, если выбрать неподходящий момент."
    "Дома я никогда ни к кому так не относился. Значит ли это, что..."
    show sarah smile talk 2
    sarah.c "[mc.name]? Ты задумался. Что такое?"
    show sarah smile
    mc.c "О-о, ничего, Сара. Просто думал... о делах."
    show sarah mad talk
    sarah.c "Да брось, мы же отдыхаем. Мне это нужно после промежуточных экзаменов."
    show sarah mad
    mc.c "Ты права, прости."
    show sarah tease talk
    sarah.c "Так вот, я {b}говорила...{/b}"
    show sarah joy
    sarah.c "Пора купаться!"
    show sarah smile talk
    sarah.c "Раздевайся!"
    hide sarah with dissolve
    "Она бежит к воде и быстро снимает верхнюю одежду, оставаясь в купальнике."
    "В нём она такая милая... И в последнее время я часто её такой вижу."
    "Пора к ней присоединиться."
    call playMusic(heartTheme) from _call_playMusic_228
    scene sarahhevent5i1 with fade
    pause
    "Перед тем как зайти в воду, я останавливаюсь полюбоваться этим прекрасным видом."
    "Сара плескается в океане, повернув ко мне свою милую попку. Боже, она сводит меня с ума."
    "..."
    "Как же мне повезло?"
    sarah.c "Чего ждёшь? Давай!"
    mc.c "Уже иду."
    scene sarahhevent5i2 with fade
    pause
    "Немного поплескаться..."
    scene sarahhevent5i3 with fade
    pause
    "Немного поплавать..."
    scene sarahhevent5i4 with fade
    pause
    "Немного отдохнуть..."
    scene sarahhevent5i5 with fade
    pause
    "Мы покачиваемся в волнах в объятиях друг друга, слушая шум прибоя."
    mc.c "Тебе стало лучше?"
    sarah.c "Ещё бы. Именно то, что нужно."
    sarah.c "Спасибо, что пришёл со мной, чувак."
    mc.c "Ты же знаешь, я всегда рядом."
    sarah.c "Ну почему ты такой сентиментальный..."
    "Она прищуривается и слегка приоткрывает губы, явно приглашая меня."
    scene sarahhevent5i6 with fade
    pause
    "Сладкий вкус её губ и мокрая шерсть вокруг..."
    "А ведь говорят, что мокрая собака неприятно пахнет."
    scene sarahhevent5i7 with fade
    pause
    "Мы прерываем поцелуй, я обнимаю её за талию и хватаю ладонью упругую попку."
    sarah.c "Вот ты и кобелёк..."
    mc.c "А как ещё мне за тебя держаться? Тебя же может унести волной."
    sarah.c "Глупыш~"
    "Мне сложно сдерживаться и не наброситься на неё прямо сейчас. Но, наверное, посреди океана это не лучшая идея."
    sarah.c "Нам, пожалуй, стоит пойти домой. Мне нравится здесь, но соль вредна для шерсти."
    mc.c "Ага, я уже весь сморщился."
    sarah.c "У людей такая забавная кожа."
    call playMusic(chillTheme) from _call_playMusic_229
    scene black with fade
    "Мы выходим из моря, насколько можем вытираемся, одеваемся и идём домой."
    "Хорошо, что светит солнце: пока дойдём до города, высохнем. Тут недалеко."
    "Сначала мы приходим ко мне, потому что моя квартира ближе. Я прямо не приглашал Сару, но она идёт к двери за мной, словно приглашение и так понятно."
    sarah.c "Можно воспользоваться твоим душем? Хочу как можно скорее смыть с себя соль."
    sarah.c "И у тебя душ лучше, чем у меня дома."
    mc.c "Любой повод, да? Конечно, без проблем."
    "Она заходит следом за мной."
    $ location_home.showBackground()
    show sarah smile talk with dissolve
    sarah.c "Шампуня хватит? Знаю, людям нужно совсем немного."
    show sarah smile
    mc.c "Думаю, да... Пользуйся всем, что найдёшь."
    show sarah tease talk
    sarah.c "Ха, чувак. Держу пари, у тебя там бутылка отбеливателя «пять в одном»."
    show sarah tease
    mc.c "Ну-ну, принцесса. Не думал, что ты такая привередливая."
    show sarah tease talk
    sarah.c "Собачке нужно ухаживать за шерстью, очевидно. Я всё-таки девушка."
    scene sarahhevent5i8 with fade
    pause
    "Она направляется в ванную, но прямо в коридоре снимает первый слой одежды."
    sarah.c "Фух, это тоже надо будет постирать, но потом. Принеси мне полотенце, ладно?"
    "..."
    "Я замираю от неожиданности. Она явно совсем меня не стесняется. Да и с чего бы ей?"
    "Она и так была в довольно открытом купальнике, но..."
    "Покачивает своей милой попкой... Будто дразнит меня. Я весь день держался, но теперь..."
    scene sarahhevent5i9 with fade
    pause
    "Она снимает трусики и уходит в ванную, виляя хвостом. Это уже слишком."
    "Не замечает она этого или специально меня дразнит — мысли у меня только об одном."
    call stopMusic from _call_stopMusic_42
    scene black with fade
    "Она скрывается в ванной, но я не могу оторвать взгляд."
    "Услышав, как она включает душ, я решаюсь."
    "К тому же мне тоже нужно помыться."
    call playMusic(sexyTheme) from _call_playMusic_230
    image sarah shower doggy start 1 = Image("images/characters/sarah/hscenes/showerSex/start1.webp")
    show sarah shower doggy start 1 with fade
    pause
    "Она меня ещё не заметила, а я уже разделся, готовый к «совместному душу»."
    "Я бесшумно открываю дверь и подкрадываюсь сзади, прежде чем она замечает меня."
    image sarah shower doggy start 2 = Image("images/characters/sarah/hscenes/showerSex/start2.webp")
    show sarah shower doggy start 2 with fade
    pause
    sarah.c "Ого, [mc.name]?!"
    sarah.c "Эй... Не мог подождать?"
    mc.c "После того как ты весь день меня дразнила, уже не мог."
    "Я сжимаю её ягодицу."
    sarah.c "О-о? Я вроде ничего такого не делала."
    mc.c "Одного твоего вида достаточно. А тут ты ещё и разделась прямо в коридоре. Ну же."
    sarah.c "Хе. Ладно. Может, я немного..."
    "Мой уже твёрдый член трётся о её попку."
    mc.c "Тогда я не против."
    sarah.c "Тебе не решать!"
    mc.c "Ну что, ты против?"
    sarah.c "Вообще-то нет..."
    sarah.c "Но... прямо здесь?"
    "Я подношу член к её входу."
    sarah.c "М-м-м, [mc.name]..."
    sarah.c "Давай~"
    image sarah shower doggy part 1 = Movie(play="images/characters/sarah/hscenes/showerSex/part1.webm")
    show sarah shower doggy part 1 with fade
    pause
    "Я прижимаю её к стеклу и обхватываю за бёдра."
    "Вхожу без труда — она уже влажная. И дело, конечно, не только в душе."
    sarah.c "М-м-м~ О-о-о~"
    "Я скольжу внутри неё, мягко прижимаясь к её милой попке."
    "Она легко принимает меня целиком, когда я прижимаю её к двери душевой."
    image sarah shower doggy part 2 = Movie(play="images/characters/sarah/hscenes/showerSex/part2.webm")
    show sarah shower doggy part 2 with fade
    pause
    sarah.c "А-а-а~ [mc.name]..."
    mc.c "Ты божественна, Сара."
    sarah.c "Ну перестань..."
    mc.c "Что? Это правда."
    sarah.c "Я начинаю думать, что тебе нравится только моя попа..."
    mc.c "Она и правда сводит меня с ума... Как и всё остальное в тебе."
    sarah.c "М-м-м~ Ладно, прощу тебя~"
    "Нежно и приятно, но мне хочется большего."
    image sarah shower doggy part 3 = Movie(play="images/characters/sarah/hscenes/showerSex/part3.webm")
    show sarah shower doggy part 3 with fade
    pause
    "Я притягиваю её к себе и начинаю сильно шлёпать по попке."
    "Я крепко держу её за талию и двигаю вверх-вниз на своём члене."
    sarah.c "О-о-о~ Чёрт~"
    sarah.c "А-а~ [mc.name]... Да~"
    "С каждым толчком Сара дрожит, пока я прижимаюсь к ней."
    "С её мокрой шерсти при каждом движении слетают брызги."
    image sarah shower doggy part 4 = Movie(play="images/characters/sarah/hscenes/showerSex/part4.webm")
    show sarah shower doggy part 4 with fade
    pause
    "Сара опускает плечи и изо всех сил упирается ладонями в стекло."
    "Поза немного ненадёжная... Но чертовски горячая."
    sarah.c "А-а-а~ Да~ А-а-а~ [mc.name]~"
    "Хочу взять её без остатка... наполнить... оплодотворить..."
    "Я теряю голову от животной страсти."
    image sarah shower doggy part 5 = Movie(play="images/characters/sarah/hscenes/showerSex/part5.webm")
    show sarah shower doggy part 5 with fade
    pause
    "Я резко вхожу в неё, прижимая к стеклу."
    sarah.c "А-а~! А-а-а~! А-а-а~! Да~!"
    "С каждым толчком я почти отрываю её от пола, глубоко входя в неё."
    sarah.c "Трахай свою собачку~ Она вся твоя~"
    "Она сводит меня с ума, когда так заводится."
    "Сара вздрагивает с каждым толчком, прижав грудь к стеклу."
    sarah.c "М-м-м~ Да-а~! [mc.name]~!"
    image sarah shower doggy part 6 = Movie(play="images/characters/sarah/hscenes/showerSex/part6.webm")
    show sarah shower doggy part 6 with fade
    pause
    "Её крики удовольствия разносятся по ванной, заглушая вместе со шлепками тел шум текущей воды."
    "Я уже на пределе."
    mc.c "Сара... Я..."
    mc.c "Можно?.."
    sarah.c "Да~ Наполни меня~!"
    sarah.c "Кончи глубоко в меня~~!"
    "С каждым движением я всё ближе..."
    mc.c "Сара!"
    sarah.c "М-м-м-м~"
    image sarah shower doggy finish = Image("images/characters/sarah/hscenes/showerSex/finish.webp")
    show sarah shower doggy finish with fadewhite
    pause
    "Я кончаю глубоко в ней, выдавливая последнюю каплю."
    "Сара обмякает, прижавшись плечами к стеклу, и дрожит от наслаждения."
    "Я вытаскиваю член из её наполненной киски, и сперма тут же начинает вытекать."
    mc.c "Ох, чёрт..."
    sarah.c "*Ах* *Ах*"
    sarah.c "Ничего себе~ Боже мой~"
    sarah.c "Почему же это... было ещё лучше~?"
    "Вода смывает наши следы, пока мы приходим в себя."
    sarah.c "Ничего себе... Ты совсем не сдерживался."
    mc.c "Я весь день сдерживался. Ты слишком соблазнительная."
    sarah.c "Рада это слышать..."
    mc.c "И теперь мне не надо принимать душ. Видишь? Практично."
    sarah.c "Ну, как скажешь..."
    scene black with fade
    "Мы заканчиваем уже более... обычным душем, помогая друг другу помыться."
    "Это всё равно очень эротично. Я уже думаю о том, чтобы повторить..."
    "Но в конце концов мы заканчиваем и одеваемся."
    call playMusic(chillTheme) from _call_playMusic_231
    $ location_home.showBackground()
    show sarah tease talk with dissolve
    sarah.c "Не знаю, во что я ввязалась с тобой."
    sarah.c "Ты правда совсем не умеешь себя контролировать?"
    show sarah tease
    mc.c "Стыдно признаться, но рядом с тобой — похоже, нет."
    mc.c "Сможешь вообще меня терпеть?"
    show sarah bashful talk
    sarah.c "Буду считать это комплиментом."
    show sarah smile talk
    sarah.c "Ладно, извини, мне надо бежать. Встречаюсь с парой одногруппников."
    show sarah smile
    mc.c "Конечно, без проблем."
    show sarah smile talk 2
    sarah.c "Спасибо за сегодняшний день, [mc.name]."
    show sarah smile
    mc.c "За пляж или за секс?"
    show sarah tease
    "Она оборачивается с немного смущённой улыбкой."
    show sarah tease talk
    sarah.c "Ладно-ладно, и за то и за другое, дурачок."
    hide sarah with dissolve
    show sarah kiss with dissolve
    sarah.c "*М-м*"
    hide sarah with dissolve
    show sarah smile talk with dissolve
    sarah.c "Пока!"
    hide sarah with dissolve
    "Сара уходит, улыбаясь."
    "Ну и девушка..."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return {'location':location_home}

label sarahHEvent6(fromGallery = False):
    $ location_town.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_232
    show sarah smile with dissolve
    "Мы с Сарой возвращаемся домой после небольшой совместной прогулки."
    "Приятная прогулка, кафе и экскурсия по городу."
    "Теперь мы просто разглядываем витрины, идя по улице."
    "Сара останавливается у магазина одежды. Она что-то рассматривает в витрине, но с моего угла не видно, что именно."
    show sarah surprise
    sarah.c "Ой, э-э, [mc.name]."
    show sarah smile talk
    sarah.c "Раз уж мы здесь, не против, если я куплю пару вещей?"
    show sarah smile
    mc.c "Конечно. Что-нибудь конкретное?"
    show sarah bashful talk
    sarah.c "Нет... Просто... Нужно кое-что, чего у меня не хватает."
    show sarah bashful
    mc.c "А, понятно. Значит, кружевное женское бельё! Конечно, пойдём."
    show sarah mad talk
    sarah.c "Да замолчи, [mc.name]..."
    sarah.c "Но да, мне бы не помешало купить бельё и ещё кое-что."
    show sarah mad
    mc.c "Устроишь мне небольшое дефиле в новом белье?"
    show sarah mad talk
    sarah.c "После такого — ни за что, придурок!"
    show sarah mad
    mc.c "Мой день разрушен..."
    "Она всё равно улыбается. Ей не привыкать к поддразниваниям."
    show clothesshop with fade
    show sarah thinking with dissolve
    sarah.c "Так, где же оно?.."
    show sarah tease talk
    sarah.c "Знаешь что, тебе тоже стоит кое-что купить. Половина твоей одежды вся в дырках."
    show sarah tease
    mc.c "Мне эти дырки нравятся. В этой одежде я уже много лет хожу."
    show sarah tease talk
    sarah.c "Иди выбери что-нибудь в мужском отделе. Не хочу, чтобы ты подглядывал за женским бельём~"
    show sarah tease
    "Она меня прогнала. Неужели она не хочет, чтобы я видел, что выбирает?"
    mc.c "Ну ладно... Тогда скоро тебя найду."
    show sarah smile talk 2
    sarah.c "Хорошо, я недолго."
    hide sarah with dissolve
    "Мне, пожалуй, не помешала бы парочка футболок."
    scene black with fade
    "Я перебираю одежду на нескольких стойках. Ничего мне не нравится."
    "После недолгих вялых поисков одежды я замечаю, как Сара машет мне."
    show clothesshop with fade
    show sarah smile with dissolve
    "У неё в руках упаковка белья и носков, а под мышкой зажат какой-то комок ткани. Не могу понять, что это."
    mc.c "Что нашла?"
    show sarah bashful talk
    sarah.c "Я купила то, что нужно, но, кажется, хочу кое-что примерить. Ты не против?"
    show sarah bashful
    mc.c "Конечно, давай."
    show sarah bashful talk
    sarah.c "Хорошо, пойдём со мной, но подожди снаружи. Может, спрошу твоё мнение."
    show sarah bashful
    "Что она нашла? Она ведёт себя немного странно."
    call playMusic(heartTheme) from _call_playMusic_233
    hide sarah with dissolve
    "Она почти нерешительно скрывается в примерочной."
    "Неужели всё-таки покажет мне обновку?"
    "Через пару минут шороха она отодвигает занавеску."
    scene sarahhevent6i1 with fade
    pause
    "Ничего себе!"
    "Сара в милом платье! Никогда не видел её в таком."
    "Она совсем не похожа на себя обычную. Выглядит невероятно... женственно."
    "Она позирует, слегка выставив колено, но видно, что ей совершенно некомфортно."
    mc.c "Ничего себе, Сара! Тебе очень идёт!"
    sarah.c "Правда?.."
    mc.c "Конечно! Почему ты выбрала именно его? Я никогда не видел тебя в таком." 
    sarah.c "Просто увидела и подумала... Не знаю... Что-нибудь необычное."
    mc.c "Оно хорошо сидит? Купишь?"
    sarah.c "Не, глупость какая-то. Просто шутка! Думала, будет смешно, ха-ха..."
    mc.c "На тебе оно совсем не глупо смотрится. Правда, потрясающе!"
    sarah.c "Не стоит... Я бы его не носила, будет зря потрачено..."
    "Наверное, так и есть. Хотя иногда было бы здорово видеть её в чём-то таком."
    mc.c "Если ты уверена. Если дело в деньгах, я не против..."
    sarah.c "Нет! Правда, не стала бы... Для меня оно слишком смелое. Как девушки вообще такое носят?"
    sarah.c "Я повешу его обратно. Давай возьмём только это..."
    scene black with fade
    "Она возвращает платье и оплачивает необходимые покупки."
    "Я тоже ничего себе не нашёл."
    call playMusic(chillTheme) from _call_playMusic_234
    $ location_town.showBackground()
    show sarah neutral with dissolve
    "Всё ещё немного раскрасневшись, мы идём дальше. Что это вообще было?"
    "Мы проходим мимо продуктового магазина."
    show sarah smile talk
    sarah.c "Слушай, может, я приготовлю что-нибудь у тебя? Куплю продуктов и зайду?"
    sarah.c "Ты всегда водишь меня куда-нибудь поесть. Давай попробуем что-нибудь другое."
    show sarah smile
    mc.c "Ты же знаешь, я не умею готовить... Не хочу подвергать тебя испытанию моими блюдами."
    mc.c "Ты умеешь готовить? Знаю, каково жить студентом."
    show sarah mad talk
    sarah.c "К-конечно умею! Немного! Какая женщина не приготовит хороший ужин для..."
    sarah.c "Я кое-что умею готовить!"
    show sarah mad
    "Это совсем не похоже на Сару."
    mc.c "Конечно, было бы здорово! Не могу отказаться. Но можем пойти к тебе — на знакомой кухне тебе будет проще."
    mc.c "Или ты всё ещё прячешь меня от друзей?"
    "Я понимающе толкаю её в бок."
    show sarah bashful talk
    sarah.c "Не в этом дело... Фу... Тебе {b}точно не{/b} стоит видеть, что у меня на кухне."
    sarah.c "Она даже не была чистой, когда мы въехали. Что мы должны были делать? И никто за собой не убирает."
    show sarah bashful
    mc.c "Ты, я уверен, тоже."
    show sarah mad talk
    sarah.c "Э-э, ну... Я {b}стараюсь{/b}, но почему я всегда должна убирать за всеми?"
    show sarah neutral talk
    sarah.c "Так что, купить продуктов?"
    show sarah neutral
    mc.c "Было бы здорово, спасибо, Сара. Пойдём."
    show sarah smile talk
    sarah.c "Подожди здесь. Пусть будет сюрприз!"
    show sarah smile
    mc.c "Ладно."
    hide sarah with dissolve
    "Она скрывается в магазине."
    scene black with fade
    "Через некоторое время она выходит с пакетом продуктов, из которого торчат овощи."
    "По дороге домой она не раскрывает секрет."
    $ location_home.showBackground()
    show sarah smile talk
    sarah.c "Ладно, пойду готовить."
    show sarah smile
    mc.c "Помочь?"
    show sarah surprise
    sarah.c "Не-а! И на кухню не заходи! Это сюрприз!"
    mc.c "Звучит заманчиво. Не терпится попробовать."
    show sarah bashful talk
    sarah.c "Ну, посмотрим..."
    hide sarah with dissolve
    "Она скрывается на кухне. День становится всё страннее."
    "..."
    call stopMusic from _call_stopMusic_43
    "*Грохот*"
    sarah.c "Ой..."
    "*Бах*"
    sarah.c "Чёрт..."
    "Следующие двадцать минут из кухни доносятся всевозможные звуки, грохот и вскрики."
    "Там либо готовят что-то авангардное, либо находится самый неуклюжий повар в мире."
    mc.c "Ты уверена, что помощь не нужна?"
    sarah.c "Н-нет! Всё хорошо!"
    "Ладно, не буду ей мешать."
    "..."
    "Через некоторое время снова что-то грохочет..."
    sarah.c "Э-э... [mc.name]... уже несу..."
    "Я сажусь за стол, и Сара выходит с двумя тарелками."
    call playMusic(heartTheme) from _call_playMusic_235
    show sarah sad talk with dissolve
    sarah.c "Это... Э-э... Ну..."
    show sarah sad
    "Она ставит тарелку передо мной. Первым делом мне хочется отшатнуться."
    "Передо мной коричнево-серая непонятная масса, не похожая ни на что знакомое."
    mc.c "С-спасибо. Э-э... Что это?"
    show sarah sad talk
    sarah.c "Ой, чувак, даже не догадаешься... Это вообще не похоже на то, чем должно было быть."
    sarah.c "Это... должна была быть лазанья."
    show sarah sad
    "Теперь, если очень постараться, я могу представить, что когда-то это было похоже на лазанью."
    "Но откуда взялся серый цвет?"
    mc.c "Ха-ха, не переживай, внешний вид еды для меня ничего не значит. Отлично, спасибо!"
    show sarah bashful talk
    sarah.c "Э-э... Ну..."
    show sarah bashful
    "Я набираю вилкой небольшую порцию и внимательно рассматриваю её. Настоящая загадка. Нужно сохранять непредвзятость."
    "..."
    "На вкус одновременно горелое, сырое, горячее, холодное, пресное и пересоленное. Как это возможно?"
    "Сара тоже осторожно пробует кусочек."
    show sarah sad
    "Ей тоже не нравится."
    call stopMusic from _call_stopMusic_44
    show sarah sad talk
    sarah.c "Чёрт... Ужасно."
    show sarah sad
    mc.c "Это... необычно."
    call playMusic(sadTheme) from _call_playMusic_236
    show sarah sad talk
    sarah.c "Нет... Это отвратительно. Чёрт, у меня вообще ничего не получается..."
    show sarah sad
    mc.c "Погоди, успокойся. Всё не так плохо, правда."
    "Хотя это неправда. Как вообще можно так приготовить мясо, пасту и сыр?"
    "Она и правда выглядит расстроенной. Попробую разрядить обстановку."
    mc.c "Ты ещё не пробовала мою стряпню, ха-ха! Эта кухня многое повидала."
    "Не помогает. Кажется, она вот-вот расплачется."
    mc.c "Погоди, Сара, что случилось? Ничего страшного."
    show sarah bashful talk
    sarah.c "Просто... Сегодня я выставила себя полной дурой. И после всего..."
    show sarah sad talk
    sarah.c "У меня вообще ничего не получается... {size=28}для... {size=20}тебя...{/size}"
    show sarah sad
    "Что она имеет в виду? Сегодня она странно себя ведёт, совсем не как обычно."
    mc.c "С тобой сегодня что-то не так, Сара. Что происходит?"
    show sarah sad talk
    sarah.c "Мне хотелось бы быть для тебя настоящей девушкой, [mc.name]."
    sarah.c "Мои подруги, у которых есть парни... Они красивые, нежные и заботливые. Такие... женственные."
    show sarah mad talk
    sarah.c "Они готовят и убираются, красиво выглядят в юбках и платьях, заботятся о своих парнях..."
    sarah.c "А я ничего этого не умею. Не могу! Я..."
    show sarah sad talk
    sarah.c "Вокруг столько других девушек... Зачем тебе быть с лохматой собакой? Я тебя потеряю..."
    show sarah sad
    "Не верится, что я это слышу. Неужели она и правда думает, что недостаточно хороша для меня?"
    "Я пересаживаюсь к ней и сжимаю её плечи."
    mc.c "Ты с ума сошла."
    sarah.c "..."
    mc.c "Как ты вообще можешь думать, что {b}я{/b} так считаю?"
    mc.c "Мы же уже говорили об этом! Зачем бы я был с тобой, если бы хотел, чтобы ты изменилась?"
    mc.c "Ты весёлая, игривая, интересная и красивая. Нам ведь хорошо вместе, правда?"
    mc.c "Я с тобой, потому что люблю всё это! Ты потрясающая!"
    mc.c "Сейчас я не хотел бы быть нигде больше."
    show sarah bashful talk
    sarah.c "Я не красивая..."
    show sarah bashful
    mc.c "Красивая! Горячая, сексуальная, милая, очаровательная — вся такая! Тебе не нужны никакие нарядные платья."
    show sarah bashful talk
    sarah.c "Я ещё какое-то время не буду готовить..."
    show sarah bashful
    mc.c "Я и так предпочитаю еду на вынос."
    show sarah sad talk
    sarah.c "И буду ходить в шортах и майке..."
    show sarah sad
    mc.c "Так лучше видно твоё милое тело."
    sarah.c "..."
    show sarah bashful talk
    sarah.c "Боже, какая же я глупая... Прости..."
    show sarah bashful
    "Не могу смотреть, как ей плохо... Я притягиваю её к себе."
    hide sarah with dissolve
    show sarah kiss with dissolve
    pause
    sarah.c "М-м-м~"
    hide sarah with dissolve
    show sarah bashful talk with dissolve
    sarah.c "Я не выпрашивала комплименты... Просто... Не знаю... Увидела подруг, и..."
    show sarah bashful
    mc.c "Хватит, Сара. Будь собой."
    sarah.c "..."
    show sarah bashful talk
    sarah.c "Так... что будем делать с едой?"
    show sarah bashful
    "Неаппетитная масса становится ещё хуже, пока остывает."
    mc.c "Могу сварить лапшу."
    show sarah neutral talk
    sarah.c "...Ладно..."
    show sarah neutral
    "Она слегка улыбается."
    call stopMusic from _call_stopMusic_45
    scene black with fade
    "Мы ужинаем настоящим пиршеством из... лапши быстрого приготовления."
    "Мы устраиваемся поудобнее, и Сара постепенно успокаивается после моих слов. Хотелось бы, чтобы ей не приходилось искать утешения."
    "Но я буду поддерживать её до конца жизни."
    "Пара напитков, немного телевизора — и мир снова прекрасен."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_home.showBackground()
    call playMusic(heartTheme) from _call_playMusic_237
    show sarah smile with dissolve
    "Сара задерживается у меня допоздна, и вечер получается очень приятным."
    "Она снова улыбается и становится самой собой. Лучше всего вести себя как обычно."
    mc.c "Так и не вернёшься за тем платьем?"
    show sarah thinking
    sarah.c "Хм... А стоит?"
    show sarah tease talk
    sarah.c "Я бы надела его только для тебя. На улице я бы ни за что в нём не показалась."
    show sarah tease
    mc.c "Даже чтобы побегать по лугам, усыпанным ромашками?"
    show sarah tease talk
    sarah.c "Это хоть {b}похоже{/b} на меня?"
    show sarah tease
    mc.c "Даже отдалённо нет."
    hide sarah with dissolve
    show sarah hug with dissolve
    "Она бросается ко мне в объятия."
    sarah.c "Слушай, уже поздно..."
    mc.c "Тонко намекаешь, что хочешь остаться на ночь?"
    sarah.c "Ну конечно."
    mc.c "Да, намёки — не твоя сильная сторона."
    show sarah kiss with dissolve
    pause
    show sarah hug with dissolve
    sarah.c "Ладно, скажу прямо, чего хочу."
    call stopMusic from _call_stopMusic_46
    sarah.c "Давай займёмся сексом."
    mc.c "Ты меня опередила."
    hide sarah with dissolve
    show sarah bashful talk with dissolve
    sarah.c "Но есть одно условие..."
    sarah.c "Хочу... лицом к лицу."
    show sarah bashful
    "А?"
    mc.c "Погоди, разве мы так ещё не пробовали?"
    show sarah tease talk
    sarah.c "Ты всегда берёшь меня сзади. Мне нравится, но..."
    sarah.c "Я уже начала думать, что тебе нравится только моя попа."
    show sarah tease
    mc.c "Она мне и правда нравится... Не замечал, что мы ещё не..."
    show sarah tease talk
    sarah.c "Хватит болтать."
    show sarah tease
    call playMusic(sexyTheme) from _call_playMusic_238
    scene black with fade
    "Мы быстро раздеваемся и направляемся к кровати."
    "Я укладываю Сару на спину, и мы продолжаем растворяться в объятиях друг друга."
    image sarah makeout part 1 = Movie(play="images/characters/sarah/hscenes/makeout/part1.webm")
    show sarah makeout part 1 with fade
    pause
    "Сара притягивает меня к себе и нежно кладёт руку мне на плечо."
    "Мы закрываем глаза и приоткрываем губы, целуясь и играя языками."
    sarah.c "М-м-м~"
    "Мягкая шерсть Сары шелестит под моими пальцами, когда я глажу её бок."
    sarah.c "М-м-м~ [mc.name]~"
    image sarah makeout part 2 = Movie(play="images/characters/sarah/hscenes/makeout/part2.webm")
    show sarah makeout part 2 with fade
    pause
    "Мы перекатываемся на бок, неловко ищем руками ладони друг друга."
    "Мы крепко сплетаем пальцы и глубоко целуемся, наши языки кружат вместе."
    sarah.c "А-а~ М-м-м~"
    "Мы тихо стонем от удовольствия, отдаваясь ласкам. Сара трётся ногой о меня, и мы прижимаемся грудью друг к другу."
    "Сара порой бывает резкой, неуклюжей и немного пацанистой..."
    "Но в моих объятиях она тает, становясь самой нежной девушкой, которую я когда-либо знал."
    "Как бы ни было хорошо, долго мы так не выдержим."
    image sarah missionary start = Image("images/characters/sarah/hscenes/missionary/start.webp")
    show sarah missionary start with fade
    pause
    "Мы снимаем бельё, и я нависаю над ней, любуясь её прекрасным телом."
    "Почему я так долго не решался быть с ней вот так?"
    sarah.c "[mc.name]..."
    "Я опускаюсь и вхожу в неё."
    image sarah missionary part 1 = Movie(play="images/characters/sarah/hscenes/missionary/part1.webm")
    show sarah missionary part 1 with fade
    pause
    sarah.c "А-а-а~ М-м-м~"
    "Сара прижимается к кровати, когда я медленно вхожу в неё."
    "Горячая и влажная от ожидания, она принимает меня целиком. Стенки её киски сжимаются вокруг меня."
    sarah.c "[mc.name]~ [mc.name]~~"
    "Её грудь вздымается от стонов удовольствия, пока я медленно и размеренно двигаюсь."
    "Когда наши взгляды встречаются, её взгляд полон желания. Хочется просто лечь рядом и провести так всю жизнь."
    mc.c "Дай я приподниму тебя."
    sarah.c "Да~ Хочу ещё~"
    image sarah missionary part 2 = Movie(play="images/characters/sarah/hscenes/missionary/part2.webm")
    show sarah missionary part 2 with fade
    pause
    "Я сажусь и поднимаю её ноги, притягивая её бёдра к себе."
    "Направляя её бёдра за колени, я сильнее вхожу в неё."
    sarah.c "О-о-о~ Чёрт~ Да-а~"
    sarah.c "[mc.name]~ Трахни меня~"
    "Я сильно прижимаю её к кровати, медленно и мощно двигаясь бёдрами."
    "Войдя в Сару до конца, я чувствую, как она сжимает меня и хватается за постель."
    image sarah missionary part 3 = Movie(play="images/characters/sarah/hscenes/missionary/part3.webm")
    show sarah missionary part 3 with fade
    pause
    sarah.c "А-а-а~ М-м-м~ Так хорошо~"
    sarah.c "Мне так нужен ты, [mc.name]~ Очень~"
    "Стоны наслаждения Сары разносятся по комнате. Я уже задыхаюсь."
    "Её пышная упругая грудь покачивается с каждым толчком, но мне хочется увидеть больше."
    "Пора усилить темп. Хочу довести её до криков восторга."
    mc.c "Дай мне руки."
    "Я протягиваю ей руки, она отвечает. Я хватаю её за запястья..."
    image sarah missionary part 4 = Movie(play="images/characters/sarah/hscenes/missionary/part4.webm")
    show sarah missionary part 4 with fade
    pause
    "Я притягиваю её к себе, приподнимая плечи над кроватью, и мощно вхожу в неё."
    sarah.c "А-а! А-а-а~! Чёрт~!"
    sarah.c "Да, [mc.name!u]~ М-м-м~"
    "Я мощно двигаю бёдрами. Влажные шлепки заглушают стоны Сары."
    "Стараюсь не сжимать её слишком сильно, но удовольствие переполняет меня. Она полностью во власти моих рук, и ей это нравится."
    sarah.c "А-а-а~ М-м-м~ О-о-о~"
    image sarah missionary part 5 = Movie(play="images/characters/sarah/hscenes/missionary/part5.webm")
    show sarah missionary part 5 with fade
    pause
    "Её грудь сжимается и подпрыгивает от моих движений."
    "Её киска крепко сжимает меня с каждым толчком, подрагивая от наслаждения."
    sarah.c "ОХ, ЧЁРТ, ЧЁРТ, ЧЁРТ~~~ [mc.name!u], Я КОНЧАЮЮЮ~"
    "Она содрогается от моих толчков и запрокидывает плечи."
    "Я тоже почти на пределе."
    mc.c "Сара, я..."
    sarah.c "А-а~ П-прости~~ М-м-м~ Н-не внутрь~ О-о~ С-сегодня..."
    "Хорошо, что она не забыла об этом, несмотря на происходящее. Я вот-вот кончу."
    mc.c "Сара!"
    image sarah missionary end 1 = Image("images/characters/sarah/hscenes/missionary/end1.webp")
    show sarah missionary end 1 with fadewhite
    pause
    "Я в последний момент вытаскиваю член и крепко притягиваю её к себе, обильно кончая на неё."
    sarah.c "М-м-м~"
    image sarah missionary end 2 = Image("images/characters/sarah/hscenes/missionary/end2.webp")
    show sarah missionary end 2 with fade
    pause
    mc.c "*Ах* *Ах*"
    "Я тяжело дышу, откидываясь после мощного оргазма."
    "Я полностью покрываю Сару спермой, струи долетают до самого её лица."
    sarah.c "*Ах* *Ах* М-м~"
    sarah.c "О-о~ *Ах* [mc.name]~ Чёрт..."
    sarah.c "Это было... *Ах*..."
    mc.c "Потрясающе..."
    sarah.c "Похоже, да, чувак~"
    mc.c "Прости, дай я помогу..."
    "Я тянусь за салфетками, чтобы вытереть Сару."
    call playMusic(heartTheme) from _call_playMusic_239
    scene sarahpillowtalk with fade
    pause
    "Мы перекатываемся на бок и переводим дыхание, наслаждаясь послевкусием."
    sarah.c "Это было так хорошо~"
    mc.c "Как я так долго обходился без классической миссионерской позы с тобой? Мне нужно видеть твоё лицо."
    sarah.c "Это ты называешь классикой? Ты там совсем разошёлся."
    mc.c "Ты такая потрясающая, что я не могу сдержаться."
    sarah.c "А когда ты вообще сдерживаешься?"
    mc.c "Рядом с тобой никогда."
    sarah.c "Ну, было здорово. Разрешаешь снова оторваться~?"
    mc.c "Никакая неудачная еда не помешает мне наслаждаться сексом с тобой."
    sarah.c "Ой, боже, обязательно?"
    mc.c "...Прости."
    "Я нежно целую её в щёку."
    sarah.c "Прости меня за сегодня..."
    mc.c "Я всегда рядом, Сара."
    sarah.c "День был долгий и эмоциональный, я совсем вымоталась."
    mc.c "Мы оба."
    "Я хитро улыбаюсь, намекая, что именно меня вымотало."
    sarah.c "Фу, чувак."
    mc.c "Останься сегодня, Сара."
    sarah.c "Не думаю, что вообще смогу добраться до дома, хе-хе~"
    scene black with fade
    "Мы прибираемся и ложимся спать."
    call sarahSleepover from _call_sarahSleepover_1
    sarah.c "Спокойной ночи, [mc.name]."
    mc.c "Сладких снов."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return {'location':location_home}

label sarahLikeEvent4(fromGallery = False):
    $ location_home.showBackground()
    "Я дома, изучаю кое-что для бара. Пожалуй, пора поменять ассортимент."
    "Смотрю, что продаётся, а что нет. Гляньте на меня — занимаюсь {i}начальницкими{/i} делами. Может, всё наладится."
    call playMusic(funnyTheme) from _call_playMusic_240
    sarah.c "Чёрт! Блин!"
    "А, и Сара тоже здесь."
    show sarah mad talk with dissolve
    sarah.c "Ар-р, да чтоб тебя!"
    show sarah mad
    "Она пришла не ко мне — просто отлично пользуется моей приставкой. Увлеклась какой-то новой игрой."
    "Это одиночная игра, но иногда интересно смотреть через плечо, особенно когда она так... увлечена."
    "Кажется, это уже пятая или шестая попытка. Сначала она продвигалась хорошо, но по звукам за последний час ясно — стало трудно."
    show sarah surprise
    sarah.c "Чувак, ты видел? Ну же!"
    mc.c "Похоже, тебя там разносят."
    show sarah mad talk
    sarah.c "Да-да, как скажешь."
    show sarah surprise
    sarah.c "А-а!"
    "Она погибла."
    mc.c "Ты погибла."
    show sarah mad
    sarah.c "..."
    show sarah mad talk
    sarah.c "Очень наблюдательно, придурок."
    show sarah mad
    mc.c "Сделай перерыв, если уже не весело."
    show sarah mad talk
    sarah.c "Мне {i}весело{/i}! Было бы ещё веселее, если бы ты не язвил..."
    show sarah mad
    "Взгляд у неё убийственный... Обожаю её дразнить. К счастью, кажется, я ещё ни разу не перегнул палку."
    show sarah bashful talk
    sarah.c "Чёрт... Здесь я застряла. Как он это сделал?.."
    show sarah bashful
    "Она достаёт телефон и хмурится."
    show sarah mad talk
    sarah.c "Ну давай, оставь меня без ответа, мелкий засранец."
    show sarah mad
    mc.c "Кто не отвечает?"
    show sarah neutral talk
    sarah.c "А, младший брат. Он тоже в это играет. Говорит, что всё легко! Уверена, когда мы переписывались, он уже прошёл этот участок."
    show sarah mad talk
    sarah.c "Я написала ему вчера, а он так и не ответил. И ведь точно видел! Вот же..."
    show sarah mad
    mc.c "Занятой парень? Сколько ему лет?"
    show sarah neutral talk
    sarah.c "Ему... Чёрт. Уже пятнадцать... Куда время делось?"
    show sarah neutral
    mc.c "А, середина подросткового возраста. Наверное, у него есть дела поважнее, чем его занудная старшая сестра."
    show sarah mad
    sarah.c "..."
    show sarah mad talk
    sarah.c "Я сейчас {i}не в лучшем{/i} настроении... Будь осторожен, если хочешь, чтобы я когда-нибудь снова с тобой переспала."
    show sarah mad
    mc.c "...Понял."
    call playMusic(heartTheme) from _call_playMusic_241
    show sarah bashful talk
    sarah.c "Эх... В последнее время он всё чаще так себя ведёт..."
    show sarah neutral talk
    sarah.c "Почти не отвечает на мои сообщения... Вечно хмурый..."
    sarah.c "А когда я приезжаю домой, он либо уходит к друзьям, либо сидит в своей комнате..."
    show sarah sad talk
    sarah.c "Куда делся мой милый младший брат?"
    show sarah sad
    mc.c "Каким он был раньше?"
    show sarah smile talk 2
    sarah.c "Таким милым... Мы всё время болтали и играли!"
    show sarah smile talk
    sarah.c "Играли... Грязными бегали по улице... Я помогала ему с домашними заданиями... Даже научила его кататься на велосипеде..."
    show sarah joy
    sarah.c "Когда показывал оценки, всегда кричал: «Сар, Сар, смотри!»"
    "Я бы пошутил насчёт успехов Сары в учёбе, но сегодня и так уже слишком близко подошёл к опасной черте."
    show sarah smile talk 2
    sarah.c "А когда к нему приходили друзья, мы все вместе играли."
    show sarah neutral talk
    sarah.c "Я даже не знаю, кто теперь его друзья."
    show sarah neutral
    mc.c "Даже школьные друзья? Редкость, когда ребёнок не стесняется старшей сестры перед приятелями."
    show sarah tease talk
    sarah.c "Да они все меня обожали. Со старшей девчонкой можно было играть в спорт и видеоигры..."
    sarah.c "Кажется, парочка даже была в меня влюблена~"
    show sarah tease
    mc.c "Не сомневаюсь..."
    mc.c "Он просто взрослеет... Ты ведь в его возрасте тоже менялась. Мы все менялись."
    show sarah bashful talk
    sarah.c "Ага... Просто... Я скучаю по своему милому братишке. Он меняется, пока меня даже нет рядом..."
    show sarah bashful
    "Грустно... Мне её жаль."
    "С самого знакомства она с теплотой говорит о младшем брате. Уверен, в детстве она была бы прекрасной старшей сестрой."
    "Похоже, она прекрасно ладит с детьми. Я сам это видел — она всегда игрива и дружелюбна с незнакомыми детьми в общественных местах."
    "Не могу не задуматься... Ограничивается ли её любовь к детям дружбой с ребятами школьного возраста?"
    "Как бы она вела себя с малышом... подолгу..." 
    "Хотела бы она своих детей?"
    "Мы никогда об этом не говорили... А почему? Мы знакомы не так давно. Просто двое молодых людей, влюблённых друг в друга."
    "Или... После признания, после всего времени вместе... Мы уже на том этапе? Разве нам не стоит обсуждать такие вещи?"
    "А вдруг она очень хочет детей, а я нет? Или наоборот? Что станет с нашими отношениями?"
    "Чего же {i}я{/i} хочу? С Сарой?.."
    "Она задумчиво улыбается экрану телефона, вероятно, перечитывая переписку с братом."
    "Можно ли осторожно подвести разговор к этой теме? Наверное, стоит попробовать... Уверен, она отнесётся к этому разумно и спокойно."
    mc.c "Ты ведь всегда хорошо ладила с детьми?"
    show sarah smile talk
    sarah.c "Хе, да, наверное. Мы с братом и его друзьями всегда ладили. У нескольких подруг тоже были братья или сёстры, и мы находили общий язык."
    show sarah smile talk 2
    sarah.c "В основном я была для них вроде приятеля, ха-ха."
    show sarah smile
    mc.c "А с девочками?"
    show sarah neutral talk
    sarah.c "Думаю, тоже хорошо. Особенно маленькие — они играют, как и любые дети, правда?"
    sarah.c "Некоторые старшие сёстры моих подруг мне не нравились, но это ничего не значит — тогда {i}я{/i} сама была ребёнком."
    show sarah tease talk
    sarah.c "Когда они становятся такими модными и изысканными... Наверное, тогда мы уже не на одной волне. Не удивительно, хе-хе."
    show sarah tease
    "Ага, это подтверждает мои мысли... Она всегда очень дружелюбна с детьми, хотя другие могут закатывать глаза и раздражаться. У неё талант."
    "Никак не подвести к этому разговору плавно, да? Ладно..."
    mc.c "Скажем... Когда ты росла... Ты когда-нибудь думала, что, может быть... Ты могла бы..."
    show sarah smile talk 2
    sarah.c "Говори уже, чувак!"
    show sarah smile
    "Да, я ужасно это формулирую."
    mc.c "Ты когда-нибудь думала о том, чтобы завести собственных детей?"
    sarah.c "..."
    show sarah neutral talk
    sarah.c "Хе... Что?"
    show sarah neutral
    "Она смотрит на меня совершенно непонимающе... Как она отреагирует?"
    mc.c "Просто... Гипотетически..."
    sarah.c "..."
    show sarah joy
    sarah.c "Ха-ха! Представляешь?"
    show sarah tease talk
    sarah.c "Ладно-ладно, ты меня сегодня уже слишком дразнил. Похоже, какое-то время секса тебе не видать~"
    show sarah tease
    "Так, она не воспринимает меня всерьёз. Уходит от ответа или правда не верит?"
    mc.c "Почему нет? Ты хорошо ладишь с детьми. Я подумал, может, ты об этом задумывалась."
    show sarah surprise
    sarah.c "Чувак... Ты серьёзно?"
    mc.c "Ага. Просто стало интересно..."
    show sarah joy
    sarah.c "Ха-ха! Боже мой!"
    show sarah smile talk 2
    sarah.c "Ты, блин, шутишь. Я? Мама?"
    show sarah smile talk
    sarah.c "Ну... Просто представь! Вот представь!"
    show sarah smile
    mc.c "Вроде могу."
    show sarah surprise
    sarah.c "Что, чувак?! Ни за что."
    show sarah tease talk
    sarah.c "Чувак... Ты правда можешь представить меня в цветастом платьице и с маленьким животиком?"
    sarah.c "Помешиваю большую кастрюлю, пока малыш бегает у меня под ногами? Убираю за ним, вытираю пятнышко со щеки?"
    show sarah tease
    mc.c "Ну... Не обязательно всё было бы именно так. Ты бы осталась собой, просто... с маленькой частичкой себя рядом."
    show sarah surprise
    sarah.c "..."
    show sarah bashful
    "Она отводит взгляд, поняв, что я не шучу."
    show sarah bashful talk
    sarah.c "Чувак... Я..."
    sarah.c "Ну... Конечно, я иногда об этом думала..."
    show sarah neutral talk
    sarah.c "Каждая девушка хоть раз об этом задумывается, да?.."
    show sarah bashful talk
    sarah.c "Но... не так уж много."
    show sarah bashful
    mc.c "Я не вкладывал в это особого смысла. Мы же ещё молодые. Не говорю, что тебе нужно об этом думать."
    "Чёрт, я сказал «{b}мы{/b} ещё молодые». Не хотел намекнуть, что мы..."
    mc.c "Просто хотел узнать, думала ли ты об этом... Не то чтобы нужно было куда-то торопиться."
    show sarah neutral talk
    sarah.c "Не... Да брось... Я? Не думаю, что {i}когда-нибудь{/i} стану такой..."
    show sarah neutral
    mc.c "Почему? Ты всегда хорошо ладила с детьми, и им ты явно нравишься..."
    mc.c "Ты добрая, заботливая, чуткая, практичная..."
    show sarah bashful talk
    sarah.c "Хе, практичная? Я не умею готовить и убираться... У меня даже работы нет."
    show sarah bashful
    mc.c "Ну, пожалуй. Но если посмотреть на других родителей..."
    mc.c "Думаю, ты была бы прекрасной матерью."
    "Для неё это довольно неожиданно. Прости, Сара, но мне нужно было это сказать."
    show sarah bashful talk
    sarah.c "Чувак..."
    show sarah bashful
    mc.c "Прости, что вывалил это на тебя. Я не делал предложение, просто решил спросить."
    show sarah neutral talk
    sarah.c "Да ничего. Наверное... это вполне нормальный разговор, да?"
    sarah.c "Раз уж мы вместе... Вполне естественно, что ты спросил."
    show sarah neutral
    mc.c "Если хочешь, можем на этом закончить. Прости."
    show sarah bashful talk
    sarah.c "Да... Просто застал меня врасплох."
    show sarah bashful
    "Всё прошло не совсем так, как я представлял... Или как хотел..."
    "Если бы я был немного тактичнее... Не забегаю ли я вперёд? Она ещё учится в колледже, и я сам не так давно оттуда выпустился."
    "Но это не прозвучало как категоричное «нет»... Если бы она совсем не хотела детей, просто сказала бы, да? Похоже, она просто не уверена в себе."
    "Пора оставить эту тему. Может, хотя бы закончим разговор на хорошей ноте?"
    mc.c "Представь... Маленькая ты, которая поможет тебе наконец выиграть в игры, в которых ты так плоха."
    show sarah smile talk
    sarah.c "Хе-хе, эй! Вот обидно."
    show sarah smile talk 2
    sarah.c "Ты бы заставил его разливать пиво, как только он до стойки дотянется, да, маленький эксплуататор?"
    show sarah smile 
    mc.c "Эй..."
    scene black with fade
    "Мы сглаживаем неловкость и продолжаем день в хорошем настроении."
    "Она удивилась и отмахнулась, но мне кажется... Может быть... Когда-нибудь..."
    "После сегодняшнего разговора я всё чаще об этом думаю... И могу представить такую жизнь лучше, чем раньше."

    if(not fromGallery):
        $ sarah.addLike(1)
        $ sarah.addLove(1)
    
    return

label sarahLikeEvent5Invitation(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_242
    show sarah smile
    "У нас с Сарой всё спокойно и хорошо."
    "Мы всё больше похожи на настоящую пару. Особенно после той ночи на тропе..."
    "Изменилось не так уж много: она всё такая же шумная и простая в общении. Не стала вдруг чересчур нежной и влюблённой..."
    "Просто между нами словно стало меньше преград... Я уже не сомневаюсь, серьёзны ли наши отношения, и больше доверяю им. Между нами всё ясно."
    "Она довольно спокойная студентка, но её график постоянно меняется: то бесконечно много свободного времени, то она запирается и зубрит..."
    "Иногда я вижу её реже, чем хотелось бы. Жаль."
    "Если она не приходит ко мне, другая возможность — её студенческий дом — почему-то недоступна."
    "Она категорически отказывается пускать меня. Говорит, что там грязно, ничего не работает, соседи устроили беспорядок..."
    "Я уже несколько раз привозил её и забирал, но дальше входной двери так и не заходил."
    "Я понимаю: видел, в каком ужасном состоянии бывает студенческое жильё. Привыкнув, перестаёшь замечать, насколько всё плохо."
    "Может, соседи всё ещё подшучивают над ней из-за всего этого «человека»..."
    "В любом случае, её жильё — запретная территория. Мы не проводим время у неё."
    "Впрочем, это не проблема. Сара знает, что может приходить ко мне когда угодно. И она этим пользуется."
    "Похоже, ей у меня нравится. Она постоянно говорит, какая удобная у меня кровать... А диванами и игровой приставкой она точно пользуется вовсю."
    "Интересно, хотела бы она сделать это более постоянным... Я был бы только рад."
    "На самом деле, я был бы в восторге."
    "Просыпаться вместе... Засыпать вместе... Возвращаться домой после работы, где меня ждёт весёлая Сара... Это было бы счастье."
    "Но хотела бы она этого? Не хочу отрывать её от соседей, но так она могла бы выбраться из ужасных условий."
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Да!' if(homeHasRoom) else "Нужно улучшить жильё" 
    if(not fromGallery):
        menu:
            "Стоит ли предложить Саре переехать ко мне? Этот выбор можно сделать в любое время."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "Пока нет":
                call endCharacterInteraction(sarah) from _call_endCharacterInteraction_5
    "Почему бы и нет? Наверняка ей это уже надоело."
    "Всё зависит от договора аренды. Иногда договоры в студенческих домах даже не действуют целый год."
    mc.c "Слушай, Сара."
    show sarah smile talk 2
    sarah.c "Чё как, чувак?"
    show sarah smile
    mc.c "Что там с твоим жильём? Какой у вас договор?"
    call playMusic(funnyTheme) from _call_playMusic_243
    show sarah surprise
    sarah.c "Ох, чувак, ты сейчас откроешь целый {i}ящик{/i} проблем..."
    mc.c "Что случилось?"
    show sarah bashful talk
    sarah.c "Господи, там полный бардак."
    show sarah neutral talk
    sarah.c "Нас там пятеро, да? Мы все вместе оформляли жильё через колледж. У них какое-то соглашение с хозяином."
    sarah.c "Договор заканчивается через пару месяцев, и колледж спрашивает, будем ли продлевать. Нужно решить в ближайшее время."
    show sarah bashful talk
    sarah.c "Но Энни может бросить учёбу... Если так, она съедет."
    show sarah surprise
    sarah.c "А Нина говорит, что, может, переедет к парню, но сама толком не решила."
    "Как обычно..."
    show sarah mad talk
    sarah.c "Короче, мы вообще не понимаем, что происходит."
    sarah.c "И почему-то, если они съедут, даже если мы найдём замену, нельзя просто заселить новых людей."
    sarah.c "Что-то про договор, оформленный на всех нас."
    show sarah mad
    mc.c "Звучит как-то неправильно..."
    show sarah surprise
    sarah.c "Вот именно! Какая-то глупость! Если оформлять всё заново, цена вырастет, и ещё какие-то проблемы с залогом..."
    show sarah mad talk
    sarah.c "Чувак, я ничего не понимаю. И никто из нас не понимает."
    show sarah mad
    mc.c "Колледж не помогает?"
    show sarah bashful talk
    sarah.c "В колледже есть какой-то отдел, который всё это оформлял, но там полный хаос и ничего не понятно. Ещё и хозяин дома..."
    sarah.c "Было бы проще сразу всё делать напрямую. Похоже, в следующий раз так и придётся... Вот же головная боль."
    show sarah bashful
    mc.c "Хм... Хорошо, что я как раз собирался спросить..."
    show sarah neutral talk
    sarah.c "А? О чём?"
    show sarah neutral
    mc.c "Звёзды сошлись... Какое счастье..."
    show sarah smile talk 2
    sarah.c "Хе, о чём ты, дуралей? Расскажи."
    show sarah smile
    mc.c "Невероятное совпадение. Хм..."
    "Сара легонько бьёт меня по руке."
    show sarah tease talk
    sarah.c "Что?! Говори уже!"
    call playMusic(heartTheme) from _call_playMusic_244
    show sarah tease
    mc.c "Я хотел спросить, не хочешь ли ты переехать ко мне."
    sarah.c "..."
    "Сара смотрит на меня так, будто не сразу поняла, что я сказал."
    sarah.c "..."
    show sarah surprise
    sarah.c "Ч-что?!"
    "Я знаю, что она услышала. Приподнимаю её висячее ухо и тихо говорю прямо в него."
    mc.c "Я спросил, не хочешь ли ты вместо этого переехать ко мне?"
    mc.c "Я и так собирался спросить, а теперь это кажется отличной идеей, правда?"
    sarah.c "Чувак..."
    show sarah joy
    sarah.c "Ох, чёрт! Конечно!"
    hide sarah with dissolve
    show sarah hug with dissolve
    "Она бросается мне на грудь, чуть не сбивая с ног."
    sarah.c "Боже мой! Конечно!"
    sarah.c "Ты этого хочешь?! Тебя не смущает?"
    mc.c "Ну конечно хочу! Если ты сама этого хочешь."
    sarah.c "[mc.name]~"
    show sarah kiss with dissolve
    sarah.c "М-м~"
    show sarah hug with dissolve
    sarah.c "Чёрт, я сейчас расплачусь..."
    mc.c "Ты и так знаешь, что можешь приходить ко мне когда угодно... Мне очень нравится, когда ты рядом."
    mc.c "Ты всё равно не пускаешь меня к себе, так что я уже забыл о твоём доме."
    sarah.c "Хе~ Вот именно..."
    mc.c "Ну да. Это не должно стать слишком резким изменением... А найти новое студенческое жильё будет сложно..."
    sarah.c "Тебе больше не надо меня уговаривать! Это идеально..."
    show sarah kiss with dissolve
    sarah.c "М-м~"
    hide sarah with dissolve
    show sarah smile with dissolve
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Ты знаешь, что [len(girlsAlreadyMovedIn)] других девушек уже почти переехали, но, возможно, вы ещё не успели нормально познакомиться..."
        if(alice.movedIn and sarahAliceDuoStoryEvent1.unlocked):
            mc.c "Ну, конечно, ты уже знаешь Элис."
            show sarah smile talk 2
            sarah.c "Ага! Мы пару раз болтали об этом. Ей у тебя очень нравится!"
            show sarah smile
        mc.c "Тебя это устраивает?"
        show sarah joy
        sarah.c "Ещё бы! Не могу дождаться!"
        show sarah smile
    mc.c "Тогда можешь переезжать, когда захочешь. До конца договора ещё пара месяцев."
    show sarah joy
    sarah.c "К чёрту, я хочу переехать прямо сейчас!"
    show sarah smile talk 2
    sarah.c "Дай мне пару дней уладить дела и всё рассказать ребятам."
    show sarah smile
    mc.c "Я могу приехать и помочь в любое время. Заходить внутрь не обязательно..."
    show sarah joy
    sarah.c "Да! Боже мой, [mc.name], я тебя люблю!"
    scene black with fade
    "От счастья Сара весь остаток дня не может усидеть на месте. Я так же счастлив, как и она."
    "Она сообщит, когда будет готова, а я приеду за ней на машине. И тогда... Мой дом станет и её домом."
    "Договорились. Загляни в расписание!"

    return

label sarahLikeEvent5(fromGallery):
    call playMusic(memoriesTheme) from _call_playMusic_245
    $ location_home_bedroom.showBackground()
    "Солнечный свет льётся в окно свежим ясным утром."
    "Сегодня будет отличный день. Сара переезжает ко мне."
    "Договор аренды в её студенческом доме и так разваливается, так что это имеет смысл. Похоже, мы оба давно этого хотели."
    "Жизнь с Сарой... Хотя она и так почти превратила мою квартиру во второй дом."
    "Сегодня утром она собирает вещи, и я помогу перевезти хотя бы часть."
    "Мне запретили даже заходить к ней, чтобы помочь собраться... Иногда интересно, не хуже ли там на самом деле, чем я думаю."
    "Так что я сижу и жду, когда она позвонит и разрешит заехать."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "О, может, это сообщение?"
    sarah.c "почти готва"
    sarah.c "машина?"
    "Да, Сара, машина уже ждёт. Пора ехать."
    scene black with fade
    "Я освободил место в машине, хотя не знаю, сколько вещей ожидать. Что у неё вообще есть?"
    "Недолгая поездка — и я снова у знакомого дома."
    scene suburbs with fade
    "Я подъезжаю, а Сара уже вышла с грудой... багажа, если это можно так назвать."
    show sarah smile with dissolve
    "Заметив машину, она широко улыбается и принимается бороться с нелепой кучей сумок."
    show sarah smile talk 2
    sarah.c "Ох~ Доброе утро!"
    show sarah smile
    "Пошатываясь к машине, она роняет на землю пару трусиков."
    show sarah surprise
    sarah.c "Ах!"
    mc.c "Доброе утро. Помочь?.."
    show sarah bashful talk
    sarah.c "Хе, да."
    show sarah bashful
    "Я забираю из её рук несколько неудобных сумок, а она быстро поднимает трусики с тротуара."
    "Горы одежды в пластиковых пакетах, рюкзак, который едва застёгивается и набит странными предметами..."
    mc.c "У тебя что, чемодана не было? Я мог бы привезти вещи, если бы ты позволила помочь."
    show sarah surprise
    sarah.c "Клянусь, был! Понятия не имею, куда он делся!"
    show sarah smile talk 2
    sarah.c "Вот и сложила всё в то, что нашла."
    show sarah smile
    mc.c "Вижу, пригодился ящик с пакетами на кухне."
    show sarah tease talk
    sarah.c "Хе~ Да, там их миллион."
    show sarah tease
    "Мы загружаем оставшиеся сумки и ненадолго останавливаемся."
    show sarah joy
    sarah.c "[mc.name]!"
    hide sarah with dissolve
    show sarah hug with dissolve
    "Она бросается мне в объятия и прижимается к груди."
    sarah.c "Мы и правда это делаем, да?"
    mc.c "Последний шанс передумать..."
    sarah.c "Ни за что! Я давно этого хотела!"
    mc.c "Я так рад..."
    show sarah kiss with dissolve
    sarah.c "Муа~"
    show sarah hug with dissolve
    mc.c "Я люблю тебя."
    sarah.c "И я тебя люблю."
    mc.c "Уже попрощалась с соседями?"
    sarah.c "Да, всё сделала. Думаю, они всё равно ещё спят."
    sarah.c "Да и неважно, большинство я завтра всё равно увижу в колледже!"
    sarah.c "Ну всё, поехали отсюда!"
    scene black with fade
    "Мы садимся в машину и едем домой."
    scene sarahlikeevent5i1 with fade
    pause
    sarah.c "Ха-а~"
    "Войдя внутрь, мы сгружаем «багаж» в угол, а Сара прыгает на диван."
    sarah.c "Вот это {i}настоящий{/i} диван~ Наш старый меня достал. Он разваливался..."
    sarah.c "М-м... Пахнет тобой."
    "Она утыкается лицом в обивку и умиротворённо вздыхает."
    mc.c "Добро пожаловать домой."
    scene sarahlikeevent5i2 with fade
    pause
    sarah.c "Хе-хе~ Спасибо, что приютил меня~"
    sarah.c "Надеюсь, ты понимаешь, на что подписался~"
    mc.c "О да, понимаю. Кажется..."
    sarah.c "Хе~ Иди сюда~"
    "Сара зовёт меня присоединиться к ней на диване, куда она неловко плюхнулась."
    scene sarahlikeevent5i3 with fade
    pause
    "Я переваливаюсь через подлокотник и нависаю над её весёлым лицом."
    sarah.c "Ну... Представь, чем мы теперь будем заниматься~"
    mc.c "Хм... Готовка, уборка, стирка..."
    sarah.c "Э-э... Не это, дурачок!"
    "Я сжимаю её бок, и она вздрагивает."
    sarah.c "Ха-ха! Перестань~"
    "Глядя на её сияющую улыбку, я не могу устоять."
    scene sarahlikeevent5i4 with fade
    pause
    "Я наклоняюсь к ней и прижимаю её к дивану."
    sarah.c "М-м~"
    "Мы ненадолго отстраняемся, чтобы посмеяться, а потом снова прижимаемся друг к другу."
    scene sarahlikeevent5i3 with fade
    pause
    sarah.c "Хе-хе~ Ну ты даёшь."
    mc.c "Можем сделать перерыв и... распаковать вещи."
    sarah.c "Фу~ Потом."
    sarah.c "Я проголодалась."
    mc.c "У тебя теперь новая кухня. Может, приготовишь мне одно из своих знаменитых блюд?"
    sarah.c "Ха! Да ну, чувак, сегодня праздник!"
    sarah.c "Давай закажем пиццу и отдохнём~ Я знаю, что посмотреть."
    mc.c "Вот это план."
    scene sarahlikeevent5i5 with fade
    pause
    "Мы заказываем что-нибудь вкусненькое из любимого места Сары и берём побольше — в честь переезда."
    "Мы разваливаемся на диване и смотрим по телевизору её новое увлечение."
    sarah.c "Чёрт, как вкусно~"
    "Сара и раньше не стеснялась чувствовать себя как дома, но теперь это на самом деле её дом."
    "За то, чтобы таких дней было ещё много."

    if(not fromGallery):
        $ sarah.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label sarahHEvent7(fromGallery):
    call playMusic(funnyTheme) from _call_playMusic_246
    scene sarahhevent7i1 with fade
    pause
    "После переезда Сары жизнь стала прекрасной."
    "Несмотря на её живой характер, студенческий график часто оставляет её дома днём, что прекрасно сочетается с моим гибким расписанием."
    "Теперь я могу просыпаться рядом с ней, а она может приходить и уходить между занятиями. В любом случае, мы проводим вместе больше времени."
    sarah.c "Хе-хе~ Ага!"
    "Кажется, ей тоже нравится. Она вовсю пользуется удобствами... Приставку ещё никогда так часто не включали."
    "Теперь у неё появилось больше денег, и она купила новую часть классического файтинга. Раньше я хорошо играл в одну из старых..."
    sarah.c "Получай, придурок!"
    "В онлайне она уже довольно хороша. Надеюсь, голосовой чат сейчас выключен."
    scene sarahhevent7i2 with dissolve
    sarah.c "Ха! Слишком легко."
    sarah.c "Давай сыграй, чувак. Сейчас подбор слабенький."
    mc.c "Не знаю, не хочу тебя позорить."
    sarah.c "О-о~ Вот как? Тогда придётся подкрепить слова делом."
    mc.c "Как знаешь. Я уже вижу слабые места в твоей игре."
    sarah.c "Ты у меня получишь... А за такую самоуверенность проигравшему полагается наказание."
    mc.c "Да? Проигравший сегодня моет посуду?"
    sarah.c "{i}Скучно~{/i} Может..."
    sarah.c "За каждый раунд снимаем по одной вещи."
    "Интересный выбор, Сара... Какие-то скрытые мотивы?"
    "В любом случае я не вижу проигравших, но забавно смотреть, как она дуется."
    mc.c "Идёт, извращенка."
    sarah.c "Хе-хе~ Вот ты и останешься голым."
    scene sarahhevent7i3 with fade
    "Я сползаю с дивана к ней на пол, и мы запускаем игру."
    "Сара выбирает того же бойца, за которого играла в онлайне. Прямо в мою ловушку..."
    mc.c "Вот этого, да? Ты подписала себе приговор. Я знаю идеальную контратаку."
    sarah.c "Как? Игра только вышла, а я ни разу не видела, как ты играешь."
    mc.c "Я ветеран этой серии."
    sarah.c "Старикан, да? Наверняка с тех пор всё изменилось."
    "Мне нужно время, чтобы войти в ритм. Небольшие различия в движениях сбивают меня."
    scene sarahhevent7i4 with dissolve
    "Нельзя сказать, что бой был близким, но я начинал понимать игру..."
    sarah.c "Ну и где твоя контратака, чувак?"
    mc.c "Хм... Просто привыкаю..."
    sarah.c "Ладно, снимай одежду, неудачник."
    "Я готов продолжать. Снимаю футболку, начинается второй раунд."
    scene sarahhevent7i5 with dissolve
    "Я откидываюсь назад и играю осторожно, понемногу нанося базовые удары, полагаясь на мышечную память."
    sarah.c "Чёрт! Вот же..."
    "Но когда заполняется её шкала спецприёма, я уже не понимаю, что происходит. Всё меняется."
    sarah.c "Да!"
    "Я отчаянно сопротивляюсь, но..."
    scene sarahhevent7i6 with dissolve
    sarah.c "Уже лучше... Но ты всё равно отстой."
    mc.c "Гр-р..."
    "Я заржавел. Чувствую, что уже почти получается, просто..."
    mc.c "Следующий раунд."
    sarah.c "Не-а, штаны тоже снимай."
    scene sarahhevent7i7 with dissolve
    "Третий раунд. Я сижу на полу в одних трусах, как идиот-подросток."
    "Я понемногу вспоминаю, как играть, но и Сара становится лучше."
    sarah.c "Ха! Ха!"
    mc.c "Давай же!"
    "Всё происходит быстро. На экране слишком много всего."
    "Я не успеваю... Я..."
    scene sarahhevent7i8 with dissolve
    "Я проигрываю. На этот раз борьба была равной, но всё равно проиграл."
    sarah.c "*Зевает*~ Да уж, в онлайне играть интереснее."
    mc.c "Я уже почти догоняю..."
    sarah.c "Тебе ещё годы тренироваться, старик."
    sarah.c "Давай, неудачник. Доставай член."
    mc.c "Ладно, но я ещё отыграюсь. Точно доберусь до твоей груди."
    sarah.c "О чём ты? Игра закончилась, чувак. Я победила."
    mc.c "По правилам игры на раздевание всё заканчивается, только когда ты проиграл и на тебе больше нечего снять."
    sarah.c "С каких это пор? Ты всё выдумываешь."
    mc.c "Следующий раунд."
    sarah.c "Хмф..."
    scene sarahhevent7i9 with dissolve
    "В следующем раунде придётся пустить в ход всё, даже грязные приёмы."
    "Надеюсь, этот трюк сработает, а она ещё не сталкивалась с такой защитой от новичков."
    "Я меняю персонажа и выбираю бойца с дешёвыми, простыми снарядами."
    sarah.c "Э-эй, какого чёрта?"
    sarah.c "Это нечестно! Дерись со мной!"
    mc.c "Всё разрешено."
    "Я атакую издалека и снова и снова запускаю снаряды."
    "Она не может подобраться."
    scene sarahhevent7i10 with dissolve
    mc.c "Ха-ха!"
    sarah.c "Да это же нечестно, чувак!"
    mc.c "Приём вполне законный. Научись его контрить, нуб."
    sarah.c "Гр-р... Ты отстой."
    mc.c "Теперь я тебя поймал. Ну-ка покажи грудь."
    sarah.c "Погоди, это только верхний слой."
    mc.c "Да брось, Сара, на тебе даже лифчика нет."
    sarah.c "Ой. Точно."
    scene sarahhevent7i11 with dissolve
    "Она снимает топ, и на следующий раунд грудь уже открыта."
    sarah.c "Да чтоб тебя!"
    "Я немного отвлекаюсь, но благодаря новой тактике всё ещё побеждаю."
    sarah.c "Чёртов придурок!"
    "Может, победа и некрасивым способом, но трофей того стоит."
    scene sarahhevent7i12 with dissolve
    sarah.c "Ты просто ничтожество."
    mc.c "Ничтожество, которое побеждает. Научись играть."
    sarah.c "Чувак... Я будто вижу тебя с совершенно новой стороны..."
    mc.c "Теперь снимай шорты."
    mc.c "Или ты ещё и трусики не надела?"
    sarah.c "Э-э... Кажется, нет..."
    scene sarahhevent7i13 with dissolve
    "В следующем раунде преимущество остаётся за мной."
    "Краем глаза я замечаю, как покачивается её грудь."
    "К счастью для меня, эта тактика настолько проста, что я могу постоянно на неё поглядывать."
    sarah.c "Чёрт!"
    "В этой суматохе, глядя на неё рядом, я начинаю... возбуждаться."
    "Как ни странно, это помогает мне: теперь моя соперница тоже отвлекается..."
    sarah.c "Хр-р... О чём ты думаешь?.."
    scene sarahhevent7i14 with dissolve
    "Не успеваю оглянуться, как на экране снова появляется надпись о моей победе. На этот раз она сопротивлялась ещё меньше."
    "Сара смотрит на мой член."
    sarah.c "Серьёзно, чувак? Как ты можешь сейчас?"
    mc.c "А что такого? Ты бы предпочла, чтобы он не стоял, когда ты голая?"
    sarah.c "Боже... Ну ты и идиот..."
    "Она говорит раздражённо, но в её взгляде проступает желание."
    mc.c "А этот идиот говорит... «снимай трусики»."
    sarah.c "..."
    "Не думаю, что в следующем раунде она будет стараться."
    scene sarahhevent7i15 with dissolve
    "Следующий раунд проходит как обычно. Я отражаю её вялые атаки."
    "На этот раз Сара почти молчит и едва сопротивляется."
    "Она ёрзает на месте. Кажется, мыслями она уже не в игре."
    scene sarahhevent7i16 with dissolve
    "На экране появляется надпись «Победа»."
    mc.c "Вот так, Сара."
    mc.c "Не расстраивайся. Ты просто попалась на классическую уловку."
    sarah.c "Тебе повезло."
    mc.c "Тебе ещё сто лет расти, чтобы меня победить~"
    sarah.c "Да ладно, придурок."
    sarah.c "Раз уж правила {i}ты{/i} придумывал на ходу, что теперь должен делать проигравший?"
    "Она ёрзает на месте. Мы оба голые. Я возбуждён. Она, кажется, вот-вот начнёт пускать слюни."
    mc.c "Ну..."
    sarah.c "..."
    mc.c "..."
    call playMusic(sexyTheme) from _call_playMusic_247
    image sarahFloorReverseCowgirl1 = Movie(play="images/characters/sarah/hscenes/floorReverseCowgirl/part1.webm")
    scene sarahFloorReverseCowgirl1 with fade
    pause
    sarah.c "Ха-а~ Ха-а~ А-а~"
    "Мы оба знали, что это случится. Сара перекидывает ногу через мои бёдра и садится на мой член."
    "Она резко опускается на меня, а я хватаю её за ягодицы и двигаю вверх-вниз."
    sarah.c "Чёрт~ Чёрт~"
    mc.c "Это награда или наказание?"
    sarah.c "М-м~ Заткнись, член~ М-м~"
    sarah.c "Чёрт, чёрт~ Твой дурацкий~ М-м~ Член~"
    "Она впивается когтями в мои бёдра и откидывает зад назад как никогда прежде."
    "Её раздражение перерастает в неконтролируемую страсть. Я никогда не видел её такой. Она по-настоящему завелась."
    "Я слегка шлёпаю её по попке, которая покачивается передо мной; её киска пульсирует и сжимает мой член."
    image sarahFloorReverseCowgirl2 = Movie(play="images/characters/sarah/hscenes/floorReverseCowgirl/part2.webm")
    scene sarahFloorReverseCowgirl2 with fade
    pause
    sarah.c "Чёрт~ Это не... М-м~ Для тебя~ А-а~"
    sarah.c "Ты меня дразнишь... Чёрт~ Придурок~"
    "Её киска раскалена и насквозь промокла. Она больше не могла сдерживаться."
    "Она поворачивается и впивается ногтями мне в плечо. Раздражение на её лице сменяется чистой страстью и желанием."
    mc.c "Если ты так переживаешь из-за проигрыша, я готов обыгрывать тебя каждый день."
    sarah.c "Это просто~ А-а-а~ Чёрт..."
    "Влажные шлепки разносятся по комнате вместе с громкими стонами Сары."
    "Её милая упругая попка бьётся о мои бёдра, когда она резко опускается на меня и цепляется руками."
    sarah.c "Н-ну~ А-а~ Я кончу первой! Да?!"
    mc.c "Ох, чёрт, спорим. Посмотрим."
    sarah.c "Спорим... М-м~ Ты уже почти... А-а~"
    image sarahFloorReverseCowgirl3 = Movie(play="images/characters/sarah/hscenes/floorReverseCowgirl/part3.webm")
    scene sarahFloorReverseCowgirl3 with fade
    pause
    sarah.c "О-о-о~! А-а~! А-а~!"
    "Я принимаю вызов и обхватываю её тело руками."
    "Я упираюсь ногами и начинаю мощно двигаться ей навстречу, не оставляя ей возможности сопротивляться."
    sarah.c "Чёрт, чёрт, чёрт~~ А-а-а~"
    "Я глубоко и сильно вхожу в её киску, мои яйца шлёпают по влажной шерсти у входа."
    "Я тянусь и сжимаю подпрыгивающую грудь. Она полностью в моей власти и дрожит от наслаждения."
    mc.c "Хр-р~ Уже кончаешь?"
    sarah.c "Н-нет~ А-а~ Это ты~! М-м~"
    "Слышны только громкие шлепки и стоны, а диван за моей спиной скрипит от толчков."
    "Я чувствую, как она содрогается вокруг моего члена. Она уже близко..."
    sarah.c "Ох, чёрт~"
    "Уже почти... Не могу сдержаться..."
    scene sarahfloorreversecowgirlfinish1 with fadewhite
    pause
    sarah.c "А-а-а-а-а-а~!"
    mc.c "Ххг!"
    "Когти Сары впиваются в меня, когда мы оба содрогаемся и вместе достигаем пика."
    "Её внутренние мышцы сжимаются вокруг моего члена, выдавливая из меня всё до последней капли, пока я изливаю в неё огромное количество спермы."
    "Она покачивается на месте, выжимая из меня последние капли, и мы начинаем падать друг на друга."
    scene sarahfloorreversecowgirlfinish2 with fade
    pause
    sarah.c "Ха-а~ Чёрт~"
    "Сара скатывается с моих колен и бесформенной кучей падает на пол."
    "Я едва могу сидеть, прислонившись к дивану. Я вымотан, голова кружится."
    "Мы оба тяжело дышим, ошеломлённые наслаждением."
    "Постепенно приходя в себя на полу, Сара опускает взгляд и показывает, как из неё вытекают следы моей работы."
    sarah.c "Ха-а~ Ха-а~ Ха-а~"
    sarah.c "Я... Ха-а~ Побе..."
    mc.c "Ни за что... Ха-а..."
    "Не знаю, кто победил, но мы оба совершенно измучены. Это было невероятно."
    mc.c "Слишком близко... Будем играть решающий раунд?"
    sarah.c "...Заткнись."
    sarah.c "Чёрт~ Твой член..."
    scene black with fade
    "Наконец мы немного остываем и приводим себя в порядок."
    "Сара всё ещё немного злится, что проиграла. Может, ещё сыграем."

    return
