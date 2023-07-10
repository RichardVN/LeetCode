"""
CLUES FROM GIVEN INFORMATION:
-- GENERAL Problem Solving --:
    - Ask about assumptions / constraints. Note these down
    - "What does it really mean?"   translate the problem into what we ware trying to find out in CODE.
        - ex. What constitutes this string is a palindrome? (walk from both ends, values should be same)
        - ex. What constitutes a possible palindrome?    (each character in set should have even parity except one)
        - ex. What constitues permutation?  (Same length, same count of each value)
        - ex. What is max profit? (The price we sell at from a previous, smaller indexed local minimum)
    - Use smaller examples
    - DRAW IT OUT
    - Try rephrasing the problem as its negation
        ex. Remove duplicates -> find unique values
        ex. move zeroes to end -> move non-zeroes to front

    - Optimize
        1. We are NOT using the all the available information given
        2. We are trying to solve MORE than we are asked for, thereby taking more time/space.
    - Convert what the problem is saying into what it means in terms of code
        ex. Greatest profit means biggest positive delta from local min, to local max towards right
    

-- Strings --:
    - NOTE: Strings are immutable in python. It is likely we have to convert to list and then ''.join
    - NOTE: Interview clarification questions
        - Can there be whitespace?
        - Does casing matter?
        - What are the allowed characters? ASCII? (0-127) .... goes from space -> digits -> upper -> lower
    - Tips:
        - Consider making a static array that maps chars to count (128 for ASCII)
        - If we are only considering lower case alpha, adjust indices.  i = ord('j') - ord('a')
        - If we have to modify by indices, convert string to list first

    - Reverse a string:
        - r_string = string[::-1]
        - r_string = ''.join(reversed(string))
    - Group characters by index in list of strings:
        - Consider zipping them to match letter groups.    list(zip(*strs))
    - Manipulate a string:
        - convert to list of chars and change via indices
        - use splice notation. Ex Removal: s = s[:8] + s[9:]

    - NOTE: Concatenation of sequence of strings size m and string size n is O(M+N)
    - Iteratively concatenating a list of strings would be O(N^2). You have to copy the beginning section over and voer
    - Instead: 
        1. Loop to add strings to list.      
        2. ''.join(iterable)           Both steps are sequential O(N)

    - Important string methods:
        chars = list(string)        => turn word into a list of chars
        unique_chars = set(string)  => turn word into set of unique, no duplicate Chars

        string.split()              => splits WORDS at specified separator (default whitespace), returns list
        '-'.join(iterable)          => joins iterable of strings, with an indicated separator between str elements

        string.index('substring')   => index of substring, throws error if not found
        string.rindex('substring')  => last position of where substring starts, scan start from right side

        string.isalnum()            => True if digits or alpha
        string.isdigit()            => '0' - '9'

-- ARRAY PROBLEMS --:
    - TODO:  0 based index TO array length conversions 
        - the length of subarray i to j (NOT INCLUDE J) is j - 1
        - the length of inclusive subarray 0 to index is one more than index

    - NOTE: Ask Interviewer
        - Am I allowed to change the input data? (in place, saves space)
        - Sorted or unsorted?
        - Integers only?
        - Positive only?
        - Range of values limited?
    - To get O(N) time, it might be necessary to make multiple passes over the array
Unsorted Array:
    - Unless we sort, we likely have to make another array to hold answer. Space: O(N)
Sorted Array 
    - NOTE: Think of 2 pointer and binary search
    - Duplicates MUST be next to each other
    - ** We can GUARANTEE that a larger index results in a equal or larger value
    - Doing insert(i, val) will add val to current index, shift everything to the right, and can result in infinite inserts.

In Place Modify Array 
    - NOTE: Two Pointer method
        - Fast Pointer: Reads over all original array values. (perhaps with for loop)
            - Guarantee increment each loop
        - Slow Pointer: Writes in the new values, overwriting original values. 
            - Increment ONLY when we find a value we want. Does not jump ahead of fast pointer, do NOT overwrite unread elements
    - Inserts will likely take O(N^2). NOTE: Try to move each Element ONCE
    - Look at original array and expected output array. Likely a pattern in how much the element is shifted.
    - NOTE: Types of In-Place questions
        - 1. Adding elements (e.g. duplicate zeroes)
            - If we add elements to the RIGHT of i (ex. insert i+1), we need to loop R to L to avoid writing over unread elements
            - Look at original vs. expected. Is there a pattern in how much each element is shifted?
        - 2. Removing elements (e.g. remove duplicates)
            - Reword the question into what we are trying to find
            - Two pointer method. Fast pointer loops over original. Slow pointer writes in the desired values at front.
        - 3. Reorganize. Same size. (e.g. zeroes at back, even numbers in front)
            - Reword the question to what values we are trying to write at front w. slow pointer
            - NOTE ** Utilize Variable Swapping.     a, b = b, a     to reorganize desired values to front

Array Sort Problems:
    - If the values are POSITIVE and range is less than or equal to number of elements N
        - Use count_sort which is O(n+k), or O(N) time if above condition
Array Search Problems:
    - If sorted, can use binary search in O(log N) time
    - If not sorted, should take O(N) at most to do linear search.
        - Sorting, then binary search would take O(N log N)


-- Linked List --

- ** 1. While loop conditions. 
        1a.  Ensure we break out of loop by iterating current pointer
        1b.  Ensure we dont access .next or .val from None
        - If we accessing current.next.val or current.next.next, then we have to ensure current.next != None 
            ex. fast.next.next
        - If we have fast / slow pointers. The fast pointer is the one we check for in the while condition.
- ** 2. Always check for special case where you change the head node. You will need to change Head Pointer.
- ** 3. Modify List: One pointer for head. Second pointer to iterate while second pointer is not None.
- ** 4. Make List: Dummy node. Pointer for appending to tail, and keeping track last node
-    5. When you think you need size of list: Consider two pointer method with a constant gap to do in one pass.
- ** 6. Get last K nodes. Set fast = slow = head. increment fast K times.    While fast: increment by one fast and slow... slow is at N-kth node
- ** 7. Need to access nodes out of traversal order (ex. Deep Copy Clones)
        -

- Floyd's Tortoise and Hare, Cycle detection. Midpoint detection.
    - slow jumps one node at a time, fast jumps two nodes. At N iterations, fast is guaranteed to be in same spot as slow (one lap ahead)
        1. If NOT Cycle: fast reaches None or fast.next reaches None (end of list) and slow is at MIDPOINT.
        2. If Cycle: fast pointer catches up to slow pointer
    - After slow catches fast. We can find the loop start, as both slow and fast are m nodes away from loop start.
        - While fast != None and fast.next != None
            * we are accessing fast = fast.next.next, therefore fast.next can NOT be None

- Find Intersect:
    - PtrA and ptrB traverse respective lists. Switch to other list after reaching None
    - Eventually ptrs will intersect. If no intersection, guaranteed meet at None after a+b iterations.
        - ** use   if ptrA is None    check. We allow ptrs to reach None "node", because that is where they will intersect.

- Complexities:
    - Space: O(1) if only using pointers
    - Time: analyze how many times we loop.
        - No cycle, fast is O(N/2) to reach end
        - Cycle, slow takes O(N) to reach cycle and O(K) for fast to lap 

"""


