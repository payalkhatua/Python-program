def ispalindrome(s):
    return s==s[::-1]

s="able was i ere i saw elba"
ans=ispalindrome(s)

if ans:
    print("yes,it is palindrome")
else:
    print("No,it is not palindrome")
