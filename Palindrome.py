# Native Approach (just reverse the string)

def ispalindrome (str):
  original_string = str(str)
  return original_string == original_string[::-1]

str = 121
str_1 = ispalindrome(str)

if str:
  print('yes')
else:
  print('no')

# Using Iterative Method

def isPalindrome(str):

    new_str = int(len(str)/2)
    for i in range(0, new_str):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

s = '121'
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")



