init offset = 3

default sarahAliceDuoStoryEvent1 = Event('Сара и Алиса', 'sarahAliceDuoStoryEvent1', [sarah, alice], 0, 0, [sarahHEvent2, aliceHEvent2], location_park)
default sarahAliceDuoStoryEvent2 = Event('Кошки и собаки', 'sarahAliceDuoStoryEvent2', [sarah, alice], 0, 0, [sarahAliceDuoStoryEvent1, sarahHEvent3, aliceHEvent3], location_cafe)
default sarahAliceDuoHEvent1 = Event('Особое угощение', 'sarahAliceDuoHEvent1', [sarah, alice], 0, 0, [sarahAliceDuoStoryEvent2, sarahHEvent4, aliceHEvent4], location_bar, ['Evening', 'Night'])
default sarahAliceDuoHEvent2 = Event('Совместная подготовка', 'sarahAliceDuoHEvent2', [sarah, alice], 0, 0, [sarahAliceDuoHEvent1, sarahHEvent5, aliceHEvent5], location_town, ['Evening', 'Night'])

label sarahaliceSexSelect:
    hide screen mainUi
    image sarahalice idle = Movie(play="images/characters/sarahalice/sexWaiting.webm")
    show sarahalice idle with fade
    call screen sarahaliceSexSelectScreen
    call endScene(targetLocation = location_home) from _call_endScene_21

screen sarahaliceSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(sarahAliceDuoHEvent1.unlocked or persistent.debugMode):
                textbutton 'Минет вдвоём' keysym str(1):
                    action [Jump('sarahAliceBlowjob')]
            else:
                textbutton 'Закрыто'
            if(sarahAliceDuoHEvent2.unlocked or persistent.debugMode):
                textbutton 'Тройничок' keysym str(2):
                    action [Jump('sarahAliceThreesome')]
            else:
                textbutton 'Закрыто'
            textbutton 'Выход' keysym str(3):
                action [Hide('sarahaliceSexSelectScreen'), Return()]

label sarahAliceBlowjob:
    image sarah alice blowjob start = Image("images/characters/sarahalice/blowjob/start.webp")
    show sarah alice blowjob start with fade
    pause
    image sarah alice blowjob part 1 = Movie(play="images/characters/sarahalice/blowjob/part1.webm")
    show sarah alice blowjob part 1 with fade
    pause
    image sarah alice blowjob part 2 = Movie(play="images/characters/sarahalice/blowjob/part2.webm")
    show sarah alice blowjob part 2 with fade
    pause
    image sarah alice blowjob part 3 = Movie(play="images/characters/sarahalice/blowjob/part3.webm")
    show sarah alice blowjob part 3 with fade
    pause
    image sarah alice blowjob part 4 = Movie(play="images/characters/sarahalice/blowjob/part4.webm")
    show sarah alice blowjob part 4 with fade
    pause
    image sarah alice blowjob part 5 = Movie(play="images/characters/sarahalice/blowjob/part5.webm")
    show sarah alice blowjob part 5 with fade
    pause
    image sarah alice blowjob end 1 = Image("images/characters/sarahalice/blowjob/end1.webp")
    show sarah alice blowjob end 1 with fadewhite
    pause
    image sarah alice blowjob end 2 = Image("images/characters/sarahalice/blowjob/end2.webp")
    show sarah alice blowjob end 2 with fade
    pause
    jump sarahaliceSexSelect

label sarahAliceThreesome:
    scene sarahalicethreesomestart1 with fade
    pause
    image sarahalice sarah fuck 1 = Movie(play="images/characters/sarahalice/threesome/sarahfuck1.webm")
    show sarahalice sarah fuck 1 with fade
    pause
    image sarahalice sarah fuck 2 = Movie(play="images/characters/sarahalice/threesome/sarahfuck2.webm")
    show sarahalice sarah fuck 2 with fade
    pause
    image sarahalice sarah fuck 3 = Movie(play="images/characters/sarahalice/threesome/sarahfuck3.webm")
    show sarahalice sarah fuck 3 with fade
    pause
    scene sarahalicesarahfinish with fadewhite
    pause
    image sarahalice alice fuck 1 = Movie(play="images/characters/sarahalice/threesome/alicefuck1.webm")
    show sarahalice alice fuck 1 with fade
    pause
    image sarahalice alice fuck 2 = Movie(play="images/characters/sarahalice/threesome/alicefuck2.webm")
    show sarahalice alice fuck 2 with fade
    pause
    image sarahalice alice fuck 3 = Movie(play="images/characters/sarahalice/threesome/alicefuck3.webm")
    show sarahalice alice fuck 3 with fade
    pause
    scene sarahalicealicefinish with fadewhite
    pause
    jump sarahaliceSexSelect

