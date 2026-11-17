define persistent.knowCharacterLocations = True
define persistent.eventHints = True
define persistent.groupSex = True
define persistent.cheatsEnabled = False
define persistent.debugMode = False
define persistent.cheatMode = False
define persistent.likeLoveMultiplier = 1
define persistent.dialogueBoxOpacity = 1.0
define persistent.tutorialSeen = False

translate spanish python:
    gui.text_font = "DejaVuSans.ttf"
    gui.system_font = "DejaVuSans.ttf"
    gui.button_text_font = "DejaVuSans.ttf"
    gui.interface_text_font = "DejaVuSans.ttf"
    gui.name_text_font = "DejaVuSans.ttf"

# System: Called on loads of save file 
label after_load:
    $ upgraded = False
    #debug "config [config.version]"
    #debug "store [store._version]"
    if store._version != config.version:
        #debug "Needs Upgrade"
        $ upgraded = True

    if upgraded:
        # Stop roll back to an unsupported game state.
        $ renpy.block_rollback()
        call hideAllScreens from _call_hideAllScreens_8
        call updater from _call_updater_1
    $ store._version = config.version
    if upgraded:
        $ renpy.pop_call()
        $ renpy.block_rollback()
        call goToLocation(location_home) from _call_goToLocation_8
    return

label splashscreen:
    scene black
    with Pause(0.5)
    show screen patreonBackerScreen with dissolve
    with Pause(7)
    hide screen patreonBackerScreen with dissolve
    return

screen patreonBackerScreen:
    vbox:
        align (0.5, 0.5)
        style_prefix 'splashScreenPatrons'
        text "Игра от ofkeres":
            color '#ffffff'
        text "Особая благодарность моим подписчикам на Patreon:":
            color '#ffffff'
        text "" size 10
        text "{b}[patronTopSupporterTitle]:{/b}":
            color '#71368a'
            size 38
        hbox:
            for supporter in patronTopSupporters:
                text supporter:
                    color '#71368a'
                    size 38
        text "" size 15
        text "{b}[patronSuperSupporterTitle]:{/b}":
            color '#e74c3c'
            size 32
        hbox:
            for supporter in patronSuperSupporters:
                text supporter:
                    color '#e74c3c'
                    size 32
        text "" size 15
        text "{b}[patronExtraSupporterTitle]:{/b}":
            color '#c27c0e'
            size 32
        hbox:
            for supporter in patronExtraSupporters:
                text supporter:
                    color '#c27c0e'
                    size 32
        text "" size 15
        text "{b}[patronSupporterTitle]:{/b}":
            color '#206694'
            size 30
        hbox:
            for supporter in patronSupporters:
                text supporter:
                    color '#206694'
                    size 30

style splashScreenPatrons_text:
    text_align 0.5
    align (0.5, 0.5)

style splashScreenPatrons_hbox:
    xalign 0.5
    spacing 75
    box_wrap True
    box_align 0.5

# System: New Game call. Initialise objects and attributes
label start:
    call initialiseLocations from _call_initialiseLocations
    call initialiseCharacters from _call_initialiseCharacters
    call updateCharacterStatics from _call_updateCharacterStatics_1
    call initialiseWorld from _call_initialiseWorld
    jump newGame
    #jump devNewGame

# The game starts here proper
label newGame:
    python:
        persistent.cheatsEnabled = False
        persistent.likeLoveMultiplier = 1
        persistent.debugMode = False
        persistent.cheatMode = False
    call stopMusic from _call_stopMusic_77
    "Как тебя зовут?"
    python:
        mcNameInput = renpy.input(prompt='Введите имя:', default = 'MC', length=20)
        mcNameInput = mcNameInput.strip()
        mc.name = mcNameInput
        mc.c.name = mcNameInput
    mc.c "Меня зовут [mc.name]."
    menu:
        "Пропустить вступление?"
        "Да":
            pass
        "Нет":
            call intro from _call_intro
    $ location_home.showBackground()
    if(not persistent.tutorialSeen):
        $ persistent.tutorialSeen = True
        menu:
            "Показать краткое обучение?"
            "Да":
                call gameTutorial from _call_gameTutorial
            "Нет":
                pass
    call goToLocation(location_home) from _call_goToLocation_9

