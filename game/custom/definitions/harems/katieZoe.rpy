init offset = 3

default katieZoeDuoStoryEvent1 = Event('Лисы и волки', 'katieZoeDuoStoryEvent1', [katie, zoe], 0, 0, [katieHEvent4, zoeHEvent4], location_bar)
default katieZoeDuoHEvent1 = Event('Будь главной', 'katieZoeDuoHEvent1', [katie, zoe], 0, 0, [katieZoeDuoStoryEvent1, katieHEvent5, zoeHEvent5], location_home, ['Evening', 'Night'])

label katiezoeSexSelect:
    hide screen mainUi
    image katiezoe idle = Movie(play="images/characters/katiezoe/sexWaiting.webm")
    show katiezoe idle with fade
    call screen katiezoeSexSelectScreen
    call endScene(targetLocation = location_home) from _call_endScene_20

screen katiezoeSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(katieZoeDuoHEvent1.unlocked or persistent.debugMode):
                textbutton 'Верхом' keysym str(1):
                    action [Jump('katieZoeRiding')]
            else:
                textbutton 'Закрыто'
            textbutton 'Выход' keysym str(2):
                action [Hide('katiezoeSexSelectScreen'), Return()]

label katieZoeRiding:
    image katiezoe riding handjob = Movie(play="images/characters/katiezoe/hEvent1/handjob.webm")
    show katiezoe riding handjob with fade
    pause
    image katiezoe facesitting = Movie(play="images/characters/katiezoe/hEvent1/faceSitting.webm")
    show katiezoe facesitting with fade
    pause
    image katiezoe riding 1 = Movie(play="images/characters/katiezoe/hEvent1/riding1.webm")
    show katiezoe riding 1 with fade
    pause
    image katiezoe riding 2 = Movie(play="images/characters/katiezoe/hEvent1/riding2.webm")
    show katiezoe riding 2 with fade
    pause
    scene katiezoeridingfinish1 with fadewhite
    pause
    scene katiezoeridingfinish2 with fade
    pause
    jump katiezoeSexSelect

