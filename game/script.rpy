# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
init:
    image bg1 = im.Scale("bg dull_street.png", 1920, 1080)
    image bg2 = im.Scale("field 2.png", 1920, 1080)
    image bg3 = im.Scale("castle.png", 1920, 1080)
    image bg4 = im.Scale("town.png", 1920, 1080)
    image bg5 = im.Scale("wheat field.png", 1920, 1080)
    image bg6 = im.Scale("forest.png", 1920, 1080)
    image bg7 = im.Scale("shop.png", 1920, 1080)
    image bg8 = im.Scale("room.png", 1920, 1080)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    show bg1

    show eileen happy

    e "Шикарный фон1"

    jump episode2


label episode2:

    show bg2

    e "ООО ШИКАРНЫЙ ФОН 2"

    jump episode3


label episode3:
    
    show bg3

    e "ОПА ШИКАРНЫЙ ФОН 3"

    jump episode4


label episode4:

    show bg4

    e "УРААА ШИКАРНЫЙ ФОН 4"
    
    jump episode5


label episode5:

    show bg5

    e "Блин что не фон все красивые"
    
    jump episode6



label episode6:

    show bg6

    e "Ура фон 6 :)"
    
    jump episode7


label episode7:

    show bg7

    e "Фон 7 погнали"

    jump episode8


label episode8:

    show bg8

    e "Фон 8 норм"

    return