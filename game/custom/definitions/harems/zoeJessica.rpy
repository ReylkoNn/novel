init offset = 3

default zoeJessicaDuoStoryEvent1 = Event('Зои и Джессика', 'zoeJessicaDuoStoryEvent1', [zoe, jessica], 0, 0, [zoeHEvent2, jessicaHEvent2], location_bar)
default zoeJessicaHEvent1 = Event('В клубе', 'zoeJessicaHEvent1', [zoe, jessica], 0, 0, [zoeHEvent3, jessicaHEvent3], location_home, ['Night'])

label zoejessicaSexSelect:
    hide screen mainUi
    scene black with fade
    image zoejessica idle = Movie(play="images/characters/zoejessica/sexWaiting.webm")
    show zoejessica idle with fade
    call screen zoejessicaSexSelectScreen
    call endScene(targetLocation = location_home) from _call_endScene_22

screen zoejessicaSexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(zoeJessicaHEvent1.unlocked or persistent.debugMode):
                textbutton 'Верхом' keysym str(1):
                    action [Jump('zoeJessicaRiding')]
            else:
                textbutton 'Закрыто'
            textbutton 'Выход' keysym str(2):
                action [Hide('zoejessicaSexSelectScreen'), Return()]

label zoeJessicaRiding:
    scene zoejessicacowgirlstart with fade
    pause
    image zoe jessica cowgirl part 1 = Movie(play="images/characters/zoejessica/cowgirl/part1.webm")
    show zoe jessica cowgirl part 1 with fade
    pause
    image zoe jessica cowgirl part 2 = Movie(play="images/characters/zoejessica/cowgirl/part2.webm")
    show zoe jessica cowgirl part 2 with fade
    pause
    image zoe jessica cowgirl part 3 = Movie(play="images/characters/zoejessica/cowgirl/part3.webm")
    show zoe jessica cowgirl part 3 with fade
    pause
    image zoe jessica cowgirl part 4 = Movie(play="images/characters/zoejessica/cowgirl/part4.webm")
    show zoe jessica cowgirl part 4 with fade
    pause
    scene zoejessicacowgirlend1 with fadewhite
    pause
    scene zoejessicacowgirlend2 with fade
    pause
    jump zoejessicaSexSelect

