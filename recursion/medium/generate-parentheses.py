# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/
def generateParenthesis(n: int) -> list[str]:
    result = []
    def helper(open, close, string):
        nonlocal result
        nonlocal n
        if open + close == 2*n:
            result.append(string)
        if open < n:
            helper(open+1, close, string + '(')
        if close < n and open > close:
            helper(open, close + 1, string + ')')
    helper(0, 0, '')
    return result

# Time Complexity: O(4^n / sqrt(n)) - the number of valid parenthesizations is the n-th Catalan number C_n ~ 4^n / (n * sqrt(n)), and building/copying each string of length 2n takes O(n) time
# Space Complexity: O(n) - maximum recursion call stack depth is 2n (excluding output space O(4^n / sqrt(n)) for result)

print(generateParenthesis(1))
