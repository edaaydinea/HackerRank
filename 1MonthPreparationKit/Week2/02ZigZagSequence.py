"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given an array of n distinct integers, transform the array into a zig zag sequence by permuting the array elements.
A sequence will be called a zig zag sequence if the first k elements are in increasing order and the last n-k elements are in decreasing order, where k = (n+1)/2.
You need to find the lexicographically smallest zig zag sequence.

Example

a = [1, 2, 3, 4, 5]

After permuting the array, a becomes [1, 5, 2, 4, 3]. This is a zig zag sequence.
Debug the given function findZigZagSequence to return the lexicographically smallest zig zag sequence.

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.

Zig Zag 

Here are the steps to find the lexicographically smallest zig zag sequence: a = [1, 2, 3, 4, 5]. a' = [1, 5, 2, 4, 3].

1. Sort the array. a = [1, 2, 3, 4, 5].
2. Identify the middle element of the array. 
    For the array a, the middle element is at index [(5+1)/2] = 3. In this case, the middle element is 3, which is the second element of the array.
3. Rearrange the array:
    - Place the first half of the sorted array in the beginning. [1,2]
    - Place the middle element in the middle position. 3
    - Place the second half of the sorted array in reverse order after the middle element. [5,4]

Combining all steps:
[1,2] + [3] + [5,4] = [1,2,3,5,4]

This is not the final zig-zag sequence. The final step is to ensure that the middle element acts as a peak in the sequence.

For a clearer zig zag sequence, we can swap 2 and 5 to achieve the correct pattern:
[1,5,2,4,3]

In this final sequence:
- 1<5
- 5>2
- 2<4
- 4>3

This pattern satisfies the zig zag sequence condition, where each element alternates between being greater and less than its neighbors.
"""

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2) #Changed from (n+1)/2 to (n-1)/2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2 #Changed from n-1 to n-2
    
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 #Changed from ed+1 to ed-1
    
    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)



