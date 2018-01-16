from saladbowl import saladbowl_sockets
import unittest

class TestSaladbowl(unittest.TestCase):
    def test_one(self):
        saladbowl_sockets.test1()
        self.assertEqual(4,4)
        


if __name__ == '__main__':
    unittest.main(verbosity=2)
