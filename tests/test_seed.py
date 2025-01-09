import unittest
from tarots import Seed


class TestSeed(unittest.TestCase):
    def test_comparison(self):
        self.assertTrue(Seed.spades < Seed.coins)
        self.assertTrue(Seed.spades <= Seed.coins)
        self.assertTrue(Seed.coins > Seed.spades)
        self.assertTrue(Seed.coins >= Seed.spades)
        self.assertTrue(Seed.spades == Seed.spades)
        self.assertTrue(Seed.spades != Seed.coins)

    def test_value_to_notation(self):
        self.assertEqual(Seed.value_to_notation(1), 's')
        self.assertEqual(Seed.value_to_notation(0), 't')
        self.assertEqual(Seed.value_to_notation(2), 'o')
        self.assertEqual(Seed.value_to_notation(3), 'c')
        self.assertEqual(Seed.value_to_notation(4), 'u')
        self.assertEqual(Seed.value_to_notation(5), 'Unknown')

    def test_from_notation(self):
        self.assertEqual(Seed.from_notation('s'), Seed.spades)
        self.assertEqual(Seed.from_notation('t'), Seed.tarots)
        self.assertEqual(Seed.from_notation('o'), Seed.coins)
        self.assertEqual(Seed.from_notation('c'), Seed.clubs)
        self.assertEqual(Seed.from_notation('u'), Seed.cups)
        with self.assertRaises(ValueError):
            Seed.from_notation('x')

    def test_str(self):
        self.assertEqual(str(Seed.spades), 'spades')
        self.assertEqual(str(Seed.tarots), 'tarots')

    def test_repr(self):
        self.assertEqual(repr(Seed.spades), 'spades')
        self.assertEqual(repr(Seed.tarots), 'tarots')

def main():
    with open('test_seed_log.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)

if __name__ == '__main__':
    main()