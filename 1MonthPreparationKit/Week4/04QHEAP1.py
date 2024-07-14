# This question is designed to help you get a better understanding of basic heap operations.
# There 3 types of query:
# 1. "1 v" - Add an element v to the heap.
# 2. "2 v" - Delete the element v from the heap.
# 3. "3" - Print the minimum of all the elements in the heap.

#Note: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only one element will be deleted from the heap.

# Input Format
# The first line contains the number of queries, Q.
# Each of the next Q lines contains a single query of any one of the 3 above mentioned types.

# Output Format
# For each query of type 3, print the minimum element in the heap.

# Constraints
# 1 <= Q <= 10^5
# -10^9 <= v <= 10^9

# Sample Input
# 5             Q = 5
# 1 4           Add 4 to the heap
# 1 9           Add 9 to the heap
# 3             Print the minimum element
# 2 4           Delete 4 from the heap
# 3             Print the minimum element

# Sample Output
# 4
# 9

# Solution:
import heapq

def QHEAP1(queries):
    heap = []
    present = set()
    result = []
    
    for query in queries:
        if query[0] == 1:
            heapq.heappush(heap, query[1])
            present.add(query[1])
        elif query[0] == 2:
            if query[1] in present:
                present.remove(query[1])
        elif query[0] == 3:
            while heap[0] not in present:
                heapq.heappop(heap)
            result.append(heap[0])
    
    return result

if __name__ == '__main__':
    Q = int(input().strip())
    queries = []
    
    for _ in range(Q):
        queries.append(list(map(int, input().rstrip().split())))
    
    result = QHEAP1(queries)
    
    for res in result:
        print(res)

    

