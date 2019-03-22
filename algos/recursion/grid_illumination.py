import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            solve([[0,0], [0,4]], [[0,4],[0,1],[1,4]]),
            [1, 1, 0]
        ),
    def test2(self):
        self.assertEqual(
            solve([[0,0], [4,4]], [[1,1],[1,1]]),
            [1,1]
        ),
    def test3(self):
        self.assertEqual(
            solve([[0,0], [1,0]], [[1,1],[1,1]]),
            [1,0]
        ),
    def test4(self):
        self.assertEqual(
            solve([[0,0],[0,1],[0,4]],[[0,0],[0,1],[0,2]]),
            [1,1,1]
        ),
    def test5(self):
        self.assertEqual(
            solve([[3,9],[3,6],[8,3],[5,3],[8,1],[1,3],[5,9],[4,2]], [[1,9],[4,9],[7,1],[6,9]]),
            [1,1,1,1]
        ),
    def test6(self):
        self.assertEqual(
            solve([[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]],[[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]),
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1]
        )

def solve(lamps, queries):
    lamp_set = set()
    horizontal_moves = {}
    vertical_moves = {}
    right_diag_moves = {}
    left_diag_moves = {}
    result = []

    for lamp in lamps:
        lamp_set.add((lamp[0], lamp[1]))
        if lamp[0] not in horizontal_moves:
            horizontal_moves[lamp[0]] = 1
        else:
            horizontal_moves[lamp[0]] += 1
        
        if lamp[1] not in vertical_moves:
            vertical_moves[lamp[1]] = 1
        else:
            vertical_moves[lamp[1]] += 1
        
        if lamp[0] + lamp[1] not in right_diag_moves:
            right_diag_moves[lamp[0] + lamp[1]] = 1
        else:
            right_diag_moves[lamp[0] + lamp[1]] += 1
        
        if lamp[0] - lamp[1] not in left_diag_moves:
            left_diag_moves[lamp[0] - lamp[1]] = 1
        else:
            left_diag_moves[lamp[0] - lamp[1]] += 1

    for query in queries:
        #check each query
        if check_query(query, horizontal_moves, vertical_moves, right_diag_moves, left_diag_moves):
            result.append(1)
        else:
            result.append(0)

        #check_adj / update maps 
        remove_lamps(query, lamp_set, horizontal_moves, vertical_moves, right_diag_moves, left_diag_moves)
    
    return result
    
def check_query(query, horizontal_moves, vertical_moves, right_diag_moves, left_diag_moves):
    if query[0] in horizontal_moves or query[1] in vertical_moves or (query[0] + query[1]) in right_diag_moves or (query[0] - query[1]) in left_diag_moves:
        return True
  
    return False

def check_adj(query, lamp_set):
    x = query[0]
    y = query[1]

    result = []

    if (x-1, y-1) in lamp_set:
        result.append((x-1,y-1))
    if (x-1, y) in lamp_set:
        result.append((x-1, y))
    if (x-1, y+1) in lamp_set:
        result.append((x-1, y+1))
    if (x, y-1) in lamp_set:
        result.append((x,y-1))
    if (x, y) in lamp_set:
        result.append((x, y))
    if (x, y+1) in lamp_set:
        result.append((x, y+1))
    if (x+1, y-1) in lamp_set:
        result.append((x+1,y-1))
    if (x+1, y) in lamp_set:
        result.append((x+1, y))
    if (x+1, y+1) in lamp_set:
        result.append((x+1, y+1))

    return result
        

def remove_lamps(query, lamp_set, horizontal_moves, vertical_moves, right_diag_moves, left_diag_moves) :
    to_remove = check_adj(query, lamp_set)

    while to_remove:
        cur = to_remove.pop()
        
        if cur[0] in horizontal_moves:
            horizontal_moves[cur[0]] -= 1
            if horizontal_moves[cur[0]] == 0:
                del horizontal_moves[cur[0]]

        if cur[1] in vertical_moves:
            vertical_moves[cur[1]] -= 1
            if vertical_moves[cur[1]] == 0:
                del vertical_moves[cur[1]]

        if cur[0] + cur[1] in right_diag_moves:
            right_diag_moves[cur[0] + cur[1]] -= 1
            if right_diag_moves[cur[0] + cur[1]] == 0:
                del right_diag_moves[cur[0] + cur[1]]
        
        if cur[0] - cur[1] in left_diag_moves:
            left_diag_moves[cur[0] - cur[1]] -= 1
            if left_diag_moves[cur[0] - cur[1]] == 0:
                del left_diag_moves[cur[0] - cur[1]]

        lamp_set.remove(cur)

if __name__ == "__main__":
    unittest.main()

