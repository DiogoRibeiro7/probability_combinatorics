import math

def binomial_probability(n, k, p):
    """
    Calculate the binomial probability for k successes in n trials with success probability p.
    
    :param n: int - number of trials
    :param k: int - number of successes
    :param p: float - probability of success on a single trial
    :return: float - binomial probability
    """
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parameters
n = 1000  # Number of layers
p = 0.5   # Probability of moving right

# Calculate the total probability of landing in bins 400 to 600
probability_sum = sum(binomial_probability(n, k, p) for k in range(400, 601))

print(probability_sum)

import math

def binomial_probability(n, k, p):
    """
    Calculate the binomial probability for k successes in n trials with success probability p.
    
    :param n: int - number of trials
    :param k: int - number of successes
    :param p: float - probability of success on a single trial
    :return: float - binomial probability
    """
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parameters
n = 1000  # Number of layers
p = 0.5   # Probability of moving right

# Calculate the total probability of landing in bins 400 to 600
probability_sum = sum(binomial_probability(n, k, p) for k in range(400, 601))

print(probability_sum)


import math

def binomial_probability(n, k, p):
    """
    Calculate the binomial probability for k successes in n trials with success probability p.
    
    :param n: int - number of trials
    :param k: int - number of successes
    :param p: float - probability of success on a single trial
    :return: float - binomial probability
    """
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

# Parameters
n = 100  # Number of layers
p = 0.5  # Probability of moving right

# Calculate the total probability of landing in bins 40 to 60
probability_sum = sum(binomial_probability(n, k, p) for k in range(40, 61))

print(probability_sum)


