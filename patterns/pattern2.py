# Question
# https://www.codingninjas.com/codestudio/problems/n-2-forest_6570178?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems


def func(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print("", end="\n")


func(5)