label zoeJessicaDuoStoryEvent1(fromGallery):
    $ location_bar.showBackground()
    call playMusic(barTheme) from _call_playMusic_329
    "Сегодня мне совсем не хотелось ничего делать, но пришлось выйти на смену и отработать несколько часов."
    "Не хватало сотрудников, и по какой-то причине я не смог связаться с остальными."
    "Настроение так себе. Бедный я, приходится тяжело работать в собственном заведении. Какой ужас..."
    "К счастью, Джессика сегодня встречается с парой подруг, так что я не умираю со скуки."
    "Мы немного поболтали, но я оставил их за столиком сплетничать. Боже, как много они говорят..."
    "Похоже, Джессика идёт за следующей порцией."
    show jessica tease talk with dissolve
    jessica.c "Привет, бармен~ Нам три одинаковых, пожалуйста~"
    show jessica tease
    "Теперь она открыто флиртует со мной при подругах. Думаю, они уже знают обо мне."
    "Я смотрю на их столик. Они тихонько хихикают."
    mc.c "Конечно. Хорошо проводите время?"
    show jessica smile talk 2
    jessica.c "О да, Лиза рассказывала о новом парне. Он, типа, такой зануда, но она этого не замечает!"
    show jessica smile talk
    jessica.c "Она просто по уши в него влюблена, непонятно почему. У неё ужасный вкус на мужчин."
    show jessica smile
    mc.c "Надеюсь, они не говорят обо мне то же самое?.."
    show jessica surprise
    jessica.c "Ой, ну конечно нет!"
    show jessica smile talk
    jessica.c "Они пока тебя толком не знают, но по моим рассказам считают, что ты хороший парень."
    show jessica tease talk
    jessica.c "Вообще-то, раз уж мы тут, кажется, они считают тебя красавчиком~"
    show jessica tease
    mc.c "Я? Ни за что... Это ты у нас настоящая добыча."
    show jessica tease talk
    jessica.c "Не знаю... Одна из них может положить на тебя глаз..."
    show jessica tease
    "Это... немного странно. Она улыбается, когда говорит это. Она что-то одобряет?"
    "Я стараюсь не обращать на это внимания и разливаю три бокала."
    mc.c "Ну, за то, что вы такие хорошие посетительницы, эта порция за мой счёт."
    "И чего это я угощаю явно небедных девушек?"
    "В Джессике есть что-то такое... Она умеет заставить тебя прыгать вокруг неё. Кажется, я совсем пропал."
    show jessica joy
    jessica.c "О-о~ Спасибочки~!"
    "Она наклоняется через стойку и целует меня."
    hide jessica with dissolve
    show jessica kiss with dissolve
    jessica.c "Чмок~"
    hide jessica with dissolve
    show jessica smile with dissolve
    "Она уже собирается отнести бокалы, как в другом конце зала что-то громко гремит."
    show jessica surprise
    "Слышно, как дверь распахивается и с грохотом ударяется о стену."
    zoe_unknown "Ну всё, ваш {i}спаситель{/i} здесь. Вот же вы..."
    "Что происходит? Я оглядываюсь."
    show jessica at twoPersonLeft with ease
    show zoe tease talk at twoPersonRight with dissolve
    zoe.c "И что бы вы без меня делали?"
    show zoe tease
    "Зои врывается в бар и сразу заходит за стойку. Что происходит?"
    unknown "Спасибо, Зои..."
    show zoe smile talk
    zoe.c "Ну же, ребята, в следующий раз скажите пораньше. Я же не кусаюсь."
    show zoe smile
    show jessica neutral
    "Она разбирается с другим сотрудником. Похоже, её вызвали подменить того, кто не вышел на смену."
    "Понятно. Рад, что они сами решают такие вопросы и что Зои всегда наготове и готова подменить."
    "Похоже, мне самому надо было заняться этим. Может, я сегодня не следил за общим чатом..."
    "Она направляется сюда."
    show zoe smile talk
    zoe.c "Что такое, худыш? Опять флиртуешь с бедной девушкой?"
    show zoe tease talk
    zoe.c "С ним поосторожнее, он настоящий кобель. Если начнёт приставать — скажи, я его приструню~"
    show zoe tease
    "*Шлёп*"
    show jessica surprise
    "Она шлёпает меня по заднице, проходя мимо, и это замечают все вокруг, включая Джессику."
    hide zoe with dissolve
    "И вот она уходит... Достаёт бокалы из посудомойки."
    show jessica at center with ease
    jessica.c "Эта девушка... Она только что шлёпнула тебя по заднице?"
    mc.c "Э-э..."
    jessica.c "Разве это не сексуальное домогательство на работе?"
    show jessica thinking
    jessica.c "Но ты же начальник... Как это вообще работает?"
    call mcFretAboutPolyamory from _call_mcFretAboutPolyamory_5
    mc.c "Это... Зои, она здесь работает."
    mc.c "Она... моя подруга. Иногда выходит на смену, и... э-э..."
    "Кажется, Зои подслушала."
    show jessica neutral at twoPersonRight with ease
    show zoe tease talk at twoPersonLeft with dissolve
    zoe.c "Подруга~? Да, мы {i}очень{/i} дружны, да, жеребец?"
    show zoe tease
    "Она снова подходит к нам и опирается локтем на моё плечо."
    show zoe tease talk
    zoe.c "[mc.name] тебя не достаёт, милашка? Видимо, этому ненасытному зверю меня мало~"
    show zoe tease
    show jessica neutral talk
    jessica.c "А? Нет, э-э... Мы..."
    show jessica neutral
    if(not mc.polyamoryExplained):
        "Похоже, мне крышка... Как вообще это объяснить? Надо было предвидеть такое..."
        "Зои здесь постоянно. Это должно было когда-нибудь случиться. О чём я думал?"
        "Мне не выкрутиться, Зои слишком явно показывает, что происходит. Насколько серьёзны мои отношения с ней — спорно, но две девушки одновременно? Это может разбить Джессике сердце..."
        "Остаётся только сказать правду..."
        mc.c "Зои... Это Джессика. Я не знаю, как сказать, но..."
        mc.c "Мы... встречаемся. Уже какое-то время..."
        show zoe smile talk
        zoe.c "О-о~ Правда?"
        show zoe smile
        "Она улыбается... Страшно..."
        mc.c "А Джессика, мне очень, очень жаль, но... Я встречался... то есть встречаюсь с Зои."
        mc.c "...Уже какое-то время."
        mc.c "Так получилось... Я ходил на свидания и не понимал, насколько всё становится серьёзным..."
        mc.c "И... и..."
        "Я замолкаю. Что ещё сказать?"
        show jessica smile talk
        jessica.c "О, ладненько! Привет, Зои, я Джессика!"
        show jessica smile
        show zoe smile talk 2
        zoe.c "О, она у нас такая бодренькая? Какое у тебя разнообразие вкусов, а?"
        show zoe smile
        "...Что?"
        "Они просто улыбаются и болтают друг с другом. Я что, неясно объяснил? Они поняли?"
        mc.c "Э-э..."
        show zoe neutral talk
        zoe.c "[mc.name], алло? Что ты так растерялся?"
        show zoe neutral
        show jessica thinking
        jessica.c "Да, ну, что случилось?"
        mc.c "П-прости... Я хотел сказать... Я встречаюсь с вами обеими... До сих пор, прямо сейчас..."
        "Я перевожу взгляд с одной на другую, пытаясь объяснить, но в ответ вижу лишь непонимание."
        show zoe neutral talk
        zoe.c "...Ну да? Чудак."
        show zoe neutral
        show jessica neutral talk
        jessica.c "Не понимаю тебя, [mc.name]. Ты что, собирался встречаться только с Зои?"
        show jessica neutral
        show zoe tease talk
        zoe.c "Мы? Ха! Я похожа на какую-нибудь консервативную психопатку?"
        show zoe tease
        "Я совсем перестаю понимать, что происходит..."
        show zoe smile talk
        zoe.c "Худыш, ты ведь не думал, что я такая, да?"
        show zoe smile
        mc.c "Ну... Мы не обсуждали... То есть... Разве это не?.."
        show jessica smile talk
        jessica.c "Я тоже не обсуждала. Так в чём проблема?"
        show jessica smile
        "Я правда не понимаю. Они обе... не против?"
        mc.c "Я встречаюсь с вами обеими. Я никому из вас об этом не говорил..."
        show jessica thinking
        jessica.c "Не понимаю, из-за чего ты так нервничаешь..."
        show zoe smile talk 2
        zoe.c "Что, это какая-то человеческая заморочка?"
        zoe.c "Нас такое вообще не волнует."
        show zoe smile
        mc.c "То есть... только вас? Или..."
        show zoe smile talk 2
        zoe.c "Нас точно не волнует. По крайней мере, волкоподобных."
        show jessica smile talk 2
        jessica.c "У папы две жены... У вас что, так не принято?"
        show jessica smile
        mc.c "Не особо..."
        show zoe tease talk
        zoe.c "О-о, ты из-за этого переживал? Ха-ха! Как мило~ Похоже, ты вообще ничего не знаешь."
        show zoe tease
        mc.c "...Серьёзно?"
        "Девушки немного рассказывают об отношении антропоморфов к отношениям."
        "Полиамория — это нормально. Люди часто заводят нескольких партнёров, иногда даже вступают в несколько браков. Каждый сам решает, как ему жить, и это считается совершенно обычным."
        call mcPolyamoryExplainedConclusion from _call_mcPolyamoryExplainedConclusion_5
        mc.c "То есть... Вы обе...?"
        show jessica neutral talk
        jessica.c "Ты знаешь, я только-только рассталась с парнем, когда мы познакомились, [mc.name]... И с тех пор была только с тобой."
        show jessica neutral
        show zoe thinking
        zoe.c "Нет... Я давно этим не занималась..."
        show zoe tease talk
        zoe.c "Гордись, сейчас ты удовлетворяешь все мои потребности~"
        zoe.c "Но раз ты так переживаешь... Я буду говорить тебе прямо, ладно, жеребец?"
        show zoe tease
        "Невероятно... Я могу продолжать встречаться с ними обеими..."
    else:
        "Надо было быть откровеннее с самого начала..."
        "За Зои я не особенно переживаю, но совершенно не знаю, как отреагирует Джессика. Всё может пойти плохо..."
        mc.c "Прости, Джессика, Зои, позвольте объяснить."
        mc.c "Зои, это Джессика. Мы встречаемся уже некоторое время..."
        mc.c "А Джессика, я ещё встречался с Зои. Ещё до того, как она начала здесь работать..."
        mc.c "Прости, мне стоило рассказать раньше, но я не знал, как поднять эту тему. Я всё ещё привыкаю к местной культуре свиданий."
        mc.c "Вы обе... не против?"
        if(zoe.polyamoryExplained):
            show zoe thinking
            zoe.c "Мы ведь уже это обсуждали, [mc.name], помнишь? Не нервничай..."
        else:
            show zoe smile talk
            zoe.c "О-о, посмотри на себя~ Чего ты так переживаешь? Думаешь, меня это волнует?"
        show zoe smile
        if(jessica.polyamoryExplained):
            show jessica smile talk 2
            jessica.c "Я уже говорила, что не против, так что..."
        show jessica smile talk
        jessica.c "А почему я должна быть против, глупыш? Я вроде не говорила обратного..."
        show jessica smile
        mc.c "Наверное, я всё ещё не привык к этому... Наши отношения развивались с разной скоростью, а я не успел во всём разобраться..."
        "Зои снова шлёпает меня по заднице."
        show zoe tease talk
        zoe.c "Хватит быть таким сентиментальным, жеребец. Фу, аж противно..."
        show zoe tease
        show jessica tease talk
        jessica.c "Ой~ Не будь такой. Мне нравится, когда он милый."
        show jessica tease
    call playMusic(barTheme) from _call_playMusic_330
    show zoe smile talk
    zoe.c "Раз [mc.name] перестал чудить..."
    zoe.c "Кстати, кажется, я видела тебя раньше в клубе? Твою куртку легко узнать..."
    show zoe smile
    show jessica joy
    jessica.c "О, ты про мою сумочку «Фьюттон»? Купила пару недель назад, {i}такая классная{/i}, да?"
    show zoe neutral talk
    zoe.c "Э-э... Я имела в виду пятна..."
    show zoe surprise
    zoe.c "Погоди, у тебя сумка «Фьюттон»? Откуда она у тебя, чёрт возьми?!"
    show jessica neutral talk
    jessica.c "Я... купила?.. В магазине?.."
    show jessica neutral
    zoe.c "Вот же богачка, худыш? Золотишко копаешь, пёс мелкий?"
    show jessica bashful talk
    jessica.c "Она была не такая уж дорогая..."
    show jessica bashful
    show zoe thinking
    zoe.c "Понятно, что ты задумал, худыш... Ловко..."
    show zoe tease talk
    zoe.c "Когда урвёшь немного денег, поделись с нами, ладно?"
    show zoe tease
    show jessica bashful talk
    jessica.c "Пожалуй, я всё-таки заплачу за напитки..."
    show jessica bashful
    scene black with fade
    "Мы ещё немного болтаем, пока Джессика и её подруги допивают."
    "Зои продолжает поддразнивать меня из-за того, что я переживал о разговоре об отношениях."
    "Похоже, всё может продолжаться... Как же мне управляться с этими двумя?"

    if(not fromGallery):
        $ zoe.polyamoryExplained = True
        $ jessica.polyamoryExplained = True
        $ mc.polyamoryExplained = True
        $ zoe.knowsDating = list(set(zoe.knowsDating + [jessica]))
        $ jessica.knowsDating = list(set(jessica.knowsDating + [zoe]))

    return

