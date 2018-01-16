from saladbowl.saladbowl_game import Saladbowl_game

def msg_create(room_id):
    """ --------------------------------------------------
    room_id : id of the room
    game_state : GS_WAITING_TO_START
    """
    return {'room_id' : room_id,
            'game_state' : Saladbowl_game.GS_WAITING_TO_START}

def msg_join(game):
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
