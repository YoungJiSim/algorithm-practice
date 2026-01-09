def contain_duplicate(nums):
    """
    https://leetcode.com/problems/contains-duplicate/description/
    
    Given an integer array nums, 
    return true if any value appears at least twice in the array, and 
    return false if every element is distinct.

    Example 1:
        Input: nums = [1, 2, 3, 1]
        Output: true
        Explanation:
        The element 1 occurs at the indices 0 and 3.

    Example 2:
        Input: nums = [1, 2, 3, 4]
        Output: false
        Explanation:
        All elements are distinct.
        
    Example 3:
        Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        Output: true
        
    Constraints:
        1 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
    """
    return len(set(nums)) != len(nums)


def is_anagram(s, t):
    """
    https://leetcode.com/problems/valid-anagram/description/
    
    Given two strings s and t,
    return true if t is an anagram of s, and
    false otherwise.
    
    Example 1:
        Intput: s = "anagram", t = "nagaram"
        Output: true
        
    Example 2:
        Input: s = "rat", t = "car"
        Output: false
        
    Constraints:
        1 <= s.length, t.length <= 5 * 10^4
        s and t consist of lowercase English letters.
    """
    return sorted(s) == sorted(t)


def main():
    # print(contain_duplicate([1, 2, 3, 1]))
    # print(contain_duplicate([1, 2, 3, 4]))
    # print((contain_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])))

    print(is_anagram("anagram", "nagaram"))
    print(is_anagram("rat", "car"))


if __name__ == "__main__":
    main()   