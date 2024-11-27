def palindrome(nums):
  for i in range(0, len(nums)):
    res = nums[i]
  for j in range(-1, len(nums)):
    ret = nums[j]
  if res == ret:
      return True
  else:
        return False
ot = palindrome([121])
print(ot)