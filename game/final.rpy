define me = Character('Максим', color="#3f5af3")
init:
    image white = Solid("#fff")
    image daily_room = im.Scale("daily_room.png", 1920, 1080)

label final:
    show white
    with fade

    me "Солнце…"

    show daily_room
    with fade
    hide white

    me "Уф...давно я так хорошо не спал"
    me "Вот черт, время...опаздываю на работу!"