# How to set up two pointers in an array

def two_pointers(array):
    left = 0
    right = len(array) - 1
    mismatch_count = 0
    while left <= right:
        if array[left] != array[right]:
           mismatch_count +=1 
           right = right - 1 
        left = left + 1
        right = right -1 
    return False if mismatch_count > 1 else True
    

def is_palindrome(s):
  # Write your code here
  # Tip: You may use the code template provided
  # in the two_pointers.py file
  

  return two_pointers(s)



if __name__ == "__main__":
  s = "abbababa"
  print(is_palindrome(s))