from saladbowl import saladbowl_sockets, saladbowl_game, saladbowl_player
import unittest

USERNAMES=['fred','sally','jack','amy','drew','shrek']
IDS=[str(x) for x in list(range(0,len(USERNAMES)))]
ROOM_ID='ABCD'

class TestSaladbowl(unittest.TestCase):

    def create_game(self):
        game = saladbowl_game(room_id=ROOM_ID,
                              num_words_per_player=3)
        for id_, user in zip(USERNAMES, IDS):
            game.add_id_to_player(user, id_)
        return game
    
    def test_(self):
        self.assertEqual(4,4)
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
