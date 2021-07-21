"""
Approach: Greedy, extract biggest value from num as possible and append corresponding letters

1. Initialize letters and values arrays from GREATEST to LEAST
2. iterate thru both letters and values, divide num by the letter value
    - append letter (quotient) times to end of result string
    - modulo num for next iteration

"""

class Solution(object):
    def intToRoman(self, num):
        # array of letters and values GREATEST to LEAST value
        letters = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ""
        for letter, value in zip(letters, values):
            # divide num by value to see if letter fits
            letter_count = num // value
            # modulo to get the remainder for future letters
            num = num % value
            # append letters to result
            result = result + letter_count * letter
            
            if num == 0:
                break
        return result