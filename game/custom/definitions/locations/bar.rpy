define bar_rent = 100

default bar_capacity = 10
define bar_capacityUpgradeCost = 200
define bar_capacityMax = 95

default bar_drinkLevel = 1
default bar_drinkMaxLevel = 5
define bar_drinkLevelUpgradeCost = 300
define bar_drinkIncomeBase = 250
define bar_drinkIncomePerLevel = 10
default bar_drinkStock = 500
define bar_drinkStockCostPerLevel = 1.2

default bar_foodLevel = 0
default bar_foodMaxLevel = 5
define bar_foodLevelUpgradeCost = 300
define bar_foodIncomeBase = 200
define bar_foodIncomePerLevel = 10
default bar_foodStock = 0
define bar_foodStockCostPerLevel = 1.5

default bar_numberOfStaff = 1
define bar_numberOfStaffMax = 9
define bar_costPerEmployee = 70

default bar_autoRestockDrink = False
default bar_autoRestockFood = False
define bar_autoRestockCost = 100

# Functions
label workInBar:
    call hideAllScreens from _call_hideAllScreens_3
    hide screen mainUi
    call hideInSceneCharacters(True) from _call_hideInSceneCharacters_2
    $ workShiftPay = mc.wage
    "Я отрабатываю смену за стойкой."
    "За смену набралось чаевых на $[workShiftPay]."
    $ mc.money += workShiftPay
    python:
        for character in [character for character in location_bar.occupants if character.knownToMC]:
            character.addLike(1)
            renpy.scene()
            renpy.show(character.apiName + 'bar')
            renpy.with_statement(Dissolve(0.5))
            renpy.say('', 'За смену мне удалось поговорить с [character.name].')
    window hide
    call endScene() from _call_endScene_23

label barEndDay:
    python:
        bar_drinkProfitLoss = bar_drinkIncomeBase + (bar_drinkIncomePerLevel * (bar_drinkLevel-1)) if bar_drinkStock > 0 else 0
        bar_foodProfitLoss = bar_foodIncomeBase + (bar_foodIncomePerLevel * (bar_foodLevel-1)) if bar_foodLevel > 0 and bar_foodStock > 0 else 0
        bar_capacityProfitMultiplier = round(0.6 + round(bar_capacity / 25, 2), 2)
        bar_profit = round((bar_drinkProfitLoss + bar_foodProfitLoss) * bar_capacityProfitMultiplier, 2)

        bar_staffCosts = bar_numberOfStaff * bar_costPerEmployee
        bar_loss = bar_staffCosts + bar_rent

        bar_totalProfitLoss = int(bar_profit - bar_loss)
        mc.money += bar_totalProfitLoss

        stockDeduction = bar_capacity * 5
        if(bar_drinkStock >= stockDeduction):
            bar_drinkStock -= bar_capacity * 5
        else:
            bar_drinkStock = 0
        if(bar_drinkStock <= 0):
            if(bar_autoRestockDrink):
                mc.money -= round(bar_drinkStockCostPerLevel * 500)
                mc.money -= round(bar_autoRestockCost)
                bar_drinkStock += 500
            else:
                renpy.notify('В баре закончились напитки!')

        if(bar_foodLevel > 0):
            if(bar_foodStock >= stockDeduction):
                bar_foodStock -= bar_capacity * 5
            else:
                bar_foodStock = 0
            if(bar_foodStock <= 0):
                if(bar_autoRestockDrink):
                    mc.money -= round(bar_foodStockCostPerLevel * 500)
                    mc.money -= round(bar_autoRestockCost)
                    bar_foodStock += 500
                else:
                    renpy.notify('В баре закончилась еда!')
    return

# Screens

screen bar:
    zorder 2
    style_prefix 'characterInteractionMenuStyle'
    frame:
        at characterInteractionMenuReveal
        vbox:
            button:
                hbox:
                    add 'moneyicon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Work (Earn Tips)')
                action Jump('workInBar')
            button:
                hbox:
                    add 'baricon' fit "contain" xsize 35 anchor (0.0, 0.5) ypos 0.5 xoffset 10
                    text _('Manage')
                action Show('barOverview')

