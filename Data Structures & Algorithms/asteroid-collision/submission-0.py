class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s_pos = [i for i in asteroids if i < 0]
        s_neg = [i for i in asteroids if i >= 0]

        while s_pos and s_neg:
            if abs(s_pos[-1]) > abs(s_neg[-1]):
                s_neg.pop()
            elif abs(s_pos[-1]) < abs(s_neg[-1]):
                s_pos.pop()
            else:
                s_pos.pop()
                s_neg.pop()
        
        return s_pos if s_pos else s_neg