init offset = 3
default katie = Person(Character(name='Katie', who_color='#d3b016', image = 'katie'), 'Katie', '', 'katie', 'female', 35)

label initialiseCharacter_katie:
    python:
        katie.currentLocation = location_away
        location_away.occupants.extend([katie])
        katie.availableEvents = [katieFirstMeetingEvent]

    return

label updateCharacterStatics_katie:
    python:
        # Personal attributes
        katie.species = 'Fox'
        katie.birthday = 3
        katie.job = 'Office worker'
        katie.giftLoves = [item_goldRing]
        katie.giftLikes = [item_flowers, item_wine, item_dress, item_perfume]
        katie.giftHates = [item_videogame]

        # Skill attributes

        # Sexual attributes
        katie.virgin = False

        # Personal effects

        # Event attributes
        katie.events = [katieFirstMeetingEvent, katieLikeEvent1, katieLikeEvent2, katieHEvent1, katieHEvent2, katieHEvent3, katieHEvent4, katieLikeEvent3, katieHEvent5, katieHEvent6, katieVacation, katieLikeEvent4, katieHEvent7]
        katie.specialEvents = [katieMollyDuoStoryEvent1, katieMollyDuoHEvent1, katieMollyDuoHEvent2, katieZoeDuoStoryEvent1, katieZoeDuoHEvent1]
        katie.selfieOptions = ['beach1', 'bedroom1', 'home1', 'home2', 'homekitchen1']
        katie.wakeUpOptions = ['handjob']
        katie.dateChats = ['Background', 'Job', 'Hobbies']
        katie.pantiesOptions = 3

        # Relationship to MC statistics
        lastStoryEvent = katie.events[-1]
        katie.maxLike = lastStoryEvent.requiredLike
        katie.maxLove = lastStoryEvent.requiredLove

        # World attributes
        katie.preferredMondaySchedule = [location_offices, location_offices, location_town, location_away]
        katie.preferredTuesdaySchedule = [location_offices, location_cafe, location_shop, location_away]
        katie.preferredWednesdaySchedule = [location_offices, location_offices, location_diner, location_away]
        katie.preferredThursdaySchedule = [location_offices, location_offices, location_town, location_bar]
        katie.preferredFridaySchedule = [location_offices, location_park, location_bar, location_away]
        katie.preferredSaturdaySchedule = [location_town, location_cafe, location_diner, location_bar]
        katie.preferredSundaySchedule = [location_cafe, location_beach, location_town, location_away]

        katie.preferredMovedInMondaySchedule = [location_cafe, location_offices, location_home, location_home]
        katie.preferredMovedInTuesdaySchedule = [location_home, location_offices, location_home, location_home]
        katie.preferredMovedInWednesdaySchedule = [location_home, location_offices, location_home, location_home]
        katie.preferredMovedInThursdaySchedule = [location_home, location_offices, location_bar, location_home]
        katie.preferredMovedInFridaySchedule = [location_home, location_offices, location_home, location_home]
        katie.preferredMovedInSaturdaySchedule = [location_home, location_home, location_home, location_home]
        katie.preferredMovedInSundaySchedule = [location_home, location_shop, location_home, location_home]
    return

# Sprites
screen katieClickable(xcenter):
    $ spriteload = katie.apiName + ' neutral'
    imagebutton:
        style 'characterClickable'
        idle spriteload
        xcenter xcenter
        action Call('startCharacterInteraction', character = katie)
        at characterSpriteHover

# Character methods
label katieEvaluateAvailableInteractions:
    python:
        if katie.like >= 5:
            katie.availableActions = list(set(katie.availableActions + ['Spend time']))
        if katie.like >= 20 and katieHEvent2.unlocked:
            katie.availableActions = list(set(katie.availableActions + ['Invite over']))

        if katie.isDateable and katie.like >= 1:
            katie.availableActions = list(set(katie.availableActions + ['Date']))
        if katie.love >= 3:
            katie.availableActions = list(set(katie.availableActions + ['Affection']))
            katie.availableAffections.extend(['Pat'])
        if katie.love >= 6:
            katie.availableAffections.extend(['Hug'])
        if katie.love >= 10 and katieHEvent1.unlocked:
            katie.availableAffections.extend(['Chin Scratch', 'Kiss'])
        if katieHEvent4.unlocked:
            katie.availableAffections.extend(['Caress Butt'])
        if katieHEvent6.unlocked:
            katie.availableAffections.extend(['Boob Grab'])
        if katieHEvent7.unlocked:
            katie.availableActions.extend([{'homebathroom': ['Fingering']}])
        if katie.movedIn:
            katie.availableCommandsPrivate.extend(['Show Panties'])
            katie.availableAffections.extend(['Snuggle'])
    return

# Character interactions
label katieChat:
    show katie smile talk
    return

label katieChat_beach:
    show katie joy
    katie.c "Обожаю нежиться на солнышке!"
    return

label katieChat_shop:
    show katie bashful talk
    katie.c "Я редко выбираюсь в супермаркет, так что придётся довольствоваться этим."
    return

label katieChat_diner:
    show katie tease talk
    katie.c "Ой, как же вкусно они это готовят! О~ И вот это тоже. Иногда я беру..."
    return

label katieChat_cafe:
    show katie thinking
    katie.c "Я часто захожу за кофе, иначе не выдержу весь день."
    return

label katieChat_town:
    show katie smile talk 2
    katie.c "На сегодня с работой покончено. Идёшь за покупками?"
    return

label katieChat_bar:
    show katie bashful
    katie.c "Фух, после сегодняшнего дня не отказалась бы от бокальчика..."
    show katie tease talk
    katie.c "...или нескольких."
    return

label katieChat_aquarium:
    show katie neutral talk
    katie.c "Здесь такая приятная атмосфера. Можно немного расслабиться."
    return

label katieChat_theater:
    show katie smile talk 2
    katie.c "О, привет! У меня появилось немного свободного времени, решила посмотреть, что тут идёт!"
    show katie tease talk
    katie.c "Если ты что-то задумал, я могу составить тебе компанию."
    return

label katieChat_homebedroom:
    if(timeOfDay == 'Morning'):
        show katie smile talk 2
        katie.c "Доброе утро, милый! Рада тебя видеть до начала дня."
    elif(timeOfDay == 'Afternoon'):
        show katie smile talk 2
        katie.c "Сегодня отдыхаю~ Не хочешь присоединиться?"
    elif(timeOfDay == 'Evening'):
        show katie tease talk
        katie.c "М-м~ Как уютно~ Садись рядом, милый."
    elif(timeOfDay == 'Night'):
        show katie tease talk
        katie.c "*Зевает*~ Извини, я уже готова ложиться. Как прошёл твой день?"
    return

label katieChat_homelounge:
    if(timeOfDay == 'Morning'):
        show katie tease talk
        katie.c "Доброе утро! Решила посмотреть телевизор, пока не нужно выходить."
    elif(timeOfDay == 'Afternoon'):
        show katie smile talk 2
        katie.c "Ах~ Обожаю ленивые вечера~"
    elif(timeOfDay == 'Evening'):
        show katie tease talk
        katie.c "[mc.name]! Иди сюда, я обожаю это шоу! Посмотри со мной~"
    elif(timeOfDay == 'Night'):
        show katie tease talk
        katie.c "Уже поздно, да? Я собираюсь ложиться. Ты тоже?"
    return

label katieChat_homekitchen:
    if(timeOfDay == 'Morning'):
        show katie tease talk
        katie.c "Доброе утро, милый! Я как раз готовлю завтрак. Хочешь?"
    elif(timeOfDay == 'Afternoon'):
        show katie tease talk
        katie.c "Привет, милый! Хочешь перекусить? Я могу что-нибудь быстро приготовить!"
    elif(timeOfDay == 'Evening'):
        show katie tease talk
        katie.c "После такого дня я проголодалась. Что будем есть?"
    elif(timeOfDay == 'Night'):
        show katie smile talk
        katie.c "Я скоро пойду спать. Помоги мне здесь прибраться, пожалуйста, милый."
    return

label katieInteractionBathroom:
    katie.c "О-ох! [mc.name]~"
    katie.c "Я просто моюсь..."
    return

label katieSpendTime(onDate):
    if(onDate):
        scene expression 'katie[mc.currentLocation.apiName]date'
    else:
        scene expression 'katie[mc.currentLocation.apiName]'
    with fade
    return

label katieReceiveGift(item, likeChange, loveChange):
    show katie neutral talk
    katie.c "Хм?"
    if(loveChange > 0):
        show katie joy
        katie.c "Для меня? Правда? Тебе не стоило."
        katie.c "Большое спасибо!"
        if(katieVacation.unlocked):
            katie.c "Люблю тебя!"
    elif(likeChange > 1):
        show katie smile talk 2
        katie.c "Ой, как мило! Спасибо!"
    elif(likeChange < 1):
        show katie mad talk
        katie.c "Мне... это не очень нравится..."
    else:
        show katie smile talk
        katie.c "Как мило с твоей стороны. Спасибо."
    return

label katieReceiveDateInvitation:
    show katie neutral talk
    katie.c "О-о~ Конечно! Что ты задумал?"
    show katie neutral
    call dateInvitationSelector(katie) from _call_dateInvitationSelector_4
    show katie neutral talk
    katie.c "Значит, [proposedDateDayOfWeek], в [proposedDateTime], в месте «[proposedDateLocation.name]»? Чудесно!"

    python:
        scheduledDate = Date(katie, proposedDateLocation, proposedDateDay, proposedDateDayOfWeek, proposedDateTime)
        mc.scheduledDates.append(scheduledDate)
        katie.scheduledDates.append(scheduledDate)
    return

label katieStartDate:
    if(mc.currentLocation == location_home):
        show katie tease with dissolve
        katie.c "Ты специально убрался ради меня?"
    else:
        show katie smile talk with dissolve
        katie.c "Я так ждала сегодняшнего дня!"
    return

label katieDateInteraction:
    show katie smile with dissolve
    show screen dateUi(katie) with dissolve
    call screen dateInteractionScreen(katie, mc.currentLocation)

label katieChatDate:
    show katie smile talk 2
    katie.c "Прекрасное угощение, правда?"
    return

label katieChatDate_beach:
    show katie tease talk
    katie.c "Ах, полежать в шезлонге... Лучше и не придумаешь."
    return

label katieChatDate_park:
    show katie smile talk 2
    katie.c "Давай присядем здесь."
    show katie smile talk
    katie.c "Смотри, цветы распускаются. Ой, сейчас расскажу. Вот эти..."
    return

label katieChatDate_diner:
    show katie joy
    katie.c "Вкуснотища!"
    show katie smile talk 2
    katie.c "Тебе обязательно нужно попробовать. Давай, открывай рот."
    return

label katieChatDate_cafe:
    show katie thinking
    katie.c "Какой тортик мне выбрать?"
    show katie tease talk
    katie.c "О, ты возьмёшь их? Тогда поделимся, спасибо!"
    return

label katieChatDate_bar:
    show katie bashful talk
    katie.c "Мне бы не стоило брать ещё... На этой неделе я уже несколько выпила."
    show katie tease
    katie.c "Если только... Ты не пытаешься меня опьянить~?"
    return

label katieChatDate_aquarium:
    show katie joy
    katie.c "Как здесь красиво!"
    show katie tease talk
    katie.c "В сувенирной лавке тоже есть симпатичные вещи. Давай посмотрим."
    return

label katieChatDate_theater:
    show katie joy
    katie.c "Какая чудесная идея, милый! Спасибо!"
    show katie thinking
    katie.c "О-о~ Уже чувствую запах попкорна~"
    return

# Date topics
label katieChat_background:
    show katie thinking
    katie.c "О-о, ну что я могу сказать..."
    show katie smile talk
    katie.c "Я выросла в городке в паре часов отсюда. У меня довольно большая семья: пятеро братьев и сестёр — один старший и четверо младших."
    katie.c "Обычная школьная жизнь. Когда мне исполнилось восемнадцать, я вместе с друзьями поступила в колледж в соседнем городе."
    show katie smile talk 2
    katie.c "Специальность была немного бестолковая — «История искусств». Практической пользы от неё, конечно, никакой, зато было интересно. В детстве я любила искусство."
    show katie bashful talk
    katie.c "Хорошее было время... Я никогда не была тусовщицей, но мы с девочками отлично проводили время. Студенческие годы были чудесными."
    katie.c "Я до сих пор общаюсь с большинством подруг оттуда."
    show katie neutral talk
    katie.c "В общем, я поработала в нескольких местах, немного поездилa, когда появлялись новые возможности..."
    show katie smile talk
    katie.c "...А теперь я здесь! Переехала сюда около семи лет назад и с тех пор живу здесь."
    show katie bashful talk
    katie.c "Ох, куда уходит время..."
    show katie bashful
    mc.c "Да ладно, ты говоришь так, будто это было в древности."
    show katie smile talk
    katie.c "Милый, это {b}и было{/b} давно. Даже кажется, будто ещё дольше."
    show katie tease
    katie.c "Оглянуться не успеешь, как тоже будешь вспоминать, куда ушли годы."
    katie.c "Пользуйся молодостью, пока она у тебя есть."
    return

label katieChat_job:
    show katie thinking
    katie.c "Ох, боюсь, я утомлю тебя до слёз."
    mc.c "Это невозможно."
    show katie smile talk
    katie.c "Красиво говоришь... Но, поверь, будет хуже, чем ты можешь себе представить."
    show katie smile
    mc.c "Ну, удиви меня."
    show katie neutral talk
    katie.c "*Вздыхает* Это бумажная компания..."
    katie.c "Тонны бумаги..."
    show katie neutral
    "Ох... Вряд ли это можно как-то приукрасить."
    mc.c "То есть {b}ты{/b} производишь бумагу?"
    show katie joy
    katie.c "Ой, ха-ха! Господи, нет! Вот бы мне так повезло."
    show katie smile talk 2
    katie.c "Обычная офисная работа... Делопроизводство. Цифры, логистика, всякие офисные... дела."
    katie.c "Честно говоря, я иногда даже не знаю, как официально называется моя должность. Компания небольшая, офис общий, поэтому я занимаюсь понемногу всем."
    katie.c "Настоящая «работа с электронной почтой», как некоторые говорят..."
    show katie thinking
    katie.c "Хотя это всё же лучше, чем продажи. Вот это настоящий кошмар."
    mc.c "Значит, офис-менеджмент? Кадры?"
    show katie neutral
    katie.c "..."
    show katie mad talk
    katie.c "Я разве похожа на кадровичку?"
    mc.c "Ой, нет! Я не..."
    show katie bashful talk
    katie.c "*Фух* Слава богу..."
    show katie bashful
    mc.c "Вообще, рад, что ты тоже терпеть не можешь таких людей..."
    show katie tease talk
    katie.c "После стольких лет в офисе удивляюсь, что ещё никого из них не придушила."
    show katie tease
    mc.c "Ха-ха. Значит, ты работаешь в этой компании с самого переезда?"
    show katie bashful talk
    katie.c "Ага... Боже, неужели так давно?"
    show katie bashful
    mc.c "А чем ты занималась раньше?"
    show katie neutral talk
    katie.c "После выпуска я перебивалась разными работами в городе, где училась. В основном делопроизводство: работала в мэрии, помогала местной администрации и ещё в паре случайных компаний..."
    show katie smile talk
    katie.c "Несколько раз меняла работу, обычно просто искала зарплату побольше."
    katie.c "Когда увидела вакансию в этом городе, сразу решила попробовать. Я слышала о нём много хорошего, и рада, что переехала."
    return

label katieChat_hobbies:
    show katie tease talk
    katie.c "О, я просто обожаю готовить!"
    show katie bashful talk
    katie.c "Наверное, ты уже заметил, что я люблю вкусно поесть..."
    show katie tease talk
    katie.c "Я много времени провожу на кухне и за выпечкой: придумываю рецепты, пробую новое."
    katie.c "Теперь я уже довольно горжусь своим набором рецептов!"
    show katie tease
    mc.c "Звучит здорово. Надеюсь, когда-нибудь я всё это попробую."
    show katie bashful talk
    katie.c "О, обязательно..."
    show katie smile talk 2
    katie.c "Приятно готовить для того, кто это ценит."
    katie.c "Так что, когда придёт время, готовься — я приготовлю много всего!"
    show katie smile
    mc.c "Буду ждать. А что у тебя получается лучше всего?"
    show katie thinking
    katie.c "Хм... Обожаю наваристое рагу, особенно с мясом."
    show katie tease talk
    katie.c "Пробовал крольчатину?"
    show katie tease
    mc.c "Э-э... Нет, но я бы попробовал."
    show katie smile talk 2
    katie.c "Думаю, я смогу тебя убедить. Ты удивишься~"
    show katie smile talk
    katie.c "А из выпечки... Обожаю хороший бисквит. И у меня есть отличные рецепты маффинов."
    show katie smile
    mc.c "Я уже проголодался..."
    show katie joy
    katie.c "Отлично! Всегда приятно готовить для хорошего едока!"
    show katie thinking
    katie.c "Посмотри на меня — всё о еде... Ещё я..."
    show katie neutral talk
    katie.c "Встречаюсь с подругами. Ходим в кино или на спектакли. Ещё люблю хороший мюзикл."
    show katie smile talk
    katie.c "Дома я довольно много читаю, когда получается."
    show katie smile
    mc.c "Что именно?"
    show katie neutral
    katie.c "...В основном романы..."
    show katie bashful talk
    katie.c "...Иногда любовные романы..."
    show katie bashful
    "Она слегка смущается... Лучше сменить тему."
    return

#

label katieDatePayFor:
    show katie tease talk
    katie.c "О-о~ Какой джентльмен!"
    show katie smile talk 2
    katie.c "Спасибо, милый!"
    if(katieVacation.unlocked):
        katie.c "Чем я заслужила тебя?"
    return

label katieEndDate:
    if(dateScore < 40):
        show katie sad
        katie.c "Сегодня вышло немного скучно... *Вздыхает*"
    else:
        if(katie.movedIn):
            show katie tease talk
            katie.c "Я чудесно провела вечер, милый. Люблю тебя!"
        else:
            show katie joy
            katie.c "Сегодня было прекрасно. Не затягивай до следующего раза, ладно?"
    return

label katieContinueDateAtHome:
    scene expression 'katie[mc.currentLocation.apiName]bedroom' with fade
    pause
    $ allowContinueToBed = False
    if(katieHEvent1.unlocked):
        $ allowContinueToBed = True
    return allowContinueToBed

label katieHomeStartSex:
    show katie tease talk
    katie.c "О-хо~ Правда? Ну тогда..."
    katie.c "Конечно~"
    return

label katieHomeSexJoinIn(character):
    show katie bashful talk at twoPersonLeft with dissolve
    molly.c "[mc.name]~ [character.name]~ Ты не против, если... я присоединюсь?"
    show katie bashful
    return

label katieEndDateAtHome:
    if(katieVacation.unlocked):
        katie.c "Я чудесно провела время, милый. Люблю тебя!"
    else:
        katie.c "Мне пора. Скоро увидимся, [mc.name]!"
    return

image katie pat animated = Movie(play="images/characters/katie/affections/katiePat.webm", side_mask=True, loop=True)
label katieReceivePat:
    hide katie with dissolve
    show katie pat animated with dissolve
    pause
    katie.c "Нечестно так обращаться с леди..."
    katie.c "Но... Пока не останавливайся."
    return

image katie chinscratch animated = Movie(play="images/characters/katie/affections/katieChinscratch.webm", side_mask=True, loop=True)
label katieReceiveChinScratch:
    hide katie with dissolve
    show katie chinscratch animated with dissolve
    pause
    katie.c "Ох, боже..."
    katie.c "Что ты со мной делаешь~"
    return

image katie caressbutt animated = Movie(play="images/characters/katie/affections/katieCaressButt.webm", side_mask=True, loop=True)
label katieReceiveCaressButt:
    hide katie with dissolve
    show katie caressbutt animated with dissolve
    pause
    katie.c "О-ох!"
    katie.c "Хе-хе~ [mc.name]! Ну ты и шалун... Кто-нибудь увидит~"
    return

image katie boobgrab animated = Movie(play="images/characters/katie/affections/katieBoobGrab.webm", side_mask=True, loop=True)
label katieReceiveBoobGrab:
    hide katie with dissolve
    show katie boobgrab animated with dissolve
    pause
    katie.c "О-ох! Милый~"
    katie.c "Ну никак не можешь остановиться, да? Вот озорник~"
    return

image katie snuggle animated = Movie(play="images/characters/katie/affections/katieSnuggle.webm", side_mask=True, loop=True)
label katieReceiveSnuggle:
    "Мы отдыхаем на диване с Кэти, и я обнимаю её."
    show katie smile talk
    katie.c "Милый~"
    hide katie with dissolve
    show katie snuggle animated with dissolve
    pause
    "Она принимает приглашение и уютно прижимается ко мне, переплетая наши пальцы."
    katie.c "Ой, милый~ Я люблю тебя~"
    pause
    return

label katieReceiveHug:
    hide katie with dissolve
    show katie hug with dissolve
    pause
    katie.c "Ох, милый..."
    katie.c "Можешь обнять меня покрепче, если хочешь."
    return

