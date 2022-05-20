import random
import numpy as np

"""
This Python program is to simulate the card drawing process
"""
def main():
    X = 1000  # times of simulation
    n = 400  # number of distinct cards
    m = 6  # number of cards in one pack
    print(X,"times simulation,",n, "cards, packs of", m, ", average Number of packs =", collect_card(X, n, m))


# Simulate the card drawing process
#
# X: times of simulation
# n: number of distinct cards
# m: number of cards in one pack
def collect_card(X, n, m):
    cost = [0]*X  # store simulation result in a list
    for i in range(X):
        card_set = set([i for i in range(0, n)])  # checklist
        while True:
            # collect number of m of cards
            draw = random.sample(range(0, n), m)
            cost[i] += m
            card_set = card_set - set(draw)
            if len(card_set) == 0:  # all the types are collected
                break
        if i % (X/10) == 0:
            print(str(i/X*100) + "% finished")

    return sum(cost)/X/m

if __name__ == "__main__":
    main()