"""
WHEN TO USE DATA STRUCTURES:

Array (python list)
    - WHEN:
        - ACCESS BY INDEX
    - PROS:
        - Maintains Order
        - O(1) random access by index, ANYWHERE
        - If sorted, Binary search in log n time
    - CONS: 
        - Insertion/Deletion is O(N)
        - Append is amortized O(1) +

Linked List (python deque)
    - WHEN:
        - INSERT / DELETE FROM ENDS ... appendleft, popleft
    - PROS:
        - Add / Remove from ENDS in O(1)
        - Index access from ENDS is O(1)
    - CONS:
        - Index access from MIDDLE is O(n) time
        - Insertion / Deletions given a node is O(N) for singly-linked, b/c we have to find node before. If doubly-linked, then O(1)

HashSet (python set)
    - WHEN:
        - FAST LOOKUP VALUE
    - PROS:
        - No duplicates ("Think of as bag")
        - O(1) SEARCH / ACCESS  * on average *
        - O(1) Add / Delete * on average *
    - CONS:
        - Not ordered, no duplicates
        - Values only, no associations
        - O(N) time to copy, O(N) space unless values are bounded to constant < N elements
        - In WORST case, operations are O(N) due to collisions if hash function is bad

HashMap (python dictionary)
    - WHEN:
        - FAST LOOKUP key-value pair
    - PROS:
        - No duplicates
        - O(1) SEARCH / ACCESS   Key
        - O(1) Add / Delete
    - CONS:
        - not ordered by index(unless use OrderedDict), no duplicates
        - O(N) space, where N is the # key-value pairs
        - O(N) time to copy, O(N) space unless keys are restricted (think 26 alphabet characters)
        - Worst case operations O(N) due to collisions
Counter (dicitonary subset)
    -WHEN: need a count of each element from an iterable
            ex. d = Counter(my_string)   or   d = Counter(my_list)
* from collections import Counter

Balanced Binary Search Tree
    - Pros:
        - Potentially less space than hash map
        - Can iterate through the keys in order
    - Cons:
        - O(log n) lookup time


"""


