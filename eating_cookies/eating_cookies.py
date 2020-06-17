'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n == 0:
        return 1
    count = 0
    if n>0:
        count+=eating_cookies(n-1)
        count+=eating_cookies(n-2)
        count+=eating_cookies(n-3)
    

    return count

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
