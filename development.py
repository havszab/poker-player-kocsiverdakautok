test = {
    "tournament_id": "550d1d68cd7bd10003000003",

    "game_id": "550da1cb2d909006e90004b1",

    "round": 0,
    "bet_index": 0,

    "small_blind": 10,

    "current_buy_in": 320,

    "pot": 400,

    "minimum_raise": 240,
    "dealer": 1,

    "orbits": 7,

    "in_action": 1,

    "players": [
        {

            "id": 0,

            "name": "Albert",

            "status": "active",

            "version": "Default random player",

            "stack": 1010,

            "bet": 320
        },
        {
            "id": 1,
            "name": "kocsiverdakautok",
            "status": "active",
            "version": "Default random player",
            "stack": 1590,
            "bet": 80,
            "hole_cards": [

                {
                    "rank": "6",
                    "suit": "hearts"
                },
                {
                    "rank": "K",
                    "suit": "spades"
                }
            ]
        },
        {
            "id": 2,
            "name": "Chuck",
            "status": "out",
            "version": "Default random player",
            "stack": 0,
            "bet": 0
        }
    ],
    "community_cards": [
        {
            "rank": "4",
            "suit": "spades"
        },
        {
            "rank": "A",
            "suit": "hearts"
        },
        {
            "rank": "6",
            "suit": "clubs"
        }
    ]
}


def get_our_info(game_state):
    for player in game_state["players"]:
        if player["id"] == 5:
            return player


def is_A_or_K(our_player):
    hand = our_player["hole_cards"]
    high_card = ["A", "K"]
    if hand[0]["rank"] in high_card or hand[1]["rank"] in high_card:
        return True
    return False


def is_Q_or_J(our_player):
    hand = our_player["hole_cards"]
    high_card = ["Q", "J"]
    if hand[0]["rank"] in high_card or hand[1]["rank"] in high_card:
        return True
    return False


def is_card_in_hand_pair(our_player):
    hand = our_player["hole_cards"]
    if hand[0]["rank"] == hand[1]["rank"]:
        return True
    return False


