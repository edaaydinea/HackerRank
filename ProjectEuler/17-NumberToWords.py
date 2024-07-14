# The numbers 1 to 5 written out in words are one, two, three, four, five
# First character of each word will be capital letter for example: 104382426112 is One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty Six Thousand One Hundred Twelve

# Input Format
# The first line contains an integer T, i.e., number of test cases.
# Next T lines will contain an integer N.

# Constraints
# 1 <= T <= 100
# 1 <= N <= 10^12

# Output Format
# Print the values corresponding to each test case.

# Sample Input
# 2
# 10
# 17

# Sample Output
# Ten
# Seventeen

# Explanation
# For N = 10, we have "Ten".
# For N = 17, we have "Seventeen".

# Solution:
# 1. Create a dictionary with numbers as keys and their corresponding words as values.
# 2. Create a function that converts a number to words.
# 3. Iterate through the input numbers and print the corresponding words.

def number_to_words(n):
    words = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
        80: 'Eighty', 90: 'Ninety'
    }
    if n in words:
        return words[n]
    if n < 100:
        return words[n // 10 * 10] + ' ' + words[n % 10]
    if n < 1000:
        return words[n // 100] + ' Hundred ' + number_to_words(n % 100)
    for i, j in enumerate(('Thousand', 'Million', 'Billion'), 1):
        if n < 1000 ** (i + 1):
            return number_to_words(n // 1000 ** i) + ' ' + j + ' ' + number_to_words(n % 1000 ** i)
        
for _ in range(int(input())):
    print(number_to_words(int(input())))
    