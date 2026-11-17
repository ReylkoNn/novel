init offset = 3
init python:
    def adjust_molly_attributes(image_name):
        tag = image_name[0]
        attributes = list(image_name[1:])

        if (not inEventReplay and molly.movedIn and dayOfWeek in ["Saturday", "Sunday"]
            and "casual" not in attributes
            and "nude" not in attributes # bathroom nude
            and "sex" not in attributes): # sex animations
            attributes.insert(0, "casual")

        return (tag,) + tuple(attributes)

    config.adjust_attributes["molly"] = adjust_molly_attributes

default molly = Person(Character(name='Molly', who_color='#3d1922', image = 'molly'), 'Molly', '', 'molly', 'female', 26)

label initialiseCharacter_molly:
    python:
        molly.currentLocation = location_away
        location_away.occupants.extend([molly])
        molly.availableEvents = [mollyFirstMeetingEvent]

    return

label updateCharacterStatics_molly:
    python:
        # Personal attributes
        molly.species = 'Kodiak Bear'
        molly.birthday = 1
        molly.job = 'Paralegal'
        molly.giftLoves = [item_flowers, item_goldRing]
        molly.giftLikes = [item_candles, item_dress]
        molly.giftHates = []

        # Skill attributes

        # Sexual attributes
        molly.virgin = False

        # Personal effects

        # Event attributes
        molly.events = [mollyFirstMeetingEvent, mollyLikeEvent1, mollyLikeEvent2, mollyLikeEvent3, mollyHEvent1, mollyHEvent2, mollyHEvent3, mollyHEvent4, mollyHEvent5, mollyHEvent6, mollyVacation, mollyLikeEvent4, mollyHEvent7]
        molly.specialEvents = [katieMollyDuoStoryEvent1, katieMollyDuoHEvent1, katieMollyDuoHEvent2, graceMollyDuoStoryEvent1, graceMollyDuoHEvent1]
        molly.selfieOptions = ['office1', 'hotel1', 'hotel2', 'hotel3', 'homebedroom1']
        molly.wakeUpOptions = ['legjob', 'blowjob']
        molly.dateChats = ['Background', 'Job', 'Hobbies']
        molly.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = molly.events[-1]
        molly.maxLike = lastStoryEvent.requiredLike
        molly.maxLove = lastStoryEvent.requiredLove

        # World attributes
        molly.preferredMondaySchedule = [location_offices, location_offices, location_offices, location_away]
        molly.preferredTuesdaySchedule = [location_offices, location_town, location_park, location_away]
        molly.preferredWednesdaySchedule = [location_offices, location_offices, location_diner, location_town]
        molly.preferredThursdaySchedule = [location_offices, location_cafe, location_offices, location_away]
        molly.preferredFridaySchedule = [location_offices, location_offices, location_bar, location_bar]
        molly.preferredSaturdaySchedule = [location_cafe, location_away, location_away, location_away]
        molly.preferredSundaySchedule = [location_away, location_away, location_away, location_away]

        molly.preferredMovedInMondaySchedule = [location_home, location_offices, location_home, location_home]
        molly.preferredMovedInTuesdaySchedule = [location_home, location_offices, location_home, location_home]
        molly.preferredMovedInWednesdaySchedule = [location_offices, location_cafe, location_home, location_home]
        molly.preferredMovedInThursdaySchedule = [location_home, location_offices, location_offices, location_home]
        molly.preferredMovedInFridaySchedule = [location_offices, location_offices, location_bar, location_home]
        molly.preferredMovedInSaturdaySchedule = [location_home, location_home, location_home, location_home]
        molly.preferredMovedInSundaySchedule = [location_home, location_home, location_home, location_home]
    return

# Sprites
screen mollyClickable(xcenter):
    if(molly.movedIn and dayOfWeek in ["Saturday", "Sunday"]):
        $ spriteload = molly.apiName + ' casual ' + ' neutral'
    else:
        $ spriteload = molly.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = molly)
        at characterSpriteHover

# Character methods
label mollyEvaluateAvailableInteractions:
    python:
        if molly.like >= 5 and mollyLikeEvent2.unlocked:
            molly.availableActions = list(set(molly.availableActions + ['Spend time']))
        if mollyHEvent2.unlocked:
            molly.availableActions = list(set(molly.availableActions + ['Invite over']))

        if molly.isDateable and molly.love >= 1:
            molly.availableActions = list(set(molly.availableActions + ['Date']))
        if molly.love >= 1 and mollyHEvent1.unlocked:
            molly.availableActions = list(set(molly.availableActions + ['Affection']))
            molly.availableAffections.extend(['Pat'])
        if molly.love >= 1 and mollyHEvent1.unlocked:
            molly.availableAffections.extend(['Chin Scratch'])
        if molly.love >= 1 and mollyLikeEvent3.unlocked:
            molly.availableAffections.extend(['Hug'])
        if molly.love >= 1 and mollyLikeEvent3.unlocked:
            molly.availableAffections.extend(['Kiss'])
        if mollyHEvent3.unlocked:
            molly.availableAffections.extend(['Caress Butt'])
        if mollyHEvent5.unlocked:
            molly.availableAffections.extend(['Boob Grab'])
        if mollyHEvent7.unlocked:
            molly.availableActions.extend([{'homelounge': ['Nursing Handjob']}])
        if molly.movedIn:
            molly.availableCommandsPrivate.extend(['Show Panties'])
            molly.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label mollyChat:
    show molly smile talk
    return

label mollyChat_beach:
    show molly smile talk
    molly.c "Фух, свежий воздух..."
    show molly mad talk
    molly.c "Да ну, кто опять мне звонит..."
    return

label mollyChat_park:
    show molly sad
    molly.c "Фух... Надо немного посидеть..."
    molly.c "Можем поговорить, только... дай секунду глаза закрою..."
    return

label mollyChat_shop:
    show molly neutral talk
    molly.c "Просто куплю несколько баночных кофейных напитков. Сегодня будет долгий день."
    return

label mollyChat_diner:
    show molly smile talk 2
    molly.c "Слава богу, здесь такие большие порции."
    show molly bashful talk
    molly.c "Ой, э-э, я не всегда так ем... Ах..."
    return

label mollyChat_cafe:
    show molly bashful talk
    molly.c "Только никому не говори, но я иногда прихожу сюда просто сбежать из офиса."
    show molly smile talk
    molly.c "К тому же кофе тут лучше."
    return

label mollyChat_town:
    show molly thinking
    molly.c "Из одного офиса в другой, весь день в бегах..."
    show molly surprise
    molly.c "Ой, прости, мне надо ответить. Наверное, звонят по важному делу."
    return

label mollyChat_bar:
    show molly smile talk 2
    molly.c "Красного вина, пожалуйста, [mc.name]. Надо расслабиться после такого дня."
    return

label mollyChat_aquarium:
    show molly smile talk 2
    molly.c "Когда застреваю в городе, приятно приходить в такие места."
    show molly thinking
    molly.c "Если бы только у меня было больше времени..."
    return

label mollyChat_theater:
    show molly smile talk
    molly.c "Рядом с домом моих родителей нет театра, так что надо пользоваться возможностью, пока могу."
    show molly smile talk 2
    molly.c "А ты? На что собирался пойти?"
    return

label mollyChat_homebedroom:
    if(timeOfDay == 'Morning'):
        if(dayOfWeek in ['Saturday', 'Sunday']):
            show tease talk
            molly.c "М-м~ Доброе утро~ Может, сегодня просто поваляемся?"
        else:
            show molly smile talk
            molly.c "Доброе утро! Прости, мне скоро надо бежать."
    elif(timeOfDay == 'Afternoon'):
        show molly smile talk 2
        molly.c "Хорошо, что сегодня не работаю. Хочешь чем-нибудь заняться?"
    elif(timeOfDay == 'Evening'):
        show molly bashful talk
        molly.c "Фух~ Целый день на ногах в этих туфлях..."
    elif(timeOfDay == 'Night'):
        show molly tease talk
        molly.c "*Зевает*~ День выдался долгим... Скоро спать?"
    return

label mollyChat_homelounge:
    if(timeOfDay == 'Morning'):
        show molly tease talk
        molly.c "Попалась, хе-хе~ Просто хотела посмотреть сериалы."
    elif(timeOfDay == 'Afternoon'):
        show molly smile talk 2
        molly.c "Хочешь что-нибудь посмотреть? Только не страшное..."
    elif(timeOfDay == 'Evening'):
        show molly tease talk
        molly.c "Хочу посмотреть фильм. Обнимемся?"
    elif(timeOfDay == 'Night'):
        show molly tease talk
        molly.c "О, уже стемнело, я потеряла счёт времени. Пойдём спать?"
    return

label mollyChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show molly surprise
        molly.c "Это мой завтрак? Эй, не так уж много..."
    elif(timeOfDay == 'Afternoon'):
        show molly thinking
        molly.c "Что бы съесть, что бы съесть..."
    elif(timeOfDay == 'Evening'):
        show molly tease talk
        molly.c "О-о, выглядит вкусно~ Можно кусочек?"
    elif(timeOfDay == 'Night'):
        show molly bashful talk
        molly.c "Ой, я просто... Хотела немного перекусить..."
    return

label mollyInteractionBathroom:
    katie.c "[mc.name]! Что ты такое?.."
    katie.c "Хм... Ты просто будешь смотреть~?"
    return

label mollySpendTime(onDate):
    if(onDate):
        scene expression 'molly[mc.currentLocation.apiName]date'
    else:
        scene expression 'molly[mc.currentLocation.apiName]'
    with fade
    return

label mollyReceiveGift(item, likeChange, loveChange):
    show molly neutral talk
    molly.c "О? Правда? Это мне?"
    if(loveChange > 0):
        show molly surprise
        molly.c "А-а! Ничего себе."
        show molly joy
        molly.c "Ой, не верится! Спасибо!"
        if(mollyVacation.unlocked):
            molly.c "Я люблю тебя, [mc.name]!"
    elif(likeChange > 1):
        show molly tease talk
        molly.c "Ой, большое спасибо, [mc.name]!"
    elif(likeChange < 1):
        show molly thinking
        molly.c "Э-э... хм... {b}*Кхм*{b}"
    else:
        show molly smile talk 2
        molly.c "Как мило! Спасибо!"
    return

