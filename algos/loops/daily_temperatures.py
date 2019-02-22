import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            daily_temp([73, 74, 75, 71, 69, 72, 76, 73]),
            [1,1,4,2,1,1,0,0]
        )

def daily_temp(T):
    temperatures = T
    stack = []
    result = [0]*len(temperatures)
    for i in range(len(temperatures)):
        while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
            # print('here: ', end="")
            # print(i)
            # print('temperatures[stack[-1]]: ', end='')
            # print(temperatures[stack[-1]])
            j = stack.pop()
            result[j] = i-j
        stack.append(i)
        # print(stack)
        # print(stack[-1])
    return result

if __name__ == "__main__":
    unittest.main()

#bruteforce
#def daily_temp(T):
    # i = 0
    # result = [0] * len(T)
    # count = 0

    # while i < len(T):
    #     for j in range(i+1, len(T)):
    #         count += 1
    #         if T[i] < T[j]:
    #             result[i] = count
    #             break
    #     i+=1
    #     count = 0
    # return result

print(daily_temp([73, 74, 75, 71, 69, 72, 76, 73]))