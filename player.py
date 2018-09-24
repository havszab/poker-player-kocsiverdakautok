import development


class Player:
    VERSION = "3.2"

    def betRequest(self, game_state):
        our_player = development.get_our_info(game_state)

        if development.is_card_in_hand_pair(our_player):
            if int(game_state["current_buy_in"]) > int(our_player["stack"]):
                return int(our_player["stack"])
            return max(int(game_state["current_buy_in"]), int(our_player["stack"] * 0.25))

        elif development.is_A_or_K(our_player):
            if int(game_state["current_buy_in"]) > int(our_player["stack"]):
                return int(our_player["stack"])
            return max(int(game_state["current_buy_in"]), int(our_player["stack"] * 0.2))

        elif development.is_Q_or_J(our_player):
            if int(game_state["current_buy_in"]) > int(our_player["stack"]):
                return int(our_player["stack"] * 0.2)
            return max(int(game_state["current_buy_in"]), int(our_player["stack"] * 0.1))

        return 0

    def showdown(self, game_state):
        pass

