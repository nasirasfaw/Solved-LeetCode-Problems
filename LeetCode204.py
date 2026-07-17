class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt

        prime = [True] * n
        if n > 0:
            prime[0] = False
        if n > 1:
            prime[1] = False

        for i in range(2, int(sqrt(n)) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False

        return sum(prime)
