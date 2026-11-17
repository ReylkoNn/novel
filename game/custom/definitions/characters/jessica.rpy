init offset = 3
default jessica = Person(Character(name='Jessica', who_color='#999016', image = 'jessica'), 'Jessica', '', 'jessica', 'female', 20)

label initialiseCharacter_jessica:
    python:
        jessica.currentLocation = location_away
        location_away.occupants.extend([jessica])
        jessica.availableEvents = [jessicaFirstMeetingEvent]
        jessica.blockedLocations = [location_bar]
    return

label updateCharacterStatics_jessica:
    python:
        # Personal attributes
        jessica.species = 'Leopard'
        jessica.birthday = 1
        jessica.job = 'Student'
        jessica.giftLoves = [item_goldRing, item_dress]
        jessica.giftLikes = [item_perfume, item_flowers]
        jessica.giftHates = [item_videogame]

        # Skill attributes

        # Sexual attributes
        jessica.virgin = False

        # Personal effects

        # Event attributes
        jessica.events = [jessicaFirstMeetingEvent, jessicaLikeEvent1, jessicaLikeEvent2, jessicaLikeEvent3, jessicaHEvent1, jessicaHEvent2, jessicaHEvent3, jessicaHEvent4, jessicaHEvent5, jessicaHEvent6, jessicaVacation, jessicaLikeEvent4, jessicaHEvent7, jessicaLikeEvent5]
        jessica.specialEvents = [zoeJessicaDuoStoryEvent1, graceJessicaDuoStoryEvent1, zoeJessicaHEvent1, graceJessicaDuoHEvent1]
        jessica.selfieOptions = ['beach1', 'changingroom1', 'changingroom2', 'bedroom1', 'homebedroom1']
        jessica.wakeUpOptions = ['handjob']
        jessica.dateChats = ['Background', 'Hobbies']
        jessica.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = jessica.events[-1]
        jessica.maxLike = lastStoryEvent.requiredLike
        jessica.maxLove = lastStoryEvent.requiredLove

        # World attributes
        jessica.preferredMondaySchedule = [location_college, location_town, location_diner, location_town]
        jessica.preferredTuesdaySchedule = [location_college, location_beach, location_cafe, location_away]
        jessica.preferredWednesdaySchedule = [location_college, location_college, location_beach, location_town]
        jessica.preferredThursdaySchedule = [location_town, location_college, location_college, location_away]
        jessica.preferredFridaySchedule = [location_cafe, location_shop, location_bar, location_bar]
        jessica.preferredSaturdaySchedule = [location_park, location_beach, location_bar, location_bar]
        jessica.preferredSundaySchedule = [location_park, location_cafe, location_diner, location_away]

        jessica.preferredMovedInMondaySchedule = [location_home, location_college, location_home, location_home]
        jessica.preferredMovedInTuesdaySchedule = [location_home, location_college, location_home, location_home]
        jessica.preferredMovedInWednesdaySchedule = [location_home, location_college, location_beach, location_home]
        jessica.preferredMovedInThursdaySchedule = [location_home, location_shop, location_college, location_home]
        jessica.preferredMovedInFridaySchedule = [location_home, location_home, location_home, location_home]
        jessica.preferredMovedInSaturdaySchedule = [location_home, location_beach, location_town, location_home]
        jessica.preferredMovedInSundaySchedule = [location_home, location_town, location_home, location_home]
    return

# Sprites
screen jessicaClickable(xcenter):
    $ spriteload = jessica.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = jessica)
        at characterSpriteHover

# Character methods
label jessicaEvaluateAvailableInteractions:
    python:
        if jessica.like >= 6 and jessicaLikeEvent1.unlocked:
            jessica.availableActions = list(set(jessica.availableActions + ['Spend time']))
        if jessica.like >= 20 and jessicaHEvent2.unlocked:
            jessica.availableActions = list(set(jessica.availableActions + ['Invite over']))

        if jessica.isDateable and jessica.love >= 1:
            jessica.availableActions = list(set(jessica.availableActions + ['Date']))
        if jessica.love >= 1 and jessicaLikeEvent3.unlocked:
            jessica.availableAffections.extend(['Pat', 'Chin Scratch'])
        if jessica.love >= 1 and jessicaLikeEvent2.unlocked:
            jessica.availableActions = list(set(jessica.availableActions + ['Affection']))
            jessica.availableAffections.extend(['Hug'])
        if jessica.love >= 1 and jessicaLikeEvent3.unlocked:
            jessica.availableAffections.extend(['Kiss'])
        if jessicaHEvent3.unlocked:
            jessica.availableAffections.extend(['Caress Butt'])
        if jessicaHEvent5.unlocked:
            jessica.availableAffections.extend(['Boob Grab'])
        if jessicaHEvent7.unlocked:
            jessica.availableActions.extend([{'homebathroom': ['Tailjob']}])
        if jessica.movedIn:
            jessica.availableCommandsPrivate.extend(['Show Panties'])
            jessica.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label jessicaChat:
    show jessica smile talk
    return

label jessicaChat_beach:
    show jessica joy
    jessica.c "А-а~ Вот теперь хорошо!"
    return

label jessicaChat_park:
    show jessica smile talk
    jessica.c "Эй~ Куда-то собралась?"
    return

label jessicaChat_shop:
    show jessica mad
    jessica.c "Боже, здесь никогда ничего интересного нет."
    return

label jessicaChat_diner:
    show jessica bashful talk
    jessica.c "Папа сказал, что мне надо поменьше тратить..."
    show jessica neutral talk
    jessica.c "Место... Ну, сойдёт."
    return

label jessicaChat_cafe:
    show jessica smile talk 2
    jessica.c "Обязательно попробуй какао-латте, он такой вкусный!"
    show jessica joy
    jessica.c "На, попробуй, попробуй!"
    return

label jessicaChat_town:
    show jessica smile talk
    jessica.c "Мне было ужасно скучно, вот и пошла купить пару нарядов."
    show jessica surprise
    jessica.c "А? Ты что, так не делаешь?"
    return

label jessicaChat_bar:
    show jessica smile talk
    jessica.c "А ты готовишь эти... фруктовые коктейли?"
    return

label jessicaChat_aquarium:
    show jessica smile talk 2
    jessica.c "Ой, идеальное место для фото!"
    show jessica joy
    jessica.c "Сфоткай меня, пожалуйста!"
    return

label jessicaChat_theater:
    show jessica smile talk
    jessica.c "Привет, [mc.name]! Вышел новый фильм!"
    show jessica joy
    jessica.c "Как я могла пропустить? Эта актриса такая милая, правда?"
    return

label jessicaChat_homebedroom:
    if(timeOfDay == 'Morning'):
        show jessica smile talk 2
        jessica.c "М-м~ Доброе утро... Ты сегодня работаешь или собираешься куда-нибудь?"
    elif(timeOfDay == 'Afternoon'):
        show jessica thinking
        jessica.c "Занятия? Э-э, не знаю. Кажется, сегодня нет?"
    elif(timeOfDay == 'Evening'):
        show jessica joy
        jessica.c "Смотри, какая фотка~ Нам надо сделать пару таких со мной!"
    elif(timeOfDay == 'Night'):
        show jessica tease talk
        jessica.c "Иди в кровать, {i}любимый~{/i} Хе-хе~ Я тебя согрею~"
    return

label jessicaChat_homelounge:
    if(timeOfDay == 'Morning'):
        show jessica joy
        jessica.c "[mc.name], [mc.name]~ Ну же, пойдём сегодня гулять!"
    elif(timeOfDay == 'Afternoon'):
        show jessica smile talk 2
        jessica.c "Зацени инсту этой девушки. Милая, да? Можешь говорить честно~"
    elif(timeOfDay == 'Evening'):
        show jessica tease talk
        jessica.c "Эй, давай вместе посмотрим фильм! Но выбирать буду я~"
    elif(timeOfDay == 'Night'):
        show jessica smile talk 2
        jessica.c "Я совсем вымоталась, пойдём спать? Что я сегодня делала? Э-э..."
    return

label jessicaChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show jessica smile talk 2
        jessica.c "Доброе утро~! Хе-хе, я встала раньше тебя! Иду за покупками, пойдёшь со мной?"
    elif(timeOfDay == 'Afternoon'):
        show jessica thinking
        jessica.c "Эх, ничего не хочется. Наверное, просто закажу еду."
    elif(timeOfDay == 'Evening'):
        show jessica tease talk
        jessica.c "Ого, вкусно пахнет~ Дай попробовать!"
    elif(timeOfDay == 'Night'):
        show jessica surprise
        jessica.c "А? Уже так поздно? Сейчас приду, только ещё пару видео посмотрю..."
    return

# Date topics
label jessicaChat_background:
    show jessica thinking
    jessica.c "Тааак~ До дома ехать часа четыре?"
    show jessica smile talk
    jessica.c "Только я, мама и папа!"
    jessica.c "Мы живём на окраине города. Он меньше этого, но папе, кажется, принадлежат там какие-то предприятия."
    show jessica smile
    mc.c "Предприятия?"
    show jessica smile talk 2
    jessica.c "Ага! Не знаю, чем они занимаются, хе-хе. Звучит ужасно скучно."
    show jessica thinking
    jessica.c "Он всё время говорит по телефону и всякое такое."
    mc.c "Значит, ваша семья довольно обеспеченная?"
    show jessica neutral talk
    jessica.c "Ничего особенного. В школе большинство девочек были примерно такими же."
    show jessica neutral
    mc.c "...Это была какая-то частная школа?"
    show jessica thinking
    jessica.c "Кажется... Вроде там учились какие-то знаменитости..."
    show jessica joy
    jessica.c "А ты ходил в такую?"
    mc.c "...Не совсем."
    mc.c "И как ты сюда попала?"
    show jessica smile talk 2
    jessica.c "Родители хотели, чтобы я съехала и поехала учиться в другой город."
    show jessica neutral talk
    jessica.c "Сказали, что мне надо «пожить в реальном мире». Что это вообще значит?"
    show jessica joy
    jessica.c "Ой! Сначала я взяла год перерыва, конечно! Путешествовала по всему миру!"
    mc.c "То есть, отправилась искать себя? Познавать природу, исследовать густые леса и далёкие края?"
    show jessica neutral talk
    jessica.c "Э-э, нет?"
    show jessica smile talk 2
    jessica.c "Посмотрела самые крутые города, центры моды и всё такое, жила в хороших отелях!"
    show jessica smile talk
    jessica.c "А когда закончила, выбрала этот город!"
    show jessica smile
    mc.c "Почему именно его?"
    show jessica joy
    jessica.c "Он у моря! Я никогда раньше не жила у моря!"
    "..."
    "Ну ладно..."
    return

label jessicaChat_hobbies:
    show jessica smile talk 2
    jessica.c "Наверное, мода! Обожаю покупать одежду и аксессуары!"
    jessica.c "Я же модель, поэтому в основном этим и занимаюсь!"
    show jessica smile talk
    jessica.c "Ну, соцсети, видео и всё такое."
    show jessica thinking
    jessica.c "Ещё фотография, наверное."
    mc.c "И все фотографии — тебя, да?"
    show jessica mad talk
    jessica.c "Не всегда!"
    show jessica bashful talk
    jessica.c "Иногда... На заднем плане что-нибудь есть..."
    show jessica smile talk 2
    jessica.c "Но теперь ты будешь фотографировать меня. У тебя получается {b}гораздо{/b} лучше."
    show jessica smile
    mc.c "Значит, я жестоко отнял у тебя фотографию. Чем ещё занимаешься?"
    show jessica thinking
    jessica.c "Хм-м..."
    show jessica joy
    jessica.c "Путешествия? Есть классные города, куда я хочу съездить!"
    jessica.c "В мире столько мест для шопинга!"
    return

#

label jessicaInteractionBathroom:
    jessica.c "О-о~ [mc.name]~?"
    jessica.c "Не хочешь присоединиться?"
    return

label jessicaSpendTime(onDate):
    if(onDate):
        scene expression 'jessica[mc.currentLocation.apiName]date'
    else:
        scene expression 'jessica[mc.currentLocation.apiName]'
    with fade
    return

label jessicaReceiveGift(item, likeChange, loveChange):
    show jessica neutral talk
    jessica.c "Ой! Это мне?"
    if(loveChange > 0):
        show jessica joy
        jessica.c "Боже мой!"
        jessica.c "Класс! Спасибо, [mc.name]!"
        if(jessicaVacation.unlocked):
            jessica.c "Люблю тебя~!"
    elif(likeChange > 1):
        show jessica smile talk
        jessica.c "Ой, вообще-то довольно мило! Неплохо!"
    elif(likeChange < 1):
        show jessica mad talk
        jessica.c "А? И что мне с этим делать?"
    else:
        show jessica smile talk
        jessica.c "Как мило! Спасибо!"
        if(jessicaVacation.unlocked):
            jessica.c "Люблю тебя~!"
    return

