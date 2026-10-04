# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
#1. Rotate Right
# Rotate the values in a collection to the right by k steps.
# Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_right(values,k):
    # Edge Cases
    if not isinstance(values, list):
        return "Values must be a list"
    if len(values) == 0:
        return []
    if not isinstance(k, int):
        return "k must be an integer"

    # Makes sure K can't be longer than the length of "values"
    k = k % len(values)  

    return values[-k:] + values[:-k]

# Test Cases
print(rotate_right([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
print(rotate_right([],2))  # Output: []
print(rotate_right("a",2))  # Output: "Values must be a list"
print(rotate_right([1,2,3,4], "right")) # Output: "k must be an integer"

"""
For this timed challenge, I picked the “Rotate Right” problem and decided to use a basic Python list with slicing. 
I chose this approach because it’s something I already understand well, and slicing makes it easy to move parts of a list around without writing a bunch of complicated code. 
Instead of trying to build a rotation algorithm from scratch or using a more advanced structure, I stuck with something simple that I knew would work. Lists are flexible, 
and slicing lets you grab the last part of the list and stick it in front, which is basically what rotating is. The 30‑minute time limit definitely affected how I approached the problem. 
When you’re on a timer, you don’t want to waste time experimenting or trying to be fancy. You just want a solution that works and is easy to test. 
Because of that, I didn’t overthink the data structure choice. I went with the one that would let me finish the problem quickly and still feel confident that the output was correct. 
I did make a few trade‑offs because of the time limit. For example, slicing creates a new list instead of modifying the original one, which isn’t the most memory‑efficient option. 
But for a coding challenge, that’s totally fine. I also didn’t spend time adding deep error handling or extra features. My main goal was to get a clean, working solution within the time limit, 
and I think the approach I chose balanced speed and correctness well.
"""