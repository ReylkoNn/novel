init offset = 3
default grace = Person(Character(name='Grace', who_color='#ee4e56', image = 'grace'), 'Grace', '', 'grace', 'female', 22)

label initialiseCharacter_grace:
    python:
        grace.currentLocation = location_shop
        location_shop.occupants.extend([grace])
        grace.availableEvents = [graceFirstMeetingEvent]
        
    return

label updateCharacterStatics_grace:
    python:
        # Personal attributes
        grace.species = 'Rabbit'
        grace.birthday = 6
        grace.job = 'Cashier'
        grace.giftLoves = [item_videogame]
        grace.giftLikes = [item_chocolateBar, item_book]
        grace.giftHates = [item_wine, item_dress]

        # Skill attributes

        # Sexual attributes


        # Personal effects

        # Event attributes
        grace.events = [graceFirstMeetingEvent, graceLikeEvent1, graceLikeEvent2, graceLikeEvent3, graceLikeEvent4, graceHEvent1, graceHEvent2, graceHEvent3, graceHEvent4, graceHEvent5, graceHEvent6, graceHEvent7, graceVacation, graceLikeEvent5, graceHEvent8]
        grace.specialEvents = [graceJessicaDuoStoryEvent1, graceJessicaDuoHEvent1, graceMollyDuoStoryEvent1, graceMollyDuoHEvent1]
        grace.selfieOptions = ['bedroom1', 'bedroom2', 'bedroom3', 'bedroom4', 'homebedroom1']
        grace.wakeUpOptions = ['blowjob']
        grace.dateChats = ['Background', 'Job', 'Hobbies']
        grace.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = grace.events[-1]
        grace.maxLike = lastStoryEvent.requiredLike
        grace.maxLove = lastStoryEvent.requiredLove

        # World attributes
        grace.preferredMondaySchedule = [location_away, location_shop, location_shop, location_away]
        grace.preferredTuesdaySchedule = [location_away, location_shop, location_shop, location_town]
        grace.preferredWednesdaySchedule = [location_away, location_away, location_away, location_away]
        grace.preferredThursdaySchedule = [location_park, location_theater, location_diner, location_away]
        grace.preferredFridaySchedule = [location_shop, location_shop, location_bar, location_away]
        grace.preferredSaturdaySchedule = [location_shop, location_shop, location_park, location_away]
        grace.preferredSundaySchedule = [location_away, location_shop, location_beach, location_away]

        grace.preferredMovedInMondaySchedule = [location_home, location_shop, location_shop, location_home]
        grace.preferredMovedInTuesdaySchedule = [location_home, location_shop, location_shop, location_home]
        grace.preferredMovedInWednesdaySchedule = [location_home, location_home, location_home, location_home]
        grace.preferredMovedInThursdaySchedule = [location_home, location_home, location_home, location_home]
        grace.preferredMovedInFridaySchedule = [location_home, location_shop, location_home, location_home]
        grace.preferredMovedInSaturdaySchedule = [location_home, location_shop, location_home, location_home]
        grace.preferredMovedInSundaySchedule = [location_home, location_shop, location_home, location_home]
    return

# Sprites
screen graceClickable(xcenter):
    $ spriteload = grace.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = grace)
        at characterSpriteHover

# Character methods
label graceEvaluateAvailableInteractions:
    python:
        if grace.like >= 5 and graceLikeEvent3.unlocked:
            grace.availableActions = list(set(grace.availableActions + ['Spend time']))
        if grace.like >= 20 and graceHEvent3.unlocked:
            grace.availableActions = list(set(grace.availableActions + ['Invite over']))

        if grace.isDateable and grace.love >= 1:
            grace.availableActions = list(set(grace.availableActions + ['Date']))
        if grace.love >= 3 and graceLikeEvent2.unlocked:
            grace.availableActions = list(set(grace.availableActions + ['Affection']))
            grace.availableAffections.extend(['Pat'])
        if grace.love >= 6 and graceLikeEvent3.unlocked:
            grace.availableAffections.extend(['Hug', 'Chin Scratch'])
        if grace.love >= 10 and graceLikeEvent4.unlocked:
            grace.availableAffections.extend(['Kiss'])
        if graceHEvent4.unlocked:
            grace.availableAffections.extend(['Caress Butt'])
        if graceHEvent6.unlocked:
            grace.availableAffections.extend(['Boob Grab'])
        if graceHEvent8.unlocked:
            grace.availableActions.extend([{'homebathroom': ['Blowjob']}])
        if grace.movedIn:
            grace.availableCommandsPrivate.extend(['Show Panties'])
            grace.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label graceChat:
    show grace smile talk
    return

label graceChat_beach:
    if(timeOfDay != 'Night'):
        show grace mad talk
        grace.c "Солнце так слепит... Ничего не видно на экране."
    else:
        show grace smile talk
        grace.c "Фух~ Хоть солнце уже село."
    return

label graceChat_park:
    show grace thinking
    grace.c "Н-ну, здесь довольно приятно. Тише, чем где бы то ни было..."
    return

label graceChat_shop:
    if(graceLikeEvent4.unlocked):
        show grace smile talk 2
        if(grace.movedIn):
            grace.c "Привет, дорогой!"
        else:
            grace.c "[mc.name]! Привет!"
    else:
        show grace neutral talk
        grace.c "О-ой, э-э... привет..."
    return

label graceChat_diner:
    show grace bashful talk
    grace.c "Деньги, что я получаю, хоть позволяют иногда вкусно поесть..."
    show grace mad talk
    grace.c "Но на этом польза от работы заканчивается."
    return

label graceChat_cafe:
    show grace neutral talk
    grace.c "Ах... Почему здесь всегда так много народу..."
    return

label graceChat_town:
    if(graceLikeEvent4.unlocked):
        show grace smile talk
        grace.c "О, привет, [mc.name]."
        show grace thinking
        grace.c "Прости, я просто так устала после работы."
    else:
        show grace sad talk
        grace.c "Блин... Я так вымоталась... Сколько это ещё будет продолжаться?"
    return

label graceChat_bar:
    if(graceLikeEvent4.unlocked):
        show grace smile talk
        grace.c "Наверное, выпью чего-нибудь..."
        grace.c "Ты же знаешь, что я люблю."
    else:
        show grace bashful talk
        grace.c "М-меня коллеги сюда затащили. Не понимаю зачем, я не привыкла к таким местам."
    return

label graceChat_aquarium:
    show grace smile talk
    grace.c "Я иногда сюда захожу. Тут никогда не бывает многолюдно..."
    return

label graceChat_theater:
    show grace smile talk
    grace.c "Я так долго ждала этот фильм! Обожаю это аниме."
    show grace mad talk
    grace.c "Я-и настоящее кино иногда смотрю!"
    return

label graceChat_homebedroom:
    if(timeOfDay == 'Morning'):
        show grace thinking
        grace.c "Уф, разбуди меня через пять минут... Мне же тоже на работу..."
    elif(timeOfDay == 'Afternoon'):
        show grace tease talk
        grace.c "Хе-х~ На работу идёшь, работяга~? Захвати мне по дороге вкусняшек~"
    elif(timeOfDay == 'Evening'):
        show grace joy
        grace.c "А-а-а~ У тебя такая удобная кровать~ Не хочу вставать~"
    elif(timeOfDay == 'Night'):
        show grace smile talk 2
        grace.c "Ладно, ладно, я уже закончила. Теперь можешь ложиться~"
    return

label graceChat_homelounge:
    if(timeOfDay == 'Morning'):
        show grace thinking
        grace.c "У меня совсем сбился режим сна. По утрам никогда ничего интересного..."
    elif(timeOfDay == 'Afternoon'):
        show grace smile talk
        grace.c "Эй, эй, посмотри со мной, [mc.name]~"
    elif(timeOfDay == 'Evening'):
        show grace tease talk
        grace.c "Можем посмотреть новое аниме, если хочешь. Ну, то пошлое~"
    elif(timeOfDay == 'Night'):
        show grace tease
        grace.c "Уже спать? Слабак~"
    return

label graceChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show grace mad talk
        grace.c "Эй, эй, всё вкусное из хлопьев закончилось!"
    elif(timeOfDay == 'Afternoon'):
        show grace thinking
        grace.c "Готовить? Э-э, не знаю... В шкафу есть снеки..."
    elif(timeOfDay == 'Evening'):
        show grace smile talk
        grace.c "Я голодная... Приготовишь мне что-нибудь~? Пожалуйста~?"
    elif(timeOfDay == 'Night'):
        show grace smile talk
        grace.c "Погоди, мне надо пройти этот уровень..."
    return

# Date topics
label graceChat_background:
    show grace thinking
    grace.c "Э-э... Н-ну..."
    grace.c "Я местная... Училась неподалёку. Это совсем близко к твоему бару..."
    show grace neutral talk
    grace.c "И-и ты уже знаешь, что я живу дома..."
    show grace neutral
    mc.c "Только ты и мама, да?"
    show grace thinking
    grace.c "Да... почему-то она хотела только одного ребёнка... Для кроликов это необычно..."
    grace.c "А-а ещё... Папа ушёл, когда мне было тринадцать..."
    mc.c "Прости..."
    show grace neutral talk
    grace.c "Н-не надо, всё нормально... Он был... м-мудаком... Даже когда жил с мамой, почти не участвовал в нашей жизни..."
    grace.c "Говорил, что это из-за работы... Не понимаю..."
    show grace thinking
    grace.c "В-в общем, он что-то замышлял... Наверное, изменял... Вот они и расстались."
    mc.c "Мне жаль, Грейс. Как мама это пережила?"
    show grace sad talk
    grace.c "Ей было очень больно... Но она понимает, что так было лучше. Без него нам лучше."
    show grace smile talk
    grace.c "Мы стали ближе, чем когда-либо... Дома теперь всё намного лучше. Я люблю маму... Она меня вырастила."
    show grace bashful talk
    grace.c "Ну, она и сейчас за мной приглядывает..."
    show grace bashful
    mc.c "Ты ведь только недавно начала работать?"
    show grace bashful talk
    grace.c "Д-да... После школы я искала работу, но... Испугалась."
    grace.c "Так и... осталась дома..."
    show grace neutral talk
    grace.c "Не хочу об этом говорить... Прости..."
    "Больная тема. Лучше не продолжать."
    return

label graceChat_job:
    mc.c "Как тебе работается в магазинчике?"
    show grace sad talk
    grace.c "Уф... Ну... как-то так..."
    grace.c "Только на полставки. Больше я, наверное, не потяну."
    show grace sad
    mc.c "Как ты там оказалась?"
    show grace thinking
    grace.c "Я захотела помогать маме и вносить деньги на домашние расходы. Слишком долго была для неё обузой."
    mc.c "Она так сказала?"
    show grace neutral talk
    grace.c "Н-нет, нет... Она никогда меня ни к чему не принуждала... Сказала, что мне это пойдёт на пользу, но знает, какая я..."
    show grace thinking
    grace.c "Я понимала, что она права, просто ужасно боялась."
    show grace neutral talk
    grace.c "Однажды зашла туда за покупками и увидела объявление. Оно уже давно висело."
    grace.c "Работа на полставки... Гибкий график... Я и так часто там покупала, да и народу обычно немного."
    grace.c "Наверное, это лучший вариант после нескольких лет безработной затворницы."
    show grace neutral
    mc.c "Так, не всё так плохо?"
    show grace smile talk
    grace.c "Ага... Наверное. Коллеги нормальные, хоть и немного... обычные."
    grace.c "И мама рада. Наверное, поэтому работа и кажется стоящей."
    show grace smile
    mc.c "Я тоже могу зайти и поболтать. Если тебе станет скучно."
    show grace bashful
    grace.c "Хм... Ага..."
    return

label graceChat_hobbies:
    show grace bashful talk
    grace.c "Э-э... Я вообще-то полная задротка, но ты уже знаешь..."
    show grace bashful
    mc.c "И я не против. Это ты тоже знаешь."
    show grace thinking
    grace.c "...Ага."
    mc.c "Но чем конкретно увлекаешься?"
    show grace neutral
    grace.c "Видеоигры... Аниме... Манга, комиксы... Всё такое."
    grace.c "Почти всё время сижу за компьютером. Наверное, звучит скучно."
    mc.c "А вот косплей интересный."
    show grace bashful talk
    grace.c "А-а... Жаль, что ты увидел меня в нём в первый раз... Это было так глупо."
    show grace bashful
    mc.c "Понимаю, что ты не хочешь показывать костюмы кому попало, но, по-моему, это круто."
    mc.c "Я тоже по-своему задрот. Раньше больше смотрел и читал, чем сейчас."
    show grace thinking
    grace.c "Всё равно это не особо полезное увлечение..."
    mc.c "Зато шитьё требует мастерства. Это впечатляет. Я даже собственные рваные джинсы зашить не могу."
    show grace tease talk
    grace.c "Хе-х~ Д-да, я видела дырки на твоей одежде."
    show grace surprise
    grace.c "Н-не то чтобы я... Э-э..."
    show grace thinking
    grace.c "Л-ладно... Может быть..."
    mc.c "В какие видеоигры ты играешь?"
    show grace smile talk
    grace.c "Раньше я увлекалась некоторыми ММО... И приключенческими играми."
    show grace thinking
    grace.c "Но с тех пор, как я начала работать, времени почти не осталось... Теперь в основном играю на телефоне."
    mc.c "На телефонах вообще бывают хорошие игры?"
    show grace smile talk
    grace.c "Конечно, полно! Там такие милые персонажи и всё такое. Вот, смотри..."
    show grace smile
    "Похоже и звучит как гача-игры..."
    return

#

label graceInteractionBathroom:
    grace.c "[mc.name]? Я-я здесь..."
    grace.c "...Ты на меня смотришь..."
    return

label graceSpendTime(onDate):
    if(onDate):
        scene expression 'grace[mc.currentLocation.apiName]date'
    else:
        scene expression 'grace[mc.currentLocation.apiName]'
    with fade
    return

label graceReceiveGift(item, likeChange, loveChange):
    show grace bashful talk
    grace.c "А-а? Ты хочешь подарить мне что-то?"
    if(loveChange > 0):
        show grace surprise
        grace.c "Т-ты ведь не шутишь?"
        show grace joy
        grace.c "О боже! С-спасибо огромное!"
        if(graceVacation.unlocked):
            grace.c "Я тебя так люблю!"
    elif(likeChange > 1):
        show grace smile talk
        grace.c "Правда? Это очень мило... Спасибо!"
        if(graceVacation.unlocked):
            grace.c "Я тебя не заслуживаю..."
    elif(likeChange < 1):
        show grace sad
        grace.c "Э-э... С-спасибо, наверное..."
    else:
        show grace smile talk
        grace.c "Спасибо."
    return

