class Saladbowl_game(object):
    def __init__(self, room_id='', word_list=[], num_words_per_player=3, players_by_username={}, username=''):
        self.room_id = room_id
        self.word_list = word_list
        self.num_words_per_player = num_words_per_player
        self.players_by_username = players_by_username

    def to_dic(self):
        return {
            "room_id": self.room_id,
            "players": players_by_username.keys(),
            "word_list": self.word_list,
        }

    def get_player_from_id(player_id):
        for username in self.players_by_username:
            cur_player = players_by_username[username]
            if player_id in cur_player.id_list:
                return cur_player
        return None

    def add_id_to_player(username, player_id):
        if username in [x.username for x in player_to_ids]:
            if not player_id in player_to_ids[]:
                player_to_ids[player].append(player_id)
        else:
            player_to_ids[Saladbowl_player(player] = [player_id]

            
class Saladbowl_player(object):
    def __init__(self, username='', id_list=[], submitted_words=False):
        self.username = username
        self.id_list = id_list
        self.submitted_words = submitted_words

    def __hash__():
        return hash(username)
