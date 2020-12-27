class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return None
        # initialize each row
        triangle = []
        for i in range(numRows):
            row = [0] * (i+1)
            triangle.append(row)

        # set value of top row, so we can calculate values of successive rows
        triangle[0][0] = 1

        # if numRows is 0, this loop wont run
        for i in range(1, numRows):
            # NOTE: number of elements in row is equal to row idx + 1
            num_vals = i + 1
            for j in range(num_vals):
                if j == 0:
                    triangle[i][j] = triangle[i-1][0]
                elif j == num_vals-1:
                    triangle[i][j] = triangle[i-1][num_vals-2]
                else:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

        return triangle
