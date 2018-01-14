import saladbowl.saladbowl_player
from saladbowl.saladbowl_player import Saladbowl_player

GS_WAITING_FOR_WORDS="WAITING_FOR_WORDS"
GS_WAITING_TO_START="WAITING_TO_START"
GS_STARTED="STARTED"

class Saladbowl_game(object):
    
    def __init__(self, room_id='', num_words_per_player=3, word_list=[]):
        self.room_id = room_id
        self.num_words_per_player = num_words_per_player
        self.word_list = word_list
        self.players_by_username = {}
        self.game_state = GS_WAITING_FOR_WORDS
        self.player_counter = 0
        if word_list:
            # if we already have a word list, then the players just need to hit start
            self.game_state = GS_WAITING_TO_START

    def get_sorted_players(self):
        return sorted([x for _,x in self.players_by_username.items()])

    def to_dic(self):
        return {
            "room_id": self.room_id,
            "players": [x.username for x in self.get_sorted_players()],
            "player_teams": [x.team for x in self.get_sorted_players()],
            "word_list": self.word_list,
            "game_state": self.game_state
        }

    def get_player_from_id(self, player_id):
        """
        Returns the Saladbowl_player object that has player_id in its id_list
        """
        for username in self.players_by_username:
            cur_player = self.players_by_username[username]
            if player_id in cur_player.id_list:
                return cur_player
        return None

    def add_id_to_player(self, username, player_id):
        """ 
        Adds a user to the players_by_username dictionary.
        If the user doesn't exist, create the user.
        If the user does exist, add the player_id to the player's id_list
        """ 
        if username in self.players_by_username:
            cur_player = self.players_by_username[username]
            if not player_id in cur_player.id_list:
                cur_player.id_list.append(player_id)
        else:
            tmp_player = Saladbowl_player(username, [player_id], False, self.player_counter)
            self.player_counter += 1

            # default team is blue
            count_blue = [x.team for _,x in self.players_by_username.items()].count(Saladbowl_player.TEAM_BLUE)
            if count_blue > len(self.players_by_username) / 2:
                tmp_player.team = Saladbowl_player.TEAM_RED
                
            self.players_by_username[username] = tmp_player

    def get_player(self, username):
        """
        Returns the player object associated with username
        """
        return self.players_by_username[username]

    def remove_player_id(self, player_id):
        """
        Finds the player with the given ID, and removes it from their id_list
        If there are no more IDs in the id_list, remove the player from the players_by_username dict
        """
        cur_player = self.get_player_from_id(player_id)
        if not cur_player:
            print ("Unable to find player with id: " + player_id)
            return False
        cur_player.remove_id(player_id)
        if len(cur_player.id_list) == 0:
            self.players_by_username.pop(cur_player.username)
        return True

