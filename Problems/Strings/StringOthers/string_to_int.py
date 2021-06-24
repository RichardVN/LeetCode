class Solution:
    def myAtoi(self, s: str) -> int:
        """   
        NOTE: when using while loops, make sure to increment pointer.
        # read and ignore whitespace
            # check if next char after whitespace is + or -
            # read digits until next non digit OR end of input
            # ignore rest of string
            # convert digits to integer, change sign as necessary
            # clamp integer into 32 bit range
            # """
        
        # ex.  "    -42with"
        SYSMAX = 2**31-1
        SYSMIN = -2**31
        
        i = 0
        sign = 1
        result = 0
        
        # jump i past whitespace **AND within word
        while i < len(s) and s[i] == " ":
            i += 1
        
        # read sign
        if i < len(s) and s[i] == "+":
            sign = 1
            i+=1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i+=1
        # else sign is just positive
        
        # read digits until NON digit or end of input
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # check if we will overflow. Either first x digits greater, or exactly match
            print(result)
            if result > SYSMAX // 10 or (result == SYSMAX // 10 and digit > 7):
                # overflow, return max or min
                return SYSMAX if sign == 1 else SYSMIN
            
            # No overflow. add digit to whatever digits we have in result so far
            result = 10*result + digit
            
            # iterate i to next digit
            i+=1
            
        # remember to add sign
        return result * sign