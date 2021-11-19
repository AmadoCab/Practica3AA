class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                for val in row:
                    if val == target:
                        return True
                    else:
                        pass
            else:
                pass
        return False

# rehacer luego #
