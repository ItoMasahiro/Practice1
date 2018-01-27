import random


def randlist(size,lower=0,upper=100):
    ranli = []
    for i in range(size):
        ranli.append(random.randint(lower, upper))
    return ranli


resli = randlist(10,upper=12,lower=10)
print(resli)
