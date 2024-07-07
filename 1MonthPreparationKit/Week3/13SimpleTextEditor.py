# Implement a simple text editor. The editor initially contains an empty string, S. Perform Q operations of the following 4 types:
# 1. append(W) - Append string W to the end of S.
# 2. delete(k) - Delete the last k characters of S.
# 3. print(k) - Print the kth character of S.
# 4. undo() - Undo the last (not previously undone) operation of type 1 or 2, reverting S to the state it was in prior to that operation.

# Example
# s = 'abcde'
# operations = [(1, 'f'), (2, 3), (3, 3), (4), (1, 'g'), (4)]

# Operation 1: Append 'f' to s -> s = 'abcdef'
# Operation 2: Delete last 3 characters of s -> s = 'abc'
# Operation 3: Print 3rd character of s -> 'c'
# Operation 4: Undo last operation 2 -> s = 'abcdef'
# Operation 1: Append 'g' to s -> s = 'abcdefg'
# Operation 4: Undo last operation 1 -> s = 'abcdef'

import os

def simple_text_editor(operations):
    S = ""
    history_stack = []
    
    output = []
    
    for operation in operations:
        if operation[0] == 1:  # Append(W)
            _, W = operation
            history_stack.append((1, len(W)))
            S += W
        elif operation[0] == 2:  # Delete(k)
            _, k = operation
            removed_string = S[-k:]
            history_stack.append((2, removed_string))
            S = S[:-k]
        elif operation[0] == 3:  # Print(k)
            _, k = operation
            output.append(S[k - 1])
        elif operation[0] == 4:  # Undo()
            last_operation = history_stack.pop()
            if last_operation[0] == 1:  # Undo Append(W)
                _, length_of_W = last_operation
                S = S[:-length_of_W]
            elif last_operation[0] == 2:  # Undo Delete(k)
                _, removed_string = last_operation
                S += removed_string
    
    return '\n'.join(output)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    q = int(input().strip())
    
    operations = []
    
    for _ in range(q):
        op = input().strip().split()
        if op[0] == '1':
            operations.append((1, op[1]))
        elif op[0] == '2':
            operations.append((2, int(op[1])))
        elif op[0] == '3':
            operations.append((3, int(op[1])))
        elif op[0] == '4':
            operations.append((4,))
    
    result = simple_text_editor(operations)
    
    fptr.write(result + '\n')
    
    fptr.close()
    
    


