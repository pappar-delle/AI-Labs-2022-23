def string_times(str, n):
  return str*n

def front_times(str, n):
  return (str[0:3]*n)*(len(str)>3) or str*n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  return "".join(str[:i] for i in range(1,len(str)+1))

def last2(str):
  return sum(1 for i in range(0, len(str)-2) if str[i:i+2] == str[-2:])

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  return nums[:4].count(9) > 0

def array123(nums):
  return any([1,2,3] == nums[i:i+3] for i in range(0,len(nums)-2))

def string_match(a,b):
    return sum(1 for i in range(len(a)*(len(a)<len(b)) or len(b)) if a[i:i+2] == b[i:i+2] and len (a[i:i+2])==2 and len(b[i:i+2])==2)

def make_bricks(small, big, goal):
  return goal%5 >= 0 and goal%5 - small <= 0 and small + 5*big >= goal

def lone_sum(a, b, c):
  return sum(n for n in [a,b,c] if [a,b,c].count(n) == 1)

def lucky_sum(a, b, c):
  return sum(n for n in [a,b,c,13][:([a,b,c,13]).index(13)])

def no_teen_sum(a, b, c):
  return sum(n for n in [a,b,c] if n not in [13,14,17,18,19])

def round_sum(a, b, c):
  return sum((((abs(i)+10-(abs(i)%10))*((abs(i)%10) >=6) or (abs(i) - (abs(i)%10)))*-1)*(i<0) or ((i+10-(i%10))*((i%10) >=5) or (i - (i%10))*(i>0)) for i in [a,b,c])

def close_far(a, b, c):
  return (abs(a-c)<=1 and abs(b-c)>=2 and  abs(a-b)>=2) or (abs(a-b)<=1 and abs(b-c)>=2 and abs(a-c)>=2)

def make_chocolate(small, big, goal):
  return (-1)*((small + (big*5) < goal) or (goal % 5 > small)) or (goal - (big*5))*(big*5 < goal) or (goal%5)

def double_char(str):
  return "".join(char*2 for char in str)

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
  return str.count("cat") == str.count("dog")

def count_code(str):
  return sum(1 for i in range(len(str)-3) if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e')

def end_other(a, b):
  return bool((a.lower().endswith(b.lower())) * (len(a) >= len(b))) or bool(b.lower().endswith(a.lower()))

def xyz_there(str):
  return str.count("xyz") > str.count(".xyz")

def count_evens(nums):
  return sum(-(n%2-1) for n in nums)

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  return int(sum(sorted(nums)[1:-1]) / (len(nums) - 2)) * ((sum(sorted(nums)[1:-1]) / (len(nums) - 2)) > 0) or round(sum(sorted(nums)[1:-1]) / (len(nums) - 2))

def sum13(nums):
  return sum((nums[i]) * (nums[i] != 13 and nums[i - 1] != 13 and len(nums) > 2) or (nums[i]) * (nums[i] != 13 and len(nums) == 2 and nums[i - 1] != 13) or nums[i] * (len(nums) == 2 and i == 0 and nums[i] != 13) for i in range(0, len(nums)))


def sum67(nums):
  while 6 in nums: del nums[nums.index(6):nums.index(7, nums.index(6)) + 1]
  return sum(nums)

def has22(nums):
  return any(v == 2 and nums[i+1] == 2 for i,v in enumerate(nums[:-1]))

#Pooja Somayajula, 4, 2024