label sarahAliceDuoStoryEvent1(fromGallery):
    $ location_park.showBackground()
    show alice smile with dissolve
    call playMusic(chillTheme) from _call_playMusic_315
    "Сегодня я встретился с Алисой в парке, чтобы поболтать, пока у неё выходной."
    "Могу отлучиться когда захочу — вот привилегия владельца бизнеса."
    "Мы сидим рядом на скамейке и рассказываем, как прошла неделя."
    "Как всегда, у неё целая энциклопедия тем. Она всегда так увлекается."
    show alice smile talk
    alice.c "Я ищу следующее издание того учебника."
    show alice smile talk 2
    alice.c "Не мог бы ты посмотреть? Если где-нибудь увидишь, скажи мне."
    show alice smile
    "Я не особо хожу по книжным..."
    mc.c "Уверен, можно заказать в интернете. Давай посмотрим."
    show alice neutral talk
    alice.c "В интернете? Это опять на компьютере, да?"
    show alice neutral
    "Иногда забываю, что человек нашего поколения может быть настолько неграмотен в компьютерах."
    mc.c "Ты же пользуешься телефоном. Это тоже компьютер."
    show alice thinking
    alice.c "Я понимаю приложение для сообщений, но на этом мои знания заканчиваются."
    mc.c "Давай посмотрим на моём компьютере, я покажу."
    show alice smile talk
    alice.c "Было бы здорово, спасибо."
    show alice smile
    "Забавная девушка..."
    "Мы сидим рядом. В какой-то момент я кладу руку поверх её на скамейке."
    "Она нечасто сама проявляет инициативу, но, к счастью, привыкла к нашим публичным проявлениям чувств и не жалуется."
    sarah_unknown "О, привет, [mc.name]!"
    "А?"
    show alice neutral at twoPersonLeft with ease
    show sarah smile at twoPersonRight with dissolve
    "Это Сара. Похоже, она проходила мимо."
    mc.c "О, привет, Сара."
    show sarah smile talk 2
    sarah.c "Кто твоя подруга?"
    show sarah smile
    mc.c "О, это..."
    "Я собираюсь представить Алису, но замечаю, что мы очень явно держимся за руки."
    call mcFretAboutPolyamory from _call_mcFretAboutPolyamory_4
    mc.c "Я, э-э... А..."
    "Не могу подобрать слова."
    show alice neutral talk
    alice.c "Меня зовут Алиса."
    show alice neutral
    show sarah smile talk
    sarah.c "Привет, я Сара."
    show sarah smile
    "Мы всё ещё держимся за руки у неё на виду."
    "Она наверняка уже заметила, а они просто... разговаривают?"
    show sarah smile talk 2
    sarah.c "Чем занимаетесь?"
    show sarah smile
    show alice smile talk
    alice.c "Мы как раз обсуждали материалы о средневековых религиозных текстах. Тебя интересует эта тема?"
    show alice smile
    show sarah surprise
    sarah.c "Э-э..."
    show sarah thinking
    sarah.c "Не особо... Звучит... весело?"
    show alice smile talk 2
    alice.c "О, это, безусловно, увлекательно. Могу поделиться материалами, если хочешь."
    show alice smile
    show sarah smile talk 2
    sarah.c "Э-э, это было свидание? Я ничего не прервала?"
    show sarah smile
    show alice thinking
    alice.c "Не уверена. [mc.name], это считается одним из наших «свиданий»? Всё произошло довольно спонтанно."
    "Теперь всё раскрыто. Что мне сказать?"
    if(not mc.polyamoryExplained):
        "Что происходит? Я сижу в полном оцепенении."
        "Лихорадочно пытаюсь придумать, как это объяснить."
        mc.c "Сара, я могу объяснить..."
        show alice neutral
        show sarah neutral talk
        sarah.c "А? Что объяснить?"
        show sarah neutral
        mc.c "Я... Ну... Мы..."
        "Обе смотрят на меня скорее с любопытством. Неужели я так сильно предал их доверие, что они не могут поверить?"
        mc.c "Сара, Алиса, мне так жаль... Но... я... встречаюсь с вами обеими."
        mc.c "Когда всё было несерьёзно, я ходил на свидания с несколькими девушками. А потом отношения развивались, и я не мог выбрать."
        mc.c "Простите..."
        sarah.c "..."
        alice.c "..."
        "Они переглядываются."
        show sarah neutral talk
        sarah.c "Алиса, ты понимаешь, из-за чего он так паникует?"
        show sarah neutral
        show alice thinking
        alice.c "Я не была уверена, но теперь догадываюсь. Судя по тому, что я знаю о человеческой культуре..."
        show alice neutral talk
        alice.c "В подавляющем большинстве случаев люди состоят в отношениях только с одним партнёром. Несколько партнёров одновременно осуждаются."
        show alice neutral
        show sarah surprise
        sarah.c "О, точно! Выбираешь одного на всю жизнь, да?"
        "Что происходит? Я что-то упустил?"
        mc.c "Ч-что ты имеешь в виду?"
        show sarah smile talk
        sarah.c "Обычно встречаются с одним человеком за раз, верно? Это считается нормой. Ты думал, что...?"
        show sarah smile
        "Я не могу осмыслить происходящее. Они обе всё понимают, но им всё равно? Человеческая культура? Что?"
        show sarah smile talk 2
        sarah.c "Хватит паниковать. Здесь вполне нормально встречаться с несколькими людьми."
        show sarah smile
        mc.c "А? Это... особенность антропоморфов?"
        show sarah smile talk
        sarah.c "Большинство антропоморфов, которых я встречала, так и поступают. Это норма."
        show sarah thinking
        sarah.c "Как в долгих, так и в коротких отношениях... Иметь детей от нескольких партнёров тоже вполне обычно."
        show sarah smile
        mc.c "Это правда, Алиса?"
        show alice neutral talk
        alice.c "Думаю, да. Такова распространённая культура отношений среди антропоморфных животных."
        show alice thinking
        alice.c "Я предполагала, что люди могут относиться к этому иначе."
        show alice neutral
        show sarah tease talk
        sarah.c "Удивлена, что ты раньше не понял, глупыш. Я видела, как ты флиртовал с несколькими девушками..."
        show sarah tease
        mc.c "Т-ты видела?"
        mc.c "И... ничего не сказала?"
        show sarah tease talk
        sarah.c "Не думала, что придётся."
        sarah.c "Так ты встречался с несколькими девушками, боясь разбить их бедные сердечки?"
        show sarah tease
        mc.c "Я... не думал, что..."
        "Она поддразнивает меня, но права. Что я вообще делал?"
        "Как бы я с этим справился?"
        "Если всё это правда, значит ли это...?"
        mc.c "Значит... Вы обе...?"
        show sarah smile talk 2
        sarah.c "О, я? Нет, я ни с кем больше не встречаюсь."
        show sarah smile talk
        sarah.c "Мне это всегда казалось лишней морокой. У кого на это время? Мне и тебя хватает, [mc.name]."
        show sarah smile
        mc.c "Алиса?.."
        show alice smile talk
        alice.c "Ты знаешь, ты мои первые и единственные отношения, [mc.name]. Мне казалось, это очевидно. Прости, если не объяснила."
        show alice smile
        call mcPolyamoryExplainedConclusion from _call_mcPolyamoryExplainedConclusion_4
    else:
        mc.c "Э-э, Сара. Это Алиса, мы уже какое-то время встречаемся."
        mc.c "А Алиса, я тоже уже какое-то время встречаюсь с Сарой."
        show sarah smile talk
        sarah.c "Приятно познакомиться."
        show sarah smile
        show alice smile talk 2
        alice.c "Взаимно."
        show alice smile
        mc.c "Я не хотел ничего скрывать от вас. Прости."
        show sarah neutral talk
        sarah.c "За что ты извиняешься? Ты же знаешь..."
        show sarah neutral
        mc.c "Знаю, но мне всё ещё неловко. Я просто не хочу никого обидеть."
    call playMusic(chillTheme) from _call_playMusic_316
    mc.c "То есть, вы обе не против?"
    show sarah smile talk 2
    if(sarah.polyamoryExplained):
        sarah.c "Ты и так знаешь, что я об этом думаю..."
    sarah.c "Да не парься, чувак! Только не забывай уделять мне время, ладно?"
    show sarah smile
    show alice smile talk 2
    if(alice.polyamoryExplained):
        alice.c "Мы уже говорили об этом, [mc.name], так что..."
    alice.c "Я ценю твою заботу, но не волнуйся. Я и так всё понимала."
    show alice smile
    "Похоже, обе дали своё благословение. Как же мне повезло."
    show sarah smile talk 2
    sarah.c "Так, чем ты занимаешься, Алиса?"
    show sarah smile
    show alice smile talk
    alice.c "Я работаю в городской библиотеке. А ты, Сара?"
    show alice smile
    show sarah smile talk 2
    sarah.c "Я учусь в колледже, изучаю географию."
    show sarah smile
    show alice smile talk 2
    alice.c "О, прекрасно, будущий учёный. Наверное, часто бываешь в нашей библиотеке. Может, мы уже встречались?"
    show alice smile
    show sarah bashful talk
    sarah.c "Э-э... Ха-ха... Ну..."
    show sarah bashful
    "Две красавицы, с которыми я встречаюсь, непринуждённо болтают друг с другом."
    "Я снова такой везучий. Вот это жизнь."
    "Всё ещё трудно поверить. Как всё сложится?"
    show sarah tease talk
    sarah.c "Ладно, оставлю вас, голубки."
    show sarah smile talk 2
    sarah.c "Как-нибудь все вместе погуляем, хорошо?"
    show sarah smile
    show alice smile talk 2
    alice.c "Да, с удовольствием."
    show alice smile
    show sarah joy
    sarah.c "Пока, ребята!"
    hide sarah with dissolve
    show alice at center with ease
    show alice smile talk
    alice.c "Она милая. Однажды я хотела бы обсудить с ней некоторые темы."
    show alice smile
    mc.c "При всём уважении к Саре, ты, наверное, поразишь её своими знаниями. Ты каждый день поражаешь меня."
    scene black with fade
    "Мы завершаем день и прощаемся."
    "Ну вот, я прояснил отношения между мной, Алисой и Сарой. Что теперь нас ждёт?"

    if(not fromGallery):
        $ sarah.polyamoryExplained = True
        $ alice.polyamoryExplained = True
        $ mc.polyamoryExplained = True
        $ sarah.knowsDating = list(set(sarah.knowsDating + [alice]))
        $ alice.knowsDating = list(set(alice.knowsDating + [sarah]))

    return