label mollyReceiveDateInvitation:
    show molly thinking
    molly.c "Я бы очень хотела, но... Когда ты собирался?"
    call dateInvitationSelector(molly) from _call_dateInvitationSelector_5
    show molly tease talk
    molly.c "[proposedDateDayOfWeek], [proposedDateTime]? О, отлично! Я смогу. Увидимся там!"

    python:
        scheduledDate = Date(molly, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        molly.scheduledDates.append(scheduledDate)
    return

label mollyStartDate:
    if(mc.currentLocation == location_home):
        show molly tease with dissolve
        molly.c "П-привет, [mc.name]~"
    else:
        show molly smile talk with dissolve
        molly.c "Привет! Спасибо, что пришёл!"
    return

label mollyDateInteraction:
    show molly smile with dissolve
    show screen dateUi(molly) with dissolve
    call screen dateInteractionScreen(molly, mc.currentLocation)

label mollyChatDate:
    show molly smile talk 2
    molly.c "Как же хорошо. Мне редко удаётся так отдохнуть."
    return

label mollyChatDate_beach:
    show molly joy
    molly.c "Лучше не бывает!"
    show molly smile talk 2
    molly.c "Если бы я здесь жила, проводила бы на берегу каждые выходные!"
    return

label mollyChatDate_park:
    show molly smile talk 2
    molly.c "Ой, расскажу тебе, что сегодня случилось в офисе."
    show molly bashful talk
    molly.c "Хотя нет, прости, лучше не буду. Надо отвлечься от работы."
    return

label mollyChatDate_diner:
    show molly smile talk
    molly.c "Так приятно. Обычно, когда я здесь, приходится есть одной."
    show molly tease talk
    molly.c "Так что спасибо, [mc.name]."
    return

label mollyChatDate_cafe:
    show molly smile talk 2
    molly.c "Не волнуйся, телефон на беззвучном."
    show molly tease talk
    molly.c "Ничего не отвлечёт нас~"
    return

label mollyChatDate_bar:
    show molly tease talk
    molly.c "Сегодня я бы выпила. Неделя выдалась тяжёлая."
    show molly smile talk 2
    molly.c "Только немного, вдруг утром позвонят по работе."
    return

label mollyChatDate_aquarium:
    show molly joy
    molly.c "Хи-хи! Посмотри на них!"
    show molly tease talk
    molly.c "Какие же милые!"
    return

label mollyChatDate_theater:
    show molly tease talk
    molly.c "Ой, как здорово, спасибо, [mc.name]!"
    show molly smile talk 2
    molly.c "Тогда я куплю нам попкорн, договорились?"
    return

# Date topics
label mollyChat_background:
    mc.c "Итак, Молли, откуда ты ездишь на работу?"
    show molly thinking
    molly.c "О, это небольшой городок. На машине около часа сорока пяти минут, если нет пробок."
    show molly neutral talk
    molly.c "Прямого поезда сюда нет, так что приходится ездить на машине."
    show molly neutral
    mc.c "Каждый день туда и обратно? По-моему, это кошмар..."
    show molly neutral talk
    molly.c "Сначала я тоже так думала... Но привыкаешь. Радио, подкасты и музыка помогают скоротать дорогу."
    show molly neutral
    mc.c "Почему ты так мучаешься? Нельзя переехать сюда? Или хотя бы поближе?"
    show molly thinking
    molly.c "Могла бы... Но это дорого. Аренда здесь недешёвая."
    mc.c "А, значит, там ты сняла жильё подешевле?"
    show molly bashful talk
    molly.c "О-о, нет, э-э... Я... всё ещё живу с родителями..."
    show molly bashful
    mc.c "О, ничего страшного, Молли. Пока можешь экономить на аренде — пользуйся, ха! Если только не сойдёшь с ума. А я лично съехал от родителей при первой возможности."
    show molly joy
    molly.c "Нет, я люблю свою семью. Теперь в большом доме живём только я и родители, так что места хватает."
    show molly smile talk
    molly.c "Они оба почти на пенсии. Мама готовит, папа возится с машинами... Дома здорово."
    show molly smile
    mc.c "Только ты и родители {i}теперь{i}?"
    show molly smile talk 2
    molly.c "У меня две старшие сестры, обе давно съехали и разъехались по стране. Они уехали из-за работы, так что мне до своей добираться сравнительно недалеко."
    show molly smile
    mc.c "Ты с ними ладишь?"
    show molly thinking
    molly.c "Хм... Да..."
    mc.c "Чувствую, ты что-то недоговариваешь."
    show molly neutral talk
    molly.c "Они дружелюбные... Но... скажем так, мы всегда соперничали."
    molly.c "Они очень хорошо учились и постоянно старались быть лучшими. Я младшая из трёх и всегда чувствовала, что отстаю."
    molly.c "Даже сейчас они стараются преуспеть в своих областях. Эрика руководит отделом в технологической компании, а Наоми уже занимает высокую должность на госслужбе."
    show molly neutral
    mc.c "А ты будущий юрист. Похоже, ты тоже втянулась в эту гонку."
    show molly smile talk
    molly.c "Не буду врать. Я тоже стараюсь изо всех сил. Нам всем хочется быть лучшими в глазах родителей."
    show molly smile
    mc.c "Уверен, родители так не думают."
    show molly smile talk 2
    molly.c "Может быть... Но нам всегда хочется обойти сестёр. Похвастаться. Сейчас я немного отстаю, но... Сдать экзамен на адвоката было бы серьёзной победой."
    show molly smile talk
    molly.c "И сейчас я остаюсь дома отчасти ради этого... Чтобы накопить денег..."
    show molly tease talk
    molly.c "Тогда я смогу первой из нас купить дом... Вот это будет победа."

    return

label mollyChat_job:
    mc.c "Мы много говорили о твоей работе. Если хочешь отвлечься, скажи, но... Почему ты решила заниматься юриспруденцией?"
    show molly neutral talk
    molly.c "Мне это было интересно ещё с детства. Кажется, лет с четырнадцати я уже собиралась стать юристом."
    show molly thinking
    molly.c "А почему... Честно говоря, думаю, в детстве я {i}слишком{/i} много смотрела телевизор."
    show molly smile talk
    molly.c "Криминальные драмы, детективы и всё такое. Меня заинтересовало правосудие."
    molly.c "Я не собираюсь заниматься уголовным правом, но всё равно это юриспруденция."
    show molly thinking
    molly.c "В школе у меня хорошо получалось, и как-то всплыла эта тема. Учителя меня поддержали... Я стала больше изучать обществознание и всё такое..."
    show molly smile talk 2
    molly.c "У сестёр тоже были большие амбиции, и я как-то последовала за ними."
    molly.c "Поступила на юридический факультет, прошла стажировку, и... вот я здесь. Забавно, как всё складывается."
    show molly smile
    mc.c "Как я уже говорил, это достойно уважения."
    show molly smile talk
    molly.c "Ты так говоришь... Большинство людей юристов терпеть не может. Зажатые костюмы, бюрократическая волокита и всё такое."
    show molly tease talk
    molly.c "А уж платить за их услуги никто не любит."
    show molly tease
    mc.c "Точно... Хотя я уверен, что с тобой был бы в надёжных руках, надеюсь, мне не придётся скоро иметь дело с законом."
    mc.c "Но я имею в виду, что ты упорно трудишься и добиваешься своего в мире, где доминируют мужчины. Это впечатляет."
    show molly thinking
    molly.c "Хм... Это не так трудно, как ты думаешь... Иногда мне кажется, что я {i}слишком{/i} хорошо вписываюсь..."
    mc.c "Что ты имеешь в виду?"
    show molly bashful talk
    molly.c "О, ничего особенного. Я ничего такого не хотела сказать... Ко мне относятся нормально..."
    show molly bashful
    "Я не совсем понимаю, что она имеет в виду. Ладно, оставлю это..."

    return

label mollyChat_hobbies:
    mc.c "Чем ты занимаешься в свободное время?"
    show molly neutral talk
    molly.c "Свободное время? У меня его почти нет..."
    show molly thinking
    molly.c "Ну... я... э-э..."
    molly.c "Хм..."
    show molly bashful talk
    molly.c "Честно говоря, кроме работы у меня почти ни на что не остаётся времени... Если не работаю, то еду туда-сюда... Почти ничего больше не успеваю."
    molly.c "Домой я возвращаюсь совершенно без сил... Помогаю родителям с делами — и пора спать."
    molly.c "Часть выходных я тоже провожу за учёбой... Чтобы сдать экзамен на адвоката, нужно очень много заниматься..."
    show molly sad talk
    molly.c "Когда говорю это вслух, звучит очень грустно. Прости, наверное, я скучная..."
    show molly sad
    mc.c "Нет, вовсе нет! Ты серьёзно относишься к карьере, и это здорово. Да и работа интересная."
    mc.c "Приятно видеть, как человек старается. Я за тебя болею."
    show molly bashful talk
    molly.c "Спасибо... Прости, я давно не ходила на свидания. В последнее время совсем не думала, как к ним готовиться."
    show molly bashful
    mc.c "Расслабься, всё нормально. Не надо готовиться — просто будь собой. Есть хоть какие-нибудь мелочи, которыми тебе нравится заниматься? Может, что-то с родителями?"
    show molly bashful talk
    molly.c "Ну... Мне нравится... Хм... мамина еда?.."
    show molly bashful
    mc.c "Это был вопрос?"
    show molly smile talk
    molly.c "Хе-хе~ Ладно. Обожаю мамины блюда!"
    molly.c "Помогаю на кухне, когда она готовит что-то большое и сложное, но чаще всего просто прихожу поесть."
    show molly joy
    molly.c "Она замечательно готовит и всегда накладывает огромные порции. Не знаю, что бы я без этого делала!"
    mc.c "Мне нравится такой досуг — поесть. Только не жди от меня особых кулинарных чудес..."
    show molly tease talk
    molly.c "Хе-хе~ Ничего страшного. Я и сама не лучший повар, но кое-чему научилась."
    mc.c "А что ты слушаешь в дороге? Наверняка включаешь что-нибудь, чтобы пережить эту долгую поездку."
    show molly thinking
    molly.c "Хм... Есть хорошие подкасты о судебных делах..."
    mc.c "Ты прямо живёшь этой работой."
    show molly smile talk
    molly.c "Иначе не добиться успеха. А вообще, когда хочется отдохнуть от работы, я включаю музыку."
    show molly smile talk 2
    molly.c "В основном попсу, то, что звучит в хит-парадах. Знаешь Софи Регилу?"
    show molly smile
    mc.c "Кажется, да. Это та, от которой все девчонки-подростки без ума?"
    show molly surprise
    molly.c "Эй! Она хорошая! Взрослым тоже можно её слушать!"
    mc.c "Ха-ха, знаю. Просто шучу. Пусть наша грозная юристка слушает музыку для подростков."
    show molly tease talk
    molly.c "Не дразни меня... В душе я всё ещё девчонка."

    return

#

label mollyDatePayFor:
    show molly surprise
    molly.c "Ты уверена? Я... не против, если..."
    show molly tease talk
    molly.c "О-о, спасибо~ Хи-хи~"
    if(mollyVacation.unlocked):
        molly.c "Люблю тебя~"
    return

label mollyEndDate:
    if(dateScore < 40):
        show molly bashful
        molly.c "Мне, э-э, надо поработать..."
    else:
        if(molly.movedIn):
            show molly tease talk
            molly.c "Сегодня было очень весело, дорогой! Спасибо за встречу! Люблю тебя!"
        else:
            show molly joy
            molly.c "Сегодня было здорово, [mc.name]! Если найдётся время, давай скоро повторим?"
            if(mollyVacation.unlocked):
                molly.c "До скорого! Люблю тебя!"
    return

label mollyContinueDateAtHome:
    scene expression 'molly[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(mollyHEvent2.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label mollyHomeStartSex:
    show molly tease talk
    molly.c "Прямо сейчас? Хм~"
    molly.c "Я тоже хочу~"
    return

label mollyHomeSexJoinIn(character):
    show molly bashful talk at twoPersonLeft with dissolve
    molly.c "Ребята... Можно я тоже?.."
    show molly bashful
    return

label mollyEndDateAtHome:
    molly.c "Жаль, что мне так скоро надо уходить... Давай заранее договоримся о следующей встрече!"
    if(mollyVacation.unlocked):
        molly.c "Люблю тебя!"
    return

image molly casual pat animated = Movie(play="images/characters/molly/affections/mollyPatCasual.webm", side_mask=True, loop=True)
image molly pat animated = Movie(play="images/characters/molly/affections/mollyPat.webm", side_mask=True, loop=True)
label mollyReceivePat:
    hide molly with dissolve
    show molly pat animated with dissolve
    pause
    molly.c "Не тяни... Д-дай я немного наклонюсь..."
    return

image molly casual chinscratch animated = Movie(play="images/characters/molly/affections/mollyChinscratchCasual.webm", side_mask=True, loop=True)
image molly chinscratch animated = Movie(play="images/characters/molly/affections/mollyChinscratch.webm", side_mask=True, loop=True)
label mollyReceiveChinScratch:
    hide molly with dissolve
    show molly chinscratch animated with dissolve
    pause
    molly.c "Хм-м~?"
    molly.c "Наверное, сейчас я выгляжу совсем непрофессионально~"
    return

image molly casual caressbutt animated = Movie(play="images/characters/molly/affections/mollyCaressButtCasual.webm", side_mask=True, loop=True)
image molly caressbutt animated = Movie(play="images/characters/molly/affections/mollyCaressButt.webm", side_mask=True, loop=True)
label mollyReceiveCaressButt:
    hide molly with dissolve
    show molly caressbutt animated with dissolve
    pause
    molly.c "Ох, [mc.name]..."
    molly.c "Только не рядом с моей работой, ладно? Я бы просто сгорела со стыда."
    return

image molly boobgrab animated = Movie(play="images/characters/molly/affections/mollyBoobGrab.webm", side_mask=True, loop=True)
image molly casual boobgrab animated = Movie(play="images/characters/molly/affections/mollyBoobGrabCasual.webm", side_mask=True, loop=True)
label mollyReceiveBoobGrab:
    hide molly with dissolve
    show molly boobgrab animated with dissolve
    pause
    molly.c "[mc.name]! Ну правда, прямо сейчас? Ах..."
    molly.c "Ладно, только нежно~ Хм-хм~"
    return

image molly snuggle animated = Movie(play="images/characters/molly/affections/mollySnuggle.webm", side_mask=True, loop=True)
image molly casual snuggle animated = Movie(play="images/characters/molly/affections/mollySnuggleCasual.webm", side_mask=True, loop=True)
label mollyReceiveSnuggle:
    "Я лежу на диване, а Молли ищет, где сесть. Я раскрываю объятия."
    show molly smile talk
    molly.c "Прямо на тебе? Ну ты и глупыш..."
    hide molly with dissolve
    show molly snuggle animated with dissolve
    pause
    "Мы тесно устраиваемся на диване. Я едва могу обхватить её рукой и притянуть к себе."
    molly.c "Хм-хм~ Глупо, но мило, дорогой~"
    pause
    return

label mollyReceiveHug:
    hide molly with dissolve
    show molly hug with dissolve
    pause
    molly.c "Осторожнее, а то я тебя задавлю..."
    return

label mollyReceiveKiss:
    hide molly with dissolve
    show molly kiss with dissolve
    pause
    molly.c "*Чмок*"
    molly.c "[mc.name]~"
    if(molly.movedIn):
        molly.c "Люблю тебя, дорогой."
    elif(mollyVacation.unlocked):
        molly.c "Я люблю тебя~"
    return

label mollyInitiatePat:
    show molly tease with dissolve
    "Молли слегка наклоняется с таким милым личиком... Наверное, она хочет..."
    hide molly with dissolve
    show molly pat animated with dissolve
    pause
    molly.c "Ой, откуда ты догадался, [mc.name]?"
    return

label mollyInitiateChinScratch:
    show molly tease with dissolve
    "Её подбородок чуть выше моих глаз, и это очень соблазнительно..."
    "Похоже, она замечает мой взгляд и усмехается."
    hide molly with dissolve
    show molly chinscratch animated with dissolve
    pause
    molly.c "Ты такой нежный, обожаю~"
    return

label mollyInitiateHug:
    show molly tease talk with dissolve
    molly.c "[mc.name], обними меня покрепче~"
    hide molly with dissolve
    show molly hug with dissolve
    pause
    if(molly.movedIn):
        molly.c "Хе-хе~ Спасибо, дорогой~"
    else:
        molly.c "Хе-хе~ Там всё в порядке?"
    return

label mollyInitiateKiss:
    show molly joy with dissolve
    if(molly.movedIn):
        molly.c "Дорогой~"
    else:
        molly.c "[mc.name]~"
    hide molly with dissolve
    show molly kiss with dissolve
    molly.c "*Чмок*"
    pause
    hide molly with dissolve
    show molly smile talk with dissolve
    molly.c "Не смогла удержаться!"
    if(mollyVacation.unlocked):
        molly.c "Я так сильно тебя люблю!"
    return

label mollyInitiateSnuggle:
    show molly tease
    "Я лежу на диване, и Молли смотрит на меня с озорной улыбкой."
    show molly tease talk
    molly.c "Обнимешь меня~?"
    hide molly with dissolve
    show molly snuggle animated with dissolve
    pause
    "Она устраивается передо мной и направляет мои руки, чтобы я обнял её."
    molly.c "Хе-хе~ Спасибо, дорогой. Люблю тебя~"
    pause
    return

label mollyInitiateHomeSex:
    show molly bashful talk
    molly.c "[mc.name]... Я..."
    molly.c "Я хочу... сделать это."
    show molly bashful
    return

label mollyInitiateHomeSexDeny:
    show molly bashful talk
    molly.c "Ну ты и дразнила..."
    return

label mollySeesAffection(affection):
    show molly bashful
    molly.c "*Кхм*"
    "Рядом шевелится Молли. Наверняка она тоже хочет немного нежности..."
    call expression 'mollyReceive' + affection from _call_expression_42
    hide molly with dissolve
    return

label mollyInviteOver:
    show molly tease talk
    molly.c "О-ох~? Да, пойдём~"
    return

label mollyInitiateInviteOver:
    show molly tease talk
    molly.c "Слушай, я бы не хотела возвращаться в отель. Может, я... ненадолго пойду к тебе?"
    show molly smile
    menu:
        'Yes':
            show molly joy
            molly.c "Ура! Отлично!"
            return True
        'No':
            show molly neutral talk
            molly.c "А, ладно, не переживай."
    return False

label mollyInviteGoHomeTogether:
    show molly smile talk
    molly.c "Да, пойдём домой."
    show molly tease talk
    molly.c "Домой~ Хе-хе~"
    return

label mollyInitiateGoHomeTogether:
    show molly tease talk
    molly.c "Готов идти домой? Хе-хе~ Я никак не привыкну к этому~"
    show molly tease
    menu:
        'Yes':
            show molly tease talk
            molly.c "О, будем держаться за руки? Хе-хе~"
            return True
        'No':
            show molly smile talk 2
            molly.c "Ладно! Увидимся дома, дорогой~"
    return False

label mollyShowPanties(pantiesIndex = 1):
    show molly bashful talk
    molly.c "Не понимаю, почему ты всё время хочешь их видеть..."
    $ renpy.show(molly.apiName + ' panties ' + str(pantiesIndex), tag=molly.apiName)
    with dissolve
    if(dayOfWeek == 'Saturday' or dayOfWeek == 'Sunday'):
        if(pantiesIndex == 1):
            molly.c "Ничего особенного... Кажется, купила их со скидкой."
        elif(pantiesIndex == 2):
            molly.c "Э-э... Купила их для нас... Вот и решила надеть."
        elif(pantiesIndex == 3):
            molly.c "Они у меня с подросткового возраста... Так стыдно..."
    else:
        if(pantiesIndex == 1):
            molly.c "Мне показались милыми..."
        elif(pantiesIndex == 2):
            molly.c "У меня почти не осталось чистого белья. Эти немного жмут..."
        elif(pantiesIndex == 3):
            molly.c "Хотела надеть что-нибудь сексуальное для тебя, но они оказались неожиданно удобными."
    return

label mollySendDateText(proposedDate):
    python:
        molly.textChain.append(Message(mc, molly, "Завтра у меня будет немного свободного времени. Не хочешь встретиться?", Null, day, timeOfDay))
        molly.textChain.append(Message(mc, molly, "Ты свободен в " + proposedDateTime + "? Я бы с удовольствием сходила в " + proposedLocation.name, Null, day, timeOfDay, proposedDate))
    return

label mollyGetSelfieOptions:
    $ mollySelfieOptions = []
    if(mollyLikeEvent2.unlocked):
        $ mollySelfieOptions.extend(['office1'])
    if(mollyLikeEvent3.unlocked):
        $ mollySelfieOptions.extend(['hotel1'])
    if(mollyHEvent2.unlocked):
        $ mollySelfieOptions.extend(['hotel2'])
    if(mollyHEvent4.unlocked):
        $ mollySelfieOptions.extend(['hotel3'])
    if(molly.movedIn):
        $ mollySelfieOptions.extend(['homebedroom1'])
    return mollySelfieOptions

label mollySendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'office1':
                potentialResponses.append({'text': "Гарантирую, я самый умный человек в том кабинете", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Хочешь, я прилечу и спасу тебя?", 'statChange': 'love', 'statChangeAmount': 1})
                molly.textChain.append(Message(mc, molly, 'Спасите... Как скучно...', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'hotel1':
                potentialResponses.append({'text': "Очень элегантно выглядишь!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "О-о, да, здорово! Ты потрясающе выглядишь", 'statChange': 'love', 'statChangeAmount': 1})
                molly.textChain.append(Message(mc, molly, "Надеть сегодня юбку?", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'hotel2':
                potentialResponses.append({'text': "Ха-ха, скучаешь в гостиничном номере без меня?", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Если они останутся такими, то точно нет...", 'statChange': 'love', 'statChangeAmount': 1})
                molly.textChain.append(Message(mc, molly, "Может, мне нужна новая пижама...", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'hotel3':
                potentialResponses.append({'text': "Ты просто идеальна", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Мне тебя всегда мало", 'statChange': 'love', 'statChangeAmount': 1})
                molly.textChain.append(Message(mc, molly, "Вижу, ты украдкой поглядываешь на мою попку... Вот", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homebedroom1':
                potentialResponses.append({'text': "Не могу дождаться, когда вернусь, любимый", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "После такого я уже еду к тебе, целую xx", 'statChange': 'love', 'statChangeAmount': 1})
                molly.textChain.append(Message(mc, molly, "Где ты, мой дорогой?", selfieName, day, timeOfDay, responses = potentialResponses))
    return

label mollySexSelect:
    hide screen mainUi
    scene black with fade
    image mollysex waiting = Movie(play="images/characters/molly/hscenes/sexWaiting.webm")
    show mollysex waiting with fade

    call screen mollySexSelectScreen
    if(mollyHEvent3.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(molly.movedIn):
            menu mollySleepTogether:
                "Переспать с Молли?"
                'Yes':
                    molly.c "А-а~ Да, давай спать."
                    molly.c "Люблю тебя~"
                    call characterSleepover(molly) from _call_characterSleepover_10
                'No':
                    pass
        else:
            menu mollyStayTheNight:
                "Пригласить [molly.name] остаться на ночь?"
                'Yes':
                    $ molly.addLove(1)
                    molly.c "Ура! Дай мне приготовиться~"
                    call characterSleepover(molly) from _call_characterSleepover_11
                'No':
                    molly.c "Скоро увидимся~"

    call endScene(character = molly, targetLocation = location_home) from _call_endScene_13

screen mollySexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(mollyHEvent1.unlocked or persistent.debugMode):
                textbutton 'Blowjob' keysym str(1):
                    action [Jump('mollyBlowjob')]
            else:
                textbutton 'Locked'
            if(mollyHEvent2.unlocked or persistent.debugMode):
                textbutton 'Cunnilingus' keysym str(2):
                    action [Jump('mollyCunnilingus')]
            else:
                textbutton 'Locked'
            if(mollyHEvent3.unlocked or persistent.debugMode):
                textbutton 'Missionary' keysym str(3):
                    action [Jump('mollyMissionary')]
            else:
                textbutton 'Locked'
            if(mollyHEvent5.unlocked or persistent.debugMode):
                textbutton 'Cowgirl' keysym str(4):
                    action [Jump('mollyCowgirl')]
            else:
                textbutton 'Locked'
            if(mollyHEvent6.unlocked or persistent.debugMode):
                textbutton 'Prone Bone' keysym str(5):
                    action [Jump('mollyPronebone')]
            else:
                textbutton 'Locked'
            if(mollyVacation.unlocked or persistent.debugMode):
                textbutton 'Makeout' keysym str(6):
                    action [Jump('mollyMakeout')]
            else:
                textbutton 'Locked'
            if(mollyVacation.unlocked or persistent.debugMode):
                textbutton 'Mating Press' keysym str(7):
                    action [Jump('mollyMatingpress')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(8):
                action [Hide('mollySexSelectScreen'), Return()]

label mollySleepover:
    scene mollysleepover with fade
    pause
    return

label mollyMorningBedInteraction:
    scene mollyhomemorning with fade
    pause
    if(molly.movedIn):
        molly.c "Доброе утро, [mc.name]. Хм~ Ты улыбался во сне."
        molly.c "Мне скоро вставать, но мы ещё немного можем поваляться в обнимку~"
        molly.c "Люблю тебя."
    else:
        molly.c "Доброе утро, [mc.name]~"
        molly.c "Я чудесно провела ночь. Ты так уютно лежал рядом."
        molly.c "Я ведь ночью не слишком... придавила тебя?"
    return

label mollyMorningBedInteractionSex(event):
    if(event == 'legjob'):
        image mollysex morning legjob 1 = Movie(play="images/characters/molly/hscenes/morning/legjob1.webm")
        show mollysex morning legjob 1 with fade
        pause
        "Я просыпаюсь, полностью укутанный мягким уютным одеялом."
        "В том числе..."
        mc.c "Доброе утро."
        molly.c "М-м..."
        mc.c "Что-то задумала, Молли?"
        molly.c "Хм-м~?"
        "Ага, она всё знает."
        image mollysex morning legjob 2 = Movie(play="images/characters/molly/hscenes/morning/legjob2.webm")
        show mollysex morning legjob 2 with fade
        pause
        "Она сжимает мой член задней частью колена и нежно водит вверх-вниз."
        "Шёлковая, гладкая, тёплая кожа, и на удивление эффективно. Как давно она этим занимается? Я уже почти..."
        mc.c "Молли..."
        scene mollymorninglegjobend with fadewhite
        pause
        molly.c "О-хо... [mc.name]~ Да что ты такое говоришь~"
    if(event == 'blowjob'):
        scene mollymorningblowjob1 with fade
        pause
        molly.c "Доброе утро, [mc.name]~"
        mc.c "Привет. Ой, уже уходишь?"
        molly.c "Ага, собираюсь."
        molly.c "У меня есть немного времени. [mc.name]... Может, тебе... помочь?"
        mc.c "Если не против..."
        image mollysex morning blowjob 1 = Movie(play="images/characters/molly/hscenes/morning/blowjob1.webm")
        show mollysex morning blowjob 1 with fade
        pause
        "Наклонившись над кроватью, Молли нежно опускается на мой член и легко принимает его в свою мордочку."
        molly.c "М-м~ Хм-м~"
        "Я погружаюсь в её обжигающе горячий рот, член зажат её блестящими губами. Я в раю."
        mc.c "Ох, чёрт, Молли..."
        molly.c "Так~ М-м~ Рано~ М-м~"
        mc.c "Это совершенно естественно..."
        image mollysex morning blowjob 2 = Movie(play="images/characters/molly/hscenes/morning/blowjob2.webm")
        show mollysex morning blowjob 2 with fade
        pause
        molly.c "М-м~ М-м~ М-м-м~"
        molly.c "Ты... М-м~ Уже близко~?"
        mc.c "Ага, чёрт... Молли, я..."
        molly.c "Кончи мне в рот~ М-м~ Не хочу... Хм-м~ испачкаться~"
        scene mollymorningblowjobfinish with fadewhite
        pause
        "Смахнув каплю спермы, Молли откидывается назад с самодовольной улыбкой."
        mc.c "Ничего себе..."
        molly.c "Хм-хм~ Доволен?"
        mc.c "Вот это начало дня."
        if(molly.movedIn):
            molly.c "Мне пора бежать. Хорошего дня, дорогой!"
        else:
            molly.c "Ладно, мне пора. До встречи, [mc.name]. Хорошего дня!"
    return

# Sex scenes
label mollyBlowjob:
    image mollysex blowjob part 1 = Movie(play="images/characters/molly/hscenes/blowjob/homeVariant/part1.webm")
    show mollysex blowjob part 1 with fade
    pause
    image mollysex blowjob part 2 = Movie(play="images/characters/molly/hscenes/blowjob/homeVariant/part2.webm")
    show mollysex blowjob part 2 with fade
    pause
    image mollysex blowjob part 3 = Movie(play="images/characters/molly/hscenes/blowjob/homeVariant/part3.webm")
    show mollysex blowjob part 3 with fade
    pause
    image mollysex blowjob part 4 = Movie(play="images/characters/molly/hscenes/blowjob/homeVariant/part4.webm")
    show mollysex blowjob part 4 with fade
    pause
    scene mollybjhomevariantend1 with fadewhite
    pause
    scene mollybjhomevariantend2 with fade
    pause
    jump mollySexSelect

label mollyCunnilingus:
    image mollysex hotel cunnilingus part 1 = Movie(play="images/characters/molly/hscenes/cunnilingus/part1.webm")
    show mollysex hotel cunnilingus part 1 with fade
    pause
    image mollysex hotel cunnilingus part 2 = Movie(play="images/characters/molly/hscenes/cunnilingus/part2.webm")
    show mollysex hotel cunnilingus part 2 with fade
    pause
    image mollysex hotel cunnilingus part 3 = Movie(play="images/characters/molly/hscenes/cunnilingus/part3.webm")
    show mollysex hotel cunnilingus part 3 with fade
    pause
    scene mollycunnilingusfinish with fadewhite
    pause
    jump mollySexSelect

label mollyMissionary:
    scene mollymissionarystart with fade
    pause
    image mollysex missionary part 1 = Movie(play="images/characters/molly/hscenes/missionary/part1.webm")
    show mollysex missionary part 1 with fade
    pause
    image mollysex missionary part 2 = Movie(play="images/characters/molly/hscenes/missionary/part2.webm")
    show mollysex missionary part 2 with fade
    pause
    image mollysex missionary part 3 = Movie(play="images/characters/molly/hscenes/missionary/part3.webm")
    show mollysex missionary part 3 with fade
    pause
    image mollysex missionary part 4 = Movie(play="images/characters/molly/hscenes/missionary/part4.webm")
    show mollysex missionary part 4 with fade
    pause
    image mollysex missionary part 5 = Movie(play="images/characters/molly/hscenes/missionary/part5.webm")
    show mollysex missionary part 5 with fade
    pause
    scene mollymissionaryend1 with fadewhite
    pause
    scene mollymissionaryend2 with fade
    pause
    jump mollySexSelect

label mollyCowgirl:
    image mollysex clothed cowgirl 1 = Movie(play="images/characters/molly/hscenes/cowgirl/part1.webm")
    show mollysex clothed cowgirl 1 with fade
    pause
    image mollysex clothed cowgirl 2 = Movie(play="images/characters/molly/hscenes/cowgirl/part2.webm")
    show mollysex clothed cowgirl 2 with fade
    pause
    image mollysex clothed cowgirl 3 = Movie(play="images/characters/molly/hscenes/cowgirl/part3.webm")
    show mollysex clothed cowgirl 3 with fade
    pause
    image mollysex clothed cowgirl 4 = Movie(play="images/characters/molly/hscenes/cowgirl/part4.webm")
    show mollysex clothed cowgirl 4 with fade
    pause
    image mollysex clothed cowgirl 5 = Movie(play="images/characters/molly/hscenes/cowgirl/part5.webm")
    show mollysex clothed cowgirl 5 with fade
    pause
    scene mollycowgirlfinish with fadewhite
    pause
    jump mollySexSelect

label mollyPronebone:
    image mollysex pronebone 1 = Movie(play="images/characters/molly/hscenes/pronebone/part1.webm")
    show mollysex pronebone 1 with fade
    pause
    image mollysex pronebone 2 = Movie(play="images/characters/molly/hscenes/pronebone/part2.webm")
    show mollysex pronebone 2 with fade
    pause
    image mollysex pronebone 3 = Movie(play="images/characters/molly/hscenes/pronebone/part3.webm")
    show mollysex pronebone 3 with fade
    pause
    image mollysex pronebone 4 = Movie(play="images/characters/molly/hscenes/pronebone/part4.webm")
    show mollysex pronebone 4 with fade
    pause
    image mollysex pronebone 5 = Movie(play="images/characters/molly/hscenes/pronebone/part5.webm")
    show mollysex pronebone 5 with fade
    pause
    scene mollypronebonefinish1 with fadewhite
    pause
    scene mollypronebonefinish2 with fade
    pause
    jump mollySexSelect

label mollyMakeout:
    image mollysex makeout 1 = Movie(play="images/characters/molly/hscenes/makeout/part1.webm")
    show mollysex makeout 1 with fade
    pause
    image mollysex makeout 2 = Movie(play="images/characters/molly/hscenes/makeout/part2.webm")
    show mollysex makeout 2 with fade
    pause
    jump mollySexSelect

label mollyMatingpress:
    image mollysex matingpress 1 = Movie(play="images/characters/molly/hscenes/matingpress/part1.webm")
    show mollysex matingpress 1 with fade
    pause
    image mollysex matingpress 2 = Movie(play="images/characters/molly/hscenes/matingpress/part2.webm")
    show mollysex matingpress 2 with fade
    pause
    # Can re-do the lost animation here
    scene mollymatingpressfinish with fadewhite
    pause
    jump mollySexSelect

label mollyhomeloungeNursingHandjob:
    scene mollyhevent7i1 with fade
    pause
    scene mollyhevent7i2 with fade
    pause
    image mollysex nursing handjob 1 = Movie(play="images/characters/molly/hscenes/nursingHandjob/part1.webm")
    show mollysex nursing handjob 1 with fade
    pause
    image mollysex nursing handjob 2 = Movie(play="images/characters/molly/hscenes/nursingHandjob/part2.webm")
    show mollysex nursing handjob 2 with fade
    pause
    scene mollynursinghandjobfinish1 with fadewhite
    pause
    scene mollynursinghandjobfinish2 with fade
    pause
    return

# Events
default mollyFirstMeetingEvent = Event('Bump in the street', 'mollyFirstMeeting', [molly], 0, 0, [], location_town, triggerDay = 5)
# Known to MC
default mollyLikeEvent1 = Event('Proper meeting', 'mollyLikeEvent1', [molly], 0, 0, [mollyFirstMeetingEvent], location_bar, ['Evening', 'Night'])
# Dateable
default mollyLikeEvent2 = Event('The invitation', 'mollyLikeEvent2', [molly], 5, 0, [mollyLikeEvent1], location_town, ['Evening'])
# Kiss.
default mollyLikeEvent3 = Event('Feminine charm', 'mollyLikeEvent3', [molly], 15, 5, [mollyLikeEvent2], location_diner, ['Evening'])
# Girly rant. Blowjob
default mollyHEvent1 = Event('Big expectations', 'mollyHEvent1', [molly], 25, 10, [mollyLikeEvent3], location_bar, ['Evening', 'Night'])
# Cunnilingus
default mollyHEvent2 = Event('Changing plans', 'mollyHEvent2', [molly], 35, 15, [mollyHEvent1], location_home, ['Evening', 'Night'])
# Lovey dovey sex sleepover
default mollyHEvent3 = Event('Fire drill', 'mollyHEvent3', [molly], 45, 20, [mollyHEvent2], location_bar, ['Afternoon'], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
# Squeeze into bath, boobjob
default mollyHEvent4 = Event('Long soak', 'mollyHEvent4', [molly], 55, 25, [mollyHEvent3], location_town, ['Evening', 'Night'])
# Dress up cowgirl
default mollyHEvent5 = Event('Sickly sweet', 'mollyHEvent5', [molly], 65, 30, [mollyHEvent4], location_town, ['Evening'])
# Saturday morning pronebone
default mollyHEvent6 = Event('Lazy saturday', 'mollyHEvent6', [molly], 75, 35, [mollyHEvent5], location_home, ['Morning'], ['Saturday', 'Sunday'])
# Cottage retreat
default mollyVacation = Event('Cosy Cottage', 'mollyVacation', [molly], 90, 40, [mollyHEvent6], Null, extraNotes = 'Organise a getaway with Molly. Special option in interaction menu.', cost=800, requiredItems = [item_car], requiresInvite = True)
# Move in invite + event
default mollyLikeEvent4 = Event('Closer to home', 'mollyLikeEvent4', [molly], 100, 45, [mollyVacation], Null, extraNotes = 'Things are getting serious. Are we ready for the next step?\nSpecial option in interaction menu.', requiresInvite = True)
# Sofa nursing handjob
default mollyHEvent7 = Event('Fresh out', 'mollyHEvent7', [molly], 110, 50, [mollyLikeEvent4], location_home_lounge, ['Evening', 'Night'], mcInitiated = True)

label mollyFirstMeeting(fromGallery):
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_174
    "Я прогуливаюсь по городу."
    "Улица приятная: хорошие магазины, кафе и несколько высоток. Похоже, поблизости есть офисы."
    "Я вижу утренний и вечерний час пик. Офисные работники в костюмах и прочие. По вечерам многие заходят в бар."
    "Замечаю улицу, по которой почти никогда не хожу. Магазинов там нет — кажется, это просто проход мимо офисов."
    "Заворачиваю за угол..."
    call stopMusic from _call_stopMusic_32
    scene black
    mc.c "Уф!"
    molly_unknown "Ой!"
    "На секунду темнеет в глазах, когда я натыкаюсь на... кого-то?"
    "Будто врезался в стену, только немного мягкую. Удар чувствуется с головы до ног, и первым, кажется, сталкивается моё лицо."
    "Солнце словно заслоняют... Глаза привыкают к свету..."
    scene mollyfirstmeetingi1 with fade
    pause
    "Передо мной возвышается огромная фигура. Приходится запрокинуть голову."
    "Размер и морда... Может, медведица?"
    "Это, должно быть, самая большая девушка-антро из всех, кого я видел. Она нависает надо мной."
    "Тот тихий вскрик, когда мы столкнулись... Из неё вырвался?!"
    "Она с лёгким беспокойством спрашивает:"
    molly_unknown "В-вы в порядке, сэр?"
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_175
    show molly surprise with dissolve
    pause
    mc.c "О-ох, да, я в порядке. Простите, а вы не ушиблись?"
    molly_unknown "Прошу прощения, сэр. Я торопилась за угол и читала письмо."
    mc.c "Всё нормально, правда. Наверное, я сам не смотрел, куда иду."
    show molly neutral talk
    molly_unknown "Нет-нет, мне надо быть осторожнее, учитывая мой размер. Простите меня."
    show molly neutral
    mc.c "Всё хорошо, обещаю."
    "Я отступаю и могу наконец разглядеть её. Она огромная."
    "Высокая, широкоплечая, фигуристая... Во всех смыслах крупная. На вид — метра два."
    "На ней строгий женский костюм, а огромные бёдра будто вот-вот разорвут брюки."
    "Я уже привыкаю к антро. Видел нескольких крупных, но медведиц, кажется, ещё не встречал."
    "Похоже, она заметила, что я пялюсь."
    show molly neutral talk
    molly_unknown "...Сэр?"
    show molly neutral
    mc.c "Ой, э-э... Простите, я просто... Наверное, вы поняли, что я здесь недавно."
    show molly neutral talk
    molly_unknown "Понимаю... Вы человек, верно?"
    show molly neutral
    mc.c "Да, я ещё ко всему привыкаю."
    show molly neutral talk
    molly_unknown "Понимаю. Надеюсь, я не слишком вас пугаю..."
    show molly neutral
    "Она говорит сверху вниз. «Пугает» — не совсем подходящее слово..."
    mc.c "Ой, нет. Простите, дело не в этом. Просто вы..."
    show molly neutral talk
    molly_unknown "Если вы не привыкли к антро, поясню. Я медведица. Мы обычно довольно крупные."
    show molly bashful talk
    molly_unknown "Даже для медведицы я довольно большая..."
    show molly bashful
    mc.c "Простите, что уставился. Я не боюсь, просто никогда раньше не встречал никого вроде вас. Это поразительно."
    show molly bashful talk
    molly_unknown "...Удивительно?"
    show molly bashful
    mc.c "Да, среди антро столько разных видов. Мне это очень интересно, но я ещё не привык."
    mc.c "Прости, если показалось, что я пялюсь."
    show molly smile talk
    molly_unknown "О-о, всё в порядке."
    show molly smile
    "На секунду её лицо светлеет. Похоже, она боялась, что я испугаюсь."
    "Многие антро тоже не привыкли к людям, как и я к ним. Думаю, обычный человек от такого зрелища растерялся бы."
    show molly thinking
    molly_unknown "{b}*Кхм*{/b} Простите, я веду себя непрофессионально..."
    "Она роется в кармане пиджака."
    show molly neutral talk
    molly_unknown "Я работаю здесь, в юридической фирме Hughes & Henderson."
    show molly neutral
    "Она протягивает мне визитку и указывает на офисное здание рядом."
    show molly neutral talk
    molly_unknown "Если вам понадобится юридическая помощь — по наследству, возмещению ущерба, защите по уголовным делам или любому другому вопросу — пожалуйста, обращайтесь к нам."
    show molly neutral
    mc.c "А, вы юрист? Если мне понадобится компенсация за травму лица, которую я только что получил?"
    show molly surprise
    molly_unknown "А-а! О нет! Э-э, да, полагаю... что..."
    "Это уже слишком жестоко."
    mc.c "Ха-ха, прости, я шучу. Плохая шутка..."
    show molly thinking
    molly_unknown "О-ох... {b}*Кхм*{/b} Хорошо, сэр..."
    show molly neutral talk
    molly_unknown "Прошу прощения, мне пора. Была рада познакомиться, сэр."
    show molly neutral
    mc.c "Взаимно..."
    "Кажется, в жизни меня ещё никогда так часто не называли «сэр»."
    hide molly with dissolve
    "Она уверенно уходит по улице. Несмотря на внушительный размер, держится очень грациозно."
    "Настоящая деловая женщина. На вид она совсем не старая, хотя мне пока сложно судить."
    "...Я не спросил её имя. Смотрю на визитку."
    "Молли..."
    "Может, ещё увидимся?"

    if(not fromGallery):
        $ molly.addLike(1)

    return

label mollyLikeEvent1(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_176
    "Приближается один из двух наплывов посетителей."
    "Сразу после работы: местные заканчивают смену, приходят группами с коллегами и так далее."
    "Позже будет второй наплыв: местные придут выпить с друзьями, студенты и пары встретятся."
    "Сегодня народу достаточно, но атмосфера остаётся спокойной. Честно говоря, в последнее время дела идут отлично."
    "Я обслуживаю посетителя и замечаю у стойки знакомое лицо."
    show molly thinking with dissolve
    "Вспоминаю визитку... Молли, кажется? Медведица, в которую я врезался на улице. Юрист? Забавно, что мы так скоро снова встретились. Раньше я её здесь не видел."
    "Наверное, я бы запомнил её даже без нашего знакомства. Её трудно не заметить."
    mc.c "Добрый вечер, Молли. Что вам налить?"
    molly.c "Мне..."
    show molly surprise
    molly.c "А? О-ох!"
    molly.c "Ты?.. А, мы виделись на днях..."
    mc.c "Ага. Не хотел тебя пугать."
    show molly bashful talk
    molly.c "Откуда ты знаешь, как меня зовут?"
    show molly bashful
    mc.c "Ты дала мне визитку при знакомстве."
    show molly thinking
    molly.c "Точно..."
    show molly neutral talk
    molly.c "А, значит, вы здесь работаете, сэр?"
    show molly neutral
    mc.c "Пожалуйста, больше не называй меня сэром... Чувствую себя стариком."
    mc.c "Вообще-то я владелец и управляю этим местом. Недавно тут работаю."
    show molly surprise
    molly.c "Ого! Правда? А что случилось с прежним владельцем? Он ведь тоже был человеком. Вы..."
    mc.c "Нет, мы не родственники. Долгая история, как-нибудь расскажу. Терри недавно вышел на пенсию, и я его заменил."
    mc.c "Значит, ты уже бывала здесь?"
    show molly neutral talk
    molly.c "Да, иногда захожу выпить, когда остаюсь в городе. Здесь приятнее, чем в баре при гостинице."
    show molly neutral
    mc.c "А, значит, ты не местная? Просто в гостях?"
    show molly neutral talk
    molly.c "Не совсем. Я здесь работаю, но живу далеко и езжу на машине."
    molly.c "Иногда на работе полно дел и приходится задерживаться, поэтому проще переночевать в гостинице поблизости."
    show molly bashful talk
    molly.c "Иногда это удобно — не нужно поздно ехать домой в темноте, но в гостинице быстро становится скучно..."
    show molly neutral talk
    molly.c "{b}*Кхм*{/b} В общем, да, иногда я захожу сюда выпить."
    show molly neutral
    mc.c "Кстати. Что тебе налить?"
    show molly neutral talk
    molly.c "Красного домашнего, пожалуйста."
    show molly neutral
    mc.c "Сейчас принесу."
    show molly neutral talk
    molly.c "Спасибо, э-э..."
    show molly neutral
    mc.c "[mc.name]. Рад снова познакомиться, Молли."
    show molly smile talk
    molly.c "Приятно познакомиться, [mc.name]."
    show molly neutral
    "Она слегка улыбается, пока я иду за напитком. Держится сдержанно, строго профессионально."
    "Наверное, сказывается её работа. Сплошная чопорность и строгие воротнички. Как же хорошо, что я от всего этого далёк..."
    "Для такой крупной женщины она говорит и ведёт себя очень изящно. Не ожидал. Но, наверное, судить о ком-то по виду его вида было бы невежливо."
    "Она пришла выпить одна, чтобы не скучать в унылом гостиничном номере. Мне хотелось бы узнать её поближе..."
    mc.c "Вот ваш напиток."
    "Похоже, она просматривала электронную почту. Наверное, всё ещё думает о работе."
    show molly neutral talk
    molly.c "Спасибо."
    show molly neutral
    mc.c "Значит, ты юрист? Работа тяжёлая?"
    show molly neutral talk
    molly.c "Я пока помощник юриста, формально ещё не юрист, но стремлюсь к этому."
    show molly bashful talk
    molly.c "Иногда... очень тяжело. Поздние вечера, стрессовые встречи, требовательные клиенты..."
    show molly bashful
    mc.c "И всё время надо вести себя исключительно профессионально."
    show molly neutral talk
    molly.c "{b}*Кхм*{/b} Да, именно."
    show molly neutral
    mc.c "Ты сейчас не на работе, Молли. Расслабься. Для этого и нужен бокал."
    show molly smile talk
    molly.c "Ты прав... День был долгим."
    show molly sad talk
    molly.c "Письма всё приходят, и мне кажется, что я должна..."
    show molly sad
    mc.c "Я настаиваю. У нас в баре никакой работы."
    show molly smile talk
    molly.c "Хе-хе... Ладно... Если вы настаиваете, [mc.name]."
    show molly smile
    "Мне удаётся уговорить её хотя бы перевернуть телефон экраном вниз. Ей не помешает с кем-нибудь поговорить."
    mc.c "То есть помощник юриста — это следующая ступень перед полноценной практикой?"
    show molly smile talk
    molly.c "В основном да. Многие идут этим путём, практикуя право и готовясь к экзамену адвокатуры."
    show molly smile talk 2
    molly.c "Хотя можно сделать карьеру и помощником юриста, я всё же хочу когда-нибудь сдать экзамен."
    show molly smile
    mc.c "Звучит достойно. Говорят, он очень сложный? Некоторые годами пытаются сдать?"
    show molly neutral talk
    molly.c "Это правда. Обычно сдают примерно к тридцати — зависит от того, сколько учился на юрфаке и стажировался в фирме."
    molly.c "Я работаю в фирме уже три года, мне [molly.age], так что я серьёзно готовлюсь."
    show molly neutral
    "Я всё думал, как спросить. Мне было интересно, сколько ей лет. По внешности не определить."
    mc.c "Интересно. А чем именно ты занимаешься как помощник юриста?"
    show molly smile talk
    molly.c "Ну..."
    scene black with fade
    "Вечер проходит за разговорами, то и дело нас отвлекают другие посетители."
    "После пары бокалов она понемногу расслабляется."
    "На самом деле она очень обаятельная. То тепло и непринуждённо болтает, то спохватывается и снова выпрямляется, возвращаясь к своему профессиональному образу."
    "Очень трудолюбивая девушка, стремится преуспеть в непростой сфере... Хорошо, что не я..."
    $ location_bar.showBackground()
    show molly thinking with dissolve
    molly.c "{b}*Вздыхает*{/b} Больше всего давит необходимость всё успевать, быть идеальной и справляться со всем одновременно..."
    show molly bashful talk
    molly.c "И не хочу так говорить, но женщине приходится нелегко. Всё время нужно поддерживать определённый образ."
    molly.c "Любую ошибку женщины тут же замечают. Нас критикуют строже, особенно если мы молоды..."
    show molly bashful
    mc.c "Звучит тяжело... Считай это место безопасной гаванью. Здесь можешь расслабиться."
    show molly thinking
    molly.c "Честно говоря, мне проще, чем другим. Так многое зависит от впечатления..."
    molly.c "Крупное телосложение, сила и уверенность очень помогают при личном общении, и..."
    show molly bashful talk
    molly.c "То, что я такая... большая... тоже помогает, наверное. Не то чтобы я..."
    show molly thinking
    molly.c "Ой, я уже заболталась... Не обращай внимания..."
    mc.c "Принести ещё один, Молли?"
    show molly smile talk
    molly.c "Нет, спасибо, [mc.name]. Мне уже хватит. Я скоро собиралась вернуться в гостиницу."
    show molly smile
    mc.c "Завтра рано вставать?"
    show molly thinking
    molly.c "Да, довольно рано. Не намного раньше, чем если бы я ехала домой."
    show molly smile talk 2
    molly.c "Приятно было сегодня поболтать. Спасибо, [mc.name], мне это было нужно. Когда я за рулём, выпить не получается."
    show molly smile
    mc.c "Всегда тебе рад. Буду рад увидеть тебя снова."
    show molly smile talk
    molly.c "Я обязательно вернусь."
    show molly smile
    mc.c "До встречи, Молли!"
    hide molly with dissolve
    "На прощание она машет большой... очень большой... рукой и мило улыбается."
    "Она совсем не похожа на ту женщину, которую я встретил в первый день. Профессионал, преданная работе, но уставшая от давления."
    "Я бы хотел увидеть её снова."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.knownToMC = True

    return

label mollyLikeEvent2(fromGallery):
    $ location_town.showBackground()
    "Я направляюсь на вечернюю смену. Сейчас обычно становится оживлённее, лишние руки не помешают."
    "...А впереди знакомая крупная фигура."
    call playMusic(chillTheme) from _call_playMusic_177
    mc.c "Молли!"
    show molly neutral with dissolve
    molly.c "Хм?.."
    "Она оборачивается и сонно секунду разглядывает меня."
    show molly surprise
    molly.c "О! [mc.name]! Д-добрый вечер..."
    show molly neutral talk
    molly.c "Ой, прости, я немного не в себе. День был долгим."
    show molly neutral
    mc.c "Только сейчас закончила? Тяжело..."
    show molly sad talk
    molly.c "И не говори... Но ещё не совсем. Завтра тоже дел полно."
    show molly sad
    mc.c "Сегодня домой не едешь?"
    show molly thinking
    molly.c "Нет... Но ничего страшного. Если поеду сейчас, уже будет темно. Иногда лучше переночевать здесь."
    show molly smile talk
    molly.c "Так у меня будет немного времени отдохнуть, номер чистый, и на следующий день не нужно долго ехать..."
    show molly smile
    mc.c "Тогда как насчёт зайти ко мне?"
    show molly surprise
    molly.c "...!"
    molly.c "Т-ты?.. Я..."
    mc.c "Ой, я про бар, Молли. Я как раз туда иду и подумал, не хочешь ли ты выпить."
    show molly bashful talk
    molly.c "О-о, да, конечно, ты именно это и имел в виду..."
    show molly smile talk
    molly.c "Вообще-то именно туда я сегодня и собиралась. Я уже заселилась в гостиницу."
    show molly smile
    mc.c "Отлично! Пойдём вместе сейчас или встретимся там позже?"
    show molly smile talk
    molly.c "Если не возражаешь, я пойду с тобой прямо сейчас."
    show molly smile
    mc.c "Конечно, пойдём."
    show molly tease talk
    molly.c "Веди, бармен! Хе-хе~"
    show molly tease
    "Наконец-то она немного шутит. Как мило..."
    "Мы направляемся в бар. Она знает дорогу, но приятно идти вместе."
    mc.c "В гостинице нормально?"
    show molly neutral talk
    molly.c "Вполне... Обычная деловая гостиница в городе. Фирма немного компенсирует расходы, поэтому выбирают они."
    show molly smile talk
    molly.c "Я не привередлива. Я провожу там не так много времени. Крыша, кровать и стол — больше ничего не нужно."
    show molly thinking
    molly.c "Только душ и ванна могли бы быть побольше... Мне там тесновато..."
    "Наверное, тяжело. Мне любопытно, но, может, сейчас не время спрашивать. Похоже, она стесняется своего размера."
    mc.c "Если фирма платит, ты, выходит, большая шишка?"
    "Ой, зря я сказал {b}большая{/b} шишка..."
    show molly neutral talk
    molly.c "Не совсем. Фирма довольно известная и часто отправляет сотрудников по стране и за границу."
    molly.c "Такое положено почти всем, кроме стажёров, так что мне повезло."
    molly.c "Например..."
    scene black with fade
    "Мы приятно прогуливаемся до бара, а Молли рассказывает о фирме и работе."
    "Она признаётся, что работа тяжёлая, но я чувствую, как она гордится тем, что делает и чего добилась."
    "А я большую часть жизни старался работать как можно меньше... Стыдно."
    $ location_bar.showBackground()
    "Мы приходим, и Молли занимает своё обычное место у стойки, усаживаясь на табурет, который вдруг кажется слишком хлипким..."
    show molly smile with dissolve
    molly.c "С чего начнём?"
    show molly smile talk
    molly.c "Сегодня я, пожалуй, побалую себя. Есть просекко?"
    show molly smile
    mc.c "О-о, сегодня по-королевски... Уже несу, {i}мадам~{/i}"
    show molly tease talk
    molly.c "Хе-хе~ Спасибо, {i}сэр~{/i}"
    show molly tease
    "Мы пару раз сталкивались в городе, болтали и проводили время вместе. Кажется, мы неплохо подружились."
    "Я катастрофически плохо флиртую... Это лучшая попытка. Она вроде отвечает тем же? Не уверен, может, просто вежлива."
    "Мы ещё не говорили о её личной жизни. Не буду врать, она мне интересна."
    "Помимо первого... неожиданного... знакомства, Молли мне очень понравилась. Она возвышается надо мной, но в ней чувствуется нежная и добрая душа."
    "Умная, утончённая и при этом милая. Целеустремлённая, но скромная. Я всё ещё привыкаю к антро, но считаю её очень красивой. Надеюсь, в следующие визиты узнаю о ней больше."
    scene black with fade
    call stopMusic from _call_stopMusic_33
    "Вечер продолжается. Молли выпивает, а мы болтаем, когда я не занят другими посетителями."
    "Честно говоря, я немного забросил остальных... Но когда я занят, она спокойно проверяет телефон. Наверное, работает."
    "Порой её трудно остановить."
    "Вечер идёт дальше: несколько напитков и пара закусок, которые она неожиданно быстро съедает..."
    $ location_bar.showBackground()
    call playMusic(heartTheme) from _call_playMusic_178
    mc.c "Этот за мой счёт, Молли."
    "Я ставлю перед ней ещё один бокал."
    show molly surprise with dissolve
    molly.c "Правда, [mc.name]? Не надо..."
    mc.c "Угощаю за компанию сегодня вечером."
    show molly smile talk
    molly.c "Не глупи, это ты мне составляешь компанию. Иначе я бы просто сидела и проверяла почту."
    show molly smile talk 2
    molly.c "Раньше я иногда болтала с Терри, но обычно сидела одна."
    show molly tease talk
    molly.c "Но... с удовольствием приму. Спасибо, [mc.name]. Хотя это будет последний бокал на сегодня."
    show molly tease
    mc.c "Уже захмелела?"
    show molly smile talk
    molly.c "О, нет. Чтобы по-настоящему опьянеть, мне нужно очень много выпить."
    show molly thinking
    molly.c "Ну, ты понимаешь, из-за размера..."
    mc.c "Не знаю, преимущество это или нет."
    show molly smile talk
    molly.c "Хе-хе~ По крайней мере, утром голова ясная. В этом есть плюс."
    show molly bashful
    molly.c "Один из немногих..."
    show molly neutral
    "Такое бывает... Она иногда говорит о своём размере с неприязнью. Интересно, дело в том, как он влияет на неё как на женщину..."
    "Хочу узнать. И вообще хочу узнать о ней больше. Хочу увидеться снова, а не только когда она иногда заходит после работы."
    "Надо спросить, пока вечер не закончился. Кто знает, когда мы ещё встретимся."
    mc.c "Слушай, Молли, когда ты снова будешь в городе? Ну, не в тот день, когда сразу едешь домой после работы?"
    show molly thinking
    molly.c "Хм, пока не знаю. Сейчас на работе завал, иногда только за день узнаю, что останусь здесь..."
    show molly neutral talk
    molly.c "А что такое?"
    show molly neutral
    mc.c "Я хотел узнать, не сходишь ли ты как-нибудь выпить. По-настоящему, не урывками, пока я работаю."
    mc.c "Или... выпить кофе, поесть где-нибудь? Если тебе надоел гостиничный сервис..."
    "Вот сейчас узнаю, не занята ли она. Не могу упрекнуть себя за попытку, но спросить всё равно надо."
    show molly neutral talk
    molly.c "Да, конечно, это было бы здо..."
    molly.c "..."
    show molly surprise
    molly.c "...А?"
    "Она шокирована или удивлена. Наверное, я застал её врасплох. Неудачный момент? Ненавижу, когда неправильно понимаю намёки..."
    show molly bashful talk
    molly.c "Э-э... {b}*Кхм*{/b} Прости, я просто не ожидала..."
    show molly bashful
    mc.c "Ой, ничего страшного. Прости, если я перешёл границу, просто подумал..."
    show molly bashful talk
    molly.c "П-погоди! Э-э... Да..."
    show molly smile talk
    molly.c "Да, я бы очень хотела, [mc.name], если тебе удобно..."
    show molly smile
    mc.c "Конечно, удобно! Когда тебе будет удобно?"
    show molly smile talk
    molly.c "Придётся ответить, что пока не знаю... Но, может, обменяемся номерами и договоримся позже?"
    show molly smile
    mc.c "Отлично, вот..."
    "Мы обмениваемся номерами и радостно улыбаемся, как школьники."
    "Молли допивает и спрыгивает с табурета."
    show molly tease talk
    molly.c "Я прекрасно провела время, [mc.name]. Спасибо! Скоро поговорим?"
    show molly tease
    mc.c "Да, конечно! Спасибо, что пришла сегодня, Молли. До скорого!"
    show molly tease talk
    molly.c "Не могу дождаться. Пока!"
    hide molly with dissolve
    "Молли машет мне на прощание и уходит, а в зале становится тише."
    "Похоже, у меня появился шанс на свидание."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)
        $ molly.isDateable = True
        "Теперь можно приглашать [molly.name] на свидания."

    return

label mollyLikeEvent3(fromGallery):
    $ location_diner.showBackground()
    call playMusic(chillTheme) from _call_playMusic_179
    show molly smile with dissolve
    "Я очень рад, что сегодня удалось связаться с Молли."
    "Её график мешает найти время для встречи: часто она задерживается в офисе, а потом ей ещё долго ехать домой."
    "Это было непросто, но она явно хочет выкроить время. Уже хороший знак."
    "Похоже, мы пока только узнаём друг друга. Она мне очень нравится, но вопрос, наверное, в том, подхожу ли я ей."
    "Она целеустремлённая карьеристка... Может, я не соответствую её ожиданиям и жизненным целям. Ну, если так, ничего не поделаешь."
    "Мне нравится время, которое мы проводим вместе. Сначала мои приглашения немного её удивили, но, может, я просто слишком торопился."
    "К счастью, сегодня она снова ночует в гостинице, так что это отличный шанс встретиться. Ужин или напитки нам подходят."
    show molly smile talk
    molly.c "Здесь куда лучше, чем в офисной столовой. Удобно, что не нужно выходить из здания, но еда там так себе."
    show molly smile
    mc.c "Ты приносишь еду из дома?"
    show molly smile talk
    molly.c "О да, если получается, я предпочитаю брать что-нибудь, что приготовила мама."
    molly.c "Если остаётся, она собирает мне с собой. Но остатки бывают редко — дома все хорошо едят, ха~"
    show molly smile talk 2
    molly.c "Но из-за гостиниц иногда приходится довольствоваться унылыми обедами."
    show molly smile
    "Она набрасывается на еду, будто голодала неделю, и откусывает огромный бургер."
    "Большие порции, наверное, для неё проблема. Чтобы поддерживать такую фигуру, нужно много есть, особенно с её загруженным графиком."
    "Боюсь, она заметила, как я с восхищением на неё смотрю."
    show molly surprise
    molly.c "...!"
    show molly bashful talk
    molly.c "Прости... Я пропустила обед..."
    show molly bashful
    mc.c "Эй, не извиняйся. Просто приятно видеть, как кто-то наслаждается едой."
    show molly bashful talk
    molly.c "Не очень женственно, да? Не лучшее впечатление для свидания... Ха-ха..."
    show molly bashful
    mc.c "Просто расслабься рядом со мной. У тебя ведь стрессовая работа? Иногда можно снять маску."
    show molly neutral talk
    molly.c "А-а... Ты прав. Напряжённость стала моей привычкой... Надо всё время быть профессиональной."
    show molly thinking
    molly.c "Иногда я забываю переключиться. Всё время в деловом костюме и прочее..."
    show molly neutral talk
    molly.c "А в такой мужской среде к женщинам предъявляют очень строгие требования. Нельзя показывать слабость или уязвимость. Как только тебя начинают воспринимать как женщину..."
    show molly bashful talk
    molly.c "{size=20}Не то чтобы это мне грозило...{size=20}"
    show molly bashful
    "Она обрывает фразу и тихо бормочет."
    mc.c "Что ты имеешь в виду?"
    show molly bashful talk
    molly.c "Ох... Просто..."
    show molly thinking
    molly.c "Я... ничего особенного не имею в виду. Иногда кажется, что меня никогда не воспринимают как женщину."
    molly.c "Наверное, я сама выбрала этот путь. Но, возможно, не ожидала, что он займёт всю мою жизнь."
    mc.c "На работе не нашлось поклонников? Я думал, молодая профессиональная женщина в такой среде..."
    show molly neutral talk
    molly.c "О, точно нет. Встречаться с коллегами было бы ужасной идеей. Это и не приветствуется."
    show molly neutral
    mc.c "А за пределами работы? Или мешает дорога и жизнь с родителями?"
    show molly thinking
    molly.c "Это... было непросто. Я пыталась, я ведь уже много лет здесь живу."
    molly.c "Ничего не получилось. Такие мужчины, которые..."
    molly.c "..."
    "Она снова замолкает и слегка грустит. Не очень-то везло?"
    show molly neutral talk
    molly.c "Прости, не хочу вдаваться в подробности. Скажем так: пока ничего не сложилось."
    show molly neutral
    "Что из этого следует? Может, у неё высокие требования. Может, встречались одни неудачники. Или ей нравятся амбициозные мужчины."
    "Подхожу ли я? Мы уже несколько раз ходили на свидания, и она всё ещё заинтересована. Хотя я не особо амбициозный..."
    mc.c "Значит, мне повезло. Я был уверен, что ты уже с кем-то встречаешься."
    show molly tease talk
    molly.c "Хм... Приятно это слышать."
    show molly smile talk
    molly.c "Мне нравится ходить на такие встречи... На свидания... Давно такого не было."
    show molly tease talk
    molly.c "Так что спасибо тебе. Правда."
    show molly tease
    mc.c "За что ты благодаришь? Я просто рад, что ты согласилась. Я не был уверен..."
    show molly smile talk
    molly.c "Я не хотела показаться нерешительной в первый раз. Ты просто застал меня врасплох, я не ожидала."
    show molly smile
    "Бургер всё ещё у неё в руке, и он кажется совсем маленьким."
    "Пока мы разговариваем, она устраивает небольшой беспорядок. Соус вот-вот потечёт из-под булочки."
    mc.c "Молли, осторожно, соус."
    show molly surprise
    molly.c "Ой!"
    "Мило..."
    show molly smile talk
    molly.c "Чуть не испачкалась, спасибо. Пришлось бы срочно сдавать костюм в химчистку. А у меня только один пиджак с собой. Хе-хе~"
    scene black with fade
    "Молли немного расслабляется, и мы продолжаем есть."
    "Мы выпиваем по паре напитков, а Молли рассказывает о своей неделе. Ей есть что сказать, хотя многое мне непонятно."
    "Она говорит о любви и гордости за работу, но чувствуется и раздражение, и усталость."
    $ location_diner.showBackground()
    call playMusic(heartTheme) from _call_playMusic_180
    show molly smile with dissolve
    mc.c "Было вкусно. Ты довольна?"
    show molly smile talk 2
    molly.c "Хе-хе, это, наверное, было очевидно, хм-хм~"
    show molly smile talk
    molly.c "Мне это было нужно. И после сегодняшнего дня пара напитков пришлась кстати."
    show molly smile
    "Мы уже давно здесь. Было весело, но у неё начинают слипаться глаза."
    mc.c "Закругляемся на сегодня?"
    show molly thinking
    molly.c "Ой, прости, [mc.name]. Это было заметно? Я рано встала и поздно заканчиваю, так что..."
    mc.c "Ничего страшного, я тебя задержал. Мне было приятно."
    show molly tease talk
    molly.c "Мне тоже."
    show molly tease
    mc.c "Я заплачу, а потом провожу тебя «домой», если хочешь."
    show molly tease talk
    molly.c "Хе-хе~ Спасибо. В такие моменты рада, что живу за углом."
    scene black with fade
    "Я расплачиваюсь, и мы выходим вместе."
    "Мы выходим в прохладный ночной воздух."
    "До гостиницы идти недалеко, и я провожаю Молли до входа."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_town.showBackground()
    show molly tease with dissolve
    "Сегодня мне кажется, что мы шли чуть ближе друг к другу. Мы уже несколько раз встречались — что же будет дальше?"
    mc.c "Я рад, что снова тебя увидел. Когда повторим?"
    show molly tease talk
    molly.c "Мне тоже очень понравилось. Не знаю, когда снова буду в городе, но надеюсь, что скоро."
    show molly tease
    "Я поднимаю взгляд на возвышающуюся надо мной Молли. Она даже заслоняет уличный фонарь, и вокруг неё остаётся светлый ореол."
    "Она тепло улыбается и сейчас выглядит особенно милой."
    "Я чувствую напряжение между нами. Кажется, сейчас не будет слишком рано попробовать..."
    "Наши взгляды встречаются. Я чуть-чуть подхожу ближе и протягиваю руку. Наши пальцы соприкасаются."
    "Молли слегка сгибает колени и опускает лицо ко мне."
    hide molly with Dissolve(0.8)
    show molly kiss with Dissolve(0.8)
    pause
    "Вытягивая шею, я целую её."
    "Нежный поцелуй в губы. Молли держит меня за руку. Целовать кого-то настолько выше себя — совершенно необычное ощущение."
    "Поцелуй длится чуть дольше, но остаётся невероятно нежным."
    "Нас прерывает проезжающая мимо машина."
    hide molly with dissolve
    show molly tease with dissolve
    "Мы просто улыбаемся друг другу. Что тут скажешь?"
    show molly tease talk
    molly.c "*Кхм* Э-э... Хе-хе~"
    show molly tease
    mc.c "Спасибо за вечер. Скоро увидимся?"
    show molly tease talk
    molly.c "Скоро, обязательно. Буду ждать."
    show molly tease
    "Молли направляется в холл и машет мне на прощание своей маленькой ладошкой."
    hide molly with dissolve
    "Когда она скрывается внутри, я сияю от счастья."
    "Похоже, всё идёт хорошо. Может, пора перестать переживать и посмотреть, что будет дальше."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return {'location':location_town}


label mollyHEvent1(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_181
    "Из-за внезапных перемен в планах Молли написала мне."
    "Она задержалась в офисе из-за срочного дела и срока сдачи, поэтому ей снова пришлось ночевать в гостинице."
    "Но вечером ей нечем заняться, так что я приглашаю её выпить."
    show molly smile with dissolve
    "Она с радостью соглашается. Не против выпить со мной за мой счёт. Я рад, что мы снова увидимся."
    "После прошлой встречи стало ясно, к чему всё идёт. Кажется, она чувствует то же самое."
    "Признаюсь, я не знал, чего ожидать. Многие виды для меня в новинку, а Молли... заметно отличается физически."
    "Она вполне могла бы мне отказать. Если подумать, какая женщина захочет встречаться с мужчиной ниже себя?"
    "Но она такая милая. Трудолюбивая, зрелая для своего возраста, с непростой карьерой, но при этом очень мягкая и добрая."
    "Эта тёплая улыбка на большом лице делает её невероятно уютной."
    "Мы выпиваем и рассказываем о прошедших неделях. Из-за её графика встретиться бывает трудно, и я очень рад, что сегодня получилось."
    mc.c "Надеюсь, внезапная перемена планов не слишком тебя утомила."
    show molly thinking
    molly.c "Такое иногда случается. Неприятно, когда всё меняется в последний момент, но всё же лучше, чем несколько часов ехать домой и обратно."
    molly.c "Я просто предупредила родителей, они всё понимают. И не приходится ехать домой в темноте."
    mc.c "Позволь быть эгоистом, но мне это на руку. Есть возможность увидеться."
    show molly tease talk
    molly.c "Согласна. Иначе я бы провела вечер одна в гостинице за ноутбуком."
    molly.c "А когда ты рядом, задержаться здесь... уже не так неприятно, как раньше."
    show molly tease
    "Она мило улыбается мне. После пары бокалов расслабляется и постепенно раскрывается."
    "Судя по тому, как развиваются наши отношения, неудивительно, что я начинаю задумываться, какая она за закрытыми дверями."
    "Большая и сильная... Любит эксперименты? Что-нибудь поострее? Предпочитает командовать?"
    "Или она такой же мягкий, уютный плюшевый мишка, какой кажется в начале наших отношений?"
    "Только бы не назвать её плюшевым мишкой... Это может прозвучать неуместно."
    mc.c "Рад, что мы сегодня встретились. За нас."
    show molly joy
    molly.c "За нас!"
    scene black with fade
    "В баре довольно оживлённо, пока мы выпиваем и общаемся."
    "Сегодня я не на смене — хотел провести время с Молли, — но здесь становится шумновато."
    "Когда вокруг всё больше людей, разговору сложнее течь свободно."
    $ location_bar.showBackground()
    show molly neutral talk with dissolve
    molly.c "Сегодня у тебя тут многолюдно. Видно, дела идут хорошо."
    show molly neutral
    mc.c "В последнее время да. Как-то всё удачно складывается."
    mc.c "Честно говоря, я не знал, справлюсь ли, но, к счастью, это место почти само собой работает."
    show molly smile talk
    molly.c "Значит, ты всё правильно делаешь. Можешь гордиться собой."
    show molly smile
    "Один посетитель протискивается мимо нашего столика и слегка задевает Молли. Её фигура занимает больше места, чем у большинства."
    mc.c "Прости, столики стоят тесно, когда здесь столько народу."
    show molly thinking
    molly.c "Не волнуйся, но здесь и правда становится душновато."
    mc.c "Да, на этой неделе жарко. Иногда здесь трудно проветрить."
    molly.c "Хм, слушай..."
    "Похоже, она чего-то стесняется. Ей некомфортно?"
    show molly smile talk
    molly.c "Скажи, может... пойдём куда-нибудь ещё? Я бы выпила ещё в более тихом месте."
    show molly smile talk 2
    molly.c "В моём номере есть мини-бар, а гостиничные расходы частично оплачивает фирма... Если хочешь..."
    show molly smile
    "Она приглашает меня к себе в номер? Глупо было бы отказаться."
    mc.c "Да, с удовольствием."
    show molly tease talk
    molly.c "Отлично, пошли!"
    scene black with fade
    "Мы выходим и быстро доходим до гостиницы за углом."
    "Я впервые захожу внутрь. Через холл мы направляемся в её номер..."
    scene hotelroom with fade
    "В номере идеально чисто, хоть и довольно просто."
    "На кровати никто не лежал, сумка Молли стоит на соседнем стуле, на столе — пара туалетных принадлежностей."
    mc.c "Ты не знал, что сегодня придётся остаться? Взял сменную одежду?"
    show molly neutral talk with dissolve
    molly.c "Да, я привыкла держать в машине несколько вещей на случай, если придётся переночевать."
    show molly neutral
    mc.c "Если так подумать, ужасно, что тебе приходится это делать..."
    show molly smile talk
    molly.c "Э... Ничего страшного. В общем..."
    show molly smile
    "Молли наклоняется к мини-холодильнику и достаёт пару маленьких бутылок пива."
    show molly tease talk
    molly.c "Будешь?"
    show molly tease
    mc.c "Конечно."
    "Мы какое-то время сидим за столиком, пьём, болтаем и смотрим телевизор."
    "Меньше говорим о работе и больше — о жизни. Я узнаю больше о её семье, друзьях и детстве."
    call playMusic(heartTheme) from _call_playMusic_182
    show molly thinking
    "Но разговор о прошлых отношениях даётся нелегко. Молли немного замыкается."
    mc.c "Ты в порядке, Молли? Если устала, можем на сегодня закончить."
    show molly bashful talk
    molly.c "О, да-да, всё хорошо."
    show molly thinking
    molly.c "Просто... Мы ведь теперь встречаемся, да? Кажется, мне нужно кое-что сказать, иначе..."
    mc.c "Что такое? Не стесняйся."
    molly.c "Прости, эту тему немного трудно обсуждать... Не хочу, чтобы ты неправильно меня понял, поэтому скажу прямо."
    show molly neutral talk
    molly.c "Помнишь, я говорила, что мои прошлые отношения... не сложились?"
    show molly neutral
    mc.c "Да? У всех бывало что-то подобное. Хочешь поговорить?"
    show molly thinking
    molly.c "Мне кажется, я должна..."
    show molly neutral talk
    molly.c "Скажем так... Наверное, поэтому я немного колебалась и не сразу отвечала на твои ухаживания."
    show molly bashful talk
    molly.c "Мне кажется, я привлекаю только представителей крупных видов, которые ищут кого-то себе под стать, и причины у них не самые приятные..."
    show molly bashful
    mc.c "То есть... я не вписываюсь в их представления?"
    show molly surprise
    molly.c "Да, ну... нет! То есть да, но... Я не говорю, что это проблема. Совсем наоборот."
    show molly bashful talk
    molly.c "Дело в том... чего мужчины от меня ожидают. Из-за моего вида и роста..."
    molly.c "Мне попадались только крупные мужчины. Медведи, львы, гориллы и тому подобные."
    show molly mad talk
    molly.c "Один парень на свидании как-то прямо сказал, что {i}\"я идеально подхожу, чтобы родить больших и сильных детей\"{/i}."
    molly.c "Представляешь? Будто мне приятно такое слышать."
    show molly mad
    mc.c "Ничего себе. Это уже слишком."
    show molly thinking
    molly.c "Ты, конечно, не такой... Я совсем не хочу, чтобы меня так воспринимали..."
    molly.c "Но бывает и иначе... Редко попадаются не такие мужчины — зато они помельче, и..."
    show molly bashful talk
    molly.c "Боже... Прости, странный разговор, но..."
    molly.c "Мужчины помельче, которым хочется, чтобы я была какой-то огромной властной женщиной, хотя я даже не понимаю, что они имеют в виду. Грубой, жестокой или вроде того..."
    molly.c "Или встречаешься с кем-то, начинаете сближаться — а он уже хочет, чтобы его связали и доминировали над ним, хотя я никогда не проявляла к этому интереса!"
    show molly bashful
    mc.c "Я..."
    show molly mad talk
    molly.c "Это несправедливо! Я такая же молодая женщина, как и все! Девушка! А в итоге начинаю думать, что никто никогда не увидит во мне девушку..."
    show molly sad talk
    molly.c "Я просто хотела, чтобы со мной обращались хорошо, как с обычной девушкой..."
    molly.c "До тебя мной никогда не интересовался человек. Да и людей здесь немного... Но я просто не знала, чего ожидать."
    show molly bashful talk
    molly.c "Я боялась, что ты тоже окажешься таким... Поэтому была настороже. Меня уже пару раз обжигали."
    molly.c "Но ты... такой милый. Добрый и нежный. Мне кажется, я могу говорить с тобой по-настоящему, а не быть просто объектом чьих-то фетишей..."
    molly.c "Просто подумала: прежде чем мы зайдём слишком далеко... прежде чем зря потратим время... надо понять, чего мы оба хотим..."
    show molly bashful
    "Она уже выпила несколько бокалов и наконец-то выговорилась. Вот это откровенный разговор."
    "Я уважаю её желание прояснить, какими могут быть отношения. Если ей попадаются мужчины, которые хотят того, чего она сама не хочет..."
    "Не знаю, через что проходят крупные девушки. Наверное, к ним и правда относятся иначе."
    "Я старался относиться к ней как к любой другой. Не буду отрицать, что замечаю разницу в размерах, но для меня это только плюс."
    "Она красивая, и её тело, конечно, часть этого. Но я не такой..."
    mc.c "Мне жаль, что тебе пришлось через всё это пройти. Но я должен быть с тобой откровенен."
    mc.c "Ты сразу меня привлекла, а когда я узнал тебя поближе, ты понравилась мне ещё больше. Но как бы это сказать..."
    mc.c "Физически ты мне очень нравишься. Разница в размерах меня совсем не отталкивает. Наоборот, мне это нравится, но не в таком смысле..."
    mc.c "Не в том смысле, наверное... Даже не знаю, как объяснить."
    show molly bashful talk
    molly.c "А-а~ Я поставила тебя в неловкое положение. Прости..."
    show molly bashful
    mc.c "Нет, нет, подожди."
    mc.c "Может, у меня нет предубеждений, как у других видов, а может, дело просто во мне. Но раз уж надо сказать прямо..."
    mc.c "Я вижу в тебе милую, красивую женщину. Интересную, весёлую, умную, но главное — девушку, как и любую другую."
    show molly surprise
    mc.c "Хотя фраза «как и любую другую» может прозвучать красиво, но... ты понимаешь, что я имею в виду."
    show molly smile talk
    molly.c "Я... понимаю. Спасибо... Мне нужно было услышать именно это. Хоть раз..."
    molly.c "Прости, что поставила тебя в неловкое положение. Я никогда не думала о тебе плохо, но всякое бывает."
    molly.c "Я не сомневалась в тебе... Просто сегодня выпила, и слова сами полились."
    show molly smile
    mc.c "Понимаю. Хорошо, что мы всё прояснили."
    mc.c "Не сомневайся в себе."
    "Надеюсь, ей стало спокойнее, когда она наконец это высказала. Похоже, она всё ещё настороже."
    "Я беру её ладонь — такую большую по сравнению с моей — и слегка поглаживаю."
    "Мы придвигаемся на краешках сидений. Кажется, нам обоим чего-то хочется."
    hide molly with dissolve
    show molly kiss with dissolve
    pause
    molly.c "М-м~"
    show molly hug with dissolve
    molly.c "Наверное, я немного драматизировала..."
    mc.c "Тебе не о чем беспокоиться."
    molly.c "Так приятно, когда мужчина обращается со мной как с обычной девушкой... Впервые за целую вечность~"
    show molly kiss with dissolve
    pause
    molly.c "М-мм~"
    "Я скольжу рукой по её массивным бёдрам. Молли крепко кладёт ладонь мне на пояс, и я особенно остро чувствую её мощное тело."
    show molly hug with dissolve
    mc.c "Внутри тебя есть нежная, хрупкая девушка, я знаю. До сих пор помню твой милый вскрик, когда мы впервые «столкнулись»."
    molly.c "Хе-хе~ Правда? Прости, но на работе я стараюсь не показывать эту сторону."
    "Мы ещё немного обнимаемся. Едва уловимый аромат духов Молли окутывает меня."
    "Я чувствую её дыхание, тень, которую она отбрасывает на меня, мягкий мех под тесными брюками... Я уже сильно возбуждён."
    "Она бросает взгляд вниз и улыбается. Заметила."
    call playMusic(sexyTheme) from _call_playMusic_183
    molly.c "О-ох... Ничего себе~"
    mc.c "Э-э, прости, я ничего не могу с этим поделать..."
    molly.c "Всё в порядке... Это... доказательство?"
    mc.c "Наверное... Прости..."
    molly.c "Хочешь, чтобы я...?"
    "Это приглашение. На её лице нет ни смущения, ни намёка на обязанность. Просто мужчина и женщина... которые хотят друг друга."
    scene black with fade
    "Мы берёмся за руки, встаём и направляемся к кровати. Не знаю, как далеко мы зайдём, но постепенно начинаем раздеваться."
    "Когда я стягиваю последние штанины, Молли впервые предстаёт передо мной обнажённой."
    scene mollybjstart1 with fade
    "Сев, она возвышается надо мной ещё сильнее. Вид открывается поистине уникальный."
    "На ней остались только неожиданно милые кружевные трусики. Я любуюсь этой невероятно сексуальной женщиной."
    molly.c "Ты раньше была с кем-то вроде... меня?"
    mc.c "В смысле, с сексуальной?"
    molly.c "...Такой большой."
    mc.c "Таких потрясающих, как ты, мало. Ты одна такая."
    mc.c "Я с нетерпением этого жду."
    molly.c "Ах... Ты..."
    "Если бы я ещё не возбудился, эта сцена точно поставила бы меня на ноги."
    "Я собираюсь встать, чтобы подойти к ней, но она неожиданно усаживает меня обратно и опускается на колени между моих ног."
    molly.c "Я хочу посмотреть..."
    scene mollybjstart2 with fade
    "Когда я в последний раз стягиваю трусы, член вываливается наружу."
    molly.c "Н-ничего себе..."
    mc.c "Хорошее «ничего себе»?"
    molly.c "Д-да~ Он... впечатляет."
    "Приятно слышать."
    "Она придвигается ближе и изучает мой подрагивающий член. Что она собирается делать?"
    "И тут она тянется ко мне."
    image mollysex hotel blowjob part 1 = Movie(play="images/characters/molly/hscenes/blowjob/part1.webm")
    show mollysex hotel blowjob part 1 with fade
    pause
    "Она неуверенно обхватывает мой ствол рукой и нежно начинает водить вверх-вниз."
    "Её ладони такие большие... Длинные пальцы полностью обхватывают мой член, и на их фоне он кажется крошечным. Я чувствую себя немного не по-мужски..."
    molly.c "Это... нормально? Для людей, я имею в виду... Он больше, чем..."
    mc.c "Я... не совсем уверен."
    "Её хватка становится крепче. Она буквально «берёт меня в свои руки», намеренно или нет, и мне это чертовски нравится."
    molly.c "Позволь мне доставить тебе удовольствие. Я хочу~"
    image mollysex hotel blowjob part 2 = Movie(play="images/characters/molly/hscenes/blowjob/part2.webm")
    show mollysex hotel blowjob part 2 with fade
    pause
    "Она направляет себя и медленно опускается на мой член, принимая его целиком."
    "Я исчезаю в ней без остатка. Её большой рот легко принимает меня. Она даже поджимает губы, чтобы удержать его."
    molly.c "М-мм~"
    "Она мычит в такт движениям, лаская языком нижнюю сторону члена."
    mc.c "Чёрт~ Молли..."
    "Я медленно исчезаю в ней целиком. Внутри невероятно жарко..."
    "Я впервые смотрю на неё сверху вниз, но даже так ощущаю и вижу, насколько мы разные по размеру."
    image mollysex hotel blowjob part 3 = Movie(play="images/characters/molly/hscenes/blowjob/part3.webm")
    show mollysex hotel blowjob part 3 with fade
    pause
    "Она легко проводит рукой по моей груди и задирает рубашку. Ей так просто до меня дотянуться."
    "Прижав огромную ладонь к моей груди, она вдавливает меня в кресло."
    "Едва заметно проводит одним пальцем по соску, дразня меня и не отрывая взгляда."
    molly.c "М-мм~ М-мфф~"
    "Она слегка ускоряется, загоняя меня глубже в горло."
    "Я так глубоко, но даже не чувствую конца. Глубокая полость её рта, уходящая в длинную морду... Она принимает меня целиком."
    "Она плотно втягивает щёки, сжимая меня со всех сторон. Слишком хорошо... Боюсь, долго я не продержусь."
    mc.c "Молли..."
    image mollysex hotel blowjob part 4 = Movie(play="images/characters/molly/hscenes/blowjob/part4.webm")
    show mollysex hotel blowjob part 4 with fade
    pause
    "Она читает выражение моего лица. Я совсем потерялся в удовольствии."
    "Она снова крепко обхватывает мой член, чтобы удержаться и двигаться вверх-вниз ещё быстрее."
    "Если я кончу, то какое-то время не смогу продолжать. На этом всё и закончится."
    mc.c "П-подожди, я сейчас..."
    "Она подтверждает взглядом и не останавливается. Она этого хочет."
    "Крепко сжав меня и заглотив глубоко, она доводит меня до края."
    scene mollybjend1 with fadewhite
    pause
    "Молли складывает губы и проводит по мне языком, пока меня пробирает дрожь и я изливаю сперму глубоко ей в горло."
    molly.c "М-мм!"
    "Жар и давление невероятные. Я целиком утопаю в её рту."
    "Немного спермы вытекает из её губ, но она опускается на мой член ещё глубже и собирает всё до капли."
    scene mollybjend2 with fade
    pause
    "Она медленно отстраняется и поднимает голову."
    "Быстро проглотив всё, она смотрит на меня и улыбается."
    molly.c "*Хаа* Ну как, понравилось~?"
    mc.c "Ещё бы... Боже мой, это было невероятно."
    mc.c "Тебе не обязательно было... Хорошо было только мне. Я ничего для тебя не сделал."
    molly.c "Я... сама этого хотела. Не волнуйся."
    mc.c "Дай мне немного времени... На этом всё не обязательно закончится."
    molly.c "М-м..."
    "В уголке её рта собирается капля, которую она слизывает языком."
    molly.c "Дай мне только вытереть рот..."
    scene black with fade
    "Она уходит в ванную, а я привожу себя в порядок."
    "Она задала мне жару."
    "Это было так горячо. Она невероятная. Я всё ещё возбуждён. Если немного задержимся, думаю, смогу продолжить."
    "Я чувствую, как Молли с заметной тяжестью падает обратно на кровать. Я стою к ней спиной, пока привожу себя в порядок."
    mc.c "Дай хотя бы мне отплатить тебе тем же."
    "..."
    "Ответа нет."
    mc.c "Молли?"
    call stopMusic from _call_stopMusic_34
    scene mollybjend3 with fade
    molly.c "..."
    "Молли тихонько и нежно дышит."
    "Она отключилась. Совсем."
    "После пары бокалов она быстро устаёт. Она много и допоздна работает, так что не могу её винить."
    "Я бы забеспокоился, если бы на её лице не была такая довольная улыбка. Спокойной ночи, Молли."
    scene black with fade
    "Я как могу укрываю её и ухожу. Лучше не тревожить — завтра ей рано вставать."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return {'location':location_home}

label mollyHEvent2(fromGallery):
    $ location_home.showBackground()
    call playMusic(barTheme) from _call_playMusic_184
    "Сегодня вечером я должен был встретиться с Молли."
    "Она собиралась закончить работу в разумное время, мы хотели быстро и без затей перекусить, а потом она поехала бы домой в тот же вечер. Как обычный офисный работник."
    "Таков был план. По крайней мере, до вчерашнего дня."
    "Но планы изменились: на работе что-то случилось, и сегодня ей пришлось задержаться и снова ночевать в гостинице. Вообще-то меня это устраивает. Мы даже сможем провести больше времени вместе."
    "Теперь мы собираемся поужинать, а раз она не за рулём, сможет расслабиться за бокалом. Я жду, когда она закончит, чтобы встретиться."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "О, телефон. Наверное, сообщение от неё."
    molly.c "[mc.name], прости, у нас тут небольшая заминка, и я ещё какое-то время не смогу уйти."
    "Вот беда..."
    molly.c "Знаю, мы собирались встретиться. Если ты забронировал столик, прости, но я, скорее всего, не успею..."
    "Я действительно забронировал столик. Мы бы успели вовремя, но теперь, похоже, нет. Жаль, конечно, но ничего страшного."
    mc.c "Совсем не страшно, Молли, не переживай. Всё равно хочешь увидеться, когда закончишь?"
    "Надеюсь, что да. Может, тогда лучше поедим у меня."
    "..."
    "Она не сразу отвечает. Должно быть, очень занята."
    molly.c "Да, я всё ещё хочу. Прости, что так вышло. В худшем случае закончу через пару часов."
    "Бедняжка. Надо заказать что-нибудь вкусное к её приезду."
    mc.c "Ничего страшного, не нужно постоянно писать мне. Просто занимайся делом. Ты знаешь мой адрес, я буду дома."
    "Так... Кажется, я знаю, что ей нравится. Пицца всегда беспроигрышный вариант."
    scene black with fade
    "..."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    "..."
    $ location_home.showBackground()
    "Прошло уже пару часов... Она давно не писала."
    "Тем временем я решил проявить смекалку и заказал еду, думая, что она уже скоро будет."
    "Заказ приехал раньше неё... Держу его тёплым в духовке, надеюсь, ещё не остыл."
    "В сотый раз проверяю телефон. Ничего."
    "Жаль, но это не её вина. Иногда трудно выкроить время, чтобы встретиться."
    "А пицца в духовке напоминает мне, что я и тут всё испортил. Нельзя ничего предполагать."
    "*Дзынь-дон*"
    "Второй звонок в дверь за вечер."
    show molly sad with dissolve
    mc.c "Привет, Молли! Заходи!"
    show molly sad talk
    molly.c "Ох, [mc.name], прости, что всё так вышло с нашими планами... Тут дела навалились..."
    show molly sad
    mc.c "Эй, эй, не переживай! Ты не виновата. Рад, что ты всё-таки приехала."
    mc.c "Заходи, устраивайся поудобнее."
    "Я провожаю её в комнату и усаживаю. Она ставит сумку и осторожно снимает неудобные туфли."
    show molly sad talk
    molly.c "В последнее время это часто случается. Я просто надеялась..."
    show molly sad
    mc.c "Хватит, пожалуйста, не за что извиняться. Ты уже здесь. И смотри, у меня для тебя сюрприз."
    "Я достаю пиццу из духовки."
    mc.c "Проголодалась?"
    show molly surprise
    molly.c "О! Ты приготовил пиццу?"
    mc.c "А-а, нет. Я не особо умею готовить. Заказал доставку и просто держал её тёплой."
    show molly smile talk 2
    molly.c "Ты заранее заказал? Это так мило, [mc.name]... Я правда проголодалась."
    show molly smile talk
    molly.c "Надеюсь, она не слишком долго лежала?"
    show molly smile
    "Ну... довольно долго. Надеюсь, ещё нормальная."
    mc.c "Не так уж долго. Думаю, всё в порядке."
    show molly thinking
    molly.c "Не стоило... Я же сказала, что могу задержаться на пару часов..."
    mc.c "Это моя вина. Хотел угадать, когда ты приедешь, и устроить сюрприз. Не надо было."
    molly.c "Погоди..."
    "Молли смотрит на часы."
    call playMusic(heartTheme) from _call_playMusic_185
    show molly surprise
    molly.c "Ничего себе! Уже так поздно?! Боже, я даже не заметила!"
    show molly bashful talk
    molly.c "Я совсем потеряла счёт времени в офисе и даже не предупредила тебя. Я приехала гораздо позже, чем обещала..."
    show molly bashful
    mc.c "Серьёзно, не переживай."
    show molly bashful talk
    molly.c "А ты ещё и бронировал столик... Я доставила тебе столько хлопот..."
    show molly bashful
    mc.c "Да мне совершенно всё равно. Домашняя доставка и уютный вечер — это как раз по мне."
    "Я поднимаю неаккуратный кусок, запихиваю в рот огромный жирный ломоть и показываю ей большой палец."
    mc.c "Расслабься... Похоже, день был тяжёлый."
    show molly smile
    molly.c "..."
    "Вот она."
    show molly smile talk
    molly.c "Выглядит вкусно."
    show molly smile
    mc.c "Это из моего любимого места поблизости. Налетай, а то мигом всё съедим."
    show molly smile talk
    molly.c "М-м-м... Не вздумай соревноваться со мной в поедании пиццы..."
    show molly smile
    "Её плечи наконец расслабляются, и она откидывается на диван."
    "Не получится всегда строить чёткие планы. Для меня уже достаточно просто провести с ней вот так время."
    "Можно сидеть в ресторане, а можно развалиться на диване перед телевизором с пиццей. Я знаю, что выберу."
    "Мы устраиваем себе приятный вечер."
    scene black with fade
    "Пицца, дурацкое телешоу, приятная компания, хорошая беседа и пара бутылок пива... Я помогаю Молли расслабиться."
    "Она не может перестать говорить о работе, пусть иногда та её и бесит."
    "Иногда нужно просто выговориться и сбросить напряжение. Я не против побыть тем, кому она изливает душу."
    $ location_home.showBackground()
    show molly smile talk with dissolve
    molly.c "Ты прав, было очень вкусно. То, что надо."
    show molly smile
    "Молли с лёгкостью умяла невероятное количество пиццы. Я ожидал, что останутся куски."
    mc.c "Там можно и посидеть. Как-нибудь сходим."
    show molly smile talk 2
    molly.c "Да, было бы здорово. Когда мои планы станут чуть... предсказуемее."
    show molly smile
    "Она заметно расслабилась, но телефон продолжает жужжать, и она то и дело на него смотрит, хотя обещала убрать."
    show molly neutral talk
    molly.c "Прости, мне надо проверить дела на завтра."
    show molly neutral
    mc.c "Без проблем."
    "Пока она листает сообщения, лицо у неё немного мрачнеет. Похоже, она тревожится... Мысли о работе не отпускают."
    mc.c "Завтра опять долгий день?"
    show molly thinking
    molly.c "Да... Но если завтра всё пройдёт хорошо, остаток недели может быть полегче..."
    show molly neutral talk
    molly.c "Я постараюсь загладить вину. Ты так старался, несмотря на то, что я сорвала наши планы."
    show molly neutral
    mc.c "Для меня вечер не испорчен. Я отлично провёл время. Надеюсь, ты тоже."
    show molly smile talk
    molly.c "Да."
    show molly smile
    "Она откидывается, и взгляд теплеет. Глаза постепенно закрываются — так всегда бывает, когда она наконец может расслабиться."
    "Она нормально воспринимает лёгкие подколы."
    mc.c "Только не отключайся опять."
    show molly tease talk
    molly.c "Хе-хе, прости, просто клонит в сон. Погоди, опять?"
    show molly tease
    mc.c "В прошлый раз."
    show molly thinking
    molly.c "В прошлый раз..."
    "Она пытается вспомнить, о чём я."
    molly.c "А, мы выпили у тебя... Потом вернулись в мою гостиницу."
    molly.c "Мы..."
    show molly bashful talk
    molly.c "Я... *кхм* Сделала... это..."
    "Отсосала мне, да. Да, именно."
    show molly thinking
    molly.c "А потом... странно, я не помню... Я..."
    show molly surprise
    molly.c "Погоди, неужели я...?"
    mc.c "Ага. Уснула прямо там. Наверное, я тебя разочаровал."
    show molly bashful
    molly.c "Боже мой, как стыдно... Наверное, я совсем вымоталась..."
    show molly bashful talk
    molly.c "Как же это невежливо... Прости... Ты ничего не сказал! Наверное, ужасно на меня обиделся..."
    show molly bashful
    mc.c "Только на то, что не смог ответить тебе тем же."
    show molly bashful talk
    molly.c "Ответить тем же...? Ты имеешь в виду...?"
    show molly bashful
    mc.c "И потом, ты ведь переживаешь из-за работы. Говорят, это отлично помогает снять стресс. Позволишь мне...?"
    show molly surprise
    molly.c "П-п-погоди, тебе не нужно..."
    mc.c "Я бы обиделся, если бы ты не позволила."
    molly.c "..."
    show molly bashful talk
    molly.c "Ты..."
    show molly bashful
    "Я беру Молли за руку и веду к кровати."
    call playMusic(sexyTheme) from _call_playMusic_186
    hide molly with dissolve
    show molly kiss with dissolve
    molly.c "М-м~"
    show molly hug with dissolve
    mc.c "Позволь мне снять с тебя напряжение. Считай это терапией."
    molly.c "О-ох..."
    scene mollycunnilingusstart with fade
    pause
    "С моей помощью Молли нерешительно раздевается."
    "С каждым снятым предметом одежды открывается всё больше её крупного прекрасного тела, покрытого густым коричневым мехом."
    mc.c "Просто расслабься."
    molly.c "[mc.name], я не уверена..."
    mc.c "Не отказывай мне, Молли. Считай это ответной услугой."
    "Я осторожно усаживаю Молли и развожу ей ноги. Передо мной раскрывается её влажная, нежная красота."
    image mollysex hotel cunnilingus part 1 = Movie(play="images/characters/molly/hscenes/cunnilingus/part1.webm")
    show mollysex hotel cunnilingus part 1 with fade
    pause
    "Уткнувшись лицом между её огромных бёдер, я прижимаюсь носом к заветному месту."
    molly.c "О-ох~ М-мм~"
    molly.c "[mc.name]~ Т-ты..."
    "Я провожу языком по влажному меху вокруг складок её киски."
    "У неё такой сладкий вкус. Молли вздрагивает под моим языком, пока я с наслаждением ласкаю её."
    "Я чувствую, как её лицо и язык отзываются нежными звуками удовольствия, а сам слизываю всё больше её соков."
    molly.c "Я... никогда~ О-ох~ Не испытывала такого~"
    image mollysex hotel cunnilingus part 2 = Movie(play="images/characters/molly/hscenes/cunnilingus/part2.webm")
    show mollysex hotel cunnilingus part 2 with fade
    pause
    "Молли медленно откидывается назад, её сознание растворяется в наслаждении."
    molly.c "[mc.name]~ А-а-а~ М-мм~"
    molly.c "О-о-ох~"
    "Молли целиком окружает мою голову; жар исходит от каждой её части, и она прижимает моё лицо к себе."
    "Я едва могу поднять голову, чтобы вдохнуть, так что остаётся только проникнуть глубже."
    "Я лижу вверх-вниз, внутрь и наружу, ласкаю клитор из стороны в сторону — киска Молли содрогается от удовольствия с каждым движением."
    molly.c "О-о-ох~~ Так хоро-о-ошо~"
    "Чувствую, как она всё сильнее разгорается. Хочу довести её до оргазма. Пусть кончит мне на лицо."
    image mollysex hotel cunnilingus part 3 = Movie(play="images/characters/molly/hscenes/cunnilingus/part3.webm")
    show mollysex hotel cunnilingus part 3 with fade
    pause
    "Я хватаю Молли за бёдра и изо всех сил прижимаю её к кровати."
    "Дразня её то с одной, то с другой стороны, я набрасываюсь на её киску, будто давно не ел."
    molly.c "А-а-а~ А-а-а-а~ М-мм~ О-о-о-ох~"
    molly.c "Н-не надо~ Ты же заставишь меня~ О-о-ох~"
    "Это не просьба остановиться. Да и разве я теперь могу? Её вот-вот накроет."
    "Её бёдра подрагивают, дыхание становится глубже. Она кончает."
    molly.c "М-м-м-м~!"
    scene mollycunnilingusfinish with fadewhite
    pause
    "Молли выгибается и содрогается от экстаза, обрызгивая моё лицо своими сладкими соками."
    "Между её ног полный беспорядок: наши соки, пот и слюна стекают по огромным бёдрам."
    molly.c "О-о-ох~"
    molly.c "Ха-а~ Ха-а~"
    molly.c "К-как~ Ты это~ Ха-а~"
    molly.c "Что ты со мной сделал~~"
    "Её грудь вздымается и опадает, пока она переводит дыхание."
    scene black with fade
    "Я даю ей полежать и прийти в себя, пока сам немного привожу себя в порядок. По-моему, получилось отлично."
    scene mollypillowtalk with fade
    call playMusic(heartTheme) from _call_playMusic_187
    "Немного погодя я присоединяюсь к Молли на кровати, когда она уже может поддерживать разговор."
    molly.c "Никто никогда так со мной не делал... Не могу поверить... Это у тебя... талант?"
    mc.c "Мне хочется так думать."
    mc.c "Теперь стало легче?"
    molly.c "Думаю, стало, пока ты мне об этом не напомнил..."
    mc.c "Вот беда. Значит, придётся повторить."
    molly.c "Хе-хе~ Да ты не сможешь..."
    mc.c "Ещё как смогу."
    molly.c "Ох... Но давай не сегодня..."
    molly.c "Я даже не зарегистрировалась в гостинице, а уже поздно."
    "Ох. Какая-то часть меня надеялась, что она останется на ночь."
    mc.c "Можешь остаться у меня, знаешь?"
    "Она на мгновение удивлённо смотрит на меня, словно не ожидала такого предложения. Немного думает, а потом тепло улыбается."
    molly.c "Наверное, не стоит... Если я не зарегистрируюсь, возникнут вопросы. К тому же я и так отняла у тебя весь вечер..."
    mc.c "Мне совсем не трудно, но если ты уверена... В другой раз?"
    molly.c "Конечно, я бы хотела."
    scene black with fade
    "Посмотрев на часы, Молли решает отправиться домой."
    $ location_home.showBackground()
    show molly tease talk with dissolve
    molly.c "Несмотря на все трудности, я отлично провела вечер. Спасибо."
    show molly tease
    mc.c "Я тоже. Надеюсь, скоро повторим."
    show molly tease talk
    molly.c "Какую часть? Хе-хе~"
    show molly tease
    mc.c "Всё, и даже больше."
    hide molly with dissolve
    show molly kiss with dissolve
    molly.c "М-мм~"
    hide molly with dissolve
    show molly tease talk with dissolve
    molly.c "Спокойной ночи, [mc.name]."
    show molly tease
    mc.c "Скоро поговорим."
    hide molly with dissolve
    "Молли уходит в гостиницу."
    "Надеюсь, мы сможем чаще проводить время дома."
    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return

label mollyHEvent3(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_188
    "В будни в обед здесь обычно тихо. Это ожидаемо."
    "В основном приходит публика постарше, поспокойнее — это приятно. Но бывают долгие и скучные часы, да и выручка невысокая."
    "Но нет ничего лучше спокойного бокала в обеденный перерыв. Мне нравится думать, что я даю местным такую возможность."
    "Посетителей мало, лишь изредка кто-нибудь заходит или выходит. Но когда дверь снова распахивается, я вижу неожиданное лицо."
    show molly neutral with dissolve
    "Она почти заполняет собой дверной проём и быстро оглядывается."
    show molly smile
    "Заметив меня, она озаряется почти облегчённой улыбкой и направляется ко мне."
    mc.c "Молли! Не ожидал тебя увидеть."
    show molly smile talk
    molly.c "Привет, [mc.name]. Рада, что ты здесь. Я рискнула, прости, что не проверила заранее..."
    show molly smile
    "И правда, она ничего не писала. Обычно она сообщила бы, если бы оказалась в городе и была свободна."
    mc.c "Что ж, это приятный сюрприз. Рад тебя видеть. Выдался редкий шанс на полноценный обеденный перерыв?"
    show molly smile talk 2
    molly.c "Вообще-то тут забавная история..."
    molly.c "В офисе была учебная тревога. Или, по крайней мере, нам так сказали — до сих пор неясно, учения это или настоящее происшествие."
    show molly smile
    mc.c "Пожар? Всё в порядке?"
    show molly smile talk 2
    molly.c "Да-да, всё хорошо. Просто немного переполошились, когда сигнализация не замолкала, а потом началась неразбериха. Весь офис выгнали на улицу."
    show molly thinking
    molly.c "Больше получаса пожарные не могли перезапустить систему или что-то в этом роде, многие двери заперты, в офисе настоящий хаос."
    show molly tease talk
    molly.c "Так что... начальник сказал всем идти домой."
    show molly tease
    mc.c "Класс, вот это повезло, да?"
    show molly tease talk
    molly.c "Дел ещё полно, могла бы продолжить работать, но, если честно... да, я очень рада."
    show molly tease
    mc.c "Ты из тех, кого приходится {i}заставлять{/i} брать выходной, да?"
    show molly thinking
    molly.c "..."
    show molly smile talk
    molly.c "Наверное, да, хе-хе... Поймал."
    show molly smile
    mc.c "Знаю таких. Пару таких уже видел. А когда сам работал здесь, я точно {b}не{/b} был таким."
    show molly tease talk
    molly.c "Лентяй, да? Удивительно, что это место вообще работает, если ты тут так редко появляешься."
    show molly tease
    mc.c "Эй! Это твоё любимое место, значит, я что-то делаю правильно."
    show molly tease talk
    molly.c "Ладно, это было грубо. М-м-м~"
    show molly tease
    "Она всё больше расслабляется рядом со мной. Приятно видеть, как постепенно исчезают её сомнения и эта профессиональная маска."
    mc.c "Значит, внеплановый выходной. Уже знаешь, чем хочешь заняться? Сегодня ведь ты не собиралась ночевать в гостинице?"
    show molly smile talk
    molly.c "Точно. Я и сама не знала, что делать. Просто решила зайти, надеясь, что ты будешь на месте."
    show molly smile
    mc.c "Может, выпьем? Или... воспользуемся редкой возможностью и куда-нибудь сходим. Днём я тебя почти не вижу."
    show molly neutral talk
    molly.c "Звучит здорово, но ты разве не на смене?"
    show molly neutral
    mc.c "Думаю, что-нибудь придумаю..."
    show molly smile talk 2
    molly.c "Тогда было бы замечательно..."
    scene black with fade
    "Сегодня тихо, так что уйти с рабочего места несложно. Скоро всё равно должна прийти ещё одна сотрудница на полставки."
    "Немного обсудив планы, мы выходим без особого плана — просто прогуляться и посмотреть, куда занесёт."
    $ location_cafe.showBackground()
    show molly smile with dissolve
    call playMusic(memoriesTheme) from _call_playMusic_189
    "Для начала — лёгкий обед в кафе. Пара пирожных и кофе — всегда хороший выбор."
    "Молли уплетает их за обе щёки. Она умеет справляться с порциями."
    "Приятно видеть её такой. Неожиданно закончившийся рабочий день словно выключил в ней все рабочие мысли. Остались только мы."
    "Мы сближаемся. Она всё больше раскрывает свою женственность и уже не стесняется этого."
    "Она всегда была доброй, нежной и вежливой, но, очевидно, мужчины и свидания приносили ей неприятный опыт."
    "Я очень рад, что той ночью в гостинице она откровенно всё объяснила. Теперь я могу бережнее относиться к её неуверенности."
    "Да, она крупная и уютная, но прежде всего — замечательная молодая женщина. Красивая и женственная, как и любая другая, даже если её не всегда так воспринимают."
    "Есть целый мир антропоморфных отношений, межвидовых связей и тонкостей, о которых я ничего не знаю. Думаю, это даже сыграло мне на руку."
    "Для меня перед глазами просто красивая девушка."
    show molly tease talk
    molly.c "Ты засмотрелся..."
    show molly tease
    mc.c "Просто любуюсь твоей мордочкой. Для меня всё это в новинку."
    mc.c "Так и хочется поцеловать."
    show molly tease talk
    molly.c "Ой... Ну ты даёшь..."
    show molly tease
    scene black with fade
    $ location_town.showBackground()
    show molly smile with dissolve
    "Приятный сытный обед заканчивается прогулкой по городу."
    "Болтаем и обходим красивые места, пользуясь тихим будним днём."
    "Самое настоящее свидание, хотя Молли всё ещё в рабочей одежде — это немного портит картинку. Не то чтобы я жаловался: в этом она чертовски сексуальна..."
    "Будто по подсказке мы проходим мимо магазина одежды, и я замечаю, как Молли туда заглядывается."
    mc.c "Хочешь что-нибудь купить, раз уж мы здесь? Подозреваю, магазины обычно уже закрыты к тому времени, как ты заканчиваешь."
    show molly neutral talk
    molly.c "Я как раз об этом думала... Ты прав, я обычно сразу еду домой и почти не гуляю по городу."
    show molly neutral
    mc.c "Зайдём, посмотрим, найдёшь ли что-нибудь по душе."
    show molly smile talk
    molly.c "Да, пожалуй. Спасибо."
    show molly smile
    scene clothesshop with fade
    "Мы заходим внутрь и вместе прогуливаемся между рядами. Молли перебирает несколько вешалок."
    "По её выбору понятно, какой у неё стиль. Строгие вещи, подходящие и для официального случая, хотя и повседневнее её костюма."
    "Ничего слишком вызывающего, в основном образы с брюками. А мне бы хотелось увидеть что-нибудь более..."
    mc.c "Как насчёт этого?"
    "Я держу в руках какое-то платье. Даже сам не понял, что это такое, пока не вытащил его с вешалки. Просто показалось достаточно большим."
    show molly tease talk with dissolve
    molly.c "Ох, это совсем не мой привычный стиль, [mc.name]. Тебе ещё учиться и учиться."
    show molly tease
    mc.c "Ну и что? Уверен, тебе в нём будет отлично."
    show molly bashful
    molly.c "Ни за что... Это совсем не моё..."
    mc.c "Точно не смогу тебя уговорить?"
    show molly bashful talk
    molly.c "Тебе бы такое не понравилось..."
    show molly bashful
    mc.c "Как же ты ошибаешься."
    "Я перекидываю платье через руку. Оно пойдёт с нами в примерочную."
    mc.c "О, смотри-ка, оно всё равно окажется в примерочной."
    show molly thinking
    molly.c "Ничего не обещаю..."
    scene black with fade
    "Немного побродив по магазину, Молли выбирает несколько вещей на примерку. Плюс моё особое дополнение."
    "Устраиваем небольшой показ мод. Ничего вычурного — несколько милых повседневных образов. Я начинаю понимать её стиль."
    molly.c "Ладно, [mc.name], ты победил, но это же нелепо."
    "О?.."
    scene mollyhevent3i1 with fade
    pause
    "Ничего себе."
    "Молли в совершенно новом свете."
    molly.c "Не понимаю, о чём ты думал..."
    mc.c "Выглядит потрясающе! О чём ты говоришь? Ты просто красотка!"
    molly.c "Да ну, оно едва налезло... Этот крой... Слишком много всего напоказ..."
    molly.c "То есть... Посмотри на мою... мою... {size=20}грудь...{/size} Оно только привлекает к ней внимание..."
    mc.c "Пока не вижу проблемы..."
    molly.c "О боже... Ты помешан на груди?"
    mc.c "Я помешан на всём."
    molly.c "Ясно... Учту..."
    "Молли немного ёрзает. Ей явно некомфортно. Возможно, она права насчёт размера — платье и правда может быть тесновато."
    "Не ей, а мне, чёрт возьми, оно кажется великолепным. Хотелось бы убедить её, но давить не стану."
    mc.c "Спорить не буду. Но знай: ты прекрасно выглядела во всём, даже в этом."
    molly.c "Это не моё, прости, [mc.name]."
    scene black with fade
    "Молли выбирает несколько вещей. Я предлагаю заплатить, но она наотрез отказывается. У неё свои деньги. Интересно, сколько она зарабатывает..."
    "День продолжается..."
    "Мы ещё немного ходим по магазинам на главной улице, и время летит незаметно. Потом заходим поужинать."
    $ location_diner.showBackground()
    show molly smile with dissolve
    "Ничего изысканного — просто сытный ужин неподалёку, в одном из мест, куда Молли часто заходила во время поздних командировок."
    "Делим еду, выпиваем пару бокалов и от души смеёмся. Все сомнения насчёт нашей совместимости давно исчезли."
    "Закончив ужин, мы расплачиваемся и выходим в вечерний свет."
    if(not fromGallery):
        $ timeOfDay = 'Evening'
    $ location_town.showBackground()
    "Сегодня был настоящий подарок. До сих пор мне не удавалось провести с ней столько времени. Для нас это свидание стало первым в своём роде."
    mc.c "Сегодня было здорово. Спасибо, что пошла со мной. Ты могла бы провести это время дома."
    show molly smile talk with dissolve
    molly.c "Ты что такое говоришь? Это я заявилась без предупреждения. Спасибо тебе за сегодня, я тоже прекрасно провела время."
    show molly smile
    "Я понимаю, как поздно уже. Обычно Молли к этому часу заканчивает работу и отправляется в долгую дорогу домой."
    "Мы стоим на улице, не решаясь, что делать дальше. Ей пора домой? Не отнял ли я у неё слишком много времени?"
    "Но она сама тянется ко мне и берёт меня за руку, полностью накрывая мою ладонь своей большой лапой."
    "Я бы очень хотел, чтобы сегодня она осталась со мной."
    mc.c "Ты... не хочешь сегодня остаться у меня?"
    show molly smile talk
    molly.c "В машине у меня есть привычная сумка на случай ночёвки, так что..."
    molly.c "Если ты не против... я бы с радостью осталась."
    show molly smile
    "Да!"
    scene black with fade
    "Мы быстро заходим к её машине, а потом отправляемся ко мне, держась за руки."
    "Я уже весь в предвкушении. Сегодняшний день меня здорово завёл."
    $ location_home.showBackground()
    call playMusic(sexyTheme) from _call_playMusic_190
    show molly tease with dissolve
    "Едва переступив порог, мы набрасываемся друг на друга. Напряжение и предвкушение копились между нами весь день. Мы оба знали, чем всё закончится."
    hide molly with dissolve
    show molly kiss with dissolve
    molly.c "М-мм~ М-мм~"
    "Мы целуемся глубоко, ещё глубже, чем когда-либо. В каждом движении — похоть и страсть."
    "Вытягивая шею, мы гладим друг друга. Я исследую большое, уютное и местами мягкое тело Молли. Её изгибы заполняют мои ладони."
    show molly hug with dissolve
    molly.c "Ха-а~ [mc.name]~ Я так этого хочу~"
    mc.c "Я тоже."
    scene black with fade
    "Мы постепенно раздеваем друг друга, целуемся и тяжело дышим от страсти."
    "Мы, спотыкаясь, добираемся до кровати. Молли такая большая и сильная, что, вопреки моим планам, в конце концов валит меня на кровать."
    scene mollyhevent3i2 with fade
    pause
    "Я смотрю на эту большую красивую девушку, оседлавшую меня. Она упирается руками и ногами в кровать вокруг меня, отбрасывая на меня большую тень."
    "Наши взгляды встречаются. Молли чуть приподнимается и отстраняется, осознав, что произошло."
    molly.c "О-ох... Прости, я не хотела..."
    mc.c "Ха-ха, не переживай, Молли. Я не против. Зрелище и правда впечатляющее..."
    molly.c "Но я..."
    "Я её понимаю. Теперь я знаю: ей хочется быть снизу. Быть хрупкой маленькой девушкой в глазах мужчины."
    "А сейчас немного порулить."
    scene mollymissionarystart with fade
    pause
    "Я кладу руку ей на бедро и осторожно переворачиваю на спину, нависая над ней."
    "Её большая грудь ложится на грудную клетку, а Молли смотрит мне в глаза с похотливым блеском."
    molly.c "[mc.name]..."
    "Я уже весь в боевой готовности и с нетерпением жду, когда наконец соединюсь с Молли, которая так открыто мне себя предлагает."
    "Но я любуюсь этой прекрасной женщиной: её широкими бёдрами, заметной талией, массивными ляжками, рядом с которыми я кажусь крошечным..."
    "И невольно думаю: достаточно ли я для неё большой? Я отнюдь не маленький, но... разница в размерах становится очевидной."
    "До сих пор это нам не мешало. Иногда приходилось лишь присесть или вытянуть шею. Но смогу ли я доставить ей удовольствие?"
    "Кажется, она замечает моё колебание."
    molly.c "Не волнуйся... Тебя более чем достаточно, [mc.name]."
    molly.c "Пожалуйста, просто возьми меня~"
    "Эти слова заставляют меня действовать."
    image mollysex missionary part 1 = Movie(play="images/characters/molly/hscenes/missionary/part1.webm")
    show mollysex missionary part 1 with fade
    pause
    "Я осторожно вхожу в Молли. Её тепло манит меня, и она легко принимает меня целиком."
    "Прижимаясь бёдрами к её бёдрам, я чувствую, как мягкий тонкий мех шелестит, пока я скольжу между её ног."
    molly.c "О-ох... М-мм~"
    "Молли быстро обнимает меня, крепко прижимая лапы к моей спине."
    "Большие, но нежные ладони лежат у меня на плечах. Это такое тёплое, уютное чувство, словно она принимает меня целиком."
    "Ощущение восхитительное. Молли тихо мурлычет и нежно стонет, пока я скольжу по её складкам."
    molly.c "[mc.name]~"
    mc.c "Тебе достаточно?"
    molly.c "Так хорошо~ Ты идеален~"
    image mollysex missionary part 2 = Movie(play="images/characters/molly/hscenes/missionary/part2.webm")
    show mollysex missionary part 2 with fade
    pause
    "Двигаясь вверх-вниз, входя и выходя из девушки намного крупнее меня... Это скорее ощущение в голове, чем физическое."
    "Она заполняет мой взгляд и всю кровать, легко тянется ко мне, окружая мягкостью и теплом."
    "Мы продолжаем медленно двигаться, не размыкаясь."
    molly.c "М-мм~ Мне это... и правда было нужно..."
    mc.c "Я хотел тебя с самой первой встречи."
    "Её прекрасное нежное лицо откидывается в наслаждении... Больше не могу просто смотреть, хочу прикоснуться к ней всей."
    image mollysex missionary part 3 = Movie(play="images/characters/molly/hscenes/missionary/part3.webm")
    show mollysex missionary part 3 with fade
    pause
    "Я зарываюсь лицом в её шею, прижимаюсь и осыпаю поцелуями и лёгкими укусами."
    molly.c "О-ох~ [mc.name]~ Это... щекотно~"
    "Это не просьба остановиться, да я и не смог бы отстраниться. Я прижимаю нос к её ключице и исследую её тело."
    "Молли притягивает меня к себе, прижимает ладони к моей спине и обвивает меня ногами."
    "Я оказываюсь в тёплом объятии большого пушистого одеяла. Нежно двигаюсь в ней, и мы растворяемся друг в друге."
    molly.c "[mc.name]~ А-а-а~ А-а-а~"
    "Мы полностью окутаны друг другом; жар нарастает, мы сливаемся в страстной неге."
    "Я мог бы оставаться с ней так вечно. Но желание разгорается. Пора взять инициативу."
    image mollysex missionary part 4 = Movie(play="images/characters/molly/hscenes/missionary/part4.webm")
    show mollysex missionary part 4 with fade
    pause
    "Я приподнимаюсь и обхватываю её манящие бёдра."
    "Мои руки впиваются в её мягкое уютное тело. Все её пышные формы покачиваются от моих напористых толчков."
    molly.c "А-а~ Ха-а~ А-а~ [mc.name]~"
    molly.c "Ты так глубоко~ Ха-а~"
    "Раздаются влажные шлепки. Молли вся промокла от удовольствия, её мех постепенно становится влажным, пока я вдавливаю бёдра в неё."
    "Молли стонет всё громче. Её обычно сдержанный, возможно намеренно приглушённый голос звучит громче, чем когда-либо."
    "Молли сжимает меня бёдрами и вздрагивает, пока я толкаюсь в глубине её киски, едва сдерживая стоны удовольствия."
    molly.c "Ха-а~ Так хорошо~ [mc.name]~"
    "Во мне нарастает удовольствие. Я близок к финалу. Больше всего хочу услышать, как Молли закричит от наслаждения."
    image mollysex missionary part 5 = Movie(play="images/characters/molly/hscenes/missionary/part5.webm")
    show mollysex missionary part 5 with fade
    pause
    "Я усиливаю напор, бросаюсь вперёд и с силой вдавливаю её в кровать."
    molly.c "А-а-а~ А-а-а-а~ Ха-а-а~"
    "Она полностью отдалась похоти. Эта спокойная, добрая, собранная, деловая женщина сдаётся под натиском страстного экстаза."
    "Отталкиваясь от её массивного тела, я без колебаний вдавливаюсь в неё. С силой шлёпаюсь о неё, не боясь причинить боль."
    "Я крепко хватаю её за бока. Её огромная грудь подпрыгивает от напора."
    "Молли хватает меня за запястье — её большая ладонь почти полностью обхватывает моё предплечье. Невероятно видеть, как эта огромная женщина теряет голову от страсти."
    molly.c "М-мм~ Я конча-а-аю~ Конча-а-аю~"
    "Молли вздрагивает. Я тоже вот-вот кончу. Мне хватает самообладания, чтобы вытащить."
    scene mollymissionaryend1 with fadewhite
    pause
    molly.c "А-а-а-а~"
    "В последний момент я выхожу из неё, выпуская густую струю на живот Молли."
    scene mollymissionaryend2 with fade
    pause
    molly.c "Ха-а~ Ха-а~"
    "Молли извивается и приподнимает голову. Её туловище залито моей спермой, которая уже впитывается в мех."
    molly.c "[mc.name]~"
    mc.c "Я не был уверен..."
    molly.c "О-ох~ [mc.name]~ Это было... О-ох, боже..."
    molly.c "Пожалуй... *ха-а* Так и лучше..."
    "Молли откидывается и тяжело дышит. Я сажусь и любуюсь результатом."
    "Пульс постепенно замедляется, мы покрыты соками и потом. Наслаждаемся послевкусием."
    scene black with fade
    pause
    scene mollypillowtalk with fade
    call playMusic(heartTheme) from _call_playMusic_191
    "Немного отдышавшись и приведя себя в порядок, Молли переворачивается на живот и смотрит мне в лицо. Её губы расплываются в довольной улыбке."
    mc.c "Тебе понравилось?"
    molly.c "Это... было невероятно. Ты настоящий жеребец..."
    mc.c "Значит, я здоровенный, как конь."
    molly.c "Хе-хе~ Ну... не то чтобы далеко от правды."
    molly.c "Сначала ты был таким нежным и ласковым. Мне это очень понравилось."
    mc.c "Прости, я не переборщил?"
    molly.c "Нет, нет... Может, мне больше нравится помедленнее, но ты и так, и так был прекрасен. И всё было здорово. Ты был таким милым."
    molly.c "Такого дня... у меня никогда не было. Вообще никогда."
    molly.c "Я так долго работала без остановки, что почти забыла, каково это — просто провести такой день и расслабиться. Особенно с мужчиной."
    molly.c "Ты совсем не похож на других, кого я встречала. Правда. Спасибо тебе за сегодня."
    mc.c "Нет, это тебе спасибо. Ты тоже единственная в своём роде. Я просто рад, что ты дала мне шанс."
    molly.c "Это ещё не всё..."
    "Мы снова смотрим друг другу в глаза. Молли излучает тепло — добрая и нежная душа в крупном уютном теле."
    "Наступает ночь, и за день мы успели многое. Молли на несколько секунд закрывает глаза."
    mc.c "Готова спать?"
    molly.c "Ага. Дай мне собраться. Завтра, конечно, рано вставать. Постараюсь тихонько уйти, чтобы тебя не разбудить..."
    mc.c "Даже не думай. Пожалуйста, разбуди меня перед уходом — хочу увидеть тебя утром."
    "Она улыбается мне и садится, чтобы пойти в ванную."
    scene black with fade
    "Быстро приведя себя в порядок, мы забираемся в кровать и обнимаемся."
    molly.c "Хорошо, что у тебя большая кровать. Иногда мне на них бывает тесновато."
    molly.c "Не стесняйся растолкать меня, если ночью я займусь слишком много места..."
    call mollySleepover from _call_mollySleepover
    "Молли прижимается ко мне и удивительно быстро засыпает."
    "Устраиваясь поудобнее, она обнимает меня и постепенно почти полностью накрывает собой."
    "Жить под боком у огромной бурой медведицы... Вот это жизнь."
    scene black with Fade (1.5, 0.0, 1.5)
    pause
    pause
    "Хм..."
    "Рядом слышится тихое шуршание."
    scene mollyhomemorning with fade
    pause
    molly.c "Ой, прости, [mc.name], я старалась не шуметь."
    mc.c "Ничего, я, кажется, и так уже проснулся. Как спалось?"
    molly.c "Вообще отлично. Я переживала, каково будет снова делить постель с кем-то, но... Да, было очень хорошо."
    molly.c "Правда, когда проснулась, я немного придавила тебя. Я не мешала ночью?"
    mc.c "Вовсе нет. Мне понравилось большое пушистое одеяло."
    molly.c "Хе-хе... Ну, раз ты так говоришь."
    molly.c "Мне скоро пора, так что прощаюсь. Спасибо, что оставил меня у себя. Я отлично провела вечер."
    mc.c "Я тоже. Ты всегда можешь остаться."
    molly.c "Может, я и воспользуюсь этим..."
    scene black with fade
    "Для меня ещё рано, поэтому я даю Молли собраться и провожаю поцелуем."
    "Похоже, теперь я чаще буду принимать у себя гостей."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return {'location':location_home, 'time':'Morning'}

label mollyHEvent4(fromGallery):
    scene hotelroom with fade
    call playMusic(chillTheme) from _call_playMusic_192
    "После рабочего дня я провожаю Молли обратно в гостиницу."
    "После долгого дня она, кажется, совсем вымоталась, поэтому мы решаем просто заказать обслуживание в номер."
    "Мы едим, выпиваем пару бокалов, и вечер незаметно затягивается."
    show molly smile talk with dissolve
    molly.c "Ой, слушай, я хотела кое-что тебе показать."
    molly.c "Номер мне достаётся случайный, но в этот раз мне очень повезло!"
    show molly smile
    "Я оглядываю комнату, но ничего особенного не замечаю. Обычный гостиничный номер."
    mc.c "И что же? Кровать особенно удобная или что-то вроде того?"
    show molly tease talk
    molly.c "Нет, пойдём, смотри."
    show molly tease
    "Молли берёт меня за руку и ведёт... в ванную?"
    "Открываю дверь, но снова не замечаю ничего необычного. Может, это..."
    show molly smile talk 2
    molly.c "Ладно, выглядит не так уж необычно, но..."
    show molly joy
    molly.c "Посмотри на эту ванну! Она огромная!"
    "Теперь и я замечаю: она действительно большая, больше похожа на ванну в люксовом номере. Почти джакузи."
    mc.c "О-о... Понимаю. Ты говорила, что иногда тебе достаётся неудобный номер."
    molly.c "Ага! Сегодня я смогу спокойно понежиться в ванне!"
    mc.c "Обычно такой возможности нет, да?"
    show molly thinking
    molly.c "Обычно о ванне можно только мечтать... Может достаться неудобный душ без сиденья или шаткая табуретка."
    mc.c "Ох, я об этом даже не думал..."
    show molly neutral talk
    molly.c "Вообще-то гостиницам стоило бы учитывать особенности вида при бронировании. Более того, они обязаны это делать. Ты ведь замечал это, когда сам бронировал жильё?"
    show molly neutral
    mc.c "Да, наверное. Я никогда не обращал на это особого внимания. Раньше рядом со мной почти не было антро, как ты знаешь."
    show molly thinking
    molly.c "Раз проживание бронирует моя работа, сомневаюсь, что они указывают такие детали. Вот и получаю что получаю."
    show molly smile talk
    molly.c "Дома я люблю принимать ванну и скучаю по ней, когда оказываюсь здесь. Может, это звучит глупо, но именно этого я сегодня ждала."
    show molly smile
    mc.c "Совсем не глупо, я понимаю. Я ведь не мешаю тебе расслабиться?"
    show molly smile talk
    molly.c "Ой, нет, нет. Это на потом. Пока есть возможность, хочу провести время с тобой. В последнее время я была занята."
    show molly surprise
    molly.c "Ой! Э-э, не так я хотела сказать. Не то чтобы... Просто..."
    mc.c "Ха-ха, я понял, Молли. Я не против, что работа у тебя на первом месте, правда. Я ведь говорил."
    show molly smile talk
    molly.c "Хорошо, да, говорил. Но поверь, часто мне больше хотелось бы быть с тобой..."
    show molly smile
    "Теперь, когда я представляю, как Молли нежится в ванне, мне пришла идея."
    "Можно провести время вместе {i}и{/i} дать ей сделать то, чего она хочет."
    "Эта ванна... Интересно, поместимся ли мы вдвоём?"
    mc.c "Почему бы не совместить приятное с полезным?"
    show molly neutral talk
    molly.c "Совместить?"
    show molly neutral
    mc.c "Теперь, когда ты показала мне ванну, мне тоже хочется в ней полежать."
    call playMusic(barTheme) from _call_playMusic_193
    mc.c "Может... залезем туда вместе?"
    show molly surprise
    molly.c "Вместе?"
    show molly bashful talk
    molly.c "О-ох... Люди и правда так делают...? Я никогда..."
    show molly bashful
    mc.c "Наверное? Чем больше думаю, тем больше мне хочется попробовать с тобой..."
    mc.c "Хотя не переживай, если это помешает твоему «времени для себя»..."
    show molly bashful talk
    molly.c "Погоди... Это..."
    show molly tease talk
    molly.c "Вообще-то... звучит очень мило."
    show molly tease
    "Она согласилась! Вот это удача."
    mc.c "Я мог бы вымыть тебе спину, а ты мне..."
    show molly tease talk
    molly.c "Хе-хе~ Правда? Звучит заманчиво..."
    scene black with fade
    "Это было спонтанное предложение, но вот мы уже здесь."
    "Мы раздеваемся и идём в ванную. Молли садится под душем после того, как я предложил её помыть."
    scene mollyhevent4i1 with fade
    pause
    "Передо мной обнажённое тело Молли. Мягкая, уютная плоть под прекрасным мехом блестит от влаги."
    molly.c "Ты собирался вымыть мне спину, да~?"
    mc.c "К вашим услугам..."
    "Я сажусь позади неё и медленно провожу ладонью по спине."
    "Рука погружается в её мех, и он нежно щекочет пальцы, раздвигаясь под моей лаской."
    "Намылив её мех, я глажу Молли сверху вниз, ощущая тепло её спины."
    molly.c "М-м~ Приятно, [mc.name]~"
    "Молли направляет душ на себя и моет переднюю часть тела, брызгая немного воды мне на плечи."
    "Так интимно мыть эту прекрасную женщину... Невероятное ощущение."
    "Ох. Мы собирались просто расслабиться, но не уверен, что смогу сдержаться."
    mc.c "Помочь вымыть переднюю часть, мадам?"
    molly.c "О-хо-хо~ Думаешь, я сама не справлюсь?"
    mc.c "Сегодня тебе надо расслабиться, позволь мне заняться этим..."
    call playMusic(sexyTheme) from _call_playMusic_194
    image mollysex bath fingering = Movie(play="images/characters/molly/hscenes/boobjob/fingering1.webm")
    show mollysex bath fingering with fade
    pause
    "Я обнимаю Молли, лаская её бёдра и живот."
    "Намыливая её тело, я чувствую, как она вздрагивает от моих прикосновений."
    molly.c "М-мм~ [mc.name]~"
    "Я не могу удержаться и исследую её тело {i}целиком{/i}."
    "Нежно обхватываю её грудь и сжимаю, а она делает несколько глубоких вдохов."
    "Провожу рукой ниже и чувствую жар между её ног."
    molly.c "О-ох~ Ты..."
    "Молли тихонько стонет от удовольствия, пока я дразню её клитор и глажу пальцами киску."
    "Прижимаясь грудью к её спине, я обнимаю её и ласкаю, доводя до наслаждения."
    "Вода смывает её соки, но я чувствую, как Молли вздрагивает под моими руками."
    molly.c "[mc.name]~ Я сейчас..."
    mc.c "Не сдерживайся. Отдайся этому."
    molly.c "[mc.name]~"
    scene mollyshowerfingeringend with fadewhite
    pause
    molly.c "А-а~ А-а-а~"
    "Её тело слегка выгибается назад — я понимаю, что она кончила."
    molly.c "Ха-а~ Ха-а~ О-ох... [mc.name]~"
    "Я несколько мгновений смываю с неё соки. При этом мой эрегированный член отчётливо упирается ей в зад."
    molly.c "Хе-хе~ Кажется, кому-то не помешала бы ответная услуга~"
    image mollysex bath boobjob 1 = Movie(play="images/characters/molly/hscenes/boobjob/boobjob1.webm")
    show mollysex bath boobjob 1 with fade
    pause
    molly.c "Таков был план с самого начала?"
    mc.c "Не совсем... Но это было почти неизбежно."
    molly.c "Я так и думала... И, кажется, знаю, чего тебе хочется..."
    "Молли наклоняется к моему паху, сжимая огромную грудь."
    "Её шелковистый мех насквозь промок. Она скользит грудью вверх-вниз по моему твёрдому члену, намыливая его."
    mc.c "Ох, Молли..."
    "Её мокрая пушистая грудь сжимает мой член, окутывая теплом. В ванной раздаются непристойные шлепки влажной плоти."
    image mollysex bath boobjob 2 = Movie(play="images/characters/molly/hscenes/boobjob/boobjob2.webm")
    show mollysex bath boobjob 2 with fade
    pause
    "Она смотрит мне в глаза, явно наслаждаясь тем, что делает со мной."
    "Влага, скользящая по её меху, создаёт невероятные ощущения, пока она двигается вверх-вниз."
    molly.c "Хе-хе~ Правда так хорошо?"
    mc.c "Ты даже не представляешь..."
    "Головка моего члена время от времени показывается сверху, щекоча её... Я целиком утопаю в её огромной груди..."
    "Молли сжимает груди, заключая меня в эротические объятия."
    molly.c "Ты... кончишь?"
    mc.c "Обязательно... Может, чуть быстрее?"
    molly.c "Попробую~"
    image mollysex bath boobjob 3 = Movie(play="images/characters/molly/hscenes/boobjob/boobjob3.webm")
    show mollysex bath boobjob 3 with fade
    pause
    "Молли наклоняется ко мне, сжимая грудь и шлёпая ею по моим бёдрам."
    "Её упругая плоть подпрыгивает на мне, а ванная наполняется непристойными шлепками мокрого меха о кожу."
    molly.c "Ха-а~ Вот так~?"
    mc.c "Да, блядь... Вот так, блядь..."
    "Жар и трение... Вид и звуки... Меня пробирает дрожь от удовольствия."
    molly.c "Хе-хе~ Чувствую, как ты..."
    mc.c "Я сейчас кончу..."
    molly.c "Давай~"
    scene mollybathboobjobend with fadewhite
    pause
    "Молли сжимает меня и в последний раз шлёпает грудью — я кончаю поверх неё."
    "Сперма выстреливает высоко и покрывает её лицо и грудь."
    molly.c "О-ох~ [mc.name]~"
    mc.c "Ничего себе... Молли, это было невероятно."
    "Сперма стекает вниз, и проточная вода постепенно смывает её."
    molly.c "Наверное, теперь можно залезать в ванну. Но... как нам там устроиться?"
    mc.c "Можем сесть лицом друг к другу или, если хочешь, ты обопрёшься на меня."
    molly.c "Не знаю, получится ли, но давай попробуем..."
    call playMusic(heartTheme) from _call_playMusic_195
    scene mollyhevent4i2 with fade
    pause
    "Молли забирается в ванну, устраивается между моих ног и медленно откидывается на меня."
    "Надо было догадаться: мне приходится широко расставить ноги, а лицо оказывается напротив её плеч."
    molly.c "Э-э... [mc.name]? Тебе удобно?"
    molly.c "Кажется, так не получится..."
    "Я задыхаюсь и могу только хрипеть, пока вес Молли прижимает меня."
    mc.c "В-вполне удо-обно...!"
    molly.c "Ох... Может, поменяемся местами?"
    "Я не жалуюсь, но не уверен, что долго выдержу в таком положении. Было бы здорово, но с Молли мне точно не быть «большой ложкой»."
    mc.c "Ладно..."
    scene mollyhevent4i3alt with fade
    pause
    "Мы меняемся местами, и я откидываюсь на Молли, со всех сторон окружённый мягким, податливым телом."
    "Молли обнимает меня и прижимает к себе. Я расслабляюсь у неё на груди, чувствуя, как её бёдра сжимают меня."
    "Мне бы стоило почувствовать себя не по-мужски, но это ощущение полностью перекрывает то, как мне уютно."
    molly.c "М-мм~ Так лучше~"
    mc.c "Не совсем так, как я ожидал, но... Да, тоже очень хорошо."
    molly.c "Если ванна достаточно большая для меня, значит, и нам двоим места хватит."
    mc.c "У меня дома мы бы так не поместились. Может, всё-таки есть смысл в этих шикарных гостиничных номерах за счёт фирмы."
    molly.c "Хе-хе~ Немного глуповатый повод прийти ко мне..."
    mc.c "Похоже, дома надо установить ванну побольше."
    molly.c "Тебе правда настолько нравится? Если задуматься, это немного нелепо..."
    mc.c "Конечно! Я бы мог так уснуть."
    molly.c "Хе-хе~ Наверное, так будет не очень удобно, но... Да~"
    "Мы вместе расслабляемся в ванне, отогреваясь в горячей воде."
    "Мы долго и приятно отмокаем в ванне."
    scene black with fade
    "После приятного отдыха мы выходим из ванны, вытираемся и идём в кровать."
    scene mollyhotelpillowtalk with fade
    pause
    "Молли оглядывается на меня с немного смущённой улыбкой."
    molly.c "Это было немного глупо? Наверное, ты ожидал совсем другого."
    mc.c "Ты права, не такого. Получилось даже лучше."
    molly.c "Хе-хе~ Раз ты так говоришь... Я тоже не жалуюсь."
    "Мы обнимаемся в полутёмной комнате. Вокруг тихо."
    molly.c "Можешь остаться на ночь, если хочешь. Не придётся идти домой."
    "Я не планировал ночевать, но уже поздно. Немного неприлично оставаться в гостинице, забронированной на одного. Но соблазнительно..."
    mc.c "Я бы с удовольствием, если ты не против."
    molly.c "Только я рано встану. Если до полудня оставишь ключ на стойке, всё должно быть в порядке."
    mc.c "О боже, что подумает девушка на стойке, когда ты сдашь ключ за меня? Сразу станет ясно, что я ночевал."
    molly.c "Хе-хе~ Наверное, да... Кажется, пара сотрудников уже видела, как мы несколько раз приходили и уходили вместе. Интересно, что они думают?"
    mc.c "Наверное: «Как этому неудачнику удалось заполучить такую красотку?»"
    molly.c "Тише..."
    scene black with fade
    "Немного погодя мы готовимся ко сну, и я остаюсь ночевать с Молли в гостинице."
    "Когда утром я просыпаюсь, её уже нет. Бедняжка, каждый день встаёт ни свет ни заря."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return {'location':location_home, 'time':'Morning'}

label mollyHEvent5(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_196
    $ location_diner.showBackground()
    show molly smile with dissolve
    "Сегодня вечером я гуляю с Молли. Мы сходили поужинать — она настояла, что заплатит. Сказала, надо отметить успех на работе."
    "Теперь заканчиваем вечер кофе и небольшим десертом..."
    "Мы приятно проводим время, когда в паузе разговора до нас доносятся звуки от посетителей за парой столиков."
    unknown2 "Ха-ха, ну ты даёшь~"
    unknown "О-ох~ Хе-хе~"
    show molly thinking
    "Мы оба оборачиваемся: там пара молодых грызунов, явно влюблённые."
    "Они обнимаются, хихикают и шепчут друг другу нежности."
    "Парень подхватывает вилкой кусочек торта и собирается покормить девушку, но вместо этого оставляет крем у неё на носу."
    unknown "Хе-хе~ Ой, перестань~"
    unknown2 "М-мм~"
    "Девушка стирает его пальцем и размазывает по губам парня, а тот слизывает крем."
    unknown2 "Такой же сладкий, как ты~"
    unknown "Ой, ну ты~"
    "Слащаво до приторности. Если честно, немного утомляет."
    "Я поворачиваюсь к Молли, чтобы подшутить над этой сценой, но вижу, что она задумалась."
    mc.c "Вот она, юная любовь."
    molly.c "Хм..."
    mc.c "Тоже хочешь, чтобы за тобой ухаживали? Могу намазать тебе нос кремом, если хочешь."
    show molly smile talk
    molly.c "Ой, хе-хе~ Нет, пожалуйста. Представляешь?"
    show molly thinking
    molly.c "Я просто задумалась..."
    show molly neutral talk
    molly.c "*Вздыхает* Сегодня на работе меня особо отметили, вывели перед всем офисом."
    molly.c "Отметили за мои усилия с недавним клиентом и делом."
    show molly neutral
    mc.c "Эй, здорово! Это мы сегодня отмечаем?"
    show molly neutral talk
    molly.c "Да, я была очень довольна."
    show molly thinking
    molly.c "Но когда вспоминаю, как меня описали..."
    show molly bashful talk
    molly.c "Я была... «сильной, властной, профессиональной»... и «полностью держала под контролем целый зал мужчин»."
    show molly bashful
    mc.c "Это... хорошо? Тебя похвалили за отличную работу, верно?"
    show molly thinking
    molly.c "Да... Приятно получить признание, но как женщине мне от этого не очень хорошо..."
    mc.c "Ну же, ты знаешь, что я ничего плохого в этом не вижу."
    show molly bashful talk
    molly.c "Знаю, но если посмотреть на них... Она моя полная противоположность. «Сильная и властная»..."
    molly.c "Разве большинство мужчин не предпочли бы милое свидание с хрупкой девушкой?"
    show molly bashful
    mc.c "Знаешь, та сцена..."
    "Я оглядываюсь, чтобы убедиться, что нас не слышат."
    mc.c "Фу!"
    "Я изображаю рвотный позыв, будто проталкиваю палец в горло."
    show molly smile talk 2
    molly.c "Ха-ха-ха~ Боже мой! Как грубо..."
    show molly smile
    mc.c "Серьёзно, такие сцены — мой ночной кошмар. Мне гораздо больше нравится то, что есть у нас. Это куда искреннее."
    show molly smile talk
    molly.c "Ладно, ладно... От тебя другого ответа я и не ждала..."
    show molly smile
    mc.c "Мне гораздо больше нравится моя умная, целеустремлённая, успешная и красивая женщина рядом."
    show molly tease talk
    molly.c "Ох~ Ну всё, достаточно, [mc.name]..."
    show molly tease
    mc.c "Теперь я буду говорить это чаще, имей в виду."
    show molly tease
    molly.c "Дурачок..."
    show molly smile talk
    molly.c "Наверное, я могла бы быть чуть более женственной... Я даже всё ещё в костюме."
    show molly smile
    mc.c "Тут мало что поделаешь. Хотя можешь оставить у меня кое-какие вещи."
    show molly smile talk 2
    molly.c "Я знаю, спасибо. Вообще-то... на днях в обеденный перерыв я купила ещё несколько повседневных вещей."
    show molly thinking
    molly.c "Хотя кое-что из них... Хм... Возможно, получилось чересчур в другую сторону."
    mc.c "Теперь мне интересно..."
    show molly tease talk
    molly.c "Я так и думала. Но я пока не уверена."
    show molly tease
    mc.c "Узнать можно только одним способом... Назовём это «тестом [mc.name]»."
    show molly tease talk
    molly.c "Если тестировать будешь ты... Они всё ещё в моей машине."
    show molly tease
    "Сегодня она и так ночует у меня. Идеальная возможность."
    mc.c "Теперь мне не терпится."
    show molly tease talk
    molly.c "Тогда поедем к тебе?"
    show molly tease
    "Мы киваем и встаём. Пока Молли собирает вещи, я стираю немного сахарной пудры с тарелки и мажу ей влажный нос."
    show molly surprise
    molly.c "Ах!"
    show molly tease talk
    molly.c "Хе-хе~ [mc.name]... О боже..."
    scene black with fade
    call stopMusic from _call_stopMusic_35
    "Мы возвращаемся ко мне. Молли останавливается у машины и забирает несколько вещей, включая один загадочный пакет... Наверное, там её наряд."
    "Что же там может быть?"
    $ location_home.showBackground()
    call playMusic(heartTheme) from _call_playMusic_197
    show molly smile with dissolve
    "Зайдя внутрь, Молли снимает туфли и заглядывает в сумку."
    show molly thinking
    molly.c "Хм, даже не знаю, о чём я думала, когда покупала это..."
    mc.c "Теперь мне ещё интереснее. Уверен, ты будешь выглядеть потрясающе."
    show molly smile talk
    molly.c "Ладно... Только для тебя."
    hide molly with dissolve
    "Молли уходит за угол переодеться."
    "Проходит несколько минут, полных предвкушения."
    molly.c "Ну вот..."
    scene mollyhevent5i1 with fade
    pause
    "Молли застенчиво выходит в милом наряде, и я сразу замечаю открытые участки меха."
    "Милая зелёная блузка и клетчатая юбка... Типичный милый, женственный повседневный образ."
    mc.c "Ничего себе, Молли, ты потрясающе выглядишь!"
    molly.c "Ох, почему-то в магазине юбка казалась подлиннее... Я просто обрадовалась, что она налезла на талию..."
    mc.c "Короткая юбка — это неплохо..."
    molly.c "Она, конечно, очень женственная... Но... не знаю... Может, в [molly.age] уже не стоит такое носить..."
    mc.c "Ты с ума сошла. Послушай себя."
    mc.c "Ты прекрасно выглядишь, серьёзно. Очень мило."
    molly.c "Угу..."
    "Неудивительно, что при таком виде меня накрывает."
    mc.c "Скажи, что делают милые хрупкие девушки?"
    molly.c "Хм... Носят платья?"
    call playMusic(sexyTheme) from _call_playMusic_198
    mc.c "Они садятся парню на колени."
    "Я сажусь на край кровати и жестом зову Молли."
    "Молли сильно краснеет, но всё же подходит. Я помогаю ей сесть ко мне на колени верхом."
    scene mollyhevent5i2 with fade
    pause
    molly.c "Правда? Я ведь тебя раздавлю..."
    mc.c "Никогда, моя маленькая цветочная фея весит меньше пёрышка."
    molly.c "Не такая уж я и маленькая фея..."
    "Мягкие бёдра Молли прижимаются ко мне, её нежные ляжки обвивают мою талию, а я чувствую её упругую задницу сквозь юбку... Я..."
    molly.c "Ох... [mc.name], ты..."
    "Да, я возбуждён... Мой член очевидно упирается в неё."
    mc.c "А кто устоит перед такой милашкой?"
    molly.c "Не думаю, что от слова «милая» у тебя должен вставать..."
    mc.c "Тогда чертовски сексуальная. Не могу с собой совладать."
    "Я обхватываю её ягодицы и приподнимаю новую юбку."
    molly.c "О-ох, ничего себе~ И правда, вот и всё, что понадобилось?"
    image mollysex clothed cowgirl 1 = Movie(play="images/characters/molly/hscenes/cowgirl/part1.webm")
    show mollysex clothed cowgirl 1 with fade
    pause
    "Отодвинув трусики, я высвобождаю член из ширинки и погружаюсь в тёплые объятия Молли."
    molly.c "О-о боже... [mc.name]~"
    molly.c "Ты правда не мог подождать? Дай мне хотя бы раздеться..."
    mc.c "Не могу ждать... Ты слишком соблазнительная."
    "Молли тихо стонет от удовольствия, медленно покачиваясь у меня на коленях и обвивая меня мягкими шелковистыми бёдрами."
    "Я ощущаю весь её вес, когда она опускается на меня, крепко сжимая член влажной киской."
    image mollysex clothed cowgirl 2 = Movie(play="images/characters/molly/hscenes/cowgirl/part2.webm")
    show mollysex clothed cowgirl 2 with fade
    pause
    molly.c "М-мм~ [mc.name]~"
    molly.c "Ты помнёшь мою новую одежду..."
    mc.c "Готов на такую цену. Ты в ней невероятно сексуальна."
    molly.c "А-а~ Спасибо... Кажется, я понимаю~ М-мм~ о чём ты~"
    "Я крепко сжимаю её пышную задницу и прижимаю Молли к себе. Она обнимает меня, нежно и уютно."
    molly.c "Тебе... не больно внизу?"
    mc.c "Более чем нормально. Иди сюда."
    "Я откидываюсь назад и помогаю Молли оседлать меня."
    image mollysex clothed cowgirl 3 = Movie(play="images/characters/molly/hscenes/cowgirl/part3.webm")
    show mollysex clothed cowgirl 3 with fade
    pause
    "Я ложусь на спину, а Молли опирается на мою грудь."
    "Я подбадриваю её, и она начинает подпрыгивать на моём члене, вздрагивая и полностью накрывая меня сверху."
    molly.c "А-а~ М-мм~"
    "Я почти срываю с неё блузку и задираю лифчик, открывая её великолепную грудь."
    molly.c "О-ох~ М-мм~ [mc.name]~"
    "Её глаза закатываются от удовольствия. Она постепенно увлекается и ускоряется, пока я подаюсь ей навстречу."
    image mollysex clothed cowgirl 4 = Movie(play="images/characters/molly/hscenes/cowgirl/part4.webm")
    show mollysex clothed cowgirl 4 with fade
    pause
    "Из неё текут сладкие соки, а я глубоко вхожу в киску. Её стенки вздрагивают с каждым толчком."
    "Её большая лапа вцепляется в мою рубашку, царапает грудь и прижимает меня к кровати."
    molly.c "Ха-а~ Ха-а~ [mc.name]~ [mc.name]~"
    "Я весь в поту, полностью сдавлен и окружён большой горячей Молли."
    "Ощущения и наслаждение настолько сильные, что я уже не могу скрывать эмоции."
    molly.c "М-мм~ [mc.name]~ После всего этого мне, наверное, не стоило быть сверху... М-мм~ Правда?"
    "Что за глупости. Я больше ничего и желать не могу."
    "Пора показать ей, какое удовольствие можно получить в таком положении."
    mc.c "Именно так. Особенно когда я могу сделать вот это!"
    image mollysex clothed cowgirl 5 = Movie(play="images/characters/molly/hscenes/cowgirl/part5.webm")
    show mollysex clothed cowgirl 5 with fade
    pause
    "Я обнимаю Молли и притягиваю её к себе, прижимая к груди."
    "Упираясь в кровать, я изо всех сил толкаюсь вверх, врезаясь в бёдра Молли под непристойный ритм."
    molly.c "А-а-а~! А-а-а~! О-о-ох~!"
    molly.c "[mc.name]~ [mc.name]~ [mc.name]~~!"
    "Прижатый к её груди, я едва могу дышать и тяжело пыхчу, вкладывая в Молли всю силу."
    "Она яростно подпрыгивает на моих бёдрах, принимая член целиком с каждым толчком."
    molly.c "Ха-а~ Ха-а~ А-а-а~"
    "Удовольствие нарастает. Мы оба тяжело дышим от первобытной страсти."
    molly.c "Я... М-мм... Я..."
    "Отсюда мне не вырваться: весь вес Молли придавил меня к кровати, она полностью поглотила меня."
    "Я не могу остановиться."
    mc.c "Молли!"
    molly.c "М-м-м~ Давай~!"
    scene mollycowgirlfinish with fadewhite
    pause
    molly.c "А-а-а-а-а~~~~!"
    "Последним толчком я глубоко вхожу в Молли и изливаю в неё огромную порцию спермы."
    "Молли содрогается от удовольствия и кричит, а мы оба крепко обнимаем друг друга в экстазе."
    "Сперма стекает по моему члену, бёдра Молли вздымаются и опускаются с каждым вздохом. Мы оба отчаянно пытаемся отдышаться."
    "Я зажат всей массой Молли, лицом уткнулся ей в грудь и уже не могу шевелиться. Да и не хочу."
    "Неплохой способ умереть..."
    molly.c "Хо-о~ [mc.name]~"
    molly.c "Не могу~ Ха-а~ поверить, как это хорошо~ Ха-а~"
    "Я могу только промычать что-то между грудей Молли."
    mc.c "М-мф."
    molly.c "Ох... О-ох~ Прости..."
    scene black with fade
    "Наконец она приходит в себя настолько, чтобы скатиться с меня и упасть на кровать."
    "Мы лежим неподвижно и тяжело дышим ещё какое-то время."
    call playMusic(heartTheme) from _call_playMusic_199
    scene mollypillowtalk with fade
    "В конце концов мы переворачиваемся на живот и встречаемся лицом к лицу."
    "Молли снимает остатки одежды, уцелевшие после нашей близости."
    molly.c "Мой бедный наряд..."
    mc.c "Похоже, я немного увлёкся. Прости, Молли... Ты так чертовски хорошо выглядела."
    mc.c "Если одежду уже не спасти, куплю тебе новую."
    molly.c "Хе-хе~ Всё нормально. Когда выбирала её, я не ожидала {i}такой{/i} реакции."
    molly.c "К тому же... оно того стоило... Это было невероятно~"
    mc.c "Ещё бы. Всегда того стоит."
    molly.c "Хм-хм~"
    "Наступает ночь, и от усталости у нас слипаются глаза."
    molly.c "*Зевает* Пожалуй, на сегодня хватит... Завтра рано вставать..."
    mc.c "Я бы ещё мог продолжить. В той сумке есть что-нибудь ещё более откровенное?"
    molly.c "Хм-хм~ Нет, [mc.name]... Веди себя прилично~"
    call stopMusic from _call_stopMusic_36
    scene black with fade
    "Наконец мы забираемся под одеяло, обнимаемся и засыпаем."
    "Сладких снов с моей милой девушкой."

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return

label mollyHEvent6(fromGallery):
    $ location_home.showBackground()
    "Дела по дому, дела по дому..."
    "Навести порядок, убраться, вскрыть письма, которые наверняка окажутся счетами..."
    "Неужели нам суждено вечно находить себе дела?"
    "Но за этот бардак в этот раз отвечаю не только я. Вчера вечером у меня была компания..."
    call playMusic(barTheme) from _call_playMusic_200
    scene mollyhevent6i1 with fade
    pause
    "Молли нежится в кровати. Очень милое зрелище."
    "Она осталась у меня на ночь — такое и раньше случалось редко, но постепенно становится привычнее, и теперь мы проводим вместе выходные."
    "На следующий день ей не нужно работать, поэтому гостиница от работы ей не полагается. Она осталась просто потому, что сама захотела, и это приятно."
    "Я замечаю, как Молли немного шевелится. Она уже проснулась, но всё ещё вымотана. Я дал ей отдохнуть."
    mc.c "Ну как, Молли?"
    molly.c "М-м~"
    mc.c "Я никогда не видел, чтобы ты так долго спала. А мне вообще-то надо пропылесосить."
    molly.c "Потом, [mc.name]... Дай мне отдохнуть... Неделя была долгой."
    mc.c "Ладно, ладно. Отдыхай сколько хочешь. Тебе никуда не надо."
    molly.c "Может... Потом всё-таки встану..."
    molly.c "Мне не спать надо, просто дай полежать..."
    "Бедняжка. Я бы в жизни не смог работать {i}так{/i} много."
    "Приятно, что она здесь и мы можем спокойно провести больше времени вместе, но это заставляет задуматься..."
    mc.c "Молли, ты обычно уезжаешь домой в пятницу вечером... Родные не удивляются, когда ты остаёшься на выходные?"
    scene mollyhevent6i2 with fade
    pause
    molly.c "Удивляются? Чему?"
    mc.c "Ну... Почему ты не едешь домой, если не работаешь. Где ты ночуешь..."
    mc.c "Наверное, я спрашиваю, рассказала ли ты им обо мне?"
    molly.c "Конечно, глупыш! Мне пришлось объяснить, где я ночую, когда я стала реже ездить домой."
    molly.c "С тех пор мама постоянно спрашивает о тебе..."
    mc.c "А сёстры?"
    molly.c "Фу-у... Да, они тоже знают, хотя {i}им-то{/i} особо неинтересно."
    mc.c "Правда?"
    molly.c "Я упоминала... Нас с тобой, то есть... Но они не придали этому значения."
    molly.c "Учитывая, как быстро закончились мои прошлые отношения, если они вообще о них узнавали, думаю, они и не ждут ничего серьёзного."
    mc.c "Ох..."
    molly.c "Ой! Я не это имела в виду! Просто... Они не знают, насколько ты другой. Я не так уж много с ними говорила о нас, когда мы по-настоящему..."
    molly.c "Они просто очень заняты. Слишком заняты, чтобы особо интересоваться младшей сестрой..."
    mc.c "Уверен, это не так..."
    molly.c "Не знаю. Они, наверное, работают не меньше меня. Наоми помолвлена, у неё полно дел с подготовкой..."
    mc.c "Что ж, передай ей мои поздравления."
    molly.c "Брак... Серьёзное обязательство, наверное, много хлопот..."
    "Ой-ой. Не ожидал, что разговор станет таким серьёзным."
    "Не лучшее время для этого, да? Она застала меня врасплох, и я не знаю, что ответить."
    scene mollyhevent6i1 with fade
    pause
    "К счастью, она переворачивается на другой бок и снова засыпает. Надеюсь, она ничего такого не имела в виду..."
    "Мы никуда не собираемся, так что я заканчиваю уборку."
    scene black with fade
    "Я быстро убираюсь на кухне и возвращаюсь: Молли уже немного приподнялась."
    scene mollyhevent6i3 with fade
    pause
    "Она проснулась, поэтому я сажусь на край кровати."
    mc.c "Доброе утро."
    molly.c "Хе-хе~ Почти. Прости, что сегодня со мной скучно. Как будто я сама лишаю смысла встречаться с тобой на выходных..."
    mc.c "Да брось, совсем нет. Даже смотреть, как ты спишь, — отдых для глаз."
    molly.c "Хм..."
    "Молли приподнимается и листает телефон."
    "Она не из тех, кто бездумно листает соцсети, значит, это может означать только одно..."
    mc.c "Только не говори, что это рабочая почта."
    molly.c "Э-э... Ну..."
    mc.c "Только один заслуженный сон подольше — и ты снова за работу?"
    molly.c "Я... Это просто рефлекс... Я всё время проверяю."
    mc.c "Цок-цок. Я велел тебе отдыхать. Плохая девочка..."
    "Я слегка шлёпаю её по заднице. Пышные ягодицы очень приятно покачиваются под пижамой."
    scene mollyhevent6i4 with fade
    pause
    molly.c "О-ой! [mc.name]!"
    molly.c "Ладно, ладно~ Ты прав..."
    mc.c "Настоятельно требую, чтобы ты отдыхала, пока ты здесь."
    call stopMusic from _call_stopMusic_37
    "Эти коротенькие шортики подрагивают, пока она покачивается. Кажется, они вот-вот лопнут, пытаясь удержать всю эту задницу..."
    call playMusic(sexyTheme) from _call_playMusic_201
    "В этом есть что-то особенное... Я не могу оторвать взгляд."
    "Молли закатывает глаза, заметив, как я на неё пялюсь."
    molly.c "Хм? Ну что, [mc.name]?"
    "Я... Э-э... Мне надо..."
    mc.c "Вообще-то, тебе следует просто лечь вот здесь... Вот так..."
    molly.c "Интересно почему~"
    "Я хватаю ладонью её мягкую плоть и чувствую тёплый пушистый мех. У меня уже встаёт."
    molly.c "Хм... Что ты задумал?"
    mc.c "Чтобы помочь тебе расслабиться, позволь мне сделать тебе {i}массаж{/i}."
    molly.c "{i}Массаж{/i}, да? Плечи? Спину? Интересно..."
    mc.c "Я думал о другом..."
    molly.c "Хе-хе~ Ну... Раз уж всю работу будешь делать ты..."
    molly.c "Мне просто лежать и наслаждаться... Звучит {i}приятно{/i}."
    "Я обхватываю её задницу, медленно стягиваю шорты и оседлываю свою большую прекрасную медведицу."
    image mollysex pronebone 1 = Movie(play="images/characters/molly/hscenes/pronebone/part1.webm")
    show mollysex pronebone 1 with fade
    pause
    "Снимаю брюки и с приятным шлепком провожу эрегированным членом по её ягодицам."
    molly.c "Хм... Быстро же..."
    mc.c "Всегда готов к службе."
    "Я медленно провожу членом вверх-вниз, раздвигая тонкие клочки меха головкой и нежно сжимая его между огромных мясистых ягодиц."
    "Молли улыбается, оборачиваясь через плечо, и слегка поднимает зад."
    molly.c "Для кого же на самом деле этот {i}массаж{/i}, а?"
    mc.c "Скоро почувствуешь его эффект."
    "Я раздвигаю ей ягодицы и открываю киску Молли, уже блестящую от возбуждения."
    image mollysex pronebone 2 = Movie(play="images/characters/molly/hscenes/pronebone/part2.webm")
    show mollysex pronebone 2 with fade
    pause
    "Я вхожу в её влажную киску и не могу сдержаться, начиная двигаться в ровном ритме."
    molly.c "А-а-а~ Боже мой... [mc.name]~"
    "Проникая в неё, я чувствую, как крупная задница Молли трётся обо мне. Сочетание ощущений невероятное."
    "Её задница слегка подпрыгивает от моих толчков. Молли напрягает плечи, пока я вхожу как можно глубже."
    molly.c "М-м~ Так~ правда хорошо~ Вот так~"
    "Я едва могу оседлать её широкие бёдра, а огромная задница раздвигается, принимая мой член."
    "Я вижу, как она выгибается от удовольствия, и чувствую её стоны всем телом. Голова идёт кругом от наслаждения."
    "Но чтобы по-настоящему её удовлетворить, нужно сменить положение."
    mc.c "Кажется, тебе нужна более основательная процедура."
    image mollysex pronebone 3 = Movie(play="images/characters/molly/hscenes/pronebone/part3.webm")
    show mollysex pronebone 3 with fade
    pause
    "Перебравшись в положение лёжа, я могу хорошенько прижать Молли и глубоко входить между её ягодиц."
    molly.c "А-а~! О-ох~ М-мм~"
    molly.c "Да~~ [mc.name]~ Так глубоко~"
    "Её огромная задница покачивается от каждого толчка, а милая Молли сдерживает крики удовольствия, пока я вхожу и выхожу."
    "Её бёдра вздрагивают, киска крепко сжимается при каждом толчке, а между ягодиц становится скользко от соков."
    molly.c "А-а-а~ А-а-а~ М-мм~"
    "Молли хватается за кровать, совершенно теряя самообладание."
    image mollysex pronebone 4 = Movie(play="images/characters/molly/hscenes/pronebone/part4.webm")
    show mollysex pronebone 4 with fade
    pause
    mc.c "Достаточно хорошо?"
    molly.c "О боже~ Да-а-а~ Не останавливайся~"
    "Раздаются влажные шлепки и скрип кровати, когда под моим весом Молли вдавливается в матрас."
    "Милая Молли подо мной, беззащитная и полностью в моей власти. Я контролирую всё и трахаю её сзади."
    "Её мягкая мясистая задница содрогается и сжимает меня, горячий мокрый мех липнет к коже."
    "Невероятная поза, Молли прижата к кровати. Я теряю голову от животной страсти. Мне нужно вколачиваться в неё."
    image mollysex pronebone 5 = Movie(play="images/characters/molly/hscenes/pronebone/part5.webm")
    show mollysex pronebone 5 with fade
    pause
    molly.c "А-а-а~ М-м-мм~ О-о-ох~"
    "Я падаю на неё сверху и быстро трахаю, словно животное в течке."
    "Голова кругом, я мечусь и ищу, за что бы ухватиться."
    "Зарываюсь лицом ей в шею, покрываю поцелуями и хватаюсь за морду Молли. Она широко открывает рот и стонет от наслаждения."
    molly.c "А-а~ А-а-а~ А-а~"
    molly.c "М-мм~~ [mc.name]~ Я сейчас~"
    "Я тоже уже близко. Из паха поднимается обжигающий жар."
    mc.c "Я..."
    molly.c "А-а~ М-мм~ [mc.name]~ М-мм~ О-о-о-о-ох~"
    "Молли содрогается, и я тоже срываюсь."
    scene mollypronebonefinish1 with fadewhite
    pause
    molly.c "А-а-а-а-а~!"
    "В последний момент я приподнимаюсь и изливаю густую струю на задницу Молли."
    "Кажется, поток бесконечен, а Молли подо мной вздрагивает от экстаза."
    scene mollypronebonefinish2 with fade
    pause
    "Соки растекаются по её пушистым ягодицам. Она слегка покачивается, переводя дыхание."
    molly.c "Хо-о~ [mc.name]..."
    "Она делает несколько глубоких вдохов и оглядывается на меня через плечо."
    molly.c "Ничего себе~ Это было... невероятно..."
    mc.c "Блядь... Никогда ничего подобного не чувствовал."
    molly.c "И так скоро с утра? Вот это да~"
    mc.c "Ты же знаешь, я всегда готов. К тому же утро уже почти {i}закончилось{/i}."
    mc.c "Кажется, после такой основательной порки я дал тебе повод ещё немного поваляться."
    molly.c "Хе-хе~ Вообще-то, должна признаться, я получила огромное удовольствие. И почему-то чувствую себя... удивительно бодрой."
    molly.c "Сначала пойду в душ... А потом нам стоит куда-нибудь выбраться сегодня."
    scene black with fade

    if(not fromGallery):
        $ molly.addLike(1)
        $ molly.addLove(1)

    return

label mollyLikeEvent4Invitation(fromGallery):
    call playMusic(heartTheme) from _call_playMusic_202
    show molly smile
    "Думаю, уже можно без преувеличений сказать, что мы безумно влюблены..."
    "Наши ночи вместе были волшебными, словно во сне. И с тех пор всё только лучше."
    "Она быстро привыкла оставаться у меня на ночь. Теперь относится к этому куда спокойнее..."
    "Похоже, гостиницы остались в прошлом. Если она в городе, то ночует у меня — даже когда приезжает не по работе. Просто ради нас."
    "И всё же мы проводим вместе меньше времени, чем мне хотелось бы. Большинство выходных она проводит дома, а я не хочу, чтобы она тратила выходные на дорогу сюда."
    "Я думал об этом, когда мы были вместе в отъезде, но так и не заговорил об этом."
    "Если мы хотим проводить больше времени вместе и сблизиться... надо просто жить поближе."
    "Она работает здесь, но экономит, живя у родителей. Как-то раз она упомянула, что в будущем, возможно, купит собственное жильё."
    "Это дорогое удовольствие, но с её работой, наверное, она может себе позволить... Купит в городе? Просто поблизости? Всё равно будет ездить на работу?"
    "И мы всё равно не сможем видеться каждый день?"
    "Если таковы её планы, пусть делает что хочет. Но если говорить эгоистично... я хочу, чтобы она жила здесь."
    "Здесь, со мной."
    "Если подумать, необязательно выбирать что-то одно. Не обязательно всё так сильно менять."
    "Она всё ещё может ездить домой по выходным или в любые другие дни. Может, её и сейчас всё устраивает."
    "Но... я бы хотел, чтобы и мой дом стал для неё родным."
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Yes!' if(homeHasRoom) else "Нужно улучшить жильё"
    if(not fromGallery):
        menu:
            "Предложить Молли переехать ко мне? Этот выбор можно сделать когда угодно."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "Пока нет":
                call endCharacterInteraction(molly) from _call_endCharacterInteraction_4
    "Уверен, она отнесётся к этому практично. Посмотрим, что она скажет."
    mc.c "Молли, ты знаешь, чем займёшься в следующие выходные? Ты говорила, что пока не решила."
    show molly thinking
    molly.c "Ой, точно... Что же там..."
    show molly smile talk 2
    molly.c "А, да! Мама с папой {i}и правда{/i} пойдут на вечеринку, которую устраивают их друзья."
    molly.c "Они сказали, что решили съездить туда и остаться на ночь. До последнего не знали, стоит ли."
    show molly smile
    mc.c "Ясно. А ты, кажется, не собиралась с ними?"
    show molly thinking
    molly.c "Могла бы... Я их знаю, но там будут одни старики..."
    mc.c "Старики? Ха-ха."
    show molly smile talk
    molly.c "Ты понимаешь, о чём я. Только их старые друзья... Решила оставить их в покое."
    show molly tease talk
    molly.c "Я бы лучше воспользовалась этим как поводом остаться у тебя на выходные, если ты не против."
    show molly tease
    mc.c "Конечно! Мне кажется, мы давно не виделись."
    show molly smile talk
    molly.c "Да... Не хочу навязываться тебе {i}каждые{/i} выходные."
    show molly smile
    "Как же она ошибается... Я хочу, чтобы она была здесь постоянно. Самое время поговорить."
    mc.c "Ты никогда не навязываешься. Ну... разве что заслоняешь мне солнце."
    show molly smile talk 2
    molly.c "Тише... Злюка..."
    show molly smile
    mc.c "Ты всегда желанный гость — когда захочешь и на сколько захочешь."
    mc.c "Честно говоря... Я хочу сказать..."
    mc.c "Может, ты... хотела бы переехать ко мне? По-настоящему, насовсем?"
    show molly surprise
    molly.c "Переехать к тебе?"
    mc.c "Ну да... Ты постоянно мотаешься туда-сюда. Работаешь здесь..."
    mc.c "Ты и так всегда можешь оставаться у меня... Получается, ты почти уже переехала, но... Не знаю. Я хотел спросить."
    mc.c "Необязательно что-то сильно менять... Просто... Считай мой дом своим..."
    show molly tease talk
    molly.c "Ох, [mc.name]~"
    show molly joy
    molly.c "Это так мило! Боже мой!"
    show molly smile talk
    molly.c "Я... Ох, что сказать?"
    molly.c "Ты уверен, [mc.name]?"
    show molly smile
    mc.c "Что ты имеешь в виду?! Конечно, уверен! Я ничего не хочу сильнее. Но только если ты сама этого хочешь."
    show molly smile talk
    molly.c "[mc.name]~"
    hide molly with dissolve
    show molly hug with dissolve
    "Она подходит и крепко обнимает меня, почти полностью погребая в своих объятиях."
    molly.c "[mc.name]... Я бы очень этого хотела..."
    mc.c "Правда? Я так рад, но... твоя семья..."
    molly.c "Я же не навсегда от них уезжаю! У меня всегда останется своя комната, я уверена."
    molly.c "Буду время от времени ездить домой! Как ты и сказал, почти ничего не должно измениться."
    molly.c "Но я бы с радостью считала тебя и твой дом своим {i}домом{/i}."
    mc.c "Молли..."
    show molly kiss with dissolve
    molly.c "Муа~"
    "Я наклоняю её ко мне, и мы долго целуемся."
    show molly hug with dissolve
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Ты знаешь, ещё [len(girlsAlreadyMovedIn)] девушек почти переехали ко мне, но ты, возможно, не со всеми знакома..."
        if(katie.movedIn and katieMollyDuoStoryEvent1.unlocked):
            mc.c "Ну, Кэти ты, конечно, уже знаешь."
            molly.c "Да, знаю, как ей здесь нравится~"
        if(grace.movedIn and graceMollyDuoStoryEvent1.unlocked):
            mc.c "Ещё Грейс. Кажется, вы неплохо ладите."
            molly.c "Ага! Мы уже говорили об этом."
        mc.c "Тебя... всё это устраивает?"
        molly.c "Конечно, [mc.name]. Я всё понимаю!"
    hide molly with dissolve
    show molly tease with dissolve

    mc.c "Тогда считай всё моё — своим."
    show molly tease talk
    molly.c "Хе-хе~ Так и буду."
    show molly tease
    mc.c "Так что... когда захочешь. Что нужно будет сделать? Помочь тебе с переездом?"
    show molly smile talk 2
    molly.c "Нет, нет, думаю, не нужно. У меня здесь и так уже немало одежды..."
    molly.c "Так что только кое-какие рабочие вещи, учебные материалы... Пара сумок, наверное. У меня ведь нет собственной мебели."
    show molly smile talk
    molly.c "В следующий раз, когда поеду сюда, просто привезу вещи. Может, за пару поездок."
    show molly smile
    mc.c "Не могу дождаться."
    show molly tease talk
    molly.c "Я тоже~"
    scene black with fade
    "Вот и всё. Она согласилась!"
    "Она сказала, что привезёт несколько вещей через пару дней, и с тех пор это будет её новый дом..."
    "Дело решено. Отметь в календаре!"

    return

label mollyLikeEvent4(fromGallery):
    call playMusic(memoriesTheme) from _call_playMusic_203
    $ location_home.showBackground()
    "Полы пропылесосил; ванную вычистил; спальню прибрал."
    "Больше уже нечего делать. Я с самого утра на ногах в предвкушении. Сегодня приезжает Молли."
    "Она официально переезжает ко мне... Мы делаем огромный шаг вместе."
    "Сейчас она у родителей, собирает кое-какие вещи и сегодня приедет."
    "Она сказала, что выедет утром, но время в пути может отличаться. За рулём она не сможет писать или звонить."
    "Так что я просто сижу и верчу пальцами, не зная, чем себя занять, и жду звонка в дверь."
    "Я вне себя от радости и одновременно нервничаю..."
    "А вдруг ничего не выйдет? А вдруг ей не понравится? Она так сильно меняет свою жизнь ради меня."
    "Хочу, чтобы всё было идеально. Сделать бы хоть что-нибудь."
    "Но я беспомощно сижу тут. Она даже не позволила мне помочь. Она всё равно едет на своей машине..."
    "..."
    scene black with fade
    "Хожу по дому кругами, ничего полезного не делаю..."
    "*Дзынь-дон*"
    "Это она!"
    scene mollylikeevent4i1 with fade
    pause
    "Я открываю дверь своей красавице. Она приехала с чемоданом. Теперь до меня по-настоящему дошло... Всё действительно происходит."
    molly.c "[mc.name]!"
    mc.c "Добро пожаловать домой."
    molly.c "Хе-хе~"
    scene mollylikeevent4i2 with fade
    pause
    "Молли крепко обнимает меня и прижимает к пышной пушистой груди."
    molly.c "[mc.name]! Я правда приехала! Мы это сделали!"
    "Она сжимает меня так крепко, что я не могу вдохнуть, уткнувшись лицом ей в грудь. Ответить не получается."
    molly.c "Была небольшая пробка. Я хотела написать, когда приеду, но решила сделать тебе сюрприз!"
    mc.c "Мф-ф..."
    molly.c "А? О-ох..."
    scene mollylikeevent4i3 with fade
    pause
    molly.c "...Прости."
    mc.c "Фух~ Ничего страшного. Вообще-то, теперь я каждый день жду таких объятий."
    molly.c "М-мм~ Теперь-то мы сможем обниматься каждый день, правда, [mc.name]..."
    mc.c "Я так рад, что ты здесь. Помочь тебе с чем-нибудь?"
    molly.c "В машине осталось ещё несколько вещей. Не поможешь?"
    mc.c "Конечно."
    scene black with fade
    "Остаётся всего пара раз сходить за остальными сумками и парой небольших коробок."
    "Одежда, рабочие вещи, мелочи и довольно тяжёлая коробка с увесистыми книгами по праву."
    scene mollylikeevent4i4 with fade
    pause
    "Когда мы всё заносим, Молли тут же принимается за дело."
    mc.c "Не обязательно разбирать всё прямо сейчас. Расслабься! Ты уже дома."
    molly.c "Раз уж начали, [mc.name]! Давай не откладывать на потом."
    mc.c "В моём доме принято как можно больше отдыхать. Тебе ещё предстоит этому научиться."
    molly.c "Хе-хе~ Постараюсь привыкнуть."
    "Она раскладывает одежду по новым местам, ищет, куда убрать вещи."
    "Когда зубная щётка оказывается в стакане в ванной, тут-то всё и становится по-настоящему..."
    molly.c "Кажется, нам понадобится ещё один комод, как думаешь?"
    mc.c "Конечно, купим."
    molly.c "Можем выбрать его вместе~"
    "Так здорово смотреть, как моя девушка обживается..."
    "Видеть её вещи вокруг, её одежду, которую «не жалко испачкать»..."
    "Что-то во всём этом кажется совершенно правильным."
    scene mollylikeevent4i5 with fade
    pause
    "Следующее время мы распаковываем вещи и решаем, что ещё нужно купить для дома."
    "Это ещё не всё, но пока хватит. Время от времени она будет ездить домой. Но сейчас она здесь."
    molly.c "Фух~ Спасибо, [mc.name]! Пока сойдёт!"
    mc.c "Молодец."
    scene mollylikeevent4i6 with fade
    pause
    "Молли обнимает меня за плечи, сияя тёплой улыбкой."
    molly.c "С тех пор как я уехала учиться в колледж, я впервые живу не дома... Мне... немного тревожно."
    mc.c "Не обязательно что-то сильно менять. Главное, теперь твоя любимая кровать вот здесь."
    molly.c "Да... Я очень рада, что больше не придётся так долго ездить..."
    molly.c "Смогу возвращаться домой в нормальное время... Спать чуть дольше... И на выходные я уже здесь..."
    mc.c "А ещё больше времени со мной, да?!"
    molly.c "Ага, это самое лучшее~"
    molly.c "Кстати о твоей кровати..."
    mc.c "О {i}нашей{/i} кровати."
    molly.c "Хе-хе~ Точно~"
    molly.c "Я всё думаю о {i}нашей{/i} кровати. Кажется, она даже удобнее моей. Может, полежим?"
    scene black with fade
    "Складываем последние коробки и возвращаемся в спальню поваляться."
    scene mollylikeevent4i7 with fade
    pause
    "Молли плюхается на кровать, потягивается и переворачивается."
    molly.c "М-мм~"
    mc.c "Устала?"
    molly.c "Немного, если подумать. Я даже сегодня утром ещё кое-что собирала."
    mc.c "Как прошло утро с родителями?"
    molly.c "Они отнеслись к этому как к чему-то совершенно обычному, ха-ха. Это я чуть не расплакалась."
    molly.c "Когда я впервые им сказала, они совсем не удивились. Словно давно этого ждали. Наверное, я много о тебе рассказывала..."
    molly.c "Они уже проходили через это с Эрикой и Наоми много лет назад... А я была младшенькой и просто за ними тянулась."
    mc.c "Ох..."
    molly.c "Хе-хе~ Ничего. Пожалуй, давно пора было."
    molly.c "И как ты сказал... Они не на другом конце света. Я буду навещать их, и моя комната всегда останется за мной."
    molly.c "Но быть я хочу именно здесь~"
    "Я сжимаю её ладонь."
    mc.c "Я люблю тебя."
    molly.c "Я тоже тебя люблю, э-э..."
    molly.c "Хм-м..."
    mc.c "Что такое?"
    molly.c "Ну, теперь, когда я здесь... Глупо просто называть тебя [mc.name]..."
    mc.c "Да ну?"
    molly.c "Хм... Надо было сразу сказать. Теперь только неловко получилось."
    mc.c "Ха-ха, что именно?"
    molly.c "...Я люблю тебя... М-милый..."
    mc.c "Ох..."
    scene mollylikeevent4i8 with fade
    pause
    "Я прикасаюсь к её морде и нежно притягиваю к себе для поцелуя."
    molly.c "М-м~"
    "Мы целуемся, смеёмся и снова целуемся..."
    scene black with fade
    "Мы ещё немного лежим рядом, обнимаемся и тихо болтаем. Я хочу, чтобы она почувствовала себя дома."

    if(not fromGallery):
        $ molly.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label mollyHEvent7(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_204
    $ location_home_lounge.showBackground()
    "После долгого дня я захожу в гостиную, мечтая рухнуть лицом на диван."
    "Едва зайдя с затуманенным взглядом, я слышу работающий телевизор."
    scene mollyhevent7i1 with fade
    pause
    molly.c "Добрый вечер, [mc.name]!"
    "Молли уже развалилась на диване и смотрит телевизор."
    "На ней... такой маленький для её фигуры топ и одни трусики?"
    mc.c "Привет, Молли. Давно ты вернулась?"
    molly.c "Да совсем недавно, только что быстро приняла душ."
    molly.c "Ты выглядишь уставшим. День был долгий?"
    mc.c "Немного, ничего страшного. Просто устал."
    molly.c "Ох... Иди сюда~"
    "Она вытягивает ноги и похлопывает по бёдрам, предлагая устроиться у неё на коленях."
    mc.c "Ты хочешь, чтобы я сел тебе на колени?"
    molly.c "Нет, глупыш! Мф... На них можно положить голову..."
    "Вот это звучит заманчиво."
    scene mollyhevent7i2 with fade
    pause
    "Я вытягиваюсь на диване, и массивные бёдра Молли становятся отличной подушкой."
    molly.c "Так лучше, милый~?"
    mc.c "Просто рай."
    molly.c "Хе-хе~"
    "Молли нежно гладит меня по голове, а я таю на этой чудесной подушке из мягкого шелковистого меха."
    mc.c "Только что из душа, да?"
    "Я бросаю взгляд на её обнажённое тело."
    molly.c "Ну да... Я весь день ходила в этих брюках... Не хотела снова ничего надевать после душа..."
    mc.c "Хоть совсем голой ходи, я не против."
    molly.c "Хм... Тебе бы это понравилось, да?.."
    "Меня со всех сторон окружает её мягкая плоть. Я погружаюсь в неё и не могу не заметить приятный аромат."
    mc.c "Ты приятно пахнешь."
    molly.c "Спасибо! Я купила новый шампунь."
    molly.c "Тот, что стоял у тебя, ужасный, [mc.name]... Что это за штука «пять в одном»?"
    mc.c "Делает своё дело."
    molly.c "Но не для леди..."
    mc.c "Ладно, согласен. Хороший выбор."
    "Молли гладит меня по голове и продолжает смотреть телевизор."
    "Такие трогательные моменты напоминают мне, что Молли теперь действительно живёт здесь. Это её дом не меньше, чем мой."
    "Я почти проваливаюсь в сон, окружённый её сладким ароматом и ощущая прикосновение ладони к голове. Но не даёт мне заснуть..."
    "Её бёдра у меня на шее и вид её огромной груди прямо надо мной."
    "Молли снова смотрит на меня."
    molly.c "Ты просто пялишься на меня... Не хочешь смотреть телевизор?"
    mc.c "Хм... Мне и так есть на что посмотреть."
    "Её грудь мягко покачивается, и она приподнимает бровь, поняв, что я имею в виду."
    molly.c "А... Понятно..."
    "Я пришёл домой совершенно измученным, но красота Молли, нежные прикосновения и ласковые слова снова меня взбодрили. Я в её чудесных руках."
    "Может, дело только в трусиках и сиськах, но в целом... я уже завёлся."
    "Кажется, Молли замечает, что у меня начинает вставать..."
    molly.c "[mc.name]... Это..."
    mc.c "Э-э... Возможно."
    molly.c "Понятно..."
    call playMusic(sexyTheme) from _call_playMusic_205
    molly.c "Хочешь, чтобы я...? Тебе ведь не помешало бы немного расслабиться после долгого дня..."
    "Ничего себе. Она и правда готова? Я боялся, что испортил приятный момент."
    mc.c "Ты... правда хочешь?"
    molly.c "Хе-хе~ Конечно, милый~"
    image mollysex nursing handjob 1 = Movie(play="images/characters/molly/hscenes/nursingHandjob/part1.webm")
    show mollysex nursing handjob 1 with fade
    pause
    "Молли ловко расстёгивает ширинку, и мой член вываливается наружу — уже эрегированный, будто поставил рекорд по скорости."
    molly.c "Хо-о~ И это всё, что понадобилось?"
    mc.c "Ты же меня знаешь... Особенно рядом с тобой..."
    molly.c "Что ж, польщена."
    "Не в силах устоять перед её покачивающейся грудью, я задираю маленький топ, открывая её во всей красе."
    "Я слегка сжимаю одну грудь, а другая опускается так близко, что её можно поцеловать."
    molly.c "О-ох! [mc.name]~"
    molly.c "Нежнее, пожалуйста~"
    "Она медленно водит рукой вверх-вниз по моему стволу, щекоча его свежим, чистым и шелковистым мехом."
    image mollysex nursing handjob 2 = Movie(play="images/characters/molly/hscenes/nursingHandjob/part2.webm")
    show mollysex nursing handjob 2 with fade
    pause
    "Я обвожу языком её соблазнительный коричневый сосок, уже затвердевший от ласк."
    molly.c "А-а~ Ох, [mc.name]~ Ты такой смешной иногда... М-м~"
    mc.c "Не отговоришь меня. Я бы мог заниматься этим вечно."
    molly.c "М-мм~ Кажется, я тебе верю..."
    "Я лежу и посасываю её грудь... Она окутывает меня почти материнским теплом..."
    "Она с улыбкой смотрит на меня, доставляя рукой невероятное удовольствие."
    "Я сжимаю, лижу, целую и покусываю её грудь. По её лицу видно, что ей тоже приятно."
    molly.c "М-мм~ Хе-хе~"
    molly.c "Продолжим?"
    mc.c "Пожалуйста."
    image mollysex nursing handjob 3 = Movie(play="images/characters/molly/hscenes/nursingHandjob/part3.webm")
    show mollysex nursing handjob 3 with fade
    pause
    "Молли сжимает мой член чуть крепче и начинает водить рукой вверх-вниз."
    "Подушечки лап и мех скользят по пульсирующему члену, который уже вот-вот разорвёт меня."
    "Я отвечаю ей тем же, разминая и посасывая грудь, пока её рука направляет мою голову."
    molly.c "Ха-а~ Осторожнее, [mc.name]~"
    mc.c "Прости, просто..."
    molly.c "Ничего~ М-мм~ Так приятно~"
    mc.c "Ха-а~ Молли, я сейчас..."
    molly.c "М-мм~ Хорошо~ Кончай~"
    "Молли ускоряет движения, собираясь выдоить меня досуха."
    scene mollynursinghandjobfinish1 with fadewhite
    pause
    mc.c "Хр-нн~!"
    "От последнего сжатия я взрываюсь от экстаза."
    "Моя голова всё ещё у неё между грудей. Я напоследок посасываю сосок, пока извергаю струю спермы вверх."
    molly.c "О-ох~!"
    scene mollynursinghandjobfinish2 with fade
    pause
    mc.c "Ха-а~ Ха-а~"
    mc.c "Ох, блядь, Молли..."
    molly.c "Хм-м~ Сегодня ты много кончил..."
    molly.c "Понравилось?"
    mc.c "Невероятно..."
    molly.c "Хе-хе~ Отлично~"
    "Сперма стекает по члену, а вся ладонь Молли залита ею."
    mc.c "Я сейчас приведу себя в порядок..."
    molly.c "Ага~"
    scene black with fade
    "Немного прибравшись и переодевшись, мы возвращаемся на диван и теперь просто обнимаемся перед телевизором..."

    if(not fromGallery):
        $ molly.addLove(1)

    return
