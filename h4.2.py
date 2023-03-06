import random
berries = [random.randint(1, 25) for i in range(0, int(input()))]
print(berries)

n = int(input()) - 1

print(berries[n - 1] + berries[n] + berries[n + 1])


