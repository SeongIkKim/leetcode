class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        for letters in list(zip(*strs)):
            if len(set(letters)) != 1:
                break
            ans.append(letters[0])
        return ''.join(ans)