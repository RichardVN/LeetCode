"""                
NOTE: 2 key facts:
1. There are N + M - 1 diagonals in an N x M matrix
2. Diagonal values are grouped by sum of i + j indices
3. to SNAKE: reverse every other diagonal level, therefore check if divisible by 2

Approach:
    1. Traverse over each element in the matrix
        a. Add i + j for the element. This is the key
        b1. Add to dictionary the value of the element in a LIST, with index_sum as key
        b2. If the key already exists for that diagonal, just append the value to that list
    2. Loop over all diagonal lists from 0 to num_diagonals - 1
        a. reverse the diagonal_list if it has even i+j
        b. append diagonal to answer list
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        d = dict()
	#loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
		#if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
			#If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
		# we're done with the pass, let's build our answer array
        ans = []
        # number of diagonals is num_rows + num_cols - 1
        num_diagonals = len(matrix) + len(matrix[0]) - 1

        # the sum of i + j for each diagonal goes from 0 .... (num_diagonals - 1)
        for ij_sum in range(num_diagonals):
            # this is the list of elements
            diagonal = d[ij_sum]
            # we reverse diagonal list if i+j is even. The first diagonal (i+j = 0) is reversed
            if ij_sum % 2 == 0:
                diagonal.reverse()
            # append each element of diagonal to answer list
            ans.extend(diagonal)
        return ans