screen barOverview:
    dismiss action Hide('barOverview')
    zorder 4
    frame:
        modal True
        xalign 0.5 yalign 0.5
        xsize 0.94 ysize 0.84
        background None
        at shopRevealTransition
        vbox:
            frame:
                background Frame('gui/genericUIBoxRoundedTop.webp', 40, 40, 40, 40)
                xsize 1.0 ysize 0.1
                textbutton '{size=30}X':
                    style 'genericCircleButtonStyle'
                    text_align (0.5, 0.5)
                    action Hide('barOverview')
                textbutton _('Tutorial'):
                    xalign 0.8
                    text_size 25
                    style 'genericButtonStyle_button'
                    action Show('barTutorial1')
                text '$' + str(mc.money) xalign 1.0
            frame:
                background Frame('gui/genericUIBoxRoundedBottom.webp', 40, 40, 40, 40)
                xsize 1.0 ysize 1.0
                style_prefix "barOverviewGrid"
                grid 8 9:
                    xspacing 2
                    yspacing 6
                    text _('{b}Item{/b}')
                    text _('{b}Level{/b}')
                    text "{b}+/-{/b}"
                    text _('{b}Stock{/b}')
                    text _('{b}Restock{/b}')
                    text _('{b}Auto{/b}')
                    text _('{b}Downgrade{/b}')
                    text _('{b}Upgrade{/b}')

                    text _('Rent')
                    text "-"
                    text "-[str(bar_rent)]"
                    text "-"
                    text "-"
                    text "-"
                    text "-"
                    text "-"

                    text _('Employees')
                    text str(bar_numberOfStaff)
                    $ bar_staffCosts = bar_numberOfStaff * bar_costPerEmployee
                    text "-[str(bar_staffCosts)]"
                    text "-"
                    text "-"
                    text "-"
                    textbutton _('Downgrade'):
                        hovered [CaptureFocus('employeeDowngradeHover'), Show('employeeDowngradeTooltip')]
                        unhovered Hide('employeeDowngradeTooltip')
                        action [Call('fireEmployee')]
                    textbutton _('Upgrade'):
                        hovered [CaptureFocus('employeeUpgradeHover'), Show('employeeUpgradeTooltip')]
                        unhovered Hide('employeeUpgradeTooltip')
                        if(bar_numberOfStaff < bar_numberOfStaffMax):
                            action [Hide('employeeUpgradeTooltip'), Call('hireEmployee')]

                    text _('Drinks')
                    text str(bar_drinkLevel)
                    $ bar_drinkProfitLoss = bar_drinkIncomeBase + (bar_drinkIncomePerLevel * (bar_drinkLevel-1)) if bar_drinkStock > 0 else 0
                    text str(bar_drinkProfitLoss)
                    text str(bar_drinkStock)
                    hbox:
                        textbutton "+100":
                            hovered [CaptureFocus('restockHover'), Show('restockTooltip', stockType = "Drink", amount = 100)]
                            unhovered Hide('restockTooltip')
                            action [IncrementField(mc, 'money', -1 * int(bar_drinkStockCostPerLevel * 100)), IncrementVariable('bar_drinkStock', 100)]
                        textbutton "+500":
                            hovered [CaptureFocus('restockHover'), Show('restockTooltip', stockType = "Drink", amount = 500)]
                            unhovered Hide('restockTooltip')
                            action [IncrementField(mc, 'money', -1 * int(bar_drinkStockCostPerLevel * 500)), IncrementVariable('bar_drinkStock', 500)]
                    if(bar_autoRestockDrink):
                        textbutton _('On'):
                            hovered [CaptureFocus('autoRestockHover'), Show('autoRestockTooltip')]
                            unhovered Hide('autoRestockTooltip')
                            action [ToggleVariable('bar_autoRestockDrink')]
                    else:
                        textbutton _('Off'):
                            hovered [CaptureFocus('autoRestockHover'), Show('autoRestockTooltip')]
                            unhovered Hide('autoRestockTooltip')
                            action [ToggleVariable('bar_autoRestockDrink')]
                    text "-"
                    textbutton _('Upgrade'):
                        hovered [CaptureFocus('drinkUpgradeHover'), Show('drinkUpgradeTooltip')]
                        unhovered Hide('drinkUpgradeTooltip')
                        if(bar_drinkLevel < bar_drinkMaxLevel):
                            action [Hide('drinkUpgradeTooltip'), Call('buyDrinkUpgrade')]

                    text _('Food')
                    text str(bar_foodLevel)
                    $ bar_foodProfitLoss = bar_foodIncomeBase + (bar_foodIncomePerLevel * (bar_foodLevel-1)) if bar_foodLevel > 0 and bar_foodStock > 0 else 0
                    text str(bar_foodProfitLoss)
                    text str(bar_foodStock)
                    hbox:
                        textbutton "+100":
                            hovered [CaptureFocus('restockHover'), Show('restockTooltip', stockType = "Food", amount = 100)]
                            unhovered Hide('restockTooltip')
                            action [IncrementField(mc, 'money', -1 * int(bar_foodStockCostPerLevel * 100)), IncrementVariable('bar_foodStock', 100)]
                        textbutton "+500":
                            hovered [CaptureFocus('restockHover'), Show('restockTooltip', stockType = "Food", amount = 500)]
                            unhovered Hide('restockTooltip')
                            action [IncrementField(mc, 'money', -1 * int(bar_foodStockCostPerLevel * 500)), IncrementVariable('bar_foodStock', 500)]
                    if(bar_autoRestockFood):
                        textbutton _('On'):
                            hovered [CaptureFocus('autoRestockHover'), Show('autoRestockTooltip')]
                            unhovered Hide('autoRestockTooltip')
                            action [ToggleVariable('bar_autoRestockFood')]
                    else:
                        textbutton _('Off'):
                            hovered [CaptureFocus('autoRestockHover'), Show('autoRestockTooltip')]
                            unhovered Hide('autoRestockTooltip')
                            action [ToggleVariable('bar_autoRestockFood')]
                    text ""
                    textbutton _('Upgrade'):
                        hovered [CaptureFocus('foodUpgradeHover'), Show('foodUpgradeTooltip')]
                        unhovered Hide('foodUpgradeTooltip')
                        if(bar_foodLevel < bar_foodMaxLevel):
                            action [Call('buyFoodUpgrade')]

                    text ""
                    text ""
                    text ""
                    text ""
                    text ""
                    text ""
                    text ""
                    text ""

                    text ""
                    text ""
                    text _('{b}Income X{/b}')
                    text _('{b}Impact{/b}')
                    text ""
                    text ""
                    text ""
                    text ""

                    text _('Capacity')
                    text str(bar_capacity)
                    $ bar_capacityProfitMultiplier = round(1.0 + (0.2 * ((bar_capacity - 10)*0.2)), 2)
                    text "x[str(bar_capacityProfitMultiplier)]"
                    text "-[str(bar_capacity * 5)]"
                    text ""
                    text ""
                    textbutton _('Downgrade'):
                        hovered [CaptureFocus('capacityDowngradeHover'), Show('capacityDowngradeTooltip')]
                        unhovered Hide('capacityDowngradeTooltip')
                        action [Call('capacityDowngrade')]
                    textbutton _('Upgrade'):
                        hovered [CaptureFocus('capacityUpgradeHover'), Show('capacityUpgradeTooltip')]
                        unhovered Hide('capacityUpgradeTooltip')
                        if(bar_capacity < bar_capacityMax):
                            action [Hide('capacityUpgradeTooltip'), Call('buyCapacityUpgrade')]

                    text _('Total')
                    text _('Per Day')
                    python:
                        bar_profit = round((bar_drinkProfitLoss + bar_foodProfitLoss) * bar_capacityProfitMultiplier, 2)
                        bar_loss = bar_staffCosts + bar_rent
                        bar_totalProfitLoss = int(bar_profit - bar_loss)
                    text str(bar_totalProfitLoss)
                    text ""
                    text ""
                    text ""
                    text ""
                    text ""
                if(mc.money < -1000):
                    textbutton _('Bankrupt?'):
                        xalign 1.0 yalign 1.0
                        action [Show('bankruptScreen')]

