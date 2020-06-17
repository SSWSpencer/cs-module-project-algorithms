'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    for a in range(0, len(arr)):
        counter = 0
        for b in range(0, len(arr)):
            if arr[a] == arr[b]:
                counter += 1
        if counter == 1:
            return arr[a]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")