init offset = 3

default katieMollyDuoStoryEvent1 = Event('Деловая встреча', 'katieMollyDuoStoryEvent1', [katie, molly], 0, 0, [katieHEvent3, mollyHEvent3], location_bar, ['Evening'], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
default katieMollyDuoHEvent1 = Event('Готовка', 'katieMollyDuoHEvent1', [katie, molly], 0, 0, [katieMollyDuoStoryEvent1, katieHEvent4, mollyHEvent4], location_home, ['Evening'])
default katieMollyDuoHEvent2 = Event('Девичник', 'katieMollyDuoHEvent2', [katie, molly], 0, 0, [katieMollyDuoHEvent1, katieHEvent5, mollyHEvent5], location_bar, ['Evening', 'Night'], ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

label katiemollySexSelect:
    hide screen mainUi
    image katiemolly idle = Movie(play="images/characters/katiemolly/sexWaiting.webm")
    show katiemolly idle with fade
    call screen katiemollySexSelectScreen
    call endScene(targetLocation = location_home) from _call_endScene_19

screen katiemollySexSelectScreen:
    modal True
    zorder 3
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            if(katieMollyDuoHEvent1.unlocked or persistent.debugMode):
                textbutton 'Тройничок' keysym str(1):
                    action [Jump('katieMollyThreesome')]
            else:
                textbutton 'Закрыто'
            if(katieMollyDuoHEvent2.unlocked or persistent.debugMode):
                textbutton 'Ласки грудью вдвоём' keysym str(2):
                    action [Jump('katieMollyDoubleBoobjob')]
            else:
                textbutton 'Закрыто'
            textbutton 'Выход' keysym str(3):
                action [Hide('katiemollySexSelectScreen'), Return()]

label katieMollyThreesome:
    scene katiemollyhevent1i1 with fade
    pause
    image katiemolly katie fuck 1 = Movie(play="images/characters/katiemolly/hevent1/katiefuck1.webm")
    show katiemolly katie fuck 1 with fade
    pause
    image katiemolly katie fuck 2 = Movie(play="images/characters/katiemolly/hevent1/katiefuck2.webm")
    show katiemolly katie fuck 2 with fade
    pause
    image katiemolly molly fuck 1 = Movie(play="images/characters/katiemolly/hevent1/mollyfuck1.webm")
    show katiemolly molly fuck 1 with fade
    pause
    image katiemolly molly fuck 2 = Movie(play="images/characters/katiemolly/hevent1/mollyfuck2.webm")
    show katiemolly molly fuck 2 with fade
    pause
    scene katiemollythreesomeend with fadewhite
    pause
    jump katiemollySexSelect

label katieMollyDoubleBoobjob:
    image katiemolly handjob = Movie(play="images/characters/katiemolly/hevent2/handjob.webm")
    show katiemolly handjob with fade
    pause
    image katiemolly boobjob 1 = Movie(play="images/characters/katiemolly/hevent2/boobjob1.webm")
    show katiemolly boobjob 1 with fade
    pause
    image katiemolly boobjob 2 = Movie(play="images/characters/katiemolly/hevent2/boobjob2.webm")
    show katiemolly boobjob 2 with fade
    pause
    image katiemolly boobjob 3 = Movie(play="images/characters/katiemolly/hevent2/boobjob3.webm")
    show katiemolly boobjob 3 with fade
    pause
    scene katiemollyboobjobfinish1 with fadewhite
    pause
    scene katiemollyboobjobfinish2 with dissolve
    pause
    jump katiemollySexSelect

label katieMollyDuoStoryEvent1(fromGallery):
    $ location_town.showBackground()
    call playMusic(barTheme) from _call_playMusic_303
    "Захожу в бар подменить кого-нибудь на вечерней смене. Не особо хочется — обычно это самое загруженное время."
    "Погоди, я же владелец, должен радоваться. Больше денег, да? Чёрт, я такой ленивый."
    "Ладно, посмотрим."
    $ location_bar.showBackground()
    "О, не так уж плохо. Всего несколько посетителей, заняты лишь пара столиков. Ещё один день, когда можно отлынивать."
    "Я уже собираюсь пройти за стойку, как сразу замечаю..."
    show katie smile at twoPersonLeft
    show molly smile at twoPersonRight
    with dissolve
    "Здесь Кэти и Молли. Они сидят рядом у стойки, с напитками. И... разговаривают?"
    "Они были знакомы? Только что встретились? Случайно пересеклись после работы? Ни одна не говорила, что сегодня придёт."
    "Я замираю чуть поодаль и слышу их разговор..."
    show katie neutral talk
    katie.c "Ты снова отлично справилась. Мой начальник, как видишь, настоящий заноза в заднице..."
    show katie smile talk
    katie.c "Не сомневаюсь, из-за него мы и оказались в такой ситуации. Вечно он всё делает по-своему..."
    show katie smile
    show molly neutral talk
    molly.c "Ничего страшного. Для этого и нужны такие встречи, как сегодня, чтобы разобраться в делах."
    molly.c "Не волнуйтесь, всё в порядке. Нужно лишь оформить кое-какие исправления и подготовить несколько документов."
    show molly neutral
    "Их компании работают вместе? Так они познакомились?"
    show katie thinking
    katie.c "Когда-то у нас {i}был{/i} целый юридический отдел... Теперь всем занимается один человек — тот, кого ты сегодня встретила."
    katie.c "Неудивительно, что у нас такие проблемы..."
    show molly smile talk
    molly.c "Да, бедняга. Не виню его, что он не заметил эту лазейку: закон в этой области довольно запутанный."
    show molly smile
    show katie smile talk
    katie.c "Похоже, мы в надёжных руках."
    katie.c "И вы ещё пригласили всю компанию выпить сюда. С некоторыми из наших сотрудников это недёшево. У вас, должно быть, очень крупная фирма?"
    show katie smile
    show molly smile talk 2
    molly.c "В каком-то смысле, да. Мы всегда приглашаем новых клиентов. Это помогает наладить отношения во время сотрудничества."
    show molly smile
    "Похоже, они после работы пришли выпить вместе. Вон за соседним столиком сидят некоторые их коллеги."
    show katie smile talk
    katie.c "Ну, за тебя, Молли. Приятно познакомиться. И место отличное, это мой любимый бар."
    show katie smile
    show molly smile talk
    molly.c "Мой тоже. Я живу не в городе, но если остаюсь на ночь, часто сюда захожу."
    molly.c "Кстати, я знаю владельца. Возможно, ты его видела. Молодой человек?"
    show molly smile
    "Ой-ой."
    show katie tease talk
    katie.c "Да, ещё как {i}хорошо{/i}~ Хе-хе~"
    show katie tease
    show molly smile talk 2
    molly.c "Правда? Он твой друг?"
    show molly smile
    show katie tease talk
    katie.c "Хм-хм~ Мы вообще-то уже довольно давно встречаемся. Всё идёт очень хорошо~"
    show katie tease
    show molly neutral talk
    molly.c "Ты... правда?"
    show molly neutral
    call mcFretAboutPolyamory from _call_mcFretAboutPolyamory_2
    "Один из сотрудников замечает, что я топчусь неподалёку."
    unknown "Эй, босс!"
    "Обе девушки сразу понимают, о ком речь, и оборачиваются ко мне."
    show katie smile talk
    show molly neutral talk
    "Обе" "[mc.name]?"
    show katie smile
    show molly neutral
    "Что мне вообще сказать?"
    mc.c "А-а... Привет..."
    mc.c "Не ожидал увидеть вас здесь сегодня вечером..."
    show katie smile talk
    katie.c "Мы спонтанно решили зайти выпить с компанией, с которой работаем. С юристами из... э-э..."
    show katie smile
    show molly neutral talk
    molly.c "Хьюз и Хендерсон."
    show molly neutral
    show katie smile talk 2
    katie.c "Верно. А Молли сказала, что она твоя подруга?.."
    show katie smile
    mc.c "Да, э-э... Дело в том, что..."
    if(not mc.polyamoryExplained):
        "О боже, не верю, что я так поступил. Остаётся только сказать правду..."
        mc.c "Молли... Кэти..."
        mc.c "Прости, Кэти права. Я встречаюсь с ней."
        show katie neutral
        show molly neutral
        mc.c "Кэти... Я ещё недавно встречался с Молли. Мы несколько раз виделись и... продолжали..."
        mc.c "Мне так жаль... Я не говорил вам обеим, потому что... потому что..."
        mc.c "Я... не знаю. Я только переехал сюда и познакомился с вами обеими..."
        mc.c "Мне казалось, что мы обе нашли общий язык. А потом всё стало серьёзным..."
        mc.c "Я собирался рассказать вам, правда. Просто не мог..."
        mc.c "Не мог выбрать..."
        "..."
        "Девушки молча переглядываются."
        "Ошеломлённая тишина? Шок? Они точно не ожидали такого. Какой же я мерзавец..."
        show katie neutral talk
        katie.c "...Выбрать?"
        show katie neutral
        show molly thinking
        molly.c "Хм... Что он имеет в виду, Кэти?"
        show katie neutral talk
        katie.c "Милый, зачем тебе выбирать?"
        show katie neutral
        "...Что?"
        "Они... А?"
        mc.c "Ч-что ты имеешь в виду?.."
        show molly neutral talk
        molly.c "Не думаю, что это как-то влияло на наше время вместе. Если просто не поднимали эту тему, всё нормально. Можем обсудить сейчас, верно?"
        show molly neutral
        mc.c "Обсудить? Я..."
        show katie smile talk
        katie.c "О-о-о... Хм-хм~"
        show katie smile
        "Кэти хихикает. Что тут может быть смешного?"
        show molly smile talk
        molly.c "Что такое, Кэти? Какая-то его забавная черта?"
        show molly smile
        show katie smile talk 2
        katie.c "Кажется, люди не одобряют отношения с несколькими партнёрами. Наверное, [mc.name] думает, что и мы так считаем."
        show katie smile
        show molly surprise
        molly.c "Погоди, правда? То есть... обязательно {i}быть{/i} только с одним?"
        mc.c "А? Что вы..."
        show katie tease talk
        katie.c "Хе-хе~ [mc.name]... Антропоморфы не думают об отношениях так."
        katie.c "У моего отца тоже было несколько партнёров помимо мамы. У меня есть сводные братья и сёстры. Я тебе не рассказывала?"
        show katie tease
        mc.c "Нет..."
        show molly tease talk
        molly.c "Ой, [mc.name], надо было сказать! Я не знала, что ты такой..."
        molly.c "Мне это даже в голову не приходило. Ты не рассказывал о других, но и не обязан."
        show molly tease
        "Я ошеломлён. По-настоящему. В какой мир я попал? Неужели я не знал такого простого и важного факта?"
        call mcPolyamoryExplainedConclusion from _call_mcPolyamoryExplainedConclusion_2
    else:
        call playMusic(barTheme) from _call_playMusic_304
        mc.c "Прости, я подслушал ваш разговор. Мы знакомы, но..."
        mc.c "Я ещё и с Молли встречаюсь... Уже... некоторое время."
        show katie neutral talk
        katie.c "О?"
        show katie neutral
        mc.c "Кэти, Молли, простите, что не объяснил раньше. С момента переезда сюда я ходил на свидания, познакомился с несколькими девушками..."
        mc.c "Прежде чем я понял, мы все зашли далеко. Не знал, в какой момент нужно было... сказать..."
        "Они смотрят на меня спокойно. Кажется, всё может быть в порядке."
    mc.c "То есть... Чтобы прояснить... Вас обеих устраивает, что я встречаюсь с другой?"
    show katie smile talk 2
    if(katie.polyamoryExplained):
        katie.c "Милый, ты и так знаешь, что я об этом думаю..."
    katie.c "Конечно! Если это не мешает нашим отношениям. Пока не мешает, так почему бы и нет?"
    show katie smile
    show molly smile talk
    if(molly.polyamoryExplained):
        molly.c "Ты знаешь, что я об этом думаю."
    molly.c "Я тоже, [mc.name]. Не спрашивала, потому что это не моё дело, но раз уж мы об этом говорим, я не против. Кэти очень милая."
    molly.c "Меня это тоже вполне устраивает."
    show molly smile
    show katie smile talk
    katie.c "Я вообще впечатлена, [mc.name]. Она очень милая! Сегодня мы отлично поработали. Настоящий профессионал!"
    show katie tease talk
    katie.c "Она явно выше твоего уровня! Хе-хе~"
    show katie tease
    show molly bashful talk
    molly.c "Н-нет... Я не такая... Это [mc.name]..."
    show molly tease talk
    molly.c "*Кхм* Ну и повезло же тебе, [mc.name], такая красивая женщина~"
    molly.c "А ты видела её в деле? Она лучше всех разбиралась в комнате. В офисе её очень уважают."
    show molly tease
    show katie bashful talk
    katie.c "Ой, перестань..."
    show katie bashful
    mc.c "Значит, вы обе тоже можете встречаться с другими мужчинами?"
    show katie bashful talk
    katie.c "Милый, ты и так знаешь весь мой опыт с мужчинами... Вниманием я не обделена..."
    show katie bashful
    show molly bashful talk
    molly.c "Я рассказывала тебе о своём прошлом... Ты мой первый партнёр за долгое время, и я не собираюсь это менять."
    show molly bashful
    show katie smile talk 2
    katie.c "У тебя тоже был трудный период, Молли? Не верится..."
    show katie smile
    show molly smile talk
    molly.c "Был... Но всё уже позади. Если у тебя тоже, как-нибудь обменяемся историями."
    show molly smile
    show katie joy
    katie.c "О да! Люблю сплетни о романтике~"
    "Вот так дела. Две прекрасные женщины... обе мои и готовы делить меня."
    "Как же мне повезло? Чем я заслужил такое..."
    mc.c "У меня словно груз с плеч упал. Рад, что вы заранее встретились. Не знаю, как бы я справился."
    show molly smile talk 2
    molly.c "Хорошо получилось, правда? Мы уже сделали за тебя трудную часть, [mc.name]."
    show katie tease talk
    katie.c "Начинаю думать... У него фетиш на деловых женщин?"
    show katie tease
    "Есть такое?"
    show molly smile
    mc.c "*Кхм* Ладно... Расскажите лучше о вашем сотрудничестве."
    show katie smile talk
    katie.c "О, с чего бы начать? Ну, наш дурацкий начальник..."
    scene black with fade
    "Мы проводим часть вечера за разговорами, и девушки узнают друг друга получше."
    "Похоже, они отлично ладят. Замечательно."
    "Я приношу ещё напитки девушкам и их коллегам, и дела идут очень хорошо."
    "В общем, смена выдалась {i}очень{/i} интересной."

    if(not fromGallery):
        $ katie.polyamoryExplained = True
        $ molly.polyamoryExplained = True
        $ mc.polyamoryExplained = True
        $ katie.knowsDating = list(set(katie.knowsDating + [molly]))
        $ molly.knowsDating = list(set(molly.knowsDating + [katie]))

    return

label katieMollyDuoHEvent1(fromGallery):
    $ location_home.showBackground()
    call playMusic(chillTheme) from _call_playMusic_305
    "День был утомительным — разборки с поставщиками. Из-за путаницы во времени и количествах нам привезли слишком много коробок."
    "Полдня таскал их туда-сюда и пытался найти место для хранения. Бедный я, пришлось пальцем пошевелить."
    "Некоторые вещи пришлось даже отвезти домой, чтобы было где хранить. Сейчас моя квартира — мечта алкоголика."
    "Ну, по крайней мере, всё закончилось, я дома. Хм... проголодался."
    "В холодильнике ничего привлекательного. Разве что замороженная ерунда, которая не утолит голод..."
    "Эх, я сегодня слишком много работал. Заслужил награду. Мог бы заказать еду, но сегодня ужасно лениво..."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Я беру телефон и просматриваю варианты доставки, как вдруг... Что? Он завибрировал у меня в руке."
    "На экране уведомление. Кэти!"
    katie.c "Я только вернулась с работы. Если ты ещё не ел, хочу попробовать новый рецепт! Прийти к тебе сегодня вечером?"
    "Будто по волшебству, Кэти появляется как раз вовремя. Её домашняя еда лучше любого другого варианта в любой день недели."
    "Уже слюнки текут. Я собираюсь ответить громким «да». Но тут..."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "А? Ещё вибрация? Популярен я сегодня."
    "Новое уведомление появляется поверх моего ответа. Это Молли."
    molly.c "Ты сегодня свободен? Я обещала как-нибудь приготовить тебе что-нибудь. Может, сегодня? Пока не знаю, что именно, но могу зайти в магазин по дороге."
    "О-о... Она и правда говорила об этом. Иногда она готовит с мамой и хотела показать свои умения. Не удавалось только найти время."
    "Отличная возможность, жалко упускать. Неизвестно, когда она снова согласится. Но Кэти..."
    "Хм... Вот дилемма..."
    "Может, поступить эгоистично и не выбирать? Вроде бы они уже неплохо дружат..."
    "Не повредит спросить... Как сформулировать..."
    "Я пишу им обеим и объясняю, что каждая предложила приехать. Надеюсь..."
    $ renpy.play('audio/sfx/phoneVibrate.mp3', 'audio')
    "Хотя бы одна уже ответила."
    katie.c "Конечно! Я как раз собиралась встретиться с Молли!"
    "Отлично! А?.."
    molly.c "Конечно! Кэти рассказывала о своей готовке, мне стало интересно. Хочу посмотреть, как она это делает."
    "Невероятно. Уже представляю... Две красавицы готовят для меня на кухне..."
    "Такая роскошь кажется преступлением. Я этого не заслужил."
    "А теперь ждём..."
    call stopMusic from _call_stopMusic_58
    scene black with fade
    "Девушки сами договариваются сходить в магазин за продуктами. Интересно, что они купят?"
    "Примерно через полчаса я встречаю у себя двух девушек."
    $ location_home.showBackground()
    call playMusic(barTheme) from _call_playMusic_306
    show katie smile at twoPersonLeft
    show molly smile at twoPersonRight
    with dissolve
    mc.c "Добрый вечер, девочки."
    show katie smile talk
    katie.c "Привет, милый!"
    show katie kiss zorder 3 with dissolve
    katie.c "Муа~"
    show katie smile zorder 2 with dissolve
    "Она целует меня, а Молли не возражает. К этим отношениям всё ещё нужно привыкнуть."
    molly.c "Спасибо, что пригласил, [mc.name]."
    show molly kiss zorder 3 with dissolve
    molly.c "М-м~"
    show molly smile zorder 2 with dissolve
    "Молли наклоняется и целует меня, а Кэти улыбается. Я на седьмом небе."
    mc.c "Да брось, я рад вас обеих видеть. Спасибо, что обе согласились приехать — потому я это и предложил."
    show molly smile talk
    molly.c "Отличная идея. Мы хотели немного вместе приготовить, так что это идеально."
    show molly smile
    show katie tease talk
    katie.c "В магазине мы придумали, что приготовить. Думаю, сегодня тебя ждёт угощение~"
    show katie tease
    mc.c "С твоей готовкой всегда праздник. Уверен, вдвоём вы сделаете ещё вкуснее."
    show molly smile talk 2
    molly.c "Не обольщайся... Пока я никому за пределами семьи не готовила. Сегодня я буду помощницей шеф-повара."
    show molly smile
    mc.c "Тогда ты в надёжных руках."
    mc.c "Итак... Что будем есть?"
    show katie smile talk 2
    katie.c "Скоро узнаешь... Сначала подготовка."
    show katie smile
    "Девушки выкладывают продукты на столешницы. Похоже на пир."
    "Раз уж меня так балуют, надо быть хорошим хозяином. Пущу в дело часть запасов."
    mc.c "Девушки, хотите вина? Есть бутылки из бара получше."
    show katie tease talk
    show molly tease talk
    'Обе' "Нам побольше!"
    show katie tease
    show molly tease
    'Обе' "..."
    show katie joy
    show molly joy
    'Обе' "Хе-хе~"
    scene black with fade
    "Мы наливаем себе по бокалу, чокаемся, и девушки принимаются за дело."
    "Как говорит Кэти, готовить лучше всего с бокалом в руке."
    "Они отлично работают вместе, делят обязанности и используют кулинарные слова, которых я даже не понимаю."
    "Мог бы отдыхать в другой комнате, но на такое зрелище нельзя не посмотреть."
    image katiemolly cooking = Movie(play="images/characters/katiemolly/hevent1/cooking.webm")
    show katiemolly cooking with fade
    pause
    "Вот это зрелище. Две красавицы, увлечённые делом."
    molly.c "Сколько обычно нужно добавить?.."
    katie.c "Примерно половину от того, что у тебя сейчас, пока тушится, и ещё немного перед подачей."
    molly.c "Понятно..."
    "Обмениваясь советами, они превращают это в настоящее блюдо."
    "Мастер-класс для всех чувств. Запах еды, звук кипения, вкус вина и вид... этих двух попок..."
    "После пары бокалов я должен бы думать о блюде, но ещё и любуюсь этими двумя сексуальными девушками."
    "Если мы все здесь, может ли что-нибудь случиться?"
    katie.c "Ладно, [mc.name], садись, подаём!"
    mc.c "Сейчас, я умираю с голоду!"
    $ location_home.showBackground()
    "Девушки приносят тарелки, и аромат заполняет комнату."
    show katie smile at twoPersonLeft
    show molly smile at twoPersonRight
    with dissolve
    mc.c "Ничего себе, как вкусно пахнет. Что это?"
    show katie smile talk
    katie.c "Что-то вроде лососевого карри. Смесь нескольких рецептов: кокос, кешью, овощи, специи..."
    show katie smile talk 2
    katie.c "Мы придумали рецепт в магазине, и Молли предложила пару вещей, о которых я не подумала!"
    show katie smile
    show molly tease talk
    molly.c "Всего несколько вещей, которым меня научила мама. Основную работу сделала Кэти."
    show molly tease
    mc.c "В любом случае, выглядит и пахнет потрясающе."
    "Я набираю ложку. Рыба нежная, рис рассыпчатый, специи идеально сбалансированы."
    "Невероятно, сливочно, нежно, но вкус очень насыщенный."
    mc.c "Боже мой, восхитительно!"
    "Молли доедает кусочек."
    show molly surprise
    molly.c "Ого! Он прав! Я никогда такого не пробовала!"
    show katie tease talk
    katie.c "О-о~ И правда отлично получилось! Рыба восхитительная!"
    show katie tease
    show molly smile talk
    molly.c "Как ты это сделала, Кэти? Я же видела, но всё равно это нечто!"
    show molly smile
    show katie smile talk
    katie.c "Эй, это и твоё блюдо тоже! Одна я бы такого не придумала."
    show katie smile
    show molly smile talk 2
    molly.c "Надо будет записать рецепт для мамы~"
    scene black with fade
    if(not fromGallery):
        $ timeOfDay = 'Night'
    "Мы уплетаем невероятный ужин. Кэти готовила не раз, но это блюдо, пожалуй, лучшее."
    "Вечер продолжается. Мы пытаемся растянуть трапезу, но она слишком вкусная — все быстро съедают свои порции."
    "К счастью, есть добавка. На троих точно хватит."
    "За приятными разговорами и напитками солнце садится."
    $ location_home.showBackground()
    "Мы немного расслабились после нескольких бокалов, смеёмся и болтаем. Отличный вечер с двумя трудолюбивыми девушками."
    show katie smile at twoPersonLeft
    show molly smile at twoPersonRight
    with dissolve
    show molly smile talk
    molly.c "Мы обсуждали, как мы познакомились с тобой, [mc.name]. Признаюсь, я немного завидовала..."
    show molly smile
    show katie bashful talk
    katie.c "Тогда у меня был не лучший период..."
    show katie tease talk
    katie.c "Но... в итоге всё сложилось хорошо~"
    show katie tease
    show molly tease talk
    molly.c "Посмотри на вас, вы так мило познакомились!"
    show molly bashful talk
    molly.c "А мы просто... случайно столкнулись на дороге... Я со своим большим телом опять всем мешала..."
    show molly bashful
    show katie smile talk
    katie.c "Не говори глупостей, Молли, у тебя прекрасная фигура. Завидую... [mc.name], наверное, без ума от неё~"
    show katie smile talk 2
    katie.c "Хотела спросить... Ты придерживаешься особой диеты или занимаешься спортом?"
    show katie smile
    show molly thinking
    molly.c "Нет, ничего особенного... На работе я неожиданно много времени провожу на ногах, вот и всё..."
    show katie thinking
    katie.c "Ах, быть молодой~"
    show molly tease talk
    molly.c "Молодой? Да ты не старая, Кэти! У тебя отличная пышная фигура. Понимаю, почему [mc.name] выбрал тебя~"
    show molly smile talk
    molly.c "Прекрасная женщина в расцвете лет~"
    show molly smile
    show katie bashful talk
    katie.c "Ох... Скажи это моей талии..."
    show katie bashful
    show molly smile talk 2
    molly.c "Да брось, у тебя точно размер меньше моего! Посмотри на меня! Хотела бы быть такой хрупкой и изящной, как ты."
    show molly smile
    show katie smile talk
    katie.c "Всё дело в пропорциях, а у тебя они чертовски идеальны!"
    show katie smile
    mc.c "Девушки, хватит, вы обе прекрасны. Я что, недостаточно ясно выразился?"
    show katie tease talk
    katie.c "Ой, [mc.name], это просто девичьи разговоры~"
    katie.c "Не волнуйся, ты нам это {i}очень{/i} ясно дал понять~"
    show katie tease
    show molly tease
    'Both' "Хе-хе~"
    mc.c "Погодите, а чего вы смеётесь?.."
    show molly tease talk
    molly.c "О, просто делимся кое-какими... знаниями~"
    show molly tease
    show katie tease talk
    katie.c "Эй, Молли, он..."
    show katie tease
    "Они наклоняются друг к другу, шепчутся и лукаво улыбаются."
    show katie tease talk
    katie.c "{size=25}Он...............................тоже так делает...?{/size}"
    show katie tease
    show molly joy
    molly.c "О да, хе-хе~ {size=25}И когда он..................{/size}"
    show katie joy
    katie.c "О-о~ Хе-хе~"
    "Похоже, они обмениваются подробностями... о наших {i}интимных{/i} моментах?"
    "Кажется, мне не о чем беспокоиться... Может, это алкоголь, но я представляю, как мы проводили время вместе."
    show katie tease
    show molly tease
    "В конце концов мы садимся на диван. По девушке с каждой стороны от меня."
    "После нескольких бокалов мы немного расслаблены и уютно прижимаемся друг к другу."
    "Эти две женщины рядом... Я хочу их. Обеих."
    "Я кладу руку каждой на бедро и слегка сжимаю."
    "Они отвечают тем же, поглаживая мои колени."
    "Первой наклоняется Кэти..."
    call playMusic(sexyTheme) from _call_playMusic_307
    show katie kiss zorder 3 with dissolve
    katie.c "М-м-м~"
    "Мы задерживаем поцелуй, чуть шире раскрывая губы и лаская друг друга языками."
    "Молли слегка сжимает меня, наклоняясь. Мы с Кэти отстраняемся, и я тянусь к ней."
    show katie tease with dissolve
    show molly kiss zorder 3 with dissolve
    molly.c "М-м-м~"
    "Мы страстно целуемся, переплетаясь языками и обмениваясь слюной."
    "Рука Кэти поднимается выше по моему бедру, и я вздрагиваю. Не смогу себя сдержать."
    show molly tease talk with dissolve
    molly.c "Фух~ Вино сегодня крепкое, [mc.name]? Мне немного... жарко~"
    show molly tease
    show katie tease talk
    katie.c "Хе-хе~ Мне тоже... Но вечер от этого только веселее~"
    show katie tease
    "Обе девушки проводят руками по моим бёдрам и дразнят член сквозь штаны. Он уже твёрдый."
    "Похоже, всё идёт как я надеялся..."
    show katie tease talk
    katie.c "Молли, ты когда-нибудь... делилась мужчиной?"
    show katie tease
    show molly bashful talk
    molly.c "Н-нет... Ты предлагаешь?.."
    molly.c "Как... это может?.."
    show katie bashful talk
    katie.c "Не знаю... Но... думаю, у нас получилось бы?.."
    show katie bashful
    "Вот это девушки. Боже... Неужели это правда происходит?"
    show katie tease talk
    katie.c "[mc.name], может, ты знаешь, что делать~"
    show katie tease
    "В голове мелькают мысли. Это вполне ясное приглашение от них обеих."
    scene black with fade
    "Не успев обсудить идею, мы уже раздеваемся."
    "Мы исследуем тела друг друга, гладим, ласкаем, целуемся и падаем на кровать."
    scene katiemollyhevent1i1 with fade
    pause
    "Надо мной нависают две прекрасные женщины, весь мой мир — мягкие, нежные красавицы."
    "Но возникает вопрос..."
    molly.c "Как нам..."
    katie.c "Я думала, [mc.name] сам..."
    mc.c "Ну..."
    "Я теряюсь в выборе. Лежу с эрекцией, но не решаюсь. Что делать?"
    molly.c "Я... хочу, чтобы ты начала, Кэти. Я никогда такого не делала..."
    katie.c "Я тоже, Молли! Но... не возражаю."
    mc.c "Ладно, девочки, может..."
    scene black with fade
    "Я укладываю девушек на спину — передо мной невероятно эротичное зрелище."
    image katiemolly katie fuck 1 = Movie(play="images/characters/katiemolly/hevent1/katiefuck1.webm")
    show katiemolly katie fuck 1 with fade
    pause
    "Я поднимаю ногу Кэти, прижимая бёдра девушек друг к другу, и вхожу в её тёплую, манящую киску."
    katie.c "О-о~ М-м~"
    molly.c "Ничего себе~ Кэти, посмотри на своё лицо~ Хорошо, да?"
    katie.c "А-а-а~ Да-а~"
    "Я обхватываю её мясистое бедро и нежно вхожу и выхожу."
    katie.c "М-м~ [mc.name]~"
    "Поначалу Молли лишь наблюдает, но у меня для неё тоже есть занятие."
    image katiemolly katie fuck 2 = Movie(play="images/characters/katiemolly/hevent1/katiefuck2.webm")
    show katiemolly katie fuck 2 with fade
    pause
    "Я тянусь к киске Молли, глубоко ввожу пальцы и ласкаю её клитор."
    molly.c "О-ох~ [mc.name]~ М-м~"
    "Её тёплая влажная киска принимает мою руку, и она тихо стонет, пока я ласкаю обеих."
    molly.c "М-м~ Как ты... М-м~ Так хорошо~"
    katie.c "А-а~ [mc.name]~"
    molly.c "Он такой *а-а* большой, не представляю, как тебе..."
    katie.c "Он так хорошо меня заполняет *а-а*~"
    "Ощущения невероятные. Стоны двух моих девушек — будто я попал в другой мир."
    "Честно говоря, и моё удовольствие нарастает. Я мог бы кончить прямо сейчас."
    katie.c "Молли... Пока он не кончил... *а-а* Твоя очередь~"
    molly.c "М-м~"
    image katiemolly molly fuck 1 = Movie(play="images/characters/katiemolly/hevent1/mollyfuck1.webm")
    show katiemolly molly fuck 1 with fade
    pause
    "Немного передохнув, я аккуратно ставлю девушек на четвереньки."
    "Молли сразу принимает мой член своей огромной упругой задницей. Я не сдерживаюсь и сразу же вбиваюсь в неё изо всех сил."
    molly.c "А-а-а~! М-м~ М-м-м~ О-о~ [mc.name]~"
    katie.c "О-о~ Как бурно~"
    "Я не забываю Кэти: тянусь к её пухлой заднице, ласкаю киску и ввожу два пальца, быстро двигая ими."
    katie.c "О-ох~ А-а-а~ А-а-а~"
    molly.c "[mc.name]~ *А-а* М-м~"
    image katiemolly molly fuck 2 = Movie(play="images/characters/katiemolly/hevent1/mollyfuck2.webm")
    show katiemolly molly fuck 2 with fade
    pause
    "В беспорядке из влаги, удовольствия, жара и стонов мы теряемся в развратной оргии."
    "Я шлёпаю Молли по заднице, она подпрыгивает на моём члене и вздрагивает с каждым толчком."
    "Левая рука залита горячей влагой из истерзанной киски Кэти. Жар нарастает, и я чувствую, как она содрогается у меня в руке."
    molly.c "[mc.name]~ [mc.name]~ Я сейчас..."
    katie.c "Я кончаю, [mc.name]~ Кончаю-у-у~"
    "Я уже на грани."
    molly.c "М-м-м~!"
    katie.c "А-а-а-а~!"
    scene katiemollythreesomeend with fadewhite
    pause
    "Не желая обделить ни одну, я выскальзываю и кончаю."
    "Я извергаю несколько мощных струй, покрывая их сжатые вместе ягодицы."
    "Эти скромные, зрелые, деловые женщины превратились в развратный клубок удовольствия..."
    katie.c "О-о~ Милый~"
    molly.c "А-а~ А-а~ О-ох~"
    "Комнату наполняет тяжёлое дыхание. Девушки опускаются на четвереньки, приходя в себя после бурного оргазма."
    molly.c "Н-ничего себе~ Это..."
    katie.c "Было потрясающе~"
    call playMusic(heartTheme) from _call_playMusic_308
    scene katiemollypillowtalk with fade
    pause
    "Мы лежим вместе и наслаждаемся послевкусием, всё ещё кружится голова от экстаза."
    "Переведя дыхание, девушки приподнимаются на кровати."
    katie.c "Я не была уверена, но... Это было здорово."
    molly.c "Никогда не думала, что смогу... такое сделать."
    mc.c "Привыкайте. Теперь я знаю: лучше каждой из вас по отдельности только вы обе вместе."
    molly.c "Это было здорово, но... наверное, не каждый раз."
    "На улице совсем темно. Мы провели вместе весь вечер. Завтра обеим на работу, так что лучше им остаться у меня. Но ради шутки..."
    mc.c "Ладно, девочки, спасибо за ужин и секс. А теперь вон отсюда."
    katie.c "А-а? Да ты бы не посмел, злодей~"
    molly.c "Даже если бы захотела, я бы не смогла уйти..."
    mc.c "Конечно, вы останетесь на ночь. И никак иначе. Вы обе не против?"
    katie.c "У [mc.name] здесь есть несколько моих вещей, так что всё хорошо."
    molly.c "У меня тоже, и кое-что в машине."
    katie.c "А? Если подумать, я никогда не видела тебя не в костюме. Хотелось бы посмотреть, что ты носишь."
    molly.c "Я бываю здесь только по работе, так что... У меня тоже только рабочая одежда."
    katie.c "Жаль. Надо как-нибудь сходить вместе по магазинам."
    molly.c "О-о~ Я бы хотела."
    scene black with fade
    "Мы медленно засыпаем втроём в одной постели."
    "Тёплой и уютной ночью."
    pause
    "..."
    pause
    scene katiemollymorning with fade
    pause
    "Раннее утро, но, как и ожидалось, девушки просыпаются раньше меня."
    mc.c "Доброе утро, девочки."
    katie.c "М-м~ Доброе утро."
    molly.c "Вчерашний вечер... Это было... нечто."
    molly.c "Я бы хотела ещё побыть, но... ты знаешь."
    katie.c "Я тоже, к сожалению. Но вчера было здорово."
    mc.c "Уходите так рано утром? Тогда я ещё посплю."
    katie.c "Повезло тебе, да, Молли? Не понимаю, почему мы его терпим."
    molly.c "Немного завидую..."
    scene black with fade
    "Они по очереди принимают душ, собираются и вместе идут на работу."
    "Я откидываюсь и думаю о прошедшей ночи. Какая же у меня невероятная жизнь."

    return {'time':'Morning'}

label katieMollyDuoHEvent2(fromGallery):
    $ location_town.showBackground()
    call playMusic(barTheme) from _call_playMusic_309
    "Захожу в бар."
    "Не планировал, но сегодня у меня особое приглашение, от которого не отказаться."
    "Кэти и Молли договорились выпить вместе, хотя их рабочее сотрудничество, кажется, подходит к концу."
    "Похоже, они отлично ладят. Я только сейчас узнал, что Молли останется в городе."
    "Я не обижаюсь... Наоборот, это очень приятно. И мне нравится, что они выбрали мой дом местом встреч."
    "Раньше я не смог к ним присоединиться, так что не знаю, сколько они тут уже сидят."
    "Пойду посмотрю, как они."
    $ location_bar.showBackground()
    "Я захожу и оглядываюсь."
    show katie joy at twoPersonLeft
    show molly joy at twoPersonRight
    with dissolve
    'Обе' "Хе-хе~!"
    "Они смеются за столиком в углу."
    "На столе несколько пустых бокалов. Кажется, им было весело."
    molly.c "Кэти, ты такая смешная~!"
    katie.c "Хе-хе-хе~"
    "Когда я подхожу, они вытирают слёзы и допивают свои бокалы."
    mc.c "Привет, девочки!"
    show katie tease talk
    katie.c "[mc.name]~!"
    show katie tease
    show molly tease talk
    molly.c "О! Добрый вечер, [mc.name]!"
    show molly tease
    mc.c "Вечер? Уже довольно поздно."
    show molly surprise
    molly.c "О боже! Уже так поздно? Мы так долго здесь сидим, Кэти?"
    show katie smile talk
    katie.c "Хе-хе~ Пару часов, не больше, да~?"
    show katie smile
    "Они такие оживлённые и весёлые. Давно вышли из рабочего режима."
    "Похоже, они выпили..."
    mc.c "Наверное, да. Жаль, не смог присоединиться раньше... Кажется, я многое пропустил."
    show molly tease talk
    molly.c "Ха-ха~ Ещё как, мне очень весело!"
    show molly tease
    "Я сажусь между ними, замечая пустые бокалы вокруг."
    mc.c "Вижу, вы вовсю пользуетесь заведением..."
    show molly smile talk 2
    molly.c "Хе-хе~ Ещё бы!"
    molly.c "Обычно я не пью много, но это вино очень вкусное... Как оно называется, Кэти?"
    show molly smile
    show katie smile talk
    katie.c "Пино-гриджио. Сейчас у вас здесь очень хорошее, [mc.name]!"
    show katie smile
    mc.c "Рад слышать."
    show katie tease talk
    katie.c "Кстати говоря~"
    katie.c "Не принесёшь нам ещё, официант?"
    show katie tease
    mc.c "Конечно... Тебе тоже, Молли?"
    show molly tease talk
    molly.c "О-о~ Давай, почему бы и нет?"
    show molly tease
    mc.c "Сейчас."
    show katie tease talk
    katie.c "За работу с тобой!"
    show katie tease
    "Она говорит это и слегка шлёпает меня по заднице..."
    show molly joy
    molly.c "Ха-ха!"
    hide katie
    hide molly
    with dissolve
    "Девушки хихикают, пока я убираю со стола и несу новую порцию."
    "Наблюдать, как они разговаривают через стойку... Очень трогательное зрелище."
    "Один из сотрудников подшучивает над моей компанией. Похоже, у меня среди них репутация из-за моих женщин..."
    "Сегодня я лишь наполовину на смене... С напитками в руках возвращаюсь к ним."
    show katie smile at twoPersonLeft
    show molly smile at twoPersonRight
    with dissolve
    mc.c "Дамы."
    show katie tease talk
    katie.c "Спасибо, милый!"
    show katie tease
    show molly tease talk
    molly.c "Прекрасно, спасибо, [mc.name]!"
    show molly tease
    "Мы поднимаем бокалы и чокаемся."
    show katie joy
    show molly joy
    'Все' "За нас!"
    show katie smile
    show molly smile
    "Они делают по большому глотку. Для Кэти это обычно, но я редко вижу, чтобы Молли пьянела."
    mc.c "Так чем вы занимались вместе? В последнее время несколько раз встречались, да?"
    show katie smile talk 2
    katie.c "Да! Наши компании всё ещё иногда встречаются, и мы обедаем вместе."
    show katie smile
    show molly smile talk
    molly.c "Даже когда встречи нет, офисы рядом, так что можем пересечься."
    show molly smile talk 2
    molly.c "Кэти показывает мне местные кафе. Некоторые я совсем не замечала!"
    show molly smile
    mc.c "Здорово. Ты на этой неделе вообще выходила из офиса?"
    show molly smile talk
    molly.c "Находила время. В последнее время не так много дел."
    show molly joy
    molly.c "Иногда даже получается уйти пораньше и встретиться с Кэти после работы! Выпить или поужинать."
    mc.c "Здорово. Меня, как вижу, не звали..."
    show molly smile
    show katie tease talk
    katie.c "Ой, ну хватит, [mc.name]... Иногда девочкам надо побыть одним!"
    katie.c "Уверена, ты не захотел бы с нами ходить... Ну, по магазинам и сплетничать."
    show katie tease
    mc.c "Я люблю ходить по магазинам! За... э-э... едой и всяким таким..."
    show molly tease talk
    molly.c "Хе-хе~ Не за этим... Иногда приятно сходить за одеждой с женщиной! Я так давно не ходила."
    show molly tease
    show katie smile talk
    katie.c "У нас похожие вкусы. Недавно мы вместе кое-что купили."
    show katie smile
    mc.c "Вы же знаете, меня {i}очень{/i} волнует, что вы носите..."
    show katie thinking
    katie.c "А-а~ Это точно..."
    show molly tease talk
    molly.c "Хе-хе~ И тебе тоже?"
    show molly tease
    show katie tease talk
    katie.c "Ты всё время пытаешься нарядить меня во что-нибудь необычное... У тебя фетиши, [mc.name]~"
    show katie tease
    mc.c "Разве преступление считать двух своих девушек красавицами?"
    show katie bashful
    show molly tease
    katie.c "О-о~ Ну хватит~"
    molly.c "Хм-хм~"
    scene black with fade
    "Вечер продолжается, мы потягиваем напитки."
    "Обсуждаем прошедшую неделю, чем они занимались вместе и что я делал с девушками..."
    "Наша троица отлично ладит... Надо ущипнуть себя, чтобы поверить, что мне так повезло."
    "Когда мы заканчиваем, идём домой через необычно тёплый вечер. Уже поздно, и, похоже, Молли снова останется у меня."
    "Чтобы не отставать, Кэти тоже идёт. Немного вместе «расслабиться»..."
    if(not fromGallery):
        $ timeOfDay = 'Night'
    $ location_home.showBackground()
    "Войдя в дом, девушки скидывают туфли и бросают сумки."
    show katie tease at twoPersonLeft
    show molly tease at twoPersonRight
    with dissolve
    show molly tease talk
    molly.c "А-а~ Ой, я немного кружусь! Наверное, выпила больше, чем обычно!"
    show molly tease
    show katie tease talk
    katie.c "Фух~ Я тоже! Молли, это ты виновата! Ты меня споила!"
    show katie tease
    show molly joy
    molly.c "Ха-ха~ Я? Это ты на меня плохо влияешь~"
    show katie joy
    katie.c "Хе-хе~!"
    "Вернувшись с бодрой прогулки и устроившись дома, мы сразу чувствуем, как здесь тепло."
    show molly bashful talk
    molly.c "Фух~ Это я одна, или здесь довольно жарко?"
    show molly bashful
    show katie smile talk 2
    katie.c "Нет, я тоже чувствую... От пары бокалов меня бросает в жар~"
    show katie smile
    mc.c "Прости, так иногда бывает. Кажется, сегодня я не открыл окно."
    show molly smile talk
    molly.c "[mc.name]... Не возражаешь, если я сниму этот душный костюм? День был долгий~"
    show molly smile
    mc.c "Конечно, часть твоих вещей в том ящике."
    show katie tease talk
    katie.c "Тогда и я переоденусь. Во что-нибудь поудобнее~"
    show katie tease
    mc.c "Конечно, твои вещи в соседнем ящике."
    scene black with fade
    "Девушки без колебаний начинают раздеваться прямо на месте. Кажется, мы настолько привыкли друг к другу."
    "Но, к моему удивлению, сняв верхние слои одежды, они не стали надевать что-то взамен..."
    scene katiemollyhevent2i1 with fade
    pause
    molly.c "Фух~"
    katie.c "А-а~"
    "Девушки лениво плюхаются на диван, почти полностью раздетые. Только бельё..."
    molly.c "М-м~ К чёрту верх, мне и так хорошо..."
    katie.c "После долгого дня пора снять и это..."
    katie.c "Ты не против, милый?"
    mc.c "Вы правда думаете, что я буду против?"
    molly.c "Хе-хе~ Ну да~"
    "Их можно понять, здесь правда душно."
    scene katiemollyhevent2i2 with fade
    pause
    "Я присоединяюсь к ним на диване, устраиваясь между двумя любимыми женщинами."
    "Мы включаем телевизор, чтобы расслабиться, и откидываемся."
    katie.c "Может, ты и не поймёшь, [mc.name]... Но вся одежда поверх моей шёрстки... Вам, людям, повезло."
    molly.c "Забавно, да? Мне приходится ходить на работу в {i}полном{/i} костюме..."
    mc.c "Повезло мне, да? Зимой у нас наоборот."
    katie.c "Нам лучше всего {i}в естественном виде~{/i}"
    "Мы отдыхаем и обсуждаем всякую ерунду по телевизору."
    "Я обнимаю девушек и прижимаю к себе."
    "Несмотря на жару, они придвигаются поближе, и их обнажённая шерсть трётся обо мне."
    "Я окружён... Тёплой... мягкой... пушистой... плотью."
    "Их обнажённая грудь прижимается ко мне. Если бы я не знал лучше, решил бы, что они меня дразнят."
    katie.c "Молли~"
    molly.c "Да-а~?"
    katie.c "Помнишь, как он... сделал это... с нами обеими~"
    molly.c "Хе-хе~ А что именно? Не помню~"
    call playMusic(sexyTheme) from _call_playMusic_310
    katie.c "Хм... Когда ты... своей грудью~"
    molly.c "Кэти! Хе-хе~"
    "Что?"
    katie.c "Я подумала... Может, мы... сделаем ему приятное~"
    molly.c "О да~? Что ты задумала? Хм-хм~"
    "Они говорят надо мной, будто меня здесь нет. Вот же..."
    "Кэти проводит рукой ближе к моей промежности."
    katie.c "Может... если мы обе~"
    katie.c "Как думаешь, [mc.name]~?"
    "Кажется, я догадываюсь, о чём они..."
    "Молли тоже присоединяется. У меня уже текут слюнки от одной мысли."
    mc.c "Я... не откажусь..."
    "Кэти и Молли переглядываются и хихикают."
    scene black with fade
    "Они встают и берут меня за руки."
    katie.c "Идём~"
    molly.c "Хе-хе~"
    "Девушки ведут меня к кровати."
    image katiemolly handjob = Movie(play="images/characters/katiemolly/hevent2/handjob.webm")
    show katiemolly handjob with fade
    pause
    "Они раздевают меня, укладывают, затем встают на колени у моих ног."
    "Я уже твёрдый, но они всё равно немного разогревают меня."
    molly.c "Хе-хе~ Он уже готов~"
    katie.c "Он такой простой, да?"
    "Молли нежно сжимает мой член и гладит вверх-вниз."
    "Кэти мягко массирует головку, и по спине пробегают мурашки."
    mc.c "Господи, Кэти..."
    katie.c "Хм-хм~ Приятно, милый?"
    "Их нежные прикосновения и шелковистая шерсть скользят по мне."
    "Для смазки начинает выделяться предэякулят. Похоже, он пригодится..."
    katie.c "Посмотри на его лицо~ Ему не терпится."
    mc.c "Ещё бы..."
    molly.c "Так... Как это будет?"
    katie.c "Хм... Ну... Может, ноги сюда..."
    katie.c "А... вот так?"
    image katiemolly boobjob 1 = Movie(play="images/characters/katiemolly/hevent2/boobjob1.webm")
    show katiemolly boobjob 1 with fade
    pause
    "Они сводят мои ноги и встают по обе стороны, нависая над бёдрами."
    "Поднимают груди и прижимают друг к другу, заключая мой член в мягкий рай."
    molly.c "Так?.."
    katie.c "Хе-хе~ Думаю, да, милый?"
    mc.c "Да, боже, да."
    "Они скользят вверх-вниз, нежно лаская мой ствол шелковистой шерстью и щекоча нижнюю сторону головки."
    "Их соски слегка трутся друг о друга. Чёрт, это невероятно."
    molly.c "О-ох~"
    katie.c "М-м~ Какой ты твёрдый~"
    mc.c "Девушки... А-а~"
    "Ощущения и зрелище слишком сильные."
    image katiemolly boobjob 2 = Movie(play="images/characters/katiemolly/hevent2/boobjob2.webm")
    show katiemolly boobjob 2 with fade
    pause
    "Девушки начинают двигать большими красивыми грудями вверх-вниз, даря невероятное удовольствие."
    mc.c "О-о... чёрт..."
    katie.c "Хе-хе~ Посмотри на его лицо, Молли."
    molly.c "Хм-хм~ Он такой любитель груди, правда~"
    mc.c "Ещё бы. А здесь две лучшие пары в мире..."
    "Девушки смотрят мне в глаза и улыбаются, сжимая член между горячими упругими грудями."
    "Мягкий пушистый рай обрушивается на меня, ощущения нарастают."
    molly.c "Фух~ Это довольно утомительно, да?"
    katie.c "Немного... Но, думаю, он скоро кончит, да?"
    mc.c "Ага..."
    katie.c "Тогда давай его добьём~"
    image katiemolly boobjob 3 = Movie(play="images/characters/katiemolly/hevent2/boobjob3.webm")
    show katiemolly boobjob 3 with fade
    pause
    "Они сжимают груди вместе и прижимаются ко мне, быстро двигаясь вверх-вниз."
    "Шёлковая шерсть скользит по члену, и я теряю голову."
    mc.c "Ох, чёрт..."
    "Их пышные груди шлёпаются друг о друга и подпрыгивают, пока сжимают мой член."
    katie.c "А-а~ А-а~ Хе-хе~ Продолжай~"
    molly.c "Хе-хе~ Так... А-а~ Хорошо, [mc.name]~?"
    "Жар их тел и трение... Я уже на грани."
    molly.c "А-а~ А-а~ [mc.name]~"
    katie.c "А-а~ Милый~ А-а~ Ты?.."
    mc.c "Я сейчас...!"
    scene katiemollyboobjobfinish1 with fadewhite
    pause
    molly.c "О-о~!"
    katie.c "А-а~!"
    "После последнего сжатия мой член извергает сперму между их грудей, прямо им на лица."
    scene katiemollyboobjobfinish2 with dissolve
    pause
    "Сперма разлетается и стекает, заливая их груди и лица."
    molly.c "О-о боже~"
    katie.c "Хе-хе~ Так много~"
    "Они кладут груди мне на колени и тяжело дышат, продолжая прижимать мой пульсирующий член."
    mc.c "Охренеть... А-а..."
    katie.c "Хорошо было, милый~?"
    mc.c "Невероятно..."
    "Сперма стекает по лицу Молли."
    molly.c "Кажется, это новый рекорд... Не ожидала~"
    "Сперма стекает по их телам, и девушки хихикают над тем, что со мной сделали."
    molly.c "Давайте уберёмся..."
    katie.c "Ага~"
    scene black with fade
    "Не планировал сегодня увидеть Кэти и Молли вместе, но как же здорово всё вышло."
    "Девушки остаются у меня на ночь, расслабленные и слегка навеселе."

    return{'location':location_town, 'time':'Morning'}
