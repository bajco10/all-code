"""def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))"""

# English ruler using recursion

def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followd by optional label)"""
    line = "-" * tick_length
    if tick_label:
        line += " " + tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length -1)
        draw_line(center_length)
        draw_interval(center_length -1)
    
def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, "0")
    for j in range(1, 1+num_inches):
        draw_interval(major_length -1)
        draw_line(major_length, str(j))

# draw_ruler(3, 2)

# binary search algorithm -> runs in O(log n) time

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list
    The search only considers the portion from data[low] to data[high] inclusive"""
    if low > high:
        return False # interval is empty; no match
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        elif target > data[mid]:
            # recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)

# recursive function for reporting disk usage of a file system
import os

def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usage(childpath)
    
    print("{:<7}".format(total), path)
    return total

# print(disk_usage("/home/tomas/Desktop/all-code/SCHOOL"))

# calculating n-th number of the fibonacci sequence

def good_fibonacci(n):
    if n<=1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)

# print(good_fibonacci(5))

# linear sum of a slice of a list
def linear_sum(S, n):
    if n ==0:
        return 0
    else:
        return linear_sum(S, n-1)+S[n-1]
    
test = [2, 2, 45, 2, 11, 80, 83, 248]

# print(linear_sum(test, 5))

def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)  # rely on truncated division
        result = partial * partial
        if n % 2 == 1:  # if n is odd, include an extra factor of x
            result *= x
        return result

print(power(2, 13))