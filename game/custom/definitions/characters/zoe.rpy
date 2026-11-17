init offset = 3
default zoe = Person(Character(name='Zoe', who_color='#562186', image = 'zoe'), 'Zoe', '', 'zoe', 'female', 28)

label initialiseCharacter_zoe:
    python:
        zoe.currentLocation = location_away
        location_away.occupants.extend([zoe])
        zoe.availableEvents = [zoeFirstMeetingEvent]
        zoe.job = 'Безработная'
    return

label updateCharacterStatics_zoe:
    python:
        # Personal attributes
        zoe.species = 'Серый волк'
        zoe.birthday = 14
        # zoe.job = 'Unemployed' Can't as job might change
        zoe.giftLoves = [item_perfume, item_goldRing]
        zoe.giftLikes = [item_wine, item_dress]
        zoe.giftHates = [item_videogame, item_chocolateBar]

        # Skill attributes

        # Sexual attributes
        zoe.virgin = False

        # Personal effects

        # Event attributes
        zoe.events = [zoeFirstMeetingEvent, zoeLikeEvent1, zoeHEvent1, zoeLikeEvent2, zoeLikeEvent3, zoeHEvent2, zoeHEvent3, zoeHEvent4, zoeHEvent5, zoeHEvent6, zoeLikeEvent4, zoeVacation, zoeLikeEvent5, zoeHEvent7]
        zoe.specialEvents = [zoeJessicaDuoStoryEvent1, zoeJessicaHEvent1, katieZoeDuoStoryEvent1, katieZoeDuoHEvent1]
        zoe.selfieOptions = ['beach1', 'changingroom1', 'gym1', 'gym2', 'homelounge1']
        zoe.wakeUpOptions = ['cowgirl']
        zoe.dateChats = ['Background', 'Job', 'Hobbies']
        zoe.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = zoe.events[-1]
        zoe.maxLike = lastStoryEvent.requiredLike
        zoe.maxLove = lastStoryEvent.requiredLove

        # World attributes
        if(zoe.job == 'Безработная'):
            zoe.preferredMondaySchedule = [location_away, location_town, location_cafe, location_away]
            zoe.preferredTuesdaySchedule = [location_away, location_shop, location_beach, location_town]
            zoe.preferredWednesdaySchedule = [location_away, location_diner, location_park, location_bar]
            zoe.preferredThursdaySchedule = [location_away, location_cafe, location_offices, location_beach]
            zoe.preferredFridaySchedule = [location_away, location_bar, location_bar, location_bar]
            zoe.preferredSaturdaySchedule = [location_away, location_away, location_bar, location_bar]
            zoe.preferredSundaySchedule = [location_away, location_shop, location_beach, location_town]
        else:
            zoe.preferredMondaySchedule = [location_shop, location_bar, location_bar, location_bar]
            zoe.preferredTuesdaySchedule = [location_shop, location_bar, location_bar, location_town]
            zoe.preferredWednesdaySchedule = [location_away, location_cafe, location_diner, location_beach]
            zoe.preferredThursdaySchedule = [location_beach, location_park, location_bar, location_bar]
            zoe.preferredFridaySchedule = [location_cafe, location_bar, location_diner, location_town]
            zoe.preferredSaturdaySchedule = [location_town, location_beach, location_park, location_away]
            zoe.preferredSundaySchedule = [location_away, location_beach, location_diner, location_away]

        zoe.preferredMovedInMondaySchedule = [location_home, location_bar, location_bar, location_bar]
        zoe.preferredMovedInTuesdaySchedule = [location_home, location_bar, location_bar, location_home]
        zoe.preferredMovedInWednesdaySchedule = [location_home, location_home, location_home, location_home]
        zoe.preferredMovedInThursdaySchedule = [location_home, location_home, location_bar, location_bar]
        zoe.preferredMovedInFridaySchedule = [location_home, location_bar, location_home, location_home]
        zoe.preferredMovedInSaturdaySchedule = [location_town, location_town, location_home, location_home]
        zoe.preferredMovedInSundaySchedule = [location_home, location_beach, location_home, location_home]
    return

# Sprites
screen zoeClickable(xcenter):
    $ spriteload = zoe.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = zoe)
        at characterSpriteHover

# Character methods
label zoeEvaluateAvailableInteractions:
    python:
        if zoe.like >= 5:
            zoe.availableActions = list(set(zoe.availableActions + ['Spend time']))
        if zoe.like >= 10 and zoeHEvent1.unlocked:
            zoe.availableActions = list(set(zoe.availableActions + ['Invite over']))

        if zoe.isDateable and zoe.love >= 1:
            zoe.availableActions = list(set(zoe.availableActions + ['Date']))
        if zoe.love >= 3 and zoeLikeEvent3.unlocked:
            zoe.availableActions = list(set(zoe.availableActions + ['Affection']))
            zoe.availableAffections.extend(['Pat'])
        if zoe.love >= 6 and zoeHEvent3.unlocked:
            zoe.availableAffections.extend(['Hug'])
        if zoe.love >= 10 and zoeHEvent5.unlocked:
            zoe.availableAffections.extend(['Chin Scratch','Kiss'])
        if zoeHEvent3.unlocked:
            zoe.availableAffections.extend(['Caress Butt'])
        if zoeHEvent5.unlocked:
            zoe.availableAffections.extend(['Boob Grab'])
        if zoeHEvent7.unlocked:
            zoe.availableActions.extend([{'homebedroom': ['Anal']}])
        if zoe.movedIn:
            zoe.availableCommandsPrivate.extend(['Show Panties'])
            zoe.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label zoeChat:
    show zoe smile talk
    return

label zoeChat_beach:
    show zoe thinking
    zoe.c "Фух~ Надо бы окунуться."
    show zoe tease talk
    zoe.c "Спорим, тебе не терпится увидеть меня в бикини, да?"
    return

label zoeChat_park:
    show zoe smile talk 2
    zoe.c "Сходи, принеси мне напиток из автомата, ладно?"
    return

label zoeChat_shop:
    show zoe thinking
    zoe.c "Хм... Какую водку взять?"
    show zoe smile talk
    zoe.c "Ты ведь должен знать, да?"
    return

label zoeChat_diner:
    show zoe smile talk
    zoe.c "Привет, красавчик. Хочешь присоединиться? С мужчиной, который платит, еда вкуснее."
    return

label zoeChat_cafe:
    show zoe tease talk
    zoe.c "Раз уж ты здесь... Угостишь?"
    return

label zoeChat_town:
    show zoe neutral talk
    zoe.c "Пойдём развлекаться, [mc.name]."
    show zoe mad talk
    zoe.c "Э-эй, ну же!"
    return

label zoeChat_bar:
    show zoe tease talk
    zoe.c "Ещё один сюда, красавчик."
    zoe.c "Ты же не заставишь девушку платить за выпивку?"
    return

label zoeChat_aquarium:
    show zoe neutral talk
    zoe.c "Подумала, что здесь можно сделать хорошие фотографии."
    return

label zoeChat_theater:
    show zoe thinking
    zoe.c "А, я? Да ничего, просто время убиваю."
    show zoe smile talk
    zoe.c "Спорим, фильм будет дерьмовый. Составишь мне компанию?"
    return

label zoeChat_homebedroom:
    if(timeOfDay == 'Morning'):
        show zoe smile talk 2
        zoe.c "Привет, жеребец. Хе-хе, вид у тебя утром помятый~"
    elif(timeOfDay == 'Afternoon'):
        show zoe smile talk
        zoe.c "Я сегодня на смене, {i}босс{/i}~? Хе-хе~"
    elif(timeOfDay == 'Evening'):
        show zoe tease talk
        zoe.c "Девчонки сегодня ничем не заняты, так что... похоже, я застряла с тобой~"
    elif(timeOfDay == 'Night'):
        show zoe smile talk
        zoe.c "Да, сегодня я пораньше лягу спать, и что? Будешь паинькой — разрешу лечь рядом~"
    return

label zoeChat_homelounge:
    if(timeOfDay == 'Morning'):
        show zoe smile talk 2
        zoe.c "Это куда лучше всего, что у меня когда-либо было... Богатенький."
    elif(timeOfDay == 'Afternoon'):
        show zoe thinking
        zoe.c "Нужна сегодня лишняя пара рук в баре? Мне всё равно нечем заняться..."
    elif(timeOfDay == 'Evening'):
        show zoe smile talk
        zoe.c "Хм... Хочешь сегодня куда-нибудь? Надо нажраться~"
    elif(timeOfDay == 'Night'):
        show zoe smile talk 2
        zoe.c "Уже собрался спать? Ха-а, всё равно по телеку ничего нет, я к тебе присоединюсь~"
    return

label zoeChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show zoe smile talk
        zoe.c "Доброе утро, худыш. Смотри, я даже кофе тебе налила."
    elif(timeOfDay == 'Afternoon'):
        show zoe smile talk
        zoe.c "У нас продукты заканчиваются, худыш. Живо в магазин."
    elif(timeOfDay == 'Evening'):
        show zoe mad talk
        zoe.c "Конечно, я немного умею готовить. Приходилось самой о себе заботиться, знаешь ли..."
    elif(timeOfDay == 'Night'):
        show zoe tease talk
        zoe.c "Ха-ха, я пока не могу лечь, там в чате такая драма разгорается. Слушай..."
    return

# Date topics
label zoeChat_background:
    show zoe thinking
    zoe.c "Хм? Что хочешь узнать?"
    mc.c "Откуда ты, какая у тебя семья, как ты жила — ну, всякое такое."
    show zoe mad talk
    zoe.c "Это что, собеседование?"
    show zoe mad
    mc.c "Я просто..."
    show zoe tease talk
    zoe.c "Ха-ха! Да шучу я, красавчик."
    show zoe thinking
    zoe.c "Ну так... Я выросла в маленькой деревне в нескольких часах отсюда."
    show zoe neutral talk
    zoe.c "Надо было оттуда свалить. Деревня крошечная, ночной жизни нет, заняться нечем..."
    zoe.c "Уехала, как только смогла. Честно говоря, это был самый крупный город, куда я могла добраться без денег. Подруга приехала сюда раньше и пустила меня пожить."
    show zoe smile talk
    zoe.c "Чёрт, хорошо, что так вышло. Страшно подумать, чем бы я занималась, если бы осталась там."
    show zoe smile
    mc.c "То есть... с родителями не ладишь?"
    show zoe thinking
    zoe.c "Я бы так не сказала..."
    show zoe neutral talk
    zoe.c "Просто они слишком правильные, понимаешь? У них были на меня планы и ожидания. Да ну их."
    show zoe mad talk
    zoe.c "Поступить в колледж, найти стабильную работу, выйти замуж, подарить им внуков..."
    zoe.c "Боже, я ещё ребёнком была, а они уже распланировали всю мою жизнь. Ни за что."
    show zoe neutral talk
    zoe.c "Теперь... они просто слишком часто пилят меня... Переживают, куда катится моя жизнь и всё такое."
    show zoe smile talk 2
    zoe.c "Я просто живу своей жизнью. Мне больше нравится город. Клубы, бары, люди, понимаешь?"
    show zoe thinking
    zoe.c "Дома ничего такого не было."
    return

label zoeChat_job:
    if(zoeLikeEvent3.unlocked):
        show zoe smile talk 2
        zoe.c "Ну, пока ты так {b}любезно{/b} не решил меня взять на работу..."
        zoe.c "Да я просто слонялась без дела... Подрабатывала тут и там..."
    else:
        show zoe bashful talk
        zoe.c "Да я просто слонялась без дела... Подрабатывала тут и там..."
    show zoe neutral talk
    zoe.c "Работала официанткой в кафе и ресторанах... Немного кассиром в магазинах... Ну, ты понял."
    zoe.c "Рассказывать особо нечего. Карьеру я не строила."
    show zoe tease talk
    zoe.c "Хватало на выходные развлечения~"
    show zoe tease
    mc.c "Долго где-нибудь задерживалась?"
    show zoe smile talk
    zoe.c "Пока меня не увольняли или я сама не уходила. Обычно долго не выходило."
    show zoe smile talk 2
    zoe.c "Ну... максимум полгода?"
    show zoe smile
    mc.c "Удивлён, что места, где тебя готовы взять, ещё не закончились. Город-то небольшой."
    show zoe tease talk
    zoe.c "Ха-ха! Следи за языком, худыш~"
    show zoe smile talk 2
    zoe.c "Это студенческий город, люди постоянно приезжают и уезжают, поэтому работники всегда нужны. Даже такие, как я, которые работать не рвутся."
    show zoe smile
    mc.c "Умеешь пользоваться системой, да, Зои?"
    show zoe smile talk
    zoe.c "А то~"
    if(zoeLikeEvent3.unlocked):
        show zoe tease talk
        zoe.c "Не переживай, жеребец. Я не сбегу от тебя, как от всех остальных. Засчитаю тебе пару очков... Это лучшая работа в моей жизни."
    else:
        show zoe smile talk
        zoe.c "Ох... Давай не будем так много говорить о работе, худыш... Скукота."
        show zoe smile
        mc.c "Ладно."
    return

label zoeChat_hobbies:
    show zoe tease talk
    zoe.c "Алкоголь считается? Хе-хе~"
    show zoe tease
    mc.c "По-моему, вполне."
    show zoe tease talk
    zoe.c "Ты бы именно так и сказал, правда? Маленький торговец."
    show zoe smile talk 2
    zoe.c "Но я не собираюсь всё время торчать у тебя. Тут есть пара хороших клубов. По выходным мы с девчонками обычно где-нибудь тусуемся."
    show zoe smile talk
    zoe.c "Или ходим по более... {i}шикарным{/i} барам. Без обид..."
    show zoe smile
    mc.c "Не обижаюсь. Не хочу быть одним из них. Там собирается неподходящая публика, понимаешь?"
    "Я понимающе подмигиваю ей."
    show zoe tease talk
    zoe.c "О-о~ Значит, нам теперь вход закрыт? Тебе ведь не помешали бы такие красотки, как я и мои подруги. Заодно привлечём посетителей."
    show zoe tease
    mc.c "Хм... Может, ты и права."
    show zoe tease talk
    zoe.c "Только не бегай за всеми подряд. Я первая на тебя глаз положила~"
    show zoe smile talk 2
    zoe.c "К тому же, это я вкалываю в спортзале."
    show zoe smile
    mc.c "Силовые или кардио?"
    show zoe smile talk
    zoe.c "И то и другое понемногу. Хочу держать себя в тонусе, понимаешь?"
    show zoe tease talk
    zoe.c "Немного мышц в спальне очень даже помогают~"
    show zoe tease
    "Я слегка сглатываю. Она стройная, но у неё заметны мышцы. Нежной хрупкой девушкой её не назовёшь."
    mc.c "Значит, вечеринки и тренировки?"
    show zoe smile talk
    zoe.c "Ты так говоришь, будто этого недостаточно. А в клубе есть музыка, танцы..."
    show zoe tease talk
    zoe.c "Общение~"
    show zoe tease
    "Вечно поддразнивает..."
    return

#

label zoeInteractionBathroom:
    zoe.c "Эй, худыш, кто разрешил тебе смотреть на шоу~?"
    zoe.c "Господи... Девушке нельзя немного побыть в покое?"
    return

label zoeSpendTime(onDate):
    if(onDate):
        scene expression 'zoe[mc.currentLocation.apiName]date'
    else:
        scene expression 'zoe[mc.currentLocation.apiName]'
    with fade
    return

label zoeReceiveGift(item, likeChange, loveChange):
    show zoe tease talk
    zoe.c "О-о-о~ Надеюсь, это будет что-то стоящее."
    if(loveChange > 0):
        show zoe joy
        zoe.c "О да! Идеально!"
    elif(likeChange > 1):
        show zoe smile talk 2
        zoe.c "Отличный выбор, [mc.name], молодец."
    elif(likeChange < 1):
        show zoe mad talk
        zoe.c "В следующий раз постарайся лучше."
    else:
        show zoe smile talk
        zoe.c "Спасибо, красавчик."
    return

