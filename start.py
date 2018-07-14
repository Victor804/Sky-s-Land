from game_files.character import Character
from game_files.level import Level
from game_files.menu import Menu

menu = Menu()
button = menu.main()

if (button == "play"):
    print("play")

elif (button == "saves"):
    menu.saves()

elif (button == "options"):
    menu.options()
