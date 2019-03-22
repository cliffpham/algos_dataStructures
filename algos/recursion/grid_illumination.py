def solve(lamps, queries):
    lamps = lamps
    result = []

    for query in queries:
        if check_query(query, lamps):
            result.append(1)
        else:
            result.append(0)
        lamps = remove_lamps(query, lamps)
    
    return result
    
def check_query(query, lamps):
    # print('this is the lamps at check_query: ', end='')
    # print(query, lamps)
    for lamp in lamps:
        if check_illumination(query, lamp):
            return True
    
    return False


def check_illumination(query, lamp):
    # print('this is the query and lamp we are checking: ', end='')
    # print(query, lamp)
    x1 = query[0]
    y1 = query[1]
    x2 = lamp[0]
    y2 = lamp[1]

    if check_ver(y1, y2) or check_hor(x1, x2) or check_diag(x1, y1, x2, y2):
        return True
    
    return False

def check_ver(y1, y2):
    if y1 == y2:
        return True
    
    return False

def check_hor(x1, x2):
    if x1 == x2:
        return True
    
    return False

def check_diag(x1, y1, x2, y2):
    return abs(x1- x2) == abs(y1-y2)

def check_adj(x1, y1, x2, y2):
    return abs(x2 - x1) < 2 and abs(y2 - y1) < 2

def remove_lamps(query, lamps):
    copy = lamps[:]

    for lamp in copy:
        if check_adj(query[0], query[1], lamp[0], lamp[1]):
            # print(query, lamp)
            copy.remove(lamp)
            # print(copy)
            return remove_lamps(query, copy)

    return copy


lamps = [[0,0], [0,4]]
queries = [[0,4],[0,1],[1,4]]

lamps2 = [[0,0], [4,4]]
queries2 = [[1,1],[1,1]]

lamps3 = [[0,0], [1,0]]
queries3 = [[1,1],[1,1]]

lamps4 = [[0,0],[0,1],[0,4]]
queries4 = [[0,0],[0,1],[0,2]]

lamps5 = [[3,9],[3,6],[8,3],[5,3],[8,1],[1,3],[5,9],[4,2]]
queries5 = [[1,9],[4,9],[7,1],[6,9]]

lamps6 = [[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]]
queries6 = [[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]

print(solve(lamps, queries)) #[1,1,0]
print(solve(lamps2, queries2)) #[1,1]
print(solve(lamps3, queries3)) #[1,0]
# print(solve(lamps4, queries4)) #[1,1,1]
# print(solve(lamps5, queries5)) #[1,1,1,1]
# print(solve(lamps6, queries6)) #[1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1]


