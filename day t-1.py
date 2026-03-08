#Python Interview Questions and Answers

#1. Compress String (Run-Length Encoding) – Variation

# Input ="aaabbca"
# Output = '3a2b1c1a'



# #2. Reverse each word in a sentence

# Input= "hello world"
# Output= "olleh dlrow"

# #3. Find first non-repeating character
# Input= "aabbcddde"
# Output= 'c'


# #4. Count vowels in a string
# Input="engineering"
# #Output= e=3, i=2

# #5. Remove duplicates but keep order
# Input= "banana"
# Output= "ban"

# #6. Check if two strings are anagrams
# Input= "silent", "listen"
# Output= True

# #7. Frequency of each character
# Input= "malayalam"
# Output= {'m':2,'a':4,'l':2,'y':1}

# #8. Find max occurring character
# Input= "success"
# Output= 's'

# #9. Swap two numbers without third variable

# a = 5
# b = 10

# #10. Reverse a string using loop (interview favourite)
# s = "suresh"

# #11. Palindrome check (string)
# Input= "radar" 
# Output= True
# s = "radar"

# #12. Check if number is prime
# Input= 29 
# Output= True

# #13. Fibonacci (n-th) using iteration
# Input= n=7 
# Output= 13 ('sequence = 0,1,1,2,3,5,8,13')

# #14. Remove duplicates from list (preserve order)
# Inp= [1,2,2,3,1,4] 
# Output= [1,2,3,4]

# out = []

# for i in Inp:
#    if i not in out:
#       out.append(i)
# print(out)      

# #15. Two-sum (indices) — O(n)
# Input= nums=[2,7,11,15],
# target=9 
# Output= [0,1]

# #16 Merge two sorted lists (like merge step)
# Input= [1,3,5] [2,4,6] 
# Output= [1,2,3,4,5,6]

# #17. Check balanced parentheses
# Input= "( [ ] )" 
# Output= True

# s = "([ ])".replace(" ", "")
# pairs = {'(':')','[':']','{':'}'}
# stack = []
# for ch in s:
#     if ch in pairs:
#         stack.append(ch)
#     else:
#         if not stack or pairs[stack.pop()] != ch:
#             print(False); 
#             break
#         else:
#          print(not stack)

# #18. Flatten nested list (single level)
# Input= [[1,2],[3,4],5] 
# Output= [1,2,3,4,5]

# #19 Count words in sentence

# Input= "hello hello world" 
# Output= {'hello':2,'world':1}

# #20. Check if list is palindrome
# Input= [1,2,3,2,1] 
# Output= True


#2. Reverse each word in a sentence

Input= "hello world"
Output= ""

from loguru import logger

for i in Input:
    Output = i+ Output
logger.info(Output)