label fireEmployee:
    python:
        if(bar_numberOfStaff > 1):
            bar_numberOfStaff -= 1
            if(bar_numberOfStaff == 1):
                bar_foodLevel = 0
                renpy.notify('Обслуживание едой остановлено: не хватает сотрудников!')
            if(bar_capacity - 5 > (bar_numberOfStaff + 1) * 10):
                bar_capacity -= 10
                renpy.notify('Вместимость бара снижена из-за нехватки сотрудников!')
    call screen needInteraction

label hireEmployee:
    python:
        bar_drinkProfitLoss = bar_drinkIncomeBase + (bar_drinkIncomePerLevel * (bar_drinkLevel-1))
        bar_foodProfitLoss = bar_foodIncomeBase + (bar_foodIncomePerLevel * (bar_foodLevel-1)) if bar_foodLevel > 0 else 0
        bar_capacityProfitMultiplier = round(0.6 + round(bar_capacity / 25, 2), 2)
        bar_profit_potential = round((bar_drinkProfitLoss + bar_foodProfitLoss) * bar_capacityProfitMultiplier, 2)
        bar_staffCosts_potential = (bar_numberOfStaff+1) * bar_costPerEmployee
        bar_loss_potential = bar_staffCosts_potential + bar_rent
        bar_totalProfitLoss_potential = int(bar_profit_potential - bar_loss_potential)
        if(bar_totalProfitLoss_potential > 0):
            bar_numberOfStaff += 1
        else:
            renpy.notify('Дополнительный сотрудник приведёт к убыткам!')
    call screen needInteraction