label katieZoeDuoStoryEvent1(fromGallery):
    if(katie.movedIn and zoe.movedIn):
        ofkeres "Это событие предполагает, что вы ещё не заселили обеих девушек к себе. Оно должно произойти до того, как они переедут."
        ofkeres "Если вы видите это сообщение, представьте, что девушки знакомятся впервые. Приятной игры :)"
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_311
    show zoe neutral with dissolve
    "Сегодня я на смене со своей правой рукой... девушкой... волчицей."
    "С ней всё идёт как по маслу. Я могу предоставить Зои вести беседы с постоянными посетителями. Мисс Популярность."
    unknown2 "Ещё одну сюда, Зои!"
    "Один из завсегдатаев весело зовёт Зои с другого конца стойки."
    show zoe smile talk
    zoe.c "Ещё одну, старик? Тебе бы сбавить темп, а то всё выпьешь!"
    show zoe smile talk 2
    zoe.c "Спорим, ты бы сам мне фору дал~"
    show zoe smile
    unknown2 "А-ха-ха!"
    hide zoe with easeoutleft
    "Зои подходит к клиенту и приносит ещё пива, перекидываясь с ним шутками."
    "Она отлично болтает с общительными посетителями. Для бизнеса она настоящая находка."
    "Я занимаюсь своими делами и вытираю стакан. Входит знакомое лицо."
    show katie smile with dissolve
    "Кэти переступает порог, сразу замечает меня за стойкой и подходит."
    show katie tease talk
    katie.c "Привет, милый!"
    show katie tease
    "Это немного неожиданно. Обычно она пишет, чтобы узнать, работаю ли я сегодня."
    mc.c "Кэти! Какой приятный сюрприз. Я что, пропустил сообщение?"
    show katie smile talk
    katie.c "Нет, я просто решила заглянуть. Подумала, что сегодня ты на смене."
    show katie neutral talk
    katie.c "Я не помешала?"
    show katie neutral
    mc.c "Нисколько! Всегда тебе рад."
    show katie smile talk 2
    katie.c "Ой, отлично~ Я бы выпила бокал твоего мерло. Оно сейчас у тебя хорошее."
    show katie smile
    mc.c "Конечно, сейчас принесу."
    "Я поворачиваюсь за бутылкой. В это время возвращается Зои."
    show katie at twoPersonRight with ease
    show zoe smile at twoPersonLeft with easeinleft
    show zoe smile talk
    zoe.c "Этот старик такой забавный. Он всегда такой пьяный?"
    show zoe smile
    mc.c "Он тут знаменитость ещё до моего появления. Терри мне про него рассказывал."
    show zoe smile talk 2
    zoe.c "А, мерло? Хороший выбор... э-э... Кэти, верно?"
    show zoe smile
    show katie smile talk
    katie.c "Всё верно."
    show katie smile
    "А?"
    call mcFretAboutPolyamory from _call_mcFretAboutPolyamory_3
    "Очевидно, эти двое уже пересекались, Зои ведь здесь работает..."
    "Но наши отношения друг с другом они видят впервые..."
    mc.c "Вы... знакомы?"
    show katie smile talk 2
    katie.c "Конечно, она меня несколько раз обслуживала."
    show katie smile talk
    katie.c "С посетителями она очень разговорчивая, это приятно."
    show katie smile
    show zoe neutral talk
    zoe.c "Кэти иногда заходит после работы с коллегами."
    show zoe thinking
    zoe.c "Ты говорила, где работаешь... В офисе неподалёку, да?"
    show katie tease talk
    katie.c "Да, [mc.name] знает, хе-хе~"
    show katie tease
    show zoe smile talk
    zoe.c "Правда? И какая тут история?"
    show zoe smile
    if(not mc.polyamoryExplained):
        "Чёрт... Теперь не скрыться."
        "Я слишком долго тянул, и теперь придётся за это расплачиваться..."
        "Как глупо было доводить до этого. О чём я думал? Зои же здесь работает, чёрт возьми."
        "Они всё равно должны были встретиться... И всё закончится катастрофой."
        mc.c "Э-э... Зои..."
        show zoe neutral
        mc.c "Мы... э-э..."
        show katie neutral
        'Обе' "...?"
        "Чёрт... Какой же я идиот."
        mc.c "Мы с Кэти... встречаемся."
        "Зои смотрит на меня непонимающе. Она не совсем понимает, что я говорю?"
        "Кэти тоже явно растеряна..."
        mc.c "А Кэти, мне очень жаль, но..."
        mc.c "Я ещё встречался с Зои."
        mc.c "Я не хотел, чтобы всё так вышло. С тех пор как переехал сюда, ходил на свидания, и..."
        mc.c "Мне казалось, что мы обе друг другу понравились. А потом всё зашло так далеко, что..."
        mc.c "Я не мог отпустить ни одну из вас... Это не оправдание. Мне очень жаль."
        "Девушки растерянно смотрят то друг на друга, то на меня."
        show zoe neutral talk
        zoe.c "Прости, Кэти, я что-то пропустила?"
        show zoe neutral
        show katie thinking
        katie.c "Я и сама не уверена..."
        "А? Такой реакции я не ожидал..."
        mc.c "Я... Прости..."
        show katie neutral talk
        katie.c "За что, милый? За то, что раньше не сказал?"
        show katie neutral
        mc.c "Э-э... Ну да, наверное, но..."
        show zoe neutral talk
        zoe.c "Я разве говорила, что ты должен спрашивать разрешения?"
        show zoe neutral
        "Что? Я не понимаю."
        mc.c "...Разрешения?"
        show zoe smile talk
        zoe.c "Чего ты так нервничаешь? Прямо как будто..."
        show zoe smile talk 2
        zoe.c "О-о-о~ Ха-ха~"
        show zoe smile
        show katie smile talk 2
        katie.c "Что такое, Зои? Это какая-то ваша шутка?"
        show katie smile
        show zoe smile talk
        zoe.c "Этот болван... Всё ещё мыслит по-человечески~"
        zoe.c "Парень, ты же знаешь, что здесь можно встречаться с кем угодно? Мы не живём в этой странной собственнической манере."
        show zoe smile
        mc.c "Что ты..."
        show katie tease talk
        katie.c "Ой, милый! Она права. У антропоморфов часто бывает несколько партнёров."
        katie.c "Я не знала, что ты не в курсе!"
        show katie tease
        mc.c "Что? Серьёзно?"
        show zoe tease talk
        zoe.c "А-ха! Посмотри, как он ёрзает."
        show zoe smile talk 2
        zoe.c "Ты и правда не знал, да?"
        show zoe smile
        call mcPolyamoryExplainedConclusion from _call_mcPolyamoryExplainedConclusion_3
    else:
        "Мне всё ещё неловко это говорить, но... после прошлого раза... просто скажу."
        mc.c "Мы... встречаемся уже некоторое время."
        mc.c "Прости, что вот так сообщаю, Зои. Я давно собирался тебе сказать."
        mc.c "А Кэти... Я ещё и с Зои встречаюсь. Уже давно, ещё до того, как она начала здесь работать, хотя это неважно..."
        mc.c "Мне следовало рассказать раньше. Не стоило вот так всё раскрывать, прости."
        show zoe smile talk 2
        zoe.c "О-о~?"
        show zoe smile
        show katie surprise
        katie.c "Правда? Ого, я и не замечала!"
    call playMusic(barTheme) from _call_playMusic_312
    mc.c "Так... Вы обе не против?.."
    if(katie.polyamoryExplained):
        show katie tease talk
        katie.c "Милый, ты и так знаешь, что я об этом думаю..."
    show katie smile talk
    katie.c "Конечно, милый! Она кажется хорошей девушкой!"
    show katie smile
    show zoe smile talk 2
    if(zoe.polyamoryExplained):
        zoe.c "Всё ещё нервничаешь... Мы же уже говорили об этом, идиот."
    zoe.c "Всё нормально, жеребец. Расслабься."
    show zoe smile
    "К счастью... Всё хорошо. Две замечательные девушки меня одобряют."
    "У них совершенно разные характеры, забавно, особенно если подумать — лисы и волки..."
    show zoe tease talk
    zoe.c "Так... Эта пышная красотка зашла в твой бар... Вот же ты ловкач, худыш~"
    zoe.c "Я должна была догадаться~"
    show zoe tease
    show katie bashful talk
    katie.c "О-о боже..."
    katie.c "Ну... Наверное, этого следовало ожидать~ Симпатичная молодая девушка, которую ты видишь каждый день."
    show katie bashful
    show zoe smile talk 2
    zoe.c "Молодая? Я на несколько лет старше этого парня."
    show zoe smile
    show katie surprise
    katie.c "Правда? Ни за что бы не подумала! У тебя такая красивая шёрстка!"
    show zoe smile talk
    zoe.c "Сама-то посмотри на себя. Ты сияешь, подруга."
    show zoe smile
    show katie smile talk
    katie.c "Ну... Как вы ладите? Хочу услышать все сплетни!"
    "Зои демонстративно шлёпает меня по заднице."
    show zoe smile talk 2
    zoe.c "Ну... он нормальный. Не знаю, как я умудрилась связаться с этим балластом. Не повезло мне, да?"
    show zoe smile
    show katie surprise
    katie.c "О-ох! Бедный [mc.name]!"
    show katie tease talk
    katie.c "Как жестоко... Не мой милый~"
    show katie tease
    show zoe tease talk
    zoe.c "О боже, вот как ты заставила её с тобой разговаривать? Фу~"
    show zoe tease
    mc.c "Это не мой выбор... Но мне приятно. Может, ты тоже иногда будешь поласковее, Зои."
    show zoe smile talk
    zoe.c "Ни за что, худыш!"
    show zoe smile
    show katie bashful talk
    katie.c "Я замечала, как вы общаетесь... Она всегда такая... резкая с тобой. Я и не подозревала."
    show katie neutral talk
    katie.c "Но... «худыш»? Разве это не немного... ну, ты понимаешь?.."
    show katie neutral
    mc.c "Нет, всё нормально. Она просто такая..."
    show zoe smile talk
    zoe.c "Он выдержит. Иногда его надо немного встряхнуть~ Ты же понимаешь?"
    show zoe smile
    show katie neutral
    katie.c "Хм?.."
    "Для меня это уже слишком... Ещё немного, и мы заговорим о нашей сексуальной жизни... Наши отношения сильно отличаются."
    mc.c "{b}*Кхм*!{/b} Ну, все мы разные, да? Забавно, я думал, что вы будете немного похожи."
    show katie neutral talk
    katie.c "Почему?"
    show katie neutral
    show zoe neutral talk
    zoe.c "Ага... Что?"
    show zoe neutral
    mc.c "Ну... понимаешь... Лиса и волчица?"
    zoe.c "..."
    katie.c "..."
    mc.c "Вы же... типа... родственники?"
    show zoe neutral talk
    zoe.c "Иногда меня поражает твоя глупость..."
    show zoe neutral
    show katie bashful talk
    katie.c "Ох, милый..."
    show katie bashful
    mc.c "А?"
    show zoe neutral talk
    zoe.c "Мы очень дальние родственники. С чего тебе вообще пришло такое в голову?"
    show zoe smile talk
    zoe.c "Это всё равно что люди и {i}настоящий{/i} бабуин."
    show zoe smile
    mc.c "Что?"
    show katie bashful talk
    katie.c "Да, это было глупо, милый..."
    show katie bashful
    "...А-а."
    scene black with fade
    "Девушки смеются надо мной."
    "Мы выпиваем вместе, но они не дают мне забыть эту историю."
    "В своё оправдание скажу, что я ещё новичок среди антропоморфов..."

    if(not fromGallery):
        $ katie.polyamoryExplained = True
        $ zoe.polyamoryExplained = True
        $ mc.polyamoryExplained = True
        $ katie.knowsDating = list(set(katie.knowsDating + [zoe]))
        $ zoe.knowsDating = list(set(zoe.knowsDating + [katie]))

    return

