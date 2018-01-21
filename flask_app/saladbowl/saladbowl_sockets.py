from saladbowl.saladbowl_game import Saladbowl_game

SOCKET_JOIN_ROOM="join_room"
SOCKET_JOIN_ROOM_CAST="join_room_cast"
SOCKET_GAME_UPDATE_CAST="game_update_cast"


def msg_create(room_id):
    """ --------------------------------------------------
    room_id : id of the room
    game_state : GS_WAITING_TO_START
    """
    return {'room_id' : room_id,
            'game_state' : Saladbowl_game.GS_WAITING_TO_START}

def msg_join_room(game):
    """ --------------------------------------------------
    room_id : game.room_id
    game_state : game.game_state
    ordered_players : game.get_sorted_player_names()
    word_list : game.word_list
    players : dictionary of players:
              'username' : player.username
              'submitted_words' : player.submitted_words
              'team' : player.team
    """
    return game.to_dic()

def msg_game_update_cast(game):
    return game.to_dic()

def msg_join_room_cast(game):
    return game.to_dic()
