define me = Character('Максим', color="#3f5af3")
define tapher = Character('Тапфер', color="#3cbada")
define schwert = Character('Шверт', color="#d6702b")
define lignarin = Character('Лигнарин', color="#d83939")

init:
    image village = im.Scale("village.png", 1920, 1080)
    image tapher_pic = im.Scale("tapher.png", 615, 1024)
    image schwert_pic = im.Scale("schwert.png", 615, 1024)
    image lignarin_pic = im.Scale("lignarin.png", 615, 1024)

label episode7:
    show village
    with fade

    show lignarin_pic at center
    show marco_pic at left
    show tapher_pic at right
    with dissolve

    lignarin "О, наконец-то вы добрались. Успели познакомиться с нашим новым товарищем?"

    tapher "Успели, успели. Отдохнем пару часиков и двинем дальше"

    lignarin "Отлично! А ты что скажешь, друг?"

    me "Ну, мне бы хотелось знать, куда мы все-таки идем"

    lignarin "Хах, какой нетерпеливый. Мы идем помогать одним очень хорошим людям"

    me "Да-да, это я уже слышал"

    hide tapher_pic
    show schwert_pic
    with dissolve

    schwert "Эй, неужели в наше захолустье кого-то заносит? Вы явно не местные"

    lignarin "Ну, не сказала бы, что не местные"

    schwert "Тогда я попрошу помочь мне, следуйте за мной в кузницу"

    lignarin "А с чего ты решил, что мы побежим за каким-то незнакомцем?"

    schwert "Вот, сразу видно, что не из этих краев. Здесь все меня знают — я кузнец Шверт. В пятидесяти верстах вам не найти лучше кузнеца, чем я. Идем"

    menu:
        "Пойти с кузнецом":
            me "Веди нас, кузнец. Всегда мечтал увидеть, как доспехи делают"

            hide lignarin_pic
            hide marco_pic
            hide schwert_pic
            hide village
            with fade

            jump episode8

        "Отказаться":
            me "Какой-то подозрительный он, не доверяю ему я. Пойдемте отсюда"

            schwert "Ах, вот как! Шверта подозрительным звать решил?! Чтоб не видел я тебя в наших землях! Проваливай!"

            lignarin "Ну и ну...пойдемте, друзья"

            hide lignarin_pic
            hide marco_pic
            hide schwert_pic
            hide village
            with fade

            jump episode9
