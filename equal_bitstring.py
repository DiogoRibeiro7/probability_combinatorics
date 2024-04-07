import math

def combinations(n, k):
    """
    Calculate the number of combinations (n choose k).
    
    Parameters:
    n (int): Total number of items.
    k (int): Number of items to choose.
    
    Returns:
    int: Number of combinations.
    """
    return math.comb(n, k)

# Number of ways to arrange 3 zeroes and 3 ones in a string of length 6
arrangements = combinations(6, 3)

print("Number of bit-strings of length 6 with equal number of 0's and 1's:", arrangements)