label katieReceiveKiss:
    hide katie with dissolve
    show katie kiss with dissolve
    katie.c "*Чмок*"
    pause
    if(katieHEvent3.unlocked):
        katie.c "Так страстно~ Мой большой, сильный мужчина..."
    else:
        if(katieVacation.unlocked):
            katie.c "Я люблю тебя, [mc.name]~"
        else:
            katie.c "Я могла бы к этому привыкнуть..."
    return

label katieInitiatePat:
    show katie sad talk with dissolve
    katie.c "Какой был день..."
    katie.c "Мне нужно поднять настроение."
    hide katie with dissolve
    show katie pat animated with dissolve
    pause
    katie.c "Хи-хи."
    katie.c "И это было нетрудно."
    return

label katieInitiateHug:
    show katie tease talk with dissolve
    katie.c "[mc.name]!"
    hide katie with dissolve
    show katie hug with dissolve
    pause
    katie.c "М-м-м... Можно ещё немного?.."
    return

label katieInitiateKiss:
    show katie tease talk with dissolve
    katie.c "[mc.name]..."
    hide katie with dissolve
    show katie kiss with dissolve
    katie.c "*Чмок*"
    pause
    hide katie with dissolve
    show katie smile with dissolve
    katie.c "Рада тебя видеть, милый."
    return

label katieInitiateSnuggle:
    show katie tease
    "Я отдыхаю на диване, когда Кэти плюхается рядом."
    show katie tease talk
    katie.c "Милый~ Обнимемся?"
    hide katie with dissolve
    show katie snuggle animated with dissolve
    pause
    "Она прижимается к моему плечу и берёт меня за руку."
    katie.c "Хе-хе~ Как хорошо~"
    pause
    return

label katieInitiateHomeSex:
    show katie bashful talk
    katie.c "Милый, мне как-то... хочется~"
    show katie tease talk
    katie.c "Может, займёмся?.."
    show katie tease
    return

label katieInitiateHomeSexDeny:
    show katie bashful talk
    katie.c "О-ох... Да, прости, если ты занят..."
    return

label katieSeesAffection(affection):
    show katie tease talk with dissolve
    katie.c "[mc.name]~ Можно мне, может быть?.."
    show katie tease
    "Кэти смотрит на меня умоляющими глазами. Кто ей откажет?"
    mc.c "Конечно."
    call expression 'katieReceive' + affection from _call_expression_41
    hide katie with dissolve
    return

label katieInviteOver:
    show katie smile talk
    katie.c "О-о~? Тогда пойдём."
    return

label katieInitiateInviteOver:
    show katie bashful talk
    katie.c "[mc.name], ты не против, если... я сегодня зайду к тебе?"
    show katie bashful
    menu:
        'Yes':
            show katie joy
            katie.c "О-о~ Здорово!"
            return True
        'No':
            show katie neutral talk
            katie.c "Ладно, ничего страшного!"
    return False

label katieInviteGoHomeTogether:
    show katie smile talk
    katie.c "Готов идти домой, милый? Хорошо!"
    show katie tease talk
    katie.c "Веди~ Хм-хм~"
    return

label katieInitiateGoHomeTogether:
    show katie tease talk
    katie.c "Ну что... Пойдём {i}домой{/i} вместе? Хм-хм~"
    show katie tease
    menu:
        'Yes':
            show katie joy
            katie.c "Хе-хе~"
            return True
        'No':
            show katie smile talk
            katie.c "Ладно, увидимся дома, милый!"
    return False

label katieShowPanties(pantiesIndex = 1):
    show katie bashful talk
    katie.c "Опять? Ты странный, милый..."
    $ renpy.show(katie.apiName + ' panties ' + str(pantiesIndex), tag=katie.apiName)
    with dissolve
    if(pantiesIndex == 1):
        katie.c "Обычные удобные трусики. Прости, что они не очень сексуальные..."
    elif(pantiesIndex == 2):
        katie.c "Я хотела что-нибудь чуть симпатичнее. Только оборки, наверное, уже перебор. Нормально смотрятся?"
    elif(pantiesIndex == 3):
        katie.c "Купила их для... наших вечеров вместе~"
    return

label katieSendDateText(proposedDate):
    python:
        katie.textChain.append(Message(mc, katie, 'Hi [mc.name]! Fancy going out somewhere tomorrow?', Null, day, timeOfDay))
        katie.textChain.append(Message(mc, katie, 'The ' + proposedDate.location.name + ' in the ' + proposedDate.time + ' might be quite nice!', Null, day, timeOfDay, proposedDate))
    return

label katieGetSelfieOptions:
    $ katieSelfieOptions = []
    if(katieLikeEvent2.unlocked):
        $ katieSelfieOptions.extend(['beach1'])
    if(katieHEvent1.unlocked):
        $ katieSelfieOptions.extend(['bedroom1', 'home1'])
    if(katieHEvent2.unlocked):
        $ katieSelfieOptions.extend(['home2'])
    if(katie.movedIn):
        $ katieSelfieOptions.extend(['homekitchen1'])

    return katieSelfieOptions

