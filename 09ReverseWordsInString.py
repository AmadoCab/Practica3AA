class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = ''
        word = ''
        for l in s:
            if l == ' ':
                reverse = reverse + word + ' '
                word = ''
            else:
                word = l + word
        reverse = reverse + word
        return reverse

# EOF #
