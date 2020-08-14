'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # commented out code assumes duplicates will always come in as pair values
    '''for i in range(0, (len(arr)-1), 2):
        print(i, 'iteration')
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                print(i, j, 'duplicate')
                break
            if arr[i] != arr[j]:
                print(i)
                print(j)
                print(arr[i], f' is the value at index {i}')
                print(arr[j], f' is the value at index {j}')
                return arr[i]'''
    ourSet = set()  # set is ultimate way because it cant contain duplicates

    for i in arr:
        if i in ourSet:
            ourSet.remove(i)
        else:
            ourSet.add(i)

    return list(ourSet)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