label katieZoeDuoHEvent1(fromGallery):
    call playMusic(chillTheme) from _call_playMusic_313
    $ location_home_kitchen.showBackground()
    "По комнате плывут аппетитные запахи."
    "Готовится что-то особенное, и точно не моими руками."
    "Сегодня в меню приятный вечер в хорошей компании."
    show katie smile at twoPersonRight
    show zoe smile at twoPersonLeft
    with dissolve
    "Кэти и Зои со мной."
    "Хотя для Зои слово {b}«приятная»{/b} не совсем подходит... Она весёлая по-своему и сегодня ведёт себя прилично."
    "Они сами напросились в гости. Что-то вроде маленького званого ужина. Конечно, я был только рад."
    "Оказывается, девушки снова встретились в баре и разговорились за парой напитков."
    "Разговор, конечно, зашёл о любви Кэти к готовке, и это привлекло Зои. Она ненасытна не только в еде."
    "Они договорились, что Кэти приготовит домашний ужин. У меня дома, почему-то. Ну, хорошая еда — отличный повод."
    "Сегодня стейки с замечательным домашним соусом и овощным гарниром. Божественно."
    show katie smile talk
    katie.c "Вот, пожалуйста! Надеюсь, понравится."
    show katie smile
    show zoe smile talk 2
    zoe.c "Чёрт, подруга, посмотри! Вот это шик!"
    show zoe smile
    show katie bashful talk
    katie.c "Пустяки..."
    show katie bashful
    "Зои отрезает большой кусок, от которого ещё идёт пар, и откусывает острыми клыками."
    show zoe surprise
    zoe.c "Ничего себе!"
    show katie surprise
    katie.c "Ч-что такое?"
    show zoe smile talk 2
    zoe.c "Это чертовски вкусно!"
    show zoe smile talk
    zoe.c "Я думала: «просто стейк», но боже, как ты это приготовила?"
    show zoe smile
    "Похоже, ей понравилось."
    show katie tease talk
    katie.c "О-о~ Рада, что тебе нравится, Зои."
    show katie smile talk 2
    katie.c "В основном дело в хорошем мясе. Соус совсем простой..."
    show katie smile
    show zoe smile talk 2
    zoe.c "Простой? Чёрт, научи меня так готовить, подруга."
    show zoe smile
    show zoe tease talk
    zoe.c "Этот тебя каждый вечер стейками балует, да? Неудивительно, что ты меня не просила готовить."
    zoe.c "Хотя я бы всё равно отказалась~"
    show zoe tease
    show katie tease talk
    katie.c "Решила приготовить нам сегодня что-нибудь особенное. За новых подруг, да?"
    show katie tease
    mc.c "Она права, Кэти, очень вкусно."
    show zoe smile talk 2
    zoe.c "Держись за неё, худыш! Хотя бы ради меня! Ха-ха!"
    show zoe smile talk
    zoe.c "Можно привыкнуть к такому~"
    show zoe smile
    show katie tease talk
    katie.c "Хе-хе~ Ну, спасибо, Зои."
    show katie smile
    "Невероятная ситуация. Две потрясающие девушки словно устроили со мной свидание."
    "Вкуснейшая еда и такая прекрасная компания..."
    "В какой же счастливый мир я попал?"
    "Мы ужинаем и болтаем за парой напитков."
    "Рассказываем, как познакомились, о работе в баре и о жизни после переезда из других городов."
    "Кажется, до сегодняшнего вечера девушки уже кое-что обсуждали о нас..."
    $ location_home_bedroom.showBackground()
    "В конце концов мы перебираемся в спальню, устраиваемся на диване и болтаем."
    show katie smile at twoPersonRight
    show zoe smile talk at twoPersonLeft
    with dissolve
    zoe.c "Так, худыш. Тебе одной из нас мало? Захотелось разнообразия?"
    show zoe smile
    mc.c "Э-э... Ну..."
    show zoe tease talk
    zoe.c "Тебе нужна милая, нежная, мягкая девушка, которая будет тебя баловать после меня, да? Ха-ха!"
    zoe.c "Уже представляю~ Она гладит тебя по голове, пока ты засыпаешь у неё на коленях~"
    show zoe tease
    mc.c "Ой, Кэти, ты ей это рассказала?"
    show katie bashful talk
    katie.c "Я не..."
    show katie bashful
    show zoe surprise
    zoe.c "А? Погоди, серьёзно?"
    show katie joy
    katie.c "Хе-хе~"
    show zoe tease talk
    zoe.c "Боже, вы двое..."
    zoe.c "Неужели вы {i}всё{/i} время такие влюблённые голубки?"
    show zoe tease
    show katie bashful talk
    katie.c "Ну... А почему нет? Он милый..."
    show katie bashful
    show zoe smile talk 2
    zoe.c "Я бы так не сказала~"
    show zoe smile
    show katie tease talk
    katie.c "Ой~ Не дразни~"
    katie.c "Мне так нравится, как нежно он меня обнимает, ласкает и целует~"
    show katie joy
    katie.c "Как он прижимается к моей шее, шепчет милые слова, пока мы... О-о~"
    show katie tease
    show zoe smile talk
    zoe.c "Хе-х~ Ску-у-учно~"
    zoe.c "Он всё время пытается со мной так обращаться. Что в этом весёлого?"
    show zoe smile
    mc.c "Эй..."
    show katie bashful talk
    katie.c "Скучно?.."
    show katie bashful
    show zoe smile talk
    zoe.c "Ага, унылая миссионерская поза каждую ночь?"
    show zoe smile
    "Так, теперь стало слишком откровенно."
    show zoe smile talk
    zoe.c "Иногда тебе надо быть главным. Брать контроль на себя. Особенно с этим~"
    show zoe smile
    show katie bashful talk
    katie.c "Но мне... нравится, когда... {size=20}он берёт контроль на себя...{/size}"
    show katie bashful
    show zoe smile talk 2
    zoe.c "Похоже, пора показать тебе пару новых приёмов, подруга."
    zoe.c "Иногда надо заставлять его ёрзать~"
    show zoe smile
    "Боже, к чему это идёт?"
    "Кажется, мне даже нравится..."
    show zoe smile talk
    zoe.c "Посмотри на его лицо. Он уже всё представляет."
    show zoe smile
    show katie tease talk
    katie.c "Хе-хе~ Ну, он ведь часто бывает очень нетерпеливым, правда?"
    show katie tease
    mc.c "Я..."
    show zoe smile talk
    zoe.c "Точно, маленький негодник."
    zoe.c "В такие моменты, подруга, не надо позволять ему всегда делать всё по-своему."
    show zoe smile
    show katie bashful talk
    katie.c "Что ты имеешь в виду?.."
    show katie bashful
    call playMusic(sexyTheme) from _call_playMusic_314
    show zoe tease talk
    zoe.c "Думаю, пора кое-чему тебя научить~"
    show zoe tease
    "Что меня ждёт?.."
    "Зои встаёт с дивана и помогает Кэти подняться, взяв её за руку."
    show zoe tease talk
    zoe.c "Смотри, как {i}я{/i} это делаю~"
    show zoe tease
    "Зои бросает на меня самодовольную ухмылку."
    show zoe mad talk
    zoe.c "Встать!"
    show zoe mad
    "Я сразу подчиняюсь её тону. Кажется, за это меня ждёт награда..."
    show zoe mad talk
    zoe.c "К кровати."
    show zoe mad
    "Я подчиняюсь."
    "Я поворачиваюсь к ним, и Зои стягивает с меня рубашку."
    show katie surprise
    katie.c "О-ох~ Милый~"
    show zoe tease talk
    zoe.c "И штаны~"
    show zoe tease
    "Мне нравится, к чему всё идёт. Я расстёгиваю ремень и стягиваю штаны, обнажая уже готовый к делу член."
    show zoe tease talk
    zoe.c "Хе-х~ Видишь? Уже готов~"
    show katie bashful talk
    katie.c "О-о~"
    show katie bashful
    show zoe tease talk
    zoe.c "Наверное, ты любишь, когда он укладывает тебя~ Крепко обнимает~"
    zoe.c "Но сегодня не тот случай~"
    "Зои кладёт руку мне на плечо и..."
    scene katiezoehevent1i1 with Fade(0.2, 0.0, 0.2)
    pause
    "...С силой толкает меня на кровать."
    mc.c "Уф."
    "Я падаю на спину, полностью обнажённый, с выставленной напоказ эрекцией."
    "Две мои девушки нависают надо мной. Зои ухмыляется, а Кэти немного растеряна."
    katie.c "[mc.name]... Уже~?"
    katie.c "Я и не знала, что ты..."
    zoe.c "Хе-х~ Девочка, он тут ничего не решает."
    zoe.c "Как и в наш первый раз, да, жеребец?"
    "Если буду слишком радоваться, испорчу момент. Я лишь киваю."
    zoe.c "У меня есть план, но сначала надо убедиться, что он готов~"
    image katiezoe riding handjob = Movie(play="images/characters/katiezoe/hEvent1/handjob.webm")
    show katiezoe riding handjob with fade
    pause
    "Зои забирается на кровать на колени, возвышаясь надо мной."
    "Она быстро хватает мой член у основания и сжимает, пока он не становится твёрдым."
    zoe.c "Надо убедиться, что он как следует возбуждён~"
    "Кэти наклоняется к кровати и начинает улыбаться, наблюдая за происходящим."
    "У меня выступает предэякулят. Кэти смущённо тянется и щекочет головку члена."
    katie.c "Ты всегда так быстро готов~"
    zoe.c "Как хороший мальчик~ Хоть на что-то он годится~"
    "Кэти ведёт подушечкой лапы вверх-вниз по головке, которая подрагивает в руке Зои."
    zoe.c "Ладно, Кэти, пора проявить немного доминирования~"
    zoe.c "Это будет только для {i}твоего{/i} удовольствия~"
    katie.c "Зои?.."
    "Что же будет?"
    zoe.c "Сядь ему на лицо."
    "О да."
    katie.c "Ч-что?!"
    katie.c "Ты хочешь... залезть сверху... и... Я не могу..."
    katie.c "То есть... [mc.name]?.. Я же тебя задушу..."
    mc.c "Не задушишь!"
    katie.c "..."
    zoe.c "Хе-х~ Не спрашивай разрешения. Просто сделай это, подруга! Поверь мне."
    katie.c "Милый?.."
    "Я стараюсь не звучать {i}слишком{/i} нетерпеливо и подмигиваю ей. Зои, конечно, знает, что мне понравится, но незачем разрушать иллюзию."
    "И не собираюсь позволять Кэти отказаться."
    scene black with fade
    "Девушки раздеваются передо мной, Кэти слегка колеблется."
    "Она заползает на кровать и ставит колени над моей головой."
    "Она устраивается, открывая мне чудесный вид..."
    katie.c "В-вот так?.."
    zoe.c "Не сдерживайся, опустись на него всем весом~"
    image katiezoe facesitting = Movie(play="images/characters/katiezoe/hEvent1/faceSitting.webm")
    show katiezoe facesitting with fade
    pause
    "Кэти медленно опускается на меня, и моё лицо исчезает в тепле, мягкости и пушистом блаженстве."
    katie.c "О-ох~"
    "Её киска прижимается ко рту, влага блестит на моих губах."
    "Не теряя времени, я лакаю её соки, ведя языком по складочкам вверх, вниз и из стороны в сторону."
    katie.c "М-м~ О-о, [mc.name]~"
    zoe.c "Хе-х~ Вот так. Заставь его постараться языком."
    "Я чувствую, как Зои садится поперёк моих бёдер, берёт головку моего члена когтями, сжимает и массирует."
    zoe.c "Задуши его. Покатайся сверху. Сегодня всё только для тебя."
    katie.c "Это так... М-м~ Необычно~"
    "Ощущения ошеломляющие. Лицо в киске и вес двух девушек сверху..."
    "Забавно, что это должно быть наказанием."
    zoe.c "По его лицу видно, как хорошо он старается, словно послушный мальчик~"
    zoe.c "Может, ему стоит немного отплатить~ Готов ко мне, жеребец?"
    image katiezoe riding 1 = Movie(play="images/characters/katiezoe/hEvent1/riding1.webm")
    show katiezoe riding 1 with fade
    pause
    "Не желая просто смотреть, как мы извиваемся, Зои приподнимается и вводит мой член в себя."
    zoe.c "М-м~ О, чёрт, да~"
    zoe.c "Извращенец обожает это~ М-м~ Он весь твёрдый~"
    "Зои покачивается у меня на коленях. Я чувствую, как она уже промокла."
    "На меня нападают с двух сторон, хоть этого и не видно. Я почти теряю рассудок."
    katie.c "А-а~ А-а~"
    katie.c "Ох, милый~ М-м~ Продолжай~ М-м~"
    "Её большая задница продолжает покачиваться у меня на лице, пока она извивается от ласк моего языка."
    "Я пытаюсь делать короткие вдохи, когда удаётся, но она всем весом прижимается ко мне и теряет контроль."
    katie.c "А-а~ А-а-а~"
    zoe.c "Хе-х~ М-м~ Чёрт~ Так горячо~"
    katie.c "Я... кажется, сейчас..."
    zoe.c "О-о~ Заставь его постараться, девочка. Работай бёдрами."
    zoe.c "Давай измучаем его~"
    image katiezoe riding 2 = Movie(play="images/characters/katiezoe/hEvent1/riding2.webm")
    show katiezoe riding 2 with fade
    pause
    "Я чувствую, как Зои убирает руки с моих ног, и Кэти сильнее прижимается ко мне."
    "Я тянусь и хватаю Зои за бёдра. Начинаю толкаться вверх, заставляя её подпрыгивать."
    zoe.c "А-а~ А-а-а~ Чёрт, да~ Трахни меня, худыш~"
    katie.c "А-а~ М-м-м~ М-м~ А-а~"
    "Кэти начинает тереться киской о моё лицо быстрее и сильнее."
    "Моё лицо полностью мокрое от её соков, губы киски дрожат от каждого движения языка."
    "Она яростно трётся задницей, и я чувствую, как сильно виляет её хвост."
    "Мои бёдра шлёпают по заднице Зои, наши гениталии издают непристойные звуки и сочатся."
    zoe.c "Чёрт, да, да~"
    zoe.c "Заставь нас кончить, жеребец~ А-а~"
    katie.c "Ещё немного~ А-а~"
    zoe.c "Чёрт, да~ Я сейчас..."
    "Я вот-вот кончу."
    mc.c "М-мф!"
    scene katiezoeridingfinish1 with fadewhite
    pause
    katie.c "О-о-о-о~~!"
    zoe.c "А-а-а-а~~!"
    "Бёдра Зои опускаются на мои, и её тепло целиком обволакивает мой член. Я изливаю глубоко в неё огромное количество спермы."
    "Бёдра Кэти дрожат, киска пульсирует от удовольствия и брызжет мне на лицо."
    "Полностью утопая в горячем, мокром, мягком беспорядке из шерсти, мы все выдыхаем от экстаза."
    scene katiezoeridingfinish2 with fade
    pause
    "Я чувствую, как Зои медленно поднимается с моего члена."
    "Мои соки заливают лицо, сперма стекает по члену. Мы в полном разврате."
    katie.c "А-а~ А-а~"
    zoe.c "М-м~ Чёрт~"
    katie.c "О боже~ А-а~ Это было..."
    zoe.c "Хе-х~ Хорошо, правда?"
    katie.c "Это было так... М-м~ Хорошо~"
    "Девушки сидят на мне, пытаясь отдышаться."
    "Как бы ни было чудесно, силы Кэти на исходе, и её вес начинает меня душить."
    "Я хлопаю её по бёдрам, прося отпустить."
    katie.c "О-ох! Милый~ Прости~"
    scene katiezoehevent1i2 with fade
    pause
    "Девушки скатываются с меня, давая вдохнуть."
    "Я сажусь на кровати и наконец вижу похотливое лицо Кэти и её вздымающуюся грудь."
    "Мы сидим и приходим в себя, покрытые потом и соками."
    mc.c "Ничего себе... Девушки..."
    zoe.c "Хе-х~ Ну как тебе, подруга?"
    katie.c "Это... нечто..."
    katie.c "Тебе нравится вот так~?"
    zoe.c "Ещё бы~"
    katie.c "Ой, я имела в виду [mc.name]..."
    mc.c "Ну... всему своё время и место. Но это было потрясающе."
    zoe.c "Да хоть где и когда, худыш~"
    zoe.c "Теперь это касается и тебя, Кэти."
    katie.c "Хм... Посмотрим..."
    scene black with fade
    "Мы какое-то время лежим вместе, наслаждаясь послевкусием."
    "Кэти постепенно приходит в себя и немного смущается, а Зои поддразнивает её."
    "В конце концов мы приводим себя в порядок и проводим остаток вечера ещё за парой напитков."
    return
