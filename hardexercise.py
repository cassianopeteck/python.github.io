def largestRange(array):
    numbers = {x: 0 for x in array}
    left = right = 0

    for number in array:
        if numbers[number] == 0:
            left_count = number - 1
            right_count = number + 1

        while left_count in numbers: #0(1)
            numbers[left_count] = 1
            left_count -= 1
        left_count += 1

        while right_count in numbers:
            numbers[right_count] = 1
            right_count += 1
        right_count -= 1

        if (right-left) <= (right_count - left_count):
            right = right_count
            left = left_count

    return [left,right]

array = [52,3,1,9,32,2,5,66,99,24]
print(largestRange(array))
