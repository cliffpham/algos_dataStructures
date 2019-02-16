import unittest

class test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            min_index_sum(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]),
            ['Shogun', 'Tapioca Express', 'Burger King', 'KFC']
        )

def min_index_sum(list1, list2):
    initial_result = []
    final_result = []
    pref = float('inf')
   
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                initial_result.append((i,j))

    if len(initial_result) > 1:
        for i in initial_result:
            if sum(i) <= pref:
                pref = sum(i)
                final_result.append(list1[i[0]])
        return final_result

    
    r = initial_result[0][0]
    return [list1[r]]

  
if __name__ == "__main__":
    unittest.main()
