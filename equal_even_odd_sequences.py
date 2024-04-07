from math import comb

# Calculate the number of ways to choose 3 positions out of 6 for even digits
positions = comb(6, 3)

# Calculate the possibilities for choosing even and odd digits
even_digits = 5**3
odd_digits = 5**3

# Calculate the total number of sequences
total_sequences = positions * even_digits * odd_digits

print(total_sequences)

