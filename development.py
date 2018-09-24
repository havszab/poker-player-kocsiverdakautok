test ={"game_state":{"tournament_id":"5b968a7bb7b7260004000002","game_id":"5ba8b9933e762d0004000078","round":0,"players":[{"name":"Legnehezebb","stack":1000,"status":"active","bet":0,"hole_cards":[],"time_used":0,"version":"0.4.3","id":0},{"name":"team Korda","stack":1000,"status":"active","bet":0,"hole_cards":[],"time_used":0,"version":"1.0 Black Widow","id":1},{"name":"Eager Ducks","stack":1000,"status":"active","bet":0,"hole_cards":[],"time_used":0,"version":"Default Java folding player","id":2},{"name":"The Embarrassed Partridges","stack":1000,"status":"active","bet":0,"hole_cards":[],"time_used":0,"version":"Java player V0.1","id":3},{"name":"pokerInterFace","stack":1000,"status":"active","bet":0,"hole_cards":[],"time_used":0,"version":"0.1","id":4},{"name":"kocsiverdakautok","stack":1000,"status":"active","bet":0,"hole_cards":["A", "A"],"time_used":0,"version":"1.2","id":5}],"small_blind":2,"big_blind":4,"orbits":0,"dealer":4,"community_cards":[],"current_buy_in":0,"pot":0}}


def get_our_info(game_state):
    for player in game_state["players"]:
        if player["name"] is "kocsiverdakautok":
            return player


def is_high_cards(our_player):
    hand = our_player["hole_cards"]
    high_card = ["A", "K", "Q", "J"]
    if hand[0]["rank"] in high_card or hand[1]["rank"] in high_card:
        return True
    else:
        return False


def is_card_in_hand_pair(our_player):
    hand = our_player["hole_cards"]
    if hand[0]["rank"] == hand[1]["rank"]:
        return True
    return False