define me = Character('Максим', color="#3f5af3")
define vice = Character('Вайс', color = "#8b5207")
define lignarin = Character('Лигнарин', color="#d83939")
define unknown_lignarin = Character('Девушка', color = "#fff")

init:
    image dog = im.Scale("doggy.png", 615, 1024)
    image town = im.Scale("town.png", 1920, 1080)
    image lignarin_pic = im.Scale("lignarin.png", 615, 1024)

label episode4:
    show town
    with fade

    me "В провинциальном городке, был праздник, музыка звучала…"
    me "И как-то странно на него смотрели местные собаки..."
    me "Почему-то как-то неуютно. Все смотрят на меня, словно я у них что-то украл"

    show dog at right
    
    vice "Р-р-р-р-р-р-р"

    me "Твою ж... пес!"

    unknown_lignarin "Вайс, место! А ну, ушел от него!"

    show lignarin_pic
    with dissolve

    unknown_lignarin "Извините его, обычно он себя так не ведет. Даже не знаю, что на него нашло"

    me "Да, п-пожалуй не стоит злиться на животное. А мы с вами не встречались уже?"

    unknown_lignarin "Хм, могли. Многие меня здесь знают, всех не упомнить"

    me "Ладно, возможно мне и показалось"

    menu:
        "Где можно поесть?":
            me "Слушай, подскажи, а где можно вкусно перекусить?"

            lignarin "Это ты обратился по адресу, друг. Идем за мной. Меня, кстати, Лигнарин зовут"

            hide dog
            hide town
            hide lignarin_pic
            with dissolve
            jump episode5

        "Что это за место?":
            pass

    me "Слушай, подскажи..."

    unknown_lignarin "Ну и что ты хочешь от меня узнать? Надеюсь, что-то важное"

    menu:
        "Как заработать денег?":
            me "Можно ли тут как-то монету заработать? А то есть хочу очень"

            lignarin "Это ты обратился по адресу, друг. Идем за мной. Меня, кстати, Лигнарин зовут"

        "Где тут отдохнуть?":
            me "Устал я как-то, подскажи, где можно весело провести время, если ты понимаешь о чем я"

            lignarin "У меня имя есть — Лигнарин. Пошли-ка за мной"
    
    hide dog
    hide town
    hide lignarin_pic
    with dissolve
    jump episode5