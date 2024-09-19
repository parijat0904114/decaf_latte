class Driver(object):
    def prime(self, n):
        """
        Generates prime numbers using the Sieve of Eratosthenes algorithm.

        This function implements a Pythonic version of the Sieve of Eratosthenes, an efficient algorithm 
        for finding all prime numbers up to a specified limit.

        Args:
            n (int): The upper limit (inclusive) for generating prime numbers. 
                    The function will return all prime numbers from 2 to n.

        Returns:
            list: A list of prime numbers from 2 up to n. If n is less than 2, an empty list is returned.

        Examples:
            >>> sieve = Driver()
            >>> sieve.prime(10)
            [2, 3, 5, 7]

            >>> sieve.prime(1)
            []
        """

        prime_stack = [True] * (n+1)
        prime_stack[0] = prime_stack[1] = False

        p = 2

        while (p*p <= n):
            if prime_stack[p] == True:
                for i in range(p*p, n+1, p if p == 2 else 2*p):
                    prime_stack[i] = False
            p += 1 if p == 2 else 2

        return ([i for i, b in enumerate(prime_stack) if b])


d = Driver()
print(d.prime(10))
print(d.prime(1))
