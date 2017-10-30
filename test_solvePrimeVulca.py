import unittest
from main import SolvePrimeVulca

class TestSolvePrimeVulca(unittest.TestCase):

    def testIsPrime13(self):
        self.assertEqual(True, SolvePrimeVulca.isPrime(13))
        self.assertEqual(False, SolvePrimeVulca.isPrime(10))
        self.assertEqual(False, SolvePrimeVulca.isPrime(1))

    def testMatrice1_1(self):
        self.assertEqual(0, SolvePrimeVulca.solve(["1"]))
        self.assertEqual(1, SolvePrimeVulca.solve(["13"]))
        self.assertEqual(0, SolvePrimeVulca.solve(["12"]))

    def testMatrice2_1(self):
        self.assertEqual(1, SolvePrimeVulca.solve(["1 1"]))
        self.assertEqual(0, SolvePrimeVulca.solve(["9 10"]))
        self.assertEqual(2, SolvePrimeVulca.solve(["9 11"]))
        self.assertEqual(2, SolvePrimeVulca.solve(["7 9"]))

    def testMatrice3_1(self):
        self.assertEqual(3, SolvePrimeVulca.solve(["3 2 3"]))

    def testMatrice4_1(self):
        self.assertEqual(1, SolvePrimeVulca.solve(["1 1 1 1"]))
        self.assertEqual(0, SolvePrimeVulca.solve(["4 4 4 4"]))

    def testMatrice1_2(self):
        self.assertEqual(1, SolvePrimeVulca.solve(["1", "1"]))

    def testMatrice2_2(self):
        self.assertEqual(3, SolvePrimeVulca.solve(["1 3", "1 3"]))
        self.assertEqual(6, SolvePrimeVulca.solve(["2 3", "1 7"]))

    def testMatrice4_4(self):
        self.assertEqual(1, SolvePrimeVulca.solve(["0 0 0 0", "0 0 0 0", "0 2 0 0", "0 0 0 0"]))

    def testMatrice6_6(self):
        self.assertEqual(78, SolvePrimeVulca.solve(["3 1 7 3 3 3", "9 9 5 6 3 9", "1 1 8 1 4 2", "1 3 6 3 7 3 ", "3 4 9 1 9 9", "3 7 9 3 7 9"]))

if __name__ == '__main__':
    unittest.main()