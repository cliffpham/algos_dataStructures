import unittest

class Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(
        sieve_of_eratosthenes(10),
        4
        )


def sieve_of_eratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    count = 0
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
       
    for p in range(2, n): 
        if prime[p]: 
            count += 1 
    
    return count

#Optimized School Method
#def is_prime(n):
#    if n <= 1:
#        return False
#    if n <= 3:
#        return True
#    if n % 2 == 0 or n % 3 == 0:
#        return False
#
#    i = 5
#
#    while i * i <= n:
#        if n % i == 0 or n % (i+2) == 0:
#            return False
#    return True
#
##brute force
#def count_primes(n):
#    i = 0
#    count = 0
#
#    while i < n:
#        if is_prime(i):
#            count += 1
#        i += 1
#
#    return count
#
#School Method
#def is_prime(n):
#    if n <= 1:
#        return False
#    
#    for i in range(2, n):
#        if n % i == 0:
#            return False
#
#    return True

if __name__ == "__main__":
    unittest.main()
