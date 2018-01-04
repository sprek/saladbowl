class Saladbowl_game(object):
    def __init__(self, room_id='', word_list=[], num_words_per_player=3, players=[], username=''):
        self.room_id = room_id
        self.word_list = word_list
        self.word_list = word_list
        self.num_words_per_player = num_words_per_player
        self.players = players
        self.numtest = 0

    def to_dic(self):
        return {
            "room_id": self.room_id,
            "players": self.players,
            "word_list": self.word_list,
            "numtest" : self.numtest,
        }

    
