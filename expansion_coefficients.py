def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient "n choose k".

    Parameters:
    n (int): Total number of items.
    k (int): Number of items to choose.

    Returns:
    int: Binomial coefficient "n choose k".
    """
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

def expansion_coefficients(n):
    """
    Compute the coefficients of the expansion of (3a - 2b)^3.

    Parameters:
    n (int): Exponent of the binomial.

    Returns:
    list: Coefficients of the expansion.
    """
    coefficients = []
    for k in range(n + 1):
        coeff = binomial_coefficient(n, k) * (3 ** (n - k)) * ((-2) ** k)
        coefficients.append(coeff)
    return coefficients

# Coefficients of the expansion
coefficients = expansion_coefficients(7)
print("Coefficients of the expansion:", coefficients)