label devNewGame:
    python:
        persistent.cheatsEnabled = True
        mc.money = 10000
        sarah.knownToMC = True
        sarah.isDateable = True
        sarah.like = 99
        sarah.love = 99
        alice.knownToMC = True
        alice.isDateable = True
        alice.like = 99
        alice.love = 99
        katie.knownToMC = True
        katie.isDateable = True
        katie.like = 99
        katie.love = 99
        grace.knownToMC = True
        grace.isDateable = True
        grace.like = 99
        grace.love = 99
        zoe.knownToMC = True
        zoe.isDateable = True
        zoe.like = 99
        zoe.love = 99
        jessica.knownToMC = True
        jessica.isDateable = True
        jessica.like = 99
        jessica.love = 99
        molly.knownToMC = True
        molly.isDateable = True
        molly.like = 99
        molly.love = 99
        eve.knownToMC = True
        eve.isDateable = True
        eve.like = 99
        eve.love = 99
    call goToLocation(location_home) from _call_goToLocation_10

label intro:
    mc.c "Ну вот, наконец-то распаковал вещи. Кажется, начинаю привыкать..."
    call playMusic(mainTheme) from _call_playMusic_370
    $ location_home.showBackground()
    "Опять пришлось переехать."
    "Цены росли так быстро, что меня вот-вот должны были выселить из квартиры. Я не знал, что делать."
    "Я работал в баре в родном городе. Всё шло неплохо. Даже получил небольшой стаж, если это можно так назвать."
    "И тут начальник сделал мне предложение."
    "Его старый друг из другого города попросил о помощи. Он хотел уйти на пенсию и оставить собственный бар, но не мог найти желающих принять его дела."
    "Никто не хотел брать аренду на себя, но он не мог просто закрыть бар насовсем. Это было его наследие."
    "Невероятно, но начальник предложил мне занять его место. Руководить всем баром."
    "Он сказал, что бар уже приносит прибыль и будет приносить её дальше, и что у меня всё получится."
    "Редкая возможность. Шанс не просто существовать, а самому выбрать свой путь."
    $ location_map.showBackground()
    "Но это очень далеко отсюда. Честно говоря, я едва слышал об этом месте. Оказалось, это довольно большой приморский городок на другом конце страны."
    "Это относительно молодой город, и, говорят, большинство жителей — антропоморфы. Я не против, просто удивительно, что такие обособленные общины существуют и в наши дни."
    "Надеюсь, я им тоже не помешаю? Не знаю. Дома и в поездках я лишь изредка встречал антропоморфов."
    "У меня были сомнения. Здесь я никого не знаю. Давно мне не приходилось знакомиться с новыми людьми. Если не получится, здесь будет очень одиноко."
    "Но пора было что-то менять. Начать с чистого листа. Я достаточно перебивался случайными подработками и устал от одних и тех же мест и лиц."
    $ location_town.showBackground()
    "Университет был не для меня. Диплом ничего для меня не значил. Я не хотел становиться офисным работником, ушлым продавцом или кем там ещё становятся обычные люди."
    "Я хотел жить свободнее. Но это несбыточная мечта. Обычному парню такая роскошь недоступна."
    "Мне не нужно ничего особенного. Просто возможность жить по-своему."
    window hide
    pause
    "Место выглядит неплохо."
    "Чистые улицы."
    $ location_beach.showBackground()
    "Отличный климат. Море рядом."
    $ location_park.showBackground()
    "Тихие уголки. Могло быть и хуже."
    "Надеюсь, с работой всё будет хорошо."
    $ location_home.showBackground()
    "Начальник сказал прийти сегодня после обеда, забрать ключи и ознакомиться с делами."
    "Честно говоря, до сих пор не верится."
    "Пожалуй, пора идти."
    $ location_bar.showBackground()
    "Вот и он."
    "Я оглядываю бар в деревенском стиле. Открытые стены, колонны и трубы. Простые столики. Холодный пол. Самое настоящее непритязательное заведение вдали от проторенных дорог."
    "Выглядит как место, к которому я привык. Это поможет: надеюсь, управлять им будет так же, как баром у меня дома."
    "За стойкой в дальнем конце зала единственный посетитель потягивает пиво ранним днём, уткнувшись в газету."
    "Другой мужчина за стойкой протирает стакан и поднимает глаза."
    show man with dissolve
    unknown "Выпить пришёл, сынок? Или кого-то ищешь?"
    "Прежде чем я успеваю ответить, он быстро смотрит на часы и снова поднимает голову."
    unknown "А, ты, должно быть, [mc.name]? Сегодня тот самый день, да?"
    mc.c "Ага, это я."
    terry "Я Терри. Мы разговаривали по телефону."
    mc.c "Приятно познакомиться."
    "Мы крепко жмём друг другу руки."
    "Это старый друг моего бывшего начальника, который уходит на пенсию. Он явно рад, что нашёлся человек, готовый принять дела. Бар — его гордость и радость."
    terry "Рад, что ты приехал, сынок. Никого не нашлось, кто захотел бы взяться за это место."
    terry "Молодёжь видит тут только старую забегаловку. Недостаточно модно для них."
    terry "Не очень-то я его рекламирую, да? Ну ладно, теперь уже поздно, сынок."
    "Он громко смеётся."
    mc.c "Всё нормально, Терри. Бар, где я работал дома, был таким же. С нетерпением жду начала."
    terry "Спасибо, парень. Я и сам им горжусь."
    "Я сажусь, а Терри обходит стойку."
    terry "Ты и так знаешь, как всё устроено. Краны, стаканы, бутылки, погреб, касса..."
    "Терри несколько минут показывает мне бар и объясняет основы. Ничего сложного."
    terry "...По словам моего приятеля, ты знаешь своё дело."
    terry "Здесь редко бывает слишком людно. Но посетители разные, и это помогает сводить концы с концами. Постоянные посетители, редкие туристы и студенты, которые то приезжают в город, то уезжают."
    terry "Как ты уже заметил, тут в основном антропоморфы. Так было всегда. Меня это устраивает: выпить они любят не меньше людей, так что для бизнеса это только плюс!"
    "Терри снова смеётся. Но когда он говорит о прошлом, в его голосе слышится лёгкая грусть."
    terry "Ты издалека добирался, да? Совсем не как дома, верно? Спасибо, что проделал такой путь."
    mc.c "Да, немного. Но всё нормально, я не особо привязан к дому. Считаю это шансом начать здесь с чистого листа."
    terry "Всё у тебя получится, сынок. Я живу неподалёку, так что если будут проблемы с обустройством — дай знать. Поможем."
    terry "Уверен, будешь время от времени видеть меня здесь. Только теперь — по другую сторону стойки."
    "Терри понимающе подмигивает и улыбается."
    mc.c "Спасибо, Терри, я ценю это."
    "Терри вешает последний протёртый стакан."
    terry "Ну, пожалуй, на этом всё."
    terry "Я уже говорил, что тут есть пара работников на полставки. Присматривай за ними — ребята хорошие."
    mc.c "Звучит отлично, Терри. Всё понял."
    terry "Ну что, готов начинать? Дай старику закончить последнюю смену. А теперь всё это твоё, парень."
    hide man with dissolve
    "Терри поворачивается и скрывается в погребе, перебирая коробки и бочки."
    "Пора начинать. Пока Терри показывал мне бар, заглянула ещё пара пожилых посетителей. Он без заминки обслужил их, и они устроились в углу с напитками."
    "В баре тихо играет музыка по радио — ровно настолько громко, чтобы разбавить тишину. В тёплый день входная дверь открыта, с улицы доносятся шум и шаги прохожих."
    "Пока дел немного, воспользуюсь случаем и протру стойку."
    call stopMusic from _call_stopMusic_78
    scene black with fade
    "Смена проходит спокойно. Мы подали несколько напитков и закусок, а Терри время от времени выглядывал из погреба."
    "Некоторые завсегдатаи уже знали, что Терри уходит на пенсию, и им было любопытно, кто его сменит. Все отнеслись ко мне очень тепло."
    $ location_bar.showBackground()
    "День близится к концу. В целом тихо, можно поболтать с постоянными посетителями."
    "Как раз когда Терри заканчивает внизу и возвращается, входит компания из шести человек и занимает столик."
    "По одежде видно, что они заметно моложе и моднее остальных сегодняшних посетителей."
    call playMusic(funnyTheme) from _call_playMusic_371
    show man with dissolve
    terry "Ну как, ребята? Рад, что снова заглянули."
    "Компания машет Терри и окликает его."
    unknown "Как обычно, начальник!"
    terry "Есть!"
    "Терри поворачивается ко мне и ставит на стойку два кувшина."
    terry "Это те студенты, о которых я говорил. Часто заходят недорого выпить. И пьют они немало. Хорошие клиенты."
    hide man with dissolve
    "Компания заказывает пару кувшинов лагера. Пока Терри болтает с ними, видно, что они давно знакомы и шутят с хозяином."
    "Похоже, все они антропоморфы разных видов. Неудивительно — в городе я видел таких немало."
    "Наполнив кувшины, я направляюсь к столику."
    "Когда я ставлю их на стол, несколько благодарных кивков сменяются удивлёнными взглядами."
    scene sarahintroi1 with fade
    pause
    "Одна девушка за столом поднимает на меня взгляд. В её глазах смешались удивление, растерянность и любопытство."
    "Светло-коричневая шерсть с маленькими пучками, почти скрытыми короткой майкой. Небрежная коричневая стрижка-каре и большие висячие уши."
    "Густые брови нависают над большими щенячьими глазами. Она буквально похожа на..."
    "Похоже, она из семейства псовых. За столом собрались самые разные виды."
    "К такому зрелищу мне придётся привыкнуть. Судя по лицу девушки, им тоже придётся привыкнуть ко мне."
    $ location_bar.showBackground()
    show sarah surprise with dissolve
    sarah_unknown "Ничего себе, привет! Терри, я не знала, что у тебя есть сын!"
    show sarah at twoPersonRight with ease
    show man at twoPersonLeft with dissolve
    terry "О чём ты? У меня нет детей."
    sarah_unknown "Тогда кто это?"
    terry "Это [mc.name], он сменит старика. Теперь вы будете у него в надёжных руках."
    show sarah thinking
    "Девушка скептически смотрит на меня."
    sarah_unknown "Какова вероятность, что баром снова управляет человек? Ты меня не разыгрываешь?"
    terry "В наших краях не только я один, знаешь ли."
    mc.c "Он прав, я только сегодня переехал. И он мне не отец..."
    "Меня лишь слегка задевает, что нас считают похожими. Терри — далеко не красавец. Может, для них мы все выглядим одинаково."
    show sarah bashful
    "Девушка заметно сникает и ёрзает на стуле."
    show sarah bashful talk
    sarah_unknown "Ой, чёрт... Это было очень грубо. Прости... Просто..."
    show sarah bashful
    mc.c "Да всё нормально, понимаю. Нас тут не так много, да, Терри?"
    "Если это завсегдатаи, надо произвести хорошее впечатление и разрядить обстановку."
    mc.c "Да и к тому же, я явно не унаследовал его безупречную внешность."
    "За столом раздаются смешки."
    terry "Вот именно, парень. Думаю, ты справишься."
    sarah.c "А, ха-ха..."
    unknown "Не обращайте внимания на Сару, она редко думает, прежде чем говорить."
    show sarah sad talk
    sarah.c "Эй, это не пра... Ну, может быть... Но..."
    show sarah sad
    "За столом снова раздаётся смех, и все разливают напитки по бокалам."
    mc.c "Всё нормально. Наслаждайтесь напитками, и зовите, если что-нибудь понадобится."
    unknown "Спасибо!"
    sarah.c "Прости ещё раз..."
    hide man
    hide sarah
    with dissolve
    "Мы возвращаемся к стойке, оставив молодых посетителей за столиком."
    $ location_bar.showBackground()
    "Компания шумно и весело проводит время: болтают, смеются, пьют и закусывают, пока не приходит время закрываться."
    "Даже у той девушки, [sarah.name], настроение быстро улучшилось."
    "Пора закрываться. Компания начинает собираться."
    unknown "Пока, Терри!"
    terry "Пока, ребята! Хорошего вечера. Не переживайте, я ещё буду иногда сюда заглядывать."
    "Пока я убираю со стола, девушка задерживается, пока остальные выходят, а затем оборачивается ко мне."
    show sarah neutral talk with dissolve
    sarah.c "Привет, прости ещё раз. Не хотела грубить."
    mc.c "Я не обиделся, правда! Было смешно."
    show sarah smile talk
    sarah.c "О, здорово. Не обращай внимания, я, как они говорят, немного неуклюжая."
    sarah.c "Кстати, меня зовут [sarah.name]."
    mc.c "Приятно познакомиться, [sarah.name]. Я [mc.c]."
    show sarah smile talk 2
    sarah.c "Ещё увидимся? Мы часто сюда заходим."
    show sarah smile
    mc.c "Буду ждать встречи. Хорошего вечера."
    hide sarah with dissolve
    $ location_home.showBackground()
    "Неплохо для первого дня. Похоже, беспокоиться не о чем."
    "До сих пор не верится. Теперь я здесь главный. Ответственность немалая."
    "Начинается моя новая жизнь."
    return
