init offset = 3
default alice = Person(Character(name='Alice', who_color='#9f9ca5', image = 'alice'), 'Alice', '', 'alice', 'female', 23)

label initialiseCharacter_alice:
    python:
        alice.currentLocation = location_cafe
        location_cafe.occupants.extend([alice])
        alice.availableEvents = [aliceFirstMeetingEvent]

    return

label updateCharacterStatics_alice:
    python:
        # Personal attributes
        alice.species = 'House cat'
        alice.birthday = 2
        alice.job = 'Librarian'
        alice.giftLoves = [item_goldRing]
        alice.giftLikes = [item_book, item_candles, item_dress]
        alice.giftHates = [item_wine, item_videogame]

        # Skill attributes

        # Sexual attributes


        # Personal effects

        # Event attributes
        alice.events = [aliceFirstMeetingEvent, aliceLikeEvent1, aliceLikeEvent2, aliceLikeEvent3, aliceHEvent1, aliceHEvent2, aliceHEvent3, aliceHEvent4, aliceHEvent5, aliceHEvent6, aliceLikeEvent4, aliceVacation, aliceLikeEvent5, aliceHEvent7]
        alice.specialEvents = [sarahAliceDuoStoryEvent1, sarahAliceDuoStoryEvent2, sarahAliceDuoHEvent1, sarahAliceDuoHEvent2]
        alice.selfieOptions = ['beach1', 'bedroom1', 'bedroom2', 'bedroom3', 'homebedroom1']
        alice.wakeUpOptions = ['kiss', 'licking']
        alice.dateChats = ['Background', 'Hobbies']
        alice.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = alice.events[-1]
        alice.maxLike = lastStoryEvent.requiredLike
        alice.maxLove = lastStoryEvent.requiredLove

        # World attributes
        alice.preferredMondaySchedule = [location_park, location_beach, location_town, location_away]
        alice.preferredTuesdaySchedule = [location_library, location_library, location_cafe, location_away]
        alice.preferredWednesdaySchedule = [location_park, location_library, location_library, location_town]
        alice.preferredThursdaySchedule = [location_library, location_library, location_shop, location_away]
        alice.preferredFridaySchedule = [location_library, location_library, location_bar, location_away]
        alice.preferredSaturdaySchedule = [location_library, location_cafe, location_shop, location_away]
        alice.preferredSundaySchedule = [location_cafe, location_cafe, location_park, location_away]

        alice.preferredMovedInMondaySchedule = [location_home, location_home, location_home, location_home]
        alice.preferredMovedInTuesdaySchedule = [location_library, location_library, location_home, location_home]
        alice.preferredMovedInWednesdaySchedule = [location_home, location_library, location_library, location_home]
        alice.preferredMovedInThursdaySchedule = [location_home, location_library, location_shop, location_home]
        alice.preferredMovedInFridaySchedule = [location_home, location_library, location_home, location_home]
        alice.preferredMovedInSaturdaySchedule = [location_home, location_cafe, location_home, location_home]
        alice.preferredMovedInSundaySchedule = [location_home, location_home, location_home, location_home]
    return

# Sprites
screen aliceClickable(xcenter):
    $ spriteload = alice.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = alice)
        at characterSpriteHover

# Character methods
label aliceEvaluateAvailableInteractions:
    python:
        if alice.like >= 5:
            alice.availableActions = list(set(alice.availableActions + ['Spend time']))
        if alice.like >= 20 and aliceLikeEvent3.unlocked:
            alice.availableActions = list(set(alice.availableActions + ['Invite over']))

        if alice.isDateable and alice.love >= 1:
            alice.availableActions = list(set(alice.availableActions + ['Date']))
        if alice.love >= 3:
            alice.availableActions = list(set(alice.availableActions + ['Affection']))
            alice.availableAffections.extend(['Pat'])
        if alice.love >= 6:
            alice.availableAffections.extend(['Hug'])
        if alice.love >= 1 and aliceLikeEvent3.unlocked:
            alice.availableAffections.extend(['Chin Scratch', 'Kiss'])
        if aliceHEvent4.unlocked:
            alice.availableAffections.extend(['Caress Butt'])
        if aliceHEvent6.unlocked:
            alice.availableAffections.extend(['Boob Grab'])
        if aliceHEvent7.unlocked:
            alice.availableActions.extend([{'homelounge': ['Fingering']}])
        if alice.movedIn:
            alice.availableCommandsPrivate.extend(['Show Panties'])
            alice.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label aliceChat:
    show alice smile talk
    return

label aliceChat_beach:
    show alice bashful talk
    alice.c "Я не особо люблю плавать. Вода там ужасно солёная."
    return

label aliceChat_park:
    show alice smile talk
    alice.c "Здесь так спокойно и тихо."
    return

label aliceChat_shop:
    show alice neutral talk
    alice.c "Очень удобно. Я предпочитаю небольшие покупки, поэтому почти всё беру здесь."
    return

label aliceChat_diner:
    show alice neutral talk
    alice.c "Здесь очень большие порции. Я часто не могу всё доесть."
    show alice smile talk 2
    alice.c "Хотите кусочек?"
    return

label aliceChat_cafe:
    show alice smile talk
    alice.c "Если я не на работе, то обычно бываю здесь. Сегодня читаю..."
    return

label aliceChat_town:
    if(aliceVacation.unlocked):
        show alice smile talk
        alice.c "[mc.name]! Как приятно случайно встретиться."
    else:
        show alice neutral talk
        alice.c "Здравствуйте. Я иду домой. Не хотите поговорить?"
    return

label aliceChat_bar:
    show alice neutral talk
    alice.c "Я почти не пью... Не совсем понимаю, что в этом находят."
    show alice smile talk 2
    alice.c "Но коллегам нравится сюда заходить, вот я иногда и присоединяюсь."
    return

label aliceChat_aquarium:
    show alice neutral talk
    alice.c "Я иногда сюда захожу. Здесь очень интересно."
    return

label aliceChat_theater:
    show alice smile talk 2
    alice.c "Приятно, когда документальный фильм выпускают в прокат."
    show alice smile talk
    alice.c "Не хотите посмотреть его вместе?"
    return

label aliceChat_homebedroom:
    if(timeOfDay == 'Morning'):
        if(dayOfWeek in ['Saturday', 'Sunday']):
            show smile talk 2
            alice.c "Доброе утро, [mc.name]. Как спалось?"
        else:
            show alice smile talk
            alice.c "Доброе утро, [mc.name]. Скоро мне на работу, но пока есть немного времени."
    elif(timeOfDay == 'Afternoon'):
        show alice thinking
        alice.c "М? Ой, прости, [mc.name], я так увлеклась книгой, что ничего вокруг не замечала."
    elif(timeOfDay == 'Evening'):
        show alice smile talk
        alice.c "Как прошёл день, [mc.name]? Хочешь чем-нибудь заняться сегодня вечером?"
    elif(timeOfDay == 'Night'):
        show alice smile talk 2
        alice.c "Немного почитать перед сном — отличный способ успокоиться. Я готова ложиться, если и ты не против."
    return

label aliceChat_homelounge:
    if(timeOfDay == 'Morning'):
        show alice smile talk
        alice.c "О, я рано встала. Просто ищу что-нибудь интересное."
    elif(timeOfDay == 'Afternoon'):
        show alice thinking
        alice.c "Мне нравится подборка книг у тебя... Но со временем, пожалуй, понадобятся дополнительные полки."
    elif(timeOfDay == 'Evening'):
        show alice smile talk
        alice.c "Можем вместо этого что-нибудь посмотреть. Кажется, найдётся кое-что, что понравится нам обоим..."
    elif(timeOfDay == 'Night'):
        show alice smile talk 2
        alice.c "Да, меня тоже уже клонит в сон. Хочешь сегодня лечь вместе?"
    return

label aliceChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show alice neutral talk
        alice.c "[mc.name], утром обязательно нужно нормально поесть. Так голова будет лучше работать."
    elif(timeOfDay == 'Afternoon'):
        show alice smile talk
        alice.c "Я приготовила себе рыбу на обед. Хочешь немного, [mc.name]?"
    elif(timeOfDay == 'Evening'):
        show alice thinking
        alice.c "Ужин? О-о, точно, я же за этим и пришла... Кажется, я отвлеклась..."
    elif(timeOfDay == 'Night'):
        show alice smile talk
        alice.c "Ой, я совсем потеряла счёт времени. Ты уже ложишься?"
    return

# Date topics
label aliceChat_background:
    show alice neutral talk
    alice.c "Мне [alice.age] лет. Я родилась и выросла здесь; оба моих родителя — Anthro-Felis-Catus."
    alice.c "Я училась здесь, а потом поступила в городской университет и получила диплом по современной истории и литературе Anthro-Animalia."
    show alice neutral
    alice.c "..."
    "Ну, похоже, я получил ответ на свой вопрос. Но, кажется, придётся копнуть поглубже."
    mc.c "Ага. Значит, ты всё ещё живёшь дома? Семья тоже здесь?"
    show alice neutral talk
    alice.c "Они остались в городе. Но я съехала от родителей три года назад."
    show alice thinking
    alice.c "Родители сами подталкивали меня к этому. Сказали, что мне стоит «чаще выбираться из дома»."
    show alice neutral talk
    alice.c "Наверное, цель достигнута: я снимаю квартиру. Хотя меня бы вполне устроило и жить с родителями."
    alice.c "У людей это тоже считается обычным делом?"
    show alice neutral
    mc.c "В общем, да. Обычно где-то в 18–21 люди съезжают от родителей: поступают в колледж или начинают работать."
    mc.c "Кажется, наше поколение всё чаще откладывает это на потом. Экономика, всё такое."
    show alice smile talk
    alice.c "У Anthro-Animalia всё сильно зависит от вида-предка. Некоторые живут большими семьями, несколькими поколениями под одной крышей."
    alice.c "Любопытно, что их культура часто отражает древние повадки вида-предка. Этим занимаются исследователи, и работы у них очень интересные."
    show alice smile talk 2
    alice.c "Если тебе интересно, я могу одолжить тебе кое-какие свои книги и материалы."
    show alice smile
    mc.c "М-может, как-нибудь в другой раз..."
    show alice smile talk 2
    alice.c "Как пожелаешь."
    return

label aliceChat_hobbies:
    show alice smile talk
    alice.c "В свободное от работы время я в основном читаю."
    show alice smile
    alice.c "..."
    mc.c "Что именно читаешь?"
    show alice smile talk
    alice.c "В основном нон-фикшен: история, научные труды, исследовательские статьи, биографии и всё такое."
    alice.c "Иногда читаю и художественную литературу. В основном классику."
    show alice smile
    mc.c "Это для работы...?"
    show alice smile talk
    alice.c "Нет, мне это просто нравится. В мире столько всего можно узнать. А если вспомнить, сколько на планете разных культур, — целых миров."
    show alice smile talk 2
    alice.c "К примеру, люди. У вас такие разные культуры в разных странах, а иногда даже в разных городах. Мне это ужасно интересно."
    alice.c "Почти у каждой темы полно разных точек зрения — общество и культура влияют на то, как люди смотрят на вещи."
    show alice bashful talk
    alice.c "Я подошла к тебе в самом начале, потому что хотела... узнать всё из первых рук."
    show alice neutral talk
    alice.c "Прости за моё поведение в тот день. Мне говорили, что я иногда странно веду себя в обществе."
    show alice neutral
    mc.c "Элис, не переживай. Я и сам рад был с кем-то поговорить — я здесь недавно."
    mc.c "Да и с антро я тоже почти не общался. Мы в одной лодке."
    show alice smile talk
    alice.c "Спасибо. Значит, будем учиться друг у друга?"
    show alice smile
    mc.c "Можно и так..."
    mc.c "А кроме книг, есть ещё увлечения?"
    show alice thinking
    alice.c "..."
    show alice neutral talk
    alice.c "Иногда я смотрю документальные фильмы. Камера отлично подходит для некоторых тем."
    show alice neutral
    "Снова учёба..."
    mc.c "Может, что-нибудь... повеселее?"
    show alice smile talk 2
    alice.c "А мне это весело. Ты ведь об этом спросил, верно?"
    show alice smile
    "Ну, наверное..."
    return

#

label aliceInteractionBathroom:
    alice.c "Ах, [mc.name], я здесь."
    alice.c "А, ты уже понял? Понятно..."
    return

label aliceSpendTime(onDate):
    if(onDate):
        scene expression 'alice[mc.currentLocation.apiName]date'
    else:
        scene expression 'alice[mc.currentLocation.apiName]'
    with fade
    return

label aliceReceiveGift(item, likeChange, loveChange):
    show alice neutral talk
    alice.c "Ты хочешь мне что-то подарить?"
    if(loveChange > 0):
        show alice joy
        alice.c "Это невероятно щедро с твоей стороны."
        alice.c "Я буду беречь этот подарок. Спасибо."
    elif(likeChange > 1):
        show alice smile talk
        alice.c "Это очень мило с твоей стороны. Спасибо."
    elif(likeChange < 1):
        show alice mad talk
        alice.c "Зачем ты подарил мне это?"
    else:
        show alice smile talk
        alice.c "Спасибо."
    return

