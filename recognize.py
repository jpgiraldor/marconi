import random

def cheat(y0, y1, false_positives=0, false_negatives=0):
    matches = [i == j for (i, j) in zip(y0, y1)]

    for i in range(len(matches)):
        if matches[i]:
            if random.random() < false_negatives:
                matches[i] = False
        else:
            if random.random() < false_positives:
                matches[i] = True

    return matches
