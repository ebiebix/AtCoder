def palindrome(string):
    return 1 if string==string[::-1] else 0

s = input()
if(palindrome(s)):
    n = len(s)
    if(palindrome(''.join(list(s)[:((n-1)//2)]))):
        if(palindrome(''.join(list(s)[((n+3)//2)-1:n]))):
            print('Yes')
            exit()
print('No')