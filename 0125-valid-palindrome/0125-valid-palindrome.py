class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=''
        for i in s:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48<= ord(i) <=57:
                x+=i
        p=x[::-1]

        if x.lower()==p.lower():
            return True
        else:
            return False
        