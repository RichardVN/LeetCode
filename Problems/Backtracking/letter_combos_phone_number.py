"""
time:  O(4^N),  height of tree is N digits, branch x4 times each level

approach:
    - If input is empty return an empty array
    - initialize a hash map that maps digits to their letters
    - lock in the letters of first digit
    - Loop thru rest of digits
        - get current triplet
        - Loop thru existing_combos and current_triplet 
            append each letter of triplet to combo and append to current combo
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        # hash map to look up letters for each digit
        interpret_digit = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        # Find the letter triplet for first digit
        first_triplet = interpret_digit[digits[0]]
        # lock in each of the three letters for first digit
        result_combinations = [character for character in first_triplet]
        
        # loop through rest of digits
        for i in range(1, len(digits)):
            # get the letter triplet for this digit
            current_triplet = interpret_digit[digits[i]]
            
            # array of cominations for this level of the tree
            combinations_this_level = []
            # Loop through combinations and current chars,  append chars for each combination
            for combination in result_combinations:
                for letter in current_triplet:
                    combinations_this_level.append(combination+letter)
            result_combinations[:] = combinations_this_level
        
        return result_combinations