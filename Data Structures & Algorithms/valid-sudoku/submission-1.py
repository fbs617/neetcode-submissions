class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        square = 0

        for i in range(9):
            for j in range(9): 

                value = board[i][j]

                if value == ".":
                    continue

                if i < 3:
                    square = 0
                elif i >= 3 and i < 6:
                    square = 3
                else:
                    square = 6

                if j < 3:
                    square += 0
                elif j >= 3 and j < 6:
                    square += 1
                else:
                    square += 2

                if (value in rows[i]) or (value in cols[j]) or (value in squares[square]):
                    return False
                else:
                    rows[i].add(value)
                    cols[j].add(value)
                    squares[square].add(value)
                
        return True
        