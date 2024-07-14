# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, <= N, produces the longest chain? If many possible such numbers are there print the maximum one.

# Note: Once the chain starts the terms are allowed to go above N.

def calculate_collatz_lengths(max_n):
    # Initialize an array to store the lengths of the Collatz sequences
    step = [1] * (max_n + 1)

    for ind in range(2, max_n + 1):
        cnt = 0
        cur = ind
        while cur >= ind:
            if cur % 2 == 0:
                cur = cur // 2
            else:
                cur = (3 * cur) + 1
            cnt += 1
        step[ind] = cnt + step[cur]

    return step

def find_longest_collatz_numbers(max_n, step):
    # Initialize an array to store the number producing the longest Collatz sequence up to each index
    res = [1] * (max_n + 1)
    mxnum = 1
    mxval = 1

    for i in range(2, max_n + 1):
        if step[i] >= mxval:
            mxval = step[i]
            mxnum = i
        res[i] = mxnum

    return res

def main():
    # Read input
    inps = [int(input()) for _ in range(int(input()))]
    max_n = max(inps)

    # Calculate Collatz lengths up to max_n
    step = calculate_collatz_lengths(max_n)

    # Find the longest Collatz numbers up to max_n
    res = find_longest_collatz_numbers(max_n, step)

    # Output results for each input
    for inp in inps:
        print(res[inp])

if __name__ == "__main__":
    main()
