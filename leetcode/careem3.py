# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.8.10
    moves = 0
    while True:
        total = 0
        count = 0 
        for i in range(0, len(A)-1):
            total += A[i]
            count +=1 
            if (total < 0) or (total + A[i+1] < 0):
                moves += 1
                expense = A.pop(i)
                A.append(expense)
                break
                    
        if count == len(A)-1: # Checked all the elements
            return moves

# print(solution([5,-2,-3,1]))
# print(solution([10,-10,-1,-1,10]))
# print(solution([-1,-1,-1,1,1,1,1]))
print(solution([2,-5,5]))
