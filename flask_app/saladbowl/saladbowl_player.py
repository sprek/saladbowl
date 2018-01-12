
class Saladbowl_player(object):

    TEAM_BLUE='blue'
    TEAM_RED='red'
    
    def __init__(self, username='', id_list=[], submitted_words=False, order=0):
        self.username = username
        self.id_list = id_list
        self.submitted_words = submitted_words
        self.team = self.TEAM_BLUE
        self.order = order

    def __hash__(self):
        return hash(username)

    def __lt__(self, other):
        return self.order < other.order

    def remove_id(self, player_id):
        try:
            self.id_list.remove(player_id)
        except:
            print ("Unable to remove id from player: " + self.username)
