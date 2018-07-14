from game_files.character import Character
from game_files.level import Level
from game_files.main_menu import Menu

menu = Menu()
button = menu.main()

if (button == "play"):
    print("play")

elif (button == "saves"):
    print("saves")

elif (button == "options"):
    print("options")

else:
    print("Error")
