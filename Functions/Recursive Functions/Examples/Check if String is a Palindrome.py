### Check if string is a palindrome ###

def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

print (palindrome("level")) ''' Output: True '''
print (palindrome("hello")) ''' Output: False '''