"""
PYTHON SPECIFIC TIPS
Loops:
    - for i in range(N):   
        # N iterations
        # index 0 to N-1
        # after loop, i == N
    - What value is i left with?
        - In a WHILE loop, i becomes N, the value that breaks the condition
        - In a FOR loop, i becomes N-1, it does NOT take on the excluded value specified in range() 
        - In a FOR loop to an index in LINKED LIST, i becomes the node at index. This is because we iterate to idx-1 node THEN current.next

    - ** Whenever accessing i + 1 or i - 1, care for index access error. (first value is 0, last is N - 1)

*For loops:
    - Use when we know how many iterations, and we guarantee an iterator advance no matter what 
    - The iterator of for loop can act as the "fast" / "Reader" pointer

    - 1. Don't loop over entire array, or iterate reverse
        for i in range(len(arr)-1, -1, -1):
    - 2a. Loop over entire array, need to MODIFY the original array
        for i in range(len(arr)):    OR     for i in enumerate(arr):
    - 2b. Loop over entire array, only need READ values without modifying original array
        for val in arr:
        
    - ** In all these cases, i is left with the excluded value indicated within Range

*While Loops:
    - The break condition can be something we are trying to FIND.
        ex. while item != 'needle':  item = item.next
        ex. while current.next is not None: current = current.next      # FIND THE TAIL
    - FIRST and MOST IMPORTANT: ensure that there is the condition is eventually broken. Care for infinite loops
    - Multiple conditions!:
        - If first condition is met, the second contition is skipped (in case of index error)
            - So always put index checks i < N before access checks a[i+1] ... 
        - be sure to account for either case in which condition breaks

Iterate over array:
    - Use enumerate() when looping through entire array, front to back. And need to modify original values with index.
    - Use range(start, end, step) when going backwards, or starting at a specific index

List Comprehension:
    - Use when you want to create an entirely NEW list based off an existing lists values. O(N) space
    - replaces the new_list = []   ...    for element in old_list:   new_list.append()     construct

2D Arrays / Matrices: 
    - NOTE: Matrix =  a list of rows
    - Initialize 2d matrix:     matrix = [[0 for col in cols] for row in rows]
    - ** Number of rows  =  len(matrix)
    - ** Number of cols  =  len(matrix[0])
    - Traverse ALL elements in matrix, no modify...Rows in outer loop.   
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
    - Traverse over a single row
        for j in range(num_cols):
            matrix[ROW][c] = something..
    - Traverse over a single col
        for i in range(num_rows):
            matrix[i][0] = something..

    - Number of DIAGONALS = num_rows + num_cols - 1
    - All elements in diagonal have same i + j  (indices sum)


Integer Manipulation:
    - Retrieve Digits from end of Number:   Modulo by the next highest digit place
        - Get digit at ones place:      num % 10            ("anything lower than 10")
        - Get digits at tens and ones:  num % 100            ("anything lower than 100)
    - Remove Digits from end of Number:     Integer division by 10 ^ (digits to remove)
        - Remove last digit of integer: num // 10
    - ** Array Digits or Linked List digits to integer:
        - go from least significant to most significant digit. value = value + digit * 10**index
    - ** Addition
        - Go from least significant to most significant digit.
        - get digit_sum = n1 + n2 + carry
            - if digit sum >= 10, set carry to 1. Else set carry to 0.
            - write in the node: digit_sum % 10


Linked List Techniques:
    1. Set current to the tail node (current.next is None).     Inner statements that access Node attributes of current.NEXT
        current = self.head
        while current.next is not None:    
            # statements where we access current.next.val or current.next.next         
            current = current.next
        # at end of loop, current will be the tail node

    2. Do work over EACH node in the linked list.               Inner statements access node attributes of CURRENT
        current = self.head
        while current:                              # at end of loop, current will be None after tail node
            # statements to do stuff with node
            current = current.next

    3. have current end on i-th node
        for i in range(self.index):
            # statements to do stuff
            current = current.next

    4. Insert before index-th Node, including appending at end
        current = self.head
        # find node before the node to remove
        for i in range(index - 1): 
            current = current.next          # think of this as i++
        # current will end at the node BEFORE the node at i-th index (including NONE)
        # skip the ith node
        current.next = current.next.next
    
"""


"""
TODO: COMPLEXITY OF PYTHON METHODS
https://wiki.python.org/moin/TimeComplexity

NOTE:
--- Things we can get for "FREE" O(N) ---
    - Reverse:                        iterable.reverse()      reversed(iterable) -> Returns an iterator object that must be containerized
    - Maximum or minimum:            min(iterable)           max(iterable)
    - Total SUM:                     sum(iterable)
    - Length:                        len(iterable)
    - Count:                         list.count(X)


List Comprehension: O(N) temporary space

 * sort is O(N log N) Time   and  O(N) Space
Sorted: returns a copy of sorted array       * can use reverse = True
.sort(): method, mutate sorts array in place

Additional Notes:
Arrays:
    - Negative indices:
        - arr[-2]  is  arr[N-2]     ...    if N is 4, that means  arr[N-2]   is    arr[2]
    - Set slice of array is only O(k), if the replacement slice is of the same size. No shifting of other elements.
    - Get Slice: O(k), not in-place
    - .clear()      O(N) clears all elements
ASCII Conversion
    - ord()   returns integer Unicode value of character
    - chr()   returns character from Unicode value
String to Integer:
    - str() similar to atoi() which is O(N) time O(1) space
String comparison:
    - O(max(m,n))
Hashing a string value:
    O(K) where k i length of string
"""


"""
Additional problem solving Algorithms

Sliding window:
    - We are optimizing for something (most, smallest)
    - We are given a sequential data structure (array, linked list)

Dynamic Programming:
    - The solution to the whole problem can be derived from solution to similar, smaller subproblems
    - There is repeated work in recursion that can be memoized
"""
