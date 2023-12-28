define seller = Character('Продавец', color="#c8ffc8")
define anton = Character('Антон', color="#50fa50")
define me = Character('Максим', color="#3f5af3")

init:
    image shop = im.Scale("shop.png", 1920, 1080)
    image anton_pic = im.Scale("anton.png", 615, 1024)

label episode1(beer = False):
    show shop
    with fade

    me "Моего напарника отстранили от работы, а это значит, что теперь я могу работать один, и никто мне не помешает. Такое действительно бывает не часто. Что же мне по такому случаю взять?"

    menu:
        "Пиво" if beer:
            me "На меня глядит игриво пиво, пиво...\nПожалуй, возьму именно его"
        "Чай":
            me "Золотая чаша золотая... А я беру зеленый чай"
        "Ничего":
            me "Дома есть кофе, им и обойдусь сегодня"

    show anton_pic
    with dissolve
    seller "Здравствуйте, пакет нужен, скидочная карта есть?"

    me "Здра..."
    me "Тоха? Ты чтоль? Вот это встреча!"

    anton "Ух ты! Неожиданно…"

    me "Не ожидал увидеть выпускника УГИ здесь, хах, удачи тебе. Сдачи не надо"

    hide shop
    hide anton_pic

    $ renpy.call("episode2", beer=beer)

