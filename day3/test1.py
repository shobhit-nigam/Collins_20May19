import unittest
class TestA(unittest.TestCase):
    def test_lstrip(self):
        self.assertEqual('hello '.lstrip(), ' hello ')
    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())


if __name__ == '__main__':
    unittest.main(argv = ['HEllo'], exit=False)    
