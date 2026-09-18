class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        count = 0
        end = 0
        for i in range(len(s)):
            for j in range(i+k,len(s)+1):
                if self.is_pal(s[i:j]):
                    if end < i:
                        count += 1
                        end = j-1
        return count

    def is_pal(self,s:str) -> bool:
        return s == s[::-1]

test = Solution()
print(test.maxPalindromes("fttfjofpnpfydwdwdnns",2))
