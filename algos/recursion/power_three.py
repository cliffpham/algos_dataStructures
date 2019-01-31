import unittest

class test_power_three(unittest.TestCase):
    def test1(self):
        self.assertTrue(
            power_three(2187)
        )
    def test2(self):
        self.assertFalse(
            power_three(45)
        )
        


def power_three(n):
    if n == 0 :
       return False
    if n == 1:
        return True
    else:
        if n % 3 == 0:
            return power_three(n/3)
        else:
            return False

if __name__ == "__main__":
     unittest.main()   
  