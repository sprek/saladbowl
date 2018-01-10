class Saladbowl_player(object):
    def __init__(self, username='', id_list=[], submitted_words=False):
        self.username = username
        self.id_list = id_list
        self.submitted_words = submitted_words

    def __hash__(self):
        return hash(username)

    def remove_id(self, player_id):
        try:
            self.id_list.remove(player_id)
        except:
            print ("Unable to remove id from player: " + self.username)
