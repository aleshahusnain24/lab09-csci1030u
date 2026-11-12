# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #  make two for-loops one that goes through i and one through j and check if the 
    # check if the sum adds upt to be the target and have the rest iterate 

    # then return the indices pair that had a sum equaks to the target

    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]




def max_profit(prices):
    # Outline:
    #  since profit = sell price - buying price 
    # we can check the lowest price and updates it when found a min price
    #  buy it, for-loop to iterate and check through each index for min
    #and check for the highest price and calculate max profit made

     # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.

    if len(prices) == 0: # out of bound test check
        return 0
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

    return max_profit




def max_subarray(nums):
    # Outline:
    # Using a for loop iterate through the list of nums and decide to start a new array or add to the same 
    # update the largest sum found and return max_sum found

    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    
    current_sum = nums[0] #  start with 0 
    max_sum = nums[0]
    
    for num in nums[1:]: # iterate through each index
        current_sum = max(num,current_sum + num)
        
        if current_sum> max_sum:
            max_sum = current_sum

    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # You need to check if the brackets are in the right order for it to retunr true 
    #append adds bracket on toop of stack and pop removes if wrongly placed 

    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    # stack = []
    
    stack = []

    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
          }
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False

            if stack[-1] != bracket_pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0




       


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    two_sum([2, 7, 11, 15], 9)   # returns [0, 1]   (2 + 7)
    two_sum([3, 2, 4], 6)        # returns [1, 2]   (2 + 4)

    max_profit([7, 1, 5, 3, 6, 4])   # returns 5   (buy at 1, sell at 6)
    max_profit([7, 6, 4, 3, 1])      # returns 0   (prices only fall)

    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])   # returns 6   (4 + -1 + 2 + 1)
    max_subarray([5, 4, -1, 7, 8])                  # returns 23  (the whole list)

    is_balanced("()[]{}")   # returns True
    is_balanced("{[]}")     # returns True
    is_balanced("([)]")     # returns False   (closed in the wrong order
    
    
    
if __name__ == "__main__":
    main()
