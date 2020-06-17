'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    modArr = []
    for x in range(0, len(arr)):
        if arr[x] != 0:
            modArr.append(arr[x])
    for x in range(0, len(arr)):
        if arr[x] == 0:
            modArr.append(arr[x])
    return modArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")