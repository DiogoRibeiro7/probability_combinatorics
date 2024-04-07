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

# Number of ways to choose 3 cards from 13 hearts
hearts_combinations = combinations(13, 3)

# Number of ways to choose 3 cards from 13 spades
spades_combinations = combinations(13, 3)

# Total number of 6-card hands with three hearts and three spades
total_hands = hearts_combinations * spades_combinations

print("Number of 6-card hands with three hearts and three spades:", total_hands)