label katieSendSelfie(selfieName):
    python:
        potentialResponses = []
        match selfieName:
            case 'beach1':
                potentialResponses.append({'text': "Наслаждайся!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Красотка!", 'statChange': 'love', 'statChangeAmount': 1})
                katie.textChain.append(Message(mc, katie, 'Немного загораю!', selfieName, day, timeOfDay, responses = potentialResponses))
            case 'bedroom1':
                potentialResponses.append({'text': "Тебе очень идёт!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Просто сногсшибательно! Красотка!", 'statChange': 'love', 'statChangeAmount': 1})
                katie.textChain.append(Message(mc, katie, 'Ходила с подругой за покупками. Она уговорила меня купить это платье.', Null, day, timeOfDay))
                katie.textChain.append(Message(mc, katie, "Для меня это платье немного смелое...", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'home1':
                potentialResponses.append({'text': "Пышные бёдра спасают жизни!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Дай сжать их в ладонях...", 'statChange': 'love', 'statChangeAmount': 1})
                katie.textChain.append(Message(mc, katie, "Как там говорится у вас, молодых? \"Пышные бёдра спасают жизни\"?", selfieName, day, timeOfDay, responses = potentialResponses))
            case 'home2':
                potentialResponses.append({'text': "Упс!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "Что ты сказал? Я немного... отвлеклась :P", 'statChange': 'love', 'statChangeAmount': 1})
                katie.textChain.append(Message(mc, katie, 'Отдыхаю дома и думаю о тебе.', selfieName, day, timeOfDay))
                katie.textChain.append(Message(mc, katie, 'Ой! Как же это верх так задрался? :)', Null, day, timeOfDay, responses = potentialResponses))
            case 'homekitchen1':
                potentialResponses.append({'text': "Всё, что ты готовишь, очень вкусное, красавица!", 'statChange': 'like', 'statChangeAmount': 1})
                potentialResponses.append({'text': "М-м... Кусочек того торта.", 'statChange': 'love', 'statChangeAmount': 1})
                katie.textChain.append(Message(mc, katie, 'Что бы ты сегодня хотел съесть, милый? <3', selfieName, day, timeOfDay))
    return

label katieSexSelect:
    hide screen mainUi
    scene black with fade
    image katie sex waiting = Movie(play="images/characters/katie/hscenes/sexWaiting.webm")
    show katie sex waiting with fade

    call screen katieSexSelectScreen
    if(katieHEvent3.unlocked and (timeOfDay == 'Evening' or timeOfDay == 'Night')):
        if(katie.movedIn):
            menu katieSleepTogether:
                "Переспать с Кэти?"
                'Yes':
                    katie.c "Спокойной ночи, милый~"
                    call characterSleepover(katie) from _call_characterSleepover_8
                'No':
                    pass
        else:
            menu katieStayTheNight:
                "Пригласить [katie.name] остаться на ночь?"
                'Yes':
                    $ katie.addLove(1)
                    katie.c "С удовольствием, милый. Спасибо."
                    call characterSleepover(katie) from _call_characterSleepover_9
                'No':
                    katie.c "Можешь приглашать меня когда угодно~"

    call endScene(character = katie, targetLocation = location_home) from _call_endScene_12

screen katieSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(katieHEvent1.unlocked or persistent.debugMode):
                textbutton 'Blowjob' keysym str(1):
                    action [Jump('katieBlowjob')]
            else:
                textbutton 'Locked'
            if(katieHEvent2.unlocked or persistent.debugMode):
                textbutton 'Boobjob' keysym str(2):
                    action [Jump('katieBoobjob')]
            else:
                textbutton 'Locked'
            if(katieHEvent3.unlocked or persistent.debugMode):
                textbutton 'Missionary' keysym str(3):
                    action [Jump('katieMissionary')]
            else:
                textbutton 'Locked'
            if(katieHEvent5.unlocked or persistent.debugMode):
                textbutton 'Nursing Handjob' keysym str(4):
                    action [Jump('katieNursingHandjob')]
            else:
                textbutton 'Locked'
            if(katieVacation.unlocked or persistent.debugMode):
                textbutton 'Doggy Style' keysym str(5):
                    action [Jump('katieDoggyStyle')]
            else:
                textbutton 'Locked'
            if(katieVacation.unlocked or persistent.debugMode):
                textbutton 'Reverse Cowgirl' keysym str(6):
                    action [Jump('katieReverseCowgirl')]
            else:
                textbutton 'Locked'
            textbutton 'End' keysym str(7):
                action [Hide('katieSexSelectScreen'), Return()]

label katieSleepover:
    scene katiesleepover with fade
    pause
    return

label katieMorningBedInteraction:
    scene katiehomemorning with fade
    pause
    if(katie.movedIn):
        katie.c "Хм-хм~ Доброе утро, мой замечательный мужчина~"
        katie.c "Скоро встану и приготовлю завтрак, но сначала..."
        katie.c "Давай ещё немного поваляемся~"
    else:
        katie.c "Доброе утро, милый."
        katie.c "Можешь ещё немного поспать."
        katie.c "Или... приготовить завтрак?"
    return

label katieMorningBedInteractionSex(event):
    if(event == 'handjob'):
        image katie morning handjob 1 = Movie(play="images/characters/katie/hscenes/morning/handjob1.webm")
        show katie morning handjob 1 with fade
        pause
        katie.c "О! Доброе утро, милый!"
        katie.c "Э-э... Я просто..."
        katie.c "Увидела твоего дружка... Подумала, что тебе может понравиться..."
        katie.c "Ты не против? Ну, думаю, нет."
        katie.c "Иди сюда, [mc.name]..."
        image katie morning handjob 2 = Movie(play="images/characters/katie/hscenes/morning/handjob2.webm")
        show katie morning handjob 2 with fade
        pause
        katie.c "М-м~"
        katie.c "Доброе утро."
    return

# Sex scenes
label katieBlowjob:
    image katie blowjob part 1 = Movie(play="images/characters/katie/hscenes/blowjob/part1.webm")
    show katie blowjob part 1 with fade
    pause
    image katie blowjob part 2 = Movie(play="images/characters/katie/hscenes/blowjob/part2.webm")
    show katie blowjob part 2 with fade
    pause
    image katie blowjob end = Image("images/characters/katie/hscenes/blowjob/end.webp")
    scene katie blowjob end with fadewhite
    pause
    jump katieSexSelect

label katieBoobjob:
    image katie boobjob start = Image("images/characters/katie/hscenes/blowjob/start.webp")
    scene katie boobjob start with fade
    pause
    image katie boobjob part 1 = Movie(play="images/characters/katie/hscenes/boobjob/part1.webm")
    show katie boobjob part 1 with fade
    pause
    image katie boobjob part 2 = Movie(play="images/characters/katie/hscenes/boobjob/part2.webm")
    show katie boobjob part 2 with fade
    pause
    image katie boobjob part 3 = Movie(play="images/characters/katie/hscenes/boobjob/part3.webm")
    show katie boobjob part 3 with fade
    pause
    image katie boobjob end = Image("images/characters/katie/hscenes/boobjob/end.webp")
    scene katie boobjob end with fadewhite
    pause
    jump katieSexSelect

label katieMissionary:
    image katie missionary start = Movie(play="images/characters/katie/hscenes/missionary/kissing.webm")
    scene katie missionary start with fade
    pause
    image katie missionary part 1 = Movie(play="images/characters/katie/hscenes/missionary/part1.webm")
    show katie missionary part 1 with fade
    pause
    image katie missionary part 2 = Movie(play="images/characters/katie/hscenes/missionary/part2.webm")
    show katie missionary part 2 with fade
    pause
    image katie missionary part 3 = Movie(play="images/characters/katie/hscenes/missionary/part3.webm")
    show katie missionary part 3 with fade
    pause
    image katie missionary part 4 = Movie(play="images/characters/katie/hscenes/missionary/part4.webm")
    show katie missionary part 4 with fade
    pause
    image katie missionary end = Image("images/characters/katie/hscenes/missionary/end.webp")
    scene katie missionary end with fadewhite
    pause
    jump katieSexSelect

label katieNursingHandjob:
    image katie nursing handjob part 1 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part1.webm")
    show katie nursing handjob part 1 with fade
    pause
    image katie nursing handjob part 2 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part2.webm")
    show katie nursing handjob part 2 with fade
    pause
    image katie nursing handjob part 3 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part3.webm")
    show katie nursing handjob part 3 with fade
    pause
    image katie nursing handjob part 4 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part4.webm")
    show katie nursing handjob part 4 with fade
    pause
    image katie nursing handjob end 1 = Image("images/characters/katie/hscenes/nursingHandjob/end1.webp")
    scene katie nursing handjob end 1 with fadewhite
    pause
    image katie nursing handjob end 2 = Image("images/characters/katie/hscenes/nursingHandjob/end2.webp")
    scene katie nursing handjob end 2 with fade
    pause
    jump katieSexSelect

label katieDoggyStyle:
    image katie doggy 1 = Movie(play="images/characters/katie/hscenes/doggy/part1.webm")
    show katie doggy 1 with fade
    pause
    image katie doggy 2 = Movie(play="images/characters/katie/hscenes/doggy/part2.webm")
    show katie doggy 2 with fade
    pause
    jump katieSexSelect

label katieReverseCowgirl:
    image katie reverse cowgirl = Movie(play="images/characters/katie/hscenes/reverseCowgirl/part1.webm")
    show katie reverse cowgirl with fade
    pause
    jump katieSexSelect

label katiehomebathroomFingering:
    scene katiehevent7i3 with fade
    pause
    image katiesex bath fingering 1 = Movie(play="images/characters/katie/hscenes/bathFingering/part1.webm")
    show katiesex bath fingering 1 with fade
    pause
    image katiesex bath fingering 2 = Movie(play="images/characters/katie/hscenes/bathFingering/part2.webm")
    show katiesex bath fingering 2 with fade
    pause
    scene katiebathfingeringfinish1 with fadewhite
    pause
    return

# Events
default katieFirstMeetingEvent = Event('First meeting', 'katieFirstMeeting', [katie], 0, 0, [], location_bar, ['Evening', 'Night'], triggerDay = 3)
default katieLikeEvent1 = Event('Helping hand', 'katieLikeEvent1', [katie], 10, 0, [katieFirstMeetingEvent], location_town, ['Afternoon', 'Evening', 'Night'])
# Makes her dateable
default katieLikeEvent2 = Event('First date', 'katieLikeEvent2', [katie], 20, 0, [katieLikeEvent1], location_park, ['Morning', 'Afternoon', 'Evening', 'Night'])
# First kiss. First H (blowjob)
default katieHEvent1 = Event('Some tea?', 'katieHEvent1', [katie], 30, 10, [katieLikeEvent2], location_cafe, ['Afternoon', 'Evening'])
# Boobjob
default katieHEvent2 = Event('Some advantages', 'katieHEvent2', [katie], 40, 15, [katieHEvent1], location_bar, ['Afternoon', 'Evening', 'Night'])
# First sex (missionary)
default katieHEvent3 = Event('Like a woman', 'katieHEvent3', [katie], 50, 20, [katieHEvent2], location_diner, ['Evening'], ['Friday', 'Saturday'])
# Table doggy
default katieHEvent4 = Event('Entranced', 'katieHEvent4', [katie], 60, 25, [katieHEvent3], location_bar, ['Afternoon', 'Evening'], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
# Discussion on kids and birth control
default katieLikeEvent3 = Event('Little ones', 'katieLikeEvent3', [katie], 70, 30, [katieHEvent4], location_beach, ['Morning', 'Afternoon'])
# Nursing handjob
default katieHEvent5 = Event('Sweet dreams', 'katieHEvent5', [katie], 80, 35, [katieLikeEvent3], location_home, ['Afternoon', 'Evening', 'Night'])
# Lingerie cowgirl
default katieHEvent6 = Event('Handyman', 'katieHEvent6', [katie], 90, 40, [katieHEvent5], location_home)
# Abroad hotel beach pool vacation
default katieVacation = Event('Poolside getaway', 'katieVacation', [katie], 100, 45, [katieHEvent6], Null, extraNotes = 'Organise a vacation. Special option in interaction menu.', cost=2000, requiresInvite = True)
# Move in invite + event
default katieLikeEvent4 = Event('Moving in', 'katieLikeEvent4', [katie], 110, 50, [katieVacation], Null, extraNotes = 'Things are getting serious. Are we ready for the next step?\nSpecial option in interaction menu.', requiredItems = [item_car], requiresInvite = True)
# Bath fingering
default katieHEvent7 = Event('Letting off steam', 'katieHEvent7', [katie], 120, 55, [katieLikeEvent4], location_home_bathroom, ['Evening', 'Night'], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], mcInitiated = True)

label katieFirstMeeting(fromGallery):
    $ location_bar.showBackground()
    $ katie.knownToMC = True
    hide katie
    "Сегодня я работаю за стойкой в баре. Вечер должен быть довольно тихим, так что одного-двух сотрудников хватит."
    "Бар не совсем в центре города, но и не в особенно густонаселённом районе. Что-то среднее — сюда приходят, только если знают о заведении."
    "У нас бывают самые разные посетители: постоянные местные, проводящие весь вечер с друзьями, и пары, заглянувшие выпить перед сном."
    "Когда в баре наступает затишье, я обхожу столики и собираю пустые бокалы."
    scene katiefirstmeetingi1 with fade
    pause
    "Подойдя, я замечаю за столиком лисичку. Кажется, она пришла минут пятнадцать назад и весь вечер сидит одна."
    "Медленно потягивает вино, то поглядывая на дверь, то на часы, то в телефон."
    "Из-под длинного цветочного платья выглядывает яркая рыжевато-коричневая шерсть. Волосы — ослепительно светлые, почти оранжевые."
    "А больше всего бросаются в глаза большие ушки и пушистый хвост, чуть покачивающийся позади."
    "В ней есть утончённость взрослой женщины, но лицо выглядит немного печальным."
    $ location_bar.showBackground()
    show katie thinking with dissolve
    call playMusic(sadTheme) from _call_playMusic_139
    mc.c "Принести вам ещё бокал мерло, мисс?"
    katie_unknown "..."
    katie_unknown "...Хм, нет, спасибо."
    "Она говорит довольно меланхолично. Похоже, вечер идёт совсем не так, как она ожидала."
    "Она села за столик на двоих лицом к двери, но у неё нет ни книги, ни газеты, чтобы скоротать время. Кого-то ждёт?"
    mc.c "Вы кого-то ждёте?"
    show katie sad talk
    katie_unknown "Должна была... Теперь уже не уверена..."
    show katie sad
    "Её лицо заметно омрачается. Кажется, я спросил не то."
    mc.c "Уверен, они скоро придут. Наше место немного спрятано."
    show katie sad
    katie_unknown "Хм..."
    "Наверное, лучше пока оставить её в покое. Неужели её бросили ждать?"
    mc.c "Позовите, если захотите ещё чего-нибудь."
    hide katie with dissolve
    "Не получив ответа, я оставляю её в покое. Возвращаюсь за стойку и готовлю ещё пару напитков для посетителей."
    scene black with fade
    pause
    $ location_bar.showBackground()
    "Вечерняя смена подходит к концу, посетителей становится меньше — они заканчивают вечер."
    "Я собирался передать бар паре сотрудников на подмене и отправиться домой."
    "Время от времени я поглядываю на лисичку. Она подпирает подбородок рукой и теперь в основном смотрит в телефон."
    "Похоже, тот, кого она ждала, так и не пришёл."
    "Вряд ли она хорошо провела вечер. Разве я хороший хозяин, если оставлю всё как есть? У меня появляется идея."
    "Я наливаю бокал мерло и подхожу к ней."
    show katie thinking with dissolve
    pause
    "Я ставлю бокал на её столик."
    mc.c "Извините, мисс. Я по ошибке налил не тот напиток другому посетителю. Не хочу, чтобы он пропал, поэтому мы угощаем вас, если вы не против. Вы ведь заказывали именно это вино?"
    show katie neutral talk
    katie_unknown "О, правда? Спасибо, я с удовольствием воспользуюсь предложением."
    show katie neutral
    mc.c "Друг не пришёл?"
    show katie sad talk
    katie_unknown "{b}Свидание{/b} сорвалось..."
    show katie sad
    "Ох... Кажется, я вляпался."
    mc.c "О-ох... Простите, мисс. Он хотя бы написал вам?"
    show katie sad talk
    katie_unknown "Вообще ничего."
    mc.c "Первое свидание?"
    "Она делает глоток."
    katie_unknown "Должно было быть. Подруга коллеги моей подруги всё устроила. Не совсем свидание вслепую, но почти. Мы даже не знакомы."
    show katie sad
    "Знаю по себе: ужасное чувство — когда незнакомец бросает тебя, даже не объяснившись."
    "Наверное, ей не помешает компания. Я сажусь напротив."
    mc.c "Мне очень жаль. Со мной тоже такое бывало, я знаю, каково это."
    mc.c "Но это лишь значит, что он не стоил твоего времени. Зато ты избежала нескольких неловких вечеров с идиотом, верно?"
    show katie neutral talk
    katie_unknown "Это правда. Со мной такое уже бывало."
    show katie neutral
    "Она почти улыбается. Думаю, ей просто нужно с кем-нибудь поговорить."
    mc.c "Что подруга рассказывала об этом парне? Похоже, она не слишком хорошо его проверила."
    show katie neutral talk
    katie_unknown "Не так уж много. Мне проще поговорить и всё выяснить лично. Я самая обычная офисная сотрудница, работаю в страховании или вроде того."
    mc.c "Кем вы работаете?"
    show katie smile talk
    katie_unknown "Ой, ну я..."
    call stopMusic from _call_stopMusic_25
    scene black with fade
    pause
    $ location_bar.showBackground()
    call playMusic(heartTheme) from _call_playMusic_140
    show katie smile talk 2
    katie_unknown "...и с тех пор я с ним не разговаривала. После этого я как следует высказала Рэйчел всё, что думаю!"
    "Мы какое-то время беседуем о её жизни, работе, друзьях и о нескольких неудачных свиданиях."
    "Но теперь она улыбается. Когда разговорится, она оказывается очень жизнерадостной. Надеюсь, вечер не прошёл для неё совсем зря."
    show katie bashful talk
    katie_unknown "Ох, я и правда задержала тебя, заболтала. Ты ведь должен работать, да?"
    show katie bashful
    mc.c "Да не за что, я владелец этого места. Просто сегодня был на смене. Не знаю, бывали ли вы здесь раньше, но старина Терри ушёл на пенсию, и я его заменил."
    show katie surprise
    katie_unknown "Ничего себе! Это твоё заведение? И в таком молодом возрасте!"
    show katie bashful talk
    katie_unknown "В любом случае, я, кажется, задержала тебя и не дала закончить вечер. Не стоило тебе возиться со старушкой вроде меня."
    "Старина? Ей ведь на вид чуть за тридцать."
    mc.c "Мне тоже хотелось с кем-нибудь поговорить. Как я уже сказал, сам бывал в такой ситуации. Выглядело так, будто вечер не задался. Какой же я хозяин, если оставлю такую очаровательную леди одну?"
    show katie bashful talk
    katie_unknown "О-ох, спасибо. Было приятно, в итоге ты сделал этот вечер не таким уж плохим."
    show katie mad talk
    katie_unknown "Ты прав. К чёрту этого парня. Он и правда не казался таким уж интересным."
    show katie smile
    mc.c "Совершенно верно."
    show katie smile talk 2
    katie_unknown "Наверное, мне уже пора. Спасибо, что составил мне компанию."
    mc.c "Я провожу вас, мне тоже пора."
    "Допив вино и почувствовав, что разговор подошёл к концу, мы вместе направляемся к выходу. Рад, что ей стало веселее."
    mc.c "Кстати, меня зовут [mc.name]. Буду рад снова увидеть вас здесь."
    show katie smile talk
    katie.c "Конечно! Я [katie.name], рада была познакомиться, [mc.name]. Спасибо, что уделил мне время."
    katie.c "Я обязательно вернусь. У тебя тут очень уютно. Расскажу девочкам — как-нибудь придём сюда все вместе."
    mc.c "Рад слышать, буду ждать."
    scene black with fade
    "Мы выходим и расходится каждый своей дорогой, улыбаясь и махая друг другу на прощание."
    "Надеюсь, мы ещё увидимся."

    if(not fromGallery):
        $ katie.addLike(1)

    return

label katieLikeEvent1(fromGallery):
    $ location_town.showBackground()
    "По дороге домой я иду через город и замечаю впереди знакомое лицо."
    show katie neutral with dissolve
    call playMusic(chillTheme) from _call_playMusic_141
    "Это [katie.name], кажется, она несёт домой пакет с продуктами."
    "Было бы здорово поздороваться. Мне кажется, мы поладили, когда познакомились в баре. Я ускоряю шаг, чтобы догнать её."
    "Я почти догоняю её и замечаю, что пакет вот-вот порвётся."
    "Покупки высыпаются на тротуар, продукты и упаковки разлетаются по сторонам."
    show katie mad talk
    katie.c "Ох, ну вот!"
    "Она пытается остановить покупки, чтобы те не укатились далеко, но некоторые уже вне досягаемости."
    mc.c "[katie.name]! Давай помогу."
    "Я останавливаю пару предметов и наклоняюсь, чтобы помочь."
    show katie surprise
    katie.c "О, [mc.name]! Спасибо! Наверное, я слишком много туда положила..."
    mc.c "Удачно я подоспел, да? Как раз собирался тебя догнать, когда увидел, что пакет порвался. Вот, у меня есть другой."
    show katie smile talk
    katie.c "Спасибо, милый. Ты мой герой."
    show katie smile
    "Мы несколько минут собираем покупки."
    mc.c "Возвращаешься с работы?"
    show katie neutral talk
    katie.c "Ага, обычно захожу в тот магазин за продуктами. А ты? Уже закончил в баре на сегодня?"
    mc.c "Да, моя смена закончилась. Остальным оставил бар до конца дня, а сам иду домой."
    "Мы немного проходим и доходим до перекрёстка."
    show katie smile
    katie.c "Мы в одну сторону?"
    mc.c "Похоже на то. Не возражаешь, если я пройдусь с тобой?"
    show katie smile talk 2
    katie.c "Вовсе нет."
    scene black with fade
    "Мы немного болтаем о том, как прошёл день."
    $ location_town.showBackground()
    show katie neutral talk
    katie.c "Помнишь Ребекку, о которой я рассказывала в тот вечер? Подругу, которая познакомила меня с тем неудачным кавалером, от которого ты меня спас?"
    katie.c "В конце концов она извинилась. Она и сама ничего о нём не знала. Обычная история про друга друга друга."
    mc.c "Тогда следующая попытка? Есть кто-нибудь на примете?"
    call playMusic(heartTheme) from _call_playMusic_142
    show katie sad talk
    katie.c "Хм, нет. Не знаю, стоит ли продолжать. Последние двое ничем не лучше, даже если хотя бы пришли."
    katie.c "Начинаю сомневаться, что оно того стоит..."
    "Бедняжке тяжело. Не понимаю почему: со мной она была очень милой. И, по-моему, она симпатичная."
    katie.c "Среди одиноких мужчин не так много тех, кому интересны женщины моего возраста. Я уже не юная и не стройная."
    show katie sad
    "Она немного полновата, но, на мой взгляд, это ей идёт. Такая уютная, мягкая и пушистая."
    mc.c "Глупости, ты выглядишь очень молодо. Я бы не дал тебе больше двадцати!"
    show katie sad talk
    katie.c "Не смеши меня. Я знаю, что я неприметная и толстая. Видел бы ты девушек с моей работы. Часами торчат в спортзале, лица в макияже... Все взгляды на них."
    show katie sad
    "Нельзя позволить ей так себя принижать."
    mc.c "Думаю, тебе просто не везло. Многие мужчины были бы рады встречаться с такой женщиной, как ты."
    show katie sad talk
    katie.c "Все так говорят, но в жизни всё иначе."
    show katie sad
    mc.c "Послушай, мне понравился тот вечер в баре. Я отлично провёл время."
    show katie neutral talk
    katie.c "Ты просто был хорошим хозяином."
    show katie neutral
    mc.c "Может, сначала и так, но потом мне понравилось с тобой общаться."
    mc.c "Если ты не против, может, как-нибудь повторим? Сходим на кофе или перекусим?"
    show katie surprise
    katie.c "..."
    show katie bashful talk
    katie.c "Ха-ха... Не трать время на такую старушку, как я. Уверена, у тебя полно ровесниц."
    show katie bashful
    mc.c "Какая разница? Мы не так уж далеки по возрасту. Для меня это ничего не значит. Просто мне показалось, что нам было хорошо вместе. Я бы хотел повторить."
    mc.c "Конечно, только если ты сама этого хочешь. Никакого давления."
    show katie neutral talk
    katie.c "Ты... просто шутишь..."
    show katie neutral
    mc.c "Я серьёзно. Ну же, я бы не стал так играть с женщиной. Тебе и так пришлось нелегко, я понимаю, каково это."
    katie.c "..."
    show katie bashful talk
    katie.c "Это... очень мило с твоей стороны."
    katie.c "Если ты говоришь правду... я не отказываюсь, но дай мне немного подумать. После прошлого раза я решила вообще взять перерыв от свиданий."
    show katie bashful
    mc.c "Конечно, без проблем. Просто знай, что предложение остаётся в силе."
    show katie smile talk
    katie.c "Спасибо, [mc.name]. Может, ты просто так говоришь, но всё равно мне приятно."
    show katie smile
    "Мы доходим до развилки и расходимся в разные стороны."
    show katie smile talk 2
    katie.c "Мне сюда. И ещё раз спасибо за помощь."
    show katie smile
    mc.c "Ладно, доброй ночи, [katie.name]. Буду ждать новостей."
    hide katie with dissolve
    "Мы слегка машем друг другу на прощание."
    "Надеюсь, она серьёзно отнесётся к моему приглашению. Или я слишком многого о себе возомнил? Может, некоторые антро предвзято относятся к людям."
    "Не буду настаивать. Надеюсь, мы ещё будем время от времени встречаться."

    if(not fromGallery):
        $ katie.addLike(1)
        $ katie.addLove(1)

    return

label katieLikeEvent2(fromGallery):
    $ location_park.showBackground()
    call playMusic(heartTheme) from _call_playMusic_143
    "[katie.name] написала и предложила встретиться."
    "Когда мы расстались, я почти пригласил её на свидание — она как раз собиралась отказаться от знакомств после нескольких неудачных попыток."
    "Возможно, она решила, что я шучу. Она так разочарована неудачами в любви, что могла потерять уверенность в себе."
    "Я бы никогда не стал так с ней поступать. Она искренняя и замечательная, и я правда хотел позвать её на свидание."
    show katie smile talk with dissolve
    katie.c "Привет, [mc.name]! Надеюсь, ты недолго ждал?"
    mc.c "Вовсе нет. Рад тебя видеть, [katie.name]. Спасибо, что позвала."
    katie.c "Да, спасибо, что пришёл. Прости, я немного странно себя веду."
    mc.c "Странно?"
    show katie bashful talk
    katie.c "Да, из-за того, как мы закончили тот разговор... Ты пригласил меня на свидание, а я отмахнулась."
    katie.c "Я всё об этом думала. Не сразу поняла, что ты имел в виду. Ты и правда приглашал меня на свидание, да?"
    show katie bashful
    mc.c "Именно. Может, я слишком ходил вокруг да около или застал тебя в неподходящий момент. Прости."
    show katie neutral talk
    katie.c "Нет, это ты меня прости. Я не восприняла твои слова всерьёз."
    katie.c "Думала, ты просто хотел меня подбодрить. При встрече я только и делаю, что жалуюсь на свою личную жизнь."
    show katie bashful talk
    katie.c "...и ещё кое-что. Я ведь для тебя старовата, да? Мне [katie.age], если ты не знал."
    show katie bashful
    mc.c "Нисколько. Не будь к себе так строга. Меня это совсем не смущает."
    show katie bashful talk
    katie.c "Ну и... антро и люди... Я не была уверена, что тебе это интересно. И у меня никогда не было... ну, ты понимаешь. Ты говорил, что раньше почти не общался с нами."
    show katie bashful
    mc.c "То же самое. Меня это нисколько не смущает."
    "Наверное, лучше не говорить, что это одна из главных причин, почему мне интересно..."
    show katie neutral talk
    katie.c "Понимаю..."
    katie.c "Ну, если ты уве..."
    mc.c "Абсолютно."
    show katie surprise
    pause
    show katie smile talk
    katie.c "...Тогда я с удовольствием схожу с тобой на свидание. Спасибо, что дал мне время подумать."
    mc.c "Как насчёт прямо сейчас?"
    show katie tease talk
    katie.c "Правда? Конечно, я свободна."
    scene black with fade
    call stopMusic from _call_stopMusic_26
    pause
    scene diner with fade
    show katie smile
    call playMusic(chillTheme) from _call_playMusic_144
    "Я отвёл [katie.name] в ресторан в городе, где бывал пару раз. Ей понравилась идея: это одно из её любимых мест."
    "Мы поговорили о своей жизни: школе, работе, увлечениях."
    "Она старше, так что ей есть что рассказать, и это интересно."
    "Мы немного затронули прошлые отношения. Я не хотел задерживаться на этой теме, чтобы не расстраивать её, но на этот раз она не унывает."
    "Надеюсь, дело в приятной компании."
    "За столом она держится изящно и вежливо. Кажется, она очень старается соблюдать все правила этикета."
    "Это контрастирует с количеством еды, которую она заказала. Она явно любит поесть — и это хорошо, — но, кажется, немного стесняется."
    "На самом деле это очень мило."
    "Свидание проходит прекрасно, и мы доедаем."
    show katie smile talk 2
    katie.c "Очень вкусно. Надоело всё время готовить дома. А тебе понравилось?"
    mc.c "Мне тоже, как всегда. Кажется, я бывал здесь чаще, чем где-либо ещё с тех пор, как переехал."
    katie.c "Тут много хороших мест, тебе стоит попробовать и другие. Подкину пару рекомендаций."
    show katie smile
    "Официант кладёт на стол счёт."
    mc.c "Позволь мне."
    show katie smile talk
    katie.c "Можем разделить счёт."
    mc.c "Я угощаю, всё-таки это я тебя пригласил."
    katie.c "Не буду спорить, знаю вас, мужчин. Но в следующий раз плачу я."
    show katie smile
    "В следующий раз? Отлично!"
    mc.c "Тогда буду ждать следующего раза."
    show katie bashful
    pause
    scene black with fade
    "Расплатившись, мы продолжаем разговор и направляемся домой."
    $ location_town.showBackground()
    show katie smile
    mc.c "Кажется, здесь наши пути расходятся. Я прекрасно провёл время."
    show katie smile talk
    katie.c "Я тоже. Спасибо за сегодняшний день."
    "[katie.name] раскрывает объятия, приглашая меня."
    hide katie with dissolve
    show katie hug with dissolve
    "Мы ненадолго обнимаемся. Я вдыхаю тонкий, соблазнительный аромат её духов."
    "Когда мы прижимаемся друг к другу, её шерсть слегка касается моей щеки. За её плечом мягко покачивается большой пушистый хвост."
    "Её пушистая фигура дарит мне такое мягкое тепло, что отстраняться совсем не хочется."
    hide katie with dissolve
    show katie smile with dissolve
    "Мы улыбаемся друг другу."
    mc.c "Увидимся снова?"
    show katie tease talk
    katie.c "С удовольствием."
    hide katie with dissolve
    "Мы машем на прощание и расходимся, оба сияя от счастья."
    "Всё прошло замечательно."

    if(not fromGallery):
        $ katie.addLike(1)
        $ katie.addLove(1)
        $ katie.isDateable = True
        "Теперь можно приглашать [katie.name] на свидания."

    return

label katieHEvent1(fromGallery):
    $ location_cafe.showBackground()
    "Кажется, у нас с [katie.name] всё складывается отлично."
    "Мы уже несколько раз встречались, и граница между дружеской встречей и свиданием постепенно размывается. Это не были свидания вслепую или знакомства, устроенные кем-то, к которым она привыкла в последнее время."
    "Мы уже поладили и решили сделать следующий шаг. Но я отношусь к этому серьёзно и не хочу торопить события."
    show katie tease with dissolve
    call playMusic(heartTheme) from _call_playMusic_145
    "Мы встретились в кафе, одном из её любимых, выпить кофе и съесть пирожное."
    "Разговор шёл легко. Мы уже прошли этап вопросов для знакомства и воспоминаний о прошлом и теперь просто дружески рассказывали о повседневной жизни."
    show katie smile talk 2
    katie.c "Боже, датская выпечка здесь просто объедение. Хорошо, что кафе рядом с работой — опасное место."
    "[katie.name] смотрит на тарелку, а потом на прилавок с выставленными пирожными."
    show katie sad talk
    katie.c "Эх... Опять испортила диету..."
    mc.c "О чём ты? Тебе совершенно не о чем волноваться."
    katie.c "Нет, мне правда надо следить за собой. Я стараюсь, честное слово. Но всё время что-то мешает, и вот уже несколько недель я питаюсь как попало."
    katie.c "Мне просто не хватает силы воли. Это так трудно."
    show katie sad
    "[katie.name] часто рассказывает о своей неуверенности. Она переживает из-за веса и того, как люди на неё смотрят."
    "Ещё из-за возраста — точнее, из-за нашей разницы, которая довольно велика. Она постоянно спрашивает что-то вроде: «Зачем ты проводишь время со старушкой вроде меня?»"
    "Думаю, неудачи на свиданиях за эти годы всё ещё её расстраивают, но я очень хочу изменить её отношение к себе."
    mc.c "Жизнь слишком коротка, чтобы переживать из-за такого. Наслаждайся и делай, что хочется."
    show katie smile talk
    katie.c "Послушай-ка, заговорил как старый дед. *Хм-хм*"
    show katie bashful talk
    katie.c "Но вообще... Мне правда надо бы стараться сильнее. Наверное, из-за этого мужчины мной и не интересуются..."
    show katie thinking
    pause
    show katie bashful talk
    "Она осекается. Кажется, она связывает многие неудачи в личной жизни со своей внешностью."
    "Не хочу давить на неё, но мне неприятно слышать, как она себя принижает."
    mc.c "По-моему, ты прекрасна такой, какая есть."
    show katie sad talk
    katie.c "Лисы должны быть стройными и грациозными. Я совсем не такая."
    show katie sad
    "Я только улыбаюсь [katie.name] в духе «ну ты и...» Она и так знает, что я не верю ни одному её слову."
    show katie bashful talk
    katie.c "Но... спасибо. Приятно слышать такое, даже если я сама в это не верю..."
    show katie bashful
    mc.c "Поверь мне, сестрёнка."
    show katie tease talk
    katie.c "Ну ты и глупый."
    show katie tease
    mc.c "Проводить вас до дома, юная леди?"
    show katie tease talk
    katie.c "Благодарю, э-э, старичок."
    show katie tease
    "Мы тихонько посмеиваемся и уходим."
    scene black with fade
    pause
    $ location_town.showBackground()
    "Когда мы подходим к перекрёстку, я собираюсь обнять её на прощание, но [katie.name] заговаривает первой."
    show katie smile talk 2 with dissolve
    katie.c "А-вообще-то, я хотела спросить, не зайдёшь ли ты ко мне? Недавно купила хороший чай и давно хотела угостить. Если хочешь."
    "[katie.name] впервые приглашает меня к себе. Я давно этого ждал."
    mc.c "С удовольствием! Веди."
    show katie joy
    katie.c "Отлично!"
    scene black with fade
    "Немного прогулявшись..."
    scene katielivingroom with fade
    "Мы приходим к [katie.name] домой. Это уютный дом в хорошем районе, со вкусом обставленный и безупречно чистый."
    "Она ведёт меня в гостиную, а сама идёт на кухню поставить чайник."
    "Мы немного говорим о доме, а потом она приносит две чашки и садится рядом на диван."
    show katie smile talk with dissolve
    katie.c "Подруга подарила мне этот чай, но я ещё не успела его попробовать. Самое время, да?"
    show katie tease
    "Мне подают ароматный травяной чай. Я не большой любитель чая, но не собирался отказываться от приглашения [katie.name]."
    "Мы ещё немного беседуем за чаем, а потом она проводит меня по дому."
    "Через некоторое время разговор начинает затихать. Сегодня мы провели вместе много времени, но после прогулки домой возникло несколько неловких моментов."
    "Собственно, после того, как она пригласила меня..."
    "[katie.name] сидит рядом на диване, почти касаясь меня плечом. Напряжение в комнате растёт. На мгновение наши взгляды встречаются."
    "Не говоря ни слова, мы медленно наклоняемся друг к другу."
    hide katie with dissolve
    show katie kiss with dissolve
    pause
    "Время замирает. Мы осторожно касаемся губами в лёгком поцелуе, не размыкая губ, и наслаждаемся моментом."
    "Она напряжённо закрывает глаза, словно не уверена, чем всё закончится, а я не могу отвести взгляд от её прекрасного лица."
    "Это могли быть секунды или минуты — время будто остановилось."
    hide katie with dissolve
    show katie bashful with dissolve
    pause
    "[katie.name] с улыбкой отстраняется, но тут же краснеет и отводит взгляд."
    "Я кладу руку поверх её ладони, и она сразу сжимает её в ответ."
    katie.c "Я ведь не перешла черту?"
    mc.c "Почему ты так думаешь?"
    katie.c "Не знаю... Просто давно ничего подобного не было, и я не уверена..."
    "К счастью, она не жалеет о поцелуе, а лишь сомневается, хотел ли я этого. Представьте себе."
    "Я не нахожу слов, поэтому кладу ладонь ей на мордочку и снова притягиваю к себе."
    hide katie with dissolve
    show katie kiss with dissolve
    "На этот раз мы целуемся страстнее. Шеи изгибаются, сердца колотятся, поцелуй становится настойчивее."
    "Я притягиваю [katie.name] ближе, обхватываю за талию, и мы исследуем рты друг друга."
    "Ощущения совершенно новые. Форма её мордочки дарит непривычные чувства. Странно, что её глаза так далеко, но я определённо могу к этому привыкнуть."
    katie.c "М-м-м."
    hide katie with dissolve
    show katie hug with dissolve
    "Мы немного отстраняемся, но всё ещё остаёмся в объятиях друг друга."
    katie.c "Я..."
    katie.c "Не знаю, что сказать."
    mc.c "Я кое-что придумал."
    katie.c "Ч-что?"
    mc.c "Ты прекрасна."
    katie.c "Ну перестань..."
    "Барьер между нами исчез. Я рад, что [katie.name] чувствует то же самое."
    mc.c "Мне очень нравится проводить с тобой время. Теперь ты веришь, что я отношусь к нашим отношениям серьёзно?"
    katie.c "Ха-ха, да, теперь я тебе верю. Хотя всё равно не могу поверить, что это происходит."
    "Я вспоминаю свою фразу «Поверь мне, сестрёнка», но не хочу портить момент. Просто улыбаюсь ей."
    katie.c "Посмотри на нас — ведём себя как дети."
    mc.c "Я не жалуюсь."
    "Мы оба смеёмся, и [katie.name] откидывается назад."
    hide katie with dissolve
    show katie tease with dissolve
    katie.c "Дай мне минутку. Я весь день в этой одежде, хочу переодеться во что-нибудь поудобнее, если ты не против."
    mc.c "Конечно."
    hide katie with dissolve
    "[katie.name] идёт по коридору, хвост покачивается за ней. Я на седьмом небе от того, как прошёл день. Интересно, как далеко мы зайдём."
    "Через пару минут [katie.name] возвращается в более удобной домашней одежде — майке и шортах. Не удивляюсь, что ей захотелось снять длинное платье."
    "Садясь рядом, она соблазнительно кладёт ладонь мне на грудь."
    image katie blowjob start = Image("images/characters/katie/hscenes/blowjob/start.webp")
    scene katie blowjob start with fade
    katie.c "[mc.name], ты был таким джентльменом, несмотря на свой возраст. Спасибо, что проявил терпение."
    katie.c "Я знаю, что часто себя принижаю, но после нашей встречи ты так сильно изменил мою жизнь к лучшему."
    katie.c "Надеюсь, мы продолжим наши отношения, если ты не против."
    mc.c "Я ни за что не хотел бы иначе, [katie.name]."
    katie.c "В таком случае мы вели себя как дети, но теперь..."
    katie.c "Ну, я знаю, что жаловалась на диету, но мне хочется попробовать кое-что ещё."
    "А? Перекусить чем-нибудь к чаю?"
    scene black with fade
    call playMusic(sexyTheme) from _call_playMusic_146
    "О-ох..."
    "[katie.name] ласкает мой пах, где, стыдно признаться, член уже наполовину стоял с самого поцелуя."
    "Она медленно расстёгивает ширинку. Поняв намёк, я помогаю ей стянуть с меня штаны."
    "Она наклоняется, её губы приближаются к моей головке..."
    window hide
    image katie blowjob part 1 = Movie(play="images/characters/katie/hscenes/blowjob/part1.webm")
    show katie blowjob part 1 with fade
    pause
    "Боже, какие невероятные ощущения."
    "Удлинённая мордочка [katie.name] обхватывает мой член, и она страстно двигает головой вверх-вниз."
    katie.c "М-м-м-м, хр-р-р..."
    "[katie.name] тихонько мычит, принимая в рот значительную часть моего члена. Её шерсть и волосы скользят по коже, и по позвоночнику пробегает электрический разряд."
    mc.c "А-а, о-о..."
    "Я не могу сдержать стоны наслаждения. Такого я ещё не испытывал. Подушечки лап [katie.name] рисуют маленькие круги у меня на бедре."
    "Я не могу удержаться и тянусь к её мягкой попке, сжимаю её руками и, конечно, пушистый хвост."
    "[katie.name] вздрагивает от моих прикосновений, но не останавливается."
    window hide
    pause
    image katie blowjob part 2 = Movie(play="images/characters/katie/hscenes/blowjob/part2.webm")
    show katie blowjob part 2 with fade
    pause
    "Не прерываясь ни на миг, [katie.name] ускоряется, двигая головой вверх-вниз. Влажные шлепки разносятся по комнате."
    "Она кладёт руку к основанию моего члена и нежно обхватывает пальцами яички. Я никогда не привыкну к этим лапкам."
    katie.c "*Гвак* *Гвак* *Ах*"
    "[katie.name] обводит языком мой член, а головка касается задней стенки её горла."
    "Можно было бы пошутить, что она умеет хорошо «есть», но я не стану портить момент дешёвой шуткой."
    "Ощущения такие сильные, что долго я не продержусь."
    katie.c "М-м-м, фр-м-м..."
    "Не знаю, пытается ли она что-то сказать, и интересно, как долго она сможет продолжать. Хотя это уже не важно, я почти..."
    mc.c "Я сейчас..."
    katie.c "М-м!"
    "Она наверняка услышала, но [katie.name] начинает двигать головой быстрее и глубже. Похоже, останавливаться она не собирается."
    "Я крепко хватаю её за пышную грудь и..."
    window hide
    pause
    image katie blowjob end = Image("images/characters/katie/hscenes/blowjob/end.webp")
    scene katie blowjob end with fadewhite
    pause
    katie.c "Мр-р-р-пф-ф-ф!"
    "Я изливаю ей в горло, кажется, самую большую порцию спермы в жизни."
    "Она не отстраняется, а лишь хватает воздух носом, медленно поднимаясь с моего дрожащего члена."
    "Раздаётся тихий хлопок, когда её губы соскальзывают с головки. Мы оба тяжело дышим, и в комнате воцаряется тишина."
    scene katielivingroom with fade
    pause
    "Мы оба откидываемся на диван и тяжело дышим, как собаки на солнцепёке."
    call playMusic(heartTheme) from _call_playMusic_147
    show katie hug with dissolve
    mc.c "Это было *ах* невероятно."
    katie.c "*Ах* *Ах* Похоже, *ах* тебе понравилось."
    "[katie.name] бросает на меня самодовольный взгляд."
    "Мы смотрим друг другу в глаза, переводя дыхание, и ещё несколько минут нежно ласкаем друг друга."
    mc.c "Тебе не обязательно было это делать."
    katie.c "О, я сама хотела, поверь."
    katie.c "Уже поздно..."
    mc.c "Наверное, мне пора... Если только..."
    katie.c "Не переживай, я не ждала, что ты останешься. Но, может быть, в другой раз? Пожалуйста?"
    mc.c "Тебе будет трудно заставить меня отказаться."
    "Мы тихонько смеёмся."
    hide katie with dissolve
    "Я собираю одежду, а она провожает меня к двери."
    "Я машинально наклоняюсь, чтобы поцеловать её, но [katie.name] слегка отстраняется."
    katie.c "Не думаю, что ты захочешь меня поцеловать..."
    mc.c "Мне приходится изо всех сил сдерживаться, чтобы не наброситься на тебя, но..."
    katie.c "Хи-хи. Береги себя, [mc.name]."
    mc.c "До скорого."
    scene black with fade
    "Вот такая у нас была чайная вечеринка."

    if(not fromGallery):
        $ katie.addLove(1)

    return

label katieHEvent2(fromGallery):
    $ location_bar.showBackground()
    "Я встретился с [katie.name] в баре. На этот раз я не работаю, а пришёл как на настоящее свидание."
    "Мы уже некоторое время встречаемся — сначала узнавали друг друга поближе, а теперь видимся как друзья."
    "Флирт, редкие прикосновения, задушевные разговоры и лёгкие беседы... Я всё ещё не понимаю, кто мы друг другу."
    "Постепенно она избавляется от неуверенности в себе, но сомнения всё ещё проскальзывают — и в ней самой, и в наших отношениях."
    show katie thinking with dissolve
    "На работе у неё выдалась тяжёлая неделя, и ей нужно выговориться. Я могу выслушать. Иногда просто необходимо выпустить пар."
    "...Выпустить."
    call playMusic(funnyTheme) from _call_playMusic_148
    "Я замечаю, что украдкой поглядываю на неё. У неё... очень пышная грудь. Надеюсь, я достаточно незаметен. Но сегодня мне трудно отвести взгляд..."
    katie.c "Эх... Так утомительно. Неделя за неделей. Когда же они научатся?"
    katie.c "В последнее время я всё чаще думаю: «Хочу выпить»."
    show katie smile talk
    katie.c "Хорошо, что ты рядом, да? *Хм-хм*"
    show katie smile
    pause
    mc.c "...Ну да, я здесь, моя леди. Сколько вина захотите."
    "Ой, я немного отключился. Они слегка покачиваются, пока она говорит... На это легко засмотреться."
    "Она ведь не заметила?"
    show katie smile talk 2
    katie.c "Только не поощряй меня... А то я буду приходить сюда каждый вечер. Ты знаешь, сколько калорий в бокале красного? Мне правда надо пить меньше."
    show katie smile
    mc.c "Надеюсь, только не сегодня! Думаю, ты заслужила бокальчик после такого дня."
    show katie smile talk 2
    katie.c "Меня можно уговорить."
    show katie smile
    scene black with fade
    "Сегодня [katie.name] расслабляется, отдыхает и веселится, осушая несколько бокалов."
    "Так приятно видеть её улыбающейся."
    "Вечер складывается хорошо."
    "Но я хозяин заведения, и нас постоянно прерывают."
    $ location_bar.showBackground()
    show katie thinking with dissolve
    unknown "Эй, [mc.name], кажется, у нас закончились чистые {b}кувшины{/b}."
    mc.c "Кувшины?"
    unknown "Ну, знаешь, те самые {b}большие кувшины{/b}?"
    mc.c "Кувшины? Они должны быть..."
    scene black with fade
    "И всё продолжает..."
    $ location_bar.showBackground()
    show katie smile with dissolve
    unknown2 "А-а, [mc.name], где те красивые рюмки?"
    unknown "Не отвлекай [mc.name], идиот! Они на той {b}полке{/b}."
    unknown "Знаешь, рядом с {b}банками{/b}."
    scene black with fade
    "...напоминать мне..."
    $ location_bar.showBackground()
    show katie tease with dissolve
    unknown "Кажется, {b}молоточки{/b} на входной двери расшатались."
    mc.c "Кто вообще ими пользуется? Двери и так открыты."
    mc.c "*Вздыхает* Ладно, посмотрю на них завтра..."
    scene black with fade
    "...об этих чёртовых..."
    $ location_bar.showBackground()
    show katie thinking with dissolve
    unknown2 "Эй, босс, я принёс фрукты для коктейлей. Куда положить {b}дыни{/b}? Они слишком большие для холодильника."
    "Дыни? Серьёзно? С каких пор мы добавляем чёртовы дыни в коктейли? Это уже смешно."
    mc.c "Просто оставь их на столе, в холодильник класть не надо."
    scene black with fade
    "...БОЛЬШИХ СИСЬКАХ!"
    $ location_bar.showBackground()
    show katie smile with dissolve
    "Сегодня я совсем не могу сосредоточиться. Не могу выбросить их из головы."
    "Если она заметила, то наверняка считает меня настоящим хамом."
    "Раньше она считала меня таким джентльменом."
    show katie smile talk 2
    katie.c "Ничего себе, я сегодня выпила больше обычного... Пожалуй, хватит."
    show katie tease with dissolve
    "Она слегка наклоняется вперёд, и её грудь мягко прижимается к краю стола."
    "Я снова на неё засматриваюсь. Она вообще когда-нибудь НЕ в поле моего зрения?"
    "...Она точно заметила. Просто слишком вежлива, чтобы сказать. Наверное, я заставил её чувствовать себя неловко. Всё испортил?"
    mc.c "Ха-ха, я тоже. Пора заканчивать вечер?"
    "Мне тоже пора остановиться, пока я не свёл себя с ума."
    mc.c "Давай провожу тебя домой, не хочу, чтобы ты шаталась одна."
    katie.c "Спасибо, милый. Веди!"
    scene black with fade
    "Немного прогулявшись в прохладном вечернем воздухе..."
    $ location_town.showBackground()
    "Мы почти дошли до места, где разошлись бы, если бы я не провожал её."
    "Но [katie.name] мягко тянет меня за рукав."
    show katie smile talk with dissolve
    katie.c "Слушай... Можно я ненадолго зайду к тебе? Например, выпить кофе?"
    katie.c "Немного протрезветь."
    mc.c "Конечно, даже спрашивать не нужно. Можем посмотреть то шоу, о котором ты столько рассказывала."
    show katie tease
    katie.c "Угу."
    scene black with fade
    "Мы направляемся ко мне, держась за руки."
    "Подвыпившая [katie.name] трогательно прижимается ко мне."
    $ location_home.showBackground()
    "Мы приходим ко мне. [katie.name] плюхается на диван."
    "...и грудь подпрыгивает... Боже..."
    "Я иду на кухню."
    mc.c "Кофе? Или, может, чай?"
    call playMusic(chillTheme) from _call_playMusic_149
    katie.c "Хм, нет."
    "А?"
    mc.c "Я оборачиваюсь. По её лицу всё понятно..."
    show katie tease with dissolve
    katie.c "Я пришла не за чаем..."
    katie.c "Кажется, весь день ты думал совсем о другом~"
    "О боже, как бы я ни старался вести себя незаметно, всё было очевидно. Может, притвориться, что не понимаю?"
    mc.c "Э-э, кхм, о чём ты?"
    "[katie.name] встаёт и покачиваясь подходит ко мне."
    hide katie with dissolve
    show katie hug with dissolve
    katie.c "Милый, не притворяйся. Весь вечер украдкой на меня поглядывал."
    katie.c "Хотя «украдкой» — не совсем подходящее слово."
    "[katie.name] с озорной улыбкой прижимает грудь к моей груди."
    mc.c "Э-э... Правда? Я... не уверен."
    katie.c "Я приму это за комплимент, раз уж ты так смотришь~"
    "Меня раскрыли. Жалкое зрелище."
    hide katie with dissolve
    show katie kiss with dissolve
    hide katie with dissolve
    show katie tease talk with dissolve
    katie.c "Скажем так, это одно из... преимуществ... пышной фигуры."
    mc.c "Ты не..."
    show katie mad
    katie.c "Я уже говорила: перестань нести эту чушь."
    show katie tease talk
    katie.c "Я принимаю себя... И ты ясно дал понять, что тебя это не смущает."
    katie.c "Так что... Садись..."
    scene black with fade
    call playMusic(sexyTheme) from _call_playMusic_150
    "[katie.name] берёт меня за руку и ведёт к краю кровати, сама вставая передо мной."
    katie.c "На этот раз рассмотри меня как следует."
    "[katie.name] грациозно начинает раздеваться. Длинное платье падает на пол, обнажая бельё, едва сдерживающее её пышные формы."
    "От одного этого вида я уже возбуждаюсь, но она ещё не закончила."
    "Она наклоняется, стягивает бельё и расстёгивает бюстгальтер, открывая мне грудь..."
    image katie boobjob start = Image("images/characters/katie/hscenes/boobjob/start.webp")
    scene katie boobjob start with fade
    pause
    "Чудесное зрелище. Пышные изгибы её тела."
    "Элегантные длинные волосы. Шерсть слегка переливается на свету."
    "Мягко покачивается пушистый хвост."
    "И эта огромная грудь... с неожиданно розовыми сосками."
    katie.c "Вот я вся. Ну, разглядывай."
    mc.c "Ты прекрасна."
    "[katie.name] краснеет от этих слов. Она выпила, но всё равно явно смущена."
    katie.c "...Спасибо."
    "Похоже, это ещё не всё, чего она хотела, поэтому я тоже начинаю раздеваться, снимая рубашку."
    katie.c "Ты тоже ничего, милый."
    "Я протягиваю руку, собираясь притянуть её для поцелуя у кровати."
    "[katie.name] берёт меня за руку и подходит ближе, но вместо этого опускается на колени между моих ног, подставляя мне прекрасную грудь."
    katie.c "Всё ещё будешь отрицать, что весь день думал о ней?"
    mc.c "Кажется, меня уже не разоблачить сильнее."
    image katie boobjob part 1 = Movie(play="images/characters/katie/hscenes/boobjob/part1.webm")
    show katie boobjob part 1 with fade
    pause
    "[katie.name] обхватывает грудь и кладёт её мне на бёдра, зажимая между грудями мой член."
    "Член почти полностью исчезает между ними. Они невероятно мягкие, обхватывают ствол и щекочут головку, скользя вверх-вниз."
    katie.c "Я подумала, тебе понравится."
    mc.c "Ты угадала..."
    "Тепло окутывает меня, а невероятно развратное зрелище заставляет возбуждение нарастать."
    "Она пристально смотрит мне в глаза — в них глубокое желание и невинное смущение."
    katie.c "Тебе хорошо, милый?"
    "Она словно дразнит меня словами. Обычно она так и говорит, но сейчас это напоминает игру в мамочку."
    "Не решаюсь ничего сказать, но чёрт, как же это заводит."
    mc.c "Боже, это невероятно, [katie.name]."
    katie.c "Позволь дать тебе то, чего ты так хотел~"
    pause
    "Её грудь уже влажная от моего предэякулята, и ощущения могут довести меня до оргазма в любой момент."
    "Но [katie.name] не может двигаться быстрее, наверное, она устанет."
    "Голова кружится, пора взять всё в свои руки."
    mc.c "Хочу ещё, но... ложись на кровать."
    image katie boobjob part 2 = Movie(play="images/characters/katie/hscenes/boobjob/part2.webm")
    show katie boobjob part 2 with fade
    pause
    "Я разворачиваю её и нависаю сверху."
    katie.c "Ох, боже!"
    "Я беру инициативу, опускаюсь на её туловище и снова зажимаю член между грудями, сжимая мягкую пушистую плоть."
    "Я быстро двигаюсь, трахая её грудь и сжимая член по бокам."
    "Каждый толчок пробегает по телу разрядом, головка члена покалывает от возбуждения."
    mc.c "А-а, прости, [katie.name], так хорошо."
    katie.c "Мой сильный мужчина... Продолжай... Пользуйся моей грудью сколько хочешь."
    "Она точно знает, что её слова в постели заводят меня. Милая, женственная [katie.name] говорит такие непристойности..."
    pause
    image katie boobjob part 3 = Movie(play="images/characters/katie/hscenes/boobjob/part3.webm")
    show katie boobjob part 3 with fade
    pause
    "Я ускоряюсь настолько, насколько могу."
    "Я весь в поту и быстро двигаюсь между её большой подпрыгивающей грудью."
    "Я чувствую, как бьётся её сердце, и мы оба тяжело дышим."
    mc.c "*Ах* *Ах*"
    katie.c "*Ах* *А-а*, да~"
    "Я больше не могу сдерживаться."
    mc.c "Куда мне..."
    katie.c "Давай, кончай для меня, [mc.name]~"
    katie.c "На меня~"
    "Эти слова словно переключают что-то в моей голове."
    mc.c "Я сейчас~!"
    mc.c "А-а-а-а!"
    image katie boobjob end = Image("images/characters/katie/hscenes/boobjob/end.webp")
    scene katie boobjob end with fadewhite
    pause
    "Я мощно кончаю, двигаясь между её прекрасных грудей."
    "Сперма разлетается по её груди и попадает даже на лицо, портя её прежде изящный вид."
    "Сперма покрывает её грудь и стекает в ложбинку, пока она тяжело дышит."
    "Я не могу оторвать руки от этих прекрасных грудей."
    katie.c "О-ох~ *Ах* Ничего себе~"
    katie.c "*Ах* *Ах*. Тебе *ах* понравилось?"
    mc.c "*Ах* А как ты *ах* думаешь..."
    "Мы некоторое время смотрим друг другу в глаза, постепенно приходя в себя после головокружительного наслаждения."
    katie.c "Можно?.."
    "[katie.name], кажется, немного смущает, сколько спермы попало на её шерсть."
    mc.c "О, да, прости."
    scene black with fade
    "Я слезаю с неё и ложусь на кровать, всё ещё переводя дыхание."
    "[katie.name] идёт в ванную, чтобы вытереться."
    "Вскоре [katie.name] возвращается и прижимается ко мне на кровати."
    scene katiepillowtalk with fade
    mc.c "Это было невероятно."
    katie.c "Я рада."
    katie.c "Сегодня всё было для тебя. Но в следующий раз... Я тоже захочу немного ласки."
    mc.c "Можешь получить всё, что захочешь."
    katie.c "Я запомню."
    "Мы некоторое время обнимаемся на кровати."
    "Одевшись, я провожаю [katie.name] домой и целую на прощание."

    if(not fromGallery):
        $ katie.addLove(1)

    return

label katieHEvent3(fromGallery):
    scene diner with fade
    call playMusic(chillTheme) from _call_playMusic_151
    "Свидание с [katie.name]."
    "В последнее время она очень занята на работе и предложила поужинать вне дома, чтобы не возиться с готовкой, уборкой и прочим."
    "Я с радостью согласился. С ней всегда приятно, даже если большую часть времени..."
    show katie thinking with dissolve
    katie.c "Я так рада, что эта неделя закончилась... Там сейчас полный хаос."
    show katie sad
    katie.c "Не заставляй меня возвращаться туда на следующей неделе... Фу..."
    "...она жалуется на работу."
    "Я понимаю. Иногда нужно выговориться. Похоже, там не слишком одобряют жалобы на работе."
    "Наши свидания помогают ей выпустить пар. Даже когда она ворчит, остаётся такой же чудесной женщиной."
    show katie smile talk
    katie.c "Спасибо, что пригласил меня, [mc.name]. Я не хотела только и делать, что жаловаться, просто..."
    show katie smile
    mc.c "В любое время, [katie.name], серьёзно. Жалуйся сколько угодно."
    show katie smile talk
    katie.c "Эх, я уже наверняка тебе надоела. Да и самой надоело."
    show katie smile
    mc.c "Не переживай, можешь выговориться. Я тоже был бесправным сотрудником на паре прежних работ."
    mc.c "Рад, что теперь от этого избавился... Управлять заведением тоже бывает непросто, но, надеюсь, я справляюсь."
    mc.c "По крайней мере, остальные сотрудники вроде не жалуются..."
    show katie tease talk
    katie.c "Уверена, что так. Я видела, как ты работаешь. У тебя всё под контролем."
    show katie tease
    "[katie.name] наклоняется и гладит меня по руке, тепло улыбаясь."
    "Во время разговора от неё веет таким успокаивающим теплом. Почти материнским... Не то чтобы у меня был такой типаж, но мне это нравится."
    "Она всё ещё иногда думает о разнице в возрасте, но, кажется, худшее уже позади."
    "Она уже может спокойно шутить на эту тему и поддразнивать меня."
    mc.c "Спасибо, мам!"
    show katie mad
    "За это она слегка шлёпает меня по руке, которую только что так нежно гладила."
    show katie bashful
    katie.c "Да перестань ты."
    mc.c "С тобой слишком легко, [katie.name]."
    show katie tease
    katie.c "...Ну ты и шалун."
    show katie bashful talk
    katie.c "Не говори так громко. Кто-нибудь увидит нас вместе и решит, что я встречаюсь с молодым жеребцом."
    show katie bashful
    mc.c "Да ладно, [katie.name], мы не так уж далеко друг от друга. Ты говоришь, будто уже бабушка."
    show katie bashful talk
    katie.c "Ага-ага, всё ты повторяешь. Просто с вами, молодыми мужчинами..."
    show katie bashful
    mc.c "Ой, не глупи."
    "Я тянусь и тоже глажу её руку, проводя пальцами по шерсти."
    show katie smile
    "По её тёплой улыбке видно, что она просто дразнится и уже не переживает так, как прежде."
    "Бедняжка постепенно выбирается из ямы отчаяния после многих лет неудач на свиданиях. Такое кого угодно доведёт до слёз."
    "Хочу помочь ей выбраться."
    scene black with fade
    scene diner with fade
    "После вкусного ужина и пары бокалов вина — и десерта, перед которым [katie.name] не устоит..."
    show katie joy with dissolve
    katie.c "Было чудесно! Спасибо, что выбрался со мной."
    mc.c "И правда. Ты всегда отлично выбираешь места."
    mc.c "Сегодня я угощаю, [katie.name]. На этой неделе у нас в баре всё хорошо."
    "Говорю я, готовясь оплатить счёт."
    show katie smile talk 2
    katie.c "Не стану спорить, спасибо, милый."
    hide katie with dissolve
    show katie kiss with dissolve
    "Она наклоняется через стол и быстро целует меня в щёку."
    hide katie with dissolve
    show katie tease with dissolve
    "К тому же теперь она свободнее проявляет чувства на людях, и мы всё больше похожи на пару."
    "Я благоразумно не упоминаю, что её грудь едва не опрокинула бокал, когда она наклонилась."
    mc.c "Пойдём?"
    katie.c "Пожалуйста~"
    scene black with fade
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_town.showBackground()
    with fade
    call playMusic(heartTheme) from _call_playMusic_152
    "Мы идём через город."
    "Держимся за руки, ладони тёплые в прохладном вечернем воздухе."
    mc.c "Выходные ведь. Может, зайдём выпить? Бар ещё открыт."
    show katie smile talk 2 with dissolve
    katie.c "М-м, нет, если ты не против. Я выпила ровно столько, сколько хотела."
    show katie tease talk
    katie.c "Но ведь вечер не обязательно заканчивать прямо сейчас?"
    show katie tease
    mc.c "Конечно."
    "Больше ничего не нужно говорить. Мы уже привыкли заканчивать свидания у меня дома."
    "Я крепче сжимаю её руку, и мы идём домой."
    scene black with fade
    $ location_home.showBackground()
    mc.c "Хочешь чаю или кофе?"
    show katie tease with dissolve
    katie.c "..."
    "Наверное, не надо."
    hide katie with dissolve
    show katie kiss with dissolve
    "[katie.name] почти бросается мне в объятия и страстно целует."
    "Её мордочка прижимается к моей щеке, наши языки переплетаются."
    katie.c "*М-м-м*"
    "Она крепко обнимает меня, а я кладу руку ей на талию."
    hide katie with dissolve
    show katie hug with dissolve
    mc.c "Чего-то хочешь?"
    katie.c "Заставляешь девушку просить?"
    mc.c "Ты же знаешь, я бываю немного тугодумом."
    katie.c "Ох, [mc.name]..."
    katie.c "Я так тебе благодарна. Хочу, чтобы ты это знал."
    katie.c "Я не ожидала, что ты появишься в моей жизни, но ты мне был нужен, особенно тогда..."
    katie.c "Все эти неудачные свидания, мужчины, которые от меня отмахивались."
    katie.c "С тобой я чувствую себя... любимой. Снова чувствую себя женщиной..."
    katie.c "Не хочу драматизировать."
    "У меня нет слов. Она так искренне признаётся мне в любви."
    "Я немного растерян. В такие моменты я не знаю, что делать. Остаётся только..."
    window hide
    hide katie with dissolve
    show katie kiss with dissolve
    "Я крепче прижимаю её к себе и снова страстно целую."
    "Мои руки скользят по её боку, затем поднимаются по спине."
    "Она обнимает меня за спину, хвост покачивается и задевает мою руку."
    "Я стягиваю с её плеч верхнюю одежду, и мы, пошатываясь, движемся к кровати."
    scene black with fade
    call playMusic(sexyTheme) from _call_playMusic_153
    "Мы быстро раздеваем друг друга, лишь ненадолго прерывая поцелуи, чтобы снять одежду."
    "Её грудь выскальзывает из бюстгальтера, и мы садимся на кровать."
    image katie missionary start = Movie(play="images/characters/katie/hscenes/missionary/kissing.webm")
    scene katie missionary start with fade
    pause
    "Мы продолжаем целоваться, я глажу её талию и нежно разминаю мягкую пушистую грудь."
    "Мы прижимаемся друг к другу, окутанные теплом."
    katie.c "М-м-м, [mc.name]..."
    "Мы облизываем губы друг друга, переплетаем языки, дыхание становится всё чаще."
    katie.c "Я хочу тебя~"
    mc.c "Я тоже хочу тебя, [katie.name]."
    "Я укладываю [katie.name], и она раздвигает мягкие бёдра."
    katie.c "Нежно... Я... давно этим не занималась..."
    image katie missionary part 1 = Movie(play="images/characters/katie/hscenes/missionary/part1.webm")
    show katie missionary part 1 with fade
    pause
    katie.c "О-о-о-о~"
    "Я нежно вхожу в её киску, уже влажную от нетерпения."
    "Её живот складывается, когда я прижимаю её к кровати. Это невероятно соблазнительное зрелище."
    "Я ощущаю мягкие, мясистые бёдра, пока двигаюсь в ней."
    katie.c "Ты... *А-а* такой большой~"
    mc.c "[katie.name]..."
    mc.c "Ты прекрасна."
    "Её хвост дёргается в сторону, когда я погружаю член до основания."
    image katie missionary part 2 = Movie(play="images/characters/katie/hscenes/missionary/part2.webm")
    show katie missionary part 2 with fade
    pause
    "[katie.name] крепко сжимает мои плечи, слегка впиваясь ногтями."
    katie.c "*А-а-а~*"
    "Передо мной мягко покачивается её пышная грудь, а прекрасная вытянутая лисья мордочка выражает чистое наслаждение."
    katie.c "Сделай меня *а-а* своей женщиной..."
    katie.c "Возьми меня целиком..."
    "[katie.name] полностью отдаётся удовольствию, как и я."
    "Я сдерживал себя изо всех сил, но теперь принимаю её приглашение и ускоряюсь."
    image katie missionary part 3 = Movie(play="images/characters/katie/hscenes/missionary/part3.webm")
    show katie missionary part 3 with fade
    pause
    "Я наклоняюсь к ней, прижимаю огромную грудь к своей и двигаюсь сильнее и быстрее."
    "Я утыкаюсь лицом ей в шею. Её золотистые волосы окружают меня, и я вдыхаю её сладкий запах."
    "Шампунь, духи, её естественный аромат..."
    "Я нежно целую её шею, а она крепко прижимает меня к себе."
    katie.c "О-о-о *Ах* О-о-о~ *А-а-а*"
    "Я не могу удержаться и слегка покусываю её шерсть."
    katie.c "Да-а~ *Ах* [mc.name]~~~"
    "В комнате раздаются влажные шлепки, но сильнее всего я слышу тяжёлое дыхание [katie.name]."
    katie.c "*Ах* *Ах* *А-а*, не останавливайся~~~"
    image katie missionary part 4 = Movie(play="images/characters/katie/hscenes/missionary/part4.webm")
    show katie missionary part 4 with fade
    pause
    "[katie.name] обвивает меня ногами и притягивает к себе, приглашая проникнуть глубже."
    "От этой мысли голова идёт кругом. Я теряю контроль и думаю только о том, как глубже в неё войти."
    mc.c "*Ах* [katie.name]... [katie.name]..."
    katie.c "[mc.name]~~"
    "Наслаждение нарастает, всё тело дрожит в предвкушении."
    "Голова кружится, в мыслях осталось одно животное желание."
    katie.c "К-КОНЧИ В МЕНЯ~ *А-А-А* НАПОЛНИ МЕНЯ~"
    image katie missionary end = Image("images/characters/katie/hscenes/missionary/end.webp")
    scene katie missionary end with fadewhite
    pause
    katie.c "*М-М-М-М-М-М-М-М*~~"
    "Я глубоко кончаю в ней, полностью погружённый в мягкое, пышное, горячее тело [katie.name]."
    "Мы оба покрыты потом, крепко обнимаем друг друга и содрогаемся от экстаза."
    "[katie.name] не отпускает меня, всё ещё вздрагивая от удовольствия."
    katie.c "А-а~ А-а~"
    scene black with fade
    "Кажется, целую вечность мы остаёмся соединёнными и наслаждаемся объятиями."
    "Я лишь утыкаюсь лицом ей в шею и оставляю ещё несколько любовных укусов."
    "Подушечки лап [katie.name] нежно скользят по моей спине, а её ноги, прежде крепко обнимавшие меня, расслабляются."
    "Через некоторое время мы перекатываемся на бок."
    call playMusic(heartTheme) from _call_playMusic_154
    scene katiepillowtalk with fade
    pause
    "Я беру её за руку, и мы смотрим друг другу в глаза."
    "Наши груди вздымаются и опускаются, мы улыбаемся, немного смущаясь."
    mc.c "Это было невероятно."
    katie.c "Ты был чудесен. Я никогда раньше не испытывала ничего подобного..."
    mc.c "Для мужчины это лучший комплимент."
    katie.c "К такому можно привыкнуть."
    katie.c "Мне так повезло, что ты у меня есть."
    "Её глаза слегка наполняются слезами. Я крепче сжимаю её ладонь."
    mc.c "Мне тоже повезло с тобой."
    "Когда дыхание приходит в норму, мы просто лежим в обнимку."
    mc.c "Останься у меня. Завтра на работу не надо."
    katie.c "Правда? Ох, [mc.name]... Я буду рада."
    scene black
    "Мы быстро приводим себя в порядок и готовимся ко сну."
    call katieSleepover from _call_katieSleepover
    "Сегодня мы впервые спим в одной постели."
    katie.c "Сладких снов, [mc.name]."
    "[katie.name] засыпает первой с лицом счастливой красавицы."
    "Хочу, чтобы этот миг длился вечно."

    if(not fromGallery):
        $ katie.addLove(1)

    return {'location':location_home, 'time':'Morning'}

label katieHEvent4(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_155
    "В баре выдалось несколько тяжёлых дней. Не хватает сотрудников, поэтому мне приходится чаще обычного управлять всем самому."
    "Не то чтобы это было проблемой, мы справляемся. Всё равно лучше, чем на прежней работе."
    "Надо просто продержаться до конца дня. Сегодня меня ждёт особое угощение, ради него я справлюсь."
    "Сегодня после работы за мной заедет [katie.name]."
    "Она отвезёт меня к себе и приготовит ужин. Чудесно."
    "Она отлично готовит, намного лучше меня. Её блюда — настоящая домашняя еда, приготовленная с любовью, «как у мамы», как говорится."
    "Но не придавай этому значения. У меня {b}совершенно{/b} нет от неё материнского вайба и мне {b}совершенно{/b} не нравится это."
    "О, а вот и она."
    show katie smile with dissolve
    "[katie.name] заглядывает в дверь, одетая как обычно для работы, с сумочкой в руке."
    show katie tease
    "Она замечает меня, оглядывает комнату, озаряется своей чудесной улыбкой и подходит."
    show katie tease talk
    katie.c "Привет, милый!"
    hide katie with dissolve
    show katie kiss with dissolve
    katie.c "*Чмок*"
    hide katie with dissolve
    show katie tease talk with dissolve
    show katie tease
    katie.c "Как прошёл день?"
    "Такая ласковая... Мягкая, уютная, радостная женщина приходит к своему мужчине на работу..."
    "Как во сне. Мне так повезло."
    mc.c "День был тяжёлым, но ради встречи с тобой всё стоило того, [katie.name]."
    show katie bashful talk
    katie.c "Ну ты и сердцеед..."
    show katie bashful
    mc.c "Как твой день?"
    show katie smile talk 2
    katie.c "Неплохо. Рада, что наконец ушла оттуда. Готов идти?"
    show katie smile
    mc.c "Конечно. Не хочешь сначала выпить?"
    show katie smile talk
    katie.c "Нет, спасибо, дома у меня бутылка. Отлично подойдёт к ужину."
    show katie smile
    mc.c "С нетерпением жду. Всё, что ты готовишь, восхитительно."
    show katie tease talk
    katie.c "Мне всегда приятно готовить для тебя. Пойдём!"
    scene black with fade
    $ location_town.showBackground()
    "По дороге через город мы перекидываемся любезностями, держась за руки."
    "Она вдруг замолкает и крепче сжимает мою руку."
    call stopMusic from _call_stopMusic_27
    show katie surprise with dissolve
    katie.c "!"
    mc.c "Что такое, [katie.name]?"
    call playMusic(sadTheme) from _call_playMusic_156
    katie.c "Тот мужчина впереди..."
    show katie thinking
    katie.c "Мы ходили на свидание... Наверное, около года назад. Он хотя бы пришёл. Нас устроила друг другу коллега."
    katie.c "Это было ужасно. Я так радовалась, а он оказался грубым..."
    show katie sad talk
    katie.c "У него буквально отвисла челюсть, когда он меня увидел. Весь вечер сидел в телефоне, а потом ни звонка, ни сообщения."
    katie.c "Я... могу тебе признаться. Я тогда плакала. Наверное, это был мой худший момент."
    show katie sad
    "Похоже, чувства из-за всех этих неудачных свиданий и разочарований снова накрывают её."
    "Ей больше не нужно так себя чувствовать. Теперь я рядом."
    "Я тоже сжимаю её руку и притягиваю чуть ближе."
    mc.c "Мне жаль, что тебе пришлось через это пройти. Но позволь минутку побыть эгоистом. Как же мне повезло, правда?"
    mc.c "Сейчас я могу быть с тобой."
    show katie bashful
    katie.c "..."
    show katie smile talk
    katie.c "Это мне повезло. Если ради встречи с тобой пришлось через всё это пройти, значит, так и должно было быть."
    show katie smile
    "Улыбка [katie.c] говорит, что всё будет хорошо. Это не улыбка облегчения и не попытка скрыть боль — она искренне светится теплом."
    "Мужчина идёт нам навстречу и пока, кажется, не заметил [katie.name]."
    show katie neutral
    katie.c "Хм... Кольца нет..."
    mc.c "Что такое?"
    show katie neutral talk
    katie.c "Он без кольца. Значит, ещё не женился."
    show katie neutral
    mc.c "Как ты это заметила? Мне бы и в голову не пришло."
    show katie tease talk
    katie.c "Женщины обращают внимание на такие вещи."
    show katie neutral talk
    katie.c "Кстати, вспомнила. Тогда, пока мы разговаривали, он всё твердил о браке и детях."
    katie.c "Просто без конца говорил о «женских обязанностях» и прочей ерунде."
    katie.c "Да и не то чтобы он хотел всего этого со мной. Он был напористым и высокомерным."
    show katie sad talk
    katie.c "Но слова о том, что «время уходит», больно задели. Ему за тридцать, как и мне, а он хотел поскорее со всем определиться."
    show katie thinking
    katie.c "Значит, он тоже ещё не женат. Наверное, и у него не складывается. Скольких женщин он обидел..."
    call playMusic(funnyTheme) from _call_playMusic_157
    show katie tease
    "На её лице появляется немного зловещая улыбка."
    "Мужчина уже близко. Он только что поднял глаза от телефона и посмотрел в нашу сторону."
    katie.c "{size=20}У меня идея...{/size}"
    "Она шепчет мне на ухо, внезапно притягивает мою руку к себе и прижимает её к груди, крепко обнимая."
    "Мы продолжаем идти, она прижимает голову ко мне. Скоро мы поравняемся с тем незнакомцем."
    show katie joy
    katie.c "Ха-ха, милый, ты такой смешной!"
    hide katie with dissolve
    show katie kiss with dissolve
    "Она притягивает мою голову и страстно целует в губы."
    hide katie with dissolve
    show katie tease talk with dissolve
    katie.c "Я люблю тебя, милый!"
    show katie tease
    "Мужчина точно обращает на нас внимание, когда мы проходим мимо. Он слегка приподнимает бровь."
    "Я подыгрываю ей, обнимаю за талию и слегка сжимаю попку."
    show katie surprise
    katie.c "О-ох!"
    show katie tease talk
    katie.c "Ну ты и шалун~"
    show katie tease
    "Мы идём дальше. Я оглядываюсь через плечо, чтобы убедиться, что мы уже отошли подальше."
    mc.c "Ничего себе, я не ожидал. Не знал, что ты на такое способна."
    show katie tease talk
    katie.c "Хи-хи, хотела показать ему, чего он лишился."
    katie.c "Может, он вспомнит, может, нет. Неважно."
    show katie tease
    mc.c "Поверь, он многое потерял. Наверняка теперь жалеет."
    show katie tease talk
    katie.c "Ха! Надеюсь."
    show katie tease talk
    "Мы продолжаем идти, осталось совсем немного."
    scene black with fade
    "После этой сцены... Она сказала, что любит меня."
    "Мы... ещё не говорили друг другу таких слов. Это была часть представления или она и правда так думает?"
    "В конце концов, мы недолго вместе. Всё кажется искренним, но слово «любовь» очень серьёзное."
    "Может ли это изменить наши отношения?"
    scene katielivingroom with fade
    call playMusic(chillTheme) from _call_playMusic_158
    "[katie.name] готовит восхитительный ужин: невероятное рагу из говядины с разными овощами, приготовленными до совершенства."
    "Наверняка на это ушло много времени, но она управляется на кухне так легко, словно это само собой разумеется."
    "И, как всегда, порции у неё щедрые."
    show katie smile with dissolve
    mc.c "Это было невероятно, [katie.name], как всегда."
    show katie smile talk 2
    katie.c "Ой, ты преувеличиваешь, но мне приятно."
    show katie smile
    "Вкусный ужин, пара бокалов вина и отличная компания. Сегодня разговор легко клеился, и мы прекрасно провели время."
    show katie smile talk
    katie.c "Садись на диван, а я пока приберусь."
    show katie tease talk
    katie.c "И не вздумай отказываться — я тебя к столу не подпущу. Просто отдыхай."
    hide katie with dissolve
    "Я не спорю и делаю, как она велит. Она всегда так заботится обо мне. Сажусь на диван, а она убирает со стола."
    "Не могу не любоваться этой прекрасной пышной женщиной."
    "Она берёт тряпку, поворачивается ко мне спиной и начинает вытирать стол..."
    call playMusic(sexyTheme) from _call_playMusic_159
    image katie tabledoggy start 1 = Movie(play="images/characters/katie/hscenes/tableDoggy/start1.webm")
    show katie tabledoggy start 1 with fade
    pause
    "Если бы я не знал, решил бы, что она делает это нарочно..."
    "Покачивает пухлой попкой из стороны в сторону, а за ней виляет большим пушистым хвостом."
    "..."
    katie.c "Хм-хм-м-м~"
    "Она тихонько напевает и продолжает покачиваться."
    "Я зачарован."
    "Кровь приливает к голове. И к члену."
    "Она ждёт, что я {b}не{/b} наброшусь на неё прямо сейчас?"
    image katie tabledoggy start 2 = Movie(play="images/characters/katie/hscenes/tableDoggy/start2.webm")
    show katie tabledoggy start 2 with fade
    pause
    katie.c "Хм-хм-хм~"
    "Я медленно подхожу сзади. Её попка манит меня всё ближе."
    "Под длинной одеждой я представляю скрытые соблазнительные формы."
    "В голове только похоть. Не могу думать ни о чём, кроме желания."
    "Я задираю нижнюю часть её платья, обнажая большую красивую попку."
    image katie tabledoggy start 3 = Image("images/characters/katie/hscenes/tableDoggy/start3.webp")
    scene katie tabledoggy start 3 with fade
    pause
    katie.c "О-ох! [mc.name]!"
    katie.c "О боже~"
    katie.c "Что ты там делаешь?"
    "Трусики едва сдерживают всю эту соблазнительную плоть."
    "Я хватаю её за пухлые ягодицы и слегка ласкаю киску, желая её и подготавливая к тому, что будет дальше."
    katie.c "М-м-м... [mc.name]..."
    mc.c "Не смог удержаться..."
    "Вскоре появляется влага. Может, она тоже ждала этого вечера."
    mc.c "Ты нарочно меня дразнила? Ты уже немного намокла, да?"
    katie.c "Н-нет..."
    "Я начинаю стягивать бельё и с неё, и с себя."
    image katie tabledoggy start 4 = Image("images/characters/katie/hscenes/tableDoggy/start4.webp")
    scene katie tabledoggy start 4 with fade
    pause
    "Мой член уже каменный — так быстро со мной ещё не бывало. В этой женщине есть что-то особенное..."
    "[katie.name] смотрит на мой член, удивлённая и возбуждённая."
    katie.c "О-ого... [mc.name]..."
    katie.c "П-погоди, я весь день работала... Дай хотя бы принять душ..."
    "Уже поздно. Я твёрдый как камень и не могу остановиться."
    mc.c "Перед тобой невозможно устоять."
    katie.c "...Если уж так хочешь~"
    "Я сбрасываю с неё шаль, задираю юбку и спускаю бретельки."
    "Я направляю член и крепко держу её за бёдра, чтобы войти в её тепло."
    image katie tabledoggy part 1 = Movie(play="images/characters/katie/hscenes/tableDoggy/part1.webm")
    show katie tabledoggy part 1 with fade
    pause
    katie.c "А-а-а~ [mc.name]~"
    "Я начинаю двигаться плавно, исследуя глубину и нежные складки её тёплой влажной киски."
    mc.c "Не мог больше ждать... Ты так соблазнительно покачивала попкой..."
    katie.c "Я... Э-э..."
    katie.c "Ни один мужчина ещё... так меня не хотел..."
    mc.c "Они, должно быть, слепые."
    "Я сжимаю мягкие огромные груди перед собой, а её большой пушистый хвост покачивается у моего лица."
    "Одного этого уже достаточно, чтобы уткнуться в них лицом."
    katie.c "О-о~ Милый~"
    mc.c "[katie.name]... Я хочу тебя."
    image katie tabledoggy part 2 = Movie(play="images/characters/katie/hscenes/tableDoggy/part2.webm")
    show katie tabledoggy part 2 with fade
    pause
    "Я ускоряюсь и прижимаю [katie.name] к столу."
    "Хватаю её за основание хвоста и толкаюсь глубже, сильнее, дальше."
    "Врезаюсь в её большую попку."
    katie.c "[mc.name]~ О-о~ М-м-м~"
    "Может, она не привыкла к такой страсти, но перед ней невозможно устоять."
    katie.c "А-а-а~ Ты такой большой~"
    katie.c "Мой большой... сильный... мужчина~"
    "Слова не идут. Каждая её фраза, намеренно или нет, сводит меня с ума от желания."
    mc.c "[katie.name]..."
    image katie tabledoggy part 3 = Movie(play="images/characters/katie/hscenes/tableDoggy/part3.webm")
    show katie tabledoggy part 3 with fade
    pause
    "Её подпрыгивающая попка заводит меня ещё сильнее."
    "Даже сзади я вижу, как огромная грудь подпрыгивает с каждым толчком."
    katie.c "*Ах* *Ах* Да~ [mc.name]~"
    katie.c "Продолжай~"
    mc.c "Мне тебя мало."
    katie.c "Я вся твоя, милый~"
    "..."
    "Мне трудно сдерживаться. Хочется прижать её к столу и сделать своей."
    "Я..."
    mc.c "Хочу тебя видеть."
    image katie tabledoggy part 4 = Movie(play="images/characters/katie/hscenes/tableDoggy/part4.webm")
    show katie tabledoggy part 4 with fade
    pause
    "Услышав мои слова, она разворачивается так, чтобы мы могли смотреть друг другу в глаза."
    "Я ускоряюсь, сжимаю её ягодицы и вхожу в киску."
    katie.c "М-м-м~ Хм-м~ О-о-о~"
    katie.c "[mc.name]... Возьми меня, [mc.name]~"
    mc.c "А-а-а~"
    "Её попка покачивается, грудь подпрыгивает — я никогда не видел [katie.name] такой развратной."
    image katie tabledoggy part 5 = Movie(play="images/characters/katie/hscenes/tableDoggy/part5.webm")
    show katie tabledoggy part 5 with fade
    pause
    "Мы встречаемся взглядами. Она закатывает глаза, задыхается от удовольствия и морщится."
    katie.c "А-а-а~ Я *ах* сейчас..."
    mc.c "И я..."
    "Эта прекрасная зрелая мордочка сводит меня с ума."
    katie.c "Всё хорошо~ Кончай в меня~"
    "Отлично. Не уверен, что смог бы сейчас отстраниться."
    mc.c "Я сейчас!"
    katie.c "Да~!"
    image katie tabledoggy end = Image("images/characters/katie/hscenes/tableDoggy/end.webp")
    scene katie tabledoggy end with fadewhite
    pause
    "Я глубоко кончаю в неё, а [katie.name] содрогается от экстаза."
    "[katie.name] обессиленно падает на стол."
    katie.c "*Ах* *А-а* *А-а*"
    "Она едва держит глаза открытыми, грудь вздымается и опускается, пока она приходит в себя."
    mc.c "[katie.name]... Это было так хорошо..."
    katie.c "Ничего себе~"
    katie.c "Ты был потрясающим~"
    mc.c "...Прости за беспорядок..."
    katie.c "Думаю, я тебя прощу~"
    scene black with fade
    call playMusic(chillTheme) from _call_playMusic_160
    "Дав [katie.name] немного отдохнуть, она встаёт со стола."
    "Она поправляет одежду и подходит ко мне."
    scene katielivingroom with fade
    show katie bashful with dissolve
    mc.c "Это было... слишком?"
    show katie bashful talk
    katie.c "Неужели ты совсем не мог себя контролировать, молодой человек?"
    show katie bashful
    mc.c "...Нет."
    katie.c "..."
    show katie tease talk
    katie.c "Тогда ничего не поделаешь, правда?"
    show katie tease
    mc.c "Я... Постараюсь в следующий раз лучше себя контролировать."
    mc.c "Но ничего не обещаю, особенно когда вижу эту попку."
    show katie bashful
    katie.c "Ой, перестань..."
    "Она такая милая, когда смущается. Не привыкла, чтобы ею так восхищались."
    "..."
    "Теперь вечер стал немного неловким. О чём вообще говорят после такого?"
    mc.c "Еда была чудесная, [katie.name]."
    show katie smile talk
    katie.c "Хи-хи, спасибо, милый."
    show katie surprise
    katie.c "Ой!"
    mc.c "Ч-что такое?"
    show katie tease talk
    katie.c "Я же собиралась приготовить десерт!"
    scene black with fade
    "Остаток вечера мы проводим вместе."
    "Она продолжает как ни в чём не бывало, хотя я кончил в неё."
    "Чудо, что я не кончил ещё раз."

    if(not fromGallery):
        $ katie.addLove(1)

    return {'location':location_home, 'time':'Night'}

label katieLikeEvent3(fromGallery):
    $ location_beach.showBackground()
    call playMusic(chillTheme) from _call_playMusic_161
    "После чудесного свидания мы с Кэти заезжаем на пляж."
    "Не купаться, а просто посидеть у моря, подышать прохладным бризом и отдохнуть."
    "Мягкий шум волн и пловцы в воде создают расслабляющую атмосферу."
    show katie joy with dissolve
    katie.c "О-о, как же хорошо. Надеюсь, ты не против, что старушка просто отдыхает."
    mc.c "Не знаю, Кэти. Я рассчитывал на захватывающее приключение. Знаю, какая ты."
    show katie tease talk
    katie.c "Хе-хе~ Да-да, молодой человек~ Будто мне всегда сложно поспевать за твоей энергией..."
    show katie tease
    mc.c "Ладно, признаю. Я и сам сейчас хочу именно этого."
    "В наших отношениях проявляется любовь к простым радостям жизни."
    "Вкусный ужин, разговор, фильм, кофе, прогулка или просто отдых дома. Это то, чего мы хотим и что мне нравится делать с ней."
    "Больше и желать нечего."
    show katie smile talk
    katie.c "Идеально провели выходной. Спасибо, милый!"
    show katie smile talk 2
    katie.c "Приятно иногда брать отдельные выходные. Неделя разбивается, и можно куда-то сходить, пока там тихо."
    show katie thinking
    katie.c "Раньше я копила все выходные, а потом брала отпуск сразу на неделю или две, но особо нечем было заняться. Мне становилось скучно."
    mc.c "Если у тебя ещё остались выходные, давай выберемся куда-нибудь. Мне повезло — я могу взять выходной почти когда угодно."
    show katie smile talk
    katie.c "Конечно! Теперь у меня есть такой красавец, с которым можно проводить время~ Чем займёмся?"
    show katie smile
    mc.c "Можем куда-нибудь съездить? Например, отдохнуть за городом или даже отправиться за границу в настоящий отпуск."
    mc.c "Не знаю. А что бы ты хотела?"
    show katie tease talk
    katie.c "Хе-хе~ Какая замечательная идея!"
    show katie thinking
    katie.c "Боже, когда же я в последний раз была за границей?.."
    show katie tease talk
    katie.c "Ты правда хотел бы поехать туда со мной, старушкой?"
    show katie tease
    mc.c "Ну что за глупый вопрос, Кэти. Мне кажется, это было бы здорово."
    show katie smile talk 2
    katie.c "Ты же знаешь, я люблю солнце... Здесь есть море, но здорово было бы оказаться в тёплом климате!"
    katie.c "Солнце, море, вздремнуть у бассейна в отеле..."
    show katie joy
    katie.c "О-о, я уже вся взбудоражилась от одной мысли! Мы можем поехать куда угодно!"
    mc.c "Мне нравится. Я мало путешествовал за границу, по крайней мере взрослым."
    mc.c "Я бы с радостью. Давай подумаем..."
    show katie tease talk
    katie.c "Я посмотрю варианты в интернете. Может, девочки что-нибудь посоветуют."
    show katie tease
    "Поездка с Кэти... Если подумать, это большой шаг в наших отношениях. Совместный отпуск."
    "Надеюсь, скоро получится."
    call stopMusic from _call_stopMusic_28
    "Наш разговор прерывает приближающийся шум."
    "Мимо пробегают двое малышей, крича и смеясь."
    "Два мальчика бегают друг за другом. Старший размахивает палкой над головой, а младший визжит от смеха."
    unknown "Мальчики! Ну-ка, идите сюда!"
    "За ними спешит взрослая женщина, по всей видимости их мама."
    unknown "Положи это, пожалуйста, Уильям! Сколько я тебе говорила?"
    "Она умоляет их успокоиться, выглядит измученной и едва поспевает за их неуёмной энергией."
    "Разговор прерван, и я смотрю на Кэти."
    call playMusic(heartTheme) from _call_playMusic_162
    show katie smile
    "Она следит за мальчиками с тёплой улыбкой. В её взгляде — радость от того, как они играют."
    mc.c "Милые дети."
    show katie neutral talk
    katie.c "Ага, хм-хм~ Бедная мама."
    show katie neutral
    "Она так говорит, но всё равно с умилением наблюдает за трогательной сценой."
    "Но я чувствую что-то ещё... Лёгкую тоску и грусть."
    "Возможно, Кэти хочет детей. Она такая заботливая, но ей некого опекать по-матерински."
    "Зная Кэти, думаю, она считает, что её время уже прошло. Молодые годы миновали, а серьёзных отношений так и не было."
    "В середине тридцатых ведь ещё не поздно. Да, с возрастом шансов становится меньше, но... Если она действительно этого хочет..."
    "Кажется, я знаю ответ, но хочу услышать его от неё. Как поднять такую тему с новым бойфрендом?"
    "Я и сам не знаю, что хотел бы услышать от неё. Что бы я сделал?"
    mc.c "Кажется, это тяжёлая работа, но все, с кем я говорил, утверждают, что она того стоит."
    show katie smile talk
    katie.c "Я слышу то же самое от знакомых мам и на работе. То взлёты, то трудности — в зависимости от возраста ребёнка."
    show katie smile
    "Её улыбка становится шире, пока она смотрит на маму, вытирающую что-то с лица мальчика."
    unknown "Ну и неряха ты..."
    unknown2 "Ма-а-ам~~!"
    show katie smile talk
    katie.c "Хм-хм~ Мальчики... У Рози сын примерно такого возраста..."
    show katie smile
    mc.c "Ты сама хотела бы такого?"
    call playMusic(sadTheme) from _call_playMusic_163
    show katie neutral
    katie.c "..."
    "Её лицо немного омрачается... Похоже, тема болезненная."
    show katie neutral talk
    katie.c "Детей?"
    show katie neutral
    mc.c "Да..."
    katie.c "..."
    show katie bashful talk
    katie.c "Ох, милый, в моём возрасте уже поздно... Когда-то я... Ах..."
    show katie bashful
    "Она отводит взгляд вдаль."
    mc.c "Кэти, пожалуйста... Тебе ещё нет сорока. Это не..."
    show katie neutral talk
    katie.c "Думаю... Да, хотела. Не то чтобы это было главной целью жизни, но когда окружающие начали заводить детей, я тоже задумалась."
    show katie bashful talk
    katie.c "Думаю, если бы я... встретила кого-нибудь... возможно, завела бы."
    show katie bashful
    mc.c "Ты ещё..."
    show katie bashful talk
    katie.c "Я изучала этот вопрос... Поверь... Боже, не верится, что мы сейчас об этом говорим..."
    show katie bashful
    mc.c "Прости, Кэти. Я не знал, что ты так думаешь. Я думал..."
    show katie neutral talk
    katie.c "Хорошо, да, {i}в теории{/i} я могла бы... Просто... Я уже давно мысленно исключила такую возможность."
    katie.c "Мне кажется, что время прошло. Думаю, я уже смирилась с этим."
    show katie neutral
    "Похоже, она правда хотела детей, но ей казалось, что время ушло."
    "И главный вопрос... Если до этого дойдёт, готов ли я стать отцом? Это же безумие."
    "Если я хочу быть с Кэти. По-настоящему, {b}вместе{/b}. Захотела бы она этого? А я сам? {i}Я{/i} этого хочу? Сейчас... не знаю."
    "И это важно: мы до сих пор не предохранялись."
    mc.c "Прости, что спрашиваю, но... Значит... Ты понимаешь... Насчёт контрацепции?"
    show katie bashful talk
    katie.c "...Да, я предохранялась. На всякий случай. Я не знала, что между нами происходит..."
    show katie smile talk
    katie.c "Не хотелось бы случайной беременности, да? Думаю, ни одному из нас не нужно, чтобы такое произошло неожиданно и без плана."
    show katie neutral
    "К счастью, она предусмотрительнее меня... Но значит ли это, что она допускает такую возможность?"
    "Возможно, она не совсем отказалась от этой мечты."
    "Я не знаю, готов ли к такому прямо сейчас... Ещё рано. Если слишком много говорить об этом, могут возникнуть проблемы."
    "Я просто сижу рядом и кладу руку ей на ладонь. Не знаю, что сказать."
    show katie neutral talk
    katie.c "Давай... пока оставим этот разговор, [mc.name]? Я хочу, чтобы всё оставалось как есть."
    show katie bashful talk
    katie.c "Я не... отказываюсь от этой идеи совсем. Просто... Ох, как бы это выразить?"
    show katie bashful
    mc.c "Всё хорошо, Кэти, правда. Я ни на чём не настаиваю. Прости, что тема всплыла. Я просто хотел понять, что ты..."
    show katie smile talk 2
    katie.c "Всё в порядке, милый, ты ни в чём не виноват. Правильно обо всём говорить открыто..."
    show katie smile
    "Наконец мы снова смотрим друг другу в глаза и, к счастью, всё ещё улыбаемся."
    "Сегодня я узнал о Кэти больше. О том, что ей пришлось пережить и что у неё сейчас на душе."
    "Я сжимаю её руку, и она отвечает тем же."
    hide katie with dissolve
    show katie kiss with dissolve
    pause
    katie.c "{b}*Чмок*{/b}"
    hide katie with dissolve
    show katie hug with dissolve
    pause
    "Мы прижимаемся друг к другу, а семья уходит вдоль берега."
    "Кэти смотрит им вслед, но крепко и искренне обнимает меня."
    katie.c "Пойдём домой?"
    mc.c "Конечно, пойдём."
    scene black with dissolve
    "Мы идём домой, держась за руки. Разговор о детях не испортил нам день."
    "Лучше переключиться на возможный отпуск..."

    if(not fromGallery):
        $ katie.addLove(1)
    return

label katieHEvent5(fromGallery):
    $ location_home.showBackground()
    call playMusic(funnyTheme) from _call_playMusic_164
    "Так... Последние штрихи. Что там было? Соль... Соевый соус..."
    "Чёрт, забыл добавить чеснок... Можно теперь уже без него?"
    "Где он? Я вообще его нарезал?"
    "В панике я задеваю нож, и он падает на пол."
    mc.c "Чёрт!"
    katie.c "Там всё в порядке, [mc.name]?"
    mc.c "Э-э, да, всё под контролем! Уже почти готово..."
    "Сегодня я принимаю Кэти у себя и готовлю для нас ужин."
    "Хочу отплатить ей за все её чудесные блюда, но до её мастерства мне далеко."
    "Обычно готовлю сносно, но сейчас всё идёт не так. Решил приготовить непривычное блюдо, чтобы впечатлить её."
    "До её обычных ужинов не дотягивает. Ну, уже готово... Пора подавать..."
    mc.c "Ужин готов, Кэти."
    "Я отношу тарелки к столу."
    show katie joy with dissolve
    katie.c "О, [mc.name]! Как мило с твоей стороны!"
    mc.c "Только не жди слишком многого... Кажется, получилось не очень."
    show katie tease talk
    katie.c "Милый, не волнуйся, уверена, будет вкусно. Смотри, выглядит отлично!"
    show katie tease
    "На вид всё нормально... Даже {b}выглядит{/b} не так уж плохо, но вкус меня пугает."
    mc.c "Надеюсь, но заранее прости."
    show katie tease talk
    katie.c "Не глупи, уверена, мне понравится."
    show katie tease
    "Если мужчина, который умеет готовить, привлекателен, то насколько непривлекателен мужчина, который совсем не умеет?"
    "Мы начинаем есть. Я разглядываю кусочки, некоторые недожаренные, другие пережаренные."
    "Я кладу кусочек в рот. Он..."
    "Безвкусный. Сплошная пресная каша. Текстура совсем не та, что я ожидал."
    "Куда делся весь вкус, который я добавлял?"
    "Кэти тоже пробует. Пережёвывая, она приподнимает бровь. Если мне невкусно, боюсь представить, каково ей."
    show katie thinking
    katie.c "Хм~"
    "Это притворный стон восторга, который я когда-либо слышал. Скорее любопытный, чем радостный."
    katie.c "Здесь должен был быть чеснок?"
    mc.c "Должен. Кажется, я каким-то образом совсем забыл его добавить."
    katie.c "Мясо ты посолил до или после приготовления?"
    mc.c "Я... после... просто посыпал сверху."
    show katie bashful talk
    katie.c "Понятно..."
    show katie bashful
    mc.c "Прости. Я всё испортил."
    show katie smile talk
    katie.c "Ой, перестань, [mc.name], очень вкусно!"
    show katie smile
    mc.c "Не надо мне врать. По крайней мере, это съедобно... Наверное."
    "Я откусываю ещё и как можно выразительнее морщусь."
    show katie joy
    katie.c "Ха-ха! Да не так уж плохо, милый."
    show katie smile talk 2
    katie.c "Главное — внимание!"
    show katie smile
    mc.c "Видимо, это моё жизненное кредо... А в итоге ничего не получается."
    show katie tease talk
    katie.c "Ой, мне правда очень приятно. Всегда здорово, когда для тебя готовят."
    katie.c "Но я не против готовить для нас — здесь или у себя! Мне ведь это нравится!"
    show katie tease
    mc.c "Я всё равно буду мучить тебя своими попытками. Не могу же я позволить жене..."
    "Я на секунду осекаюсь. Чуть не проговорился."
    mc.c "...не могу позволить даме одной заниматься готовкой."
    show katie bashful talk
    katie.c "О-ох, да, не хотелось бы, верно? Как прогрессивно с твоей стороны, [mc.name]."
    show katie bashful
    "Она ненадолго отводит взгляд. Наверное, заметила, что я чуть не сказал."
    show katie smile talk 2
    katie.c "В следующий раз приготовим вместе, хорошо?"
    show katie smile
    mc.c "Буду рад паре советов."
    call stopMusic from _call_stopMusic_29
    scene black with fade
    "Мы доедаем. Блюдо неудачное, зато компания чудесная. В итоге вышло неплохо."
    "Мы немного отдыхаем на диване, как обычно, когда она приходит ко мне."
    "Есть несколько шоу, которые любит Кэти. Она обожает викторины и реалити-шоу."
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_165
    show katie smile with dissolve
    "Мы обнимаемся, а одно из её шоу как раз начинается."
    "Я до слёз скучаю, но ей очень нравится. Чувствую, что глаза закрываются."
    show katie neutral talk
    katie.c "Ты в порядке, [mc.name]? Глаза слипаются."
    show katie neutral
    mc.c "Да, всё нормально. Просто последние пару недель были загруженными, в баре возникли проблемы."
    mc.c "Ничего серьёзного, сейчас всё налаживается. Просто режим сна совсем сбился."
    show katie neutral talk
    katie.c "Ой, милый, можешь немного вздремнуть, если хочешь. Смотри~"
    show katie neutral
    "Она сводит ноги и похлопывает себя по коленям."
    show katie smile talk
    katie.c "Отдохни здесь. Я не против, если ты немного поспишь~"
    show katie smile
    "Очень заманчивое предложение... Мягкие пухлые бёдра Кэти — тёплая подушка."
    "И я правда вымотался. Конечно, я соглашусь."
    mc.c "Не придётся просить дважды."
    "Я вытягиваюсь и кладу голову ей на колени."
    scene katiehevent5i1 with fade
    "Надо мной чудесный вид: огромная грудь Кэти почти нависает над лицом."
    "Вот так и умереть можно."
    "Она кладёт руку мне на голову и нежно гладит."
    katie.c "Можешь немного поспать."
    "Всего через несколько мгновений, под её успокаивающие поглаживания, я засыпаю."
    call stopMusic from _call_stopMusic_30
    scene black with fade
    "..."
    "Сладкие сны... О мире прекрасных девушек-антро..."
    "И все они мои..."
    "..."
    "Я начинаю просыпаться. Что это за незнакомый голос?.."
    "А, телевизор всё ещё работает. Как долго я спал?"
    scene katiehevent5i2 with fade
    "Кэти замечает, что я шевелюсь."
    katie.c "Хорошо отдохнул, [mc.name]?"
    mc.c "Да, даже не представляешь."
    mc.c "Но реальность ещё лучше."
    "Она сияюще улыбается мне."
    call playMusic(sexyTheme) from _call_playMusic_166
    "Эта пышная грудь покачивается у меня перед глазами... Я вдруг чувствую прилив сил..."
    "Прилив в определённом месте... Она так приятно пахнет... И нежно гладит меня, что тоже помогает."
    "Не могу удержаться и эгоистично сжимаю её..."
    image katie nursing handjob part 1 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part1.webm")
    show katie nursing handjob part 1 with fade
    pause
    katie.c "О-ох! [mc.name]..."
    mc.c "Прости, она такая соблазнительная... Ты не против?"
    katie.c "Ну... Ничего страшного, милый... У тебя была тяжёлая неделя."
    "Я лежу у неё на коленях, а Кэти гладит меня по голове... Блаженство."
    katie.c "Э-э... [mc.name]... Ты немного... возбудился?"
    "Как оказалось, ещё как. Она замечает растущую выпуклость и начинает опускать руку."
    katie.c "Похоже, тебе нужна небольшая помощь... Хочешь немного расслабиться?"
    mc.c "Думаю, да, Кэти..."
    "Она нежно расстёгивает ширинку, и член становится твёрдым."
    image katie nursing handjob part 2 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part2.webm")
    show katie nursing handjob part 2 with fade
    pause
    "Она нежно ласкает мой член вверх-вниз, так деликатно, словно прирождённая заботливая мамочка."
    katie.c "[mc.name]... Ты так возбудился из-за такой старушки, как я~?"
    mc.c "Не знаю, кто бы устоял... Когда о тебе заботится такая красавица."
    katie.c "Ой, перестань..."
    "Я нежно разминаю её огромную грудь, и она полностью заполняет мою ладонь мягкостью."
    katie.c "Милый... Я всегда помогу тебе, когда будет нужно."
    mc.c "Осторожнее... Я не остановлюсь."
    katie.c "О боже~"
    "Её грудь касается моего лица, когда она наклоняется. Надо воспользоваться моментом..."
    "Я стягиваю бретельки её платья, чтобы насладиться великолепной грудью."
    image katie nursing handjob part 3 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part3.webm")
    show katie nursing handjob part 3 with fade
    pause
    katie.c "О-ох... [mc.name]!"
    katie.c "Н-не мои сос... М-м~"
    "Не могу удержаться и облизываю вкусный розовый сосок, покачивающийся на её пышной груди."
    "Высасывая его у неё на коленях, я чувствую себя почти младенцем..."
    katie.c "М-м~ [mc.name]~ Ты такой твёрдый..."
    "Я обхватываю свободную грудь и щекочу затвердевший сосок, нежно сминая его пальцами."
    "Пальцы глубоко погружаются в тёплую мягкую шерсть..."
    mc.c "Кэти... Продолжай..."
    image katie nursing handjob part 4 = Movie(play="images/characters/katie/hscenes/nursingHandjob/part4.webm")
    show katie nursing handjob part 4 with fade
    pause
    "От моего языка на соске она напрягается, крепче сжимая и страстнее лаская мой член."
    katie.c "А-аккуратнее... Он чувствительный~"
    mc.c "М-м~ Так хорошо..."
    "Я крепко сжимаю её прекрасную грудь и беру нежный сосок в рот... Ощущения переполняют меня."
    "Всё вместе с нежной рукой доводит меня до оргазма."
    mc.c "М-м, Кэти..."
    katie.c "Выпусти всё, [mc.name]~ Кончи для меня~"
    "Эти слова становятся последней каплей."
    image katie nursing handjob end 1 = Image("images/characters/katie/hscenes/nursingHandjob/end1.webp")
    scene katie nursing handjob end 1 with fadewhite
    pause
    "Она проводит рукой вверх и сжимает головку, пока я кончаю."
    katie.c "О-ох~!"
    "Она старается, но спермы оказывается слишком много."
    image katie nursing handjob end 2 = Image("images/characters/katie/hscenes/nursingHandjob/end2.webp")
    scene katie nursing handjob end 2 with fade
    pause
    "Я с причмокиванием отпускаю её сосок и откидываюсь ей на колени, тяжело дыша от удовольствия."
    katie.c "Ничего себе, милый, тебе это было нужно, да~?"
    katie.c "Тебе лучше~?"
    mc.c "Ты ходячее чудодейственное лекарство, Кэти..."
    katie.c "Хм-хм~ Приятно слышать. Теперь, когда ты проснулся, лучше встань. Не хочу всё испачкать..."
    scene black with fade
    call playMusic(chillTheme) from _call_playMusic_167
    "Я сажусь и помогаю Кэти привести себя в порядок, чтобы она снова почувствовала себя прилично."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_home.showBackground()
    show katie tease with dissolve
    "Мы какое-то время сидим вместе и смотрим телевизор, пряча смущённые улыбки."
    show katie smile talk
    katie.c "Ну, уже поздно... Не думала, что мы..."
    show katie smile
    mc.c "Я тоже. Может, я что-то добавил в еду?"
    show katie tease talk
    katie.c "Хе-хе~ Ты бы так поступил~?"
    show katie tease
    mc.c "Я и половины содержимого своих шкафчиков не знаю. Ни за что."
    mc.c "Уже поздно. Может, ты... останешься у меня? Я не могу отправить леди домой одну в такую ночь."
    "На всякий случай она уже оставила здесь немного одежды, чтобы ночевать у меня в рабочие дни."
    show katie smile talk
    katie.c "Если ты не против?"
    show katie smile
    mc.c "На самом деле, я настаиваю."
    show katie tease talk
    katie.c "Чудесно!"
    scene black with fade
    "Мы прибираемся после ужина и готовимся ко сну."
    call katieSleepover from _call_katieSleepover_1
    "Мы уютно устраиваемся в кровати."
    katie.c "Спасибо за сегодняшний вечер, милый."
    mc.c "В следующий раз закажем еду?"
    katie.c "Хе-хе~ Может быть..."
    scene black with fade

    if(not fromGallery):
        $ katie.addLove(1)

    return {'location':location_home, 'time':'Morning'}

label katieHEvent6(fromGallery):
    $ location_home.showBackground()
    call playMusic(barTheme) from _call_playMusic_168
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Хм? Звонок... Посмотрим. Надеюсь, не напоминают об оплате счёта..."
    "О, это Кэти? Она предпочитает звонить. Может, просто хочет поболтать."
    mc.c "Привет, лисичка."
    katie.c "П-привет... Ой, это ты..."
    "Кажется, я слышу, как она краснеет по телефону."
    mc.c "Как ты?"
    katie.c "Всё хорошо, спасибо, милый. Хотела узнать: ты сейчас занят?"
    "Вообще ничего не делаю. Вот такая у меня насыщенная жизнь..."
    mc.c "Нет, сейчас ничем не занят. Что случилось?"
    katie.c "Хотела попросить тебя помочь... Кажется, с кухонной раковиной что-то не так."
    mc.c "Правда? А что с ней? Что происходит?"
    katie.c "Она, э-э... медленно сливает воду? И... шумит немного? Не знаю точно."
    katie.c "Можешь взглянуть? Если ничего страшного, не придётся вызывать мастера."
    "Какие-то странные и расплывчатые симптомы... Я не сантехник, но у меня есть кое-какие инструменты. И как мужчина я будто обязан... Может, разберусь."
    mc.c "Конечно, Кэти. Хочешь, я прямо сейчас зайду?"
    katie.c "Это было бы замечательно! Спасибо! Я буду дома."
    mc.c "Не за что, скоро буду."
    katie.c "Спасибо, милый! До скорого."
    "*Щёлк*"
    "Так, где мой ящик с инструментами?"
    "Пара мелочей... Отвёртки, ручная пила, молоток..."
    "Сойдёт."
    scene black with fade
    "Недалеко идти. Было бы здорово примчаться и спасти положение — почувствую себя настоящим мужчиной."
    "Я прихожу и звоню в дверь."
    katie.c "[mc.name]!"
    scene katielivingroom with fade
    show katie smile with dissolve
    "Кэти открывает дверь и тянет меня за руку внутрь."
    mc.c "Сантехник [mc.name] к вашим услугам. Вызывали, мадам?"
    show katie smile talk 2
    katie.c "Хе-хе~ Ну перестань... Но спасибо, что пришёл."
    hide katie with dissolve
    show katie kiss with dissolve
    katie.c "*Чмок*"
    hide katie with dissolve
    show katie smile with dissolve
    mc.c "Покажи пациента. Может, потребуется операция."
    show katie smile talk 2
    katie.c "Хе-хе~ Ну, вот кухня..."
    show katie smile
    mc.c "В чём проблема? Возможно, придётся разобрать трубы."
    show katie neutral talk
    katie.c "Ну, она... э-э... Немного дребезжала?"
    show katie neutral
    mc.c "И вода медленно уходила?"
    show katie bashful talk
    katie.c "Ой, э-э, да... Я не очень разбираюсь в таких вещах..."
    show katie bashful
    "Всё ещё очень расплывчато. Ладно, посмотрю."
    mc.c "Хорошо... Посмотрю, что можно сделать."
    "Я ставлю ящик с инструментами и заглядываю под шкафчик, где проходят трубы."
    show katie tease talk
    katie.c "Спасибо, милый. Я как раз разбирала одежду, дай мне несколько минут."
    show katie tease
    mc.c "Конечно."
    hide katie with dissolve
    "Кэти уходит в спальню, а я озадаченно смотрю на трубы. Так, посмотрим..."
    "Я некоторое время пускаю воду. Вроде всё нормально."
    "Она даже уходит как положено... Странно."
    "Проверяю горячую и холодную воду, разный напор... Набираю раковину и сливаю... Всё в порядке."
    "Даже стучу по трубам снизу. Всё, кажется, работает идеально."
    "Почёсывая затылок, думаю... Может, сделать вид, что починил? Заработаю очки."
    "С самого начала описание проблемы было странным."
    "Я ковыряюсь у слива и слышу, как открывается дверь спальни. Думая, что Кэти просто ходит туда-сюда, делаю вид, что занят."
    katie.c "[mc.name]~"
    "Она зовёт меня."
    mc.c "Я... кхм... Диагностирую..."
    katie.c "Вот как~?"
    "В её голосе слышится игривость. Заинтригованный, я поднимаю голову."
    call playMusic(sexyTheme) from _call_playMusic_169
    scene katiecowgirlstart1 with fade
    pause
    "О боже..."
    "Кэти стоит у двери в соблазнительном комплекте чёрного белья."
    "Она принимает провокационную позу, в глазах игривое, похотливое выражение."
    mc.c "Я..."
    "Я стою с открытым ртом. Она невероятна."
    katie.c "Хм-хм~ Что такое, милый?"
    "Она самодовольно улыбается. Погоди-ка, это всё была игра?"
    "Небольшой план «соблазнить сантехника»? Она мгновенно меня покорила."
    mc.c "Ты... потрясающе выглядишь..."
    katie.c "Я купила кое-что новенькое... Подумала, тебе может понравиться..."
    mc.c "Обожаю."
    katie.c "Хе-хе~ Может, попробуем... Я не знаю... устроить это?"
    "Она игрива и сама проявляет инициативу. Редкость, но я только рад."
    "Я обхожу столешницу. Хочется наброситься на неё."
    "Она манит меня пальцем и скрывается за углом."
    scene katiecowgirlstart2 with fade
    pause
    mc.c "Красавица..."
    "Я стягиваю штаны, член уже возбуждён в предвкушении. Кэти смущённо улыбается."
    katie.c "[mc.name], я кое-что хотела бы попробовать."
    "О? Держу пари, мне понравится."
    mc.c "Что угодно."
    katie.c "Мне никогда не удавалось... быть... «сверху»... Можно?"
    "В мозгу вспыхивают нейроны. Звучит невероятно."
    mc.c "Конечно."
    scene katiecowgirlstart3 with fade
    pause
    "Я быстро снимаю остальную одежду и притягиваю Кэти к себе, сжимая её бёдра."
    katie.c "О-ох... Может, это..."
    "Теперь, когда она заняла позицию, кажется, она колеблется."
    mc.c "Это невероятно, Кэти. Я этого хочу!"
    katie.c "П-понятно..."
    "Мой член трётся о её промежность, трусики спроектированы так, чтобы спускаться, не снимая остальное. Это невероятно заводит."
    mc.c "Ты потрясающе в них выглядишь. Они точно останутся на тебе."
    katie.c "М-м~"
    "Немного направив её, я помогаю Кэти опуститься на мой пульсирующий член."
    image katie cowgirl part 1 = Movie(play="images/characters/katie/hscenes/cowgirl/part1.webm")
    show katie cowgirl part 1 with fade
    pause
    "Я мягко покачиваюсь, полностью погружённый в неё и сжатый её большими мягкими бёдрами."
    katie.c "М-м-м~ Ты уже такой..."
    mc.c "Перед тобой невозможно устоять."
    "Даже от её мягких покачиваний невероятно приятно, её промежность скользит по мне."
    mc.c "Ох, чёрт~"
    katie.c "Я не слишком тяжёлая, [mc.name]?"
    mc.c "Вовсе нет. Мне нравится, когда ты сверху, Кэти... Ты идеальна."
    image katie cowgirl part 2 = Movie(play="images/characters/katie/hscenes/cowgirl/part2.webm")
    show katie cowgirl part 2 with fade
    pause
    "Она чуть тяжелее большинства, но ощущение, что она сильнее обнимает меня и прижимает к кровати, просто потрясающее."
    "Я обхватываю её мясистые бёдра и направляю вверх-вниз."
    katie.c "А-а-а~ Так глубоко~"
    "Её бёдра давят на мои, прижимая меня к кровати."
    "Соки скользят по члену и издают непристойные влажные звуки."
    "Я едва вижу, как позади неё от удовольствия виляет большой пушистый хвост."
    katie.c "М-м~ М-м~"
    "Вижу, ей нравится, но пора добавить."
    mc.c "Возьми меня за руки."
    "Кэти откидывается назад и держится за мои руки."
    image katie cowgirl part 3 = Movie(play="images/characters/katie/hscenes/cowgirl/part3.webm")
    show katie cowgirl part 3 with fade
    pause
    "Опираясь на меня и помогая толчками снизу, Кэти начинает подпрыгивать выше и быстрее, ударяясь о мои бёдра."
    katie.c "А-а-а~ А-м-м~"
    katie.c "О-о-ох~"
    "Её большая мягкая грудь подпрыгивает вместе с ней. Как же красиво она выглядит."
    "Светлая шерсть контрастирует с прекрасным чёрным кружевом... Я возбуждён сильнее, чем когда-либо."
    "Она крепко держит меня за переплетённые пальцы, сжимая их с каждым толчком."
    mc.c "Тебе хорошо?"
    katie.c "Я... *Ах* обожаю~"
    image katie cowgirl part 4 = Movie(play="images/characters/katie/hscenes/cowgirl/part4.webm")
    show katie cowgirl part 4 with fade
    pause
    "Она заглядывает мне в глаза, которые с трудом держатся открытыми от удовольствия."
    katie.c "Так~ хорошо~ А-а-а~"
    mc.c "Ты невероятна, Кэти..."
    "Напряжение нарастает в паху. Я весь охвачен удовольствием, но всё сильнее хочется пуститься во все тяжкие."
    "Она устаёт, и я её понимаю. Пора взять инициативу."
    "Я маню её опустить лицо к моему."
    mc.c "Иди сюда~"
    image katie cowgirl part 5 = Movie(play="images/characters/katie/hscenes/cowgirl/part5.webm")
    show katie cowgirl part 5 with fade
    pause
    "Она наклоняется, и мы глубоко целуемся."
    "Я пользуюсь моментом, хватаю её за мясистую попку и прижимаю бёдра к себе."
    katie.c "М-м~ Хм-м~!"
    "Я толкаюсь в неё, заставляя подпрыгивать с каждым движением. Вокруг разносятся влажные шлепки."
    "Кэти едва успевает делать короткие вдохи. Она содрогается, пока я яростно трахаю её."
    "Мы сливаемся в одно целое, покрытые соками и стонами, продолжая целоваться и переплетать языки."
    katie.c "А-а~ М-м~ [mc.name]~ [mc.name]~"
    mc.c "Я... М-м~ Сейчас кончу~"
    katie.c "А-а-а~ Пожалуйста~ *Ах* Давай~ Я почти..."
    "Я чувствую, как она вздрагивает подо мной, поднимает голову и выгибает спину от удовольствия. Я сейчас кончу."
    scene katiecowgirlend1 with fadewhite
    pause
    katie.c "А-А-А-А-А~"
    "Кэти кричит и содрогается вместе со мной."
    "Я мощно кончаю и чувствую, как сперма стекает по члену. Я полностью наполнил её."
    "Прижимая бёдра к моим, мы вздрагиваем от экстаза."
    "Кэти обессиленно падает на меня, и мы остаёмся в объятиях."
    katie.c "Ах~ Хм-м~"
    scene katiecowgirlend2 with fade
    pause
    "Наконец Кэти перекатывается на бок и ложится рядом, а мы оба постепенно переводим дыхание."
    katie.c "Ах~ М-м~ О боже~"
    katie.c "Ничего себе... Так здорово~ Не думала, что это настолько отличается."
    mc.c "Мне очень понравилось смотреть на тебя."
    katie.c "Я ведь не выглядела совсем уж нелепо?"
    mc.c "Хочу, чтобы ты чаще так отпускала себя."
    "Она улыбается и обнимает меня. Мы ещё немного лежим вместе."
    "Вот это поворот. Наверное, она с самого начала всё спланировала."
    mc.c "С раковиной ничего не было, да?"
    katie.c "Хе-хе~ Ничего... Просто захотелось немного подшутить."
    mc.c "Ах ты проказница... Тогда можешь обманывать меня в любое время."
    "Я сжимаю её руку, а она уютно прижимается ко мне."
    scene black with fade
    "Мы закрываем глаза и немного отдыхаем."
    "Мягкая шёлковая шерсть Кэти, спокойное дыхание... Я в раю."
    "В конце концов мы оба ненадолго засыпаем."
    "Проснувшись, я помогаю ей немного прибраться и целую на прощание."

    if(not fromGallery):
        $ katie.addLove(1)

    return {'location':location_town}

label katieLikeEvent4Invitation(fromGallery):
    call playMusic(heartTheme) from _call_playMusic_170
    show katie smile
    "У нас с Кэти всё просто замечательно."
    "Мы всё чаще проводим время вместе: ужинаем, смотрим фильмы, гуляем вдоль берега, ездим куда-нибудь."
    "Мне нравится, когда она звонит и справляется, как у меня дела. Нравится, когда она приходит. Обожаю её еду, смех и пушистый хвост..."
    "Люблю засыпать с ней в объятиях и просыпаться рядом с её сияющим лицом."
    "В последнее время она часто приходит ко мне. Порой кажется, что у меня она бывает чаще, чем у себя."
    "И я начинаю задумываться... Может, стоит сделать наши отношения немного... официальнее?"
    "Иногда я жалею, что утром её нет рядом. Хочу, чтобы она чувствовала себя у меня как дома..."
    "У неё и свой дом есть... Хороший, значит, недешёвый. Она прилично зарабатывает, но..."
    "Захочет ли она переехать насовсем?"
    "В конце концов, часть вещей уже хранит у меня. Может, просто переехать?"
    "Не слишком ли рано?"
    $ girlsAlreadyMovedIn = [character for character in characters if character.movedIn == True]
    $ homeHasRoom = len(girlsAlreadyMovedIn) + girlsMovingIn < homeCapacity
    $ yesOption = 'Да!' if(homeHasRoom) else "Нужно улучшить дом"
    if(not fromGallery):
        menu:
            "Может, попросить Кэти переехать ко мне? Это можно сделать в любой момент."
            "[yesOption]" if(homeHasRoom):
                $ girlsMovingIn += 1
                pass
            "Пока нет":
                call endCharacterInteraction(katie) from _call_endCharacterInteraction_3
    show katie smile talk 2
    katie.c "[mc.name]~? Почему ты так на меня смотришь? У тебя такое забавное лицо."
    show katie smile
    mc.c "Ой, э-э, прости, я..."
    "Чёрт, я слишком переживаю. Ничего страшного, если спрошу, да?"
    mc.c "Я просто подумал... Ты в последнее время часто остаёшься у меня, да?"
    show katie neutral talk
    katie.c "Хм, пожалуй. Я тебе мешаю?"
    show katie neutral
    mc.c "Нет, конечно! Просто... Тебе нравится у меня? Тебе лучше у меня, чем у себя?"
    show katie smile talk
    katie.c "Здесь уютно, конечно. Но дому не помешал бы небольшой уход~"
    show katie smile
    mc.c "Или тебе удобнее добираться отсюда на работу?"
    show katie thinking
    katie.c "Хм... Примерно одинаково, разницы почти нет. Но из бара к тебе чуть быстрее."
    show katie neutral talk
    katie.c "К чему эти странные вопросы, милый?"
    show katie neutral
    "Ладно, хватит глупостей... Я этого хочу."
    mc.c "Прости, я хотел сказать..."
    mc.c "Ты бы хотела... сделать наши отношения более постоянными? Переехать ко мне..."
    show katie tease talk
    katie.c "Милый~ Ты спрашиваешь, не хочу ли я переехать к тебе~?"
    show katie tease
    mc.c "...Очень неуклюже. Да."
    show katie tease talk
    katie.c "Хе-хе~ Чего ты так нервничаешь?"
    mc.c "Не знаю. Ты ведь можешь не захотеть, и это было бы совершенно нормально."
    show katie tease
    if(len(girlsAlreadyMovedIn) > 0):
        mc.c "Ты же знаешь, [len(girlsAlreadyMovedIn)] других девушек уже почти переехали ко мне, хотя ты, возможно, ещё не со всеми познакомилась..."
        if(molly.movedIn and katieMollyDuoStoryEvent1.unlocked):
            mc.c "Ну, Молли ты уже знаешь."
            show katie tease talk
            katie.c "О да~ Будет здорово видеться с ней чаще."
            show katie tease
        if(zoe.movedIn and katieZoeDuoStoryEvent1.unlocked):
            mc.c "Зои уже переехала. Кажется, ты иногда видишь её в баре."
            show katie smile talk 2
            katie.c "Хе-хе~ Да, она забавная."
            show katie smile
        mc.c "Тебя это... устраивает?"
        show katie smile talk
        katie.c "Да, конечно, милый. Я всё понимаю."
    show katie tease talk
    katie.c "Попробуй ещё раз~"
    show katie tease
    mc.c "*Кхм* Итак... Кэти... Позволь официально спросить..."
    mc.c "Ты хочешь переехать ко мне?"
    show katie smile talk 2
    katie.c "Милый... Я..."
    show katie joy
    katie.c "Да! Конечно, да!"
    show katie tease talk
    katie.c "Я всё ждала, вдруг мы... Может, мне самой спросить? Он собирается?"
    show katie joy
    katie.c "Я с удовольствием!"
    hide katie with dissolve
    show katie kiss with dissolve
    katie.c "М-м~"
    "Кэти бросается мне на руки и прижимается мордочкой к моим губам."
    "Я крепко обнимаю её, и мы страстно целуемся."
    show katie hug with dissolve
    katie.c "Ох, милый, я так счастлива~"
    mc.c "Наверное, надо было спросить раньше... Я ни секунды не сомневался."
    katie.c "Не переживай. Думаю, ты правильно сделал, что подождал. Кто знает... Но теперь мы готовы~"
    mc.c "Ещё бы. Не могу дождаться."
    hide katie with dissolve
    show katie tease with dissolve
    mc.c "Как ты хочешь это устроить? А что насчёт твоего дома?"
    show katie thinking
    katie.c "Ну... Надо проверить договор. Наверное, он ещё не скоро закончится."
    show katie smile talk 2
    katie.c "Но это хорошо! Я смогу постепенно перевезти вещи и всё рассортировать. Нам ведь не понадобится ещё больше мебели! Хе-хе~"
    katie.c "Я не против дождаться конца аренды, ничего страшного."
    show katie joy
    katie.c "Но я хочу переехать как можно скорее!"
    mc.c "Я тоже. Чем могу помочь?"
    show katie smile talk
    katie.c "Дай мне несколько дней всё уладить и собрать самое нужное... Решить, что делать с остальным..."
    show katie smile talk 2
    katie.c "Остальное перевезу постепенно."
    show katie smile
    mc.c "Я приеду на машине, так что бери с собой сколько угодно."
    show katie tease talk
    katie.c "О, здорово~ Хе-хе~"
    scene black with fade
    "Вот и всё. Она согласилась!"
    "Мы выбрали удобный день, я помогу ей перевезти вещи, и с этого момента... Она дома."
    "Договорились. Не забудь внести в расписание!"

    return

label katieLikeEvent4(fromGallery):
    $ location_home.showBackground()
    call playMusic(heartTheme) from _call_playMusic_171
    "Я так взволнован. Сегодня Кэти наконец-то официально переезжает ко мне."
    "Давно ли это назревало? Или я просто так сильно влюблён... Сейчас всё кажется правильным."
    "Она тоже была очень рада. Я счастлив. Вдруг она решит, что ещё рано, или захочет остаться у себя..."
    "Сегодня утром я заеду за ней на машине. Думаю, у неё всего несколько коробок. Мы ведь пока не объединяем два целых дома."
    "Пора отправляться."
    scene black with fade
    "..."
    scene katielivingroom with fade
    "Я захожу и вижу, как Кэти вытирает пыль с вещей и складывает их в картонную коробку."
    mc.c "Доброе утро, Кэти!"
    show katie tease talk with dissolve
    katie.c "[mc.name]!"
    show katie tease
    "Она торопливо подходит ко мне."
    hide katie with dissolve
    show katie kiss with dissolve
    katie.c "Муа~"
    show katie hug with dissolve
    katie.c "И тебе доброе утро!"
    hide katie with dissolve
    show katie joy with dissolve
    katie.c "Ой, милый, я так волнуюсь!"
    show katie tease talk
    katie.c "Я почти не спала этой ночью, так переживала!"
    show katie tease
    mc.c "Я тоже. Честно говоря, не мог дождаться."
    mc.c "Как продвигается?"
    show katie smile talk 2
    katie.c "Осталось совсем немного... Уже собрала часть одежды и всякие мелочи..."
    show katie tease talk
    katie.c "А здесь кухонные вещи. Твоей кухне не помешала бы новая посуда. У тебя почти ничего нет!"
    show katie tease
    mc.c "Виновен. Вообще-то поэтому я и зову тебя к себе."
    show katie smile talk
    katie.c "Ой, перестань~ Хе-хе~"
    show katie smile
    mc.c "Тебе помочь?"
    show katie thinking
    katie.c "Не особо... Это последняя коробка. Если что-то забуду, заберу позже."
    mc.c "А что будешь делать с мебелью?"
    show katie smile talk
    katie.c "Вообще многое уже было в доме. Из моего только несколько небольших вещей."
    katie.c "Может, я со временем привезу ещё немного мебели, если у тебя найдётся место?"
    show katie smile
    mc.c "Думаю, моему дому не помешает немного женского уюта..."
    show katie tease talk
    katie.c "Совершенно верно, молодой человек~ Хм-хм~"
    show katie smile talk 2
    katie.c "Остальное продам. Это же не семейные реликвии."
    katie.c "К тому же давно пора избавиться от лишнего. Я с нетерпением жду новую главу~ Начать с чистого листа, да?"
    show katie smile
    mc.c "Для нас обоих. Ничего лучше не придумать."
    hide katie with dissolve
    show katie hug with dissolve
    "Я крепко притягиваю Кэти к себе."
    katie.c "О-ох~"
    mc.c "Теперь я смогу делать это гораздо чаще..."
    show katie kiss with dissolve
    katie.c "М-м~"
    show katie hug with dissolve
    katie.c "Хе-хе~ Я могла бы к этому привыкнуть~"
    scene black with fade
    "Помогая ей упаковать последние вещи, мы загружаем машину и отправляемся домой. В наш новый общий дом."
    scene katielikeevent4i1 with fade
    pause
    katie.c "Фух~"
    mc.c "Вот и последние две."
    katie.c "Ага! Дай отдышаться. Я собирала вещи с самого утра. Разобрать их можно потом."
    mc.c "Конечно. Всё, теперь ты официально переехала."
    katie.c "Хе-хе~ Да, правда..."
    katie.c "Мы и правда здесь... И правда делаем это."
    mc.c "Теперь не передумаешь. Я тебя обратно не повезу."
    katie.c "Хе-хе~ Конечно нет, милый. Просто..."
    scene katielikeevent4i2 with fade
    pause
    katie.c "Я не могла представить такое... Ещё недавно это казалось несбыточной мечтой."
    katie.c "Что кто-нибудь... выберет меня."
    mc.c "Кэти..."
    katie.c "Не думала, что всё обернётся так... В такой неожиданной упаковке."
    mc.c "Человек?"
    katie.c "Хе-хе~ Ну да... Такой молодой, обаятельный, красивый, добрый, заботливый мужчина..."
    mc.c "Уже понял, что это точно не я."
    katie.c "Тише, милый~"
    "Мы медленно наклоняемся друг к другу."
    scene katielikeevent4i3 with fade
    pause
    katie.c "М-м~"
    "Кэти обнимает меня и притягивает к себе."
    "Я крепко прижимаю её, показывая, что я рядом."
    "Теперь мы вместе. Всё будет хорошо."
    scene katielikeevent4i2 with fade
    pause
    mc.c "Я люблю тебя, Кэти."
    katie.c "Я тоже тебя люблю, милый~"
    mc.c "Как отпразднуем? Хочешь сходить куда-нибудь поесть?"
    katie.c "Хм... Я бы хотела чего-нибудь вкусненького... Но..."
    katie.c "Мне хочется просто остаться дома. Только мы вдвоём и ленивый день, понимаешь?"
    mc.c "Мне нравится такой план. Закажем что-нибудь."
    katie.c "О-о, замечательно~"
    scene black with fade
    "Мы решаем сегодня расслабиться, а дела оставить на потом."
    scene katielikeevent4i4 with fade
    pause
    "Я заказываю еду, и мы устраиваемся на диване. Впервые в нашем теперь уже {i}общем{/i} доме."
    "Кэти включает фильм, который мы можем посмотреть. Будем перекусывать и болтать."
    "Пока фильм идёт, мы обнимаемся, и я предлагаю ей сесть ко мне на колени."
    katie.c "Хе-хе~ Как же хорошо."
    mc.c "Когда захочешь."
    katie.c "Кажется, я буду проситься каждый вечер~"
    scene katielikeevent4i5 with fade
    pause
    "Я нежно глажу её по голове, и она довольно мурлычет."
    katie.c "М-м~"
    "Теперь она рядом со мной. Всё правильно. Будто именно так и должно быть."
    mc.c "Я люблю тебя, Кэти."
    katie.c "Я тебя тоже, милый."
    scene black with Fade(1.5, 0.0, 0.0)
    pause

    if(not fromGallery):
        $ katie.movedIn = True
        $ girlsMovingIn -= 1

    return {'time': 'Evening'}

label katieHEvent7(fromGallery):
    call playMusic(barTheme) from _call_playMusic_172
    scene katiehevent7i1 with fade
    pause
    "Проходя мимо, я слышу, как набирается ванна."
    "Заглянув за угол, я вижу, как Кэти проверяет воду."
    katie.c "М-м-м~"
    "Именно в такие моменты я понимаю, что теперь она живёт здесь. Чувствует себя как дома."
    "Я вижу её по утрам, мы вместе готовим и целуемся на ночь."
    "Ей здесь уютно. Это всё, чего я хочу."
    "Её милая попка покачивается из стороны в сторону, за ней большой пушистый хвост..."
    "Не успеваю опомниться, как уже захожу внутрь."
    scene katiehevent7i2 with fade
    pause
    katie.c "О-ох! Милый, я не услышала, как ты вошёл."
    mc.c "Ой, прости, сам не заметил, как зашёл. Меня притянуло сюда..."
    katie.c "Хе-хе~ Ну что мне с тобой делать~"
    katie.c "День был долгий, я собиралась подольше полежать в ванне."
    mc.c "Тяжёлый день? Проблемы на работе?"
    katie.c "Нет, просто немного устала..."
    mc.c "А-а... Я могу чем-то помочь?"
    katie.c "Ну, скажу тебе, чего мы ещё не делали. Это было бы приятно..."
    katie.c "Хочешь... принять ванну вместе?"
    mc.c "Надеялся, что ты предложишь..."
    katie.c "Я так и думала, милый~"
    scene black with fade
    "Раздевшись, мы забираемся в ванну."
    scene katiehevent7i3 with fade
    pause
    "Я сажусь, а Кэти устраивается между моих ног."
    "Она прислоняется спиной к моей груди и с выдохом расслабляет плечи."
    "Хорошо, что я взял большую ванну именно для такого случая."
    katie.c "М-м~"
    katie.c "Хе-хе~ Как приятно~"
    mc.c "Для этого я и купил такую большую ванну."
    katie.c "Отличная идея, милый. Я могла бы к этому привыкнуть."
    "Я обнимаю её и провожу руками по мокрой шерсти — она всё такая же шелковистая."
    mc.c "Дома всё хорошо? Уже освоилась?"
    katie.c "Конечно, милый! Мне и раньше нравилось у тебя. Здесь уютно!"
    katie.c "Ведь не так уж многое изменилось, да? Просто я теперь чаще здесь."
    mc.c "Да, но я так рад, что ты рядом. Хочу, чтобы это был и твой дом."
    katie.c "Хе-хе~ Спасибо, милый. Я люблю тебя."
    katie.c "Но на кухне кое-чего не хватает. Я отметила несколько вещей, которые надо заменить, когда переезжала."
    mc.c "Конечно. Ты лучше знаешь. Сходим за покупками на выходных?"
    katie.c "Давай~"
    "Мы только забрались в ванну, но уже чувствуя её волосы у лица, я ощущаю такой сладкий аромат."
    "И то, что у меня между ног, тоже чувствует себя прекрасно. Её пышная попка прижата к моему паху."
    "Обнимая Кэти, я не могу удержаться и блуждаю руками по её телу."
    katie.c "[mc.name], ты сжимаешь мне живот..."
    mc.c "Одно из моих любимых занятий."
    katie.c "Хм... Ты такой странный..."
    mc.c "Ничего странного. Ты мягкая, тебя приятно обнимать."
    "Моя рука скользит по её талии. Она слегка подрагивает, когда я глажу живот."
    "И, конечно, нужно добраться до этой груди."
    katie.c "М-м~ Я так и думала, что всё к этому идёт..."
    "Тёплая ванна, аромат Кэти, её тело прижимается ко мне... Я обожаю её прикосновения."
    mc.c "После тяжёлого дня я знаю, что поможет тебе расслабиться."
    katie.c "М-м~?"
    call playMusic(sexyTheme) from _call_playMusic_173
    image katiesex bath fingering 1 = Movie(play="images/characters/katie/hscenes/bathFingering/part1.webm")
    show katiesex bath fingering 1 with fade
    pause
    "Я провожу рукой чуть ниже по её животу и нежно касаюсь клитора кончиками пальцев."
    katie.c "О-ох~ М-м~ [mc.name]~"
    katie.c "М-м~ Приятно~"
    "Я обхватываю её грудь и нежно провожу большим пальцем по соску. Кэти слегка вздрагивает в моих объятиях."
    katie.c "А-а~! Милый..."
    mc.c "Расслабься. Позволь мне помочь."
    katie.c "М-м~ Я... О-о~ Пожалуйста~"
    "Я чувствую её тихое мурлыканье спиной, а её бёдра слегка покачиваются в такт движениям моей руки."
    "Она приподнимает бёдра навстречу моей ладони, позволяя ласкать её и проводить пальцами по складкам киски."
    katie.c "М-м-м~ О-о~ Да~ Милый~"
    mc.c "Ещё?"
    katie.c "А-а~ Продолжай~ Не останавливайся~"
    image katiesex bath fingering 2 = Movie(play="images/characters/katie/hscenes/bathFingering/part2.webm")
    show katiesex bath fingering 2 with fade
    pause
    "Подготовив её, я скольжу внутрь и ввожу два пальца в горячую киску."
    katie.c "А-а~ А-а~ О-о~"
    katie.c "М-м~ Да, [mc.name]~ М-м~"
    "Она прижимает мою руку к своей груди, извивается на моих коленях и выгибает спину."
    "Она хватается за мою руку, словно удерживая меня, и просит движениями пальцев ласкать её сильнее."
    mc.c "Хорошо?"
    katie.c "А-а~ Да~ Да-а~"
    katie.c "О-о-о~"
    "Её стоны становятся громче и разносятся по кафельной ванной."
    "Она полностью тает в моих объятиях, погружаясь в наслаждение от моих ласк."
    "Она широко раздвигает ноги, приглашая меня. Бёдра покачиваются у моего паха, а киска подрагивает, когда я двигаю пальцами."
    katie.c "А-а~ Милый~ А-а~ Я почти..."
    katie.c "Я..."
    "Последними быстрыми движениями я ввожу и вывожу пальцы, щекоча клитор и доводя её до оргазма."
    scene katiebathfingeringfinish1 with fadewhite
    pause
    katie.c "О-о-о-о-о~!"
    "Кэти вскрикивает от оргазма, выгибается, запрокидывает голову и прижимается ко мне."
    "Даже сквозь воду я чувствую, как она оставляет немного жидкости на моих пальцах."
    "Я прижимаюсь к её обнажённой шее и глубоко целую, пока она откидывается в экстазе. Я зажимаю сосок, а её дыхание сбивается."
    katie.c "А-а-а~"
    katie.c "Хо-о~ Хо-о~ Боже..."
    mc.c "Угу..."
    katie.c "А-а~ А-а~ Милый~"
    katie.c "Это было... М-м~ Так хорошо~"
    scene katiehevent7i3 with fade
    pause
    "Она откидывается на меня, тяжело дыша."
    mc.c "Расслабилась?"
    katie.c "А-а~ «Расслабилась»... Не совсем подходящее слово..."
    katie.c "Но ничего себе~ Как ты так хорошо это делаешь?"
    mc.c "Наверное, что-то в воде..."
    katie.c "М-м~ Если так... Надо устраивать такое регулярно..."
    mc.c "С удовольствием."
    "Немного придя в себя, Кэти опускается поглубже в воду и позволяет обнять себя."
    "Мы ещё немного лежим в ванне и говорим о прошедшем дне."

    if(not fromGallery):
        $ katie.addLove(1)

    return
