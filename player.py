import development


class Player:
    VERSION = "2.1.4 logic order modified "

    def betRequest(self, game_state):
        our_player = development.get_our_info(game_state)
        if development.is_card_in_hand_pair(our_player):
            return max(int(game_state["current_buy_in"]), int(our_player["stack"] * 0.25))
        if development.is_high_cards(our_player):
            if int(game_state["current_buy_in"]) > int(our_player["stack"]):
                return int(our_player["stack"])
            return max(int(game_state["current_buy_in"]), int(our_player["stack"] * 0.1))
        if game_state["current_buy_in"] == int(game_state["small_blind"])*2:
            return int(game_state["small_blind"])*2
        return 0

    def showdown(self, game_state):
        pass

