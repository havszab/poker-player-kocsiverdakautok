
class Player:
    VERSION = "1.2"

    def betRequest(self, game_state):
        return int(game_state["small_blind"])*2

    def showdown(self, game_state):
        pass

