import saladbowl.saladbowl_player
from saladbowl.saladbowl_player import Saladbowl_player

class Saladbowl_game(object):
    GS_WAITING_TO_START="WAITING_TO_START"
    GS_WAITING_ON_TURN="WAITING_ON_TURN"
    GS_PLAYING="PLAYING"
    GS_ROUND1="ROUND1";
    GS_ROUND2="ROUND2";
    GS_ROUND3="ROUND3";
    GS_ROUND4="ROUND4";
    GS_FINISHED="FINISHED";
    
    def __init__(self, room_id='', num_words_per_player=3, word_list=[]):
        self.room_id = room_id
        self.num_words_per_player = num_words_per_player
        self.word_list = word_list
        self.players_by_username = {}
        self.player_counter = 0
        self.game_state = self.GS_WAITING_TO_START
        self.round_num = 0
        self.num_rounds = 3

    def get_players_in_turn_order(self):
        ordered_list = self.get_sorted_players()
        team1_list = [x for x in ordered_list if x.team == Saladbowl_player.TEAM_BLUE]
        team2_list = [x for x in ordered_list if x.team == Saladbowl_player.TEAM_RED]
        return [team1_list, team2_list]

    def get_sorted_players(self):
        """ --------------------------------------------------
        returns list of Saladbowl_players in their player order
        """
        return sorted([x for _,x in self.players_by_username.items()])

    def get_sorted_player_names(self):
        return [x.username for x in self.get_sorted_players()]

    def increase_round(self):
        if self.round_num == self.num_rounds:
            return False
        self.round_num += 1
        return True

    def to_dic(self):
        players_dict = {}
        for k,x in self.players_by_username.items():
            players_dict[k] = {'username' : x.username,
                               'submitted_words' : x.submitted_words,
                               'team' : x.team}
        print ("PLAYERS DICT: " + str(players_dict))
        return {
            "room_id": self.room_id,
            #"players": [x.username for x in self.get_sorted_players()],
            #"player_teams": [x.team for x in self.get_sorted_players()],
            "ordered_players": self.get_sorted_player_names(),
            "word_list": self.word_list,
            "game_state": self.game_state,
            "round_num": self.round_num,
            "players": players_dict,
            "next_color": self.get_next_color(),
            #"test" : {'user1': {'team':'user1_team', 'status': 'user1_status'},
            #          'user2': {'tea':'user2_team', 'status':'user2_status'}},
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
            tmp_player.team = self.get_next_color()
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

    def remove_player(self, username):
        self.players_by_username.pop(username)


    def get_next_color(self):
        count_blue = [x.team for _,x in self.players_by_username.items()].count(Saladbowl_player.TEAM_BLUE)
        if count_blue > len(self.players_by_username) / 2:
            return Saladbowl_player.TEAM_RED
        return Saladbowl_player.TEAM_BLUE
