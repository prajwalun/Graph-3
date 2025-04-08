# findCelebrity:
# - Check each person to see if they could be a celebrity.
# - A celebrity knows no one and is known by everyone else.
# - Use nested loops to verify the conditions for each person.

# TC: O(n^2) due to nested checks with knows(i, j).
# SC: O(n) for storing possible celebrities.


class Solution:
    def findCelebrity(self, n: int) -> int:
        
        isCelebrity = [True] * n
        for i in range(n):
            if isCelebrity[i]:
                for j in range(n):
                    if j != i and (knows(i, j) or not knows(j, i)):
                        isCelebrity[i] = False
                        break
                if isCelebrity[i]:
                    return i
        return -1