label buyDrinkUpgrade:
    python:
        if(mc.money >= bar_drinkLevelUpgradeCost):
            mc.money -= bar_drinkLevelUpgradeCost
            bar_drinkLevel += 1
            renpy.hide_screen('drinkUpgradeTooltip')
    call screen needInteraction

label buyFoodUpgrade:
    python:
        if(mc.money >= bar_foodLevelUpgradeCost and bar_numberOfStaff > 1):
            mc.money -= bar_foodLevelUpgradeCost
            bar_foodLevel += 1
            renpy.hide_screen('foodUpgradeTooltip')
    call screen needInteraction

label capacityDowngrade:
    python:
        if(bar_capacity >= 15):
            bar_capacity -= 5
    call screen needInteraction

label buyCapacityUpgrade:
    python:
        if(mc.money >= bar_capacityUpgradeCost):
            if(bar_capacity + 5 <= (bar_numberOfStaff + 1) * 10):
                mc.money -= bar_capacityUpgradeCost
                bar_capacity += 5
            else:
                renpy.notify('Чтобы увеличить вместимость, найми ещё сотрудников!')
    call screen needInteraction

# Tooltip screens
screen employeeDowngradeTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'employeeDowngradeHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Fire employee.\nThis may reduce the capacity or food level.')

screen employeeUpgradeTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'employeeUpgradeHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Hire extra employee.\nAllows upgrades to food level and capacity.\nIncrease costs by an additional $[str(bar_costPerEmployee)] per day')

screen drinkUpgradeTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'drinkUpgradeHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Improve quality and\nvariety of drink selection.\n$[str(bar_drinkLevelUpgradeCost)]')

screen foodUpgradeTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'foodUpgradeHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Improve quality and\nvariety of food selection.\n$[str(bar_foodLevelUpgradeCost)]')

screen capacityDowngradeTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'capacityDowngradeHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Reduce bar capacity by 5.')

screen capacityUpgradeTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'capacityUpgradeHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Increase bar capacity by 5.\n$[bar_capacityUpgradeCost]')

screen restockTooltip(stockType, amount):
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'restockHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            if(stockType == "Drink"):
                $ restockCost = int(bar_drinkStockCostPerLevel * amount)
                text _('Restock by [amount].\n$[restockCost]\nYou are allowed to go into debt for stock!')
            elif(stockType == "Food"):
                $ restockCost = int(bar_foodStockCostPerLevel * amount)
                text _('Restock by [amount].\n$[restockCost]\nYou are allowed to go into debt for stock!')

