import time
import random
import sys


def yahtzee_counter(rolls):
    counter = {}
    for roll in rolls:
        counter.setdefault(roll, 0)
        counter[roll] += roll
    else:
        counter[roll] = roll
    return max(counter.values())

def list_generator(length, low=1, high=10):
    bigun = []
    for i in range(0, length):
        bigun.append(random.randint(low, high))
    return bigun

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        start = time.time()
        print(yahtzee_counter([1, 2, 3, 4, 5, 5, 5, 6, 6]))
        end = time.time()
        print(end - start)
    elif len(args) == 2:
        bigboi = list_generator(int(args[1]))
        print(bigboi)
        start = time.time()
        print(yahtzee_counter(bigboi))
        end = time.time()
        print(end - start)
    else:
        bigboi = list_generator(int(args[3]), int(args[1]), int(args[2]))
        print(bigboi)
        start = time.time()
        print(yahtzee_counter(bigboi))
        end = time.time()
        print(end - start)