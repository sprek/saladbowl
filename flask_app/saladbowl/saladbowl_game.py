class Saladbowl_game(object):
    def __init__(self, game_id='', word_list=[], num_words_per_player=3, players=[], cur_player=''):
        self.game_id = game_id
        self.word_list = word_list
        self.word_list = word_list
        self.num_words_per_player = num_words_per_player
        self.players = players
        self.cur_player = cur_player

    def to_dic(self):
        return {
            "game_id": self.game_id,
            "word_list": self.word_list,
            "players": self.players,
            "cur_player": self.cur_player
        }

    
