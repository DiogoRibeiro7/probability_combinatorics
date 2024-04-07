def pascal_triangle_sum(n):
    """
    Calculate the sum of the first n rows of Pascal's triangle.

    Parameters:
    n (int): Number of rows to consider.

    Returns:
    int: Sum of the first n rows of Pascal's triangle.
    """
    def binomial_coefficient(n, k):
        """
        Calculate the binomial coefficient C(n, k).

        Parameters:
        n (int): Total number of items.
        k (int): Number of items to choose.

        Returns:
        int: Binomial coefficient C(n, k).
        """
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

    # Calculate the sum of the elements in the first n rows
    total_sum = 0
    for row in range(n):
        for col in range(row + 1):
            total_sum += binomial_coefficient(row, col)

    return total_sum

# Example usage:
n = 6
print("Sum of the first", n, "rows of Pascal's triangle:", pascal_triangle_sum(n))