label jessicaReceiveDateInvitation:
    show jessica neutral talk
    jessica.c "О-о~ Да, ладно! Чем хочешь заняться?"
    show jessica neutral
    call dateInvitationSelector(jessica) from _call_dateInvitationSelector_3
    show jessica neutral talk
    jessica.c "[proposedDateDayOfWeek], [proposedDateTime], в заведении «[proposedDateLocation.name]»? Класс-класс!"

    python:
        scheduledDate = Date(jessica, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        jessica.scheduledDates.append(scheduledDate)
    return

label jessicaStartDate:
    if(mc.currentLocation == location_home):
        show jessica tease with dissolve
        jessica.c "Эй! Спасибо, что позвал."
    else:
        show jessica smile talk with dissolve
        jessica.c "Привет, [mc.name]!"
    return

label jessicaDateInteraction:
    show jessica smile with dissolve
    show screen dateUi(jessica) with dissolve
    call screen dateInteractionScreen(jessica, mc.currentLocation)

label jessicaChatDate:
    show jessica smile talk 2
    jessica.c "Это так мило с твоей стороны, знаешь?"
    return

label jessicaChatDate_beach:
    show jessica tease talk
    jessica.c "А-а, сейчас я больше нигде не хочу быть."
    show jessica bashful
    jessica.c "Вот бы мне не надо было на занятия..."
    return

label jessicaChatDate_park:
    show jessica smile talk 2
    jessica.c "Ага-ага, здесь такая приятная атмосфера."
    show jessica tease talk
    jessica.c "Давай сделаем селфи! Ну же, подвинься!"
    return

label jessicaChatDate_diner:
    show jessica smile talk
    jessica.c "А здесь, вообще-то, довольно неплохо."
    show jessica tease talk
    jessica.c "Дай попробовать твоё~"
    return

label jessicaChatDate_cafe:
    show jessica joy
    jessica.c "Смотри, смотри! Тут всё такое милое!"
    show jessica neutral talk
    jessica.c "А? Еда? Ну, на вкус тоже вроде нормально..."
    return

label jessicaChatDate_bar:
    show jessica thinking
    jessica.c "Кажется, мне начинает нравиться ваш «деревенский» стиль."
    show jessica surprise
    jessica.c "Только не говори, что я отстала от какого-то нового тренда?"
    return

label jessicaChatDate_aquarium:
    show jessica joy
    jessica.c "Быстрее, сфотографируй меня здесь!"
    show jessica smile talk 2
    jessica.c "О-о~ Хорошая фотка! Ты всё-таки на что-то годишься."
    return

label jessicaChatDate_theater:
    show jessica joy
    jessica.c "Ой, давай посмотрим вот это, пожалуйста~"
    show jessica tease talk
    jessica.c "Я разрешу тебе прижаться ко мне~"
    return

label jessicaDatePayFor:
    show jessica neutral talk
    jessica.c "Если хочешь, иногда могу платить сама."
    show jessica thinking
    jessica.c "Это же просто деньги..."
    return

label jessicaEndDate:
    if(dateScore < 40):
        show jessica mad talk
        jessica.c "Э-э... Ладно... Пока."
    else:
        if(jessica.movedIn):
            show jessica joy
            jessica.c "Сегодня было так здорово!"
            show jessica tease talk
            jessica.c "Надо каждый день гулять! Всегда-всегда!"
        else:
            show jessica smile talk 2
            jessica.c "Мне очень понравилось, [mc.name]!"
            if(jessicaVacation.unlocked):
                jessica.c "Люблю тебя!"
    return

label jessicaContinueDateAtHome:
    scene expression 'jessica[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(jessicaHEvent2.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label jessicaHomeStartSex:
    show jessica tease talk
    jessica.c "О-о~ Ты {i}правда{/i} хочешь прямо сейчас~?"
    jessica.c "Хе-хе~ Ладно!"
    show jessica tease
    return

label jessicaHomeSexJoinIn(character):
    show jessica joy at twoPersonLeft with dissolve
    jessica.c "Ой! Звучит весело! Возьмите меня с собой!"
    show jessica joy
    return

label jessicaEndDateAtHome:
    jessica.c "У тебя дома довольно мило. До встречи, [mc.name]!"
    if(jessicaVacation.unlocked):
        jessica.c "Люблю тебя!"
    return

image jessica pat animated = Movie(play="images/characters/jessica/affections/jessicaPat.webm", side_mask=True, loop=True)
label jessicaReceivePat:
    hide jessica with dissolve
    show jessica pat animated with dissolve
    pause
    jessica.c "О-о-о~"
    jessica.c "У меня такие классные волосы, правда?"
    return

image jessica chinscratch animated = Movie(play="images/characters/jessica/affections/jessicaChinscratch.webm", side_mask=True, loop=True)
label jessicaReceiveChinScratch:
    hide jessica with dissolve
    show jessica chinscratch animated with dissolve
    pause
    jessica.c "Хм-м~"
    jessica.c "Кто сказал тебе, что это слабое место леопарда?"
    return

image jessica caressbutt animated = Movie(play="images/characters/jessica/affections/jessicaCaressButt.webm", side_mask=True, loop=True)
label jessicaReceiveCaressButt:
    hide jessica with dissolve
    show jessica caressbutt animated with dissolve
    pause
    jessica.c "Хе-хе~ Милая попка, правда?"
    jessica.c "Я знаю, как тебе нравится её лапать~"
    return

image jessica boobgrab animated = Movie(play="images/characters/jessica/affections/jessicaBoobGrab.webm", side_mask=True, loop=True)
label jessicaReceiveBoobGrab:
    hide jessica with dissolve
    show jessica boobgrab animated with dissolve
    pause
    jessica.c "Хе-хе~ Знаю, как ты их обожаешь. Давай~"
    jessica.c "Они все твои~"
    return

image jessica snuggle animated = Movie(play="images/characters/jessica/affections/jessicaSnuggle.webm", side_mask=True, loop=True)
label jessicaReceiveSnuggle:
    "Я отдыхаю на диване, когда Джессика ловит мой взгляд. Я хлопаю по месту рядом."
    show jessica tease talk
    jessica.c "Я знаю этот взгляд~"
    hide jessica with dissolve
    show jessica snuggle animated with dissolve
    pause
    "Вместо этого она садится ко мне на колени и крепко обнимает."
    jessica.c "Хе-хе~ Просто попроси меня, любимый~!"
    pause
    return

label jessicaReceiveHug:
    hide jessica with dissolve
    show jessica hug with dissolve
    pause
    jessica.c "Хе-хе, ты такой милый~"
    return

label jessicaReceiveKiss:
    hide jessica with dissolve
    show jessica kiss with dissolve
    jessica.c "*Чмок*"
    pause
    jessica.c "Ещё~"
    return

label jessicaInitiatePat:
    show jessica tease with dissolve
    jessica.c "[mc.name]! Погладь меня!"
    hide jessica with dissolve
    show jessica pat animated with dissolve
    pause
    jessica.c "Хи-хи~"
    if(jessicaVacation.unlocked):
        jessica.c "Люблю тебя~"
    return

label jessicaInitiateChinScratch:
    show jessica tease with dissolve
    "[jessica.name] самодовольно улыбается и слегка приподнимает подбородок."
    hide jessica with dissolve
    show jessica chinscratch animated with dissolve
    pause
    jessica.c "М-м-м~ Оставлю на тебе свой запах."
    return

label jessicaInitiateHug:
    show jessica tease talk with dissolve
    jessica.c "Иди сюда, [mc.name]."
    hide jessica with dissolve
    show jessica hug with dissolve
    pause
    jessica.c "Обними меня крепче!"
    return

label jessicaInitiateKiss:
    show jessica smile with dissolve
    jessica.c "[mc.name]!"
    hide jessica with dissolve
    show jessica kiss with dissolve
    jessica.c "*Чмок*"
    pause
    hide jessica with dissolve
    show jessica smile with dissolve
    if(jessicaVacation.unlocked):
        jessica.c "Хе-хе~ Я тебя люблю~"
    return

label jessicaInitiateSnuggle:
    show jessica joy
    "Я сижу на диване, и Джессика замечает меня и подпрыгивая подбегает."
    jessica.c "Любимый~!"
    hide jessica with dissolve
    show jessica snuggle animated with dissolve
    pause
    "Она запрыгивает на диван, садится верхом на меня и прижимает мою голову к груди."
    jessica.c "Не удержалась! Нам нужно больше обнимашек~!"
    pause
    return

label jessicaInitiateHomeSex:
    show jessica tease talk
    jessica.c "[mc.name]~ Хочешь немного повеселиться~?"
    jessica.c "Ну же, {i}любимый~{/i}. Пожалуйста~?"
    show jessica tease
    return

label jessicaInitiateHomeSexDeny:
    show jessica neutral talk
    jessica.c "Правда? Скучно..."
    return

label jessicaSeesAffection(affection):
    show jessica joy with dissolve
    jessica.c "Ой-ой~ Я тоже!"
    "Джессика вмешивается в наше занятие. Не думаю, что она будет против..."
    call expression 'jessicaReceive' + affection from _call_expression_40
    hide jessica with dissolve
    return

label jessicaInviteOver:
    show jessica smile talk
    jessica.c "Ладно! Класс!"
    return

label jessicaInitiateInviteOver:
    show jessica smile talk 2
    jessica.c "Эй-эй, можно я вернусь к тебе домой? Ну пожалуйста~"
    show jessica smile
    menu:
        'Yes':
            show jessica joy
            jessica.c "Ура~!"
            return True
        'No':
            show jessica neutral talk
            jessica.c "О? Ладно, тогда в другой раз."
    return False

label jessicaInviteGoHomeTogether:
    show jessica smile talk 2
    jessica.c "Хорошо, пошли!"
    show jessica tease talk
    jessica.c "Чем займёмся дома, а?"
    return

label jessicaInitiateGoHomeTogether:
    show jessica smile talk 2
    jessica.c "[mc.name], мне скучно~ Пойдём домой."
    show jessica smile
    menu:
        'Yes':
            show jessica joy
            jessica.c "Ура~! Чем займёмся, когда вернёмся?"
            return True
        'No':
            show jessica neutral talk
            jessica.c "Ладно. Только возвращайся домой поскорее, хорошо?"
    return False

label jessicaShowPanties(pantiesIndex = 1):
    show jessica tease talk
    jessica.c "Хорошо! Конечно!"
    $ renpy.show(jessica.apiName + ' panties ' + str(pantiesIndex), tag=jessica.apiName)
    with dissolve
    if(pantiesIndex == 1):
        jessica.c "Самое лучшее! Леопардовый принт! Знаю, как он тебе нравится~"
    elif(pantiesIndex == 2):
        jessica.c "Миленькие! Правда, совершенно не сочетаются. Хорошо, что их видишь только ты."
    elif(pantiesIndex == 3):
        jessica.c "Совсем прозрачные~ Хе-хе~"
    return

label jessicaSendDateText(proposedDate):
    python:
        jessica.textChain.append(Message(mc, jessica, '[mc.name!l] lets do something tomorrow', Null, day, timeOfDay))
        jessica.textChain.append(Message(mc, jessica, proposedLocation.name.lower() + '? ' + proposedDateTime.lower() + ' ?', Null, day, timeOfDay, proposedDate))
    return

label jessicaGetSelfieOptions:
    $ jessicaSelfieOptions = []
    if(jessicaLikeEvent2.unlocked):
        $ jessicaSelfieOptions.extend(['beach1'])
    if(jessicaLikeEvent3.unlocked):
        $ jessicaSelfieOptions.extend(['changingroom1'])
    if(jessicaHEvent1.unlocked):
        $ jessicaSelfieOptions.extend(['changingroom2'])
    if(jessicaHEvent3.unlocked):
        $ jessicaSelfieOptions.extend(['bedroom1'])
    if(jessica.movedIn):
        $ jessicaSelfieOptions.extend(['homebedroom1'])
    return jessicaSelfieOptions

label jessicaSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'beach1':
                potentialResponses.append({'text': "Отлично выглядишь!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Жаль, что меня там нет.", 'statChange': 'love', 'statChangeAmount': 1})
                jessica.textChain.append(Message(mc, jessica, 'join me!.', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'changingroom1':
                potentialResponses.append({'text': "Очень элегантно.", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Супер-мило.", 'statChange': 'love', 'statChangeAmount': 1})
                jessica.textChain.append(Message(mc, jessica, "В этом я выгляжу такой взрослой, да?", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'changingroom2':
                potentialResponses.append({'text': "Конечно! Тебе идёт.", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Леопардовый принт ничто не переплюнет.", 'statChange': 'love', 'statChangeAmount': 1})
                jessica.textChain.append(Message(mc, jessica, "Мне это купить?", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom1':
                potentialResponses.append({'text': "Вау!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Что нужно сделать, чтобы получить ещё?", 'statChange': 'love', 'statChangeAmount': 1})
                jessica.textChain.append(Message(mc, jessica, "Думаю, ты заслужил награду.", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homebedroom1':
                potentialResponses.append({'text': "<3 <3 <3 <3 <3", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Когда будем их разнашивать? ;)", 'statChange': 'love', 'statChangeAmount': 1})
                jessica.textChain.append(Message(mc, jessica, "Нравится? <3", selfieName, day, timeOfDay, responses = potentialResponses))
    return

label jessicaSexSelect:
    hide screen mainUi
    scene black with fade
    image jessica sex waiting = Movie(play="images/characters/jessica/hscenes/sexWaiting.webm")
    show jessica sex waiting with fade

    call screen jessicaSexSelectScreen
    if(jessicaHEvent4.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(jessica.movedIn):
            menu jessicaSleepTogether:
                "Переспать с Джессикой?"
                'Yes':
                    jessica.c "Я вымоталась. Может, обнимемся?"
                    jessica.c "Ура~ Люблю тебя."
                    call characterSleepover(jessica) from _call_characterSleepover_6
                'No':
                    pass
        else:
            menu jessicaStayTheNight:
                "Предложить [jessica.name] остаться на ночь?"
                'Yes':
                    $ jessica.addLove(1)
                    jessica.c "...Да, давай!"
                    call characterSleepover(jessica) from _call_characterSleepover_7
                'No':
                    jessica.c "Скоро позвони мне, ладно?"
                    if(jessicaVacation.unlocked):
                        jessica.c "Люблю тебя!"

    call endScene(character = jessica, targetLocation = location_home) from _call_endScene_11

screen jessicaSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(jessicaHEvent2.unlocked or persistent.debugMode):
                textbutton 'Blowjob' keysym str(1):
                    action [Jump('jessicaBlowjob')]
            else:
                textbutton 'Locked'
            if(jessicaHEvent3.unlocked or persistent.debugMode):
                textbutton 'Seated Cowgirl' keysym str(2):
                    action [Jump('jessicaSeatedCowgirl')]
            else:
                textbutton 'Locked'
            if(jessicaHEvent4.unlocked or persistent.debugMode):
                textbutton 'Makeout' keysym str(3):
                    action [Jump('jessicaMakeout')]
            else:
                textbutton 'Locked'
            if(jessicaHEvent4.unlocked or persistent.debugMode):
                textbutton 'Missionary' keysym str(4):
                    action [Jump('jessicaMissionary')]
            else:
                textbutton 'Locked'
            if(jessicaHEvent4.unlocked or persistent.debugMode):
                textbutton 'Spooning' keysym str(5):
                    action [Jump('jessicaSpooning')]
            else:
                textbutton 'Locked'
            if(jessicaHEvent5.unlocked or persistent.debugMode):
                textbutton 'Footjob' keysym str(6):
                    action [Jump('jessicaFootjob')]
            else:
                textbutton 'Locked'
            if(jessicaVacation.unlocked or persistent.debugMode):
                textbutton 'Cowgirl' keysym str(7):
                    action [Jump('jessicaCowgirl')]
            else:
                textbutton 'Locked'
            if(jessicaVacation.unlocked or persistent.debugMode):
                textbutton 'Leglock Missionary' keysym str(8):
                    action [Jump('jessicaLeglockMissionary')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(9):
                action [Hide('jessicaSexSelectScreen'), Return()]

label jessicaSleepover:
    scene jessicasleepover with fade
    pause
    return

label jessicaMorningBedInteraction:
    scene jessicahomemorning with fade
    pause
    if(jessica.movedIn):
        jessica.c "М-м~ Доброе утро, [mc.name]~"
        jessica.c "Я так хорошо провела ночь~"
        jessica.c "Встаёшь? Давай сегодня куда-нибудь сходим~"
    else:
        jessica.c "*Зевает* Доброе утро~"
        jessica.c "Пока не хочу вставать..."
        jessica.c "Обнимемся?"
    return

label jessicaMorningBedInteractionSex(event):
    if(event == 'handjob'):
        image jessica morning handjob 1 = Movie(play="images/characters/jessica/hscenes/morning/handjob1.webm")
        show jessica morning handjob 1 with fade
        pause
        mc.c "Э-э... Привет, Джесс."
        jessica.c "Ну же~ Просыпайся уже."
        mc.c "Ты так меня будишь?"
        jessica.c "Сработало же? Мне скучно, давай куда-нибудь сходим..."
        mc.c "Чёрт, подожди..."
        image jessica morning handjob 2 = Image("images/characters/jessica/hscenes/morning/handjob2.webp")
        show jessica morning handjob 2 with fadewhite
        pause
        jessica.c "Ха-ха~ Так тепло~"
        image jessica morning handjob 3 = Image("images/characters/jessica/hscenes/morning/handjob3.webp")
        show jessica morning handjob 3 with fade
        pause
        jessica.c "Ну что, уже проснулся?"
    return

# Sex scenes
label jessicaBlowjob:
    image jessica blowjob start = Image("images/characters/jessica/hscenes/blowjob/start.webp")
    scene jessica blowjob start with fade
    pause
    image jessica blowjob part 1 = Movie(play="images/characters/jessica/hscenes/blowjob/part1.webm")
    show jessica blowjob part 1 with fade
    pause
    image jessica blowjob part 2 = Movie(play="images/characters/jessica/hscenes/blowjob/part2.webm")
    show jessica blowjob part 2 with fade
    pause
    image jessica blowjob part 3 = Movie(play="images/characters/jessica/hscenes/blowjob/part3.webm")
    show jessica blowjob part 3 with fade
    pause
    image jessica blowjob part 4 = Movie(play="images/characters/jessica/hscenes/blowjob/part4.webm")
    show jessica blowjob part 4 with fade
    pause
    image jessica blowjob part 5 = Movie(play="images/characters/jessica/hscenes/blowjob/part5.webm")
    show jessica blowjob part 5 with fade
    pause
    image jessica blowjob end 1 = Image("images/characters/jessica/hscenes/blowjob/end1.webp")
    scene jessica blowjob end 1 with fadewhite
    pause
    image jessica blowjob end 2= Image("images/characters/jessica/hscenes/blowjob/end2.webp")
    scene jessica blowjob end 2 with fade
    pause
    jump jessicaSexSelect

label jessicaSeatedCowgirl:
    image jessica seated cowgirl start = Image("images/characters/jessica/hscenes/seatedCowgirl/start1.webp")
    scene jessica seated cowgirl start with fade
    pause
    image jessica seated cowgirl start 2 = Image("images/characters/jessica/hscenes/seatedCowgirl/start2.webp")
    scene jessica seated cowgirl start 2 with fade
    pause
    image jessica seated cowgirl part 1 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part1.webm")
    show jessica seated cowgirl part 1 with fade
    pause
    image jessica seated cowgirl part 2 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part2.webm")
    show jessica seated cowgirl part 2 with fade
    pause
    image jessica seated cowgirl part 3 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part3.webm")
    show jessica seated cowgirl part 3 with fade
    pause
    image jessica seated cowgirl part 4 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part4.webm")
    show jessica seated cowgirl part 4 with fade
    pause
    image jessica seated cowgirl part 5 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part5.webm")
    show jessica seated cowgirl part 5 with fade
    pause
    image jessica seated cowgirl end 1 = Image("images/characters/jessica/hscenes/seatedCowgirl/end1.webp")
    scene jessica seated cowgirl end 1 with fadewhite
    pause
    image jessica seated cowgirl end 2 = Image("images/characters/jessica/hscenes/seatedCowgirl/end2.webp")
    scene jessica seated cowgirl end 2 with fade
    pause
    jump jessicaSexSelect

label jessicaMakeout:
    image jessica makeout part 1 = Movie(play="images/characters/jessica/hscenes/makeout/part1.webm")
    show jessica makeout part 1 with fade
    pause
    image jessica makeout part 2 = Movie(play="images/characters/jessica/hscenes/makeout/part2.webm")
    show jessica makeout part 2 with fade
    pause
    jump jessicaSexSelect

label jessicaMissionary:
    image jessica missionary start = Image("images/characters/jessica/hscenes/missionary/start.webp")
    show jessica missionary start with fade
    pause
    image jessica missionary part 1 = Movie(play="images/characters/jessica/hscenes/missionary/part1.webm")
    show jessica missionary part 1 with fade
    pause
    image jessica missionary part 2 = Movie(play="images/characters/jessica/hscenes/missionary/part2.webm")
    show jessica missionary part 2 with fade
    pause
    jump jessicaSexSelect

label jessicaSpooning:
    image jessica spooning part 1 = Movie(play="images/characters/jessica/hscenes/spooning/part1.webm")
    show jessica spooning part 1 with fade
    pause
    image jessica spooning part 2 = Movie(play="images/characters/jessica/hscenes/spooning/part2.webm")
    show jessica spooning part 2 with fade
    pause
    image jessica spooning end 1 = Image("images/characters/jessica/hscenes/spooning/end1.webp")
    show jessica spooning end 1 with fadewhite
    pause
    image jessica spooning end 2 = Image("images/characters/jessica/hscenes/spooning/end2.webp")
    show jessica spooning end 2 with fade
    pause
    jump jessicaSexSelect

label jessicaFootjob:
    scene jessicahevent5i2 with fade
    pause
    image jessica chair footjob 1 = Movie(play="images/characters/jessica/hscenes/chairFootjob/part1.webm")
    show jessica chair footjob 1 with fade
    pause
    image jessica chair footjob 2 = Movie(play="images/characters/jessica/hscenes/chairFootjob/part2.webm")
    show jessica chair footjob 2 with fade
    pause
    image jessica chair footjob 3 = Movie(play="images/characters/jessica/hscenes/chairFootjob/part3.webm")
    show jessica chair footjob 3 with fade
    pause
    scene jessicachairfootjobfinish1 with fadewhite
    pause
    scene jessicachairfootjobfinish2 with fade
    pause
    jump jessicaSexSelect

label jessicaCowgirl:
    image jessica cowgirl 1 = Movie(play="images/characters/jessica/hscenes/cowgirl/part1.webm")
    show jessica cowgirl 1 with fade
    pause
    image jessica cowgirl 2 = Movie(play="images/characters/jessica/hscenes/cowgirl/part2.webm")
    show jessica cowgirl 2 with fade
    pause
    scene jessicacowgirlfinish with fadewhite
    pause
    jump jessicaSexSelect

label jessicaLeglockMissionary:
    image jessica leglock missionary 1 = Movie(play="images/characters/jessica/hscenes/leglockmissionary/part1.webm")
    show jessica leglock missionary 1 with fade
    pause
    image jessica leglock missionary 2 = Movie(play="images/characters/jessica/hscenes/leglockmissionary/part2.webm")
    show jessica leglock missionary 2 with fade
    pause
    image jessica leglock missionary 3 = Movie(play="images/characters/jessica/hscenes/leglockmissionary/part3.webm")
    show jessica leglock missionary 3 with fade
    pause
    scene jessicaleglockmissionaryfinish1 with fadewhite
    pause
    scene jessicaleglockmissionaryfinish2 with fade
    pause
    jump jessicaSexSelect

label jessicahomebathroomTailjob:
    image jessica shower caressing = Movie(play="images/characters/jessica/hscenes/shower/caressing.webm")
    show jessica shower caressing with fade
    pause
    image jessica shower tailjob 1 = Movie(play="images/characters/jessica/hscenes/shower/tailjob/part1.webm")
    show jessica shower tailjob 1 with fade
    pause
    image jessica shower tailjob 2 = Movie(play="images/characters/jessica/hscenes/shower/tailjob/part2.webm")
    show jessica shower tailjob 2 with fade
    pause
    scene jessicashowertailjobfinish1 with fadewhite
    pause
    scene jessicashowertailjobfinish2 with fade
    pause
    return

# Events
default jessicaFirstMeetingEvent = Event('First meeting', 'jessicaFirstMeeting', [jessica], 0, 0, [], location_beach, ['Morning', 'Afternoon'], triggerDay = 4)
default jessicaLikeEvent1 = Event('Sure this is it?', 'jessicaLikeEvent1', [jessica], 5, 0, [jessicaFirstMeetingEvent], location_bar)
# Hug. Start dating
default jessicaLikeEvent2 = Event('Seafront studio', 'jessicaLikeEvent2', [jessica], 10, 0, [jessicaLikeEvent1], location_beach, ['Morning', 'Afternoon', 'Evening'])
# Park photoshoot. Pat and kiss
default jessicaLikeEvent3 = Event('Support', 'jessicaLikeEvent3', [jessica], 20, 5, [jessicaLikeEvent2], location_park, ['Morning', 'Afternoon'])
# Changing room handjob
default jessicaHEvent1 = Event('Changing room', 'jessicaHEvent1', [jessica], 30, 10, [jessicaLikeEvent3], location_town, ['Morning', 'Afternoon', 'Evening'])
# Home blowie
default jessicaHEvent2 = Event('Home studio', 'jessicaHEvent2', [jessica], 40, 15, [jessicaHEvent1], location_home, ['Morning', 'Afternoon', 'Evening'])
# Tipsy straddling couch cowgirl
default jessicaHEvent3 = Event('Make you jealous?', 'jessicaHEvent3', [jessica], 50, 20, [jessicaHEvent2], location_bar, ['Evening', 'Night'])
# Missionary/spooning makeout sleepover
default jessicaHEvent4 = Event('Family policy', 'jessicaHEvent4', [jessica], 60, 25, [jessicaHEvent3], location_diner, ['Evening', 'Night'])
# Bothering working footjob
default jessicaHEvent5 = Event('Special Content', 'jessicaHEvent5', [jessica], 70, 30, [jessicaHEvent4], location_home)
# Beach changing room standing sex
default jessicaHEvent6 = Event('Getting hit on', 'jessicaHEvent6', [jessica], 80, 35, [jessicaHEvent5], location_beach, ['Morning', 'Afternoon'])
# Visit her family home without them there
default jessicaVacation = Event('Manor Jess', 'jessicaVacation', [jessica], 90, 40, [jessicaHEvent6], Null, extraNotes = 'You have some spare time. See what Jessica\'s up to? Special option in interaction menu.', cost=150, requiredItems = [item_car], requiresInvite = True)
# Move in / invite
default jessicaLikeEvent4 = Event('Dropping hints', 'jessicaLikeEvent4', [jessica], 100, 45, [jessicaVacation], Null, extraNotes = 'Things are getting serious. Are we ready for the next step?\nSpecial option in interaction menu.', requiredItems = [item_car], requiresInvite = True)
# Shower blowjob
default jessicaHEvent7 = Event('Flick of the tail', 'jessicaHEvent7', [jessica], 110, 50, [jessicaLikeEvent4], location_home_bathroom, ['Morning', 'Afternoon'], mcInitiated = True)
# Kids talk
default jessicaLikeEvent5 = Event('Mommy says', 'jessicaLikeEvent5', [jessica], 120, 55, [jessicaVacation], location_home)

label jessicaFirstMeeting(fromGallery):
    $ location_beach.showBackground()
    call playMusic(chillTheme) from _call_playMusic_104
    "В хорошую погоду по дороге домой я люблю пройтись вдоль моря."
    "Прохладный бриз и тихий плеск волн приятно разнообразят путь между баром и домом."
    "Здесь, конечно, всегда полно народу. Парочки, семьи и все остальные."
    "Приятно видеть. Я всё ещё привыкаю к разнообразию видов: столько забавных форм, размеров, цветов и узоров."
    "Кстати об узорах: увидев кое-кого, я замираю на месте."
    "Чуть ниже тропинки, на пляже, стоит очень эффектная девушка."
    scene jessicafirstmeetingi1 with fade
    "Изящная, стройная, кошачья. Она похожа на леопарда?"
    "Вся покрыта характерными пятнышками, которые хорошо видны сквозь довольно откровенную одежду."
    "Она очень стройная и довольно высокая для девушки: длинные выразительные руки и ноги, почти модельные пропорции."
    "На вид совсем молодая, одета по последней моде, ещё и украшена дорогими безделушками."
    "Может, она учится в университете? Я мало что понимаю в моде, но одежда и аксессуары выглядят дорогими."
    $ location_beach.showBackground()
    show jessica tease with dissolve
    "Наверное, среди студентов тоже бывают богатенькие детки."
    "Я стою неподалёку и таращусь на неё как идиот. Пора идти, пока меня не приняли за извращенца."
    "Но она уткнулась в телефон и, похоже, делает селфи. {b}Очень много{/b} селфи."
    "Принимает разные позы, держит телефон под всевозможными углами, показывает жесты и подмигивает камере."
    "...Пора идти."
    show jessica thinking
    "Как раз когда я прохожу за её спиной, она отрывается от телефона и оглядывается."
    show jessica smile talk
    jessica_unknown "Эй! Ты!"
    jessica_unknown "Не мог бы сфотографировать меня на фоне моря? Спасибочки!"
    show jessica smile
    "Она говорит со мной, почти не замечая меня, суёт мне телефон и отбегает на несколько шагов."
    show jessica joy
    "Она поворачивается и принимает позу. Я смотрю на открытое приложение камеры. Пожалуй, надо помочь."
    "Люди сейчас предпочитают горизонтальные или вертикальные фото? Я уже не знаю."
    "Решаю сделать вертикальный снимок в полный рост, чтобы море тоже попало в кадр."
    "Я не фотограф, но, кажется, у меня есть хоть немного художественного чутья."
    mc.c "Готово."
    show jessica smile talk 2
    jessica_unknown "Спасибо!"
    show jessica smile
    "Она подбегает и выхватывает телефон из моей руки, даже не глядя мне в глаза."
    "Но, забирая его, бросает взгляд на мою руку. Потом снова смотрит мне в лицо."
    show jessica surprise
    jessica_unknown "А?"
    jessica_unknown "Ничего себе, ты, типа, человек или кто?"
    mc.c "Э-э, да, человек."
    jessica_unknown "Ого! Мне никто не говорил, что тут есть такие, как ты."
    "Такие, как я?"
    mc.c "Это... проблема?"
    jessica_unknown "..."
    "Она показалась довольно резкой, но, кажется, только сейчас поняла, как это прозвучало."
    show jessica bashful talk
    jessica_unknown "Ой... Э-э... Нет... Просто..."
    jessica_unknown "Прости, я не хотела ничего такого сказать..."
    jessica_unknown "Я только переехала... Думала, тут одни антро."
    show jessica bashful
    mc.c "В основном так и есть. Я тоже недавно приехал."
    mc.c "Но тут есть ещё несколько людей."
    show jessica sad talk
    jessica_unknown "Это прозвучало ужасно грубо. Прости."
    show jessica sad
    mc.c "Всё нормально. Удивлён, что ты не заметила этого, когда попросила меня сфотографировать."
    show jessica thinking
    jessica_unknown "И правда. Как я так умудрилась?"
    "Похоже, она быстро забывает этот разговор и снова смотрит в телефон."
    show jessica joy
    jessica_unknown "Ого! Это просто потрясающе!"
    jessica_unknown "Я тут такая милая, правда?"
    "Она снова поворачивает телефон ко мне. Это тот снимок, который я только что сделал..."
    mc.c "Э-э, да, конечно."
    show jessica tease
    "Она забирает телефон и начинает листать галерею, всё время улыбаясь. Там одни её фотографии."
    show jessica smile talk 2
    jessica_unknown "Ага-ага, эту точно выложу."
    jessica_unknown "Раз уж ты меня сфотографировал, давай добавлю тебя в «Инстру». Какой у тебя ник?"
    show jessica smile
    mc.c "Ой, я там не зарегистрирован."
    show jessica surprise
    jessica_unknown "Чего-о? Почему?"
    mc.c "Просто не моё."
    show jessica thinking
    jessica_unknown "Хм... Ладно, неважно."
    "Чёртова старомодность — упускаю шанс взять у девушки контакты..."
    show jessica smile talk
    jessica.c "Кстати, я Джессика. Только начала здесь учиться. Ты тоже?"
    jessica.c "Хотя я год путешествовала, так что поступила только в этом году!"
    show jessica smile
    mc.c "Я? Нет, я уже не учусь. Бросил колледж."
    mc.c "Я [mc.name], управляю баром в городе. Знаешь тот, что на Лейн-стрит?"
    show jessica neutral talk
    jessica.c "Э-э... Кажется, нет."
    show jessica neutral
    mc.c "Ничего страшного. Студентам у нас рады, так что наверняка ещё заглянешь."
    mc.c "Приходи поздороваться."
    show jessica smile talk 2
    jessica.c "О, ладно."
    show jessica neutral
    "Разговор постепенно затихает. Она снова утыкается в телефон."
    mc.c "Я пойду туда. Удачи в колледже, ладно?"
    show jessica smile talk
    jessica.c "Конечно! И ещё раз спасибо за фото!"
    jessica.c "Как-нибудь ещё меня поснимай."
    show jessica smile
    "Я немного удивлён. Похоже, она не против увидеться снова."
    hide jessica with dissolve
    "Я машу ей рукой и иду дальше по пляжу."
    "Не совсем такого я ожидал сегодня, но... В ней есть что-то завораживающее."
    "Надеюсь, мы ещё встретимся."

    if(not fromGallery):
        $ jessica.knownToMC = True
        $ jessica.addLike(1)

    return


label jessicaLikeEvent1(fromGallery):
    $ location_bar.showBackground()
    call playMusic(chillTheme) from _call_playMusic_105
    "Прямо посреди {b}очень{/b} скучной смены."
    "Сегодня почему-то совсем тихо. Что происходит? В городе что-то случилось?"
    "Заглянуло всего несколько старых завсегдатаев. Хорошо, что постоянные клиенты есть."
    "Всё вымыто, краны наполнены, касса проверена... Осталось только ждать."
    "Надо бы купить лицензию на спортивные трансляции. Хоть будет что посмотреть."
    "К счастью, в дверь входит знакомое лицо."
    show jessica neutral with dissolve
    "Та девушка, Джессика. А за ней — несколько девушек студенческого возраста, похоже, её подруги."
    "Пока они болтают и выбирают столик, Джессика растерянно оглядывается."
    "Наконец подруги привлекают её внимание и обсуждают планы. Не слышу, о чём речь, но Джессика подходит ко мне, пока остальные садятся."
    mc.c "Привет, Джессика! Рад, что ты пришла."
    show jessica bashful talk
    jessica.c "Э-э, привет, [mc.name]."
    show jessica bashful
    "Она не выглядит особенно довольной."
    mc.c "Что-то случилось?"
    show jessica bashful talk
    jessica.c "Ой, э-э, ну..."
    show jessica neutral talk
    jessica.c "Это правда твоё заведение?"
    show jessica neutral
    mc.c "Ага! Я им горжусь."
    show jessica bashful talk
    jessica.c "Ой... Э-э... Ну ладно..."
    show jessica bashful
    mc.c "А что такое?"
    show jessica bashful talk
    jessica.c "Просто... Я представляла себе совсем другое."
    show jessica bashful
    mc.c "Правда? А что именно?"
    show jessica bashful talk
    jessica.c "Не знаю... Какое-нибудь модное место."
    jessica.c "Диваны, музыка, свет..."
    jessica.c "И народу почти нет."
    show jessica bashful
    mc.c "Извини, что разочаровал. Это скорее скромный паб."
    "Похоже, она привыкла к заведениям классом повыше... Вот чёрт."
    mc.c "Зато у нас рады студентам и местным. Дёшево и весело."
    call playMusic(funnyTheme) from _call_playMusic_106
    show jessica neutral talk
    jessica.c "Дёшево... и весело?"
    show jessica neutral
    "Она смотрит на меня так, словно никогда не слышала о таком понятии."
    mc.c "Ага, просто место, где можно выпить, без лишних заморочек. Никакой чепухи."
    show jessica thinking
    jessica.c "Хм..."
    show jessica smile talk
    jessica.c "О, мне нравится!"
    jessica.c "Ладно, почему нет? Может быть весело! Вдруг это новый тренд?"
    show jessica smile
    "Странный разговор, но, кажется, я её переубедил."
    show jessica smile talk 2
    jessica.c "Ладно! Подруги хотят шампанского или чего-то такого."
    show jessica smile
    "Для нашего бара заказ необычный, но, кажется, где-то есть бутылка..."
    mc.c "Ого, ладно! Что отмечаете?"
    show jessica neutral talk
    jessica.c "Ничего...?"
    show jessica neutral
    "..."
    "Ладно... Для неё это, видимо, обычный вечер. Может, она и правда богата."
    "Она протягивает карту. На ней точно не её имя."
    mc.c "Я думал, тебя зовут Джессика."
    show jessica mad talk
    jessica.c "А?"
    show jessica smile talk
    jessica.c "А, это папина карта."
    show jessica smile
    "Кажется, я начинаю понимать. Богатую девочку отправили учиться за папин счёт."
    "Вот откуда такие ожидания. В какой семье она выросла?"
    mc.c "Он не против, что ты пользуешься его картой?"
    show jessica smile talk 2
    jessica.c "Конечно. А почему нет?"
    show jessica smile
    "...Наивность или полная оторванность от реальности?"
    mc.c "Ладно, без проблем. Раз уж напитки такие изысканные, сам принесу их к вашему столику. Хорошо?"
    show jessica tease talk
    jessica.c "Спасибочки!"
    hide jessica with dissolve
    "Джессика разворачивается и вприпрыжку возвращается к подругам."
    "Я разношу им напитки и оставляю компанию отдыхать."
    scene black with fade
    "Они сплетничают и хихикают. К счастью, в течение дня заходят и другие компании."
    "Похоже, эти девушки совсем не думают о расходах. Особенно странно для студенток, которые обычно сюда заходят."
    "Либо они очень богатые, либо вообще не замечают, сколько тратят."
    "Кому-то повезло, да?"
    $ location_bar.showBackground()
    "В течение дня девушки изрядно напиваются и хихикают за столиком."
    "Похоже, они уже собираются уходить: забирают свои вещи."
    "Джессика поглядывает на меня, они перешёптываются и снова хихикают."
    "Остальные ждут у двери, пока Джессика подбегает ко мне."
    show jessica smile talk 2 with dissolve
    jessica.c "[mc.name]! Спасибочки, нам понравилось~"
    show jessica smile
    mc.c "Рад, что мне удалось покорить вас своим скромным заведением."
    show jessica smile talk 2
    jessica.c "Мы точно ещё придём!"
    show jessica tease talk
    jessica.c "И слушай..."
    jessica.c "Фото, которое ты сделал, просто лучшее! Мне поставили кучу лайков!"
    jessica.c "Правда, надо попросить тебя сделать ещё несколько моих фото."
    show jessica smile talk 2
    jessica.c "А раз тебя нет в «Инстре»..."
    show jessica tease talk
    jessica.c "Держи мой номер!"
    show jessica tease
    "Она протягивает мне листок с номером телефона."
    show jessica joy
    jessica.c "Пока!"
    hide jessica with dissolve
    "Девушки заливаются смехом и, пошатываясь, выходят."
    "Забавно получилось..."
    "Это было приглашение?"

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.blockedLocations.remove(location_bar)

    return


label jessicaLikeEvent2(fromGallery):
    $ location_beach.showBackground()
    call playMusic(chillTheme) from _call_playMusic_107
    "К приятному удивлению, Джессика сама предложила встретиться."
    "Мы переписывались и иногда сталкивались, но теперь договорились увидеться."
    "К сожалению, не на свидании, а... я буду её фотографом."
    "Она не шутила... Почему-то она одержима той фотографией, которую я мимоходом сделал, когда мы ещё не были знакомы."
    "...И сама собой. Никогда не встречал человека, который так восхищался бы собственной внешностью."
    "Наверное, её можно понять. Она очень... эффектная. Считается ли леопардовый принт красивым среди антро?"
    "В общем, она уверена, что я подхожу на эту роль. Я не совсем бездарь, но и художник из меня никакой. А вдруг прошлый снимок был случайной удачей?"
    "Снова идём на пляж — устроить небольшую фотосессию. Интересно, что она задумала. Может, мне повезёт и я увижу её в бикини?"
    "Я оглядываюсь. Как ни странно, сначала её не замечаю..."
    show jessica joy with dissolve
    jessica.c "[mc.name]!"
    "Она первой замечает меня и машет рукой. Несмотря на яркую внешность, её шерсть почти сливается с песком."
    "А, вот так работает эволюция окраса. Забавно."
    mc.c "Привет, Джессика."
    show jessica smile talk 2
    jessica.c "Спасибо, что пришёл! Ты меня просто спас!"
    show jessica smile
    mc.c "Спас? Я же всего лишь сделаю несколько фото, да?"
    show jessica smile talk 2
    jessica.c "Ну, твои прошлые фотографии были потрясающие! Мне нужно больше."
    show jessica mad talk
    jessica.c "{size=20}А эти стервы не захотели помочь...{/size}"
    show jessica mad
    mc.c "Что ты сказала?"
    show jessica mad talk
    jessica.c "Эх, неважно..."
    show jessica neutral talk
    jessica.c "Я бы сама справилась, но с треногой так неудобно."
    show jessica neutral
    mc.c "Мне не сложно, но ты уверена? Я не профессионал."
    show jessica smile talk 2
    jessica.c "Не знаю, в той прошлой фотографии было что-то особенное."
    jessica.c "Моим подписчикам понравилось!"
    show jessica smile
    mc.c "Ты типа модель для «Инстры»?"
    show jessica thinking
    jessica.c "Хм... Пока нет, наверное."
    show jessica smile talk 2
    jessica.c "Но хочу! Это прямо моё!"
    show jessica smile
    mc.c "Ты давно ведёшь страницу? Сколько у тебя подписчиков?"
    show jessica tease talk
    jessica.c "Несколько месяцев! Завела во время путешествий. Куча фоток с отдыха, знаешь?"
    show jessica joy
    jessica.c "Уже целых восемьдесят! Последнее фото собрало семь лайков!"
    "..."
    "Модель {b}начинающая{/b}, мягко говоря. Я не особо разбираюсь в этой сфере, но звучит как-то скромно."
    mc.c "О, ну... здорово..."
    show jessica surprise
    jessica.c "Только папе нельзя говорить! Он хочет, чтобы я устроилась на работу или ещё что-нибудь."
    show jessica thinking
    jessica.c "А что я тут изучаю? Что-то-логия... что-то-ведение..."
    show jessica joy
    jessica.c "Не знаю, просто выбрала что-то."
    "Забавная она. Немного рассеянная, жизнерадостная."
    "Хочет стать моделью, что не удивительно для красивой и, вероятно, популярной девушки. Но ожидания от славы у неё на удивление скромные."
    "Она могла бы быть богатой и высокомерной, считать, что станет знаменитой просто так."
    "Она всё равно влюблена в себя, но это даже мило."
    mc.c "Начнём? Что ты хотела сделать?"
    show jessica smile talk
    jessica.c "Конечно! Хочу ещё снимков на фоне моря. Я буду позировать, а ты выбирай ракурсы. Просто!"
    show jessica smile
    jessica.c "Думаю, справлюсь. Только направляй меня."
    show jessica smile talk
    jessica.c "Сначала дай свой телефон, посмотрим, у кого камера лучше..."
    show jessica smile
    "Я показываю ей свой жалкий, простенький, слегка потрёпанный кирпич."
    show jessica neutral
    jessica.c "..."
    show jessica neutral talk
    jessica.c "Серьёзно?"
    show jessica neutral
    mc.c "Э-э, да?"
    show jessica surprise
    jessica.c "Ему уже {b}сто лет{/b}."
    jessica.c "Как ты вообще пользуешься этой штукой?"
    "Я никогда особо не ценил современность телефона."
    mc.c "Значит, будем фотографировать на твой."
    show jessica bashful talk
    jessica.c "Э-э, ага. Прости."
    show jessica bashful
    mc.c "Ничего страшного."
    "Она протягивает мне свой безупречный стильный телефон. Похоже, одна из последних моделей."
    show jessica joy
    jessica.c "Ладно, сначала переоденусь."
    mc.c "Переоденешься?"
    show jessica neutral talk
    jessica.c "Ну да, в купальник. Очевидно же."
    show jessica neutral
    "Вот это да."
    hide jessica with dissolve
    "Джессика вприпрыжку бежит в кабинку для переодевания. Интересно, какой у неё купальник?"
    "Вот я стою с телефоном девушки и собираюсь фотографировать её в бикини. А она ещё и благодарит меня. Как я сюда попал?"
    "Через пару минут..."
    jessica.c "Ну что, готов?"
    scene jessicalikeevent2i1 with fade
    "Ничего себе!"
    "Джессика появляется в ярко-синем раздельном купальнике."
    "Лиф украшен оборками, а поверх очень открытого низа надета мини-юбка."
    "На фоне открывшегося узорчатого меха она выглядит очень эффектно."
    "Теперь я вижу едва заметные различия в цвете шерсти на её теле."
    "Изящная, элегантная и очень красивая. Конечно, я про шерсть..."
    jessica.c "Язык проглотил?"
    mc.c "Ой, э-э, выглядит здорово!"
    jessica.c "Знаю, да? Самый милый узор на свете."
    "Она это прекрасно знает..."
    jessica.c "Ладно, я пойду туда. Ты встань вот тут и снимай как в прошлый раз!"
    "Джессика принимает милую невинную позу."
    scene jessicalikeevent2i2 with fade
    jessica.c "Ниже!"
    jessica.c "Да, вот так!"
    "Она командует, куда мне направлять камеру, и водит меня по разным участкам пляжа."
    scene jessicalikeevent2i3 with fade
    "Постепенно позы становятся... всё откровеннее."
    "Она принимает самые разные позы и меняет выражения лица."
    scene jessicalikeevent2i4 with fade
    "Кадр за кадром..."
    scene black with fade
    "Так продолжается довольно долго..."
    "К концу я замечаю нескольких зевак. Она притягивает взгляды и оборачивает за собой головы."
    jessica.c "Думаю, достаточно. Уже прохладно, дай быстро оденусь."
    "Она быстро бежит к кабинке для переодевания."
    $ location_beach.showBackground()
    show jessica smile talk 2 with dissolve
    jessica.c "Давай смотреть!"
    show jessica smile
    "Она почти вырывает телефон из моих рук."
    "Её глаза широко распахнуты от предвкушения новых снимков, на лице сияет улыбка."
    show jessica tease talk
    jessica.c "О-о~"
    show jessica smile talk 2
    jessica.c "О да!"
    "Она листает снимки туда-сюда."
    show jessica joy
    jessica.c "Боже мой!"
    jessica.c "Они такие классные, [mc.name]!"
    jessica.c "Смотри, смотри! Просто огонь!"
    "Она суёт мне один снимок под нос. Я тоже особенно им гордился."
    mc.c "Да, красиво получилось."
    show jessica tease talk
    jessica.c "То есть, очень горячо? Миленько-горячо? Просто мило?"
    show jessica tease
    "Она выжидающе смотрит на меня. Что ответить? Что-то среднее?"
    mc.c "...Миленько-горячо?"
    show jessica joy
    jessica.c "Вот именно! Так и хотела!"
    "В яблочко. Было бы ошибкой сказать «обжигающе сексуально», как я подумал."
    hide jessica with dissolve
    show jessica hug with dissolve
    pause
    "Она крепко обнимает меня, застав врасплох."
    jessica.c "Ты так здорово справился!"
    jessica.c "Теперь ты должен фотографировать меня постоянно! Я стану вирусной!"
    mc.c "Ха-ха, когда угодно, Джессика. Было весело."
    hide jessica with dissolve
    show jessica tease talk with dissolve
    jessica.c "Ты хороший парень, [mc.name]. Спасибо. Я тут ещё мало кого знаю, но ты классный."
    show jessica tease
    mc.c "Не за что. Ты сама классная. Круче меня."
    show jessica thinking
    jessica.c "Ну... Типа того..."
    show jessica smile talk 2
    jessica.c "Может, повторим как-нибудь?"
    mc.c "Если только ты не используешь меня ради моих невероятных художественных навыков."
    show jessica surprise
    jessica.c "Нет! То есть, ну... можем..."
    mc.c "Шучу. Да, конечно, я буду рад помочь или просто погулять."
    show jessica bashful
    "Кажется, она немного краснеет."
    show jessica smile talk
    jessica.c "Я выложу часть этих фотографий и расскажу, как всё прошло, ладно?"
    show jessica smile talk 2
    jessica.c "Спасибочки, [mc.name]!"
    hide jessica with dissolve
    show jessica hug with dissolve
    hide jessica with dissolve
    "На прощание она быстро обнимает меня и с радостной улыбкой бежит по песчаному склону."

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)
        $ jessica.isDateable = True
        "Теперь можно приглашать [jessica.name] на свидания."

    return

label jessicaLikeEvent3(fromGallery):
    call playMusic(funnyTheme) from _call_playMusic_108
    $ location_park.showBackground()
    "Ещё одна фотосессия с Джессикой."
    "Она с энтузиазмом потащила меня на новую съёмку. Ей очень понравились пляжные фотографии."
    "Я упрямо не регистрируюсь в «Инстре», так что не знаю, насколько они популярны, но она была в восторге от первого раза."
    "Она прислала мне фотографии, которые выкладывала."
    "Хотя снимал я, они получились неожиданно хорошими."
    "Думаю, всё дело в модели. Она очень... эффектная. Её сложно плохо сфотографировать."
    jessica.c "[mc.name]~"
    show jessica joy with dissolve
    jessica.c "Привет!"
    mc.c "Привет, Джессика."
    show jessica tease talk
    jessica.c "Смотри, смотри!"
    show jessica tease
    "Джессика суёт телефон мне под нос. Она открыла одну из новых пляжных публикаций с нашей съёмки."
    mc.c "Ага, красиво, да?"
    show jessica smile talk 2
    jessica.c "Ну конечно, но посмотри на реакции!"
    show jessica smile
    "Я щурюсь, пытаясь найти цифры в этом приложении."
    "«16 отметок „Нравится“, 3 комментария»"
    "Больше, чем у прошлой фотографии, которой она радовалась, но всё равно... Для начинающей модели это не так уж много."
    mc.c "О, здорово. Это твой рекорд?"
    show jessica tease talk
    jessica.c "Да! С большим отрывом!"
    show jessica tease
    mc.c "Что пишут в комментариях?"
    show jessica neutral talk
    jessica.c "Э-э..."
    show jessica neutral
    "Она на секунду замолкает и разворачивает телефон к себе."
    show jessica neutral talk
    jessica.c "Один поставил сердечко, а второй оказался спам-ботом..."
    jessica.c "А третий написал «абабабаб»."
    show jessica thinking
    jessica.c "Не знаю, что это значит."
    show jessica tease talk
    jessica.c "Может, на каком-то языке это значит «потрясающе»!"
    jessica.c "Кажется, им нравится!"
    show jessica tease
    "Это не самые восторженные отзывы, но её фотографии хотя бы замечают. Если ей это нужно."
    show jessica smile talk 2
    jessica.c "Так что всё благодаря тебе."
    jessica.c "Поэтому я и хотела ещё фотографий. Здесь такой красивый парк, правда?"
    show jessica smile
    "Обычный городской парк. Скорее дворик, чем что-то особенное. Но в целом симпатичный."
    mc.c "Конечно. Я часто здесь бываю. Думаю, тут есть красивые места для снимков."
    show jessica surprise
    jessica.c "Ничего себе, ты точно не профессионал? Звучит так, будто ты разбираешься!"
    "Комплимент с подвохом, но, кажется, она хотела сказать приятное."
    mc.c "Ну, не жди слишком многого."
    mc.c "К тому же дело в том, кто на снимке, а не в фотографе."
    "Кажется, этот флирт немного слишком явный..."
    show jessica tease talk
    jessica.c "Ну, это правда."
    show jessica tease
    "И она прекрасно это знает..."
    show jessica smile talk
    jessica.c "Ладно, держи телефон. С чего начнём?"
    mc.c "Давай попробуем здесь. Встань сюда, и..."
    scene black with fade
    "Мы продолжаем фотосессию."
    "Несмотря на уверенность в себе, она доверяет мне выбирать позы и ракурсы."
    "Похоже, прежние удачные снимки придали мне авторитет."
    scene jessicapark with fade
    "Я мало знаю о моделинге, но у неё природная грация, которая отлично смотрится на фото."
    "Стройная фигура с гармоничными изгибами."
    "Юное милое лицо. Даже красивое."
    scene jessicalikeevent3i1 with fade
    "И этот невероятный узор. Не знаю стандартов красоты у антро, но чем ярче, тем лучше?"
    "Не могу оторваться от некоторых снимков. Стоит ей лишь откинуть волосы, и все обернутся."
    "А её экзотические глаза смотрят прямо на меня. Я и сам поражён."
    scene black with fade
    "Мы долго ходим по парку, и она таскает меня за собой."
    jessica.c "Ладно, хватит. Давай смотреть фотографии!"
    call playMusic(chillTheme) from _call_playMusic_109
    $ location_park.showBackground()
    show jessica tease with dissolve
    "Мы садимся на скамейку, а она начинает просматривать снимки."
    show jessica tease talk
    jessica.c "О-о~ М-м~"
    show jessica tease
    "Она сияет и листает фотографии, явно довольная результатом."
    show jessica smile talk
    jessica.c "Боже мой! Вот эта такая милая!"
    show jessica smile
    "Она задерживается на одном из множества снимков. Честно, они все похожи. На каждом она очень красивая..."
    show jessica joy
    jessica.c "О-о-о~ И эта тоже~"
    jessica.c "Безумно мило!"
    show jessica smile talk 2
    jessica.c "Опять такие классные фотографии, [mc.name]! Обожаю их!"
    show jessica smile
    mc.c "Отлично! С тобой легко. Думаю, у кого угодно получились бы хорошие фото, если бы ты была моделью."
    show jessica tease talk
    jessica.c "Но это ты их сделал! Я правда очень-очень благодарна."
    show jessica neutral talk
    jessica.c "Ты мог бы заниматься чем угодно, но помог мне. Я ведь не веду себя эгоистично?"
    show jessica neutral
    mc.c "Да не проблема, правда. Мне весело."
    show jessica tease
    "Она снова улыбается и продолжает любоваться нашими снимками."
    "Интересно, чего она добивается. Просто хочет внимания?"
    "Она говорила, что хочет стать моделью в «Инстре». Что для этого нужно? Это то, что сейчас называют «инфлюенсером»?"
    mc.c "Собираешься что-нибудь выложить?"
    show jessica smile talk
    jessica.c "Конечно. Не могу выбрать."
    show jessica smile
    mc.c "Можно спросить... Какова цель? Получить просмотры и лайки — и всё? Дело только в цифрах?"
    show jessica neutral talk
    jessica.c "Ну, отчасти. Если их станет больше, компании обратят на меня внимание и напишут в личку."
    show jessica neutral
    mc.c "Компании?"
    show jessica neutral talk
    jessica.c "Ага, производители одежды. Бренды."
    show jessica neutral
    mc.c "А, они будут присылать одежду, чтобы ты её рекламировала?"
    show jessica smile talk 2
    jessica.c "Да! Буду настоящей моделью!"
    show jessica smile
    mc.c "Моделью... Значит, будешь сниматься для журналов?"
    show jessica mad talk
    jessica.c "Журналы? Кто их читает? Сколько тебе лет, [mc.name]?"
    show jessica mad
    "Ой. Похоже, сейчас это уже не актуально."
    show jessica smile talk
    jessica.c "Нет, много девушек зарабатывают только благодаря моделингу в «Инсте»."
    call playMusic(heartTheme) from _call_playMusic_110
    show jessica bashful talk
    jessica.c "Думаешь, у меня получится?"
    show jessica bashful
    "Её лицо омрачается."
    mc.c "Конечно. А ты сама сомневаешься?"
    show jessica bashful talk
    jessica.c "Я думала, что получится, но... Мне говорили бросить это."
    show jessica bashful
    mc.c "Правда? Кто?"
    show jessica bashful talk
    jessica.c "Ну... Родители... И бывший."
    jessica.c "Он сказал, что леопардов не берут в модели. Агентствам не нужны модели с пятнистой шерстью или что-то такое."
    show jessica bashful
    "Неужели среди антро и правда есть предпочтения к узорам шерсти? Я не замечал."
    "Грустно... Как кто-то мог не оценить эту красоту?"
    "Но это значит... Она свободна?"
    show jessica sad talk
    jessica.c "Родители довольно строгие. Я бы даже не училась в колледже, если бы они не заставили."
    show jessica sad
    mc.c "О... Они тебя не поддерживают?"
    show jessica sad talk
    jessica.c "Нет... Папа особенно. Хочет, чтобы у меня была «настоящая работа». Наверное, поэтому я и здесь."
    show jessica sad
    mc.c "Жаль. Но почему нельзя совмещать? Соцсети не мешают учиться."
    show jessica surprise
    jessica.c "Я им то же самое говорила! Боже!"
    show jessica thinking
    jessica.c "Хотя учёба — это совсем другое... Я плохо учусь..."
    show jessica tease talk
    jessica.c "Может, поможешь мне с этим?"
    show jessica tease
    mc.c "Не смотри на меня. Я тоже никогда не любил учиться..."
    show jessica joy
    jessica.c "Ха-ха! Ничего, я просто шучу~"
    "Её настроение меняется мгновенно. Только что она была расстроена, а теперь уже забыла об этом."
    show jessica smile talk 2
    jessica.c "[mc.name]... Ты хороший парень. Все люди такие?"
    show jessica smile
    mc.c "Конечно нет. Я лучший из всех. Держись подальше от остальных."
    show jessica joy
    jessica.c "Ха-ха-ха! Боже мой~ Перестань~"
    "Она игриво хлопает меня по руке."
    mc.c "Если что, от безволосого — твой узор очень красивый."
    show jessica smile talk 2
    jessica.c "Ой, спасибочки! Твоя кожа такая... Э-э... М-м..."
    show jessica smile
    mc.c "..."
    jessica.c "..."
    show jessica joy
    jessica.c "Ха-ха-ха!"
    mc.c "Хе-хе."
    "Мы оба тихонько хихикаем, потому что она не может подобрать слова."
    show jessica smile talk
    jessica.c "Ха-а~ Ты смешной."
    show jessica smile
    "Мы всё ещё сидим на скамейке, рассматриваем фотографии и постепенно придвигаемся друг к другу."
    "Но сейчас она впервые не смотрит в телефон. Мы смотрим друг на друга."
    "Между нами нарастает напряжение, мы молча улыбаемся. Я правильно всё понимаю?"
    "Она мне определённо нравится. Это заметно? Нужно сказать прямо?"
    jessica.c "..."
    "Она... незаметно придвигается ближе?"
    "Стоит попробовать..."
    hide jessica with dissolve
    show jessica kiss with dissolve
    pause
    jessica.c "М-м~"
    "Мы одновременно наклоняемся друг к другу и соприкасаемся губами."
    "Наши губы слегка приоткрываются. Это уже не чмок в щёку. Мы задерживаемся в поцелуе."
    "Я осторожно кладу руку ей на бедро, но она не отстраняется."
    show jessica hug with dissolve
    jessica.c "..."
    mc.c "..."
    "Не могу придумать ничего романтичного. Как обычно..."
    mc.c "Я подумал, что ты рядом только из-за моих талантов фотографа."
    jessica.c "М-м~ Отчасти..."
    jessica.c "Но потом поняла, что ты и сам довольно милый."
    mc.c "Ничего себе. Я и модель — что скажет пресса?"
    jessica.c "Хе-хе~"
    show jessica kiss with dissolve
    jessica.c "М-м~"
    "Мы снова целуемся."
    hide jessica with dissolve
    show jessica tease talk with dissolve
    jessica.c "[mc.name]... Ещё раз спасибо~"
    show jessica tease
    mc.c "Не за что, Джессика. Всегда пожалуйста."
    show jessica tease talk
    jessica.c "В следующий раз давай сходим куда-нибудь как следует~"
    show jessica tease
    mc.c "Предоставь это мне!"
    show jessica joy
    jessica.c "Пока-пока!"
    hide jessica with dissolve
    "Она вприпрыжку скрывается за углом, как всегда подпрыгивая на ходу."
    "Не верится, что я ей тоже понравился."
    "Сделаем из неё настоящую модель!"

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaHEvent1(fromGallery):
    $ location_town.showBackground()
    show jessica smile with dissolve
    call playMusic(chillTheme) from _call_playMusic_111
    "Мы гуляем по центру города с Джессикой."
    "Для нас это обычный выходной по одной простой причине. Эта девушка... очень любит шопинг."
    "Она долго выбирает, но и без меня покупает немало одежды. Куда она всё складывает? Студенческое жильё не может быть таким большим."
    "Наверняка папа снимает ей хорошую квартиру."
    "Я стараюсь не жаловаться, как типичный мужчина, что меня таскают по магазинам, но... похоже, это неизбежная часть жизни."
    "Надо напоминать себе, как мне повезло. Я вижу эту красавицу в невероятных нарядах. Всё не так уж плохо."
    show jessica joy
    jessica.c "О-о~ [mc.name], [mc.name], глянь!"
    "Она подбегает к витрине и показывает на модный комплект из рубашки и шорт на манекене."
    "Вроде... неплохо? Я ничего не понимаю в моде. Сам-то я хожу в простой серой футболке и джинсах."
    mc.c "Хорошо выглядит. Думаешь взять рубашку или шорты?"
    show jessica mad talk
    jessica.c "А? Это комплект, глупыш. Они должны идти вместе!"
    show jessica mad
    "Ой."
    mc.c "А, ну конечно... Хочешь примерить?"
    show jessica thinking
    jessica.c "Хм... Не. Мне не нравится молния на шортах. Сейчас не сезон."
    "Для молнии тоже есть сезон?"
    show jessica smile talk 2
    jessica.c "Ну же, пойдём. Тут неподалёку есть хороший магазин."
    show jessica smile
    "Она хватает меня за запястье, поворачивает и тащит вверх по улице."
    "Она совсем не боится прикосновений. Это довольно мило."
    show jessica tease talk
    jessica.c "Вот, вот!"
    show jessica tease
    "Мы останавливаемся перед довольно роскошным магазином. Видно, что он дорогой."
    "За всё время здесь я ни разу не решался зайти. Явно модное место. А мужское там вообще продают?"
    mc.c "В этот магазин?"
    show jessica neutral talk
    jessica.c "Ага, почему нет?"
    show jessica neutral
    mc.c "Да нет, просто выглядит дороговато для меня. Я здесь никогда не был."
    show jessica thinking
    jessica.c "Дорого? Не знаю, я уже покупала здесь кое-что."
    "Похоже, у нас разные представления о дороговизне..."
    mc.c "Тебе виднее. Я в моде ничего не понимаю."
    show jessica tease talk
    jessica.c "Ну очевидно... Посмотри на себя."
    jessica.c "Может, и тебе что-нибудь найдём?"
    show jessica tease
    "Ай. Но... да, она права."
    "Но я не представляю себя в чём-то настолько модном. Наверное, всё равно будем выбирать ей."
    scene clothesshop with fade
    show jessica smile with dissolve
    "Мы заходим внутрь, и она сразу направляется к стойкам с одеждой."
    "Внутри несколько человек. В основном молодые, модно одетые женщины."
    "И один бедолага развалился на диване с несколькими пакетами и несчастным видом. Устал ходить за кем-то или расстроен, что платит за всё?"
    show jessica thinking
    jessica.c "Хм~ Неа."
    show jessica smile talk 2
    jessica.c "О-о~ Может быть..."
    show jessica smile
    "Джессика перебирает вешалки, иногда снимает вещь и прикладывает к себе, чтобы оценить размер."
    show jessica surprise
    jessica.c "О-о~ Да!"
    show jessica tease talk
    jessica.c "[mc.name], [mc.name], как тебе?"
    show jessica tease
    "Она прикладывает к груди красивое необычное платье. Яркое и, похоже, довольно откровенное."
    mc.c "О, да, выглядит хорошо."
    show jessica neutral talk
    jessica.c "Хорошо? Не слишком осеннее? Подойдёт к этому ожерелью?"
    show jessica neutral
    "Я смотрю на неё каменным лицом. Я... понятия не имею."
    mc.c "Э-э..."
    show jessica joy
    jessica.c "Ахаха! Видел бы ты своё лицо."
    mc.c "Прости. Вряд ли я тут чем-то помогу."
    show jessica smile talk 2
    jessica.c "Поможешь. Мне понадобится твой совет, когда я их примерю."
    show jessica smile
    "Она подмигивает мне и суёт платье в руки."
    show jessica smile talk
    jessica.c "Давай, подержи. Поищем ещё."
    "Она осматривает зал, выбирая, что посмотреть дальше."
    scene black with fade
    "Мы долго выбираем. То есть она. А я хожу за ней в роли передвижной вешалки."
    "Она набирает небольшую стопку вещей для примерки."
    scene clothesshop with fade
    show jessica smile talk
    jessica.c "Так, пора в примерочную!"
    show jessica thinking
    jessica.c "Хм... С чего начать?"
    show jessica smile talk 2
    jessica.c "Давай вот это!"
    show jessica smile
    "Она выбирает первое платье, которое мы нашли. Уверен, оно ей отлично подойдёт..."
    mc.c "Ладно, конечно."
    "Когда она снимает его с моей руки, я замечаю ценник."
    mc.c "Ого!"
    show jessica neutral talk
    jessica.c "А? Что?"
    show jessica neutral
    mc.c "Цена!"
    "Она бросает взгляд на ценник, даже не дрогнув."
    show jessica neutral talk
    jessica.c "И что?"
    show jessica neutral
    "Триста долларов. Что за чёрт?"
    "Господи. Для неё это нормально? Знаю, семья у неё богатая, но всё же. Наверное, она привыкла."
    "Я почти всё покупаю на распродажах."
    mc.c "Это... нормально?"
    show jessica thinking
    jessica.c "Вроде да? У этой марки обычно такие цены."
    mc.c "Если ты так говоришь."
    "Надеюсь, она не ждёт, что я за это заплачу. И это только первое платье!"
    show jessica tease talk
    jessica.c "Ладно! Будь хорошим мальчиком, подожди снаружи и подержи остальные вещи."
    hide jessica with dissolve
    "Она скрывается в примерочной и с поворотом закрывает занавеску."
    "Уже представляю её в этом платье. Неужели мне устроят показ мод?"
    "..."
    "Проходит пара минут. Из-за занавески слышно лишь шуршание одежды. Сейчас никого больше нет."
    "Интересно, как там тот бедолага с пакетами?"
    jessica.c "[mc.name]?"
    mc.c "Да?"
    jessica.c "Там никого нет?"
    mc.c "Сейчас нет. Можешь выйти и показать, если хочешь."
    jessica.c "Не, я имею в виду..."
    call stopMusic from _call_stopMusic_19
    jessica.c "Зайди сюда..."
    "Погоди... Серьёзно?"
    "Только показать платье, да?"
    mc.c "Ты уверена?"
    jessica.c "Если никто не смотрит... Да~"
    "Ничего себе... Что меня ждёт внутри?"
    call playMusic(sexyTheme) from _call_playMusic_112
    image jessica changingroom handjob start = Image("images/characters/jessica/hscenes/changingRoomHandjob/start.webp")
    scene jessica changingroom handjob start with fade
    pause
    "На ней новое платье. Она мило позирует и выглядит потрясающе."
    "Я задвигаю занавеску за собой."
    mc.c "Ничего себе, оно... тебе очень идёт."
    jessica.c "Правда?"
    "Оно такое же откровенное, как я и думал. Очень... соблазнительное."
    "Грудь полностью открыта, а разрезы по бокам доходят почти до бёдер."
    "Я пытаюсь вспомнить, как раньше её описывал."
    mc.c "Д-да... Миленько-горячо?.."
    jessica.c "Ой, боже... Оно вообще не должно быть миленько-горячим..."
    mc.c "Э-э... Ну..."
    "Мне становится жарко. Здесь тесно, а передо мной очень горячая девушка показывает нечто невероятное."
    jessica.c "Хе-хе... Похоже, тебе {b}правда{/b} нравится, да?"
    "Она с лукавой улыбкой смотрит вниз на моё тело."
    "Ой-ой. Кажется, я возбуждён. Член живёт своей жизнью. Похоже, она не против..."
    mc.c "Д-да... Ты отлично выглядишь."
    "Стоит ли стыдиться, что я так быстро возбудился? Здесь тесно... Она приятно пахнет... Просто..."
    jessica.c "Вижу, что ты не врёшь~"
    jessica.c "Слушай... Хочешь, я немного помогу?"
    "Она осторожно кладёт руку мне на пах, где уже начинает выпирать."
    "В её глазах особый взгляд. Кто я такой, чтобы отказываться?"
    mc.c "Ну?.."
    jessica.c "Не отговаривай себя..."
    "Наверное, лучше молча кивнуть."
    jessica.c "Хорошо~"
    "Она опускается на колени и расстёгивает мне ремень."
    "Вид её в этом платье только ускоряет процесс — я уже возбуждён."
    image jessica changingroom handjob part 1 = Image("images/characters/jessica/hscenes/changingRoomHandjob/part1.webp")
    scene jessica changingroom handjob part 1 with fade
    pause
    "Она стягивает с меня штаны, и мой член гордо выскакивает наружу. Глаза Джессики расширяются."
    jessica.c "О-ого... Боже..."
    "Рад, что она впечатлена."
    jessica.c "Почему у тебя такой большой? Это типа у всех людей так?"
    mc.c "Почему? Не знаю..."
    "Удивление на её лице быстро сменяется похотью."
    image jessica changingroom handjob part 2 = Movie(play="images/characters/jessica/hscenes/changingRoomHandjob/part2.webm")
    show jessica changingroom handjob part 2 with fade
    pause
    "Она несколько раз поглаживает меня, смотрит снизу вверх и придвигает лицо, разглядывая меня."
    jessica.c "Ничего себе~ Вот это да..."
    mc.c "Не делай такое удивлённое лицо..."
    jessica.c "Ну... Кто бы ожидал чего-то такого?"
    "Она нежно обхватывает мой ствол несколькими пальцами и медленно водит ими по всей длине."
    "Длинные изящные пальцы и длинные чёрные когти... Приятный контраст."
    "И ощущения потрясающие."
    jessica.c "Тебе хватило одного этого наряда?"
    mc.c "Он чертовски откровенный. Но дело ещё и в том, кто его носит."
    image jessica changingroom handjob part 3 = Movie(play="images/characters/jessica/hscenes/changingRoomHandjob/part3.webm")
    show jessica changingroom handjob part 3 with fade
    pause
    "Она поднимается и обхватывает мой член обеими руками."
    "Её глаза загораются от восторга."
    jessica.c "Ого, он такой большой, что мне нужны обе руки."
    "Ощущения невероятные, а похвала тоже приятна."
    "Вот так и надо повышать самооценку мужчины."
    mc.c "Ого, чертовски приятно..."
    image jessica changingroom handjob part 4 = Movie(play="images/characters/jessica/hscenes/changingRoomHandjob/part4.webm")
    show jessica changingroom handjob part 4 with fade
    pause
    jessica.c "Он такой твёрдый. У тебя фетиш на одежду или что?"
    "Под её рубашку можно заглянуть. Эротичнее некуда."
    mc.c "Не совсем, но... Тебе почти всё идёт."
    "Я почти полностью отдаюсь моменту, но вдруг вспоминаю, что мы в общественной примерочной."
    mc.c "Чёрт, надо вести себя потише."
    jessica.c "Расслабься, мы же тихо? Дай я тогда закончу~"
    mc.c "Если продолжишь в таком духе, я долго не продержусь."
    "Она с вызовом ухмыляется..."
    image jessica changingroom handjob part 5 = Movie(play="images/characters/jessica/hscenes/changingRoomHandjob/part5.webm")
    show jessica changingroom handjob part 5  with fade
    pause
    "Она ускоряется, сильно водит рукой по моему члену, крепко сжимая его."
    mc.c "О-о..."
    jessica.c "Хе-хе~ Не шуми~"
    mc.c "Я думал, ты милая и невинная девушка... А теперь..."
    jessica.c "Ой~ Просто немного повеселимся~"
    jessica.c "Тебе ведь тоже нравится~"
    "Ещё как. Слишком. Я уже близко."
    mc.c "Джессика, я почти..."
    jessica.c "Ой, э-э..."
    jessica.c "Нельзя так пачкать платье..."
    "Она подносит губы к моей головке и быстро водит рукой по члену."
    mc.c "Чёрт, я..."
    image jessica changingroom handjob end 1 = Image("images/characters/jessica/hscenes/changingRoomHandjob/end1.webp")
    scene jessica changingroom handjob end 1 with fadewhite
    pause
    "Я кончаю прямо ей в рот, а она старается собрать всё до последней капли."
    "Так хорошо, что рот у неё наполняется и сперма вот-вот польётся через край."
    jessica.c "М-мф!"
    "Несколько струй всё же пролетают мимо и попадают ей на лицо."
    "Она ненадолго морщится, а потом быстро проглатывает остатки."
    image jessica changingroom handjob end 2 = Image("images/characters/jessica/hscenes/changingRoomHandjob/end2.webp")
    scene jessica changingroom handjob end 2 with fade
    pause
    jessica.c "Хе-хе~"
    mc.c "Ничего себе."
    jessica.c "Ну... Платье одобряешь?"
    mc.c "Определённо."
    mc.c "Э-э, у тебя на лице немного..."
    "Я показываю на её лицо."
    jessica.c "Ой~"
    "Она вытирает остатки салфеткой, а я подтягиваю штаны."
    mc.c "Я... выйду первым."
    jessica.c "...Проверь, что снаружи никого нет..."
    call playMusic(chillTheme) from _call_playMusic_113
    scene clothesshop with fade
    "Я убеждаюсь, что меня никто не видит, и выхожу."
    "Через пару минут Джессика возвращается, снова переодевшись."
    show jessica bashful with dissolve
    "...Она немного нервничает."
    show jessica bashful talk
    jessica.c "Давай... пропустим остальное... Но это платье я куплю."
    show jessica tease talk
    jessica.c "Кажется, тебе понравилось~ Может, даже чересчур~"
    show jessica tease
    mc.c "Ещё бы."
    scene black with fade
    "Мы немного неловко идём к кассе."
    "К моему облегчению, она не намекает, что я должен заплатить. Наверное, всё за счёт папиной карты."
    "Я смущённо краснею, когда мы выходим из магазина."
    $ location_town.showBackground()
    show jessica tease talk with dissolve
    jessica.c "С-спасибо, что сегодня сходил со мной по магазинам..."
    show jessica tease
    mc.c "Нет, это {b}тебе{/b} спасибо."
    show jessica bashful
    jessica.c "М-м~"
    show jessica tease talk
    jessica.c "Мне пора... типа... учиться или ещё что-нибудь..."
    show jessica tease
    mc.c "Думаю, мы оба знаем, что ты этого не сделаешь."
    show jessica smile talk 2
    jessica.c "Хе~"
    hide jessica with dissolve
    show jessica kiss with dissolve
    "Она нежно целует меня в щёку."
    hide jessica with dissolve
    show jessica joy with dissolve
    jessica.c "Пока-пока!"
    hide jessica with dissolve


    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaHEvent2(fromGallery):
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_114
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "О, это мой телефон. Звонок?"
    "Это Джессика. Сейчас редко кто звонит. Надеюсь, ничего не случилось."
    mc.c "Алло?"
    jessica.c "Привееет~ [mc.name]~"
    "Ну, теперь я спокоен — она всё такая же энергичная."
    mc.c "Привет, Джессика. Что случилось?"
    jessica.c "Ничегошеньки~ Чем занимаешься?"
    "На самом деле она застала меня в скучный момент. Чем я вообще занимаюсь дома, когда не в баре?"
    mc.c "Ой, э-э... Ничего особенного, дома сижу, занимаюсь бумажной работой."
    jessica.c "Идеально!"
    mc.c "Идеально?"
    jessica.c "Ага! Слушай, я тут недавно купила новые наряды. Отлично подойдут для фотографий, правда?"
    mc.c "О, конечно. Где хочешь? Ты упоминала, что хотела как-нибудь посниматься в аквариуме."
    jessica.c "Ну-у-у~ Может, как-нибудь потом. А я думала..."
    jessica.c "Может, поснимаемся у тебя? Мы будем одни, да?"
    jessica.c "Некоторые наряды будут немного... ну, ты понимаешь..."
    jessica.c "Скажем так: думаю, тебе тоже понравится~ Хе-хе~"
    "Вот это уже привлекло моё внимание. Она прекрасно это знает."
    mc.c "Ладно, звучит хорошо. Когда хочешь прийти?"
    jessica.c "Э-э, а можно сейчас?"
    "В голосе слышится лёгкое сомнение."
    mc.c "Ты уверена? Не прогуливаешь занятия?"
    jessica.c "..."
    jessica.c "Всё нормально~ Обещаю~"
    "Ну и девушка..."
    "Но я не собираюсь отказываться от такой возможности."
    mc.c "Если ты так говоришь, Джессика..."
    jessica.c "Ура! Ты лучший, [mc.name]!"
    mc.c "Я свободен когда угодно. Напишу тебе адрес."
    jessica.c "Хорошо! Спасибо! Пока-пока!"
    "Я кладу трубку."
    "Она ещё не была у меня. Как-то не случалось. Я отправляю ей адрес и жду."
    "Интересно, какие наряды она имеет в виду?"
    "Она относится к этому довольно серьёзно, но как-то странно."
    "Только мы вдвоём, телефон с камерой и любительские снимки по городу."
    "Если она и правда хочет добиться успеха, то могла бы нанять профессионала."
    "Либо я и правда такой классный фотограф, либо ей просто нравится проводить со мной время."
    "...Либо она ещё не догадалась об этом..."
    scene black with fade
    "Примерно через двадцать минут..."
    $ location_home.showBackground()
    "Звенит дверной звонок. Я иду к двери."
    call playMusic(funnyTheme) from _call_playMusic_115
    show jessica joy with dissolve
    jessica.c "Приве-е-ет~!"
    hide jessica with dissolve
    show jessica hug with dissolve
    "Она почти прыгает мне на руки, заодно задевая меня большой модной сумкой."
    "Она стройная, но довольно высокая, так что весит не так уж мало."
    mc.c "Уф."
    jessica.c "Ой~"
    mc.c "Добро пожаловать."
    jessica.c "Спасибо!"
    hide jessica with dissolve
    show jessica smile talk with dissolve
    jessica.c "Ну-у~ Вот это твоя квартира?"
    "Она с любопытством оглядывается, но я замечаю, как её лицо слегка меняется."
    show jessica neutral
    jessica.c "..."
    mc.c "Да, не богато, но мне подходит."
    show jessica bashful
    jessica.c "Э-э... понятно..."
    "Она явно не впечатлена. Интересно, какой у неё был дом?"
    mc.c "Не нравится?"
    show jessica bashful talk
    jessica.c "Я просто... удивлена. У тебя ведь свой бизнес, да?"
    jessica.c "Я думала... Ну, представляла себе что-то другое."
    show jessica bashful
    mc.c "Бизнес не настолько успешный. Все деньги, что зарабатываю, уходят обратно в него, чтобы платить сотрудникам и держаться на плаву."
    show jessica sad talk
    jessica.c "Чёрт, прости, я не хотела вести себя как стерва."
    jessica.c "Наверное, я всё ещё привыкаю к тому, как живут обычные люди..."
    jessica.c "Моё студенческое жильё тоже стало для меня большим сюрпризом... Прости."
    show jessica sad
    mc.c "Не извиняйся, всё нормально. Я не обиделся, правда."
    "Ну, самую малость обиделся. Но, думаю, она ничего плохого не имела в виду. Просто мы из разных миров."
    mc.c "Да ладно, здесь уютно. Есть всё необходимое. Кажется, сегодня даже вода из крана идёт."
    show jessica surprise
    jessica.c "...!"
    mc.c "...Шучу."
    jessica.c "..."
    show jessica joy
    jessica.c "О-о-о~ Ха-ха-ха!"
    "Я учусь поднимать ей настроение."
    mc.c "Ладно. Покажи, что принесла."
    "Она снова наклоняется к сумке."
    show jessica smile talk 2
    jessica.c "Ага! Купила их на днях, они {b}такие{/b} милые~"
    show jessica tease talk
    jessica.c "И ещё кое-что {b}посмелее{/b}~"
    show jessica tease
    mc.c "Звучит неплохо. Какой план?"
    show jessica thinking
    jessica.c "Думаю, можно посниматься где-нибудь. У тебя дома такой непринуждённый шик, знаешь?"
    mc.c "Не совсем, но звучит хорошо. Как скажешь."
    show jessica smile talk
    jessica.c "Ладно, сначала выберу наряд."
    show jessica smile
    mc.c "Можешь переодеться в ванной."
    show jessica tease talk
    jessica.c "Хм... Наверное, переоденусь здесь."
    jessica.c "Только пообещай не подглядывать."
    show jessica tease
    "Она подмигивает мне."
    mc.c "Конечно, не посмею."
    show jessica smile talk 2
    jessica.c "Посмотрим~ Будешь паинькой — может, получишь награду~"
    hide jessica with dissolve
    "Я сажусь за стол и отворачиваюсь, чтобы Джессика могла переодеться."
    "Уже жду свой маленький показ мод."
    "Теперь, когда мы наедине, всё кажется более интимным."
    "Кажется, за моей спиной перестали шуршать одеждой."
    jessica.c "Ладно! Первый наряд!"
    scene jessicahevent2i1 with fade
    pause
    "Милая комбинация свитера и платья. Чуть более консервативная, чем её обычная одежда, но такая же очаровательная."
    mc.c "О-о! Красиво!"
    jessica.c "Да, правда? Я просто {b}должна была{/b} это купить!"
    "Я уже приготовил телефон. Кажется, этот кадр можно делать сразу."
    mc.c "Замри, отличный кадр получится."
    jessica.c "Хорошо!"
    scene black with fade
    "Мы переходим от одного наряда к другому."
    "Мы долго фотографируем каждый наряд в нескольких позах. Джессика в каждом выглядит безупречно."
    "Дело не в одежде. Дело в модели."
    scene jessicahevent2i2 with fade
    pause
    "Где-то повседневно, где-то мило."
    "В любом случае образ ей идёт, и она умеет его подать."
    scene jessicahevent2i3 with fade
    pause
    "Она так легко носит всё, что ей надевает. Будто вещи специально для неё созданы. Идеальная рама для произведения искусства."
    "Настоящая модница."
    scene black with fade
    "Некоторые наряды становятся всё откровеннее, и в комнате делается жарковато."
    "Не хочу портить ей настроение, если она пришла только ради снимков. Но я не могу не возбуждаться."
    "Наконец, пока я отворачиваюсь..."
    jessica.c "Э-э, я готова, но этот наряд..."
    jessica.c "Ну... сам увидишь."
    mc.c "Что там такое?.."
    "Я поворачиваюсь."
    call playMusic(sexyTheme) from _call_playMusic_116
    scene jessicahevent2i4 with fade
    pause
    mc.c "Ничего себе!"
    "Она... просто сногсшибательна."
    "Особенно этот комплект... По сути, одно нижнее бельё. В леопардовый принт."
    mc.c "Леопардовый принт? Серьёзно?"
    jessica.c "А что? Я горжусь своим узором! И бельё милое!"
    "Милое — не то слово. Не должно бы сработать, но ей невероятно идёт."
    "Если расфокусировать взгляд, она совсем голая..."
    jessica.c "[mc.name]..."
    mc.c "Да?"
    jessica.c "Тебе опять нравится, что видишь?"
    mc.c "Конечно! Фотографии отлично получаются."
    jessica.c "Ой, [mc.name], я не про это."
    jessica.c "Я же вижу, что у тебя стоит."
    "Я смотрю вниз. Она права: я уже давно возбуждён, штаны вот-вот лопнут."
    mc.c "Э-э... Как ты там говоришь... «Ой»?"
    jessica.c "Хи-хи~ Всё нормально, [mc.name]... Думаю, фотографий уже достаточно."
    jessica.c "Кажется, мы закончили на высокой ноте. Это твой любимый снимок?"
    mc.c "Ага."
    "Я могу только промычать в ответ. Кажется, я вот-вот начну пускать слюни."
    jessica.c "Ладно. За такую хорошую работу надо с этим что-то сделать~"
    "Она подходит ко мне, пока я сажусь на кровать."
    image jessica blowjob start = Image("images/characters/jessica/hscenes/blowjob/start.webp")
    scene jessica blowjob start with fade
    pause
    jessica.c "Как ты так быстро возбуждаешься? Я, конечно, милая, но всё же..."
    mc.c "Ты не просто милая. Ты сногсшибательная."
    "Она мягко обхватывает основание моего члена, щекоча его пушистыми кончиками пальцев."
    "Она слегка встряхивает его."
    jessica.c "И что же мне теперь с этим делать~?"
    "Я уже не могу шутить, чтобы сбить настроение, поэтому просто откидываюсь и позволяю ей продолжить."
    image jessica blowjob part 1 = Movie(play="images/characters/jessica/hscenes/blowjob/part1.webm")
    show jessica blowjob part 1 with fade
    pause
    "Она удивляет меня: нежно приподнимает член и облизывает снизу."
    "С тёплым соблазнительным взглядом она медленно и нежно ласкает ствол языком."
    jessica.c "М-м-м~"
    "Её прохладный влажный нос слегка касается меня снизу, а горячее дыхание создаёт контраст."
    mc.c "Ничего себе... Джессика..."
    jessica.c "Он... такой большой~"
    "Медленные движения совсем не похожи на её обычный быстрый, энергичный характер. Невероятные ощущения и зрелище."
    "Но мы только начинаем."
    mc.c "...Можно предложить кое-что?"
    jessica.c "Муа~ Да?"
    mc.c "Лифчик тут, кажется, совсем лишний... Не совсем..."
    jessica.c "Ага~ Хочешь увидеть мою грудь?"
    mc.c "...Да..."
    jessica.c "Не стесняйся."
    "Она снимает лифчик и снова опускает голову к кончику моего члена."
    image jessica blowjob part 2 = Movie(play="images/characters/jessica/hscenes/blowjob/part2.webm")
    show jessica blowjob part 2 with fade
    pause
    "Она широко открывает рот и медленно опускается на головку, беря в рот несколько дюймов."
    jessica.c "А-а-а~"
    mc.c "Ох, чёрт~ Невероятно~"
    "Она чуть крепче обхватывает меня и медленно направляет глубже в горло."
    "Если она и правда удивлена моим размером, то справляется очень хорошо."
    jessica.c "М-м-а~ М-м-м~"
    "Она покрывает мой член слюной, скользя по нему языком из стороны в сторону."
    "Жар, давление, сам вид — всё потрясающе."
    image jessica blowjob part 3 = Movie(play="images/characters/jessica/hscenes/blowjob/part3.webm")
    show jessica blowjob part 3 with fade
    pause
    mc.c "Так хорошо~ Не останавливайся."
    jessica.c "М-м-м~"
    "Её голос слегка вибрирует вокруг моего члена, усиливая ощущения."
    "Её длинный изящный хвост радостно покачивается за спиной. Ей тоже нравится."
    "Её большая грудь слегка покачивается, пока она старается взять меня глубже."
    mc.c "Ты потрясающая."
    image jessica blowjob part 4 = Movie(play="images/characters/jessica/hscenes/blowjob/part4.webm")
    show jessica blowjob part 4 with fade
    pause
    "Вдруг она ускоряется."
    "Она поворачивает головой и берёт в рот почти весь мой член..."
    "Я чувствую, как головка упирается ей в заднюю стенку горла."
    mc.c "Ох, чёрт..."
    jessica.c "А-а~ М-м-м~~"
    "Она смотрит на меня снизу вверх с невероятно похотливым выражением."
    "Влажные звуки становятся всё громче и непристойнее."
    "Она очень умелая. В её взгляде — ожидание одобрения."
    mc.c "Чёрт~ Не останавливайся. Я сейчас кончу."
    image jessica blowjob part 5 = Movie(play="images/characters/jessica/hscenes/blowjob/part5.webm")
    show jessica blowjob part 5 with fade
    pause
    jessica.c "А-а~ Чёрт."
    jessica.c "Мне надо было вдохнуть."
    "Она энергично дрочит мне обеими руками."
    "Поворачивая запястьями, она высасывает из меня все силы."
    "Она смотрит на меня снизу вверх и довольно улыбается, видя моё выражение лица."
    jessica.c "Хе-хе~ Хорошо?"
    mc.c "Чёрт, Джессика, я почти..."
    jessica.c "Выпусти всё. Кончи мне на грудь, знаю, что хочешь."
    "От этих слов я срываюсь. Она крепко сжимает меня."
    image jessica blowjob end 1 = Image("images/characters/jessica/hscenes/blowjob/end1.webp")
    scene jessica blowjob end 1 with fadewhite
    pause
    "С последним сжатием я обильно кончаю ей на грудь."
    jessica.c "Ого~!"
    "Сперма всё не перестаёт литься. Меня трясёт от наслаждения."
    "Она несколько раз проводит рукой по члену, выжимая из меня последние капли."
    image jessica blowjob end 2= Image("images/characters/jessica/hscenes/blowjob/end2.webp")
    scene jessica blowjob end 2 with fade
    pause
    jessica.c "Ого, ничего себе~"
    "Её грудь полностью покрыта спермой."
    mc.c "Ничего себе... Боже мой..."
    jessica.c "Ага, да? Ты что, так долго терпел?"
    mc.c "Это было невероятно."
    "Мы оба тяжело дышим, пока сперма стекает по ней."
    "Джессика трогает несколько капель у себя на груди."
    jessica.c "Надо это вытереть..."
    "Она вытирается салфетками, которые лежат рядом."
    jessica.c "Дай мне привести себя в порядок и переодеться... Не хочу возвращаться в этом."
    mc.c "Ты всё это надела только ради меня?"
    jessica.c "Тсс, ты~"
    jessica.c "Может быть~"
    scene black with fade
    "Она приводит себя в порядок, возвращается переодеться в свой наряд и собирает вещи, которые принесла."
    "Теперь мне не нужно отворачиваться. Мы уже перешли этот этап."
    $ location_home.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_117
    show jessica smile with dissolve
    "Я возвращаю ей телефон, чтобы посмотреть, что получилось."
    "Она садится рядом и листает фотографии."
    show jessica smile talk
    jessica.c "О-о...!"
    show jessica smile talk 2
    jessica.c "Этот наряд хорошо получился..."
    show jessica smile
    "Она листает снимки с привычной улыбкой. Рад, что ей нравится."
    mc.c "Некоторые снимки получились довольно сексуальными. Будешь их выкладывать?"
    show jessica smile talk 2
    jessica.c "Что, ревнуешь?"
    show jessica smile
    mc.c "...Немного."
    show jessica smile talk
    jessica.c "Ой~ Как мило. Не переживай, выложу только пару обычных."
    show jessica tease talk
    jessica.c "Остальные оставлю только для тебя~"
    show jessica tease
    "Она ещё немного листает снимки, сидя совсем близко ко мне."
    show jessica joy
    jessica.c "Как всегда отлично, [mc.name]. Не понимаю, как у тебя получается."
    jessica.c "Спасибочки!"
    mc.c "Не за что. Скорее, это мне тебя благодарить."
    show jessica bashful
    jessica.c "М-м..."
    "Она смущённо и неодобрительно мычит, когда я напоминаю ей о том, что мы сделали."
    show jessica smile talk
    jessica.c "Мне... наверное... уже пора."
    jessica.c "Ты прав, я прогуляла занятие, чтобы прийти."
    show jessica mad talk
    jessica.c "Но оно {b}тааааакое{/b} скучное, ну правда."
    show jessica mad
    mc.c "Не задерживайся из-за меня."
    show jessica smile talk
    jessica.c "Эй, [mc.name]."
    show jessica smile
    mc.c "Да?"
    show jessica smile talk 2
    jessica.c "Ты был прав. Здесь уютно. Ты ведь ещё позовёшь меня?"
    show jessica smile
    mc.c "Конечно! Приходи когда захочешь."
    hide jessica with dissolve
    show jessica kiss with dissolve
    jessica.c "Муа~"
    show jessica hug with dissolve
    jessica.c "Скоро увидимся!"
    hide jessica with dissolve
    show jessica joy with dissolve
    jessica.c "Пока-пока!"
    hide jessica with dissolve
    "Я провожаю её до двери, в руках у неё большая сумка."
    "Она весело машет на прощание и вприпрыжку скрывается за углом."


    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaHEvent3(fromGallery):
    $ location_bar.showBackground()
    "Мне удалось сделать почти невероятное — вытащить Джессику в мой бар."
    "Ясно, что обычно ей больше нравятся модные заведения. Но иногда можно уговорить и её."
    "Приятно, что она проводит время со мной, грязным простолюдином. Наверное, я заслужил её благосклонность, помогая ей."
    call playMusic(funnyTheme) from _call_playMusic_118
    show jessica joy with dissolve
    jessica.c "Приве-е-ет~ Как дела~?"
    "Она всё такая же радостная и энергичная..."
    mc.c "Рад тебя видеть, Джессика."
    hide jessica with dissolve
    show jessica kiss with dissolve
    pause
    jessica.c "Муа~"
    hide jessica with dissolve
    show jessica smile talk with dissolve
    jessica.c "Что значит «рад меня видеть»? Ты сам меня пригласил, глупыш."
    show jessica smile
    jessica.c "Ну да, но вдруг ты не захочешь идти со мной в мою забегаловку..."
    show jessica mad talk
    jessica.c "Эй! Я не легкомысленная! Я же сказала, что приду..."
    show jessica mad
    "Она слегка хлопает меня по плечу."
    mc.c "Ха-ха, да-да, знаю. Всё равно рад, что пришла."
    show jessica smile talk 2
    jessica.c "Конечно, глупыш. Надо же радовать своего сотрудника."
    show jessica smile
    mc.c "Сотрудника... Значит, мне полагается зарплата за эту {i}ужасную{/i} изнурительную работу?"
    show jessica tease talk
    jessica.c "Не притворяйся, будто тебе не нравится. У нас полно доказательств."
    show jessica thinking
    jessica.c "Но я не очень понимаю, как это работает. Когда начнутся выплаты?"
    "Кажется, она, как всегда, немного наивно представляет себе карьеру модели. Но нам обоим весело."
    mc.c "Тогда с этим можно повременить. Зато есть другие приятные бонусы..."
    "Она снова легонько хлопает меня по спине."
    show jessica tease talk
    jessica.c "Боже мой! Перестань~"
    show jessica tease
    mc.c "Ладно, что тебе принести?"
    "Говорю так, но внутри уже тревожусь."
    "Она удивительно хорошо умеет выбирать самые дорогие напитки в баре, сама того не замечая."
    show jessica smile talk
    jessica.c "Хм, посмотрим..."
    jessica.c "Мне водку с содовой, и диетическую. Надо следить за весом."
    show jessica smile
    mc.c "Весом? Да брось, ты же худая как щепка."
    show jessica neutral talk
    jessica.c "Нет! Серьёзно! Вот, смотри!"
    show jessica neutral
    "Она пытается ущипнуть талию, где почти нечего щипать."
    mc.c "Что я должен увидеть?"
    show jessica neutral talk
    jessica.c "Жир! Вот же он!"
    show jessica neutral
    "Там ничего нет."
    mc.c "Пей что хочешь, но тебе {b}точно{/b} не грозят проблемы с весом."
    mc.c "Надеюсь, ты не собираешься стать анорексичной моделью..."
    show jessica bashful talk
    jessica.c "Фу, нет, это {i}так{/i} отвратительно. Такие девушки мне не нравятся."
    show jessica smile talk
    jessica.c "Просто хочу хорошо выглядеть. Тебе ведь это нравится."
    show jessica smile
    mc.c "Хм, да. Не жалуюсь. Хотя немного набрать вес тебе бы не повредило."
    show jessica surprise
    jessica.c "Боже мой, ты из тех парней, да?"
    mc.c "Ха! Не совсем... Просто ты в миллионе километров от любых проблем с весом. Ты в полном порядке. Просто великолепна."
    show jessica smile talk
    jessica.c "Ой... Я бы привыкла такое от тебя слышать~"
    scene black with fade
    "Я приношу нам напитки. Сегодня я здесь как спутник, так что могу не работать. Надеюсь, сотрудникам не понадобится моя помощь."
    "Вечер проходит за приятной беседой. Она рассказывает последние сплетни о подругах."
    "Похоже, она общается с девушками из похожих семей: обеспеченными, гламурными, модными... Порой это совсем другой мир."
    "Несмотря на разговоры о диете, она заказывает ещё несколько напитков."
    "Она совсем хрупкая, поэтому быстро слегка пьянеет."
    $ location_bar.showBackground()
    show jessica smile with dissolve
    mc.c "Кстати, Джессика, как идут дела со страницей в «Инстре»? Цифры растут?"
    show jessica smile talk 2
    jessica.c "Вполне! Почти каждый день появляется новый подписчик!"
    show jessica smile
    "Всё ещё не так много, но если её это радует, значит, она не такая уж оторванная от реальности, как иногда кажется."
    "Она достаёт телефон."
    show jessica smile talk 2
    jessica.c "Так... Сто шестьдесят два! А один снимок с последней съёмки {b}правда{/b} хорошо зашёл! Смотри!"
    show jessica smile
    "Она суёт телефон мне под нос. Это одна фотография с нашей последней съёмки у меня дома. Та, что разошлась..."
    "Я замечаю первые несколько комментариев."
    mc.c "«Сиськи-сиськи»..."
    show jessica joy
    jessica.c "А, это. Ха-ха! Эти ребята такие смешные! Там полно таких комментариев."
    "Теперь я понимаю, что мне не очень нравится, когда другие парни пялятся на мою девушку..."
    "Некоторые фотографии довольно откровенные. Знаю, в этом весь смысл, да и снимал их я сам, но всё же..."
    show jessica smile talk 2
    jessica.c "Ой, что такое? Ты о чём-то думаешь, прямо по лицу видно."
    show jessica smile
    mc.c "Я... Правда? Я ни о чём таком не думал..."
    show jessica tease talk
    jessica.c "Хе-хе~ Ты же {i}ревнуешь{/i}, да, [mc.name]?"
    jessica.c "Не переживай~"
    show jessica tease
    mc.c "Ревную? Э-э... Нет, всё нормально. Я понимаю, что это твоё дело..."
    "Неужели ревную? Похоже, да. Хочу, чтобы она была только моей..."
    show jessica joy
    jessica.c "Ха-ха-ха! Ой, ты такой милый сейчас! Посмотри на себя!"
    show jessica tease talk
    jessica.c "На, покажу кое-что~"
    show jessica tease
    "Она что-то нажимает в телефоне и разворачивает его ко мне. Это... личные сообщения. Похоже, из «Инстры»."
    "Там несколько непрочитанных сообщений."
    'fukmaster33' "Ты такая горячая, красотка. Ты в Нортвуде? Давай встретимся! Куплю тебе всё, что захочешь, будет классно."
    'fukmaster33' "Ответь, красотка, у меня отличный член, он тебе нужен. Если у тебя есть парень — брось его, я лучше."
    "Какой придурок..."
    mc.c "Тебе часто такое пишут?"
    show jessica smile talk
    jessica.c "Не, всего пару раз..."
    show jessica smile
    "Наверное, моё лицо сейчас перекошено. Даже если этот тип очевидный неудачник, мне всё равно неприятна сама мысль."
    "Надеюсь, она просто меня дразнит."
    show jessica tease talk
    jessica.c "Ой, [mc.name]~ Не волнуйся, я сразу их блокирую."
    show jessica thinking
    jessica.c "Или... может, он прав... Может, стоит?"
    mc.c "Ладно-ладно, понял. Это уже слишком..."
    show jessica smile talk
    jessica.c "Хе-хе~ Прости, [mc.name]~ Ты такой смешной."
    show jessica tease talk
    jessica.c "К тому же ты ещё не доказал, насколько ты хорош."
    call stopMusic from _call_stopMusic_20
    show jessica tease
    mc.c "А?"
    jessica.c "..."
    "Она просто улыбается мне. Лукаво, понимающе. Она намекает на то, о чём я думаю?"
    mc.c "Ты?.."
    show jessica tease talk
    jessica.c "Может, вернёмся к тебе домой~?"
    scene black with fade
    "Дорога домой проходит словно в тумане. Мы почти бегом возвращаемся ко мне."
    "Когда она это сказала, мне захотелось подхватить её на руки и выбежать оттуда."
    "Смеясь по дороге, мы заходим ко мне."
    call playMusic(sexyTheme) from _call_playMusic_119
    $ location_home.showBackground()
    show jessica kiss with dissolve
    jessica.c "М-м~ А-а~"
    "Мы сразу набрасываемся друг на друга: целуемся, обнимаемся, не можем оторваться."
    "Я глажу её стройное тело, ощущая шерсть под пальцами."
    "Провожу по её щеке и притягиваю лицо к своему, наши языки переплетаются."
    "Мы, спотыкаясь, добираемся до комнаты и падаем на диван."
    image jessica seated cowgirl start = Image("images/characters/jessica/hscenes/seatedCowgirl/start1.webp")
    scene jessica seated cowgirl start with fade
    pause
    jessica.c "Почему мы так долго тянули~?"
    mc.c "Не знаю. Теперь это кажется глупым, да?"
    jessica.c "Не могу ждать. Хочу тебя прямо сейчас~"
    "Она начинает расстёгивать мне ремень, сидя прямо на диване. Я хотел предложить кровать, но, похоже, мы останемся здесь."
    "Наконец она стягивает с меня штаны, я помогаю ей, скидывая их на пол. Она садится на меня верхом в соблазнительной позе."
    image jessica seated cowgirl start 2 = Image("images/characters/jessica/hscenes/seatedCowgirl/start2.webp")
    scene jessica seated cowgirl start 2 with fade
    pause
    "Джессика кончиками пальцев направляет мой член к своей киске, уже влажной от ожидания."
    jessica.c "Когда я вижу его вот так... не знаю, как с ним справиться~"
    mc.c "Для этого ты выбрала довольно подходящую позу... Но мы могли бы..."
    jessica.c "Нет, я хочу почувствовать его целиком..."
    image jessica seated cowgirl part 1 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part1.webm")
    show jessica seated cowgirl part 1 with fade
    pause
    jessica.c "М-м-м~ Ох, чёрт~"
    "Джессика опускается на мой член, придерживаясь за плечо."
    "Она мягко подпрыгивает, вдавливая меня в диван."
    jessica.c "А-а~ Так глубоко~"
    jessica.c "М-м-м~ М-м~"
    image jessica seated cowgirl part 2 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part2.webm")
    show jessica seated cowgirl part 2 with fade
    pause
    "Её стройные бёдра неожиданно мягко ударяются о мои."
    "Под моим руководством она принимает примерно половину моего члена, и я уже чувствую, как её киска сжимается."
    jessica.c "О-о-о~ Да-а~ [mc.name]~"
    jessica.c "Готов к большему? *Ах*"
    mc.c "Дай полюбоваться твоей красотой."
    "Джессика задирает рубашку и лифчик, обнажая упругую грудь."
    image jessica seated cowgirl part 3 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part3.webm")
    show jessica seated cowgirl part 3 with fade
    pause
    "Я направляю её за бёдра, и она резко опускается на меня, принимая мой член целиком."
    jessica.c "О-о-о~ Чёрт~ Да-а~"
    jessica.c "Боже мой~ А-а~"
    "Она вскрикивает от удовольствия с каждым толчком, а её киска пульсирует."
    jessica.c "Как же хорошо~ *Ах*"
    image jessica seated cowgirl part 4 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part4.webm")
    show jessica seated cowgirl part 4 with fade
    pause
    "Джессика шлёпает себя по попке и разводит ягодицы, скользя на мне вверх-вниз."
    "Её хвост яростно виляет и подрагивает с каждым стоном."
    jessica.c "М-м-м~ М-м-м~ О-о-о~"
    "Я крепко держу её за талию и зарываюсь пальцами в шерсть."
    "Я могу кончить в любой момент, и кажется, она тоже близко. Пора ускориться."
    image jessica seated cowgirl part 5 = Movie(play="images/characters/jessica/hscenes/seatedCowgirl/part5.webm")
    show jessica seated cowgirl part 5 with fade
    pause
    "Я крепко обхватываю её за талию и резко опускаю на свой член."
    jessica.c "А-а-а~ А-а~ А-а-а~ А-а-а-а~"
    jessica.c "[mc.name!u] [mc.name!u] [mc.name!u]~!"
    "Джессика хватает меня за запястья, чтобы удержаться, пока я резко двигаю её вверх-вниз."
    "Её грудь подпрыгивает перед моим лицом. Я чувствую, как она дрожит от восторга."
    jessica.c "М-м-м~ А-а-а~ Да-а~"
    "Напряжение нарастает, я вот-вот кончу. Из этой позы мне не выбраться."
    mc.c "Я сейчас..."
    jessica.c "КОНЧИ ДЛЯ МЕНЯ~"
    image jessica seated cowgirl end 1 = Image("images/characters/jessica/hscenes/seatedCowgirl/end1.webp")
    scene jessica seated cowgirl end 1 with fadewhite
    pause
    jessica.c "А-а-а~ А-а~ Фу-у~"
    "Джессика резко опускается на мой член и выжимает из меня огромную порцию спермы."
    "Я кончаю глубоко в ней, наполняя её киску так, что сперма начинает вытекать."
    "Джессика так крепко сжимает мои запястья, что становится больно. Она содрогается от экстаза."
    jessica.c "М-м-м~ М-м-м~ О-о~"
    image jessica seated cowgirl end 2 = Image("images/characters/jessica/hscenes/seatedCowgirl/end2.webp")
    scene jessica seated cowgirl end 2 with fade
    pause
    "Джессика скатывается с меня и, тяжело дыша, распластывается на диване."
    jessica.c "А-а~ Ха-а~ Ничего себе... Чёрт, [mc.name]~"
    jessica.c "Это было... очень интенсивно~"
    mc.c "Думаю, это целиком твоя заслуга. В такой позе я почти ничего не мог сделать."
    jessica.c "Кажется, не зря я тебя завела~"
    mc.c "Так вот к чему ты вела?"
    jessica.c "Может быть... Хе-хе~"
    "Мы лежим и переводим дыхание. Часть спермы вытекает из неё..."
    "Не могу не задуматься..."
    jessica.c "Кстати, не переживай. *Ах* Я принимаю таблетки."
    "Очень прямо... Но рад это слышать."
    mc.c "Значит, ты ожидала, что так случится?"
    jessica.c "Ну, это ведь должно было произойти? Ты давно уже не можешь сдерживаться, здоровяк."
    mc.c "Не могу отрицать..."
    call playMusic(chillTheme) from _call_playMusic_120
    scene black with fade
    "Мы наслаждаемся послевкусием, переживая этот миг вместе. Наш первый раз прошёл не совсем так, как я представлял, но было здорово."
    "Наконец мы приводим себя в порядок и отдыхаем на диване."
    $ location_home.showBackground()
    show jessica smile with dissolve
    mc.c "Кажется, ты уже протрезвела после сегодняшних напитков..."
    show jessica smile talk
    jessica.c "Надеюсь. Сегодня я неожиданно разошлась..."
    show jessica smile
    mc.c "Но было весело, да?"
    show jessica tease talk
    jessica.c "Очень~"
    hide jessica with dissolve
    show jessica kiss with dissolve
    pause
    jessica.c "М-м~"
    hide jessica with dissolve
    show jessica smile talk with dissolve
    jessica.c "Мне, наверное, пора домой, [mc.name]."
    show jessica smile
    mc.c "Уверена? Можешь остаться у меня."
    show jessica smile talk 2
    jessica.c "Это мило, но... Я вся грязная... В другой раз, ладно?"
    show jessica smile
    mc.c "Можешь принять душ здесь, но, конечно, как хочешь. Предложение остаётся."
    scene black with fade
    "Мы целуемся на прощание."
    "Обещаем скоро снова встретиться."

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaHEvent4(fromGallery):
    $ location_diner.showBackground()
    call playMusic(chillTheme) from _call_playMusic_121
    "Я пригласил Джессику поесть."
    "...В дешёвую, жирную и простую закусочную."
    "Вряд ли еда соответствует её изысканному вкусу, но она не жалуется. Она привыкла к высокому классу, но, к счастью, не избалованна."
    mc.c "Еда вкусная?"
    show jessica smile talk with dissolve
    jessica.c "Вполне. Я иногда тоже сюда захожу."
    show jessica smile
    mc.c "Наверное, не сравнится с твоими дорогими ресторанами."
    show jessica neutral talk
    jessica.c "Я не так часто туда хожу, как ты думаешь..."
    show jessica smile talk 2
    jessica.c "Но дома у нас отличная еда. Папа может достать всё, что угодно."
    show jessica smile
    mc.c "О, он хорошо готовит?"
    show jessica neutral talk
    jessica.c "Нет, я про поваров, которых он нанимает."
    show jessica neutral
    mc.c "Мог бы догадаться... Ну и глупец."
    show jessica mad
    jessica.c "Ну извини~ Я же не прошу об этом..."
    mc.c "Да я шучу. Хотя немного завидую: каждый вечер ресторанная еда. Ты ещё не пробовала мою ужасную стряпню."
    show jessica tease talk
    jessica.c "Хе-хе~ Не умеешь сам о себе позаботиться, [mc.name]? Нужна девушка, чтобы готовила?"
    show jessica tease
    mc.c "Уже набралась опыта? Какое у тебя фирменное блюдо?"
    jessica.c "..."
    show jessica bashful talk
    jessica.c "Мне сначала надо научиться..."
    show jessica smile talk
    jessica.c "Ладно, если хочешь, как-нибудь приходи ко мне..."
    call stopMusic from _call_stopMusic_21
    show jessica surprise
    "Она замолкает, на секунду задумывается и расширяет глаза, будто её осенило."
    jessica.c "Чёрт! Ты же не леопардоподобный! И даже не кошачьего вида!"
    "...Что?"
    mc.c "Верно подмечено, Джессика. И что это значит?"
    jessica.c "Я даже не подумала..."
    call playMusic(heartTheme) from _call_playMusic_122
    "Она меня тревожит..."
    mc.c "Что-то не так? Мне что, нужна шерсть или усы?"
    show jessica bashful
    jessica.c "Чёрт... Прости... Моя семья всегда..."
    show jessica bashful talk
    jessica.c "Они всегда хотели, чтобы я встречалась с леопардоподобным."
    jessica.c "Что-то про честь рода, чистоту или вроде того..."
    show jessica mad talk
    jessica.c "Я всегда говорила, что это чушь! Это же видовая дискриминация! Как это... видизм?"
    show jessica mad
    mc.c "Похоже, ты только сейчас вспомнила об этом предубеждении."
    show jessica bashful talk
    jessica.c "Ну... Да. Я никогда не придавала значения тому, что он говорил..."
    show jessica sad talk
    jessica.c "Поверь! Я никогда так не думала! Ни разу!"
    show jessica sad
    mc.c "Всё нормально, Джессика. Рад, что ты за меня заступаешься. Но проблема довольно серьёзная."
    show jessica bashful talk
    jessica.c "Я просто перестала рассказывать семье о таких вещах. До сих пор не говорю..."
    show jessica bashful
    mc.c "Значит, они обо мне не знают?"
    show jessica neutral talk
    jessica.c "Нет. Наверное, они пытаются подобрать мне кого-нибудь из своего «круга»..."
    jessica.c "Какого-нибудь заносчивого сына успешного делового партнёра папы..."
    show jessica bashful talk
    jessica.c "Давно о таком не слышала, но это может случиться..."
    show jessica bashful
    mc.c "Если это произойдёт... Ты бы?.."
    show jessica bashful talk
    jessica.c "Я... Не знаю, что бы сделала... Я, наверное, даже не знала бы этого парня..."
    jessica.c "Но мои родители..."
    show jessica bashful
    "Она выглядит расстроенной. Кажется, совсем забыла, что такое может случиться."
    "Значит, мы встречаемся достаточно долго, чтобы в уравнение вошли родители."
    "Мысль приятная, но после этого... Не знаю, есть ли у этих отношений будущее."
    mc.c "Не будем пока об этом переживать. Я рад, что ты так не думаешь."
    show jessica neutral talk
    jessica.c "Можем просто продолжать как сейчас?"
    show jessica neutral
    mc.c "Я ничего другого и не хочу. Не переживаю."
    call playMusic(funnyTheme) from _call_playMusic_123
    show jessica smile talk 2
    jessica.c "Всё равно мы и так собирались продолжать, просто я совсем забыла об этом... Хе-хе~"
    show jessica smile
    "Она снова улыбается."
    mc.c "Вот моя девочка."
    "Я успокаивающе глажу её по руке."
    "Но это действительно тревожит. Наверное, стоило ожидать, что некоторые антро так думают. Иначе как им удалось сохраниться?"
    "Сейчас не время об этом думать."
    mc.c "У нас есть дела поважнее — например, кто оплатит счёт?"
    show jessica neutral talk
    jessica.c "О, я могу... Погоди..."
    show jessica tease talk
    jessica.c "Ты же мужчина. Как можно заставлять девушку платить на свидании?"
    show jessica tease
    mc.c "Ну не знаю, с такой богачкой рядом я подумал, что она поделится своим состоянием..."
    show jessica smile talk 2
    jessica.c "Я бы {i}может быть{/i} и предложила, но раз ты так говоришь, придётся тебе платить~"
    show jessica smile
    "Я и так собирался заплатить. Так легко дразнить её из-за денег."
    mc.c "Ну ладно, моя леди... Посмотрим, хватит ли у меня медяков..."
    "Я притворно хмурюсь и жалобно вздыхаю."
    show jessica smile talk 2
    jessica.c "Не волнуйся, я придумаю, как тебя отблагодарить~ Награда такому джентльмену~"
    show jessica smile
    "Опять этот взгляд. Маленькая кокетка. Кажется, я понимаю, что она имеет в виду. Надеюсь..."
    mc.c "Правда? И где мне получить эту награду?"
    call stopMusic from _call_stopMusic_22
    show jessica tease talk
    jessica.c "Как насчёт... у тебя дома. Минут через пятнадцать?"
    show jessica tease
    mc.c "...Думаю, получится."
    scene black with fade
    "Я оплачиваю счёт, а Джессика прижимается ко мне, когда мы выходим и быстрым, нетерпеливым шагом направляемся домой."
    "Мы болтаем и флиртуем, но не можем дождаться, когда окажемся дома."
    $ location_home.showBackground()
    "Джессика сразу же скидывает туфли и плюхается на кровать."
    show jessica smile talk 2 with dissolve
    jessica.c "А-а... Удобная у тебя кровать~ Напоминает мою дома."
    show jessica smile talk
    jessica.c "Итак, мистер [mc.name], твоя награда... Ты можешь..."
    show jessica joy
    jessica.c "Сделать мне массаж!"
    "..."
    "Я не против, но вообще-то думал..."
    show jessica joy
    jessica.c "Ха-ха! Видел бы ты своё лицо, [mc.name]~"
    call playMusic(sexyTheme) from _call_playMusic_124
    "Она начинает раздеваться."
    show jessica tease talk
    jessica.c "Иди сюда~"
    scene black with fade
    "Я спешу к ней. Она манит меня на кровать, лёжа на спине."
    "Не могу устоять перед её соблазнительным лицом."
    image jessica makeout part 1 = Movie(play="images/characters/jessica/hscenes/makeout/part1.webm")
    show jessica makeout part 1 with fade
    pause
    "Джессика притягивает меня к себе для глубокого поцелуя, слегка впиваясь длинными когтями в мою обнажённую кожу."
    "Но страстный поцелуй с ней настолько приятен, что это того стоит."
    jessica.c "М-м-м~ [mc.name]~"
    "Её руки нежно скользят по моей коже. Я направляю её голову, положив ладонь на мягкую щёку."
    "Шёлковая шерсть под моим пальцем расходится, обнажая красивые пятнышки у её подрагивающих усов."
    jessica.c "А-а~ Муа~"
    image jessica makeout part 2 = Movie(play="images/characters/jessica/hscenes/makeout/part2.webm")
    show jessica makeout part 2 with fade
    pause
    "Я наклоняюсь, и мы перекатываемся. Джессика прижимается ко мне обнажённой грудью, её шерсть щекочет меня и пробегают мурашки."
    "Она полностью садится на меня, не разрывая объятий."
    "Я чувствую, как её хвост медленно виляет, пока моя рука обхватывает её округлую попку."
    jessica.c "М-м-м~ Хм~"
    "Её соски скользят по моей груди. Хочется сжать её и не отпускать, но впереди ещё кое-что."
    image jessica missionary start = Image("images/characters/jessica/hscenes/missionary/start.webp")
    show jessica missionary start with fade
    pause
    "Джессика ложится на спину, снимает бельё и открывается мне. Я уже твёрдый."
    jessica.c "Я готова~ Пожалуйста~"
    mc.c "Тебе не придётся просить дважды."
    jessica.c "И... не сдерживайся~"
    "Эти простые слова заводят меня ещё сильнее. Она уже мокрая и готова. Я не могу себя сдержать."
    image jessica missionary part 1 = Movie(play="images/characters/jessica/hscenes/missionary/part1.webm")
    show jessica missionary part 1 with fade
    pause
    "Я легко вхожу в неё и начинаю двигаться, прижимаясь к её приглашающим бёдрам."
    jessica.c "М-м-м~ Да~ [mc.name]~"
    "Она проводит рукой по телу, ощущая каждый глубокий толчок."
    "С каждым шлепком срывается стон."
    jessica.c "О-о~ А-а~ Фу-у~"
    jessica.c "Ещё~"
    image jessica missionary part 2 = Movie(play="images/characters/jessica/hscenes/missionary/part2.webm")
    show jessica missionary part 2 with fade
    pause
    "Я подхватываю её разведённые ноги и сильнее вхожу в её бёдра."
    "Складки её влажной киски поддаются, а член скользит всё глубже."
    jessica.c "А-а-а~ М-м~ Чёрт, да-а~"
    jessica.c "Он такой *Ах* большой~"
    "Она пытается заглушить голос сжатым кулаком, но полностью отдаётся удовольствию."
    "Её невероятно стройное, но соблазнительное тело извивается передо мной. Джессика смотрит мне прямо в глаза, полные желания."
    "Я могу дать ей больше..."
    mc.c "Дай попробую кое-что..."
    image jessica spooning part 1 = Movie(play="images/characters/jessica/hscenes/spooning/part1.webm")
    show jessica spooning part 1 with fade
    pause
    "Я переворачиваю Джессику на бок, обнимаю сзади и легко вхожу в неё."
    jessica.c "А-а-а~ М-м-м~ Так глубоко~"
    "Входя ещё глубже, я чувствую, как она напрягается и вздрагивает, когда я достигаю предела."
    "Я обхватываю её небольшую грудь, пока от моих резких толчков она подпрыгивает."
    "Её спина выгибается с каждым толчком. Пышная попка смягчает удары, но я глубоко проникаю в неё."
    jessica.c "А-а~ Да-а~ [mc.name], [mc.name]~"
    jessica.c "Так *ах* хорошо~"
    "Я прижимаюсь лицом к её шее, вдыхая сладкий запах шерсти и шёлковых волос."
    "Мне мало. Я теряю контроль."
    image jessica spooning part 2 = Movie(play="images/characters/jessica/hscenes/spooning/part2.webm")
    show jessica spooning part 2 with fade
    pause
    "Я поднимаю её ногу и из этой позы толкаюсь так быстро, как могу."
    jessica.c "А-а~ А-а-а~ М-м-м~ Чёрт~"
    "Мои толчки подбрасывают её на кровати, комнату наполняют шлепки влажной кожи и шерсти."
    jessica.c "О-о~ *Ах* Боже~ *Ах* мой~"
    jessica.c "ТРАХНИ МЕНЯ~"
    "Мы оба тяжело дышим. Я чувствую, как она сжимается вокруг меня. Долго я не продержусь."
    jessica.c "Кончай вместе со мной~ КОНЧАЙ СО МНОЙ~"
    image jessica spooning end 1 = Image("images/characters/jessica/hscenes/spooning/end1.webp")
    show jessica spooning end 1 with fadewhite
    pause
    "Её киска крепко сжимается, пока она содрогается от экстаза, вытягивая из меня всё."
    "Я изливаю в неё огромную порцию спермы, словно бесконечным потоком."
    jessica.c "А-а-а-а-а~"
    jessica.c "О-о~ А-а~ [mc.name]~ Так много~"
    "Мы ещё некоторое время остаёмся соединёнными, погружённые в наслаждение."
    "Сперма начинает вытекать из неё, и я наконец отстраняюсь, любуясь результатом."
    image jessica spooning end 2 = Image("images/characters/jessica/hscenes/spooning/end2.webp")
    show jessica spooning end 2 with fade
    pause
    "Из неё вытекает целая лужа спермы. Джессика приподнимается передо мной."
    jessica.c "*Ах* *Ах* Чёрт... [mc.name]~"
    jessica.c "Ты был таким диким~ *Ах* Ты наполнил меня~"
    mc.c "Я не сдерживался."
    scene jessicapillowtalk with fade
    pause
    call playMusic(heartTheme) from _call_playMusic_125
    "Джессика падает на спину, переводя дыхание."
    mc.c "Я не сдерживался."
    jessica.c "И не сдерживайся. *Ах* Боже, это было так хорошо~"
    "Она улыбается мне — тепло и с полным удовлетворением."
    "Мы отдыхаем, глядя друг другу в глаза."
    mc.c "Не собираешься опять убегать?"
    jessica.c "Теперь, когда я вспомнила, какая у тебя удобная кровать..."
    mc.c "Можешь остаться у меня на всю ночь, если хочешь."
    jessica.c "Правда?"
    mc.c "Конечно, хочу. Если только ты не хочешь, чтобы я сегодня замёрз и остался один..."
    jessica.c "Хе-хе~ Ладно, да, было бы здорово~"
    mc.c "После такого я не могу тебя отпустить. Останься со мной."
    scene black with fade
    "Мы приводим себя в порядок и готовимся провести первую ночь вместе."
    call jessicaSleepover from _call_jessicaSleepover
    "Джессика потягивается и переворачивается на живот."
    jessica.c "Спокойной ночи, [mc.name]."
    mc.c "Сладких снов."
    "Джессика быстро засыпает, и тихое мурлыканье её дыхания убаюкивает меня."

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaHEvent5(fromGallery):
    $ location_home.showBackground()
    "Накопилось полно дел по бару. Бумаги, счета, расписание, заявления на работу..."
    "Ну почему я всё это откладываю? Моя лень никуда не делась."
    "Как бы ни было скучно, надо закончить. Никаких отвлечений..."
    call playMusic(chillTheme) from _call_playMusic_126
    jessica.c "...А потом она подошла к ней и такая: «Что ты здесь делаешь?»"
    mc.c "Угу..."
    jessica.c "А она ей такая: «А ты {i}что{/i} здесь делаешь?» Представляешь? А потом знаешь, что она сказала?"
    mc.c "Угу..."
    jessica.c "А? Как думаешь?"
    mc.c "Ага."
    jessica.c "Ты меня не слушаешь!"
    image jessica couch feet idle = Movie(play="images/characters/jessica/events/hevent5/couchidle.webm")
    show jessica couch feet idle with fade
    pause
    "Во всяком случае, не сам себя отвлекаю. Ко мне заглянула моя болтушка и трещит без умолку."
    "Кажется, я отключился. Какие-то сплетни о её подругах."
    "Она просто заявилась после занятий — если вообще на них ходит..."
    "Я рад, что она здесь, но сразу предупредил: мне нужно поработать."
    mc.c "Ох, э-э... Прости. Я вообще не слушал."
    jessica.c "Ну же, [mc.name]..."
    mc.c "Прости, Джесс, мне надо наверстать дела. Ты говорила что-то важное?"
    jessica.c "Ещё бы! Драма между Эми и Фло — это главное!"
    mc.c "Ясно..."
    "Она развалилась на диване, листает телефон и болтает обо всём подряд."
    "Она бы меньше отвлекала, если бы я сейчас не видел её трусики под юбкой. И эти милые лапки направлены прямо на меня..."
    mc.c "Ладно, спрошу: что на тебе надето?"
    jessica.c "Что ты имеешь в виду? Я постоянно такое ношу."
    mc.c "Кажется, этих чулок я раньше не видел."
    jessica.c "А, они новые. Такие милые, да?"
    "Милые? Наверное. Выше колена, немного прозрачные... Может, даже соблазнительные."
    $ location_home.showBackground()
    "Чёрт, надо сосредоточиться. Некоторые дела срочные."
    "Пока Джессика листает телефон, я успеваю немного поработать. Она та ещё зависимая от соцсетей."
    jessica.c "А-а~ Скукотища~"
    show jessica smile talk with dissolve
    jessica.c "Ну давай, пойдём повеселимся~"
    show jessica smile
    "Джессика наваливается мне на плечи и заглядывает в экран."
    mc.c "Сейчас не могу, прости."
    show jessica tease talk
    jessica.c "Обязательно {i}именно сейчас{/i}? Что случится, если отложишь?"
    show jessica tease
    mc.c "Потеряю бар и быстро окажусь на улице."
    show jessica smile talk 2
    jessica.c "О-о~ Как усердно работаешь... Зачем тебе деньги? Я могу за всё заплатить~"
    show jessica smile
    mc.c "Не соблазняй меня таким заманчивым предложением..."
    mc.c "Нет, я должен сам всего добиться. К тому же это деньги твоего отца, не твои."
    show jessica tease talk
    jessica.c "А трачу я их как захочу~ Ну же~ Пойдём куда-нибудь!"
    show jessica tease
    mc.c "Прости, может, позже... Слишком много дел."
    show jessica mad talk
    jessica.c "Ну и скучный..."
    scene jessicahevent5i1 with fade
    pause
    "Джессика демонстративно садится мне на колени, окончательно мешая работать."
    jessica.c "Держу пари, ты бы предпочёл заниматься {i}чем угодно{/i}, только не этим~"
    mc.c "Конечно, но ничего не поделаешь..."
    "Джессика гладит меня по груди маленькой лапкой, рисуя кружки."
    "Её волосы касаются щеки, я чувствую запах духов и шерсть её стройной руки..."
    "Сейчас есть немало вещей, которыми я бы предпочёл заняться с ней."
    mc.c "Я рад, что ты здесь, просто..."
    jessica.c "Хе-хе~ Ладно, ворчун, не буду мешать~"
    scene black with fade
    "Джессика надувается, встаёт с моих колен и нарочито неспешно прогуливается по комнате."
    "После пары преувеличенных вздохов она снова подходит — теперь сзади."
    call playMusic(sexyTheme) from _call_playMusic_127
    scene jessicahevent5i2 with fade
    pause
    "Джессика каким-то образом протискивается между мной и спинкой кресла и обнимает меня. {i}Формально{/i}, теперь она мне не мешает."
    "Но ниже пояса уже назревает явное отвлечение."
    jessica.c "Так... Значит, тебе нравятся эти чулки?"
    "Она дразнит меня, проводя ступнями совсем рядом с пахом, всё ещё обнимая."
    mc.c "Просто любопытно."
    jessica.c "Слушай... Для моего инстаграма... Кажется, некоторым парням нравятся ступни..."
    jessica.c "Как думаешь~ Может, сделаешь несколько снимков для публикации~?"
    mc.c "Да эти парни, должно быть, настоящие извращенцы, ха-ха..."
    jessica.c "Эй~ Ты что, намекаешь, что у меня некрасивые лапки? Они тебе не нравятся~?"
    "Я начинаю потеть. Наверное, она всё понимает."
    mc.c "Нет... Я просто... работаю..."
    jessica.c "М-м-м~? Тогда что это такое?"
    "Она трётся ступнёй о мой полутвёрдый член, и я тут же вздрагиваю. Я попался."
    mc.c "Не знаю, о чём ты."
    jessica.c "Хе-хе~"
    image jessica chair footjob 1 = Movie(play="images/characters/jessica/hscenes/chairFootjob/part1.webm")
    show jessica chair footjob 1 with fade
    pause
    "Джессика ловко расстёгивает ширинку и достаёт мой член."
    "Обвив меня ногами сзади, она дразнит головку члена ступнями, и я чувствую под носками подушечки лап."
    jessica.c "Хе-хе~ Ну и извращенец, да?"
    mc.c "Ты меня поймала..."
    "Шёлковая ткань щекочет мой член, доводя его до полной твёрдости. Джессика держится за мою грудь."
    jessica.c "И зачем {i}кому-нибудь{/i} заводиться от такого, а?"
    mc.c "Справедливо..."
    jessica.c "Эй, почему ты перестал печатать? Я ведь больше не мешаю, да~?"
    mc.c "Ну же..."
    "Как будто я могу продолжать... Ощущения слишком сильные."
    jessica.c "Хм... Они новые, не хочу их испачкать~"
    jessica.c "А может..."
    image jessica chair footjob 2 = Movie(play="images/characters/jessica/hscenes/chairFootjob/part2.webm")
    show jessica chair footjob 2 with fade
    pause
    "Она быстро снимает носки и сжимает мой член между голыми ступнями."
    "Шёлковая шерсть щекочет ствол, скользя вверх-вниз и крепко сжимая."
    "Она заглядывает мне через плечо, прижимается подбородком и хихикает, глядя на результат."
    jessica.c "Хе-хе~ Что такое, [mc.name]? Если не будешь работать за компьютером, на что мы будем есть?"
    mc.c "Не совсем так..."
    jessica.c "Я тебе мешаю? Может, мне остановиться~?"
    "Ощущения невероятные. Её прикосновения щекочут головку, а подушечки лап крепко сжимают..."
    "Даже угроза остановиться... Я не выдержу."
    mc.c "Н-..."
    jessica.c "М-м~? Говори громче, [mc.name]."
    mc.c "Нет, не останавливайся..."
    jessica.c "Ну что скажешь?"
    mc.c "Пожалуйста, Джесс, так хорошо."
    jessica.c "Хе-хе~"
    image jessica chair footjob 3 = Movie(play="images/characters/jessica/hscenes/chairFootjob/part3.webm")
    show jessica chair footjob 3 with fade
    pause
    "Она ловко сжимает меня пальцами ног и умело водит ступнями вверх-вниз."
    "Немного предэякулята усиливает и без того невероятные ощущения."
    "Она прижимается к моей шее, целует и покусывает, вызывая дрожь по всему телу."
    jessica.c "М-м~ Хе-хе~"
    jessica.c "Если тебе нравится — скажи честно~"
    mc.c "Да... Обожаю."
    jessica.c "М-м~ Хочешь кончить? Прямо здесь? Всё запачкать?"
    mc.c "Мне всё равно, я уже не могу сдерживаться..."
    jessica.c "Хе-хе~ Хорошо~"
    jessica.c "М-м~ Выпусти всё~"
    "Прикосновения Джессики доводят меня до края."
    scene jessicachairfootjobfinish1 with fadewhite
    pause
    mc.c "А-а!"
    "Я теряю контроль, её хватка заставляет меня резко кончить, извергая всё до последней капли."
    jessica.c "Ничего себе~ Хе-хе~"
    scene jessicachairfootjobfinish2 with fade
    pause
    "Сперма разлетается повсюду, попадает на стол, на пол — бог знает куда ещё..."
    "Джессика шевелит испачканными спермой ступнями и наклоняется через моё плечо, прижимаясь щекой к моей."
    jessica.c "Вот это было весело~"
    mc.c "Чёрт... Ты ради этого пришла?"
    jessica.c "Нет, но нужно было как-то привлечь твоё внимание~"
    mc.c "Получилось... Чёрт."
    jessica.c "Ну и бардак~"
    mc.c "Я не против, но лучше убраться, пока клавиатура не пострадала..."
    "Я тянусь за салфетками и вытираю хотя бы то, что вижу."
    $ location_home.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_128
    show jessica tease with dissolve
    "Джессика спрыгивает со стула и самодовольно улыбается."
    show jessica tease talk
    jessica.c "Хе-хе~ Ты определённо из этих {i}извращенцев~{/i}"
    show jessica tease
    mc.c "Скажем так... Мне нравится женское тело во всех его проявлениях."
    show jessica smile talk 2
    jessica.c "Ладно, ладно, оставлю тебя с твоей {i}скучной работой{/i}~ А сама буду скучать..."
    show jessica smile
    mc.c "Я... вряд ли смогу ещё поработать... Не с тобой рядом."
    mc.c "Пойдём куда-нибудь..."
    show jessica joy
    jessica.c "Ура!"
    mc.c "Раз мой бар под угрозой, угощаешь ты."
    show jessica tease talk
    jessica.c "Хе-хе~ Ладно, ворчун. Позабочусь о тебе~"
    scene black with fade
    "Мы отправляемся вкусно поесть, а потом, как и следовало ожидать, идём за покупками."
    "Если подумать, невероятная девушка сделала мне футджоб и ещё оплатит свидание. Я попал в рай."
    "С работой разберусь в другой день..."

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaHEvent6(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_129
    $ location_beach.showBackground()
    "Сегодня прекрасный день. Просто чудесный."
    "Ни облачка, идеальная температура и лёгкий ветерок."
    "Совсем не хочется сидеть в душном баре. Хотя с летней верандой мы бы, наверное, озолотились..."
    "Повезло, у меня есть отличный повод выбраться."
    show jessica joy
    jessica.c "М-м-м~ Чувствуешь? В такой воздух у меня усы подрагивают~"
    "Из-за такой погоды Джессика {i}настояла{/i}, чтобы я сопровождал её на пляж."
    "И не только ради фотографий, хотя наверняка они тоже будут."
    show jessica smile talk 2
    jessica.c "Я быстро переоденусь. У меня кое-что новенькое на сегодня."
    show jessica tease talk
    jessica.c "Думаю, тебе понравится~"
    show jessica tease
    mc.c "Опять? Сколько тебе их вообще нужно?"
    show jessica smile talk 2
    jessica.c "Много не бывает! К тому же это коллекция нового сезона."
    show jessica smile
    mc.c "Разве пляжный сезон не длится всё лето?"
    show jessica tease talk
    jessica.c "Пф-ф, ты {i}совсем{/i} ничего не понимаешь, да?"
    show jessica tease
    jessica.c "Погоди, не думаю, что ты будешь жаловаться~"
    hide jessica with dissolve
    "Она с сумкой направляется к кабинкам для переодевания."
    "Фух, жара невыносимая. Хорошо, что мне достаточно снять рубашку."
    "..."
    "Через несколько минут кто-то слегка хлопает меня по плечу."
    jessica.c "[mc.name]!"
    "Я оборачиваюсь и поднимаю взгляд."
    scene jessicahevent6i1 with fade
    pause
    "Джессика принимает эффектную позу и гордо улыбается своему наряду."
    "Яркий зелёно-жёлтый цветочный принт. Высокие вырезы и низкая посадка на бёдрах."
    "Купальник идеально обтягивает её пышную грудь, которая эффектно выделяется на фоне узора."
    "Солнце сверкает на светлых прядях её шерсти."
    "Она выглядит великолепно и сама это знает."
    mc.c "Ого... Ничего себе."
    jessica.c "«Ничего себе» — и всё?"
    mc.c "Ты потрясающе выглядишь."
    jessica.c "Правда? Обожаю этот бренд, у меня теперь есть несколько их вещей~"
    scene jessicahevent6i2 with fade
    pause
    "Джессика садится рядом. Отсюда открывается прекрасный вид на её декольте..."
    jessica.c "М-м? Куда это ты смотришь?"
    mc.c "А-а, на швы... Качественно сшито, да?"
    "Она толкает меня локтем."
    jessica.c "Хм-хм~ Только лучшее~"
    mc.c "Сегодня будут эффектные фото?"
    jessica.c "Не-а... Это только для твоих глаз, хе-хе~"
    mc.c "...И всех остальных на пляже."
    jessica.c "Да-да, как скажешь."
    "Мы некоторое время сидим на солнце и болтаем."
    scene jessicahevent6i3 with fade
    pause
    "Наконец мы заходим в воду, плаваем и брызгаемся."
    "Кошки ведь не любят воду? Или это оскорбительно?"
    "Я любуюсь своей кошачьей красавицей... Её прекрасные пятна на длинном стройном теле блестят на солнце."
    "Поверить не могу, что я сейчас здесь."
    scene jessicahevent6i4 with fade
    pause
    "Вытершись, мы ещё немного загораем. Кажется, им не страшны солнечные ожоги. Повезло."
    "Настоящее блаженство: ветерок обдувает нас, а волны накатывают и отступают."
    "Она даже ненадолго отрывается от телефона... Невероятно."
    "Для такого гладкокожего, как я, уже слишком жарко."
    mc.c "Хочешь мороженого?"
    jessica.c "О-о, да, спасибо! Ты знаешь, что я люблю~"
    mc.c "Скоро вернусь."
    scene black with fade
    "Я иду к киоску. Вот это цены на мороженое... Чёрт."
    "Но сегодня без него не обойтись. Может, стоило выбрать другой бизнес?.."
    "Получив мороженое, я возвращаюсь к Джессике."
    call playMusic(madTheme) from _call_playMusic_130
    scene jessicahevent6i5 with fade
    pause
    "Подойдя, я замечаю рядом с ней двух парней. Кажется, они разговаривают."
    "Леопардоподобный и... может, ягуароподобный? Может, её знакомые?"
    "Подойдя поближе, я начинаю слышать их разговор."
    unknown2 "Давай, красотка, повеселимся."
    jessica.c "Как насчёт нет? Я..."
    unknown "Ты такая горячая... Тебе надо стать моделью или что-то вроде того."
    jessica.c "Э-э, я и так модель..."
    unknown "Серьёзно? Какой у тебя инстаграм? Давай познакомимся."
    jessica.c "Ни за что. Я здесь со своим парнем..."
    unknown2 "И что, он оставил такую красотку одну? Вот придурок."
    jessica.c "Красотку? Отвали..."
    "Теперь я уже рядом и вижу, что происходит."
    mc.c "Ну что, ребята? Вы знакомы с Джесс?"
    scene jessicahevent6i6 with fade
    pause
    unknown2 "А это ещё кто такой, доходяга?"
    jessica.c "[mc.name]!"
    jessica.c "Наконец-то. Эти придурки никак не отстанут."
    jessica.c "Мой парень уже здесь, так что проваливайте."
    "Они оба хмуро смотрят на меня."
    "Они немного выше меня, хотя довольно стройные — так часто выглядят представители небольших кошачьих видов."
    unknown "Чёртов {i}человек{/i}, серьёзно?"
    unknown2 "Какого чёрта..."
    unknown "Тебе и правда стоит встречаться с леопардом, красотка. Я-то знаю, как о тебе позаботиться."
    mc.c "Похоже, нам пора."
    "Парни хмурятся и переглядываются."
    unknown2 "Как хотите..."
    "Они уходят, наверняка уже высматривая следующую девушку, к которой можно подкатить."
    call playMusic(barTheme) from _call_playMusic_131
    scene jessicahevent6i7 with fade
    pause
    mc.c "Прости. Ты в порядке?"
    jessica.c "Пф-ф. Я умею обращаться с такими придурками, это постоянно случается."
    mc.c "А-а... Ты слишком хороша собой. Как мне тебя удержать?"
    jessica.c "Хе-хе~ Ну, это правда~ Но ты отлично справляешься, [mc.name]... Мне никто другой не нужен."
    jessica.c "Мне очень нравится мой маленький человек~"
    "Она искренне улыбается мне. Я готов ей поверить."
    "Мы доедаем мороженое. Я смотрю на часы. Мы здесь уже несколько часов. Не уверен, что ещё один слой крема от загара поможет."
    scene jessicahevent6i8 with fade
    pause
    jessica.c "Да, нам пора. Ты уже красный, как панда!"
    mc.c "Панды... А, точно, они же существуют."
    jessica.c "Спасибо, что сегодня пришёл со мной! И спас меня~"
    mc.c "Да пустяки... Настоящий альфа-самец."
    jessica.c "Как ты их отшил... Такой мужественный~"
    jessica.c "Дай только переодеться. Слушай..."
    call stopMusic from _call_stopMusic_23
    jessica.c "Мне может понадобиться небольшая {i}помощь~{/i}"
    "Я сглатываю. В её глазах появляется озорной, похотливый взгляд. Она не шутит."
    scene black with fade
    "Джессика берёт меня за руку, и мы вместе пробираемся к свободной кабинке."
    "К счастью, вокруг тихо..."
    call playMusic(sexyTheme) from _call_playMusic_132
    image jessica beach room sex 1 = Movie(play="images/characters/jessica/hscenes/beachroomSex/part1.webm")
    scene jessica beach room sex 1 with fade
    pause
    "Не раздумывая, Джессика стягивает с меня шорты и прижимает к стене кабинки."
    "Она ласкает мой член, доводя его до твёрдости, и тут же страстно целует меня."
    mc.c "Чёрт, Джесс, прямо здесь?"
    jessica.c "М-м~ Хе-хе~ М-м~ А почему нет?"
    jessica.c "Мы ведь можем вести себя тихо?"
    mc.c "Не знаю..."
    "Я крепко сжимаю её упругую попку, пока мы целуемся."
    jessica.c "То есть ты отказываешься?"
    "Как я могу отказаться?"
    mc.c "Нет..."
    "Джессика наклоняется к моему уху."
    jessica.c "Тогда трахни меня~"
    "Джессика спускает низ купальника, поворачивается и подставляет мне попку."
    image jessica beach room sex 2 = Movie(play="images/characters/jessica/hscenes/beachroomSex/part2.webm")
    scene jessica beach room sex 2 with fade
    pause
    "Я тут же вхожу в неё — от нетерпения она уже вся мокрая."
    jessica.c "М-м-м~ Ох, чёрт~"
    mc.c "Ох, чёрт, Джесс..."
    "Упираясь руками в стену, Джессика подаётся навстречу моим толчкам. Деревянные доски скрипят от напряжения."
    "Она тихонько вскрикивает и вздрагивает на моём члене."
    mc.c "Тише..."
    jessica.c "М-м~ Я стараюсь~ Ты слишком хорош~"
    "За занавеской слышен лишь шум волн, поблизости никого. Но в любой момент..."
    jessica.c "Это... М-м~ довольно весело~"
    mc.c "Ты часто так делаешь?"
    jessica.c "Никогда, но... Чёрт, просто трахни меня~"
    "Я нервничаю, но искушение слишком велико. Она такая приятная."
    image jessica beach room sex 3 = Movie(play="images/characters/jessica/hscenes/beachroomSex/part3.webm")
    scene jessica beach room sex 3 with fade
    pause
    "Я ускоряюсь. Крепко обхватив её стройную талию, резко толкаюсь в её упругую попку."
    "Мы всё сильнее стонем от удовольствия, в кабинке звучат влажные шлепки..."
    jessica.c "А-а~ А-а~ М-м-м~"
    mc.c "Чёрт... Я не могу... Остановиться..."
    mc.c "Нас же поймают..."
    "Она смотрит на меня с невероятно развратным видом, только сильнее меня заводя."
    jessica.c "Мне уже всё равно~ Трахни меня~ М-м-м~"
    "Она права. Мне тоже уже всё равно. Мне мало."
    jessica.c "Дай мне... увидеть тебя~"
    image jessica beach room sex 4 = Movie(play="images/characters/jessica/hscenes/beachroomSex/part4.webm")
    scene jessica beach room sex 4 with fade
    pause
    "Я вытаскиваю член, разворачиваю её и прижимаю к стене кабинки."
    "Подняв её ногу, я толкаюсь вверх, заставляя её подпрыгивать у стены."
    jessica.c "А-а~ А-а~ А-а-а~"
    "Она опирается на мои плечи и подпрыгивает в такт моим бёдрам, трущимся о её влажную, покрытую шерстью киску."
    mc.c "А-а... А-а... Чёрт..."
    "Не думал, что буду стонать, но когда приходится сдерживаться... Чёрт, это трудно."
    jessica.c "Ох, чёрт, ох, чёрт~~~"
    "Её небольшая грудь подпрыгивает, пока я отрываю её от пола и прижимаю к стене."
    "Нам уже всё равно, мы отдаёмся страсти до конца."
    jessica.c "Я кончаю, кончаю~"
    jessica.c "Кончи в меня, кончи в меня~"
    scene jessicabeachroomsexfinish1 with fadewhite
    pause
    jessica.c "М-м-м-м~~~!"
    "Двигая бёдрами, я изливаю в её киску одну порцию спермы за другой."
    "Джессика крепко сжимает меня, пока я глубоко наполняю её огромным количеством спермы."
    jessica.c "О-о-о~"
    "Мы остаёмся в объятиях, прижавшись к стене и тяжело дыша, а снаружи шумят волны."
    scene jessicabeachroomsexfinish2 with fade
    pause
    "Я медленно отстраняюсь и выхожу из неё. Из Джессики вытекает густая струя спермы."
    mc.c "Вот это да..."
    jessica.c "Чёрт~ А-а~ Это было так хорошо~"
    jessica.c "Кажется, в этот раз ты кончил побольше."
    mc.c "Может быть... Обстановка..."
    jessica.c "Заводит, да?"
    mc.c "Не хочу, чтобы это вошло в привычку, но чёрт..."
    mc.c "Во всём виноват купальник."
    jessica.c "Хе-хе~"
    scene black with fade
    "На этот раз я даю Джессике спокойно переодеться. Убедившись, что вокруг никого, мы выходим из кабинки."
    "Теперь скрываться, наверное, бессмысленно. Если бы кто-нибудь вошёл в соседнюю кабинку, было бы совершенно ясно, чем мы занимались."
    $ location_beach.showBackground()
    show jessica tease with dissolve
    jessica.c "Хе-хе-хе~"
    "Джессика хихикает, и мы уходим, всё ещё красные от смущения."
    mc.c "Чёрт... Ты сумасшедшая."
    show jessica tease talk
    jessica.c "А ты, похоже, был не против~"
    show jessica tease
    mc.c "Ещё бы, но, боже..."
    mc.c "Пойдём отсюда."
    jessica.c "Хе-хе~"
    scene black with fade
    "Поднимаясь по песку, я смотрю вдаль."
    "Те два парня ссорятся с группой медведей, которые на них кричат. Так им и надо."

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return

label jessicaLikeEvent4Invitation(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_133
    show jessica smile
    "Ох, Джессика... Я окончательно влюблён."
    "После нашего внезапного признания во время поездки она стала ещё {i}ласковее{/i}."
    "Внезапным оно было лишь потому, что мы оба слишком долго не решались сказать об этом."
    "Наш разговор застал её врасплох, но могу сказать за нас обоих: это ощущалось совершенно правильно."
    "Мы проводим вместе уйму времени — от шикарных свиданий до простого отдыха дома."
    "Я очень счастлив с ней и уверен, что она со мной тоже."
    "Она жизнерадостная, весёлая, милая и любящая... Кажется, ей нравится новая жизнь вдали от дома."
    "Беззаботная студенческая жизнь, свобода делать что хочется. Учится она, конечно, не слишком много."
    "Не думаю, что ей чего-то не хватает. С деньгами у неё тоже всё в порядке. Вряд ли ей когда-нибудь придётся нуждаться."
    "Так что просьба будет чисто эгоистичной, но..."
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Да!' if(homeHasRoom) else "Нужно улучшить дом"
    if(not fromGallery):
        menu:
            "Может, предложить Джессике переехать ко мне? Это можно решить в любой момент."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "«Пока нет»":
                call endCharacterInteraction(jessica) from _call_endCharacterInteraction_2
    "У неё есть студенческое жильё, но она всё равно регулярно остаётся у меня и проводит здесь время."
    "Почему бы не сделать наши отношения серьёзнее? Я бы хотел, чтобы она жила со мной."
    mc.c "Слушай, Джесс."
    show jessica smile talk 2
    jessica.c "Да~?"
    show jessica smile
    mc.c "Как тебе студенческое жильё? Нравится?"
    show jessica smile talk 2
    jessica.c "Да! Классно!"
    show jessica smile talk
    jessica.c "Девушки милые. Я не со {i}всеми{/i} прямо подружилась, но они классные."
    show jessica smile
    mc.c "Ты ведь специально хотела жить с соседками?"
    show jessica smile talk 2
    jessica.c "Да. Мама с папой хотели оплатить целую квартиру, но я уговорила их не делать этого."
    show jessica neutral talk
    jessica.c "У меня нет братьев и сестёр, и я немного устала от большого пустого дома..."
    show jessica smile talk
    jessica.c "Я хотела пожить со сверстниками. Думала, будет весело!"
    show jessica neutral talk
    jessica.c "Хотя иногда бывает... Тяжеловато, понимаешь?"
    show jessica neutral
    mc.c "Тяжеловато?"
    show jessica bashful talk
    jessica.c "Ну, дом не очень хороший... Немного разваливается."
    jessica.c "А девушки бывают довольно неряшливыми... И убираться приходится самим."
    show jessica bashful
    mc.c "Студентам не полагаются уборщики, богатенькая."
    show jessica tease talk
    jessica.c "Отстань~"
    show jessica smile talk 2
    jessica.c "Да, сначала к некоторым вещам было трудно привыкнуть..."
    jessica.c "Но я привыкла."
    show jessica smile
    mc.c "А что насчёт договора?"
    show jessica neutral talk
    jessica.c "Какого?"
    show jessica neutral
    mc.c "Например, краткосрочная аренда? На двенадцать месяцев или помесячно? Частное жильё или от колледжа? Что-нибудь такое?"
    show jessica thinking
    jessica.c "Хм..."
    show jessica joy
    jessica.c "Не знаю!"
    show jessica smile talk 2
    jessica.c "Я ничего такого не знаю~"
    show jessica smile
    mc.c "Дай угадаю..."
    show jessica joy
    jessica.c "Папа всё устроил и просто сказал, куда идти!"
    mc.c "Ну конечно..."
    call playMusic(heartTheme) from _call_playMusic_134
    show jessica tease talk
    jessica.c "Зачем ты задаёшь столько вопросов~? М-м~?"
    show jessica tease
    "Хм... Похоже, она всё понимает и ждёт от меня чего-то..."
    "Она меня раскусила? Может, догадалась, что я собираюсь сказать."
    mc.c "Я спрашиваю, потому что..."
    show jessica tease talk
    jessica.c "Ты хочешь мне что-то сказать~?"
    show jessica tease
    "Она улыбается, и её сияющие глаза блестят ещё ярче."
    "Она наклоняется ближе, с каждой секундой всё самодовольнее."
    mc.c "Я подумал... Может, ты захочешь переехать ко мне."
    show jessica joy
    jessica.c "А-а-а~!"
    hide jessica with dissolve
    show jessica hug with dissolve
    "Она радостно визжит и бросается мне на шею."
    jessica.c "Ты сказал! Ты сказал~!"
    mc.c "Джесс?"
    show jessica kiss with dissolve
    jessica.c "М-м~!"
    show jessica hug with dissolve
    jessica.c "Я ждала, когда ты это предложишь!"
    mc.c "Правда?"
    jessica.c "Я уже целую вечность тебе намекала~!"
    jessica.c "И ты не замечал?"
    "Иногда тонкие женские намёки проходят мимо меня..."
    mc.c "Я... Похоже, нет."
    hide jessica with dissolve
    show jessica smile with dissolve
    mc.c "Просто уточню: это согласие?"
    show jessica joy
    jessica.c "Хе-хе~ {i}Конечно{/i}, глупыш!"
    mc.c "Слава богу!"
    show jessica tease talk
    jessica.c "Хе-хе~ Посмотри на себя, весь разволновался!"
    jessica.c "Думал, я откажусь?"
    show jessica tease
    mc.c "Кто знает... Может, тебе и там хорошо."
    show jessica tease talk
    jessica.c "Конечно, я хочу быть с тобой..."
    show jessica tease
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Просто напоминаю: [len(girlsAlreadyMovedIn)] других девушек уже почти живут у меня, хотя ты, возможно, ещё не со всеми познакомилась..."
        if(grace.movedIn and graceJessicaDuoStoryEvent1.unlocked):
            mc.c "Грейс, может, уже рассказывала тебе об этом."
            show jessica joy
            jessica.c "Да! Она всегда говорит о тебе, когда мы болтаем."
        if(zoe.movedIn and zoeJessicaDuoStoryEvent1.unlocked):
            mc.c "Зои уже переехала. Вы с ней проводили время вместе."
            show jessica tease talk
            jessica.c "О да, и чем вы там занимаетесь~"
            show jessica tease
        mc.c "Тебя это... устраивает?"
        show jessica joy
        jessica.c "Ага!"
        show jessica joy
    mc.c "А как же твои соседки?"
    show jessica smile talk 2
    jessica.c "Я всё равно буду с ними видеться! Я и так часто бываю у тебя~"
    show jessica smile
    mc.c "А договор аренды? Не знаю, можно ли просто съехать."
    show jessica thinking
    jessica.c "..."
    show jessica joy
    jessica.c "Да ладно, всё устроится! Уверена, папа продолжит платить~"
    mc.c "Наверное... Не спрашивай — и не придётся объяснять."
    scene black with fade
    "Мы ещё немного обсуждаем детали. Всё довольно просто."
    "Она соберёт вещи, а через несколько дней я помогу перевезти их сюда. К её вещам, которые уже у меня, добавится ещё немного."
    "Договорились. Не забудь внести в расписание!"

    return

label jessicaLikeEvent4(fromGallery):
    scene black with fade
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Хм?.."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Телефон..."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    $ location_home_bedroom.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_135
    "Телефон без умолку вибрирует. Я только наполовину проснулся. Что случилось так рано?"
    "Я включаю экран — там целая стена уведомлений."
    jessica.c "[mc.name!l][mc.name!l][mc.name!l]"
    jessica.c "сегодня сегодня!"
    jessica.c "приезжай приезжай приезжай приезжай!"
    "Это было бы тревожно, если бы я не знал контекст."
    "Сегодня я обещал заехать за Джессикой и помочь ей переехать."
    "Она и правда переезжает... И, судя по всему, очень этому рада. Вчера вечером она долго звонила мне, пока собирала вещи."
    "Я, конечно, тоже рад. Эта чудесная девушка будет жить у меня. Как же мне повезло."
    "Не думал, что она встанет так рано. Пора ехать. Напишу ей."
    scene black with fade
    "Недолгая поездка, телефон время от времени вибрирует..."
    scene suburbs with fade
    "Я приезжаю и, честное слово, вижу лицо Джессики, прижатое к окну дома."
    show jessica joy with dissolve
    "Она вылетает из входной двери и бросается ко мне, едва я выхожу из машины."
    jessica.c "[mc.name]~!"
    show jessica hug with dissolve
    "...И прыгает в мои объятия."
    jessica.c "Хе-хе~ Боже мой~!"
    jessica.c "Мы правда это делаем! Уии~!"
    show jessica kiss with dissolve
    jessica.c "М-м~"
    "Она обнимает меня и осыпает поцелуями."
    show jessica hug with dissolve
    mc.c "Сегодня что-то особенное?"
    jessica.c "Не притворяйся. Хе-хе~!"
    jessica.c "Я всё собрала! Поехали, скорее!"
    mc.c "С удовольствием."
    scene black with fade
    "Я помогаю отнести к машине несколько сумок, в том числе пару подозрительно набитых чемоданов."
    "Кажется, места для одежды у меня маловато..."
    $ location_home_bedroom.showBackground()
    "Мы приезжаем домой и заносим первые сумки в прихожую."
    "Бросив их на пол, Джессика мчится в спальню и прыгает на кровать."
    scene jessicalikeevent4i1 with fade
    pause
    jessica.c "Хе-хе-хе~"
    jessica.c "Наша кровать~"
    "Она сразу чувствует себя как дома. Иного я и не ожидал."
    "Она катается по кровати, болтая ногами и утыкаясь лицом в простыни."
    mc.c "Метки территорию ставишь?"
    jessica.c "Хе-хе~ Может быть~"
    mc.c "Хочешь занести остальные сумки?"
    jessica.c "Потом~ Я просто хочу..."
    jessica.c "Иди сюда~"
    call playMusic(heartTheme) from _call_playMusic_136
    scene jessicalikeevent4i2 with fade
    pause
    "Она поворачивается и манит меня. Я подхожу и нависаю над ней на кровати."
    "Она поднимает на меня сияющий взгляд и притягивает к себе за талию."
    mc.c "Добро пожаловать домой."
    jessica.c "Я дома, любимый~"
    "«Любимый»? Боже, как красиво..."
    mc.c "Для тебя это... неожиданно старомодно."
    jessica.c "Хе-хе~ Я думала об этом... Мама иногда так называет папу."
    jessica.c "Мне это всегда нравилось... И я подумала, теперь, когда мы {i}по-настоящему{/i} вместе..."
    mc.c "Мне нравится."
    jessica.c "Я люблю тебя~"
    scene jessicalikeevent4i3 with fade
    pause
    "Я наклоняюсь и целую её."
    "Её мягкая шерсть касается моего лица, усы щекочут щёки."
    "Мы долго не размыкаем страстных объятий, целуемся легко и глубоко."
    scene jessicalikeevent4i2 with fade
    pause
    "Наконец мы отстраняемся и смеёмся."
    jessica.c "Чем займёмся?"
    mc.c "Надо занести остальные сумки... Не хочу оставлять их в машине."
    jessica.c "Эх~ Ладно..."
    jessica.c "О! Надо найти место для моей одежды!"
    mc.c "Я этого и боялся."
    jessica.c "Да ладно~ Уверена, ты найдёшь место~"
    scene jessicalikeevent4i4 with fade
    pause
    "Забрав последние сумки, Джесс сразу принимается разбирать самое необходимое."
    "То есть наряды..."
    "Достав несколько вещей, она тут же хочет показать мне что-то новое, а потом отвлекается на очередную вещь и переодевается."
    "Заняв последние свободные вешалки, она сортирует одежду и убирает её везде, где находится место."
    mc.c "Похоже, придётся купить ещё один шкаф."
    scene jessicalikeevent4i5 with fade
    pause
    jessica.c "Не думала, что у тебя так мало места! Как ты вообще так живёшь?"
    mc.c "Очень просто, если тебе всё равно, как ты одеваешься."
    mc.c "Тогда возникает вопрос: как мне удалось заполучить такую красивую девушку?"
    jessica.c "Пришлось немного прикусить язык... Хе-хе~"
    jessica.c "Для начала надо избавиться от этой рубашки. Пойдём за покупками~"
    scene black with fade
    "Распаковка и прочие шалости занимают у нас остаток дня."
    "Но в конце концов она обустраивается."
    "Теперь мы и правда живём {i}вместе{/i}."

    if(not fromGallery):
        $ jessica.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label jessicaHEvent7(fromGallery):
    scene homehallway with fade
    "Я привыкаю к тому, что дома теперь больше народу."
    "Даже начинаю узнавать по деревянному полу характерный топот лап каждой девушки."
    "Кажется, в коридоре прошла Джессика. Похоже, она зашла в ванную."
    "Слышу, как включается душ. И дверь определённо приоткрыта."
    "Хм..."
    scene jessicashowerapproach with fade
    pause
    "Я не ошибся. Эти упругие шаги ни с чем не перепутаешь."
    "Она поворачивается ко мне спиной и намыливается под душем, покачивая милой попкой."
    "Она не будет против, если я составлю ей компанию..."
    scene jessicashowerapproach2 with fade
    pause
    "Я тихо приоткрываю дверь и захожу, но её уши тут же поднимаются, и она замечает меня."
    jessica.c "[mc.name]~!"
    mc.c "Э-э... Привет."
    jessica.c "Чего ждёшь? Хочешь ко мне присоединиться~?"
    "И это вообще вопрос?"
    mc.c "Ещё как."
    jessica.c "Давай! Потрёшь мне спинку~"
    image jessica shower caressing = Movie(play="images/characters/jessica/hscenes/shower/caressing.webm")
    show jessica shower caressing with fade
    pause
    "Она улыбается, пока я раздеваюсь и захожу внутрь."
    "Подойдя сзади, я обнимаю её, погружая руки в мокрую шерсть."
    jessica.c "Хе-хе~ Надо было просто попросить~"
    jessica.c "Мне бы хотелось немного компании~"
    mc.c "Учту..."
    "Я медленно глажу её гладкое стройное тело."
    "Такая стройная и хрупкая... Но при этом с чудесными мягкими формами, за которые хочется держаться..."
    "Шёлковые пряди шерсти расходятся под пальцами, капли воды разлетаются, когда шерсть расправляется обратно."
    jessica.c "Кажется, я просила спинку~"
    mc.c "Раз уж я здесь, вымою тебя целиком."
    jessica.c "Хе-хе~"
    "Она довольно быстро освоилась в новом доме."
    "У неё всё ещё есть студенческое жильё, но каждую ночь она возвращается сюда. Теперь это её дом."
    mc.c "Тебе здесь нравится?"
    jessica.c "Конечно! А почему нет?"
    jessica.c "Я уже давно ждала приглашения~"
    mc.c "Прости... Я не знал, может, ты хотела там остаться..."
    jessica.c "Ты слишком много думаешь, {i}любимый~{/i}"
    "Каждый раз, когда слышу это от неё, у меня замирает сердце. Так мило..."
    jessica.c "Но... Нам кое-что понадобится."
    mc.c "Например?"
    jessica.c "Ещё место в комоде? Когда выйдет новая коллекция~"
    mc.c "Для одежды..."
    jessica.c "Именно! И для твоей тоже. Надо вместе сходить по магазинам."
    mc.c "Если за твой счёт."
    jessica.c "Хе-хе~ Конечно!"
    "Её гладкое, сексуальное тело прижимается ко мне... Я начинаю заводиться."
    "Её виляющий хвост щекочет мою обнажённую грудь, и по спине пробегает дрожь."
    "А я всё сильнее {i}выпячиваюсь{/i}, и это становится заметно."
    jessica.c "[mc.name]~ Ты о чём-то думаешь~?"
    mc.c "Конечно. Ты же меня знаешь..."
    jessica.c "Ну и ну, а я думала, мы вместе принимаем романтичный душ..."
    mc.c "Прости..."
    jessica.c "Но погоди, я кое-что придумала~"
    image jessica shower tailjob 1 = Movie(play="images/characters/jessica/hscenes/shower/tailjob/part1.webm")
    show jessica shower tailjob 1 with fade
    pause
    "Не поворачиваясь, она ведёт хвостом по моей груди к бёдрам и проводит кончиком по головке моего члена."
    "Я быстро возбуждаюсь, и она мягко обвивает член хвостом, начиная водить им вверх-вниз."
    mc.c "Ничего себе... Ты так умеешь?"
    jessica.c "А почему нет?"
    mc.c "А я и не знал, что у тебя такой талант..."
    "Джесс оглядывается через плечо и самодовольно улыбается."
    jessica.c "Что, тебе нравится мой хвост~?"
    mc.c "Ты мне вся нравишься."
    jessica.c "Как мило... Вроде бы."
    "Она слегка сжимает хвост вокруг моего члена и медленно водит им вверх-вниз — ощущения невероятные."
    mc.c "Ох, чёрт..."
    jessica.c "Хе-хе~ Хорошо, да? Ну тогда~"
    image jessica shower tailjob 2 = Movie(play="images/characters/jessica/hscenes/shower/tailjob/part2.webm")
    show jessica shower tailjob 2 with fade
    pause
    "Она крепче обхватывает меня и ускоряется, умело укутывая мой член тёплым хвостом."
    mc.c "Боже..."
    "Она водит им вверх-вниз, мокрая шерсть скользит по стволу. Ни на что не похоже."
    jessica.c "Боже, какое у тебя лицо~"
    jessica.c "Ну ты и извращенец~"
    mc.c "Ты сама начала дрочить мне хвостом... Это твоя вина."
    jessica.c "Ладно, тогда перестану~"
    mc.c "Н-нет... Я..."
    jessica.c "Хе-хе, кончить собрался~?"
    "Хвост крепко сжимает меня и щекочет головку."
    mc.c "Чёрт, я..."
    jessica.c "Выпусти всё, {i}любимый{/i}~ Кончи мне на попку~"
    scene jessicashowertailjobfinish1 with fadewhite
    pause
    "В середине толчка я сжимаюсь и изливаю сперму ей на спину и попку."
    jessica.c "О-о~"
    "Её движения замедляются, пока я продолжаю пачкать её тело спермой, дрожа от удовольствия."
    scene jessicashowertailjobfinish2 with fade
    pause
    mc.c "Ха-а..."
    jessica.c "Хе-хе~ Хороший мальчик~"
    "Вода смывает сперму, и густые капли стекают по шерсти и хвосту."
    mc.c "Ты задала опасный прецедент, Джесс..."
    jessica.c "О нет~ И что же мне делать~?"
    scene black with fade
    "Мы ещё немного остаёмся под душем и как следует моем друг друга."
    "По-моему, всё ещё романтично."

    if(not fromGallery):
        $ jessica.addLove(1)

    return

label jessicaLikeEvent5(fromGallery):
    $ location_home_bedroom.showBackground()
    "Хм... Растянулся на диване. Ещё одни ленивые выходные..."
    if(dayOfWeek not in ['Saturday', 'Sunday']):
        "Я проверяю телефон. Сегодня [dayOfWeek], [mc.name]. Вот чёрт."
    "Вот в чём плюс быть начальником... Можно отдыхать в любой день недели."
    "Особенно приятно, когда кто-то другой вкалывает без передышки."
    call playMusic(funnyTheme) from _call_playMusic_137
    show jessica neutral with dissolve
    "Джессика в комнате. Мы просто отдыхали, но она вспомнила, что ей нужно сделать несколько заданий, и я разрешил ей воспользоваться компьютером."
    "Если подумать, я {b}вообще{/b} впервые вижу, как она занимается..."
    show jessica thinking
    jessica.c "Э-э~?"
    "Я говорю «усердно работает», но отсюда не похоже, что она много делает."
    "Пару минут постучит по клавишам и пощёлкает мышкой, а потом начинает отвлекаться."
    show jessica bashful
    jessica.c "Хмф..."
    "Она ещё и злится на меня за то, что я забрал у неё телефон, чтобы она сосредоточилась."
    mc.c "Что такое?"
    show jessica bashful talk
    jessica.c "Не понимаю~"
    show jessica bashful
    mc.c "Чего именно?"
    show jessica bashful talk
    jessica.c "Хм... Предельный... микро... какой-то... анализ... чего-то..."
    show jessica bashful
    "...Понятно."
    mc.c "Я так и не получил от тебя внятного ответа: на кого ты вообще учишься?"
    show jessica thinking
    jessica.c "Это... что-то вроде... каких-то там исследований..."
    show jessica smile talk 2
    jessica.c "Я никогда не запоминаю, да и какая разница. Главное — я знаю расписание занятий!"
    show jessica smile
    mc.c "По твоему бормотанию я понял, что, по крайней мере, сейчас ты занимаешься чем-то из области экономики."
    show jessica neutral talk
    jessica.c "Может быть. Тут повсюду знаки доллара."
    show jessica neutral
    "«Может быть»... Господи боже."
    show jessica smile talk 2
    jessica.c "Слушай, у тебя же есть бар, значит... Ты разбираешься в деньгах, да?"
    show jessica smile
    mc.c "Да. Пока всё настолько просто, что мне не нужно никого нанимать. Обычные доходы и расходы."
    show jessica smile talk 2
    jessica.c "Тогда ты должен знать. Помоги мне... Что такое «убывающая предельная полезность»?"
    show jessica smile
    mc.c "Э-э... Звучит как настоящая экономика. Тут я вряд ли помогу."
    show jessica bashful talk
    jessica.c "Эх... Как же сложно..."
    show jessica bashful
    "Мне жаль, но я точно не смогу помочь. Да и сам не могу умничать — я ведь бросил учёбу."
    "Глядя, как она мучается, я вспоминаю свои студенческие годы. Мне не нравились ни занятия, ни студенческая жизнь в целом."
    "Ей, кажется, нравится её жизнь, но об учёбе она почти не говорит... Вот и интересно."
    mc.c "Джесс, тебе вообще нравится то, чем ты занимаешься?"
    show jessica neutral talk
    jessica.c "Это?"
    show jessica joy
    jessica.c "Чёрта с два!"
    mc.c "Ха-ха. Это заметно."
    mc.c "Я имею в виду... Колледж. Твою специальность."
    show jessica tease talk
    jessica.c "Я обожаю колледж! Друзья классные, мы ходим по магазинам, выпиваем, там студенческие вечера, клубы на кампусе~"
    show jessica tease
    mc.c "А сама учёба?"
    show jessica mad talk
    jessica.c "Да, она отстой."
    show jessica joy
    jessica.c "А что, если бы в колледже не задавали домашку?"
    mc.c "Это называется безработица, и она тоже довольно паршивая."
    mc.c "Если ты бедный, конечно."
    show jessica bashful talk
    jessica.c "А-а... Ну да..."
    show jessica bashful
    mc.c "Я к тому, что ты ведь не совсем сама это выбрала, да?"
    show jessica neutral talk
    jessica.c "Не совсем. Но колледж я выбрала сама."
    show jessica neutral
    mc.c "А чем {i}ты{/i} хочешь заниматься? В будущем?"
    show jessica bashful
    jessica.c "Хм..."
    mc.c "Надеюсь, ты не просто делаешь всё, что велел отец."
    mc.c "Как там было... Просто получить работу? А чем именно заниматься?"
    show jessica neutral talk
    jessica.c "Не знаю... Наверное, какой-нибудь должностью в одной из его компаний..."
    jessica.c "Но это ещё через много лет. Я пока об этом не думаю."
    show jessica neutral
    "Я всё же волнуюсь..."
    mc.c "Хорошо, а что думает твоя мама?"
    show jessica thinking
    jessica.c "Хм~"
    show jessica smile talk 2
    jessica.c "Мама говорит, что женщины в нашей семье должны «получить образование», следить за собой и выйти замуж за богача..."
    show jessica smile
    "Надо было догадаться..."
    call stopMusic from _call_stopMusic_24
    show jessica smile talk 2
    jessica.c "...И завести детей!"
    show jessica smile
    "...О."
    "Боже мой. Её слова и выражение лица так меня потрясли, что я вздрогнул."
    "Дети..."
    "Она сказала это так легко и непринуждённо... Она об этом думает?"
    "Наши отношения ведь серьёзные, да? Я знаю, что её семья пока обо мне не знает, но..."
    "Может, я забегаю вперёд."
    call playMusic(heartTheme) from _call_playMusic_138
    mc.c "Итак... Ты разделяешь взгляды своей мамы?"
    show jessica tease talk
    jessica.c "Ну, думаю, ты не совсем тот «богач», о котором она говорила, хе-хе~"
    show jessica joy
    jessica.c "Но не переживай, я всё равно тебя люблю! Ха-ха!"
    mc.c "Спасибо..."
    mc.c "А насчёт детей?.."
    show jessica smile talk 2
    jessica.c "О, да, когда-нибудь!"
    show jessica thinking
    jessica.c "Мне кажется, мама иногда жалеет, что у неё только я, так что она наверняка хочет, чтобы у меня было несколько детей."
    show jessica smile talk 2
    jessica.c "Разве это не было бы {i}так{/i} мило~?"
    show jessica smile
    "...Вот это быстро."
    "Ничего себе. Я не думал, что этот разговор пойдёт так. Наверное, сам виноват."
    "Я не знаю, что сказать. Моя постоянная девушка, моя любимая, говорит о детях."
    "А я?.."
    show jessica smile talk 2
    jessica.c "А ты что думаешь?"
    show jessica smile
    "Боже, она не умолкает. Кажется, этот разговор её почти не задел."
    "Она так легко к этому относится или давно об этом думала?"
    mc.c "Я... Э-э..."
    show jessica surprise
    jessica.c "Ого! Я не пыталась на тебя давить!"
    show jessica thinking
    jessica.c "Но ты сам заговорил об этом~"
    mc.c "Прости, ты просто застала меня врасплох. Я не ожидал такого прямого ответа."
    show jessica neutral talk
    jessica.c "О... А почему? Я уже давно об этом знаю."
    show jessica neutral
    mc.c "Правда?"
    show jessica smile talk 2
    jessica.c "Я не имею в виду {i}прямо сейчас{/i}, но... Да, почему бы и нет?"
    jessica.c "У нас всегда будут деньги, чтобы их обеспечить. Можем нанять няню, отдать в садик, или я {i}с радостью{/i} стану мамой на полный день~"
    show jessica smile
    "«Мы». Она определённо представляет нас вместе... И явно давно об этом думает, не сомневаясь..."
    "Неужели она и правда уже рассматривала такое будущее для нас?"
    mc.c "Но твоя семья?.."
    show jessica neutral talk
    jessica.c "А что с ними?"
    show jessica neutral
    mc.c "Ну... Я человек."
    show jessica thinking
    jessica.c "А, точно~ Хм~"
    show jessica tease talk
    jessica.c "Разве я не говорила, что меня это не волнует?"
    show jessica tease
    "Говорила, но тогда мы обсуждали только свидания..."
    mc.c "Как они отреагируют?"
    show jessica tease talk
    jessica.c "Я же папина драгоценная дочурка. Уверена, я смогу его убедить~"
    jessica.c "Да и думал так в основном он. Если мама будет на моей стороне, всё будет просто."
    show jessica tease
    "Она определённо... Не против. Даже больше — она ни капли не сомневается."
    "Я молчу, не зная, что ещё сказать. Немного ошеломлён."
    show jessica neutral talk
    jessica.c "Ох... [mc.name]... Прости, не хотела так серьёзно всё представить. Я не пытаюсь на тебя давить."
    show jessica smile talk 2
    jessica.c "Но, как я уже сказала, я не хочу детей прямо сейчас. У нас ещё полно времени, правда?"
    show jessica joy
    jessica.c "Просто подумай об этом, ладно?"
    show jessica thinking
    jessica.c "Так, на чём я остановилась?.."
    "Она поворачивается обратно к экрану и продолжает заниматься, будто не только что огорошила меня."
    "Это откровение почти не выбило её из колеи, и она продолжает как ни в чём не бывало."
    "Ничего себе... Не знаю, что сказать. Но теперь я точно об этом думаю."
    "Хочу ли я детей от Джессики? Когда мы будем готовы?"
    "В каком-то смысле она гораздо взрослее меня."

    if(not fromGallery):
        $ jessica.addLike(1)
        $ jessica.addLove(1)

    return
