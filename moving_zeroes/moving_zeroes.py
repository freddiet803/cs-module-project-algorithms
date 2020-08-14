'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    sorted = arr
    sorted.sort()
    # print(sorted)
    lhs = []
    pivot = arr[0]
    rhs = []

    for i in range(1, len(sorted)):
        if arr[i] != 0:
            lhs.append(arr[i])
        else:
            rhs.append(arr[i])

    return lhs + [pivot] + rhs


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
