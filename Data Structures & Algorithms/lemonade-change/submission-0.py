class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        inhand = {5:0, 10:0, 20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                inhand[5] += 1
            elif bills[i] == 10:
                if inhand[5] <= 0:
                    return False
                inhand[5] -= 1
                inhand[10] += 1
            elif bills[i] == 20:
                if inhand[10] <= 0 and inhand[5] < 3:
                    return False
                elif inhand[10] > 0 and inhand[5] > 0:
                    inhand[10] -= 1
                    inhand[5] -= 1
                elif inhand[5] >= 3:
                    inhand[5] -= 3
                else:
                    return False

        return True