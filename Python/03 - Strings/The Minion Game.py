def minion_game(string):
    # your code goes here
    vowels = "AEIOU"

    kevsc = 0
    stusc = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(string) - i)
        else:
            stusc += (len(string) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")