label zoeJessicaHEvent1(fromGallery):
    $ location_home.showBackground()
    call playMusic(barTheme) from _call_playMusic_331
    "*Зевок*"
    "Долгий был день... А когда я вернулся домой, пришли важные письма."
    "Поздняя ночь — позже, чем обычно. Нужно было разобраться с письмами, иначе они бы не давали мне уснуть."
    "Кое-как продержался на кофеине, но теперь совсем вымотался."
    "Пора ложиться. Немного привычного бесконечного листания ленты — и я отключусь."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Я беру телефон, и он тут же вибрирует."
    "Сообщение от... Джессики? Что это?"
    jessica.c "uy ionmm-&s>>"
    "...Что?"
    "Может, она написала его задницей, а может, это одно из её пьяных сообщений. В этот раз особенно непонятное."
    "Я просто отправляю в ответ вопросительный знак. Неважно, ответит ли она."
    "Я снова смотрю на телефон — сообщение быстро помечено прочитанным. Она онлайн, но не отвечает."
    "Я в недоумении откладываю телефон и готовлюсь ко сну. Наверное, сегодня она где-то развлекается."
    "Быстро переодевшись и почистив зубы..."
    "*Дзинь-дон*"
    "А? Кто-то у двери? В такой час? Сосед, что ли?"
    "Я осторожно подхожу к двери и открываю..."
    call playMusic(funnyTheme) from _call_playMusic_332
    show zoe tease talk at twoPersonLeft
    show jessica joy at twoPersonRight
    with dissolve
    "Обе" "Эйййййй~~~~"
    show zoe tease
    "Зои и Джессика покачиваясь стоят в дверях, обнявшись за талию."
    "Глаза полузакрыты, на лицах расплылись пьяные улыбки. Они слегка покачиваются — очевидно, что этой ночью они куда-то ходили."
    show jessica tease talk
    jessica.c "[mc.name]~ Пусти нассс~"
    show jessica tease
    "Она громко и невнятно произносит это для такого позднего часа."
    mc.c "Тише, девочки, ладно? Уже поздно."
    show zoe tease talk
    zoe.c "Мы будем паиньками~"
    show zoe tease
    "Я осторожно впускаю их. Они спотыкаются, падают на диван, скидывают туфли и бросают сумочки через всю комнату."
    show jessica joy
    jessica.c "А-а-а-ха-ха~"
    mc.c "Ну... Вы сегодня гуляли?"
    show zoe smile talk
    zoe.c "В «Бархатную комнату», знаешь, в клуб, куда я не могу затащить тебя, большой ребёнок~"
    show zoe smile
    mc.c "Так и думал. Хорошо провели время?"
    show jessica tease talk
    jessica.c "Офигенно весело~"
    show jessica tease
    mc.c "Здорово, что вы проводите время вместе. Не знал, что вы собираетесь встретиться."
    show zoe smile talk
    zoe.c "Мы случайно встретились там. Каждая была со своей компанией, но потом все разошлись."
    show zoe smile
    show jessica tease talk
    jessica.c "Мы разговорились! Зои такая классная!"
    show jessica tease
    show zoe smile talk
    zoe.c "Так ты и правда охотник за деньгами, да, худыш? Вот это богачка~"
    show zoe smile
    show jessica joy
    jessica.c "О боже~ Стерва~ Заткнись~"
    "Они игриво толкают друг друга. Кажется, они поладили — по-своему, по-девичьи."
    "Забавное сочетание... Я не мог представить их вместе, но, похоже, у них есть общее."
    show jessica tease talk
    jessica.c "Мы точно пойдём по магазинам, как и договорились~"
    show jessica tease
    show zoe smile talk 2
    zoe.c "Погоди, девочка. После того последнего напитка я пока на мели..."
    show zoe tease talk
    zoe.c "Если только наш босс не даст ещё премию за хорошее поведение...?"
    show zoe tease
    mc.c "Интересное у тебя понимание «хорошего поведения» — врываться сюда так поздно. Обычно я уже сплю."
    mc.c "Кстати... Что вы вообще здесь делаете?"
    show jessica joy
    jessica.c "Почему бы и нет~ Было весело, но когда там остались только я и Зо, стало совсем скучно~"
    show jessica tease talk
    jessica.c "Почему бы не выпить ещё? Ты никогда с нами не ходишь..."
    show jessica tease
    show zoe smile talk 2
    zoe.c "Не выгонишь нас, жеребец? К тому же... Мы тут разговаривали..."
    show zoe smile talk
    zoe.c "О {i}тебе~{/i}"
    show zoe smile
    show jessica surprise
    jessica.c "Нет, правда?!"
    show zoe tease talk
    zoe.c "Что такое, девочка? Раньше ты выглядела заинтересованной~"
    show zoe tease
    show jessica bashful talk
    jessica.c "Ой, да ладно... Раз уж мы здесь..."
    show jessica bashful
    "Любопытно..."
    mc.c "Ну и что интересного?"
    show zoe smile talk 2
    zoe.c "Хм~ Сравнивали заметки?"
    show zoe smile
    show jessica tease
    jessica.c "Хи-хи~"
    call stopMusic from _call_stopMusic_61
    show zoe smile talk
    zoe.c "О том, кто лучше тебя трахает."
    show zoe smile
    "...Ладно..."
    mc.c "Так... Мне стоит волноваться?"
    show jessica joy
    jessica.c "Хи-хи~ Зо говорила, что ты был л- {w=1.0}{nw}"
    show zoe mad talk
    zoe.c "П-погоди, Джесс! Это девчачьи разговоры, ясно?"
    show zoe mad
    show jessica tease talk
    jessica.c "Хи-хи~"
    show jessica tease
    show zoe smile talk
    zoe.c "Короче... Ты сдаёшь на троечку, жеребец. Но тебе ещё предстоит испытание..."
    show zoe smile talk 2
    zoe.c "Ничего сложного, думаю, тебе понравится~"
    show zoe smile
    "Кажется, я понимаю, к чему это идёт. И мне, наверное, понравится."
    mc.c "И что же это?"
    call playMusic(sexyTheme) from _call_playMusic_333
    "Зои начинает расстёгивать рубашку."
    show zoe tease talk
    zoe.c "Сними с него штаны."
    zoe.c "Не волнуйся, Джесс, можешь им поманипулировать. Кажется, ему нравится~"
    show jessica smile
    jessica.c "Хм~"
    scene black with fade
    "Девушки почти силой тащат меня к кровати, по дороге раздевая меня и себя."
    zoe.c "В этот раз ты должен удовлетворить {i}нас обеих{/i}, жеребец."
    jessica.c "Как это будет?"
    zoe.c "Тебе достанется первый член, девочка. А я прокачусь на своём~"
    "Девушки устраиваются..."
    scene zoejessicacowgirlstart with fade
    pause
    "Джессика садится верхом на мой член, а Зои подозрительно нависает у меня над головой. Интересно, что она собирается делать..."
    jessica.c "О боже, даже не знаю~"
    zoe.c "Не переживай, будет весело. А старому худышу понравится."
    jessica.c "Ты... называешь его худышом? Это же... ну..."
    zoe.c "Он не жалуется. К тому же теперь мы командуем, девочка."
    "Джессика трётся киской о мой член и вот-вот опустится на него."
    "Зои подползает к ней и располагается бёдрами прямо у меня над лицом. Она собирается меня задушить..."
    jessica.c "Это странно, но, чёрт, мне давно этого хотелось..."
    zoe.c "Посмотрим, на что способен этот язычок..."
    image zoe jessica cowgirl part 1 = Movie(play="images/characters/zoejessica/cowgirl/part1.webm")
    show zoe jessica cowgirl part 1 with fade
    pause
    "Джессика опускается на колени и насаживается на мой член до основания."
    "Она с силой прижимает меня к кровати и вдавливается в мои бёдра."
    jessica.c "О-о-о~ М-м-м~ Чёрт~"
    "А Зои просто садится мне на лицо. Я полностью утопаю лицом в её мокрой киске."
    "Невероятное ощущение: меня целиком обволакивает горячая влажная шелковистая шерсть — и сверху, и снизу."
    jessica.c "М-м-м~ А-а~"
    zoe.c "Покажи ему незабываемое, девочка. Хочу чувствовать, как он тяжело дышит внизу."
    image zoe jessica cowgirl part 2 = Movie(play="images/characters/zoejessica/cowgirl/part2.webm")
    show zoe jessica cowgirl part 2 with fade
    pause
    "Как обычно у Зои, это выглядит как доминирующий жест, но мне от него одно сплошное удовольствие."
    "Я кружу языком по её горячим влажным складочкам. Она прижимается ко мне, почти не давая дышать, но я чувствую, как она вздрагивает."
    zoe.c "О да~ Вот так, жеребец~ М-м~"
    jessica.c "А-а~ Он может... М-м~ дышать?"
    "Я лишь показываю большой палец — рот занят. Я в раю."
    "Я лакаю соки Зои, полностью утопая в её удовольствии. Честно говоря, дышать немного трудно. Но какая смерть..."
    zoe.c "О да~ Глубже языком, жеребец~"
    jessica.c "М-м~ Он такой твёрдый~"
    zoe.c "А-а~ Скачи на нём как следует, Джесс. Вот..."
    "Зои тянется к плечам Джессики..."
    image zoe jessica cowgirl part 3 = Movie(play="images/characters/zoejessica/cowgirl/part3.webm")
    show zoe jessica cowgirl part 3 with fade
    pause
    jessica.c "А-а~ А-а-а~ М-м-м~"
    "Джессика яростно скачет на мне, вдавливая меня в кровать."
    "Я чувствую, как её киска сжимается с каждым движением, а когти впиваются мне в грудь."
    jessica.c "Чёрт~ Чёрт~"
    "Зои наваливается на меня всем весом и вращает бёдрами, пока я ласкаю её киску языком."
    zoe.c "А-а-а~ Да-а~"
    image zoe jessica cowgirl part 4 = Movie(play="images/characters/zoejessica/cowgirl/part4.webm")
    show zoe jessica cowgirl part 4 with fade
    pause
    "От Зои исходит жар, а моё лицо всё мокрое от удовольствия."
    "Ощущения невероятные, я вот-вот кончу..."
    zoe.c "Ох, чёрт, да~ Ещё, ещё~"
    jessica.c "М-м~ М-м~ Я сейчас кончу~"
    zoe.c "А-а~ Уже почти~ П-погоди, девочка~"
    "Их движения становятся всё быстрее — мы все вот-вот достигнем оргазма."
    "Я могу лишь глухо стонать, полностью зажатый между ними."
    jessica.c "М-м-м~"
    zoe.c "А-а-а~"
    scene zoejessicacowgirlend1 with fadewhite
    pause
    jessica.c "А-а-а-а-а~"
    zoe.c "Ч-ёрт~!"
    "Моё лицо заливает горячей влагой, Зои кончает и содрогается от экстаза."
    "Я крепко хватаю Джессику за бёдра и изливаю в неё сперму, пока она прижимает меня к постели."
    "Мы превращаемся в сцену разврата, крича и содрогаясь от общего оргазма."
    scene zoejessicacowgirlend2 with fade
    pause
    "Девушки падают без сил. Мы лежим в собственной жидкости, тяжело дыша и хватая ртом воздух."
    jessica.c "А-а-а~ О-о~"
    zoe.c "А-а... Ах..."
    mc.c "О боже..."
    "Все мы ошеломлённо пытаемся отдышаться."
    zoe.c "Вот это да~ Ты и правда умеешь *а-а* стараться, жеребец~"
    jessica.c "Таак хорошо~"
    "Я тоже совершенно вымотан. Даже просто лежать и позволять им всё делать оказалось невероятно утомительно, но потрясающе."
    "Девушки слегка шевелятся, тяжело дышат и довольно улыбаются."
    "Я оглядываюсь на разбросанную одежду. Как теперь доставить их домой?"
    mc.c "Ну что... Я сдал?"
    call stopMusic from _call_stopMusic_62
    "..."
    mc.c "Джесс? Зои?"
    "..."
    "Я смотрю на них. Обе вырубились и крепко спят."
    "Наверное, вечер у них выдался бурным — теперь их свалило от выпивки."
    "Похоже, они останутся на ночь... Да я и не против."
    "На остатках сил я устраиваю их поудобнее и ложусь рядом. Для меня уже слишком поздно."
    "Обе тихонько сопят, на лицах чуть сонные, довольные улыбки."
    "Вот это была ночь."
    scene black with fade
    "..."
    "..."
    scene zoejessicacowgirlend3 with Fade(2.0, 0.0, 2.0)
    call playMusic(barTheme) from _call_playMusic_334
    "Незнакомое приветствие."
    "...А, точно... Они вчера вырубились здесь. Вот это была ночь."
    jessica.c "М-м... [mc.name]?.."
    "Выглядят они ужасно."
    mc.c "Давно проснулись?"
    jessica.c "Нет... Мне хреново... Голова..."
    mc.c "А Зои?"
    zoe.c "М-м-м... Не разговаривай со мной..."
    "Наверное, вчера они перебрали."
    mc.c "Хотите позавтракать?"
    jessica.c "...Звучит неплохо..."
    scene black with fade
    "После неторопливого утра девушки наконец приходят в себя."
    "Они уходят с головной болью, но без сожалений. Я тоже ни о чём не жалею."
    "Вот это была ночь."

    return {'time':'Morning'}
