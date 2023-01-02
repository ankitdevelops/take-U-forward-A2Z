# Question: https://www.codingninjas.com/codestudio/problems/star-triangle_6573671?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_patternproblems


def func(n):
    for i in range(n):
        # space
        for j in range(n - i - 1):
            print(" ", end=" ")
        # star
        for j in range(2 * i + 1):
            print("*", end=" ")
        # space
        for j in range(n - i - 1):
            print(" ", end=" ")
        print("", end="\n")


func(5)
