label startTutorial:
    call hideAllScreens from _call_hideAllScreens_9
    hide screen mainUi
    call gameTutorial from _call_gameTutorial_1
    call goToLocation(mc.currentLocation) from _call_goToLocation_11


label gameTutorial:
    image gametutorialmap1 = Image('images/tutorial/main/map1.webp')
    scene gametutorialmap1 with fade
    ofkeres "Вот короткое обучение тому, чем тебе предстоит заниматься в Tails on the Rocks."
    ofkeres "Это карта мира. Осмотрись — вдруг встретишь новых друзей!"
    image gametutorialmap2 = Image('images/tutorial/main/map2.webp')
    scene gametutorialmap2 with dissolve
    ofkeres "В баре можно отработать смену или заняться управлением. Так ты будешь зарабатывать деньги."
    ofkeres "Давай быстро посмотрим, как устроен бар."
    image barTutorial1 = Image('images/tutorial/bar/profit.webp')
    scene barTutorial1 with dissolve
    pause
    image barTutorial2 = Image('images/tutorial/bar/level.webp')
    scene barTutorial2 with dissolve
    pause
    image barTutorial3 = Image('images/tutorial/bar/stock.webp')
    scene barTutorial3 with dissolve
    pause
    image barTutorial4 = Image('images/tutorial/bar/capacity.webp')
    scene barTutorial4 with dissolve
    pause
    image barTutorial5 = Image('images/tutorial/bar/general.webp')
    scene barTutorial5 with dissolve
    pause
    ofkeres "К этому обучению можно вернуться в любой момент — просто зайди в бар."
    image gametutorialmap1 = Image('images/tutorial/main/map1.webp')
    scene gametutorialmap1 with fade
    image gametutorialphone1 = Image('images/tutorial/main/phone1.webp')
    scene gametutorialphone1 with dissolve
    pause
    image gametutorialphone2 = Image('images/tutorial/main/phone2.webp')
    scene gametutorialphone2 with dissolve
    pause
    image gametutorialphone3 = Image('images/tutorial/main/phone3.webp')
    scene gametutorialphone3 with dissolve
    pause
    image gametutorialphone4 = Image('images/tutorial/main/phone4.webp')
    scene gametutorialphone4 with dissolve
    pause
    image gametutorialphone5 = Image('images/tutorial/main/phone5.webp')
    scene gametutorialphone5 with dissolve
    pause
    image gametutorialphone6 = Image('images/tutorial/main/phone6.webp')
    scene gametutorialphone6 with dissolve
    pause
    ofkeres "Давай посмотрим, как взаимодействовать с персонажами."
    image gametutorialinteract1 = Image('images/tutorial/main/interact1.webp')
    scene gametutorialinteract1 with dissolve
    pause
    ofkeres "Щёлкни по девушке в локации, чтобы начать взаимодействие."
    ofkeres "Разные действия по-разному повышают симпатию и любовь. В некоторых местах доступны особые действия."
    ofkeres "У действий есть ограничения: например, {b}подарок{/b} можно вручить только раз в день, а {b}поболтать{/b} — лишь раз за каждый период суток."
    ofkeres "Проведённое вместе время переведёт часы на следующий период."
    ofkeres "По мере прохождения событий персонажа тебе будут открываться новые действия."
    image gametutorialdate1 = Image('images/tutorial/main/date1.webp')
    scene gametutorialdate1 with dissolve
    pause
    ofkeres "Ну вот, вы встретились на свидании! Отлично!"
    ofkeres "На свидании набирай как можно больше очков (шкала сверху) — максимум 100."
    ofkeres "Во время свидания у тебя будет 5 действий. Когда они закончатся, свидание завершится."
    ofkeres "Каждое действие даёт разное количество очков. Некоторые можно выполнить только один раз."
    ofkeres "По мере прохождения её событий станут доступны новые действия."
    ofkeres "Если свидание пройдёт удачно, девушка будет симпатизировать тебе сильнее! А если всё пойдёт плохо — может и обидеться..."
    ofkeres "Удачное свидание {b}вечером{/b} или {b}ночью{/b} может закончиться тем, что девушка поедет к тебе домой. Всё зависит от того, насколько далеко ты продвинулся в её истории."
    image gametutorialmap1 = Image('images/tutorial/main/map1.webp')
    scene gametutorialmap1 with fade
    ofkeres "Вот и всё! Вернуться к обучению можно в любой момент — нажми на значок в правом верхнем углу панели навигации."
    ofkeres "Исследуй мир и получай удовольствие!"
    return

screen gameTutorial1:
    modal True
    zorder 100
    style_prefix 'bartutorial'
    frame:
        add 'images/tutorial/bar/profit.webp'
        textbutton 'Далее >':
            xalign 1.0
            action [Hide('barTutorial1'), Show('barTutorial2')]
        textbutton '< Закрыть':
            xalign 0.0
            action [Hide('barTutorial1')]