label graceReceiveDateInvitation:
    if(graceVacation.unlocked):
        show grace smile talk
        grace.c "Да, с радостью!"
        show grace smile
    else:
        show grace surprise
        grace.c "А? С-со мной?"
        show grace neutral
    call dateInvitationSelector(grace) from _call_dateInvitationSelector_2
    show grace smile talk
    grace.c "[proposedDateDayOfWeek], [proposedDateTime], в [proposedDateLocation.name]? Л-ладно!"

    python:
        scheduledDate = Date(grace, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        grace.scheduledDates.append(scheduledDate)
    return

label graceStartDate:
    if(mc.currentLocation == location_home):
        show grace bashful talk with dissolve
        grace.c "П-привет, [mc.name]..."
    else:
        show grace smile talk with dissolve
        grace.c "Т-ты правда пришёл...!"
    return

label graceDateInteraction:
    show grace smile with dissolve
    show screen dateUi(grace) with dissolve
    call screen dateInteractionScreen(grace, mc.currentLocation)

label graceChatDate:
    show grace smile talk 2
    grace.c "М-мне здесь нравится..."
    return

label graceChatDate_beach:
    show grace neutral
    grace.c "Я... не очень хорошо переношу солнце."
    show grace surprise
    grace.c "Я н-не жалуюсь! Просто... посижу в тени..."
    return

label graceChatDate_park:
    show grace smile talk 2
    grace.c "Ты часто сюда приходишь?"
    show grace smile talk
    grace.c "Наверное, здесь неплохо... Ну, на природе..."
    return

label graceChatDate_diner:
    show grace bashful
    grace.c "П-прости, я, наверное, слишком много ем..."
    show grace surprise
    grace.c "А?! М-мило? П-прекрати..."
    return

label graceChatDate_cafe:
    show grace thinking
    grace.c "Здесь всегда так много народу?"
    show grace smile talk
    grace.c "Ну... Ты нашёл для нас столик в углу. Спасибо."
    return

label graceChatDate_bar:
    show grace neutral talk
    grace.c "То есть... тут в основном кола?"
    show grace tease
    grace.c "О-о~ На самом деле, довольно вкусно..."
    return

label graceChatDate_aquarium:
    show grace tease talk
    grace.c "Хе-хе~ Посмотри на его мордочку..."
    grace.c "Он такой милый."
    return

label graceChatDate_theater:
    show grace smile talk
    grace.c "Спасибо, что привёл меня."
    show grace tease talk
    grace.c "О-о~ Купим попкорн?"
    return

label graceDatePayFor:
    if(graceVacation.unlocked):
        show grace tease talk
        grace.c "Ой, ты всё время мне что-нибудь покупаешь~"
        grace.c "Ты, наверное, правда меня любишь! Хе-х~"
    else:
        show grace surprise
        grace.c "Эй, тебе не обязательно..."
    return

label graceEndDate:
    if(dateScore < 40):
        show grace sad 
        grace.c "Прости... Знаю, со мной скучно..."
    else:
        if(grace.movedIn):
            show grace joy
            grace.c "Хе-х~ Сегодня было очень весело!"
            grace.c "Я тебя очень люблю, [mc.name]!"
        else:
            show grace tease talk
            grace.c "Это было здорово, [mc.name]. Спасибо..."
            if(graceVacation.unlocked):
                show grace joy
                grace.c "Люблю тебя!"
    return

label graceContinueDateAtHome:
    scene expression 'grace[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(graceHEvent3.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label graceHomeStartSex:
    show grace tease talk
    grace.c "Хе-х~ Извращенец~"
    grace.c "Но вообще я и правда хочу~"
    show grace tease
    return

label graceHomeSexJoinIn(character):
    show grace bashful talk at twoPersonLeft with dissolve
    grace.c "[mc.name[0]]-[mc.name]... [character.name[0]]-[character.name]..."
    grace.c "М-можно я... присоединюсь?"
    show grace bashful
    return

label graceEndDateAtHome:
    if(graceVacation.unlocked):
        grace.c "Мне пора... Но скоро увидимся."
        grace.c "И, [mc.name]? Люблю тебя~"
    else:
        grace.c "Можно я как-нибудь снова к тебе зайду?"
    return

image grace pat animated = Movie(play="images/characters/grace/affections/gracePat.webm", side_mask=True, loop=True)
label graceReceivePat:
    hide grace with dissolve
    show grace pat animated with dissolve
    pause
    grace.c "Хе-хе-хе~"
    grace.c "Не думала, что люди и правда так делают~"
    return

image grace chinscratch animated = Movie(play="images/characters/grace/affections/graceChinscratch.webm", side_mask=True, loop=True)
label graceReceiveChinScratch:
    hide grace with dissolve
    show grace chinscratch animated with dissolve
    pause
    grace.c "Э-эй, ну же..."
    grace.c "Мне неловко..."
    return

image grace caressbutt animated = Movie(play="images/characters/grace/affections/graceCaressButt.webm", side_mask=True, loop=True)
label graceReceiveCaressButt:
    hide grace with dissolve
    show grace caressbutt animated with dissolve
    pause
    grace.c "[mc.name:.1]-[mc.name]~!"
    grace.c "М-можешь, только... осторожно..."
    return

image grace boobgrab animated = Movie(play="images/characters/grace/affections/graceBoobGrab.webm", side_mask=True, loop=True)
label graceReceiveBoobGrab:
    hide grace with dissolve
    show grace boobgrab animated with dissolve
    pause
    grace.c "Эй... Ты ведь меня дразнишь, да?"
    grace.c "Хмф... Ладно, если хочешь, глупыш~"
    return

image grace snuggle animated = Movie(play="images/characters/grace/affections/graceSnuggle.webm", side_mask=True, loop=True)
label graceReceiveSnuggle:
    "Я сажусь рядом с Грейс на диван."
    show grace smile talk
    grace.c "Эй, что такое?"
    hide grace with dissolve
    show grace snuggle animated with dissolve
    pause
    "Я протягиваю руку, обнимаю её и притягиваю к себе. Она кладёт голову мне на грудь."
    grace.c "О-о, [mc.name]... Что ты делаешь~?"
    pause
    return

label graceReceiveHug:
    hide grace with dissolve
    show grace hug with dissolve
    pause
    grace.c "М-м-м~"
    if(graceHEvent5.unlocked):
        grace.c "Обними меня покрепче~"
    else:
        grace.c "П-погоди, от меня же не пахнет?"
    return

label graceReceiveKiss:
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "*Чмок~*"
    pause
    grace.c "А-а~ Можно... ещё?"
    return

label graceInitiatePat:
    show grace bashful talk with dissolve
    if(grace.movedIn):
        grace.c "М-милый..."
    else:
        grace.c "[mc.name]..."
    grace.c "Я... х-хочу..."
    "[grace.name] ёрзает на месте. Кажется, я понимаю, чего она хочет."
    hide grace with dissolve
    show grace pat animated with dissolve
    pause
    grace.c "Хе-хе-хе~"
    grace.c "Спасибо..."
    return

label graceInitiateHug:
    show grace neutral talk with dissolve
    grace.c "Э-эй!"
    "[grace.name] нерешительно раскрывает объятия, приглашая меня."
    hide grace with dissolve
    show grace hug with dissolve
    pause
    if(grace.movedIn):
        grace.c "Хе-хе~ Люблю тебя."
    else:
        grace.c "Т-тебе нормально?"
    return

label graceInitiateKiss:
    show grace joy with dissolve
    if(grace.movedIn):
        grace.c "Милый!"
    else:
        grace.c "[mc.name]!"
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "*Чмок~*"
    pause
    hide grace with dissolve
    show grace surprise with dissolve
    grace.c "Прости... Э-это было слишком?"
    return

label graceInitiateSnuggle:
    show grace smile
    "Я отдыхаю на диване, когда Грейс подходит ко мне."
    show grace smile talk
    grace.c "М-милый... Можно немного обняться?"
    hide grace with dissolve
    show grace snuggle animated with dissolve
    pause
    "Я раскрываю объятия и крепко прижимаю её к себе."
    grace.c "Хе-х~ Спасибо... Люблю тебя."
    pause
    return

label graceInitiateHomeSex:
    show grace bashful
    grace.c "..."
    show grace mad talk
    grace.c "Чёрт, [mc.name], я так возбуждена! Трахни меня!"
    show grace mad
    return

label graceInitiateHomeSexDeny:
    show grace thinking
    grace.c "Блин... Придётся самой подрочить. Но это будет совсем не то..."
    return

label graceSeesAffection(affection):
    show grace bashful with dissolve
    "Я замечаю, как Грейс нервно ёрзает рядом. Она нас видела и, уверен, хочет присоединиться..."
    mc.c "Просто попроси, Грейс."
    show grace surprise
    grace.c "А? Я..."
    "Я приглашаю её присоединиться."
    call expression 'graceReceive' + affection from _call_expression_39
    hide grace with dissolve
    return

label graceInviteOver:
    show grace smile talk
    grace.c "О, здорово. Будем что-нибудь смотреть?"
    return

label graceInitiateInviteOver:
    show grace bashful talk
    grace.c "Э-э... Можно... пойти к тебе домой?"
    show grace bashful
    menu:
        'Yes':
            show grace joy
            grace.c "П-правда? Ура!"
            return True
        'No':
            show grace neutral talk
            grace.c "А... Ничего страшного."
    return False

label graceInviteGoHomeTogether:
    show grace smile talk
    grace.c "Мы... вместе идём домой... В один и тот же дом..."
    show grace joy 
    grace.c "Хе-хе~ Не верится~"
    return

label graceInitiateGoHomeTogether:
    show grace thinking
    grace.c "Я устала... Пойду домой. Ты идёшь, милый?"
    show grace thinking
    menu:
        'Yes':
            show grace tease talk
            grace.c "Хе-х~ Ура~"
            return True
        'No':
            show grace smile talk
            grace.c "Ладно. Может, я уже буду спать, когда ты вернёшься. Пока!"
    return False

label graceShowPanties(pantiesIndex = 1):
    show grace thinking
    grace.c "...Извращенец."
    if(pantiesIndex == 1):
        $ renpy.show(grace.apiName + ' panties ' + str(pantiesIndex), tag=grace.apiName)
        with dissolve
        grace.c "Они просто из дешёвого набора из магазина..."
    elif(pantiesIndex == 2):
        $ renpy.show(grace.apiName + ' panties ' + str(pantiesIndex), tag=grace.apiName)
        with dissolve
        grace.c "Хе-хе~ Полосатые~ Немного маловаты..."
    elif(pantiesIndex == 3):
        grace.c "О-ой, чёрт... Кажется..."
        $ renpy.show(grace.apiName + ' panties ' + str(pantiesIndex), tag=grace.apiName)
        with dissolve
        grace.c "Сегодня без них... Хе-х~"
    return

label graceSendDateText(proposedDate):
    python:
        timeText = {'Morning': 'утром', 'Afternoon': 'днём', 'Evening': 'вечером', 'Night': 'ночью'}.get(proposedDateTime, proposedDateTime.lower())
        locationPhrase = {'beach': 'на пляж', 'park': 'в парк', 'town': 'в город', 'cafe': 'в кафе', 'library': 'в библиотеку', 'diner': 'в закусочную', 'bar': 'в бар', 'aquarium': 'в океанариум', 'theater': 'в театр', 'shop': 'в магазин'}.get(proposedLocation.apiName, 'в «' + _(proposedLocation.name).lower() + '»')
        grace.textChain.append(Message(mc, grace, 'я тут подумал... Ты не обязана, но', Null, day, timeOfDay))
        grace.textChain.append(Message(mc, grace, 'не хочешь завтра сходить ' + locationPhrase + '? Может быть... ' + timeText + '? >_<', Null, day, timeOfDay, proposedDate))
    return

label graceGetSelfieOptions:
    $ graceSelfieOptions = []
    if(graceLikeEvent3.unlocked):
        $ graceSelfieOptions.extend(['bedroom1'])
    if(graceHEvent2.unlocked):
        $ graceSelfieOptions.extend(['bedroom2'])
    if(graceHEvent3.unlocked):
        $ graceSelfieOptions.extend(['bedroom3'])
    if(graceHEvent4.unlocked):
        $ graceSelfieOptions.extend(['bedroom4'])
    if(grace.movedIn):
        $ graceSelfieOptions.extend(['homebedroom1'])
    return graceSelfieOptions

label graceSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'bedroom1':
                potentialResponses.append({'text': "Впечатляет! Я знаю это аниме!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Чертовски милая!", 'statChange': 'love', 'statChangeAmount': 1})
                grace.textChain.append(Message(mc, grace, 'один из моих косплеев ^_^', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom2':
                potentialResponses.append({'text': "Ха-ха, возможно...", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Похоже, теперь не нужно гадать >:)", 'statChange': 'love', 'statChangeAmount': 1})
                grace.textChain.append(Message(mc, grace, 'помнишь её? интересно, что на ней под одеждой? а мне вот... x3', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom3':
                potentialResponses.append({'text': "Непослушная", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Теперь у меня есть всё, чтобы сделать то же самое", 'statChange': 'love', 'statChangeAmount': 1})
                grace.textChain.append(Message(mc, grace, 'спорим, не угадаешь, чем я занималась XD', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom4':
                potentialResponses.append({'text': "Чёрт!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Я сохраню их в секрете, если сделаешь, что я скажу... >:)", 'statChange': 'love', 'statChangeAmount': 1})
                grace.textChain.append(Message(mc, grace, 'ой, злой господин... что ты собираешься сделать с этими фотографиями??? >:3', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homebedroom1':
                potentialResponses.append({'text': "Сегодня будешь спать на том краю", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Я уж доведу тебя до конца, не волнуйся", 'statChange': 'love', 'statChangeAmount': 1})
                grace.textChain.append(Message(mc, grace, 'разогреваюсь, пока жду тебя >_<', selfieName, day, timeOfDay, responses = potentialResponses))
    return

label graceSexSelect:
    hide screen mainUi
    scene black with fade
    image grace sex waiting = Movie(play="images/characters/grace/hscenes/sexWaiting.webm")
    show grace sex waiting with fade

    call screen graceSexSelectScreen
    if(graceHEvent5.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(grace.movedIn):
            menu graceSleepTogether:
                "Переспать с Грейс?"
                'Yes':
                    grace.c "Не могу встать... Можно я сегодня останусь здесь?"
                    grace.c "Хе-х~ Спокойной ночи... Люблю тебя, милый~"
                    call characterSleepover(grace) from _call_characterSleepover_4
                'No':
                    pass
        else:
            menu graceStayTheNight:
                "Предложить [grace.name] остаться на ночь?"
                'Yes':
                    $ grace.addLove(1)
                    grace.c "Правда? Д-да!"
                    call characterSleepover(grace) from _call_characterSleepover_5
                'No':
                    grace.c "Тебе... понравилось?"
    
    call endScene(character = grace, targetLocation = location_home) from _call_endScene_10

screen graceSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(graceHEvent2.unlocked or persistent.debugMode):
                textbutton 'Handjob' keysym str(1):
                    action [Jump('graceHandjob')]
            else:
                textbutton 'Locked'
            if(graceHEvent3.unlocked or persistent.debugMode):
                textbutton 'Blowjob' keysym str(2):
                    action [Jump('graceBlowjob')]
            else:
                textbutton 'Locked'
            if(graceHEvent5.unlocked or persistent.debugMode):
                textbutton 'Missionary' keysym str(3):
                    action [Jump('graceMissionary')]
            else:
                textbutton 'Locked'
            if(graceHEvent6.unlocked or persistent.debugMode):
                textbutton 'Doggy style' keysym str(4):
                    action [Jump('graceDoggystyle')]
            else:
                textbutton 'Locked'
            if(graceHEvent7.unlocked or persistent.debugMode):
                textbutton 'Anal' keysym str(5):
                    action [Jump('graceAnal')]
            else:
                textbutton 'Locked'
            if(graceVacation.unlocked or persistent.debugMode):
                textbutton 'Cowgirl' keysym str(6):
                    action [Jump('graceCowgirl')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(7):
                action [Hide('graceSexSelectScreen'), Return()]

label graceSleepover:
    scene gracesleepover with fade
    pause
    return

label graceMorningBedInteraction:
    scene gracehomemorning with fade 
    pause
    if(grace.movedIn):
        grace.c "М-м~ Доброе утро, [mc.name]~"
        grace.c "Ой, тебе правда надо вставать? Может, останешься со мной? Пожалуйста~"
    else:
        grace.c "*Зевает*~"
        grace.c "О-ой... Привет, [mc.name]... Забыла, что я здесь."
        grace.c "Ты смотрел, как я сплю?"
    return

label graceMorningBedInteractionSex(event):
    if(event == 'blowjob'):
        image grace morning blowjob 1 = Movie(play="images/characters/grace/hscenes/morning/blowjob1.webm")
        show grace morning blowjob 1 with fade
        pause
        grace.c "М-м~ М-м-м~"
        mc.c "И тебе доброе утро, Грейс."
        grace.c "Погоди~ М-м~ Ты такой твёрдый~"
        grace.c "А-а~ М-м~ Просто не удержалась~"
        image grace morning blowjob 2 = Movie(play="images/characters/grace/hscenes/morning/blowjob2.webm")
        show grace morning blowjob 2 with fadewhite
        pause
        grace.c "Хе-хе~ Такой большой~"
    return

# Sex scenes
label graceHandjob:
    image grace handjob start = Image("images/characters/grace/hscenes/handjob/start.webp")
    scene grace handjob start with fade
    pause
    image grace handjob part 1 = Image("images/characters/grace/hscenes/handjob/part1.webp")
    scene grace handjob part 1 with fade
    pause
    image grace handjob part 2 = Movie(play="images/characters/grace/hscenes/handjob/part2.webm")
    show grace handjob part 2 with fade
    pause
    image grace handjob part 3 = Movie(play="images/characters/grace/hscenes/handjob/part3.webm")
    show grace handjob part 3 with fade
    pause
    image grace handjob part 4 = Movie(play="images/characters/grace/hscenes/handjob/part4.webm")
    show grace handjob part 4 with fade
    pause
    image grace handjob end = Image("images/characters/grace/hscenes/handjob/end.webp")
    scene grace handjob end with fadewhite
    pause
    jump graceSexSelect

label graceBlowjob:
    image grace blowjob start 1 = Image("images/characters/grace/hscenes/blowjob/start1.webp")
    scene grace blowjob start 1 with fade
    pause
    image grace blowjob start 2 = Image("images/characters/grace/hscenes/blowjob/start2.webp")
    scene grace blowjob start 2 with fade
    pause
    image grace blowjob start 3 = Image("images/characters/grace/hscenes/blowjob/start3.webp")
    scene grace blowjob start 3 with fade
    pause
    image grace blowjob part 1 = Image("images/characters/grace/hscenes/blowjob/part1.webp")
    scene grace blowjob part 1 with fade
    pause
    image grace blowjob part 2 = Movie(play="images/characters/grace/hscenes/blowjob/part2.webm")
    show grace blowjob part 2 with fade
    pause
    image grace blowjob part 3 = Movie(play="images/characters/grace/hscenes/blowjob/part3.webm")
    show grace blowjob part 3 with fade
    pause
    image grace blowjob part 4 = Movie(play="images/characters/grace/hscenes/blowjob/part4.webm")
    show grace blowjob part 4 with fade
    pause
    image grace blowjob part 5 = Movie(play="images/characters/grace/hscenes/blowjob/part5.webm")
    show grace blowjob part 5 with fade
    pause
    image grace blowjob part 6 = Movie(play="images/characters/grace/hscenes/blowjob/part6.webm")
    show grace blowjob part 6 with fade
    pause
    image grace blowjob end = Image("images/characters/grace/hscenes/blowjob/end.webp")
    scene grace blowjob end with fadewhite
    pause
    jump graceSexSelect

label graceMissionary:
    image grace missionary start = Image("images/characters/grace/hscenes/missionary/start.webp")
    show grace missionary start with fade
    pause
    image grace missionary part 1 = Movie(play="images/characters/grace/hscenes/missionary/part1.webm")
    show grace missionary part 1 with fade
    pause
    image grace missionary part 2 = Movie(play="images/characters/grace/hscenes/missionary/part2.webm")
    show grace missionary part 2 with fade
    pause
    image grace missionary part 3 = Movie(play="images/characters/grace/hscenes/missionary/part3.webm")
    show grace missionary part 3 with fade
    pause
    image grace missionary part 4 = Movie(play="images/characters/grace/hscenes/missionary/part4.webm")
    show grace missionary part 4 with fade
    pause
    image grace missionary part 5 = Movie(play="images/characters/grace/hscenes/missionary/part5.webm")
    show grace missionary part 5 with fade
    pause
    image grace missionary finish = Image("images/characters/grace/hscenes/missionary/finish.webp")
    show grace missionary finish with fadewhite
    pause
    jump graceSexSelect

label graceDoggystyle:
    image grace doggy home part 1 = Movie(play="images/characters/grace/hscenes/doggy/homeVariant/part1.webm")
    show grace doggy home part 1  with fade
    pause
    image grace doggy home part 2 = Movie(play="images/characters/grace/hscenes/doggy/homeVariant/part2.webm")
    show grace doggy home part 2  with fade
    pause
    image grace doggy home part 3 = Movie(play="images/characters/grace/hscenes/doggy/homeVariant/part3.webm")
    show grace doggy home part 3  with fade
    pause
    image grace doggy home part 4 = Movie(play="images/characters/grace/hscenes/doggy/homeVariant/part4.webm")
    show grace doggy home part 4  with fade
    pause
    image grace doggy home part 5 = Movie(play="images/characters/grace/hscenes/doggy/homeVariant/part5.webm")
    show grace doggy home part 5  with fade
    pause
    image grace doggy home part 6 = Movie(play="images/characters/grace/hscenes/doggy/homeVariant/part6.webm")
    show grace doggy home part 6  with fade
    pause
    image grace doggy home end 1 = Image("images/characters/grace/hscenes/doggy/homeVariant/end1.webp")
    show grace doggy home end 1 with fadewhite
    pause
    image grace doggy home end 2 = Image("images/characters/grace/hscenes/doggy/homeVariant/end2.webp")
    show grace doggy home end 2 with fade
    pause
    jump graceSexSelect

label graceAnal:
    scene graceanalstart with fade
    pause
    image grace anal part 1 = Movie(play="images/characters/grace/hscenes/anal/part1.webm")
    show grace anal part 1  with fade
    pause
    image grace anal part 2 = Movie(play="images/characters/grace/hscenes/anal/part2.webm")
    show grace anal part 2  with fade
    pause
    image grace anal part 3 = Movie(play="images/characters/grace/hscenes/anal/part3.webm")
    show grace anal part 3  with fade
    pause
    scene graceanalend1 with fadewhite
    pause
    scene graceanalend2 with fade
    pause
    jump graceSexSelect

label graceCowgirl:
    image grace cowgirl 1 = Movie(play="images/characters/grace/hscenes/cowgirl/part1.webm")
    show grace cowgirl 1  with fade
    pause
    image grace cowgirl 2 = Movie(play="images/characters/grace/hscenes/cowgirl/part2.webm")
    show grace cowgirl 2  with fade
    pause
    scene gracecowgirlfinish with fadewhite
    pause
    jump graceSexSelect

label gracehomebathroomBlowjob:
    scene graceshowerapproach with fade
    pause
    image grace shower caressing = Movie(play="images/characters/grace/hscenes/shower/caressing.webm")
    show grace shower caressing  with fade
    pause
    image grace shower blowjob 1 = Movie(play="images/characters/grace/hscenes/shower/blowjob1.webm")
    show grace shower blowjob 1  with fade
    pause
    image grace shower blowjob 2 = Movie(play="images/characters/grace/hscenes/shower/blowjob2.webm")
    show grace shower blowjob 2  with fade
    pause
    scene graceshowerblowjobfinish with fadewhite
    pause
    return

# Events
default graceFirstMeetingEvent = Event('First meeting', 'graceFirstMeeting', [grace], 0, 0, [], location_shop, triggerDay = 1)
# known to mc
default graceLikeEvent1 = Event('Second meeting', 'graceLikeEvent1', [grace], 0, 0, [graceFirstMeetingEvent], location_shop)
default graceLikeEvent2 = Event('Accidental exposure', 'graceLikeEvent2', [grace], 10, 0, [graceLikeEvent1], location_park, ['Afternoon', 'Evening'])
# Dateable
default graceLikeEvent3 = Event('Must be joking', 'graceLikeEvent3', [grace], 20, 0, [graceLikeEvent2], location_town, ['Afternoon', 'Evening'])
# First Kiss
default graceLikeEvent4 = Event('Self image', 'graceLikeEvent4', [grace], 30, 10, [graceLikeEvent3], location_diner)
# Caught masturbating
default graceHEvent1 = Event('Caught', 'graceHEvent1', [grace], 40, 15, [graceLikeEvent4], location_town)
# Handjob
default graceHEvent2 = Event('Got it all wrong', 'graceHEvent2', [grace], 0, 0, [graceHEvent1], location_park, extraNotes = 'Wait a few days after \"Caught\"')
# Blowjob
default graceHEvent3 = Event('Veil lifted', 'graceHEvent3', [grace], 50, 20, [graceHEvent2], location_shop)
# Cunnilingus (cosplay)
default graceHEvent4 = Event('Fashion show', 'graceHEvent4', [grace], 60, 25, [graceHEvent3], location_town, ['Morning', 'Afternoon', 'Evening'])
# Lose virginity sleep over
default graceHEvent5 = Event('Next step', 'graceHEvent5', [grace], 70, 30, [graceHEvent4], location_home)
# Rough doggy at hers
default graceHEvent6 = Event('Home alone', 'graceHEvent6', [grace], 80, 35, [graceHEvent5], location_home)
# Anal
default graceHEvent7 = Event('The real deal', 'graceHEvent7', [grace], 90, 40, [graceHEvent6], location_home, ['Afternoon', 'Evening'])
# Abroad hotel beach pool vacation
default graceVacation = Event('Pilgrimage', 'graceVacation', [grace], 100, 45, [graceHEvent7], Null, extraNotes = 'Organise a vacation. Special option in interaction menu.', cost=2500, requiresInvite = True)
# Move in invite + event
default graceLikeEvent5 = Event('New pastures', 'graceLikeEvent5', [grace], 110, 50, [graceVacation], Null, extraNotes = 'Things are getting serious. Are we ready for the next step?\nSpecial option in interaction menu.', requiredItems = [item_car], requiresInvite = True)
# Shower blowjob
default graceHEvent8 = Event('Helping hand', 'graceHEvent8', [grace], 120, 55, [graceLikeEvent5], location_home_bathroom, mcInitiated = True)


label graceFirstMeeting(fromGallery):
    $ location_shop.showBackground()
    call playMusic(chillTheme) from _call_playMusic_60
    "Этот магазинчик очень удобный. Он рядом с баром, по пути домой и обратно, да и выбор для небольшой лавки вполне приличный."
    "Если во время смены чего-нибудь не хватает, сотрудники тоже могут сюда заглянуть."
    "Когда живёшь один, большой поход за продуктами редко имеет смысл, так что проще докупать понемногу по мере необходимости."
    "Я набираю несколько вещей и направляюсь к кассе."
    scene gracefirstmeetingi1 with fade
    pause
    "За прилавком стоит немного неловкая девушка — похоже, крольчиха. Она заметно ёрзает."
    "На вид примерно моего возраста, хотя с этими антро пока трудно определять возраст — я ещё привыкаю к их внешности."
    "Обычный спортивный костюм, нелеповатые очки, простые косички и здоровенные круги под глазами."
    "Я пытаюсь поймать её взгляд, подходя ближе, но она смотрит куда-то в сторону и выглядит смущённой."
    "Я уже собираюсь положить покупки у кассы, но бедняжка будто готова выпрыгнуть из собственной шкуры, если я подойду ещё ближе."
    "Рядом возится с чем-то другой сотрудник и наблюдает за происходящим."
    $ location_shop.showBackground()
    unknown "Эй! Новенькая! Покупатель!"
    show grace surprise
    grace_unknown "И-и-и!"
    "Мужчина резко окликает её, и бедная девушка испуганно переводит взгляд с коллеги на меня."
    show grace at twoPersonLeft with ease
    show man at twoPersonRight with dissolve
    grace_unknown "Э-э-э, я-я... М-м..."
    unknown "Давай живее, девушка, обслужи покупателя."
    show grace sad 
    grace_unknown "Э-э-э-э~"
    unknown "Прошу прощения, сэр. Она у нас недавно работает."
    mc.c "Ничего страшного."
    unknown "Возьми у него покупки и пробей."
    grace_unknown "А, д-да..."
    "Девушка неловко подбирает несколько вещей, которые я положил на прилавок, и принимается сканировать — каждый товар считывается не с первой попытки."
    hide man with dissolve
    show grace at center with ease
    "Убедившись, что девушка пробивает мои покупки, мужчина возвращается к своим делам."
    "Девушка щурится, пытаясь разобраться в цифрах на экране со своей стороны."
    "Наконец она заканчивает."
    show grace sad talk
    grace_unknown "А... С вас... 12 долларов 49 центов... с-сэр."
    show grace sad
    mc.c "Конечно."
    "Я достаю из бумажника несколько купюр. Девушка снова отводит взгляд и переминается с ноги на ногу."
    mc.c "И пакет, пожалуйста."
    show grace sad talk
    grace_unknown "О-ох... да..."
    "Мужчина слышит это со своего места в магазине."
    unknown "Я же говорил, девушка! Всегда предлагай покупателям пакет!"
    show grace surprise
    grace_unknown "А! Д-да, сэр! П-простите..."
    "Девушка с трудом достаёт пластиковый пакет и складывает туда покупки. Она и правда совсем новенькая, похоже, раньше никогда не работала."
    "Интересно, чем она занималась до этого?"
    mc.c "Эй, не переживай."
    show grace neutral
    "Я пытаюсь улыбнуться, чтобы успокоить её, но она лишь неловко отводит глаза."
    "Наконец она берёт деньги и тщательно отсчитывает сдачу, будто ужасно боится ошибиться."
    "Жестоко ли было расплачиваться наличными? Может, с картой ей было бы проще? Хотя тогда пришлось бы разбираться с компьютером."
    show grace neutral talk
    grace_unknown "В-вот ваша сдача... Сэр."
    show grace neutral
    mc.c "Большое спасибо."
    "Мужчина снова подаёт голос."
    unknown "И ещё раз прошу прощения за неё, сэр. Она только на этой неделе начала работать. Говорит, раньше нигде не работала, представляете? Нынешняя молодёжь..."
    "Последнее он произносит с усмешкой, будто ждёт, что я поддержу его подколки насчёт поколений."
    unknown "Да она вроде как затворница или что-то такое. Мать просто хочет выгнать её из дома! Ха!"
    show grace sad
    "Господи, ну и жестокость — кричать такое на весь магазин. Хорошо хоть, кроме нас, здесь, кажется, никого нет."
    "Девушка смотрит прямо в пол, убитая горем. Её ведь только что унизили на глазах у всех."
    "К счастью, мужчина уходит в подсобку с коробками."
    mc.c "Эй, не бери в голову. Я знаю, каково это. Помню свою первую работу в сфере обслуживания. Все через это проходили."
    show grace sad talk
    grace_unknown "Д-да... Простите."
    mc.c "Не извиняйся. Слушай, со временем станет легче, ладно? Просто держись."
    "Я показываю дурацкий палец вверх и натянуто улыбаюсь, отчаянно пытаясь её подбодрить."
    show grace neutral
    grace_unknown "Н-надеюсь... Спасибо..."
    mc.c "И ещё раз спасибо."
    scene black with fade
    "Я разворачиваюсь и выхожу из магазина."
    "Я часто сюда захожу. Интересно, увижу ли я её снова?"
    "Хотя, возможно, она здесь надолго не задержится."

    if(not fromGallery):
        $ grace.addLike(1)

    
    return {'location':location_town}


label graceLikeEvent1(fromGallery):
    $ location_shop.showBackground()
    "Сегодня ужасно жарко."
    "Хочу заглянуть в магазин и взять что-нибудь прохладное. В баре почти нет безалкогольных напитков — сколько можно пить обычную колу и тоник."
    "Я заглядываю в проход и замечаю знакомое лицо за прилавком. Она как раз заканчивает обслуживать другого покупателя."
    show grace neutral talk with dissolve
    call playMusic(funnyTheme) from _call_playMusic_61
    grace_unknown "С-спасибо, мэм. Хорошего дня..."
    hide grace with dissolve
    "Похоже, она понемногу привыкает к работе. Покупательница едва успевает отойти, а девушка уже вежливо кланяется ей вслед."
    "Но едва отвернувшись, она опускает плечи и уныло смотрит на прилавок."
    "Наверное, такие разговоры с покупателями отнимают у неё все силы. Понимаю — со временем к этому привыкаешь."
    "Я беру напиток из холодильника и подхожу к кассе. В магазине никого больше нет, и того сотрудника с прошлого раза тоже не видно."
    mc.c "Сегодня ворчун не работает?"
    show grace surprise with easeinbottom
    grace_unknown "И-и-и!"
    "Ой, я её напугал. Она меня не заметила."
    mc.c "Прости, прости! Не хотел тебя пугать."
    "Я стараюсь улыбкой разрядить обстановку и успокоить её."
    show grace sad talk
    grace_unknown "П-простите, сэр... Я должна была..."
    show grace sad
    mc.c "Это моя вина, не переживай."
    mc.c "Так что, старого ворчуна сегодня нет?"
    show grace tease talk
    grace_unknown "А... Он на перерыве... Хе-хе~"
    "Ух ты, она уже улыбнулась. Похоже, прекрасно понимает, о ком я."
    show grace neutral talk
    grace_unknown "Я-я, наверное, не должна ничего говорить... Вдруг услышит..."
    show grace neutral
    mc.c "Да ладно, он придурок. Прости, что в прошлый раз он так с тобой обошёлся."
    mc.c "С тех пор стало хоть немного легче?"
    show grace neutral talk
    grace_unknown "Д-да... Вроде... Спасибо."
    "Мне любопытно, что тот мужчина имел в виду в прошлый раз. Первая работа, затворница? Надеюсь, это не слишком болезненная тема."
    mc.c "Это у тебя первая работа?"
    show grace neutral
    grace_unknown "Да... Мама заставила..."
    mc.c "А чем ты занималась раньше?"
    grace_unknown "Н-ничем... После школы... Уже несколько лет..."
    mc.c "Эй, я не осуждаю. Как там говорят: работа ещё никого не убила, но зачем рисковать?"
    show grace tease talk
    grace_unknown "Хе-хе-хе~"
    "Неловко смеётся, но так мило — и улыбка у неё такая же милая."
    mc.c "Ладно, мне вот это, пожалуйста."
    "Я протягиваю ей напиток, который всё это время грелся у меня в руке."
    show grace smile talk
    grace_unknown "К-конечно."
    show grace smile
    "Похоже, она немного расслабилась. Покупатели бывают очень пугающими, а порой и жестокими без всякой причины."
    "Она пробивает покупку, и я расплачиваюсь."
    mc.c "Я часто сюда захожу. Меня зовут [mc.name]. А тебя?"
    show grace smile talk
    grace.c "А-а... Г-[grace.name]..."
    show grace smile
    mc.c "Приятно познакомиться. Я управляю баром в паре кварталов отсюда. Знаешь его?"
    show grace smile talk
    grace.c "Эм... Кажется, да..."
    grace.c "Некоторые сотрудники заходят туда после закрытия..."
    grace.c "Н-но я почти не пью... Простите..."
    show grace smile
    mc.c "Ничего страшного. Ладно, тогда ещё увидимся..."
    show grace surprise
    "Меня перебивает какой-то сигнал с телефона [grace.name]. Из динамика раздаётся приторно-сладкая мелодия."
    "Телефон лежит на прилавке экраном вверх, и на заставке появляется какая-то девушка из аниме."
    "К телефону прикреплена яркая подвеска в стиле волшебницы из аниме."
    grace.c "А! Чёрт... Я должна была его выключить..."
    "Она оглядывает магазин, будто проверяет, не услышал ли кто-нибудь из сотрудников."
    show grace sad talk
    grace.c "Если меня поймают... Они очень разозлятся."
    show grace sad
    mc.c "Не скажу ворчуну, секрет останется между нами."
    "Если подумать, мелодия кажется знакомой. Может, это из сериала на заставке её телефона."
    "Я не особо его знаю, название не помню, но вроде видел где-то."
    mc.c "Тебе нравится это аниме?"
    show grace surprise
    grace.c "А? Ты... Тоже любишь...?"
    mc.c "Немного, время от времени. Раньше, когда был помоложе, смотрел чаще."
    show grace smile talk
    grace.c "Д-да... Мне нравится... Я ещё в игры играю... И читаю..."
    mc.c "Здорово. В следующий раз расскажешь, что тебе больше всего нравится."
    show grace bashful 
    grace.c "Эм, ладно..."
    "В этот момент из подсобки выходит тот самый ворчливый коллега и поглядывает на кассу."
    "Лучше закончить разговор. Не хочу, чтобы он допрашивал её из-за чего-нибудь."
    mc.c "Большое спасибо, мисс!"
    show grace neutral talk
    grace.c "А, пожалуйста. С-эр..."
    scene black with fade
    "Она может оказаться интересной девушкой."
    "Надеюсь, мы ещё увидимся."

    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.knownToMC = True

    
    return {'location':location_home}

label graceLikeEvent2(fromGallery):
    $ location_park.showBackground()
    "В парке я замечаю знакомое лицо."
    "Это [grace.name]. Она сидит на скамейке, обмякнув и едва не засыпая; глаза уже слипаются."
    "Редко вижу её где-то кроме работы. Может, получится нормально с ней поговорить."
    show grace sad with dissolve
    call playMusic(sadTheme) from _call_playMusic_62
    "Она меня не заметила. Неудивительно — похоже, мыслями она где-то далеко."
    "Я всё время её пугаю, так что на этот раз попробую подойти осторожно."
    mc.c "[grace.name]...?"
    show grace surprise
    grace.c "А-а-а!"
    "Ну вот, опять не вышло."
    mc.c "Прости, не хотел тебя пугать. У меня это уже входит в привычку, да?"
    grace.c "А! Э-э, п-прости. Всё в порядке..."
    "Скорее я разбудил её после сна, чем просто застал врасплох."
    mc.c "Ты в порядке? Ты выглядела так, будто сейчас свалишься со скамейки."
    show grace sad
    grace.c "Д-да, всё хорошо... Просто немножко у-устала..."
    mc.c "Сегодня работала?"
    grace.c "Да... Утренняя смена... Пришлось встать в... *зевает* семь утра..."
    grace.c "Я шла д-домой... Дошла сюда и почувствовала, что сейчас упаду..."
    mc.c "Настолько всё плохо?"
    "За углом стоит автомат. Мог бы ей помочь."
    mc.c "Давай куплю тебе кофе или что-нибудь. Вон там автомат."
    show grace surprise
    grace.c "А? Ой, н-не нужно обо мне заботиться..."
    mc.c "Ничего страшного, я и себе собирался взять."
    grace.c "А..."
    hide grace with dissolve
    "Я беру пару банок и возвращаюсь."
    mc.c "Держи."
    show grace smile talk with dissolve
    mc.c "С-спасибо..."
    show grace smile
    "Она открывает банку и делает глоток. Мгновенно кофе её, конечно, не взбодрит, но хотя бы получится сделать что-то приятное."
    mc.c "За здоровье."
    "Я подношу свою банку, чтобы чокнуться."
    show grace bashful talk
    grace.c "З-за здоровье."
    "Я сажусь рядом и отпиваю кофе. Некоторое время мы молчим."
    pause
    "..."
    "Надеюсь, я не слишком навязываюсь. Похоже, ей очень трудно общаться с людьми."
    "Я пытаюсь придумать, о чём заговорить, но тут она сама произносит своим тихим, немного неловким голосом:"
    show grace neutral talk
    grace.c "М-можно спросить кое-что...?"
    show grace neutral 
    mc.c "Конечно."
    show grace neutral talk
    grace.c "Ты раньше говорил... Правда... Становится ли легче? Р-рано вставать... Каждый день выходить н-наружу..."
    grace.c "Я знала, что работа будет тяжёлой... Но всё это такое... бесконечное."
    show grace neutral
    mc.c "Ну, режим сна изменится, и к этому ты привыкнешь."
    mc.c "Но со временем это и правда выматывает. Иногда выгореть — совершенно нормально."
    show grace sad
    "Она заметно поникает."
    mc.c "Но справляться помогают люди, с которыми работаешь. Своего рода коллективное страдание, если так посмотреть."
    mc.c "Найди в этом что-нибудь смешное. Например, того мерзкого начальника у вас. Спорим, все остальные его тоже терпеть не могут."
    show grace neutral
    grace.c "Д-да..."
    mc.c "Пользуйся этим: вместе с коллегами жалуйтесь на начальство, иногда подшучивайте над ним за спиной — всё такое."
    mc.c "Мне это, по крайней мере, помогало пережить рабочие дни."
    show grace neutral talk
    grace.c "Меня за это не у-уволят? Кто-нибудь может донести..."
    show grace neutral
    mc.c "Большинство в той же лодке, что и ты. Им, наверное, тоже тяжело и всё это не нравится. А как у вас дела?"
    show grace neutral talk
    grace.c "Я не очень в-вписываюсь... Но... Они ничего..."
    show grace neutral
    mc.c "Попробуй продержаться. Прими всю эту безнадёгу. Со временем просто привыкнешь, как бы грустно это ни звучало."
    show grace neutral talk
    grace.c "Эм... Я п-постараюсь..."
    show grace neutral
    mc.c "Когда-нибудь этому парню воздастся."
    call playMusic(funnyTheme) from _call_playMusic_63
    show grace tease talk
    grace.c "Хе-хе-хе~ Ну... Кстати..."
    grace.c "На днях он крупно опозорился, когда приезжал региональный менеджер."
    grace.c "Кто-то сфотографировал, как тот отчитывал его в подсобке. Он там чуть ли не на коленях ползал."
    grace.c "Мне прислали фото. Д-дай покажу."
    show grace tease
    "[grace.name] достаёт телефон и начинает листать галерею."
    "Сидя рядом, я вижу её экран целиком. Не хочу подглядывать, но она и не пытается его прятать."
    "Несколько обычных пейзажей — наверное, местных. Пара снимков уличных животных."
    "Но на следующем фото вдруг..."
    call stopMusic from _call_stopMusic_10
    scene gracelikevent2selfie with fade
    pause 1.0
    grace.c "А-а-а!!{w=1.0}{nw}"
    $ location_park.showBackground()
    show grace surprise with dissolve
    "Вскрикнув, [grace.name] быстро выключает экран, переворачивает телефон и роняет его на пол."
    grace.c "Т-ты-ты... Т-ты в-в-видел...?"
    "Я не успел толком разглядеть, но это было похоже на селфи [grace.name] перед зеркалом. На ней был какой-то замысловатый наряд."
    "Подозрительно похожий то ли на костюм волшебницы, то ли на платье айдола."
    mc.c "Эм... Ну... Не особо..."
    show grace sad talk
    grace.c "Т-ты точно видел! Чёрт..."
    call playMusic(heartTheme) from _call_playMusic_64
    show grace sad
    "Тут есть два варианта: отрицать и, может, успокоить её или признаться, но попробовать поддержать разговор."
    "В прошлый раз в магазине она немного разговорилась, когда я узнал заставку на телефоне. Наверное, она отаку и стесняется об этом говорить."
    mc.c "Ну... Я не особо разглядел, но это был косплей? Я даже не понял, что это ты, пока ты не вскрикнула."
    grace.c "..."
    mc.c "Эй, всё нормально. Тут нечего стыдиться. Правда."
    show grace sad talk
    grace.c "Т-ты знаешь, что такое к-косплей...?"
    mc.c "Конечно. Я даже был на конвенте. Пару знакомых тоже этим занимались."
    mc.c "Не то чтобы я знал все их образы, но это же просто весело, верно? Никого не осуждаю — каждому своё."
    mc.c "На самом деле, это круто."
    show grace surprise
    grace.c "П-правда?"
    mc.c "Конечно. А почему нет?"
    show grace neutral talk
    grace.c "М-мне неловко... Большинство бы засмеялось..."
    show grace neutral
    mc.c "Я не большинство. Но понимаю, почему ты хочешь оставить это при себе. Со мной можешь не переживать."
    mc.c "Ты выкладываешь фото в сеть? Или ходишь на конвенты?"
    show grace surprise
    grace.c "Что!? О-ой, нет... Боже, н-не смогла бы..."
    show grace sad talk
    grace.c "Я п-просто... Для себя иногда... Это г-глупо, не стоило..."
    show grace sad
    mc.c "Это не глупо. Ты сама шьёшь костюмы? Или купила готовый?"
    show grace neutral talk
    grace.c "П-пытаюсь кое-что шить... А остальное приходится покупать."
    mc.c "А кого ты косплеила? Я толком не разглядел. Покажешь ещё раз?"
    show grace bashful talk
    grace.c "...Н-нет... Не могу... Она в п-платье и всё такое... Я в нём плохо в-выгляжу..."
    show grace bashful
    "Не стану настаивать. Она очень стеснительная, и похоже, я вторгся в её личное пространство."
    "Хотя хотелось бы взглянуть ещё раз... Она всегда ходит в этом спортивном костюме. Будто в ней скрывается совсем другая, подавленная сторона."
    mc.c "Ничего, настаивать не буду. Но знай: я считаю это крутым. Если у тебя будут ещё фото, хотел бы посмотреть. Может, узнаю персонажа."
    show grace bashful talk
    grace.c "М-м... Не знаю..."
    "Она поднимает телефон, с облегчением видит, что экран не разбился, и встаёт."
    show grace neutral talk
    grace.c "М-мне пора... Мама ждёт..."
    mc.c "Без проблем. Было приятно поговорить."
    show grace thinking
    grace.c "..."
    "Она собирается уходить, но оглядывается через плечо."
    show grace smile talk
    grace.c "И... э-э... Спасибо за кофе... И за совет..."
    show grace smile
    mc.c "Не за что, [grace.name]. Обращайся. Ещё увидимся, ладно?"
    show grace smile talk
    grace.c "Д-до встречи..."
    scene black with fade
    "Мы расходимся, неловко улыбнувшись и помахав друг другу."

    if(not fromGallery):
        $ grace.addLike(1)

    
    return {'location':location_park}

label graceLikeEvent3(fromGallery):
    $ location_town.showBackground()
    "По дороге через город я замечаю знакомое лицо."
    show grace thinking with dissolve
    call playMusic(chillTheme) from _call_playMusic_65
    "Впереди идёт [grace.name], как обычно ссутулившись."
    "Наверняка возвращается домой после изматывающей смены."
    "Хочется с ней пообщаться. Она интересная, хоть и держится в стороне."
    "Чтобы с ней сблизиться, придётся самому проявлять инициативу. Кажется, мы уже неплохо поладили."
    mc.c "[timeOfDay], [grace.name]."
    show grace surprise
    grace.c "М-м!?"
    "Ну конечно."
    show grace neutral talk
    grace.c "О-о, [mc.name]... Привет."
    show grace neutral
    mc.c "Как ты? Сегодня работала?"
    show grace neutral talk
    grace.c "Да... Неплохо. Кажется, понемногу привыкаю..."
    mc.c "Здорово. От «хреново» до «не так хреново», да?"
    show grace smile talk
    grace.c "Хе-х, да..."
    show grace neutral talk
    grace.c "Ты... Работаешь в баре... да? Т-ты туда сейчас?"
    mc.c "Не, я сегодня уже закончил. Проходил мимо, увидел тебя и решил поздороваться."
    grace.c "О-о, ясно."
    show grace neutral
    "..."
    "Проходит мгновение. [grace.name] отводит взгляд и теребит руки. Она пока не мастак поддерживать беседу, да и я для неё всё ещё почти незнакомец."
    "Придётся самому проявить инициативу."
    mc.c "Слушай, ещё не поздно. Может, ты... ну, не хочешь выпить кофе? Или перекусить где-нибудь?"
    call playMusic(funnyTheme) from _call_playMusic_66
    show grace neutral talk
    grace.c "..."
    mc.c "..."
    grace.c "..."
    "Она смотрит на меня с лёгким замешательством и любопытством."
    grace.c "...Зачем?"
    "Вот это вопрос. Если бы я не знал, решил бы, что она пытается перевернуть ситуацию. Теперь нервничаю уже я."
    mc.c "Ну... Э-э... Я хотел... провести время вместе? Узнать тебя получше?"
    grace.c "..."
    show grace neutral
    grace.c "...Зачем тебе это?"
    "Неожиданно прямой вопрос от [grace.name], но в голосе апатия."
    "Может, я ей совсем неинтересен. Или она не поняла, к чему я веду."
    mc.c "Ты показалась мне классной. И милой. Но ты не обязана соглашаться... Я просто решил спросить."
    show grace neutral talk
    grace.c "..."
    show grace surprise
    grace.c "П-п-п-погоди... Т-ты имеешь в виду... вроде как..."
    grace.c "Т-ты... П-приглашаешь м-меня на с-свидание!?"
    mc.c "Я... Да, пытаюсь."
    grace.c "Н-н-но..."
    show grace thinking
    grace.c "П-погоди..."
    show grace mad talk
    grace.c "Это Ноэль тебя надоумил, д-да?"
    show grace mad
    mc.c "А? Кто?"
    show grace mad talk
    grace.c "В-вечно меня д-дразнит на работе..."
    grace.c "{size=20}Зачем я только сказала, что у меня никогда не было парня...{/size}"
    show grace mad
    mc.c "Прости, я не знаю, кто это. И никто меня не подговаривал. Я сам хотел тебя пригласить."
    grace.c "..."
    "Она пристально смотрит мне в глаза сквозь очки."
    grace.c "..."
    show grace thinking
    grace.c "..."
    show grace neutral
    grace.c "Ты ведь просто шутишь..."
    mc.c "Нет."
    grace.c "..."
    show grace surprise
    grace.c "Я?.."
    mc.c "Да, ты. А почему нет? Если ты не против..."
    grace.c "П-постой!"
    call playMusic(heartTheme) from _call_playMusic_67
    show grace sad talk
    grace.c "Н-но ты же уже... видел меня... Я некрасивая..."
    grace.c "Я до сих пор живу с м-мамой... Я противный отаку... Едва заставляю себя выходить на работу в дурацкий магазин..."
    show grace sad
    mc.c "Да ты вовсе не некрасивая. О чём ты?"
    mc.c "И всё остальное меня не волнует... У нас ведь есть общие интересы, да?"
    mc.c "Ничего страшного, если мы как-нибудь сходим куда-нибудь и узнаем друг друга получше. Если ты не против."
    show grace sad talk
    grace.c "Ты... правда?.."
    show grace sad
    mc.c "Правда. Как мне это доказать?"
    show grace neutral talk
    grace.c "..."
    show grace bashful talk
    grace.c "Эм... Не сейчас... Н-но..."
    grace.c "Д-да... Как-нибудь..."
    show grace bashful
    mc.c "Отлично! Спасибо, [grace.name]. Тогда в следующий раз?"
    show grace surprise
    grace.c "П-ПОКА!"
    hide grace with dissolve
    "[grace.name] почти убегает по улице, словно я её спугнул."
    "Плохо она это восприняла. Низкая самооценка или неудачный прошлый опыт?"
    "И всё же... Вроде как она согласилась. Надеюсь, помогу ей немного раскрыться. Та её сторона, которую я уже увидел, мне нравится."

    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.addLove(1)
        $ grace.isDateable = True
        "Теперь можно приглашать [grace.name] на свидания."

    
    return {'location':location_home}

label graceLikeEvent4(fromGallery):
    scene diner with fade
    call playMusic(funnyTheme) from _call_playMusic_68
    "Мы с [grace.name] уже несколько раз куда-то выбирались."
    "Сначала она очень сомневалась и не верила каждому моему предложению; при первом приглашении чуть не убежала."
    "Но, кажется, она ко мне привыкла. Стала открываться, меньше замыкаться и радоваться нашим встречам."
    show grace smile talk with dissolve
    grace.c "...а потом она проходит сцену превращения, и боже, это так мило."
    grace.c "Даже анимация потрясающая — будто весь бюджет потратили на неё. Это же лучшая часть сериала..."
    show grace smile
    "Впрочем, мы скорее просто проводим время как друзья, а не ходим на свидания."
    "Мы болтаем о своих интересах и обо всём таком, но становится ясно, что она почти не ходила на свидания, если вообще ходила."
    "Мы уже виделись несколько раз, но пока почти никуда не продвинулись. Всё хорошо, но интересно, куда это приведёт. Похоже, чтобы сблизиться, мне придётся немного подтолкнуть события."
    show grace tease talk
    grace.c "...а, я говорила про костюм? Это немного изменённая версия прежнего дизайна. Куплю новые материалы и..."
    show grace tease
    "Иногда она начинает без умолку рассказывать о своих увлечениях: аниме, манге или видеоиграх."
    "Я часто теряюсь в подробностях, но знаний хватает, чтобы следить за её рассказом."
    "И всё же приятно. Когда ей комфортно, она совсем другая."
    mc.c "О, новый косплей? На этот раз обязательно покажешь."
    show grace sad talk
    grace.c "О-о... Точно, ты ведь уже видел один..."
    grace.c "Не думаю... Мне неловко."
    show grace sad talk
    mc.c "Не стану заставлять, но мне правда хотелось бы посмотреть."
    mc.c "То, что я успел увидеть, выглядело здорово. Кажется, теперь я знаю сериал, из которого этот образ — ты пару раз о нём рассказывала."
    show grace thinking
    grace.c "А-а... Ну, не такой уж он и хороший. Да и я в нём... только всё испорчу..."
    "Она всё время ругает свою внешность. Постоянно ходит в простом спортивном костюме, ничего не показывает."
    "Она такая худая — может, её это беспокоит?"
    mc.c "Почему ты так плохо о себе думаешь? Ты очень милая, и, уверен, в костюме будешь прекрасно выглядеть."
    call playMusic(sadTheme) from _call_playMusic_69
    show grace bashful talk
    grace.c "Н-нет... Я не..."
    "Сейчас, возможно, наступлю на мину, но рискну..."
    show grace bashful
    mc.c "Ещё как. Ты уже не раз себя при мне унижала. Что именно тебе в себе не нравится?"
    show grace sad
    grace.c "..."
    show grace sad talk
    grace.c "М-многое... Я очень худая... Ты и сам видишь."
    grace.c "У меня такое плохое зрение, что приходится носить эти дурацкие очки..."
    grace.c "Но главное..."
    show grace sad
    grace.c "..."
    "Она замолкает, словно боится признаться в чём-то. Что же такого страшного?"
    mc.c "[grace.name], что такое? Можешь мне рассказать."
    show grace sad talk
    grace.c "Это... М-мой мех."
    show grace sad
    "Честно говоря, я не замечал у [grace.name] ничего странного с мехом. Хотя видел только её лицо и руки."
    mc.c "Что с твоим мехом?"
    show grace sad talk
    grace.c "Он уродливый. Некрасивый окрас и пятна. У кроликов так не бывает."
    show grace sad
    mc.c "Отсюда всё выглядит нормально. А каким должен быть мех у кроликов?"
    show grace sad talk
    grace.c "Ну, например, симметричным. И цвет пятен обычно не так сильно отличается от основного..."
    grace.c "Или, если пятна яркие, переход между цветами мягкий, и рисунок симметричный..."
    show grace sad
    mc.c "А у тебя?.."
    show grace sad talk
    grace.c "У меня резкие пятна. Не красивый узор, а просто разводы повсюду."
    grace.c "Выглядит плохо, поэтому я всё закрываю. Потому всегда ношу одежду с длинными рукавами."
    show grace sad
    "Я и не представлял, что её это так мучает. У неё ужасные проблемы с самооценкой. Я даже не думал, что узоры меха могут быть больной темой для антро."
    "Как помочь ей перестать так страдать?"
    mc.c "[grace.name]... Мне жаль, что ты так себя чувствуешь. Но можно скажу честно?"
    show grace neutral talk
    grace.c "Д-да?.."
    show grace neutral
    "Я пытаюсь разрядить обстановку и с усмешкой говорю..."
    mc.c "Мне, если честно, плевать."
    show grace surprise
    grace.c "!"
    "Так... Это прозвучало хуже, чем я рассчитывал."
    mc.c "Ха-ха... Прости, не так хотел сказать..."
    mc.c "Я имею в виду... Даже если это правда, а я уверен, что нет, такое волнует разве что других кроликов — не то что остальных антро."
    show grace neutral talk
    mc.c "...А я человек. Для меня это вообще ничего не значит."
    mc.c "Ты знаешь, я раньше почти не общался с антро. У меня нет никаких представлений о том, как должны или не должны выглядеть разные виды."
    "Она смотрит на меня то ли недоверчиво, то ли скептически."
    mc.c "...Для меня ты просто крольчиха... Девушка... В общем, крольчиха."
    mc.c "И очень милая."
    grace.c "..."
    mc.c "..."
    "..."
    "Непонятно, как это воспримется. Её это утешит или прозвучит пренебрежительно?"
    show grace bashful
    grace.c "..."
    grace.c "Т-ты... правда так думаешь?"
    mc.c "Ты понимаешь культурные ожидания и нормы, связанные с человеческой кожей? Или, например, с формой человеческих ушей?"
    show grace neutral talk
    grace.c "Я... понимаю, к чему ты..."
    show grace neutral
    mc.c "Прости, если прозвучало пренебрежительно. Из-за этого у тебя раньше были проблемы?"
    show grace neutral talk
    grace.c "В школе... всё было плохо. Популярные кролики меня задирали..."
    grace.c "Потом всё покатилось под откос. Я всегда была такой тихой и робкой..."
    show grace neutral
    mc.c "Мне жаль, что тебе пришлось через это пройти, [grace.name]."
    mc.c "Но это уже в прошлом. Не позволяй детским издевательствам управлять твоей жизнью. Не хочу, чтобы ты мучилась из-за жестокости детей."
    show grace neutral talk
    grace.c "Я... знаю... Но... Это трудно..."
    grace.c "Гораздо проще просто... прятаться от всех."
    show grace neutral
    "До недавнего времени она почти не выходила из дома... Неужели причина вот в этом?"
    mc.c "Давай так: со мной не сдерживайся. Я хочу увидеть тебя настоящую."
    mc.c "Ты мне нравишься, и я с радостью посмотрю на то, что ты создаёшь. Когда будешь готова."
    mc.c "И вообще, я бы до смерти хотел увидеть тебя в юбке..."
    show grace tease
    grace.c "Хе-х~ Замолчи..."
    show grace smile talk
    grace.c "Л-ладно... Я тебе верю..."
    show grace bashful talk
    grace.c "Я покажу... К-как-нибудь..."
    show grace bashful
    "Это огромный шаг вперёд. Ей просто нужно немного поддержки."
    mc.c "Прости, что испортил настроение. Давай я заплачу — сегодня за мой счёт — и пойдём отсюда."
    show grace smile
    grace.c "М-м."
    scene black with fade
    "Мы уходим, и я провожаю её часть пути. Она всегда настаивает, чтобы я не доводил её до самого дома."
    "Говорит, не хочет, чтобы мама увидела её с парнем. В этом есть что-то милое."
    $ location_town.showBackground()
    call playMusic(heartTheme) from _call_playMusic_70
    show grace smile talk with dissolve
    grace.c "С-спасибо за сегодня, [mc.name]. В последнее время мне так весело."
    show grace smile
    mc.c "Мне тоже очень нравится. Давай скоро повторим? В следующий раз место можешь выбрать ты."
    grace.c "Угу."
    "Я на мгновение задерживаю взгляд на её лице. Она не отворачивается и не уходит сразу."
    "Может, я всё надумываю, но кажется, с её плеч будто свалился груз."
    grace.c "..."
    mc.c "..."
    "Никто из нас не двигается, оба ждём, кто первым уйдёт."
    "Похоже, момент подходящий."
    "Я делаю небольшой шаг вперёд и беру её за руку."
    show grace neutral talk
    "Она широко раскрывает глаза, но не отводит взгляд и не отстраняется. Я медленно наклоняюсь к ней, следя, не передумала ли она."
    hide grace with Dissolve(1)
    show grace kiss with Dissolve(1)
    pause
    "Нахмурившись, мы соприкасаемся губами. Короткий, но чуть затянувшийся поцелуй."
    hide grace with dissolve
    show grace bashful with dissolve
    grace.c "Я... Э-э..."
    "Она заливается румянцем и беспокойно переводит взгляд. На сегодня достаточно."
    mc.c "До скорого, [grace.name]."
    show grace smile talk
    grace.c "А... П-пока!"
    hide grace with dissolve
    "Она резко разворачивается и быстро уходит, вся напряжённая."
    "Сегодня для неё всё было слишком эмоционально. Но, кажется, отношения развиваются в правильном направлении."

    if(not fromGallery):
        $ grace.addLove(1)

    return {'location':location_home}

label graceHEvent1(fromGallery):
    $ location_town.showBackground()
    "У нас с [grace.name] всё складывается хорошо."
    "После первого поцелуя мы, кажется, стали ближе. Она чувствует себя свободнее, и это заметно по тому, как мы сближаемся."
    "Хотя совсем немного. Она всё ещё неловко себя чувствует, мы пока только иногда держимся за руки и целуемся."
    "Мы ещё не бывали друг у друга дома. Я несколько раз предлагал, но она всегда уклонялась."
    "Но кое-что изменилось: пару раз она позволила проводить её прямо до дома и больше не пыталась скрывать меня от семьи."
    "Либо она рассказала маме, либо мама сама как-то узнала. В любом случае живёт она совсем недалеко."
    scene suburbs with fade
    call playMusic(funnyTheme) from _call_playMusic_71
    "Сегодня утром я ей написал, но ответа не получил. Я неподалёку... Так уж плохо будет заглянуть к ней?"
    "Рискуя навлечь на себя её гнев, я всё-таки хочу её увидеть. Лучше просить прощения, чем разрешения. Вот и её дом."
    "Я уже собираюсь позвонить в дверь, но она сама распахивается."
    show rabbitwoman with dissolve
    unknown "Ой, как вы меня напугали. Чем могу помочь?"
    "Из дома выходит крольчиха и поправляет сумку на плече, будто собралась куда-то идти."
    "Как обычно, возраст антро определить трудно, но она выглядит зрелой, ухоженной и элегантно одета."
    "Наверное, это мама [grace.name]. Она немного о ней рассказывала — кто же ещё?"
    mc.c "О-ой, э-э, простите, мэм, я как раз собирался позвонить. [grace.name] дома?"
    "Женщина на мгновение подозрительно оглядывает меня, потом узнаёт и расплывается в доброй улыбке."
    unknown "О-о-о~ Так вы, должно быть, [mc.name]! Тут нечасто встретишь людей. Конечно, надо было сразу догадаться."
    mc.c "Вы обо мне знаете?"
    unknown "Милый, [grace.name] в последнее время только о тебе и говорит. Она от тебя без ума."
    unknown "То [mc.name], это [mc.name] — ты бы слышал, как она тебя обсуждает! Совсем на неё не похоже, обычно она такая молчаливая."
    mc.c "Рад это слышать. Не знал, упоминала ли она меня."
    unknown "Однажды я видела вас двоих из окна, и ей пришлось всё рассказать. Правда, тебя толком не разглядела."
    unknown "Какой красавец! Ну надо же, [grace.name], молодец!"
    "Она подмигивает мне с озорной ухмылкой. Это она со мной заигрывает? Может, поэтому [grace.name] так долго не хотела знакомить меня с мамой."
    unknown "Она тебя ждёт?"
    mc.c "Э-э, нет. Я написал ей утром, но она, похоже, ещё не прочитала. Я был неподалёку, вот и..."
    unknown "Ну что ж, ничего страшного. Она дома, наверху, у себя в комнате. Спала, но я вроде слышала, как недавно она зашевелилась."
    unknown "Зная эту девочку, она, скорее всего, просто валяется без дела."
    unknown "Я как раз ухожу, так что проходи! Она наверняка обрадуется. Наверху, вторая дверь слева."
    scene gracehomehall with fade
    "Женщина поправляет серьги и провожает меня внутрь, сама выходя из дома."
    unknown "Мне пора! Хорошо вам провести время. Пусть она приготовит тебе что-нибудь, холодильник полный!"
    mc.c "О-о, э-э... Спасибо, мэм."
    unknown "Пока-пока!"
    "Дверь захлопывается, а я остаюсь в коридоре чужого дома."
    "А здесь довольно уютно. Чисто, прибрано, светло и тепло."
    "Но неловко просто стоять в чужом доме, когда никто из домашних не знает, что ты здесь."
    "Пойду поищу [grace.name]."
    "..."
    "Кажется, вот её комната? Я подхожу к закрытой двери, хотя меня сюда никто не приглашал. Это нормально?"
    call stopMusic from _call_stopMusic_11
    "*Тук-тук*"
    "Я негромко стучу пару раз."
    "..."
    "Тишина. Но в щели под дверью виден слабый свет. Там включена лампа?"
    "*Тук-тук*"
    "На этот раз чуть громче."
    "..."
    "Если совсем прислушаться, слышно какое-то шуршание, но шагов и ответа нет."
    "Она опять уснула? Или что-то смотрит в наушниках?"
    "Нерешительно я чуть приоткрываю дверь..."
    scene black with fade
    "Первым делом замечаю темноту. Свет не включён, лишь дневное сияние пробивается сквозь закрытые шторы."
    "А потом... тяжёлый воздух. Затхлость комнаты, которую давно не проветривали, смешивается с... женским запахом."
    "Когда глаза привыкают, на кровати проступает силуэт..."
    image grace masturbation part 1 = Movie(play="images/characters/grace/hscenes/masturbation/part1.webm")
    show grace masturbation part 1 with fade
    pause
    call playMusic(sexyTheme) from _call_playMusic_72
    grace.c "Ahh... Mmmhh..."
    "Это... [grace.name]."
    "Совершенно ясно, чем она занимается. Она мастурбирует."
    "Лежит на спине и смотрит в телефон. Звука не слышно, но понятно, что там."
    grace.c "Ohhh~ Mmmmmm~"
    "Она тихонько, робко постанывает, словно пытается сдержать удовольствие. Наверное, думала, что мама ещё дома."
    "Она и правда делает это днём, когда дома не одна?"
    "Несколько секунд я ошарашенно застываю, выглядывая из-за двери."
    "Я едва знаю эту девушку, а она лежит с голым низом, водит фаллоимитатором туда-сюда и даже не подозревает, что я здесь."
    "Понимаю, что веду себя как извращенец, но чёрт, это чертовски горячо."
    image grace masturbation part 2 = Movie(play="images/characters/grace/hscenes/masturbation/part2.webm")
    show grace masturbation part 2 with fade
    pause
    grace.c "Ох, чёрт~ М-м~"
    "Она полностью поглощена происходящим, ей ни до чего нет дела."
    "С обнажённой нижней половиной тела видно, какая она худенькая. Но ноги... Обманчиво изящные."
    "В темноте не разглядеть как следует, но я замечаю её пятна. Это о них она говорила?"
    "Пусть они и немного неровные, стыдиться тут нечего. Да и сейчас она выглядит чертовски сексуально."
    grace.c "Ahhh~ Ahhhh~ Haaahh~"
    "Мы ещё не были близки... Она сдерживалась? Нервничала? Я пытался начать, но она отстранялась."
    image grace masturbation part 3 = Movie(play="images/characters/grace/hscenes/masturbation/part3.webm")
    show grace masturbation part 3 with fade
    pause
    "В доме стоит тишина, но через открытую дверь я слышу каждый звук."
    "Похотливый голос, тихий шелест ткани на кровати, влажные звуки фаллоимитатора."
    "Я никогда не подглядывал за людьми, но член уже встал, и я не могу отвести взгляд."
    "Мне нельзя здесь оставаться, но... Я не могу перестать смотреть. Как это прекратить? Закрыть дверь? Вдруг она услышит?"
    "Но прежде чем я успеваю что-то сделать..."
    image grace masturbation end = Image("images/characters/grace/hscenes/masturbation/end.webp")
    scene grace masturbation end with fade
    pause
    "...Она косится на дверь и замечает меня."
    grace.c "...!"
    grace.c "А-А-А! ЧЁРТ!!"
    grace.c "В-В-ВОН ОТСЮДА!"
    scene gracehomehall with fade
    "Я поспешно захлопываю дверь."
    call playMusic(sadTheme) from _call_playMusic_73
    "Боже мой. Я только что застал её за этим..."
    "О чём я только думал?! Я всё разглядел. Просто стоял и пялился..."
    "Она будет в ярости... Сейчас у неё в голове, наверное, творится что угодно."
    "Из-за двери доносятся грохот и шорох одежды."
    "..."
    grace.c "{size=20}[mc.name]...? Т-ты ещё там..?{/size}"
    "Из-за двери доносится тихий дрожащий голос."
    mc.c "Э-э... Да..."
    grace.c "{size=20}О-о боже...{/size}"
    grace.c "{size=20}П-просто... зайди...{/size}"
    "Удивившись, что она не прогнала меня, я нерешительно поворачиваю ручку двери."
    scene gracebedroom with fade
    show grace sad with dissolve
    "[grace.name] уже одета. В комнате включена единственная лампа, чуть рассеивая темноту."
    show grace sad talk
    grace.c "Ч-что ты здесь д-делаешь...?"
    show grace sad
    mc.c "Чёрт, [grace.name], мне так жаль."
    mc.c "Я написал тебе, но ты не ответила. Я проходил мимо и решил зайти, а твоя мама открыла дверь..."
    mc.c "...Она впустила меня, сама куда-то умчалась и сказала найти тебя. Я пару раз постучал, ты не ответила, но я слышал, что ты дома, и..."
    mc.c "Я... открыл дверь..."
    show grace sad talk
    grace.c "Д-давно... ты... здесь?.."
    show grace sad
    "Честность сейчас ни к чему. Лучше никому не станет. Если хочу выбраться отсюда целым, придётся немного приукрасить правду."
    mc.c "В-всего секунду! Я открыл дверь как раз, когда ты обернулась! Я ничего не увидел... Я..."
    "Будто она в это поверит."
    grace.c "..."
    "Боже, она уставилась в пол. Её почти трясёт."
    mc.c "Прости... Я могу уйти..."
    show grace sad talk
    grace.c "П-прости, что тебе пришлось это увидеть..."
    grace.c "Наверное, ты считаешь меня такой мерзкой..."
    show grace sad
    mc.c "Ч-что? Нет! А? Я даже не..."
    "Что мне вообще сказать? Понятия не имею. Явно никого не обманешь."
    "Почему ОНА извиняется ПЕРЕДО МНОЙ? Ей стыдно? Будто она сделала что-то плохое?"
    "Что плохого в том, что девушка мастурбирует? Она считает меня каким-то ханжой?"
    mc.c "I..."
    show grace sad talk
    grace.c "Т-тебе не обязательно оставаться... Я пойму..."
    mc.c "З-зачем мне уходить? Если хочешь, я могу, но... Меня это не смущает..."
    show grace mad talk
    grace.c "Т-тебя не смущает, что я п-полная неудачница? У-уродливая, жалкая чокнутая?!"
    grace.c "Грязная затворница, которая д-дрочит под хентай?! А?! Кому вообще хочется такое видеть!"
    grace.c "И использую все эти с-секс-игрушки..."
    grace.c "По н-несколько раз за д-день. К-каждый день?!"
    grace.c "Я весь д-день только об этом и думаю... Одержима!"
    grace.c "Я никогда н-ни с кем не была... Ничего, чёрт возьми, не умею..."
    grace.c "Постоянно думаю обо всём этом, но н-не могу нормально себя вести среди обычных людей..."
    grace.c "Я п-посмешище..."
    show grace sad talk
    grace.c "С-смотреть... Ч-читать... Рисовать..."
    grace.c "Как полная чёртова н-неудачница..."
    grace.c "Не надо притворяться... Я знаю, кто я... Что я такое..."
    grace.c "Кому вообще захочется быть рядом с такой..."
    show grace sad
    "..."
    "Господи... Её прорвало. Никогда не видел её такой."
    "Наверное, это называется... Полностью подавленная сексуальность?"
    "Я замечал, какая она неопытная. Видимо, рано или поздно это должно было вырваться наружу."
    mc.c "[grace.name]... Я не..."
    show grace mad talk
    grace.c "П-просто у-уходи... Пожалуйста..."
    "У неё на глазах выступают слёзы."
    grace.c "Уходи..."
    show grace mad
    "Не хочу злить её ещё сильнее, пока она такая уязвимая. Мне больно оставлять её в таком состоянии, но..."
    "Наверное, так будет лучше. Но оставить всё как есть я не могу..."
    mc.c "Прости, [grace.name]."
    scene black with fade
    "Я ухожу, и [grace.name] закрывает за мной дверь."
    scene gracehomehall with fade
    "Лучше просто уйти."
    scene suburbs with fade
    "Я дам ей немного времени."
    
    if(not fromGallery):
        $ grace.hidden = True
        $ grace.hiddenDays = 3
        python:
            if(len(grace.scheduledDates) > 0):
                mc.scheduledDates.remove(grace.scheduledDates[0])
                grace.scheduledDates = []

    return {'location':location_home}

label graceHEvent2(fromGallery):
    $ location_park.showBackground()
    call playMusic(sadTheme) from _call_playMusic_74
    "Пару дней ушло на то, чтобы [grace.name] наконец ответила. До этого она игнорировала все мои попытки связаться."
    "После того, как мы расстались в прошлый раз, не понимаю, злится ли она на меня, сердится на себя, стыдится или что-то ещё."
    "Она долго не отвечала, а потом пару раз коротко отмахнулась, чтобы я оставил её в покое."
    "После того, как её прорвало... Не хочу, чтобы на этом закончились наши отношения."
    "К счастью, она согласилась встретиться и поговорить. Она очень нервничала, но мне пришлось настоять. Перепиской тут ничего не решить."
    "Я прихожу первым и сажусь на скамейку. Она скоро должна быть."
    "..."
    show grace neutral with dissolve
    mc.c "Привет, [grace.name]. Спасибо, что пришла."
    grace.c "П-привет..."
    "Я предлагаю ей сесть рядом, и она нерешительно соглашается."
    mc.c "Я скучал по нашим разговорам. Спасибо, что ответила."
    grace.c "..."
    mc.c "Для начала хочу от всего сердца извиниться. Я не хотел вторгаться в твою личную жизнь, но всё равно поступил неправильно. Мне очень жаль."
    show grace sad
    grace.c "..."
    show grace sad
    grace.c "Это... не твоя вина."
    mc.c "Нет, моя. Я мог просто уйти."
    show grace sad talk
    grace.c "Я не ждала, что ты придёшь. Твои сообщения увидела только потом... Ты хотел как лучше..."
    grace.c "Прости, что всё испортила. Я так злюсь на себя за то, что разрушила... нас..."
    show grace sad
    mc.c "Тебе не за что извиняться, [grace.name]. Правда. Это целиком моя вина."
    mc.c "Но что ты имеешь в виду, говоря «испортила»? Не понимаю."
    show grace sad talk
    grace.c "Теперь ты меня увидел. Настоящую меня. Грязную, уродливую, жалкую."
    grace.c "П-парни никогда не обращали на меня внимания... По крайней мере, это ты и так знаешь."
    grace.c "Всю жизнь я... была р-разочарована."
    grace.c "Я превратилась в жалкую затворницу, погрязшую в разврате, но ты..."
    grace.c "Я не понимаю, почему ты был со мной таким добрым и терпел, когда я вела себя так странно."
    grace.c "Но теперь ты увидел худшую сторону меня. Наверняка больше не захочешь иметь со мной ничего общего..."
    show grace sad
    mc.c "Но я ведь сейчас здесь, верно?"
    grace.c "..."
    "Почему она раньше мне ничего не рассказывала? Хороший вопрос. Если я что-то и понял про [grace.name], так это то, что ей просто нужен кто-то на её стороне."
    "Она стыдится отсутствия опыта? Если подумать, всё указывает на то, что она девственница и никогда не была с мужчинами."
    "И ей этого стыдно? Она ласкает себя, как и все остальные. Почему-то она решила, что это неправильно или что мне это не понравится."
    mc.c "[grace.name]... Почему ты мне ничего не рассказывала?"
    show grace sad talk
    grace.c "А?.."
    show grace sad
    mc.c "Не понимаю, почему тебе так неловко. С чего бы мне тебя за это осуждать?"
    show grace neutral
    grace.c "Не знаю... Девушки ведь не должны быть такими..."
    call stopMusic from _call_stopMusic_12
    mc.c "Ты вообще понимаешь... как же чертовски здорово это слышать?"
    show grace neutral talk
    grace.c "...!"
    grace.c "Ч-что ты такое говоришь...?"
    mc.c "То есть ты исследуешь свою сексуальность? Ты не ханжа?"
    mc.c "Да брось, я мужчина. Ты же знаешь, что говорят о мужской мастурбации."
    mc.c "Не знаю, что ещё сказать. Ты просто всё совсем неправильно поняла."
    call playMusic(heartTheme) from _call_playMusic_75
    show grace neutral talk
    grace.c "Н-но... Ты же не..."
    show grace thinking
    grace.c "Я имею в виду... Это не всегда что-то обычное. Например..."
    grace.c "Всякие ф-фетиши... х-хентай... Странные вещи..."
    mc.c "По-моему, звучит здорово. Как я уже сказал, просто делись этим со мной!"
    show grace surprise
    mc.c "Ты мне нравишься такой, какая ты есть, а не какой-то фальшивой маской. Я хочу узнать тебя целиком. Разве я этого не показывал?"
    grace.c "..."
    mc.c "Что тут такого удивительного? Мы встречаемся, и ты мне нравишься!"
    grace.c "..."
    grace.c "Я-я-я не знаю... Просто..."
    show grace neutral talk
    grace.c "Ни о-один мужчина никогда н-не хотел... быть со мной..."
    mc.c "Как ты думаешь, чем я всё это время занимался?"
    show grace neutral
    grace.c "..."
    show grace bashful talk
    grace.c "П-правда?.."
    show grace bashful
    mc.c "Конечно! На все сто процентов! Не до конца понимаю, что у тебя в голове и как мы до этого дошли, но хочу разобраться!"
    mc.c "Но сначала пойми: ничто из того, что ты делала или что я видел, не оттолкнуло меня. Наоборот..."
    grace.c "..."
    "Она какое-то время сидит, отводя взгляд и пытаясь всё осмыслить."
    "И правда, я не совсем понимаю, что у неё в голове и почему она так себя накрутила."
    "Будто она сама саботирует себя и наши отношения, потому что боится всего этого."
    call stopMusic from _call_stopMusic_13
    show grace mad talk
    grace.c "Н-ну! Е-если ты правда так думаешь, докажи!"
    show grace mad
    mc.c "Я на всё готов, [grace.name]. Правда."
    grace.c "..."
    call playMusic(funnyTheme) from _call_playMusic_76
    show grace mad talk
    grace.c "Т-тогда... П-покажи..."
    grace.c "ПОКАЖИ МНЕ СВОЙ ЧЛЕН!"
    show grace mad
    "..."
    "Она... выпалила это довольно громко. Наверное, громче, чем собиралась."
    "К счастью, быстрый взгляд по сторонам показывает, что в парке мы одни и никто нас не слышал."
    grace.c "..."
    "[grace.name] вызывающе смотрит мне прямо в глаза, явно ожидая ответа."
    mc.c "Э-э, [grace.name]... Мы же на людях..."
    show grace mad talk
    grace.c "Н-не здесь, идиот! Отведи меня к себе!"
    grace.c "Если хочешь м-меня поддержать, д-дай мне посмотреть!"
    show grace mad
    "Вот это... приглашение."
    "Странное, но всё же приглашение. Раньше я никак не мог привести её к себе, а теперь она сама предлагает — и в такой необычной форме."
    "Что я за мужчина, если откажусь?"
    "Я встаю и беру её за руку."
    show grace surprise
    grace.c "Eep!"
    mc.c "Как пожелаешь."
    grace.c "...!"
    scene black with fade
    "Мы молча идём ко мне домой, держась за руки."
    "В другой ситуации это было бы очень романтично, но... Она не может вымолвить ни слова и всю дорогу смотрит в пол."
    $ location_home.showBackground()
    mc.c "Вот, это мой дом."
    "[grace.name] тревожно оглядывается и, кажется, принюхивается."
    show grace bashful talk with dissolve
    grace.c "П-погоди... М-может, это не лучшая идея..."
    grace.c "П-прости! Я опять говорю странные вещи! Не слушай меня..."
    grace.c "Я-я просто уйду..."
    show grace bashful
    "Если позволю, она опять сбежит, как всегда."
    "Она совсем не умеет за себя постоять. Ей нужен кто-то, кто не даст ей разрушить всё самой. Смогу ли я стать таким человеком?"
    mc.c "Нет... Ты сама сказала, что тебе это поможет. Ты этого хочешь?"
    show grace bashful talk
    grace.c "Я... Н-но..."
    show grace bashful
    "Вопреки здравому смыслу и риску показаться слишком настойчивым или просто мерзким, я начинаю расстёгивать ремень..."
    mc.c "Я тебя уже видел, теперь и ты меня увидишь. Справедливо?"
    show grace mad talk
    grace.c "Д-да! Так б-будет честно..."
    show grace mad
    "[grace.name] смотрит мне между ног, пока я расстёгиваю ремень и спускаю штаны."
    show grace neutral talk
    "Она чуть шире раскрывает глаза: я остаюсь в одних трусах, а член уже выпирает — он возбуждён с тех пор, как мы шли домой."
    "Мы можем остановиться, если она этого захочет. Но она не отводит взгляд и даже чуть придвигается."
    "Я сажусь на кровать и подзываю её к себе."
    call playMusic(sexyTheme) from _call_playMusic_77
    image grace handjob start = Image("images/characters/grace/hscenes/handjob/start.webp")
    scene grace handjob start with fade
    pause
    "Сохраняя приличную дистанцию, [grace.name] пристально разглядывает мой стояк."
    "Я слегка откидываюсь и даю ему выпрямиться; он немного покачивается."
    grace.c "{size=20}О-о боже...{/size}"
    "Она не может отвести взгляд; рот приоткрыт от удивления."
    "Она молча стоит передо мной. Немного неловко. Всё-таки это для неё."
    mc.c "Подойди, рассмотри. Мне нечего стесняться."
    "Я подзываю её. [grace.name] нерешительно подходит и опускается на колени, чтобы получше рассмотреть."
    image grace handjob part 1 = Image("images/characters/grace/hscenes/handjob/part1.webp")
    scene grace handjob part 1 with fade
    pause
    "Она уже в нескольких сантиметрах от моего лица. Её глаза расширяются, пока она изучает член сверху вниз."
    grace.c "П-почему он... т-такой большой?.."
    mc.c "Почему? Наверное, я так рад тебя видеть."
    grace.c "Н-не это... я имела в в-виду..."
    "Она запинается и сглатывает, будто заворожённая."
    "Честно говоря, мне хотелось бы, чтобы она сняла верх. Но из-за её комплексов по поводу внешности сейчас настаивать не буду."
    mc.c "Он твой, [grace.name]. Можешь потрогать, если хочешь."
    grace.c "П-потрогать?.."
    mc.c "Разве тебе не хочется?"
    grace.c "Хочется..."
    "На секунду она смотрит мне в глаза, словно проверяя, правда ли я разрешаю, и медленно поднимает руку."
    image grace handjob part 2 = Movie(play="images/characters/grace/hscenes/handjob/part2.webm")
    show grace handjob part 2 with fade
    pause
    "Она нежно касается кончиками пальцев и осторожно гладит по бокам."
    "Она чуть наклоняется ближе и пару раз принюхивается."
    grace.c "У-ух ты..."
    mc.c "Не такой, как ты представляла?.."
    grace.c "Он... твёрдый... и тёплый..."
    "Она всё так же нежно гладит его вверх-вниз, скорее изучая, чем пытаясь доставить удовольствие."
    "Возможно, её придётся немного подбодрить, но явно этого она и хочет."
    "Теперь она немного расслабилась — думаю, шутку тоже поймёт."
    mc.c "У тебя есть игрушка такого размера?"
    grace.c "Э-э... Ну... О-одна..."
    mc.c "Думаешь, тогда справишься?"
    grace.c "Э-э... Хм?.."
    "Не буду её дразнить. Пусть просто наслаждается."
    mc.c "Попробуй обхватить покрепче. Возьми его всей ладонью."
    grace.c "Л-ладно..."
    image grace handjob part 3 = Movie(play="images/characters/grace/hscenes/handjob/part3.webm")
    show grace handjob part 3 with fade
    pause
    "После моего приглашения она начинает двигать рукой увереннее. Всё ещё нежно, но уже по-настоящему."
    "Она прищуривается, будто опьянённая происходящим."
    "Мне тоже очень приятно."
    mc.c "Вот так, [grace.name]. Продолжай."
    grace.c "П-правда?"
    "Она иногда поглядывает на меня, проверяя реакцию. Я могу лишь показать, насколько мне хорошо."
    "В её взгляде то и дело мелькает похотливая улыбка."
    mc.c "Да... Твоя рука такая приятная."
    grace.c "Даже если это я?.."
    mc.c "Особенно потому, что это ты."
    "Она краснеет и на миг отводит взгляд. Похоже, начинает втягиваться."
    "Не дожидаясь подсказки, она устраивается удобнее и ускоряется."
    image grace handjob part 4 = Movie(play="images/characters/grace/hscenes/handjob/part4.webm")
    show grace handjob part 4 with fade
    pause
    mc.c "Ох, чёрт..."
    "Честно говоря, долго я так не продержусь, но хочу, чтобы она сама делала то, чего ей хочется."
    "От усилия её дыхание становится чаще."
    grace.c "*Haah* *Haah*"
    "Её ладонь скользит по члену, собирая предэякулят, который уже выступил."
    "Её маленькие лапки ласкают и щекочут меня, а пальцы покрыты тонким мехом..."
    grace.c "Чувствую... Он напрягается?"
    mc.c "Да, я скоро кончу..."
    "Она могла бы остановиться, если хотела продолжить иначе, но просто не прекращает."
    mc.c "Я могу взять салфе..."
    grace.c "НЕТ!"
    "Она смотрит на меня, готовая принять всё."
    mc.c "Я сейчас!"
    "[grace.name] придвигает лицо к головке и не отрывает от неё взгляда."
    image grace handjob end = Image("images/characters/grace/hscenes/handjob/end.webp")
    scene grace handjob end with fadewhite
    pause
    "Меня накрывает оргазм, я кончаю ей на лицо и очки."
    "Она вздрагивает, но крепко держит и помогает мне кончить до конца."
    grace.c "О-ох~ *ха-а* Чёрт~"
    "Сперма стекает по её лицу. Она ошеломлённо стоит на коленях, разглядывая и вдыхая запах."
    mc.c "Чёрт, это было потрясающе."
    grace.c "О-ох... Ничего себе..."
    "Она несколько мгновений сидит неподвижно, но когда я начинаю терять эрекцию, а сперма стекает с её лица, уходит умыться."
    $ location_home.showBackground()
    "[grace.name] возвращается, нерешительно выглядывая из-за двери, пока я одеваюсь."
    show grace bashful with dissolve
    grace.c "..."
    mc.c "Это было потрясающе, [grace.name]. Правда. Спасибо."
    show grace bashful talk
    grace.c "Э-э... И-тебе спасибо..."
    show grace bashful
    call playMusic(funnyTheme) from _call_playMusic_78
    "Не каждый день благодаришь за то, что тебе подрочили."
    mc.c "Теперь мы квиты, да?"
    "Она замечает, что я шучу."
    show grace smile talk
    grace.c "Хе-хе..."
    show grace smile
    "Похоже, она расслабилась. Я притягиваю её к себе."
    hide grace with dissolve
    show grace hug with dissolve
    pause
    mc.c "Мы снова в порядке?"
    grace.c "Д-да... П-прости, что так странно себя вела."
    mc.c "Не извиняйся. Просто вышло недоразумение."
    mc.c "Просто помни: со мной ты всегда можешь быть откровенной."
    grace.c "[mc.name]..."
    hide grace with dissolve
    show grace kiss with dissolve
    show grace smile with dissolve
    "После лёгкого поцелуя она наконец садится рядом."
    mc.c "Знаешь, это не последний раз. Просто... не сегодня."
    show grace tease talk
    grace.c "Правда?.."
    show grace tease 
    mc.c "Обещаю: всё будет так, как ты захочешь."
    show grace tease talk
    grace.c "Т-ты можешь пожалеть, что это сказал..."
    show grace tease 
    mc.c "Обещаю."
    "Мы немного молчим. [grace.name] кладёт ладонь на мою."
    mc.c "Слушай, всё это приятно, но разве у тебя нет подушечек на лапах? Я думал, у антро они есть."
    show grace neutral talk
    grace.c "А? У кроликов их нет..."
    mc.c "Хм. Я почему-то решил, что они есть у всех. Даже не задумывался об этом."
    show grace tease talk
    grace.c "Хе-х~ Нет... И ты правда этого не знал? Глупенький~"
    show grace tease
    mc.c "Выходит, я ненастоящий фанат антро..."
    show grace thinking
    grace.c "То есть для тебя мы просто фетиш?"
    mc.c "Ой, я... э-э..."
    show grace tease talk
    grace.c "Хе-хе~ Да шучу я~"
    show grace bashful talk
    grace.c "Чёрт, скоро уже на работу..."
    show grace bashful
    mc.c "О, ладно, не буду тебя задерживать."
    show grace tease talk
    grace.c "Я не успею принять душ... Пойти на работу вся в твоей сперме... Боже мой..."
    grace.c "Какая же я грязнуля~"
    show grace tease
    "Как и думал, она немного извращенка — в хорошем смысле. Но вслух так говорить не буду."
    mc.c "Чёрт, непослушная девочка. Почему мне кажется, что ты ненасытная?"
    show grace tease talk
    grace.c "Постарайся меня не разочаровать."
    "[grace.name] встаёт и направляется к двери. Я провожаю её."
    mc.c "Я скоро тебе позвоню."
    show grace smile talk 2
    grace.c "Ага... [mc.name]..."
    grace.c "Спасибо."
    hide grace with dissolve
    "Она быстро разворачивается и, краснея, выбегает за дверь."
    "Кто бы мог подумать, что всё так обернётся?"

    if(not fromGallery):
        $ grace.hidden = False
        $ grace.addLike(1)
        $ grace.addLove(1)

    return {'location':location_home}

label graceHEvent3(fromGallery):
    $ location_shop.showBackground()
    "[grace.name]... Последние несколько встреч с ней пролетели вихрем."
    "Я застал её за мастурбацией, потом она взорвалась от злости и ненависти к себе. Снова замкнулась."
    "...И та дрочка..."
    "С тех пор мы откровеннее говорим обо всём этом. Будто у неё с плеч свалился груз."
    "Она многое держала в себе и, по правде, ей просто нужен был тот, кому можно довериться. Теперь она может быть собой."
    "В спокойные дни я захожу за [grace.name], когда у неё заканчивается смена. Иногда мы немного гуляем."
    show grace smile talk with dissolve
    call playMusic(funnyTheme) from _call_playMusic_79
    grace.c "...Так вот, новая глава вышла вчера. Начинается новая арка, выглядит круто, там..."
    show grace smile
    "Она всегда умела без умолку болтать о своих отаку-увлечениях. Это никуда не делось."
    "И это очень мило."
    show grace thinking
    grace.c "Ну вот... Теперь ждать до следующей недели. Почему главы всегда такие короткие? Обидно."
    "Она на секунду оглядывает пустой магазин."
    show grace smile talk 2
    grace.c "Слушай, кстати... После того раза, ну, ты понимаешь."
    show grace smile
    mc.c "Не понимаю."
    show grace smile talk
    grace.c "Ой, не прикидывайся. Мне же пришлось сразу идти на работу."
    grace.c "Весь день тут работать после того, как ты... {size=20}кончил на меня{/size}..."
    show grace bashful talk
    grace.c "Я так нервничала, но..."
    show grace tease talk
    grace.c "Меня это возбудило."
    show grace tease
    mc.c "Давай не будем делать это привычкой."
    show grace tease talk
    "Она наклоняется и шепчет мне на ухо."
    show grace tease talk
    grace.c "А я... ну... ещё пару раз... вспоминала об этом. Хе-хе~"
    show grace tease
    "Вот настоящая [grace.name], и мне это нравится."
    mc.c "Не трать все силы, когда настоящий я рядом."
    show grace tease talk
    grace.c "Тс-с, боже мой... Хе-хе-хе~"
    "До конца её смены недолго, и она то и дело поглядывает на часы."
    mc.c "Хочешь куда-нибудь сходить после работы? Перекусить? Или тебе надо поскорее домой?"
    show grace smile talk
    grace.c "Не, сегодня не получится. Мама как раз принимает друзей, так что лучше я буду подальше от них."
    show grace thinking
    grace.c "Поесть я бы не отказалась, но..."
    show grace bashful talk
    grace.c "Я сейчас... немного на мели. Потратила всю последнюю зарплату на игры. До следующей недели почти без денег."
    show grace bashful
    mc.c "Ничего, я угоща..."
    show grace mad talk
    grace.c "Нет! Перестань."
    show grace thinking
    grace.c "Я не могу позволить тебе всё время на меня тратиться. Это нечестно, я никогда не смогу отплатить."
    mc.c "Меня это совсем не беспокоит..."
    show grace bashful talk
    grace.c "А меня беспокоит... Не хочу чувствовать себя обязанной."
    show grace bashful
    mc.c "Ладно, давай найдём компромисс. Я могу приготовить что-нибудь у себя. Продукты уже есть, так что тратиться не придётся."
    show grace bashful talk
    grace.c "Ты правда это сделаешь?"
    show grace bashful
    mc.c "Конечно, с удовольствием. Пойдём."
    show grace smile talk 2
    grace.c "С-спасибо, здорово."
    show grace smile
    "В магазин заходит другой сотрудник — видимо, пришёл на смену."
    unknown2 "Йо, [grace.name]. Тебе пора, везучая."
    show grace smile talk 2
    grace.c "Фух, наконец-то."
    call stopMusic from _call_stopMusic_14
    scene black with fade
    "Я жду на улице, пока [grace.name] заканчивает дела в подсобке."
    $ location_town.showBackground()
    show grace smile talk with dissolve
    call playMusic(chillTheme) from _call_playMusic_80
    grace.c "Спасибо, что подождал."
    show grace smile
    mc.c "Пойдём."
    "Я протягиваю ей руку. Даже такая простая нежность на людях всё ещё её смущает."
    show grace bashful
    grace.c "..."
    "Но в конце концов она берёт меня за руку."
    scene black with fade
    "После вполне обычного ужина..."
    $ location_home.showBackground()
    show grace joy with dissolve
    grace.c "Спасибо за еду, было очень вкусно!"
    "Хорошо, что у [grace.name] нет утончённого вкуса — ей всё нравится."
    mc.c "На здоровье. Правда, ничего особенного — я готовлю так себе."
    show grace smile talk 2
    grace.c "Да нет, всё правда вкусно! Мне очень понравилось."
    show grace bashful talk
    grace.c "Я... почти ничего не умею готовить. Мама всё делает."
    grace.c "А ты здорово справляешься. Сам живёшь, обо всём заботишься и даже бизнесом управляешь."
    show grace bashful
    mc.c "Научишься. Каждый идёт в своём темпе."
    show grace smile
    grace.c "Hmm..."
    call playMusic(funnyTheme) from _call_playMusic_81
    "Я убираю со стола и отношу посуду на кухню. Обернувшись, замечаю в глазах [grace.name] лукавый огонёк."
    show grace bashful talk
    grace.c "Ой, сэр~ Кажется, я забыла бумажник~"
    show grace sad talk
    grace.c "У меня нет денег за ужин..."
    show grace sad
    "На несколько секунд я теряюсь."
    "Но, судя по её сообщениям, кажется, я понимаю, что она задумала."
    mc.c "О-ой, какая неприятность... Так дело не пойдёт."
    show grace bashful talk
    grace.c "Мне очень жаль, сэр... Может, я могу что-нибудь сделать?"
    grace.c "Н-найти другой способ расплатиться?.."
    show grace bashful
    "Не могу сказать, что у меня большой опыт в таких играх, но попробую подхватить и помочь ей получить желаемое."
    mc.c "Другой способ расплатиться? Посмотрим. Есть что-нибудь ещё на обмен? Украшения, например?"
    show grace bashful talk
    grace.c "Н-нет, сэр..."
    show grace bashful
    mc.c "Могу оставить тебя поработать на кухне, но не уверен, что ты справишься..."
    show grace bashful talk
    grace.c "Для такой физической работы я не гожусь~"
    show grace bashful
    mc.c "Тогда даже не знаю, как ты можешь возместить мне ущерб. Придётся позволить тебе поесть бесплатно."
    show grace surprise
    grace.c "Э-это было бы позором! Пожалуйста, позвольте мне хоть что-нибудь сделать!"
    mc.c "И что же ты предлагаешь, юная леди?"
    show grace bashful talk
    grace.c "Я могла бы... могла бы..."
    show grace tease talk
    grace.c "М-может... доставить вам удовольствие, сэр?"
    show grace tease
    mc.c "Доставить удовольствие? Каким образом, милашка?"
    show grace tease talk
    grace.c "Похоже, вашему {b}достоинству{/b} не помешало бы немного внимания."
    show grace tease
    "И как вовремя — мне даже не приходится притворяться: от этой игры у меня уже встаёт."
    mc.c "О, совершенно верно. Кажется, о нём и правда стоит позаботиться..."
    "Самому себе я сейчас кажусь нелепым. Ужасно играю."
    "[grace.name], похоже, это совсем не смущает. Кажется, ей нравится."
    show grace smile talk 
    grace.c "П-присядьте сюда, сэр. Я... позабочусь о вас..."
    show grace smile
    "[grace.name] ведёт меня к дивану и предлагает сесть. Она снова хочет подрочить мне, как в прошлый раз? Или, может..."
    "Я сажусь, пока она возится с моим ремнём. Думаю, не пора ли нам преодолеть ещё одну преграду."
    "Возможно, это уже слишком. Её внешность под одеждой — болезненная тема."
    "Я видел её ноги лишь мельком, да и было темно. С тех пор мы стали ближе, но я всё ещё не видел больше её тела."
    "Попробую."
    call stopMusic from _call_stopMusic_15
    mc.c "Погоди, милая. Ты ничего не забыла?"
    show grace neutral talk
    grace.c "Забыла?"
    mc.c "Не хочешь испачкать свою одежду, правда?"
    call playMusic(heartTheme) from _call_playMusic_82
    show grace neutral talk
    grace.c "..."
    show grace bashful 
    grace.c "..."
    "Похоже, её взгляд и правда искренний. Она медлит — не слишком ли далеко я зашёл?"
    grace.c "К-как пожелаешь..."
    "Она медленно тянется к молнии куртки. Неужели это наконец происходит?"
    "Нерешительно отворачиваясь, [grace.name] начинает снимать спортивный костюм."
    image grace blowjob start 1 = Image("images/characters/grace/hscenes/blowjob/start1.webp")
    scene grace blowjob start 1 with fade
    pause
    "Сначала куртка падает на пол, открывая стройное, худенькое тело [grace.name]."
    "Белый мех струится по ней, словно драпировка, и чуть поблёскивает на солнце."
    "Но на белом фоне проступают светло-коричневые пятна. Часть узора видна на лице и шее, а здесь..."
    "Он покрывает туловище и руки без всякой симметрии, хаотичными пятнами."
    "[grace.name] краснеет и не может встретиться со мной взглядом, но продолжает раздеваться."
    image grace blowjob start 2 = Image("images/characters/grace/hscenes/blowjob/start2.webp")
    scene grace blowjob start 2 with fade
    pause
    "Она снимает брюки, и становится видно, как белый мех по всему телу переходит в песочный."
    "Узор неровный, но..."
    mc.c "Красиво."
    grace.c "..."
    "[grace.name] краснеет и молчит. Наверное, ей приходится собрать всю волю, чтобы продолжать."
    "Когда я решил, что всё, она тянется к застёжке бюстгальтера..."
    image grace blowjob start 3 = Image("images/characters/grace/hscenes/blowjob/start3.webp")
    scene grace blowjob start 3 with fade
    pause
    "Он падает на пол, обнажая аккуратную грудь."
    "Посреди неё выступают два идеально розовых соска."
    "Она стоит передо мной в одних трусиках, напряжённая и скованная от смущения."
    "Я теряю дар речи. Передо мной эта застенчивая, нежная, нервная и прекрасная женщина."
    "Слова сейчас ни к чему. Я протягиваю руку, приглашая её продолжить."
    call playMusic(sexyTheme) from _call_playMusic_83
    image grace blowjob part 1 = Image("images/characters/grace/hscenes/blowjob/part1.webp")
    scene grace blowjob part 1 with fade
    pause
    "[grace.name] опускается на колени между моих ног. Член уже каменный от возбуждения."
    "Она щурится, сосредоточенно его разглядывая, но без колебаний берёт за ствол."
    grace.c "Он всё ещё... такой большой."
    grace.c "Я всё вспоминала этот запах..."
    image grace blowjob part 2 = Movie(play="images/characters/grace/hscenes/blowjob/part2.webm")
    show grace blowjob part 2 with fade
    pause
    "Она тихонько принюхивается, высовывает язык и начинает ласково лизать нижнюю сторону головки."
    "От этого ощущения по спине уже бегут мурашки."
    mc.c "Ох, чёрт... [grace.name]..."
    grace.c "М-м-м. На вкус он..."
    "Даже боюсь представить."
    grace.c "...Приятный..."
    "Она смотрит мне в глаза невероятно похотливым взглядом, будто теряет себя в происходящем."
    "В таких ситуациях в ней будто щёлкает переключатель — наружу выходят скрытые желания."
    "Очевидно, что она очень сексуальна, но ей понадобилось время, чтобы раскрепоститься со мной."
    mc.c "Как же хорошо, [grace.name]."
    grace.c "Mmmm~"
    image grace blowjob part 3 = Movie(play="images/characters/grace/hscenes/blowjob/part3.webm")
    show grace blowjob part 3 with fade
    pause
    "Она накрывает губами головку и, опуская голову, мягко втягивает её в рот."
    "Её тепло невероятно приятно, она обхватывает мой член губами."
    mc.c "Ух ты..."
    grace.c "Mmmhhpf~"
    "Я не разбираю её слов, но слышу, как она довольно стонет."
    "Она крепко сжимает основание и двигает головой, едва умещая его во рту."
    image grace blowjob part 4 = Movie(play="images/characters/grace/hscenes/blowjob/part4.webm")
    show grace blowjob part 4 with fade
    pause
    "Зрелище потрясающее. Маленькая Грейс ласкает мой член, будто это роскошное блюдо."
    "Её изящные пальцы, тонкая талия — теперь всё открыто мне, пока она ублажает меня."
    "Невероятно."
    grace.c "Mmmmm~ Hmmm~"
    "Она тихонько мычит от удовольствия. Прищурившись, наслаждается моментом, будто давно этого хотела."
    mc.c "Fuck~"
    "Я растворяюсь в наслаждении."
    grace.c "Mhrhh?"
    "Не знаю, что она хотела сказать."
    mc.c "Продолжай... пожалуйста..."
    image grace blowjob part 5 = Movie(play="images/characters/grace/hscenes/blowjob/part5.webm")
    show grace blowjob part 5 with fade
    pause
    "Она опускает рот ниже, заглатывая член глубже."
    "Язык скользит по нижней стороне, каждый раз щекоча головку."
    mc.c "Так хорошо, [grace.name]. Не останавливайся..."
    grace.c "Mmmmmm~"
    "Она кладёт ладонь мне на бедро, усиливая ощущения."
    "С этого ракурса я вижу, куда она положила другую руку..."
    image grace blowjob part 6 = Movie(play="images/characters/grace/hscenes/blowjob/part6.webm")
    show grace blowjob part 6 with fade
    pause
    "Она всё это время ласкает себя сквозь трусики."
    "Похоже, ей не меньше нравится, чем мне."
    grace.c "Ih... Hmmhhmm... Hmmth... Hhmhh.."
    "Как бы неловко ни было, я уже близок к пределу."
    mc.c "[grace.name], это потрясающе... Я скоро кончу..."
    "Она на мгновение широко раскрывает глаза, но продолжает, возможно, даже быстрее."
    "Она вздрагивает. Неужели сама кончила?"
    mc.c "I'm..."
    grace.c "Mmmmhh~!"
    "Я оставляю ей возможность отстраниться, но она продолжает, решив довести меня до конца."
    mc.c "[grace.name]!"
    image grace blowjob end = Image("images/characters/grace/hscenes/blowjob/end.webp")
    scene grace blowjob end with fadewhite
    pause
    "Я с силой кончаю ей прямо в горло."
    "Она принимает всё в рот и замирает. Лишь когда я перестаю подёргиваться, медленно отстраняется."
    mc.c "О-ох~ Чёрт."
    "Она поднимает на меня невероятно развратный взгляд и самодовольно улыбается."
    grace.c "Ahhh~"
    "Она открывает рот, показывая результат — не пытается отвернуться или поскорее выплюнуть."
    "Сперма стекает по её губам..."
    mc.c "Это... было потрясающе."
    grace.c "Я о-обожаю твой член~"
    "..."
    "Она снова смотрит на меня."
    call playMusic(funnyTheme) from _call_playMusic_84
    grace.c "Ну, сэр, значит, теперь мы в расчёте?"
    "А?"
    "А, точно. Мы же должны были разыграть эту глупую сценку. Я совсем забыл об этом, когда она начала раздеваться."
    "Ей не обязательно так делать, чтобы проявить инициативу, но было весело. Актёрское мастерство мне ещё стоит подтянуть..."
    mc.c "О-о, {b}*кхм*{/b} да, юная леди, считайте свой долг погашенным."
    mc.c "Но не вздумайте в следующий раз снова поесть за мой счёт!"
    "[grace.name] поднимает на меня озорной взгляд."
    grace.c "Ни за что~"
    "..."
    "Мы несколько мгновений наслаждаемся послевкусием, смущённо переглядываясь."
    grace.c "Д-дай мне на этот раз как следует привести себя в порядок..."
    mc.c "Конечно..."
    scene black with fade
    "Она направляется в ванную, покачивая милой попкой."
    "[grace.name] принимает душ. Многое бы отдал, чтобы присоединиться, но пока лучше не торопить события."
    $ location_home.showBackground()
    show grace smile with dissolve
    mc.c "Сцена окончена?"
    show grace smile talk 2
    grace.c "Хе-х, да. Не слишком глупо получилось?"
    show grace smile
    mc.c "Нет, было весело. Просто застала меня врасплох. Откуда это вообще взялось?"
    show grace thinking
    grace.c "Ну... Я просто не знала, как начать."
    show grace bashful talk
    grace.c "Что мне сказать? «Спасибо за еду, теперь дай пососать твой член»?"
    show grace bashful
    mc.c "В прошлый раз всё было не так уж далеко от этого."
    show grace thinking
    grace.c "...Д-да, стараюсь больше так не делать."
    grace.c "Но этот способ, наверное, тоже был глупым."
    mc.c "Ты можешь говорить мне всё что угодно. Вряд ли ты способна меня удивить."
    show grace bashful talk
    grace.c "Ну..."
    show grace bashful
    "Зловеще. Я это сказал, но почему-то мне кажется, что однажды [grace.name] меня ещё удивит."
    show grace smile talk
    grace.c "Мне... пора идти. Но спасибо, что пригласил."
    show grace smile
    mc.c "Всегда пожалуйста. Иди сюда."
    "Я притягиваю её ближе."
    hide grace with dissolve
    show grace hug with dissolve
    mc.c "Перед уходом, [grace.name]."
    grace.c "?"
    mc.c "Ты и правда очень красивая."
    grace.c "..."
    grace.c "..."
    hide grace with dissolve
    show grace kiss with dissolve
    hide grace with dissolve
    show grace smile talk 2 with dissolve
    grace.c "П-пока!"
    hide grace with dissolve
    "И вот так она поспешно вылетает за дверь."
    "Забавная девчонка."

    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.addLove(1) 

    return

label graceHEvent4(fromGallery):
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_85
    "Мы с [grace.name] провели день вместе. Ничего особенного: поели, поболтали, прогулялись."
    "Пока ещё рано, и мы решаем, чем заняться дальше."
    show grace smile with dissolve
    mc.c "Тебе надо за покупками? Можем заглянуть на «рынок для гиков», как ты его называешь."
    show grace thinking
    grace.c "Не, пожалуй, на этой неделе больше тратиться не стоит. Я почти на мели."
    "Я собираюсь что-то сказать."
    show grace mad talk
    grace.c "И не вздумай снова предлагать денег."
    show grace neutral
    grace.c "...По крайней мере, на этой неделе."
    grace.c "Я купила новые материалы, они оказались дороже, чем я думала..."
    mc.c "Делаешь что-то новое?"
    show grace thinking
    grace.c "Есть одна задумка, пока только наброски."
    mc.c "Вот оно!"
    show grace neutral talk
    grace.c "Что именно?"
    mc.c "Покажи мне свои костюмы! До сих пор я видел их только на фотографиях."
    mc.c "Можно к тебе зайти?"
    "Мы уже видели друг друга почти голыми. Неужели она не выдержит небольшой показ своих нарядов?"
    show grace bashful talk
    grace.c "Не знаю..."
    show grace bashful
    mc.c "Твоя мама не будет против, если я зайду? Она показалась милой."
    show grace bashful talk
    grace.c "Н-нет, она не будет против... И сейчас её всё равно нет дома, так что..."
    show grace bashful
    "Тем лучше."
    mc.c "Пожалуйста, [grace.name]. Я бы очень хотел хоть что-нибудь увидеть. Ты столько сил вложила."
    show grace thinking
    grace.c "Ты... правда хочешь?"
    mc.c "Конечно!"
    grace.c "..."
    show grace bashful talk
    grace.c "Наверное, можешь. Правда, никто ещё не видел их вживую..."
    show grace bashful
    mc.c "Уверен, они потрясающие. Пойдём!"
    show grace smile
    grace.c "Л-ладно!"
    scene black with fade
    scene suburbs with fade
    call playMusic(funnyTheme) from _call_playMusic_86
    "Знакомое место. Я несколько раз провожал её до дома, но внутрь не заходил с того самого дня."
    "Интересно, ей всё ещё неловко из-за того случая?"
    scene black with fade
    scene gracehomehall with fade
    "[grace.name] заводит меня внутрь. Быстро кричит, чтобы проверить, нет ли мамы, и ведёт наверх."
    show grace mad talk with dissolve
    grace.c "Я бы сказал «добро пожаловать», но ты уже знаешь дорогу, да?"
    show grace mad
    "Кажется, она просто шутит..."
    mc.c "А-ха-ха... {b}*кхм*{/b}"
    show grace tease
    grace.c "Хе-хе-хе~"
    scene black with fade
    "Мы заходим в её комнату. Приятно снова здесь оказаться."
    scene gracebedroom with fade
    "Полумрак, как и в прошлый раз. Шторы задёрнуты. Но теперь я могу всё рассмотреть."
    "На стенах постеры аниме и игр, на полу разбросана одежда."
    "Полки с мангой, играми и парой фигурок. Настоящая комната отаку."
    "В воздухе снова чувствуется тяжесть. Стоило бы открыть окно, но..."
    "Мне не мешает. Пахнет ею."
    show grace bashful talk with dissolve
    grace.c "Э-э, я не думала, что ты зайдёшь... Я не убралась."
    grace.c "Чёрт, наверное, я ужасно выгляжу."
    show grace bashful
    mc.c "Не мешает. Это же твой беспорядок, значит, он прекрасен."
    show grace mad talk
    grace.c "Ой, з-заткнись."
    show grace thinking
    grace.c "Садись. Я принесу нам что-нибудь попить, подожди минутку."
    show grace mad talk
    grace.c "И-н-не ройся в моих вещах!"
    show grace mad
    mc.c "Обещаю!"
    hide grace with dissolve
    "Не обещаю."
    "..."   
    "Я сажусь на её кровать и оглядываюсь."
    "Сразу видно, что раньше здесь жила затворница. Рад, что она начала выбираться из дома."
    "Может, ей и не нравится работа, но надеюсь, она привыкает. А я, может быть, помогаю ей легче переносить жизнь за пределами дома."
    "Одежда разбросана по всему полу: что-то лежит стопками, что-то — где попало."
    "Даже нижнее бельё. Простое и изящное. Она велела не рыться, но, [grace.name], и что мне с этим делать?"
    "В этот момент я что-то чувствую ногой. Опускаю взгляд..."
    scene gracehevent4i1 with fade
    pause
    "Ты просто оставила это на полу? Ну, если не ждёшь гостей..."
    "Кажется, это даже не та игрушка, которую я видел тогда. Она большая любительница игрушек? Не удивлён."
    "Меня это не смущает, я за сексуальную свободу. Эх, если бы я тоже мог..."
    "Погодите, что я хотел этим сказать? Сам не знаю."
    "..."
    "Я не могу отвести взгляд от этой штуки. Сколько их у неё? Как часто она ими пользуется?"
    "Вопреки здравому смыслу я наклоняюсь и поднимаю её. Чего мне брезговать? Я ведь знаю, где она побывала."
    scene gracehevent4i2 with fade
    "Ну и здоровяк. Но, кажется, я всё-таки покрупнее. Мужская гордость спасена."
    "..."
    "Что я творю?"
    scene gracebedroom with fade
    show grace smile talk with dissolve
    grace.c "Кола подойдёт?"
    show grace surprise
    grace.c "А-А-А!"
    grace.c "ЧТО ТЫ ДЕЛАЕШЬ?!"
    mc.c "Э-э, твой друг валялся прямо на полу..."
    show grace mad talk
    grace.c "Чёрт возьми... Я же просила не рыться в моих вещах."
    show grace mad
    mc.c "Она просто прямо тут лежала."
    show grace mad talk
    grace.c "З-зачем ты её поднял, извращенец?"
    show grace mad
    mc.c "Хотел спросить, нет ли у неё интересных историй."
    grace.c "..."
    "Она вырывает игрушку у меня из рук и запихивает в ящик."
    "Я не вижу содержимое, но по звуку там лежит ещё несколько штук."
    show grace thinking
    grace.c "Идиот..."
    mc.c "До встречи, дружок!"
    show grace tease
    grace.c "П-ф-ф!"
    show grace tease talk
    grace.c "Тебе повезло, что ты смешной..."
    show grace thinking
    grace.c "{b}*Кхм*{/b} Ладно, забудем об этом..."
    grace.c "Я покажу тебе один наряд, если будешь хорошо себя вести..."
    mc.c "Что мне достанется?"
    grace.c "Посмотрим... Как насчёт волшебницы? Наверное, это мой лучший костюм. Ты уже видел его на фотографии."
    mc.c "Ура!"
    show grace mad
    grace.c "..."
    show grace thinking
    grace.c "Просто отвернись. И не подглядывай, иначе выгоню тебя отсюда."
    mc.c "Так точно, капитан."
    scene black with fade
    call stopMusic from _call_stopMusic_16
    "..."
    "Я поворачиваюсь к шторам. За спиной слышно, как шуршит одежда."
    "..."
    "За такую выдержку мне полагается награда."
    grace.c "Это... займёт ещё немного времени, там много деталей..."
    mc.c "Не могу дождаться."
    "..."
    "Спустя пару минут..."
    grace.c "Всё... Можешь повернуться."
    call playMusic(heartTheme) from _call_playMusic_87
    image grace cunnilingus start 1 = Image("images/characters/grace/hscenes/cunnilingus/start1.webp")
    scene grace cunnilingus start 1 with fade
    pause
    mc.c "Ничего себе..."
    "Теперь она почти не похожа на себя. Обычно я вижу её в спортивном костюме, с головы до ног укрытую одеждой."
    "А в этом струящемся цветочном кружевном платье она совсем преобразилась."
    "И без очков выглядит совсем иначе."
    mc.c "Ты прекрасна!"
    grace.c "Р- речь не обо мне... О костюме, [mc.name]..."
    mc.c "А, да, конечно, он потрясающий! Столько деталей."
    mc.c "И тебе он тоже очень идёт!"
    grace.c "..."
    grace.c "Спасибо..."
    image grace cunnilingus start 2 = Image("images/characters/grace/hscenes/cunnilingus/start2.webp")
    scene grace cunnilingus start 2 with fade
    pause
    "Она кружится. Вид [grace.name] в юбке пробуждает во мне что-то глубоко внутри. Я уже начинаю заводиться."
    "[grace.name] показывает мне этот милый наряд, и это неожиданно меня возбуждает."
    "Она приглаживает складки."
    mc.c "Просто великолепно, ты отлично поработала."
    grace.c "Ну... Не так уж хорошо..."
    image grace cunnilingus start 3 = Image("images/characters/grace/hscenes/cunnilingus/start3.webp")
    scene grace cunnilingus start 3 with fade
    pause
    "Юбка чуть приподнимается, и я мельком вижу её трусики."
    "Трусики..."
    grace.c "Ну... нравится?"
    mc.c "Очень."
    "Она слегка подходит ближе и поправляет часть костюма, совсем отвлёкшись."
    "Опасно стоять так близко ко мне в таком наряде."
    "Я покидаю кровать и ныряю под подол её юбки."
    call playMusic(sexyTheme) from _call_playMusic_88
    image grace cunnilingus part 1 = Image("images/characters/grace/hscenes/cunnilingus/part1.webp")
    scene grace cunnilingus part 1 with fade
    pause
    grace.c "[mc.name]! Т-ты что делаешь?!"
    mc.c "Не обращай внимания, я просто... исследую."
    grace.c "В-вылезай оттуда, и-идиот..."
    grace.c "O-oohh~"
    "Я утыкаюсь носом в её изящные трусики."
    grace.c "О-ой~ П-погоди..."
    "Она тихо постанывает от удовольствия, когда я ласкаю её клитор лицом."
    mc.c "Позволь мне немного эгоизма — я хочу узнать, что повидала твоя игрушка."
    grace.c "О-о боже~"
    grace.c "П-подожди! Может, тебе сначала принять душ?"
    mc.c "Ни за что."
    image grace cunnilingus part 2 = Movie(play="images/characters/grace/hscenes/cunnilingus/part2.webm")
    show grace cunnilingus part 2 with fade
    pause
    "Я прижимаюсь лицом к её промежности и трусь о влажнеющую ткань."
    grace.c "О-о-о~ [mc.name]~"
    "Её протесты сменяются стонами удовольствия."
    "Она нежно кладёт руку мне на голову и едва заметно прижимает меня к себе. Ей это нравится не меньше, чем мне."
    grace.c "А-а-а~ Д-да..."
    "Трусики быстро промокают. Я даже облизываю ткань. Рано или поздно я их отодвину."
    "Хочу прочувствовать всё до конца."
    image grace cunnilingus part 3 = Movie(play="images/characters/grace/hscenes/cunnilingus/part3.webm")
    show grace cunnilingus part 3 with fade
    pause
    "Я обхватываю её за талию и крепко сжимаю упругую попку, плотнее прижимаясь к ней лицом."
    grace.c "Это... боже мой~"
    "С набитым ртом я не могу говорить. Можно продолжать, пока она не кончит, но долго так она не простоит."
    "Я кое-как отстраняюсь, чтобы сказать:"
    mc.c "Ложись. Теперь моя очередь отплатить тебе за прошлый раз."
    grace.c "Ха-а~ П-правда?"
    mc.c "То есть... если ты сама этого хочешь?"
    grace.c "Да! Да!"
    "Я отстраняюсь, обхватываю её за талию и уверенно разворачиваю к кровати."
    image grace cunnilingus part 4 = Movie(play="images/characters/grace/hscenes/cunnilingus/part4.webm")
    show grace cunnilingus part 4 with fade
    pause
    "Я укладываю её на кровать и утыкаюсь лицом в её киску, по пути снимая трусики."
    grace.c "О-ох~ Чёрт..."
    "Передо мной её маленькая, горячая, мокрая киска."
    "[grace.name] извивается, пока я провожу языком по ней."
    "Я ласково сжимаю её ноги, она корчится от удовольствия и без стеснения стонет."
    grace.c "О боже~ [mc.name]~"
    grace.c "Я и представить не могла... М-м-м~ что будет так приятно..."
    "Я слегка сжимаю её ногу, а она прижимает бёдра к моей голове, буквально вдавливая меня глубже."
    image grace cunnilingus part 5 = Movie(play="images/characters/grace/hscenes/cunnilingus/part5.webm")
    show grace cunnilingus part 5 with fade
    pause
    "Я провожу языком по входу, лаская клитор."
    grace.c "М-м-м~ [mc.name]~~"
    "Сладкий вкус и запах этой нежной, но очень непослушной девушки."
    "От каждого прикосновения она вздрагивает. Я и сам теряю голову."
    "Всё, о чём я могу думать, — продолжать."
    grace.c "А-а-а~ М-м-м~"
    "Её сжимающиеся бёдра подсказывают, что она близка. Пора довести дело до конца."
    image grace cunnilingus part 6 = Movie(play="images/characters/grace/hscenes/cunnilingus/part6.webm")
    show grace cunnilingus part 6 with fade
    pause
    "Я придвигаю [grace.name] повыше на кровати и сильнее прижимаюсь к её промежности."
    grace.c "А-А-А~ ЧЁРТ~"
    "Я ускоряюсь, а она инстинктивно упирается ногами мне в спину, направляя мои плечи к себе."
    "Мне уже трудно дышать, но умереть вот так было бы неплохо..."
    "Я тянусь и сжимаю её грудь, чувствуя, как дыхание становится всё чаще."
    grace.c "Не останавливайся~ Я уже почти..."
    "Повсюду влажные чмокающие звуки. Я как можно глубже проникаю языком внутрь."
    "[grace.name] направляет мою голову рукой."
    image grace cunnilingus part 7 = Movie(play="images/characters/grace/hscenes/cunnilingus/part7.webm")
    show grace cunnilingus part 7 with fade
    pause
    grace.c "ДА, ДА, ДА, ДАААА~"
    grace.c "ЗАСТАВЬ МЕНЯ КОНЧИТЬ~"
    "Она всё сильнее дрожит — вот-вот кончит."
    "Я не остановлюсь, пока она не достигнет пика."
    image grace cunnilingus end 1 = Image("images/characters/grace/hscenes/cunnilingus/end1.webp")
    scene grace cunnilingus end 1 with fadewhite
    pause
    grace.c "MMMMMMMMM~~~!"
    grace.c "AAAAHHHHHH~ HAAAHHH~"
    "[grace.name] кончает, забрызгивая моё лицо соками."
    "Я прижимаюсь лицом к её киске, пока она содрогается от экстаза."
    grace.c "Oohhh~~~ Oooooohhhh~"
    grace.c "Haaaa..."
    "..."
    "Она вздрагивает от удовольствия, наконец разжимает ноги и падает на спину, тяжело дыша."
    image grace cunnilingus end 2 = Image("images/characters/grace/hscenes/cunnilingus/end2.webp")
    scene grace cunnilingus end 2 with fade
    pause
    grace.c "*Haah* *Haah*"
    grace.c "Боже мой..."
    grace.c "Как ты это..."
    "Я с гордостью любуюсь своей работой."
    "Девушка совсем обессилела от мощного оргазма."
    mc.c "Ну как?"
    grace.c "*Haah*"
    "Она пытается прийти в себя, а когда возбуждение спадает, наконец осознаёт происходящее."
    call playMusic(chillTheme) from _call_playMusic_89
    grace.c "Что ты, чёрт возьми, сделал, [mc.name]?"
    grace.c "Я же просто показывала тебе костюм..."
    mc.c "Э-э... Ролевая игра?"
    grace.c "Ну так себе у тебя получилось."
    grace.c "..."
    mc.c "Но было горячо, да?"
    grace.c "Ага~"
    grace.c "Дай мне переодеться, ладно? Ты весь костюм измял и испачкал."
    scene black with fade
    "Она садится."
    "Приглаживает несчастный косплей, который я только что испортил."
    mc.c "Прости..."
    scene gracebedroom with fade
    show grace thinking with dissolve
    grace.c "Ты просто зверь."
    mc.c "Кажется, это ты у нас больше похожа на зверя."
    grace.c "Очень смешно..."
    "Я обнимаю её."
    hide grace with dissolve
    show grace hug with dissolve
    "Я вытер лицо, но после того, как она кончила мне на него..."
    mc.c "Я бы тебя поцеловал, но ты же понимаешь..."
    "Она всё понимает, широко раскрывает глаза и сама целует меня."
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "*Mmmhh*"
    "Чёрт, грязно получилось."
    hide grace with dissolve
    show grace smile talk with dissolve
    grace.c "На сегодня представление окончено. Я ещё долго не выдержу такого."
    show grace smile
    mc.c "Будто ты у себя не делаешь так снова и снова."
    show grace mad
    grace.c "..."
    show grace thinking
    grace.c "Ну... Пожалуй, ты прав."
    mc.c "Вот это да."
    mc.c "Спорим, твой маленький дружок так не умеет."
    grace.c "Перестань..."
    grace.c "Мама скоро вернётся. Не хочу, чтобы она нас застала."
    mc.c "Понял: попользовалась и выбросила, да?"
    show grace smile talk 2
    grace.c "Заткнись, [mc.name]. В другой раз продолжим."
    grace.c "Если..."
    show grace smile
    mc.c "Я на всё готов ради тебя."
    show grace bashful 
    grace.c "..."
    mc.c "До скорого, [grace.name]."
    show grace smile talk
    grace.c "Пока, [mc.name]."
    scene black with fade

    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.addLove(1) 

    return {'location':location_town}


label graceHEvent5(fromGallery):
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_90
    show grace smile with dissolve
    "Грейс стала иногда бывать у меня после работы."
    "Я часто зову её сам, а иногда она приходит после наших прогулок. В любом случае мне это нравится."
    "Она всё чаще выходит из своей скорлупы и проводит время вне дома, пусть в основном со мной. Хочу, чтобы ей было комфортно."
    "Она может отдохнуть от мамы — доброй, но иногда слишком назойливой. Это даёт ей немного самостоятельности."
    "Она приходит в гости к своему парню. Не думаю, что слишком самонадеянно так говорить. Мы уже столько всего пережили вместе."
    "Но один большой шаг всё ещё впереди... Я не говорю об этом прямо, однако между нами всё ясно."
    "Я её первый парень. Её первое {b}всё{/b}. Она явно любит секс, но всё ещё девственница."
    "Ей уже комфортно самой проявлять инициативу. Иногда она с любопытством спрашивает о том, каково быть с «парнем»."
    "Но до главного мы пока не дошли. Чёрт знает, как я этого хочу, но решил оставить этот шаг ей — когда будет готова."
    "Как бы то ни было, милая девушка отдыхает у меня дома... Что ещё нужно?"
    "Мы едим, смотрим всякую ерунду, играем или просто даём ей расслабиться с мангой или телефоном."
    "Мы обнялись на диване и только что досмотрели новый эпизод какого-то аниме, которое ей нравится."
    "Если честно, полная ерунда. Типичное высокое фэнтези с игровыми механиками... Но вроде связано с какой-то игрой, в которую она играет. Не знаю."
    show grace thinking
    grace.c "Ну и отстой. Эта арка совсем никудышная."
    mc.c "Вот и я о том. Думал, может, чего-то не понимаю."
    show grace smile talk
    grace.c "Зато девочки милые, правда?"
    show grace tease talk
    grace.c "Зато девочки милые, правда?"
    show grace tease
    "Она легонько толкает меня в бок."
    mc.c "М-м, но у них нет таких милых ушек, как у тебя."
    "Я слегка щекочу одно из её висячих ушей."
    show grace joy
    grace.c "Хе-хе, перестань!"
    show grace smile talk 2
    grace.c "Да ладно, глупыш."
    show grace smile
    "Мы устраиваемся поудобнее, пока идут титры, а Грейс прижимается ко мне."
    "Мне совсем не хочется отпускать её, но она уже давно здесь, а мне надо кое-чем заняться."
    mc.c "Мне нужно отправить пару писем — счета и всё такое. Ты не против, если я...?"
    show grace smile talk
    grace.c "Конечно, занимайся. А я пока почитаю."
    show grace smile
    "Она отодвигается, чтобы я мог встать, но я успеваю украдкой поцеловать её."
    hide grace with dissolve
    show grace kiss with dissolve
    hide grace with dissolve
    show grace smile with dissolve
    mc.c "Это ненадолго."
    show grace bashful
    grace.c "Mhm..."
    "...Она всё ещё смущается от поцелуев, даже после всего, что между нами было. Такая милая."
    show grace smile
    "Она снова достаёт телефон. И минуты не проходит без того, чтобы она что-нибудь читала или бездумно щёлкала в гача-игре."
    "Мне не нравятся внутриигровые валюты, но мы уже это обсуждали. Не стану поднимать тему снова, пусть развлекается."
    scene black with fade
    "Примерно полчаса утомительной бумажной работы спустя..."
    call playMusic(heartTheme) from _call_playMusic_91
    $ location_home.showBackground()
    show grace thinking with dissolve
    "Каждый раз, как я поглядывал на неё, она листала что-то в телефоне, наверное читала."
    "Я почти закончил. Со своего стола не вижу экран, но она, кажется, полностью поглощена тем, что читает."
    "Она так увлекается, что порой её трудно вернуть в реальность."
    "Я наклоняюсь, пытаясь разглядеть, что она читает."
    "Она так поглощена, что не замечает, как я подхожу."
    "Какая-то манга. Не могу разобрать подробности, но по мере того, как она листает, становится всё откровеннее."
    "Различаю лишь силуэты тел, но, похоже, они там занимаются сексом."
    "Она не отрывает глаз от экрана."
    mc.c "Что это?"
    show grace surprise
    grace.c "А! [mc.name]..."
    "Она чуть отворачивает телефон."
    show grace neutral
    grace.c "О-ой, э-э... Просто читаю кое-что, что нашла..."
    mc.c "Порно?"
    show grace surprise
    grace.c "Н-нет!"
    show grace thinking
    grace.c "Это манга..."
    grace.c "Я прочитала описание, думала, там обычное исекай... Не ожидала, что всё будет настолько... настолько..."
    "Она умолкает, продолжая медленно листать страницы и следить за происходящим."
    show grace neutral talk
    grace.c "Ну, э-э..."
    grace.c "..."
    "Я подхожу и сажусь рядом, чтобы рассмотреть получше."
    "Да уж, это секс. Какой-то приключенец занимается сексом с кем-то."
    "Человек-мужчина и женщина, похожая на крольчиху."
    "...Похоже, такого материала полно."
    mc.c "Ты просто случайно наткнулась на это, да?"
    "Она снова опускает телефон."
    show grace neutral
    grace.c "Кхм, ну да. Всё равно ничего особенного..."
    "Она ерзает и крепко сжимает колени. Ей что, понравилось?"
    mc.c "Ха-ха, Грейс, не надо ничего скрывать. Помнишь, мне всё равно, что тебе нравится."
    show grace bashful talk
    grace.c "Да мне было не особо интересно... Но..."
    show grace bashful
    grace.c "..."
    "Она снова замыкается. Иногда ей нужно мягко помочь раскрыться."
    "Я успокаивающе кладу руку ей на колено. Она смотрит вниз, но продолжает ёрзать."
    show grace neutral
    grace.c "I..."
    grace.c "..."
    grace.c "[mc.name]... Я..."
    show grace thinking
    grace.c "Я... х-хочу... сделать это... с тобой..."
    "Я удивлённо округляю глаза и сглатываю. Она явно предложила заняться сексом."
    "Наверняка ей стоило огромных усилий набраться смелости. Знала бы она, как приятно мужчинам это слышать. Да и бояться нечего."
    "Я поглаживаю её ногу, пытаясь успокоить."
    mc.c "Я тоже хочу, Грейс. Правда. Если ты уверена, ладно?"
    show grace smile talk
    grace.c "П-правда?"
    show grace smile
    mc.c "Ну ты и глупышка. Конечно! Кто бы отказался? Я давно этого хотел, просто ждал, пока ты будешь готова."
    show grace smile talk
    grace.c "Я... Да..."
    "Она не знает, что сказать. Я тоже, если честно. Тут поступки важнее слов. Я притягиваю её к себе."
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "*Mhmm*"
    grace.c "*Mwah*"
    hide grace with dissolve
    show grace hug with dissolve
    mc.c "Я хочу тебя."
    grace.c "Я... тоже тебя хочу..."
    scene black with fade
    "Мы перебираемся к кровати, по пути раздеваясь."
    "Я укладываю её и целую, исследуя друг друга в объятиях."
    image grace makeout 1 = Movie(play="images/characters/grace/hscenes/missionary/makeout1.webm")
    show grace makeout 1 with fade
    pause
    grace.c "*Mhnm*~"
    "Наши губы сливаются в страстном поцелуе — ещё более страстном, чем прежде."
    "Мы переплетаемся языками, тихо вздыхая и постанывая от каждого движения."
    grace.c "[mc.name]~"
    mc.c "Грейс..."
    "Грейс гладит меня по щеке. Её нежный мех щекочет мои пальцы."
    "Вкус её губ и языка... Мы продолжаем переплетать языки в медленном поцелуе."
    "Желая почувствовать её ещё ближе, я укладываю Грейс на себя."
    image grace makeout 2 = Movie(play="images/characters/grace/hscenes/missionary/makeout2.webm")
    show grace makeout 2 with fade
    pause
    "Её туловище прижимается к моей груди, скромная грудь трётся обо мне."
    "Мы обнимаемся, тесно прижимаясь друг к другу и продолжая страстно целоваться."
    "Я опускаю руку и крепко хватаю её упругую попку."
    grace.c "*Mmmhnnn*~"
    "Наше дыхание учащается, мы растворяемся в жаре страсти."
    "Её промежность прижимается к моей... Член вот-вот порвёт трусы."
    "Наконец мы отстраняемся. Грейс ложится на спину, приготовившись."
    image grace missionary start = Image("images/characters/grace/hscenes/missionary/start.webp")
    show grace missionary start with fade
    pause
    "Передо мной лежит прекрасная Грейс."
    "Её яркий мех, стройное тело, милое невинное лицо..."
    "Она открылась... мне."
    "Она... расслабилась."
    "Я чуть придвигаюсь к ней."
    grace.c "Секундочку..."
    "Она передумала?"
    grace.c "Можно я... сниму очки? Если ты не против..."
    grace.c "Не хочу, чтобы они мешали."
    mc.c "Конечно. Ты красивая и в очках, и без."
    grace.c "Hmm..."
    "Она аккуратно откладывает очки. Редкое зрелище — Грейс без них."
    "Она прекрасна, как всегда."
    "Она снимает трусики, и передо мной открывается её блестящая от влаги киска."
    "Она вся мокрая и готова, а я так долго этого ждал, что едва могу сдержаться."
    "Я уже собираюсь спросить, всё ли хорошо, но она сама говорит:"
    grace.c "[mc.name]. Не волнуйся, я этого хочу и полностью готова..."
    grace.c "Твой... Хе-х~ Твой дружок меня не пугает. Хе-хе~"
    "Она уже может шутить, и это успокаивает меня. Похоже, мы просто сможем наслаждаться моментом."
    call playMusic(sexyTheme) from _call_playMusic_92
    scene black with fade
    "Мы снимаем оставшееся бельё. Я осторожно поднимаю её ноги к своей талии и медленно вхожу в неё впервые."
    image grace missionary part 1 = Movie(play="images/characters/grace/hscenes/missionary/part1.webm")
    show grace missionary part 1 with fade
    pause
    "Грейс легко принимает меня. Я погружаюсь в её горячую, мокрую киску."
    "Она вздрагивает, когда я вхожу, но постепенно привыкает к ощущениям."
    grace.c "О-ох~ Ничего себе~"
    mc.c "Скажи, если..."
    grace.c "Нет! Всё... прекрасно~"
    "Она прикрывает глаза и закатывает их, пока я исследую её глубину."
    "Её небольшая грудь приподнимается и опускается, когда я двигаюсь."
    image grace missionary part 2 = Movie(play="images/characters/grace/hscenes/missionary/part2.webm")
    show grace missionary part 2 with fade
    pause
    grace.c "О-ох~ Я так долго этого хотела..."
    mc.c "Я тоже тебя хотел."
    "Она знакома с проникновением. Интересно, приятнее ли ей, чем с игрушками? Надеюсь, моё самолюбие не пострадает."
    "Она смотрит на меня с нежностью и желанием, слегка вцепившись в кровать, пока я вхожу глубже."
    grace.c "Ahhh~ Mmmmhh~"
    grace.c "Ещё~ Не останавливайся..."
    "Она уже хочет большего. Как и я."
    image grace missionary part 3 = Movie(play="images/characters/grace/hscenes/missionary/part3.webm")
    show grace missionary part 3 with fade
    pause
    "Я слегка поднимаю её ноги, придвигая её бёдра к себе."
    "Я придерживаю её за талию и могу входить сильнее и глубже."
    "Её мягкие складки нежно сжимаются вокруг моего члена, пока я двигаюсь внутри."
    grace.c "О-ох~ Чёрт~"
    grace.c "[mc.name]... Да-а~"
    mc.c "Грейс... Ты такая восхитительная..."
    grace.c "Ты такой большой~ Так хорошо~"
    "Она тихо вскрикивает от удовольствия, забывая о стеснении."
    "Я хочу заставить её кричать, подарить ей нечто совершенно новое."
    "Она закатывает глаза и откидывает голову на кровать с каждым толчком."
    grace.c "Почему~ *А-а* Мне пришлось так *А-а* долго ждать~"
    mc.c "Теперь я здесь. Надо наверстать упущенное..."
    grace.c "Хочу, чтобы ты был во мне всегда~"
    "Ей явно нравится, и меня это заводит ещё сильнее."
    "Нужно сменить позу, чтобы ускориться. Хочу услышать её крики."
    image grace missionary part 4 = Movie(play="images/characters/grace/hscenes/missionary/part4.webm")
    show grace missionary part 4 with fade
    pause
    "Я нависаю над ней и прижимаюсь к её киске всем телом."
    grace.c "О-ох~ А-а-а~"
    grace.c "Да~ Да-а~"
    grace.c "ТРАХАЙ МЕНЯ, ТРАХАЙ!"
    "Она теряет голову, отпуская все свои запреты."
    "Обычно она такой не бывает. Мне хочется помочь ей раскрыться ещё сильнее."
    mc.c "Что такое, Грейс? Хочешь ещё?"
    grace.c "ДА! ДА! *А-А* ТРАХАЙ МЕНЯ!"
    grace.c "MHMHHNNN~"
    "Она содрогается от удовольствия — явно только что кончила."
    "Я сам уже близок к пределу."
    image grace missionary part 5 = Movie(play="images/characters/grace/hscenes/missionary/part5.webm")
    show grace missionary part 5 with fade
    pause
    "Её прекрасное, невинное лицо растворяется в наслаждении."
    "Её блестящие зелёные глаза проглядывают сквозь прищур, полные желания."
    "Она смотрит прямо мне в глаза... с похотью."
    grace.c "Ahhnn~ Haaaa~"
    mc.c "Грейс... Я..."
    grace.c "КОНЧИ В МЕНЯ, ПОЖАЛУЙСТА~"
    grace.c "НАПОЛНИ МЕНЯ~"
    "Я и так был на пределе, а теперь окончательно теряю контроль."
    mc.c "Грейс!"
    image grace missionary finish = Image("images/characters/grace/hscenes/missionary/finish.webp")
    show grace missionary finish with fadewhite
    pause
    "Я глубоко кончаю в неё. Она вздрагивает и стонет."
    "От удовольствия у меня темнеет в глазах, мы крепко обнимаем друг друга."
    "Сперма сразу вытекает из её киски — удержать такой объём невозможно."
    grace.c "О-ох~ *ха-а* Чёрт~"
    grace.c "Боже мой~ Это было... *ха-а* Вау~"
    scene black with fade
    "Наконец я приподнимаюсь с неё, всё ещё тяжело дыша."
    "Когда возбуждение спадает, Грейс с трудом поворачивается ко мне."
    call playMusic(heartTheme) from _call_playMusic_93
    scene gracepillowtalk with fade
    pause
    mc.c "Ты была невероятной."
    grace.c "*ха-а* Да~"
    grace.c "Лучше, чем я могла представить..."
    grace.c "Я... странно себя вела?"
    mc.c "Не страннее обычного, Грейс."
    "Она находит силы слегка толкнуть меня в руку."
    grace.c "Заткнись..."
    mc.c "Спорю, теперь ты больше не захочешь мистера Пластикового."
    grace.c "Не... Порти... этот момент..."
    "Мы лежим рядом, наслаждаясь тем, что произошло."
    "Её милое раскрасневшееся лицо смотрит прямо на меня. Не хочу, чтобы этот миг заканчивался."
    grace.c "[mc.name]. Спасибо."
    mc.c "Не каждый день благодарят за секс с прекрасной девушкой, но я не против."
    grace.c "Ладно, больше не буду тебя благодарить... Господи..."
    "Мы переглядываемся, слегка улыбаясь и смеясь."
    "Мы ещё никогда не были так близки. Даже не хочется отпускать её."
    mc.c "Грейс, я бы хотел, чтобы ты осталась у меня на ночь."
    grace.c "П-правда? Переночевать здесь?"
    mc.c "Останешься?"
    grace.c "Д-да! Очень хочу."
    grace.c "Только напишу маме..."
    grace.c "Погоди! Она же поймёт, что..."
    mc.c "Когда-нибудь ей всё равно придётся узнать, Грейс. Мы взрослые. Наверняка она уже обо всём догадывается."
    grace.c "Угу... Не хочу представлять, что она думает обо мне..."
    mc.c "Неужели ты заставишь меня сегодня спать одного?"
    grace.c "...Ладно, тут ты меня поймал."
    scene black with fade
    "После пары сообщений Грейс ложится со мной в кровать."
    call graceSleepover from _call_graceSleepover
    "Сегодня я буду обнимать эту милую, прекрасную девушку, пока она не уснёт."
    mc.c "Спокойной ночи, Грейс."
    grace.c "Спокойной ночи, [mc.name]."
    "За ещё много прекрасных мгновений вместе."
    pause
    call graceMorningBedInteraction from _call_graceMorningBedInteraction
    
    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.addLove(1)
        $ grace.virgin = False

    return {'time':'Morning'}

label graceHEvent6(fromGallery):
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_94
    "Скучно, скучно, скучно..."
    "Передо мной мерцает экран компьютера. Счета, накладные, цифры..."
    "Лучше, чем работать на кого-то, но порой всё равно слишком тяжело."
    "Я всё сделаю, просто... не сегодня."
    "Я плюхаюсь на диван. Чем бы заняться? Совсем нет сил."
    "Может, поиграть... Не, игра сейчас слишком напряжённая."
    "Телевизор... Ничего интересного."
    "Сериалы? Всё уже посмотрел."
    "Чёрт, я как старик. Должен же быть полон энергии."
    "Может, просто полежу... Пойдёт."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "А?"
    "О, телефон. Наверное, сообщение. Надеюсь, не очередная внезапная перестановка смены."
    "О, это Грейс! Вот от кого я сейчас хотел бы получить сообщение."
    grace.c "эй, чем занимаешься?"
    "О-о, интересуется, как я. Мило."
    mc.c "Разбирался с налогами, но уже до смерти заскучал."
    mc.c "Пытаюсь придумать, чем заняться, но пока просто бездельничаю. А ты?"
    "..."
    "Она долго печатает, потом перестаёт."
    "Снова долго печатает и снова останавливается."
    "Хочет сказать что-то важное? Или просто слишком долго обдумывает каждое слово."
    grace.c "смотрела аниме"
    "И всё? Что же она тогда так долго печатала?"
    "Нет, ещё сообщение."
    grace.c "так ты ничего не делаешь?"
    mc.c "Ага. Если ты свободна, может, увидимся?"
    "Она снова печатает. Обычно в переписке отвечает быстрее."
    "Наверное, что-то её тревожит. Дам ей договорить."
    "..."
    "Или нет... Перестала печатать."
    mc.c "Что-то случилось? Можешь мне рассказать."
    "Печатает... Забавная она всё-таки."
    "..."
    grace.c "ты мне нужен"
    mc.c "Что тебе нужно? Помочь с чем-нибудь?"
    "..."
    call stopMusic from _call_stopMusic_17
    grace.c "я возбуждена"
    "Я сразу оживляюсь. Стыдно признаться, но тут же вскакиваю. Что я, подросток?"
    grace.c "я дома мамы нет"
    "Я уже на ногах и почти у двери. Не стоит так поспешно срываться, но кто бы меня осудил?"
    grace.c "придешь?"
    "Натягивая обувь, я уже набираю ответ."
    mc.c "Уже иду."
    "Ничего себе. Вроде прямое приглашение, хоть и не совсем. Повезло же мне."
    "Она часто слишком долго думает, как выразиться, а потом говорит прямо и без обиняков."
    "Как мило. Но сейчас это ещё и чертовски возбуждает."
    $ location_town.showBackground()
    call playMusic(sexyTheme) from _call_playMusic_95
    "Я вылетаю из дома в рекордное время."
    "Почти бегу к ней, счастливый как ребёнок. Я так рад, что Грейс вызывает во мне такие чувства."
    "Надо держать себя в руках. От ожидания уже появляется полуэрекция..."
    scene suburbs with fade
    "Вот это да. Ей и правда хотелось меня увидеть, раз она так прямо написала."
    "А вдруг это... розыгрыш?"
    "Немного не похоже на неё... Я иногда её дразню... Может, решила отомстить?"
    "Не, вряд ли."
    "Вот я и пришёл. Дома одна, да?"
    "{b}*Динь-дон*{/b}"
    "Я жду у двери, весь в предвкушении, сердце так и трепещет."
    "Забавно, как женщины могут так вскружить мужчине голову, да?"
    "Дверь открывается, и из-за неё выглядывает маленькая Грейс."
    show grace bashful with dissolve
    show grace bashful talk
    grace.c "П-привет..."
    show grace bashful
    mc.c "Курьер доставил посылку для мисс Грейс. Распишитесь здесь."
    show grace bashful talk
    grace.c "О-о боже... Не верится, что я это сделала."
    grace.c "Заходи..."
    scene gracehomehall with fade
    show grace bashful with dissolve
    mc.c "Погоди, что случилось?"
    show grace bashful talk
    grace.c "Я... не должна была."
    show grace bashful
    mc.c "Даже не представляю, как ты могла подумать, что мне не хочется быть здесь прямо сейчас."
    show grace bashful talk
    grace.c "Всё равно... Это немного... ну, ты понимаешь..."
    show grace mad talk
    grace.c "Но, чёрт! Я не могла перестать о тебе думать."
    show grace mad
    mc.c "Приятно слышать."
    mc.c "Обо мне или о моём члене?"
    show grace mad talk
    grace.c "О твоём члене, дурак!"
    show grace bashful talk
    grace.c "П-погоди... О тебе, конечно..."
    grace.c "С тех пор как мы... Ну, ты понимаешь..."
    show grace bashful
    "Милая Грейс всё ещё теряется, когда пытается выразить свои чувства, и сомневается на каждом шагу."
    "Так и хочется сжать её в объятиях до хруста."
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "Mhhh!"
    "Сейчас я её успокою."
    hide grace with dissolve
    show grace hug with dissolve
    mc.c "Теперь я точно не уйду. Было бы жестоко."
    grace.c "Хе... Глупый..."
    hide grace with dissolve
    show grace kiss with dissolve
    "Она отвечает мне глубоким поцелуем."
    "Мы начинаем ласкать друг друга. Не могу дождаться."
    hide grace with dissolve
    show grace hug with dissolve
    grace.c "Давай..."
    scene black with fade
    "Она берёт меня за руку и ведёт в свою комнату."
    scene gracebedroom with fade
    show grace smile talk with dissolve
    grace.c "Мне это нужно..."
    show grace smile
    "Не теряя времени, она снимает одежду и предстаёт передо мной."
    scene gracehevent6i1 with fade
    pause
    "Какая перемена по сравнению с тем, что было недавно. Она больше не стесняется своей внешности рядом со мной."
    "Я только хотел, чтобы ей было комфортно со мной. Чтобы она чувствовала себя красивой и желанной..."
    "Тепло в её взгляде говорит больше любых слов. Рядом со мной она всё меньше себя сдерживает."
    "И, судя по кровати, она уже успела позабавиться."
    mc.c "Вижу, ты тут развлекалась без меня."
    "Я киваю на ноутбук и фаллоимитатор, которые даже не пытались спрятать."
    grace.c "А? О-ой... Э-э..."
    grace.c "Да... Н-но этого было мало..."
    grace.c "Я просто..."
    grace.c "Мне нужно по-настоящему... Ты~"
    mc.c "Даже не говори больше... Никогда раньше не чувствовал себя настолько нужным. Приятно."
    "Я начинаю раздеваться и подхожу к кровати. Грейс поворачивается, чтобы забраться на неё, и я замечаю кое-что неожиданное."
    scene gracehevent6i2 with fade
    "Вот это подарочек."
    mc.c "{b}*Кхм*{/b}. Это?.."
    grace.c "Eh?"
    "Она понимает, на что я смотрю, и её лицо вытягивается."
    grace.c "О-о, чёрт..."
    grace.c "Я... забыла, что... Дай мне..."
    mc.c "Погоди. Тебе нравится?"
    grace.c "А-а... Ну... Д-да, иногда... Когда я... Ты знаешь..."
    mc.c "Тогда оставь."
    grace.c "А-а... Эм..."
    "Она так смущена, что не знает, что думать. Почему бы и нет? Может быть интересно."
    mc.c "Не двигайся."
    image grace doggy part 1 = Movie(play="images/characters/grace/hscenes/doggy/part1.webm")
    show grace doggy part 1  with fade
    pause
    "Пока она ещё не успела забраться на кровать, я тянусь к её красивой киске."
    grace.c "О-ох~ [mc.name]~"
    "Она уже вся мокрая, внутри жарко. Успела позабавиться."
    "Ненасытная."
    "Тёплые влажные складки легко скользят по моим пальцам. Я двигаю ими, и Грейс вздрагивает."
    grace.c "А-а-а~ М-м-м~"
    mc.c "Просто разогреваю тебя."
    grace.c "Я... уже готова... ну же..."
    "Она не врёт. Я снимаю трусы и подхожу к её входу."
    image grace doggy part 2 = Movie(play="images/characters/grace/hscenes/doggy/part2.webm")
    show grace doggy part 2  with fade
    pause
    "Я уже не могу ждать, но ещё немного дразню её — провожу головкой члена по её губам, собирая влагу."
    "Такая горячая и готовая."
    grace.c "Давай же~ Хватит меня дразнить, трахни меня, дурак~"
    "Кажется, она и правда начинает терять терпение. Ей не терпится почувствовать мой член."
    "Я и так достаточно её дразнил. Сам уже не могу ждать."
    mc.c "Трахнуть тебя, дура или трахнуть тебя до потери рассудка?"
    grace.c "И ТАК, И ТАК!"
    "Ух ты, она и правда настроена решительно. Не нужно больше её разогревать."
    image grace doggy part 3 = Movie(play="images/characters/grace/hscenes/doggy/part3.webm")
    show grace doggy part 3  with fade
    pause
    "Я сразу вхожу глубоко и резко, врезаясь в скромную попку Грейс."
    grace.c "М-м-м~ О-ох~"
    grace.c "Д-да-а~ [mc.name]..."
    "Я легко вхожу и выхожу. Она так долго этого ждала. Ей это было нужно."
    "Я вхожу до упора, глубоко в её киску."
    grace.c "М-м-м~ Чёрт~ Да-а~"
    "Её плечи вздрагивают, когда я шлёпаю её по заднице. Её киска сжимается при каждом толчке."
    "Я крепко держу её за узкую талию, двигая ею, словно тряпичной куклой."
    grace.c "Ahnn~ Haaahh~"
    image grace doggy part 4 = Movie(play="images/characters/grace/hscenes/doggy/part4.webm")
    show grace doggy part 4  with fade
    pause
    "Меня интригует вид её блестящей пробки. Не знаю, как она влияет на ощущения."
    mc.c "Её мягкий мех шелестит под моими руками, а милые косички ложатся на узор её стройной спины."
    mc.c "Ты такая милая, Грейс."
    grace.c "М-м-м~ З-заткнись~"
    "Она вздрагивает, когда я вхожу чуть сильнее. Она легко принимает меня целиком."
    mc.c "Стало легче?"
    grace.c "М-м-м~ Нет... Мне нужно больше~"
    "Отлично. Я ещё не закончил."
    "Я прижимаю её грудью к кровати. Грейс выгибается, подставляя мне киску."
    image grace doggy part 5 = Movie(play="images/characters/grace/hscenes/doggy/part5.webm")
    show grace doggy part 5  with fade
    pause
    "Я вкладываю всю силу в толчки, жёстко трахая её попку."
    grace.c "О-О, ЧЁРТ, ДА-ДА-ДА~"
    grace.c "MMMhhhnnn~! AAhhhhhh~!"
    "Раздаются влажные шлепки, пока я глубоко вхожу в Грейс и выхожу из неё."
    "Крепко удерживая её, я наваливаюсь всем весом, вдавливая в кровать."
    grace.c "ЕЩЁ, ЕЩЁ~ СИЛЬНЕЕ, СИЛЬНЕЕ~"
    "Она кричит от удовольствия, теряя голову от желания и экстаза."
    grace.c "AHH~ AH~ MMMM~ MNNNHHH~"
    "Её киска и попка сжимаются при каждом толчке. Невероятно."
    image grace doggy part 6 = Movie(play="images/characters/grace/hscenes/doggy/part6.webm")
    show grace doggy part 6  with fade
    pause
    "Мы оба тяжело дышим, отдаваясь животной страсти."
    "Мы двигаемся вместе, как животные в течке. Я вот-вот взорвусь."
    grace.c "А-А-А~ [mc.name]~ Я КОНЧАЮ~!"
    "Она вздрагивает, а я крепко держу её за бёдра. Я тоже почти на пределе."
    mc.c "Я уже..."
    grace.c "М-м-м~ КОНЧИ В МЕНЯ~ ПОЖАЛУЙСТА~!"
    "Ещё несколько лихорадочных толчков — и я тоже на грани."
    image grace doggy end 1 = Image("images/characters/grace/hscenes/doggy/end1.webp")
    show grace doggy end 1 with fadewhite
    pause
    grace.c "AAAAAHHHHHHHH~~~~~"
    grace.c "MMMHNNNNNNN~~~"
    "Я резко вхожу, глубоко кончая в неё."
    "Её киска крепко сжимается, пока она вздрагивает от удовольствия."
    "Она сжимает меня, выжимая из меня всё до последней капли."
    image grace doggy end 2 = Image("images/characters/grace/hscenes/doggy/end2.webp")
    show grace doggy end 2 with fade
    pause
    "После бесконечного оргазма я выхожу, оставляя за собой горячий беспорядок."
    "Из Грейс вытекает сперма. Я наполнил её до краёв."
    "Она обмякает и неловко падает на кровать, приподняв бёдра."
    grace.c "*Haah* *Haah*"
    grace.c "Ohhhh~"
    grace.c "Боже мой~"
    "Она лежит без сил, остекленевшим взглядом уставившись в потолок."
    mc.c "Ты... в порядке?"
    grace.c "Чёрт~ Это было так хорошо~"
    mc.c "Ты довольна?"
    grace.c "Просто... *ха-а* дай мне минутку... Или пять..."
    "Грейс нужно время, чтобы прийти в себя и отдышаться."
    "Она выложилась по полной. Ну, точнее, заставила меня выложиться."
    "Вот же проказница. Может оказаться ненасытной..."
    image grace doggy end 3 = Image("images/characters/grace/hscenes/doggy/end3.webp")
    show grace doggy end 3 with fade
    pause
    call playMusic(chillTheme) from _call_playMusic_96
    "Наконец она переворачивается, немного придя в себя. Я ложусь рядом."
    grace.c "[mc.name]... Спасибо~"
    mc.c "Не надо благодарить меня за то, что я был с тобой, Грейс. Это мне повезло."
    grace.c "Ты не представляешь, как мне это было нужно."
    grace.c "Всё это."
    mc.c "Для тебя — когда угодно."
    scene black with fade
    "Я ложусь рядом, и мы какое-то время обнимаемся, постепенно приходя в себя."
    "Нам всё равно, что мы до сих пор перемазаны собственными соками. Я бы не хотел сейчас быть где-то ещё."
    "Жаль, что этот вечер не может длиться вечно. Но ночевать у Грейс, наверное, не лучшая идея."
    "Наконец мы всё же заставляем себя разойтись и... немного прибраться."
    scene gracebedroom with fade
    show grace smile with dissolve
    mc.c "Мне очень понравилось, хоть это и было не совсем свидание..."
    show grace smile talk
    grace.c "Мне тоже..."
    show grace thinking
    grace.c "Ты ведь не злишься, что я позвала тебя только ради этого?"
    mc.c "Я не против иногда получать приглашения на секс. Если на следующий день смогу зайти к тебе на работу."
    mc.c "Погоди, как-то странно прозвучало."
    show grace tease talk
    grace.c "Хе-хе-хе~"
    grace.c "Если ты это сделаешь, не уверена, что смогу себя сдержать..."
    show grace tease
    mc.c "Рискну."
    mc.c "Мне уже пора, вдруг твоя мама вернётся."
    show grace smile talk 2
    grace.c "Я бы хотела, чтобы ты остался, но понимаю."
    show grace smile
    mc.c "Скоро увидимся."
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "Mmm~"
    hide grace with dissolve
    show grace smile talk with dissolve
    grace.c "Пока, [mc.name]!"
    scene black with fade
    "Мы машем друг другу на прощание, и я выхожу."
    "Какой зверь мне достался. Мне так повезло."

    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.addLove(1)

    return {'location':location_town}

label graceHEvent7(fromGallery):
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_97
    "Выхожу из бара и иду домой через город быстрым шагом."
    "Обычно я думаю, чем займусь, когда приду: телевизор, игры, перекусить или эта ужасная бумажная работа?"
    "Но сегодня мне повезло: дома меня ждёт маленькая подруга. Вот это подарок."
    "Грейс осталась у меня на ночь, а сегодня у неё выходной, так что она весь день провела у меня. Я совсем не против."
    "Когда дома ждёт милая девушка, дорога становится чуточку приятнее."
    "Почти пришёл..."
    $ location_home.showBackground()
    mc.c "Я вернулся!"
    "У двери меня не встречают. Заглянув в комнату, вижу нашу зайку на кровати."
    scene gracehevent7i1 with fade
    pause
    "..."
    "Не совсем такое приветствие я представлял, но и это совсем неплохо."
    "Её милая попка направлена ко мне. На ней обычная одежда для безделья."
    "Ноутбук, телефон, закуски... Похоже, день проходит лениво."
    mc.c "Грейс?"
    grace.c "М-м... [mc.name]?"
    "Она звучит сонно."
    mc.c "Я вернулся. Прости, ты спала?"
    scene gracehevent7i2 with fade
    "Она неуклюже переворачивается, садится, потягивается и трёт глаза."
    grace.c "А-а... Да, я немного поспала..."
    grace.c "С возвращением... {b}*зевает*{/b}"
    "Я оглядываю небольшой беспорядок, который она успела устроить."
    mc.c "Чем занималась?"
    grace.c "Хм... Немного поиграла... Посмотрела кое-что..."
    grace.c "Хе-хе~ Съела твои вкусняшки..."
    mc.c "Они же для этого и лежат."
    scene gracehevent7i3 with fade
    pause
    grace.c "Хочу пить. Будешь? Кажется, осталось две колы."
    mc.c "Всего две? Утром же была целая куча."
    grace.c "Eheheh~"
    "Она самодовольно улыбается и, переваливаясь, проходит мимо. По полу тихо шлёпают её лапки."
    "Она всё ещё одета так же, как утром."
    mc.c "Ты даже не переоделась?"
    grace.c "А? Не-а, я же никуда не выходила..."
    mc.c "Вот лентяйка."
    grace.c "Да ла-а-адно, у меня выходной..."
    "На самом деле я не сержусь. Просто забавно её поддразнивать. Чего я ожидал — что меня встретит возлюбленная в фартуке с готовым домашним ужином? Это же Грейс."
    "Мечтать не вредно, но и так хорошо."
    "В конце концов, я могу любоваться её попкой..."
    grace.c "Как работа? Наверное, отстой."
    mc.c "..."
    grace.c "[mc.name]?"
    mc.c "О... Да, всё нормально..."
    "На секунду я засмотрелся. Уже начинаю..."
    "Достав банку из холодильника, Грейс проходит мимо и плюхается на кровать."
    scene gracehevent7i4 with fade
    pause
    grace.c "Повезло тебе, что ты начальник... Можешь делать что угодно..."
    grace.c "*Вздыхает* Не хочу завтра на работу..."
    "Маленькие трусики едва прикрывают её и без того скромную попку."
    "Такая милая, упругая попка..."
    "Я сажусь позади неё."
    mc.c "Дрочила, пока меня не было?"
    grace.c "Н-нет! [mc.name], какого чёрта..."
    mc.c "Не знаю, но для тебя вопрос вполне резонный. Вероятность была высокой."
    grace.c "Н-ну, не дрочила, ясно? Я..."
    mc.c "Ты что?"
    grace.c "Я... {size=20}думала об этом...{/size} Но не дрочила!"
    mc.c "Понятно. У меня тут нет пробки... Или ты захватила свою на ночь?"
    grace.c "[mc.name[0]]-[mc.name]! Ну перестань! Я же не всегда..."
    "Я уже видел эту анальную пробку в деле. Пару раз она даже оставляла её внутри. Говорит, ей приятно. Не то чтобы я понимал."
    "В последнее время я думаю: раз ей нравится что-то туда вставлять... Может, она захочет?.."
    call stopMusic from _call_stopMusic_18
    scene gracehevent7i5 with fade
    pause
    "Я слегка поглаживаю её попку."
    grace.c "О-ох... [mc.name], ты просто увиливаешь от ответа..."
    mc.c "Ну, после такого долгого и {i}изнурительного{/i} рабочего дня я подумал..."
    grace.c "Хе-хе~ {i}Может быть{/i}, меня можно уговорить... Особенно за бесплатную кровать..."
    "Я уже почти твёрдый, но сегодня хочется чего-то нового."
    mc.c "Но есть одно дело..."
    "Неловко спрашивать, но с Грейс, которая так открыта в вопросах секса, лучше сказать прямо."
    mc.c "Хочешь попробовать анал?"
    "Глаза Грейс на мгновение расширяются."
    grace.c "Т-ты..."
    mc.c "Ты когда-нибудь об этом думала?"
    grace.c "К-конечно... Просто... С тобой, наверное... может..."
    mc.c "Слишком большой? Я видел твои игрушки."
    grace.c "*Вздыхает* Да, видел... Но... не знаю..."
    mc.c "Не обязательно. Я просто подумал, что, может, тебе этого хочется."
    grace.c "..."
    call playMusic(sexyTheme) from _call_playMusic_98
    grace.c "Хочу..."
    "Этого приглашения достаточно. Я уже весь горю от нетерпения."
    scene black with fade
    "Немного подготовившись и переведя дух, Грейс собирается и принимает нужную позу."
    scene graceanalstart with fade
    pause
    "Она подставляет мне свою милую попку. Я буду первым, кто её лишит девственности. Словно открываю новую землю."
    mc.c "Ты точно уверена?"
    grace.c "Да~ Я всегда... этого хотела."
    mc.c "Сразу скажи, если будет слишком больно, Грейс."
    grace.c "С-сразу скажу... [mc.name]... Только сначала нежно, ладно?.."
    "Зрелище слишком соблазнительное. Я беру её за бёдра, подхожу к ней и начинаю входить."
    image grace anal part 1 = Movie(play="images/characters/grace/hscenes/anal/part1.webm")
    show grace anal part 1  with fade
    pause
    "Сопротивление очень сильное. Её анус туго сжимается и поддаётся лишь немного, когда я проникаю головкой."
    "К счастью, я настолько возбуждён, что твёрже уже некуда. Я осторожно вхожу на несколько сантиметров."
    grace.c "А-а... Ф-фу..."
    mc.c "Всё в порядке?"
    grace.c "Д-да... Приятно~"
    grace.c "Я никогда раньше не чувствовала там ничего... тёплого..."
    "Внутри очень туго и горячо. Постепенно Грейс расслабляется, но ощущения всё равно невероятные."
    "Её попка крепко сжимает меня. Чтобы войти глубже, нужно приложить усилие. Но это потрясающе."
    mc.c "Чёрт, Грейс, это невероятно."
    grace.c "П-правда?"
    mc.c "Тебе удобно? Можно глубже?"
    grace.c "Да~ Хорошо~"
    image grace anal part 2 = Movie(play="images/characters/grace/hscenes/anal/part2.webm")
    show grace anal part 2  with fade
    pause
    "Я обхватываю её за бёдра и проверяю, насколько глубоко смогу войти."
    "Чем глубже я вхожу, тем сильнее Грейс сперва напрягается, но когда смазка распределяется, член начинает скользить туда-сюда."
    grace.c "А-а-а~ М-м-м~"
    mc.c "Чёрт... Тебе приятно?"
    grace.c "Да~ Глубже~ Трахни меня в попку~"
    "Мой член безжалостно трахает милую попку Грейс."
    "Грейс опускает плечи, выгибая спину с каждым толчком."
    "Передо мной девушка, теряющаяся в ощущениях от моего члена."
    grace.c "Это... а-а-а... намного лучше~"
    mc.c "Попрощайся со своими игрушками."
    grace.c "Чёрт~ Ты заполняешь меня~"
    "Её анус полностью подстраивается под меня, крепко сжимает, но уже не так сильно сопротивляется."
    grace.c "Mhhhnnnn~"
    "Она тихо мычит от удовольствия. Похоже, одних этих ощущений хватает, чтобы её возбудить. Эти стоны... хочу увидеть её лицо."
    mc.c "Хочу видеть твоё лицо. Иди ко мне."
    image grace anal part 3 = Movie(play="images/characters/grace/hscenes/anal/part3.webm")
    show grace anal part 3  with fade
    pause
    "Я переворачиваю её на живот и начинаю двигаться так сильно, как осмеливаюсь. Её попка сжимает меня так крепко, что долго я не продержусь."
    grace.c "А-а-а~ [mc.name]~ [mc.name]~"
    grace.c "Чёрт~ Так хорошо~"
    "Её лицо искажено наслаждением, а попка и киска сжимаются с каждым толчком."
    "Она опускает руку и быстро трёт клитор. Она полностью отдалась сексуальному удовольствию."
    "Наши бёдра мокрые и горячие, и я чувствую, как её анус подёргивается вокруг меня."
    "Я проникаю как можно глубже и вижу, как Грейс теряет голову от экстаза. Я тоже уже не соображаю."
    mc.c "Грейс... Я скоро кончу."
    grace.c "К-кончи~ Кончи мне в попку~"
    grace.c "Кончи, кончи, кончи, кончи, я сейчас к-кончу~"
    "Грейс яростно трёт киску, а я довожу себя до оргазма."
    scene graceanalend1 with fadewhite
    pause
    grace.c "MMMMHHNNNNNnnnnnnn~~~~~"
    "Её попка крепко сжимается, вытягивая из меня всё до последней капли."
    "Я глубоко кончаю ей в анус, и сперма тут же начинает вытекать."
    "Грейс тоже бурно кончает, вскрикивая от удовольствия и заливая мои бёдра своими соками."
    grace.c "Ahhhh~ Haaaahhhh~ Haaaahhhh~"
    "Она вздрагивает от удовольствия, наконец расслабляется и отпускает меня."
    scene graceanalend2 with fade
    pause
    grace.c "Ahhhh~ Oohhhh~"
    grace.c "Чёрт~ [mc.name]~ Это было потрясающе~"
    mc.c "Это было... Ты такая тугая."
    "Сперма бесконечно вытекает из задницы Грейс и смешивается с её соками на кровати."
    "Грейс продолжает лежать, затуманенным взглядом наслаждаясь послевкусием."
    grace.c "М-м-м~ Как я теперь... смогу... повторить это..."
    mc.c "Похоже, придётся положиться на меня."
    grace.c "Mhnn~"
    scene black with fade
    "Через пару минут, когда мы немного приходим в себя, я помогаю ей привести себя в порядок."
    "Грейс всё ещё подкашиваются ноги, но она укладывается рядом со мной."
    scene gracepillowtalk with fade
    pause
    grace.c "Haah... Haah..."
    grace.c "Чёрт~ Я думала, уже привыкла, но... ощущения будто стали в десять раз сильнее..."
    grace.c "Чувство наполненности... В этом есть что-то невероятно приятное..."
    mc.c "Тебе и правда приятно?"
    grace.c "Д-да~"
    "Она слегка ёрзает на кровати."
    mc.c "Всё хорошо?"
    grace.c "Да~ Просто нужно немного времени, чтобы встать..."
    mc.c "Это чертовски заводит."
    grace.c "Хе-хе~ Наверное~"
    "Грейс ненадолго закрывает глаза, всё ещё переводя дух."
    "Вот же мы устроили беспорядок."
    scene black with fade
    "Немного отдохнув, Грейс, пошатываясь, идёт в душ. К сожалению, сегодня она не останется — завтра рано на работу."
    "Слышу, как Грейс заканчивает принимать душ."
    $ location_home.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_99
    show grace smile with dissolve
    mc.c "Жаль, что ты уходишь. Сможешь добраться домой?"
    show grace tease talk
    grace.c "Еле-еле... Хе-хе..."
    grace.c "Будто ты всё ещё внутри..."
    show grace tease
    mc.c "Не знаю, может, какая-то часть меня и правда ещё там."
    show grace tease talk
    grace.c "Боже мой~ Ну ты и сумасшедший..."
    show grace bashful talk
    grace.c "Я бы осталась, но уже сказала маме..."
    show grace bashful
    mc.c "Ладно. Только никому дома ничего не рассказывай, да?"
    show grace tease talk
    grace.c "Чёрт... Представляешь..."
    show grace tease
    "У двери я притягиваю Грейс к себе и целую."
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "М-м-м~"
    show grace hug with dissolve
    mc.c "Удачи завтра на работе."
    grace.c "Эх... Всё испортил..."
    scene black with fade
    "Я провожаю Грейс. Она уходит, слегка заметно пошатываясь."

    if(not fromGallery):
        $ grace.addLike(1)
        $ grace.addLove(1)

    return {'location':location_home}

label graceLikeEvent5Invitation(fromGallery):
    call playMusic(heartTheme) from _call_playMusic_100
    show grace smile
    "Я безумно люблю Грейс."
    "И очень ею горжусь. Она вырвалась из затворничества и начала жить полной жизнью."
    "Она не бросила работу, стала общительнее, открылась мне и, похоже, снова начала заводить друзей."
    "Остался, пожалуй, ещё один важный шаг во взрослую жизнь: она всё ещё живёт с мамой."
    "Она любит маму, это я знаю. Та уже не просто {i}догадывается{/i} о наших отношениях, и мы неплохо ладим."
    "Но у совместной жизни есть и свои минусы: контроль, мало личного пространства и свободы, когда пора покинуть родительский дом."
    "Я съехал из дома при первой же возможности. Не то чтобы дома было плохо, но... мне хотелось жить своей жизнью."
    "Не могу не думать, готова ли Грейс наконец к этому шагу."
    "Я бы хотел помочь ей, если она сама этого хочет. Может, она согласится переехать ко мне?"
    "Она не будет совсем одна. Это не полная самостоятельность... но мы могли бы жить вместе."
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Да!' if(homeHasRoom) else "Нужно улучшить дом" 
    if(not fromGallery):
        menu:
            "Предложить Грейс переехать ко мне? Этот выбор можно сделать в любой момент."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "Не сейчас":
                call endCharacterInteraction(grace) from _call_endCharacterInteraction_1
    mc.c "Грейс."
    show grace smile talk 2
    grace.c "Да?"
    mc.c "Как дела с зарплатой? Тебе повысили?"
    show grace thinking
    grace.c "Да... Но после налогов и всего остального почти ничего не изменилось."
    mc.c "Вот это ты теперь настоящий налогоплательщик. Вполне взрослый человек."
    show grace tease talk
    grace.c "Хе-хе~ Заткнись. Лучше бы не была..."
    show grace tease
    mc.c "Я тобой горжусь. Ты так хорошо держишься и не бросаешь работу."
    hide grace with dissolve
    show grace pat animated with dissolve
    "Я протягиваю руку и глажу её по голове."
    grace.c "Хе-хе~ Перестань... Э-это ничего..."
    mc.c "Какая взрослая~"
    grace.c "...Дурак."
    hide grace with dissolve
    show grace smile with dissolve
    "Она отводит мою руку."
    mc.c "И всё же, тебе дома по-прежнему хорошо?"
    show grace neutral talk
    grace.c "Д-да? А почему нет?"
    mc.c "Ты зарабатываешь, у тебя своя жизнь... Я подумал, может, ты уже задумывалась о том, чтобы съехать."
    grace.c "С-съехать?.."
    mc.c "Не знаю, вдруг тебе этого хочется? Думала об этом?"
    show grace thinking
    grace.c "Хм... Ну, немного..."
    show grace neutral talk
    grace.c "Ты видел цены на аренду? Я и не знала..."
    show grace thinking
    grace.c "Надо было бы брать больше смен... Я ещё не всё посчитала, но, наверное, пришлось бы почти на полный день переходить..."
    mc.c "Не дай бог."
    show grace smile talk
    grace.c "Хе-х~ Замолчи... Да и не думаю, что у меня там вообще есть такая возможность. Только неполная занятость."
    show grace thinking
    grace.c "Придётся искать что-то новое... Я не..."
    "Понятно. Это серьёзный шаг. Примерно такого ответа я и ожидал."
    "Поэтому хочу предложить то, чего {i}сам на самом деле{/i} хочу."
    mc.c "Но если бы ты могла оставить всё как есть, ты бы хотела съехать?"
    show grace neutral
    grace.c "Хм..."
    show grace bashful talk
    grace.c "Я... хотела бы."
    grace.c "То есть... Я бы скучала по маме. Я ведь никогда не жила отдельно..."
    show grace neutral talk
    grace.c "Но я правда думаю о том, чтобы жить в другом месте... Иметь свой дом. Свои пространство и время. Делать что хочу и ни перед кем не отчитываться..."
    show grace bashful talk
    grace.c "Но мне было бы жаль маму... Не хочу, чтобы ей было одиноко."
    grace.c "Наверное, если бы я жила... неподалёку..."
    show grace bashful
    "Неподалёку... Это важно. На самом деле мы и так живём довольно близко. Многое не изменится."
    "Возможно, это сработает."
    mc.c "Ты бы согласилась переехать ко мне?"
    show grace neutral talk
    grace.c "А?.."
    show grace surprise
    grace.c "А?!"
    grace.c "Т-ты... Правда это предлагаешь?"
    mc.c "Да. Я хочу жить вместе."
    grace.c "Ты серьёзно?! Н-но..."
    mc.c "Абсолютно. Я люблю тебя, Грейс. Хочу быть с тобой."
    mc.c "Ты и так почти живёшь у меня. Мне нравится, когда ты приходишь."
    mc.c "Почему бы не сделать это по-настоящему? Пусть это будет {i}наш{/i} дом. Я хочу, чтобы ты тоже считала его своим."
    grace.c "Я..."
    show grace joy
    grace.c "Д-да! Хочу!"
    grace.c "Боже мой, боже мой, да!"
    hide grace with dissolve
    show grace hug with dissolve
    mc.c "Ох, как я рад. Не знал, согласишься ли ты..."
    grace.c "Конечно! Я просто не была уверена... Но... у нас получится?"
    mc.c "Мы справимся, Грейс. Спасибо..."
    show grace kiss with dissolve
    grace.c "Mhn~"
    show grace hug with dissolve
    grace.c "Хе-хе~ Не верится..."
    mc.c "Понимаю, это не совсем будет твой отдельный дом..."
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Как ты знаешь, [len(girlsAlreadyMovedIn)] других девушек уже почти переехали, но, возможно, ты ещё не со всеми познакомилась..."
        if(jessica.movedIn and graceJessicaDuoStoryEvent1.unlocked):
            mc.c "Ты ведь нормально ладишь с Джессикой?"
            grace.c "Угу! Она очень добрая ко мне..."
        if(molly.movedIn and graceMollyDuoStoryEvent1.unlocked):
            mc.c "Ну, Молли ты уже знаешь."
            grace.c "Ага, она классная!"
        mc.c "Тебя это устраивает?"
        grace.c "Да-да! Я знаю, и меня всё устраивает!"
    hide grace with dissolve
    show grace smile talk with dissolve
    grace.c "Поговорю с мамой... Она, наверное, удивится, но... Если честно..."
    show grace tease talk
    grace.c "Она сама спрашивала, почему мы до сих пор не живём вместе~ Хе-хе~"
    show grace tease
    mc.c "Ну и мама..."
    mc.c "И ты всё равно будешь недалеко от неё. Сможешь сбежать обратно, если я начну тебя раздражать."
    show grace tease talk
    grace.c "Хе-хе~ Ты и правда умеешь раздражать~"
    show grace tease
    mc.c "Ну что... Заберём твои вещи? Когда захочешь."
    show grace smile talk 2
    grace.c "Я всё обсужу с мамой и разберусь..."
    grace.c "Да и вещей у меня немного... Часть одежды уже у тебя..."
    show grace joy
    grace.c "Хе-хе~ Не могу дождаться!"
    mc.c "Не торопись. Всё обсудим. Когда будешь готова, я помогу."
    scene black with fade
    "Вот и всё. Она согласилась!"
    "Мы выбрали удобный день. Я помогу перевезти вещи — и с этого момента... она дома."
    "Договорились. Загляни в расписание!"

    return

label graceLikeEvent5(fromGallery):
    call playMusic(memoriesTheme) from _call_playMusic_101
    $ location_home.showBackground()
    "Сегодня Грейс наконец переезжает ко мне."
    "Не слишком ли долго мы к этому шли? Или всё случилось вовремя? Как бы то ни было, я не могу дождаться, когда она будет здесь..."
    "Я сказал, что сегодня приеду помочь забрать вещи. Ещё рано, поэтому подожду, чтобы она успела проснуться и собраться."
    scene black with fade
    "Чуть позже я пишу ей, чтобы узнать, можно ли заехать."
    "Она почти готова, так что я отправляюсь к ней."
    scene suburbs with fade
    "Я подъезжаю к её дому. Не знаю, сколько вещей она собирается взять, поэтому решил приехать на машине."
    "Вот и всё... Я приехал забрать свою девушку к себе домой."
    "Словно увожу её с собой... Интересно, как её мама это воспримет? Может, будет гордиться? Или загрустит, что её дочурка уезжает..."
    "Я звоню в дверь."
    "..."
    show grace joy with dissolve
    grace.c "[mc.name]!"
    hide grace with dissolve
    show grace kiss with dissolve
    grace.c "Чмок~"
    show grace hug with dissolve
    mc.c "Привет, Грейс. Как продвигается?"
    grace.c "Нормально, всего несколько сумок... Если что-то забыла, потом ещё заберу."
    mc.c "Ладно. Ещё помочь?"
    grace.c "Не, всё нормально. Заходи."
    scene gracehomehall with fade
    "У входной двери стоит пара сумок, набитых разной мелочёвкой."
    show grace smile talk with dissolve
    grace.c "Поднимайся, последняя сумка в моей комнате."
    show grace smile
    mc.c "Мамы нет?"
    show grace smile talk 2
    grace.c "Нет, она недавно ушла на работу."
    show grace smile
    mc.c "Ничего, что мы не попрощаемся?"
    show grace smile talk 2
    grace.c "Мы попрощались утром. Она даже сказала, что не хочет нам мешать. Это наш момент."
    grace.c "И, как ты сказал... Мы ведь недалеко. Ничего страшного."
    show grace smile
    mc.c "Для неё это всё равно важное событие. Её маленькая девочка покидает родительский дом."
    show grace bashful talk
    grace.c "Да... Она... Мы... Немного поплакали, когда говорили об этом."
    show grace smile talk 2
    grace.c "Но она правда рада. И я рада."
    show grace smile
    mc.c "А я на седьмом небе от счастья. Не могу дождаться. Давай помогу."
    scene black with fade
    "Мы забираем последние сумки, доверху набитые играми... Загружаем их в машину и едем... {i}домой{/i}."
    "Заходим внутрь, заносим последние сумки... Вот мы и дома."
    scene gracelikeevent5i1 with fade
    pause
    grace.c "Мы и правда это сделали... Теперь я здесь..."
    mc.c "Это и твой дом."
    grace.c "Я... пока не могу в это поверить."
    grace.c "Никогда не думала... что такое случится."
    mc.c "Вот это приключение, да? Ты была одной из первых, с кем я познакомился после переезда."
    grace.c "А ты — первый человек, с которым я по-настоящему поговорила..."
    grace.c "Хе-хе~ Сначала ты меня ужасно напугал... Просто подошёл и заговорил."
    mc.c "Ты и не очень-то шла на контакт. Я решил попробовать, но думал, что, возможно, перегнул палку."
    grace.c "М-м... Но я рада. Спасибо... Что не бросил меня, даже когда я была... ну, ты знаешь."
    mc.c "Спасибо, что открыла мне своё сердце."
    scene gracelikeevent5i2 with fade
    pause
    "Мы крепко обнимаемся. Я наклоняюсь, чтобы поцеловать её милое личико."
    "Её усики дрожат, когда мы прижимаемся друг к другу."
    mc.c "Я люблю тебя, Грейс."
    grace.c "И я тебя люблю~"
    scene gracelikeevent5i3 with fade
    pause
    "Мы отстраняемся, но остаёмся в объятиях и молча оглядываем комнату. Начинается наша новая совместная жизнь."
    grace.c "Э-э... И... Что мне теперь делать?"
    mc.c "Ха-ха! В каком смысле?"
    grace.c "Не знаю... Теперь, когда я здесь... Странное чувство. Не понимаю, чем себя занять..."
    mc.c "Грейс, ты уже столько раз здесь бездельничала, будто это твой дом. Делай что хочешь."
    grace.c "Хе-хе~ Знаю... Просто теперь всё по-настоящему..."
    grace.c "Ну, может, я и хотела кое-что сделать... Раз уж мы теперь живём вместе..."
    mc.c "О-о, и что же?"
    grace.c "Э-э... Это сюрприз, но... Мне нужна твоя кухня."
    mc.c "Только не говори, что собралась готовить."
    grace.c "П-почему нет? Надо же мне научиться, да?"
    mc.c "Ой, да я шучу. Конечно, готовь!"
    grace.c "Теперь уже не уверена..."
    mc.c "Ну пожа-а-алуйста~ Для меня это будет лучшим подарком."
    grace.c "Хмф..."
    scene black with fade
    "Я показываю Грейс, где что лежит на кухне, а она выставляет меня за дверь."
    grace.c "Не подглядывай!"
    "Слышу, как звенят приборы и посуда, а ещё, кажется, играет что-то с её телефона."
    grace.c "{size=20}Что за... Как? Назад...{/size}"
    "..."
    grace.c "Э-э?.. Чёрт..."
    "Интересно, что это? Её первый домашний ужин?"
    grace.c "{size=20}Так правильно?..{/size}"
    grace.c "Э-э, [mc.name]? Кажется, всё готово... М-можешь зайти..."
    "Ох..."
    scene gracelikeevent5i4 with fade
    pause
    "Когда я возвращаюсь на кухню, вижу небольшой беспорядок на столешнице."
    "Грейс переминается с ноги на ногу и предлагает мне сесть."
    grace.c "Надеюсь, получилось..."
    mc.c "Уверен, всё хорошо. Что ты приготовила?"
    scene gracelikeevent5i5 with fade
    pause
    "Грейс достаёт из-за спины тарелку."
    "Похоже на... омлет? В середине он вздулся, сверху... кетчуп?"
    grace.c "В-вот... Д-дорогой..."
    "Звучит, будто она заранее репетировала эту милую фразу, но произносит её с привычной неуверенностью."
    "И «дорогой»? Я в полном восторге, даже рот раскрыл."
    grace.c "{size=20}О боже...{/size}"
    mc.c "Грейс, выглядит отлично! Это омурайсу, да?"
    grace.c "Хе-хе~ По крайней мере, похоже."
    mc.c "Я так и думал! Классика. Не могу дождаться, чтобы попробовать."
    grace.c "Надеюсь, тебе понравится..."
    mc.c "Ты приготовила только для меня?"
    grace.c "Яиц, кажется, хватало только на одну порцию..."
    mc.c "Разделим пополам."
    scene gracelikeevent5i6 with fade
    pause
    "Это маленькое сердечко сверху... Жалко даже портить его, съедая."
    "Пробую — на самом деле очень вкусно. А то, что приготовлено с любовью, делает его ещё лучше."
    mc.c "Правда вкусно, Грейс! Я знал, что у тебя получится!"
    grace.c "Хм... А ведь и правда неплохо."
    mc.c "Хорошая работа, {i}дорогая~{/i}"
    grace.c "Ой... «Дорогая» — это уже слишком?"
    mc.c "Вовсе нет! Мне нравится."
    grace.c "Э-э... Не знаю... Ничего не обещаю..."
    scene black with fade
    "Мы заканчиваем наш особенный ужин и вместе убираем."
    scene gracelikeevent5i7 with fade
    pause
    "Позже, немного разобрав вещи, мы устраиваемся на диване, обнявшись."
    "Мы и раньше так проводили время, но теперь она останется на ночь и будет рядом утром — и снова, и снова..."
    "Не могу дождаться, как будет складываться наша жизнь. Я ещё никогда не чувствовал себя к ней так близко."
    mc.c "Я так рад, что ты здесь, Грейс. Люблю тебя."
    grace.c "И я тебя люблю, {i}дорогой~{/i}"
    scene black with Fade(1.5, 0.0, 0.0)

    if(not fromGallery):
        $ grace.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label graceHEvent8(fromGallery):
    call playMusic(funnyTheme) from _call_playMusic_102
    scene graceshowerapproach with fade
    pause
    "Мне показалось, что я слышу бегущую воду... Дверь приоткрыта, и звук хорошо доносится."
    "Я заглядываю за угол и вижу Грейс в душе."
    "Я не просто заглядываю, а захожу внутрь. Она закрыла глаза и отвернулась, поэтому не замечает меня."
    "Её милая упругая попка покачивается, пока она моется... Ну и ну."
    "Может, ей не помешает компания..."
    image grace shower caressing = Movie(play="images/characters/grace/hscenes/shower/caressing.webm")
    show grace shower caressing with fade
    pause
    "Я раздеваюсь, захожу в душ и ласкаю её сзади."
    grace.c "А-а! [mc.name]?"
    mc.c "Дверь была открыта. Моя милая грязнуля-затворница наконец моется?"
    grace.c "Ч-что? Я не затворница... И от меня ведь не пахнет, д-да?"
    "Я просто дразню. Стоит понюхать её прекрасные волосы — и сомнений не остаётся."
    mc.c "Как всегда, пахнут цветами."
    grace.c "Дурак..."
    grace.c "Хм... Кто разрешил тебе войти?"
    mc.c "Могу уйти, если хочешь."
    "Грейс прижимается ко мне спиной, пока я глажу её по боку."
    grace.c "Да ладно... Это же твой дом, извращенец."
    mc.c "{i}Наш{/i} дом. Не забывай."
    grace.c "Хм~ Ага~"
    mc.c "Всё хорошо? Я ещё не достал тебя настолько, чтобы ты убежала?"
    grace.c "Хе-хе~ Почти, но нет... Здесь так хорошо."
    grace.c "Я... люблю этот дом."
    mc.c "А я люблю, когда ты здесь. Я люблю тебя."
    grace.c "И я тебя люблю..."
    "Я обхожу её и беру в руку упругую грудь, проводя пальцами по мокрому меху."
    grace.c "М-м~ Ну же, [mc.name]~"
    mc.c "Надо же тебя вымыть, верно? Просто помогаю."
    grace.c "Господи..."
    "В конце концов, как и следовало ожидать, я не выдерживаю. Мой член трётся о её пушистый хвост."
    grace.c "[mc.name]..."
    call playMusic(sexyTheme) from _call_playMusic_103
    grace.c "Я чувствую тебя~"
    "Она нарочно прижимает попку ко мне и возбуждает меня."
    grace.c "Хочешь, чтобы я...?"
    mc.c "В чём бы ни был вопрос, я наверняка хочу..."
    grace.c "Хе-хе~"
    image grace shower blowjob 1 = Movie(play="images/characters/grace/hscenes/shower/blowjob1.webm")
    show grace shower blowjob 1  with fade
    pause
    "Она поворачивается и опускается на колени, беря мой член в руку."
    "Она лижет его снизу, поглядывая на меня озорными глазами."
    grace.c "Mhnn~ Hhmmm~ Mwaah~"
    grace.c "Уже такой твёрдый..."
    mc.c "Теперь ты всё время рядом, так что мне будет трудно себя сдерживать..."
    grace.c "Хе-хе~ Если так..."
    grace.c "Тогда не сдерживайся~"
    "Если это не возбудит, то уже ничто не поможет."
    "Она хихикает, проводя языком по всей длине члена. Влажный шершавый язык слегка щекочет."
    "Капли из душа только усиливают ощущения — она быстро доводит меня до предела."
    mc.c "Ох, чёрт..."
    grace.c "Eheh~"
    grace.c "Посмотрим, как долго ты продержишься~"
    image grace shower blowjob 2 = Movie(play="images/characters/grace/hscenes/shower/blowjob2.webm")
    show grace shower blowjob 2  with fade
    pause
    "Она обхватывает меня за талию и начинает очень быстро и напористо двигать головой вверх-вниз."
    mc.c "Она обхватывает меня за талию и начинает быстро и напористо двигать головой вверх-вниз."
    grace.c "Mhnn~ Ahmm~ Mhnnn~ Mhhhff~"
    "Она смотрит на меня заигрывающим взглядом, будто ей самой немного нравится то, что она делает."
    grace.c "Mhn Hmhnn~"
    "Я кладу руку ей на голову, направляя её движения, и чешу основание висячего уха."
    "В душе раздаются непристойные звуки: влажные шлепки её губ, скользящих по моему члену."
    "Её язык танцует и дразнит нижнюю часть головки, умело лаская самые чувствительные места."
    mc.c "Боже, чёрт..."
    "Я замечаю, как она улыбается, поняв, что я уже близко."
    mc.c "Грейс, я..."
    scene graceshowerblowjobfinish with fadewhite
    pause
    "Когда я кончаю, Грейс с громким чмоканьем отстраняется от моего члена."
    mc.c "О-о-ох~!"
    "Из моего подёргивающегося члена ей на лицо брызгает огромная порция спермы."
    grace.c "Ха-а~ Ха-а~"
    "Сперма стекает по её лицу и щекам, а она хихикает, любуясь результатом."
    grace.c "Хе-хе~ Как быстро~"
    "Она смеётся, но, чёрт, была права. Она быстро меня довела."
    mc.c "Боже, чёрт..."
    "Сперма медленно смывается в душе, но Грейс не торопится умываться."
    grace.c "Я думала, секс в душе бывает только в кино. Кажется, теперь понимаю~"
    mc.c "Похоже, у нас дома это вполне реально."
    grace.c "Хе-хе~"
    scene black with fade
    "Я ласкаю свой член, а Грейс встаёт и вытирается."
    "На этот раз мы наконец нормально заканчиваем принимать душ."

    if(not fromGallery):
        $ grace.addLove(1)
     
    return
