# Disjoint Set: A "take me to your leader" data structure
# Whenever a union occurs, we point to the nodes' leaders' rank and compare the two
# By doing so we can also assign all of the lower ranking leader's "lackeys" to the higher ranking leader
# aka "Path Compression"
# We can check if a node is directed to the correct leader by calling on the find_set function

class Node:
    def __init__(self, data):
        self.rank = 0
        self.data = data
        self.leader = self
        self.lackeys = [self]

class DisjointSet():
    def __init__(self):
        self.sets = {}

    def make_set(self, data):
        if data in self.sets:
            print("this set already exists")
        else:
            new_set = Node(data)
            self.sets[data] = new_set

    def path_compression(self, main, subordinate):
        print(main.leader.data)
        while subordinate.lackeys:
            cur = subordinate.lackeys.pop()
            cur.leader = main
            main.leader.lackeys.append(cur)

    def union(self, main, subordinate):
        sets = self.sets
        main = sets[main]
        subordinate = sets[subordinate]
        
        if main.leader.rank > subordinate.leader.rank:
            self.path_compression(main.leader, subordinate.leader)
        elif subordinate.leader.rank > main.leader.rank:
            self.path_compression(subordinate.leader, main.leader)
        elif main.leader.rank == subordinate.leader.rank:
            main.leader.rank += 1
            self.path_compression(main.leader, subordinate.leader)

    def find_set(self, main):
        sets = self.sets
        if main not in sets:
            print("Set does not exist")
        else:
            return sets[main].leader

#disjoint_set = DisjointSet()
#disjoint_set.make_set('A')
#disjoint_set.make_set('B')
#disjoint_set.make_set('C')
#disjoint_set.make_set('D')
#disjoint_set.make_set('E')
#disjoint_set.union('A', 'B')
#print(disjoint_set.sets['A'].rank)
#disjoint_set.union('C', 'D')
#print(disjoint_set.sets['D'].leader.data)
#disjoint_set.union('D', 'E')
#print(disjoint_set.sets['C'].lackeys)
#print(disjoint_set.sets['C'].rank)
#disjoint_set.union('A', 'D')
#print(disjoint_set.find_set('C'))
