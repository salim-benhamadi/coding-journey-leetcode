# Dictionary counting solution
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_count = {'R': 0, 'L': 0, 'D': 0, 'U': 0}
        for move in moves:
            move_count[move] += 1
        return move_count["U"] == move_count["D"] and move_count["R"] == move_count["L"]

# Time Complexity: O(n), where n is the length of moves string
# Space Complexity: O(1), dictionary has fixed size of 4 keys


# String count solution
class Solution2:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')

# Time Complexity: O(n), where n is the length of moves string (4 passes)
# Space Complexity: O(1), no extra space needed