label zoeReceiveDateInvitation:
    show zoe smile talk 2
    zoe.c "Пожалуй, могу, если это ты."
    show zoe neutral
    call dateInvitationSelector(zoe) from _call_dateInvitationSelector_7
    show zoe smile talk
    zoe.c "[proposedDateLocation.name], [proposedDateDayOfWeek], в [proposedDateTime]? Может быть весело."

    python:
        scheduledDate = Date(zoe, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        zoe.scheduledDates.append(scheduledDate)
    return

label zoeStartDate:
    if(mc.currentLocation == location_home):
        show zoe tease talk with dissolve
        zoe.c "Даже не представляю, что ты задумал~"
    else:
        show zoe smile talk with dissolve
        zoe.c "Ну и что ты для меня сегодня приготовил?"
    return

label zoeDateInteraction:
    show zoe smile with dissolve
    show screen dateUi(zoe) with dissolve
    call screen dateInteractionScreen(zoe, mc.currentLocation)

label zoeChatDate:
    show zoe smile talk 2
    zoe.c "Вот так хорошо, продолжай, [mc.name]."
    return

label zoeChatDate_beach:
    show zoe smile talk
    zoe.c "Ждёшь, когда я покажу побольше?"
    show zoe tease talk
    zoe.c "Кто знает, может, получишь даже больше, чем рассчитывал."
    return

label zoeChatDate_park:
    show zoe thinking
    zoe.c "Парк?"
    zoe.c "Не назвала бы это безумно весёлым свиданием, но... ты мне нравишься, [mc.name]."
    return

label zoeChatDate_diner:
    show zoe smile talk
    zoe.c "Какой джентльмен..."
    show zoe smile talk 2
    zoe.c "Все девушки любят, когда их угощают вином и ужином."
    return

label zoeChatDate_cafe:
    show zoe neutral talk
    zoe.c "Не особо люблю кофе."
    show zoe smile talk
    zoe.c "Мне больше по душе что-нибудь покрепче, да?"
    return

label zoeChatDate_bar:
    show zoe tease talk
    zoe.c "Сегодня нам только напитки с верхней полки, верно?"
    show zoe smile talk
    zoe.c "Шучу. Если только...?"
    return

label zoeChatDate_aquarium:
    show zoe thinking
    zoe.c "Не мой обычный выбор для свидания, но..."
    show zoe smile talk 2
    zoe.c "А вообще, тут довольно мило."
    return

label zoeChatDate_theater:
    show zoe smile talk 2
    zoe.c "Ну что, красавчик, что будем смотреть?"
    show zoe tease talk
    zoe.c "Только не какую-нибудь сопливую мелодраму, да?"
    return

label zoeDatePayFor:
    show zoe smile talk
    zoe.c "Обожаю, когда мужчина берёт всё в свои руки."
    return

label zoeEndDate:
    if(dateScore < 40):
        show zoe mad
        zoe.c "Честно говоря... я ожидала большего."
    else:
        if(zoe.movedIn):
            show zoe tease talk
            zoe.c "Неплохо, [mc.name]. Не сбавляй темп, даже если уже уложил меня~"
        else:
            show zoe smile talk
            zoe.c "Хорошо провела время, красавчик. Спасибо!"
    return

label zoeContinueDateAtHome:
    scene expression 'zoe[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(zoeHEvent1.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label zoeHomeStartSex:
    show zoe tease talk
    zoe.c "О-о~? Не можешь устоять перед соблазном?"
    zoe.c "Надеюсь, ты устроишь мне незабываемый вечер~"
    show zoe tease
    return

label zoeHomeSexJoinIn(character):
    show zoe tease talk at twoPersonLeft with dissolve
    zoe.c "Для ещё одного найдётся место~?"
    show zoe tease
    return

label zoeEndDateAtHome:
    zoe.c "И это всё? Ну ладно, как-нибудь можем продолжить~"
    return

image zoe pat animated = Movie(play="images/characters/zoe/affections/zoePat.webm", side_mask=True, loop=True)
label zoeReceivePat:
    hide zoe with dissolve
    show zoe pat animated with dissolve
    pause
    if(zoeHEvent5.unlocked):
        zoe.c "Да-да, хорошо."
        zoe.c "Только смотри, чтобы никто не заметил, как ты это делаешь..."
    else:
        zoe.c "А?"
        zoe.c "Э-э... Ну, если хочешь, можешь, чудик."
    return

image zoe chinscratch animated = Movie(play="images/characters/zoe/affections/zoeChinscratch.webm", side_mask=True, loop=True)
label zoeReceiveChinScratch:
    hide zoe with dissolve
    show zoe chinscratch animated with dissolve
    pause
    zoe.c "Ой, да ладно, худыш..."
    zoe.c "И с чем мне приходится мириться..."
    return

image zoe caressbutt animated = Movie(play="images/characters/zoe/affections/zoeCaressButt.webm", side_mask=True, loop=True)
label zoeReceiveCaressButt:
    hide zoe with dissolve
    show zoe caressbutt animated with dissolve
    pause
    zoe.c "О-о~? Ну как, худыш?"
    zoe.c "Вижу, ты стал смелее. Мне нравится~"
    return

image zoe boobgrab animated = Movie(play="images/characters/zoe/affections/zoeBoobGrab.webm", side_mask=True, loop=True)
label zoeReceiveBoobGrab:
    hide zoe with dissolve
    show zoe boobgrab animated with dissolve
    pause
    zoe.c "Хм~? Ладно, я видела, как ты на них пялился."
    zoe.c "Эти — бесплатно. В следующий раз платишь сам."
    return

image zoe snuggle animated = Movie(play="images/characters/zoe/affections/zoeSnuggle.webm", side_mask=True, loop=True)
label zoeReceiveSnuggle:
    show zoe smile
    "Я плюхаюсь рядом с Зои на диван."
    show zoe smile talk
    zoe.c "Чё как, худыш?"
    hide zoe with dissolve
    show zoe snuggle animated with dissolve
    pause
    "Я закидываю её ноги себе на колени и притягиваю к себе за талию."
    zoe.c "Ой, просто внимания захотел, жеребец? Ну ладно, немного можно."
    pause
    return

label zoeReceiveHug:
    hide zoe with dissolve
    show zoe hug with dissolve
    pause
    if(zoeHEvent5.unlocked):
        zoe.c "Ой, красавчик~"
        zoe.c "Обнимашек захотелось?"
    else:
        zoe.c "Посмотрите-ка, какой нежный и ласковый."
        zoe.c "Обычно я не любительница такого, но, пожалуй, сойдёт."
    return

label zoeReceiveKiss:
    hide zoe with dissolve
    show zoe kiss with dissolve
    zoe.c "М-мм~"
    pause
    return

label zoeInitiatePat:
    show zoe neutral talk with dissolve
    zoe.c "Эй..."
    zoe.c "Побалуй меня немного."
    hide zoe with dissolve
    show zoe pat animated with dissolve
    pause
    zoe.c "Знаешь, я никому больше такого не позволяю."
    return

label zoeInitiateHug:
    show zoe smile talk with dissolve
    zoe.c "Иди сюда, жеребец."
    hide zoe with dissolve
    show zoe hug with dissolve
    pause
    if(zoeVacation.unlocked):
        zoe.c "Люблю тебя, жеребец."
    else:
        zoe.c "Пожёстче. Ты ведь не слабак, а?"
    return

label zoeInitiateKiss:
    show zoe neutral talk with dissolve
    zoe.c "[zoe.name] нужна ласка."
    hide zoe with dissolve
    show zoe kiss with dissolve
    zoe.c "М-мм~"
    pause
    hide zoe with dissolve
    show zoe tease with dissolve
    zoe.c "Не удержался — ты такая милая."
    return

label zoeInitiateSnuggle:
    "Проходя мимо Зои, сидящей на диване, я слышу, как она зовёт меня."
    show zoe smile talk
    zoe.c "Худыш, иди сюда."
    hide zoe with dissolve
    show zoe snuggle animated with dissolve
    pause
    "Она притягивает меня и обвивает ногами, крепко запирая в объятиях."
    zoe.c "Надо иногда вот так обниматься~"
    pause
    return

label zoeInitiateHomeSex:
    show zoe tease talk
    zoe.c "Ты. В спальню. Сейчас."
    zoe.c "Мне нужно, чтобы меня хорошенько заполнили~"
    show zoe tease
    return

label zoeInitiateHomeSexDeny:
    show zoe surprise
    zoe.c "П-погоди? Это ты мне {i}отказываешь{/i}?!"
    return

label zoeSeesAffection(affection):
    show zoe tease talk with dissolve
    zoe.c "Смело флиртуешь при мне, худыш~"
    zoe.c "Меня тоже бросишь?"
    show zoe tease
    call expression 'zoeReceive' + affection from _call_expression_44
    hide zoe with dissolve
    return

label zoeInviteOver:
    show zoe tease talk
    zoe.c "Смело, [mc.name]."
    zoe.c "Но мне нравится."
    return

label zoeInitiateInviteOver:
    show zoe tease talk
    zoe.c "Ладно. Отвезёшь меня к себе."
    show zoe tease
    menu:
        'Да':
            show zoe tease talk
            zoe.c "Я знала, что ты не устоишь~"
            return True
        'Нет':
            show zoe neutral talk
            zoe.c "А? Ну, сам виноват — упускаешь свой шанс."
    return False

label zoeInviteGoHomeTogether:
    show zoe smile talk 2
    zoe.c "Да, пошли отсюда."
    show zoe tease talk
    zoe.c "Интересно, чем мы займёмся~?"
    return

label zoeInitiateGoHomeTogether:
    show zoe smile talk
    zoe.c "На сегодня я закончила... Просто хочу домой. Поедешь со мной?"
    show zoe smile
    menu:
        'Да':
            show zoe smile talk 2
            zoe.c "Конечно же хочешь~"
            return True
        'Нет':
            show zoe smile talk 2
            zoe.c "Ладно, не веселись без меня слишком сильно~"
    return False

label zoeShowPanties(pantiesIndex = 1):
    show zoe tease talk
    zoe.c "У тебя хватает наглости такое спрашивать~ Ладно, смотри."
    $ renpy.show(zoe.apiName + ' panties ' + str(pantiesIndex), tag=zoe.apiName)
    with dissolve
    if(pantiesIndex == 1):
        zoe.c "Классика~ Подходит ко всему, что у меня есть."
    elif(pantiesIndex == 2):
        zoe.c "Хе-хе, думала, тебе понравится. Ты же пускаешь слюни, как пёс~"
    elif(pantiesIndex == 3):
        zoe.c "Ты меня раскусил~ Вообще без одежды~"
    return

label zoeSendDateText(proposedDate):
    python:
        zoe.textChain.append(Message(mc, zoe, 'пора тебе пригласить меня на свидание', Null, day, timeOfDay))
        zoe.textChain.append(Message(mc, zoe, proposedLocation.name.lower() + ', ' + proposedDateTime.lower() + ' завтра? Как тебе идея?', Null, day, timeOfDay, proposedDate))
    return

label zoeGetSelfieOptions:
    $ zoeSelfieOptions = []
    if(zoeLikeEvent1.unlocked):
        $ zoeSelfieOptions.extend(['beach1', 'changingroom1'])
    if(zoeHEvent1.unlocked):
        $ zoeSelfieOptions.extend(['gym1', 'gym2'])
    if(zoe.movedIn):
        $ zoeSelfieOptions.extend(['homelounge1'])
    return zoeSelfieOptions

label zoeSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'beach1':
                potentialResponses.append({'text': "Я не смотрела, честно!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Тебя невозможно не заметить.", 'statChange': 'love', 'statChangeAmount': 1})
                zoe.textChain.append(Message(mc, zoe, 'я видела, как ты на меня пялился, извращенец.', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'changingroom1':
                potentialResponses.append({'text': "Ещё бы!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Только если в следующий раз наденешь его для меня.", 'statChange': 'love', 'statChangeAmount': 1})
                zoe.textChain.append(Message(mc, zoe, 'Стоит мне купить этот наряд?', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'gym1':
                potentialResponses.append({'text': "Осторожнее, шалунья.", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Сисечки...", 'statChange': 'love', 'statChangeAmount': 1})
                zoe.textChain.append(Message(mc, zoe, 'Закончила в спортзале. Никого вокруг.', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'gym2':
                potentialResponses.append({'text': "Чёрт, я почти это вижу.", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Держу пари, тебе тоже хотелось бы, чтобы я была рядом.", 'statChange': 'love', 'statChangeAmount': 1})
                zoe.textChain.append(Message(mc, zoe, 'Раздевалка только для меня. Чего бы ты отдал, чтобы оказаться здесь сейчас?', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homelounge1':
                potentialResponses.append({'text': "Да, госпожа.", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Чертовски горячо.", 'statChange': 'love', 'statChangeAmount': 1})
                zoe.textChain.append(Message(mc, zoe, 'Дом. Сейчас же.', selfieName, day, timeOfDay, responses = potentialResponses))
    return

label zoeSexSelect:
    hide screen mainUi
    scene black with fade
    image zoe sex waiting = Movie(play="images/characters/zoe/hscenes/sexWaiting.webm")
    show zoe sex waiting with fade

    call screen zoeSexSelectScreen
    if(zoeHEvent5.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(zoe.movedIn):
            menu zoeSleepTogether:
                "Переспать с Зои?"
                'Да':
                    zoe.c "Чёрт, худыш, ты меня вырубил~"
                    zoe.c "Я сразу отключаюсь."
                    call characterSleepover(zoe) from _call_characterSleepover_14
                'Нет':
                    pass
        else:
            menu zoeStayTheNight:
                "Пригласить [zoe.name] остаться на ночь?"
                'Да':
                    $ zoe.addLove(1)
                    zoe.c "...Ладно..."
                    call characterSleepover(zoe) from _call_characterSleepover_15
                'Нет':
                    zoe.c "Будь наготове, когда я позову, жеребец."

    call endScene(character = zoe, targetLocation = location_home) from _call_endScene_15

screen zoeSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(zoeHEvent1.unlocked or persistent.debugMode):
                textbutton 'Наездница' keysym str(1):
                    action [Jump('zoeCowgirl')]
            else:
                textbutton 'Закрыто'
            if(zoeHEvent3.unlocked or persistent.debugMode):
                textbutton 'Минет' keysym str(2):
                    action [Jump('zoeBlowjob')]
            else:
                textbutton 'Закрыто'
            if(zoeHEvent4.unlocked or persistent.debugMode):
                textbutton 'Футджоб' keysym str(3):
                    action [Jump('zoeFootjob')]
            else:
                textbutton 'Закрыто'
            if(zoeHEvent5.unlocked or persistent.debugMode):
                textbutton 'Поцелуи' keysym str(4):
                    action [Jump('zoeMakeout')]
            else:
                textbutton 'Закрыто'
            if(zoeHEvent5.unlocked or persistent.debugMode):
                textbutton 'Миссионерская' keysym str(5):
                    action [Jump('zoeMissionary')]
            else:
                textbutton 'Закрыто'
            if(zoeVacation.unlocked or persistent.debugMode):
                textbutton 'Раком' keysym str(6):
                    action [Jump('zoeDoggyStyle')]
            else:
                textbutton 'Закрыто'
            if(zoeVacation.unlocked or persistent.debugMode):
                textbutton 'Поцелуи сверху' keysym str(7):
                    action [Jump('zoeKissingCowgirl')]
            else:
                textbutton 'Закрыто'
            if(zoeVacation.unlocked or persistent.debugMode):
                textbutton 'Ложки' keysym str(8):
                    action [Jump('zoeSpooning')]
            else:
                textbutton 'Закрыто'
            textbutton 'Выход' keysym str(9):
                action [Hide('zoeSexSelectScreen'), Return()]

label zoeSleepover:
    scene zoesleepover with fade
    pause
    return

label zoeMorningBedInteraction:
    scene zoehomemorning with fade
    pause
    if(zoe.movedIn):
        zoe.c "Привет. О, я тоже только проснулась."
        zoe.c "Не вставай... Давай сегодня забьём на всё~"
    else:
        zoe.c "Удивлён, что я всё ещё здесь, жеребец?"
        zoe.c "Хе-хе~ Твоё сонное личико показалось мне милым."
    return

label zoeMorningBedInteractionSex(event):
    if(event == 'cowgirl'):
        image zoe morning cowgirl 1 = Movie(play="images/characters/zoe/hscenes/morning/cowgirl1.webm")
        show zoe morning cowgirl 1 with fade
        pause
        zoe.c "Ну что, жеребец?"
        "Ничего себе... Зои сегодня с утра очень занята."
        mc.c "Всё нормально?"
        zoe.c "Вспоминала прошлую ночь. Ты был не против, так что..."
        zoe.c "Просто лежи."
        image zoe morning cowgirl 2 = Image("images/characters/zoe/hscenes/morning/cowgirl2.webp")
        show zoe morning cowgirl 2 with fadewhite
        pause
        zoe.c "Ох, блядь, вот это начало дня~"
    return

# Sex scenes
label zoeCowgirl:
    image zoe cowgirl start = Image("images/characters/zoe/hscenes/cowgirl/start.webp")
    scene zoe cowgirl start with fade
    pause
    image zoe cowgirl start2 = Image("images/characters/zoe/hscenes/cowgirl/start2.webp")
    scene zoe cowgirl start2 with fade
    pause
    image zoe cowgirl part 1 = Movie(play="images/characters/zoe/hscenes/cowgirl/part1.webm")
    show zoe cowgirl part 1 with fade
    pause
    image zoe cowgirl part 2 = Movie(play="images/characters/zoe/hscenes/cowgirl/part2.webm")
    show zoe cowgirl part 2 with fade
    pause
    image zoe cowgirl part 3 = Movie(play="images/characters/zoe/hscenes/cowgirl/part3.webm")
    show zoe cowgirl part 3 with fade
    pause
    image zoe cowgirl part 4 = Movie(play="images/characters/zoe/hscenes/cowgirl/part4.webm")
    show zoe cowgirl part 4 with fade
    pause
    image zoe cowgirl part 5 = Movie(play="images/characters/zoe/hscenes/cowgirl/part5.webm")
    show zoe cowgirl part 5 with fade
    pause
    image zoe cowgirl part 6 = Movie(play="images/characters/zoe/hscenes/cowgirl/part6.webm")
    show zoe cowgirl part 6 with fade
    pause
    image zoe cowgirl end = Image("images/characters/zoe/hscenes/cowgirl/end.webp")
    scene zoe cowgirl end with fadewhite
    pause
    jump zoeSexSelect

label zoeBlowjob:
    image zoe home blowjob start 2 = Image("images/characters/zoe/hscenes/barblowjob/homeVariant/start2.webp")
    scene zoe home blowjob start 2 with fade
    pause
    image zoe home blowjob part 1 = Movie(play="images/characters/zoe/hscenes/barblowjob/homeVariant/part1.webm")
    show zoe home blowjob part 1 with fade
    pause
    image zoe home blowjob part 2 = Movie(play="images/characters/zoe/hscenes/barblowjob/homeVariant/part2.webm")
    show zoe home blowjob part 2 with fade
    pause
    image zoe home blowjob part 3 = Movie(play="images/characters/zoe/hscenes/barblowjob/homeVariant/part3.webm")
    show zoe home blowjob part 3 with fade
    pause
    image zoe home blowjob part 4 = Movie(play="images/characters/zoe/hscenes/barblowjob/homeVariant/part4.webm")
    show zoe home blowjob part 4 with fade
    pause
    image zoe home blowjob end 1 = Image("images/characters/zoe/hscenes/barblowjob/homeVariant/end1.webp")
    scene zoe home blowjob end 1 with fadewhite
    pause
    image zoe home blowjob end 2 = Image("images/characters/zoe/hscenes/barblowjob/homeVariant/end2.webp")
    scene zoe home blowjob end 2 with fade
    pause
    jump zoeSexSelect

label zoeFootjob:
    image zoe footjob part 1 = Movie(play="images/characters/zoe/hscenes/footjob/part1.webm")
    show zoe footjob part 1 with fade
    pause
    image zoe footjob part 2 = Movie(play="images/characters/zoe/hscenes/footjob/part2.webm")
    show zoe footjob part 2 with fade
    pause
    image zoe footjob part 3 = Movie(play="images/characters/zoe/hscenes/footjob/part3.webm")
    show zoe footjob part 3 with fade
    pause
    image zoe footjob part 4 = Movie(play="images/characters/zoe/hscenes/footjob/part4.webm")
    show zoe footjob part 4 with fade
    pause
    image zoe footjob part 5 = Movie(play="images/characters/zoe/hscenes/footjob/part5.webm")
    show zoe footjob part 5 with fade
    pause
    image zoe footjob end = Image("images/characters/zoe/hscenes/footjob/end.webp")
    scene zoe footjob end with fadewhite
    pause
    jump zoeSexSelect

label zoeMakeout:
    image zoe makeout part 1 = Movie(play="images/characters/zoe/hscenes/missionary/makeout1.webm")
    show zoe makeout part 1 with fade
    pause
    image zoe makeout part 2 = Movie(play="images/characters/zoe/hscenes/missionary/makeout2.webm")
    show zoe makeout part 2 with fade
    pause
    jump zoeSexSelect

label zoeMissionary:
    image zoe missionary start 2 = Image("images/characters/zoe/hscenes/missionary/start2.webp")
    show zoe missionary start 2 with fade
    pause
    image zoe missionary part 1 = Movie(play="images/characters/zoe/hscenes/missionary/part1.webm")
    show zoe missionary part 1 with fade
    pause
    image zoe missionary part 2 = Movie(play="images/characters/zoe/hscenes/missionary/part2.webm")
    show zoe missionary part 2 with fade
    pause
    image zoe missionary part 3 = Movie(play="images/characters/zoe/hscenes/missionary/part3.webm")
    show zoe missionary part 3 with fade
    pause
    image zoe missionary part 4 = Movie(play="images/characters/zoe/hscenes/missionary/part4.webm")
    show zoe missionary part 4 with fade
    pause
    image zoe missionary part 5 = Movie(play="images/characters/zoe/hscenes/missionary/part5.webm")
    show zoe missionary part 5 with fade
    pause
    image zoe missionary end 1 = Image("images/characters/zoe/hscenes/missionary/end1.webp")
    show zoe missionary end 1 with fadewhite
    pause
    image zoe missionary end 2 = Image("images/characters/zoe/hscenes/missionary/end2.webp")
    show zoe missionary end 2 with fade
    pause
    jump zoeSexSelect

label zoeDoggyStyle:
    image zoe doggy 1 = Movie(play="images/characters/zoe/events/vacation/homeVariants/doggy1.webm")
    show zoe doggy 1 with fade
    pause
    image zoe doggy 2 = Movie(play="images/characters/zoe/events/vacation/homeVariants/doggy2.webm")
    show zoe doggy 2 with fade
    pause
    image zoe doggy 3 = Movie(play="images/characters/zoe/events/vacation/homeVariants/doggy3.webm")
    show zoe doggy 3 with fade
    pause
    scene zoedoggystylefinish with fadewhite
    pause
    jump zoeSexSelect

label zoeKissingCowgirl:
    image zoe kissing cowgirl 1 = Movie(play="images/characters/zoe/events/vacation/homeVariants/cowgirl1.webm")
    show zoe kissing cowgirl 1 with fade
    pause
    image zoe kissing cowgirl 2 = Movie(play="images/characters/zoe/events/vacation/homeVariants/cowgirl2.webm")
    show zoe kissing cowgirl 2 with fade
    pause
    image zoe kissing cowgirl 3 = Movie(play="images/characters/zoe/events/vacation/homeVariants/cowgirl3.webm")
    show zoe kissing cowgirl 3 with fade
    pause
    jump zoeSexSelect

label zoeSpooning:
    image zoe spooning 1 = Movie(play="images/characters/zoe/events/vacation/homeVariants/spooning1.webm")
    show zoe spooning 1 with fade
    pause
    image zoe spooning 2 = Movie(play="images/characters/zoe/events/vacation/homeVariants/spooning2.webm")
    show zoe spooning 2 with fade
    pause
    scene zoespooningfinish1 with fadewhite
    pause
    scene zoespooningfinish2 with fade
    pause
    jump zoeSexSelect

label zoehomebedroomAnal:
    scene zoeanalagainstwallstart1 with fade
    pause
    image zoeAnalAgainstWall1 = Movie(play="images/characters/zoe/hscenes/analAgainstWall/part1.webm")
    scene zoeAnalAgainstWall1 with fade
    pause
    image zoeAnalAgainstWall2 = Movie(play="images/characters/zoe/hscenes/analAgainstWall/part2.webm")
    scene zoeAnalAgainstWall2 with fade
    pause
    image zoeAnalAgainstWall3 = Movie(play="images/characters/zoe/hscenes/analAgainstWall/part3.webm")
    scene zoeAnalAgainstWall3 with fade
    pause
    scene zoeanalagainstwallfinish1 with fadewhite
    pause
    scene zoeanalagainstwallfinish2 with fade
    pause
    return

# Events
# Known to MC
default zoeFirstMeetingEvent = Event('Первая встреча', 'zoeFirstMeeting', [zoe], 0, 0, [], location_bar, ['Evening', 'Night'], triggerDay = 4)
default zoeLikeEvent1 = Event('Взять инициативу', 'zoeLikeEvent1', [zoe], 5, 0, [zoeFirstMeetingEvent], location_town, ['Afternoon', 'Evening', 'Night'])
# Riding cowgirl
default zoeHEvent1 = Event('Что происходит?', 'zoeHEvent1', [zoe], 10, 0, [zoeLikeEvent1], location_bar, ['Afternoon', 'Evening', 'Night'])
# Job offer
default zoeLikeEvent2 = Event('Трудные времена', 'zoeLikeEvent2', [zoe], 15, 5, [zoeHEvent1], location_shop)
# Job accept. Pat head.
default zoeLikeEvent3 = Event('Серьёзно?', 'zoeLikeEvent3', [zoe], 20, 10, [zoeLikeEvent2], location_park)
# Handy behind the bar
default zoeHEvent2 = Event('Исподтишка', 'zoeHEvent2', [zoe], 30, 15, [zoeLikeEvent3], location_bar, ['Evening', 'Night'])
# Bar blowjob and hug
default zoeHEvent3 = Event('Премия', 'zoeHEvent3', [zoe], 40, 20, [zoeHEvent2], location_bar, ['Evening', 'Night'])
# Sofa Footjob
default zoeHEvent4 = Event('Немного дразнит', 'zoeHEvent4', [zoe], 50, 25, [zoeHEvent3], location_bar, ['Evening', 'Night'])
# Kiss, missionary, sleepover
default zoeHEvent5 = Event('Ночёвка', 'zoeHEvent5', [zoe], 60, 30, [zoeHEvent4], location_diner, ['Evening', 'Night'])
# Doggystyle against bar
default zoeHEvent6 = Event('Без дна', 'zoeHEvent6', [zoe], 70, 35, [zoeHEvent5], location_bar, ['Evening', 'Night'])
# Call of work. Go and check. Parents pissed her off. Want kids
default zoeLikeEvent4 = Event('В последнюю минуту', 'zoeLikeEvent4', [zoe], 80, 40, [zoeHEvent6], location_bar, ['Evening', 'Night'])
# Road trip vacation
default zoeVacation = Event('Уехать из города', 'zoeVacation', [zoe], 90, 45, [zoeLikeEvent4], Null, extraNotes = 'Зои чем-то встревожена. В меню взаимодействия появится особый вариант.', cost=350, requiredItems = [item_car], requiresInvite = True)
# Move in invite + event
default zoeLikeEvent5 = Event('Если бы встретились раньше', 'zoeLikeEvent5', [zoe], 100, 50, [zoeVacation], Null, extraNotes = 'Отношения становятся серьёзнее. Готовы ли мы к следующему шагу?\nВ меню взаимодействия появится особый вариант.', requiredItems = [item_car], requiresInvite = True)
# Caught changing / anal against wall
default zoeHEvent7 = Event('Перед вечеринкой', 'zoeHEvent7', [zoe], 110, 55, [zoeLikeEvent5], location_home_bedroom, ['Evening', 'Night'], mcInitiated = True)

label zoeFirstMeeting(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_248
    "Сегодня в баре аншлаг — самый час пик."
    "Работы много, зато дела идут отлично. У меня есть всё необходимое, чтобы это место процветало."
    "Больше никогда не работать на кого-то... Вот бы так."
    "Я должен добиться успеха."
    "Сегодня я за стойкой — на своём месте."
    zoe_unknown "О-о~ Привет, красавчик."
    "Её голос перекрывает гул разговоров в зале. Кто-то флиртует за барной стойкой?"
    "Можете звать меня любопытным, но я оборачиваюсь, чтобы незаметно взглянуть."
    scene zoefirstmeetingi1 with fade
    "Передо мной стоит женщина и прямо смотрит на меня. На ней очень откровенный короткий топ и короткая юбка."
    "Кажется, голос доносился оттуда. Я оглядываюсь, пытаясь понять, с кем она пришла, но рядом никого нет."
    zoe_unknown "Да, ты, худыш."
    "Она определённо обращается ко мне. Худыш? Я не особо тренируюсь, но не сказал бы, что я такой уж щуплый."
    mc.c "Худыш?"
    zoe_unknown "Худыш, гладкокожий, лысик — как угодно. Ты понял. Таких, как ты, здесь нечасто встретишь."
    "Я слышал несколько слов, которыми называют людей. Не уверен, оскорбления это или нет, но для первой беседы с незнакомкой звучит грубовато."
    "Она похожа на какую-то собачью. На мой взгляд, волчица, но с моими скудными знаниями лучше не делать выводов."
    "Вся такая тёмная: тёмный мех, волосы, насыщенно-фиолетовая одежда. Ногти накрашены и выглядят жутко острыми."
    "Для женщины она довольно высокая. Широкие бёдра, а на руках и ногах заметно больше мышц, чем ожидаешь. С такими плечами она точно тренируется."
    $ location_bar.showBackground()
    show zoe smile with dissolve
    mc.c "Я... понял. Что вам налить, мисс?"
    show zoe mad talk
    zoe_unknown "Во-первых, не называй меня «мисс»."
    show zoe neutral talk
    zoe_unknown "Во-вторых, двойной ром с колой."
    show zoe tease talk
    zoe_unknown "И в-третьих — свой номер."
    show zoe tease
    mc.c "Двойной ром с ко... А?"
    show zoe tease talk
    zoe_unknown "Хе-хе, не надо так удивляться. А то решу, что сделала неудачный выбор."
    show zoe tease
    "Она слегка наклоняется над стойкой, почти предлагая заглянуть в откровенное декольте."
    "Признаюсь, она застала меня врасплох. Просто дразнит или говорит серьёзно? Лучше перевести всё в шутку."
    mc.c "Двойной ром с колой сейчас будет."
    "Я отворачиваюсь, чтобы приготовить ей напиток."
    show zoe surprise
    hide zoe with dissolve
    zoe_unknown "Эй! Не заставляй девушку выпрашивать."
    "Она не сдаётся. По выражению её лица, когда я отвернулся, понятно: она ждала, что я сразу в неё влюблюсь."
    "Я продолжу заниматься своим делом и посмотрю, не отстанет ли она."
    "Я возвращаюсь с её напитком."
    show zoe tease talk with dissolve
    zoe_unknown "Что такое? Обручального кольца на пальце не вижу."
    zoe_unknown "Большинству мужчин так повезло бы познакомиться со мной."
    show zoe tease
    mc.c "Сначала пригласите меня на ужин."
    show zoe tease talk
    zoe_unknown "О-хо~ Трудно достаться, да?"
    show zoe smile talk 2
    zoe_unknown "Тогда постарайся, чтобы оно того стоило~"
    show zoe smile
    mc.c "Ваш напиток."
    "Я ставлю стакан перед ней. Она всё так же кокетливо улыбается."
    "Девушка явно смелая. С такой можно влипнуть: затянет, а потом перемелет и выплюнет."
    "Но всё же приятно хоть раз оказаться на месте того, с кем флиртуют."
    mc.c "Посмотрим, как пройдёт вечер. Ты сегодня одна?"
    call playMusic(chillTheme) from _call_playMusic_249
    show zoe thinking
    zoe_unknown "Я была с парой подруг, но они рано засобирались домой."
    zoe_unknown "А мне захотелось ещё выпить, так что я осталась."
    show zoe tease talk
    zoe_unknown "И ещё заметила симпатичного парня за стойкой. Решила подойти и... запустить коготки."
    show zoe smile talk
    zoe_unknown "А человек здесь что забыл? Учишься в колледже или подрабатываешь на карманные расходы?"
    show zoe smile
    mc.c "Вообще-то, я владелец этого места."
    show zoe smile talk 2
    zoe_unknown "Управляешь баром в таком возрасте? Впечатляет~"
    show zoe smile
    mc.c "В смысле, это мой бар. Я его владелец и управляю им."
    show zoe surprise
    zoe_unknown "Что? Прямо всем баром?"
    mc.c "Всем баром. Рад, что вы к нам заглянули."
    show zoe thinking
    zoe_unknown "..."
    show zoe smile talk
    zoe_unknown "Ого, ну ты даёшь. Очень впечатляет... Ещё одна причина тебя заполучить. И выпивать можно будет бесплатно."
    show zoe smile
    mc.c "Я не раздаю напитки всем симпатичным девушкам, а то разорюсь."
    show zoe tease talk
    zoe_unknown "Любишь пушистых, да? Ха-ха! Миленько."
    show zoe tease
    "Теперь она сидит у стойки и, похоже, не собирается возвращаться к столику."
    "Устроилась на табурете, скрестив ноги. Обтягивающая мини-юбка вот-вот лопнет по швам."
    mc.c "А ты чем зарабатываешь?"
    show zoe thinking
    zoe_unknown "Я... скажем так, сейчас в ожидании новых возможностей."
    mc.c "А чем занималась раньше?"
    show zoe neutral talk
    zoe_unknown "То тут, то там... Паршивая офисная работа, обслуживание покупателей, всякое такое."
    zoe_unknown "Просто... устала, что мной командуют."
    show zoe tease talk
    zoe_unknown "Обычно мне больше нравится самой командовать~"
    show zoe tease
    "Она соблазнительно, но не слишком заметно облизывает губы."
    "Последнюю фразу я проигнорирую. Чувствую, что попаду в её ловушку."
    mc.c "Похоже, теперь я буду часто видеть тебя здесь. Днём мы тоже открыты."
    mc.c "Кстати, меня зовут [mc.name]."
    show zoe smile talk 2
    zoe_unknown "Можно было обойтись без всех этих скучных знакомств, но ты кажешься милым — давай по-твоему."
    "Что она имела в виду?"
    zoe.c "[zoe.name]."
    show zoe smile
    mc.c "Приятно познакомиться, [zoe.name]."
    "Она делает пару больших глотков."
    "Я замечаю другого посетителя."
    mc.c "Минутку, мисс."
    show zoe mad
    zoe.c "*Хмпф*"
    hide zoe with dissolve
    "Она надувает губы, пока я занимаюсь своими делами. Похоже, мужчины привыкли давать ей всё, чего она хочет."
    "Но и слишком уж невозмутимым быть не стоит. Она чертовски горячая."
    "Закончив, я возвращаюсь к ней, держа почти пустой бокал."
    show zoe neutral with dissolve
    "..."
    show zoe neutral talk
    zoe.c "Ладно, ты победил. Не знаю, как ты перехватил инициативу, но держи."
    show zoe neutral
    "Она пододвигает мне бумажку с номером."
    show zoe neutral talk
    zoe.c "Я не шутила. Давай как-нибудь проведём время вместе. Позвони мне."
    show zoe neutral
    "Она допивает остатки и слезает с табурета, собираясь уходить."
    show zoe tease talk
    zoe.c "Ещё увидимся, красавчик."
    hide zoe with dissolve
    "Она выходит за дверь, покачивая бёдрами в короткой юбке."
    "Вот это был вихрь событий. [zoe.name]..."
    "И только сейчас я понимаю, что за последний напиток она так и не заплатила..."

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.knownToMC = True

    return

label zoeLikeEvent1(fromGallery):
    $ location_town.showBackground()
    call playMusic(madTheme) from _call_playMusic_250
    zoe_unknown "Привет, худыш!"
    "За спиной раздаётся знакомый голос."
    show zoe mad with dissolve
    "Это [zoe.name]. Она недовольно надулась, скрестив руки на широких плечах. Выглядит немного грозно."
    mc.c "Привет, [zoe.name]. Как дела?"
    show zoe mad talk
    zoe.c "Ну и что это было?"
    show zoe mad
    mc.c "Ты о чём?"
    show zoe mad talk
    zoe.c "Получил номер девушки и даже никуда её не пригласил?"
    show zoe mad
    "Давно это было. Да, она дала мне номер, но, если честно, я решил, что она просто дурачится. Или что всё это слишком хорошо, чтобы быть правдой."
    "Резкая, нахальная, требовательная, кокетливая. Вот это женщина."
    "Забавно будет и дальше играть с ней в эту игру. В прошлый раз она немного растерялась, когда я не стал отвечать ей в том же духе."
    mc.c "Если правильно помню, ты сказала что-то вроде: «Мне нравится самой всё контролировать». Может, я ждал, пока ты проявишь инициативу."
    show zoe mad talk
    zoe.c "Не в таком смысле, идиот! Так с леди не обращаются."
    show zoe mad
    mc.c "Ой, прошу прощения. Простите меня, {b}мэм{/b}."
    "На слове «мэм» [zoe.name] прожигает меня убийственным взглядом."
    zoe.c "..."
    call playMusic(funnyTheme) from _call_playMusic_251
    show zoe tease talk
    zoe.c "О-о~ Понятно, значит, играем в игры?"
    zoe.c "Играешь с огнём, мальчик. Ты не представляешь, во что ввязался."
    "По её тону у меня по спине пробегает настоящая дрожь. Справлюсь ли я с этой женщиной?"
    show zoe mad talk
    zoe.c "Сам напросился. Пошли."
    show zoe mad
    mc.c "Куда?"
    show zoe mad talk
    zoe.c "Твоё заведение открыто? Тогда пошли. Выпивка за твой счёт."
    show zoe mad
    "Я и так собирался туда. Есть способ выкрутиться? Или зачем? Может быть весело."
    "Не успеваю ничего сказать, как она толкает меня в спину."
    show zoe tease talk
    zoe.c "Шевелись."
    scene black with fade
    "Через минуту мы уже за углом."
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_252
    "Сегодня я не особо нужен, просто собирался пересчитать товар, присмотреть за заведением и проверить, всё ли у персонала в порядке."
    "Наверное, ничего страшного, если вместо этого я останусь здесь с... Это свидание?"
    show zoe smile talk
    zoe.c "Видишь, теперь ты проведёшь день с обалденной красоткой вместо каких-то скучных дел."
    zoe.c "Так что будь хорошим мальчиком и принеси нам бутылку чего-нибудь. Сам решай, ты же эксперт."
    mc.c "Как прикажете, принцесса."
    show zoe mad
    zoe.c "..."
    hide zoe with dissolve
    "Я иду к стойке, беру вино средней ценовой категории и пару бокалов."
    "Сегодня не жалко потратиться на неё. При всех её причудах, с [zoe.name] весело общаться."
    "Только не совсем понимаю, чего она добивается."
    show zoe smile talk 2 with dissolve
    zoe.c "О-о~ Как шикарно. Раскошелился ради такой старушки, как я? Неплохо, красавчик."
    show zoe smile
    "Я наливаю нам по бокалу, и мы чокаемся."
    show zoe smile talk
    zoe.c "Ну и какова твоя история, худыш? Переехал сюда, в город антро?"
    show zoe smile
    scene black with fade
    "Я рассказываю ей о бывшем начальнике, прежнем владельце и прочем."
    $ location_bar.showBackground()
    show zoe surprise with dissolve
    zoe.c "И он просто отдал его тебе, потому что о тебе хорошо отзывались?"
    mc.c "Примерно так, да."
    show zoe thinking
    zoe.c "Чёрт... Повезло тебе..."
    show zoe neutral talk
    zoe.c "А если из-за этого ты разоришься?"
    show zoe neutral
    mc.c "Я изучил все счета до того, как согласился. Всё выглядело нормально. Я был уверен, что смогу поддерживать работу заведения."
    mc.c "Это был риск, на который я пошёл. Как я и говорил, шанс начать всё заново, а быть самому себе начальником казалось огромным преимуществом."
    show zoe bashful talk
    zoe.c "За это я выпью..."
    show zoe bashful
    mc.c "Ты сказала, что сейчас не работаешь?"
    show zoe neutral talk
    zoe.c "Именно. С меня хватит этого дерьма."
    show zoe neutral
    mc.c "А чем ты занималась раньше?"
    show zoe thinking
    zoe.c "Какой-то бумажной работой в газете. Скукотища."
    zoe.c "Начальник — мудак, коллеги — отстой. Я просто перестала хоть что-то делать."
    mc.c "Тебе хватает денег на жизнь?"
    show zoe neutral talk
    zoe.c "Ну да, пока хватит. Не хочу пока думать о поиске работы, просто дай мне пожить свободно."
    show zoe mad talk
    zoe.c "Арг, зачем мы говорим о работе? Скучно же."
    show zoe mad
    mc.c "Чем тогда занимаешься на свободе?"
    show zoe smile talk
    zoe.c "Тусуюсь, выпиваю, делаю всё, чем заняты друзья. А, ещё часто хожу в спортзал."
    show zoe tease talk
    zoe.c "Зацени мои бицепсы. Горжусь этими руками. Думаешь, справишься со всем этим?"
    show zoe tease
    mc.c "Справиться как? Что ты имеешь в виду?"
    "Я, конечно, понимаю, что она имеет в виду, но всё равно изображаю непонимание."
    show zoe tease talk
    zoe.c "Ха-ха, ты забавный, [mc.name]. Мне понравится с тобой играть."
    "Она флиртует каждую минуту. Не успеваю оглянуться, как её бокал пустеет, и я наливаю ещё."
    zoe.c "Подливай, красавчик."
    scene black with fade
    call playMusic(funnyTheme) from _call_playMusic_253
    "С такой... необычной... девушкой, как [zoe.name], вечер проходит весело."
    "Это было свидание? По крайней мере, проходило оно совсем не как обычное."
    "Напитки идут легко, и в конце концов появляется ещё одна бутылка."
    "В итоге мы оба изрядно набираемся."
    $ location_bar.showBackground()
    show zoe tease talk
    zoe.c "О-о, какой-то парень... совсем не умеет пить~"
    zoe.c "Боже, я должна рассказать тебе ещё одну историю~"
    show zoe thinking
    zoe.c "Погоди-ка... Куда делся мой напиток?.. Почему стакан пустой!?"
    mc.c "Кажется... *ик* Ты его выпила..."
    show zoe tease talk
    zoe.c "Чёрт~ Спорим, это ты всё выпил... Чёртов худыш~"
    zoe.c "Блядь~ Ты так... вкусно пахнешь~"
    show zoe tease
    mc.c "Ты тоже."
    "Её глаза слипаются, она покачивается на стуле. Нас обоих развезло."
    "Мы напились сильнее, чем следовало. Не лучший исход для свидания."
    show zoe mad talk
    zoe.c "Блядь, почему мы всё ещё здесь? Мы уже должны были трахаться у тебя дома."
    show zoe mad
    "Она говорит громче, чем нужно, и посетители за соседними столиками оборачиваются."
    "В том числе сотрудники, которым смешно наблюдать за этой сценой."
    hide zoe with dissolve
    "[zoe.name] в конце концов кладёт голову на стол. Пора заканчивать вечер."
    "В баре это не редкость. У нас под рукой номера такси. Я прошу сотрудников вызвать ей машину домой."
    scene black with fade
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_town.showBackground()
    "Приезжает такси, и мне удаётся довести её до машины."
    "Пора отправлять её домой. Несмотря на её прежние слова, я не считаю правильным напаивать девушку на первом свидании, чтобы затащить её в постель."
    mc.c "Отвезите её домой, куда бы там ни пришлось, хорошо?"
    unknown "Конечно."
    show zoe mad talk
    zoe.c "Эй~ Ты что, не поедешь со мной?!"
    show zoe mad
    mc.c "Не сегодня, [zoe.c]. Но я хорошо провёл время."
    show zoe tease talk
    zoe.c "Чего-о-о? Ну пожа-а-алуйста~ Будет весело~"
    show zoe tease
    "Она пытается кокетливо улыбнуться, но пьяная лишь покачивается на сиденье, глаза закрываются."
    mc.c "Ещё увидимся, [zoe.name]."
    "Я закрываю дверцу и хлопаю по ней, давая водителю знак ехать."
    show zoe tease talk
    zoe.c "Трусишка~ Ха-ха-а~"
    hide zoe with dissolve
    scene black with fade
    "Машина уезжает, а я кое-как добираюсь домой."
    "Было весело, но не испортил ли я всё?"

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)
        $ zoe.isDateable = True
        "Теперь можно приглашать [zoe.name] на свидания."

    return {'time':'Morning'}


label zoeHEvent1(fromGallery):
    $ location_bar.showBackground()
    "Сегодня я подменяю кого-то за стойкой. Скоро уже смогу уйти."
    "Я только что обслужил клиента, как в дверь входит знакомое лицо и оглядывает зал."
    show zoe mad with dissolve
    call playMusic(madTheme) from _call_playMusic_254
    "Снова [zoe.name]. Заметив меня, она хмурится и направляется прямо ко мне."
    "Что теперь? Опять будет отчитывать меня за что-нибудь."
    show zoe mad talk
    zoe.c "[mc.name]."
    show zoe mad
    mc.c "[zoe.name]."
    zoe.c "..."
    show zoe mad talk
    zoe.c "Нам надо поговорить."
    show zoe mad
    "Ничего хорошего."
    mc.c "Э-э, конечно. Дай минутку, я только закончу."
    show zoe thinking
    zoe.c "Я буду вон там."
    hide zoe with dissolve
    "Она показывает на столик в углу и уходит."
    "Свидание прошло хорошо, после мы ещё пару раз встречались, и всё было нормально."
    "Что могло пойти не так?"
    scene black with fade
    "Я заканчиваю дела и передаю смену коллеге."
    $ location_bar.showBackground()
    show zoe thinking with dissolve
    "[zoe.name] листает телефон, когда я подхожу. Она ничего не заказала."
    mc.c "Принести тебе что-нибудь выпить?"
    show zoe mad talk
    zoe.c "Ну, очевидно, не стоит."
    show zoe mad
    mc.c "А?"
    show zoe mad talk
    zoe.c "Ну и что это было? Отлично провели время, а ты в последний момент меня бросил. Что это вообще значит?"
    show zoe mad
    mc.c "О чём ты? Не понимаю."
    show zoe bashful talk
    zoe.c "Если честно, тот вечер помню смутно. После первых пары бокалов почти ничего не осталось в памяти."
    show zoe thinking
    zoe.c "Я сама приволокла тебя сюда, и мне казалось, мы отлично провели время."
    mc.c "Так и было, да? Мне точно понравилось."
    show zoe mad talk
    zoe.c "Так что произошло в конце? Я только сейчас вспомнила."
    show zoe mad
    mc.c "Что? Я что-то сделал? Мы же оба были в стельку."
    show zoe mad talk
    zoe.c "Нет, ничего ты не сделал! В этом и проблема. Что это было: посадил меня в такси и помахал на прощание?"
    zoe.c "Мог бы ещё укрыть меня одеялком и сказку на ночь прочитать."
    show zoe mad
    mc.c "Э-э... Прости, а что мне надо было сделать?"
    show zoe mad talk
    call stopMusic from _call_stopMusic_47
    zoe.c "Ты должен был отвезти меня домой и трахнуть так, чтобы я мозги потеряла, идиот."
    show zoe mad
    "Она выпаливает это без малейшего колебания и совершенно искренне."
    "Я в полном замешательстве. Она злится, что... я не отвёз её к себе?"
    mc.c "В ту ночь ты была не в том состоянии. Как и я. Мы оба слишком много выпили."
    show zoe mad talk
    zoe.c "И что?"
    show zoe mad
    mc.c "Это было бы неправильно."
    show zoe thinking
    zoe.c "Ох, Иисусе, ты что, тряпка какая-то?"
    mc.c "Ты сама тогда примерно это и сказала, если не ошибаюсь."
    show zoe mad talk
    zoe.c "Ну так я была права. Что ты за мужик?"
    show zoe thinking
    zoe.c "Ты хочешь сказать, что я не самая горячая задница в округе?"
    show zoe neutral
    mc.c "Погоди, я ничего такого о тебе не говорю. Просто не хочу пользоваться пьяной девушкой, вот и всё."
    show zoe thinking
    zoe.c "О-о~ Какой безупречный джентльмен. Мама бы гордилась."
    show zoe mad talk
    zoe.c "Я думала, ты крутой."
    show zoe mad
    "Я правда не знаю, что теперь сказать."
    mc.c "Ну, э-э... Наверное, извини."
    show zoe mad talk
    zoe.c "Прощаю... {b}Если{/b}!"
    show zoe tease talk
    call playMusic(sexyTheme) from _call_playMusic_255
    zoe.c "Прямо сейчас отвезёшь меня к себе~"
    show zoe tease
    "Горячая, напористая девушка злится, что я {b}не{/b} переспал с ней."
    menu:
        "Хочу ли я отвезти её домой?"
        "Да":
            pass
        "Нет":
            "Мне совсем не по себе..."
            mc.c "Мне лестно, но... я правда не могу."
            show zoe surprise
            zoe.c "...!"
            "Она смотрит на меня в полном шоке, будто я совершил нечто немыслимое."
            "Похоже, ей нечасто отказывают, если вообще когда-нибудь. Такая смелая девушка — и ей отказали в случайном сексе."
            show zoe mad talk
            zoe.c "Бездикое чмо."
            hide zoe with dissolve
            "С этими словами она оставляет напиток и вылетает из бара."
            "Не знаю... Всё произошло так быстро, она была такой напористой... Что-то было не так."
            "Не знаю, конец ли это... Может, при новой встрече что-нибудь изменится?"
            return
    "Можете считать меня психом, но во всей этой ситуации... Есть что-то чертовски горячее."
    mc.c "*Кхм* Ну, э-э, конечно, {b}мадам{/b}."
    show zoe mad talk
    zoe.c "Только не вздумай потом за это расплачиваться."
    show zoe mad
    "Наверное, я идиот, но не могу не поддразнить её."
    scene black with fade
    "Она манит меня пальцем, и мы встаём и уходим. Шагает она так, будто до сих пор по-настоящему злится."
    "Хорошо, что я живу рядом, а то настроение могло бы пройти."
    $ location_home.showBackground()
    "Мы заходим внутрь, и она почти силком тащит меня за руку к кровати."
    show zoe tease talk
    zoe.c "Надеюсь, у тебя там есть чем похвастаться после того, как заставил меня столько ждать."
    show zoe tease
    mc.c "А если нет?"
    show zoe tease talk
    zoe.c "Не волнуйся, у меня на такие вещи хороший нюх."
    show zoe mad talk
    zoe.c "А теперь снимай одежду."
    show zoe mad
    "[zoe.name] с лёгкостью толкает меня на спину. В этих руках скрывается обманчивая сила..."
    "Никогда раньше у меня не было такой... напористой девушки. И я совсем не против."
    "Я мигом раздеваюсь. Не стыдно ли, что у меня уже стоит?"
    "Я и заметить не успеваю, как [zoe.name] сбрасывает с себя последние лоскутки одежды."
    image zoe cowgirl start = Image("images/characters/zoe/hscenes/cowgirl/start.webp")
    scene zoe cowgirl start with fade
    pause
    zoe.c "О-хо~ Весьма впечатляет, [mc.name]~"
    "Она ухмыляется, глядя на мой член, уже стоящий по стойке смирно в предвкушении."
    zoe.c "Обычно я не ошибаюсь в таких вещах. Ты уже готов ко мне. Хороший мальчик."
    mc.c "Рад оправдать ожидания."
    zoe.c "Делаешь вид, что сопротивляешься, а сам хочешь этого не меньше меня, да?"
    mc.c "Не стану отрицать."
    zoe.c "Ну что ж, готовься к лучшему сексу в жизни."
    "[zoe.name] забирается на кровать и начинает оседлывать меня."
    image zoe cowgirl start2 = Image("images/characters/zoe/hscenes/cowgirl/start2.webp")
    scene zoe cowgirl start2 with fade
    pause
    "Она кладёт руку мне на грудь и направляет член, чтобы сесть на него. Я вздрагиваю, когда вижу, как острые когти приближаются к особо чувствительным местам..."
    zoe.c "Не переживай, красавчик, я буду нежной~"
    "Говорит она угрожающе..."
    "Она наваливается на меня. Глядя на неё снизу вверх, я чувствую, какая она сильная."
    "Даже когда я едва сжимаю её бедро, понимаю: ноги у неё в отличной форме."
    zoe.c "Последнее предупреждение, худыш: как только этот поезд тронется, остановить его уже не получится."
    "Тёплое влажное прикосновение к головке говорит, что всё началось — хотела я этого или нет."
    image zoe cowgirl part 1 = Movie(play="images/characters/zoe/hscenes/cowgirl/part1.webm")
    show zoe cowgirl part 1 with fade
    pause
    "Она кладёт руки мне на бёдра и с неожиданной силой опускается на член."
    zoe.c "О-о-ох~ Блядь, хороший размер."
    mc.c "Без прелюдии?"
    zoe.c "Сразу к самому интересному. Блядь~"
    "Её упругие ягодицы подпрыгивают на моих бёдрах. С каждым толчком она с силой вдавливает меня в кровать."
    "Шлепки наших бёдер разносятся по комнате. Не знал, что удар о мех звучит именно так."
    "Мягкая щетина её меха трётся о моё бедро, контрастируя с силой, с которой она на меня наседает."
    zoe.c "Посмотри на своё лицо... Нравится, красавчик?"
    mc.c "Д-да... чёрт."
    image zoe cowgirl part 2 = Movie(play="images/characters/zoe/hscenes/cowgirl/part2.webm")
    show zoe cowgirl part 2 with fade
    pause
    "Она полностью берёт инициативу в свои руки и использует меня как игрушку для секса. Не будь её задница такой упругой, она бы скользила по всей длине моего члена."
    zoe.c "О-ох~ А-а-а~ Я могла бы привыкнуть к этому члену."
    "Её удивительно большая грудь начинает покачиваться прямо перед моим лицом."
    "Она уверенно ухмыляется, глядя на меня."
    "И ещё на ней остался ошейник... Горячо."
    "Я не хочу просто лежать без дела. Кладу руки ей на талию и начинаю отвечать ей с той же силой."
    image zoe cowgirl part 3 = Movie(play="images/characters/zoe/hscenes/cowgirl/part3.webm")
    show zoe cowgirl part 3 with fade
    pause
    zoe.c "О-О-О, БЛЯДЬ~ ДА-А-А~"
    zoe.c "Вот теперь-то ты понял, [mc.name]. Трахни меня пожёстче!"
    mc.c "Не собирался отдавать тебе полный контроль."
    zoe.c "Смелый мальчик... *Ха-а-а* Продолжай~"
    "Шлепки бёдер становятся громче, слышно, как мы хлюпаем."
    "Даже её хвост начинает вилять. Она хватается за мои руки, и когти снова привлекают моё внимание."
    zoe.c "Да-а~ ДА-А~"
    image zoe cowgirl part 4 = Movie(play="images/characters/zoe/hscenes/cowgirl/part4.webm")
    show zoe cowgirl part 4 with fade
    pause
    "Я крепко обхватываю её бёдра и подаюсь вверх."
    "Столкновения с этой обманчиво тяжёлой девушкой — это нечто..."
    zoe.c "Блядь, лучший член за ПОСЛЕДНИЕ ГОДЫ~"
    mc.c "Не ожидал от тебя таких комплиментов. Ты всем парням так говоришь?"
    zoe.c "Я *ха-а* ценю хороший член, когда нахожу такой~"
    zoe.c "Продолжай в том же духе, жеребец, и, может, я *ха-а-а* ещё раз тебя использую~"
    "От таких безостановочных толчков я долго не продержусь."
    zoe.c "Блядь, ты заставишь меня кончить~"
    zoe.c "Готовься~"
    image zoe cowgirl part 5 = Movie(play="images/characters/zoe/hscenes/cowgirl/part5.webm")
    show zoe cowgirl part 5 with fade
    pause
    "Она наклоняется вперёд и с силой прижимает мои плечи к кровати."
    "Оседлав меня, она ускоряется ещё сильнее, гоняя членом по всей длине."
    mc.c "О-о-ох, чёрт~ [zoe.name]~"
    zoe.c "Да, блядь~ Лежи и принимай~"
    zoe.c "Прими это, чёртов любитель меха~"
    zoe.c "*Ха-а* *Ха-а*"
    "Её дыхание тяжелеет, уверенная ухмылка исчезает."
    "Она больше не смотрит на меня — от удовольствия закатывает глаза."
    zoe.c "Бо-о-оже~ Чёрт возьми~"
    image zoe cowgirl part 6 = Movie(play="images/characters/zoe/hscenes/cowgirl/part6.webm")
    show zoe cowgirl part 6 with fade
    pause
    mc.c "Так хорошо, да?"
    zoe.c "Не... *ха-а* Зазнавайся~"
    mc.c "Не лучше ли было бы сейчас напиться?"
    zoe.c "Блядь, да ни за что~"
    zoe.c "ЭТО ЛУЧШЕЕЕ~"
    "Никогда раньше меня так не оседлывали, полностью отняв контроль."
    "Это... чертовски горячо."
    mc.c "Чёрт... [zoe.name]..."
    zoe.c "Потерпи, жеребец... *Ха-а-а* Я почти..."
    "Я больше не могу сдерживаться. Её дыхание учащается."
    "Я бы и вытащить его не смог, даже если бы захотел..."
    mc.c "Я сейчас...!"
    zoe.c "ДА-А~ *А-АХ* КОНЧАЙ~"
    image zoe cowgirl end = Image("images/characters/zoe/hscenes/cowgirl/end.webp")
    scene zoe cowgirl end with fadewhite
    pause
    zoe.c "А-а-а-а~"
    "[zoe.name] всем весом вдавливает мой член и грудь в матрас."
    "Я ничего не могу поделать и кончаю, прижатый к кровати."
    "[zoe.name] дрожит от наслаждения и упивается экстазом."
    zoe.c "Да-а-а~ Наполни меня~"
    "..."
    "Она сидит на мне, пока мы жадно ловим ртом воздух."
    "Наши соки смешиваются между бёдер, от тел исходит жар."
    zoe.c "*Ха-а* *Ха-а* Неплохо... худыш..."
    call stopMusic from _call_stopMusic_48
    scene zoepillowtalk with fade
    pause
    "Наконец она всё же скатывается с меня."
    mc.c "Это было... мощно..."
    zoe.c "Мне нравится пожёстче, жеребец~"
    zoe.c "Чёрт... Обычно парни не заставляют меня кончать так быстро."
    mc.c "Смело признаёшься."
    zoe.c "Ладно, ладно. Не задирай нос."
    "Мы несколько мгновений сидим и пытаемся отдышаться."
    scene black with fade
    "[zoe.name] садится и натягивает одежду, разбросанную по полу."
    "Я всё ещё сижу на кровати и удивляюсь, как быстро она застегнула юбку и собралась уходить."
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_256
    show zoe smile with dissolve
    zoe.c "Неплохо я тебя встряхнула, да, сладенький?"
    mc.c "Было здорово."
    show zoe tease talk
    zoe.c "Не ври. Лучший секс в твоей жизни, держу пари."
    show zoe tease
    mc.c "Можешь немного остаться, если хочешь."
    show zoe thinking
    zoe.c "Не-а, не люблю эти разговоры после секса. Я сваливаю."
    "Я встаю, чтобы догнать её, пока она не убежала."
    mc.c "О, ладно. Я позвоню тебе или вроде того, ага?"
    show zoe smile talk
    zoe.c "Буду ждать~"
    show zoe smile
    "Я наклоняюсь к ней, надеясь на поцелуй."
    call stopMusic from _call_stopMusic_49
    "Вместо этого она вежливо отталкивает меня за плечо."
    show zoe thinking
    zoe.c "Эй-эй, не надо, [mc.name]."
    show zoe neutral talk
    zoe.c "Не порть хорошее времяпровождение, принимая всё слишком серьёзно."
    show zoe neutral
    "Я немного удивлён. Вообще-то, сердце слегка сжимается. Даже после всего произошедшего это ощущается как отказ."
    "Она вместо этого просто хлопает меня по заднице."
    show zoe tease talk
    zoe.c "Неплохо потрахались. Жду от тебя новых подвигов."
    show zoe tease
    "Я в замешательстве. Меня только что оттрахали и бросили? Использовали и выбросили?"
    "Даже после отличного секса я чувствую себя немного не по-мужски."
    show zoe smile talk
    zoe.c "Ещё увидимся, жеребец."
    hide zoe with dissolve
    "Вильнув хвостом и подмигнув через плечо, [zoe.name] уходит так же быстро, как и появилась."
    "..."
    "Что, чёрт возьми, только что произошло?"

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return {'location':location_home}

label zoeLikeEvent2(fromGallery):
    $ location_shop.showBackground()
    call playMusic(chillTheme) from _call_playMusic_257
    "Просто зашёл в магазин за парой мелочей."
    "Но кого я замечаю в одном из проходов?"
    show zoe thinking with dissolve
    "[zoe.name]. Мы нормально общались, несколько раз проводили время вместе, и даже переспали, хотя тогда мне показалось, что она меня отшила."
    "Похоже, для неё это просто секс. Друзья с привилегиями? Наши «свидания» — флирт, а потом, возможно, трах."
    "Свободные взгляды на секс, раскрепощённость, ничего серьёзного — наверное, меня это устраивает."
    "Дурак, что постоянно пытался быть романтиком. Справлюсь."
    "Она меня ещё не заметила. Я хотел поздороваться, но что-то меня останавливает... Понаблюдаю немного."
    zoe.c "..."
    "Она внимательно разглядывает товары, что-то берёт с полки, читает этикетки и возвращает обратно, или..."
    show zoe bashful
    "...смотрит на цены? Как бы то ни было, она очень придирчиво выбирает."
    "И что у неё за выражение лица? Она обыскивает полки с какой-то особой тщательностью."
    show zoe thinking
    zoe.c "..."
    "Она достаёт из кармана кошелёк, там лежит несколько мелких монет."
    "Разложив их на ладони, она перебирает монеты длинными накрашенными когтями."
    show zoe sad
    zoe.c "*Вздыхает*"
    show zoe bashful
    "Тяжело вздохнув, она закрывает кошелёк, возвращает товар на полку и направляется к кассе."
    "Она экономит или просто разумно распоряжается деньгами? С её-то диким характером трудно представить её жмотом."
    "Погоди... Она сейчас без работы. Говорила, что денег пока хватит, но вдруг ей трудно?"
    "Может, она просто придерживается бюджета, а может, у неё и правда дела плохи."
    "Надо... сделать вид, будто я ничего не заметил, и поздороваться."
    mc.c "[zoe.name]! Привет!"
    show zoe surprise
    zoe.c "!"
    show zoe smile talk
    zoe.c "О-ох, привет, красавчик. Какая встреча."
    show zoe smile talk 2
    zoe.c "Сегодня не управляешь своей старой дырой?"
    show zoe smile
    mc.c "Может, зайду попозже. Ещё не решил."
    mc.c "Как ты?"
    show zoe neutral talk
    zoe.c "Э-э... нормально. Сегодня ничего особенного, просто купила домой кое-что."
    show zoe neutral
    "Кассир пробивает её покупки, и я вижу, что она выбрала."
    "Консервы и самые простые продукты. Настоящий бюджетный набор. Дешёвые товары длительного хранения — макароны, крупы..."
    "Ничего особо интересного."
    show zoe tease talk
    zoe.c "Вообще-то, вчера с девчонками дико тусили, так что сегодня надо бы отдохнуть."
    zoe.c "Не вздумай ничего себе напридумывать, жеребец."
    show zoe tease
    mc.c "Чёрт, опять облом."
    show zoe smile talk
    zoe.c "В следующий раз повезёт, красавчик."
    show zoe smile
    "Кассир пробивает её покупки. Там всего несколько вещей."
    unknown2 "С вас $19.24, пожалуйста, мисс."
    "Я легонько толкаю её и подмигиваю. Ей не понравилось, что я назвал её {b}мисс{/b}."
    show zoe mad
    "Она бросает на меня пренебрежительный взгляд и снова вежливо улыбается кассиру."
    show zoe neutral
    "Она протягивает двадцатидолларовую купюру. Может, я бы не придал этому значения, если бы раньше не заметил её у полок, но..."
    "Мне показалось, что она замялась, протягивая купюру. Даже слегка поморщилась."
    unknown2 "Спасибо, приходите ещё."
    show zoe neutral talk
    zoe.c "Спасибо."
    show zoe neutral
    "Мог бы я предложить заплатить? Нет, это было бы чересчур. И жутковато."
    "Деньги — болезненная тема. Полагаю, у неё есть гордость."
    mc.c "Эй, подожди меня. У меня всего пара вещей."
    show zoe smile talk
    zoe.c "Ладно."
    hide zoe with dissolve
    "Я быстро складываю покупки в пакет и выхожу."
    scene black with fade
    $ location_town.showBackground()
    show zoe tease talk with dissolve
    zoe.c "Собрался проводить меня домой, мой белый рыцарь-худыш? Ха-ха."
    show zoe tease
    mc.c "Вообще-то..."
    mc.c "У тебя в сумке нет скоропортящихся продуктов? Не спешишь донести покупки домой?"
    show zoe neutral talk
    zoe.c "...Нет...? А что?"
    show zoe neutral
    mc.c "Не хочешь заглянуть в кафе? Выпить кофе и съесть пирожное или вроде того?"
    mc.c "И да, можешь считать это скучным. Просто захотелось перекусить, а ты тут, вот и..."
    show zoe bashful talk
    zoe.c "...Э-э, ладно..."
    show zoe bashful
    mc.c "Я тоже угощаю. За мой счёт."
    show zoe tease talk
    zoe.c "Ого, что это? Обычно мне приходится сжимать тебе яйца, чтобы добиться такого обращения."
    show zoe tease
    mc.c "Эй, вовсе нет! Я обычно почти не сопротивляюсь... Ну, в основном..."
    show zoe tease talk
    zoe.c "Хе-хе, ну, в этот раз ты прав. Некоторые мужики, господи, такие нервные из-за денег."
    zoe.c "Раз ты угощаешь, придётся согласиться. Сегодня твой счастливый день."
    show zoe tease
    mc.c "Круто!"
    scene black with fade
    "Пара минут прогулки за угол — и мы устраиваемся в кафе."
    $ location_cafe.showBackground()
    show zoe smile with dissolve
    "Я беру нам кофе и по паре пирожных — одно несладкое, другое сладкое."
    show zoe smile talk
    zoe.c "О, чёрт, вот это да! Целый пир~ С радостью съем."
    show zoe smile
    "Она без колебаний принимается за пирожное."
    "Будто маска на миг сползла. Я вижу, как она по-настоящему наслаждается чем-то, без флиртующей надменности — искренней или наигранной."
    "Это... мило."
    "Она поднимает взгляд и ловит меня за тем, что я на неё смотрю."
    show zoe mad talk
    zoe.c "Ты чего уставился?"
    show zoe mad
    mc.c "О-ох, ничего. Вкусно?"
    show zoe neutral talk
    zoe.c "Да... сойдёт. Ешь уже своё, чудак."
    show zoe neutral
    "Я откусываю. Здесь и правда вкусно."
    "Надо как-то аккуратно подвести разговор к этой теме."
    mc.c "Уже придумала, где искать следующую работу?"
    call playMusic(sadTheme) from _call_playMusic_258
    show zoe bashful talk
    zoe.c "Ох, господи, только не ты тоже."
    show zoe bashful
    mc.c "Я тоже?"
    show zoe bashful talk
    zoe.c "Родители в последнее время не отстают с этим вопросом."
    zoe.c "Так что от тебя мне этого тоже не надо, спасибо большое."
    show zoe bashful
    "Она не злится, как я ожидал. Скорее... раздражена?"
    mc.c "Прости, не буду лезть, если не хочешь. Просто хотел узнать, не присмотрела ли ты что-нибудь."
    show zoe sad talk
    zoe.c "А... Неважно."
    show zoe sad
    "..."
    "Кажется, она хочет что-то сказать."
    show zoe sad talk
    zoe.c "Просто..."
    show zoe bashful talk
    zoe.c "Чёрт... Я просто не могу сейчас об этом думать."
    show zoe thinking
    zoe.c "Последние работы были дерьмом. ПОЛНЫМ."
    zoe.c "Никуда не деться: работать — отстой, и точка. Приходится выбирать лучшее из всего плохого."
    zoe.c "Начальники — придурки, коллеги — тупые, работа — скучная."
    show zoe tease talk
    zoe.c "Такая девушка, как я, должна быть свободна и расправить крылья, да?"
    zoe.c "Может, мне просто нужен богатый муж, хотя это и хреновый вариант..."
    show zoe tease
    mc.c "С деньгами всё нормально? Пока что?"
    show zoe bashful talk
    zoe.c "А-а~ Не переживай за меня, жеребец. Всё будет в порядке."
    show zoe neutral talk
    zoe.c "Что это ты вдруг такой искренний? Перестань."
    show zoe neutral
    "Я стараюсь посмотреть на неё с сочувствием, но не снисходительно и не с жалостью."
    zoe.c "..."
    "До неё что-то доходит."
    show zoe surprise
    zoe.c "Погоди, ты ведь ничего не заметил, верно?"
    mc.c "Ну, э-э..."
    show zoe mad talk
    zoe.c "В магазине? Как я читала каждую ценник, будто от этого жизнь зависит? Конечно, заметил."
    zoe.c "Чёрт, мы поэтому сюда пришли?"
    show zoe mad
    mc.c "Нет, нет, я просто подумал..."
    show zoe mad talk
    zoe.c "Подумал, что бедную девушку надо спасать? Хватит, [mc.name], мне ничего не нужно."
    show zoe mad
    mc.c "Ладно, я заметил. Подумал, что тебе, возможно, сейчас тяжело. Знаю, время такое, всякое бывает."
    show zoe bashful talk
    zoe.c "Да, ладно, у меня есть бюджет. И что, это разрушает твой образ меня?"
    zoe.c "Думаешь, я несчастный щенок, которому подаяние нужно? Нет уж."
    show zoe bashful
    "Как я думал, это пройдёт? Я подозревал, что у неё есть гордость. Люди в такой ситуации легко принимают всё на свой счёт."
    "Я видел такое на прежней работе. Бар иногда едва держался на плаву, но бывший начальник не принимал помощи."
    "Я уже задел её. Ну, мех взъерошил. Раз уж задумал помочь, надо идти до конца."
    "Это может всё изменить."
    mc.c "Я просто хотел предложить тебе пару смен в баре. Если хочешь."
    call playMusic(heartTheme) from _call_playMusic_259
    show zoe surprise
    mc.c "Можешь попробовать. Сотрудники приходят и уходят, в основном это молодые работники на полставки, так что график гибкий. Бери столько смен, сколько захочешь."
    mc.c "Работа не такая уж плохая. С местными у меня проблем не было. Часто тихо, но расходы покрываем."
    mc.c "И обещаю, я не «начальник-придурок»."
    zoe.c "..."
    "Она смотрит на меня с таким удивлением, какого я от неё ещё не видел."
    mc.c "Или... нет, если не хочешь. Я пойму. Может, это и правда странно..."
    show zoe neutral talk
    zoe.c "Ты серьёзно?"
    show zoe neutral
    mc.c "Да."
    zoe.c "..."
    show zoe neutral talk
    zoe.c "Даже после того, как я... рассказала, чем закончились все мои прошлые работы?"
    show zoe neutral
    mc.c "А почему бы и нет? Можем попробовать. Никому не обязательно сразу принимать окончательное решение, а дополнительные руки никогда не помешают."
    show zoe bashful
    "..."
    "Она и правда обдумывает предложение. Я думал, она сразу отмахнётся."
    show zoe bashful talk
    zoe.c "Я..."
    zoe.c "Спасибо, что подумал обо мне..."
    "Сейчас будет «но»."
    show zoe thinking
    zoe.c "...Дай мне подумать."
    mc.c "О, да, конечно."
    "..."
    "..."
    "Повисает неловкая тишина. Эта тема не располагает к лёгкой беседе."
    "Мы уже доели."
    show zoe neutral talk
    zoe.c "Спасибо за кофе. Я пойду."
    show zoe neutral
    mc.c "Конечно, [zoe.name]. Рад был тебя увидеть."
    show zoe neutral talk
    zoe.c "[mc.name]... Спасибо. Я подумаю."
    hide zoe with dissolve
    "Она резко хватает сумку и уходит. Не выглядела ни злой, ни расстроенной, но была совсем не такой, как обычно."
    "Я действительно поставил её в неловкое положение. Может, зря так начал этот разговор."
    "Неужели я всё испортил?"

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return {'location':location_cafe}


label zoeLikeEvent3(fromGallery):
    $ location_park.showBackground()
    "[zoe.name] позвала меня поговорить."
    "Её сообщение с предложением встретиться было гораздо суше, чем обычно. Обычно она обязательно вставляет какую-нибудь колкость в мой адрес."
    "Нетрудно догадаться, о чём речь. О работе."
    "Мы виделись после того, как я предложил ей работу, но никто из нас об этом не заговаривал. Как я и сказал, дал ей время подумать."
    "Удивительно, что она отнеслась к этому так серьёзно и взвешенно."
    "Я ожидал либо «А почему бы и нет?», либо «Да ни за что на свете»."
    "Вообще-то я бы предпочёл, чтобы она не воспринимала это так серьёзно. Я предложил без обязательств — просто «попробуй»."
    show zoe neutral talk with dissolve
    call playMusic(heartTheme) from _call_playMusic_260
    zoe.c "[mc.name]."
    show zoe neutral
    mc.c "Привет, [zoe.name]."
    zoe.c "..."
    mc.c "..."
    "Неловко. Обычно всю беседу ведёт она. Она невероятная экстравертка."
    mc.c "Как дела?"
    show zoe thinking
    zoe.c "...Нормально."
    zoe.c "..."
    show zoe neutral talk
    zoe.c "Ох~ Ладно, я веду себя глупо. Очевидно же, зачем мы здесь."
    show zoe neutral
    mc.c "Ага."
    show zoe bashful talk
    zoe.c "С чего бы начать?"
    show zoe neutral talk
    zoe.c "У меня ещё есть вопросы."
    show zoe neutral
    mc.c "Конечно, спрашивай."
    show zoe neutral talk
    zoe.c "Во-первых. Ты и так ясно всё объяснил, но..."
    zoe.c "Ты серьёзно?"
    show zoe neutral
    mc.c "Абсолютно. Всё, что я сказал."
    show zoe neutral talk
    zoe.c "Любые смены, без обязательств?"
    show zoe neutral
    mc.c "Если не сработается, ничего страшного. Я не против."
    show zoe mad talk
    zoe.c "И я буду полноценной сотрудницей, да? Не засунешь меня на задний двор мыть стаканы?"
    show zoe mad
    mc.c "Ну, этим понемногу занимается каждый, но все делают разную работу. Те, кто в смене, договариваются между собой."
    mc.c "Я доверяю всем сотрудникам, и всё работает как надо."
    zoe.c "..."
    show zoe bashful talk
    zoe.c "И... ты будешь мне платить?"
    show zoe bashful
    mc.c "Что?! Ха-ха, конечно буду. О чём ты вообще?"
    zoe.c "..."
    show zoe neutral talk
    zoe.c "Ну ладно... Остался последний вопрос."
    zoe.c "Почему?"
    show zoe neutral
    mc.c "Я по закону обязан выплачивать зарплату своим сотрудни-"
    show zoe mad talk
    zoe.c "Нет, идиот. Почему ты предложил работу именно мне?"
    show zoe mad
    mc.c "Ты сказала, что у тебя туго с деньгами, а мне не помешают сотрудники. Почему бы и нет?"
    mc.c "Всё довольно просто."
    zoe.c "..."
    show zoe bashful
    zoe.c "..."
    show zoe neutral talk
    zoe.c "Ладно... Просто не понимаю. Ты уже оказался у меня в штанах... Не надо ничего придумывать."
    show zoe neutral
    mc.c "Я ничего не придумываю. Вообще-то, это скорее {b}ты{/b} залезла ко мне в {b}штаны{/b}. Я там почти ничего не решал."
    show zoe tease
    zoe.c "Хе-хе~"
    show zoe thinking
    zoe.c "Наверное..."
    mc.c "Послушай, я и сам бывал в такой ситуации. Не раз. Знаю, как это паршиво. Почему бы мне не помочь?"
    show zoe mad
    mc.c "И прежде чем ты скажешь что-то ещё: это не из жалости. Просто так сложились обстоятельства. Друг помогает другу, потому что может."
    show zoe neutral
    mc.c "Если переживаешь насчёт меня как начальника, можешь спросить ребят. Можем даже прямо сейчас туда пойти."
    show zoe thinking
    zoe.c "Вообще-то, я уже спросила их однажды вечером. Сказали, у нас спокойно."
    show zoe smile talk
    zoe.c "Один даже сказал, что это лучшая работа в его жизни. Правда, он довольно молодой."
    show zoe smile
    mc.c "А, это тот, кому я заплатил за отзыв."
    show zoe smile talk 2
    zoe.c "Да-да, ладно, заткнись. Я поняла."
    show zoe bashful
    zoe.c "..."
    "Она на несколько мгновений задумывается, прокручивая всё в голове."
    "Но, кажется, постепенно смягчается. На лице появляется лёгкая улыбка, плечи расслабляются."
    "У денег есть такая сила. Предложение работы, когда у тебя трудности, может ошеломить — но и относиться к нему легкомысленно не стоит."
    show zoe thinking
    zoe.c "Ладно, с деньгами туговато, и я устала от вечных нотаций родителей."
    zoe.c "И уверена, что мой идиот-арендодатель вот-вот повысит плату. Так что..."
    show zoe neutral talk
    zoe.c "Я... соглашусь на работу. Э-э... Пожалуйста..."
    show zoe neutral
    "«Пожалуйста»? Она ещё никогда не была такой вежливой."
    call playMusic(funnyTheme) from _call_playMusic_261
    mc.c "Отлично! Сейчас скину тебе ссылку на форму, которую надо заказать..."
    zoe.c "..."
    "На эту удочку она не клюёт."
    mc.c "Хе, ладно, шучу."
    show zoe smile talk
    zoe.c "Да ну, я не дура."
    show zoe smile
    "Обычная колкость, но тёплая улыбка. Будто гора с плеч свалилась."
    "Она выглядит необычно... милой. Даже симпатичной."
    mc.c "Вот видишь, всё будет хорошо."
    "Не успеваю себя остановить..."
    hide zoe with dissolve
    show zoe pat animated with dissolve
    pause
    zoe.c "..."
    "Она ошарашенно смотрит на меня."
    "..."
    zoe.c "Какого хрена ты творишь?"
    mc.c "Э-э... Утешаю тебя?"
    mc.c "Ну-ну~"
    zoe.c "..."
    zoe.c "У тебя три секунды, чтобы убрать от меня руку..."
    mc.c "Это одно из условий. Привилегия начальника."
    zoe.c "..."
    hide zoe with dissolve
    show zoe neutral with dissolve
    "Чувствуя, как её взгляд становится всё тяжелее, я отступаю."
    show zoe tease talk
    zoe.c "Любопытный способ домогаться до сотрудницы, босс. Я скорее ожидала, что мне придётся отсосать тебе за стойкой или что-то вроде того."
    show zoe tease
    "Вот она, прежняя [zoe.name]..."
    mc.c "Не в таком солидном заведении, как наше."
    show zoe tease talk
    zoe.c "Хм-хм, посмотрим."
    show zoe smile talk
    zoe.c "Ладно, с этой неловкой хернёй покончено. Я пошла."
    show zoe smile
    mc.c "Скажи, когда захочешь выйти на первую смену, я всё улажу с ребятами."
    show zoe smile talk
    zoe.c "...Увидимся, [mc.name]."
    hide zoe with dissolve
    "Уверенно махнув рукой через плечо, она скрывается за углом."
    "Вскоре я увидел эту другую сторону [zoe.name]. Будто она не верит, что к ней могут относиться по-доброму без скрытого умысла."
    "Надеюсь, я не ошибся. Вдруг она окажется ужасной сотрудницей..."
    "Ладно, посмотрим, как пойдёт."

    if(not fromGallery):
        python:
            zoe.job = 'Бармен'
            zoe.preferredMondaySchedule = [location_shop, location_bar, location_bar, location_bar]
            zoe.preferredTuesdaySchedule = [location_shop, location_bar, location_bar, location_town]
            zoe.preferredWednesdaySchedule = [location_away, location_cafe, location_diner, location_beach]
            zoe.preferredThursdaySchedule = [location_beach, location_park, location_bar, location_bar]
            zoe.preferredFridaySchedule = [location_cafe, location_bar, location_diner, location_town]
            zoe.preferredSaturdaySchedule = [location_town, location_beach, location_park, location_away]
            zoe.preferredSundaySchedule = [location_away, location_beach, location_diner, location_away]
        "Теперь Зои работает в твоём баре! Она будет чаще там появляться."
        $ zoe.addLike(1)
        $ zoe.addLove(2)

    return

label zoeHEvent2(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_262
    "Прошло некоторое время с тех пор, как [zoe.name] устроилась в бар."
    "И, несмотря ни на что, у неё отлично получается."
    show zoehevent2i1 with fade
    "Она резкая, не слишком профессиональная, немного беззаботная..."
    "Но, честно говоря, у нас тут атмосфера совсем не такая."
    "У нас простое местное заведение для местных жителей. Ну, кроме меня, пожалуй."
    "Если я не пристаю к ней с требованиями, она спокойно работает. Кажется, ей нравится заниматься чем-то практическим, а не бюрократической ерундой."
    "Кажется, среди посетителей она одна из самых популярных сотрудниц."
    "У неё настоящий талант располагать к себе: кокетливо подмигнуть, отпустить комплимент. Как популярная пышногрудая красотка, работающая в деревенском трактире."
    "Иногда я даже ловлю себя на лёгкой ревности..."
    "Но её непринуждённое поведение не меняется, даже если формально я её начальник."
    $ location_bar.showBackground()
    show zoe smile talk with dissolve
    zoe.c "Посторонись, жеребец. Ты мешаешь."
    show zoe smile
    "Она оттесняет меня бедром и проходит мимо."
    "Она права, я стою на пути. Просто любуюсь ею, разинув рот."
    "Когда она такая уверенная, временами будто командует всем вокруг — это невероятно... горячо."
    "Похоже, всё сложилось идеально. Хорошая сотрудница, и сама она довольна. Она берёт больше смен, чем я ожидал."
    show zoe mad talk
    zoe.c "Чего уставился? Иди стаканы помой или ещё что-нибудь."
    show zoe mad
    "Так кто тут начальник?"
    scene black with fade
    "Обычный день проходит без происшествий."
    "Вечер подходит к концу. Осталась пара пожилых посетителей — наверное, тянут время, чтобы не возвращаться к семьям."
    "Боже, не дай мне к их возрасту превратиться в такого несчастного человека..."
    $ location_bar.showBackground()
    "Теперь тихо, но мы должны работать ещё какое-то время."
    "Я отпустил остальных. Остались только мы с Зои."
    show zoe neutral with dissolve
    "Зои подходит сзади и слегка шлёпает меня по заднице. Для неё это обычное дело..."
    show zoe smile talk
    zoe.c "Ну что, теперь тихо?"
    show zoe smile
    mc.c "Хорошо поработала сегодня, Зои."
    show zoe neutral talk
    zoe.c "Ага, ты тоже."
    show zoe neutral
    mc.c "Ты точно раньше этим не занималась? Удивительно быстро освоилась."
    show zoe mad talk
    zoe.c "Конечно уверена. Зачем мне врать, идиот?"
    show zoe neutral talk
    zoe.c "Я же говорила, что работала в сфере обслуживания. Всё одно и то же: бар, ресторан, магазин."
    show zoe neutral
    mc.c "Ты тут как рыба в воде. Я правда впечатлён."
    show zoe bashful
    zoe.c "..."
    show zoe bashful talk
    zoe.c "Спасибо..."
    show zoe smile talk
    zoe.c "Просто это место получше всех тех работ, вот и всё."
    zoe.c "Да и ты ничего, не соврал."
    show zoe smile
    mc.c "А ты продала себя дешевле, чем стоишь. Мы оба в выигрыше."
    mc.c "В общем, на сегодня, кажется, больше нечего делать. В такое позднее время и в этот день недели редко кто заходит."
    mc.c "Можешь уйти пораньше, если хочешь. Ты заслужила."
    show zoe thinking
    zoe.c "Хм, пожалуй, могу..."
    mc.c "Может, встретишься сегодня с подружками или вроде того?"
    zoe.c "Не-а... Я сказала им, что занята. Кажется, они сегодня тоже ничего не планируют."
    mc.c "Прости, что задерживаю."
    show zoe smile talk
    zoe.c "Нет, всё нормально. Мне тут даже... нравится."
    show zoe tease talk
    zoe.c "Не пытаешься от меня избавиться?"
    show zoe tease
    mc.c "Можешь задержаться. Мне нравится, как ты усердно работаешь, пчёлка-труженица, вся такая услужливая."
    "За это я снова получаю тычок в рёбра."
    show zoe smile talk
    zoe.c "Заткнись, худыш."
    show zoe smile
    "..."
    "Мягкие мелодии из динамиков разносятся по почти пустому залу. В углу осталась пара посетителей, повернувшихся спиной и тихо беседующих."
    "Промежутки заполняет тихий шум улицы за окном."
    "Делать нечего... Иногда такие моменты даже полезны. Нам не нужно слишком много клиентов."
    "Как и обещала, Зои не воспользовалась предложением уйти пораньше. В глубине души она удивительно старательная."
    call playMusic(sexyTheme) from _call_playMusic_263
    "Я чувствую, как Зои за моей спиной меняет позу. И вдруг ощущаю руку у себя на бедре."
    "Я оборачиваюсь. Зои стоит вплотную за моей спиной и смотрит мне прямо в лицо."
    mc.c "Э-э?.."
    show zoe smile talk
    zoe.c "Что такое, красавчик?"
    show zoe smile
    "Она снова меня дразнит. Рука скользит по моей талии, пальцы опускаются к паху."
    "Приятно, но... Прямо здесь? Насколько далеко она зайдёт?"
    "За барной стойкой нас не видно, а последние посетители сидят к нам спиной и потягивают напитки."
    mc.c "Ты..."
    show zoe tease
    zoe.c "Хм-м?.."
    "Она продолжает тереть мой пах, и выпуклость уже невозможно не заметить. Не уверен, что смогу сопротивляться."
    mc.c "О, ничего. Наверное, мне показалось."
    show zoe tease talk
    zoe.c "Вот как~ Наверное, ты переутомился, [mc.name]."
    show zoe tease
    "Член встаёт в рекордные сроки, вот-вот вырвется из брюк. Она проводит пальцами к ширинке и начинает расстёгивать её."
    "Понимаю, что она ждёт от меня реакции, но решаю не поддаваться."
    zoe.c "О-о~?"
    image zoe bar handjob part 1 = Movie(play="images/characters/zoe/hscenes/barhandjob/part1.webm")
    show zoe bar handjob part 1 with fade
    pause
    "Неизбежное происходит: мой член вываливается из брюк и чуть не задевает стойку."
    zoe.c "Хм-хм~"
    "Зои наклоняется совсем близко и тихонько смеётся. По крайней мере, старается вести себя незаметно."
    zoe.c "Ну и что это у нас?"
    "Она обхватывает мой ствол парой пальцев и медленно начинает дрочить."
    "Крепко положив руку мне на плечо, она полностью обвела меня вокруг пальца."
    mc.c "Что именно? Не понимаю, о чём ты, Зои."
    zoe.c "Да? Значит, нам обоим кажется...?"
    image zoe bar handjob part 2 = Movie(play="images/characters/zoe/hscenes/barhandjob/part2.webm")
    show zoe bar handjob part 2 with fade
    pause
    "Трудно сосредоточиться хоть на чём-то. Я стараюсь сохранять видимость спокойствия. Формально мы в общественном месте."
    mc.c "Наверное. Может, пойдёшь отдохнёшь дома?"
    zoe.c "Уверена, ты не хочешь, чтобы я это сделала, босс."
    "Чёрт, как же горячо."
    image zoe bar handjob part 3 = Movie(play="images/characters/zoe/hscenes/barhandjob/part3.webm")
    show zoe bar handjob part 3 with fade
    pause
    "Она сжимает сильнее, и по спине пробегает дрожь. Как я вообще должен стоять вот так?"
    "Теперь она двигает рукой быстрее, проводит по всей длине. Невероятное ощущение."
    zoe.c "Ой, кажется, я не вытерла этот стаканчик внизу~ Дай протру."
    "Она просто обожает меня дразнить... Ничего не может с собой поделать."
    "Но в этот раз я не жалуюсь..."
    "Учитывая обстоятельства, вряд ли она может возражать, если я тоже её полапаю..."
    image zoe bar handjob part 4 = Movie(play="images/characters/zoe/hscenes/barhandjob/part4.webm")
    show zoe bar handjob part 4 with fade
    pause
    "Я тянусь и хватаю её за упругую задницу."
    zoe.c "Хм-хм... Тебе нравится то, что ты там нащупал?"
    mc.c "Просто... помогаю."
    #
    pause
    "Продолжая ускоряться, она явно хочет выдоить меня досуха прямо за стойкой."
    "Ощущения невероятные, но я боюсь, что нас поймают. Для владельца это был бы настоящий скандал."
    "К счастью, это скоро закончится — я уже на пределе."
    mc.c "Э-э, Зои..."
    zoe.c "Да-а~?"
    "Она ухмыляется. Прекрасно знает, что происходит."
    image zoe bar handjob part 5 = Movie(play="images/characters/zoe/hscenes/barhandjob/part5.webm")
    show zoe bar handjob part 5 with fade
    pause
    "Она уже движется на полной скорости. Ощущения переполняют меня."
    "Я вот-вот кончу, стоя за собственной барной стойкой."
    mc.c "Зои..."
    zoe.c "Да, сэр~"
    "Её шёпот мне на ухо доводит меня до края."
    pause
    image zoe bar handjob end = Image("images/characters/zoe/hscenes/barhandjob/end.webp")
    scene zoe bar handjob end with fadewhite
    pause
    "Я даже не пытаюсь прикрыться и заливаю спермой всю заднюю часть стойки."
    "Мне удаётся сдержать большую часть стонов, но я всё равно содрогаюсь от удовольствия и кончаю прямо на месте."
    mc.c "Чёрт..."
    zoe.c "О-хо~"
    "Она крепко сжимает мой член и выжимает из меня каждую каплю, пока я совсем не обессилеваю."
    zoe.c "Посмотри, какой ты устроил бардак... Теперь сам и убирай, босс."
    $ location_bar.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_264
    show zoe tease talk with dissolve
    zoe.c "Хе-хе, знала, что тебе нравится динамика «начальник-подчинённая». Видел бы ты своё лицо."
    zoe.c "Но если захочешь ещё, придётся это заслужить."
    zoe.c "Главной буду я."
    show zoe tease
    mc.c "А там казалось, что главная именно ты..."
    show zoe tease talk
    zoe.c "Вот подожди и увидишь~"
    show zoe smile talk
    zoe.c "Ладно, воспользуюсь предложением уйти пораньше, жеребец."
    "Она без особого старания вытирает руки тряпкой и бросает её мне."
    zoe.c "Пока, красавчик~"
    hide zoe with dissolve
    "Самодовольно ухмыляясь, она выходит за дверь и машет на прощание оставшимся посетителям."
    "А мне остаётся убирать этот бардак... Эх..."

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return


label zoeHEvent3(fromGallery):
    $ location_bar.showBackground()
    call playMusic(heartTheme) from _call_playMusic_265
    "Дела идут отлично."
    "Пожалуй, с тех пор как я стал владельцем, всё ещё ни разу не работало так гладко."
    "Мы получаем прибыль, постоянных клиентов всё больше, и, похоже, местным у нас нравится."
    "Никаких катастроф — тьфу-тьфу, — да и стресса не так много."
    "Чёрт, даже подработка дома обычно была тяжелее, а теперь я управляю всем заведением."
    "Неужели я превращаюсь в ленивого начальника, который только пожинает плоды? Мне кажется, я вношу свою долю..."
    "В любом случае, одна из причин успеха — отличные сотрудники..."
    show zoe neutral with dissolve
    "Зои — отличный тому пример."
    "Она ворчит и строит из себя недовольную сменами, но на деле очень трудолюбива и чертовски хороша в работе."
    "У неё к этому настоящий талант. Правда, принимать искренние комплименты ей не очень нравится. Наверное, это не «круто»."
    "Думаю, ей больше хотелось бы, чтобы я просто сказал, какая она горячая."
    "И с флиртом она могла бы немного сбавить обороты... Возможно."
    "Она берёт больше смен, чем когда-либо, и меня это полностью устраивает."
    "Мы договорились «посмотрим, как пойдёт», но она уже работает здесь почти столько, сколько может."
    "Ей нужны деньги? Или ей и правда здесь нравится? Надеюсь, этой работы хватит, чтобы выбраться из финансовой ямы."
    "Кстати о деньгах... Когда бар приносит хорошую прибыль, я стал выдавать сотрудникам премии."
    "Мы всё ещё улучшаем здание, интерьер, обстановку и прочее. Некоторым вещам давно нужен серьёзный ремонт."
    "Но если остаётся приличная сумма, я добавляю ребятам немного сверх обычной зарплаты."
    "Я сам много лет был на их месте и знаю, как важны такие приятные сюрпризы."
    mc.c "Эй, Зои, ещё немного побудешь?"
    show zoe neutral talk
    zoe.c "Да, до конца смены по расписанию, {b}босс{/b}."
    show zoe tease talk
    zoe.c "Не хочу, чтобы ты считал меня бездельницей."
    show zoe tease
    mc.c "Я и не сомневался, Зои. Ты одна из лучших, как я постоянно и говорю."
    show zoe smile talk
    zoe.c "Да ладно, худыш, я не настолько хороша."
    show zoe mad talk
    zoe.c "Тебе самому разве некуда идти? Займись делом."
    show zoe mad
    mc.c "Кажется, нет. Ты, как всегда, тут всё крепко держишь в руках."
    show zoe neutral
    zoe.c "Хм..."
    mc.c "Кстати, это тебе."
    "Я протягиваю ей конверт. Внутри немного денег. Не целое состояние, но приличная доля месячной зарплаты."
    show zoe mad talk
    zoe.c "А? Что это? Меня увольняют?"
    show zoe mad
    mc.c "Конечно нет. С чего бы после всего, что я только что сказал?"
    mc.c "В конце месяца, если бар приносит прибыль, я выдаю небольшую премию."
    mc.c "Все работают неполный день и могут скоро уйти, поэтому ежегодных премий нет. Просто немного сверху, когда дела идут хорошо."
    show zoe surprise
    zoe.c "Погоди, правда? Премия?"
    mc.c "Конечно. Я делаю так уже какое-то время, а с твоим приходом дела идут ещё лучше."
    mc.c "Вот... за твою тяжёлую работу."
    show zoe smile talk
    zoe.c "Ничего себе... Спасибо, жеребец. Не ожидала."
    show zoe smile
    "Она открывает конверт и перебирает купюры."
    "Её глаза расширяются, когда она видит сумму. Последнее время мы хорошо поработали."
    show zoe surprise
    zoe.c "Ничего себе! Ты серьёзно?"
    mc.c "Конечно. Ты заслужила. Вы все заслужили."
    show zoe joy
    zoe.c "{b}Боже мой!{/b}"
    "К моему удивлению, она бросается ко мне и обнимает."
    hide zoe with dissolve
    show zoe hug with dissolve
    zoe.c "Вот чёрт! Спасибо, [mc.name]!"
    zoe.c "Блядь! Ты чертовски классный, знаешь?"
    "Ничего себе. Искренность от Зои. Кто бы мог подумать."
    "Непривычное чувство... Погоди. Мы вообще раньше обнимались?"
    "Кажется, Зои замечает, что я молчу. Её лицо резко меняется, когда она осознаёт, что делает."
    hide zoe with dissolve
    show zoe bashful talk with dissolve
    zoe.c "*Кхм* Э-э, спасибо, худыш, это правда помогает."
    show zoe bashful
    "Ничего себе. Кажется, ей и правда неловко, что на мгновение слетела эта суровая маска."
    mc.c "Конечно, без проблем. Просто часть прибыли возвращается тем, кто её заработал."
    show zoe tease talk
    zoe.c "О-о, ты уверен, что это не небольшая {b}мотивация{/b} для любимой сотрудницы?"
    zoe.c "За кое-какую {b}услугу{/b}~ Ах ты хитрец..."
    show zoe tease
    mc.c "Нет, просто премия за хорошо сделанную работу."
    show zoe surprise
    mc.c "Мне ещё надо пересчитать пару конвертов. Оставлю тебя с этим."
    zoe.c "А?"
    hide zoe with dissolve
    "Я оставляю её разбираться с деньгами. Она явно немного ошарашена."
    "Неужели она правда не привыкла к хорошему отношению? Может, прошлые работы и правда были дерьмовыми."
    "К счастью, к стойке подходит клиент, так что ей будет чем заняться."
    call stopMusic from _call_stopMusic_50
    scene black with fade
    "Я некоторое время занимаюсь разными мелочами в баре."
    "Проверяю краны, кеги."
    scene barcellar with fade
    "В подвале довольно грязно."
    "Это одна из многих вещей, которые нужно привести в порядок. Но это обойдётся в целую кучу денег."
    "В другой раз..."
    "Я проверяю запасы, но по большей части просто убиваю время. Наверху дел немного."
    "Потом слышу, как кто-то спускается по лестнице."
    show zoe smile with dissolve
    mc.c "О, привет, Зои. Проверял кое-что."
    zoe.c "..."
    "Она молча смотрит на меня и подходит ближе."
    "С этой угрожающей улыбкой..."
    mc.c "Всё в порядке, Зои?"
    "Она продолжает приближаться, загоняя меня к стене."
    call playMusic(sexyTheme) from _call_playMusic_266
    image zoe bar blowjob start 1 = Image("images/characters/zoe/hscenes/barblowjob/start1.webp")
    scene zoe bar blowjob start 1 with fade
    pause
    "Она становится вплотную, нависает надо мной и опирается рукой о стену."
    zoe.c "Значит, босс любит баловать своих сотрудниц?"
    zoe.c "И ты хочешь сказать, что делаешь это от чистого сердца? Ну-ну..."
    zoe.c "Ни за что не поверю."
    "Судя по её лицу, она просто дурачится. Иногда трудно понять..."
    mc.c "Он любит заботиться о своих людях."
    zoe.c "Мне кажется, босс хочет получить награду для себя. Изображает спасителя всех вокруг."
    zoe.c "И знаешь что? Думаю, он её заслужил. Как считаешь?"
    "От этих слов я неловко сглатываю. Она умеет звучать угрожающе, что бы ни говорила."
    mc.c "*Кхм* Ну, может, и заслужил..."
    "Господи, я совсем не умею флиртовать."
    zoe.c "Хмпф~"
    "Зои только ухмыляется и тихонько смеётся."
    image zoe bar blowjob start 2 = Image("images/characters/zoe/hscenes/barblowjob/start2.webp")
    scene zoe bar blowjob start 2 with fade
    pause
    "Медленно проведя рукой по моей груди, она опускается на колени и подносит морду к моему паху."
    "Молниеносно расстёгивает мне ремень."
    zoe.c "Какая жестокость: начальник домогается до сотрудницы. Подкупает её ради ответных услуг. Злоупотребляет властью~"
    "Она говорит так, будто сама сейчас не собирается мной помыкать."
    "Лучше не сказать ничего глупого и не испортить момент."
    image zoe bar blowjob part 1 = Movie(play="images/characters/zoe/hscenes/barblowjob/part1.webm")
    show zoe bar blowjob part 1 with fade
    pause
    "Не теряя времени, Зои жадно берёт мой член в рот, каким-то образом сохраняя самодовольную ухмылку."
    "Мой член исчезает в её длинной морде... Господи, блядь."
    mc.c "Ох, чёрт..."
    zoe.c "М-мфф, м-мф~"
    "Как ей удаётся смеяться надо мной и говорить с таким снисхождением, когда у неё во рту мой член?"
    "Эта девушка рушит все мои ожидания."
    "У неё во рту так тепло и неожиданно тесно... Наверное, дело в форме морды."
    "Её язык скользит вверх-вниз по всей длине."
    image zoe bar blowjob part 2 = Movie(play="images/characters/zoe/hscenes/barblowjob/part2.webm")
    show zoe bar blowjob part 2 with fade
    pause
    "Это невероятно. Она так меня наказывает за то, что я вроде как ждал благодарности, или просто играет?"
    "Я уже не могу её остановить — слишком хорошо."
    mc.c "Господи, Зои..."
    zoe.c "М-м-мм~"
    "Несмотря на постоянное стремление доминировать, она знает, как доставить удовольствие..."
    image zoe bar blowjob part 3 = Movie(play="images/characters/zoe/hscenes/barblowjob/part3.webm")
    show zoe bar blowjob part 3 with fade
    pause
    "Вдруг она опускает руки мне на ноги и начинает загонять член глубже в горло."
    "Быстрее, глубже, сильнее — будто она пытается поглотить меня целиком."
    mc.c "О-о-ох, чёрт~"
    zoe.c "*Кх* *Кх*"
    "Влажные звуки от моего члена, исследующего её горло, разносятся по подвалу."
    "Она даже расстегнула топ, чтобы показать свои прелести."
    "Хвост за ней так и виляет..."
    image zoe bar blowjob part 4 = Movie(play="images/characters/zoe/hscenes/barblowjob/part4.webm")
    show zoe bar blowjob part 4 with fade
    pause
    "Она смотрит мне прямо в глаза. Вот это зрелище."
    "Это она начала и теперь старается довести меня до оргазма в рекордный срок..."
    "Держу пари, ей нравится демонстрировать свои навыки."
    mc.c "Чёрт, Зои, я сейчас..."
    zoe.c "М-м~ *кх* М-мфф~"
    "Её руки сжимают крепче, а рельефные плечи двигаются вверх-вниз."
    "Я на пределе. Что же она собирается делать?"
    mc.c "Зои, я..."
    "Она не останавливается, решив выдоить меня досуха."
    image zoe bar blowjob end 1 = Image("images/characters/zoe/hscenes/barblowjob/end1.webp")
    scene zoe bar blowjob end 1 with fadewhite
    pause
    "Не сбавляя темпа, она принимает член целиком, и я кончаю ей глубоко в горло."
    "Меня продолжает трясти, колени подкашиваются, пока она высасывает из меня всё до капли."
    mc.c "О-о-ох, блядь~"
    "После нескольких движений я совсем пуст. Она отстраняется, оставляя после себя беспорядок."
    image zoe bar blowjob end 2 = Image("images/characters/zoe/hscenes/barblowjob/end2.webp")
    scene zoe bar blowjob end 2 with fade
    pause
    zoe.c "*Ха-а* Вот это ты выдал, здоровяк~"
    zoe.c "Понравилось, да?"
    mc.c "Даже не представляешь."
    zoe.c "О, ещё как представляю."
    "Она слизывает каплю спермы с уголка рта."
    zoe.c "Повезло тебе, жеребец. Я не каждому такое делаю."
    mc.c "Похоже, придётся оставить тебя при себе."
    zoe.c "Хе~"
    call playMusic(barTheme) from _call_playMusic_267
    scene barcellar with fade
    show zoe tease with dissolve
    "Зои встаёт, облизывая губы и самодовольно улыбаясь — явно довольна своей работой."
    "Она использует меня как хочет. Честно говоря, я не могу ей сопротивляться."
    "Но и мужскую гордость надо беречь. Я не могу всё время быть в проигрыше."
    mc.c "Ладно, ладно, мне уже надоело, что ты мной помыкаешь."
    show zoe tease talk
    zoe.c "Хотела бы я посмотреть, как ты попробуешь что-то с этим сделать, худыш."
    show zoe tease
    mc.c "К твоему несчастью, ты допустила ошибку."
    show zoe tease talk
    zoe.c "Да? Рассказывай~"
    show zoe tease
    mc.c "Ты показала свою... слабость."
    show zoe smile talk 2
    zoe.c "Блефуешь."
    show zoe smile
    mc.c "Ничего подобного. Есть один простой способ, и он точно сработает. Вот так..."
    "Я притягиваю её к себе и обнимаю."
    show zoe surprise
    hide zoe with dissolve
    show zoe hug with dissolve
    pause
    "Сначала, как я и предполагал, это её немного удивляет."
    "Но затем она смягчается, понимая, что это и было всё."
    mc.c "Видишь? Ты полностью обездвижена."
    "Она тепло улыбается. Всё ещё кокетничает, но в ней больше нежности, чем обычно."
    zoe.c "И это всё?"
    mc.c "Очевидно, в твоём репертуаре такого приёма нет."
    zoe.c "Да-да, ладно. Поймал меня, романтик."
    zoe.c "Не знаю, что на меня нашло. Наверное, конверт с деньгами..."
    zoe.c "Хитрый приём."
    mc.c "Я не специально, но теперь, когда знаю, берегись. Буду тебя обнимать."
    zoe.c "Фу-у..."
    "Она так не думает... Надеюсь."
    hide zoe with dissolve
    show zoe smile talk with dissolve
    zoe.c "*Вздыхает* Я так и знала, что ты немного размазня, раз так упрашивал меня переспать с тобой."
    zoe.c "Но... ты не так уж плох."
    show zoe smile
    mc.c "Стоило усилий?"
    show zoe neutral talk
    zoe.c "Смотри не зазнавайся..."
    show zoe neutral
    "Она, как обычно, легонько шлёпает меня по заднице."
    show zoe tease talk
    zoe.c "Думаю, мы ещё можем повеселиться."
    show zoe tease
    mc.c "И обниматься вдоволь."
    show zoe bashful
    zoe.c "..."
    hide zoe with dissolve
    "Немного покраснев, она разворачивается и поднимается по лестнице."
    "И напоследок покачивает бёдрами и хвостом, устраивая мне небольшое шоу."

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return


label zoeHEvent4(fromGallery):
    $ location_bar.showBackground()
    call playMusic(heartTheme) from _call_playMusic_268
    "Сегодня здесь творился настоящий хаос."
    "Забился пивной шланг, внезапно закончились несколько товаров, пришлось менять смену из-за болезни..."
    "Было напряжённо. Слава богу, всё позади, мы закрываемся."
    "На ночь остаёмся только я, Зои и ещё один сотрудник. Несмотря на обстоятельства, они отлично справились."
    "Честно говоря, лучше меня. Я теряюсь при малейших неприятностях. Может, я вообще годен для этой работы?"
    show zoe neutral talk with dissolve
    zoe.c "Я там всё закончила. Запереть дверь в подвал?"
    show zoe neutral
    mc.c "Ага, спасибо, Зои."
    zoe.c "М-м."
    hide zoe with dissolve
    "Она скрывается за углом, чтобы закончить уборку."
    "И всё же она на удивление образцовая сотрудница. Не то чтобы она принимала комплименты."
    "Фух, сегодня я был на взводе."
    show zoe tease talk with dissolve
    zoe.c "Ой, ну посмотри на себя, худыш. Весь на нервах."
    show zoe tease
    "Зои появляется из-за угла."
    show zoe tease talk
    zoe.c "Да не было {b}всё настолько{/b} плохо. Расслабься."
    show zoe tease
    mc.c "Да-да, знаю. Ты отлично со всем справилась. Спасибо."
    show zoe thinking
    zoe.c "Ой, да ладно. Пошли уже из этой дыры."
    mc.c "Эй, дыра?"
    "Я знаю, что она дразнится, поэтому только ухмыляюсь."
    show zoe smile talk
    zoe.c "Хе-хе, вот так. Забудь об этом. Будь мужиком."
    show zoe smile
    "В такие дни её беззаботность очень помогает."
    "Она умеет успокаивать — в духе «да какая разница»."
    scene black with fade
    "Мы идём к двери запирать заведение."
    if(not fromGallery):
        $ timeOfDay = 'Evening'
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_269
    show zoe smile with dissolve
    mc.c "Хорошая работа сегодня."
    zoe.c "М-м."
    "Мы отправляемся домой."
    "Мы живём в одном направлении, но редко идём домой вместе. Обычно она куда-нибудь уходит с друзьями."
    mc.c "Есть планы? Сегодня куда-нибудь пойдёшь?"
    show zoe thinking
    zoe.c "Не-а, сегодня нет..."
    "Я жду продолжения. Обычно она рассказывает, как они оторвались прошлой ночью."
    mc.c "Нет? Редкость."
    show zoe mad talk
    zoe.c "А? Да нет. Ты говоришь так, будто я алкоголичка."
    show zoe mad
    mc.c "А разве нет?"
    "В ответ получаю сердитый взгляд и резкий тычок в рёбра."
    show zoe smile talk
    zoe.c "Ой, заткнись..."
    zoe.c "Раз уж тебе {b}обязательно{/b} нужно знать, худыш, я {b}решила{/b} сегодня не идти, хотя меня звали."
    show zoe smile
    mc.c "О, поумнела, остепенилась? Отказалась от жизни оторвы?"
    show zoe mad
    zoe.c "Гр-р-р..."
    "Она бывает страшной... Но я знаю, что шутки она понимает."
    show zoe bashful talk
    zoe.c "А-а~ Вот какой ты любопытный. Просто немного коплю, сам знаешь. Клубы дорогие."
    show zoe bashful
    "Я немного переживаю — и как друг, и как работодатель. У неё всё ещё проблемы с деньгами?"
    mc.c "Ох... Прости. Тебе зарплаты не хватает? Ты ведь и так берёшь много смен."
    show zoe surprise
    zoe.c "О, нет-нет, я не это имею в виду."
    show zoe bashful talk
    zoe.c "С деньгами всё нормально. Я просто..."
    zoe.c "Немного откладываю. Хочу снять жильё получше."
    show zoe bashful
    "Мы живём в одном направлении, но я до сих пор не был у Зои. Она даже не говорит мне адрес."
    show zoe bashful talk
    zoe.c "И, кажется, скоро смогу это сделать. Нужно ещё немного подкопить, понимаешь?"
    show zoe bashful
    mc.c "О, здорово. У тебя совсем ужасное жильё? Ты ни разу не разрешила мне прийти."
    show zoe neutral talk
    zoe.c "Ужасное. Район — отстой, дом разваливается, ещё и комнату делю с соседями."
    show zoe smile talk
    zoe.c "Но, похоже, теперь я смогу позволить себе отдельное жильё."
    show zoe smile talk 2
    zoe.c "Если только ты не собирался уволить меня в ближайшее время. Ты ведь не {b}посмеешь{/b}, жеребец?"
    show zoe smile
    mc.c "Даже не думал. Ты моя звезда."
    show zoe smile talk 2
    zoe.c "Фу. Никогда больше так не говори."
    show zoe smile
    "Мы оба смеёмся. Она никогда не перестаёт меня поддевать."
    "Мы идём дальше в комфортном молчании. Прохладный ветерок освежает нас после дня в помещении."
    "Немного погодя Зои наконец заговаривает."
    show zoe smile talk 2
    zoe.c "После такого дня тебе нужно расслабиться. У тебя дома есть что-нибудь крепкое?"
    show zoe smile
    mc.c "Кажется, найдётся что-то из твоего любимого... А что?"
    show zoe tease talk
    zoe.c "Пошли выпьем. Тебе надо расслабиться."
    show zoe tease
    mc.c "Я думал, ты сегодня не собиралась тусоваться."
    show zoe tease talk
    zoe.c "Я и не собиралась {b}никуда идти{/b}. У тебя дома свободно!"
    show zoe tease
    "Она легонько толкает меня плечом."
    mc.c "Пожалуй, не отказался бы от крепкого напитка."
    mc.c "Только не выпей всё, ладно?"
    show zoe tease talk
    zoe.c "Ничего не обещаю..."
    scene black with fade
    "Мы продолжаем идти домой, болтаем и вскоре оказываемся у меня."
    $ location_home.showBackground()
    "Мы заходим, и Зои тут же скидывает туфли, отправляя их в полёт через комнату, а сама плюхается на диван как хозяйка."
    show zoe joy
    zoe.c "А-а~ Надеюсь, когда-нибудь у меня тоже будет такой диван. Ты бы видел тот, что у меня дома..."
    show zoe smile talk 2
    zoe.c "Налей мне выпить, а?"
    show zoe smile
    "Она щёлкает пальцами, ожидая, с понимающей улыбкой."
    mc.c "Конечно, мадам~"
    scene black with fade
    "Я наливаю нам по напитку, и мы какое-то время отдыхаем на диване."
    "Включаем какую-то ерунду по телевизору и расслабляемся с напитками и беседой."
    scene zoehevent4i1 with fade
    "В конце концов Зои устраивается поудобнее и вытягивается на диване."
    "Она кладёт ноги мне на колени и смотрит телевизор."
    "Обычно она такая общительная и дерзкая. Приятно видеть, как она расслабляется."
    "Наверное, ей со мной комфортно. Меньше притворства — больше искренности."
    "У нас всё было несерьёзно. Мы встречаемся, но скорее как друзья с привилегиями. Хорошо, что работа у меня не изменила наших отношений."
    "Мы гуляли, проводили время вместе и трахались, но, кажется, впервые она пришла просто поваляться."
    "Но я поспешил с выводами..."
    call playMusic(sexyTheme) from _call_playMusic_270
    image zoe footjob part 1 = Movie(play="images/characters/zoe/hscenes/footjob/part1.webm")
    show zoe footjob part 1 with fade
    pause
    "Зои начинает тереться ступнями о меня. Они уже лежат у меня на коленях и скользят к паху."
    "Я бросаю на неё взгляд, но она продолжает смотреть телевизор. Только ухмылку я всё же замечаю."
    "И не могу не... попасться на её уловку."
    mc.c "Зои?.."
    zoe.c "М-м-м~?"
    "Она слегка ухмыляется и смотрит на меня с пониманием. Ей нравится, что она делает."
    "Её пальцы играют у меня на паху, а острые когти слегка царапают ткань брюк."
    "Немного страшно, но эротично."
    image zoe footjob part 2 = Movie(play="images/characters/zoe/hscenes/footjob/part2.webm")
    show zoe footjob part 2 with fade
    pause
    "У меня уже начинает выпирать. Она трёт меня ступнями вверх-вниз."
    mc.c "Что ты задумала?"
    zoe.c "Не знаю. После сегодняшнего дня ты всё ещё {b}напряжён{/b}. Тебе надо расслабиться."
    mc.c "А, так ты {b}знаешь{/b}, что делаешь. Я и так был совершенно спокоен, спасибо."
    zoe.c "О? Значит, моя помощь тебе не нужна?"
    mc.c "Ну... Я не говорил..."
    zoe.c "М-м-хм~"
    "Она тихо смеётся. Я, как обычно, у неё в руках."
    "Она не останавливается. Наоборот, мне очень приятно. Хочу, чтобы она продолжала."
    show zoe footjob part 1 with fade
    pause
    "Она чувствует, что я уже почти каменный."
    zoe.c "Знаю, что я хороша, но ты правда сейчас кончишь в штаны, жеребец?"
    mc.c "Не хотелось бы, да?"
    "Я начинаю расстёгивать молнию на брюках. Хочу почувствовать её напрямую."
    image zoe footjob part 3 = Movie(play="images/characters/zoe/hscenes/footjob/part3.webm")
    show zoe footjob part 3 with fade
    pause
    "Мой член выскакивает из брюк и тут же оказывается зажат между ступнями Зои."
    "Одной подошвой она сжимает его снизу, другой — сверху, скользя ступнями вверх-вниз по члену."
    zoe.c "О-о~ Гляньте, кто выбрался поиграть."
    mc.c "Я могу выдержать только определённое количество поддразниваний."
    "Удивительно шелковистый короткий мех на её ступнях легко скользит по всей длине моего ствола."
    "А вместе с лёгкими прикосновениями подушечек ощущения совершенно особенные."
    "Её пальцы сгибаются, разминая мою плоть, полностью во власти Зои."
    image zoe footjob part 4 = Movie(play="images/characters/zoe/hscenes/footjob/part4.webm")
    show zoe footjob part 4 with fade
    pause
    zoe.c "Ха~ Как мило. Не забывай, я не пропускаю день ног. Одно неловкое движение — и я раздавлю твоего бедолагу."
    mc.c "А что за неловкое движение?"
    zoe.c "Хм-м~ Сейчас придумаю... Например... Не трогать."
    mc.c "Ты издеваешься..."
    zoe.c "Ха-ха~ Ты мой~"
    "Мне остаётся откинуться и наслаждаться тем, как умело и изящно Зои работает ступнями."
    "Кто бы мог подумать, что это будет так... горячо?"
    zoe.c "Кажется, парню хочется ещё?"
    mc.c "Ещё бы."
    zoe.c "Только если попросишь."
    mc.c "...Пожалуйста, Зои..."
    zoe.c "Хороший мальчик~"
    image zoe footjob part 5 = Movie(play="images/characters/zoe/hscenes/footjob/part5.webm")
    show zoe footjob part 5 with fade
    pause
    "Зои приподнимается, зажимая мой член подошвами."
    "Она быстро скользит ступнями вверх и вниз, крепко обхватывая и слегка выкручивая член."
    mc.c "О-ох, блядь..."
    zoe.c "Посмотри на себя — завёлся из-за одних ступней. Как мерзко~"
    mc.c "Не понимаю, как можно этому сопротивляться. Ты всем парням такое делаешь?"
    zoe.c "Хотел бы знать, худыш?"
    "Юбка задралась почти до талии, потому что она устроилась в совершенно неженственной позе."
    "От трения нарастает жар, а ступни всё скользят от основания к головке."
    "Каким-то образом это так же эффективно, как любой секс в моей жизни. Я уже почти кончаю."
    mc.c "Зои..."
    zoe.c "Давай закончим..."
    mc.c "Я кончаю!"
    image zoe footjob end = Image("images/characters/zoe/hscenes/footjob/end.webp")
    scene zoe footjob end with fadewhite
    pause
    "Когда меня накрывает экстаз, Зои накрывает головку члена ступнёй."
    "Огромная порция спермы выстреливает прямо ей на подошву и пальцы, забрызгивая всю ступню."
    zoe.c "Ха! Посмотри на себя. Боже мой~"
    mc.c "Господи... Как ты это сделала?"
    zoe.c "Тебя так легко довести до оргазма, милый. Совсем не по-мужски."
    mc.c "А это поведение, по-твоему, очень женственное?"
    zoe.c "Я куда женственнее, чем ты можешь вынести, худыш."
    "Сперма стекает по стволу, а Зои рисует небольшой круг на головке моего члена."
    mc.c "Чёрт..."
    zoe.c "Вот это беспорядок."
    "Вообще-то, она предотвратила куда больший бардак. Неожиданно заботливо..."
    $ location_home.showBackground()
    show zoe smile talk
    call playMusic(funnyTheme) from _call_playMusic_271
    zoe.c "Боже, [mc.name], видел бы ты своё лицо."
    zoe.c "Весь завёлся из-за ступней? Какая мерзость."
    show zoe smile
    mc.c "Как жестоко. Надеюсь, ты ничего такого обо мне не подразумеваешь."
    mc.c "Ну а как иначе... Ты же знаешь, что делаешь."
    show zoe smile talk 2
    zoe.c "Я? Да брось, жеребец. Просто научись себя контролировать."
    zoe.c "А то в следующий раз начнёшь вести себя как зверь."
    show zoe smile
    "Могу говорить что угодно, но это было чертовски горячо."
    "Для Зои всё было довольно сдержанно. Я почти ждал продолжения."
    "Честно говоря, мне мало."
    show zoe tease talk
    zoe.c "Ну, посмотри на время. Пожалуй, мне пора~"
    show zoe tease
    "А?"
    "А мы разве не..."
    mc.c "Э-э... Правда?"
    show zoe tease talk
    zoe.c "Да, у тебя был {b}долгий{/b} день. Дам тебе отдохнуть."
    show zoe tease
    mc.c "Ты... уходишь?"
    show zoe tease talk
    zoe.c "А что, ты хотел, чтобы я осталась?"
    show zoe tease
    mc.c "Ну..."
    show zoe tease talk
    zoe.c "Ах, шалун! Но знаешь что..."
    zoe.c "Мне кажется, будет забавно оставить тебя в таком виде."
    show zoe tease
    mc.c "Неужели..."
    show zoe tease talk
    zoe.c "Ещё как~"
    "Быстро вытеревшись, она надевает туфли."
    "Она и правда уходит. Просто чтобы жестоко меня подразнить."
    show zoe smile talk 2
    zoe.c "Спасибо за выпивку, жеребец."
    zoe.c "Увидимся на работе, ага?"
    show zoe smile
    mc.c "Я..."
    hide zoe with dissolve
    "Она берёт сумочку и сама выходит из дома."
    "А я остаюсь сидеть с вытащенным членом, который так и не получил разрядки."
    "Как она могла..."
    "Вот дразнилка."

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return {'location':location_home}

label zoeHEvent5(fromGallery):
    scene diner with fade
    show zoe smile with dissolve
    call playMusic(chillTheme) from _call_playMusic_272
    "После смены мы с Зои идём вместе поужинать."
    "На этот раз она сама меня пригласила... Это редкость, но мне приятно."
    "Может, она ко мне привыкает... В романтическом смысле. Можно надеяться."
    "Она сексуальная и кокетливая, но романтики пока сторонится. Никаких нежностей..."
    "Возможно, это не в её духе. А мне бы хотелось. Может, я не того жду от этих отношений? Неужели у нас ничего не получится?"
    "Лучше просто наслаждаться тем, что есть, и не накручивать себя."
    "За ужином она тоже выпивает несколько бокалов. Что-то празднует или пытается заглушить тревогу?"
    "Хотя выглядит вполне весёлой."
    show zoe smile talk 2
    zoe.c "...Короче, Мелисса в клубе весь вечер клеилась к какому-то парню и не отходила от него на танцполе."
    zoe.c "Мне он показался мутным типом, но, видимо, это её вкус. Ей всегда нравятся медведи и прочие крупные ребята."
    show zoe tease talk
    zoe.c "Господи, эта стерва такая отчаявшаяся..."
    show zoe smile talk
    zoe.c "Остальные хотели домой, но она всё ещё липла к тому парню."
    show zoe neutral talk
    zoe.c "Я не хотела просто бросить её там. Мы же этого парня не знаем."
    show zoe smile talk 2
    zoe.c "Мы уже собирались вытащить её оттуда, как вдруг..."
    show zoe tease talk
    zoe.c "Парня вырвало прямо перед ней! Он забрызгал ей туфли и всё остальное."
    zoe.c "Господи, это было так мерзко~"
    show zoe tease
    mc.c "Зои, мы вообще-то за ужином..."
    show zoe smile talk 2
    zoe.c "Ой, да брось, жеребец. Ты же выдержишь."
    show zoe smile
    mc.c "Не уговариваешь ты меня ходить в клубы. Для меня это звучит как сущий ад."
    show zoe thinking
    zoe.c "Значит, в ближайшее время я тебя в клуб не затащу?"
    mc.c "Не затащишь. Прости, это просто не моё."
    show zoe tease talk
    zoe.c "Уверен? Кто знает, чем я там занимаюсь... Мужчины обычно такие собственники."
    zoe.c "А если кто-нибудь начнёт ко мне подкатывать?"
    show zoe tease
    mc.c "...Ты хочешь сказать, что сейчас ты крутишь только со мной?"
    show zoe surprise
    zoe.c "...!"
    "Её это на мгновение ошеломляет. Я думал, мы просто дурачимся."
    show zoe bashful talk
    zoe.c "Кто знает..."
    show zoe bashful
    "Редкий случай, когда Зои теряется. Обычно её так просто не смутишь."
    "Интересно, что это значит."
    "Она немного ковыряется в еде."
    show zoe surprise
    zoe.c "Ой, чёрт, забыла тебе сказать!"
    mc.c "Надеюсь, ничего плохого?"
    show zoe thinking
    zoe.c "Нет-нет, новости."
    show zoe neutral talk
    zoe.c "То место, о котором я говорила? Квартира, которую сдают."
    zoe.c "Кажется, это была шестая квартира, которую я посмотрела."
    show zoe neutral
    mc.c "Ага, та, что тебе пока больше всего понравилась?"
    show zoe neutral talk
    zoe.c "Да. Аренда чуть дороже, чем я хотела, но..."
    show zoe smile talk
    zoe.c "Я её сняла."
    show zoe smile
    "Её лицо озаряет улыбка — радостная, но ещё и облегчённая. Чёрт знает, я её понимаю."
    mc.c "Боже мой! Здорово! Потрясающе!"
    mc.c "Поздравляю, правда. Отличное чувство, да? Если не считать мерзкого арендодателя, которому теперь достанутся твои деньги."
    show zoe smile talk 2
    zoe.c "Да, к этому я привыкла. Обычно я ненавижу переезжать, но... в этот раз всё иначе."
    zoe.c "Мне и правда нравится квартира. И жить там буду одна. Даже жду этого."
    show zoe smile
    mc.c "И правильно. Это же прекрасно. За тебя!"
    "Я поднимаю бокал за Зои."
    call playMusic(heartTheme) from _call_playMusic_273
    show zoe bashful talk
    zoe.c "Хе-хе, спасибо..."
    show zoe bashful
    mc.c "Что-то случилось?"
    show zoe bashful talk
    zoe.c "Нет, всё нормально... Просто..."
    show zoe neutral talk
    zoe.c "Это благодаря тебе, знаешь. Ты взял меня на работу и заботишься обо мне."
    zoe.c "Я... хочу тебя поблагодарить. Не знаю как. Я тебе благодарна, но чувствую себя обязанной, и не понимаю, чем отплатить."
    show zoe neutral
    mc.c "Не глупи, ты мне ничего не должна. Я нанял тебя, потому что мне нужны сотрудники, а ты отлично справляешься."
    mc.c "Вот и всё. Новую квартиру ты снимаешь на деньги, которые сама заработала, а не благодаря мне."
    mc.c "Я рад за тебя."
    show zoe bashful
    zoe.c "..."
    "Она правда не умеет принимать такие комплименты. Почему она такая?"
    show zoe bashful talk
    zoe.c "Ладно... Но всё равно..."
    show zoe smile talk
    zoe.c "Спасибо. Правда. Огромное спасибо."
    show zoe smile
    mc.c "Я ничего особенного не сделал, но пожалуйста. Рад, что у тебя всё налаживается."
    show zoe smile talk 2
    zoe.c "Хотя бы позволь мне сегодня заплатить за ужин. Я угощаю."
    show zoe smile
    mc.c "Погоди, я знаю, чем это оборачивается. Огромный залог, повышение аренды, комиссия агенту, плюс переезд..."
    mc.c "Это всё дорого. Побереги деньги. Сегодня я плачу — будем праздновать."
    show zoe neutral talk
    zoe.c "Но..."
    show zoe neutral
    mc.c "Вообще-то, прости, что не пригласил тебя в место получше. Если бы я знал, что мы празднуем..."
    show zoe mad talk
    zoe.c "Идиот, это же я выбрала место."
    zoe.c "Я не всегда хочу шиковать. Здесь мило, и недорого."
    show zoe mad
    mc.c "Просто подумал, что такой утончённой даме привычны изысканные рестораны."
    call playMusic(sadTheme) from _call_playMusic_274
    zoe.c "..."
    "Она выглядит по-настоящему рассерженной. Неужели я её так задел?"
    show zoe mad talk
    zoe.c "Гр-р-р... Чёрт..."
    zoe.c "Почему? Почему ты такой... такой..."
    zoe.c "Такой, блядь... Придурок..."
    show zoe mad
    "Погоди, что происходит?"
    mc.c "Ч-что? Зои?"
    show zoe mad talk
    zoe.c "Я не понимаю. Не понимаю тебя. Почему ты всё это для меня делаешь? Чего ты от меня хочешь?"
    zoe.c "Я ведь вообще ничего не даю тебе взамен. Обращаюсь с тобой как с дерьмом."
    show zoe mad
    "Она выпила несколько бокалов. Может, уже захмелела?"
    show zoe bashful talk
    zoe.c "В жизни никто так не поступает... Такого не бывает..."
    zoe.c "Что мне делать?"
    show zoe bashful
    "Я всегда чувствовал, что она держит дистанцию. Со мной, с большинством людей."
    "Её уверенное, дерзкое, нахальное поведение... Отношения без обязательств..."
    "Похоже, я задел её представления о жизни. Я веду себя совсем не так, как она привыкла видеть мужчин."
    "И она не знает, как реагировать. Остаётся сказать правду."
    mc.c "Не знаю, что ответить на вопрос «почему», Зои. Ты мне просто нравишься. Очень нравишься."
    show zoe surprise
    mc.c "Мне нравится быть рядом с тобой, видеть, как ты счастлива, а иногда и как ты злишься."
    mc.c "Больше нечего сказать. И ты не обращаешься со мной как с дерьмом. Ты замечательная."
    show zoe sad talk
    zoe.c "Боже..."
    zoe.c "Как ты это со мной делаешь... Не понимаю."
    show zoe sad
    mc.c "Просто будь собой и делай то, что кажется правильным."
    zoe.c "..."
    "Снаружи я сохраняю спокойствие, но внутри чуть не обосрался."
    "Может, мы и правда хотим от этих отношений разного. Я не могу навязать ей своё."
    scene black with fade
    "В неловком молчании мы доедаем остатки."
    "Несмотря на её возражения, я всё же заплатил по счёту, как и обещал."
    "Мы выходим на улицу."
    $ location_town.showBackground()
    "Мы всё ещё живём в одном направлении. Обратная дорога будет неловкой..."
    show zoe surprise with dissolve
    zoe.c "Погоди, [mc.name]..."
    show zoe bashful talk
    zoe.c "Прости... Я немного выпила и просто... немного запуталась."
    zoe.c "Не хотела на тебя срываться."
    show zoe bashful
    mc.c "Не извиняйся, ты ничего плохого не сделала."
    mc.c "Но я же не настолько мудак, да?"
    "Я выдавливаю из себя самую идиотскую улыбку."
    call stopMusic from _call_stopMusic_51
    show zoe neutral
    zoe.c "..."
    call playMusic(heartTheme) from _call_playMusic_275
    show zoe smile
    zoe.c "*Пфф* Хе~"
    show zoe smile talk
    zoe.c "Нет, ты не мудак. И ты прав."
    zoe.c "Хватит думать. Пора действовать."
    show zoe smile
    mc.c "Хм?"
    "Не совсем понимаю, что она имеет в виду, но чувствую, как она тянет меня за плечо."
    hide zoe with dissolve
    show zoe kiss with dissolve
    pause
    zoe.c "М-м-м~"
    "Она притягивает меня в крепкие объятия и целует по-настоящему страстно."
    "Влажный, жадный, страстный поцелуй. Наш первый — после всего этого..."
    hide zoe with dissolve
    show zoe hug with dissolve
    zoe.c "Ты меня путаешь. Ты не такой... Не знаю."
    zoe.c "Не похож на обычных парней."
    mc.c "Если честно, у тебя, похоже, просто ужасный вкус на мужчин."
    zoe.c "Чёрт... Подруги мне постоянно твердят то же самое..."
    zoe.c "Может, они были правы. Я и не знала, чего лишалась."
    hide zoe with dissolve
    show zoe kiss with dissolve
    pause
    zoe.c "Муа-а~"
    hide zoe with dissolve
    show zoe smile talk with dissolve
    zoe.c "Можно я вернусь к тебе, жеребец?"
    show zoe smile
    "Кто бы отказался..."
    scene black with fade
    "Сегодняшний вечер что-то значит. Мы идём домой вместе, и я чувствую, как между нами разгорается новая страсть."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_home.showBackground()
    "Раньше у нас такого не было. Она раскрылась, стала нежнее со мной и приняла меня."
    show zoe smile talk 2 with dissolve
    zoe.c "Ладно, сдаюсь. Сегодня всё будет по-твоему, чертов размазня..."
    show zoe smile
    "Я сразу притягиваю её за бедро и снова обнимаю, словно наверстываю все упущенные объятия."
    call playMusic(sexyTheme) from _call_playMusic_276
    hide zoe with dissolve
    show zoe kiss with dissolve
    pause
    zoe.c "М-м-м~"
    "Мы начинаем раздевать друг друга, путаясь в объятиях и поцелуях."
    scene black with fade
    mc.c "Иногда я тоже бываю настойчивым..."
    zoe.c "Хм~?"
    image zoe missionary start = Image("images/characters/zoe/hscenes/missionary/start1.webp")
    show zoe missionary start with fade
    pause
    "Я мягко толкаю Зои на кровать. Она падает на спину."
    zoe.c "О-ох~ Какой сильный! Какая свирепость! Не знала, что ты на такое способен, красавчик."
    mc.c "Мы уже делали по-твоему, а теперь {b}будет{/b} по-моему..."
    zoe.c "Да? И как же?"
    "Я нависаю над ней и смотрю ей в глаза. Кажется, она тоже этого хочет."
    image zoe makeout part 1 = Movie(play="images/characters/zoe/hscenes/missionary/makeout1.webm")
    show zoe makeout part 1 with fade
    pause
    "Наши губы встречаются у кончика её длинной морды."
    "Возможно, она ещё не привыкла целоваться со мной вот так и на мгновение колеблется."
    zoe.c "М-мм~"
    "Но мы постепенно углубляем поцелуй, а я ласкаю её обнажённое подтянутое тело."
    "Она отвечает взаимностью, расслабляет плечи, открываясь новой страсти и близости."
    zoe.c "М-мм~ Такой... М-мм~ размазня..."
    mc.c "Мне так нравится."
    image zoe makeout part 2 = Movie(play="images/characters/zoe/hscenes/missionary/makeout2.webm")
    show zoe makeout part 2 with fade
    pause
    "Зои снова смотрит мне в глаза. Мы чередуем лёгкие поцелуи с глубокими французскими."
    "Как же давно я хотел это сделать."
    zoe.c "М-м~"
    "Наконец мы отрываемся друг от друга."
    image zoe missionary start 2 = Image("images/characters/zoe/hscenes/missionary/start2.webp")
    show zoe missionary start 2 with fade
    pause
    zoe.c "О-о~ А я думала, на этом всё."
    mc.c "Видишь, я не {b}настолько{/b} размазня."
    mc.c "Но сначала нужно отомстить тебе за то, что ты оставила меня неудовлетворённым после ласки ногами. У меня для тебя правило."
    zoe.c "Правило?"
    mc.c "Такое же, какое ты установила тогда для меня. Не трогай меня. Просто лежи и принимай. Теперь я главный."
    zoe.c "А... Что?.."
    mc.c "Не бойся, думаю, тебе понравится."
    image zoe missionary part 1 = Movie(play="images/characters/zoe/hscenes/missionary/part1.webm")
    show zoe missionary part 1 with fade
    pause
    "Я медленно вхожу в Зои, мягко и глубоко проникая в её горячую влажную киску."
    "Впервые я сам контролирую близость с Зои."
    "Я двигаюсь в нежном ритме и могу смотреть ей в глаза, видеть, как теплеет её лицо."
    zoe.c "М-мм~ [mc.name]~"
    "Не торопясь, я исследую её всю, скользя по её широким бёдрам."
    mc.c "Вот видишь, можно и не спешить."
    zoe.c "М-мм~ Ладно... Сойдёт. Но что в этом такого?"
    mc.c "А вот что..."
    image zoe missionary part 2 = Movie(play="images/characters/zoe/hscenes/missionary/part2.webm")
    show zoe missionary part 2 with fade
    pause
    "Я снова наклоняюсь и целую её."
    "Наши языки переплетаются, а я продолжаю глубоко входить в неё."
    zoe.c "М-м-мм~ А-а~"
    zoe.c "Хм~ Ладно... М-мм~ Может, ты..."
    mc.c "М-мм~ Ну как?"
    "Зои отдаётся страсти, закрывает глаза и обнимает меня."
    "Никогда не видел её такой... покорной. Это мило, но она не совсем такая."
    show zoe missionary part 1 with fade
    pause
    zoe.c "Ты даже не представляешь, как мне трудно... не перехватить инициативу..."
    zoe.c "Я тебе ещё отомщу~"
    mc.c "Не возражаю. Но сейчас всё по-моему."
    zoe.c "М-м-м~ Ладно~ Ты заслужил, наверное~"
    "Медленный секс прекрасен, но пора прибавить темп."
    mc.c "Ты была хорошей девочкой. Пора дать тебе то, за чем ты пришла."
    zoe.c "Осторожнее с этим «хорошая девочка», худыш..."
    image zoe missionary part 3 = Movie(play="images/characters/zoe/hscenes/missionary/part3.webm")
    show zoe missionary part 3 with fade
    pause
    "Я поднимаю ноги Зои, и она раскрывается передо мной."
    "Придерживая её за бёдра, я вхожу глубоко и резко, наши тела шлёпаются друг о друга."
    zoe.c "О-ох~ Да-а~"
    zoe.c "Вот так, жеребец~ М-мм~"
    "Её подтянутое, упругое тело приятно ощущается в моих руках. Её обманчиво шелковистый мех снова застаёт меня врасплох."
    "Хочется зарыться в него мордой и умереть счастливым."
    image zoe missionary part 4 = Movie(play="images/characters/zoe/hscenes/missionary/part4.webm")
    show zoe missionary part 4 with fade
    pause
    "Вижу, ей нравится. Выражение лица не врёт."
    "Она смотрит на меня прищуренными глазами и вздрагивает с каждым толчком."
    zoe.c "М-м-мм~ Ха-а-а~"
    zoe.c "Ещё~ М-мм~ Ещё~"
    mc.c "Ещё получишь, не волнуйся."
    "Она невероятная. Если не буду осторожен, всё закончится прежде, чем она получит привычное удовольствие."
    zoe.c "М-м~ А-а~"
    mc.c "Зои..."
    image zoe missionary part 5 = Movie(play="images/characters/zoe/hscenes/missionary/part5.webm")
    show zoe missionary part 5 with fade
    pause
    "Я хватаю её за крепкие бёдра и вколачиваюсь в неё изо всех сил."
    zoe.c "О-о-ох~ Бля-я-ядь~ Да-а-а~"
    zoe.c "М-м-м~ А-а-а~"
    "Она крепко сжимает меня, а я всем телом врываюсь в неё, загоняя член глубоко."
    "Громкие шлепки прорезают наше всё более тяжёлое дыхание и стоны."
    zoe.c "Блядь, блядь, блядь, БЛЯДЬ~ А-А-А~"
    zoe.c "О-о-о-о-ох~"
    "Её тело содрогается от удовольствия. Я тоже уже близко..."
    "Мы трахаемся жёстко и первобытно, как животные в течке."
    "Чёрт, я сейчас кончу. Изо всех сил стараюсь мыслить здраво, но... внутрь кончать не стоит."
    mc.c "М-м, Зои, я сейчас..."
    zoe.c "ДА~ ДА-А~"
    image zoe missionary end 1 = Image("images/characters/zoe/hscenes/missionary/end1.webp")
    show zoe missionary end 1 with fadewhite
    pause
    zoe.c "М-М-М-М~"
    "Зои стонет, пока я выхожу из неё и заливаю её грудь огромной порцией спермы."
    image zoe missionary end 2 = Image("images/characters/zoe/hscenes/missionary/end2.webp")
    show zoe missionary end 2 with fade
    pause
    zoe.c "*Ха-а* *Ха-а*"
    "Она обессиленно откидывается назад, хватая ртом воздух и вздрагивая после оргазма."
    "Я могу только откинуться и тяжело дышать. Вложил в это всё, что у меня было."
    zoe.c "О-ох~ Чёрт..."
    zoe.c "*Ха-а* Ладно, жеребец... *ха-а* Неплохо~"
    zoe.c "Ты... *ха-а* Мог бы кончить внутрь, знаешь..."
    mc.c "Ну, э-э... Я не знал, можно ли..."
    zoe.c "*Ха-а* Я же на таблетках, очевидно."
    mc.c "Чёрт... Тогда давай ещё раз..."
    zoe.c "Сейчас-то ты вообще сможешь?"
    mc.c "...Нет."
    zoe.c "Хе~ Я тоже вымоталась... Хорошо поработал~"
    zoe.c "Просто... вытрись, ладно?"
    call playMusic(heartTheme) from _call_playMusic_277
    scene zoepillowtalk with fade
    pause
    "Мы падаем на кровать и лежим рядом, обнявшись."
    "Переведя дыхание, я поворачиваюсь к ней."
    mc.c "Вот такой вечер мне по душе."
    zoe.c "Слащаво... Но... думаю, смогу это терпеть."
    mc.c "Ну всё, растопил твоё ледяное сердце. Ты прозрела."
    zoe.c "Не думай, что теперь {b}каждый{/b} раз всё будет {b}именно так{/b}, жеребец."
    zoe.c "Так что не обольщайся..."
    "Мы наслаждаемся послевкусием близости. Впервые я увидел Зои с такой стороны."
    "Мне очень нравится."
    mc.c "Раз уж об этом... Сегодня я попробую зайти ещё дальше..."
    zoe.c "Хм~?"
    mc.c "Останься сегодня у меня. Переночуй здесь."
    zoe.c "..."
    "Она обдумывает предложение, но я замечаю её улыбку."
    zoe.c "Пожалуй, если уж надо... Чтобы ты был доволен~"
    "Она шутит. Может притворяться сколько угодно, я её уже раскусил."
    scene black with fade
    "Мы целуемся, приводим себя в порядок и готовимся провести ночь вместе..."
    "Немного погодя мы лежим рядом. Сначала ей не очень удобно, но постепенно..."
    call zoeSleepover from _call_zoeSleepover
    "Она придвигается и прижимается ко мне."
    "Тихо дышит, засыпая, положив пушистую лапку мне на грудь."
    "Мы засыпаем в тёплых объятиях."
    call stopMusic from _call_stopMusic_52
    scene black with fade
    pause
    call playMusic(heartTheme) from _call_playMusic_278
    scene zoehomemorning with fade
    pause
    zoe.c "...Эй."
    mc.c "Какое чудесное зрелище с самого утра."
    zoe.c "...Смотри, худыш. Пока ты спишь, ты уязвим."
    mc.c "И что ты собираешься со мной сделать?"
    zoe.c "Продолжишь — узнаешь."
    mc.c "Значит, ты ещё останешься как-нибудь."
    zoe.c "...Может быть."
    mc.c "В любое время, Зои."
    zoe.c "Хм."
    scene black with fade
    "Немного побыв вместе утром, Зои прощается."
    "Мне ещё нужно привыкнуть к... романтике. Но мы движемся в правильную сторону."

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return {'location':location_home, 'time':'Morning'}

label zoeHEvent6(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_279
    show zoe smile with dissolve
    "Сегодня мы с Зои — идеальная команда за работой."
    "Может, странно так говорить после всего, что между нами было, но, кажется, я её расположил к себе."
    "Мы, конечно, нравимся друг другу, но теперь делаем не только то, что трахаться и флиртовать. Она стала чуть... нежнее."
    "И это не в одну сторону..."
    show zoe smile talk
    zoe.c "Иду, худыш."
    show zoe kiss with dissolve
    zoe.c "М-м~"
    show zoe smile with dissolve
    "Проходя мимо со стопкой стаканов, она довольно резко целует меня в губы."
    "Открытые проявления чувств на работе. В баре все знают, что мы вместе. Это моё место — мои правила. Впрочем, никто не жаловался."
    "Она почти идеальная сотрудница. Разве что иногда её резкость немного смущает посетителей."
    "Но ничего страшного. Так у заведения появляется характер. А ещё благодаря ей у нас немало поклонников."
    "Все сомнения насчёт этичности наших отношений давно исчезли. Здесь она главная сотрудница, и совершенно случайно мы {i}оказались{/i} крепко вместе."
    "Вечер постепенно затихает. Сегодня мы вдвоём справились со всем."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Раздаётся звонок телефона. Но не моего."
    show zoe thinking
    zoe.c "Хм?"
    show zoe mad talk
    zoe.c "Фу-у..."
    zoe.c "Прости, {i}босс{/i}, мне надо ответить... Я выйду."
    show zoe mad
    mc.c "Что-то случилось?"
    show zoe thinking
    zoe.c "Да ничего особенного, просто мама сказала, что позвонит. Я просила не звонить..."
    mc.c "Ничего страшного, спокойно ответь. А что такого?"
    show zoe mad talk
    zoe.c "Фу-у... Она всё время пилит меня. Вечно «переживает», но это всё чушь."
    zoe.c "Дай мне минутку."
    show zoe mad
    mc.c "Конечно."
    hide zoe with dissolve
    "Она уходит за угол в подсобку, чтобы ответить на звонок."
    call playMusic(heartTheme) from _call_playMusic_280
    "В баре заметно поубавилось посетителей. За стойкой никого, музыка играет тихо, теперь здесь довольно спокойно."
    zoe.c "{size=25}Да, привет, мам...{/size}"
    "Ох, я её слышу. Не хочу подслушивать, но я и так стою неподалёку. Наверное, она отошла за угол совсем чуть-чуть."
    zoe.c "{size=25}Я же говорила, что сейчас буду на работе...{/size}"
    "..."
    zoe.c "{size=25}Конечно, это настоящая работа, твою мать.{/size}"
    "Ничего себе, она так разговаривает с мамой? Интересно, какая та?"
    "Она редко рассказывала о родителях. Я знал только, что они постоянно её пилили, пока она была без работы."
    zoe.c "{size=25}Я же сказала, что не буду этим заниматься. Сейчас у меня всё хорошо.{/size}"
    "..."
    zoe.c "{size=25}Почему ты не можешь просто дать мне самой решать?{/size}"
    "Блин... Что делать? Уйти? Сделать вид, что не слышу? Или попросить её отойти подальше?"
    "..."
    zoe.c "{size=25}Нет, я не буду этим заниматься. Я зарабатываю достаточно, и у меня классный начальник.{/size}"
    "Ну, это мило. Хотя в споре звучит немного странно."
    "..."
    zoe.c "{size=25}Что, блядь, мам? Да, человек... У него есть имя, я же тебе говорила!{/size}"
    "Я? Ой-ой."
    "..."
    zoe.c "{size=25}Ага, как же. Я тебе уже говорила, мне это не нужно. Не то чтобы он сам этого хотел.{/size}"
    "Честно говоря, я не понимаю, о чём они. Не стоило подслушивать, но..."
    "..."
    zoe.c "{size=25}Ты думаешь только о том, чего {i}сама{/i} хочешь. Это моя жизнь!{/size}"
    "Я не могу оставить всё так. Если кто-то подойдёт к стойке, тоже услышит. Не надо выносить её личные проблемы на публику."
    scene barcellar with fade
    "Я заглядываю за угол и вижу Зои, прислонившуюся к стене с телефоном."
    show zoe neutral with dissolve
    "Она замечает меня, но, кажется, не возражает."
    mc.c "Зои, прости, но я слышу тебя отсюда. Если это личное, может, выйдешь на улицу?"
    zoe.c "..."
    call playMusic(funnyTheme) from _call_playMusic_281
    show zoe tease
    zoe.c "Хе~"
    "Она почему-то ухмыляется своей фирменной улыбкой. Что-то сказала её мама?"
    show zoe tease talk
    zoe.c "Ну-ну, кстати о нём: вот и {i}мой мужчина{/i}."
    show zoe tease
    "Из телефона доносится едва слышный голос."
    show zoe tease talk
    zoe.c "Да, я на работе, и он ещё и мой начальник. {i}Какой скандал{/i}, да?"
    show zoe tease
    "..."
    "Кажется, она пытается что-то доказать."
    show zoe tease talk
    zoe.c "Чего ещё желать? Владелец бизнеса, спокойный, заботится обо мне. Разве не об этом ты всё время говоришь?"
    zoe.c "О, и в постели он тоже хорош~"
    show zoe tease
    "Боже мой. Я заноза для этой семьи..."
    "Я стою в замешательстве и не знаю, что сказать."
    show zoe thinking
    zoe.c "Хватит. Мы ни к чему не придём. Я возвращаюсь к работе. Не звони больше."
    "Она кладёт трубку."
    mc.c "Э-э... Прости, Зои."
    show zoe smile talk
    zoe.c "За что? На этой неделе я выиграла спор."
    show zoe smile
    mc.c "Выиграла?"
    show zoe smile talk 2
    zoe.c "Ага. Мы спорим. На следующей неделе будет другая тема, уверена."
    show zoe smile
    mc.c "О чём вы спорили? Это ведь не обо мне?"
    "Очевидно, обо мне."
    show zoe thinking
    zoe.c "Ну ладно, да, ты тоже всплыл."
    zoe.c "Обычная чушь про мою жизнь и всякое такое. Если честно, я не обращаю на это внимания."
    mc.c "Она меня не одобряет?"
    show zoe smile talk 2
    zoe.c "Не переживай, худыш. Не позволяй родителям решать, как тебе жить."
    show zoe smile
    "По крайней мере, она, кажется, не сильно расстроена. У всех семей свои порядки."
    mc.c "Если ты уверена, что всё нормально..."
    show zoe smile talk
    zoe.c "Всё хорошо, жеребец."
    show zoe smile
    "Интересно, что она рассказала обо мне. Мама Зои что-то не одобряет?"
    mc.c "«Твой мужчина»?"
    show zoe thinking
    zoe.c "Да-да. Она пытается свести меня с кем-то из знакомых семьи..."
    mc.c "Мне стоит беспокоиться?"
    show zoe smile talk
    zoe.c "Да ни хрена. Я не собираюсь связываться с этими занудами."
    show zoe smile
    mc.c "Тогда получается, ты «моя женщина»."
    show zoe mad
    zoe.c "..."
    show zoe mad talk
    zoe.c "Обычно меня бы это раздражало..."
    show zoe mad
    mc.c "А ты всё ещё выглядишь злой."
    show zoe mad talk
    zoe.c "Я вроде злюсь, а вроде и нет..."
    show zoe thinking
    zoe.c "Что с тобой такое?.."
    "Редкая победа [mc.name] в словесной перепалке с Зои. Обожаю."
    show zoe neutral talk
    zoe.c "Ладно. Прости за этот звонок. Уже почти пора закрываться, да?"
    show zoe neutral
    mc.c "Да, почти. Давай закончим."
    call stopMusic from _call_stopMusic_53
    scene black with fade
    "Мы закрываем бар, провожаем последних посетителей, допивающих свои напитки."
    "Моем посуду, вытираем поверхности, запираем двери — и готово."
    "И вот мы остаёмся вдвоём в тихом гуле кондиционера."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_bar.showBackground()
    mc.c "Хорошо поработала сегодня."
    show zoe smile talk with dissolve
    zoe.c "И что бы ты без меня делал?"
    show zoe smile
    mc.c "Наверное, нанял бы кого-нибудь другого, зато меньше нервничал."
    show zoe tease talk
    zoe.c "О-хо~ Ну ты же знаешь, что это неправда."
    show zoe tease
    mc.c "Ладно, ладно. Ты моя звезда. Что бы я {i}делал{/i} без тебя?"
    show zoe smile talk 2
    zoe.c "Сам знаешь. Я могу делать всё, что захочу~"
    show zoe tease talk
    zoe.c "Ты от меня не избавишься~ Даже если я..."
    zoe.c "Сделаю вот..."
    call playMusic(sexyTheme) from _call_playMusic_282
    scene zoehevent6i1 with fade
    zoe.c "Так~"
    pause
    "Боже, ни хрена себе."
    "Зои задирает юбку и показывает... Ничего. На ней нет белья."
    mc.c "Ты... всю смену так ходила?"
    zoe.c "Интересно было, заметишь ли ты. Я {i}пыталась{/i} тебя завести, но, похоже, ты недостаточно пялился на мою задницу."
    zoe.c "Я наклонялась так низко, как только могла. А ты всё равно не заметил, тупица."
    mc.c "Я..."
    "Я заворожённо смотрю, как она покачивает задом в мою сторону, открывая киску."
    "Заворожён, и чертовски возбуждён."
    "Мы одни. Бар закрыт. Всё это часть её плана..."
    "Я подхожу, и Зои хватает меня за воротник, поднося острые когти опасно близко."
    zoe.c "Собираешься что-нибудь с этим сделать?"
    "Будто я могу устоять перед чарами Зои..."
    image zoe bar doggy 1 = Movie(play="images/characters/zoe/hscenes/bardoggy/part1.webm")
    show zoe bar doggy 1 with fade
    pause
    "Я быстро высвобождаю член из ширинки и вхожу в её уже мокрую, горячую киску."
    "Зои крепко хватает меня за воротник и притягивает к себе, прижимая к бёдрам."
    zoe.c "М-мм~ Наконец-то~"
    mc.c "Блядь, Зои... Ты всегда готова."
    zoe.c "Ты заставляешь меня ждать, идиот~"
    "Я хватаю её за талию и толкаюсь в неё, прижимая к задней части стойки."
    zoe.c "О-ох, блядь~"
    "Зои оборачивается с угрожающей улыбкой. В её взгляде смешались игривость, агрессия и удовольствие."
    "Как всегда, я в её власти и поддаюсь любой прихоти. Да я и не против..."
    "Раз уж она тянет меня за воротник... пожалуй, проявлю и я немного напора..."
    image zoe bar doggy 2 = Movie(play="images/characters/zoe/hscenes/bardoggy/part2.webm")
    show zoe bar doggy 2 with fade
    pause
    zoe.c "М-мм~!"
    "Я тянусь к её морде, направляю к себе и целую мокро и жадно."
    "Зои отвечает, наши языки переплетаются в жарком страстном поцелуе."
    "Мы не отрываемся друг от друга, продолжая двигаться, обмениваясь слюной."
    zoe.c "М-мм~ Блядь~ М-мм~"
    "Она так крепко сжимает мой воротник, что почти отрывает его от рубашки. Я чувствую её стоны ладонью, ласкающей щёку."
    "Мы развлекаемся самым непристойным образом прямо в баре. Как бы я устоял, если бы раньше заметил, что на ней нет трусиков?"
    zoe.c "М-мм~ Ладно, сладенький~ Просто трахни меня уже~"
    "Отрываясь от поцелуя, Зои предлагает мне ускориться."
    image zoe bar doggy 3 = Movie(play="images/characters/zoe/hscenes/bardoggy/part3.webm")
    show zoe bar doggy 3 with fade
    pause
    "Она наклоняется над стойкой, подставляя мне задницу. Я инстинктивно хватаю её за виляющий хвост и прижимаюсь к ней."
    zoe.c "О-о-ох~ Блядь, блядь~ Да-а-а~"
    zoe.c "Ха-а-а~ Трахни меня, жеребец~ Пожёстче~"
    "Зои хватается за край стойки и царапает поверхность. Она вздрагивает при каждом толчке."
    "Её киска крепко сжимает мой член, а между ягодицами уже мокро от наших соков."
    "Влажные шлепки разносятся по бару, отражаясь от высоких потолков и широких стен в непристойном ритме."
    zoe.c "А-а~ А-а-а~ А-а~"
    image zoe bar doggy 4 = Movie(play="images/characters/zoe/hscenes/bardoggy/part4.webm")
    show zoe bar doggy 4 with fade
    pause
    "Она опускает лицо на стойку и крепко держится, упираясь в неё."
    "Я вкладываю всю силу в каждый толчок, прижимая её к краю стойки."
    zoe.c "ДА-ДА-ДА-ДА-А-А~"
    "Она отталкивается от стойки и сама подаётся назад навстречу моим бёдрам."
    "Мы оба горячие, мокрые и дрожим — предел уже близко."
    zoe.c "А-а~ А-а~ Я сейчас..."
    mc.c "Я тоже..."
    zoe.c "А-а~ Давай, жеребец. Я тут главная~"
    zoe.c "Кончай в меня~ А-а~ Наполни мою чёртову киску~"
    scene zoebardoggyend with fadewhite
    pause
    zoe.c "М-м-м-м-м~!"
    "Я глубоко кончаю в её киску. Она сжимает меня оргазмическими спазмами, а я крепко держу её."
    mc.c "Ох, блядь..."
    "Зои обессиленно падает на стойку, а я медленно выхожу из неё, открывая оставленный беспорядок."
    "Её киска всё ещё вздрагивает. Она переводит дыхание и смотрит на меня."
    zoe.c "Вот это блядь~ Наверное, твоя лучшая работа~"
    mc.c "Чёрт... Не знаю, что сказать."
    zoe.c "Хе-хе~ Я так на мужчин влияю~"
    scene black with fade
    "Немного придя в себя и вспомнив, где мы находимся, мы встаём."
    $ location_bar.showBackground()
    show zoe tease with dissolve
    "Быстро вытеревшись, она поправляет юбку. Трусиков на ней всё равно нет."
    show zoe tease talk
    zoe.c "А-а... Наконец-то~ Надеялась, ты раньше меня хорошенько оттрахаешь..."
    show zoe tease
    mc.c "В переполненном баре?"
    show zoe tease talk
    zoe.c "А что, удержался бы? Может, мне надо стараться сильнее."
    show zoe tease
    mc.c "Боже, ты опасная..."
    "Голова всё ещё кружится от произошедшего, но я вспоминаю, где мы."
    mc.c "Ты... не хочешь сегодня ко мне?"
    show zoe smile talk
    zoe.c "Ой, чтобы мы целовались и обнимались?"
    show zoe smile
    mc.c "Неплохая идея."
    show zoe smile talk 2
    zoe.c "Прости, жеребец, сегодня я иду гулять с подружками."
    zoe.c "Вернусь, переоденусь и пойду."
    show zoe smile
    mc.c "А, ладно. Тогда хорошо повеселиться."
    show zoe tease talk
    zoe.c "Кто знает, может, не стану принимать душ и прекрасно проведу вечер, всё ещё наполненная твоей спермой."
    show zoe tease
    "Член мгновенно дёргается. Как ей удаётся так легко меня заводить... Я уже думаю о втором раунде..."
    show zoe tease talk
    zoe.c "Ахаха~ Вижу этот взгляд... Остынь, жеребец. Оставь себе эту мысль."
    show zoe tease
    mc.c "Ты чудовище..."
    show zoe smile talk 2
    zoe.c "Я не такая уж жестокая... Сегодня вечером можешь подрочить, представляя это~"
    show zoe smile
    "Чёрт. Может, так и сделаю..."
    show zoe smile talk 2
    zoe.c "Ладно, мне пора. Не хочу опоздать."
    show zoe smile
    mc.c "Погоди..."
    zoe.c "Хм?"
    "Я хватаю её за руку и притягиваю к себе."
    hide zoe with dissolve
    show zoe kiss with dissolve
    zoe.c "М-мм~"
    show zoe hug with dissolve
    zoe.c "Хм-хм~ Спокойной ночи, жеребец."
    scene black with fade
    "Мы выходим и расходимся у дороги."
    "Она сводит меня с ума."
    "Но... о чём был тот разговор? Я и правда проблема? Что она имела в виду под «ты бы не захотел»?"

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return

label zoeLikeEvent4(fromGallery):
    call playMusic(barTheme) from _call_playMusic_283
    $ location_bar.showBackground()
    "Пора менять сотрудников на вечерней смене."
    "Похоже, не хватает одной сотрудницы, которую я ожидал сегодня..."
    mc.c "Эй, Зои уже пришла?"
    staff "Она сегодня не придёт, [mc.name]."
    mc.c "А?"
    staff "Посмотри в общем чате, ей понадобилась срочная замена. Джей сказал, что подменит, но ещё в пути."
    mc.c "А, ясно, прости. Сейчас гляну."
    "Я достаю телефон."
    "Всё как она сказала: за полчаса до начала смены она написала сообщение."
    zoe.c "не могу сегодня ребят  кто-нибудь выйдет вместо меня"
    "Хм... Больше ничего. К счастью, быстро нашёлся желающий. Они часто меняются сменами, но так поздно и от Зои?"
    "Проверяю остальные сообщения — лично мне она ничего не писала."
    "Хм... Странно. Надеюсь, с ней всё в порядке. Причин может быть сколько угодно."
    "Может, просто решила прогулять смену, перепутала планы или куда-то уехала..."
    "Или... заболела, попала в аварию, у неё семейные проблемы... или она в серьёзной беде?.."
    "Я начинаю волноваться. Надо ей написать."
    mc.c "Привет, только что увидел сообщение в рабочем чате. Ничего страшного, но у тебя всё нормально?"
    "Отправлено. Наверное, ничего особенного, а я себя накручиваю. Не буду её дёргать — она ответит, когда сможет."
    scene black with fade
    "Вскоре приходит сотрудник на замену Зои, и вечер проходит спокойно."
    "Выручка примерно обычная, никаких проблем. Только пара шумных парней, которые неожиданно рано и сильно набрались."
    if (not fromGallery):
        $ timeOfDay = 'Night'
    $ location_bar.showBackground()
    "В тихую минуту я в сотый раз проверяю телефон..."
    "От Зои ни слова. Она даже не прочитала моё сообщение. Что происходит?"
    "Приложение показывает, что после отправки сообщения она не заходила в сеть. Теперь я уже серьёзно волнуюсь."
    "Она ненавидит, когда я звоню, но... придётся."
    "."
    ".."
    "..."
    "Не отвечает. Теперь я по-настоящему переживаю."
    "Больше никак с ней не связаться, остаётся только одно."
    "Возможно, я немного перехожу границы, но поеду к ней. Может, она хотя бы дома."
    "Погоди, я не перехожу границы. Как бы она ни делала вид, что между нами ничего нет, я точно {b}её парень{/b}, и она мне небезразлична."
    "Уже поздно, дела постепенно затихают."
    "Я быстро придумываю отговорку и выхожу."
    call stopMusic from _call_stopMusic_54
    scene black with fade
    "Я быстрым шагом иду по прохладному ночному воздуху к дому Зои. К счастью, это недалеко."
    scene zoeapartmentshallway with fade
    "Квартира Зои... Не очень большая и не шикарная. Скорее, довольно обшарпанная. Она и сама это знает и иногда называет её своей дырой, но всё же гордится ею."
    "Я бывал здесь несколько раз, но обычно она предпочитает оставаться у меня."
    "Но одна вещь меня всегда беспокоила... Звонок всё время сломан. Надо бы как-нибудь починить..."
    "Я стучу..."
    "..."
    "Никто не отвечает. Я стучу снова и жду, но по-прежнему тишина."
    "В редком для нас проявлении бытовой предусмотрительности у нас есть запасные ключи друг от друга..."
    "Я вхожу без предупреждения только потому, что не могу до неё дозвониться. Если она дома — или даже если её нет — она ведь не будет злиться? Открываю дверь."
    scene zoeapartment with fade
    "У двери валяются несколько пар её обуви. Это ни о чём не говорит — обычно здесь такой же беспорядок."
    "Гостиная... пусто."
    "Я иду в спальню и заглядываю за угол..."
    show zoe surprise with easeinbottom
    zoe.c "А-а-а!"
    mc.c "А-а!"
    "Мы чуть не сталкиваемся в дверях и оба от неожиданности подпрыгиваем."
    zoe.c "Ч-что за херня, [mc.name]?! Что ты тут делаешь? Я думала, услышала какой-то шум."
    mc.c "Я... э-э... пришёл проверить, как ты. Сам открыл дверь."
    mc.c "Но сначала: ты в порядке?! Я не мог с тобой связаться!"
    zoe.c "Проверить меня? В порядке? А?"
    mc.c "Ты внезапно не вышла на смену, и я подумал, вдруг с тобой что-то случилось."
    zoe.c "Ты проделал весь этот путь... просто чтобы проверить? Мог бы просто..."
    call playMusic(heartTheme) from _call_playMusic_284
    show zoe bashful talk
    zoe.c "О..."
    show zoe bashful
    mc.c "Я правда переживал, Зои. Ты не из тех, кто просто так пропускает смену. Ты не отвечала на сообщения, потом и на звонки, и я начал думать..."
    show zoe bashful talk
    zoe.c "Чёрт, да... Телефон..."
    zoe.c "Я просто выключила звук и бросила его... э-э... куда-то, не знаю."
    zoe.c "Наверное, они собирались звонить и дальше... Я не хотела, блядь, это слушать."
    show zoe bashful
    mc.c "Они? Кто? Что случилось?"
    show zoe bashful talk
    zoe.c "Ох, господи... Ладно, э-э... Проходи, садись."
    show zoe bashful
    "Зои ведёт меня к дивану и несчастно опускается на него."
    show zoe bashful talk
    zoe.c "Сегодня мои родители были в городе... Настаивали, что должны меня увидеть, и сами заявились сюда."
    show zoe sad talk
    zoe.c "В итоге мы сильно поругались. Кричали друг на друга и вываливали всё дерьмо..."
    show zoe sad
    mc.c "Ты говорила, что такое у вас часто бывает."
    show zoe sad talk
    zoe.c "Вроде да, но в этот раз... всё было по-другому."
    show zoe bashful talk
    zoe.c "Фу-у... В этот раз они и правда меня задели. Всё стало очень личным. Или я слишком близко к сердцу приняла их слова."
    show zoe sad talk
    zoe.c "Я так от этого устала. Почти выставила их за дверь... Я была в бешенстве и не знала, что с собой делать."
    show zoe sad
    mc.c "Поэтому ты внезапно поменялась сменами?"
    show zoe mad talk
    zoe.c "Что, тоже будешь меня отчитывать?"
    show zoe mad
    mc.c "Нет, Зои. Я просто рад, что дело только в этом и с тобой всё в порядке."
    mc.c "То есть... ты в безопасности. Хорошо тебе, конечно, не было."
    "Я кладу ладонь ей на руку. Она слегка отдёргивается."
    show zoe bashful talk
    zoe.c "Чёрт... Я... не могла идти на работу в таком состоянии... Наверное, сорвалась бы на ком-нибудь из-за ерунды..."
    zoe.c "Прости, что подвела со сменами... Наверное..."
    show zoe bashful
    mc.c "Не извиняйся... Я просто рад, что ты в порядке."
    mc.c "Хочешь рассказать? О чём вы спорили?"
    show zoe thinking
    zoe.c "Тебе не обязательно слушать эту хрень..."
    mc.c "Обязательно. Не понимаю, что могло довести тебя до такого, и мне тяжело даже думать об этом."
    mc.c "Я ведь для этого и пришёл..."
    show zoe bashful
    zoe.c "*Вздыхает*"
    show zoe bashful talk
    zoe.c "Я весь вечер об этом думала. Но если разобраться, они и раньше говорили примерно то же самое..."
    zoe.c "Просто... они навалили всё сразу, так подбирали слова... И я сорвалась."
    show zoe bashful
    mc.c "Не понимаю. У тебя же сейчас всё хорошо, верно?"
    mc.c "Новая квартира, новая работа, классный босс, как ты сама говоришь... Чего им ещё надо?"
    show zoe mad talk
    zoe.c "В их глазах я всё сложнее нахожу то, что делаю {i}правильно{/i}."
    zoe.c "Начиная с плохих оценок в школе, того, что я при первой возможности уехала и не пошла в колледж."
    zoe.c "Не нашла «приличную» карьеру. Не посвятила всю жизнь тому, чего хотят {i}они{/i}..."
    show zoe mad
    mc.c "Чего-то помимо работы?"
    zoe.c "..."
    show zoe bashful talk
    zoe.c "Найти {i}мужа{/i}, завести {i}детей{/i} и создать {i}семью{/i}."
    show zoe mad talk
    zoe.c "И, по их словам, я чертовски их разочаровала и провалилась, раз не сделала этого."
    show zoe mad
    "Хм... Не удивлён, что это причина ваших ссор. Я уже понял это по рассказам о ваших прошлых конфликтах."
    "Меня немного удивляет, что в этот раз всё настолько её задело. Обычно она реагировала на это с насмешливым бунтарством..."
    mc.c "А ты... очевидно, этого не хочешь."
    show zoe mad talk
    zoe.c "Фу-у, вот именно! Это вообще не их собачье дело!"
    zoe.c "Они без конца об этом твердят... Всю жизнь меня пилят!"
    zoe.c "Кто знает, может, дело во мне, но они постоянно поднимают эту тему, будто это единственное, что имеет смысл..."
    zoe.c "Это не их жизнь. Дайте мне самой решать!"
    show zoe mad
    "Не совсем такой реакции я ожидал."
    "«Кто знает»? Не то категоричное «ни за что», которого я ждал. Я думал, что..."
    mc.c "То есть, может быть, ты всё-таки хочешь этого?"
    "Ох, чёрт. Не стоило такое говорить. Я не подумал. Сейчас мне влетит."
    show zoe bashful talk
    zoe.c "Блядь, не знаю."
    show zoe thinking
    zoe.c "Я никогда особо об этом не думала. Даже не задумывалась о такой херне, пока в двадцать лет {i}они{/i} не начали твердить мне об этом."
    show zoe bashful talk
    zoe.c "Я обычно просто выпаливала «нет» и забывала об этом, но..."
    show zoe bashful
    zoe.c "..."
    "Она умолкает, откидывается на диване и не смотрит мне в глаза."
    "Неужели она и правда сомневается? Понимаю, что не хочется, когда тебе указывают, как жить, но именно эта тема..."
    "Она жила беззаботно, но теперь переживает о будущем? Или в ней есть глубокие желания, которые не совпадают с её привычным образом?"
    "Зои — жена и мать?"
    mc.c "Я удивлён. Думал, ты просто пошлёшь их и на этом всё."
    show zoe bashful talk
    zoe.c "Я так и делала, но в этот раз... Не знаю. Я замялась."
    zoe.c "Я... Кажется, они это заметили. И продолжили."
    show zoe mad talk
    zoe.c "И то, что они знают, что я встречаюсь с {i}кем-то{/i}, тоже не помогло. Так что спасибо тебе."
    show zoe mad
    "Я... Мы?"
    "Неужели это возможно? Неужели она правда..."
    show zoe thinking
    zoe.c "Чёрт, после сегодняшнего дня я {i}совсем не{/i} хотел говорить об этом."
    "Не вижу смысла дальше давить на эту тему. Сегодня ей и так пришлось несладко."
    "Я обнимаю её за плечи и прижимаю к себе."
    mc.c "Прости, Зои. Не хочу на тебя давить. Тяжело тебе пришлось."
    show zoe bashful talk
    zoe.c "Да ладно. Прости, что заставила тебя проделать весь этот путь из-за какой-то ерунды."
    show zoe bashful
    mc.c "Это не ерунда. Просто хотел бы помочь тебе с {i}ними{/i}."
    show zoe neutral talk
    zoe.c "Хе. Даже я бы не стал подвергать тебя этому."
    show zoe neutral
    "Наконец она слегка улыбается. Кажется, успокоилась."
    mc.c "Хочешь, я останусь сегодня?"
    show zoe neutral talk
    zoe.c "Не-а, просто хочу лечь и проспаться. Завтра буду в порядке."
    zoe.c "То, что ты приехал, уже помогло. Спасибо, худыш."
    show zoe neutral
    "Вот она."
    mc.c "Ладно. Если что-то понадобится — скажи, хорошо?"
    show zoe neutral talk
    zoe.c "Я буду в порядке, спасибо."
    show zoe neutral
    "Я целую её в щёку и встаю, чтобы уйти."
    show zoe neutral talk
    zoe.c "На этой неделе возьму двойную смену, ладно?"
    show zoe neutral
    mc.c "Ха-ха, договорились. Всегда возьму на смену свою лучшую сотрудницу."
    scene black with fade
    "Она неуверенно машет на прощание. Я закрываю за собой дверь и иду домой."
    "Зои... Сегодняшний день заставил меня задуматься о нас."
    "Зои правда хочет такой жизни? А я?"
    "Эти мысли крутятся в голове, пока я наконец засыпаю."

    if(not fromGallery):
        $ zoe.addLike(1)
        $ zoe.addLove(1)

    return {'location':location_home, 'time':'Morning'}

label zoeLikeEvent5Invitation(fromGallery):
    call playMusic(barTheme) from _call_playMusic_285
    show zoe neutral
    "Сегодня мы с Зои отдыхаем, и вдруг она обращается ко мне с необычной просьбой."
    show zoe neutral talk
    zoe.c "Эй, э-э... [mc.name], не хочу быть обузой, но..."
    show zoe neutral
    "Она колеблется."
    mc.c "Что такое?"
    show zoe thinking
    zoe.c "Ха-а..."
    show zoe neutral talk
    zoe.c "Ты же платишь нам ежемесячную премию, да?"
    zoe.c "Ну... Во-первых, мы всё ещё так делаем?"
    show zoe neutral
    "За последнее время мы ни разу не пропустили месяц. К чему она клонит?"
    mc.c "Конечно! В этом месяце дела снова идут хорошо."
    mc.c "Благодаря твоим стараниям..."
    show zoe thinking
    zoe.c "Ага, ага..."
    show zoe neutral talk
    zoe.c "Слушай... Можно я получу свою часть немного заранее?"
    show zoe neutral
    "...Интересно. Это не проблема, но почему?"
    mc.c "Конечно. Попробую заранее прикинуть сумму."
    mc.c "Но... у тебя проблемы с деньгами? Могу помочь? Только не говори, что я мало плачу..."
    show zoe surprise
    zoe.c "Н-нет, я не это имею в виду!"
    show zoe thinking
    zoe.c "Ха-а... Это не твоя проблема и ничего страшного, просто..."
    zoe.c "Владелец моей квартиры выставил её на продажу, блядь..."
    mc.c "Чёрт! Боже, как бесит."
    mc.c "Ты справишься? Сколько времени тебе дали?"
    show zoe neutral talk
    zoe.c "Погоди, успокойся, сейчас всё {i}не настолько{/i} плохо."
    show zoe thinking
    zoe.c "Её просто выставили на продажу. Это может тянуться целую вечность."
    show zoe neutral talk
    zoe.c "Так что он перевёл договор на помесячную аренду. Пока квартиру не продадут."
    show zoe neutral
    mc.c "А... Всё равно неприятно. Не хватало ещё жить в такой неопределённости."
    show zoe mad talk
    zoe.c "Вот в чём дело... Из-за изменения договора он ещё и повысил аренду."
    show zoe mad
    mc.c "Козёл..."
    show zoe mad talk
    zoe.c "Ага, ещё какой. Мудак."
    show zoe neutral talk
    zoe.c "Помнишь, сначала аренда была чуть дороже, чем мне хотелось? Но если учитывать твою премию, я справляюсь."
    zoe.c "Я могу себе это позволить. Не пытаюсь разжалобить тебя, просто... Не знаю, как долго всё продлится."
    zoe.c "Хочу отложить денег на неизбежные расходы при переезде, когда до этого дойдёт. Поэтому и спросила про премию."
    show zoe neutral
    "Вполне понятно. Нужно подстраховаться, пока всё так неопределённо."
    "Но как же это всё бесит. Она так старалась найти это жильё. Несправедливо."
    "Не хочу, чтобы ей снова пришлось через всё это проходить."
    "А вдруг новое жильё будет далеко от города? Дорога на работу станет ещё хуже? Ей придётся переехать в плохой район?"
    "Я... могу помочь ей с этим."
    "Я уже какое-то время об этом думаю..."
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Да!' if(homeHasRoom) else "Нужно улучшить жильё"
    if(not fromGallery):
        menu:
            "Предложить Зои переехать ко мне? Этот выбор можно сделать в любое время."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "Пока нет":
                "Не сейчас... Не уверен, как она к этому отнесётся."
                "Но с деньгами я ей помочь могу. Кто знает, когда ещё до этого дойдёт."
                mc.c "Конечно. Разберусь с суммой, когда в следующий раз буду подсчитывать прибыль."
                show zoe smile talk
                zoe.c "Спасибо, жеребец. Я как-нибудь отплачу."
                show zoe smile
                mc.c "Не переживай."
                call endCharacterInteraction(zoe) from _call_endCharacterInteraction_6
    "Она не хрупкая беспомощная девочка. Ей не нужно, чтобы её {b}спасали{/o}, но... Это ведь просто логично, верно?"
    "Мне ведь самому этого хочется... Надо просто спросить."
    mc.c "Хм..."
    show zoe neutral talk
    zoe.c "Что означает этот звук? Слишком дорого выйдет?"
    show zoe neutral
    mc.c "Нет, всё нормально. Просто... ситуация ужасная, да? Я через такое проходил."
    mc.c "Не знаешь, когда тебя могут выставить... Эта тяжесть неопределённости."
    show zoe thinking
    zoe.c "Ага, отстой."
    mc.c "Я думаю, есть ли вариант получше. Только выслушай меня... и никаких обязательств..."
    call playMusic(heartTheme) from _call_playMusic_286
    mc.c "Может, ты... хотела бы переехать ко мне?"
    show zoe thinking
    zoe.c "..."
    show zoe neutral
    zoe.c "Хм?"
    "Она лишь слегка приподнимает бровь. Не поторопился ли я?"
    mc.c "А-а... Просто... Это избавило бы тебя от всей этой мороки..."
    show zoe neutral talk
    zoe.c "Погоди... Ты правда предлагаешь? Не просто пожить у тебя, пока я ищу другое место?"
    show zoe neutral
    mc.c "Да. То есть, жить со мной. Если ты хочешь... Я буду только рад."
    show zoe smile
    "На её губах появляется едва заметная улыбка, постепенно превращаясь в широкую."
    "В ней больше облегчения, чем чего-либо ещё. Будто гора с плеч свалилась."
    show zoe smile talk
    zoe.c "Правда?"
    show zoe smile
    mc.c "Конечно."
    show zoe smile talk 2
    zoe.c "Худыш..."
    show zoe joy
    zoe.c "Блядь, да!"
    "Фух..."
    mc.c "Ты согласна?"
    show zoe smile talk 2
    zoe.c "А то, идиот!"
    show zoe smile
    "Она подходит ко мне."
    hide zoe with dissolve
    show zoe hug with dissolve
    zoe.c "Блядь! Ты даже не представляешь, как я рада... Я всё думала, вдруг..."
    mc.c "Вдруг?.."
    zoe.c "Ну... Чёрт, поймал меня. Я всё ждала, когда ты спросишь."
    zoe.c "Снова переезд... Но если мы и так собирались съезжаться, бессмысленно было бы устраиваться где-то ещё. А если бы мы не..."
    "Она сбивчиво тараторит, впиваясь когтями мне в плечи. Ей нужно успокоиться."
    show zoe kiss with dissolve
    "Я крепко целую её в милые губы."
    zoe.c "М-м~"
    "Её хватка ослабевает, плечи расслабляются."
    show zoe smile talk with dissolve
    zoe.c "Ха-а~ Прости. Просто... вся эта хрень не давала мне покоя."
    show zoe smile
    mc.c "Ну вот, проблема решена!"
    mc.c "Мне тоже легче... Я боялся, что ты откажешь."
    show zoe smile talk 2
    zoe.c "Ой... Ну ты и милашка. Тебе я не могу отказать~"
    show zoe smile
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Просто напомню: ещё [len(girlsAlreadyMovedIn)] девушек уже почти переехали ко мне."
        if(jessica.movedIn and zoeJessicaDuoStoryEvent1.unlocked):
            mc.c "Джесс, конечно."
            show zoe smile talk 2
            zoe.c "Ага-ага, она всё время тебя нахваливает~"
            show zoe smile
        if(katie.movedIn and katieZoeDuoStoryEvent1.unlocked):
            mc.c "Кэти тоже уже окончательно переехала ко мне."
            show zoe smile talk
            zoe.c "Наверняка там сплошная романтика~ Ну и готовка."
            show zoe smile
        mc.c "Тебя... это всё устраивает?"
        show zoe smile talk
        zoe.c "Хе-хе~ Да, думаю, ужиться смогу~"
        show zoe smile
    mc.c "Так... Ты останешься в квартире, пока её не продадут?"
    show zoe thinking
    zoe.c "Да нет. Я просто не продлю договор на следующий месяц, так что... Осталось время до конца этого."
    show zoe smile talk
    zoe.c "Но... переехать хотелось бы поскорее."
    show zoe smile
    mc.c "Именно это я и хотел услышать."
    scene black with fade
    "Следующее время мы обсуждаем, как совместить наши смены."
    "Она соберёт несколько вещей, а я отвезу их на машине. Остаток месяца потратим на остальное."
    "Дело решено. Отметь в календаре!"

    return

label zoeLikeEvent5(fromGallery):
    call playMusic(memoriesTheme) from _call_playMusic_287
    $ location_home_bedroom.showBackground()
    "Доброе утро, мир."
    "И как же хорошо сегодня на свете: я еду забрать свою девушку, чтобы она наконец переехала ко мне."
    "Вчера вечером мы с Зои вместе закрыли бар и с нетерпением ждали этого утра."
    "Это огромный шаг. Не могу поверить, что мы дошли до этого. Наши отношения развивались стремительно."
    "Но... я счастлив как никогда. Моя девушка будет рядом."
    "Мы договорились, что утром я заеду к ней и помогу перевезти кое-какие вещи. Для начала совсем немного — у неё ещё есть время в квартире."
    "Пора выдвигаться."
    scene black with fade
    "Вскоре я подъезжаю..."
    scene zoeapartment with fade
    "Дверь приоткрыта, а на пороге стоит картонная коробка."
    mc.c "Эй, есть кто-нибудь?"
    show zoe smile with dissolve
    "Зои выглядывает из-за угла, выкатывая небольшой чемодан."
    show zoe smile talk 2
    zoe.c "Чё как, худыш?"
    show zoe smile
    "В квартире чуть меньше вещей, чем обычно. Мебель перевозить не нужно, к тому же, кажется, жильё и так меблированное."
    "В итоге мы здесь почти не бывали. Она говорит, что после прежней квартиры эта казалась роскошной, но всё равно была так себе."
    mc.c "Ну как, всё готово?"
    show zoe neutral talk
    zoe.c "Кажется, да. Всё, что мне пока понадобится, в этой коробке, сумке и чемодане."
    show zoe neutral
    mc.c "Уверена? Можем взять ещё. По-моему, у тебя больше одежды, чем здесь."
    show zoe smile talk
    zoe.c "Конечно, но почти всё остальное — платья для вечеринок."
    show zoe smile talk 2
    zoe.c "Сейчас они не нужны, разве что... сегодня вечером пойдём в клуб праздновать?"
    show zoe smile
    mc.c "Э-э... Я рад, конечно, но только не это."
    show zoe tease talk
    zoe.c "Хе-хе~ Ничего, красавчик, я понимаю."
    show zoe smile talk
    zoe.c "Остальное буду постепенно привозить после смен."
    show zoe thinking
    zoe.c "Думала, немного растрогаюсь, но, чёрт, от этого места остались одни гадкие воспоминания."
    mc.c "А ведь тогда ты так радовалась, что нашла эту квартиру..."
    show zoe smile talk
    zoe.c "Да... Если подумать, она была хороша только по сравнению с моей прежней дырой."
    zoe.c "Хозяин оказался ещё большим мудаком, чем я думала. Всё разваливалось."
    show zoe smile talk 2
    zoe.c "Ну всё, прощай, клоповник. У тебя дома куда лучше."
    show zoe smile
    mc.c "Главное, чтобы тебе нравилось."
    show zoe smile talk 2
    zoe.c "Пока мне здесь нравится. Пошли отсюда."
    scene black with fade
    "Мы относим её вещи к машине и едем... домой."
    scene zoelikeevent5i1 with fade
    pause
    "Мы заходим внутрь и раскладываем немногочисленные вещи у кровати."
    zoe.c "Хм-м~"
    "Зои потягивается и глубоко вдыхает запах комнаты, подёргивая маленьким носом."
    zoe.c "Хи~ Мы и правда это сделали..."
    zoe.c "Вот и всё, да?"
    mc.c "Тут ещё другие комнаты есть."
    scene zoelikeevent5i2 with fade
    pause
    zoe.c "...Идиот."
    "Она поворачивается ко мне, и на её лице появляется всё та же озорная, прекрасная улыбка."
    mc.c "Добро пожаловать домой."
    zoe.c "...Ага."
    "Она на мгновение замирает, осматриваясь. Кажется... расслабленной. Согретой. Дома."
    zoe.c "Боже... Знаешь, что бесит? Если бы мы встретились чуть раньше..."
    zoe.c "Мне не пришлось бы возиться с переездом в эту квартиру. Мы могли бы сразу переехать сюда."
    mc.c "Хм... Но тогда у меня, может, не было бы шанса заполучить тебя в лучшие сотрудницы..."
    zoe.c "Хе-хе~ Чёрт, теперь это звучит странновато, да?"
    mc.c "Теперь у нас семейное заведение, да?"
    zoe.c "Боже, фу~ Заткнись~"
    "Она устало улыбается, всё ещё улыбаясь моим выходкам. Не могу удержаться — подхожу к ней."
    scene zoelikeevent5i3 with fade
    pause
    zoe.c "М-мм~"
    "Я притягиваю её за бёдра и прижимаюсь губами к кончику шелковистой морды."
    "Наши губы медленно смыкаются, тихо шлёпая, а языки переплетаются."
    zoe.c "М-м~ [mc.name]~"
    scene zoelikeevent5i4 with fade
    pause
    mc.c "Я люблю тебя."
    zoe.c "И я тебя, жеребец."
    "Мы долго обнимаемся посреди комнаты, одни, в самом начале нового этапа нашей совместной жизни."
    mc.c "Хочешь распаковать вещи? Место для них найдём."
    zoe.c "Не-а... Потом."
    zoe.c "Знаешь, что мне нужно? Кофе. Приготовленный нормальной посудой, которая {i}не{/i} разваливается."
    mc.c "Не пиво? Удивляешь."
    zoe.c "Не {i}так{/i} рано. Хотя вечером, может быть."
    scene zoelikeevent5i5 with fade
    pause
    "Мы идём на кухню и вместе готовим кофе."
    "Теперь это станет привычной картиной, да? Будем проводить вместе каждое утро..."
    "Мы садимся и некоторое время болтаем."
    mc.c "Надо сказать, после нашего знакомства я такого совсем не ожидал."
    zoe.c "Да? Ты о чём?"
    mc.c "Я только недавно приехал в город, а тут на меня налетает наглая волчица и обзывает гомофобным словом."
    zoe.c "Да ладно, это не оскорбление. Это от большой любви~"
    mc.c "А потом, помнишь, ты гналась за мной по улице и кричала, что я сразу тебе не позвонил..."
    zoe.c "Я не кричала... Но была совершенно права. Ты меня продинамил!"
    mc.c "А потом отчитывала меня за то, что я не отвёз тебя к себе, когда ты была вусмерть пьяна..."
    zoe.c "Хм... И сейчас так считаю. В ту ночь я была такая возбуждённая, что почти умоляла! Как ты мог отказать?"
    mc.c "Ты была никакая."
    scene zoelikeevent5i6 with fade
    pause
    zoe.c "Грубиян..."
    zoe.c "Ну, {i}такого{/i} я тоже не ожидала. Вообще ни от кого..."
    zoe.c "Не знаю, как ты это сделал, но вот мы здесь. Теперь тебе со мной жить."
    zoe.c "С моей шерстью в душе, моим дурным настроением по утрам и поздними возвращениями..."
    zoe.c "А ещё я могу прийти домой пьяной и захотеть трахнуть тебя до потери сознания~"
    mc.c "И где тут минусы?"
    zoe.c "Пока что говоришь так..."
    mc.c "Кстати, аренда оплачивается двадцать восьмого—"
    zoe.c "Ха-ха, да ну тебя. Врёшь как дышишь. Меня не проведёшь."
    zoe.c "Лучше обсудим мою зарплату~"
    scene black with fade
    "Вот мы и сидим на кухне, болтаем."
    "Сегодня она не уходит домой и не просто «остаётся на ночь». Она дома."
    "Не могу дождаться, когда наши дни станут такими."

    if(not fromGallery):
        $ zoe.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label zoeHEvent7(fromGallery):
    call playMusic(barTheme) from _call_playMusic_288
    $ location_home_bedroom.showBackground()
    "Уже поздно, и из спальни доносится шорох."
    "Я заглядываю за угол..."
    scene zoehevent7i1 with fade
    pause
    "Это Зои. Ой, кажется, я застал её за переодеванием."
    "На кровати лежит ворох одежды. Она примеряет платье, обнажённая, если не считать белья и чулок."
    "Похоже на что-то довольно экстравагантное. Собралась куда-то?"
    mc.c "Чё как, красотка?"
    scene zoehevent7i2 with fade
    pause
    zoe.c "Хм?.. Вот так обращаются с дамой~"
    mc.c "Называю вещи своими именами."
    zoe.c "Да ещё и подглядываешь, пока я переодеваюсь? Как невежливо."
    mc.c "Чем занимаешься?"
    zoe.c "Сегодня иду с девчонками в клуб, там альтернативная вечеринка."
    zoe.c "Я бы тебя позвала, но..."
    mc.c "Ага. Нет."
    zoe.c "И правильно. Не хватало ещё, чтобы твоё {i}чувство стиля{/i} нас отпугнуло."
    mc.c "Эй..."
    "Она позирует, подчёркивая красивые бёдра и ноги в сетчатых чулках..."
    "Я заворожён. Зои усмехается мне в ответ."
    mc.c "Так... Что наденешь?"
    zoe.c "Ну~ Думаю, вот это. Секси, да?"
    "Она держит короткое платье. Оно выглядит таким узким и изящным — удивительно, что она вообще в него влезает."
    mc.c "Ага."
    zoe.c "Хе-хе~ Сразу вижу. Вот что в тебе хорошо, худыш: всё написано на лице."
    zoe.c "Мнение честного мужчины~"
    scene zoehevent7i3 with fade
    pause
    zoe.c "Например, если я спрошу, как мои ножки в этих чулках~?"
    mc.c "Вкусно."
    zoe.c "Хе-хе~ Вот это мне нравится."
    "Она точно умеет себя показать. Настоящая искусительница."
    "Она и правда заставляет всех оборачиваться..."
    zoe.c "Ха-ха~ Ой, милашка, всё хорошо~"
    zoe.c "Не ревнуй, это просто девичник, худыш."
    mc.c "Н-нет, я не... Делай что хочешь."
    zoe.c "Как скажешь, жеребец~ Мне просто нравится танцевать под огнями."
    zoe.c "Так кровь разгоняется, эндорфины выделяются — почти как тренировка."
    "А у меня кровь уже кипит."
    zoe.c "Хм~ Я знаю это лицо, худыш. Наверное, думаешь: «Вот сейчас-то у меня кровь и разгоняется», да?"
    "Боже, какой же я простак."
    zoe.c "Ты такой простак~"
    scene zoehevent7i4 with fade
    pause
    "Зои подходит ко мне, проводя когтем по моей груди."
    mc.c "Ты меня слишком хорошо знаешь."
    zoe.c "Тебя читать проще простого... Как открытую книгу. Но знаешь..."
    zoe.c "Именно за это я тебя так люблю."
    "Вот это мило."
    mc.c "Я тоже тебя люблю."
    zoe.c "Хочешь помочь мне перед вечеринкой? Немного завести меня заранее?"
    mc.c "Да? Выпить по коктейлю?"
    zoe.c "Не то."
    call playMusic(sexyTheme) from _call_playMusic_289
    scene zoeanalagainstwallstart1 with fade
    pause
    zoe.c "Трахни меня~"
    "Зои стягивает трусики и подставляет мне зад."
    "Эта сексуальная попка поверх чулок... Эти крепкие пушистые бёдра..."
    "Не стану задавать вопросов."
    mc.c "Да, мэм."
    zoe.c "Ненавижу, когда ты так говоришь..."
    zoe.c "Но этот член мне нравится. Иди сюда."
    scene zoeanalagainstwallstart2 with fade
    pause
    "Я крепко обхватываю её за талию и пристраиваюсь."
    zoe.c "Ой, подожди."
    mc.c "Что такое?"
    zoe.c "Я буду пить. С таблетками это плохо сочетается."
    mc.c "О-о."
    zoe.c "Завтра придётся пропустить таблетку, так что..."
    zoe.c "Давай в задницу."
    mc.c "Ух ты! Ты уверена?"
    zoe.c "Не делай {i}такое{/i} восторженное лицо, худыш. Только осторожно. У тебя же там монстр."
    "Мысль соблазнительна. Головка моего члена упирается в её задний проход."
    mc.c "Точно?"
    zoe.c "Давай."
    image zoeAnalAgainstWall1 = Movie(play="images/characters/zoe/hscenes/analAgainstWall/part1.webm")
    scene zoeAnalAgainstWall1 with fade
    pause
    "Слегка надавив, я преодолеваю сопротивление и вхожу в её задницу."
    "Зои прогибается, когда я проникаю в неё, но сама подаётся навстречу."
    zoe.c "О-ох, блядь..."
    zoe.c "Боже~ М-м... Ты всегда был таким толстым?"
    mc.c "Ты в порядке?"
    zoe.c "Конечно, жеребец~ М-м~ Продолжай~"
    "Она расслабляется, и проникновение становится плавнее."
    "Но её крепкая задница всё равно сжимает мой член мёртвой хваткой."
    mc.c "Чёрт... Зои..."
    zoe.c "А-а~ Наслаждайся, жеребец... М-м~ Тебе сегодня повезло~"
    "Её напряжённые вздохи постепенно превращаются в стоны наслаждения. Она не стала бы соглашаться, если бы не хотела."
    mc.c "Как же приятно."
    zoe.c "Давай, жеребец. Ха-а~ Трахни меня как следует~"
    "Она дразнит меня, подталкивая войти глубже. Я хватаю её за бёдра, готовясь к этому."
    image zoeAnalAgainstWall2 = Movie(play="images/characters/zoe/hscenes/analAgainstWall/part2.webm")
    scene zoeAnalAgainstWall2 with fade
    pause
    "Резким толчком я полностью вхожу в её задницу, прижимаясь бёдрами к её бёдрам."
    zoe.c "А-а-а~! А-а-а, блядь~!"
    "Я снова чувствую, как она напрягается вокруг меня. Едва удерживаюсь внутри."
    zoe.c "Вот так~ Трахай~ Давай, жеребец~!"
    "Она повисает, едва держась за стену, поддаваясь моему напору."
    "Её крепкая хватка лишь подзадоривает меня. Я сильнее прижимаю её и ускоряю толчки."
    "Из киски течёт целый поток сока, смачивая шерсть между её ног."
    mc.c "М-м~ Зои~"
    zoe.c "Блядь! Да! М-м~!"
    zoe.c "Трахни меня как следует! Трахай эту задницу!"
    "Она содрогается от каждого толчка, но сопротивление постепенно ослабевает."
    image zoeAnalAgainstWall3 = Movie(play="images/characters/zoe/hscenes/analAgainstWall/part3.webm")
    scene zoeAnalAgainstWall3 with fade
    pause
    "Я подхватываю её за плечо и помогаю выпрямиться."
    "Для упора я поднимаю её ногу и начинаю быстро и сильно трахать её в зад."
    zoe.c "А-А-А! БЛЯДЬ!"
    zoe.c "Так глубоко~ Ха-а~"
    "Она прижимается лицом к стене. От силы и наслаждения глаза закатываются."
    "Её хвост яростно виляет в такт движениям; наши бёдра влажно и непристойно шлёпаются друг о друга."
    "Ощущения невероятные: тугая хватка, изгибы её тела, вся эта грязь на Зои."
    "Слишком хорошо. Я сейчас..."
    mc.c "Чёрт, Зои, я сейчас кончу."
    zoe.c "Ха-а~ Ха-а~ Давай~ Заполни эту задницу спермой~"
    scene zoeanalagainstwallfinish1 with fadewhite
    pause
    mc.c "М-мф~!"
    "Последним сильным движением я вхожу как можно глубже и изливаю сперму ей в задницу."
    zoe.c "М-м-м-м~!"
    "Она не может сдержать её, и сперма быстро вытекает вокруг моего члена."
    "Я чувствую, как она вздрагивает и извивается, пока я медленно двигаюсь внутри, выжимая из себя всё."
    scene zoeanalagainstwallfinish2 with fade
    pause
    "Когда Зои приходит в себя, я медленно выскальзываю из неё; её зияющая задница издаёт влажный хлопок."
    "Густая струя спермы вытекает из неё и стекает по мокрой киске."
    zoe.c "Ха-а~ Ха-а~ Боже, блядь~"
    zoe.c "Это было..."
    "Она редко теряет дар речи. Правда ли она была готова к такому?"
    mc.c "Жарко."
    zoe.c "Ага~ Чертовски жарко~"
    zoe.c "Кажется, сегодня я уже не буду танцевать..."
    scene black with fade
    "Я помогаю Зои привести себя в порядок. Она всё равно собирается сегодня гулять."
    "Она ковыляет к выходу, заметно прихрамывая."
    "Сумасшедшая."

    return
