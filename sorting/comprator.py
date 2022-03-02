from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    # def __repr__(self):
        
    def comparator(a, b):
        #Returns a negative integer, zero, or a positive integer as the first 
        # argument is less than, equal to, or greater than the second.
        if a.score < b.score:
            return 1
        elif a.score == b.score:
            # need to add sort logic by name
            if a.name < b.name:
                return -1
            elif a.name == b.name:
                return 0
            else:
                return 1
        else:
            return -1



n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)