screen autoRestockTooltip:
    zorder 5
    style_prefix "barOverviewActionHover"
    nearrect:
        focus 'autoRestockHover'
        preferred_side 'right'
        frame:
            background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
            xalign 0.5 yalign 0.5
            text _('Automatically restock by 500 when stock runs out.\nOnly use when certain, it might drain your account!\nIncurs a $[bar_autoRestockCost] fee')

style barOverviewGrid_text:
    size 22
    align (0.5, 0.5)

style barOverviewGrid_button:
    align (0.5, 0.5)
    idle_background Frame('gui/genericButtonBackground.webp', 40, 40, 40, 40)
    hover_background Frame('gui/genericButtonBackgroundHover.webp', 40, 40, 40, 40)
    insensitive_background Frame('gui/genericButtonBackgroundDisabled.webp', 40, 40, 40, 40)
    padding (5, 3)

style barOverviewGrid_button_text:
    size 22

style barOverviewActionHover_text:
    size 20

screen bankruptScreen:
    modal True
    zorder 100
    frame:
        background Frame('gui/genericUIBoxRounded.webp', 40, 40, 40, 40)
        xcenter 0.5 ycenter 0.5
        xsize 0.6 ysize 0.6
        textbutton '{size=30}X':
            style 'genericCircleButtonStyle'
            text_align (0.5, 0.5)
            action Hide('bankruptScreen')
        vbox:
            align (0.5, 0.5)
            text _("You've fallen on hard times...\n Plenty of businesses struggle at first. Don't feel bad!\n\nYour old boss has offered to help you out. Will you accept his kind offer?"):
                text_align 0.5
            text ""
            style_prefix 'genericButtonStyle'
            hbox:
                align (0.5, 0.5)
                textbutton _('I can do this myself!'):
                    action Hide('bankruptScreen')
                text " "
                textbutton _('Yes please...'):
                    action [SetField(mc, 'money', 500), Hide('bankruptScreen')]

screen barTutorial1:
    modal True
    zorder 100
    style_prefix 'bartutorial'
    frame:
        add 'images/tutorial/bar/profit.webp'
        textbutton _('Next >'):
            xalign 1.0
            action [Hide('barTutorial1'), Show('barTutorial2')]
        textbutton _('< Close'):
            xalign 0.0
            action [Hide('barTutorial1')]

screen barTutorial2:
    modal True
    zorder 100
    style_prefix 'bartutorial'
    frame:
        add 'images/tutorial/bar/level.webp'
        textbutton _('Next >'):
            xalign 1.0
            action [Hide('barTutorial2'), Show('barTutorial3')]
        textbutton _('< Previous'):
            xalign 0.0
            action [Hide('barTutorial2'), Show('barTutorial1')]

screen barTutorial3:
    modal True
    zorder 100
    style_prefix 'bartutorial'
    frame:
        add 'images/tutorial/bar/stock.webp'
        textbutton _('Next >'):
            xalign 1.0
            action [Hide('barTutorial3'), Show('barTutorial4')]
        textbutton _('< Previous'):
            xalign 0.0
            action [Hide('barTutorial3'), Show('barTutorial2')]

screen barTutorial4:
    modal True
    zorder 100
    style_prefix 'bartutorial'
    frame:
        add 'images/tutorial/bar/capacity.webp'
        textbutton _('Next >'):
            xalign 1.0
            action [Hide('barTutorial4'), Show('barTutorial5')]
        textbutton _('< Previous'):
            xalign 0.0
            action [Hide('barTutorial4'), Show('barTutorial3')]

screen barTutorial5:
    modal True
    zorder 100
    style_prefix 'bartutorial'
    frame:
        add 'images/tutorial/bar/general.webp'
        textbutton _('Close >'):
            xalign 1.0
            action [Hide('barTutorial5')]
        textbutton _('< Previous'):
            xalign 0.0
            action [Hide('barTutorial5'), Show('barTutorial4')]

style bartutorial_frame:
    xsize 1.0 ysize 1.0
    background None
    padding (0,0)

style bartutorial_button:
    background '#f51414'
    yalign 0.5

style bartutorial_button_text:
    color '#ffffff'
    hover_color '#919191'
    size 60
