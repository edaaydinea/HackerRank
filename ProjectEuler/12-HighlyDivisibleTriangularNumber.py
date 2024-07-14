# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...    

# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over n divisors?

# Input Format
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

# Output Format
# The value of the first triangle number to have over N divisors.

# Constraints
# 1 <= T <= 10
# 1 <= N <= 1000

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

prime = [2, 3, 5, 7, 11, 13, 17, 19]
def numFavors(n):
    pf = dict()
    for num in prime:
        if n%num == 0:
            pf[num] = 0
            while n%num == 0: 
                n = n//num
                pf[num] += 1
        if n == 1: break
    if n != 1:
        k = prime[-1] + 2
        while n != 1:
            if isPrime(k):
                prime.append(k)
                if n%k == 0:
                    pf[k] = 0
                    while n%k == 0:
                        n = n//k
                        pf[k] += 1
            k += 2
    numOfFav = 1
    for v in pf.values():
        numOfFav *= (v+1)
    return numOfFav
    
minNumFav = {1:1, 2:3, 4:6, 6:28} # number_of_favors : smallest_number_with_this_value

t = int(input())
for _ in range(t):
    N = int(input())
    if N < max(minNumFav):
        for d in minNumFav:
            if d > N:
                print(minNumFav[d])
                break
    else:
        number = 3
        plus = 3
        while True:
            fav = numFavors(number)
            if not fav in minNumFav: minNumFav[fav] = number
            if fav > N: break
            number += plus
            plus += 1
        print(number)