label sarahAliceDuoStoryEvent2(fromGallery):
    $ location_cafe.showBackground()
    "Я собирался зайти в кафе перекусить."
    "И вдруг вижу неожиданное, но очень трогательное зрелище."
    call playMusic(funnyTheme) from _call_playMusic_317
    show sarah neutral at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    pause
    "Сара и Алиса сидят за столиком. Две красавицы, с которыми мне каким-то образом повезло..."
    "Они познакомились совсем недавно, по моей вине. Интересно, успели ли они узнать друг друга?"
    "Алиса увлечённо рассказывает. Она либо молчит, либо говорит без умолку. Наверняка о какой-то из своих {i}тем{/i}."
    "Сара вежливо кивает, но выглядит немного ошеломлённой. Пора её спасать."
    mc.c "Привет, девочки!"
    show sarah smile talk 2
    sarah.c "[mc.name]! Привет!"
    show sarah smile
    show alice smile talk
    alice.c "Здравствуйте."
    show alice smile
    mc.c "Что тут происходит? Встречаетесь без меня?"
    show sarah tease talk
    sarah.c "А ты разве не так делал всё это время?"
    show sarah tease
    mc.c "Э-э, ладно, поймала."
    show sarah smile talk 2
    sarah.c "Зашла выпить и увидела Алису за книжкой в углу. Решила поздороваться."
    show sarah smile
    show alice smile talk
    alice.c "Именно так."
    show alice smile
    show sarah neutral talk
    sarah.c "Но это было двадцать пять минут назад."
    show sarah bashful talk
    sarah.c "Я совершила ошибку — спросила про её книгу. Она объясняет уже вечность, а я ничего не понимаю..."
    show sarah bashful
    show alice neutral talk
    alice.c "На каком именно моменте ты потеряла нить? Вернуться к предыдущей части объяснения? Видишь ли..."
    show alice neutral
    show sarah surprise
    sarah.c "[mc.name]~ Спаси меня... Она всё говорит и говорит!"
    mc.c "Ха-ха, не волнуйся, Сара. Уверен, у всех так с Алисой. Она кладезь редких знаний."
    show alice neutral talk
    alice.c "Это правда, [mc.name]? Тебе трудно понимать мои рассуждения?"
    show alice neutral
    mc.c "Ну... скажем, я понимаю примерно половину."
    show alice neutral talk
    alice.c "...Какую половину?"
    show alice neutral
    show sarah smile
    "..."
    show sarah joy
    sarah.c "А-ха-ха! Ладно, значит, дело не только во мне."
    show sarah smile talk 2
    sarah.c "Прости, Алиса, не хотела смеяться. Ты просто забавная! В хорошем смысле!"
    show sarah smile
    show alice thinking
    alice.c "Забавная?.. Я не пыталась шутить."
    mc.c "Ты приятная в общении, верно?"
    show sarah smile talk 2
    sarah.c "Ага! Может, я не всё понимаю, но ты классная, Алиса."
    show sarah smile
    show alice smile talk
    alice.c "Классная?.. Теперь я тоже не совсем понимаю. Но раз ты так говоришь..."
    show alice smile
    mc.c "Так приятно видеть, что вы ладите. Я не знал, как вы... ну, напряжённость."
    show sarah neutral talk
    sarah.c "А с чего бы ей быть? Мы уже говорили, что такой формат отношений нас устраивает..."
    show sarah neutral
    mc.c "Не в этом дело. Просто... Как сказать... Разница характеров?"
    show sarah neutral talk
    sarah.c "Ты понимаешь, о чём этот идиот, Алиса?"
    show sarah neutral
    show alice neutral talk
    alice.c "В данном случае нет, я не понимаю ход мыслей [mc.name]."
    show alice neutral
    mc.c "Да ладно, вы же знаете: кошки... и собаки..."
    "..."
    "Похоже, шутка провалилась."
    show sarah mad talk
    sarah.c "Боже... Тупая шутка. Ты что, ребёнок?"
    show sarah mad
    show alice neutral talk
    alice.c "[mc.name], полагаю, ты опираешься на преувеличенный и безосновательный стереотип об антропоморфах, распространённый в художественных произведениях."
    show alice neutral
    show sarah mad talk
    sarah.c "Он знает, Алиса, просто опять отпускает свои ужасные шутки."
    show sarah mad
    show alice thinking
    alice.c "Понятно. Да, это действительно несмешно. Сара, ты тоже сталкивалась с его попытками пошутить?"
    "Ай..."
    show sarah tease talk
    sarah.c "Ой, посмотри на него... Да, шутки у тебя плохие, но именно поэтому ты и смешной."
    show sarah tease
    show alice smile talk
    alice.c "Не расстраивайся, [mc.name]. Я выбрала тебя не за чувство юмора."
    show alice smile
    mc.c "Ладно, сдаюсь..."
    "Мы ещё немного сидим в кафе — для меня это необычно. Две девушки рядом..."
    "Особенно такие потрясающие девушки. Надеюсь, наши отношения будут такими же устойчивыми, как они говорят."
    "И девушки, кажется, тоже сближаются. Было бы здорово, если бы они подружились."
    call playMusic(heartTheme) from _call_playMusic_318
    show sarah smile talk 2
    sarah.c "Кстати, [mc.name], мы тут болтали до твоего прихода."
    show sarah tease talk
    sarah.c "О том, чем ты занимался с нами~ Обо всём этом скандальном, что ты не рассказывал~"
    show sarah tease
    mc.c "Э-э... Ну... Ты же знаешь, я не понимал..."
    show sarah tease talk
    sarah.c "Ой, [mc.name]... Так только хуже, не так ли~? Всё тайком."
    show sarah tease
    mc.c "Погоди, ты уже дразнила меня за это... Прости..."
    show sarah smile talk 2
    sarah.c "Ну-ну, извинения приняты. Мы подумали... Надо бы нам втроём чаще проводить время вместе, да?"
    show sarah smile
    mc.c "Да, такие встречи — это весело. Давайте чаще."
    show sarah tease talk
    sarah.c "Не {i}совсем{/i} такие встречи. Верно, Алиса?"
    show sarah tease
    show alice bashful
    alice.c "А... Хм..."
    show alice smile talk 2
    alice.c "Именно."
    show alice smile
    "Они что-то задумали. Я не в курсе, но, честно говоря, звучит заманчиво."
    mc.c "Вот как? Кажется, вы уже знаете, чего хотите. Можете как-нибудь это устроить."
    show sarah tease talk
    sarah.c "Ага, у меня есть несколько идей~"
    show sarah smile talk
    sarah.c "Но позже. Уверена, ты уже весь извёлся от ожидания. Мне, наверное, пора."
    show sarah smile
    show alice smile talk 2
    alice.c "Мне тоже пора, но сегодня было очень приятно. Спасибо, Сара."
    show alice smile
    show sarah joy
    sarah.c "Ой, не за что, Алиса, и тебе спасибо! Ты такая милая!"
    mc.c "Пока вы не ушли..."
    hide sarah
    hide alice 
    with dissolve
    show alice kiss with dissolve
    pause
    alice.c "*Чмок*"
    hide alice with dissolve
    show sarah kiss with dissolve
    pause
    sarah.c "Муа~"
    hide sarah with dissolve
    show alice smile at twoPersonRight
    show sarah smile at twoPersonLeft
    with dissolve
    pause
    scene black with fade
    "Мы прощаемся, и девушки уходят. Похоже, наша троица может сработать..."

    return

