import unittest

class test_add_one(unittest.TestCase):
    def test1_add_one(self):
        self.assertEqual(
            add_one([9,9,9]),
            [1,0,0,0]
        )
    def test2_add_one(self):
        self.assertEqual(
            add_one([1,2,3]),
            [1,2,4]
        )

def add_one(a):
    
    n = len(a) 
   
    # Add 1 to last digit and find carry 
    a[n-1] += 1
    carry = a[n-1]/10
    a[n-1] = a[n-1] % 10
   
    # Traverse from second last digit | loopbackwards (start, end, which way to increment)
    for i in range(n-2,-1,-1): 
        if (carry == 1): 
           a[i] += 1
           carry = a[i]/10
           a[i] = a[i] % 10
          
    # If carry is 1, add 1 at the beginning of the arr 
    if (carry == 1): 
      a.insert(0,1) 
  
    return a

if __name__ == "__main__":
    unittest.main()
