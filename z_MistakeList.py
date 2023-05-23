"""
COMMON MISTAKES

General:
    - using = instead of ==
    - need to check if key in dictionary, before changing value of d[key]
    - When using a loop, you must iterate over an ITERABLE.  such as Range(int)
    - Unpack operator goes BEFORE iterable  ex.  *my_list
    - Do not use KEYWORDS as var namex. ex. str, list, dict, set, next, OPEN

LOOPS:
    - when using RANGE make sure that you pass in an INT
    - can only use for VAL in X, if X is iterable NOT an int ... (when IN, think of iterable)
    - Write out conjunctions of predicates FULLY
        - ex. while i < 0 or j < 0     NOT    while i OR j < 0:       <--- Infinite loop, basically while 1
    - If using two pointers, but one pointer is the i in a for loop, make sure you manually increment the other pointer

For Loop:
    - if you find yourself needing the value of i - 1 at START of loop, consider working with i at END of loop before iteration

CONDITIONALS:
    - If you put a return in a conditional, ensure that there is a return if that condition is not met

Strings:
    - To slice a reversed copy of a string,  use  reversed_string = string[::-1]
    - You can convert a string into a list of chars. You CAN NOT convert a list of 'chars / strings' into a single string
    - If casing does not matter, convert string to .lower()
    - If need to modify string, convert to list and then back with "".join(lst)
    - If you have a LIST of strings and need to group characters by index, use list(zip(*strs))

Array:
    - Pointers Are just INDEX INTEGERS  -  NOT actual array values
    - arr_pointer = len(arr) - 1   ... NOT   arr_pointer = arr[N-1]

Linked List:
    - If we access cur.next.next, cur.next cannot be None
    - Not incrementing current or fast within While loop

Classes:
    - each method takes in a SELF parameter
        - If in a method definition we use another method, we call using self.method2()
"""
