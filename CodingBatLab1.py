def sleep_in(weekday, vacation):
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


def sum_double(a, b):
    return a + b if a != b else 2 * (a + b)


def diff21(n):
    return 21 - n if n < 22 else 2 * (n - 21)


def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))


def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)


def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


def pos_neg(a, b, negative):
    return True if (a > 0 and b < 0 and negative is False) else True if (
                a < 0 and b > 0 and negative is False) else False if (
                a >= 0 and b < 0 and negative is False) else False if (
                a < 0 and b >= 0 and negative is False) else True if (a < 0 and b < 0 and negative is True) else False


def hello_name(name):
    return "Hello " + name + '!'


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    return '<' + tag + '>' + word + '<' + '/' + tag + '>'


def make_out_word(out, word):
    return out[0:int(len(out)/2)] + word + out[int(len(out)//2) + 1 - 1:]


def extra_end(str):
    return str[-2:] * 3


def first_two(str):
    return str if len(str) <= 2 else str[:2]


def first_half(str):
    return str[:int((len(str) / 2))]


def without_end(str):
    return str[1:-1]


def first_last6(nums):
    return 6 in [nums[0], nums[-1]]


def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]


def make_pi(a):
    return [3,1,4,1,5,9,2,6,5,3,5,8,9,7][:a]


def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    return sum(nums)


def rotate_left3(nums):
    return nums[1:] + nums[0:1]


def reverse3(nums):
    return nums[::-1]


def max_end3(nums):
    return ([nums[0]] * len(nums) if nums[0] >= nums[-1] else [nums[-1]] * len(nums)) if len(nums) > 1 else nums


def cigar_party(cigars, is_weekend):
    return cigars >= 40 if is_weekend else cigars in range(40, 61)


def date_fashion(you, date):
    return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1


def squirrel_play(temp, is_summer):
    return temp in range(60, 101 if is_summer else 91)


def caught_speeding(speed, is_birthday):
    return 2 if (speed - (65 if is_birthday else 60)) > 20 else 1 if (speed - (65 if is_birthday else 60)) > 0 else 0


def sorta_sum(a, b):
    return 20 if a + b in range(10, 20) else a + b


def alarm_clock(day, vacation):
    return ("7:00" if not vacation else "10:00") if day not in [6, 0] else ("10:00" if not vacation else "off")


def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6


def in1to10(n, outside_mode):
    return True if n == 1 or n == 10 else (n in range(1, 11)) ^ outside_mode
