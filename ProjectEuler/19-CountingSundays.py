# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Input Format
# First line contains T, the number of testcases. For each testcase will contain two lines:
# Y1 M1 D1 on first line denoting starting date.
# Y2 M2 D2 on second line denoting ending date.

# Constraints
# 1 <= T <= 100
# 1900 <= Y1 <= 10^16
# Y1 <= Y2 <= (Y1 + 1000)
# 1 <= M1, M2 <= 12
# 1 <= D1, D2 <= 31

# Output Format
# For each testcase, print the required answer in a newline.

# Sample Input
# 2
# 1900 1 1
# 1910 1 1
# 2000 1 1
# 2020 1 1

# Sample Output
# 18
# 35

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 31

def calculate_day_of_week(year, month, day):
    # Zeller's Congruence Algorithm to find the day of the week
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = day + 13 * (month + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    return f % 7

def count_sundays_on_first(y1, m1, d1, y2, m2, d2):
    sundays_count = 0
    
    # Start from the first of the month
    if d1 != 1:
        m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1

    # Traverse each month from y1/m1 to y2/m2
    year = y1
    month = m1
    while year < y2 or (year == y2 and month <= m2):
        if calculate_day_of_week(year, month, 1) == 1:  # Monday is 1, so Sunday is 0
            sundays_count += 1
        month += 1
        if month > 12:
            month = 1
            year += 1

    return sundays_count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        Y1, M1, D1 = int(data[index]), int(data[index + 1]), int(data[index + 2])
        Y2, M2, D2 = int(data[index + 3]), int(data[index + 4]), int(data[index + 5])
        results.append(count_sundays_on_first(Y1, M1, D1, Y2, M2, D2))
        index += 6
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