label sarahAliceDuoHEvent1(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_319
    "Ещё один хороший день позади. Всё шло гладко, посетителей было достаточно."
    "Думаю, скоро закончу и оставлю смену кому-нибудь из надёжных сотрудников."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "О, сообщение? Посмотрим."
    alice.c "Привет. Я задержалась на работе. Скоро пройду мимо твоего бара и подумала: может, ты там, и мы вместе пойдём домой?"
    "Как мило. После долгого дня я больше всего хочу именно этого."
    mc.c "Конечно! Скоро заканчиваю, заходи! Увидимся через минуту."
    alice.c "Отлично, скоро буду, [mc.name]."
    "Если она только что пошла домой, долго ждать не придётся. Теперь точно уйду пораньше."
    "Надо предупредить сотрудников и закончить ещё кое-какие дела. Это не займёт много времени."
    "Но тут в дверь входит ещё одна знакомая."
    show sarah smile talk 2 with dissolve
    sarah.c "Приветик~! Как дела, чувак?"
    show sarah smile
    "Она почти кричит в затихшем зале, несколько человек оборачиваются."
    mc.c "О, привет, Сара! Выпить пришла?"
    show sarah smile talk 2
    sarah.c "Не-а! Была поздняя учёба в кампусе. Иду домой, решила заглянуть и узнать, здесь ли ты."
    show sarah smile talk
    sarah.c "Подумала, может, пообщаемся или вместе пойдём домой?"
    show sarah smile
    mc.c "Я через пару минут закончу, но..."
    show sarah tease talk
    sarah.c "Но что?.. Теперь мне нужно записываться к тебе на приём, мистер Популярность?"
    show sarah tease
    mc.c "Нет-нет, Сара. Просто жду Алису. Она идёт домой, и мы собирались пойти вместе."
    show sarah joy
    sarah.c "О, здорово! Хочу снова её увидеть."
    "Я ожидал негативной реакции... Приятно, что Сара так легко к этому относится, особенно к нашим отношениям."
    show sarah smile talk
    sarah.c "Тогда подожду её, ладно?"
    show sarah smile
    mc.c "Конечно."
    hide sarah with dissolve
    "Сара садится за ближайший столик. Мне нужно закончить дела."
    "Через пару минут..."
    show alice neutral with dissolve
    "Алиса заходит и оглядывает зал."
    show alice smile
    "Увидев меня, она слегка машет рукой, но её прерывает..."
    sarah.c "Алиса! Привет!"
    show alice surprise
    "Редко можно увидеть, чтобы Алиса так вздрогнула. Сара привлекла её внимание и зовёт к своему столику."
    hide alice with dissolve
    "Я показываю, что задержусь на пару минут, и Алиса соглашается. Приятно, что они ладят."
    "Возясь с кассой, я краем глаза поглядываю на их столик."
    call playMusic(funnyTheme) from _call_playMusic_320
    show sarah smile at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    "Похоже на приятный разговор. Интересно, о чём они говорят."
    show sarah tease
    "Во время разговора Сара ловит мой взгляд, ухмыляется и жестом просит не подходить. Не хочет меня посвящать?"
    "Я продолжаю работать, но всё ещё вижу их. Сара наклоняется ближе, будто говорит тише."
    show alice neutral
    "Лицо Алисы немного напрягается, будто её удивили слова Сары. Что происходит?"
    show alice bashful
    "Алиса редко теряется, но после слов Сары начинает ёрзать."
    "..."
    show alice smile
    "...а потом она улыбается в ответ. Хотел бы знать, что происходит. Надо быстрее закончить и присоединиться."
    "..."
    "Через несколько минут я заканчиваю и подхожу."
    mc.c "Рад тебя видеть, Алиса. Прости, что задержался."
    show alice smile talk 2
    alice.c "Ничего страшного, [mc.name], ты говорил, что скоро закончишь работу. А Сара составила мне компанию. Ты не сказал, что она здесь."
    show alice smile
    mc.c "Она ещё не пришла, когда ты написала. Заявилась сразу после."
    show sarah mad talk
    sarah.c "Заявилась? Да ладно тебе!"
    show sarah mad
    "Я слегка глажу её по голове."
    show sarah smile talk
    sarah.c "Чем нас больше, тем веселее, да? Если только вы двое не..."
    show sarah smile
    mc.c "Нет, никаких особых планов, верно, Алиса? Она просто проходила мимо, хотела пойти домой вместе."
    "Алиса нерешительно кивает. Немного странно."
    "И клянусь, Сара подмигнула ей, когда я отвернулся."
    show sarah smile talk 2
    sarah.c "Ну-у... Пойдём отсюда?"
    show sarah smile
    mc.c "Конечно."
    show alice smile talk
    alice.c "Согласна."
    show alice smile
    scene black with fade
    "Мы собираем вещи и выходим на прохладный вечерний воздух."
    $ location_town.showBackground()
    show sarah smile at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    "Иду домой с двумя прекрасными женщинами... С обеими я встречаюсь. Не могу не подозревать, что у них есть скрытые намерения."
    mc.c "Позвольте полюбопытствовать: о чём вы говорили? Вы с Сарой шептались."
    show sarah tease talk
    sarah.c "Да, ты очень любопытный, [mc.name]! Ну же, прояви такт, чувак."
    show sarah tease
    mc.c "Значит, секреты? Хм..."
    show sarah tease talk
    sarah.c "Скажем так... Девичьи дела?"
    show sarah tease
    mc.c "А, универсальная отговорка. Теперь мне не подкопаться. Ловко."
    show sarah tease talk
    sarah.c "Поймал, неудачник."
    show sarah tease
    mc.c "Или могу просто спросить Алису. Не думаю, что она умеет врать."
    show alice tease
    alice.c "Хм-хм~"
    mc.c "И ты туда же? Не может быть..."
    show alice smile
    "Мы продолжаем путь домой, болтая о всякой ерунде. Но скоро нам придётся разойтись. Что будем делать?"
    show sarah smile talk 2
    sarah.c "Так... Мы подумали: может, посидим у тебя? Мы с Алисой хотим посмотреть один сериал."
    show sarah smile
    mc.c "Сомневаюсь, судя по тому, что знаю о вас обеих."
    show sarah surprise
    sarah.c "Правда! Выпьем и посмотрим телевизор после долгого дня. Да, Алиса?"
    mc.c "Теперь-то я знаю, что это ложь: Алиса почти не пьёт."
    show alice bashful
    alice.c "..."
    show alice thinking
    alice.c "Я... *кхм* согласна с Сарой. Мы это и обсуждали."
    "Наглая ложь, но меня это устраивает. Вообще, звучит здорово. Не понимаю, зачем я их дразню и почему они всё держали в секрете."
    mc.c "Ладно-ладно, располагайтесь. Всегда вам рад, не знаю, зачем притворялся иначе."
    show alice smile
    show sarah smile talk
    sarah.c "Класс!"
    scene black with fade
    "Вскоре мы добираемся домой. Девушки всё ещё ведут себя подозрительно."
    call playMusic(heartTheme) from _call_playMusic_321
    $ location_home.showBackground()
    "Мы устраиваемся, берём напитки и идём на диван включить телевизор."
    "Сара и Алиса по обе стороны от меня. От одной мысли об этом я до сих пор волнуюсь..."
    show sarah smile at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    mc.c "Ну... Что это за сериал, который нравится вам обеим? Боевик с примесью научной документалки?.."
    show sarah surprise
    sarah.c "А? Что за сериал? Не слышала о таком."
    mc.c "Уверен, такого не существует, Сара..."
    show sarah bashful talk
    sarah.c "Ой, точно..."
    show sarah smile talk
    sarah.c "Это... Э-э... Ладно, просто пролистаем и найдём... что-ни..."
    call playMusic(funnyTheme) from _call_playMusic_322
    show alice smile talk 2
    alice.c "Мы говорили о том, какие интимные вещи ты делал с каждой из нас."
    show alice smile
    show sarah surprise
    "..."
    sarah.c "А-Алиса! Как ты могла?!"
    show alice neutral talk
    alice.c "О, разве мы уже не закончили притворяться? Я думала, мы добились цели — проводили [mc.name] домой."
    show alice neutral
    show sarah bashful talk
    sarah.c "Н-ну... наверное... Но ведь было весело продолжать, да?"
    show sarah bashful
    mc.c "И всё? Я не против, просто понимаю, почему вы хотели оставить это между собой..."
    "Если спросите меня, звучит чертовски здорово."
    mc.c "Но мне любопытно. Какие-нибудь... открытия?"
    show sarah bashful talk
    sarah.c "Хм, не совсем... Просто..."
    show sarah bashful
    show alice neutral talk
    alice.c "Сара хочет сделать «минет», как она выразилась, одновременно с нами обеими. То есть двойной оральный секс, если я правильно поняла."
    show alice neutral
    show sarah surprise
    sarah.c "АЛИСА! Да ё-моё!"
    "Ну, вот теперь мне интересно. Спасибо, Алиса."
    show alice bashful talk
    alice.c "...Разве не в этом было предложение, Сара? Я так поняла..."
    show alice bashful
    show sarah bashful talk
    sarah.c "А-а~ Ладно, прости, Алиса, всё нормально... Ты ни в чём не виновата..."
    show sarah bashful
    sarah.c "Я просто предложила идею..."
    show sarah neutral talk
    show alice neutral
    sarah.c "Я хотела поговорить о том, что мы делали, понимаешь? Между девочками. А потом задумалась..."
    show sarah smile talk
    sarah.c "О том, как много ты для меня делаешь. Для нас обеих... И можно ли как-то... Ну... Втроём..."
    show sarah smile
    show alice smile
    mc.c "Быть с вами обеими — уже моя мечта. Больше я не могу и просить."
    "Но идея чертовски классная... Неужели они согласны?"
    call stopMusic from _call_stopMusic_59
    show sarah mad talk
    sarah.c "О, ладно, тогда не будем."
    show sarah mad
    "..."
    mc.c "П-погоди..."
    show sarah tease talk
    sarah.c "Хе-хе~ Лицо у тебя, [mc.name], просто чудо..."
    sarah.c "Ладно, я плохо умею ходить вокруг да около. Лучше говорить прямо."
    call playMusic(sexyTheme) from _call_playMusic_323
    show sarah tease
    "Сара кладёт руку мне на промежность. Даже от одного разговора я уже возбуждён..."
    mc.c "Алиса? Ты не против?"
    show alice smile talk 2
    alice.c "Раз она предложила... мне... любопытно."
    show alice smile
    "Невероятно."
    scene black with fade
    "По инициативе Сары девушки начинают раздеваться передо мной."
    "С небольшой помощью я высвобождаю уже готовый к делу член."
    image sarah alice blowjob start = Image("images/characters/sarahalice/blowjob/start.webp")
    show sarah alice blowjob start with fade
    pause
    "Девушки опускаются на колени у моих ног — невероятное зрелище..."
    "Алиса внимательно рассматривает меня, а Сара озорно улыбается. Их мягкая шерсть щекочет мои ноги."
    sarah.c "Кстати, Алиса... Теперь, когда вижу тебя без одежды — какая у тебя потрясающая задница."
    alice.c "Потрясающая? У меня крупноватый зад... Я стараюсь следить за фигурой."
    sarah.c "Уверена, [mc.name] это нравится... Он и твою так же любит, как мою?"
    alice.c "Любит? [mc.name] никогда такого не делал. Хотя я заметила, что ему... нравится прикасаться к моим ягодицам."
    sarah.c "Похоже, [mc.name] любит попки~"
    mc.c "Ну..."
    alice.c "Зато грудь у тебя больше моей, Сара. Может, она привлекательнее?"
    mc.c "Девушки, вы обе прекрасны..."
    sarah.c "Слышала? Как мило. Думаю, он заслужил награду~"
    alice.c "Но мне интересно, как это будет выглядеть на практике?"
    sarah.c "Не знаю... Я такого не делала... Может, попробуем лизать вместе?"
    image sarah alice blowjob part 1 = Movie(play="images/characters/sarahalice/blowjob/part1.webm")
    show sarah alice blowjob part 1 with fade
    pause
    "По инициативе Сары они вместе берутся за мой ствол."
    "Осторожно, чтобы не мешать друг другу, проводят языками вверх-вниз по бокам моего члена."
    "Сара берёт его у основания, щекоча мне яйца. Их мягкие лица и прохладные носы касаются меня."
    "Больше всего меня сводит с ума само зрелище. Невероятно."
    sarah.c "Кажется, ему нравится~"
    alice.c "А вдвоём приятнее, [mc.name]?"
    mc.c "Не могу описать... Вместе это лучше, чем по отдельности."
    image sarah alice blowjob part 2 = Movie(play="images/characters/sarahalice/blowjob/part2.webm")
    show sarah alice blowjob part 2 with fade
    pause
    "Эти две красавицы работают над моим членом, словно поклоняются ему."
    "Они покачивают потрясающими задницами, стоя передо мной на коленях, хвосты виляют. Им тоже, без сомнения, нравится."
    "Их тёплое дыхание обволакивает мой член, быстро увлажняя его слюной."
    sarah.c "Кажется, ему хочется ещё. Ты не против, Алиса?"
    alice.c "Пожалуйста."
    image sarah alice blowjob part 3 = Movie(play="images/characters/sarahalice/blowjob/part3.webm")
    show sarah alice blowjob part 3 with fade
    pause
    "Сара направляет мой член к себе, берёт головку в рот и начинает слегка покачиваться."
    sarah.c "М-м~ М-м~"
    mc.c "Чёрт, Сара..."
    alice.c "Рада видеть, что ты берёшь в рот не больше, чем я."
    "Пока Сара ласкает меня ртом, Алиса пользуется свободным местом и облизывает мои яйца."
    alice.c "Это... тоже приятно?"
    mc.c "Очень, девочки..."
    "Сара крепко держит меня за ногу и берёт в рот так глубоко, как может. Обе пары глаз смотрят на меня снизу вверх."
    sarah.c "М-м~"
    "Сара подталкивает Алису и поднимается, показывая ей мой член, словно игрушку."
    image sarah alice blowjob part 4 = Movie(play="images/characters/sarahalice/blowjob/part4.webm")
    show sarah alice blowjob part 4 with fade
    pause
    "Алиса не хочет отставать, пользуется случаем и берёт мой член в рот."
    alice.c "М-м~ А-а~"
    "Она двигает головой вверх-вниз, вздрагивая, когда берёт его глубже."
    sarah.c "Ничего себе~ Алиса... Вот это королева~"
    "Сара нежно гладит основание моего члена, и они обе атакуют его со всех сторон."
    sarah.c "Повезло мне, да?"
    mc.c "Я... Я самый везучий парень на свете."
    "Зрелище, звуки и ощущения невероятные. Я уже приближаюсь к пределу."
    alice.c "М-м~ М-м~"
    "Похоже, Алиса тоже."
    sarah.c "По твоему лицу всё понятно, чувак. Чего хочешь?"
    mc.c "Дайте... кончить на вас обеих."
    sarah.c "Парни... Думают, что всё как в порно..."
    image sarah alice blowjob part 5 = Movie(play="images/characters/sarahalice/blowjob/part5.webm")
    show sarah alice blowjob part 5 with fade
    pause
    "Я выскальзываю как раз перед оргазмом — хочу кончить на эти прекрасные лица."
    alice.c "*А-а* И-что теперь?"
    sarah.c "Сведи наши лица вместе, думаю. Ему понравится~"
    "Я уже вот-вот взорвусь."
    mc.c "...!"
    image sarah alice blowjob end 1 = Image("images/characters/sarahalice/blowjob/end1.webp")
    show sarah alice blowjob end 1 with fadewhite
    pause
    "Я мощно кончаю, заливая лица девушек."
    "Они удивлённо отшатываются, но остаются рядом и принимают сперму."
    image sarah alice blowjob end 2 = Image("images/characters/sarahalice/blowjob/end2.webp")
    show sarah alice blowjob end 2 with fade
    pause
    "Вся перепачканная, девушки откидываются назад, когда я наконец выжимаю из себя всё."
    "Сперма стекает по их лицам. Алиса собирает каплю с подбородка и рассматривает её."
    mc.c "Ох *а-а* боже..."
    sarah.c "Отличная работа, Алиса~"
    alice.c "А-а... Да."
    "Чёрт... Это было невероятно. Я умер и попал в рай? Чем я заслужил такое?"
    "Что бы я ни сделал в прошлой жизни..."
    alice.c "По твоему опыту, это необычно?"
    sarah.c "Ха-ха~ Алиса, ты такая забавная."
    sarah.c "Э-э, наверное? Вдвое веселее, правда, [mc.name]?"
    mc.c "Невероятно..."
    "Сара ухмыляется."
    sarah.c "Оставим нашего красавчика прийти в себя и приведём себя в порядок."
    scene black with fade
    "Девушки уходят в ванную. Я всё ещё ошеломлён."
    "Две потрясающие девушки, готовые делить меня..."
    call playMusic(chillTheme) from _call_playMusic_324
    $ location_home.showBackground()
    show sarah smile at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    "Через пару минут они возвращаются, приведя себя в порядок."
    show sarah tease talk
    sarah.c "Похоже, ты прошёл испытание~"
    show sarah tease
    show alice smile talk
    alice.c "Похоже, он полностью потерял самообладание. Думаю, мы справились, Сара?"
    show alice smile
    show sarah tease talk
    sarah.c "И что скажет сам герой?"
    show sarah tease
    mc.c "Я потерял дар речи."
    "Каждая из девушек кладёт руку мне на ногу. Мне нечего добавить."
    mc.c "Что тут скажешь... Спасибо?.."
    show sarah tease talk
    sarah.c "Хе-х~ Алиса, смотри, покажу кое-что. Он и после этого не против..."
    hide sarah with dissolve
    show sarah kiss with dissolve
    pause
    sarah.c "М-м~"
    hide sarah with dissolve
    show sarah tease at twoPersonLeft with dissolve
    show alice smile talk 2
    alice.c "Я тоже заметила. Любопытно."
    hide alice with dissolve
    show alice kiss with dissolve
    pause
    alice.c "Муа~"
    hide alice with dissolve
    show alice smile at twoPersonRight with dissolve
    mc.c "Вас обеих так приятно целовать."
    pause
    scene black with fade
    "Мы проводим остаток вечера за напитками, телевизором и приятной беседой. Мне нравится быть втроём."
    "В конце концов девушки решают разойтись одновременно. Я не знаю, как устроить ночёвку обеих, поэтому не предложил."
    "Можно ли быть настолько избалованным?"

    return

label sarahAliceDuoHEvent2(fromGallery):
    $ location_town.showBackground()
    call playMusic(barTheme) from _call_playMusic_325
    "Я несколько дней не видел Сару. Она не игнорирует меня, просто сказала, что ей нужно сосредоточиться на учёбе."
    "Скоро сдавать работу и экзамен. Готов поспорить, она долго откладывала подготовку и теперь паникует."
    "Я видел её конспекты. Не сказать, чтобы они были... подробными. Наверное, придётся наверстывать."
    "Проходя через город, я миную библиотеку. Можно заглянуть к Алисе, но не хочу отвлекать её во время работы."
    "Повторяюсь, но до сих пор невероятно, что я встречаюсь и с Алисой, и с Сарой — и обе не против. Они ещё и ладят..."
    "В прошлый раз было жарко. От Сары я такого ожидал, но не думал, что Алиса на это решится. Она не растерялась и, кажется, ей тоже понравилось."
    "Не знаю, какая у Алисы смена. Могу просто написать ей."
    "И словно по волшебству, из дверей библиотеки выходит знакомое лицо."
    show sarah bashful at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    "Они ещё не заметили меня, спускаются по лестнице и разговаривают."
    show sarah bashful talk
    sarah.c "Спасибо, что помогла, Алиса, но сегодня голова совсем не варит... Всё смешалось."
    show sarah bashful
    show alice smile talk 2
    alice.c "Ничего страшного, Сара. Я с радостью помогу и в другой раз. Могу прислать расписание смен и постараюсь помочь, когда ты снова придёшь."
    show alice smile
    show sarah bashful talk
    sarah.c "Ты такая добрая... Тратишь время на такую глупышку, как я..."
    show sarah bashful
    mc.c "Эй, Сара, Алиса!"
    show sarah neutral
    show alice smile talk 2
    alice.c "О, здравствуй, [mc.name]. Мы как раз уходим. Ты пришёл нас навестить?"
    show alice smile
    show sarah neutral talk
    sarah.c "О, привет, чувак. Как же я рада тебя видеть."
    show sarah neutral
    mc.c "Я просто проходил мимо. Удачно вышло. Что у вас тут?"
    show sarah neutral talk
    sarah.c "Мне нужна была книга из библиотеки и тихое место для занятий."
    show sarah bashful talk
    sarah.c "Алиса очень помогла. Нашла мне книгу и ещё несколько. Даже попыталась подсказать, как лучше учиться..."
    sarah.c "Но ничего не вышло, почти ничего не сделала... Голова совсем не работает."
    show sarah bashful
    mc.c "Жаль. Материал слишком сложный или просто стресс из-за срока?"
    show sarah bashful talk
    sarah.c "И то и другое..."
    show sarah neutral talk
    sarah.c "Прости, что ною. Спасибо ещё раз, Алиса, ты очень помогла. Наверное, позже я снова попрошу тебя о помощи."
    show sarah neutral
    show alice smile talk 2
    alice.c "Рада была помочь, Сара. Для этого и существуют библиотеки. Приятно, когда местные студенты пользуются нашей библиотекой для учёбы."
    show alice thinking
    alice.c "Но их удивительно мало. На кампусе есть библиотека получше?"
    mc.c "Думаю, ты просто переоцениваешь среднестатистического студента, Алиса."
    show sarah smile talk
    sarah.c "Хе-х, такие есть. Но не могу сказать, что часто бывала там."
    show sarah smile
    mc.c "Раз уж вы обе здесь, у вас есть планы?"
    show sarah neutral talk
    sarah.c "Я собиралась прийти домой и плюхнуться на кровать, но не отказалась бы отвлечься..."
    show sarah neutral
    show alice neutral talk
    alice.c "У меня конкретных планов нет. Собиралась домой готовить ужин."
    show alice neutral
    mc.c "Отлично, давайте вместе перекусим? Сара немного отвлечётся."
    mc.c "Я угощаю."
    show sarah smile talk
    sarah.c "Ну, если ты платишь, меня можно уговорить~"
    show sarah smile
    show alice smile talk 2
    alice.c "Очень любезно. С удовольствием, [mc.name]."
    show alice smile
    scene black with fade
    "Вот так, план готов."
    "Мы идём перекусить. К счастью, никто из них не привередлив."
    $ location_diner.showBackground()
    show sarah smile at twoPersonLeft
    show alice smile at twoPersonRight
    with dissolve
    show sarah joy
    sarah.c "Чёрт, как вкусно."
    show alice smile talk 2
    alice.c "Согласна, было превосходно."
    show alice smile
    show sarah tease talk
    sarah.c "Скажи, почему {i}мой мужчина{/i} не водит меня ужинать каждый день?"
    show sarah tease
    show alice smile talk 2
    alice.c "Каждый день? Не думаю, что это разумно. Тебе нужно полноценное питание, чтобы мозг работал как следует."
    show alice smile
    mc.c "А с твоим аппетитом... я быстро разорюсь..."
    show sarah tease talk
    sarah.c "Хе-хе~ Злюка."
    show sarah tease
    show alice joy
    alice.c "Хм-хм-хм~"
    show alice smile
    "О-о, чудесный вечер с двумя замечательными девушками. Я в раю."
    "И так приятно видеть, как они ладят. Я счастлив, что они стали настоящими подругами."
    show sarah tease
    mc.c "Вот что. Где угодно и сколько угодно блюд — если хорошо сдашь экзамен."
    show sarah mad talk
    sarah.c "Эй, я думала, мы собрались отвлечься от этого..."
    show sarah mad
    mc.c "Прости... Я просто немного переживаю. Не нравится видеть тебя такой напряжённой."
    show sarah bashful talk
    sarah.c "Ага-ага, всё нормально. Я немного перенервничала, но справлюсь..."
    show sarah neutral talk
    sarah.c "Я думала, если буду проводить с тобой меньше времени, то смогу сосредоточиться. Кажется, не помогло."
    show sarah neutral
    mc.c "Могу чем-нибудь помочь?"
    show sarah bashful talk
    sarah.c "Хм... Ну... А, неважно..."
    show sarah bashful
    mc.c "Может, Алиса лучше поможет с тем, о чём ты думаешь. Она не против."
    call playMusic(funnyTheme) from _call_playMusic_326
    show sarah joy
    sarah.c "Ха! А-ха~ Нет, это... Алиса не может... Ха-ха!"
    show sarah smile talk 2
    sarah.c "Хе-х~ Прости, Алиса, я не над тобой смеюсь. Ты очень помогла, но... Хе-хе~"
    show sarah smile
    mc.c "Что тут смешного?"
    show sarah smile talk
    sarah.c "Прости, нет, я не это имела в виду... Просто..."
    show sarah bashful talk
    sarah.c "Я подумала... Может, я немного... {i}воздерживалась{/i}..."
    show sarah bashful
    show alice thinking
    alice.c "Воздерживалась?"
    show sarah joy
    sarah.c "Ой, Алиса, ты такая забавная!"
    mc.c "Ты имеешь в виду..."
    show sarah bashful talk
    sarah.c "Мы давно не виделись, и я стала немного... возбуждённой..."
    show sarah bashful
    "Меня немного удивляет, что она говорит это при Алисе, но, может, мы уже перешли эту черту? После всего, что между нами было, это может стать нормой."
    show alice smile talk
    alice.c "О-о, понятно."
    show alice tease talk
    alice.c "Да, думаю, [mc.name] лучше справится с этой задачей."
    show alice tease
    "Алиса... Даже она подыгрывает. Она поддаётся влиянию или просто раскрывается? У неё отличное чувство юмора и она шутит в самый подходящий момент."
    mc.c "Ну, э-э... Ты сама сказала, что нам нужно побыть отдельно. Если бы всё зависело от меня..."
    show sarah smile talk 2
    sarah.c "Да-да, сама виновата, знаю. Теперь, когда секрет раскрыт... Без каламбура, Алиса."
    show sarah smile talk
    sarah.c "Прости, если я поставила тебя в неловкое положение..."
    show sarah smile
    show alice smile talk 2
    alice.c "Нисколько, Сара. На самом деле, [mc.name], я тоже недавно замечала это чувство. Я понимаю."
    call stopMusic from _call_stopMusic_60
    show alice tease talk
    alice.c "[mc.name], кажется, в последнее время меня тоже немного {i}напрягает{/i}~"
    show alice tease
    "Боже мой. Им обеим этого хочется. Я не могу отказаться."
    mc.c "Может... пойдём ко мне?"
    show sarah smile
    show alice smile 
    'Обе' "М-м~"
    scene black with fade
    "Охваченный волнением, я быстро расплачиваюсь, и мы возвращаемся ко мне."
    "Без предисловий и дразнилок — мы пришли заняться сексом."
    "Мы быстро раздеваемся и забираемся в постель."
    call playMusic(sexyTheme) from _call_playMusic_327
    scene sarahalicethreesomestart1 with fade
    pause
    alice.c "Сара, как именно мы это сделаем?"
    sarah.c "Я-я не знаю! Всё случилось спонтанно, я не продумала... [mc.name]?"
    mc.c "Раз уж ты так воздерживалась, что сама это предложила... Может, начнёшь ты?"
    sarah.c "Эй! Ну, наверное... И я не против..."
    alice.c "Меня это устраивает. Куда мне...?"
    "Есть несколько идей..."
    mc.c "Иди сюда, садись."
    scene black with fade
    "Я сажусь на край кровати и усаживаю готовую Сару к себе на колени."
    image sarahalice sarah fuck 1 = Movie(play="images/characters/sarahalice/threesome/sarahfuck1.webm")
    show sarahalice sarah fuck 1 with fade
    pause
    "Сара довольно мычит, опускаясь на мой член и прижимая ягодицы к моим бёдрам."
    sarah.c "М-м-м~ Чёрт~"
    sarah.c "Ты не представляешь, как мне, м-м~, этого не хватало~"
    "Она подпрыгивает на моём члене, впиваясь коготками в бёдра. Её пушистые хвосты щекочут моё лицо."
    alice.c "А-а... Мы уже делали что-то похожее, верно, [mc.name]? Только ты не входил в меня."
    alice.c "Тебе так хорошо, Сара?"
    sarah.c "О-о-очень~"
    mc.c "Я и о тебе не забыл, иди сюда..."
    image sarahalice sarah fuck 2 = Movie(play="images/characters/sarahalice/threesome/sarahfuck2.webm")
    show sarahalice sarah fuck 2 with fade
    pause
    "Усаживаю Алису рядом и нежно ласкаю пальцами её уже влажную от ожидания киску."
    alice.c "А-а... М-м~"
    alice.c "Почему у тебя это получается намного, м-м~, лучше, чем у меня?"
    mc.c "О? Дрочила, Алиса?"
    alice.c "А-а~ Немного... Но это совсем другое..."
    mc.c "Ничего, положись на меня."
    sarah.c "О-о~ Хе-х~ Такая невинная~ М-м~"
    mc.c "Вот если бы ты была чуть скромнее, как Алиса..."
    sarah.c "З-заткнись~ А-а~ Мне нужно больше~"
    image sarahalice sarah fuck 3 = Movie(play="images/characters/sarahalice/threesome/sarahfuck3.webm")
    show sarahalice sarah fuck 3 with fade
    pause
    "Прижимая её к бёдрам, Сара прыгает на мне изо всех сил, вдавливая меня в кровать."
    sarah.c "А-а-а~! М-м-м~ [mc.name]~"
    "Я усиливаю движения, наклоняюсь к Алисе и крепко целую её."
    "Алиса кладёт руку мне на грудь и вздрагивает от моих прикосновений."
    alice.c "М-м~ М-м~"
    sarah.c "О-о, чёрт~ Я сейчас кончу~"
    "Хорошо, а то я сам скоро присоединюсь. Нужно продержаться ради Алисы."
    alice.c "А-а~ Кажется..."
    sarah.c "М-м-м~!"
    alice.c "А-а-а~"
    "Девушки содрогаются и кричат от наслаждения, крепко прижимаясь ко мне."
    scene sarahalicesarahfinish with fadewhite
    pause
    sarah.c "О-о~ М-м~"
    sarah.c "Чёрт~ Так хорошо~"
    alice.c "А-а~ Только от твоей руки..."
    sarah.c "Чёрт... Ты не кончил... А-а~ Хорошо~"
    mc.c "Да. Твоя очередь, Алиса. Не волнуйся, буду нежным."
    sarah.c "*А-а* Что? Почему?"
    mc.c "Мы ещё только привыкаем друг к другу. Алиса... не так опытна."
    sarah.c "Не может быть... Алиса, ты была *а-а* девственницей до встречи с [mc.name]?"
    alice.c "Да, [mc.name] — мой первый партнёр."
    sarah.c "Но ты такая красивая... Я бы не подумала..."
    alice.c "С-спасибо, Сара."
    alice.c "[mc.name], всё хорошо. На самом деле, я хочу, чтобы мы продолжили с той же страстью. Я хочу попробовать кое-что... Дай мне быть сверху."
    "Ничего себе. Похоже, ей и правда нравится."
    scene black with fade
    "Я ложусь на спину, приглашая Алису сверху. Она опускается на мой член."
    image sarahalice alice fuck 1 = Movie(play="images/characters/sarahalice/threesome/alicefuck1.webm")
    show sarahalice alice fuck 1 with fade
    pause
    alice.c "М-м-м~ О-о, я всё ещё дрожу~"
    "Алиса покачивается, прижимаясь промежностью к моей и поворачиваясь на моём члене. Ощущения невероятные."
    sarah.c "Ничего себе~ Как горячо~"
    mc.c "Время уделить внимание и Саре. Иди сюда."
    "Сара наклоняется ко мне, и мы страстно целуемся."
    "Я тянусь к её клитору, уже мокрому и пульсирующему от возбуждения."
    sarah.c "М-м-м~ [mc.name]~ Так хорошо~"
    alice.c "А-а~ А-а~ Быть сверху... М-м~ Это... приятно."
    alice.c "Тебе хорошо, м-м~, [mc.name]?"
    mc.c "Невероятно, Алиса, продолжай."
    "Её упругая грудь подпрыгивает, а лицо теряет самообладание от удовольствия. Мягкие красивые бёдра прижимаются к моим."
    "Из киски Сары течёт сок — она всё ещё пылает после бурного секса."
    sarah.c "М-м~ М-м~"
    alice.c "А-а~ [mc.name]~"
    "Это невероятно, но я могу придумать кое-что получше. Чтобы они обе участвовали."
    mc.c "Готова прокатиться ещё раз, Сара?"
    sarah.c "Н-ну да, но..."
    mc.c "Сюда."
    "Я показываю на своё лицо. Сара удивлённо смотрит на меня."
    sarah.c "Что?! После того, как ты только что..."
    mc.c "Об этом позволь мне позаботиться. Я хочу попробовать тебя на вкус."
    sarah.c "Чёрт~ Звучит очень заманчиво~"
    image sarahalice alice fuck 2 = Movie(play="images/characters/sarahalice/threesome/alicefuck2.webm")
    show sarahalice alice fuck 2 with fade
    pause
    "Сара садится мне на лицо, а я глубоко ласкаю её киску языком."
    "Горячая влажная шерсть закрывает мне лицо, я исследую каждый изгиб."
    sarah.c "А-а-а~ Боже мой~"
    "Обхватив её крепкие бёдра, я притягиваю Алису и вхожу в неё, приподнимая над бёдрами."
    alice.c "А-а~! А-а~! [mc.name]~ О-о~"
    alice.c "Я чувствую это~ М-м~ Так глубоко~"
    sarah.c "О, чёрт~ Вот так, [mc.name]~"
    "Жидкости стекают по лицу и члену. Жар, звуки и запахи нашей оргии кружат голову от экстаза."
    image sarahalice alice fuck 3 = Movie(play="images/characters/sarahalice/threesome/alicefuck3.webm")
    show sarahalice alice fuck 3 with fade
    pause
    "Тугие стенки киски Алисы сжимают мой член, а Сара прижимается задницей к моему лицу, почти душа меня восхитительным образом."
    alice.c "А-а~ А-а~ А-а-а~ [mc.name]~"
    alice.c "Я-я почти..."
    sarah.c "Чёрт, чёрт~ Я тоже~ Почти... снова~"
    "Жар нарастает, я больше не могу сдерживать пламя в чреслах. Вот-вот кончу."
    alice.c "М-м-м~"
    sarah.c "Алиса~ Давай кончим~ [mc.name], наполни её хорошенько~"
    mc.c "Алиса... Я..."
    alice.c "А-а~ Всё хорошо~ А-а~ Сегодня внутрь~"
    sarah.c "А-а-а~ Я снова кончаю~"
    alice.c "М-м-м~!"
    scene sarahalicealicefinish with fadewhite
    pause
    "Мы одновременно достигаем оргазма в вихре наслаждения."
    "Прижимаясь ко мне, Алиса сжимает мой член, пока я глубоко вхожу в неё, охваченный бесконечным экстазом."
    "Сара с силой прижимает меня к кровати, содрогаясь на моём лице и заливая меня соком."
    alice.c "А-а-а~ А-а~ М-м~"
    sarah.c "О-о-о, чёрт~ М-м-м~"
    mc.c "Вот чёрт..."
    "Из Алисы вытекает сперма, и она обмякает у меня на груди."
    alice.c "О-о~ Это было..."
    sarah.c "Чертовски невероятно~"
    alice.c "Д-да~"
    sarah.c "Ты отлично её оттрахал, [mc.name]. Посмотри, в каком она беспорядке~"
    sarah.c "Вот тебе и невинная девственница!"
    mc.c "Кстати о твоей заднице..."
    sarah.c "О-ой, прости, чувак..."
    scene black with fade
    "Мы падаем без сил, тяжело дыша; все трое совершенно удовлетворены."
    call playMusic(heartTheme) from _call_playMusic_328
    scene sarahalicepillowtalk with fade
    "Девушки прижимаются ко мне, кладя головы на грудь."
    sarah.c "*А-а* Ничего себе~"
    sarah.c "Это было... чертовски горячо~"
    mc.c "Это... не описать словами."
    alice.c "*Хм* Сначала это немного сбивает с толку... Но... *а-а* теперь я понимаю, почему это нравится."
    alice.c "Есть что-то особенное в том, чтобы видеть, как твою подругу так ласкают... Мне от этого тоже приятнее."
    sarah.c "Боже, Алиса, ты такая милая."
    sarah.c "Когда втянется, она та ещё соблазнительница, правда, [mc.name]?"
    mc.c "Гораздо больше, чем думает."
    alice.c "Вот как..."
    "Мы лежим так некоторое время, наслаждаясь жаром тел друг друга."
    "Уже поздно, солнце село."
    "Не хочется отпускать этих двух девушек из объятий."
    mc.c "Останетесь сегодня у меня?"
    sarah.c "Ага, чувак. Я сейчас даже до двери не дойду..."
    alice.c "Если ты не против. Думаю, места хватит на всех?"
    mc.c "Отлично."
    scene black with fade
    "Вскоре мы засыпаем, уютно прижавшись к двум прекрасным девушкам."
    pause
    "..."
    pause
    scene sarahalicemorning with fade
    pause
    "Я просыпаюсь рядом с двумя красавицами."
    alice.c "Доброе утро, [mc.name]."
    mc.c "Привет, Алиса. Хорошо спала?"
    alice.c "Прекрасно. Но я за тебя волнуюсь... Тебе удобно?"
    "Как обычно, Сара лежит поперёк меня, вдавливая в кровать. Она не тяжёлая, но так неудобно..."
    mc.c "Ничего, справлюсь. Она ужасно ворочается во сне..."
    sarah.c "М-м... Я всё слышу..."
    mc.c "Раз уж проснулась, может, перестанешь меня раздавливать?"
    sarah.c "Нет... Так удобно..."
    "Мы некоторое время нежимся в утреннем солнце."
    mc.c "Вчера было невероятно."
    alice.c "Мне тоже очень понравилось. Даже больше, чем я ожидала. Спасибо, что пригласила меня, Сара."
    sarah.c "Не глупи, Алиса. Мне тоже понравилось."
    scene black with fade
    "После неторопливого утра мы встаём и собираемся к новому дню."
    "Но сперва целую своих милых девушек на прощание."

    return {'location':location_home, 'time':'Morning'}
