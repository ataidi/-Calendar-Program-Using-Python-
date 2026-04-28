n = 5

for i in range(1, n + 1):

    # espaces
    print(" " * (n - i), end="")

    # nombres croissants
    for j in range(1, i + 1):
        print(j, end="")

    # nombres décroissants
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()