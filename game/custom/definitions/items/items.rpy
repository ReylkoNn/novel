# Declare items available in the game

# Item class definition
init python:
    class Item:
        def __init__(self, name, apiName, value, description = Null, giftable = True, unique = False):
            self.name = name
            self.apiName = apiName
            self.value = value
            self.giftable = giftable
            self.unique = unique
            self.description = description

define item_chocolateBar = Item('Шоколадка', 'chocolatebar', 5)
define item_book = Item('Книга', 'book', 15)
define item_flowers = Item('Цветы', 'flowers', 10)
define item_wine = Item('Бутылка вина', 'wine', 20)
define item_videogame = Item('Видеоигра', 'videogame', 50)
define item_candles = Item('Свечи', 'candles', 25)
define item_dress = Item('Платье', 'dress', 80)
define item_perfume = Item('Духи', 'perfume', 40)
define item_goldRing = Item('Золотое кольцо', 'goldring', 300)
#define item_diamondRing = Item('Бриллиантовое кольцо', 'diamondRing', 5000, 'Предложение руки и сердца')
define item_car = Item('Машина', 'car', 2000, 'Нужна для некоторых событий', False, True)
define item_homeupgrade1 = Item('Улучшение дома 1', 'homeupgrade1', 10000, 'Увеличивает вместимость дома на 2.', False, True)
define item_homeupgrade2 = Item('Улучшение дома 2', 'homeupgrade2', 10000, 'Увеличивает вместимость дома на 2.', False, True)

label initialiseItems:
    $ i = 0

label mcBuyItem(location, itemName):
    python:
        item = getattr(renpy.store, itemName)

        mc.money -= item.value
        location.inventory[itemName] -= 1

        itemFoundInInventory = False
        if(itemName in mc.inventory.keys()):
            mc.inventory[itemName] += 1
        else:
            mc.inventory.update({itemName: 1})
    if(renpy.has_label('buyItem_' + item.apiName)):
        call expression 'buyItem_' + item.apiName from _call_expression_47
    call screen needInteraction
