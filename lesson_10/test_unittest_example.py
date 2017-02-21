import unittest
from lesson_10.doctest_example import square


class TestSquare(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(-1), 1)

    def test_square_false(self):
        # self.assertEqual(square(7), 47)
        pass


class TestSquare2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_xyz1(self):
        print('test_xyz1')

    def test_xyz2(self):
        print('test_xyz2')
        self.assertRaises(ValueError, lambda: [1, 2].index(5))
        # self.assertEquals(1, [1, 2].index(5))


if __name__ == '__main__':
    unittest.main()