from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for start in sorted(count.keys()):
            if count[start] == 0:
                continue

            freq = count[start]

            for card in range(start, start + groupSize):
                if count[card] < freq:
                    return False

                count[card] -= freq

        return True