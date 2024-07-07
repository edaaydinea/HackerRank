# A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.
# A basic queue has the following operations:
#     Enqueue: add a new element to the end of the queue.
#     Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:
#     1 x: Enqueue element x into the end of the queue.
#     2: Dequeue the element at the front of the queue.
#     3: Print the element at the front of the queue.

# Function Description
# Complete the put, pop, and peek methods in the editor below. They must perform the actions as described above.

# Input Format
# The first line contains a single integer, q, the number of queries.
# Each of the next q lines contains a single query in the form described in the problem statement above. All queries start with an integer denoting the query type, but only query 1 is followed by an integer x.

# Constraints
#     1 <= q <= 10^5
#     1 <= type <= 3
#     1 <= x <= 10^9
#     It is guaranteed that a valid answer always exists for each query of type 3.

# Output Format
# For each query of type 3, print the value of the element at the front of the queue on a new line.

# Sample Input              Function:
# 10                        q = 10
# 1 42                      queries = [1, 42]
# 2                         queries = [2]
# 1 14                      queries = [1, 14]
# 3                         queries = [3]
# 1 28                      queries = [1, 28]
# 3                         queries = [3]
# 1 60                      queries = [1, 60]
# 1 78                      queries = [1, 78]
# 2                         queries = [2]
# 2                         queries = [2]


# Sample Output
# 14
# 14

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, x):
        self.stack1.append(x)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]

def process_queries(queries):
    queue = MyQueue()
    results = []
    
    for query in queries:
        query_type = query[0]
        if query_type == 1:
            x = query[1]
            queue.enqueue(x)
        elif query_type == 2:
            queue.dequeue()
        elif query_type == 3:
            front_element = queue.peek()
            results.append(front_element)
    
    return results

# Example usage:
if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    
    for _ in range(q):
        queries.append(list(map(int, input().strip().split())))
    
    results = process_queries(queries)
    
    for result in results:
        print(result)

