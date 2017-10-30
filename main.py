class SolvePrimeVulca():
    def __init__(self):
        pass

    @staticmethod
    def isPrime(_param):
        # make sure n is a positive integer
        n = abs(int(_param))

        # 0 and 1 are not primes
        if n < 2:
            return False

        # 2 is the only even prime number
        if n == 2:
            return True

            # all other even numbers are not primes
        if not n & 1:
            return False

        # range starts with 3 and only needs to go up
        # the square root of n for all odd numbers
        for x in range(3, int(n ** 0.5) + 1, 2):
            if n % x == 0:
                return False

        return True

    @staticmethod
    def addIfDistinct(add,tab):
        if int(add) not in tab:
            tab.append(int(add))

    @staticmethod
    def checkright(i, _param, tab):
        prev = ""
        for j in range(len(_param) - i):
            prev += str(_param[j + i])
            SolvePrimeVulca.addIfDistinct(prev,tab)

    @staticmethod
    def checkbottom(x, y,_param, tab):
        prev = ""
        for i in range(len(_param) -y):
            prev += _param[i+y][x]
            SolvePrimeVulca.addIfDistinct(prev, tab)

    @staticmethod
    def solve(_param, _main=""):
        whole = []
        for p in _param:
            whole.append(p.strip().split(" "))
        result = 0
        tab = []
        for y in range(len(whole)):
            for x in range(len(whole[y])):
                SolvePrimeVulca.checkright(x, whole[y], tab)
                SolvePrimeVulca.checkbottom(x, y, whole, tab)
        if _main == '__main__':
            print (tab)
        for t in tab:
            if SolvePrimeVulca.isPrime(t):
                result += 1

        return result

if __name__ == '__main__':
    print(SolvePrimeVulca.solve(["3 1 7 3 3 3","9 9 5 6 3 9","1 1 8 1 4 2","1 3 6 3 7 3 ","3 4 9 1 9 9","3 7 9 3 7 9"],__name__))
