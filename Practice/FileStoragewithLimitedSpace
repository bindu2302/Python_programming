from typing import List

def find_max_form(strs: List[str], m: int, n: int) -> int:
    # Create a 2D DP table where dp[i][j] represents the max subset size
    # that can be formed using at most i '0's and j '1's
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for s in strs:
        count_zeros = s.count('0')
        count_ones = s.count('1')
        
        # Traverse the DP table backwards to prevent overwriting previous states
        for i in range(m, count_zeros - 1, -1):
            for j in range(n, count_ones - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - count_zeros][j - count_ones] + 1)
    
    return dp[m][n]

# Input handling
if __name__ == "__main__":
    m, n = map(int, input().split())  # Read m and n
    k = int(input())  # Number of binary strings
    strs = [input().strip() for _ in range(k)]  # Read binary strings

    # Output the result
    print(find_max_form(strs, m, n))
