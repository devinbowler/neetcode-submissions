class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        
        while hand:
            first = hand[0]
            for i in range(groupSize):
                target = first + i
                if target in hand:
                    hand.remove(target)
                else:
                    return False
            
        if len(hand) == 0:
            return True
        else:
            return False