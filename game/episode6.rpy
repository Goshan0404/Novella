define me = Character('Максим', color="#3f5af3")
define tapher = Character('Тапфер', color="#3cbada")
define marco = Character('Марко', color="#0f8a15ff")
define munce = Character('Мюнц', color="#faef50")

init:
    image bridge = im.Scale("bridge.png", 1920, 1080)
    image tapher_pic = im.Scale("tapher.png", 615, 1024)
    image marco_pic = im.Scale("marco.png", 615, 1024)
    image munce_pic = im.Scale("munce.png", 615, 1024)

label episode6:
    show bridge
    with fade

    show tapher_pic at left with dissolve
    show marco_pic at right with dissolve

    marco "И вы никого другого не нашли? Что это такое?"

    me "Во-первых, не что, а кто, а во-вторых…"

    marco "Помолчи, тебе слово не давали. Тапфер, что за ерунда? Неужели так сложно найти подходящую замену, а не вот это нечто?"

    tapher "Не бузи, Марко. Мы же не крепость штурмовать идем в конце концов, так что с задачей он справится"

    marco "Да-да, как бы этот новичок в штаны не наложил при первой опасности"

    me "Ну знаешь, за словами следи! Советую тебе прикусить язык"

    marco "А то что? Ударишь меня, а? Ты рискуешь своим здоровьем"

    tapher "Так, закончили оба. Лигнарин присоединится к нам неподалеку от деревни Рагако, так что держим путь на юго-запад"

    hide tapher_pic with dissolve
    show munce_pic at left with dissolve

    munce "Друзья, караул, мне срочно нужна ваша помощь!"

    marco "Ты кто вообще такой?"

    munce "Мюнц я, торговец. Братцы, выручайте. По мосту ехал я, колесо отлетело, повозка накренилась, того гляди упадет. Помогите вытащить"

    menu:
        "Помочь торговцу":
            me "Нельзя бросать человека в беде, ему надо помочь!"

            marco "Не надо так на меня смотреть, разве я похож на благодетеля? Сам вызвался, сам и помогай, мы подождем"

            munce "Вот спасибо. За мной, тут недалеко"

            hide marco_pic with fade

            munce "А ты силён, на вид и не скажешь. Спасибо тебе, дружище. Если будешь в районе Троста, знай, торговец Мюн всегда рад тебя видеть. Удачи"

            hide munce_pic with dissolve
            show marco_pic at right with dissolve

            marco "А ты неплох, новичок, молодец. Ладно, пошли, Лигнарин нас, наверно, заждалась уже"

        "Отказаться":
            me "Извини, но нам в другую сторону"

            marco "Ладно, в путь. Не отставай, новенький"

            hide munce_pic with dissolve

    hide marco_pic with dissolve
    hide bridge with dissolve
    jump episode7

