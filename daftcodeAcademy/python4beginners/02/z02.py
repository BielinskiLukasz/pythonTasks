# zadanie 2

def reduce(nums):
    counter = 0
    list_length = nums.__len__()
    if list_length % 2:
        nums.append(0)
    result = []
    while counter < list_length:
        result.append(nums[counter] + nums[counter + 1])
        counter += 2
    return result


assert reduce([1, 2, 3, 4, 5, 6]) == [3, 7, 11]
assert reduce([1, 2, 3, 4, 5, 6, 7]) == [3, 7, 11, 7]
