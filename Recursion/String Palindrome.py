def is_palindrome(text):
    if len(text)==0 or len(text)==1:
        return True
    if text[0]==text[-1]:
        return is_palindrome(text[1:-1])
    return False
text=input("Enter the String :").lower()
checkPalindrome=is_palindrome(text)
if checkPalindrome==True :
    print("The Given String is Palindrome")
else :
    print("The Given String is Not Palindrome")