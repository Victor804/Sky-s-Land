from game_files.character import Character
from game_files.menu import Menu
from game_files.game import Game

menu = Menu()
button = menu.main()

if (button == "play"):
    game = Game()
    game.maps(1)

elif (button == "saves"):
    menu.saves()

elif (button == "options"):
    menu.options()
