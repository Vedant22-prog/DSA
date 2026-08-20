from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        hand.sort()
        for card in hand:
            if count[card] == 0:
                continue
            for i in range(groupSize):
                if count[card + i] == 0:
                    return False
                count[card + i] -= 1
        return True