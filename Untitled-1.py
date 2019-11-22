import time


def yahtzee_counter(rolls):
    counter = {}
    for roll in rolls:
        if roll in counterkeys:
            counter[roll] += roll
        else:
            counter[roll] = roll
    return max(counter.values)

print(yahtzee_counter([1, 2, 3, 4, 5, 5, 5, 6, 6]))
