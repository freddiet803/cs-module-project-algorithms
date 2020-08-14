'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    new_array = []
    count = 0

    while count < (len(arr)):
        if count == 0:
            value = 1
            for i in range(count + 1, len(arr)):
                value *= arr[i]
                # print(value)
            new_array.append(value)
            count += 1

        else:
            value = 1
            for i in range(count+1, len(arr)):
                value *= arr[i]
            # if the end point wasnt negative kept returning 1, needed negative for loop execution, need to research more on why
            for j in range(count-1, -1, -1):
                value *= arr[j]
            new_array.append(value)
            count += 1
    return new_array


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [90, 9]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
    # 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
