import unittest

# Here's our "unit".


def IsOdd(n):
    if n % 2 != 0:
        return True
    else:
        return False

# Here's our "unit tests".


class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
