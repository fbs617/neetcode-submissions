class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            # Conversion logic 
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False










        # left_row = 0
        # left_col = 0
        # right_row = len(matrix) - 1
        # right_col = len(matrix[right_row]) - 1

        # print(right_row, right_col)
        # while right_row >= left_row and right_col >= left_col:
        #     mid = (((right_row + left_row) // 2), ((right_col + left_col) // 2))
        #     if matrix[mid[0]][mid[1]] == target:
        #         return True
        #     elif matrix[mid[0]][mid[1]] < target:
        #         if left_col > 0:
        #             left_row = mid[0]
        #             left_col = mid[1] - 1
        #         else:
        #             left_row = mid[0] - 1
        #             left_col = mid[1] + len(matrix[left_row]) - 1
        #     else:
        #         if right_col > 0:
        #             right_row = mid[0]
        #             right_col = mid[1] - 1
        #         else:
        #             right_row = mid[0] - 1
        #             right_col = mid[1] + len(matrix[right_row]) - 1
        #     print(right_row, right_col)
        # return False