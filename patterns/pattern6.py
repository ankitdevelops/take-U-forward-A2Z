# Question: https://www.codingninjas.com/codestudio/problems/reverse-number-triangle_6581889?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems


def func(n):
    for i in range(0, n + 1):
        for j in range(1, n - i + 1):
            print(j, end=" ")
        print("", end="\n")


func(5)
