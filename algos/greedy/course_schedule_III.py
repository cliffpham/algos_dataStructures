import heapq
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([[5,5],[4,6],[2,6]]),
            2
        ),
    def test2(self):
        self.assertEqual(
            solve([[100,200],[200,1300],[1000,1250],[2000,3200]]),
            3
        ),
    def test3(self):
        self.assertEqual(
            solve([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]),
            5
        )

#Greedy solution
def solve(courses):
    # sort courses by shortest deadline
    courses.sort(key=lambda x:x[1])
    pq = [] # courses to take
    accum = 0

    heapq.heappush(pq,0)
    for t,d in courses:

        # if a course duration + the minimum course duration is less than 0
        # the new course is now the first course to take
        # have the accumaltor and pq reflect the change
        if accum+t>d:
            if t+pq[0]<0:
                accum+=t+pq[0]
                heapq.heappushpop(pq,-t)

        # if the accum + current course duration is less than deadline
        # greedily add to courses to take  
        # have pq reflect change    
        else:
            accum+=t
            heapq.heappush(pq,-t)
    
    # -1 since we set course to take intially to 0
    return len(pq)-1

if __name__ == "__main__":
    unittest.main()

#DP solution - time limit exceeded

# def recur(courses, i, accum, cache):
#     ck = "%s:%s" % (i, accum)

#     if ck in cache:
#         return cache[ck]

#     if i >= len(courses):
#         return 0

#     l = recur(courses, i+1, accum, cache)

#     r = 0

#     if accum + courses[i][0] <= courses[i][1]:
#         r = recur(courses, i+1, accum + courses[i][0], cache) + 1
#     cache[ck] = max(l,r)
    
#     return max(l,r)

# def solve(courses):
#     return recur(courses, 0, 0, {})


