class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(string):
            left, right = 0, len(string) - 1
            while left <= right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                left_string = s[left+1:right+1]
                right_string = s[left:right]
                # print(f"Left side: {left_string} & right side: {right_string}")
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1

        return True
        