label aliceReceiveDateInvitation:
    show alice neutral talk
    alice.c "Конечно. Чем бы ты хотел заняться?"
    show alice neutral
    call dateInvitationSelector(alice) from _call_dateInvitationSelector
    show alice neutral talk
    alice.c "[_(proposedDateDayOfWeek)] [_(proposedDateTime)] в [_(proposedDateLocation.name)]? Тогда до встречи."

    python:
        scheduledDate = Date(alice, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        alice.scheduledDates.append(scheduledDate)
    return

label aliceStartDate:
    if(mc.currentLocation == location_home):
        show alice tease with dissolve
        alice.c "Привет! Как проходит [_(timeOfDay)]?"
    else:
        show alice smile talk with dissolve
        alice.c "Рада тебя видеть."
    return

label aliceDateInteraction:
    show alice smile with dissolve
    show screen dateUi(alice) with dissolve
    call screen dateInteractionScreen(alice, mc.currentLocation)

label aliceChatDate:
    show alice smile talk 2
    alice.c "Спасибо, что пригласил меня сегодня."
    return

label aliceChatDate_beach:
    show alice smile talk
    alice.c "Так приятно сменить обстановку."
    alice.c "Не загорай слишком долго, [mc.name]. Я читала, что солнце вредно для кожи."
    return

label aliceChatDate_park:
    show alice smile talk 2
    alice.c "Так расслабляет. Надо было захватить что-нибудь почитать."
    show alice surprise
    alice.c "Ой, это же свидание. Прости, я всё время забываю."
    return

label aliceChatDate_diner:
    show alice bashful
    alice.c "Я и кусочка больше не осилю."
    show alice smile talk 2
    alice.c "О, ты доешь за меня? Спасибо, не хочется выбрасывать."
    return

label aliceChatDate_cafe:
    show alice smile talk
    alice.c "Это ведь здесь мы впервые встретились?"
    show alice bashful
    alice.c "Кажется, я тогда немного опозорилась."
    return

label aliceChatDate_bar:
    show alice smile talk
    alice.c "Мне безалкогольный напиток, пожалуйста, [mc.name]."
    show alice thinking
    alice.c "Не понимаю, чем всех так привлекает алкоголь. Если уж пить, разве дело не во вкусе?"
    return

label aliceChatDate_aquarium:
    show alice surprise
    alice.c "О, теперь здесь есть и представители этого вида."
    show alice smile talk
    alice.c "Интересно, что у них..."
    return

label aliceChatDate_theater:
    show alice thinking
    alice.c "Хм... Что ты хотел посмотреть? Не могу сказать, что слышала об этих фильмах."
    show alice smile talk
    alice.c "Думаешь, мне понравится этот? Поверю твоему вкусу."
    return

label aliceDatePayFor:
    show alice smile talk
    alice.c "Не обязательно, [mc.name]."
    show alice smile talk 2
    alice.c "Что ж, большое спасибо."
    return

label aliceEndDate:
    if(dateScore < 40):
        show alice sad 
        alice.c "О-ох... Ну, пока тогда."
    else:
        if(alice.movedIn):
            show alice smile talk 2
            alice.c "Мне было очень хорошо, [mc.name]. Надеюсь, мы ещё не раз найдём время повторить."
            alice.c "Я люблю тебя."
        else:
            show alice smile talk 2
            if(aliceVacation.unlocked):
                alice.c "Я прекрасно провела время, [mc.name]. До скорого. Люблю тебя!"
            else:
                alice.c "Мне понравилось. Повторим как-нибудь?"
    return

label aliceContinueDateAtHome:
    scene expression 'alice[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(aliceHEvent1.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label aliceHomeStartSex:
    show alice neutral talk
    alice.c "А, ты хочешь сейчас заняться сексом?"
    show alice smile talk 2
    alice.c "Вообще-то я и сама не против~"
    show alice smile
    return

label aliceHomeSexJoinIn(character):
    show alice smile talk at twoPersonLeft with dissolve
    alice.c "[character.name], можно я к вам присоединюсь?"
    show alice smile
    return

label aliceEndDateAtHome:
    alice.c "Спасибо, что пригласил меня."
    if(aliceVacation.unlocked):
        alice.c "До скорой встречи. Люблю тебя!"
    return

image alice pat animated = Movie(play="images/characters/alice/affections/alicePat.webm", side_mask=True, loop=True)
label aliceReceivePat:
    hide alice with dissolve
    show alice pat animated with dissolve
    pause
    if(aliceHEvent3.unlocked):
        alice.c "Хм-м..."
        alice.c "Продолжай, пожалуйста."
        pause
    else:
        alice.c "..."
        alice.c "Приятно."
    return

image alice chinscratch animated = Movie(play="images/characters/alice/affections/aliceChinscratch.webm", side_mask=True, loop=True)
label aliceReceiveChinScratch:
    hide alice with dissolve
    show alice chinscratch animated with dissolve
    pause
    alice.c "Это так успокаивает, [mc.name]."
    return

image alice caressbutt animated = Movie(play="images/characters/alice/affections/aliceCaressButt.webm", side_mask=True, loop=True)
label aliceReceiveCaressButt:
    hide alice with dissolve
    show alice caressbutt animated with dissolve
    pause
    alice.c "...!"
    alice.c "[mc.name], мне приятно, что тебе так нравится... Но, пожалуйста, не на людях."
    return

image alice boobgrab animated = Movie(play="images/characters/alice/affections/aliceBoobGrab.webm", side_mask=True, loop=True)
label aliceReceiveBoobGrab:
    hide alice with dissolve
    show alice boobgrab animated with dissolve
    pause
    alice.c "Хм... Грудь у меня небольшая, но тебе всё равно нравится?"
    alice.c "Я не против... Можешь продолжать."
    return

image alice snuggle animated = Movie(play="images/characters/alice/affections/aliceSnuggle.webm", side_mask=True, loop=True)
label aliceReceiveSnuggle:
    "Я откидываюсь на диване и приглашаю Алису раскрытыми объятиями."
    show alice smile talk
    alice.c "А, хочешь, чтобы я к тебе присоединилась, [mc.name]?"
    hide alice with dissolve
    show alice snuggle animated with dissolve
    pause
    "Алиса забирается ко мне и устраивается у меня на груди."
    "Она тихонько мурлычет, а я обнимаю её и медленно глажу."
    pause
    return

label aliceReceiveHug:
    hide alice with dissolve
    show alice hug with dissolve
    pause
    alice.c "Ты такой тёплый."
    alice.c "Мне нравится."
    return

label aliceReceiveKiss:
    hide alice with dissolve
    show alice kiss with dissolve
    if(aliceHEvent3.unlocked):
        alice.c "М-м~"
        if(aliceVacation.unlocked):
            alice.c "Я люблю тебя~"
        else:
            alice.c "Мне это нравится."
    else:
        alice.c "*Чмок*"
        pause
        alice.c "Я... к такому не привыкла..."
    return

label aliceInitiatePat:
    show alice neutral talk with dissolve
    alice.c "[mc.name]. Мне нужны твои ласки."
    "[alice.name] опускает голову, приглашая погладить её."
    hide alice with dissolve
    show alice pat animated with dissolve
    pause
    alice.c "..."
    alice.c "Спасибо."
    return

label aliceInitiateHug:
    show alice smile with dissolve
    alice.c "Рада тебя видеть, [mc.name]."
    hide alice with dissolve
    show alice hug with dissolve
    pause
    alice.c "Как ты сегодня?"
    return

label aliceInitiateKiss:
    show alice smile with dissolve
    alice.c "..."
    hide alice with dissolve
    show alice kiss with dissolve
    alice.c "*Чмок*"
    pause
    hide alice with dissolve
    show alice smile with dissolve
    return

label aliceInitiateSnuggle:
    show alice smile
    "Я ложусь на диван, когда подходит Алиса."
    hide alice with dissolve
    show alice snuggle animated with dissolve
    pause
    "Не говоря ни слова, она медленно забирается на меня и сворачивается клубочком."
    alice.c "М-м~ Ты всегда такой тёплый~"
    pause
    return

label aliceInitiateHomeSex:
    show alice bashful talk
    alice.c "Э-э... [mc.name]..."
    alice.c "Мне что-то жарко... Может, займёмся сексом?"
    show alice bashful
    return

label aliceInitiateHomeSexDeny:
    show alice bashful talk
    alice.c "Ох, понятно... Ладно."
    return

label aliceSeesAffection(affection):
    show alice smile talk with dissolve
    alice.c "[mc.name], можно и мне?"
    show alice smile
    mc.c "Конечно."
    call expression 'aliceReceive' + affection from _call_expression
    hide alice with dissolve
    return

label aliceInviteOver:
    show alice smile talk
    alice.c "О-ох. Конечно."
    return

label aliceInitiateInviteOver:
    show alice smile talk
    alice.c "Подожди, [mc.name]. Я бы хотела снова побывать у тебя. Можно?"
    show alice smile
    menu:
        'Yes':
            show alice smile talk 2
            alice.c "Отлично!"
            return True
        'No':
            show alice neutral talk
            alice.c "Понимаю. Ничего страшного."
    return False

label aliceInviteGoHomeTogether:
    show alice smile talk 2
    alice.c "Да, я пойду с тобой."
    show alice smile talk 
    alice.c "Идти домой вместе... Я так рада."
    return

label aliceInitiateGoHomeTogether:
    show alice smile talk 2
    alice.c "[mc.name], я собираюсь домой. Пойдём вместе?"
    show alice smile
    menu:
        'Yes':
            show alice smile talk 2
            alice.c "Замечательно! Пойдём."
            return True
        'No':
            show alice smile talk
            alice.c "Понимаю. Тогда буду ждать тебя дома."
    return False

label aliceShowPanties(pantiesIndex = 1):
    show alice neutral talk
    alice.c "Моё бельё? Не совсем понимаю, почему тебя это интересует, но не вижу причин отказывать."
    $ renpy.show(alice.apiName + ' panties ' + str(pantiesIndex), tag=alice.apiName)
    with dissolve
    if(pantiesIndex == 1):
        alice.c "Ты уже много раз его видел, но всё равно так радуешься..."
    elif(pantiesIndex == 2):
        alice.c "Мне показался красивым узор. А тебе нравится?"
    elif(pantiesIndex == 3):
        alice.c "Кажется, ты хотел увидеть именно эти... Они уже у меня в ящике, так что надену их."
    return

label aliceSendDateText(proposedDate):
    python:
        timeText = {'Morning': 'утром', 'Afternoon': 'днём', 'Evening': 'вечером', 'Night': 'ночью'}.get(proposedDateTime, proposedDateTime.lower())
        locationPhrase = {'beach': 'на пляже', 'park': 'в парке', 'town': 'в городе', 'cafe': 'в кафе', 'library': 'в библиотеке', 'diner': 'в закусочной', 'bar': 'в баре', 'aquarium': 'в океанариуме', 'theater': 'в театре', 'shop': 'в магазине'}.get(proposedLocation.apiName, 'в «' + _(proposedLocation.name).lower() + '»')
        alice.textChain.append(Message(mc, alice, 'Здравствуйте, [mc.name]. Не хотели бы вы завтра куда-нибудь сходить?', Null, day, timeOfDay))
        alice.textChain.append(Message(mc, alice, 'Вам было бы удобно встретиться завтра ' + timeText + ' ' + locationPhrase + '?', Null, day, timeOfDay, proposedDate))
    return

label aliceGetSelfieOptions:
    $ aliceSelfieOptions = []
    if(aliceLikeEvent3.unlocked):
        $ aliceSelfieOptions.extend(['beach1'])
    if(aliceHEvent1.unlocked):
        $ aliceSelfieOptions.extend(['bedroom1'])
    if(aliceHEvent2.unlocked):
        $ aliceSelfieOptions.extend(['bedroom2', 'bedroom3'])
    if(alice.movedIn):
        $ aliceSelfieOptions.extend(['homebedroom1'])
    return aliceSelfieOptions

label aliceSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'beach1':
                potentialResponses.append({'text': "Очень мило!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Красивые ноги.", 'statChange': 'love', 'statChangeAmount': 1})
                alice.textChain.append(Message(mc, alice, 'Здравствуйте. Сегодня я была на пляже.', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom1':
                potentialResponses.append({'text': "Обычно там загорают топлес, но фото очень милое, [alice.name].", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Вот это жарко! Ты сделала мой день!", 'statChange': 'love', 'statChangeAmount': 1})
                alice.textChain.append(Message(mc, alice, "Здравствуйте. Я слышала, мужчинам нравятся фотографии груди.", Null, day, timeOfDay))
                alice.textChain.append(Message(mc, alice, "Я всё правильно делаю?", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom2':
                potentialResponses.append({'text': "Мило!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Ещё! Мне всё мало!", 'statChange': 'love', 'statChangeAmount': 1})
                alice.textChain.append(Message(mc, alice, "Здравствуйте. Я узнала, что некоторым мужчинам нравятся фотографии ног.", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom3':
                potentialResponses.append({'text': "Они отлично смотрятся, не переживай!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Ты потрясающе в них выглядишь. И попка очень красивая!", 'statChange': 'love', 'statChangeAmount': 1})
                alice.textChain.append(Message(mc, alice, "Здравствуйте. Я купила новую одежду, но теперь сомневаюсь в покупке.", Null, day, timeOfDay))
                alice.textChain.append(Message(mc, alice, "В них моя попа не кажется большой?", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'homebedroom1':
                potentialResponses.append({'text': "Скоро, красавица!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Не двигайся, я скоро буду :)", 'statChange': 'love', 'statChangeAmount': 1})
                alice.textChain.append(Message(mc, alice, "Здравствуйте. Когда вы будете дома?", selfieName, day, timeOfDay, responses = potentialResponses))
    return

label aliceSexSelect:
    hide screen mainUi
    scene black with fade
    image alice sex waiting = Movie(play="images/characters/alice/hscenes/sexWaiting.webm")
    show alice sex waiting with fade

    call screen aliceSexSelectScreen
    if(aliceHEvent4.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(alice.movedIn):
            menu aliceSleepTogether:
                "Переспать с Алисой?"
                'Yes':
                    alice.c "Ты хочешь сегодня спать вместе?"
                    alice.c "Ах, да, конечно. Спокойной ночи, [mc.name]~"
                    call characterSleepover(alice) from _call_characterSleepover
                'No':
                    pass
        else:
            menu aliceStayTheNight:
                "Пригласить [alice.name] остаться на ночь?"
                'Yes':
                    $ alice.addLove(1)
                    alice.c "Да, я бы очень этого хотела."
                    call characterSleepover(alice) from _call_characterSleepover_1
                'No':
                    if(aliceVacation.unlocked):
                        alice.c "Мне очень понравилось провести с тобой время. Я люблю тебя, [mc.name]."
                    else:
                        alice.c "Буду ждать следующего раза."
    
    call endScene(character = alice, targetLocation = location_home) from _call_endScene

screen aliceSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(aliceHEvent1.unlocked or persistent.debugMode):
                textbutton 'Handjob' keysym str(1):
                    action [Jump('aliceHandjob')]
            else:
                textbutton 'Locked'
            if(aliceHEvent2.unlocked or persistent.debugMode):
                textbutton 'Thighjob' keysym str(2):
                    action [Jump('aliceThighjob')]
            else:
                textbutton 'Locked'
            if(aliceHEvent4.unlocked or persistent.debugMode):
                textbutton 'Missionary' keysym str(3):
                    action [Jump('aliceMissionary')]
            else:
                textbutton 'Locked'
            if(aliceHEvent5.unlocked or persistent.debugMode):
                textbutton 'Make Out' keysym str(4):
                    action [Jump('aliceMakeout')]
            else:
                textbutton 'Locked'
            if(aliceHEvent5.unlocked or persistent.debugMode):
                textbutton 'Cunnilingus' keysym str(5):
                    action [Jump('aliceCunnilingus')]
            else:
                textbutton 'Locked'
            if(aliceHEvent5.unlocked or persistent.debugMode):
                textbutton 'Blowjob' keysym str(6):
                    action [Jump('aliceBlowjob')]
            else:
                textbutton 'Locked'
            if(aliceHEvent6.unlocked or persistent.debugMode):
                textbutton 'Tailjob' keysym str(7):
                    action [Jump('aliceTailjob')]
            else:
                textbutton 'Locked'
            if(aliceVacation.unlocked or persistent.debugMode):
                textbutton 'Sideways Doggy' keysym str(8):
                    action [Jump('aliceSidewaysDoggy')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(9):
                action [Hide('aliceSexSelectScreen'), Return()]

label aliceSleepover:
    scene alicesleepover with fade
    pause
    return

label aliceMorningBedInteraction:
    scene alicehomemorning with fade 
    pause
    alice.c "Доброе утро, [mc.name]~"
    if(alice.movedIn):
        alice.c "Ты хорошо спал? В твоих объятиях я всегда сплю крепко."
        alice.c "Сегодня по дому нужно что-нибудь сделать?"
    else:
        alice.c "Я просто любовалась твоим спящим лицом."
        alice.c "Ты так сладко спал. Я тоже хорошо выспалась."
    return

label aliceMorningBedInteractionSex(event):
    if(event == 'kiss'):
        image alice morning kiss 1 = Movie(play="images/characters/alice/hscenes/morning/kiss1.webm")
        show alice morning kiss 1 with fade
        pause
        alice.c "Доброе утро, [mc.name]."
        mc.c "Доброе утро, Алиса. Почему ты лежишь на мне?"
        alice.c "Мне показалось, что так правильно. Я не слишком тяжёлая?"
        mc.c "Нисколько. Иди ко мне."
        image alice morning kiss 2 = Movie(play="images/characters/alice/hscenes/morning/kiss2.webm")
        show alice morning kiss 2 with fade
        pause
        alice.c "М-м-м~"
    elif(event == 'licking'):
        image alice morning licking 1 = Movie(play="images/characters/alice/hscenes/morning/licking1.webm")
        show alice morning licking 1 with fade
        pause
        mc.c "...Алиса?"
        alice.c "Интересно, что эрекция может появиться и без внешних стимулов."
        mc.c "Ты прямо сейчас его стимулируешь..."
        alice.c "О, значит, таким ты был, когда я проснулась."
        "..."
        "Это всё равно не объясняет, почему она его лижет..."
        pause
    return

# Sex scenes
label aliceHandjob:
    image alice handjob part 1 = Movie(play="images/characters/alice/hscenes/handjob/part1.webm")
    show alice handjob part 1 with fade
    pause
    image alice handjob part 2 = Movie(play="images/characters/alice/hscenes/handjob/part2.webm")
    show alice handjob part 2 with fade
    pause
    image alice handjob end = Image("images/characters/alice/hscenes/handjob/end.webp")
    scene alice handjob end with fadewhite
    pause
    jump aliceSexSelect
    
label aliceThighjob:
    image alice thighjob part 1 = Movie(play="images/characters/alice/hscenes/thighjob/part1.webm")
    show alice thighjob part 1 with fade
    pause
    image alice thighjob part 2 = Movie(play="images/characters/alice/hscenes/thighjob/part2.webm")
    show alice thighjob part 2 with fade
    pause
    image alice thighjob end = Image("images/characters/alice/hscenes/thighjob/end.webp")
    scene alice thighjob end with fadewhite
    pause
    jump aliceSexSelect

label aliceMissionary:
    image alice missionary start = Image("images/characters/alice/hscenes/missionary2/start.webp")
    show alice missionary start with fade
    pause
    image alice missionary part 1 = Movie(play="images/characters/alice/hscenes/missionary2/part1.webm")
    show alice missionary part 1 with fade
    pause
    image alice missionary part 2 = Movie(play="images/characters/alice/hscenes/missionary2/part2.webm")
    show alice missionary part 2 with fade
    pause
    image alice missionary part 3 = Movie(play="images/characters/alice/hscenes/missionary2/part3.webm")
    show alice missionary part 3 with fade
    pause
    image alice missionary part 4 = Movie(play="images/characters/alice/hscenes/missionary2/part4.webm")
    show alice missionary part 4 with fade
    pause
    image alice missionary end = Image("images/characters/alice/hscenes/missionary2/end.webp")
    show alice missionary end with fadewhite
    pause
    jump aliceSexSelect

label aliceMakeout:
    image alice makeout part 1 = Movie(play="images/characters/alice/hscenes/cunnilingus/makeout1.webm")
    show alice makeout part 1 with fade
    pause
    image alice makeout part 2 = Movie(play="images/characters/alice/hscenes/cunnilingus/makeout2.webm")
    show alice makeout part 2 with fade
    pause
    jump aliceSexSelect

label aliceCunnilingus:
    image alice cunnilingus part 1 = Image("images/characters/alice/hscenes/cunnilingus/part1.webp")
    show alice cunnilingus part 1 with fade
    pause
    image alice cunnilingus part 2 = Movie(play="images/characters/alice/hscenes/cunnilingus/part2.webm")
    show alice cunnilingus part 2 with fade
    pause
    image alice cunnilingus part 3 = Movie(play="images/characters/alice/hscenes/cunnilingus/part3.webm")
    show alice cunnilingus part 3 with fade
    pause
    image alice cunnilingus part 4 = Movie(play="images/characters/alice/hscenes/cunnilingus/part4.webm")
    show alice cunnilingus part 4 with fade
    pause
    image alice cunnilingus end 1 = Image("images/characters/alice/hscenes/cunnilingus/end1.webp")
    show alice cunnilingus end 1 with fadewhite
    pause
    jump aliceSexSelect

label aliceBlowjob:
    image alice blowjob part 1 = Image("images/characters/alice/hscenes/blowjob/part1.webp")
    show alice blowjob part 1 with fade
    pause
    image alice blowjob part 2 = Movie(play="images/characters/alice/hscenes/blowjob/part2.webm")
    show alice blowjob part 2 with fade
    pause
    image alice blowjob part 3 = Movie(play="images/characters/alice/hscenes/blowjob/part3.webm")
    show alice blowjob part 3 with fade
    pause
    image alice blowjob part 4 = Movie(play="images/characters/alice/hscenes/blowjob/part4.webm")
    show alice blowjob part 4 with fade
    pause
    image alice blowjob part 5 = Movie(play="images/characters/alice/hscenes/blowjob/part5.webm")
    show alice blowjob part 5 with fade
    pause
    image alice blowjob end 1 = Image("images/characters/alice/hscenes/blowjob/end1.webp")
    show alice blowjob end 1 with fadewhite
    pause
    image alice blowjob end 2 = Image("images/characters/alice/hscenes/blowjob/end2.webp")
    show alice blowjob end 2 with fade
    pause
    image alice blowjob end 3 = Image("images/characters/alice/hscenes/blowjob/end3.webp")
    show alice blowjob end 3 with fade
    pause
    jump aliceSexSelect

label aliceTailjob:
    scene alicetailjobstart with fade
    pause
    image alice tailjob part 1 = Movie(play="images/characters/alice/hscenes/tailjob/part1.webm")
    show alice tailjob part 1 with fade
    pause
    image alice tailjob part 2 = Movie(play="images/characters/alice/hscenes/tailjob/part2.webm")
    show alice tailjob part 2 with fade
    pause
    image alice tailjob part 3 = Movie(play="images/characters/alice/hscenes/tailjob/part3.webm")
    show alice tailjob part 3 with fade
    pause
    scene alicetailjobend1 with fadewhite
    pause
    scene alicetailjobend2 with fade
    pause
    jump aliceSexSelect

label aliceSidewaysDoggy:
    image alice sideways doggy 1 = Movie(play="images/characters/alice/hscenes/sidewaysDoggy/part1.webm")
    show alice sideways doggy 1 with fade
    pause
    image alice sideways doggy 2 = Movie(play="images/characters/alice/hscenes/sidewaysDoggy/part2.webm")
    show alice sideways doggy 2 with fade
    pause
    scene alicesidewaysdoggyfinish1 with fadewhite
    pause
    scene alicesidewaysdoggyfinish2 with fade
    pause
    jump aliceSexSelect

label alicehomeloungeFingering:
    image alice fingering 1 = Movie(play="images/characters/alice/hscenes/fingering/fingering1.webm")
    show alice fingering 1 with fade
    pause
    image alice fingering 2 = Movie(play="images/characters/alice/hscenes/fingering/fingering2.webm")
    show alice fingering 2 with fade
    pause
    image alice fingering 3 = Movie(play="images/characters/alice/hscenes/fingering/fingering3.webm")
    show alice fingering 3 with fade
    pause
    image alice fingering 4 = Movie(play="images/characters/alice/hscenes/fingering/fingering4.webm")
    show alice fingering 4 with fade
    pause
    image alice fingering 5 = Movie(play="images/characters/alice/hscenes/fingering/fingering5.webm")
    show alice fingering 5 with fade
    pause
    scene alicefingeringfinish with fadewhite
    pause
    return

# Events
default aliceFirstMeetingEvent = Event('First meeting', 'aliceFirstMeeting', [alice], 0, 0, [], location_cafe, ['Morning', 'Afternoon'], triggerDay = 1)
default aliceLikeEvent1 = Event('Proper introduction', 'aliceLikeEvent1', [alice], 10, 0, [aliceFirstMeetingEvent], location_cafe, ['Morning', 'Afternoon', 'Evening'])
default aliceLikeEvent2 = Event('Thorough investigation', 'aliceLikeEvent2', [alice], 20, 0, [aliceLikeEvent1], location_town, ['Morning', 'Afternoon', 'Evening'])
# Makes her dateable. First kiss
default aliceLikeEvent3 = Event('Feelings felt', 'aliceLikeEvent3', [alice], 30, 0, [aliceLikeEvent2], location_cafe, ['Morning', 'Afternoon', 'Evening'])
# First sex (handjob)
default aliceHEvent1 = Event('Will you?', 'aliceHEvent1', [alice], 40, 10, [aliceLikeEvent3], location_park)
# Thighjob
default aliceHEvent2 = Event('Not ready yet', 'aliceHEvent2', [alice], 50, 15, [aliceHEvent1], location_town)
# Virginity loss
default aliceHEvent3 = Event('Liquid courage', 'aliceHEvent3', [alice], 60, 20, [aliceHEvent2], location_bar)
# Proper sex
default aliceHEvent4 = Event('Researched and prepared', 'aliceHEvent4', [alice], 70, 25, [aliceHEvent3], location_home, ['Evening', 'Night'])
# Cunnilingus / blowjob
default aliceHEvent5 = Event('Other ways', 'aliceHEvent5', [alice], 80, 30, [aliceHEvent4], location_cafe)
# Tailjob
default aliceHEvent6 = Event('Infatuation', 'aliceHEvent6', [alice], 90, 35, [aliceHEvent5], location_home)
# Discussion of kids
default aliceLikeEvent4 = Event('Quiet please', 'aliceLikeEvent4', [alice], 100, 40, [aliceHEvent6], location_town, ['Morning', 'Afternoon', 'Evening'])
# Abroad hotel beach pool vacation
default aliceVacation = Event('City break', 'aliceVacation', [alice], 110, 45, [aliceLikeEvent4], Null, extraNotes = 'Organise a vacation. Special option in interaction menu.', cost=2500, requiresInvite = True)
# Move in invite + event
default aliceLikeEvent5 = Event('Economical', 'aliceLikeEvent5', [alice], 120, 50, [aliceVacation], Null, extraNotes = 'Things are getting serious. Are we ready for the next step?\nSpecial option in interaction menu.', requiredItems = [item_car], requiresInvite = True)
# Lounge butt rub finger
default aliceHEvent7 = Event('Cat trapped', 'aliceHEvent7', [alice], 130, 55, [aliceLikeEvent5], location_home_lounge, mcInitiated = True)

label aliceFirstMeeting(fromGallery):
    $ location_cafe.showBackground()
    $ alice.knownToMC = True
    hide alice
    call playMusic(chillTheme) from _call_playMusic
    "Я недавно переехал и всё ещё осваивался: изучал местные магазины, кафе и развлечения, выяснял, что стоит внимания, а что нет."
    "Нашёл небольшое кафе недалеко от центра. Неплохой кофе, хороший выбор выпечки, да и персонал приветливый."
    "Иногда сюда стоит заглянуть, хотя бы чтобы выбраться из дома."
    "Я всё твердил себе, что заставлю себя посидеть и почитать книгу, которую уже несколько недель таскаю с собой. Ведь люди ходят в кафе в одиночку именно для этого, да?"
    "Заказываю кофе и маленький датский круассан, чтобы подкрепиться."
    scene black with fade
    "..."
    $ location_cafe.showBackground()
    "Я изо всех сил пытаюсь читать, но слова совсем не лезут в голову. Каждые несколько минут взгляд начинает блуждать."
    "Пожалуй, с книгой пора завязывать. Время не стоит того. Я оглядываю зал."
    "Мой взгляд падает на девушку, которая здесь уже столько же, сколько и я."
    scene alicefirstmeetingi1 with fade
    pause
    "Меня привлекла её угольно-чёрная шерсть. У местных столько разных окрасов и узоров. Вроде ожидаемо, но я всё ещё не привык."
    "Похожа на кошку: чёрная шерсть контрастирует с белыми отметинами на мордочке и длинными гладкими серебристыми волосами."
    "На вид она маленькая и хрупкая, но выражение лица у неё особенное... Строгое, серьёзное и немного неприступное."
    "Когда я посмотрел в её сторону, наши взгляды вроде бы встретились, но она тут же уткнулась в книгу. Может, мне показалось."
    $ location_cafe.showBackground()
    "Я снова пытаюсь читать, но ничего не выходит. Допью кофе и пойду."
    "Не могу удержаться и снова поднимаю глаза."
    show alice neutral with dissolve
    pause
    call playMusic(funnyTheme) from _call_playMusic_1
    "..."
    hide alice with dissolve
    pause
    "Каждый раз, когда я поглядываю на неё, она тоже смотрит на меня. Даже не особо скрывает, но выражение лица у неё совершенно нейтральное."
    "Стоит мне поймать её взгляд, как она снова утыкается в книгу. Подглядывает? Любопытствует? Или просто совпадение? Может, мы оба не можем сосредоточиться."
    pause
    show alice neutral with dissolve
    pause
    "Опять она."
    hide alice with dissolve
    pause
    "Становится немного странно. Я что, нарушаю какое-то местное правило? Признаюсь, здешние порядки мне пока непривычны. Я всё ещё чужак."
    "Но я совершенно не могу прочитать её выражение лица. Может, дело в кошачьих чертах, а может, я просто слишком много об этом думаю."
    "На этот раз я просто продолжу смотреть."
    "..."
    show alice neutral with dissolve
    pause
    "..."
    pause
    show alice bashful with dissolve
    hide alice with dissolve
    pause
    "Ну вот, теперь мы довольно долго смотрели друг другу в глаза. Она смутилась и резко отвернулась к своей книге."
    "Понятия не имею, что и думать."
    "Допью кофе и уйду. Книгу так и не прочитал — вылазка провалилась. Потом, конечно, снова скажу себе попробовать как-нибудь ещё. Пусть будущий я об этом и думает."
    "Я допиваю кофе, убираю книгу и замечаю, что девушка направляется ко мне."
    show alice neutral with dissolve
    pause
    "..."
    pause
    mc.c "Алло?"
    show alice neutral talk
    alice_unknown "А-а... Привет."
    alice_unknown "Прости."
    alice_unknown "За то, что смотрела."
    show alice neutral
    "..."
    "Её прямолинейность немного сбивает меня с толку, но я стараюсь ответить вежливо."
    mc.c "Всё нормально. Я тоже отвлекался. Книга, похоже, не слишком увлекательная..."
    "Я приподнимаю книгу, показывая, в чём проблема."
    show alice neutral talk
    alice_unknown "Да. Книга ужасная."
    show alice neutral
    "Опять без обиняков."
    mc.c "Похоже, я с тобой согласен. Уже собирался бросить её."
    "..."
    "..."
    mc.c "Поэтому ты на меня смотрела?"
    alice_unknown "Нет."
    show alice neutral talk
    alice_unknown "Ты ведь человек, верно?"
    show alice neutral
    mc.c "Да, именно. Таких, как я, здесь, наверное, немного. Я недавно переехал."
    show alice smile talk
    alice_unknown "Любопытно."
    show alice smile
    "..."
    "Странная встреча. И что мне на это ответить?"
    show alice smile talk
    alice_unknown "Я много читала о людях: об истории, культуре, физиологии, поведении, поселениях, политике и философии. Мне нравятся многие ваши писатели, исследователи, мыслители, музыканты..."
    "Ничего себе..."
    show alice smile talk 2
    alice_unknown "...особенно увлекательны ваши взгляды на войну, прежде всего исторические. И то, как они связаны с развитием разных культур по всему миру, и как это привело к..."
    show alice smile talk
    "Она всё продолжает..."
    alice_unknown "...и тогда исследования показывают, что—"
    "Кажется, она заметила, что я уже перестал воспринимать её слова."
    show alice bashful talk
    alice_unknown "Ой, прости. Стоит мне начать, и я начинаю болтать без остановки."
    show alice bashful
    mc.c "Ничего страшного. Ты, значит, хорошо во всём этом разбираешься?"
    show alice neutral talk
    alice_unknown "...Я много читала, но почти не общалась с людьми. Поэтому и поглядывала на тебя. Мне было любопытно."
    show alice neutral
    mc.c "Всё в порядке. Могла бы просто подойти и спросить, я бы не возражал. С тех пор как я переехал, несколько человек уже так делали. Меня это совершенно не беспокоит."
    alice_unknown "..."
    show alice neutral talk
    alice_unknown "Наверное, могла бы. У тебя сейчас есть время?"
    "Я всё равно собирался уходить, но особых планов у меня нет. Могу ещё немного посидеть."
    mc.c "Конечно, садись. О чём поговорим?"
    show alice smile
    pause
    scene black with fade
    "..."
    $ location_cafe.showBackground()
    "В итоге она задавала вопросы минут сорок пять. Про разные периоды человеческой истории и достижения, о которых я понятия не имел."
    "Кажется, я не рассказал ей ни одной вещи, которой она уже не знала."
    show alice neutral talk
    alice_unknown "Я и так отняла у тебя много времени. Спасибо, мне было очень интересно узнать твою точку зрения."
    mc.c "Да, конечно. Не за что. Рад, что хоть чем-то помог."
    alice_unknown "До свидания."
    hide alice with dissolve
    "Девушка встаёт и направляется к своему столику. Всё это время её вещи так и лежали там."
    "Но, сделав шаг, она вдруг останавливается."
    show alice smile talk with dissolve
    alice.c "Меня зовут [alice.name]. А тебя?"
    show alice smile
    "Глупо вышло: мы всё это время разговаривали и даже не представились. Я так увлёкся её рассказом."
    mc.c "Ой, прости! Я [mc.name]. Приятно познакомиться, [alice.name]."
    alice.c "Взаимно. Надеюсь, как-нибудь повторим."
    hide alice with dissolve
    "Она разворачивается, забирает вещи и выходит, даже не оглянувшись. Какая странная девушка."
    "В хорошем смысле, конечно."
    "Она сказала «как-нибудь повторим», но мы даже контактами не обменялись. Интересно, увидимся ли ещё."

    if(not fromGallery):
        $ alice.addLike(1)
    
    return

label aliceLikeEvent1(fromGallery):
    $ location_cafe.showBackground()
    call playMusic(heartTheme) from _call_playMusic_2
    "Зайти в это кафе выпить кофе стало привычкой. Иногда приятно посидеть в тишине и расслабиться."
    "Та ужасная книга давно отправилась на покой. Сегодня читаю местные новости."
    "Тут совсем не так уныло, как у меня на родине. По сравнению с большими городами это просто рай."
    "Минут через пять после того, как я сел, вошло знакомое лицо."
    show alice neutral with dissolve
    "Я пару раз видел [alice.name] в городе и в этом кафе. Перекинулись парой слов, но толком не общались."
    "Она направилась к стойке, но краем глаза заметила меня. Наши взгляды встретились."
    "Девушка подходит к моему столику."
    show alice neutral talk
    alice.c "Привет. Мне сказали, что я должна перед тобой извиниться."
    "Я не совсем понимаю, о чём речь."
    mc.c "За что? Не думаю, что должна."
    alice.c "Коллега рассказала, что видела в городе человека. После расспросов выяснилось, что это был ты."
    alice.c "Я рассказала ей о нашей первой встрече. Она уверена, что я была, как она выразилась, «бестактной» и могла доставить тебе неудобства, ведь мы были незнакомы."
    alice.c "Мне часто говорят, что я холодно или слишком напористо разговариваю. Или и то и другое сразу. Последнего я пока не понимаю."
    alice.c "Подумав, я решила, что она, вероятно, права. Поэтому хочу извиниться. Прости, что тогда побеспокоила тебя."
    mc.c "Честно, ты меня не побеспокоила. Наоборот, было приятно. Я недавно здесь, почти никого не знаю, так что поговорить с кем-то было здорово."
    mc.c "Я ведь тоже хочу завести новых друзей, как и все остальные."
    show alice bashful talk
    alice.c "Друзей..."
    show alice neutral talk
    alice.c "Значит, ты принимаешь мои извинения?"
    mc.c "Извиняться не за что, но если тебе так спокойнее — конечно, я принимаю их."
    show alice smile talk
    alice.c "Спасибо. Тогда пойду закажу что-нибудь."
    mc.c "А может, посидишь со мной? В прошлый раз я почти ничего о тебе не узнал."
    show alice neutral
    alice.c "..."
    "Она немного медлит. Я не могу понять, что означает её выражение лица."
    show alice smile talk
    alice.c "С удовольствием, спасибо. Подсяду, как только закажу."
    hide alice with dissolve
    "[alice.name] подходит к стойке, берёт небольшой чай и возвращается."
    show alice neutral with dissolve
    call playMusic(funnyTheme) from _call_playMusic_3
    "Я показываю на стул напротив. Она кивает и садится."
    alice.c "Спасибо."
    pause
    "..."
    pause
    "Я сам пригласил её к столику, но даже не придумал, с чего начать. В прошлый раз она просто рассказывала мне о жизни людей, иногда задавая вопросы."
    mc.c "Итак, кем ты работаешь?"
    show alice smile talk
    alice.c "Я работаю в городской библиотеке."
    alice.c "Ещё сотрудничаю с местными школами: подбираю учебные материалы, помогаю с исследованиями и школьными мероприятиями."
    mc.c "Здорово. Ты всегда этим занималась?"
    alice.c "Последние пять лет, сразу после школы. Работа хорошая. Если бы я не работала там, всё равно проводила бы в библиотеке большую часть времени."
    show alice thinking
    alice.c "К счастью, там почти никогда не бывает людно. Удивительно: в городе же есть университет. Где студенты берут материалы для исследований?"
    mc.c "Наверное, теперь они всё ищут в интернете. Сама знаешь, как оно бывает."
    show alice neutral talk
    alice.c "В интер...нете?"
    show alice neutral
    mc.c "Ну, скачивают электронные книги на ноутбуки и читают там."
    show alice neutral talk
    alice.c "А, компьютеры. Я в них не разбираюсь."
    show alice neutral
    "Что?"
    mc.c "У тебя нет компьютера?"
    show alice neutral talk
    alice.c "В библиотеке один есть. Я пользуюсь им, чтобы оформлять выдачу и возврат книг. Но толком не понимаю, как он работает. Обычно помогает коллега."
    show alice neutral
    "Вот это новость."
    mc.c "Правда? Сейчас это редкость, особенно среди молодых. В школе тебе не приходилось пользоваться компьютером?"
    show alice neutral talk
    alice.c "Иногда приходилось. Тогда я в них не разбиралась и сейчас не разбираюсь."
    show alice sad talk
    alice.c "Я даже провалила один школьный предмет. Позорное пятно в моём аттестате."
    show alice neutral talk
    alice.c "Но, думаю, в итоге я оказалась права. В жизни они мне ни к чему."
    mc.c "Кроме работы."
    show alice smile talk 2
    alice.c "С этой частью справится кто-нибудь другой."
    show alice smile
    "Тут проглядывает её немного ехидный характер."
    mc.c "Значит, все те вопросы в прошлый раз были не о людях в целом, а именно о человеческой коллекции?"
    show alice smile talk 2
    alice.c "Нет, мы тут не оторваны от мира. У нас есть и человеческие изобретения, и медиа."
    alice.c "Просто мне нравится узнавать о таких вещах из первых уст. Я так расспрашивала представителей почти всех других видов, с которыми встречалась. А поговорить с человеком случая не было. Ты был один, и я решила воспользоваться возможностью."
    mc.c "Рад, что смог помочь."
    show alice neutral talk
    alice.c "Вообще-то ты мог бы помочь ещё кое в чём."
    mc.c "В чём?"
    alice.c "В человеческой анатомии."
    show alice neutral
    pause
    "Её прямолинейность снова застала меня врасплох."
    mc.c "Анатомии?"
    show alice neutral talk
    alice.c "Да. Конечно, есть много книг на эту тему, но обычно там только иллюстрации."
    alice.c "Увидеть всё своими глазами было бы познавательно: кожа, шерсть или её отсутствие, кости, мышцы, половые органы—"
    show alice neutral
    pause
    "Она хотела сказать то, что мне послышалось?"
    show alice bashful talk
    alice.c "Постой, я опять тебе мешаю."
    mc.c "Нет, всё нормально, правда."
    "Похоже, она немного смутилась и покраснела."
    alice.c "Кхм. В общем, поэтому я хотела бы поддерживать с тобой связь, если ты не против."
    mc.c "Конечно, просто дай знать. Может, мне как-нибудь зайти к тебе в библиотеку?"
    alice.c "А, нет, не нужно. В другой раз."
    "[alice.name] уже давно допила чай, но вдруг резко встаёт из-за стола."
    alice.c "Спасибо, что уделил мне время. Мне пора. До свидания."
    mc.c "Ой, пока! Скоро увидимся!"
    hide alice with dissolve
    "Она ушла торопливо. Ей стало неловко или она всегда такая?"
    "По крайней мере, она хочет снова поговорить."

    if(not fromGallery):
        $ alice.addLike(1)
    
    return

label aliceLikeEvent2(fromGallery):
    $ location_town.showBackground()
    "Внезапно я получил приглашение от [alice.name]. Она предложила встретиться в городе."
    "Кажется, это связано с её любопытством, о котором она столько рассказывала."
    "Вроде бы я согласился на что-то подобное, когда мы виделись в кафе, перед тем как она так быстро ушла."
    "Не знаю, чего ожидать. С этой девушкой никогда не угадаешь."
    show alice smile talk with dissolve
    call playMusic(chillTheme) from _call_playMusic_4
    alice.c "Спасибо, что принял моё приглашение. Я ценю, что ты нашёл время."
    show alice smile
    mc.c "Не за что. У меня выходной, особо нечем заняться. Мы идём в библиотеку?"
    show alice neutral talk
    alice.c "Вообще-то нет. На работе меня всё донимают, чтобы я использовала выходные. Настойчиво просят не приходить."
    show alice neutral
    "Трудоголик? Или просто книжная зависимость?"
    mc.c "А, понятно. И чем тогда займёмся?"
    show alice neutral talk
    alice.c "Я бы хотела продолжить изучать людей, как в прошлый раз. Ты говорил, что не против. Это всё ещё так?"
    show alice neutral
    "Кажется, я и правда что-то такое сказал... Да я и не против."
    mc.c "Конечно. Может, снова пойдём в кафе? Там и поговорим."
    show alice neutral talk
    alice.c "Я хотела пригласить тебя домой. Там будет уединённее, и я смогу чувствовать себя спокойнее. Я живу неподалёку."
    "[alice.c] даже не моргнула. Мы не так хорошо знакомы, поэтому её предложение меня удивило."
    mc.c "Э-э, я не против. Веди."
    show alice smile talk
    alice.c "Тогда за мной."

    hide alice with dissolve
    scene black with fade
    "По дороге мы почти не разговаривали. Она внимательно следила за маршрутом. Хорошо, что живёт рядом."
    scene aliceshome with fade

    show alice smile talk
    alice.c "Вот мы и пришли. Проходи, садись."
    show alice neutral
    "Квартира довольно маленькая. Мы снимаем обувь, и [alice.name] ведёт меня прямиком в спальню."
    "Почти все остальные стены и поверхности заняты книжными полками."
    "Я осматриваю комнату. Чисто и аккуратно, неожиданно по-девичьи и, конечно, сплошная литература."
    "Я сажусь, как она и просила. Она сразу подходит к столу, достаёт книги и раскрывает страницы с закладками."
    show alice neutral talk
    call playMusic(funnyTheme) from _call_playMusic_5
    alice.c "Можно я прикоснусь к тебе, [mc.name]?"
    show alice neutral
    "..."
    "А?"
    mc.c "Прости, что?"
    "[alice.name] опускает взгляд на одну из раскрытых страниц."
    show alice neutral talk
    alice.c "Я хочу изучить описания человеческой кожи. Открытая кожа почти без шерсти, разве что покрыта очень тонкими волосками. Это любопытно в сравнении с другими видами."
    alice.c "Поэтому я хотела бы прикоснуться к твоей коже, если ты не против. Можно начать с руки, но вообще я хотела бы изучить несколько участков тела."
    show alice neutral
    "Сердце пропускает удар. Она бывает очень прямолинейной, но это уже нечто. Кажется, её совсем не смущает собственная просьба."
    "Да я и не против, просто немного удивлён. А ещё у неё такие изящные пушистые руки..."
    mc.c "А, понял. Да, без проблем."
    "Я протягиваю ей руку ладонью вверх."
    show alice smile talk
    alice.c "Спасибо."
    show alice neutral
    "[alice.name] осторожно касается внутренней стороны моей руки указательным пальцем, а ладонью поддерживает её снизу."
    "Я чувствую мягкие подушечки на её ладони и пальцах, а по краям — прикосновение чёрной шерсти."
    "И даже что-то похожее на коготки вместо ногтей, как у некоторых антропоморфных зверей."
    "Она так нежна, что по спине пробегает дрожь. Наверное, я краснею как идиот."
    show alice thinking
    alice.c "Любопытно: здесь совсем нет волос, а сверху растут редкие очень тонкие волоски."
    alice.c "А в некоторых местах хорошо видны вены."
    "Она долго изучает руку, ладонь и пальцы, вслух записывая наблюдения и время от времени сверяясь с книгой."
    "Иногда она наклоняется поближе, разглядывает внимательнее и тихо произносит: «Хм» или «Ого»."
    "Зрелище довольно соблазнительное, но для неё это чисто научный интерес."
    "Затем она тянется к моей голове. Я думал, она попросит потрогать что-то ещё, но, похоже, любопытство взяло верх."
    "Лучше промолчу. Мне это нравится."
    "Она зажимает несколько волосков между пальцами и перекатывает их."
    show alice neutral talk
    alice.c "Хм-м..."
    show alice neutral
    "Теперь она изучает мои уши. Я раньше не задумывался, но у разных видов они действительно сильно отличаются."
    "Её костяшки задевают мою щёку, и по спине пробегает новая дрожь. Щекотно, но я стараюсь не дёргаться, чтобы не спугнуть её."
    "Она уже совсем близко. На секунду наши взгляды встречаются."
    show alice bashful
    "Она возвращается к своим заметкам."
    show alice neutral talk
    alice.c "Спасибо, это очень помогло."
    show alice neutral
    "На этом всё? Наверное, так даже лучше. Не хочу показывать, что мне это слишком понравилось."
    mc.c "Конечно, обращайся в любое время."
    mc.c "А можно спросить: раньше у тебя не было возможности изучить человека? Я видел здесь нескольких людей, да и ты много путешествовала?"
    show alice neutral talk
    alice.c "Нет, я не путешествовала. Другие люди здесь есть, но не думаю, что незнакомцу понравилась бы такая просьба. Мне самой было бы некомфортно."
    show alice neutral
    "Приятно знать, что ей со мной настолько комфортно, что она решилась попросить, пусть это и было неожиданно."
    mc.c "Значит, тебе со мной комфортно? Рад это слышать."
    show alice smile talk 2
    alice.c "Да."
    show alice smile
    "Когда она улыбается, улыбка у неё очень милая."
    mc.c "Рад, что смог помочь."
    show alice neutral talk
    alice.c "Не хочу задерживать тебя надолго. Я систематизирую заметки."
    mc.c "Тогда я пойду. Можешь снова попросить меня, я не против. Вообще-то мне понравилось."
    show alice smile
    alice.c "Я... думаю, ещё попрошу. Спасибо, [mc.name]. До встречи."
    mc.c "До скорого!"
    hide alice with dissolve
    "Я ухожу, оставляя её снова погрузиться в книги."
    "Буду ждать следующего приглашения."

    if(not fromGallery):
        $ alice.addLike(1)
        $ alice.addLove(1)
    
    return

label aliceLikeEvent3(fromGallery):
    $ location_cafe.showBackground()
    "Мы снова встретились с [alice.name] в кафе. Это уже становится нашей традицией. На этот раз она даже сама меня пригласила."
    "Кажется, мы стали ближе. Она чаще начинает разговор и ведёт себя со мной свободнее."
    "Обычно она рассказывает о делах в библиотеке и о «любопытных» вещах, которые недавно изучала."
    "Иногда я не успеваю за её рассуждениями, но именно тогда она по-настоящему раскрывается. Становится разговорчивой и оживлённой, а её улыбка такая милая..."
    window hide
    show alice smile with dissolve
    pause
    call playMusic(chillTheme) from _call_playMusic_6
    "Она всё ещё странная, но всё равно чудесная."
    "За парой чашек кофе, чем-нибудь сладким и приятной беседой часы пролетают незаметно."
    "Но мне кажется, на этом мы не закончим."
    show alice smile talk 2
    show alice smile
    alice.c "Ты согласился бы снова зайти ко мне сегодня? Я хотела бы продолжить с того места, где мы остановились."
    "Насколько помню, в прошлый раз мы расстались немного напряжённо. Мне показалось, что она чего-то смутилась, но, может, я слишком много думаю."
    mc.c "Конечно, [alice.name]. Я же говорил: заходи когда захочешь."
    show alice joy 
    alice.c "Я очень это ценю. Спасибо."
    show alice smile talk
    alice.c "Пойдём?"
    show alice smile
    mc.c "Веди."
    scene black with fade
    pause
    "Немного спустя мы уже на знакомой дороге."
    scene aliceshome with fade
    "Мы снова в её комнате с приятным запахом. Как всегда, чисто и аккуратно."
    show alice neutral talk with dissolve
    alice.c "Снова садись на кровать. А я пока найду свои записи с прошлого раза."
    hide alice with dissolve
    "Я сажусь на край кровати, пока [alice.name] устраивается за столом и начинает перебирать стопки книг и бумаг."
    "Не решаюсь сказать это вслух, но её задница едва помещается на стуле..."
    "У неё удивительно широкие бёдра, и в этой узкой юбке-футляре фигура становится грушевидной."
    "Плохо ли, что я так о ней думаю? Я не признавался ей в своих чувствах, да и она ничем не показывала, что хочет отношений."
    show alice thinking with dissolve
    alice.c "В прошлый раз мы закончили раньше, поэтому я хотела бы продолжить изучение кожи."
    mc.c "Конечно."
    show alice neutral talk
    alice.c "Не мог бы ты снять рубашку?"
    show alice neutral
    "Немного неожиданно, но меня это совершенно не смущает."
    mc.c "Конечно."
    "Я снимаю футболку и кладу её на пол у ног."
    "Подняв взгляд на [alice.name], замечаю, что она несколько секунд просто разглядывает мой торс, переводя глаза с места на место. Она просто хотела посмотреть?"
    call playMusic(heartTheme) from _call_playMusic_7
    show alice neutral talk
    alice.c "Как и в прошлый раз, можно я прикоснусь к тебе?"
    show alice neutral
    mc.c "Конечно."
    "[alice.name], как и прежде, нежно исследует мою кожу: поглаживает подушечками пальцев, проводит по ней тыльной стороной ладони, иногда слегка щиплет."
    "Ощущения те же: шелковистое прикосновение меха и чуть шероховатые подушечки лап. Щекотно. Я стараюсь сохранять невозмутимость, но иногда всё равно вздрагиваю."
    show alice neutral talk
    alice.c "Можешь лечь, если так тебе будет удобнее."
    show alice neutral
    mc.c "О-о, ладно."
    "Я соглашаюсь. Кровать и правда удобная, а сколько продлится осмотр — неизвестно."
    "...И это даже немного возбуждает. Почти романтично?"
    "Я ложусь, а [alice.name] неожиданно забирается коленями на кровать и наклоняется ко мне, чтобы продолжить осматривать грудь."
    "Она продолжает ласкать моё тело."
    window hide
    pause
    image alice touching part 1 = Movie(play="images/characters/alice/hscenes/touching/part1.webm")
    show alice touching part 1 with fade
    pause
    "Для меня всё становится довольно горячим, но [alice.name], возможно, ничего не замечает. Для неё это просто логичное физическое обследование."
    "Она водит ладонью кругами, иногда задевая кожу коготками. Немного нервирует, но я не хочу привлекать к этому внимание — вдруг она остановится."
    "..."
    "В комнате тихо, слышно лишь лёгкий шорох её одежды."
    "Мне уже не удаётся скрывать эмоции: [alice.name] время от времени поглядывает на меня. Наверное, на фоне учащённого пульса у меня меняется всё лицо."
    alice.c "Хм... этот запах."
    "Тишина нарушена. Мой запах?"
    mc.c "Прости, от меня пахнет?"
    alice.c "Да, но не неприятно."
    alice.c "Я читала о связи между людьми и обычными кошками."
    alice.c "Не знаю, как описать. Он не похож на запах кошачьих или других видов, с которыми я встречалась. Он какой-то успокаивающий... Я..."
    "[alice.name] замолкает и наклоняется надо мной, приближая голову к моей груди."
    "Она несколько раз глубоко втягивает воздух, прищурившись. Теперь её лицо всего в нескольких сантиметрах от моего, усы подрагивают."
    alice.c "*Мурлычет*"
    "Мурлыканье? Это точно был звук мурлыканья. У неё такая естественная реакция?"
    alice.c "Это..."
    "Она медленно закрывает глаза, чуть приоткрывает рот и опускает голову. Что происходит?"
    window hide
    pause
    image alice touching part 2 = Movie(play="images/characters/alice/hscenes/touching/part2.webm")
    show alice touching part 2 with fade
    pause
    "Всё моё тело покрывается мурашками, когда она проводит языком по моей обнажённой груди."
    "Я не был к этому готов. Её усы и спадающие волосы скользят по моей коже. Ощущения невероятные."
    "Я вздрагиваю, но не могу ничего сказать. [alice.name] будто заворожена, словно ею овладел звериный инстинкт. Никогда не видел её такой."
    "Это у кошек такой рефлекс — вылизывать друг друга? Или что-то ещё?"
    "Она наклоняется надо мной, юбка задирается до талии, открывая огромные бёдра, покрытые мехом. Я пользуюсь моментом и осторожно кладу на них ладонь."
    "Она не обращает внимания и продолжает водить языком по моей груди: поднимает голову, а затем снова опускает."
    "Её небольшая грудь прижимается и трётся о мои ноги и пах. Я изо всех сил сдерживаюсь, чтобы не встать: боюсь, что это прервёт её странный транс."
    "На заднем плане виляет хвост, подрагивают уши, а в груди слышно тихое мурлыканье."
    "Не знаю, что на неё нашло, но сейчас она сама на себя не похожа."
    mc.c "[alice.name]...?"
    scene black with fade
    "Она облизывает меня в последний раз, останавливается, открывает глаза и потрясённо смотрит на меня."
    window hide
    pause
    image alice touching end part 1 = Image("images/characters/alice/hscenes/touching/endPart1.webp")
    scene alice touching end part 1 with fade
    pause
    "Некоторое время мы оба не знаем, что сказать."
    "Её естественное движение подняло голову к моей. Сейчас она почти сидит у меня верхом."
    "Она тихо и часто дышит, переводя дух; брови озабоченно нахмурены."
    alice.c "Я-я... Я... Ах—"
    "Она начинает паниковать. Я кладу руку ей на талию, надеясь не дать ей резко отстраниться."
    mc.c "Всё нормально. Я в порядке. Просто ты ничего не сказала, поэтому..."
    alice.c "Я... не знаю, что на меня нашло."
    alice.c "Прости! Позволь мне—"
    "Кажется, она хочет отстраниться, поэтому я осторожно притягиваю её поближе."
    mc.c "Не волнуйся! Не паникуй. Всё хорошо!"
    alice.c "А, я..."
    "Она явно сама удивлена, что будто потеряла контроль. Но я не хочу, чтобы это зрелище заканчивалось."
    "Я могу только улыбнуться ей, чтобы дать понять: всё в порядке."
    alice.c "Со мной такого раньше не было... В твоём запахе есть что-то такое, будто меня накрыло волной."
    mc.c "Мне понравилось, правда."
    alice.c "Я... э-э... прости."
    mc.c "Не извиняйся."
    pause
    "В комнате тихо. Дыхание [alice.name] постепенно успокаивается."
    "Напряжение снова такое же, как в прошлый раз, только тогда мы отстранились."
    "Я не позволю этому повториться. Нужно действовать."
    "Я мягко прижимаю её за талию, приглашая приблизиться."
    "[alice.name] медленно наклоняется ко мне..."
    window hide
    pause
    image alice touching end part 2 = Image("images/characters/alice/hscenes/touching/endPart2.webp")
    scene alice touching end part 2 with fade
    pause
    "Мы нежно, но неловко целуемся."
    alice.c "М-м!"
    "[alice.name] хмурится и поначалу кажется напряжённой, но после нескольких поцелуев расслабляется."
    "Мы легко целуемся, её усы касаются моего носа..."
    "Недолго исследуем рты друг друга..."
    pause
    scene black with fade
    "Через некоторое время мы садимся."
    pause
    scene aliceshome with fade
    show alice bashful with dissolve
    "..."
    "Всё произошло так внезапно, что мы оба не знаем, что сказать."
    alice.c "Я..."
    mc.c "Не извиняйся, если только не считаешь, что это была ошибка."
    show alice sad
    alice.c "Нет... Я просто... Не планировала этого."
    mc.c "Ты не жалеешь?"
    alice.c "Я потеряла контроль, но..."
    show alice bashful talk
    alice.c "Думаю, именно этого я и хотела."
    "Она явно растеряна из-за случившегося. Может, мне стоит взять инициативу в свои руки."
    mc.c "Ты мне правда нравишься, [alice.name]."
    show alice surprise
    alice.c "Нравлюсь — в романтическом смысле?"
    mc.c "А как ты сама думаешь, что это было?"
    alice.c "Не знаю. У меня никогда... Ну, ничего такого не было."
    show alice bashful talk
    show alice bashful
    alice.c "Поверь, я не хотела навязываться."
    mc.c "Я давно этого хотел. Ты ничего плохого не сделала."
    show alice bashful talk
    alice.c "Что это значит?"
    mc.c "Мне понравилось. А тебе?"
    show alice smile
    alice.c "Д-да."
    mc.c "Тогда мы можем попробовать быть вместе, если ты хочешь. Начать отношения."
    "[alice.name] на секунду задумывается."
    "Она всё ещё пытается осмыслить произошедшее, и я притягиваю её к себе."
    hide alice with dissolve
    show alice hug with dissolve
    alice.c "Я в этом не разбираюсь, так что мне, возможно, понадобится твоя помощь..."
    mc.c "Конечно. Будем двигаться в твоём темпе."
    alice.c "Тогда... да. Пожалуйста, будь со мной нежен."
    hide alice with dissolve
    show alice kiss with dissolve
    scene black with fade
    "Мы приводим себя в порядок, даём [alice.name] немного успокоиться и прощаемся."
    "Наши отношения вдруг перешли на новый уровень."
    "Буду ждать нашей следующей встречи."

    if(not fromGallery):
        $ alice.addLike(1)
        $ alice.addLove(1)
        $ alice.isDateable = True
        "Теперь ты можешь приглашать [alice.name] на свидания."
    
    return

label aliceHEvent1(fromGallery):
    $ location_park.showBackground()
    "Я договорился снова встретиться с [alice.name]."
    "На этот раз [alice.name] почему-то не захотела идти в кафе, хотя обычно это часть её привычного маршрута."
    "Когда мы это обсуждали, она заметно нервничала, поэтому решили пойти в парк. Здесь всегда тихо."
    "А, вот и она."
    show alice neutral talk with dissolve
    call playMusic(heartTheme) from _call_playMusic_8
    alice.c "[mc.name]. Спасибо, что пришёл."
    show alice neutral
    mc.c "Я всегда рад тебя видеть, [alice.name]. Не за что!"
    "Я подошёл и слегка развёл руки для объятия. Она на секунду растерянно уставилась на меня."
    show alice smile talk
    alice.c "О-ох, да, конечно."
    window hide
    hide alice with dissolve
    show alice hug with dissolve
    pause
    alice.c "Прости, я всё ещё к этому привыкаю."
    mc.c "Не заставляй себя."
    alice.c "Нет, нет. Мне... нравится."
    hide alice with dissolve
    show alice bashful talk with dissolve
    alice.c "Я всё ещё пытаюсь разобраться в этих... отношениях, как их называют?"
    alice.c "Ты уже говорил, что всё нормально, но надеюсь, моя неопытность тебя не слишком отталкивает."
    show alice bashful
    mc.c "Ни капли, [alice.name]. Всё в твоём темпе, договорились?"
    show alice smile talk
    alice.c "Спасибо."
    alice.c "Я хотела немного поговорить... о нас."
    show alice neutral talk
    alice.c "Я, конечно, знаю, что люди так делают, но сама никогда этого не испытывала и почти не понимаю, как устроены отношения."
    alice.c "Я немного почитала об этом. Наверное, теперь нас можно считать парой, верно?"
    show alice neutral
    mc.c "Ну, необязательно навешивать ярлыки, если не хочется. Но да, можно считать нас парой."
    show alice neutral talk
    alice.c "Понятно."
    show alice bashful talk
    alice.c "Мы... ц-целовались... А в моей комнате я поставила нас, ну... в довольно пикантное положение."
    show alice neutral talk
    alice.c "И ты продолжаешь со мной «встречаться», как сам это называешь."
    mc.c "Именно. Мне правда нравится быть с тобой."
    alice.c "Мне тоже нравится быть с тобой."
    call stopMusic from _call_stopMusic
    alice.c "То есть я правильно понимаю, что когда-нибудь мы поженимся?"
    show alice neutral
    "*Глоток*"
    "О чём она вообще думает? Я хотел, чтобы мы не торопились, а у неё, похоже, совсем другие ожидания."
    "Она вообще не понимает, что говорит... Милая, но жутковатая."
    mc.c "*Кхм-кхм* Э-э... Ну..."
    mc.c "Мы... э-э... не обязаны сейчас об этом думать? Ну... пока?"
    "Меня уже бросает в жар. Что мне вообще сказать? Разве «да» или «нет» не поставит крест на отношениях? Ну зачем ты спрашиваешь, [alice.name]?!"
    mc.c "Люди... иногда не женятся, а просто смотрят, как всё сложится? Может ведь и не... *Кхм*, или..."
    show alice smile
    pause
    call playMusic(funnyTheme) from _call_playMusic_9
    "Кажется, [alice.name] вот-вот улыбнётся, глядя, как я тут потею."
    mc.c "...Ты... а? Что происходит?"
    show alice smile talk
    alice.c "Что такое? Ты не хочешь на мне жениться?"
    show alice smile
    "Боже. Что она вообще несёт?"
    mc.c "Я... я-я... Э-э..."
    show alice tease
    "Эта улыбка... Я раньше не видел у неё такого выражения лица."
    show alice tease talk
    alice.c "Хи-хи-хи-хи-и."
    "А?"
    alice.c "Ты сейчас строил такие смешные рожи, [mc.name]."
    show alice tease
    mc.c "Что происходит?"
    show alice tease talk
    alice.c "Я просто пошутила! Ну что, попалась моя шутка?"
    show alice tease
    "Слава богу."
    mc.c "А... Ха-ха..."
    "*Фух*"
    mc.c "Ух, ты меня здорово подловила, [alice.name]... Это было жутко..."
    mc.c "Но... я не то чтобы... Э-э..."
    show alice smile talk 2
    alice.c "Расслабься, [mc.name]. Прости, это, наверное, было немного жестоко с моей стороны."
    alice.c "Это я хотя бы понимаю. Просто немного тебя подразнила."
    "Сердце колотилось как бешеное и только сейчас начинает успокаиваться. Кто бы мог подумать, что она на такое способна?"
    mc.c "Ага, ты меня уделала. Ха-ха."
    show alice tease talk
    alice.c "Удивлена, что ты повёлся. Я иногда бываю несообразительной, но не настолько же."
    mc.c "Похоже, я тебя недооценил..."
    show alice smile talk 2
    alice.c "Ладно, это была такая разминка, как говорится. Но я и правда хотела встретиться в тихом месте не просто так."
    mc.c "Да?"
    show alice bashful talk
    alice.c "Я не шутила насчёт того, что изучаю всё это. Для меня всё в новинку. Я рассчитываю, что ты иногда будешь вести, и ты так и делал."
    show alice smile talk
    alice.c "Ты всё это время был настоящим джентльменом. Спасибо тебе."
    show alice bashful talk
    call playMusic(heartTheme) from _call_playMusic_10
    alice.c "Но, кажется... пришло время... немного большего. Того, что делают пары."
    show alice bashful
    "Кажется, я понял, к чему она ведёт. Пора немного отыграться."
    mc.c "Например? Не понимаю."
    show alice neutral
    alice.c "...Э-э..."
    "Я невольно улыбаюсь."
    show alice tease talk
    alice.c "...О-о-о... Поняла, ты мне мстишь. Наверное, заслужила."
    "Я притягиваю [alice.name] к себе."
    hide alice with dissolve
    show alice hug with dissolve
    mc.c "Хорошо. Ты готова?"
    alice.c "Д-да... Но не ко всему, ладно? Кажется, я ещё не готова..."
    mc.c "Конечно. Тебе не нужно ничего объяснять. Будем делать только то, чего ты сама хочешь."
    alice.c "Спасибо, [mc.name]."
    scene black with fade
    "Остальное осталось за кадром: мы просто пошли ко мне, держась за руки."
    $ location_home.showBackground()
    "Мы добрались до дома. Я отвёл [alice.name] в спальню, и мы сели на кровать."
    show alice smile with dissolve
    alice.c "Я хочу кое-что попробовать."
    mc.c "И что же?"
    alice.c "Кажется, мужчинам это нравится. И признаюсь, мне самой любопытно."
    scene black with fade
    "Мы медленно раздеваем друг друга, всё это время смущённо улыбаясь."
    "Я впервые вижу тело [alice.name]. Где-то скромное, а где-то — просто охуенное."
    "[alice.name] укладывает меня на кровать — передо мной открывается невероятно возбуждающее зрелище."
    call playMusic(sexyTheme) from _call_playMusic_11
    image alice handjob part 1 = Movie(play="images/characters/alice/hscenes/handjob/part1.webm")
    show alice handjob part 1 with fade
    pause
    "[alice.name] соблазнительно наклоняется между моих ног и нежно обхватывает мой стояк своими мягкими лапками."
    "Она медленно водит рукой вверх-вниз, лаская член по всей длине в плавном ритме."
    "Её небольшая упругая грудь покачивается вместе с телом, а шелковистые волосы падают мне на ногу."
    "Наши взгляды встречаются, и на её лице появляется лукавая улыбка."
    alice.c "Тебе... приятно? Всё правильно?"
    mc.c "Да, чёрт возьми, [alice.name], это охрененно."
    alice.c "Похоже, у тебя... впечатляющий экземпляр. Я не знала, чего ожидать."
    "[alice.name] тихо мурлычет и с нежностью смотрит мне в глаза, лишь иногда поглядывая на мой член."
    "Я не могу оторваться от прекрасных изгибов [alice.name]: она плавно покачивает попкой, а за ней в такт виляет хвост."
    "Мне приходится сдерживаться изо всех сил, чтобы не вскочить и не уложить её под себя, но я хочу уважать её желания."
    "Неопытная — возможно. Но уж точно не невинная."
    mc.c "Лучше, чем ты ожидала?"
    alice.c "Не знаю, подходит ли тут слово «лучше»... Я волнуюсь, как это вообще должно... Ладно, неважно..."
    "Коготки [alice.name] слегка впиваются мне в кожу, когда она хватается за бедро. От мысли, что мой член полностью в её власти, меня немного пробирает."
    "Но её лицо говорит само за себя. Я в нежных, заботливых руках."
    pause
    alice.c "Мне ускориться?"
    mc.c "Да, пожалуйста."
    image alice handjob part 2 = Movie(play="images/characters/alice/hscenes/handjob/part2.webm")
    show alice handjob part 2 with fade
    pause
    "[alice.name] ускоряется, двигая рукой больше чем вдвое быстрее."
    "Её хватка крепнет, и меня прошивает волной чистого удовольствия."
    "Она наклоняется ниже, приближая лицо к моему члену. Я почти чувствую её дыхание, а грудь то и дело касается меня."
    "[alice.name] будто заворожена этим зрелищем: смотрит вниз с любопытством, в котором пробивается незнакомая мне похоть."
    mc.c "Это невероятно, [alice.name]. Ты просто огонь."
    alice.c "Хм... Он такой горячий. Будто пульсирует."
    "Я не удерживаюсь и несколько раз глажу её красивые шелковистые волосы."
    "Не знаю, сколько ещё продержусь."
    mc.c "[alice.name], я скоро кончу."
    alice.c "Пожалуйста, кончай, когда захочешь."
    "От этих слов у меня что-то щёлкает в голове. Уверен, она сказала это случайно, но звучит чертовски сексуально."
    "Темп слишком бешеный, удовольствие нарастает."
    pause
    image alice handjob end = Image("images/characters/alice/hscenes/handjob/end.webp")
    scene alice handjob end with fadewhite
    pause
    mc.c "А-а-а-а-а-а~~"
    alice.c "Ой!"
    "Я кончаю прямо вверх мощными струями — так быстро, что глаз едва успевает заметить."
    "От экстаза взгляд мутнеет — мне уже плевать, куда может попасть сперма."
    "Я откидываю голову, чувствуя, как [alice.name] забирается рядом."
    scene alicepillowtalk with fade
    mc.c "*Тяжело дышу* Это было охуенно."
    "[alice.name] тепло улыбается."
    alice.c "Я рада."
    "Мы лежим рядом и переводим дыхание. Тихое дыхание [alice.name] касается моей груди, а её шерсть так приятна под ладонями."
    mc.c "Похоже, удовольствие получил только я."
    alice.c "Нет, мне тоже очень понравилось."
    "Она одаривает меня озорной улыбкой."
    alice.c "Не переживай за меня. Я сама этого хотела — и пока на большее не готова."
    mc.c "Я всегда к твоим услугам, [alice.name]."
    alice.c "Я запомню. С тебя спрошу."
    "Через несколько минут [alice.name] бросает взгляд на часы, садится и начинает одеваться."
    $ location_home.showBackground()
    call stopMusic from _call_stopMusic_1
    show alice neutral talk with dissolve
    alice.c "Спасибо за эксперимент. Кажется, я собрала все нужные данные."
    mc.c "А? О... э-э... спа-"
    show alice tease talk
    alice.c "Шучу."
    mc.c "Вот же хитрюга. Я знаю, что делать с такими проказницами."
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    "Этот поцелуй длится дольше всех предыдущих, и страсти в нём всё больше."
    hide alice with dissolve
    show alice smile talk 2 with dissolve
    alice.c "Пожалуй, я могла бы к этому привыкнуть."
    scene black with fade
    "Мы прощаемся. [alice.name] уходит с самой искренней улыбкой, какую я когда-либо у неё видел."

    if(not fromGallery):
        $ alice.addLove(1)

    
    return {'location':location_home}

label aliceHEvent2(fromGallery):
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_12
    "Я встретился с [alice.name] после её смены в библиотеке. Еле оторвал её от работы — коллегам пришлось буквально выпихивать её за дверь."
    "Она и правда предана своей работе. Хотя, как сама говорит, ей просто хочется весь день сидеть там и читать."
    show alice mad talk
    alice.c "Я же ничего плохого не делаю, я им помогаю! Там ещё столько всего нужно подшить и разложить!"
    show alice mad
    mc.c "[alice.name], смены ведь не просто так придумали. Ты не можешь торчать там целыми днями."
    show alice mad talk
    alice.c "Почему нет? Там ещё столько дел."
    show alice mad
    mc.c "Остальные и без тебя справятся. Начальству влетит, если выяснится, что сотрудник торчит там круглосуточно."
    show alice mad talk
    alice.c "*Фыркает* Я уже говорила им, что мне можно больше не платить."
    show alice mad
    "Я ещё не видел её такой оживлённой. Маленький клубочек раздражения. Вообще-то это даже мило."
    mc.c "В жизни есть кое-что помимо работы. Нужно иногда отдыхать. Давай просто расслабимся."
    show alice sad
    alice.c "Наверное, ты прав. В последнее время на работе напряжённо, я немного на взводе."
    alice.c "Прости, что тебе приходится видеть меня такой."
    mc.c "Да уж, маленькая [alice.name] вышла на тропу войны! Как страшно."
    show alice mad
    pause
    show alice tease
    alice.c "Забавно. Даже если смеёшься ты надо мной."
    mc.c "Думаю, ты выдержишь."
    show alice sad talk
    alice.c "Ар-р, всё равно бесит."
    mc.c "Давай помогу тебе отвлечься. Хочешь куда-нибудь сходить? Или просто посидеть в тихом месте?"
    show alice thinking
    alice.c "Хм-м. Хочу сбежать от здешнего шума. У меня дома сейчас беспорядок. Можно я поеду к тебе?"
    mc.c "У тебя беспорядок? Да там, наверное, всего лишь посуда со вчерашнего вечера."
    show alice neutral talk
    alice.c "Именно."
    show alice neutral
    "...А. Для такой чистюли, как она, это, наверное, уже катастрофа."
    mc.c "Ха-ха, ладно. Поехали ко мне — помогу тебе расслабиться."
    show alice smile talk 2
    alice.c "Спасибо, [mc.name]."
    scene black with fade
    $ location_home.showBackground()
    call playMusic(heartTheme) from _call_playMusic_13
    "Дома я наливаю [alice.name] чего-нибудь выпить, усаживаю её и болтаю о чём угодно, только не о книгах — помогаю ей успокоиться."
    "Последнее иногда даётся нелегко, но мы справляемся."
    "Мы некоторое время смотрим телевизор. Для [alice.name] это редкость, но иногда она неожиданно увлекается какой-нибудь ерундой вроде реалити-шоу — из чистого любопытства."
    "Думаю, сегодня ей стало легче — удалось отвлечься от рабочих забот."
    "Через некоторое время замечаю, что [alice.name] то и дело поглядывает на меня."
    show alice neutral with dissolve
    mc.c "Что-то случилось?"
    "Она поворачивается ко мне и наклоняется ближе."
    hide alice with dissolve
    show alice kiss with dissolve
    hide alice with dissolve
    show alice hug with dissolve
    alice.c "Спасибо. Сегодня я только мешала тебе, а ты так заботился обо мне."
    mc.c "Ты мне не мешала, [alice.name]. Я всегда рядом, если понадоблюсь."
    hide alice hug with dissolve
    show alice smile talk with dissolve
    alice.c "Рядом с тобой мне очень спокойно. Для меня это редкое чувство."
    alice.c "Я понимаю, что некоторых отталкивает моё поведение. Знаю, я немного не такая, как все."
    mc.c "[alice.name]... Да ты вовсе не—"
    alice.c "Нет, я знаю, что это правда. И меня это устраивает."
    alice.c "Мне помогает то, что ты обращаешься со мной как с любой другой. Я отталкиваю людей, но ты не отступил."
    show alice smile talk 2
    alice.c "Я правда это ценю. Спасибо, что ты со мной, [mc.name]."
    show alice smile
    "Искренние слова [alice.name] застали меня врасплох — я едва не прослезился. Но говорит она это не с грустью, а с тихим довольством."
    "Я пользуюсь моментом и накрываю её ладонь своей."
    mc.c "И тебе спасибо, что ты рядом."
    "[alice.name] отвечает тем же и переплетает свои пальцы с моими. Мы несколько мгновений сидим молча."
    show alice smile talk
    alice.c "[mc.name], можно я попрошу тебя ещё об одной услуге?"
    mc.c "Конечно. О чём ты?"
    show alice bashful talk
    alice.c "Я хочу снова попробовать что-нибудь сексуальное."
    "Как всегда, без обиняков. Не меняйся, [alice.name]."
    alice.c "Но я всё ещё не готова... ко всему."
    show alice smile talk
    alice.c "Хочу попросить тебя вести — только помни об этом."
    show alice smile
    "В голове мгновенно проносятся миллионы мыслей. Если я хоть часть выскажу вслух, [alice.name], наверное, улетит на Луну."
    mc.c "Что угодно?"
    show alice tease talk
    alice.c "В разумных пределах, [mc.name]."
    show alice tease
    "В прошлый раз удовольствие досталось мне. Теперь хочу доставить его [alice.name] — так, чтобы нам обоим понравилось..."
    mc.c "Конечно. У меня есть идея..."
    call playMusic(sexyTheme) from _call_playMusic_14
    scene black with fade
    "Я веду [alice.name] к кровати; по дороге мы полностью раздеваемся."
    "Мой член уже стоит колом. Я сажусь на край кровати, а [alice.name] стоит передо мной голая — от её соблазнительных изгибов кровь быстрее бежит по жилам."
    alice.c "Что ты хочешь сделать?"
    mc.c "Думаю, нам обоим понравится. Я говорил, что мне больше всего нравится в твоём теле?"
    alice.c "М-моё тело?"
    "Я кладу руки ей на бёдра и осторожно разворачиваю её."
    image alice thighjob start = Image("images/characters/alice/hscenes/thighjob/start.webp")
    scene alice thighjob start with fade
    mc.c "Твои бёдра, ляжки и эта аппетитная задница."
    alice.c "Моя... попка?"
    mc.c "Всё целиком. Ты сводишь меня с ума, [alice.name]."
    "Я опускаю [alice.name], устраивая свой член между её бёдер."
    alice.c "Ты ведь не собираешься...?"
    mc.c "Нет, пока ты не будешь готова. Просто потрёмся телами — будет приятно, поверь."
    alice.c "Ну... ладно."
    "Я осторожно усаживаю её к себе на колени. Её большая задница прижимается к моим бёдрам, а член оказывается в жарком плену между её ляжек."
    "Влажные складки её пизды касаются головки моего члена, и [alice.name] вздрагивает."
    mc.c "Готова?"
    "Она едва заметно кивает..."
    image alice thighjob part 1 = Movie(play="images/characters/alice/hscenes/thighjob/part1.webm")
    show alice thighjob part 1 with fade
    pause
    "Я направляю её бёдра вверх-вниз; мягкие пухлые ляжки обхватывают мой член. Шерсть трётся о него, даря совершенно невероятные ощущения."
    alice.c "А-ах~ Я чувствую~"
    "Её нежная пизда увлажняется, пока мы опасно близко играем с проникновением. Коготки слегка впиваются мне в бёдра, а она сама двигается вверх-вниз."
    mc.c "Это так охрененно..."
    alice.c "Да... теперь понимаю~"
    "Её шерсть нежно скользит по мне, придавая ощущениям особую шелковистость. Хвост тоже виляет и порхает у меня по груди."
    "Пизда [alice.name] уже насквозь мокрая. Пора добавить жару."
    mc.c "Вот так, обопрись на меня..."
    image alice thighjob part 2 = Movie(play="images/characters/alice/hscenes/thighjob/part2.webm")
    show alice thighjob part 2 with fade
    pause
    "Теперь я двигаюсь напористее, толкаясь бёдрами вверх-вниз и крепко направляя её бёдра рукой."
    "Её огромная задница с приятным шлепком опускается мне на поясницу."
    "Я не удерживаюсь и поднимаю руку, сжимая её грудь, которая так давно меня дразнила."
    alice.c "Ах! О боже~"
    mc.c "Блядь, как же ты хороша, [alice.name]~"
    "Мы ускоряемся, и из груди вырываются стоны удовольствия. [alice.name] тянется назад, хватая меня за голову; её коготки опасно близко к коже."
    "Соки [alice.name] заливают её вход и покрывают мой член и бёдра — между её ног становится влажно и непристойно скользко."
    "Хочу, чтобы это длилось вечно, но ощущения такие охрененные, что я долго не продержусь."
    alice.c "*Ха*. *Ха*. *Хааах*."
    alice.c "Я сейчас кончу~"
    mc.c "*Ха*. Я тоже. *Ха*."
    alice.c "Ах~ А-а-а~ А-А-А-А-А-А-А-А~~~~~"
    image alice thighjob end = Image("images/characters/alice/hscenes/thighjob/end.webp")
    scene alice thighjob end with fadewhite
    pause
    "Мы одновременно кончаем, срываясь на крик экстаза."
    "Сперма выстреливает у меня между её бёдер — со стороны это, наверное, нелепое зрелище."
    "Мы падаем на кровать. Мой член всё ещё зажат между её толстыми ляжками; мы дрожим и жадно глотаем воздух."
    scene black with fade
    "Мы ещё немного лежим. [alice.name] прижимается спиной ко мне, а я обнимаю её."
    scene alicepillowtalk with fade
    pause
    "Нас окутывает блаженное послевкусие оргазма. От жара [alice.name] я весь взмок."
    "Иначе и быть не могло."
    mc.c "Ну как тебе такой опыт?"
    alice.c "*Тяжело дышит* Определённо... *Тяжело дышит* что-то..."
    "Немного погодя [alice.name] идёт в душ привести себя в порядок."
    $ location_home.showBackground()
    show alice smile talk with dissolve
    alice.c "Я не знала, что это считается сексуальной практикой."
    mc.c "Не уверен, что обычно считается... Но я найду любой повод добраться до твоих ляжек."
    show alice tease talk
    alice.c "А раньше ты был таким джентльменом..."
    show alice tease
    mc.c "Думаю, я умею и то и другое."
    hide alice with dissolve
    show alice hug with dissolve
    alice.c "Ты помог мне сегодня проветрить голову. Спасибо."
    mc.c "Тяжёлая работа, но кто-то же должен её делать."
    alice.c "...Дурачок."
    scene black with fade

    if(not fromGallery):
        $ alice.addLove(1)
    
    return

label aliceHEvent3(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_15
    "Неожиданный поворот: [alice.name] сама попросила встретиться у меня в баре."
    "Она почти не пьёт, поэтому я редко вижу её здесь — только когда тащу сюда на свидание или когда она изредка выбирается с коллегами из библиотеки."
    "Иногда она не против составить мне компанию, но здесь бывает шумновато. Совсем не то, к чему она привыкла."
    "Так что её просьба встретиться здесь сегодня вечером довольно необычна. В любом случае я сказал, когда буду на месте."
    "А, вот и она."
    show alice smile talk 2 with dissolve
    alice.c "Привет, [mc.name]! Как проходит [_(timeOfDay)]?"
    mc.c "Привет, [alice.name]! Не ожидал увидеть тебя здесь."
    show alice thinking
    alice.c "Ой, я думала..."
    mc.c "Да шучу я, [alice.name]."
    show alice surprise
    alice.c "А, э-э, да... конечно."
    "Немного жестоко с моей стороны, но её искренность до сих пор иногда меня обезоруживает."
    hide alice with dissolve
    show alice hug with dissolve
    pause
    mc.c "Прости, [alice.name], я не хотел тебя дразнить."
    alice.c "Иногда трудно понять."
    mc.c "Хорошо, что сегодня посетителей немного."
    hide alice with dissolve
    show alice smile talk with dissolve
    alice.c "Это хорошие новости, спасибо."
    mc.c "У тебя особый повод? Или просто захотелось попробовать что-то новое? Знаю, это не твоё любимое место."
    show alice bashful
    alice.c "А, э-э... Да нет, особого повода нет..."
    "Похоже, она что-то скрывает. Но давить не буду."
    mc.c "Давай сядем за столик. Я попрошу кого-нибудь подменить меня за стойкой и закончу смену."
    show alice smile
    alice.c "Да, давай."
    "Я оставляю бар на сотрудника. Теперь он справится сам."
    mc.c "Что тебе налить? Сегодня есть клюквенный сок."
    show alice neutral talk
    alice.c "Нет, пожалуй, я выпью что-нибудь алкогольное. Ты тогда не видел, но в прошлый раз коллега купила мне напиток. Он оказался... вполне сносным."
    show alice neutral
    mc.c "О, вот это сюрприз. Помнишь, какой именно?"
    "Она показывает на бутылку за стойкой, и мы идём к столику."
    mc.c "За встречу!"
    show alice smile talk 2
    alice.c "За встречу!"
    show alice neutral
    "Она осторожно отпивает, и нос у неё смешно подрагивает, когда она подносит бокал к губам."
    "Двигается она нерешительно, как я и ожидал, но старается не подавать виду."
    "Она просто пытается меня порадовать? Тут явно что-то ещё."
    mc.c "Тебе не нужно себя заставлять."
    show alice bashful talk
    alice.c "Вовсе нет, я... привыкаю."
    show alice smile talk
    alice.c "Ведь принято иногда выпить вместе, правда?"
    show alice smile
    "Обычно она говорит прямо, поэтому даже маленькая ложь у неё сразу заметна."
    "Не понимаю, в чём дело, но допытываться не стоит."
    mc.c "Ничего, ещё сделаем из тебя любительницу выпить."
    show alice smile talk
    alice.c "Не надейся..."
    scene black with fade
    "Мы проводим спокойный вечер, как на обычном свидании, только на этот раз выпиваем по паре бокалов."
    "Она рассказывает о работе и пересказывает последний роман, который читала..."
    "[alice.name] удивляет меня: выпивает ещё пару бокалов вина. Я никогда не видел, чтобы она пила больше одного."
    "Всего пару бокалов, но видно, что они уже дают о себе знать. Она миниатюрная, да и переносит алкоголь плохо."
    "Рискну предположить, что она слегка захмелела."
    $ location_bar.showBackground()
    show alice smile with dissolve
    "Алкоголь явно помогает ей расслабиться: какое-то время мы держимся за руки через стол, а она даже не смущается."
    "Прошло уже пару часов, и вряд ли она захочет ещё. Пожалуй, пора заканчивать вечер."
    show alice smile talk 2
    alice.c "У меня... голова и мысли немного плывут. Это и есть опьянение, да?"
    alice.c "Пожалуй, теперь я понимаю, чем это нравится людям."
    alice.c "Но не каждую неделю. Некоторые мои коллеги обязательно ходят куда-нибудь каждую пятницу."
    show alice smile
    mc.c "Вот это мои идеальные клиенты."
    show alice tease talk 
    alice.c "Я ведь не совсем твоя целевая аудитория. Ты же не пытаешься меня переманить?"
    show alice tease 
    mc.c "С такой упрямой девушкой, как ты, я бы всё равно проиграл эту битву."
    show alice thinking
    alice.c "Хм... Мне и раньше такое говорили. Не совсем понимаю, что имеют в виду."
    mc.c "Ты просто остаёшься собой. Это хорошо."
    show alice smile
    alice.c "Поверю тебе на слово."
    "Бокалы опустели. Кажется, наш вечер подходит к естественному завершению."
    mc.c "Хочешь, я провожу тебя домой?"
    call playMusic(heartTheme) from _call_playMusic_16
    show alice bashful
    alice.c "..."
    "Она слегка ёрзает на стуле и выглядит встревоженной."
    show alice bashful talk
    alice.c "Можно спросить... Я могу снова приехать к тебе?"
    alice.c "Я хотела бы продолжить... разговор..."
    mc.c "Конечно! Тебе не нужно спрашивать, [alice.name]. Приезжай когда захочешь."
    show alice smile
    alice.c "Замечательно!"
    scene black with fade
    "Мы идём ко мне. У [alice.name] слегка кружится голова, и всю дорогу она осторожно держится за мою руку."
    "Она почти не говорит и выглядит напряжённее обычного; большую часть пути домой не поднимает головы."
    "Может, это просто алкоголь так на неё действует."
    $ location_home.showBackground()
    "Мы приходим домой, и я направляюсь к дивану."
    "Но [alice.name] осторожно тянет меня за рубашку."
    show alice bashful
    alice.c "Э-э... [mc.name]..."
    "[alice.name] обычно не ходит вокруг да около и не стесняется — она всегда такая прямолинейная."
    alice.c "Этот алкоголь..."
    mc.c "О нет, тебе плохо, [alice.name]? Сядь. Чем помочь?"
    show alice sad
    alice.c "Нет, нет, нет... Я не это имела в виду..."
    show alice bashful
    alice.c "Я слышала выражение... «жидкая храбрость». Это так работает?"
    mc.c "Ну, э-э, да. У большинства алкоголь снижает скованность..."
    "К чему она ведёт?"
    alice.c "Не знаю. В голове полный сумбур."
    alice.c "Настоящая причина, по которой я попросила встретиться..."
    alice.c "Кажется, я готова... Точнее, хочу быть готовой... к тебе..."
    "Я почти уверен, что понял, о чём она."
    show alice sad
    alice.c "Но я так сомневаюсь. Подумала, что это может помочь..."
    mc.c "[alice.name]... Тебе не нужно себя заставлять. Я же говорил, что никогда не буду давить на тебя."
    show alice bashful
    alice.c "Ты прав, и ты сдержал слово. Я правда, правда это ценю."
    alice.c "Я правда... хочу этого..."
    show alice bashful talk
    alice.c "Я хочу впервые переспать с тобой. Мне просто нужен был небольшой толчок."
    "Я могу только взять её за руки и постараться, чтобы ей было как можно спокойнее."
    mc.c "[alice.name], как скажешь. Только дай мне знать."
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    "В редком порыве инициативы [alice.name] сама притягивает меня и целует."
    hide alice with dissolve
    show alice hug with dissolve
    mc.c "Только если ты уверена."
    alice.c "Я готова..."
    scene black with fade
    "Мы спокойно и не спеша раздеваемся, постепенно привыкая к прикосновениям друг друга."
    "После нескольких нежных ласк и поцелуев я чувствую, что она готова."
    image alice missionary attempt start = Image("images/characters/alice/hscenes/missionary/start.webp")
    show alice missionary attempt start with fade
    pause
    "[alice.name] ложится обнажённая, открываясь мне; в её взгляде смешались нервозность и ожидание."
    "Её прекрасное тело передо мной, но плечи всё ещё напряжённо приподняты."
    "Шерсть вокруг её влагалища слегка блестит от влаги."
    alice.c "Так... нормально?"
    mc.c "Просто устройся поудобнее."
    mc.c "Помни: если захочешь, чтобы я остановился, просто скажи. Не молчи."
    alice.c "Я... Спасибо..."
    "Я беру её за бёдра и осторожно развожу их."
    mc.c "Я войду."
    image alice missionary attempt part 1 = Movie(play="images/characters/alice/hscenes/missionary/part1.webm")
    show alice missionary attempt part 1 with fade
    pause
    "Я начинаю предельно осторожно, вводя лишь самую головку."
    "Она такая тугая и всё ещё очень напряжена."
    alice.c "А-а-а, я чувствую..."
    mc.c "Расслабься... Всё хорошо."
    "Я иногда вхожу чуть глубже и чувствую, как она напрягается, сжимая кулак."
    alice.c "А-А-Ах! О-о-о~"
    mc.c "Слишком?"
    alice.c "Это... Продолжай."
    "Она прищуривается; мы оба чувствуем, как тесно соединились."
    alice.c "Так... *Ах* хорошо?"
    mc.c "Это прекрасно, [alice.name]. Ты прекрасна."
    "Мы не спешим, и я чувствую, как [alice.name] понемногу расслабляется."
    "Даже при такой медленной скорости ощущения невероятные — её тугая пизда сжимает мой член."
    alice.c "Можешь... *Ах* быстрее..."
    "Я не решаюсь ускоряться слишком сильно — попробую лишь немного."
    mc.c "Дай мне руки."
    image alice missionary attempt part 2 = Movie(play="images/characters/alice/hscenes/missionary/part2.webm")
    show alice missionary attempt part 2 with fade
    pause
    "Я осторожно беру её за руки."
    "Не слишком быстро и не слишком глубоко: я осторожно вхожу и выхожу, словно с каждым толчком понемногу преодолеваю новый барьер внутри неё."
    "Когда она напрягается, коготки слегка впиваются мне в ладони."
    alice.c "А-а-а! А-а-а! М-м-м!"
    "Не могу понять, ей больно или приятно, но моё собственное удовольствие подталкивает продолжать."
    mc.c "О-ох, [alice.name]..."
    "Её дыхание становится чаще, она больше не может смотреть мне в глаза."
    "Через её ладони я чувствую каждую дрожь."
    alice.c "Так и должно... Ах! быть больно—А-А-Ах?"
    mc.c "Если слишком больно..."
    alice.c "А-Ах! А-А-Ах! [mc.name]! О-остановись!"
    image alice missionary attempt part 3 = Image("images/characters/alice/hscenes/missionary/part3.webp")
    show alice missionary attempt part 3 with fade
    pause
    call playMusic(sadTheme) from _call_playMusic_17
    "Я тут же выхожу, боясь причинить ей боль. Она откидывается назад, морщась; грудь быстро вздымается и опускается."
    mc.c "Прости, [alice.name]! Ты в порядке?"
    alice.c "*Ха-а* *Ха-а*"
    alice.c "Прости... Это было *Ха-а* слишком..."
    mc.c "Не извиняйся, [alice.name]. Не надо..."
    "Я остаюсь рядом, пока она переводит дыхание, и нежно глажу её стройный живот."
    "Её взгляд смягчается; глаза увлажнились от пережитого."
    alice.c "Мне очень жаль... Сегодня я не могу..."
    mc.c "Всё хорошо, правда. Я не хочу причинить тебе боль."
    alice.c "Наверное, я так тебя разочаровала."
    mc.c "Ни за что, [alice.name]. Я просто хочу, чтобы ты была счастлива."
    alice.c "Ты такой добрый, [mc.name]..."
    alice.c "Некоторые моменты были... приятными... Наверное. Просто всего оказалось слишком много."
    mc.c "Понимаю. Всё хорошо."
    "Даже если секс не удался, передо мной всё ещё лежит прекрасная обнажённая девушка, которой сейчас нужны нежность и забота."
    "Я наклоняюсь к ней."
    image alice missionary attempt part 4 = Image("images/characters/alice/hscenes/missionary/part4.webp")
    show alice missionary attempt part 4 with fade
    pause
    "Мы целуемся глубоко и страстно, и я буквально чувствую, как её напряжение уходит."
    alice.c "М-м-м~"
    "Я нежно ласкаю её тело и успокаиваю [alice.name], давая понять единственным доступным мне способом, что всё в порядке."
    image alice missionary attempt part 3 = Image("images/characters/alice/hscenes/missionary/part3.webp")
    show alice missionary attempt part 3 with fade
    pause
    alice.c "Спасибо, [mc.name]. Обещаю... в следующий раз..."
    mc.c "Ты мне ничего не должна, [alice.name]. Мы будем делать только то, с чем тебе комфортно, помнишь?"
    alice.c "*Ха-а* Да..."
    image alice missionary attempt part 4 = Image("images/characters/alice/hscenes/missionary/part4.webp")
    show alice missionary attempt part 4 with fade
    pause
    scene black with fade
    "Мы ещё немного обнимаемся и целуемся, пока она окончательно не успокаивается."
    "Через некоторое время [alice.name] идёт в душ. У неё всё ещё кружится голова, ноги слегка подкашиваются от пережитого."
    $ location_home.showBackground()
    show alice bashful talk with dissolve
    alice.c "Мне пора. Завтра нужно рано вставать."
    show alice bashful
    mc.c "Конечно, [alice.name]. Я отлично провёл с тобой день."
    show alice sad talk
    alice.c "И ещё раз, прости, я—"
    "Я мягко прикладываю палец к её губам и притягиваю её к себе. Не хочу слышать ещё одно извинение."
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    alice.c "М-м!"
    hide alice with dissolve
    show alice hug with dissolve
    pause
    mc.c "Всё было хорошо, [alice.name]. У нас полно времени, чтобы всё попробовать."
    alice.c "Спасибо, [mc.name]. Я..."
    alice.c "..."
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    scene black with fade
    "[alice.name] машет мне на прощание и выходит за дверь. К счастью, она улыбается."

    if(not fromGallery):
        $ alice.addLove(1)
        $ alice.virgin = False
        $ alice.virginityLossDate = day
    
    return {'location':location_home}

label aliceHEvent4(fromGallery):
    $ location_home.showBackground()
    show alice smile with dissolve
    call playMusic(chillTheme) from _call_playMusic_18
    "[alice.name] сегодня у меня. Устроили домашнее свидание."
    "Я предложил приготовить ужин в последний момент. Представлял себе романтический вечер при свечах."
    "Увы, готовлю я паршиво, а моя квартира прямо орёт: здесь живёт мужик, и женской руки тут не бывало."
    "К счастью, она как всегда вежлива. При всей своей прямолинейности она не настолько груба, чтобы жаловаться на чужую стряпню."
    "Нам обоим нравится проводить время дома. [alice.name] может спокойно рассказывать о новых книгах и своих исследованиях."
    "Несмотря на нашу не самую удачную попытку близости в прошлый раз, между нами всё по-прежнему."
    "Я всё равно дорожу тем моментом и не считаю его провалом. Но мне интересно, что думает она."
    "Тогда она извинялась и даже смущалась, но с тех пор сама об этом не заговаривала."
    show alice smile talk 2
    alice.c "Необычный вкус, [mc.name]. Я такого раньше не пробовала."
    show alice smile
    "Возвращаемся к еде. Я на скорую руку сварганил жареный рис, закинув туда остатки специй и соусов, какие нашлись."
    "Мой кулинарный репертуар скуден, и это заметно. Ничего выдающегося."
    mc.c "Э-э, да... Так себе вышло, да? Не надо быть вежливой, [alice.name]."
    alice.c "..."
    "Кажется, она уходит от ответа, отправляя в рот ещё одну ложку. Ловко, [alice.name]..."
    mc.c "Когда готовлю только для себя, обычно обхожусь простыми блюдами, понимаешь?"
    show alice smile talk
    alice.c "Нет, я очень ценю это. Чужая готовка всегда вкуснее. Да и мне надоедает собственная стряпня."
    show alice smile
    mc.c "А что ты обычно готовишь?"
    show alice thinking
    alice.c "Чаще всего овощи на пару и нежирную рыбу — например, тунца или треску. Иногда лосося."
    alice.c "В них мало калорий и жира. Стараюсь следить за фигурой."
    mc.c "За фигурой? [alice.name], да ты стройная как тростинка."
    show alice bashful talk
    alice.c "Вообще-то в последнее время юбка стала мне тесновата. Странно: талия вроде не изменилась."
    show alice bashful
    "У [alice.name] и так пышные бёдра, и я уже давал понять, как сильно мне нравятся её задница и ляжки."
    "Мысль о том, что они станут ещё сочнее... аж заводит. Надо бы не ляпнуть это вслух."
    show alice neutral talk
    alice.c "Думаю, это из-за того, что мы стали чаще проводить время вместе и ходить куда-нибудь поесть, правда?"
    alice.c "Говорят, в начале отношений парочки обычно набирают вес вместе."
    show alice neutral
    "«Парочки»... Кажется, она впервые так нас назвала. Сердце аж затрепетало."
    "Кажется, я краснею, как школьница."
    show alice neutral talk
    alice.c "Что-то не так, [mc.name]?"
    show alice neutral
    mc.c "Да нет, ничего. И не глупи, не надо переживать из-за веса. Ты прекрасно выглядишь."
    show alice smile talk
    alice.c "Не хотелось бы менять весь гардероб, но спасибо. Буду просто внимательнее следить за собой."
    show alice smile
    scene black with fade
    "Мы доедаем ужин. И каким-то чудом никто не пожаловался..."
    "Потом перебираемся на диван."
    $ location_home.showBackground()
    show alice neutral with dissolve
    mc.c "Точно не хочешь вина, [alice.name]? Я принёс домой то самое, которое тебе вроде понравилось."
    show alice neutral talk
    alice.c "Хм, нет, спасибо, [mc.name]."
    call playMusic(sadTheme) from _call_playMusic_19
    show alice bashful talk
    alice.c "В прошлый раз оно сильно ударило мне в голову. Не хочу повторения той ночи."
    "Той ночи... Она жалеет о том, что мы сделали? Ещё не была готова? Я слишком на неё надавил?"
    mc.c "[alice.name]... Я..."
    show alice neutral talk
    alice.c "Не так выразилась, прости. Я хотела сказать..."
    show alice sad
    alice.c "..."
    "Она на секунду задумывается."
    show alice sad talk
    alice.c "Не думаю, что алкоголь пошёл мне на пользу. Я хотела, как говорят, «расслабиться», но из-за него мысли путались."
    alice.c "Мне это не понравилось — вышло наоборот. Я пыталась заставить себя чувствовать то, к чему не привыкла."
    alice.c "Я хотела оправдать твои ожидания, но в голове был полный... бардак. И я слишком разволновалась."
    show alice sad
    mc.c "Оправдать? Ожидания? [alice.name], тебе не нужно ничего изображать — просто будь собой. Мне нужна настоящая ты."
    mc.c "Я правда не жду от тебя ничего сверх того, что тебе самой хочется. Мне очень жаль, если я заставил тебя почувствовать давление..."
    show alice neutral talk
    alice.c "Нет, ты меня ни к чему не принуждал. Это всё шло изнутри меня."
    alice.c "Теперь я, кажется, это понимаю. В следующий раз хочу подойти к этому с ясной головой."
    show alice neutral
    "В следующий раз... Значит, он всё-таки будет!"
    mc.c "Конечно, [alice.name]. Не переживай из-за этого."
    call playMusic(heartTheme) from _call_playMusic_20
    hide alice with dissolve
    show alice kiss with dissolve
    hide alice with dissolve
    show alice smile with dissolve 
    "[alice.name] целует меня в щёку, пока я отворачиваюсь."
    show alice smile talk 
    alice.c "Я не хотела тебя пугать. Теперь понимаю, как это могло прозвучать."
    show alice smile 
    mc.c "Всё нормально. Я просто рад, что это тебя не оттолкнуло."
    show alice smile talk 2
    alice.c "Вообще-то ты был очень добр ко мне. Я была не в лучшем состоянии, но ты вёл себя как настоящий джентльмен."
    alice.c "Не думаю, что могла бы пожелать себе партнёра лучше для первого раза."
    show alice smile
    "Это... невероятно трогательно. Сердце пропускает удар."
    show alice smile talk 2
    alice.c "Ты помогал мне со всем этим и сегодня приготовил для меня ужин..."
    show alice tease talk
    alice.c "...И прямо сейчас меня к тебе безумно тянет."
    show alice tease
    "На её лице появляется тёплая улыбка с лёгкой ноткой соблазна."
    "Она кладёт руку мне на колено и чуть наклоняется ближе. Мне не нужно повторять дважды."
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    "Мы долго целуемся в губы, слегка приоткрывая их."
    "Я притягиваю её поближе, кладу руку на её пышное бедро и нежно сжимаю покрытую мехом ляжку."
    "Мне хочется, чтобы такие моменты длились вечно, но, кажется, на этом вечер не закончится."
    hide alice with dissolve
    show alice smile talk 2 with dissolve
    alice.c "Понимаю, что ты можешь сомневаться, поэтому скажу прямо: я готова и хочу попробовать снова."
    alice.c "Если ты, конечно, не против."
    show alice smile
    mc.c "Ты уверена, [alice.name]? Не нужно себя заставлять."
    show alice smile talk
    alice.c "Абсолютно. Я морально подготовилась. Есть интересные исследования о психологии тревоги, страха..."
    "Даже сейчас она собирается рассказывать об исследованиях и книгах. Подготовка к сексу по учебникам?"
    "Звучит совсем не романтично, но... именно за это я её и люблю."
    alice.c "...Ладно, прости, не стоило начинать лекцию."
    show alice smile
    "По её лицу видно: в этот раз она спокойнее, согласна и морально готова. Беспокоиться не о чем."
    "Кого-то её деловой тон в таких вопросах мог бы оттолкнуть."
    "Но в [alice.name] меня это безумно заводит. Мне не нужно повторять дважды."
    scene black with fade
    "Мы не спеша раздеваем друг друга, и обтягивающая одежда соскальзывает с её соблазнительно пышного тела."
    "После нескольких ласк и поцелуев я веду [alice.name] к кровати."
    call playMusic(sexyTheme) from _call_playMusic_21
    image alice missionary start = Image("images/characters/alice/hscenes/missionary2/start.webp")
    show alice missionary start with fade
    pause
    "[alice.name] ложится, открывая мне стройное тело. Небольшая упругая грудь соблазнительно покачивается."
    "Между её аппетитно толстыми бёдрами виднеется киска, влажно поблёскивая и будто маня меня."
    "В её взгляде тепло. Она расслаблена, готова и даже предвкушает то, что сейчас будет."
    alice.c "Я готова, если ты тоже этого хочешь, [mc.name]."
    mc.c "Конечно, [alice.name]."
    alice.c "Пожалуйста... будь нежным. Но не переживай — я справлюсь и доверяю тебе."
    "По её движениям понятно: в этот раз всё получится. Я просто это чувствую."
    "Я быстро целую её и подвожу член к её входу, предвкушая, как он окунётся в её тепло."
    image alice missionary part 1 = Movie(play="images/characters/alice/hscenes/missionary2/part1.webm")
    show alice missionary part 1 with fade
    pause
    "Головка проскальзывает между нежных складок [alice.name], погружаясь в её тёплую влагу."
    "Её бёдра вздрагивают, когда я вхожу, но в отличие от прошлого раза она начинает расслабляться."
    alice.c "О-ох~"
    mc.c "Всё хорошо?"
    alice.c "Д-да... Я чувствую его, но... всё нормально..."
    "Она несколько раз глубоко вдыхает. Брови нахмурены, но на лице появляется искренняя улыбка."
    "Я мягко двигаюсь взад-вперёд, поддерживая её ноги под коленями, чтобы найти удобный угол."
    "Мой член входит чуть глубже головки, и я чувствую, как её тугая киска сжимает ствол."
    alice.c "Ах~ А-а~"
    "Её киска всё ещё тугая, но теперь мы оба спокойнее, и у нас получается лучше."
    mc.c "Ты невероятно хороша, [alice.name]..."
    alice.c "Ты... тоже... Мне н-нравится..."
    "Я больше ничего и не хочу. Пусть ей будет хорошо."
    "Мы остаёмся так ненадолго, не желая торопиться."
    alice.c "Можешь... Ах~ немного быстрее, если хочешь..."
    mc.c "Только если ты уверена, [alice.name]. Я не против и так."
    alice.c "Я хочу почувствовать... Ах~ ещё..."
    image alice missionary part 2 = Movie(play="images/characters/alice/hscenes/missionary2/part2.webm")
    show alice missionary part 2 with fade
    pause
    "Я начинаю двигаться чуть быстрее и глубже."
    "Киска [alice.name] постепенно принимает мой член глубже, чем раньше."
    alice.c "О-о-ох~ А-а-а~"
    "Её стоны становятся громче и чаще. Я бы волновался, но чувствую: ей приятно, а не больно."
    mc.c "Это... невероятно."
    alice.c "Да~ Так хорошо..."
    "Она всё ещё очень тугая, но хорошо справляется."
    "[alice.name] извивается от удовольствия; такого похотливого выражения на её лице я ещё не видел. Мне всё труднее сдерживаться."
    alice.c "Я и не... Ах~ знала, что так будет~"
    "Она пытается что-то сказать, но удовольствие сбивает её с мысли."
    "Невероятное ощущение. Нежная, милая, скромная [alice.name] стонет на моём члене."
    "Уверен, ей так же хорошо, как и мне. Её горячее, тугое лоно засасывает меня глубже, и по спине бегут мурашки."
    alice.c "[mc.name]~"
    alice.c "Ещё..."
    "Мы уже прошли этап, когда я проверял её после каждого движения. Больше я не могу сдерживаться."
    "Я тянусь к ней, чтобы обнять..."
    image alice missionary part 3 = Movie(play="images/characters/alice/hscenes/missionary2/part3.webm")
    show alice missionary part 3 with fade
    pause
    "Мы переплетаем пальцы, а я наклоняюсь и вхожу глубже."
    "[alice.name] смотрит мне прямо в глаза."
    alice.c "О-о-о-ох~! А-а-а-а~~!"
    "Её маленькая грудь мягко подпрыгивает, когда я почти полностью вхожу в неё."
    mc.c "Ах-х~ Как же ты хороша."
    alice.c "Это невероятно~~ Я никогда... А-Ах~ не чувствовала... О-о-ох~ ничего подобного..."
    alice.c "Я... Ах~"
    "[alice.name] отдаётся удовольствию, закатывает глаза и выпускает протяжные стоны."
    "Я чувствую каждую складочку внутри [alice.name] и не знаю, сколько ещё продержусь."
    image alice missionary part 4 = Movie(play="images/characters/alice/hscenes/missionary2/part4.webm")
    show alice missionary part 4 with fade
    pause
    "Волны её тугой киски прокатываются по члену, и каждый толчок пробирает меня до мурашек."
    "Она крепко сжимает мои руки, впиваясь ногтями."
    alice.c "М-м-м-м-м! М-м-м-м-м!"
    "[alice.name] с силой сжимает меня, вздрагивая и теряя контроль над голосом."
    "Кажется, она только что кончила. Я тоже уже близко, но не хочу, чтобы это заканчивалось."
    mc.c "Ты так хороша..."
    alice.c "Ах~ Да-а-а~ М-м-м~"
    "Мы снова встречаемся взглядами и не решаемся отвести глаза."
    "В них удовольствие, похоть, желание... Мы связаны так тесно, как никогда раньше."
    "Она снова прищуривается, когда чувствует, как мой член упирается в самую глубину."
    "Я вот-вот кончу, но мы ещё не обсуждали, куда..."
    mc.c "Я сейчас кончу, [alice.name]... Куда...?"
    alice.c "А-а-а~ А-А-А~ А-а-а~~!"
    "Она не отвечает — совсем потерялась в экстазе."
    "Как же хочется кончить ей внутрь, но... сейчас рисковать нельзя..."
    mc.c "Я...!"
    image alice missionary end = Image("images/characters/alice/hscenes/missionary2/end.webp")
    show alice missionary end with fadewhite
    pause
    "Я быстро выхожу и кончаю ей на стройный живот, заливая спермой кожу до груди."
    "[alice.name] вздрагивает и ловит ртом воздух."
    alice.c "*Ха-а* *Ха-а-а*"
    "Она открывает глаза и смотрит на то, что я натворил; мой член блестит от её соков."
    alice.c "*Ха-а* О-ох... Боже..."
    alice.c "Это было... было..."
    mc.c "Это было невероятно... Ты как...?"
    alice.c "Д-да... конечно, [mc.name]... *Ха-а* Мне... очень понравилось..."
    mc.c "Я ведь не спросил тебя насчёт..."
    "Я бросаю взгляд на свои художества."
    alice.c "А-а... Да... Я об этом не подумала..."
    alice.c "Думаю, ты правильно сделал. Спасибо."
    "Мы ещё немного лежим, переводя дыхание. Когда я прихожу в себя, тянусь за салфетками, чтобы вытереть её."
    alice.c "Спасибо, [mc.name]..."
    scene black with fade
    "После того как мы привели себя в порядок, устраиваемся на кровати. Я обнимаю [alice.name], и нас накрывает блаженная истома."
    call playMusic(heartTheme) from _call_playMusic_22
    scene alicepillowtalk with fade
    "[alice.name] переворачивается на живот и слегка приподнимается, положив ладонь мне на грудь."
    "Её лицо озаряет мягкое сияние удовлетворения."
    alice.c "Это было чудесно. А тебе понравилось?"
    mc.c "Ты даже не представляешь, [alice.name]. Это было невероятно."
    "[alice.name] широко улыбается."
    alice.c "Я рада. Немного переживала после прошлого раза, но всё оказалось даже лучше, чем я думала."
    alice.c "Многое из того, что читаешь об этом, всё равно не поймёшь на практике."
    mc.c "Читаешь эротические романы? Не ожидал от тебя такого."
    alice.c "Иногда... попадаются. Есть много книг, написанных специально для женщин."
    "Она немного краснеет. Я легонько сжимаю [alice.name], и она прижимается ближе."
    mc.c "Мне всё понравилось, и я рад, что тебе тоже."
    alice.c "«Понравилось» — слишком слабо сказано, [mc.name]. Я не знала, что могу так себя чувствовать."
    alice.c "Я рада, что разделила это с тобой."
    mc.c "Я тоже, [alice.name]."
    "Я слегка сжимаю её, и она отвечает тем же."
    mc.c "Я бы хотел, чтобы ты осталась на ночь. Если ты, конечно, не против — возможно, ты не планировала оставаться."
    alice.c "Правда? Я тоже этого хочу, но..."
    "Она ненадолго задумывается."
    alice.c "Я могу встать пораньше и переодеться дома. Тогда да, я бы очень хотела остаться. Спасибо."
    scene black with fade
    "Я целую [alice.name], и мы приводим себя в порядок перед сном."
    call aliceSleepover from _call_aliceSleepover
    "[alice.name] засыпает на удивление быстро. Сначала между нами остаётся расстояние, но вскоре она придвигается поближе."
    "Она устраивается у меня под боком, положив изящную ладонь на грудь."
    "Её стройное тело мерно вздымается, а усы изредка подрагивают."
    "Вот оно, настоящее блаженство."

    if(not fromGallery):
        $ alice.addLove(1)
    
    return {'location':location_home}

label aliceHEvent5(fromGallery):
    $ location_cafe.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_23
    "Кофе с [alice.name]. Обычная часть нашей недели."
    "Книги, работа, милые разговоры. Флиртовать у неё, правда, получается так себе."
    "Но в этом и есть часть её очарования."
    show alice smile talk with dissolve
    alice.c "Спасибо за кофе, [mc.name]. Было очень вкусно."
    show alice smile
    mc.c "Всегда пожалуйста."
    show alice smile talk 2
    alice.c "Кажется, мы оба допили. Пойдём?"
    show alice smile
    "После того как мы наконец переспали, я чувствую себя ближе к [alice.name], хотя сама она ничуть не изменилась."
    mc.c "Конечно, пойдём."
    "Мне её всё мало. Не хочется заканчивать на этом сегодняшний день."
    mc.c "Слушай, может, поедешь ко мне? Ты ведь не занята?"
    show alice thinking
    alice.c "М-м..."
    show alice neutral talk
    alice.c "Я бы хотела. Но должна кое-что сказать."
    alice.c "Судя по моему циклу, сейчас у меня повышен риск забеременеть."
    show alice neutral
    "Она произносит это совершенно тем же спокойным голосом. Я вздрагиваю, но, кажется, всё в порядке."
    "Ну и прямолинейно..."
    "И, похоже, она сразу раскусила мои намерения. Обожаю близость с ней."
    show alice neutral talk
    alice.c "И я заметила, что мы не особо любим предохраняться."
    show alice neutral
    "Это моя вина... Я обычно не думаю о таких вещах."
    "Мы занимались сексом, поддавшись страсти, и она тоже ни разу об этом не заговаривала."
    mc.c "А... Ну, прости за это..."
    show alice neutral talk
    alice.c "Не нужно извиняться. Насколько я понимаю, такие средства снижают ощущения у обоих."
    show alice neutral
    "Занятный разговор для общественного места. Хорошо, что поблизости, кажется, никого нет."
    "И снова [alice.name] говорит о сексе так прямо..."
    "Это должно бы убить настроение, но она меня только сильнее заводит."
    mc.c "Ладно, хорошо, что сказала, [alice.name]. Мы ничего не обязаны делать, если ты не хочешь."
    show alice bashful talk
    alice.c "*Кхм* Да, спасибо, [mc.name]."
    show alice bashful
    "Такой взгляд у неё редкость. Она обычно ни о чём не стесняется говорить."
    "Что-то тут не так."
    mc.c "Или... можем заняться чем-нибудь другим? Не..."
    "Попробую выразиться на её языке."
    mc.c "Не проникновение, а... что-нибудь ещё?"
    show alice smile talk
    alice.c "А мы можем?"
    show alice smile
    "Ого, она сразу оживилась. Значит, сама хотела чего-то? Порой забываю, что за её манерой говорить тоже скрываются желания — просто она реже их показывает."
    mc.c "Конечно. Мы уже кое-что пробовали. Я и сам могу придумать пару вещей, которыми хотел бы заняться..."
    show alice smile talk 2
    alice.c "Я... хотела бы."
    show alice smile
    mc.c "Тогда пошли!"
    "Я беру её за руку, и мы выходим."
    scene black with fade
    call playMusic(sexyTheme) from _call_playMusic_24
    "Дорога домой короткая, а напряжение между нами всё нарастает."
    $ location_home.showBackground()
    show alice smile with dissolve
    mc.c "Ты... что-нибудь задумала?"
    show alice thinking
    alice.c "Я кое-что посмотрела..."
    "Конечно посмотрела. Любознательность у неё в крови."
    alice.c "Мне было бы интересно... сделать тебе минет."
    "Чёрт возьми... Куда уж сильнее меня заводить."
    show alice smile talk
    alice.c "Это должно быть приятно нам обоим, но с твоими размерами... не знаю, насколько у меня получится."
    show alice smile
    "Я готов наброситься на неё в любую секунду."
    mc.c "[alice.name]..."
    show alice neutral talk
    alice.c "Да?"
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    alice.c "М-м-м... Хм-м~"
    hide alice with dissolve
    show alice hug with dissolve
    alice.c "[mc.name], ты меня удивил."
    mc.c "Ты просто слишком милая."
    mc.c "Можешь делать что угодно. И просить у меня чего угодно — просто скажи."
    alice.c "В следующий раз я не буду стесняться."
    hide alice with dissolve
    show alice kiss with dissolve
    alice.c "М-муа~"
    "Не могу наглядеться. Она такая милая."
    "Обнявшись, мы направляемся к кровати..."
    image alice makeout part 1 = Movie(play="images/characters/alice/hscenes/cunnilingus/makeout1.webm")
    show alice makeout part 1 with fade
    pause
    alice.c "О-ох~"
    "Мы падаем на кровать, и я притягиваю [alice.name] к себе сверху."
    "[alice.name] целиком помещается у меня на груди, пока мы исследуем рты друг друга."
    "Кажется, это самый страстный поцелуй в нашей жизни."
    alice.c "М-м-м~ Муа~"
    "Я крепко обхватываю её восхитительную задницу и прижимаю к себе."
    "Языки переплетаются как никогда — я на седьмом небе."
    alice.c "Так... Муа~ страстно..."
    mc.c "Мне тебя мало, [alice.name]."
    image alice makeout part 2 = Movie(play="images/characters/alice/hscenes/cunnilingus/makeout2.webm")
    show alice makeout part 2 with fade
    pause
    "В переплетении наших тел я переворачиваю [alice.name] на спину."
    alice.c "Ах~ [mc.name]... Муа~"
    "[alice.name] обнимает меня за спину, а я ласкаю её пышное бедро."
    "Хочу подготовить её к тому, что собираюсь сделать."
    mc.c "Позволь мне начать, [alice.name]."
    alice.c "Пожалуйста. *Муа*"
    mc.c "Давай тебя разденем."
    scene black with fade
    "Мы раздеваем друг друга. [alice.name] остаётся голой, а я устраиваюсь головой между её толстыми бёдрами."
    image alice cunnilingus part 1 = Image("images/characters/alice/hscenes/cunnilingus/part1.webp")
    show alice cunnilingus part 1 with fade
    pause
    mc.c "Готова?"
    alice.c "Это немного неловче, чем я ожидала..."
    mc.c "Не волнуйся, ты прекрасна. Тебе нечего стыдиться. Я буду нежным."
    alice.c "С-спасибо..."
    alice.c "Тогда... пожалуйста..."
    image alice cunnilingus part 2 = Movie(play="images/characters/alice/hscenes/cunnilingus/part2.webm")
    show alice cunnilingus part 2 with fade
    pause
    "Мне не нужно просить дважды. Я начинаю вылизывать её прекрасную тугую пизду."
    "Она уже влажная от предвкушения; её сладкий сок наполняет мой нос и рот ароматом."
    alice.c "О-ох... Ничего себе~"
    alice.c "Ах-а-а~ Это..."
    "Она не может закончить фразу и дрожит, чувствуя, как мой язык скользит по её щёлке."
    "Я прохожусь по каждой складочке, скользя по шерсти вокруг её входа и проникая языком всё глубже."
    alice.c "М-м-м~ [mc.name]~"
    alice.c "Ух ты~"
    image alice cunnilingus part 3 = Movie(play="images/characters/alice/hscenes/cunnilingus/part3.webm")
    show alice cunnilingus part 3 with fade
    pause
    "Я щекочу её клитор, чувствую, как она вздрагивает и пульсирует подо мной."
    "Естественный запах её шерсти смешивается с ароматом возбуждения и её соков."
    "Зная, как ей хорошо, я мог бы заниматься этим целый день."
    "Но я намерен довести её до оргазма."
    image alice cunnilingus part 4 = Movie(play="images/characters/alice/hscenes/cunnilingus/part4.webm")
    show alice cunnilingus part 4 with fade
    pause
    alice.c "[mc.name]~ Ты восхитителен~"
    alice.c "Я... Ах~ Кажется, скоро кончу."
    "Я невнятно выдавливаю «хорошо», но даже не могу оторваться от неё."
    "[alice.c] извивается и сжимает меня бёдрами, наслаждаясь ласками."
    "Заглядывая между её ног, я замечаю её похотливое лицо."
    "Вот это зрелище."
    alice.c "[mc.name]~"
    alice.c "Я... А-а-а~"
    "Она напрягается. Я провожу языком по всей её киске, чтобы довести до оргазма."
    image alice cunnilingus end 1 = Image("images/characters/alice/hscenes/cunnilingus/end1.webp")
    show alice cunnilingus end 1 with fadewhite
    pause
    alice.c "А-а-а-а-а~!"
    "[alice.name] кончает с пронзительным визгом."
    "Она дрожит от удовольствия и сильнее прижимает мою голову к себе."
    "Моё лицо всё залито её соками."
    alice.c "О-ох~ А-а~"
    image alice cunnilingus end 2 = Image("images/characters/alice/hscenes/cunnilingus/end2.webp")
    show alice cunnilingus end 2 with fade
    pause
    "Наконец я отстраняюсь, и [alice.name] расслабляется."
    alice.c "Ничего себе... [mc.name]~ Как тебе это удалось?"
    alice.c "Ощущения были... совсем другими."
    mc.c "Просто у меня волшебные руки."
    alice.c "Я бы... охотно в это поверила."
    mc.c "Оправдал ожидания?"
    alice.c "Даже превзошёл. Это было невероятно."
    mc.c "Всегда к вашим услугам."
    "Ну, я отлично справился. Хорошая работа — сама себе награда, но... мой член тоже каменный и вот-вот порвёт трусы."
    "[alice.name] замечает, куда я смотрю."
    alice.c "Было бы правильно отплатить тебе тем же, верно?"
    "Она редко так ухмыляется. Когда захочет, умеет быть проказницей."
    mc.c "Я был бы только рад. Ты меня уже завела."
    alice.c "Признаюсь, я давно этого хотел."
    image alice blowjob part 1 = Image("images/characters/alice/hscenes/blowjob/part1.webp")
    show alice blowjob part 1 with fade
    pause
    "[alice.name] садится на край кровати. Я спускаю трусы, и мой член покачивается прямо перед её лицом."
    "Она удивлённо смотрит на него, но осторожно обхватывает основание и улыбается мне."
    alice.c "Надеюсь, я всё делаю правильно, хотя не совсем уверена."
    mc.c "Не переживай. Уверен, мне понравится всё, что бы ты ни сделала."
    alice.c "Если я правильно помню, обычно начинают вот так..."
    image alice blowjob part 2 = Movie(play="images/characters/alice/hscenes/blowjob/part2.webm")
    show alice blowjob part 2 with fade
    pause
    "[alice.name] проводит маленьким языком по нижней стороне моего ствола."
    "Её пальцы нежно направляют мой член, а она облизывает его по всей длине."
    mc.c "О-ох, ничего себе... [alice.name]..."
    alice.c "На вкус... как и ты. А вот запах..."
    "Не колеблясь, не испытывая ни дискомфорта, ни отвращения, она ласкает мой член губами и вдыхает его запах."
    alice.c "Как и в прошлый раз, у него любопытный аромат."
    alice.c "Он всегда так пахнет?"
    mc.c "Э-э, не знаю..."
    alice.c "Хм-м~"
    "Она продолжает, прикрыв глаза, словно смакует еду."
    "Так непристойно — совсем не похоже на её обычный образ."
    alice.c "Позволь мне продолжить."
    image alice blowjob part 3 = Movie(play="images/characters/alice/hscenes/blowjob/part3.webm")
    show alice blowjob part 3 with fade
    pause
    "[alice.name] медленно впервые обхватывает губами головку моего члена."
    alice.c "М-м-м~"
    "Её усы подрагивают, а хвост виляет за спиной..."
    "Её губы скользят по нижней стороне головки..."
    "Она прокладывает путь языком, пока я заполняю её рот..."
    mc.c "А-а, [alice.name], как же приятно~"
    image alice blowjob part 4 = Movie(play="images/characters/alice/hscenes/blowjob/part4.webm")
    show alice blowjob part 4 with fade
    pause
    alice.c "Хм-м~"
    "Её тихое мычание, когда она пытается что-то произнести, только усиливает ощущения."
    "Она то и дело поглядывает на меня, словно проверяя, хорошо ли у неё получается."
    "Она мягко покачивает головой в ритм и слегка сжимает мой член, хотя ей трудно взять его глубже."
    "Она опирается рукой на мой таз, удерживая равновесие, и пушистыми пальцами щекочет основание моего члена."
    "И какое зрелище: прекрасная, милая [alice.name] с моим членом во рту, а за ней — упругая грудь и толстые ляжки..."
    mc.c "Невероятно, [alice.name]. Просто охрененно~"
    "Для первого раза у неё получается отлично. И, похоже, ей самой нравится."
    "Когда у меня начинает выделяться смазка, она берётся за дело ещё усерднее."
    image alice blowjob part 5 = Movie(play="images/characters/alice/hscenes/blowjob/part5.webm")
    show alice blowjob part 5 with fade
    pause
    "Она ускоряется, опускается ниже и сосёт напористее."
    "Свободной рукой она нежно дрочит оставшуюся часть моего члена..."
    mc.c "[alice.name], идеально... Не останавливайся..."
    alice.c "М-м-м~"
    "С решительным видом она сосредоточенно поддерживает ровный ритм."
    "Она высосет меня досуха."
    "Её коготки опасно пляшут вокруг моего члена, но я знаю — я в надёжных руках."
    "В очень умелых руках..."
    "Она отплачивает мне сполна. Я скоро кончу."
    mc.c "Ах, я сейчас кончу..."
    mc.c "Можешь отстраниться, если захочешь."
    "Не сбиваясь с ритма, она слегка качает головой, не выпуская мой член изо рта."
    "Она доведёт дело до конца. От этой мысли я кончаю ещё быстрее."
    mc.c "Ах~ Я..."
    image alice blowjob end 1 = Image("images/characters/alice/hscenes/blowjob/end1.webp")
    show alice blowjob end 1 with fadewhite
    pause
    alice.c "М-м!"
    "Я заливаю спермой заднюю стенку горла [alice.name]."
    "Она заметно морщится, но не отстраняется."
    "Оргазм такой сильный, что у меня едва не подкашивается колено."
    "После ещё нескольких сокращений я обмякаю."
    "Я чуть отстраняюсь, позволяя [alice.name] наконец вдохнуть."
    image alice blowjob end 2 = Image("images/characters/alice/hscenes/blowjob/end2.webp")
    show alice blowjob end 2 with fade
    pause
    "...Показывая, сколько я в неё кончил."
    mc.c "Блядь, это было охрененно..."
    alice.c "А-а~ вы-вытереть?"
    mc.c "Да, это было идеально."
    alice.c "Я... рада~"
    "Рот у неё полон, сперма стекает по губам, и она не знает, что делать."
    mc.c "Можешь—"
    "Но стоило мне заговорить, как она вдруг закрывает рот и сглатывает."
    image alice blowjob end 3 = Image("images/characters/alice/hscenes/blowjob/end3.webp")
    show alice blowjob end 3 with fade
    pause
    "Ничего себе..."
    mc.c "Тебе... не обязательно было."
    alice.c "Фух... После прошлого раза я многого ожидала, но когда всё попадает в рот, ощущения совсем другие."
    alice.c "На вкус... не очень, как я и читала. Но и не так уж плохо."
    alice.c "Правда ли, что мужчинам нравится, когда девушка... *кхм* «глотает»?"
    mc.c "Да, очень нравится..."
    "Она улыбается своей фирменной улыбкой, хотя губы испачканы слюной и спермой."
    "Мы ложимся на кровать и наслаждаемся послевкусием."
    scene alicepillowtalk with fade
    call playMusic(chillTheme) from _call_playMusic_25
    mc.c "Это было невероятно."
    alice.c "Мне тоже понравилось. Спасибо, [mc.name]."
    mc.c "Вообще-то это я должен тебя благодарить."
    alice.c "Нет... Ты по-прежнему заботливый, нежный и терпеливый со мной. Я правда это ценю."
    alice.c "Я рада, что могу пережить всё это вместе с тобой."
    scene black with fade
    "[alice.name] кладёт голову мне на грудь и закрывает глаза."
    "Уже поздно."
    mc.c "Останешься на ночь?"
    alice.c "Да, пожалуйста, [mc.name]. Спасибо."
    call aliceSleepover from _call_aliceSleepover_1
    "Мы быстро приводим себя в порядок и готовимся ко сну."
    "Засыпаем спокойно, [alice.name] рядом со мной."

    if(not fromGallery):
        $ alice.addLike(1)
        $ alice.addLove(1)
    
    return {'location':location_home, 'time':'Morning'}

label aliceHEvent6(fromGallery):
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_26
    "У меня в гостях одна милая девушка."
    show alice smile with dissolve
    "Алиса нередко заезжает ко мне после работы или в выходные."
    "Она превратила мою квартиру во второй дом, чему я только рад. Классно, когда она здесь. Прямо как у настоящей пары."
    "Мы перекусили, а я заканчиваю кое-какие дела. Выхожу за напитком и возвращаюсь из кухни."
    image alice tailjob start = Movie(play="images/characters/alice/hscenes/tailjob/start.webm")
    show alice tailjob start with fade
    pause
    "Алиса лежит у меня на кровати и читает. Обычное дело. Даже у меня найдутся какие-нибудь простенькие книжки, которых у неё нет."
    "Проблема только в том... что, совершенно невинно, она создала невероятно соблазнительное зрелище."
    "Наверное, это больше говорит обо мне... Она просто лежит и читает, но в этом есть что-то такое..."
    "А эта восхитительная задница — просто загляденье... Большая, круглая, мягкая... сочная... так и подставилась ко мне."
    "Но взгляд всё время соскальзывает чуть в сторону. На кое-что рядом, что привлекло моё внимание."
    "Её милый хвостик тихонько покачивается из стороны в сторону. Он дёргается и виляет в такт её настроению. Похоже, у большинства антропоморфных зверей это сохранилось."
    "Пару раз я уже осторожно трогал его, но он, кажется, очень чувствительный: она обычно отдёргивает хвост, если я не предельно нежен."
    "Такой мягкий, нежный. Шёрстка на нём особенно шелковистая, а сам хвост кажется таким экзотичным. Милый. Он..."
    "..."
    "Господи, прости, но мне в голову пришла безумная идея..."
    mc.c "Алиса?"
    alice.c "Да, [mc.name]?"
    mc.c "Возможно, вопрос совершенно глупый... Но..."
    mc.c "У тебя в хвосте есть кости, да? Там не одни мышцы?"
    alice.c "Удивительно, что ты спрашиваешь, [mc.name]. Я думала, ты знаешь. В кошачьем хвосте около двадцати маленьких позвонков."
    alice.c "В конце концов, это продолжение позвоночника. Почему спрашиваешь?"
    mc.c "И... ты полностью им управляешь? Он не просто болтается сам по себе? А ведь иногда виляет."
    alice.c "Конечно, управляю, как и любой другой частью тела. Правда, многие его движения происходят бессознательно — я не всегда делаю это специально."
    alice.c "Для антропоморфных животных хвост почти бесполезен. Для равновесия он уже мало помогает, раз мы ходим на двух ногах."
    "..."
    mc.c "То есть ты можешь им что-нибудь удержать?"
    alice.c "Если оно не слишком тяжёлое, наверное, смогу поднять."
    mc.c "Не совсем поднять. Скорее... обхватить?"
    alice.c "...Не вижу причин, почему нет."
    call stopMusic from _call_stopMusic_2
    "То есть она может... О боже. Я уже завожусь от одной мысли. Я что, извращенец?"
    alice.c "А что именно тебя интересует?"
    "С Алисой не получится ходить вокруг да около. Лучше просто сказать, что думаю."
    "Но чёрт, а вдруг она разозлится? Может, я перегибаю. Но если бы она согласилась..."
    mc.c "Я просто подумал... Может, ты не будешь против... Если я..."
    mc.c "Может, ты {i}поласкаешь{/i} меня хвостом?"
    alice.c "Как именно?"
    "Провал. Трудно просто взять и сказать прямо."
    mc.c "Ну, как рукой... чтобы... довести меня до оргазма?"
    "Я это сказал..."
    alice.c "А, ты хочешь, чтобы я стимулировала твой пенис хвостом?"
    "Когда она так формулирует, это звучит безумно..."
    alice.c "Не вижу причин, почему нет. Ты бы этого хотел, [mc.name]?"
    "Она... вроде не против? Чёрт возьми, неужели она правда согласится?"
    mc.c "Если... только если ты сама хочешь..."
    alice.c "Если будешь нежен, я не против. Он довольно чувствительный."
    mc.c "Ты правда согласна?! Да! Пожалуйста!"
    alice.c "Т-тебя это настолько заводит?"
    mc.c "Ещё как! Мне нравится твой хвост! Уверен, ощущения будут потрясающие."
    alice.c "Мне такое даже в голову не приходило... Я не знала, что это распространённая сексуальная практика."
    mc.c "Наверное, не особо. Если ты не хочешь—"
    alice.c "Как ты хочешь это сделать?"
    "Она будто перебила меня на полуслове."
    mc.c "Просто оставайся так..."
    call playMusic(sexyTheme) from _call_playMusic_27
    scene alicetailjobstart with fade
    "Я стягиваю штаны и устраиваюсь верхом на её заднице, пока она лежит на животе. Она любопытно оглядывается через плечо, а я показываю ей член."
    alice.c "...Быстро ты, [mc.name]. Почему уже стояк?"
    mc.c "Честно? Я завёлся, просто подумав об этом..."
    alice.c "Понимаю... Тебе это и правда настолько нравится?"
    mc.c "Ещё бы! Я обожаю тебя всю, даже твой хвост."
    alice.c "Ну... Я не против. Давай попробуем."
    image alice tailjob part 1 = Movie(play="images/characters/alice/hscenes/tailjob/part1.webm")
    show alice tailjob part 1 with fade
    pause
    "Она осторожно тянется ко мне хвостом и медленно обвивает им мой член."
    "Мягкая, шелковистая шерсть обхватывает меня — ощущение совершенно необычное. Я вздрагиваю даже от одного прикосновения."
    mc.c "Ого, ничего себе~"
    "Она обвивает мой член ещё несколькими витками, очень свободно сжимая его и двигая хвостом вверх-вниз."
    alice.c "Так... хорошо?"
    mc.c "Просто... продолжай... Потрясающе."
    alice.c "Понятно..."
    "Она сжимает недостаточно сильно, чтобы по-настоящему меня завести, но необычные ощущения с лихвой это компенсируют."
    "Не должно быть так приятно, но это почти невозможно описать... Когда ещё испытаешь такое?"
    alice.c "Отсюда мне трудно как следует сжать. Давай я повернусь."
    image alice tailjob part 2 = Movie(play="images/characters/alice/hscenes/tailjob/part2.webm")
    show alice tailjob part 2 with fade
    pause
    "Алиса переворачивается на бок и обвивает меня ещё большей частью своего шелковистого хвоста."
    "Я чувствую, как хватка крепнет: она обхватывает мой член и водит хвостом вверх-вниз."
    mc.c "Ох, Алиса... Потрясающе."
    alice.c "Смазки, конечно, нет. Ничего?"
    mc.c "Даже лучше, чем ничего..."
    alice.c "...Странно..."
    "Она выглядит озадаченной, но я замечаю слабую улыбку, когда она смотрит на свою работу."
    "Ситуация и правда уникальная. Думаю, ей тоже по-своему нравится."
    alice.c "Ты кончишь от этого? Тебе достаточно приятно?"
    mc.c "Определённо... Скоро кончу~"
    alice.c "Если собираешься, дай мне хотя бы снять верх."
    "Она разрешает кончить ей на грудь?"
    mc.c "А-а, конечно..."
    image alice tailjob part 3 = Movie(play="images/characters/alice/hscenes/tailjob/part3.webm")
    show alice tailjob part 3 with fade
    pause
    "Почти не прерываясь, Алиса снимает верх и позволяет мне устроиться перед ней."
    "Алиса обнажает маленькую грудь и подставляет её мне."
    "Она сжимает мой член, насколько может, и двигает хвостом вверх-вниз."
    alice.c "Ты весь дрожишь..."
    mc.c "Так приятно. И одновременно щекотно. Продолжай, пожалуйста."
    "Каждое движение её хвоста... Шелковистая шерсть касается головки... Это невероятно."
    "И эта красотка прямо передо мной. Я уже почти..."
    mc.c "Алиса, я сейчас кончу!"
    alice.c "Поняла. Только постарайся не попасть на простыни..."
    scene alicetailjobend1 with fadewhite
    pause
    "Я содрогаюсь и кончаю, пока Алиса щекочет хвостом головку моего члена."
    "Несмотря на предупреждение, Алиса слегка удивляется тому, что видит."
    scene alicetailjobend2 with fade
    pause
    "Я заливаю ей всю грудь. Огромные капли спермы стекают по милым сисечкам."
    "Она понемногу ослабляет хватку, продолжая дразнить мой член хвостом, пока я блаженно вздрагиваю."
    alice.c "Похоже, тебе понравилось. Всё было так, как ты ожидал?"
    mc.c "Невероятно... Правда..."
    alice.c "Рада, что тебе понравилось. Немного странно, но мне не мешает. Для меня это интересный опыт."
    alice.c "А что именно сделало это таким приятным? Лучше или хуже секса?"
    mc.c "Даже не знаю, как это описать..."
    alice.c "Хм-м~"
    "Из головки моего члена сочатся капли спермы. Алиса всё ещё держит меня хвостом и подставляет его кончик, чтобы собрать их."
    "Она с любопытством разглядывает меня, а потом улыбается."
    "Она делает вид, что всё это её нисколько не тронуло, но я замечаю в ней лёгкое удовлетворение."
    mc.c "Давай я тебя вытру."
    alice.c "Спасибо."
    scene black with fade
    "Я вытираю нас, а Алиса после короткого душа снова одевается."
    $ location_home.showBackground()
    show alice neutral talk with dissolve
    alice.c "Если ты удовлетворён, я тогда продолжу читать."
    show alice neutral
    mc.c "Не хочешь, чтобы я отплатил тебе тем же?"
    show alice smile talk
    alice.c "Не нужно, [mc.name], правда. Я ценю твою заботу обо мне, но сегодня мне и так хорошо."
    show alice smile
    mc.c "Если ты уверена... Спасибо, что согласилась на мою... странную просьбу."
    show alice smile talk 2
    alice.c "Каким бы странным это ни было, мне нравится исследовать всё это вместе с тобой, [mc.name]."
    show alice smile
    "Эта девушка... Я никогда не хочу её отпускать."
    mc.c "Что ты вообще читаешь?"
    show alice smile talk 2
    alice.c "Автобиографию спортивного атлета, она стояла у тебя на полке."
    show alice smile
    mc.c "Тебе такое интересно?"
    show alice neutral talk
    alice.c "Совсем нет. Просто в твоей коллекции больше ничего не привлекло моего внимания."
    show alice neutral
    mc.c "А..."
    show alice tailjob start with fade
    pause
    "Удивительно, но она продолжает читать с того места, где остановилась, будто ничего особенного не произошло."
    "А я немного смущён своей просьбой, но на седьмом небе от счастья, что она не была против."
    "Мы отлично проводим время вместе."

    if(not fromGallery):
        $ alice.addLove(1)
    
    return

label aliceLikeEvent4(fromGallery):
    $ location_town.showBackground()
    call playMusic(chillTheme) from _call_playMusic_28
    "Я договорился забрать Алису с работы, а потом мы собирались выпить кофе."
    "В библиотеке неудобно шуметь и болтать, поэтому обычно я жду снаружи. Но сегодня пришёл пораньше."
    "Было бы здорово зайти и увидеть её за работой. Может, она обрадуется сюрпризу. Вдруг даже смогу помочь."
    "Загляну. Если буду мешать, просто посмотрю книги."
    scene library with fade
    "Я сразу смотрю в сторону стойки регистрации, но Алисы там нет."
    "Да и вообще никого. Ничего необычного — может, сотрудник отошёл в подсобку. Алиса, наверное, раскладывает книги."
    "Я уже собираюсь пройтись и поискать её, как из-за угла выбегают два маленьких зверёныша."
    call playMusic(funnyTheme) from _call_playMusic_29
    unknown "Хи-хи-хи!"
    unknown2 "А-ха-ха!"
    "Два маленьких козлёнка носятся по библиотеке, шумят и натыкаются на всё подряд."
    "Один из них волочит большую книгу, явно не по возрасту."
    "Вот тебе и «публичная» библиотека."
    "Но за ними..."
    show alice bashful talk with dissolve
    alice.c "Э-э, простите... Пожалуйста..."
    alice.c "Д-дети, так нельзя. Нужно вести себя тихо..."
    show alice bashful
    "Похоже, Алиса пытается утихомирить эту парочку и убрать за ними беспорядок."
    "Но дети совершенно не обращают на неё внимания. Они продолжают носиться кругами, заглушая её тихие просьбы."
    unknown "Уиии! Уиии!"
    "Ребёнок держит книгу над головой и кружится, будто играет с самолётиком."
    "Алисе нужна помощь."
    mc.c "Алиса?"
    show alice surprise
    alice.c "О, [mc.name]!"
    alice.c "Не думала, что ты уже придёшь."
    mc.c "Да ничего, я просто пораньше зашёл. Что тут происходит?"
    show alice bashful talk
    alice.c "Э-э... Я была за стойкой, а эти дети начали бегать без присмотра."
    alice.c "Они сильно шумят, меня не слушаются и уже успели устроить беспорядок."
    show alice bashful
    mc.c "Они пришли с родителями?"
    show alice sad talk
    alice.c "Не знаю, не помню, чтобы видела их входящими. Но если они не подходили к стойке, я могла не заметить."
    show alice sad
    "Дети задевают тележку с книгами, и несколько падают на пол."
    show alice mad talk
    alice.c "Ах! Дети! П-прекратите!"
    show alice mad
    "Для Алисы это, пожалуй, самая решительная попытка когда-либо, но даже я едва слышу её отсюда. Дети тем более не слушают."
    "Посмотрим, чем я могу помочь. Замечаю на полке кое-что подходящее, беру книгу и подхожу к детям."
    mc.c "Эй, малой, тебе нравятся самолёты?"
    unknown "Ну-у, типа того..."
    unknown2 "Ты кто? А где твоя шерсть?"
    unknown "Эй, глупыш, это же человек! Ты его по телеку не видел?"
    show alice neutral
    unknown "О-о... Ты как из телевизора?"
    mc.c "Я человек, ребята. И нет, я не из телевизора — таких, как я, много. А теперь гляньте сюда."
    "Я показываю им найденную книгу — иллюстрированную историю авиации, военной и не только. Картинок там полно."
    "Похоже, они как раз в том возрасте, когда такие штуки кажутся крутыми. И правильно, они до сих пор крутые."
    unknown "Ух ты!"
    unknown2 "А у того пушки!"
    "Дети успокаиваются, садятся на пол и начинают листать страницы."
    mc.c "Смотрите на этот самолёт: у него крылья складываются и раскрываются. Видите?"
    unknown "Круто..."
    "Я оглядываюсь на Алису. Похоже, она немного выдохнула, когда всё ненадолго затихло, пусть беспорядок и остался."
    mc.c "Попробуй найти их родителей, Алиса."
    show alice surprise
    alice.c "А-а, да. Сейчас."
    hide alice with dissolve
    "Алиса убегает в соседние комнаты. Пока что дети заняты. Надеюсь, она скоро кого-нибудь найдёт."
    scene black with fade
    "Я сажусь рядом с детьми и пытаюсь удержать их на месте. Это оказалось нетрудно — я сам увлёкся картинками."
    "К счастью, через несколько минут..."
    scene library with fade
    show alice neutral talk
    alice.c "Кхм, это ваши дети, мадам?"
    show alice neutral
    unknown "Мамочка, смотри!"
    "Один из мальчиков поднимает книгу. Похоже, Алиса нашла их маму."
    show alice at twoPersonLeft with ease
    show woman at twoPersonRight with dissolve
    unknown3 "Простите за неудобства. Я всего на пару минут отлучилась в туалет и оставила их в соседней комнате..."
    unknown3 "Простите за неудобства. Я всего на пару минут отлучилась в туалет и оставила их в соседней комнате..."
    show alice bashful talk
    alice.c "А, ну, понимаю. Ничего... страшного..."
    show alice bashful
    unknown3 "Мальчики, мы уходим. Вам придётся хорошенько подумать о своём поведении."
    "Оба" "*Стон*"
    "Женщина хватает детей за руки и тащит их к выходу."
    unknown2 "Пока, дядя."
    mc.c "Давайте, бывайте."
    hide woman with dissolve
    show alice at center with ease
    call playMusic(chillTheme) from _call_playMusic_30
    "Бедная Алиса, наверное, совсем растерялась. Присматривать за детьми — явно не часть её работы."
    mc.c "Всё нормально, Алиса?"
    show alice bashful talk
    alice.c "Да, пожалуй..."
    show alice neutral talk
    alice.c "Спасибо, [mc.name]. Не знаю, что бы я без тебя делала."
    show alice neutral
    mc.c "Не за что. Ты бы одна ничего не смогла сделать. А где остальные сотрудники?"
    show alice neutral talk
    alice.c "Коллега скоро должен прийти."
    show alice neutral
    "Я оглядываю небольшой беспорядок. Ничего не сломано, но тихая и аккуратная библиотека теперь выглядит иначе."
    mc.c "Помочь прибраться?"
    show alice smile talk
    alice.c "Хм, да, пожалуйста. Спасибо, [mc.name]."
    scene black with fade
    "Мы некоторое время наводим порядок, собирая с пола разбросанные вещи и книги."
    "Вскоре приходит коллега Алисы и принимает смену."
    $ location_cafe.showBackground()
    call playMusic(heartTheme) from _call_playMusic_31
    show alice smile with dissolve
    "Мы, как и планировали, идём в кафе. Через некоторое время Алиса успокаивается после случившегося."
    show alice smile talk
    alice.c "Ещё раз спасибо, [mc.name]. У тебя здорово получилось их успокоить. Как ты это сделал?"
    show alice smile
    mc.c "Подумал, что надо найти к ним подход и увлечь чем-нибудь интересным."
    show alice smile talk 2
    alice.c "Ты со всеми детьми так хорошо ладишь?"
    show alice smile
    mc.c "Не сказал бы. Просто стараюсь отвлечь их, вот и всё."
    mc.c "Я ведь тоже когда-то был маленьким. А ещё легко, когда сам не слишком-то повзрослел, ха-ха."
    show alice neutral talk
    alice.c "Ты выглядел так уверенно, будто это само собой получается."
    show alice bashful talk
    alice.c "Я и не знала, что делать. С детьми я никогда не умела ладить."
    show alice neutral talk
    alice.c "Они шумные, неаккуратные, неуклюжие, нелогичные... Я не понимаю, как с ними лучше обращаться."
    show alice neutral
    mc.c "Не думаю, что кто-то знает. Наверное, единого ответа нет, если он вообще существует. К тому же никто не рождается готовым родителем."
    "Алиса на секунду задумывается. Я только что произнёс слово «родитель». Интересно, что она об этом думает..."
    show alice bashful talk
    alice.c "Когда я нашла их маму, они её послушались. Она была спокойной, но строгой и сразу взяла их под контроль."
    alice.c "Мне не хватает твёрдости. Я так не умею."
    show alice smile talk 2
    alice.c "А ты в такой ситуации держался уверенно. Мне кажется, ты был бы хорошим отцом."
    show alice smile
    "Вот оно. Разговор о будущем — о том, могли бы мы стать родителями. Вместе завести детей?"
    "Не рано ли об этом говорить? Может, Алиса и не задумывалась так глубоко, но после её слов о хорошем отце я уже не могу перестать думать."
    "Хочу ли я детей от Алисы? И главное — хочет ли их она? Похоже, она сомневается в себе."
    "С Алисой лучше спросить прямо."
    mc.c "А ты хотела бы когда-нибудь собственных детей, Алиса?"
    show alice neutral
    alice.c "..."
    show alice neutral talk
    alice.c "Не знаю... Как я уже говорила, не уверена, что у меня хорошо получится..."
    show alice neutral
    mc.c "Думаю, с родительством всё приходит со временем. Единственно правильного способа нет, и у тебя ещё полно времени научиться."
    show alice sad
    alice.c "..."
    "Она молча сидит и думает. Может, раньше она всерьёз об этом не задумывалась."
    show alice neutral talk
    alice.c "Думаю... Может быть, когда-нибудь. Родители раньше тоже об этом говорили."
    show alice neutral
    mc.c "Даже после сегодняшнего хаоса?"
    show alice smile talk 2
    alice.c "Хм-хм~ Увидев, как ты с ними справился, я подумала, что это, наверное, не так уж сложно. А когда они успокоились, оказались милыми."
    show alice smile
    show alice neutral talk
    alice.c "До недавнего времени я почти об этом не думала. Ведь раньше у меня никогда не было отношений."
    show alice neutral
    "Как я с ними справился... Она стала думать об этом недавно... Неужели представляет детей... со мной?"
    "Наверное, я додумываю лишнее. Сейчас не время об этом говорить. Ещё слишком рано."
    show alice neutral talk
    alice.c "Я всё ещё молода и не чувствую, что должна торопиться."
    show alice neutral
    mc.c "Наверное, это правильный настрой."
    "Дети от Алисы..."
    "Когда-нибудь... Что бы я делал?"
    scene black with fade
    "Мы переходим к другим темам и заканчиваем нашу прогулку."
    "Но мысли о детях не выходят у меня из головы. Есть о чём подумать..."

    if(not fromGallery):
        $ alice.addLove(1)
    
    return

label aliceLikeEvent5Invitation(fromGallery):
    call playMusic(heartTheme) from _call_playMusic_32
    show alice neutral
    "Я люблю Алису."
    "Она открылась мне в романтическом плане. Почти ничего не зная об отношениях, она вместе со мной осваивает совершенно новый для себя мир."
    "Мы видимся почти каждый день, ходим на свидания, иногда она остаётся у меня. Мы даже чудесно съездили вместе в отпуск."
    "Я признался ей в любви, и она ответила взаимностью. Сама она говорит это нечасто, но отвечает мне. Я не обижаюсь — просто такая она."
    "Мы даже неловко поговорили о детях... Не углублялись в тему, но это важный шаг."
    "Если оба свободны, мы куда-нибудь выбираемся или ленимся у меня дома, но к ней почти не ходим."
    "Конечно, я бывал у неё. Она пригласила меня к себе почти сразу после знакомства — для того самого «исследования» людей. Я с самого начала понял, что она необычная."
    "Забавное было время... Кто бы мог подумать, что мы окажемся вместе? Кажется, я влюбился в неё уже тогда."
    "Но есть причина, по которой мы редко бываем у неё. Во-первых, она ценит тишину и личное пространство."
    "Во-вторых, у неё очень мало места. Маленькая квартира: гостиная с кроватью, крошечная кухня, ванная — и всё."
    "Она скромно живёт на зарплату за работу на полставки в библиотеке небольшого городка."
    "Она никогда не жаловалась на деньги и не говорила, что ей чего-то не хватает. Она благоразумная, ей хватает на комфортную жизнь, да и работу свою она любит."
    "Я в этом не сомневаюсь. Она умная и способная, могла бы найти более прибыльную работу, если бы захотела, но её и так всё устраивает."
    "Кажется, между нами остался последний шаг. Я люблю её и хочу, чтобы она была рядом."
    "Хочу, чтобы она считала мой дом своим. Чтобы возвращалась сюда вечером и просыпалась здесь в выходные."
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Да!' if(homeHasRoom) else "Сначала нужно расширить дом" 
    if(not fromGallery):
        menu:
            "Предложить Алисе переехать ко мне? Это решение можно принять в любой момент."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "Пока нет":
                call endCharacterInteraction(alice) from _call_endCharacterInteraction
    "Я немного волнуюсь, когда думаю, как спросить. Но это же Алиса — что может пойти не так? Она скажет всё прямо, я уверен."
    "Она может просто отказать. Знаю, как она дорожит личным пространством. Нужно быть готовым принять её ответ."
    mc.c "Алиса, останешься у меня сегодня?"
    show alice smile talk 2
    alice.c "Хм... Я бы осталась, если ты не против. Завтра у меня дневная смена, так что по дороге утром я смогу забрать рабочие вещи. Сегодня за ними ехать не нужно."
    show alice smile
    mc.c "Отлично! Но можешь оставить вещи у меня. Часть твоей одежды уже здесь."
    show alice neutral talk
    alice.c "Рабочие вещи? Не думаю, что это разумно. Мне нужно знать, где они лежат, если я поеду из дома на работу."
    show alice neutral
    "Она уже стала легче относиться к тому, где остаётся ночевать. Обычно она любит придерживаться привычного распорядка..."
    mc.c "Тогда оставайся у меня каждую ночь! Я был бы только рад."
    show alice thinking
    alice.c "Это было бы глупо, да? Мне пришлось бы хранить у тебя ещё больше вещей, и они бы мешались. А ещё дома останется моя еда..."
    "Ладно, я слишком осторожничаю. С ней лучше говорить прямо."
    mc.c "Ладно, Алиса, я хотел сказать... Ты переедешь ко мне?"
    show alice neutral talk
    alice.c "Переехать?"
    show alice neutral
    mc.c "Жить вместе. По-настоящему. Остаться у меня и считать этот дом своим."
    show alice thinking
    alice.c "А, понимаю... Это ведь логичный следующий шаг в наших отношениях, правда?"
    "Как романтично..."
    show alice neutral talk
    alice.c "Я понимала, что однажды мы к этому придём, но не знала, сколько времени обычно должно пройти."
    show alice neutral
    "Ну, я застал её врасплох... Неудивительно, если она не была готова к такому вопросу."
    mc.c "А, прости, всё нормально, если ты—{w=1.0}{nw}"
    show alice smile talk 2
    alice.c "Да, я хочу, [mc.name]. Спасибо."
    show alice smile
    "...А? Погоди, она вот так просто согласилась?"
    mc.c "Ты... серьёзно? Ты правда хочешь?"
    show alice smile talk 2
    alice.c "Да."
    show alice smile
    "Вот это было быстро. Наверное, стоило ожидать."
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Чтобы сразу прояснить: ты знаешь, что [len(girlsAlreadyMovedIn)] других девушек уже почти переехали ко мне, но, возможно, ты ещё не со всеми познакомилась..."
        if(sarah.movedIn and sarahAliceDuoStoryEvent1.unlocked):
            mc.c "Ну, Сару ты уже знаешь."
            show alice smile talk 2
            alice.c "Да. Она рассказывала мне о жизни у тебя. Она хорошая подруга, будет приятно видеться чаще."
            show alice smile
        mc.c "Тебя это... не смущает?"
        show alice smile talk 2
        alice.c "Я всё понимаю, [mc.name]. Я уже учла это, когда отвечала."
        show alice smile
    "От радости, услышав её уверенное «да», я крепко обнимаю Алису."
    hide alice with dissolve
    show alice hug with dissolve
    alice.c "О-ох, [mc.name]~"
    mc.c "Боже, Алиса, спасибо! Я так счастлив."
    alice.c "Это я должна благодарить тебя, [mc.name]."
    alice.c "Думаю, так будет разумнее. Мы сможем вместе оплачивать счета и делить домашние заботы. Готовить и есть вместе тоже выгоднее."
    mc.c "Лучше и не скажешь."
    show alice kiss with dissolve
    "Я крепко целую её в милые губы."
    alice.c "М-м~"
    show alice hug with dissolve
    alice.c "[mc.name], ты радуешься сильнее меня. Это ты проявляешь доброту, предлагая мне свой дом, помнишь?"
    mc.c "Я просто хочу чаще тебя видеть... Это всё, чего мне хотелось."
    alice.c "Понимаю... Буду с нетерпением ждать."
    alice.c "Я тоже хочу стать частью твоего дома."
    "Она невыносима... даже не стараясь..."
    show alice kiss with dissolve
    alice.c "М-м~"
    hide alice with dissolve
    show alice smile with dissolve
    "Мы понемногу размыкаем объятия, но я беру её за руки и смотрю в улыбающееся лицо."
    "Всё решилось на удивление быстро и спокойно. Я ожидал хотя бы небольшого сопротивления — для неё это серьёзные перемены."
    "До сих пор она жила тихой, размеренной жизнью. Даже моё появление порой было для неё непривычным. И она уже так рада переезду?"
    "Наша жизнь вместе... Будет прекрасной."
    show alice smile talk 2
    alice.c "Когда мне переезжать, [mc.name]? Через несколько дней у меня выходной. Если дашь немного времени собрать вещи..."
    show alice smile
    "Точно, надо всё организовать."
    mc.c "Не обязательно перевозить всё сразу. Я помогу тебе со всем остальным постепенно, а сначала возьмём самое нужное."
    mc.c "Я приеду и помогу. В первый раз перевезём столько вещей, сколько тебе удобно."
    show alice thinking
    alice.c "Понимаю. Хм... Будет больше одежды, рабочие материалы, и, конечно, книги..."
    mc.c "А... Только не все книги сразу, Алиса. Кажется, у меня пока нет места для всей твоей коллекции."
    show alice neutral talk
    alice.c "Ничего страшного, тогда перевезём и часть моих книжных полок."
    show alice neutral
    mc.c "Конечно..."
    scene black with fade
    "Мы ещё немного обсуждаем детали."
    "Договариваемся о дне, когда я приеду помочь ей с машиной и перевезти часть вещей."
    "И тогда... Мой дом станет и её домом."
    "Договорились. Загляни в расписание!"

    return

label aliceLikeEvent5(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_33
    $ location_home_bedroom.showBackground()
    "Будильник не нужен — я проснулся ни свет ни заря."
    "Я весь на взводе от радости: сегодня Алиса переезжает ко мне."
    "У неё выходной. Она и так рано встаёт, но попросила помочь ей сегодня с утра."
    "Мы потратим остаток дня на сборы, не спеша перевезём её вещи и поможем освоиться."
    "Весь день будет нашим. И теперь она будет дома... Со мной."
    "Пора ехать. Напишу ей, что уже выезжаю."
    "..."
    "Она отвечает мгновенно."
    alice.c "Привет. Я очень волнуюсь и жду тебя."
    "Милашка. В её духе."
    scene black with fade
    "Доезжаю за несколько минут. Мы взяли машину, хотя я не представляю, сколько вещей окажется."
    scene aliceshome with fade
    "Я вхожу и словно возвращаюсь в прошлое."
    "Наша забавная первая встреча... Именно здесь мы и стали парой."
    "С тех пор я бывал у неё нечасто — обычно она охотнее приезжала ко мне."
    show alice smile with dissolve
    "Алиса аккуратно сидит на кровати. На полу — чемодан и несколько тщательно собранных сумок и коробок."
    "Комната всё ещё обставлена, мы берём только самое необходимое. Думаю, остальное перевезём постепенно."
    show alice smile talk 2
    alice.c "Доброе утро, [mc.name]."
    show alice smile
    mc.c "Доброе утро! Как идут сборы?"
    show alice smile talk 2
    alice.c "Я всё рассортировала и упаковала. Осталось только перевезти вещи."
    show alice smile
    mc.c "Уже? Я думал, сегодня утром буду помогать тебе собираться."
    show alice thinking
    alice.c "Вчера вечером я всё подготовила, чтобы точно взять нужные вещи."
    show alice neutral talk
    alice.c "Так лучше, чем в спешке собираться утром."
    show alice neutral
    mc.c "Ну, ладно. Мне же проще, ха-ха."
    mc.c "Ты готова?"
    show alice smile talk
    alice.c "Да."
    show alice smile
    "Я наклоняюсь, чтобы поднять одну из больших коробок, но едва отрываю её от пола — и застываю. Чёрт, что там такое..."
    mc.c "Ничего себе... Что ты туда положила?"
    show alice neutral talk
    alice.c "Там часть моих учебников."
    show alice neutral
    mc.c "Я же просил не брать слишком много книг за один раз..."
    show alice smile talk
    alice.c "Но это те книги, к которым я постоянно обращаюсь. Они мне понадобятся."
    show alice smile
    "Ну конечно..."
    mc.c "Ладно."
    scene black with fade
    "Мы быстро загружаем её вещи в машину и отправляемся домой."
    scene alicelikeevent5i1 with fade
    pause
    "Стоит нам войти, как я понимаю: никаких торжественных речей или сентиментальных переживаний о переезде не будет."
    "Она сразу принимается искать место для всех своих вещей."
    "В первую очередь — книжные полки. Я заранее освободил для них место."
    mc.c "Алиса, не обязательно делать всё прямо сейчас. У нас впереди {i}целая{/i} вечность..."
    alice.c "Я всё равно об этом думаю, а весь день свободна. Почему бы не заняться этим сейчас?"
    mc.c "Ладно. Помочь?"
    alice.c "Да, пожалуйста. Поможешь поднять коробку?"
    scene alicelikeevent5i2 with fade
    pause
    "Мы неспешно разбираем её вещи. {i}Все{/i} до одной."
    "Раскладываем их аккуратно и по порядку. Правда, с учётом остальных вещей дома придётся пойти на компромиссы."
    "Приятный момент — смотреть, как её вещи покидают коробки и занимают место в моём доме."
    "Её книги, мелочи, безделушки и рабочие материалы. Я даже заметил, как в ящик отправилась пара трусиков..."
    "В комнатах быстро появляется частичка Алисы."
    "И вот теперь я по-настоящему понимаю: она здесь, со мной."
    call playMusic(heartTheme) from _call_playMusic_34
    scene alicelikeevent5i3 with fade
    pause
    mc.c "Фух~ Это всё?"
    alice.c "Да, всё разобрала. Осталось сложить последнюю коробку и найти место для рюкзака."
    mc.c "Алиса, отдохни. Это подождёт. Пора освоиться, расслабься."
    alice.c "Наверное, остальное можно сделать потом."
    scene alicelikeevent5i4 with fade
    pause
    "Я беру её за руки. Она поднимает на меня взгляд."
    mc.c "Алиса... Добро пожаловать домой."
    alice.c "Спасибо, что принял меня."
    "Её мягкие подушечки лап нежно касаются моих ладоней."
    mc.c "Я так рад, что ты согласилась переехать."
    mc.c "Ты счастлива?"
    alice.c "Очень, [mc.name]."
    "По её словам и эмоциям этого не понять, но я чувствую... Она хочет быть здесь. Ей уютно."
    "Её милое личико, изогнутые губы складываются в нежную улыбку..."
    "Я не могу удержаться."
    scene alicelikeevent5i5 with fade
    pause
    alice.c "О-ох! [mc.name]!"
    alice.c "Что ты...?"
    mc.c "Я люблю тебя. Очень сильно."
    mc.c "Не могу дождаться, когда мы начнём новую жизнь вместе."
    alice.c "Ах... Да, я тоже люблю тебя, [mc.name]. Пожалуйста, позаботься обо мне."
    scene alicelikeevent5i6 with fade
    pause
    "Я притягиваю её лицо к своему и нежно целую."
    "Её усы подрагивают, когда наши носы соприкасаются. Чувствую, как хвост мягко покачивается из стороны в сторону."
    "Она тихо мурлычет у меня в объятиях, пока мы целуемся."
    "Я осторожно веду её к кровати, падаю на спину и прижимаю Алису к груди."
    scene alicelikeevent5i7 with fade
    pause
    alice.c "Ох... [mc.name]."
    mc.c "Так, постановляю: первым делом в новом доме ты должна обниматься со мной."
    alice.c "Хм-хм~ Сегодня ты особенно ласковый, [mc.name]."
    mc.c "Теперь ты живёшь здесь, так что привыкай, Алиса."
    alice.c "Я знала, на что подписываюсь. Наверное, я не против~"
    "Я крепко обнимаю её и прижимаю к себе, пока мы лежим вместе."
    scene black with fade
    "Но она не может забыть про последние дела и вскоре вскакивает с кровати, чтобы убрать коробки."
    "Алиса, никогда не меняйся..."

    if(not fromGallery):
        $ alice.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label aliceHEvent7(fromGallery):
    $ location_home_lounge.showBackground()
    "Сегодня у меня ленивый день... Пора плюхнуться на диван и расслабиться."
    "Немного закусок, телевизор и плевать на все обязанности. Вот что значит быть по-настоящему взрослым."
    "Но я не один, у меня есть компания..."
    scene alicehevent7i1 with fade
    pause
    "В какой-то момент ко мне присоединилась Алиса."
    "У неё появилось свободное время, она заглянула узнать, чем я занят, и решила остаться."
    "Весьма любопытно устроилась..."
    mc.c "Ну как ты там, Алиса?"
    alice.c "Вполне удобно."
    "Сначала она просто села рядом на диван, потом прислонилась ко мне плечом и продолжила... сползать."
    "Пока не растеклась у меня на коленях. Вот прямо как..."
    "Я не жалуюсь. Приятно чувствовать, как её мягкое, податливое тело прижимается ко мне, согревая меня."
    "Но выглядит это забавно."
    "Я слегка глажу её по спине и чувствую, как под ладонью тихо урчит мурлыканье."
    alice.c "М-м~"
    "Для неё это полная потеря самообладания. Забавно, насколько легко она поддаётся таким ласкам."
    "Не будь я с ней знаком, решил бы, что она сильнее всех поддаётся звериным инстинктам... хотя сама это отрицает."
    "Она лежит и тихонько мурлычет, пока мы вместе смотрим телевизор."
    "Наверное, это лучше всего показывает, как она освоилась в новом доме."
    "Она устроилась с комфортом, словно это её личное место отдыха. Освоилась быстрее, чем я ожидал, и меня это согревает."
    "Ей комфортно со всем новым. И со мной тоже."
    "Я провожу пальцами вдоль её позвоночника, и она слегка вздрагивает. Чувствует..."
    alice.c "М-м~"
    alice.c "Щекотно, [mc.name]."
    mc.c "Это ты на мне лежишь."
    alice.c "Тебе мешает?"
    "Такая забавная... Иногда она бывает капризной. Редко показывает эту сторону, и я её обожаю."
    mc.c "Вовсе нет."
    "И ещё мне нравится в этой ситуации... её аппетитная задница..."
    "То есть, конечно, её изящные округлости. Ляжки прижаты к моим коленям, а эта прекрасная попка так и просится к рукам."
    "Её мясистый хвостик медленно покачивается, завораживая меня своей соблазнительной формой."
    "Соблазнительно..."
    image alice fingering 1 = Movie(play="images/characters/alice/hscenes/fingering/fingering1.webm")
    show alice fingering 1 with fade
    pause
    "Я медленно веду ладонью по её бедру и забираюсь выше, чуть сжимая задницу."
    "Она слегка покачивает бёдрами в ответ, но ничего не говорит. Просто немного поглаживаю её..."
    "Нежно разминая её мягкую задницу, я набираю в ладонь целый кусок."
    "Такая мягкость... тепло... шорох шерсти под пальцами. Я бы мог делать это весь день."
    "Я сжимаю её чуть сильнее, пальцы проваливаются в мягкую плоть даже сквозь юбку."
    alice.c "М-м~"
    "Я чувствую, как она начинает мурлыкать громче. Оказывается, ласки её тоже берут..."
    "Для такой утончённой и сдержанной девушки мне нравится иногда разрушать эту броню прикосновениями."
    "За капризность ей полагается время от времени небольшая взбучка. Да и, если честно, я кое-что задумал."
    image alice fingering 2 = Movie(play="images/characters/alice/hscenes/fingering/fingering2.webm")
    show alice fingering 2 with fade
    pause
    "Я веду ладонью по её бедру, затем скольжу обратно вверх, приподнимая подол юбки."
    "Задница и трусики открыты — теперь я могу как следует ухватиться за самое интересное."
    alice.c "[mc.name], ты задрал мне юбку?"
    mc.c "Да."
    alice.c "..."
    alice.c "Ладно..."
    "Она лишь слегка удивлена, но даже не пытается пошевелиться. Можно беспрепятственно лапать её задницу."
    "Медленно обхватывая обе ягодицы, я чувствую лёгкую дрожь, пробегающую по её телу."
    "Её попка слегка вздрагивает. А то, что скрыто под последним тонким слоем ткани... сводит меня с ума."
    "Я осмеливаюсь и медленно провожу пальцем по её трусикам..."
    alice.c "М-м~"
    "Под пальцем мягко. Даже сквозь ткань я чувствую складочки и жар, исходящий от неё..."
    "Она вздрагивает, когда я провожу пальцем по щёлке, словно приглашая меня внутрь."
    "Я просто не могу устоять."
    image alice fingering 3 = Movie(play="images/characters/alice/hscenes/fingering/fingering3.webm")
    show alice fingering 3 with fade
    pause
    "Я стягиваю с неё трусики, открывая киску и задницу, "
    "Она ничего не говорит, но я чувствую её реакцию: голова слегка поворачивается и утыкается в спинку дивана."
    alice.c "М-м~"
    "Я нежно ласкаю её щёлку и чувствую, как влажная липкость стекает по шерсти к входу. Она уже вся завелась."
    "Я медленно провожу двумя пальцами вверх-вниз, заставляя её вздрагивать, когда касаюсь клитора."
    "Её тело напрягается, дрожит и мурлычет у меня на коленях, полностью отдаваясь паре движений пальцами."
    alice.c "А-а~"
    alice.c "[mc.name]~"
    "Вот оно... Она уже не может это скрыть."
    mc.c "Ты вся мокрая."
    alice.c "Я... А-а~ да..."
    alice.c "Это... М-м~ из-за тебя..."
    "Я не хочу её дразнить. Кажется, она сама хотела, чтобы что-то случилось."
    "Мы могли бы продолжить как угодно, но мне нравится просто заставлять её извиваться у меня на коленях."
    image alice fingering 4 = Movie(play="images/characters/alice/hscenes/fingering/fingering4.webm")
    show alice fingering 4 with fade
    pause
    "Я ввожу палец. Она уже такая мокрая, что он скользит внутрь без усилий."
    "Её соки стекают по ногам, блестя на шелковистой чёрной шерсти."
    "Её тело дрожит, пока я двигаю пальцем туда-сюда, и вскоре она уже не может сдерживаться."
    alice.c "М-м-м~ М-м-м~~"
    alice.c "О-о-ох~ [mc.name]~"
    alice.c "Пожалуйста~ А-а~ Не останавливайся~"
    "Она извивается у меня на коленях и выгибает спину. Когтями цепляется за диван, пока я двигаю пальцами внутри неё."
    "Я добавляю ещё один палец; её киска сжимается и пульсирует вокруг них."
    alice.c "Ха-а~ Ха-а~"
    "Она совсем потеряла голову и полностью отдалась моим ласкам."
    "Хочу довести её до оргазма, чтобы она обессиленно рухнула мне на колени."
    image alice fingering 5 = Movie(play="images/characters/alice/hscenes/fingering/fingering5.webm")
    show alice fingering 5 with fade
    pause
    "Я ускоряюсь, глубоко ввожу пальцы и двигаю ими туда-обратно."
    "Мне приходится раздвинуть её пышные ягодицы, чтобы добраться до самого сокровенного."
    "Она приподнимает задницу, приглашая меня, а её киска дрожит, пока я двигаю пальцами."
    alice.c "А-а-а~ Ах-х~ М-м-м~"
    "Её задница вздрагивает от удовольствия, пока она мурлычет и стонет без всякого стеснения."
    alice.c "[mc.name]~ М-м-м~ [mc.name]~"
    alice.c "Ха-а~ Ха-а~ Я... я..."
    alice.c "Как же хорошо~"
    "Она задыхается и часто дышит; жар и влага сочатся из её киски всё сильнее."
    "Её мышцы всё сильнее подрагивают и пульсируют. Кажется, она вот-вот..."
    scene alicefingeringfinish with fadewhite
    alice.c "М-М-М-М-М~!"
    "Её бьёт в экстазе, и соки брызгами заливают мою руку."
    alice.c "А-а-а~ А-а-а~ М-м-м~"
    "Она тяжело дышит и обмякает у меня на коленях."
    "Я чувствую, как дрожат её половые губы, когда вытаскиваю руку; она всё ещё под впечатлением."
    alice.c "Ха-а~ Ха-а~"
    alice.c "[mc.name]..."
    mc.c "Разве не этого ты хотела?"
    alice.c "Н-нет... Ну... почти."
    alice.c "Но... Ха-а~ я не против..."
    alice.c "Наверное, мне стоит тебя поблагодарить, [mc.name]. Но мне... нужно в ванную привести себя в порядок..."
    scene black with fade
    "Придя в себя, она покачивающейся походкой направляется в ванную."
    "До конца дня она больше ни разу об этом не упоминает..."
    "Забавная девушка."

    return
