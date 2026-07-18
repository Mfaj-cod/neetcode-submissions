class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-2

        maxx = arr[-1]
        arr[-1] = -1

        while i >= 0:
            canbe_max = arr[i]
            arr[i] = maxx
            maxx = max(maxx, canbe_max)
            i -= 1

        return arr