

from project_month01.my_2048_game.ui import View
from project_month01.my_2048_game.bll import GameCoreController

if __name__ == "__main__":

    view = View()
    controller = GameCoreController()
    controller.print_map()

    while True:
        view.start_game()



