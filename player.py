
class Player:
    VERSION = "2.2 Never Lucky"


    def betRequest(self, game_state):
        for player in game_state["player"]:
            if player["name"] == "kocsiverdakautok":
                return player


    def showdown(self, game_state):
        pass

