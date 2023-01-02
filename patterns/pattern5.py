# Question: https://www.codingninjas.com/codestudio/problems/seeding_6581892?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems&leftPanelTab=1


def func(n):
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            print("*", end=" ")
        print("", end="\n")


func(5)
