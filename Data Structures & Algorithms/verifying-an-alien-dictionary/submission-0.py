class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordMap = {}
        for i in range(len(order)):
            wordMap[order[i]] = i
        
        i = 0
        while i+1 < len(words):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if wordMap[word1[j]] > wordMap[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
            i += 1
            
        return True