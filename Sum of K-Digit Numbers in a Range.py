# Q4. Sum of K-Digit Numbers in a Range

# You are given three integers l, r, and k.
# Consider all possible integers consisting of exactly k digits, where each digit
# is chosen independently from the integer range [l, r] (inclusive).
# If 0 is included in the range, leading zeros are allowed.
# Return the sum of all such numbers modulo 10^9 + 7.

class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        MOD = 10**9 + 7

        lorunavemi = (l, r, k)

        n = r - l + 1                        # count of digits in [l, r]
        S = n * (l + r) // 2                  # sum of digits in [l, r]

        # Total sum = n^(k-1) * S * repunit(k)
        # where repunit(k) = (10^k - 1) / 9  (the number 111...1 with k ones)
        # We compute the division by 9 using modular inverse.

        inv9 = pow(9, MOD - 2, MOD)           # modular inverse of 9
        repunit = (pow(10, k, MOD) - 1) * inv9 % MOD

        result = pow(n, k - 1, MOD) * (S % MOD) % MOD * repunit % MOD
        return result
