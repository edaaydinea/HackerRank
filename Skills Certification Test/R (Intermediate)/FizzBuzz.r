#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

# Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:
# - If i is a multiple of both 3 and 5, print FizzBuzz.
# - If i is a multiple of 3 (but not 5), print Fizz.
# - If i is a multiple of 5 (but not 3), print Buzz.
# - If i is not a multiple of 3 or 5, print the value of i.

fizzBuzz <- function(n) {
    # Write your code here

    for (i in 1:n) {
        if (i %% 3 == 0 && i %% 5 == 0) {
            print("FizzBuzz")
        } else if (i %% 3 == 0) {
            print("Fizz")
        } else if (i %% 5 == 0) {
            print("Buzz")
        } else {
            print(i)
        }
    }
}

stdin <- file('stdin')
open(stdin)

n <- as.integer(trimws(readLines(stdin, n = 1, warn = FALSE), which = "both"))

fizzBuzz(n)

close(stdin)
